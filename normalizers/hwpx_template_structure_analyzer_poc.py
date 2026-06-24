from __future__ import annotations

import argparse
import json
import re
import zipfile
from xml.etree import ElementTree
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parent
REPO_ROOT = BASE_DIR.parent
TEMPLATE_DIR = REPO_ROOT / "templates" / "hwpx"
OUTPUT_DIR = BASE_DIR / "output"

PLACEHOLDER_PATTERN = re.compile(r"\{\{[^{}]+\}\}")

DEFAULT_TEMPLATE_CANDIDATES = {
    "one_page_report": "placeholder_one_page_report.hwpx",
    "project_plan": "placeholder_project_plan.hwpx",
    "result_report": "placeholder_result_report.hwpx",
    "review_report": "placeholder_review_report.hwpx",
}


def analyze_hwpx_template(template_path: Path) -> dict[str, Any]:
    result: dict[str, Any] = {
        "template_path": _relative_or_name(template_path),
        "available": _is_hwpx_template_available(template_path),
        "status": "template_required",
        "section_count": 0,
        "paragraph_count": 0,
        "text_node_count": 0,
        "table_count": 0,
        "placeholder_count": 0,
        "placeholders": [],
        "has_preview_text": False,
        "preview_text_length": 0,
        "errors": [],
    }

    if not result["available"]:
        result["errors"].append("템플릿 파일이 없거나 .hwpx 확장자가 아닙니다.")
        return result

    placeholders: set[str] = set()

    try:
        with zipfile.ZipFile(template_path, "r") as package:
            names = package.namelist()
            section_names = sorted(
                name
                for name in names
                if re.fullmatch(r"Contents/section\d+\.xml", name)
            )
            result["section_count"] = len(section_names)

            preview_info = package.getinfo("Preview/PrvText.txt") if "Preview/PrvText.txt" in names else None
            if preview_info is not None:
                result["has_preview_text"] = True
                result["preview_text_length"] = preview_info.file_size

            for section_name in section_names:
                section_xml = package.read(section_name).decode("utf-8", errors="replace")
                section_summary = _summarize_section_xml(section_xml)
                result["paragraph_count"] += section_summary["paragraph_count"]
                result["text_node_count"] += section_summary["text_node_count"]
                result["table_count"] += section_summary["table_count"]
                placeholders.update(section_summary["placeholders"])

    except zipfile.BadZipFile:
        result["errors"].append("HWPX ZIP 패키지를 열 수 없습니다.")
        return result
    except KeyError as exc:
        result["errors"].append(f"HWPX 패키지 항목을 읽을 수 없습니다: {exc}")
        return result

    result["placeholders"] = sorted(placeholders)
    result["placeholder_count"] = len(placeholders)
    result["status"] = "analyzed"
    return result


def _summarize_section_xml(section_xml: str) -> dict[str, Any]:
    try:
        root = ElementTree.fromstring(section_xml)
    except ElementTree.ParseError:
        return {
            "paragraph_count": len(re.findall(r"<hp:p\b", section_xml)),
            "text_node_count": len(re.findall(r"<hp:t\b", section_xml)),
            "table_count": len(re.findall(r"<hp:tbl\b", section_xml)),
            "placeholders": set(PLACEHOLDER_PATTERN.findall(section_xml)),
        }

    paragraph_count = 0
    text_node_count = 0
    table_count = 0
    placeholders: set[str] = set()

    for element in root.iter():
        local_name = _local_name(element.tag)
        if local_name == "p":
            paragraph_count += 1
        elif local_name == "t":
            text_node_count += 1
            if element.text:
                placeholders.update(PLACEHOLDER_PATTERN.findall(element.text))
        elif local_name == "tbl":
            table_count += 1

    for paragraph in root.iter():
        if _local_name(paragraph.tag) != "p":
            continue
        paragraph_text = "".join(
            text_node.text or ""
            for text_node in paragraph.iter()
            if _local_name(text_node.tag) == "t"
        )
        placeholders.update(PLACEHOLDER_PATTERN.findall(paragraph_text))

    return {
        "paragraph_count": paragraph_count,
        "text_node_count": text_node_count,
        "table_count": table_count,
        "placeholders": placeholders,
    }


def _local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1] if "}" in tag else tag


def analyze_default_templates() -> list[dict[str, Any]]:
    results = []
    for document_type, template_name in DEFAULT_TEMPLATE_CANDIDATES.items():
        result = analyze_hwpx_template(TEMPLATE_DIR / template_name)
        result["document_type"] = document_type
        result["template_name"] = template_name
        results.append(result)
    return results


def build_structure_summary(template_paths: list[Path] | None = None) -> dict[str, Any]:
    explicit_templates = template_paths is not None
    results = (
        analyze_explicit_templates(template_paths or [])
        if explicit_templates
        else analyze_default_templates()
    )
    return {
        "analyzer": "hwpx_template_structure_analyzer_poc",
        "scope": "structure_only_no_text_extraction",
        "mode": "explicit_templates" if explicit_templates else "default_templates",
        "results": results,
    }


def analyze_explicit_templates(template_paths: list[Path]) -> list[dict[str, Any]]:
    results = []
    for template_path in template_paths:
        result = analyze_hwpx_template(template_path)
        result["document_type"] = "manual_candidate"
        result["template_name"] = template_path.name
        results.append(result)
    return results


def _is_hwpx_template_available(template_path: Path) -> bool:
    return template_path.exists() and template_path.is_file() and template_path.suffix.lower() == ".hwpx"


def _relative_or_name(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except (OSError, ValueError):
        return path.name


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Analyze HWPX template package structure without extracting body text.",
    )
    parser.add_argument(
        "--template",
        action="append",
        type=Path,
        help="HWPX template or deidentified working-copy candidate to analyze. Can be repeated.",
    )
    parser.add_argument(
        "--no-output",
        action="store_true",
        help="Print results only and do not write normalizers/output summary JSON.",
    )
    return parser.parse_args(argv)


def write_summary(summary: dict[str, Any]) -> Path | None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / "hwpx_template_structure_summary.json"
    try:
        output_path.write_text(
            json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"summary_output: {output_path}")
        return output_path
    except PermissionError:
        print(f"summary_output_skipped_permission_error: {output_path}")
        return None


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    template_paths = args.template if args.template else None
    summary = build_structure_summary(template_paths)

    if args.no_output:
        print("summary_output_skipped_no_output_flag")
    else:
        write_summary(summary)

    for result in summary["results"]:
        print(
            f"{result['document_type']}: {result['status']} "
            f"sections={result['section_count']} paragraphs={result['paragraph_count']} "
            f"tables={result['table_count']} placeholders={result['placeholder_count']}"
        )


if __name__ == "__main__":
    main()
