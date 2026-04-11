#!/usr/bin/env python3
"""Ingest a sentinel-delimited review bundle into an existing review run."""

from __future__ import annotations

import argparse
from pathlib import Path

from commonplace.review.review_db import (
    connect,
    fail_review_run,
    load_review_run,
    load_review_run_gates,
    prepare_review_db,
    record_and_finalize_run,
)
from commonplace.review.review_metadata import iso_now
from commonplace.review.run_review_bundle import (
    bundle_artifact_dir,
    parse_bundle_gate_reviews,
    write_bundle_artifacts,
)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Parse a review bundle artifact and finalize its review run.",
    )
    parser.add_argument("--review-run-id", type=int, required=True, help="Review run id to ingest.")
    parser.add_argument("--input-file", required=True, help="Path to sentinel-delimited bundle output.")
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    args = parser.parse_args()

    repo_root = Path.cwd()
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
        expected_gate_ids = [row.gate_id for row in load_review_run_gates(conn, review_run_id=args.review_run_id)]

    artifact_dir = bundle_artifact_dir(repo_root, args.review_run_id)
    write_bundle_artifacts(artifact_dir=artifact_dir, raw_bundle_markdown=raw_bundle_markdown)

    try:
        canonical_bundle_markdown, gate_reviews, canonical_reviews = parse_bundle_gate_reviews(
            raw_bundle_markdown,
            expected_gate_ids=expected_gate_ids,
        )
    except ValueError as exc:
        with connect(db_path) as conn:
            fail_review_run(
                conn,
                review_run_id=args.review_run_id,
                failure_reason=str(exc),
                completed_at=iso_now(),
                raw_bundle_markdown=raw_bundle_markdown,
            )
            conn.commit()
        parser.error(str(exc))

    write_bundle_artifacts(
        artifact_dir=artifact_dir,
        raw_bundle_markdown=canonical_bundle_markdown,
        parsed_reviews=canonical_reviews,
    )

    with connect(db_path) as conn:
        try:
            gate_count = record_and_finalize_run(
                conn,
                review_run_id=args.review_run_id,
                gate_reviews=gate_reviews,
                raw_bundle_markdown=canonical_bundle_markdown,
            )
        except ValueError as exc:
            conn.commit()
            parser.error(str(exc))
        conn.commit()

    print(f"completed {args.review_run_id} {gate_count}")


if __name__ == "__main__":
    main()
