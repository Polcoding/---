"""Validate mapper payloads with the existing HWPX renderer validation rules."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from hwpx_payload_mapper_poc import map_to_hwpx_payload
from input_normalizer_poc import FIXTURE_DIR, OUTPUT_DIR, load_json, normalize_request


REPO_ROOT = Path(__file__).resolve().parents[1]
HWPX_RENDERER_DIR = REPO_ROOT / "renderers" / "hwpx_renderer"
sys.path.insert(0, str(HWPX_RENDERER_DIR))

from validation import validate_for_hwpx_rendering  # noqa: E402


def validate_fixture(path: Path) -> dict[str, Any]:
    fixture = load_json(path)
    normalized = normalize_request(fixture)
    payload = map_to_hwpx_payload(normalized)
    routing_status = normalized["routing_decision"]["status"]

    if payload is None:
        expected_skipped = routing_status in {"needs_security_review", "blocked"}
        return {
            "fixture": path.name,
            "routing_status": routing_status,
            "payload_created": False,
            "validation_passed": None,
            "reasons": [],
            "passed": expected_skipped,
        }

    validation_passed, reasons = validate_for_hwpx_rendering(payload)
    return {
        "fixture": path.name,
        "routing_status": routing_status,
        "payload_created": True,
        "validation_passed": validation_passed,
        "reasons": reasons,
        "passed": validation_passed,
    }


def main() -> None:
    results = [validate_fixture(path) for path in sorted(FIXTURE_DIR.glob("*.json"))]

    print("HWPX payload validation PoC 실행 결과")
    for result in results:
        if result["payload_created"]:
            state = "validated" if result["validation_passed"] else "validation_failed"
        else:
            state = "skipped"
        print(f"- {result['fixture']}: {result['routing_status']} / {state} / {'passed' if result['passed'] else 'failed'}")
        for reason in result["reasons"]:
            print(f"  - {reason}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / "hwpx_payload_validation_summary.json"
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
