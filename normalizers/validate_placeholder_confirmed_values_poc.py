"""Validate read-only placeholder_confirmed_values helper behavior."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from placeholder_confirmed_values import (
    find_invalid_placeholder_confirmed_values,
    is_placeholder_confirmed_value,
)


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"

HELPER_CASES: list[dict[str, Any]] = [
    {
        "case_id": "safe_placeholder_values",
        "values": {
            "schedule": "[추진 일정 확인 필요]",
            "budget": "[예산 확인 필요]",
            "results_or_metrics": "[실적 수치 확인 필요]",
            "background": "[비식별 배경 요약]",
        },
        "expected_invalid_count": 0,
    },
    {
        "case_id": "plain_text_value",
        "values": {
            "schedule": "추진 일정 확인 필요",
        },
        "expected_invalid_count": 1,
    },
    {
        "case_id": "empty_placeholder",
        "values": {
            "budget": "[]",
        },
        "expected_invalid_count": 2,
    },
    {
        "case_id": "actual_value_marker",
        "values": {
            "budget": "[실제 금액 입력됨]",
        },
        "expected_invalid_count": 2,
    },
    {
        "case_id": "not_mapping",
        "values": ["[확인 필요]"],
        "expected_invalid_count": 1,
    },
]


def validate_case(case: dict[str, Any]) -> dict[str, Any]:
    findings = find_invalid_placeholder_confirmed_values(case["values"])
    expected_invalid_count = case["expected_invalid_count"]
    passed = len(findings) == expected_invalid_count
    return {
        "case_id": case["case_id"],
        "invalid_count": len(findings),
        "expected_invalid_count": expected_invalid_count,
        "passed": passed,
        "findings": findings,
    }


def main() -> None:
    results = [validate_case(case) for case in HELPER_CASES]
    direct_checks = {
        "safe_single_value": is_placeholder_confirmed_value("[확인 필요]"),
        "unsafe_plain_text": is_placeholder_confirmed_value("확인 필요"),
    }
    all_passed = all(result["passed"] for result in results) and direct_checks == {
        "safe_single_value": True,
        "unsafe_plain_text": False,
    }

    print("placeholder_confirmed_values helper 검증 결과")
    for result in results:
        print(
            f"- {result['case_id']}: "
            f"invalid {result['invalid_count']} / "
            f"expected {result['expected_invalid_count']} / "
            f"{'passed' if result['passed'] else 'failed'}"
        )
    print(f"- direct_checks: {'passed' if all_passed else 'failed'}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / "placeholder_confirmed_values_summary.json"
    try:
        output_path.write_text(
            json.dumps(
                {
                    "all_passed": all_passed,
                    "results": results,
                    "direct_checks": direct_checks,
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        print(f"summary_output: {output_path}")
    except PermissionError:
        print(f"summary_output_skipped_permission_error: {output_path}")


if __name__ == "__main__":
    main()
