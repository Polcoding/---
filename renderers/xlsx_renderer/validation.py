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
    "civil_or_receipt_number": re.compile(r"(민원번호|접수번호|사건번호)\s*[:：]?\s*[\w가-힣-]{4,}"),
    "money": re.compile(r"\b\d{1,3}(,\d{3})+원\b|\b\d+원\b"),
}

SENSITIVE_PATTERN_LABELS = {
    "email": "실제 이메일 주소처럼 보이는 값",
    "phone": "실제 연락처처럼 보이는 값",
    "vehicle": "실제 차량번호처럼 보이는 값",
    "resident_id": "고유식별번호처럼 보이는 값",
    "civil_or_receipt_number": "실제 민원번호, 접수번호 또는 사건번호처럼 보이는 값",
    "money": "실제 금액처럼 보이는 값",
}

SENSITIVE_KEYWORDS = {
    "내부망": "내부망 관련 키워드",
    "시스템명": "내부 시스템명 관련 키워드",
    "계정": "계정정보 관련 키워드",
    "비밀번호": "비밀번호 관련 키워드",
    "API 키": "API 키 관련 키워드",
}

SAFE_CONTEXT_MARKERS = {
    "[확인 필요]",
    "placeholder",
    "제외",
    "금지",
    "확인",
    "포함하지",
    "사용하지",
    "입력하지",
}


def format_error(message: str, action: str) -> str:
    return f"{message} 조치: {action}"


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
                findings.append(SENSITIVE_PATTERN_LABELS[label])
        has_safe_context = any(marker in text for marker in SAFE_CONTEXT_MARKERS)
        if not has_safe_context:
            for keyword, label in SENSITIVE_KEYWORDS.items():
                if keyword in text:
                    findings.append(label)
    return list(dict.fromkeys(findings))


def validate_payload(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    missing_top = sorted(REQUIRED_TOP_LEVEL_FIELDS - set(data))
    if missing_top:
        errors.append(
            format_error(
                f"필수 최상위 필드가 누락되었습니다: {', '.join(missing_top)}.",
                "샘플 JSON 스키마에 맞게 누락 필드를 placeholder 또는 null로 보강하세요.",
            )
        )

    if data.get("document_type") != ALLOWED_DOCUMENT_TYPE:
        errors.append(
            format_error(
                "document_type이 survey_table이 아닙니다.",
                "XLSX 렌더러는 조사표 샘플만 처리합니다.",
            )
        )

    output_targets = data.get("output_targets", [])
    if "xlsx" not in output_targets:
        errors.append(
            format_error(
                "output_targets에 xlsx가 없습니다.",
                "XLSX 렌더링 대상이면 output_targets에 xlsx를 포함하세요.",
            )
        )

    security_review = data.get("security_review")
    if not isinstance(security_review, dict):
        errors.append(
            format_error(
                "security_review가 객체가 아닙니다.",
                "렌더링 전 보안 검토 결과를 객체 형태로 제공하세요.",
            )
        )
        return errors

    missing_security = sorted(REQUIRED_SECURITY_FIELDS - set(security_review))
    if missing_security:
        errors.append(
            format_error(
                f"security_review 필드가 누락되었습니다: {', '.join(missing_security)}.",
                "보안 검증 필드를 placeholder 기반으로 보강하세요.",
            )
        )

    risk_level = security_review.get("risk_level")
    if risk_level in BLOCKING_RISK_LEVELS:
        errors.append(
            format_error(
                f"렌더링 차단 등급입니다: risk_level={risk_level}.",
                "사람 검토 후 비식별 샘플로 다시 입력하세요.",
            )
        )

    if security_review.get("contains_personal_info") is True:
        errors.append(
            format_error(
                "개인정보 포함 플래그가 true입니다.",
                "개인정보를 제거하고 placeholder로 치환한 뒤 다시 검증하세요.",
            )
        )

    if security_review.get("contains_sensitive_info") is True:
        errors.append(
            format_error(
                "민감정보 포함 플래그가 true입니다.",
                "민감정보를 제거하고 내부 검토 대상으로 분리하세요.",
            )
        )

    if security_review.get("contains_internal_info") is True:
        errors.append(
            format_error(
                "내부 운영정보 포함 플래그가 true입니다.",
                "외부 렌더링 대상에서 제외하고 수동 검토하세요.",
            )
        )

    pattern_findings = find_sensitive_patterns(data)
    if pattern_findings:
        errors.append(
            format_error(
                "실제값 의심 패턴이 발견되었습니다: " + ", ".join(pattern_findings) + ".",
                "해당 값을 출력하지 말고 placeholder로 치환하세요.",
            )
        )

    documents = data.get("documents", [])
    if not isinstance(documents, list) or not documents:
        errors.append(
            format_error(
                "documents 배열이 비어 있습니다.",
                "조사표 문서 객체를 documents[0]에 placeholder 기반으로 추가하세요.",
            )
        )
    elif not isinstance(documents[0], dict):
        errors.append(
            format_error(
                "documents[0]이 객체가 아닙니다.",
                "조사표 문서 구조를 객체 형태로 제공하세요.",
            )
        )

    return errors
