"""Run placeholder-free HWPX autofill regression topics for sample forms."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from autofill_package import render_autofill_sections_to_hwpx
from render_autofill_batch_poc import OUTPUT_DIR, SAMPLE_FILES, default_sample_dir
from render_autofill_sample_poc import build_sample_profile_sections
from validation import has_forbidden_pattern


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_REGRESSION_TOPICS = [
    "시설 안전 점검",
    "민원 응대 절차 개선",
    "자료 취합 일정 정리",
    "회의 운영 방식 개선",
]


def build_regression_jobs(
    sample_dir: Path,
    output_dir: Path,
    topics: list[str] | None = None,
) -> list[dict[str, object]]:
    safe_topics = topics or DEFAULT_REGRESSION_TOPICS
    jobs: list[dict[str, object]] = []
    for topic_index, topic in enumerate(safe_topics, start=1):
        topic_dir = output_dir / f"topic{topic_index:02d}"
        for sample, template_name in SAMPLE_FILES.items():
            jobs.append(
                {
                    "topic_index": topic_index,
                    "topic": topic,
                    "sample": sample,
                    "template": sample_dir / template_name,
                    "template_name": template_name,
                    "output": topic_dir / f"autofill_profile_sample{sample}.hwpx",
                }
            )
    return jobs


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Regression render sample HWPX forms with safe topics.")
    parser.add_argument(
        "--topic",
        action="append",
        help="Deidentified regression topic. Can be repeated. Defaults to safe sample topics.",
    )
    parser.add_argument(
        "--sample-dir",
        type=Path,
        default=default_sample_dir(),
        help="Directory containing the two sample HWPX files.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=OUTPUT_DIR / "regression",
        help="Output directory. Default is ignored renderer output/regression.",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> None:
    args = parse_args(argv)
    topics = args.topic or DEFAULT_REGRESSION_TOPICS
    blocked = {topic: has_forbidden_pattern(topic) for topic in topics if has_forbidden_pattern(topic)}
    if blocked:
        print("regression_autofill_blocked")
        for topic, reasons in blocked.items():
            print(f"topic: {topic}")
            for reason in reasons:
                print(f"- {reason}")
        raise SystemExit(2)

    output_dir = args.output_dir if args.output_dir.is_absolute() else REPO_ROOT / args.output_dir
    jobs = build_regression_jobs(args.sample_dir, output_dir, topics)
    summary = {
        "status": "rendered",
        "topic_count": len(topics),
        "job_count": len(jobs),
        "jobs": [],
    }

    for job in jobs:
        template_path = Path(job["template"])
        output_path = Path(job["output"])
        result = render_autofill_sections_to_hwpx(
            template_path,
            output_path,
            build_sample_profile_sections(str(job["topic"]), str(job["template_name"])),
        )
        summary["jobs"].append(
            {
                "topic_index": job["topic_index"],
                "topic": job["topic"],
                "sample": job["sample"],
                "status": result["status"],
                "output": str(output_path),
                "inserted_paragraph_count": result["inserted_paragraph_count"],
                "matched_anchor_count": result["matched_anchor_count"],
            }
        )
        print(
            f"topic{job['topic_index']:02d} sample{job['sample']}: "
            f"{result['status']} inserted={result['inserted_paragraph_count']} "
            f"anchors={result['matched_anchor_count']}"
        )

    summary_path = output_dir / "autofill_regression_summary.json"
    output_dir.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"summary: {summary_path}")


if __name__ == "__main__":
    main()
