#!/usr/bin/env python3
"""Repair review DB model partition aliases."""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path

from commonplace.review.review_db import (
    connect,
    count_model_partition_records,
    prepare_review_db,
    rekey_model_partition,
)
from commonplace.review.review_model import is_registered_model_partition, model_partition_alias_target

TABLES = ("review_jobs", "acceptance_events")


def _model_partitions(conn) -> list[str]:
    model_partitions: set[str] = set()
    for table in TABLES:
        rows = conn.execute(f"SELECT DISTINCT model_partition FROM {table}").fetchall()
        model_partitions.update(row["model_partition"] for row in rows)
    return sorted(model_partitions)


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
        model_partitions = _model_partitions(conn)
        aliases = {
            model_partition: target
            for model_partition in model_partitions
            if (target := model_partition_alias_target(model_partition)) is not None
        }
        unknown_partitions = [
            model_partition
            for model_partition in model_partitions
            if not is_registered_model_partition(model_partition)
        ]

        planned: dict[tuple[str, str], dict[str, int]] = {}
        for old_model_partition, new_model_partition in aliases.items():
            counts = count_model_partition_records(conn, model_partition=old_model_partition)
            table_counts = {
                "review_jobs": counts.review_jobs,
                "acceptance_events": counts.acceptance_events,
            }
            planned[(old_model_partition, new_model_partition)] = table_counts

        if unknown_partitions and not args.dry_run:
            print(
                "refusing to repair model partitions with unknown existing partitions",
                file=sys.stderr,
            )
            for model_partition in unknown_partitions:
                print(f"unknown: {model_partition}", file=sys.stderr)
            return 1

        if not args.dry_run:
            for old_model_partition, new_model_partition in aliases.items():
                rekey_model_partition(conn, old_model_partition=old_model_partition, new_model_partition=new_model_partition)
            conn.commit()

    totals = defaultdict(int)
    for (_old_model_partition, _new_model_partition), table_counts in planned.items():
        for table, count in table_counts.items():
            totals[table] += count

    print(f"aliases: {len(planned)}")
    for (old_model_partition, new_model_partition), table_counts in sorted(planned.items()):
        total = sum(table_counts.values())
        print(
            f"{old_model_partition} -> {new_model_partition}: total={total} "
            f"review_jobs={table_counts['review_jobs']} "
            f"acceptance_events={table_counts['acceptance_events']}"
        )
    print(f"review_jobs: {totals['review_jobs']}")
    print(f"acceptance_events: {totals['acceptance_events']}")
    print(f"unknown_partitions: {len(unknown_partitions)}")
    for model_partition in unknown_partitions:
        print(f"unknown: {model_partition}")
    print(f"mode: {'dry-run' if args.dry_run else 'write'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
