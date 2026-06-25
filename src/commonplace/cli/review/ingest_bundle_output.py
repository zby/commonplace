#!/usr/bin/env python3
"""Ingest a sentinel-delimited review bundle into an existing review run."""

from __future__ import annotations

import argparse
from pathlib import Path

from commonplace.review.bundle_ingest import parse_and_finalize_bundle_output
from commonplace.review.review_db import (
    connect,
    load_review_pairs_for_run,
    load_review_run,
    prepare_review_db,
)


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Parse a review bundle artifact and finalize its review run.",
    )
    parser.add_argument("--review-run-id", type=int, required=True, help="Review run id to ingest.")
    parser.add_argument("--input-file", required=True, help="Path to sentinel-delimited bundle output.")
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    args = parser.parse_args(argv)

    repo_root = cwd if cwd is not None else Path.cwd()
    db_path = prepare_review_db(repo_root, args.db)

    input_path = Path(args.input_file)
    if not input_path.is_file():
        parser.error(f"input file not found: {args.input_file}")
    raw_bundle_markdown = input_path.read_text(encoding="utf-8")

    with connect(db_path) as conn:
        review_run = load_review_run(conn, review_run_id=args.review_run_id)
        if review_run is None:
            parser.error(f"review run not found: {args.review_run_id}")
        if review_run.status != "running":
            parser.error(f"review run is not ingestible: {review_run.status}")
        expected_pairs = [
            (row.note_path, row.gate_path)
            for row in load_review_pairs_for_run(conn, review_run_id=args.review_run_id)
        ]

    with connect(db_path) as conn:
        try:
            gate_count = parse_and_finalize_bundle_output(
                conn,
                repo_root=repo_root,
                review_run_id=args.review_run_id,
                raw_bundle_markdown=raw_bundle_markdown,
                expected_pairs=expected_pairs,
            )
        except ValueError as exc:
            conn.commit()
            parser.error(str(exc))
        conn.commit()

    print(f"completed {args.review_run_id} {gate_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
