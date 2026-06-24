"""Render a deidentified draft into a placeholder-free HWPX sample template."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from autofill_package import render_autofill_draft_to_hwpx, render_autofill_sections_to_hwpx
from validation import has_forbidden_pattern


REPO_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = Path(__file__).resolve().parent / "output"

DEFAULT_ANCHOR_CANDIDATES = [
    "보고 개요",
    "사업 개요",
    "개요",
    "목적",
    "추진 배경",
    "추진방안",
    "주요 내용",
    "본문",
    "실행방안",
    "검토 의견",
    "요약",
]


def build_draft_lines(topic: str) -> list[str]:
    safe_topic = topic.strip() or "[주제 확인 필요]"
    return [
        f"[제목] {safe_topic} 검토 보고",
        "1. 보고 개요",
        "- 목적: [확인 필요]",
        "- 대상: [확인 필요]",
        "- 기간: [확인 필요]",
        "2. 주요 내용",
        "- 추진 배경: [확인 필요]",
        "- 주요 검토사항: [확인 필요]",
        "- 예상 쟁점: [확인 필요]",
        "3. 검토 의견",
        "- 종합 의견: [확인 필요]",
        "- 후속 조치: [확인 필요]",
        "4. 보안 및 검토",
        "- 실제 개인정보, 실제 기관명, 실제 문서번호는 포함하지 않음",
        "- 최종 발송, 결재, 계약, 예산 집행은 사람이 검토",
    ]


def build_sample_profile_sections(topic: str, template_name: str) -> list[dict[str, list[str]]]:
    safe_topic = topic.strip() or "[주제 확인 필요]"
    if "요약" in template_name:
        return [
            {
                "anchor_candidates": ["개요", "목적", "개요 or 목적"],
                "lines": [
                    f"- 목적: {safe_topic} 관련 검토 방향 정리",
                    "- 대상: [확인 필요]",
                    "- 기간: [확인 필요]",
                ],
            },
            {
                "anchor_candidates": ["추진방안", "본문", "추진방안 or 본문"],
                "lines": [
                    "- 추진방안 1: 현황 및 요구사항 확인",
                    "- 추진방안 2: 관련 부서 의견 수렴",
                    "- 추진방안 3: 후속 일정 및 검토 기준 정리",
                ],
            },
            {
                "anchor_candidates": ["실행방안"],
                "lines": [
                    "- 실행 절차: [확인 필요]",
                    "- 검토 담당: [확인 필요]",
                ],
            },
            {
                "anchor_candidates": ["사업예산", "예산"],
                "lines": [
                    "- 소요예산: [확인 필요]",
                    "- 산출근거: [확인 필요]",
                ],
            },
            {
                "anchor_candidates": ["기타사항", "협조사항", "기타사항 or 협조사항"],
                "lines": [
                    "- 협조 필요사항: [확인 필요]",
                    "- 보안 검토: 실제 개인정보, 실제 기관명, 실제 문서번호 제외",
                ],
            },
        ]

    return [
        {
            "anchor_candidates": ["사업 개요", "Ⅰ. 사업 개요"],
            "lines": [
                f"- 목적: {safe_topic} 관련 기본 방향 정리",
                "- 추진 배경: [확인 필요]",
                "- 적용 범위: [확인 필요]",
            ],
        },
        {
            "anchor_candidates": ["요구 사항", "Ⅱ. 요구 사항"],
            "lines": [
                "- 일반 요구사항: [확인 필요]",
                "- 세부 요구사항: [확인 필요]",
            ],
        },
        {
            "anchor_candidates": ["계약 사항", "Ⅲ. 계약 사항"],
            "lines": [
                "- 계약 관련 검토사항: [확인 필요]",
                "- 사람 검토 필요: 계약, 선정, 예산 집행 확정 금지",
            ],
        },
        {
            "anchor_candidates": ["평가요소", "평가 방법", "Ⅳ. 평가요소"],
            "lines": [
                "- 평가 기준: [확인 필요]",
                "- 평가 방식: [확인 필요]",
            ],
        },
        {
            "anchor_candidates": ["보안관리", "Ⅵ. 보안관리"],
            "lines": [
                "- 보안 원칙: 실제 개인정보, 실제 기관명, 실제 문서번호 제외",
                "- 외부 처리 제한: 실제 원문 사용 금지",
            ],
        },
    ]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fill a placeholder-free HWPX sample with a deidentified draft.",
    )
    parser.add_argument("--template", type=Path, required=True, help="HWPX sample template path.")
    parser.add_argument("--topic", required=True, help="Deidentified draft topic.")
    parser.add_argument(
        "--output",
        type=Path,
        default=OUTPUT_DIR / "autofill_sample_poc.hwpx",
        help="Output HWPX path. Default is ignored renderer output.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    reasons = has_forbidden_pattern(args.topic)
    if reasons:
        print("autofill_blocked")
        for reason in reasons:
            print(f"- {reason}")
        raise SystemExit(2)

    output_path = args.output
    if not output_path.is_absolute():
        output_path = REPO_ROOT / output_path

    profile_sections = build_sample_profile_sections(args.topic, args.template.name)
    result = render_autofill_sections_to_hwpx(
        args.template,
        output_path,
        profile_sections,
    )

    print(f"status: {result['status']}")
    print(f"template: {result['template_path']}")
    print(f"output: {result['output_path']}")
    print(f"inserted_paragraph_count: {result['inserted_paragraph_count']}")
    print(f"matched_anchor_count: {result['matched_anchor_count']}")
    if result.get("processed_section"):
        print(f"processed_section: {result['processed_section']}")
    for section_result in result.get("section_results", []):
        matched_anchor = section_result.get("matched_anchor") or "none"
        print(
            f"section: {section_result['status']} "
            f"anchor={matched_anchor} inserted={section_result['inserted_paragraph_count']}"
        )
    for error in result.get("errors", []):
        print(f"- {error}")


if __name__ == "__main__":
    main()
