#!/usr/bin/env python3
"""Finalize a review run and advance acceptance for all requested gates."""

from __future__ import annotations

import argparse
from pathlib import Path

from review_db import (
    append_acceptance_event,
    complete_review_run,
    connect,
    ensure_db,
    fail_review_run,
    load_gate_reviews_for_run,
    load_review_run,
    load_review_run_gates,
    resolve_db_path,
)
from review_metadata import iso_now


def main() -> None:
    parser = argparse.ArgumentParser(description="Finalize a review run after all gate reviews are written.")
    parser.add_argument("--review-run-id", type=int, required=True, help="Review run id to finalize.")
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    args = parser.parse_args()

    repo_root = Path.cwd()
    db_path = Path(args.db).resolve() if args.db else resolve_db_path(repo_root)
    ensure_db(repo_root, db_path)

    with connect(db_path) as conn:
        review_run = load_review_run(conn, review_run_id=args.review_run_id)
        if review_run is None:
            parser.error(f"review run not found: {args.review_run_id}")
        if review_run.status != "running":
            parser.error(f"review run is not finalizable: {review_run.status}")

        run_gates = load_review_run_gates(conn, review_run_id=args.review_run_id)
        gate_reviews = load_gate_reviews_for_run(conn, review_run_id=args.review_run_id)
        run_gate_map = {row.gate_id: row for row in run_gates}
        written_gate_map = {row.gate_id: row for row in gate_reviews}

        missing = [row.gate_id for row in run_gates if row.gate_id not in written_gate_map]
        mismatched = [
            row.gate_id
            for row in gate_reviews
            if row.gate_id not in run_gate_map or row.gate_sha != run_gate_map[row.gate_id].gate_sha
        ]
        if missing or mismatched:
            reason_parts: list[str] = []
            if missing:
                reason_parts.append(f"missing gates: {', '.join(sorted(missing))}")
            if mismatched:
                reason_parts.append(f"gate provenance mismatch: {', '.join(sorted(mismatched))}")
            fail_review_run(
                conn,
                review_run_id=args.review_run_id,
                failure_reason="; ".join(reason_parts),
                completed_at=iso_now(),
            )
            conn.commit()
            parser.error("; ".join(reason_parts))

        completed_at = iso_now()
        complete_review_run(conn, review_run_id=args.review_run_id, completed_at=completed_at)
        for run_gate in run_gates:
            gate_review = written_gate_map[run_gate.gate_id]
            append_acceptance_event(
                conn,
                note_path=review_run.note_path,
                gate_id=run_gate.gate_id,
                model_id=review_run.model_id,
                accepted_review_id=gate_review.id,
                accepted_note_sha=review_run.reviewed_note_sha,
                accepted_note_commit=review_run.reviewed_note_commit,
                accepted_gate_sha=run_gate.gate_sha,
                accepted_at=completed_at,
                acceptance_kind="full-review",
            )
        conn.commit()

    print(f"completed {args.review_run_id} {len(run_gates)}")


if __name__ == "__main__":
    main()
