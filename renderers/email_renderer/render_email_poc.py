"""Run the Email draft renderer PoC for placeholder JSON samples."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from templates import (
    render_blocked_email_report,
    render_vendor_email_markdown,
    render_vendor_email_text,
)
from validation import validate_for_email_rendering


REPO_ROOT = Path(__file__).resolve().parents[2]
INPUT_DIR = REPO_ROOT / "examples" / "json"
OUTPUT_DIR = Path(__file__).resolve().parent / "output"

VENDOR_EMAIL_SAMPLE = "sample_vendor_email.json"
BLOCKED_SAMPLE = "sample_blocked_security_case.json"

VENDOR_MARKDOWN_OUTPUT = "sample_vendor_email_draft.md"
VENDOR_TEXT_OUTPUT = "sample_vendor_email_draft.txt"
BLOCKED_OUTPUT = "sample_blocked_security_case_blocked.md"


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def write_output(file_name: str, content: str) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / file_name
    output_path.write_text(content, encoding="utf-8")
    return output_path


def risk_level_of(data: dict[str, Any]) -> str | None:
    security_review = data.get("security_review")
    if not isinstance(security_review, dict):
        return None
    risk_level = security_review.get("risk_level")
    return str(risk_level) if risk_level is not None else None


def render_vendor_email_sample() -> list[tuple[str, str]]:
    data = load_json(INPUT_DIR / VENDOR_EMAIL_SAMPLE)
    is_safe, reasons = validate_for_email_rendering(data)
    document_type = data.get("document_type")
    risk_level = risk_level_of(data)

    if risk_level == "blocked" or not is_safe:
        output_path = write_output(BLOCKED_OUTPUT, render_blocked_email_report(data, reasons))
        return [(VENDOR_EMAIL_SAMPLE, f"blocked -> {output_path.name}")]

    if document_type != "vendor_email":
        return [(VENDOR_EMAIL_SAMPLE, f"warning: unsupported document_type={document_type}")]

    markdown_path = write_output(VENDOR_MARKDOWN_OUTPUT, render_vendor_email_markdown(data))
    text_path = write_output(VENDOR_TEXT_OUTPUT, render_vendor_email_text(data))
    return [
        (VENDOR_EMAIL_SAMPLE, f"rendered -> {markdown_path.name}"),
        (VENDOR_EMAIL_SAMPLE, f"rendered -> {text_path.name}"),
    ]


def render_blocked_sample() -> tuple[str, str]:
    data = load_json(INPUT_DIR / BLOCKED_SAMPLE)
    is_safe, reasons = validate_for_email_rendering(data)
    risk_level = risk_level_of(data)

    if risk_level == "blocked" or not is_safe:
        output_path = write_output(BLOCKED_OUTPUT, render_blocked_email_report(data, reasons))
        return BLOCKED_SAMPLE, f"blocked -> {output_path.name}"

    document_type = data.get("document_type")
    return BLOCKED_SAMPLE, f"warning: unsupported document_type={document_type}"


def main() -> None:
    results = []
    results.extend(render_vendor_email_sample())
    results.append(render_blocked_sample())

    print("Email 초안 렌더러 PoC 실행 결과")
    for input_name, result in results:
        print(f"- {input_name}: {result}")

    print("주의: 실제 이메일 발송, SMTP 연결, Gmail/Outlook 연결, API 호출은 수행하지 않았습니다.")


if __name__ == "__main__":
    main()
