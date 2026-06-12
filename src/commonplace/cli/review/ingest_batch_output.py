#!/usr/bin/env python3
"""Ingest a batch's pair-delimited review output and finalize its runs with salvage."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from commonplace.review.batch import ingest_batch_output
from commonplace.review.review_db import prepare_review_db


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Parse a batch review output artifact and finalize its review runs.",
    )
    parser.add_argument(
        "--review-run-ids",
        type=int,
        nargs="+",
        required=True,
        help="Review run ids prepared for this batch.",
    )
    parser.add_argument("--input-file", required=True, help="Path to the pair-delimited batch output.")
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    args = parser.parse_args(argv)

    repo_root = cwd if cwd is not None else Path.cwd()
    db_path = prepare_review_db(repo_root, args.db)

    input_path = Path(args.input_file)
    if not input_path.is_file():
        parser.error(f"input file not found: {args.input_file}")
    raw_bundle_markdown = input_path.read_text(encoding="utf-8")

    try:
        completed, failed = ingest_batch_output(
            repo_root=repo_root,
            db_path=db_path,
            review_run_ids=args.review_run_ids,
            raw_bundle_markdown=raw_bundle_markdown,
        )
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    payload = {
        "completed": completed,
        "failed": [{"review_run_id": review_run_id, "reason": reason} for review_run_id, reason in failed],
    }
    print(json.dumps(payload, ensure_ascii=True, sort_keys=True))
    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
