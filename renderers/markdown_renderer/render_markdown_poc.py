"""Run the Markdown preview renderer PoC for placeholder JSON samples."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Callable

from templates import (
    render_blocked_report,
    render_official_letter_preview,
    render_project_plan_preview,
    render_survey_table_preview,
    render_vendor_email_preview,
)
from validation import validate_for_markdown_rendering


REPO_ROOT = Path(__file__).resolve().parents[2]
INPUT_DIR = REPO_ROOT / "examples" / "json"
OUTPUT_DIR = Path(__file__).resolve().parent / "output"

SAMPLES = [
    ("sample_official_letter.json", "sample_official_letter_preview.md"),
    ("sample_project_plan.json", "sample_project_plan_preview.md"),
    ("sample_vendor_email.json", "sample_vendor_email_preview.md"),
    ("sample_survey_table.json", "sample_survey_table_preview.md"),
    ("sample_blocked_security_case.json", "sample_blocked_security_case_blocked.md"),
]


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def select_renderer(data: dict[str, Any]) -> Callable[[dict[str, Any]], str]:
    document_type = data.get("document_type")
    if document_type in {"survey_request_letter", "official_letter"}:
        return render_official_letter_preview
    if document_type == "project_plan":
        return render_project_plan_preview
    if document_type == "vendor_email":
        return render_vendor_email_preview
    if document_type == "survey_table":
        return render_survey_table_preview
    return render_official_letter_preview


def render_sample(input_name: str, output_name: str) -> tuple[str, str, str]:
    data = load_json(INPUT_DIR / input_name)
    is_safe, reasons = validate_for_markdown_rendering(data)
    risk_level = (data.get("security_review") or {}).get("risk_level")

    if not is_safe or risk_level == "blocked":
        markdown = render_blocked_report(data, reasons)
        result = "blocked"
    else:
        renderer = select_renderer(data)
        markdown = renderer(data)
        result = "rendered"

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / output_name
    output_path.write_text(markdown, encoding="utf-8")
    return input_name, output_name, result


def main() -> None:
    results = [render_sample(input_name, output_name) for input_name, output_name in SAMPLES]
    print("Markdown 미리보기 렌더러 PoC 실행 결과")
    for input_name, output_name, result in results:
        print(f"- {input_name} -> {output_name}: {result}")


if __name__ == "__main__":
    main()
