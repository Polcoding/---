"""Run the XLSX renderer PoC with the placeholder survey sample."""

from __future__ import annotations

import json
from pathlib import Path

from templates import build_workbook
from validation import validate_payload


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INPUT = REPO_ROOT / "examples" / "json" / "sample_survey_table.json"
DEFAULT_OUTPUT = Path(__file__).resolve().parent / "output" / "sample_survey_table_poc.xlsx"


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def render(input_path: Path = DEFAULT_INPUT, output_path: Path = DEFAULT_OUTPUT) -> Path:
    payload = load_json(input_path)
    validation_errors = validate_payload(payload)
    if validation_errors:
        joined = "\n- ".join(validation_errors)
        raise SystemExit(f"XLSX 렌더링 차단:\n- {joined}")

    workbook = build_workbook(payload)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    workbook.save(output_path)
    return output_path


if __name__ == "__main__":
    result = render()
    print(f"XLSX PoC 생성 완료: {result}")
