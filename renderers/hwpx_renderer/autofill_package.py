"""Autofill helpers for placeholder-free HWPX sample templates.

This module is intentionally conservative. It clones an existing HWPX package
and appends deidentified draft paragraphs to the first section XML. It does not
store source body text, call external AI, or add the source HWPX to Git.
"""

from __future__ import annotations

import copy
import re
import zipfile
from pathlib import Path
from typing import Any
from xml.etree import ElementTree


SECTION_PATTERN = re.compile(r"Contents/section\d+\.xml")


def render_autofill_draft_to_hwpx(
    template_path: Path,
    output_path: Path,
    draft_lines: list[str],
    anchor_candidates: list[str] | None = None,
) -> dict[str, Any]:
    """Clone a HWPX package and insert deidentified draft lines into section0."""
    result: dict[str, Any] = {
        "template_path": _display_path(template_path),
        "output_path": str(output_path),
        "status": "template_required",
        "inserted_paragraph_count": 0,
        "processed_section": None,
        "inserted_after_anchor": False,
        "matched_anchor": None,
        "errors": [],
    }

    if not _is_hwpx_template_available(template_path):
        result["errors"].append("템플릿 파일이 없거나 .hwpx 확장자가 아닙니다.")
        return result

    safe_lines = [_safe_line(line) for line in draft_lines if _safe_line(line)]
    if not safe_lines:
        result.update({"status": "no_content", "errors": ["삽입할 비식별 초안 문단이 없습니다."]})
        return result

    output_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with zipfile.ZipFile(template_path, "r") as source:
            section_names = sorted(name for name in source.namelist() if SECTION_PATTERN.fullmatch(name))
            if not section_names:
                result.update({"status": "section_required", "errors": ["Contents/section*.xml이 없습니다."]})
                return result

            target_section = section_names[0]
            with zipfile.ZipFile(output_path, "w") as target:
                for info in source.infolist():
                    raw = source.read(info.filename)
                    if info.filename == target_section:
                        section_xml = raw.decode("utf-8", errors="replace")
                        section_result = _insert_draft_lines_to_section(
                            section_xml,
                            safe_lines,
                            anchor_candidates or [],
                        )
                        raw = section_result["xml"]
                    target.writestr(info, raw)
    except zipfile.BadZipFile:
        result.update({"status": "invalid_hwpx", "errors": ["HWPX ZIP 패키지를 열 수 없습니다."]})
        return result
    except PermissionError:
        result.update({"status": "output_error", "errors": ["HWPX output 파일을 쓸 수 없습니다."]})
        return result

    result.update(
        {
            "status": "rendered",
            "inserted_paragraph_count": len(safe_lines),
            "processed_section": target_section,
            "inserted_after_anchor": section_result["inserted_after_anchor"],
            "matched_anchor": section_result["matched_anchor"],
            "errors": [],
        }
    )
    return result


def render_autofill_sections_to_hwpx(
    template_path: Path,
    output_path: Path,
    profile_sections: list[dict[str, Any]],
) -> dict[str, Any]:
    """Clone a HWPX package and insert draft lines into multiple anchor areas."""
    result: dict[str, Any] = {
        "template_path": _display_path(template_path),
        "output_path": str(output_path),
        "status": "template_required",
        "inserted_paragraph_count": 0,
        "matched_anchor_count": 0,
        "processed_section": None,
        "section_results": [],
        "errors": [],
    }

    if not _is_hwpx_template_available(template_path):
        result["errors"].append("템플릿 파일이 없거나 .hwpx 확장자가 아닙니다.")
        return result

    safe_sections = _safe_profile_sections(profile_sections)
    if not safe_sections:
        result.update({"status": "no_content", "errors": ["삽입할 비식별 초안 영역이 없습니다."]})
        return result

    output_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with zipfile.ZipFile(template_path, "r") as source:
            section_names = sorted(name for name in source.namelist() if SECTION_PATTERN.fullmatch(name))
            if not section_names:
                result.update({"status": "section_required", "errors": ["Contents/section*.xml이 없습니다."]})
                return result

            target_section = section_names[0]
            with zipfile.ZipFile(output_path, "w") as target:
                for info in source.infolist():
                    raw = source.read(info.filename)
                    if info.filename == target_section:
                        section_xml = raw.decode("utf-8", errors="replace")
                        section_result = _insert_profile_sections_to_section(
                            section_xml,
                            safe_sections,
                        )
                        raw = section_result["xml"]
                    target.writestr(info, raw)
    except zipfile.BadZipFile:
        result.update({"status": "invalid_hwpx", "errors": ["HWPX ZIP 패키지를 열 수 없습니다."]})
        return result
    except PermissionError:
        result.update({"status": "output_error", "errors": ["HWPX output 파일을 쓸 수 없습니다."]})
        return result

    result.update(
        {
            "status": "rendered",
            "inserted_paragraph_count": section_result["inserted_paragraph_count"],
            "matched_anchor_count": section_result["matched_anchor_count"],
            "processed_section": target_section,
            "section_results": section_result["section_results"],
            "errors": [],
        }
    )
    return result


def _insert_draft_lines_to_section(
    section_xml: str,
    draft_lines: list[str],
    anchor_candidates: list[str],
) -> dict[str, Any]:
    _register_namespaces(section_xml)
    root = ElementTree.fromstring(section_xml)
    anchor = _find_anchor_paragraph(root, anchor_candidates)
    if anchor is not None:
        parent, anchor_index, anchor_paragraph, matched_anchor = anchor
        paragraph_template = _select_insertion_paragraph_template(root, anchor_paragraph)
        insert_index = anchor_index + 1
        for line in draft_lines:
            paragraph = _build_text_paragraph(paragraph_template, line)
            parent.insert(insert_index, paragraph)
            insert_index += 1
        return {
            "xml": ElementTree.tostring(root, encoding="utf-8", xml_declaration=True),
            "inserted_after_anchor": True,
            "matched_anchor": matched_anchor,
        }

    paragraph_template = _find_paragraph_template(root)
    if paragraph_template is None:
        raise ValueError("section XML에 복제 가능한 문단이 없습니다.")

    for line in draft_lines:
        paragraph = _build_text_paragraph(paragraph_template, line)
        root.append(paragraph)

    return {
        "xml": ElementTree.tostring(root, encoding="utf-8", xml_declaration=True),
        "inserted_after_anchor": False,
        "matched_anchor": None,
    }


def _insert_profile_sections_to_section(
    section_xml: str,
    profile_sections: list[dict[str, Any]],
) -> dict[str, Any]:
    _register_namespaces(section_xml)
    root = ElementTree.fromstring(section_xml)
    inserted_count = 0
    matched_count = 0
    section_results: list[dict[str, Any]] = []

    for profile_section in profile_sections:
        lines = profile_section["lines"]
        anchor_candidates = profile_section["anchor_candidates"]
        anchor = _find_anchor_paragraph(root, anchor_candidates)
        if anchor is None:
            section_results.append(
                {
                    "status": "anchor_not_found",
                    "matched_anchor": None,
                    "inserted_paragraph_count": 0,
                    "anchor_candidates": anchor_candidates,
                }
            )
            continue

        parent, anchor_index, anchor_paragraph, matched_anchor = anchor
        paragraph_template = _select_insertion_paragraph_template(root, anchor_paragraph)
        insert_index = anchor_index + 1
        for line in lines:
            paragraph = _build_text_paragraph(paragraph_template, line)
            parent.insert(insert_index, paragraph)
            insert_index += 1
            inserted_count += 1
        matched_count += 1
        section_results.append(
            {
                "status": "inserted",
                "matched_anchor": matched_anchor,
                "inserted_paragraph_count": len(lines),
                "anchor_candidates": anchor_candidates,
            }
        )

    if inserted_count == 0:
        fallback_lines = [line for section in profile_sections for line in section["lines"]]
        fallback = _insert_draft_lines_to_section(section_xml, fallback_lines, [])
        return {
            "xml": fallback["xml"],
            "inserted_paragraph_count": len(fallback_lines),
            "matched_anchor_count": 0,
            "section_results": section_results,
        }

    return {
        "xml": ElementTree.tostring(root, encoding="utf-8", xml_declaration=True),
        "inserted_paragraph_count": inserted_count,
        "matched_anchor_count": matched_count,
        "section_results": section_results,
    }


def _find_anchor_paragraph(
    root: ElementTree.Element,
    anchor_candidates: list[str],
) -> tuple[ElementTree.Element, int, ElementTree.Element, str] | None:
    anchors = [_safe_line(anchor) for anchor in anchor_candidates if _safe_line(anchor)]
    if not anchors:
        return None

    root_match = _find_anchor_in_children(root, anchors)
    if root_match is not None:
        return root_match

    for parent in root.iter():
        match = _find_anchor_in_children(parent, anchors)
        if match is not None:
            return match
    return None


def _find_anchor_in_children(
    parent: ElementTree.Element,
    anchors: list[str],
) -> tuple[ElementTree.Element, int, ElementTree.Element, str] | None:
    children = list(parent)
    for index, child in enumerate(children):
        if _local_name(child.tag) != "p":
            continue
        paragraph_text = _paragraph_text(child)
        for anchor in anchors:
            if anchor in paragraph_text:
                return parent, index, child, anchor
    return None


def _find_paragraph_template(root: ElementTree.Element) -> ElementTree.Element | None:
    for child in root:
        if _is_safe_text_paragraph(child):
            return child
    for element in root.iter():
        if _is_safe_text_paragraph(element):
            return element
    for child in root:
        if _local_name(child.tag) == "p":
            return child
    for element in root.iter():
        if _local_name(element.tag) == "p":
            return element
    return None


def _select_insertion_paragraph_template(
    root: ElementTree.Element,
    preferred: ElementTree.Element,
) -> ElementTree.Element:
    if _is_safe_text_paragraph(preferred):
        return preferred
    fallback = _find_paragraph_template(root)
    if fallback is not None:
        return fallback
    return preferred


def _is_safe_text_paragraph(paragraph: ElementTree.Element) -> bool:
    if _local_name(paragraph.tag) != "p":
        return False
    has_text = False
    paragraph_count = 0
    for element in paragraph.iter():
        local_name = _local_name(element.tag)
        if local_name == "tbl":
            return False
        if local_name == "p":
            paragraph_count += 1
        if local_name == "t":
            has_text = True
    return has_text and paragraph_count == 1


def _build_text_paragraph(paragraph_template: ElementTree.Element, value: str) -> ElementTree.Element:
    paragraph = copy.deepcopy(paragraph_template)
    _remove_nested_tables(paragraph)
    _set_paragraph_text(paragraph, value)
    return paragraph


def _remove_nested_tables(paragraph: ElementTree.Element) -> None:
    parent_map = {child: parent for parent in paragraph.iter() for child in parent}
    for element in list(paragraph.iter()):
        if _local_name(element.tag) != "tbl":
            continue
        parent = parent_map.get(element)
        if parent is not None:
            parent.remove(element)


def _set_paragraph_text(paragraph: ElementTree.Element, value: str) -> None:
    text_nodes = [element for element in paragraph.iter() if _local_name(element.tag) == "t"]
    if not text_nodes:
        return

    text_nodes[0].text = value
    for node in text_nodes[1:]:
        node.text = ""


def _paragraph_text(paragraph: ElementTree.Element) -> str:
    return "".join(
        text_node.text or ""
        for text_node in paragraph.iter()
        if _local_name(text_node.tag) == "t"
    ).strip()


def _register_namespaces(xml_text: str) -> None:
    for prefix, uri in re.findall(r'xmlns:([^=]+)="([^"]+)"', xml_text):
        ElementTree.register_namespace(prefix, uri)


def _local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1] if "}" in tag else tag


def _is_hwpx_template_available(template_path: Path) -> bool:
    return template_path.exists() and template_path.is_file() and template_path.suffix.lower() == ".hwpx"


def _safe_line(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def _safe_profile_sections(profile_sections: list[dict[str, Any]]) -> list[dict[str, Any]]:
    safe_sections: list[dict[str, Any]] = []
    for section in profile_sections:
        anchors = [_safe_line(anchor) for anchor in section.get("anchor_candidates", [])]
        lines = [_safe_line(line) for line in section.get("lines", [])]
        anchors = [anchor for anchor in anchors if anchor]
        lines = [line for line in lines if line]
        if anchors and lines:
            safe_sections.append({"anchor_candidates": anchors, "lines": lines})
    return safe_sections


def _display_path(path: Path) -> str:
    return path.name
