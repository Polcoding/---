"""Run the HWPX minimal PoC renderer for placeholder JSON samples."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from template_package import (
    build_placeholder_map,
    is_hwpx_template_available,
    replace_placeholders_in_hwpx,
    write_template_required_report,
)
from validation import validate_for_hwpx_rendering


REPO_ROOT = Path(__file__).resolve().parents[2]
INPUT_DIR = REPO_ROOT / "examples" / "json"
TEMPLATE_DIR = REPO_ROOT / "templates" / "hwpx"
OUTPUT_DIR = Path(__file__).resolve().parent / "output"

SUMMARY_OUTPUT = "hwpx_render_summary.json"
TEMPLATE_REQUIRED_REPORT = "template_required_report.md"

SAMPLES = [
    {
        "input": "sample_one_page_report.json",
        "template": "placeholder_one_page_report.hwpx",
        "output": "sample_one_page_report_poc.hwpx",
    },
    {
        "input": "sample_official_letter.json",
        "template": "placeholder_official_letter.hwpx",
        "output": "sample_official_letter_poc.hwpx",
    },
    {
        "input": "sample_project_plan.json",
        "template": "placeholder_project_plan.hwpx",
        "output": "sample_project_plan_poc.hwpx",
    },
    {
        "input": "sample_result_report.json",
        "template": "placeholder_result_report.hwpx",
        "output": "sample_result_report_poc.hwpx",
    },
    {
        "input": "sample_review_report.json",
        "template": "placeholder_review_report.hwpx",
        "output": "sample_review_report_poc.hwpx",
    },
]


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def write_json(path: Path, data: Any) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    fallback_path = path.with_name(f"{path.stem}_latest{path.suffix}")
    for candidate_path in (path, fallback_path):
        try:
            candidate_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
            return candidate_path
        except PermissionError:
            continue

    if path.exists():
        return path
    raise PermissionError(f"JSON 파일을 쓸 수 없습니다: {path}")


def write_blocked_report(input_name: str, reasons: list[str]) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / f"{Path(input_name).stem}_blocked.md"
    lines = [
        "# HWPX 렌더링 차단 보고",
        "",
        "## 상태",
        "",
        "보안 검증 결과에 따라 HWPX 렌더링을 중단했습니다.",
        "",
        "## 입력",
        "",
        f"- {input_name}",
        "",
        "## 차단 사유",
        "",
    ]
    lines.extend(f"- {reason}" for reason in reasons)
    lines.extend(
        [
            "",
            "## 조치 필요",
            "",
            "- 실제 개인정보, 내부 운영정보, 민감정보가 없는 placeholder 기반 입력만 사용합니다.",
            "- 실제 기관 HWPX 양식 원본은 사용하지 않습니다.",
            "",
        ]
    )
    output_path.write_text("\n".join(lines), encoding="utf-8")
    return output_path


def summarize_paragraph_placeholders(placeholder_map: dict[str, str]) -> dict[str, Any]:
    body_keys = [
        "{{body_section_1}}",
        "{{body_section_2}}",
        "{{body_section_3}}",
    ]
    child_keys = [
        "{{body_section_1_child_1}}",
        "{{body_section_2_child_1}}",
        "{{body_section_2_child_2}}",
    ]

    return {
        "body_section_placeholder_count": sum(
            1 for key in body_keys if _has_rendered_paragraph_value(placeholder_map.get(key))
        ),
        "child_placeholder_count": sum(1 for key in child_keys if placeholder_map.get(key)),
        "body_sections_fallback_preserved": "{{body_sections}}" in placeholder_map,
    }


def _has_rendered_paragraph_value(value: str | None) -> bool:
    return bool(value) and value != "[확인 필요]"


def render_sample(sample: dict[str, str]) -> dict[str, Any]:
    input_name = sample["input"]
    template_name = sample["template"]
    output_name = sample["output"]

    input_path = INPUT_DIR / input_name
    template_path = TEMPLATE_DIR / template_name
    output_path = OUTPUT_DIR / output_name

    result: dict[str, Any] = {
        "input": str(input_path.relative_to(REPO_ROOT)),
        "template": str(template_path.relative_to(REPO_ROOT)),
        "output": str(output_path.relative_to(REPO_ROOT)),
        "status": "pending",
        "reasons": [],
    }

    data = load_json(input_path)
    is_safe, reasons = validate_for_hwpx_rendering(data)
    if not is_safe:
        report_path = write_blocked_report(input_name, reasons)
        result.update(
            {
                "status": "blocked",
                "reasons": reasons,
                "report": str(report_path.relative_to(REPO_ROOT)),
            }
        )
        return result

    placeholder_map = build_placeholder_map(data)
    result["paragraph_placeholder_summary"] = summarize_paragraph_placeholders(placeholder_map)

    if not is_hwpx_template_available(template_path):
        report_path = write_template_required_report(
            OUTPUT_DIR,
            f"{template_name} 템플릿이 없어 {input_name} 렌더링을 중단했습니다.",
        )
        template_reason = "placeholder HWPX 템플릿 필요"
        result.update(
            {
                "status": "template_required",
                "reasons": [template_reason],
                "report": str(report_path.relative_to(REPO_ROOT)),
            }
        )
        return result

    render_result = replace_placeholders_in_hwpx(template_path, output_path, placeholder_map)
    result.update(render_result)
    return result


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    results = [render_sample(sample) for sample in SAMPLES]

    summary = {
        "renderer": "hwpx_minimal_poc",
        "note": "실제 기관 양식, 실제 공문 원문, 실제 개인정보는 사용하지 않습니다.",
        "results": results,
    }
    summary_path = write_json(OUTPUT_DIR / SUMMARY_OUTPUT, summary)

    print("HWPX 최소 PoC 실행 결과")
    for item in results:
        print(f"- {item['input']}: {item['status']}")
        if item.get("report"):
            print(f"  보고서: {item['report']}")

    print(f"요약: {str(summary_path.relative_to(REPO_ROOT))}")
    print("주의: API 호출, 이메일 자동화, HWPX 새 문서 조립은 수행하지 않았습니다.")


if __name__ == "__main__":
    main()
