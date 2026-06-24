"""Batch render the two primary sample HWPX forms with one topic."""

from __future__ import annotations

import argparse
from pathlib import Path

from autofill_package import render_autofill_sections_to_hwpx
from render_autofill_sample_poc import build_sample_profile_sections
from validation import has_forbidden_pattern


REPO_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = Path(__file__).resolve().parent / "output"

SAMPLE_FILES = {
    "1": "(샘플양식1) 보고서 기본 양식.hwpx",
    "2": "(샘플양식2) 보고서 기반 양식(요약).hwpx",
}


def default_sample_dir() -> Path:
    return Path.home() / "Downloads" / "hwpx-autofill-conversion"


def build_batch_jobs(sample_dir: Path, output_dir: Path, sample: str) -> list[dict[str, Path | str]]:
    selected = SAMPLE_FILES.keys() if sample == "all" else [sample]
    jobs = []
    for key in selected:
        template_name = SAMPLE_FILES[key]
        jobs.append(
            {
                "sample": key,
                "template": sample_dir / template_name,
                "output": output_dir / f"autofill_profile_sample{key}_latest.hwpx",
                "template_name": template_name,
            }
        )
    return jobs


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render the primary sample HWPX forms.")
    parser.add_argument("--topic", required=True, help="Deidentified topic for the draft.")
    parser.add_argument(
        "--sample",
        choices=["1", "2", "all"],
        default="all",
        help="Sample form to render. Default renders both.",
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
        default=OUTPUT_DIR,
        help="Output directory. Default is ignored renderer output.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    reasons = has_forbidden_pattern(args.topic)
    if reasons:
        print("batch_autofill_blocked")
        for reason in reasons:
            print(f"- {reason}")
        raise SystemExit(2)

    output_dir = args.output_dir if args.output_dir.is_absolute() else REPO_ROOT / args.output_dir
    jobs = build_batch_jobs(args.sample_dir, output_dir, args.sample)

    print(f"topic: {args.topic}")
    for job in jobs:
        template_path = Path(job["template"])
        output_path = Path(job["output"])
        result = render_autofill_sections_to_hwpx(
            template_path,
            output_path,
            build_sample_profile_sections(args.topic, str(job["template_name"])),
        )
        print(f"sample{job['sample']}: {result['status']}")
        print(f"  template: {template_path.name}")
        print(f"  output: {output_path}")
        print(f"  inserted_paragraph_count: {result['inserted_paragraph_count']}")
        print(f"  matched_anchor_count: {result['matched_anchor_count']}")
        for section_result in result.get("section_results", []):
            matched_anchor = section_result.get("matched_anchor") or "none"
            print(
                f"  section: {section_result['status']} "
                f"anchor={matched_anchor} inserted={section_result['inserted_paragraph_count']}"
            )
        for error in result.get("errors", []):
            print(f"  - {error}")


if __name__ == "__main__":
    main()
