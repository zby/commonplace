#!/usr/bin/env python3
"""Record one gate review under an existing review run."""

from __future__ import annotations

import argparse
import sqlite3
from pathlib import Path

from commonplace.review.review_db import (
    connect,
    insert_gate_review,
    load_review_run,
    load_review_run_gates,
    prepare_review_db,
)
from commonplace.review.protocol.decisions import parse_review_decision, rewrite_review_result_footer
from commonplace.review.review_metadata import _METADATA_BLOCK_RE, iso_now


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = argparse.ArgumentParser(description="Write one gate review into the canonical review DB.")
    parser.add_argument("--review-run-id", type=int, required=True, help="Parent review run id.")
    parser.add_argument("--gate-id", required=True, help="Gate id being recorded.")
    parser.add_argument("--input-file", required=True, help="Path to markdown review body.")
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    args = parser.parse_args(argv)

    repo_root = cwd if cwd is not None else Path.cwd()
    db_path = prepare_review_db(repo_root, args.db)

    input_path = Path(args.input_file)
    if not input_path.is_file():
        parser.error(f"input file not found: {args.input_file}")
    review_text = input_path.read_text(encoding="utf-8")
    metadata_match = _METADATA_BLOCK_RE.match(review_text)
    if metadata_match is not None:
        review_text = review_text[metadata_match.end() :].lstrip("\n")
    decision = parse_review_decision(review_text)
    review_text = rewrite_review_result_footer(review_text, decision=decision)

    with connect(db_path) as conn:
        review_run = load_review_run(conn, review_run_id=args.review_run_id)
        if review_run is None:
            parser.error(f"review run not found: {args.review_run_id}")
        if review_run.status != "running":
            parser.error(f"review run is not writable: {review_run.status}")

        run_gates = {row.gate_id: row for row in load_review_run_gates(conn, review_run_id=args.review_run_id)}
        run_gate = run_gates.get(args.gate_id)
        if run_gate is None:
            parser.error(f"gate {args.gate_id} is not part of review run {args.review_run_id}")

        try:
            review_id = insert_gate_review(
                conn,
                review_run_id=args.review_run_id,
                note_path=review_run.note_path,
                gate_id=args.gate_id,
                model_id=review_run.model_id,
                decision=decision,
                rationale_markdown=review_text,
                evidence_json=None,
                gate_sha=run_gate.gate_sha,
                reviewed_note_sha=review_run.reviewed_note_sha,
                reviewed_note_commit=review_run.reviewed_note_commit,
                reviewed_at=iso_now(),
                review_kind="full-review",
            )
        except sqlite3.IntegrityError as exc:
            parser.error(str(exc))
        conn.commit()

    print(review_id)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
