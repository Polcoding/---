"""Security validation for the Email draft renderer PoC."""

from __future__ import annotations

import re
from typing import Any


BLOCKING_RISK_LEVELS = {"high", "blocked"}

FORBIDDEN_EMAIL_PATTERNS = {
    "email_address_like": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    "phone_number_like": re.compile(r"\b0\d{1,2}[-\s]?\d{3,4}[-\s]?\d{4}\b"),
    "resident_id_like": re.compile(r"\b\d{6}-\d{7}\b"),
    "document_number_like": re.compile(r"\b[A-Za-z가-힣]+-\d{2,}-\d{2,}\b"),
    "case_number_like": re.compile(r"\b\d{4}[가-힣A-Za-z-]{1,}\d{1,}\b"),
    "vehicle_number_like": re.compile(r"\b\d{2,3}[가-힣]\d{4}\b"),
    "money_amount_like": re.compile(r"\b\d{1,3}(,\d{3})+원\b|\b\d+원\b"),
}

FORBIDDEN_EMAIL_KEYWORDS = {
    "개인정보",
    "민감정보",
    "문서번호",
    "민원번호",
    "접수번호",
    "사건번호",
    "업체명",
    "계약 조건",
    "견적 금액",
    "내부망",
    "시스템명",
    "계정",
    "비밀번호",
    "API 키",
}

CONFIRMED_BUSINESS_PATTERNS = {
    "contract_confirmed": re.compile(r"(계약|선정|발주|낙찰|예산\s*집행).{0,12}(확정|완료|결정|진행)"),
    "confirmed_contract": re.compile(r"(확정|완료|결정).{0,12}(계약|선정|발주|낙찰|예산\s*집행)"),
}

SAFE_CONTEXT_MARKERS = {
    "[확인 필요]",
    "placeholder",
    "제외",
    "금지",
    "확인",
    "포함하지",
    "사용하지",
    "미확정",
    "아닙니다",
    "아님",
    "검토",
    "사전",
    "placeholder",
    "공용 연락처",
    "공용 이메일",
}

UNCONFIRMED_CONTRACT_MARKERS = {
    "계약 또는 업체 선정이 확정된 사항은 아닙니다",
    "계약",
    "선정",
    "확정",
    "아닙니다",
    "미확정",
}

PRIVACY_EXCLUSION_MARKERS = {
    "개인정보",
    "민감정보",
    "내부자료",
    "제외",
}

PUBLIC_CONTACT_MARKERS = {
    "[공용 연락처]",
    "[담당부서 공용 연락처]",
    "[공용 이메일]",
    "공용 연락처",
    "공용 이메일",
}


def flatten_values(data: Any) -> list[str]:
    """Return every string value from a nested JSON-like object."""
    if isinstance(data, str):
        return [data]

    if isinstance(data, dict):
        values: list[str] = []
        for item in data.values():
            values.extend(flatten_values(item))
        return values

    if isinstance(data, list):
        values = []
        for item in data:
            values.extend(flatten_values(item))
        return values

    return []


def has_forbidden_email_pattern(text: str) -> list[str]:
    """Return blocking reasons found in one string for email rendering."""
    reasons: list[str] = []

    for name, pattern in FORBIDDEN_EMAIL_PATTERNS.items():
        if pattern.search(text):
            reasons.append(f"금지 패턴 감지: {name}")

    has_safe_context = any(marker in text for marker in SAFE_CONTEXT_MARKERS)

    for keyword in FORBIDDEN_EMAIL_KEYWORDS:
        if keyword in text and not has_safe_context:
            reasons.append(f"금지 키워드 감지: {keyword}")

    for name, pattern in CONFIRMED_BUSINESS_PATTERNS.items():
        if pattern.search(text) and not has_safe_context:
            reasons.append(f"계약ㆍ선정ㆍ예산 집행 확정 표현 감지: {name}")

    return reasons


def validate_required_email_cautions(data: dict) -> list[str]:
    """Validate mandatory caution phrases for vendor email drafts."""
    reasons: list[str] = []
    email_draft = data.get("email_draft")

    if not isinstance(email_draft, dict):
        return ["email_draft가 없거나 객체가 아닙니다."]

    caution_notes = email_draft.get("caution_notes")
    caution_text = " ".join(caution_notes) if isinstance(caution_notes, list) else ""
    signature = email_draft.get("signature")
    signature_text = " ".join(flatten_values(signature)) if isinstance(signature, dict) else ""

    has_unconfirmed_contract_notice = (
        any(marker in caution_text for marker in UNCONFIRMED_CONTRACT_MARKERS)
        and ("아닙니다" in caution_text or "미확정" in caution_text)
    )
    if not has_unconfirmed_contract_notice:
        reasons.append("계약 또는 업체 선정 미확정 문구가 없습니다.")

    has_privacy_exclusion_notice = all(
        marker in caution_text for marker in PRIVACY_EXCLUSION_MARKERS
    )
    if not has_privacy_exclusion_notice:
        reasons.append("개인정보ㆍ민감정보 제외 요청 문구가 부족합니다.")

    if not any(marker in signature_text for marker in PUBLIC_CONTACT_MARKERS):
        reasons.append("공용 연락처 placeholder가 없습니다.")

    return reasons


def validate_for_email_rendering(data: dict) -> tuple[bool, list[str]]:
    """Validate whether a JSON payload may be rendered as an email draft."""
    reasons: list[str] = []

    security_review = data.get("security_review")
    if not isinstance(security_review, dict):
        reasons.append("security_review가 없거나 객체가 아닙니다.")
        return False, reasons

    risk_level = security_review.get("risk_level")
    if risk_level in BLOCKING_RISK_LEVELS:
        reasons.append(f"차단 risk_level: {risk_level}")

    if security_review.get("contains_personal_info") is True:
        reasons.append("contains_personal_info가 true입니다.")

    if security_review.get("contains_sensitive_info") is True:
        reasons.append("contains_sensitive_info가 true입니다.")

    if security_review.get("contains_internal_info") is True:
        reasons.append("contains_internal_info가 true입니다. 수동 검토가 필요합니다.")

    for text in flatten_values(data):
        reasons.extend(has_forbidden_email_pattern(text))

    if data.get("document_type") == "vendor_email":
        reasons.extend(validate_required_email_cautions(data))

    unique_reasons = list(dict.fromkeys(reasons))
    return len(unique_reasons) == 0, unique_reasons
