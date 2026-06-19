"""Dry-run mapper payloads against HWPX renderer prerequisites.

This script does not create HWPX files and does not call replace_placeholders_in_hwpx.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from hwpx_payload_mapper_poc import map_to_hwpx_payload
from input_normalizer_poc import FIXTURE_DIR, OUTPUT_DIR, load_json, normalize_request


REPO_ROOT = Path(__file__).resolve().parents[1]
HWPX_RENDERER_DIR = REPO_ROOT / "renderers" / "hwpx_renderer"
TEMPLATE_DIR = REPO_ROOT / "templates" / "hwpx"
sys.path.insert(0, str(HWPX_RENDERER_DIR))

from template_package import build_placeholder_map, is_hwpx_template_available  # noqa: E402
from validation import validate_for_hwpx_rendering  # noqa: E402


TEMPLATE_NAMES = {
    "one_page_report": "placeholder_one_page_report.hwpx",
    "project_plan": "placeholder_project_plan.hwpx",
    "result_report": "placeholder_result_report.hwpx",
    "review_report": "placeholder_review_report.hwpx",
}


def dry_run_fixture(path: Path) -> dict[str, Any]:
    fixture = load_json(path)
    normalized = normalize_request(fixture)
    routing_status = normalized["routing_decision"]["status"]
    payload = map_to_hwpx_payload(normalized)

    result: dict[str, Any] = {
        "fixture": path.name,
        "routing_status": routing_status,
        "payload_created": payload is not None,
        "status": "pending",
        "reasons": [],
    }

    if payload is None:
        if routing_status == "blocked":
            result["status"] = "skipped_blocked"
        elif routing_status == "needs_security_review":
            result["status"] = "skipped_security_review"
        else:
            result["status"] = "skipped_no_payload"
        return result

    is_safe, reasons = validate_for_hwpx_rendering(payload)
    result["validation_passed"] = is_safe
    result["reasons"] = reasons
    if not is_safe:
        result["status"] = "validation_failed"
        return result

    placeholder_map = build_placeholder_map(payload)
    document_type = payload.get("document_type")
    template_name = TEMPLATE_NAMES.get(document_type, "[unknown]")
    template_path = TEMPLATE_DIR / template_name
    template_available = is_hwpx_template_available(template_path)

    result.update(
        {
            "document_type": document_type,
            "placeholder_count": len(placeholder_map),
            "template": str(template_path.relative_to(REPO_ROOT)),
            "template_available": template_available,
        }
    )

    if not template_available:
        result["status"] = "template_required"
    elif routing_status == "needs_more_input":
        result["status"] = "dry_run_ready_with_missing_fields"
    else:
        result["status"] = "dry_run_ready"

    return result


def main() -> None:
    results = [dry_run_fixture(path) for path in sorted(FIXTURE_DIR.glob("*.json"))]

    print("HWPX renderer dry-run PoC 실행 결과")
    for result in results:
        print(f"- {result['fixture']}: {result['routing_status']} / {result['status']}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / "hwpx_renderer_dry_run_summary.json"
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
