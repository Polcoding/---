"""HWPX package inspection and placeholder replacement helpers.

This module treats a HWPX file as an existing zip package. It does not create a
new HWPX document from scratch and only replaces placeholders in text-like files
inside a provided placeholder template.
"""

from __future__ import annotations

import json
import re
import zipfile
from pathlib import Path
from typing import Any


PLACEHOLDER_PATTERN = re.compile(r"\{\{[A-Za-z0-9_]+\}\}")

TEXT_FILE_SUFFIXES = {
    ".xml",
    ".rels",
    ".txt",
}

ALLOWED_PLACEHOLDERS = {
    "{{document_number}}",
    "{{execution_date}}",
    "{{recipient}}",
    "{{reference}}",
    "{{title}}",
    "{{body_sections}}",
    "{{body_section_1}}",
    "{{body_section_2}}",
    "{{body_section_3}}",
    "{{body_section_1_child_1}}",
    "{{body_section_2_child_1}}",
    "{{body_section_2_child_2}}",
    "{{sub_sections}}",
    "{{overview_table}}",
    "{{schedule_table}}",
    "{{budget_table}}",
    "{{attachments}}",
    "{{closing}}",
    "{{checklist}}",
    "{{missing_fields}}",
    "{{security_review}}",
    "{{draft_status}}",
    "{{human_review_required}}",
    "{{background}}",
    "{{purpose}}",
    "{{report_summary}}",
    "{{main_points}}",
    "{{review_opinion}}",
    "{{issues_or_considerations}}",
    "{{next_steps}}",
    "{{action_items}}",
    "{{main_contents}}",
    "{{detailed_plan}}",
    "{{expected_effects}}",
    "{{review_items}}",
    "{{future_plan}}",
    "{{linked_plan_reference}}",
    "{{planned_items}}",
    "{{actual_results}}",
    "{{comparison_to_plan}}",
    "{{main_outcomes}}",
    "{{issues}}",
    "{{improvements}}",
    "{{review_background}}",
    "{{review_scope}}",
    "{{risks}}",
    "{{required_reviews}}",
    "{{next_actions}}",
}

DEFAULT_PLACEHOLDER_VALUE = "[확인 필요]"


def is_hwpx_template_available(template_path: Path) -> bool:
    """Return True when a path points to an existing .hwpx template."""
    return template_path.exists() and template_path.is_file() and template_path.suffix.lower() == ".hwpx"


def inspect_hwpx_package(template_path: Path) -> dict:
    """Inspect a HWPX zip package without exposing internal file contents."""
    result = {
        "template_path": str(template_path),
        "available": is_hwpx_template_available(template_path),
        "is_zip": False,
        "file_count": 0,
        "files": [],
        "xml_candidates": [],
        "placeholders": [],
        "errors": [],
    }

    if not result["available"]:
        result["errors"].append("템플릿 파일이 없거나 .hwpx 확장자가 아닙니다.")
        return result

    try:
        with zipfile.ZipFile(template_path, "r") as package:
            names = package.namelist()
            result["is_zip"] = True
            result["file_count"] = len(names)
            result["files"] = names
            result["xml_candidates"] = [name for name in names if _is_text_like_name(name)]

            found: set[str] = set()
            for name in result["xml_candidates"]:
                try:
                    text = package.read(name).decode("utf-8")
                except UnicodeDecodeError:
                    continue
                found.update(find_placeholders_in_text(text))

            result["placeholders"] = sorted(found)
    except zipfile.BadZipFile:
        result["errors"].append("HWPX 템플릿을 zip 패키지로 열 수 없습니다.")
    except OSError as exc:
        result["errors"].append(f"템플릿 검사 중 파일 오류가 발생했습니다: {exc}")

    return result


def find_placeholders_in_text(text: str) -> set[str]:
    """Find placeholders in {{placeholder}} format."""
    return set(PLACEHOLDER_PATTERN.findall(text))


def build_placeholder_map(data: dict) -> dict[str, str]:
    """Build allowed placeholder values from a sample JSON payload."""
    if data.get("document_type") == "one_page_report":
        return _build_one_page_report_placeholder_map(data)
    if data.get("document_type") == "project_plan":
        return _build_project_plan_placeholder_map(data)
    if data.get("document_type") == "result_report":
        return _build_result_report_placeholder_map(data)
    if data.get("document_type") == "review_report":
        return _build_review_report_placeholder_map(data)

    document = _first_document(data)
    security_review = data.get("security_review", {})
    body_section_placeholders = _build_body_section_placeholders(document.get("body_sections"))

    placeholder_map = {
        "{{document_number}}": _safe_string(document.get("document_number")),
        "{{execution_date}}": _safe_string(document.get("execution_date")),
        "{{recipient}}": _safe_string(document.get("recipient")),
        "{{reference}}": _safe_string(document.get("reference")),
        "{{title}}": _safe_string(document.get("title")),
        "{{body_sections}}": _format_body_sections(document.get("body_sections")),
        "{{sub_sections}}": _format_list(document.get("sub_sections")),
        "{{overview_table}}": _format_mapping_or_list(document.get("overview")),
        "{{schedule_table}}": _format_mapping_or_list(document.get("schedule")),
        "{{budget_table}}": _format_mapping_or_list(document.get("budget")),
        "{{attachments}}": _format_attachments(document.get("attachments") or data.get("attachments")),
        "{{closing}}": _safe_string(document.get("closing")),
        "{{checklist}}": _format_list(document.get("checklist") or data.get("checklist")),
        "{{missing_fields}}": _format_missing_fields(data.get("missing_fields")),
        "{{security_review}}": _format_security_review(security_review),
        "{{draft_status}}": _safe_string(data.get("draft_status")),
        "{{human_review_required}}": _safe_string(data.get("human_review_required")),
        "{{background}}": _safe_string(document.get("background")),
        "{{purpose}}": _safe_string(document.get("purpose")),
        "{{main_contents}}": _format_result_summary_field(
            document.get("main_contents"),
            "[주요 내용 확인 필요]",
        ),
        "{{detailed_plan}}": _format_mapping_or_list(document.get("detailed_plan")),
        "{{expected_effects}}": _format_result_summary_field(
            document.get("expected_effects"),
            "[기대효과 확인 필요]",
        ),
        "{{review_items}}": _format_result_summary_field(
            document.get("review_items"),
            "[검토사항 확인 필요]",
        ),
        "{{future_plan}}": _safe_string(document.get("future_plan")),
    }
    placeholder_map.update(body_section_placeholders)

    return {key: placeholder_map.get(key, DEFAULT_PLACEHOLDER_VALUE) for key in sorted(ALLOWED_PLACEHOLDERS)}


def _build_one_page_report_placeholder_map(data: dict) -> dict[str, str]:
    document = _first_document(data)
    security_review = data.get("security_review", {})

    placeholder_map = {
        "{{title}}": _safe_string(document.get("title")),
        "{{report_summary}}": _format_report_summary(document.get("report_summary")),
        "{{background}}": _safe_string(document.get("background")),
        "{{main_points}}": _format_list(document.get("main_points")),
        "{{review_opinion}}": _safe_string(document.get("review_opinion")),
        "{{issues_or_considerations}}": _format_list(document.get("issues_or_considerations")),
        "{{next_steps}}": _format_list(document.get("next_steps")),
        "{{action_items}}": _format_mapping_or_list(document.get("action_items")),
        "{{missing_fields}}": _format_missing_fields(data.get("missing_fields")),
        "{{checklist}}": _format_list(document.get("checklist") or data.get("checklist")),
        "{{security_review}}": _format_security_review(security_review),
        "{{draft_status}}": _safe_string(data.get("draft_status")),
        "{{human_review_required}}": _safe_string(data.get("human_review_required")),
    }

    return {key: placeholder_map.get(key, DEFAULT_PLACEHOLDER_VALUE) for key in sorted(ALLOWED_PLACEHOLDERS)}


def _build_project_plan_placeholder_map(data: dict) -> dict[str, str]:
    document = _first_document(data)
    security_review = data.get("security_review", {})

    placeholder_map = {
        "{{title}}": _safe_string(document.get("title")),
        "{{background}}": _safe_string(document.get("background")),
        "{{purpose}}": _safe_string(document.get("purpose")),
        "{{overview_table}}": _format_result_summary_field(
            document.get("overview"),
            "[사업명ㆍ추진기간ㆍ추진대상ㆍ추진방식ㆍ소요예산 확인 필요]",
        ),
        "{{main_contents}}": _format_result_summary_field(
            document.get("main_contents"),
            "[주요 내용 확인 필요]",
        ),
        "{{detailed_plan}}": _format_result_summary_field(
            document.get("detailed_plan"),
            "[단계별 세부 추진내용 확인 필요]",
        ),
        "{{schedule_table}}": _format_result_summary_field(
            document.get("schedule"),
            "[추진 단계ㆍ기간ㆍ세부 일정 확인 필요]",
        ),
        "{{budget_table}}": _format_result_summary_field(
            document.get("budget"),
            "[소요예산ㆍ예산 항목ㆍ산출 기준 확인 필요]",
        ),
        "{{expected_effects}}": _format_result_summary_field(
            document.get("expected_effects"),
            "[기대효과 확인 필요]",
        ),
        "{{review_items}}": _format_result_summary_field(
            document.get("review_items"),
            "[검토사항 확인 필요]",
        ),
        "{{future_plan}}": _safe_string(document.get("future_plan")),
        "{{attachments}}": _format_attachments(document.get("attachments") or data.get("attachments")),
        "{{checklist}}": _format_list(document.get("checklist") or data.get("checklist")),
        "{{missing_fields}}": _format_missing_fields(data.get("missing_fields")),
        "{{security_review}}": _format_security_review(security_review),
        "{{draft_status}}": _safe_string(data.get("draft_status")),
        "{{human_review_required}}": _safe_string(data.get("human_review_required")),
    }

    return {key: placeholder_map.get(key, DEFAULT_PLACEHOLDER_VALUE) for key in sorted(ALLOWED_PLACEHOLDERS)}


def _build_result_report_placeholder_map(data: dict) -> dict[str, str]:
    document = _first_document(data)
    security_review = data.get("security_review", {})

    placeholder_map = {
        "{{title}}": _safe_string(document.get("title")),
        "{{linked_plan_reference}}": _format_result_summary_field(
            document.get("linked_plan_reference"),
            "[기존 추진계획서 참조 확인 필요]",
        ),
        "{{overview_table}}": _format_result_summary_field(
            document.get("overview"),
            "[사업명ㆍ추진기간ㆍ추진대상ㆍ담당부서 확인 필요]",
        ),
        "{{planned_items}}": _format_result_summary_field(
            document.get("planned_items"),
            "[계획 항목 확인 필요]",
        ),
        "{{actual_results}}": _format_result_summary_field(
            document.get("actual_results"),
            "[추진결과ㆍ실적 수치ㆍ참여 인원ㆍ예산 집행액 확인 필요]",
        ),
        "{{comparison_to_plan}}": _format_result_summary_field(
            document.get("comparison_to_plan"),
            "[계획 대비 결과 확인 필요]",
        ),
        "{{main_outcomes}}": _format_list(document.get("main_outcomes")),
        "{{issues}}": _format_list(document.get("issues")),
        "{{improvements}}": _format_list(document.get("improvements")),
        "{{future_plan}}": _safe_string(document.get("future_plan")),
        "{{attachments}}": _format_attachments(document.get("attachments") or data.get("attachments")),
        "{{checklist}}": _format_list(document.get("checklist") or data.get("checklist")),
        "{{missing_fields}}": _format_missing_fields(data.get("missing_fields")),
        "{{security_review}}": _format_security_review(security_review),
        "{{draft_status}}": _safe_string(data.get("draft_status")),
        "{{human_review_required}}": _safe_string(data.get("human_review_required")),
    }

    return {key: placeholder_map.get(key, DEFAULT_PLACEHOLDER_VALUE) for key in sorted(ALLOWED_PLACEHOLDERS)}


def _build_review_report_placeholder_map(data: dict) -> dict[str, str]:
    document = _first_document(data)
    security_review = data.get("security_review", {})

    placeholder_map = {
        "{{title}}": _safe_string(document.get("title")),
        "{{review_background}}": _safe_string(document.get("review_background")),
        "{{review_scope}}": _safe_string(document.get("review_scope")),
        "{{review_items}}": _format_mapping_or_list(document.get("review_items")),
        "{{review_opinion}}": _safe_string(document.get("review_opinion")),
        "{{risks}}": _format_placeholder_list_without_bullets(document.get("risks")),
        "{{required_reviews}}": _format_list(document.get("required_reviews")),
        "{{next_actions}}": _format_list(document.get("next_actions")),
        "{{attachments}}": _format_attachments(document.get("attachments") or data.get("attachments")),
        "{{checklist}}": _format_list(document.get("checklist") or data.get("checklist")),
        "{{missing_fields}}": _format_missing_fields(data.get("missing_fields")),
        "{{security_review}}": _format_security_review(security_review),
        "{{draft_status}}": _safe_string(data.get("draft_status")),
        "{{human_review_required}}": _safe_string(data.get("human_review_required")),
    }

    return {key: placeholder_map.get(key, DEFAULT_PLACEHOLDER_VALUE) for key in sorted(ALLOWED_PLACEHOLDERS)}


def replace_placeholders_in_hwpx(
    template_path: Path, output_path: Path, placeholder_map: dict
) -> dict:
    """Replace placeholders in an existing HWPX package and save a new package."""
    if not is_hwpx_template_available(template_path):
        return {
            "status": "template_required",
            "replaced_count": 0,
            "remaining_placeholders": [],
            "errors": ["템플릿 파일이 없거나 .hwpx 확장자가 아닙니다."],
        }

    output_path.parent.mkdir(parents=True, exist_ok=True)

    candidate_paths = (
        output_path,
        output_path.with_name(f"{output_path.stem}_latest{output_path.suffix}"),
        *[
            output_path.with_name(f"{output_path.stem}_run{index}{output_path.suffix}")
            for index in range(1, 6)
        ],
    )

    for candidate_path in candidate_paths:
        replaced_count = 0
        remaining_placeholders: set[str] = set()
        processed_files: list[str] = []

        try:
            with zipfile.ZipFile(template_path, "r") as source:
                with zipfile.ZipFile(candidate_path, "w") as target:
                    for info in source.infolist():
                        raw = source.read(info.filename)

                        if _is_text_like_name(info.filename):
                            try:
                                text = raw.decode("utf-8")
                            except UnicodeDecodeError:
                                target.writestr(info, raw)
                                continue

                            text, count = _replace_text_placeholders(text, placeholder_map)
                            replaced_count += count
                            remaining_placeholders.update(find_placeholders_in_text(text))
                            processed_files.append(info.filename)
                            target.writestr(info, text.encode("utf-8"))
                        else:
                            target.writestr(info, raw)
        except PermissionError:
            continue

        return {
            "status": "rendered",
            "output_path": str(candidate_path),
            "processed_text_files": processed_files,
            "replaced_count": replaced_count,
            "remaining_placeholders": sorted(remaining_placeholders),
            "errors": [],
        }

    return {
        "status": "output_error",
        "output_path": str(output_path),
        "processed_text_files": [],
        "replaced_count": 0,
        "remaining_placeholders": [],
        "errors": ["HWPX output 파일을 쓸 수 없습니다."],
    }


def write_template_required_report(output_dir: Path, reason: str) -> Path:
    """Write a Markdown report when rendering cannot proceed without a template."""
    output_dir.mkdir(parents=True, exist_ok=True)
    report_path = output_dir / "template_required_report.md"
    fallback_path = output_dir / "template_required_report_latest.md"
    report = "\n".join(
        [
            "# HWPX 템플릿 필요 보고",
            "",
            "## 상태",
            "",
            "템플릿이 없어 HWPX 렌더링을 중단했습니다.",
            "",
            "## 사유",
            "",
            _safe_string(reason),
            "",
            "## 조치 필요",
            "",
            "- placeholder 기반 HWPX 테스트 템플릿을 별도 검수 후 준비해야 합니다.",
            "- 실제 기관 양식 원본, 실제 공문 원문, 실제 개인정보는 사용하지 않습니다.",
            "- 템플릿이 준비되기 전에는 실제 HWPX 파일을 생성하지 않습니다.",
            "",
        ]
    )
    for candidate_path in (report_path, fallback_path):
        try:
            candidate_path.write_text(report, encoding="utf-8")
            return candidate_path
        except PermissionError:
            continue

    if report_path.exists():
        return report_path
    raise PermissionError(f"템플릿 필요 보고서를 쓸 수 없습니다: {report_path}")


def _is_text_like_name(name: str) -> bool:
    return Path(name).suffix.lower() in TEXT_FILE_SUFFIXES


def _replace_text_placeholders(text: str, placeholder_map: dict) -> tuple[str, int]:
    replaced_count = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal replaced_count
        placeholder = match.group(0)
        if placeholder in ALLOWED_PLACEHOLDERS:
            replaced_count += 1
            return str(placeholder_map.get(placeholder, DEFAULT_PLACEHOLDER_VALUE))
        return placeholder

    return PLACEHOLDER_PATTERN.sub(replace, text), replaced_count


def _first_document(data: dict) -> dict:
    documents = data.get("documents")
    if isinstance(documents, list) and documents and isinstance(documents[0], dict):
        return documents[0]
    return {}


def _safe_string(value: Any) -> str:
    if value is None or value == "":
        return DEFAULT_PLACEHOLDER_VALUE
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (dict, list)):
        return _format_mapping_or_list(value)
    return str(value)


def _format_body_sections(sections: Any, depth: int = 0) -> str:
    if not isinstance(sections, list) or not sections:
        return DEFAULT_PLACEHOLDER_VALUE

    lines: list[str] = []
    indent = "  " * depth
    for section in sections:
        if isinstance(section, dict):
            number = _safe_string(section.get("number"))
            content = _safe_string(section.get("content"))
            lines.append(f"{indent}{number} {content}")
            children = section.get("children")
            if children:
                lines.append(_format_body_sections(children, depth + 1))
        else:
            lines.append(f"{indent}- {_safe_string(section)}")
    return "\n".join(line for line in lines if line)


def _build_body_section_placeholders(sections: Any) -> dict[str, str]:
    placeholders = {
        "{{body_section_1}}": DEFAULT_PLACEHOLDER_VALUE,
        "{{body_section_2}}": DEFAULT_PLACEHOLDER_VALUE,
        "{{body_section_3}}": DEFAULT_PLACEHOLDER_VALUE,
        "{{body_section_1_child_1}}": "",
        "{{body_section_2_child_1}}": "",
        "{{body_section_2_child_2}}": "",
    }

    if not isinstance(sections, list):
        return placeholders

    for index, section in enumerate(sections[:3], start=1):
        placeholder = f"{{{{body_section_{index}}}}}"
        placeholders[placeholder] = _format_numbered_section(section)

        if isinstance(section, dict):
            children = section.get("children")
            if isinstance(children, list):
                for child_index, child in enumerate(children[:2], start=1):
                    child_placeholder = f"{{{{body_section_{index}_child_{child_index}}}}}"
                    if child_placeholder in placeholders:
                        placeholders[child_placeholder] = _format_numbered_section(child)

    return placeholders


def _format_numbered_section(section: Any) -> str:
    if isinstance(section, dict):
        number = _safe_string(section.get("number"))
        content = _safe_string(section.get("content"))
        return f"{number} {content}".strip()
    return _safe_string(section)


def _format_attachments(attachments: Any) -> str:
    if not isinstance(attachments, list) or not attachments:
        return DEFAULT_PLACEHOLDER_VALUE

    lines: list[str] = []
    for index, attachment in enumerate(attachments, start=1):
        if isinstance(attachment, dict):
            number = attachment.get("number") or f"{index}."
            title = attachment.get("title") or "[문서명 확인 필요]"
            copies = attachment.get("copies") or "[부수 확인 필요]"
            lines.append(f"{number} {title} {copies}")
        else:
            lines.append(f"{index}. {_safe_string(attachment)}")
    return "\n".join(lines)


def _format_missing_fields(missing_fields: Any) -> str:
    if not isinstance(missing_fields, list) or not missing_fields:
        return DEFAULT_PLACEHOLDER_VALUE

    lines: list[str] = []
    for item in missing_fields:
        if isinstance(item, dict):
            field_name = item.get("field_name", "[필드명 확인 필요]")
            reason = item.get("reason", "[사유 확인 필요]")
            suggested = item.get("suggested_placeholder", DEFAULT_PLACEHOLDER_VALUE)
            lines.append(f"- {field_name}: {reason} ({suggested})")
        else:
            lines.append(f"- {_safe_string(item)}")
    return "\n".join(lines)


def _format_security_review(security_review: Any) -> str:
    if not isinstance(security_review, dict):
        return DEFAULT_PLACEHOLDER_VALUE

    keys = [
        "risk_level",
        "contains_personal_info",
        "contains_sensitive_info",
        "contains_internal_info",
        "notes",
    ]
    return "\n".join(f"- {key}: {_safe_string(security_review.get(key))}" for key in keys)


def _format_list(value: Any) -> str:
    if not isinstance(value, list) or not value:
        return DEFAULT_PLACEHOLDER_VALUE
    if len(value) == 1 and _is_placeholder_only_item(value[0]):
        return _safe_string(value[0])
    return "\n".join(f"- {_format_list_item(item)}" for item in value)


def _format_placeholder_list_without_bullets(value: Any) -> str:
    if not isinstance(value, list) or not value:
        return DEFAULT_PLACEHOLDER_VALUE
    if all(_is_placeholder_only_item(item) for item in value):
        return "\n".join(_safe_string(item) for item in value)
    return _format_list(value)


def _format_mapping_or_list(value: Any) -> str:
    if value is None or value == "":
        return DEFAULT_PLACEHOLDER_VALUE
    if isinstance(value, list):
        if not value:
            return DEFAULT_PLACEHOLDER_VALUE
        if len(value) == 1 and _is_placeholder_only_item(value[0]):
            return _safe_string(value[0])
        return "\n".join(f"- {_format_list_item(item)}" for item in value)
    if isinstance(value, dict):
        if not value:
            return DEFAULT_PLACEHOLDER_VALUE
        return "\n".join(f"- {key}: {_safe_string(item)}" for key, item in value.items())
    return _safe_string(value)


def _format_report_summary(value: Any) -> str:
    if value is None or value == "":
        return DEFAULT_PLACEHOLDER_VALUE
    if isinstance(value, dict):
        return "[보고일자ㆍ담당부서ㆍ검토자ㆍ보고목적 확인 필요]"
    if isinstance(value, list):
        return "[보고 개요 확인 필요]"
    return _safe_string(value)


def _format_result_summary_field(value: Any, fallback: str) -> str:
    if value is None or value == "":
        return DEFAULT_PLACEHOLDER_VALUE
    if isinstance(value, (dict, list)):
        return fallback
    return _safe_string(value)


def _format_list_item(item: Any) -> str:
    if isinstance(item, dict):
        if not item:
            return DEFAULT_PLACEHOLDER_VALUE
        return " / ".join(f"{key}: {_safe_string(value)}" for key, value in item.items())
    return _safe_string(item)


def _is_placeholder_only_item(item: Any) -> bool:
    if not isinstance(item, str):
        return False
    stripped = item.strip()
    return stripped.startswith("[") and stripped.endswith("]")


def _to_json_text(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2)
