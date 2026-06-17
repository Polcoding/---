"""Email draft templates for placeholder-based renderer samples."""

from __future__ import annotations

from typing import Any


DEFAULT_VALUE = "[확인 필요]"


def value_or_default(value: Any) -> str:
    if value is None or value == "":
        return DEFAULT_VALUE
    return str(value)


def render_list_or_default(items: Any, bullet: str = "-") -> str:
    if not items:
        return f"{bullet} {DEFAULT_VALUE}"
    if isinstance(items, list):
        if not items:
            return f"{bullet} {DEFAULT_VALUE}"
        return "\n".join(f"{bullet} {value_or_default(item)}" for item in items)
    return f"{bullet} {value_or_default(items)}"


def render_missing_fields_markdown(data: dict[str, Any]) -> str:
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


def render_missing_fields_text(data: dict[str, Any]) -> str:
    missing_fields = data.get("missing_fields") or []
    lines = ["확인 필요 사항"]
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


def render_security_review_markdown(data: dict[str, Any]) -> str:
    security_review = data.get("security_review") or {}
    lines = ["## 보안 점검"]
    if not isinstance(security_review, dict) or not security_review:
        lines.append("- [확인 필요]")
        return "\n".join(lines)

    lines.append(f"- risk_level: {value_or_default(security_review.get('risk_level'))}")
    lines.append(f"- contains_personal_info: {value_or_default(security_review.get('contains_personal_info'))}")
    lines.append(f"- contains_sensitive_info: {value_or_default(security_review.get('contains_sensitive_info'))}")
    lines.append(f"- contains_internal_info: {value_or_default(security_review.get('contains_internal_info'))}")
    lines.append(f"- required_review: {value_or_default(security_review.get('required_review'))}")
    lines.append(f"- notes: {value_or_default(security_review.get('notes'))}")
    return "\n".join(lines)


def render_security_review_text(data: dict[str, Any]) -> str:
    security_review = data.get("security_review") or {}
    lines = ["보안 점검"]
    if not isinstance(security_review, dict) or not security_review:
        lines.append("- [확인 필요]")
        return "\n".join(lines)

    lines.append(f"- risk_level: {value_or_default(security_review.get('risk_level'))}")
    lines.append(f"- contains_personal_info: {value_or_default(security_review.get('contains_personal_info'))}")
    lines.append(f"- contains_sensitive_info: {value_or_default(security_review.get('contains_sensitive_info'))}")
    lines.append(f"- contains_internal_info: {value_or_default(security_review.get('contains_internal_info'))}")
    lines.append(f"- required_review: {value_or_default(security_review.get('required_review'))}")
    lines.append(f"- notes: {value_or_default(security_review.get('notes'))}")
    return "\n".join(lines)


def render_signature_markdown(signature: Any) -> str:
    lines = ["## 서명 placeholder"]
    if isinstance(signature, dict) and signature:
        lines.extend(f"- {key}: {value_or_default(value)}" for key, value in signature.items())
    else:
        lines.append("- [확인 필요]")
    return "\n".join(lines)


def render_signature_text(signature: Any) -> str:
    lines = ["서명 placeholder"]
    if isinstance(signature, dict) and signature:
        lines.extend(f"- {key}: {value_or_default(value)}" for key, value in signature.items())
    else:
        lines.append("- [확인 필요]")
    return "\n".join(lines)


def render_vendor_email_markdown(data: dict[str, Any]) -> str:
    """Render a vendor email draft as Markdown preview text."""
    email = data.get("email_draft") or {}
    if not isinstance(email, dict):
        email = {}

    lines = [
        "# 검토용 이메일 초안",
        "",
        "이 파일은 실제 이메일 발송이 아니라 사람이 검토하기 위한 초안 파일입니다.",
        "",
        "실제 발송 전 사람이 최종 검토해야 합니다.",
        "",
        f"- 제목: {value_or_default(email.get('subject'))}",
        "- 수신자 placeholder: [수신자 확인 필요]",
        f"- 발신자 placeholder: {value_or_default(email.get('sender'))}",
        "",
        "## 인사말",
        value_or_default(email.get("greeting")),
        "",
        "## 요청 목적",
        value_or_default(email.get("purpose")),
        "",
        "## 요청사항",
        render_list_or_default(email.get("request_items")),
        "",
        f"## 회신기한\n{value_or_default(email.get('response_deadline'))}",
        "",
        f"## 회신방법\n{value_or_default(email.get('response_method'))}",
        "",
        "## 유의사항",
        render_list_or_default(email.get("caution_notes")),
        "",
        "## 계약 또는 업체 선정 미확정 문구",
        "계약 또는 업체 선정이 확정된 사항은 아닙니다.",
        "",
        "## 개인정보ㆍ민감정보 제외 요청 문구",
        "개인정보, 내부자료, 민감정보는 제외하여 회신해 주시기 바랍니다.",
        "",
        render_signature_markdown(email.get("signature")),
        "",
        "## 발송 전 체크리스트",
        render_list_or_default(email.get("checklist") or data.get("checklist")),
        "",
        render_missing_fields_markdown(data),
        "",
        render_security_review_markdown(data),
    ]
    return "\n".join(lines)


def render_vendor_email_text(data: dict[str, Any]) -> str:
    """Render a vendor email draft as plain text preview."""
    email = data.get("email_draft") or {}
    if not isinstance(email, dict):
        email = {}

    lines = [
        "검토용 이메일 초안",
        "",
        "이 파일은 실제 이메일 발송이 아니라 사람이 검토하기 위한 초안 파일입니다.",
        "실제 발송 전 사람이 최종 검토해야 합니다.",
        "",
        f"제목: {value_or_default(email.get('subject'))}",
        "수신자 placeholder: [수신자 확인 필요]",
        f"발신자 placeholder: {value_or_default(email.get('sender'))}",
        "",
        "인사말",
        value_or_default(email.get("greeting")),
        "",
        "요청 목적",
        value_or_default(email.get("purpose")),
        "",
        "요청사항",
        render_list_or_default(email.get("request_items")),
        "",
        f"회신기한: {value_or_default(email.get('response_deadline'))}",
        f"회신방법: {value_or_default(email.get('response_method'))}",
        "",
        "유의사항",
        render_list_or_default(email.get("caution_notes")),
        "",
        "계약 또는 업체 선정 미확정 문구",
        "계약 또는 업체 선정이 확정된 사항은 아닙니다.",
        "",
        "개인정보ㆍ민감정보 제외 요청 문구",
        "개인정보, 내부자료, 민감정보는 제외하여 회신해 주시기 바랍니다.",
        "",
        render_signature_text(email.get("signature")),
        "",
        "발송 전 체크리스트",
        render_list_or_default(email.get("checklist") or data.get("checklist")),
        "",
        render_missing_fields_text(data),
        "",
        render_security_review_text(data),
    ]
    return "\n".join(lines)


def render_blocked_email_report(data: dict[str, Any], reasons: list[str]) -> str:
    """Render a blocked email rendering report."""
    security_review = data.get("security_review") or {}
    if not isinstance(security_review, dict):
        security_review = {}

    lines = [
        "# 검토용 이메일 초안",
        "",
        "## 렌더링 차단 안내",
        "보안 검증 결과 Email 초안 렌더링이 차단되었습니다.",
        "",
        "이 샘플은 실제 이메일 초안으로 렌더링하지 않았습니다.",
        "",
        "실제 발송 전 사람이 최종 검토해야 합니다.",
        "",
        "## 차단 사유",
        render_list_or_default(reasons),
        "",
        f"## risk_level\n{value_or_default(security_review.get('risk_level'))}",
        "",
        "## blocked_items",
        render_list_or_default(security_review.get("blocked_items")),
        "",
        "## required_review",
        render_list_or_default(security_review.get("required_review")),
        "",
        "## allowed_processing",
        render_list_or_default(security_review.get("allowed_processing")),
        "",
        render_security_review_markdown(data),
    ]
    return "\n".join(lines)
