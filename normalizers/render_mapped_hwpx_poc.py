"""Render one mapped normalizer payload into HWPX.

This script only renders the ready_for_draft one_page_report fixture.
It uses local placeholder templates and writes ignored output artifacts.
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
HWPX_OUTPUT_DIR = HWPX_RENDERER_DIR / "output"
sys.path.insert(0, str(HWPX_RENDERER_DIR))

from template_package import (  # noqa: E402
    build_placeholder_map,
    is_hwpx_template_available,
    replace_placeholders_in_hwpx,
)
from validation import validate_for_hwpx_rendering  # noqa: E402


FIXTURE_NAME = "safe_one_page_report_request.json"
TEMPLATE_NAME = "placeholder_one_page_report.hwpx"
OUTPUT_NAME = "mapped_safe_one_page_report_poc.hwpx"


def render_mapped_fixture() -> dict[str, Any]:
    fixture_path = FIXTURE_DIR / FIXTURE_NAME
    fixture = load_json(fixture_path)
    normalized = normalize_request(fixture)
    routing_status = normalized["routing_decision"]["status"]

    result: dict[str, Any] = {
        "fixture": FIXTURE_NAME,
        "routing_status": routing_status,
        "template": str((TEMPLATE_DIR / TEMPLATE_NAME).relative_to(REPO_ROOT)),
        "output": str((HWPX_OUTPUT_DIR / OUTPUT_NAME).relative_to(REPO_ROOT)),
        "status": "pending",
        "reasons": [],
    }

    if routing_status != "ready_for_draft":
        result.update(
            {
                "status": "skipped_not_ready_for_draft",
                "reasons": [f"routing_status가 ready_for_draft가 아닙니다: {routing_status}"],
            }
        )
        return result

    payload = map_to_hwpx_payload(normalized)
    if payload is None:
        result.update({"status": "skipped_no_payload", "reasons": ["payload가 생성되지 않았습니다."]})
        return result

    is_safe, reasons = validate_for_hwpx_rendering(payload)
    if not is_safe:
        result.update({"status": "validation_failed", "reasons": reasons})
        return result

    template_path = TEMPLATE_DIR / TEMPLATE_NAME
    if not is_hwpx_template_available(template_path):
        result.update(
            {
                "status": "template_required",
                "reasons": ["placeholder_one_page_report.hwpx 로컬 템플릿 필요"],
            }
        )
        return result

    placeholder_map = build_placeholder_map(payload)
    render_result = replace_placeholders_in_hwpx(
        template_path,
        HWPX_OUTPUT_DIR / OUTPUT_NAME,
        placeholder_map,
    )
    result.update(render_result)
    return result


def main() -> None:
    result = render_mapped_fixture()
    print("Mapped HWPX render PoC 실행 결과")
    print(f"- {result['fixture']}: {result['status']}")
    if result.get("output_path"):
        print(f"  output_path: {result['output_path']}")
    for reason in result.get("reasons", []):
        print(f"  - {reason}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    summary_path = OUTPUT_DIR / "mapped_hwpx_render_summary.json"
    try:
        summary_path.write_text(
            json.dumps({"result": result}, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"summary_output: {summary_path}")
    except PermissionError:
        print(f"summary_output_skipped_permission_error: {summary_path}")


if __name__ == "__main__":
    main()
