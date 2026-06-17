"""Security validation helpers for the HWPX minimal PoC renderer."""

from __future__ import annotations

import re
from typing import Any


BLOCKING_RISK_LEVELS = {"high", "blocked"}

REQUIRED_TOP_LEVEL_FIELDS = {
    "document_type",
    "output_targets",
    "security_review",
    "renderer_hints",
}

REQUIRED_SECURITY_FIELDS = {
    "risk_level",
    "contains_personal_info",
    "contains_sensitive_info",
    "contains_internal_info",
}

FORBIDDEN_PATTERNS = {
    "phone_like": re.compile(r"\b0\d{1,2}[-\s]?\d{3,4}[-\s]?\d{4}\b"),
    "email_like": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    "resident_id_like": re.compile(r"\b\d{6}-\d{7}\b"),
    "vehicle_number_like": re.compile(r"\b\d{2,3}[가-힣]\d{4}\b"),
    "document_number_like": re.compile(r"\b[A-Za-z가-힣]+-\d{2,}-\d{2,}\b"),
    "civil_receipt_case_number_like": re.compile(
        r"(민원번호|접수번호|사건번호)\s*[:：]?\s*[\w가-힣-]{4,}"
    ),
    "money_like": re.compile(r"\b\d{1,3}(,\d{3})+원\b|\b\d+원\b"),
    "quantity_like": re.compile(r"\b\d+\s*(대|개|명|건|식|부|점)\b"),
}

FORBIDDEN_PATTERN_LABELS = {
    "phone_like": "실제 연락처처럼 보이는 값",
    "email_like": "실제 이메일처럼 보이는 값",
    "resident_id_like": "고유식별정보처럼 보이는 값",
    "vehicle_number_like": "실제 차량번호처럼 보이는 값",
    "document_number_like": "실제 문서번호처럼 보이는 값",
    "civil_receipt_case_number_like": "실제 민원번호, 접수번호 또는 사건번호처럼 보이는 값",
    "money_like": "실제 금액처럼 보이는 값",
    "quantity_like": "실제 수량처럼 보이는 값",
}

FORBIDDEN_KEYWORDS = {
    "문서번호": "문서번호 관련 키워드",
    "민원번호": "민원번호 관련 키워드",
    "접수번호": "접수번호 관련 키워드",
    "사건번호": "사건번호 관련 키워드",
    "차량번호": "차량번호 관련 키워드",
    "장비명": "장비명 관련 키워드",
    "장비현황": "장비현황 관련 키워드",
    "수량": "수량 관련 키워드",
    "운영정보": "내부 운영정보 관련 키워드",
    "내부망": "내부망 관련 키워드",
    "시스템명": "내부 시스템명 관련 키워드",
    "계정": "계정정보 관련 키워드",
    "비밀번호": "비밀번호 관련 키워드",
    "API 키": "API 키 관련 키워드",
}

CONFIRMED_ACTION_KEYWORDS = {
    "계약": "계약 확정으로 오해될 수 있는 표현",
    "선정": "업체 선정 확정으로 오해될 수 있는 표현",
    "발주": "발주 확정으로 오해될 수 있는 표현",
    "낙찰": "낙찰 확정으로 오해될 수 있는 표현",
    "예산 집행": "예산 집행 확정으로 오해될 수 있는 표현",
}

SAFE_CONTEXT_MARKERS = {
    "[확인 필요]",
    "placeholder",
    "제외",
    "금지",
    "확인",
    "포함하지",
    "사용하지",
    "임의 생성하지",
    "미확정",
    "검토",
    "차단",
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


def has_safe_context(text: str) -> bool:
    """Return whether a string is describing a rule instead of carrying data."""
    return any(marker in text for marker in SAFE_CONTEXT_MARKERS)


def has_forbidden_pattern(text: str) -> list[str]:
    """Return blocking reasons found in one string."""
    reasons: list[str] = []
    safe_context = has_safe_context(text)

    for name, pattern in FORBIDDEN_PATTERNS.items():
        if pattern.search(text):
            reasons.append(f"금지 패턴 감지: {FORBIDDEN_PATTERN_LABELS[name]}")

    if not safe_context:
        for keyword, label in FORBIDDEN_KEYWORDS.items():
            if keyword in text:
                reasons.append(f"금지 키워드 감지: {label}")

        for keyword, label in CONFIRMED_ACTION_KEYWORDS.items():
            if keyword in text:
                reasons.append(f"확정 표현 의심: {label}")

    return reasons


def validate_required_fields(data: dict) -> list[str]:
    """Validate minimum fields required before HWPX rendering."""
    reasons: list[str] = []

    missing_top = sorted(REQUIRED_TOP_LEVEL_FIELDS - set(data))
    if missing_top:
        reasons.append(f"필수 최상위 필드 누락: {', '.join(missing_top)}")

    security_review = data.get("security_review")
    if not isinstance(security_review, dict):
        reasons.append("security_review가 없거나 객체가 아닙니다.")
        return reasons

    missing_security = sorted(REQUIRED_SECURITY_FIELDS - set(security_review))
    if missing_security:
        reasons.append(f"security_review 필수 필드 누락: {', '.join(missing_security)}")

    output_targets = data.get("output_targets")
    if output_targets is not None:
        if not isinstance(output_targets, list):
            reasons.append("output_targets가 배열이 아닙니다.")
        elif "hwpx" not in output_targets:
            reasons.append("output_targets에 hwpx가 없습니다.")

    renderer_hints = data.get("renderer_hints")
    if renderer_hints is not None and not isinstance(renderer_hints, dict):
        reasons.append("renderer_hints가 객체가 아닙니다.")

    return reasons


def validate_for_hwpx_rendering(data: dict) -> tuple[bool, list[str]]:
    """Validate whether a JSON payload may be rendered into HWPX."""
    reasons = validate_required_fields(data)

    security_review = data.get("security_review")
    if isinstance(security_review, dict):
        risk_level = security_review.get("risk_level")
        if risk_level in BLOCKING_RISK_LEVELS:
            reasons.append(f"차단 risk_level: {risk_level}")

        if security_review.get("contains_personal_info") is True:
            reasons.append("contains_personal_info가 true입니다.")

        if security_review.get("contains_sensitive_info") is True:
            reasons.append("contains_sensitive_info가 true입니다.")

        if security_review.get("contains_internal_info") is True:
            reasons.append("contains_internal_info가 true입니다. 수동 검토 또는 차단이 필요합니다.")

    for text in flatten_values(data):
        reasons.extend(has_forbidden_pattern(text))

    unique_reasons = list(dict.fromkeys(reasons))
    return len(unique_reasons) == 0, unique_reasons
