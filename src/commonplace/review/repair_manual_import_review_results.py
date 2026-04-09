#!/usr/bin/env python3
"""Repair legacy manual-import review rows by inferring a canonical decision and footer."""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path

from commonplace.review.review_db import connect, ensure_db, resolve_db_path
from commonplace.review.review_decisions import infer_manual_import_review_decision, rewrite_review_result_footer


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Repair manual-import review rows by rewriting stale result footers and decisions."
    )
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    parser.add_argument("--dry-run", action="store_true", help="Report changes without writing them.")
    args = parser.parse_args()

    repo_root = Path.cwd()
    db_path = Path(args.db).resolve() if args.db else resolve_db_path(repo_root)
    ensure_db(repo_root, db_path)

    scanned = 0
    updated = 0
    decisions_changed = 0
    markdown_changed = 0
    inferred_counts: Counter[str] = Counter()

    with connect(db_path) as conn:
        rows = conn.execute(
            """
            SELECT id, decision, rationale_markdown
            FROM gate_reviews
            WHERE review_kind = 'manual-import'
            ORDER BY id
            """
        ).fetchall()

        for row in rows:
            scanned += 1
            inferred_decision = infer_manual_import_review_decision(row["rationale_markdown"])
            inferred_counts[inferred_decision] += 1
            rewritten_markdown = rewrite_review_result_footer(
                row["rationale_markdown"],
                decision=inferred_decision,
            )

            needs_decision_update = inferred_decision != row["decision"]
            needs_markdown_update = rewritten_markdown != row["rationale_markdown"]
            if not needs_decision_update and not needs_markdown_update:
                continue

            updated += 1
            if needs_decision_update:
                decisions_changed += 1
            if needs_markdown_update:
                markdown_changed += 1
            if args.dry_run:
                continue

            conn.execute(
                """
                UPDATE gate_reviews
                SET decision = ?, rationale_markdown = ?
                WHERE id = ?
                """,
                (inferred_decision, rewritten_markdown, row["id"]),
            )

        if not args.dry_run:
            conn.commit()

    print(f"scanned: {scanned}")
    print(f"updated: {updated}")
    print(f"decisions_changed: {decisions_changed}")
    print(f"markdown_changed: {markdown_changed}")
    for decision in ("pass", "warn", "fail", "error", "unknown"):
        print(f"inferred_{decision}: {inferred_counts[decision]}")
    print(f"mode: {'dry-run' if args.dry_run else 'write'}")


if __name__ == "__main__":
    main()
