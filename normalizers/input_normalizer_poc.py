"""Minimal input normalization PoC for HWPX report requests."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from security_filter_poc import apply_security_filter


BASE_DIR = Path(__file__).resolve().parent
FIXTURE_DIR = BASE_DIR / "fixtures"
OUTPUT_DIR = BASE_DIR / "output"

DOCUMENT_KEYWORDS = {
    "review_report": ("검토보고", "검토 의견", "법무", "계약", "개인정보 검토"),
    "result_report": ("결과보고", "추진 결과", "실적", "계획 대비"),
    "project_plan": ("추진계획", "계획서", "추진하려고", "일정", "예산"),
    "one_page_report": ("원페이지", "간단히 보고", "요약 보고", "핵심 내용"),
}

BLOCKED_REQUEST_MARKERS = ("실제 원문", "그대로 발송", "결재", "예산 집행", "자동 처리")

OUTPUT_TARGETS = {
    "one_page_report": ["hwpx", "markdown"],
    "project_plan": ["hwpx", "markdown"],
    "result_report": ["hwpx", "markdown"],
    "review_report": ["hwpx", "markdown"],
    "unknown": [],
}


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def detect_document_type(request_text: str) -> str:
    if any(marker in request_text for marker in BLOCKED_REQUEST_MARKERS):
        return "unknown"
    for document_type, keywords in DOCUMENT_KEYWORDS.items():
        if any(keyword in request_text for keyword in keywords):
            return document_type
    return "unknown"


def make_content_inputs(document_type: str) -> dict[str, Any]:
    common = {
        "title_hint": "[제목 확인 필요]",
        "purpose": "[목적 확인 필요]",
        "background": "[배경 확인 필요]",
        "main_points": ["[주요 내용 확인 필요]"],
        "risks": ["[위험요소 확인 필요]"],
        "next_steps": ["[후속조치 확인 필요]"],
    }

    if document_type == "one_page_report":
        return {
            **common,
            "title_hint": "[비식별 사업 원페이지 보고]",
            "purpose": "[보고 목적 확인 필요]",
        }
    if document_type == "project_plan":
        return {
            **common,
            "title_hint": "[비식별 업무 추진계획]",
            "schedule": "[추진 일정 확인 필요]",
            "budget": "[예산 확인 필요]",
            "department": "[담당부서 확인 필요]",
        }
    if document_type == "result_report":
        return {
            **common,
            "title_hint": "[비식별 사업 결과보고]",
            "results_or_metrics": "[실적 수치 확인 필요]",
            "schedule": "[계획 대비 일정 확인 필요]",
            "budget": "[예산 집행 여부 확인 필요]",
        }
    if document_type == "review_report":
        return {
            **common,
            "title_hint": "[비식별 사안 검토보고]",
            "purpose": "[검토 목적 확인 필요]",
            "main_points": ["[검토 항목 확인 필요]"],
            "risks": ["[위험요소 확인 필요]", "[추가 검토 필요사항 확인 필요]"],
        }
    return {}


def make_missing_fields(document_type: str) -> list[dict[str, str]]:
    missing_by_type = {
        "one_page_report": [
            ("purpose", "보고 목적 미확정", "one_page_report.report_summary"),
        ],
        "project_plan": [
            ("schedule", "추진 일정 미확정", "project_plan.schedule"),
            ("budget", "예산 미확정", "project_plan.budget"),
        ],
        "result_report": [
            ("results_or_metrics", "실적 수치 미확정", "result_report.actual_results"),
            ("budget", "예산 집행 정보 미확정", "result_report.actual_results"),
        ],
        "review_report": [
            ("review_scope", "검토 범위 미확정", "review_report.review_scope"),
            ("required_reviews", "필요 검토 주체 미확정", "review_report.required_reviews"),
        ],
    }
    return [
        {
            "field_name": field_name,
            "reason": reason,
            "required_for": required_for,
            "suggested_placeholder": "[확인 필요]",
        }
        for field_name, reason, required_for in missing_by_type.get(document_type, [])
    ]


def make_user_intent_summary(document_type: str) -> str:
    summaries = {
        "one_page_report": "[비식별 사업의 핵심 내용을 원페이지 보고서로 정리]",
        "project_plan": "[비식별 업무의 추진계획서 초안 작성]",
        "result_report": "[비식별 사업의 추진 결과를 계획 대비로 정리]",
        "review_report": "[비식별 사안의 검토보고서 초안 작성]",
        "unknown": "[문서 유형 확인 필요]",
    }
    return summaries[document_type]


def make_initial_security_flags(request_text: str) -> dict[str, Any]:
    sensitive_markers = ("개인정보", "민감정보", "법무", "계약", "감사", "징계", "수사")
    internal_markers = ("내부", "운영정보", "담당 정보", "실제값")
    suspected_sensitive = any(marker in request_text for marker in sensitive_markers)
    suspected_internal = any(marker in request_text for marker in internal_markers)
    blocked_reason = None
    if any(marker in request_text for marker in BLOCKED_REQUEST_MARKERS):
        blocked_reason = "실제 원문 또는 금지 자동화 요청 의심"

    return {
        "suspected_personal_info": "개인정보" in request_text and "검토" not in request_text,
        "suspected_sensitive_info": suspected_sensitive,
        "suspected_internal_info": suspected_internal,
        "suspected_real_document_number": "문서번호" in request_text,
        "suspected_real_case_number": "사건번호" in request_text or "민원번호" in request_text,
        "suspected_budget_or_contract_value": "예산" in request_text or "계약" in request_text,
        "risk_level_hint": "blocked" if blocked_reason else ("medium" if suspected_sensitive or suspected_internal else "low"),
        "requires_security_review": suspected_sensitive or suspected_internal or blocked_reason is not None,
        "block_reason": blocked_reason,
    }


def has_placeholder_security_gate(fixture: dict[str, Any]) -> bool:
    security_gate = fixture.get("security_gate")
    if not isinstance(security_gate, dict):
        return False
    return (
        security_gate.get("human_security_review_completed") is True
        and security_gate.get("approved_for_placeholder_rendering") is True
        and security_gate.get("review_basis") == "[비식별 보안 검토 완료]"
    )


def normalize_request(fixture: dict[str, Any]) -> dict[str, Any]:
    request_text = fixture.get("request_text", "")
    document_type = detect_document_type(request_text)
    normalized = {
        "normalized_request_id": fixture.get("fixture_id", "[정규화 요청 ID placeholder]"),
        "source_channel": "manual_input",
        "raw_input_retention": "not_stored",
        "user_intent_summary": make_user_intent_summary(document_type),
        "requested_task": "draft_document" if document_type != "unknown" else "unknown",
        "candidate_document_type": document_type,
        "output_targets": OUTPUT_TARGETS[document_type],
        "content_inputs": make_content_inputs(document_type),
        "known_values": {},
        "missing_fields": make_missing_fields(document_type),
        "security_flags": make_initial_security_flags(request_text),
        "routing_decision": {
            "status": "needs_more_input" if document_type != "unknown" else "blocked",
            "reason": "[정규화 후 보안 필터 확인 필요]",
            "next_action": "apply_security_filter",
        },
        "human_review_required": True,
    }
    if has_placeholder_security_gate(fixture):
        normalized["security_gate"] = fixture["security_gate"]
    return apply_security_filter(normalized)


def normalize_fixture_file(path: Path) -> dict[str, Any]:
    return normalize_request(load_json(path))


def main() -> None:
    fixture_paths = sorted(FIXTURE_DIR.glob("*.json"))
    results = []
    for path in fixture_paths:
        fixture = load_json(path)
        normalized = normalize_request(fixture)
        expected_document_type = fixture.get("expected_document_type")
        expected_routing_status = fixture.get("expected_routing_status")
        passed = (
            normalized["candidate_document_type"] == expected_document_type
            and normalized["routing_decision"]["status"] == expected_routing_status
        )
        results.append(
            {
                "fixture": path.name,
                "candidate_document_type": normalized["candidate_document_type"],
                "routing_status": normalized["routing_decision"]["status"],
                "expected_document_type": expected_document_type,
                "expected_routing_status": expected_routing_status,
                "passed": passed,
                "normalized": normalized,
            }
        )

    print("입력 정규화 PoC 실행 결과")
    for result in results:
        print(
            f"- {result['fixture']}: "
            f"{result['candidate_document_type']} / {result['routing_status']} / "
            f"{'passed' if result['passed'] else 'failed'}"
        )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / "normalization_summary.json"
    try:
        output_path.write_text(
            json.dumps({"results": results}, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"summary_output: {output_path}")
    except PermissionError:
        print(f"summary_output_skipped_permission_error: {output_path}")


if __name__ == "__main__":
    main()
