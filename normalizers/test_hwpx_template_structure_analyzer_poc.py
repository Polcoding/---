from __future__ import annotations

import tempfile
import unittest
import zipfile
from pathlib import Path

from hwpx_template_structure_analyzer_poc import analyze_hwpx_template, build_structure_summary


class HwpxTemplateStructureAnalyzerTest(unittest.TestCase):
    def test_analyzes_structure_without_extracting_text(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            hwpx_path = Path(temp_dir) / "placeholder_candidate.hwpx"
            section_xml = (
                '<?xml version="1.0" encoding="UTF-8"?>'
                '<hp:sec xmlns:hp="http://www.hancom.co.kr/hwpml/2011/paragraph">'
                '<hp:p><hp:run><hp:t>{{title}}</hp:t></hp:run></hp:p>'
                '<hp:p><hp:run><hp:t>safe sample</hp:t></hp:run></hp:p>'
                '<hp:tbl><hp:tr><hp:tc><hp:p><hp:t>{{body}}</hp:t></hp:p></hp:tc></hp:tr></hp:tbl>'
                "</hp:sec>"
            )
            with zipfile.ZipFile(hwpx_path, "w") as package:
                package.writestr("mimetype", "application/hwp+zip")
                package.writestr("Contents/section0.xml", section_xml)
                package.writestr("Preview/PrvText.txt", "this text must not be copied")

            result = analyze_hwpx_template(hwpx_path)

            self.assertEqual(result["status"], "analyzed")
            self.assertEqual(result["section_count"], 1)
            self.assertEqual(result["paragraph_count"], 3)
            self.assertEqual(result["text_node_count"], 3)
            self.assertEqual(result["table_count"], 1)
            self.assertEqual(result["placeholder_count"], 2)
            self.assertEqual(result["placeholders"], ["{{body}}", "{{title}}"])
            self.assertTrue(result["has_preview_text"])
            self.assertNotIn("this text must not be copied", str(result))

    def test_returns_safe_status_for_missing_template(self) -> None:
        result = analyze_hwpx_template(Path("missing_template.hwpx"))

        self.assertEqual(result["status"], "template_required")
        self.assertFalse(result["available"])
        self.assertIn("템플릿 파일이 없거나 .hwpx 확장자가 아닙니다.", result["errors"])

    def test_detects_placeholder_split_across_text_nodes(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            hwpx_path = Path(temp_dir) / "split_placeholder.hwpx"
            section_xml = (
                '<?xml version="1.0" encoding="UTF-8"?>'
                '<hp:sec xmlns:hp="http://www.hancom.co.kr/hwpml/2011/paragraph">'
                '<hp:p><hp:run><hp:t>{{split_</hp:t></hp:run>'
                '<hp:run><hp:t>title}}</hp:t></hp:run></hp:p>'
                "</hp:sec>"
            )
            with zipfile.ZipFile(hwpx_path, "w") as package:
                package.writestr("mimetype", "application/hwp+zip")
                package.writestr("Contents/section0.xml", section_xml)

            result = analyze_hwpx_template(hwpx_path)

            self.assertEqual(result["placeholder_count"], 1)
            self.assertEqual(result["placeholders"], ["{{split_title}}"])

    def test_builds_explicit_template_summary_without_absolute_path_or_text(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            hwpx_path = Path(temp_dir) / "manual_candidate.hwpx"
            section_xml = (
                '<?xml version="1.0" encoding="UTF-8"?>'
                '<hp:sec xmlns:hp="http://www.hancom.co.kr/hwpml/2011/paragraph">'
                '<hp:p><hp:run><hp:t>{{title}}</hp:t></hp:run></hp:p>'
                '<hp:p><hp:run><hp:t>body text must stay out</hp:t></hp:run></hp:p>'
                "</hp:sec>"
            )
            with zipfile.ZipFile(hwpx_path, "w") as package:
                package.writestr("mimetype", "application/hwp+zip")
                package.writestr("Contents/section0.xml", section_xml)

            summary = build_structure_summary([hwpx_path])

            self.assertEqual(summary["scope"], "structure_only_no_text_extraction")
            self.assertEqual(summary["mode"], "explicit_templates")
            self.assertEqual(len(summary["results"]), 1)
            result = summary["results"][0]
            self.assertEqual(result["document_type"], "manual_candidate")
            self.assertEqual(result["template_name"], "manual_candidate.hwpx")
            self.assertEqual(result["template_path"], "manual_candidate.hwpx")
            self.assertNotIn(str(temp_dir), str(summary))
            self.assertNotIn("body text must stay out", str(summary))


if __name__ == "__main__":
    unittest.main()
