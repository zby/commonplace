#!/usr/bin/env python3
"""Repair review DB model partition aliases."""

from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path

from commonplace.review.review_db import (
    connect,
    count_model_id_records,
    prepare_review_db,
    rekey_model_id,
)
from commonplace.review.review_model import model_alias_target

TABLES = ("review_runs", "review_pairs", "acceptance_events")


def _model_ids(conn) -> list[str]:
    model_ids: set[str] = set()
    for table in TABLES:
        rows = conn.execute(f"SELECT DISTINCT model_id FROM {table}").fetchall()
        model_ids.update(row["model_id"] for row in rows)
    return sorted(model_ids)


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Collapse known review model aliases to canonical partitions.",
    )
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report changes without writing them.",
    )
    args = parser.parse_args(argv)

    repo_root = cwd if cwd is not None else Path.cwd()
    db_path = prepare_review_db(repo_root, args.db)

    with connect(db_path) as conn:
        aliases = {
            model_id: target
            for model_id in _model_ids(conn)
            if (target := model_alias_target(model_id)) is not None
        }

        planned: dict[tuple[str, str], dict[str, int]] = {}
        for old_model_id, new_model_id in aliases.items():
            counts = count_model_id_records(conn, model_id=old_model_id)
            table_counts = {
                "review_runs": counts.review_runs,
                "review_pairs": counts.review_pairs,
                "acceptance_events": counts.acceptance_events,
            }
            planned[(old_model_id, new_model_id)] = table_counts

        if not args.dry_run:
            for old_model_id, new_model_id in aliases.items():
                rekey_model_id(conn, old_model_id=old_model_id, new_model_id=new_model_id)
            conn.commit()

    totals = defaultdict(int)
    for (_old_model_id, _new_model_id), table_counts in planned.items():
        for table, count in table_counts.items():
            totals[table] += count

    print(f"aliases: {len(planned)}")
    for (old_model_id, new_model_id), table_counts in sorted(planned.items()):
        total = sum(table_counts.values())
        print(
            f"{old_model_id} -> {new_model_id}: total={total} "
            f"review_runs={table_counts['review_runs']} "
            f"review_pairs={table_counts['review_pairs']} "
            f"acceptance_events={table_counts['acceptance_events']}"
        )
    print(f"review_runs: {totals['review_runs']}")
    print(f"review_pairs: {totals['review_pairs']}")
    print(f"acceptance_events: {totals['acceptance_events']}")
    print(f"mode: {'dry-run' if args.dry_run else 'write'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
