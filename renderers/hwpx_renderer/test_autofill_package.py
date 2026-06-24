from __future__ import annotations

import tempfile
import unittest
import zipfile
from pathlib import Path

from autofill_package import render_autofill_draft_to_hwpx, render_autofill_sections_to_hwpx
from render_autofill_sample_poc import (
    DEFAULT_ANCHOR_CANDIDATES,
    build_draft_lines,
    build_sample_profile_sections,
)
from render_autofill_batch_poc import build_batch_jobs, parse_args as parse_batch_args
from render_autofill_regression_poc import DEFAULT_REGRESSION_TOPICS, build_regression_jobs


class AutofillPackageTest(unittest.TestCase):
    def test_appends_deidentified_draft_lines_to_placeholder_free_hwpx(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            template_path = Path(temp_dir) / "placeholder_free.hwpx"
            output_path = Path(temp_dir) / "filled.hwpx"
            section_xml = (
                '<?xml version="1.0" encoding="UTF-8"?>'
                '<hp:sec xmlns:hp="http://www.hancom.co.kr/hwpml/2011/paragraph">'
                '<hp:p><hp:run><hp:t>template heading</hp:t></hp:run></hp:p>'
                "</hp:sec>"
            )
            with zipfile.ZipFile(template_path, "w") as package:
                package.writestr("mimetype", "application/hwp+zip")
                package.writestr("Contents/section0.xml", section_xml)
                package.writestr("Preview/PrvText.txt", "preview text must not be copied")

            result = render_autofill_draft_to_hwpx(
                template_path,
                output_path,
                ["[제목] 안전 점검 보고", "- 추진 배경: [확인 필요]"],
            )

            self.assertEqual(result["status"], "rendered")
            self.assertEqual(result["inserted_paragraph_count"], 2)
            self.assertTrue(output_path.exists())

            with zipfile.ZipFile(output_path) as package:
                rendered_section = package.read("Contents/section0.xml").decode("utf-8")

            self.assertIn("[제목] 안전 점검 보고", rendered_section)
            self.assertIn("- 추진 배경: [확인 필요]", rendered_section)
            self.assertNotIn("preview text must not be copied", str(result))

    def test_inserts_deidentified_draft_after_matching_anchor(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            template_path = Path(temp_dir) / "anchored.hwpx"
            output_path = Path(temp_dir) / "filled.hwpx"
            section_xml = (
                '<?xml version="1.0" encoding="UTF-8"?>'
                '<hp:sec xmlns:hp="http://www.hancom.co.kr/hwpml/2011/paragraph">'
                '<hp:p><hp:run><hp:t>머리말</hp:t></hp:run></hp:p>'
                '<hp:p><hp:run><hp:t>1. 보고 개요</hp:t></hp:run></hp:p>'
                '<hp:p><hp:run><hp:t>2. 기존 후속 항목</hp:t></hp:run></hp:p>'
                "</hp:sec>"
            )
            with zipfile.ZipFile(template_path, "w") as package:
                package.writestr("mimetype", "application/hwp+zip")
                package.writestr("Contents/section0.xml", section_xml)

            result = render_autofill_draft_to_hwpx(
                template_path,
                output_path,
                ["[삽입] 보고 개요 초안"],
                anchor_candidates=["보고 개요"],
            )

            self.assertEqual(result["status"], "rendered")
            self.assertTrue(result["inserted_after_anchor"])
            self.assertEqual(result["matched_anchor"], "보고 개요")

            with zipfile.ZipFile(output_path) as package:
                rendered_section = package.read("Contents/section0.xml").decode("utf-8")

            self.assertLess(
                rendered_section.index("1. 보고 개요"),
                rendered_section.index("[삽입] 보고 개요 초안"),
            )
            self.assertLess(
                rendered_section.index("[삽입] 보고 개요 초안"),
                rendered_section.index("2. 기존 후속 항목"),
            )

    def test_default_anchor_candidates_match_sample_summary_heading(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            template_path = Path(temp_dir) / "sample_summary.hwpx"
            output_path = Path(temp_dir) / "filled.hwpx"
            section_xml = (
                '<?xml version="1.0" encoding="UTF-8"?>'
                '<hp:sec xmlns:hp="http://www.hancom.co.kr/hwpml/2011/paragraph">'
                '<hp:p><hp:run><hp:t>OOO 신사업 보고서</hp:t></hp:run></hp:p>'
                '<hp:p><hp:run><hp:t>개요 or 목적</hp:t></hp:run></hp:p>'
                '<hp:p><hp:run><hp:t>추진방안 or 본문</hp:t></hp:run></hp:p>'
                "</hp:sec>"
            )
            with zipfile.ZipFile(template_path, "w") as package:
                package.writestr("mimetype", "application/hwp+zip")
                package.writestr("Contents/section0.xml", section_xml)

            result = render_autofill_draft_to_hwpx(
                template_path,
                output_path,
                ["[삽입] 개요 초안"],
                anchor_candidates=DEFAULT_ANCHOR_CANDIDATES,
            )

            self.assertTrue(result["inserted_after_anchor"])
            self.assertEqual(result["matched_anchor"], "개요")

    def test_anchor_insertion_does_not_duplicate_nested_tables(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            template_path = Path(temp_dir) / "nested_table_anchor.hwpx"
            output_path = Path(temp_dir) / "filled.hwpx"
            section_xml = (
                '<?xml version="1.0" encoding="UTF-8"?>'
                '<hp:sec xmlns:hp="http://www.hancom.co.kr/hwpml/2011/paragraph">'
                '<hp:p><hp:run><hp:t>simple text style</hp:t></hp:run></hp:p>'
                '<hp:p><hp:run><hp:t>사업 개요</hp:t></hp:run>'
                '<hp:tbl><hp:tr><hp:tc><hp:p><hp:run><hp:t>nested table text</hp:t></hp:run></hp:p></hp:tc></hp:tr></hp:tbl>'
                "</hp:p>"
                "</hp:sec>"
            )
            with zipfile.ZipFile(template_path, "w") as package:
                package.writestr("mimetype", "application/hwp+zip")
                package.writestr("Contents/section0.xml", section_xml)

            result = render_autofill_draft_to_hwpx(
                template_path,
                output_path,
                ["[삽입] 표 복제 방지"],
                anchor_candidates=["사업 개요"],
            )

            self.assertTrue(result["inserted_after_anchor"])
            with zipfile.ZipFile(output_path) as package:
                rendered_section = package.read("Contents/section0.xml").decode("utf-8")

            self.assertEqual(rendered_section.count("<hp:tbl"), 1)
            self.assertEqual(rendered_section.count("nested table text"), 1)
            self.assertIn("[삽입] 표 복제 방지", rendered_section)

    def test_inserts_profile_sections_after_each_matching_anchor(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            template_path = Path(temp_dir) / "profile_sections.hwpx"
            output_path = Path(temp_dir) / "filled.hwpx"
            section_xml = (
                '<?xml version="1.0" encoding="UTF-8"?>'
                '<hp:sec xmlns:hp="http://www.hancom.co.kr/hwpml/2011/paragraph">'
                '<hp:p><hp:run><hp:t>개요 or 목적</hp:t></hp:run></hp:p>'
                '<hp:p><hp:run><hp:t>기존 개요 후속</hp:t></hp:run></hp:p>'
                '<hp:p><hp:run><hp:t>추진방안 or 본문</hp:t></hp:run></hp:p>'
                '<hp:p><hp:run><hp:t>기존 본문 후속</hp:t></hp:run></hp:p>'
                "</hp:sec>"
            )
            with zipfile.ZipFile(template_path, "w") as package:
                package.writestr("mimetype", "application/hwp+zip")
                package.writestr("Contents/section0.xml", section_xml)

            result = render_autofill_sections_to_hwpx(
                template_path,
                output_path,
                [
                    {"anchor_candidates": ["개요"], "lines": ["[개요] 목적: [확인 필요]"]},
                    {"anchor_candidates": ["추진방안"], "lines": ["[본문] 추진방안: [확인 필요]"]},
                ],
            )

            self.assertEqual(result["status"], "rendered")
            self.assertEqual(result["inserted_paragraph_count"], 2)
            self.assertEqual(result["matched_anchor_count"], 2)
            with zipfile.ZipFile(output_path) as package:
                rendered_section = package.read("Contents/section0.xml").decode("utf-8")

            self.assertLess(rendered_section.index("개요 or 목적"), rendered_section.index("[개요]"))
            self.assertLess(rendered_section.index("[개요]"), rendered_section.index("기존 개요 후속"))
            self.assertLess(rendered_section.index("추진방안 or 본문"), rendered_section.index("[본문]"))
            self.assertLess(rendered_section.index("[본문]"), rendered_section.index("기존 본문 후속"))

    def test_profile_section_can_use_last_matching_anchor_to_skip_toc(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            template_path = Path(temp_dir) / "duplicate_anchors.hwpx"
            output_path = Path(temp_dir) / "filled.hwpx"
            section_xml = (
                '<?xml version="1.0" encoding="UTF-8"?>'
                '<hp:sec xmlns:hp="http://www.hancom.co.kr/hwpml/2011/paragraph">'
                '<hp:p><hp:run><hp:t>목차</hp:t></hp:run></hp:p>'
                '<hp:p><hp:run><hp:t>사업 개요</hp:t></hp:run></hp:p>'
                '<hp:p><hp:run><hp:t>중간 내용</hp:t></hp:run></hp:p>'
                '<hp:p><hp:run><hp:t>사업 개요</hp:t></hp:run></hp:p>'
                '<hp:p><hp:run><hp:t>실제 본문 다음</hp:t></hp:run></hp:p>'
                "</hp:sec>"
            )
            with zipfile.ZipFile(template_path, "w") as package:
                package.writestr("mimetype", "application/hwp+zip")
                package.writestr("Contents/section0.xml", section_xml)

            result = render_autofill_sections_to_hwpx(
                template_path,
                output_path,
                [
                    {
                        "anchor_candidates": ["사업 개요"],
                        "match_policy": "last",
                        "lines": ["[본문] 목차가 아닌 본문 뒤 삽입"],
                    },
                ],
            )

            self.assertEqual(result["status"], "rendered")
            with zipfile.ZipFile(output_path) as package:
                rendered_section = package.read("Contents/section0.xml").decode("utf-8")

            first_anchor_index = rendered_section.index("사업 개요")
            insert_index = rendered_section.index("[본문] 목차가 아닌 본문 뒤 삽입")
            second_anchor_index = rendered_section.rindex("사업 개요", 0, insert_index)
            self.assertGreater(second_anchor_index, first_anchor_index)
            self.assertLess(insert_index, rendered_section.index("실제 본문 다음"))

    def test_anchor_insert_prefers_next_safe_paragraph_style(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            template_path = Path(temp_dir) / "next_style.hwpx"
            output_path = Path(temp_dir) / "filled.hwpx"
            section_xml = (
                '<?xml version="1.0" encoding="UTF-8"?>'
                '<hp:sec xmlns:hp="http://www.hancom.co.kr/hwpml/2011/paragraph">'
                '<hp:p style="heading"><hp:run><hp:t>사업 개요</hp:t></hp:run></hp:p>'
                '<hp:p style="body"><hp:run><hp:t>기존 본문</hp:t></hp:run></hp:p>'
                "</hp:sec>"
            )
            with zipfile.ZipFile(template_path, "w") as package:
                package.writestr("mimetype", "application/hwp+zip")
                package.writestr("Contents/section0.xml", section_xml)

            result = render_autofill_sections_to_hwpx(
                template_path,
                output_path,
                [{"anchor_candidates": ["사업 개요"], "lines": ["[삽입] 본문 스타일"]}],
            )

            self.assertEqual(result["status"], "rendered")
            with zipfile.ZipFile(output_path) as package:
                rendered_section = package.read("Contents/section0.xml").decode("utf-8")

            inserted_index = rendered_section.index("[삽입] 본문 스타일")
            style_index = rendered_section.rindex('style="body"', 0, inserted_index)
            self.assertGreater(style_index, rendered_section.index("사업 개요"))

    def test_dash_line_insert_prefers_dash_paragraph_style_after_anchor(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            template_path = Path(temp_dir) / "dash_style.hwpx"
            output_path = Path(temp_dir) / "filled.hwpx"
            section_xml = (
                '<?xml version="1.0" encoding="UTF-8"?>'
                '<hp:sec xmlns:hp="http://www.hancom.co.kr/hwpml/2011/paragraph">'
                '<hp:p style="title"><hp:run><hp:t>사업 개요</hp:t></hp:run></hp:p>'
                '<hp:p style="heading"><hp:run><hp:t>□ 헤드라인M 폰트_15 POINT</hp:t></hp:run></hp:p>'
                '<hp:p style="body"><hp:run><hp:t>○ 휴먼명조 폰트_14 POINT</hp:t></hp:run></hp:p>'
                '<hp:p style="dash"><hp:run><hp:t>- 휴먼명조 폰트_14 POINT</hp:t></hp:run></hp:p>'
                "</hp:sec>"
            )
            with zipfile.ZipFile(template_path, "w") as package:
                package.writestr("mimetype", "application/hwp+zip")
                package.writestr("Contents/section0.xml", section_xml)

            result = render_autofill_sections_to_hwpx(
                template_path,
                output_path,
                [{"anchor_candidates": ["사업 개요"], "lines": ["- 목적: [확인 필요]"]}],
            )

            self.assertEqual(result["status"], "rendered")
            with zipfile.ZipFile(output_path) as package:
                rendered_section = package.read("Contents/section0.xml").decode("utf-8")

            inserted_index = rendered_section.index("- 목적: [확인 필요]")
            style_index = rendered_section.rindex('style="dash"', 0, inserted_index)
            self.assertGreater(style_index, rendered_section.index("사업 개요"))

    def test_returns_template_required_for_missing_template(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            result = render_autofill_draft_to_hwpx(
                Path(temp_dir) / "missing.hwpx",
                Path(temp_dir) / "filled.hwpx",
                ["[제목] 안전 점검 보고"],
            )

            self.assertEqual(result["status"], "template_required")
            self.assertEqual(result["inserted_paragraph_count"], 0)

    def test_builds_deidentified_draft_without_confirmed_values(self) -> None:
        draft_lines = build_draft_lines("시설 안전 점검")
        draft_text = "\n".join(draft_lines)

        self.assertIn("[제목] 시설 안전 점검 검토 보고", draft_text)
        self.assertIn("[확인 필요]", draft_text)
        self.assertNotRegex(draft_text, r"\d+\s*(명|개|건|원)")
        self.assertNotIn("담당자:", draft_text)

    def test_builds_summary_sample_profile_sections(self) -> None:
        sections = build_sample_profile_sections("시설 안전 점검", "보고서 기반 양식(요약).hwpx")

        self.assertGreaterEqual(len(sections), 5)
        self.assertEqual(sections[0]["anchor_candidates"][0], "개요")
        self.assertIn("추진방안", sections[1]["anchor_candidates"])
        self.assertTrue(any("사업예산" in section["anchor_candidates"] for section in sections))
        self.assertTrue(any("[확인 필요]" in "\n".join(section["lines"]) for section in sections))

    def test_summary_sample_profile_lines_do_not_duplicate_bullet_marker(self) -> None:
        sections = build_sample_profile_sections("시설 안전 점검", "보고서 기반 양식(요약).hwpx")
        lines = [line for section in sections for line in section["lines"]]

        self.assertTrue(lines)
        self.assertTrue(all(not line.startswith("-") for line in lines))

    def test_summary_sample_profile_uses_optional_user_fields_without_bullet_duplication(self) -> None:
        sections = build_sample_profile_sections(
            "시설 안전 점검",
            "보고서 기반 양식(요약).hwpx",
            {
                "purpose": "현장 점검 준비사항 정리",
                "target": "비식별 점검 대상",
                "period": "상반기",
                "cooperation": "관련 부서 일정 확인",
            },
        )
        lines = [line for section in sections for line in section["lines"]]

        self.assertIn("목적: 현장 점검 준비사항 정리", lines)
        self.assertIn("대상: 비식별 점검 대상", lines)
        self.assertIn("기간: 상반기", lines)
        self.assertIn("협조 필요사항: 관련 부서 일정 확인", lines)
        self.assertTrue(all(not line.startswith("-") for line in lines))

    def test_builds_basic_sample_profile_sections_with_last_anchor_policy(self) -> None:
        sections = build_sample_profile_sections("시설 안전 점검", "보고서 기본 양식.hwpx")

        self.assertTrue(sections)
        self.assertTrue(all(section.get("match_policy") == "last" for section in sections))

    def test_basic_sample_profile_uses_optional_user_fields_with_dash_style(self) -> None:
        sections = build_sample_profile_sections(
            "시설 안전 점검",
            "보고서 기본 양식.hwpx",
            {
                "purpose": "현장 점검 준비사항 정리",
                "background": "점검 기준 정비 필요",
                "scope": "비식별 점검 대상",
            },
        )
        lines = [line for section in sections for line in section["lines"]]

        self.assertIn("- 목적: 현장 점검 준비사항 정리", lines)
        self.assertIn("- 추진 배경: 점검 기준 정비 필요", lines)
        self.assertIn("- 적용 범위: 비식별 점검 대상", lines)

    def test_builds_basic_sample_profile_sections_with_body_anchor_variants(self) -> None:
        sections = build_sample_profile_sections("시설 안전 점검", "보고서 기본 양식.hwpx")
        anchor_groups = [section["anchor_candidates"] for section in sections]

        self.assertTrue(any("평가 요소" in anchors for anchors in anchor_groups))
        self.assertTrue(any("평가 요소 및 방법" in anchors for anchors in anchor_groups))
        self.assertTrue(any("보안 관리" in anchors for anchors in anchor_groups))

    def test_builds_batch_jobs_for_both_primary_samples(self) -> None:
        jobs = build_batch_jobs(Path("samples"), Path("output"), "all")

        self.assertEqual([job["sample"] for job in jobs], ["1", "2"])
        self.assertEqual(Path(jobs[0]["template"]).name, "(샘플양식1) 보고서 기본 양식.hwpx")
        self.assertEqual(Path(jobs[1]["template"]).name, "(샘플양식2) 보고서 기반 양식(요약).hwpx")
        self.assertEqual(Path(jobs[0]["output"]).name, "autofill_profile_sample1_latest.hwpx")
        self.assertEqual(Path(jobs[1]["output"]).name, "autofill_profile_sample2_latest.hwpx")

    def test_batch_parser_accepts_positional_topic_for_simple_use(self) -> None:
        args = parse_batch_args(["시설 안전 점검"])

        self.assertEqual(args.topic, "시설 안전 점검")
        self.assertEqual(args.sample, "all")

    def test_batch_parser_accepts_optional_user_fields(self) -> None:
        args = parse_batch_args(
            [
                "시설 안전 점검",
                "--purpose",
                "현장 점검 준비사항 정리",
                "--target",
                "비식별 점검 대상",
                "--period",
                "상반기",
                "--cooperation",
                "관련 부서 일정 확인",
            ]
        )

        self.assertEqual(args.profile_fields["purpose"], "현장 점검 준비사항 정리")
        self.assertEqual(args.profile_fields["target"], "비식별 점검 대상")
        self.assertEqual(args.profile_fields["period"], "상반기")
        self.assertEqual(args.profile_fields["cooperation"], "관련 부서 일정 확인")

    def test_builds_regression_jobs_for_default_topics_and_samples(self) -> None:
        jobs = build_regression_jobs(Path("samples"), Path("output"))

        self.assertEqual(len(jobs), len(DEFAULT_REGRESSION_TOPICS) * 2)
        self.assertEqual(jobs[0]["topic_index"], 1)
        self.assertEqual(jobs[0]["sample"], "1")
        self.assertEqual(Path(jobs[0]["output"]).parent.name, "topic01")
        self.assertEqual(Path(jobs[1]["output"]).parent.name, "topic01")
        self.assertEqual(Path(jobs[2]["output"]).parent.name, "topic02")


if __name__ == "__main__":
    unittest.main()
