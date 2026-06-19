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
HELPER_FIXTURE_DIR = BASE_DIR / "fixtures" / "placeholder_confirmed_values"
OUTPUT_DIR = BASE_DIR / "output"


def load_helper_cases() -> list[dict[str, Any]]:
    cases: list[dict[str, Any]] = []
    for path in sorted(HELPER_FIXTURE_DIR.glob("*.json")):
        with path.open("r", encoding="utf-8") as file:
            fixture = json.load(file)
        for case in fixture.get("cases", []):
            loaded_case = dict(case)
            loaded_case["fixture"] = path.name
            cases.append(loaded_case)
    return cases


def validate_case(case: dict[str, Any]) -> dict[str, Any]:
    if "single_value" in case:
        actual_result = is_placeholder_confirmed_value(case["single_value"])
        expected_result = case["expected_single_value_result"]
        return {
            "fixture": case.get("fixture"),
            "case_id": case["case_id"],
            "actual_result": actual_result,
            "expected_result": expected_result,
            "passed": actual_result == expected_result,
            "findings": [],
        }

    findings = find_invalid_placeholder_confirmed_values(case["values"])
    expected_invalid_count = case["expected_invalid_count"]
    passed = len(findings) == expected_invalid_count
    return {
        "fixture": case.get("fixture"),
        "case_id": case["case_id"],
        "invalid_count": len(findings),
        "expected_invalid_count": expected_invalid_count,
        "passed": passed,
        "findings": findings,
    }


def main() -> None:
    cases = load_helper_cases()
    results = [validate_case(case) for case in cases]
    all_passed = bool(results) and all(result["passed"] for result in results)

    print("placeholder_confirmed_values helper 검증 결과")
    for result in results:
        if "invalid_count" in result:
            print(
                f"- {result['fixture']} / {result['case_id']}: "
                f"invalid {result['invalid_count']} / "
                f"expected {result['expected_invalid_count']} / "
                f"{'passed' if result['passed'] else 'failed'}"
            )
        else:
            print(
                f"- {result['fixture']} / {result['case_id']}: "
                f"{result['actual_result']} / expected {result['expected_result']} / "
                f"{'passed' if result['passed'] else 'failed'}"
            )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / "placeholder_confirmed_values_summary.json"
    try:
        output_path.write_text(
            json.dumps(
                {
                    "all_passed": all_passed,
                    "results": results,
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
