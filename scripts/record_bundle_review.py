#!/usr/bin/env python3
"""Parse a bundled review artifact, record gate reviews, and finalize the run."""

from __future__ import annotations

import argparse
from pathlib import Path

from review_db import ensure_db, resolve_db_path
from run_review_bundle import BundleReviewRecordError, bundle_artifact_dir, record_bundle_review_run


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Parse a bundled review artifact and persist it into the review DB."
    )
    parser.add_argument("--review-run-id", type=int, required=True, help="Review run id to record.")
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    args = parser.parse_args()

    repo_root = Path.cwd()
    db_path = Path(args.db).resolve() if args.db else resolve_db_path(repo_root)
    ensure_db(repo_root, db_path)

    input_path = bundle_artifact_dir(repo_root, args.review_run_id) / "bundle-output.md"
    if not input_path.is_file():
        parser.error(f"bundle output not found: {input_path}")
    raw_bundle_markdown = input_path.read_text(encoding="utf-8")

    try:
        finalize_output = record_bundle_review_run(
            repo_root=repo_root,
            db_path=db_path,
            review_run_id=args.review_run_id,
            raw_bundle_markdown=raw_bundle_markdown,
        )
    except BundleReviewRecordError as exc:
        parser.exit(exc.returncode, f"{exc}\n")

    print(finalize_output)


if __name__ == "__main__":
    main()
