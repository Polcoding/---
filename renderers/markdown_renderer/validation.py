"""Security validation for the Markdown preview renderer PoC."""

from __future__ import annotations

import re
from typing import Any


BLOCKING_RISK_LEVELS = {"high", "blocked"}

FORBIDDEN_PATTERNS = {
    "phone_like": re.compile(r"\b0\d{1,2}[-\s]?\d{3,4}[-\s]?\d{4}\b"),
    "email_like": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    "resident_id_like": re.compile(r"\b\d{6}-\d{7}\b"),
    "vehicle_number_like": re.compile(r"\b\d{2,3}[가-힣]\d{4}\b"),
    "document_number_like": re.compile(r"\b[A-Za-z가-힣]+-\d{2,}-\d{2,}\b"),
    "case_number_like": re.compile(r"\b\d{4}[가-힣A-Za-z-]{1,}\d{1,}\b"),
    "money_like": re.compile(r"\b\d{1,3}(,\d{3})+원\b|\b\d+원\b"),
}

FORBIDDEN_KEYWORDS = {
    "내부 시스템명",
    "내부망",
    "계정",
    "비밀번호",
    "API 키",
    "문서번호",
    "민원번호",
    "접수번호",
    "사건번호",
    "차량번호",
    "장비명",
    "장비현황",
    "수량",
    "운영정보",
}

SAFE_EXPLANATION_MARKERS = {
    "[확인 필요]",
    "placeholder",
    "제외",
    "금지",
    "확인",
    "포함하지",
    "사용하지",
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


def has_forbidden_pattern(text: str) -> list[str]:
    """Return blocking reasons found in one string."""
    reasons: list[str] = []

    for name, pattern in FORBIDDEN_PATTERNS.items():
        if pattern.search(text):
            reasons.append(f"금지 패턴 감지: {name}")

    for keyword in FORBIDDEN_KEYWORDS:
        if keyword in text and not any(marker in text for marker in SAFE_EXPLANATION_MARKERS):
            reasons.append(f"금지 키워드 감지: {keyword}")

    return reasons


def validate_for_markdown_rendering(data: dict) -> tuple[bool, list[str]]:
    """Validate whether a JSON payload may be rendered as Markdown preview."""
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
        reasons.extend(has_forbidden_pattern(text))

    unique_reasons = list(dict.fromkeys(reasons))
    return len(unique_reasons) == 0, unique_reasons
