"""Markdown preview templates for placeholder-based renderer samples."""

from __future__ import annotations

from typing import Any


DEFAULT_VALUE = "[확인 필요]"


def value_or_default(value: Any) -> str:
    if value is None or value == "":
        return DEFAULT_VALUE
    return str(value)


def first_document(data: dict[str, Any]) -> dict[str, Any]:
    documents = data.get("documents")
    if isinstance(documents, list) and documents and isinstance(documents[0], dict):
        return documents[0]
    return {}


def render_missing_fields(data: dict[str, Any]) -> str:
    missing_fields = data.get("missing_fields") or []
    lines = ["## 확인 필요 사항"]
    if not missing_fields:
        lines.append("- 없음")
    for item in missing_fields:
        if isinstance(item, dict):
            field = value_or_default(item.get("field_name"))
            reason = value_or_default(item.get("reason"))
            placeholder = value_or_default(item.get("suggested_placeholder"))
            lines.append(f"- {field}: {reason} / {placeholder}")
        else:
            lines.append(f"- {value_or_default(item)}")
    return "\n".join(lines)


def render_security_review(data: dict[str, Any]) -> str:
    security_review = data.get("security_review") or {}
    lines = ["## 보안 점검"]
    if not isinstance(security_review, dict) or not security_review:
        lines.append("- [확인 필요]")
        return "\n".join(lines)

    lines.append(f"- risk_level: {value_or_default(security_review.get('risk_level'))}")
    lines.append(f"- contains_personal_info: {value_or_default(security_review.get('contains_personal_info'))}")
    lines.append(f"- contains_sensitive_info: {value_or_default(security_review.get('contains_sensitive_info'))}")
    lines.append(f"- contains_internal_info: {value_or_default(security_review.get('contains_internal_info'))}")
    lines.append(f"- notes: {value_or_default(security_review.get('notes'))}")
    return "\n".join(lines)


def render_common_header(title: str) -> list[str]:
    return [
        "# 자동 생성 검토용 초안",
        "",
        f"## {title}",
        "",
        "이 문서는 실제 외부 발송용이 아니라 검토용 미리보기입니다.",
        "",
        "실제 사용 전 사람이 최종 검토해야 합니다.",
        "",
    ]


def render_checklist(items: Any) -> str:
    lines = ["## 체크리스트"]
    if not items:
        lines.append("- [확인 필요]")
    elif isinstance(items, list):
        for item in items:
            lines.append(f"- {value_or_default(item)}")
    else:
        lines.append(f"- {value_or_default(items)}")
    return "\n".join(lines)


def render_body_sections(sections: Any, depth: int = 0) -> list[str]:
    lines: list[str] = []
    if not isinstance(sections, list) or not sections:
        return ["- [확인 필요]"]
    indent = "  " * depth
    for section in sections:
        if not isinstance(section, dict):
            lines.append(f"{indent}- {value_or_default(section)}")
            continue
        number = value_or_default(section.get("number"))
        content = value_or_default(section.get("content"))
        lines.append(f"{indent}- {number} {content}")
        children = section.get("children")
        if children:
            lines.extend(render_body_sections(children, depth + 1))
    return lines


def render_attachments(attachments: Any) -> str:
    lines = ["## 붙임"]
    if not attachments:
        lines.append("- 없음")
        return "\n".join(lines)
    for item in attachments:
        if isinstance(item, dict):
            number = value_or_default(item.get("number"))
            title = value_or_default(item.get("title"))
            copies = value_or_default(item.get("copies"))
            lines.append(f"- {number} {title} {copies}")
        else:
            lines.append(f"- {value_or_default(item)}")
    return "\n".join(lines)


def render_official_letter_preview(data: dict[str, Any]) -> str:
    document = first_document(data)
    lines = render_common_header("공문 미리보기")
    lines.extend(
        [
            f"- 제목: {value_or_default(document.get('title'))}",
            f"- 문서유형: {value_or_default(document.get('document_type', data.get('document_type')))}",
            f"- 문서번호: {value_or_default(document.get('document_number'))}",
            f"- 시행일자: {value_or_default(document.get('execution_date'))}",
            f"- 수신처: {value_or_default(document.get('recipient'))}",
            "",
            "## 본문",
        ]
    )
    lines.extend(render_body_sections(document.get("body_sections")))
    lines.extend(
        [
            "",
            render_attachments(document.get("attachments")),
            "",
            render_checklist(document.get("checklist") or data.get("checklist")),
            "",
            render_missing_fields(data),
            "",
            render_security_review(data),
        ]
    )
    return "\n".join(lines)


def render_project_plan_preview(data: dict[str, Any]) -> str:
    document = first_document(data)
    lines = render_common_header("추진계획서 미리보기")
    lines.extend(
        [
            f"## 추진배경\n{value_or_default(document.get('background'))}",
            f"## 추진목적\n{value_or_default(document.get('purpose'))}",
            "## 추진개요",
        ]
    )
    overview = document.get("overview") or {}
    if isinstance(overview, dict):
        for key, value in overview.items():
            lines.append(f"- {key}: {value_or_default(value)}")
    else:
        lines.append(f"- {value_or_default(overview)}")

    lines.append("## 추진일정")
    schedule = document.get("schedule") or []
    if isinstance(schedule, list) and schedule:
        for item in schedule:
            if isinstance(item, dict):
                lines.append(f"- {value_or_default(item.get('phase'))}: {value_or_default(item.get('period'))} / {value_or_default(item.get('details'))}")
            else:
                lines.append(f"- {value_or_default(item)}")
    else:
        lines.append("- [확인 필요]")

    budget = document.get("budget") or {}
    lines.append("## 소요예산")
    lines.append(f"- total: {value_or_default(budget.get('total') if isinstance(budget, dict) else budget)}")

    lines.extend(
        [
            f"## 기대효과\n{render_list_or_default(document.get('expected_effects'))}",
            f"## 검토사항\n{render_list_or_default(document.get('review_items'))}",
            f"## 향후계획\n{value_or_default(document.get('future_plan'))}",
            render_missing_fields(data),
            render_security_review(data),
        ]
    )
    return "\n\n".join(lines)


def render_vendor_email_preview(data: dict[str, Any]) -> str:
    email = data.get("email_draft") or {}
    lines = render_common_header("업체 메일 미리보기")
    lines.extend(
        [
            f"- 제목: {value_or_default(email.get('subject'))}",
            f"- 목적: {value_or_default(email.get('purpose'))}",
            f"- 회신기한: {value_or_default(email.get('response_deadline'))}",
            "",
            "## 요청사항",
            render_list_or_default(email.get("request_items")),
            "",
            "## 유의사항",
            render_list_or_default(email.get("caution_notes")),
            "",
            "## 서명 placeholder",
        ]
    )
    signature = email.get("signature") or {}
    if isinstance(signature, dict):
        lines.extend([f"- {key}: {value_or_default(value)}" for key, value in signature.items()])
    else:
        lines.append(f"- {value_or_default(signature)}")
    lines.extend(
        [
            "",
            "## 계약 또는 업체 선정 미확정 문구",
            "- 계약 또는 업체 선정이 확정된 사항은 아닙니다.",
            "",
            render_missing_fields(data),
            "",
            render_security_review(data),
        ]
    )
    return "\n".join(lines)


def render_survey_table_preview(data: dict[str, Any]) -> str:
    document = first_document(data)
    lines = render_common_header("조사표 미리보기")
    lines.extend(
        [
            f"- sheet_name: {value_or_default(document.get('sheet_name'))}",
            f"- title: {value_or_default(document.get('title'))}",
            "",
            "## columns",
            render_list_or_default(document.get("columns")),
            "",
            "## rows",
        ]
    )
    rows = document.get("rows") or []
    if isinstance(rows, list) and rows:
        for index, row in enumerate(rows, start=1):
            lines.append(f"### row {index}")
            if isinstance(row, dict):
                for key, value in row.items():
                    lines.append(f"- {key}: {value_or_default(value)}")
            else:
                lines.append(f"- {value_or_default(row)}")
    else:
        lines.append("- [확인 필요]")

    lines.extend(
        [
            "",
            f"## privacy_notice\n{value_or_default(document.get('privacy_notice'))}",
            "",
            render_checklist(document.get("checklist") or data.get("checklist")),
            "",
            render_missing_fields(data),
            "",
            render_security_review(data),
        ]
    )
    return "\n".join(lines)


def render_blocked_report(data: dict[str, Any], reasons: list[str]) -> str:
    security_review = data.get("security_review") or {}
    lines = render_common_header("렌더링 차단 보고")
    lines.extend(
        [
            "## 렌더링 차단 안내",
            "보안 검증 결과 Markdown 미리보기 렌더링이 차단되었습니다.",
            "",
            "## 차단 사유",
            render_list_or_default(reasons),
            "",
            f"## risk_level\n{value_or_default(security_review.get('risk_level') if isinstance(security_review, dict) else None)}",
            "",
            "## blocked_items",
            render_list_or_default(security_review.get("blocked_items") if isinstance(security_review, dict) else None),
            "",
            "## required_review",
            render_list_or_default(security_review.get("required_review") if isinstance(security_review, dict) else None),
            "",
            "## allowed_processing",
            render_list_or_default(security_review.get("allowed_processing") if isinstance(security_review, dict) else None),
            "",
            render_security_review(data),
        ]
    )
    return "\n".join(lines)


def render_list_or_default(items: Any) -> str:
    if not items:
        return "- [확인 필요]"
    if isinstance(items, list):
        if not items:
            return "- [확인 필요]"
        return "\n".join(f"- {value_or_default(item)}" for item in items)
    return f"- {value_or_default(items)}"
