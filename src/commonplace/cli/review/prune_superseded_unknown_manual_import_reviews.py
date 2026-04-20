#!/usr/bin/env python3
"""Delete superseded manual-import unknown reviews that are no longer current."""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path

from commonplace.review.review_db import connect, prepare_review_db


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Delete manual-import reviews with decision=unknown when the same "
            "(note, gate, model) key already has a different current accepted review."
        )
    )
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    parser.add_argument("--dry-run", action="store_true", help="Report candidates without deleting them.")
    args = parser.parse_args(argv)

    repo_root = cwd if cwd is not None else Path.cwd()
    db_path = prepare_review_db(repo_root, args.db)

    with connect(db_path) as conn:
        conn.execute("PRAGMA foreign_keys = ON")

        rows = conn.execute(
            """
            SELECT
                gr.id,
                accepted.review_kind AS replacement_review_kind
            FROM gate_reviews AS gr
            JOIN current_gate_acceptances AS current
              ON current.note_path = gr.note_path
             AND current.gate_id = gr.gate_id
             AND current.model_id = gr.model_id
            JOIN gate_reviews AS accepted
              ON accepted.id = current.accepted_review_id
            WHERE gr.review_kind = 'manual-import'
              AND gr.decision = 'unknown'
              AND current.accepted_review_id IS NOT NULL
              AND current.accepted_review_id != gr.id
            ORDER BY gr.id
            """
        ).fetchall()

        target_ids = [int(row["id"]) for row in rows]
        replacement_counts: Counter[str] = Counter(
            str(row["replacement_review_kind"]) for row in rows
        )

        historical_acceptance_refs = 0
        current_refs = 0
        if target_ids:
            placeholders = ", ".join("?" for _ in target_ids)
            historical_acceptance_refs = int(
                conn.execute(
                    f"""
                    SELECT COUNT(*)
                    FROM acceptance_events
                    WHERE accepted_review_id IN ({placeholders})
                    """,
                    target_ids,
                ).fetchone()[0]
            )
            current_refs = int(
                conn.execute(
                    f"""
                    SELECT COUNT(*)
                    FROM current_gate_acceptances
                    WHERE accepted_review_id IN ({placeholders})
                    """,
                    target_ids,
                ).fetchone()[0]
            )

        if current_refs:
            raise SystemExit(
                f"refusing to delete {current_refs} reviews that are still current acceptances"
            )

        deleted = 0
        if not args.dry_run and target_ids:
            placeholders = ", ".join("?" for _ in target_ids)
            conn.execute(
                f"""
                DELETE FROM gate_reviews
                WHERE id IN ({placeholders})
                """,
                target_ids,
            )
            conn.commit()
            deleted = len(target_ids)

    print(f"target_rows: {len(target_ids)}")
    print(f"historical_acceptance_refs: {historical_acceptance_refs}")
    print(f"replaced_by_full_review: {replacement_counts['full-review']}")
    print(f"replaced_by_manual_import: {replacement_counts['manual-import']}")
    print(f"deleted: {deleted}")
    print(f"mode: {'dry-run' if args.dry_run else 'write'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
