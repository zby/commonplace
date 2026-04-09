#!/usr/bin/env python3
"""Delete superseded legacy pre-commit review history that is no longer current."""

from __future__ import annotations

import argparse
from pathlib import Path

from commonplace.review.review_db import connect, ensure_db, resolve_db_path


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Delete superseded legacy pre-commit acceptance events and their gate reviews "
            "when the same (note, gate, model) key already has a newer current acceptance."
        )
    )
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    parser.add_argument("--dry-run", action="store_true", help="Report candidates without deleting them.")
    args = parser.parse_args()

    repo_root = Path.cwd()
    db_path = Path(args.db).resolve() if args.db else resolve_db_path(repo_root)
    ensure_db(repo_root, db_path)

    with connect(db_path) as conn:
        conn.execute("PRAGMA foreign_keys = ON")

        target_acceptance_rows = conn.execute(
            """
            WITH current_acceptance_ids AS (
                SELECT MAX(id) AS id
                FROM acceptance_events
                GROUP BY note_path, gate_id, model_id
            )
            SELECT
                e.id,
                e.accepted_review_id
            FROM acceptance_events AS e
            WHERE e.accepted_note_commit IS NULL
              AND e.id NOT IN (SELECT id FROM current_acceptance_ids)
            ORDER BY e.id
            """
        ).fetchall()
        target_acceptance_ids = [int(row["id"]) for row in target_acceptance_rows]
        target_gate_review_ids = sorted(
            {
                int(row["accepted_review_id"])
                for row in target_acceptance_rows
                if row["accepted_review_id"] is not None
            }
        )

        fully_superseded_review_run_rows = conn.execute(
            """
            WITH target_gate_reviews AS (
                SELECT DISTINCT e.accepted_review_id AS gate_review_id
                FROM acceptance_events AS e
                WHERE e.accepted_note_commit IS NULL
                  AND e.id NOT IN (
                      SELECT MAX(id)
                      FROM acceptance_events
                      GROUP BY note_path, gate_id, model_id
                  )
                  AND e.accepted_review_id IS NOT NULL
            ),
            review_run_gate_counts AS (
                SELECT
                    rr.id,
                    COUNT(gr.id) AS total_gate_reviews,
                    SUM(CASE WHEN tgr.gate_review_id IS NOT NULL THEN 1 ELSE 0 END) AS target_gate_reviews
                FROM review_runs AS rr
                JOIN gate_reviews AS gr
                  ON gr.review_run_id = rr.id
                LEFT JOIN target_gate_reviews AS tgr
                  ON tgr.gate_review_id = gr.id
                GROUP BY rr.id
            )
            SELECT id
            FROM review_run_gate_counts
            WHERE total_gate_reviews > 0
              AND total_gate_reviews = target_gate_reviews
            ORDER BY id
            """
        ).fetchall()
        target_review_run_ids = [int(row["id"]) for row in fully_superseded_review_run_rows]

        deleted_acceptance_events = 0
        deleted_gate_reviews = 0
        deleted_review_runs = 0

        if not args.dry_run:
            if target_acceptance_ids:
                placeholders = ", ".join("?" for _ in target_acceptance_ids)
                conn.execute(
                    f"""
                    DELETE FROM acceptance_events
                    WHERE id IN ({placeholders})
                    """,
                    target_acceptance_ids,
                )
                deleted_acceptance_events = len(target_acceptance_ids)

            if target_gate_review_ids:
                placeholders = ", ".join("?" for _ in target_gate_review_ids)
                conn.execute(
                    f"""
                    DELETE FROM gate_reviews
                    WHERE id IN ({placeholders})
                    """,
                    target_gate_review_ids,
                )
                deleted_gate_reviews = len(target_gate_review_ids)

            if target_review_run_ids:
                placeholders = ", ".join("?" for _ in target_review_run_ids)
                conn.execute(
                    f"""
                    DELETE FROM review_runs
                    WHERE id IN ({placeholders})
                    """,
                    target_review_run_ids,
                )
                deleted_review_runs = len(target_review_run_ids)

            conn.commit()

    print(f"target_acceptance_events: {len(target_acceptance_ids)}")
    print(f"target_gate_reviews: {len(target_gate_review_ids)}")
    print(f"target_review_runs: {len(target_review_run_ids)}")
    print(f"deleted_acceptance_events: {deleted_acceptance_events}")
    print(f"deleted_gate_reviews: {deleted_gate_reviews}")
    print(f"deleted_review_runs: {deleted_review_runs}")
    print(f"mode: {'dry-run' if args.dry_run else 'write'}")


if __name__ == "__main__":
    main()
