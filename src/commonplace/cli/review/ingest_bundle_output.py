#!/usr/bin/env python3
"""Ingest a sentinel-delimited review bundle into an existing review job."""

from __future__ import annotations

import argparse
from pathlib import Path

from commonplace.review.batch import ingest_batch_output
from commonplace.review.review_db import (
    connect,
    load_review_pairs_for_job,
    prepare_review_db,
)


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Parse a review bundle artifact and finalize its review job.",
    )
    parser.add_argument("--review-job-id", type=int, required=True, help="Review job id to ingest.")
    parser.add_argument("--input-file", required=True, help="Path to sentinel-delimited bundle output.")
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    args = parser.parse_args(argv)

    repo_root = cwd if cwd is not None else Path.cwd()
    db_path = prepare_review_db(repo_root, args.db)

    input_path = Path(args.input_file)
    if not input_path.is_file():
        parser.error(f"input file not found: {args.input_file}")
    bundle_markdown = input_path.read_text(encoding="utf-8")

    try:
        _, failed = ingest_batch_output(
            repo_root=repo_root,
            db_path=db_path,
            review_job_id=args.review_job_id,
            bundle_markdown=bundle_markdown,
        )
    except ValueError as exc:
        parser.error(str(exc))
    if failed:
        parser.error("; ".join(reason for _, reason in failed))

    with connect(db_path) as conn:
        gate_count = sum(
            1
            for row in load_review_pairs_for_job(conn, review_job_id=args.review_job_id)
            if row.pair_status == "completed"
        )

    print(f"completed {args.review_job_id} {gate_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
