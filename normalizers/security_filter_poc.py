"""Security routing helpers for the input normalization PoC."""

from __future__ import annotations

import re
from typing import Any


BLOCKED_PATTERNS = {
    "phone_like": re.compile(r"\b0\d{1,2}[-\s]?\d{3,4}[-\s]?\d{4}\b"),
    "email_like": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    "resident_id_like": re.compile(r"\b\d{6}-\d{7}\b"),
    "vehicle_number_like": re.compile(r"\b\d{2,3}[가-힣]\d{4}\b"),
}

BLOCKED_FLAG_KEYS = {
    "suspected_personal_info",
    "suspected_real_document_number",
    "suspected_real_case_number",
}


def flatten_values(data: Any) -> list[str]:
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


def detect_blocking_patterns(data: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    for text in flatten_values(data):
        for name, pattern in BLOCKED_PATTERNS.items():
            if pattern.search(text):
                reasons.append(f"blocked_pattern:{name}")
    return list(dict.fromkeys(reasons))


def decide_routing(normalized: dict[str, Any], blocked_reasons: list[str]) -> dict[str, str]:
    flags = normalized.get("security_flags") or {}
    document_type = normalized.get("candidate_document_type")
    missing_fields = normalized.get("missing_fields") or []

    if flags.get("block_reason"):
        blocked_reasons.append(flags["block_reason"])

    if any(flags.get(key) is True for key in BLOCKED_FLAG_KEYS):
        blocked_reasons.append("실제 식별정보 포함 의심")

    if blocked_reasons:
        return {
            "status": "blocked",
            "reason": "; ".join(list(dict.fromkeys(blocked_reasons))),
            "next_action": "ask_user_to_remove_real_values",
        }

    if flags.get("requires_security_review") or document_type == "review_report":
        return {
            "status": "needs_security_review",
            "reason": "보안 또는 내부 검토 가능성 확인 필요",
            "next_action": "human_security_review",
        }

    if document_type == "one_page_report":
        return {
            "status": "ready_for_draft",
            "reason": "placeholder 기반 비식별 입력",
            "next_action": "draft_with_missing_fields",
        }

    if missing_fields:
        return {
            "status": "needs_more_input",
            "reason": "필수값 확인 필요",
            "next_action": "ask_user_for_missing_fields",
        }

    return {
        "status": "ready_for_draft",
        "reason": "placeholder 기반 비식별 입력",
        "next_action": "draft_with_missing_fields",
    }


def apply_security_filter(normalized: dict[str, Any]) -> dict[str, Any]:
    blocked_reasons = detect_blocking_patterns(normalized)
    routing = decide_routing(normalized, blocked_reasons)

    flags = dict(normalized.get("security_flags") or {})
    if routing["status"] == "blocked":
        flags["risk_level_hint"] = "blocked"
        flags["requires_security_review"] = True
        flags["block_reason"] = routing["reason"]
    elif routing["status"] == "needs_security_review":
        flags["risk_level_hint"] = "medium"
        flags["requires_security_review"] = True

    normalized["security_flags"] = flags
    normalized["routing_decision"] = routing
    normalized["human_review_required"] = True
    return normalized
