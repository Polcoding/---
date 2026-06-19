"""Map normalized requests into HWPX renderer payload-shaped JSON."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from input_normalizer_poc import FIXTURE_DIR, OUTPUT_DIR, load_json, normalize_request


PAYLOAD_ALLOWED_ROUTING = {"ready_for_draft", "needs_more_input"}

TEMPLATE_IDS = {
    "one_page_report": "placeholder_one_page_report",
    "project_plan": "placeholder_project_plan",
    "result_report": "placeholder_result_report",
    "review_report": "placeholder_review_report",
}

DRAFT_STATUS_BY_ROUTING = {
    "ready_for_draft": "draft",
    "needs_more_input": "needs_input",
    "needs_security_review": "blocked",
    "blocked": "blocked",
}


def as_list(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(item) for item in value]
    if value is None:
        return []
    return [str(value)]


def map_security_review(normalized: dict[str, Any]) -> dict[str, Any]:
    flags = normalized.get("security_flags") or {}
    routing_status = (normalized.get("routing_decision") or {}).get("status")
    security_gate = normalized.get("security_gate") or {}
    allowed_processing = routing_status in PAYLOAD_ALLOWED_ROUTING
    approved_placeholder_rendering = (
        isinstance(security_gate, dict)
        and security_gate.get("approved_for_placeholder_rendering") is True
    )

    required_review = ["human_review"]
    if flags.get("requires_security_review"):
        required_review.append("security_review")

    blocked_items = []
    if flags.get("block_reason"):
        blocked_items.append(flags["block_reason"])

    return {
        "risk_level": flags.get("risk_level_hint", "low"),
        "contains_personal_info": bool(flags.get("suspected_personal_info")),
        "contains_sensitive_info": False if approved_placeholder_rendering else bool(flags.get("suspected_sensitive_info")),
        "contains_internal_info": False if approved_placeholder_rendering else bool(flags.get("suspected_internal_info")),
        "blocked_items": blocked_items,
        "allowed_processing": allowed_processing,
        "required_review": required_review,
        "notes": "[비식별 보안 검토 완료 후 placeholder 렌더링]" if approved_placeholder_rendering else "[정규화 결과 기반 보안 검토]",
    }


def map_one_page_report(content: dict[str, Any]) -> dict[str, Any]:
    return {
        "title": content.get("title_hint", "[보고 제목 확인 필요]"),
        "report_summary": content.get("purpose", "[보고 개요 확인 필요]"),
        "background": content.get("background", "[추진 배경 확인 필요]"),
        "main_points": as_list(content.get("main_points")) or ["[주요 내용 확인 필요]"],
        "review_opinion": "[검토 의견 확인 필요]",
        "issues_or_considerations": as_list(content.get("risks")) or ["[고려사항 확인 필요]"],
        "next_steps": as_list(content.get("next_steps")) or ["[향후 조치 확인 필요]"],
        "action_items": as_list(content.get("next_steps")) or ["[조치 필요사항 확인 필요]"],
        "attachments": [],
        "checklist": ["placeholder 유지", "개인정보 제외", "사람 검토"],
    }


def map_project_plan(content: dict[str, Any]) -> dict[str, Any]:
    return {
        "title": content.get("title_hint", "[사업명 확인 필요] 추진계획"),
        "background": content.get("background", "[업무 발생 배경 확인 필요]"),
        "purpose": content.get("purpose", "[활용 목적 확인 필요]"),
        "overview": "[사업명ㆍ추진기간ㆍ추진대상ㆍ추진방식ㆍ소요예산 확인 필요]",
        "main_contents": as_list(content.get("main_points")) or ["[주요 내용 확인 필요]"],
        "detailed_plan": ["[단계별 세부 추진내용 확인 필요]"],
        "schedule": content.get("schedule", "[추진 일정 확인 필요]"),
        "budget": content.get("budget", "[예산 확인 필요]"),
        "expected_effects": ["[기대효과 확인 필요]"],
        "review_items": as_list(content.get("risks")) or ["[검토사항 확인 필요]"],
        "future_plan": as_list(content.get("next_steps")) or ["[향후계획 확인 필요]"],
        "attachments": [],
        "checklist": ["예산 임의 생성 금지", "일정 확인", "사람 검토"],
    }


def map_result_report(content: dict[str, Any]) -> dict[str, Any]:
    return {
        "title": content.get("title_hint", "[사업명 확인 필요] 결과보고"),
        "linked_plan_reference": content.get("background", "[기존 추진계획서 참조 확인 필요]"),
        "overview": content.get("purpose", "[추진 개요 확인 필요]"),
        "planned_items": as_list(content.get("main_points")) or ["[계획 항목 확인 필요]"],
        "actual_results": content.get("results_or_metrics", "[추진결과 확인 필요]"),
        "comparison_to_plan": content.get("schedule", "[계획 대비 결과 확인 필요]"),
        "main_outcomes": ["[주요성과 확인 필요]"],
        "issues": as_list(content.get("risks")) or ["[문제점 확인 필요]"],
        "improvements": ["[개선사항 확인 필요]"],
        "future_plan": as_list(content.get("next_steps")) or ["[향후계획 확인 필요]"],
        "attachments": [],
        "checklist": ["실제 수치 임의 생성 금지", "개인정보 제외", "사람 검토"],
    }


def map_review_report(content: dict[str, Any]) -> dict[str, Any]:
    return {
        "title": content.get("title_hint", "[검토 대상 확인 필요] 검토보고"),
        "review_background": content.get("background", "[검토배경 확인 필요]"),
        "review_scope": content.get("purpose", "[검토범위 확인 필요]"),
        "review_items": as_list(content.get("main_points")) or ["[검토항목 확인 필요]"],
        "review_opinion": "[검토 의견 확인 필요]",
        "risks": as_list(content.get("risks")) or ["[위험요소 확인 필요]"],
        "required_reviews": ["[법무ㆍ계약ㆍ개인정보 검토 필요 여부 확인]"],
        "next_actions": as_list(content.get("next_steps")) or ["[후속조치 확인 필요]"],
        "attachments": [],
        "checklist": ["확정 표현 금지", "관련 부서 검토 필요", "사람 검토"],
    }


DOCUMENT_MAPPERS = {
    "one_page_report": map_one_page_report,
    "project_plan": map_project_plan,
    "result_report": map_result_report,
    "review_report": map_review_report,
}


def map_to_hwpx_payload(normalized: dict[str, Any]) -> dict[str, Any] | None:
    routing = normalized.get("routing_decision") or {}
    routing_status = routing.get("status")
    document_type = normalized.get("candidate_document_type")

    if routing_status not in PAYLOAD_ALLOWED_ROUTING:
        return None

    mapper = DOCUMENT_MAPPERS.get(document_type)
    if mapper is None:
        return None

    content = normalized.get("content_inputs") or {}
    return {
        "request_id": normalized.get("normalized_request_id"),
        "input_summary": normalized.get("user_intent_summary"),
        "task_type": normalized.get("requested_task", "draft_document"),
        "document_type": document_type,
        "output_targets": normalized.get("output_targets", ["hwpx"]),
        "security_review": map_security_review(normalized),
        "security_gate": normalized.get("security_gate"),
        "missing_fields": normalized.get("missing_fields", []),
        "assumptions": [],
        "draft_status": DRAFT_STATUS_BY_ROUTING.get(routing_status, "needs_input"),
        "human_review_required": True,
        "documents": [mapper(content)],
        "attachments": [],
        "email_draft": None,
        "checklist": ["정규화 결과 검토", "보안 검토", "HWPX 렌더링 전 사람 검토"],
        "renderer_hints": {
            "target_format": "hwpx",
            "template_id": TEMPLATE_IDS[document_type],
            "requires_hwpx": True,
            "requires_manual_review": True,
        },
    }


def main() -> None:
    results = []
    for path in sorted(FIXTURE_DIR.glob("*.json")):
        fixture = load_json(path)
        normalized = normalize_request(fixture)
        payload = map_to_hwpx_payload(normalized)
        routing_status = normalized["routing_decision"]["status"]
        expected_created = routing_status in PAYLOAD_ALLOWED_ROUTING
        actual_created = payload is not None
        results.append(
            {
                "fixture": path.name,
                "routing_status": routing_status,
                "payload_created": actual_created,
                "expected_payload_created": expected_created,
                "passed": actual_created == expected_created,
                "payload": payload,
            }
        )

    print("HWPX payload mapper PoC 실행 결과")
    for result in results:
        state = "created" if result["payload_created"] else "skipped"
        print(f"- {result['fixture']}: {result['routing_status']} / {state} / {'passed' if result['passed'] else 'failed'}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / "hwpx_payload_mapping_summary.json"
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
