"""Workbook template helpers for the XLSX renderer PoC."""

from __future__ import annotations

from typing import Any

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill, Border, Side
from openpyxl.utils import get_column_letter


HEADER_FILL = PatternFill("solid", fgColor="D9EAF7")
TITLE_FILL = PatternFill("solid", fgColor="E2F0D9")
WARNING_FILL = PatternFill("solid", fgColor="FFF2CC")
THIN_BORDER = Border(
    left=Side(style="thin", color="D9D9D9"),
    right=Side(style="thin", color="D9D9D9"),
    top=Side(style="thin", color="D9D9D9"),
    bottom=Side(style="thin", color="D9D9D9"),
)


def apply_basic_cell_style(cell: Any) -> None:
    cell.alignment = Alignment(vertical="top", wrap_text=True)
    cell.border = THIN_BORDER


def style_header_row(ws: Any, row: int, start_col: int, end_col: int) -> None:
    for col in range(start_col, end_col + 1):
        cell = ws.cell(row=row, column=col)
        cell.fill = HEADER_FILL
        cell.font = Font(bold=True)
        apply_basic_cell_style(cell)


def set_column_widths(ws: Any, widths: list[int]) -> None:
    for index, width in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(index)].width = width


def build_workbook(payload: dict[str, Any]) -> Workbook:
    document = payload["documents"][0]
    wb = Workbook()
    wb.remove(wb.active)

    build_survey_sheet(wb, document)
    build_instructions_sheet(wb, document)
    build_checklist_sheet(wb, document, payload)
    build_meta_sheet(wb, payload)

    return wb


def build_survey_sheet(wb: Workbook, document: dict[str, Any]) -> None:
    ws = wb.create_sheet("조사표")
    set_column_widths(ws, [12, 16, 22, 18, 18, 28, 24])
    ws.merge_cells("A1:G1")
    ws["A1"] = document.get("title", "[제목 확인 필요]")
    ws["A1"].font = Font(bold=True, size=14)
    ws["A1"].fill = TITLE_FILL
    ws["A1"].alignment = Alignment(horizontal="center")

    meta_rows = [
        ("조사 기준일", document.get("standard_date", "[확인 필요]")),
        ("작성 단위", document.get("submitting_unit", "[확인 필요]")),
        ("보안 유의사항", document.get("privacy_notice", "[개인정보 제외 안내 문구]")),
    ]
    for row_index, (label, value) in enumerate(meta_rows, start=3):
        ws.cell(row=row_index, column=1, value=label)
        ws.cell(row=row_index, column=2, value=value)
        ws.cell(row=row_index, column=1).font = Font(bold=True)
        ws.cell(row=row_index, column=1).fill = WARNING_FILL
        apply_basic_cell_style(ws.cell(row=row_index, column=1))
        apply_basic_cell_style(ws.cell(row=row_index, column=2))

    columns = document.get("columns", [])
    header_row = 8
    for col_index, column_name in enumerate(columns, start=1):
        ws.cell(row=header_row, column=col_index, value=column_name)
    style_header_row(ws, header_row, 1, len(columns))

    for row_offset, row_data in enumerate(document.get("rows", []), start=1):
        for col_index, column_name in enumerate(columns, start=1):
            cell = ws.cell(row=header_row + row_offset, column=col_index)
            cell.value = row_data.get(column_name, "[확인 필요]")
            apply_basic_cell_style(cell)

    ws.freeze_panes = "A9"


def build_instructions_sheet(wb: Workbook, document: dict[str, Any]) -> None:
    ws = wb.create_sheet("작성요령")
    set_column_widths(ws, [24, 80])
    rows = [
        ("작성 목적", "[조사 대상] 현황을 placeholder 기반으로 정리합니다."),
        ("작성 기준", document.get("standard_date", "[조사기준일 확인 필요]")),
        ("개인정보 제외 안내", document.get("privacy_notice", "[개인정보 제외 안내 문구]")),
        ("제외 정보", "실제 관서명, 차량번호, 장비명, 수량, 내부 운영정보를 입력하지 않습니다."),
        ("문의처", "[담당부서] / [공용 연락처]"),
    ]
    ws.append(["항목", "내용"])
    style_header_row(ws, 1, 1, 2)
    for item in rows:
        ws.append(list(item))
    for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=1, max_col=2):
        for cell in row:
            apply_basic_cell_style(cell)


def build_checklist_sheet(wb: Workbook, document: dict[str, Any], payload: dict[str, Any]) -> None:
    ws = wb.create_sheet("검수체크리스트")
    set_column_widths(ws, [12, 70])
    ws.append(["확인 여부", "체크 항목"])
    style_header_row(ws, 1, 1, 2)
    for item in document.get("checklist", []) + payload.get("checklist", []):
        ws.append(["[확인 필요]", item])
    for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=1, max_col=2):
        for cell in row:
            apply_basic_cell_style(cell)


def build_meta_sheet(wb: Workbook, payload: dict[str, Any]) -> None:
    ws = wb.create_sheet("메타정보")
    set_column_widths(ws, [28, 80])
    meta = [
        ("request_id", payload.get("request_id", "[확인 필요]")),
        ("document_type", payload.get("document_type", "[확인 필요]")),
        ("draft_status", payload.get("draft_status", "[확인 필요]")),
        ("human_review_required", str(payload.get("human_review_required", True))),
        ("risk_level", payload.get("security_review", {}).get("risk_level", "[확인 필요]")),
        ("source_policy", "placeholder 기반 샘플 JSON만 사용"),
    ]
    ws.append(["항목", "값"])
    style_header_row(ws, 1, 1, 2)
    for row in meta:
        ws.append(list(row))

    ws.append([])
    ws.append(["missing_fields", "suggested_placeholder"])
    style_header_row(ws, ws.max_row, 1, 2)
    for item in payload.get("missing_fields", []):
        ws.append([item.get("field_name", "[확인 필요]"), item.get("suggested_placeholder", "[확인 필요]")])

    for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=1, max_col=2):
        for cell in row:
            apply_basic_cell_style(cell)
