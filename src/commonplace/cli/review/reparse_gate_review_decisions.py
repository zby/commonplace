#!/usr/bin/env python3
"""Reparse stored gate review decisions from persisted markdown."""

from __future__ import annotations

import argparse
from pathlib import Path

from commonplace.review.protocol.decisions import parse_review_decision
from commonplace.review.review_db import connect, prepare_review_db


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = argparse.ArgumentParser(description="Reparse gate_reviews.decision from rationale_markdown.")
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    parser.add_argument(
        "--review-run-id",
        type=int,
        action="append",
        dest="review_run_ids",
        help="Restrict to one or more review runs.",
    )
    parser.add_argument(
        "--combined-only",
        action="store_true",
        help="Restrict to reviews written by bundle runs with raw_bundle_markdown.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Report changes without writing them.")
    args = parser.parse_args(argv)

    repo_root = cwd if cwd is not None else Path.cwd()
    db_path = prepare_review_db(repo_root, args.db)

    where_clauses: list[str] = []
    params: list[object] = []
    if args.review_run_ids:
        placeholders = ", ".join("?" for _ in args.review_run_ids)
        where_clauses.append(f"review_run_id IN ({placeholders})")
        params.extend(args.review_run_ids)
    if args.combined_only:
        where_clauses.append(
            """
            review_run_id IN (
                SELECT id
                FROM review_runs
                WHERE raw_bundle_markdown IS NOT NULL AND raw_bundle_markdown != ''
            )
            """
        )
    where_sql = ""
    if where_clauses:
        where_sql = "WHERE " + " AND ".join(clause.strip() for clause in where_clauses)

    with connect(db_path) as conn:
        rows = conn.execute(
            f"""
            SELECT id, decision, rationale_markdown
            FROM gate_reviews
            {where_sql}
            ORDER BY id
            """,
            params,
        ).fetchall()

        changed = 0
        unknown = 0
        for row in rows:
            new_decision = parse_review_decision(row["rationale_markdown"])
            if new_decision == "unknown":
                unknown += 1
            if new_decision == row["decision"]:
                continue
            changed += 1
            if not args.dry_run:
                conn.execute(
                    """
                    UPDATE gate_reviews
                    SET decision = ?
                    WHERE id = ?
                    """,
                    (new_decision, row["id"]),
                )

        if not args.dry_run:
            conn.commit()

    print(f"scanned: {len(rows)}")
    print(f"changed: {changed}")
    print(f"unknown: {unknown}")
    print(f"mode: {'dry-run' if args.dry_run else 'write'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
