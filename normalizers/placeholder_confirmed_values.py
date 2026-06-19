"""Read-only helpers for placeholder_confirmed_values checks."""

from __future__ import annotations

import re
from collections.abc import Mapping
from typing import Any


MAX_PLACEHOLDER_LENGTH = 80

ALLOWED_MEANING_KEYWORDS = (
    "확인 필요",
    "검토 필요",
    "미확정",
    "비식별",
    "비공개",
    "placeholder",
    "플레이스홀더",
)

DISALLOWED_ACTUAL_VALUE_MARKERS = (
    "실제",
    "원문",
    "입력됨",
    "확정값",
    "확정 금액",
    "확정 일정",
    "담당자 연락처",
    "계약 조건",
    "업체 평가",
)

SUSPECTED_REAL_VALUE_PATTERNS = {
    "phone_like": re.compile(r"\b0\d{1,2}[-\s]?\d{3,4}[-\s]?\d{4}\b"),
    "email_like": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    "resident_id_like": re.compile(r"\b\d{6}-\d{7}\b"),
    "vehicle_number_like": re.compile(r"\b\d{2,3}[가-힣]\d{4}\b"),
    "date_like": re.compile(r"\b\d{4}[./-]\d{1,2}[./-]\d{1,2}\b|\b\d{4}\s*년\s*\d{1,2}\s*월"),
    "money_like": re.compile(r"\b\d[\d,]*\s*(원|천원|만원|백만원|억원)\b|₩\s*\d"),
    "document_number_like": re.compile(r"(문서|민원|사건|접수)\s*(번호|제)?\s*[:：-]?\s*\d+"),
}


def _invalid_reasons(value: Any) -> list[str]:
    if not isinstance(value, str):
        return ["not_string"]

    stripped = value.strip()
    if not (stripped.startswith("[") and stripped.endswith("]")):
        return ["not_bracket_placeholder"]

    inner = stripped[1:-1].strip()
    reasons: list[str] = []

    if not inner:
        reasons.append("empty_placeholder")

    if len(stripped) > MAX_PLACEHOLDER_LENGTH:
        reasons.append("placeholder_too_long")

    if not any(keyword in inner for keyword in ALLOWED_MEANING_KEYWORDS):
        reasons.append("meaning_not_allowed")

    if any(marker in inner for marker in DISALLOWED_ACTUAL_VALUE_MARKERS):
        reasons.append("actual_value_marker")

    for name, pattern in SUSPECTED_REAL_VALUE_PATTERNS.items():
        if pattern.search(stripped):
            reasons.append(f"suspected_real_value:{name}")

    return list(dict.fromkeys(reasons))


def is_placeholder_confirmed_value(value: Any) -> bool:
    """Return True only when value is a safe placeholder-confirmed string."""

    return not _invalid_reasons(value)


def find_invalid_placeholder_confirmed_values(values: Any) -> list[dict[str, str]]:
    """Return invalid placeholder_confirmed_values findings without mutating input."""

    if values is None:
        return []

    if not isinstance(values, Mapping):
        return [
            {
                "field_name": "<placeholder_confirmed_values>",
                "reason": "not_mapping",
            }
        ]

    findings: list[dict[str, str]] = []
    for field_name, value in values.items():
        for reason in _invalid_reasons(value):
            findings.append(
                {
                    "field_name": str(field_name),
                    "reason": reason,
                }
            )
    return findings
