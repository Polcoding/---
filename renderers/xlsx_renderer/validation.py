"""Validation helpers for the XLSX renderer PoC."""

from __future__ import annotations

import re
from typing import Any


BLOCKING_RISK_LEVELS = {"high", "blocked"}
ALLOWED_DOCUMENT_TYPE = "survey_table"
REQUIRED_TOP_LEVEL_FIELDS = {
    "request_id",
    "input_summary",
    "task_type",
    "document_type",
    "output_targets",
    "security_review",
    "missing_fields",
    "assumptions",
    "draft_status",
    "human_review_required",
    "documents",
    "renderer_hints",
}
REQUIRED_SECURITY_FIELDS = {
    "risk_level",
    "contains_personal_info",
    "contains_sensitive_info",
    "contains_internal_info",
    "blocked_items",
    "allowed_processing",
    "required_review",
    "notes",
}

SENSITIVE_PATTERNS = {
    "email": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    "phone": re.compile(r"\b0\d{1,2}[-\s]?\d{3,4}[-\s]?\d{4}\b"),
    "vehicle": re.compile(r"\b\d{2,3}[가-힣]\d{4}\b"),
    "resident_id": re.compile(r"\b\d{6}-\d{7}\b"),
    "money": re.compile(r"\b\d{1,3}(,\d{3})+원\b|\b\d+원\b"),
}


def collect_strings(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        result: list[str] = []
        for item in value:
            result.extend(collect_strings(item))
        return result
    if isinstance(value, dict):
        result = []
        for item in value.values():
            result.extend(collect_strings(item))
        return result
    return []


def find_sensitive_patterns(data: dict[str, Any]) -> list[str]:
    findings: list[str] = []
    for text in collect_strings(data):
        for label, pattern in SENSITIVE_PATTERNS.items():
            if pattern.search(text):
                findings.append(f"{label}: {text}")
    return findings


def validate_payload(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    missing_top = sorted(REQUIRED_TOP_LEVEL_FIELDS - set(data))
    if missing_top:
        errors.append(f"필수 최상위 필드 누락: {', '.join(missing_top)}")

    if data.get("document_type") != ALLOWED_DOCUMENT_TYPE:
        errors.append("document_type이 survey_table이 아닙니다.")

    output_targets = data.get("output_targets", [])
    if "xlsx" not in output_targets:
        errors.append("output_targets에 xlsx가 없습니다.")

    security_review = data.get("security_review")
    if not isinstance(security_review, dict):
        errors.append("security_review가 객체가 아닙니다.")
        return errors

    missing_security = sorted(REQUIRED_SECURITY_FIELDS - set(security_review))
    if missing_security:
        errors.append(f"security_review 필드 누락: {', '.join(missing_security)}")

    risk_level = security_review.get("risk_level")
    if risk_level in BLOCKING_RISK_LEVELS:
        errors.append(f"차단 risk_level: {risk_level}")

    if security_review.get("contains_personal_info") is True:
        errors.append("contains_personal_info가 true입니다.")

    if security_review.get("contains_sensitive_info") is True:
        errors.append("contains_sensitive_info가 true입니다.")

    if security_review.get("contains_internal_info") is True:
        errors.append("contains_internal_info가 true입니다.")

    pattern_findings = find_sensitive_patterns(data)
    if pattern_findings:
        errors.append("실제값 의심 패턴 발견: " + " | ".join(pattern_findings))

    documents = data.get("documents", [])
    if not isinstance(documents, list) or not documents:
        errors.append("documents 배열이 비어 있습니다.")
    elif not isinstance(documents[0], dict):
        errors.append("documents[0]이 객체가 아닙니다.")

    return errors
