#!/usr/bin/env python3
"""Repair review DB model partition aliases."""

from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

from commonplace.review.review_db import (
    connect,
    count_model_id_records,
    prepare_review_db,
    rekey_model_id,
)
from commonplace.review.review_model import model_alias_target

TABLES = ("review_runs", "gate_reviews", "acceptance_events")
LEGACY_REVIEWS_ROOT = Path("kb/reports/reviews")


@dataclass(frozen=True)
class ReviewFileMove:
    source: Path
    target: Path
    old_model_id: str
    new_model_id: str


def _model_ids(conn) -> list[str]:
    model_ids: set[str] = set()
    for table in TABLES:
        rows = conn.execute(f"SELECT DISTINCT model_id FROM {table}").fetchall()
        model_ids.update(row["model_id"] for row in rows)
    return sorted(model_ids)


def _legacy_review_file_moves(repo_root: Path) -> list[ReviewFileMove]:
    reviews_root = repo_root / LEGACY_REVIEWS_ROOT
    if not reviews_root.is_dir():
        return []

    moves: list[ReviewFileMove] = []
    for source in sorted(reviews_root.rglob("*.md")):
        for suffix in (".opus-4-6.md", ".opus-4.6.md", ".claude-opus-4.6.md"):
            if not source.name.endswith(suffix):
                continue
            old_model_id = suffix.removeprefix(".").removesuffix(".md")
            new_model_id = model_alias_target(old_model_id)
            if new_model_id is None:
                continue
            target_name = f"{source.name[: -len(suffix)]}.{new_model_id}.md"
            moves.append(
                ReviewFileMove(
                    source=source,
                    target=source.with_name(target_name),
                    old_model_id=old_model_id,
                    new_model_id=new_model_id,
                )
            )
            break
    return moves


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Collapse known review model aliases to canonical partitions.",
    )
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report changes without writing them.",
    )
    args = parser.parse_args()

    repo_root = Path.cwd()
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
                "gate_reviews": counts.gate_reviews,
                "acceptance_events": counts.acceptance_events,
            }
            planned[(old_model_id, new_model_id)] = table_counts

        if not args.dry_run:
            for old_model_id, new_model_id in aliases.items():
                rekey_model_id(conn, old_model_id=old_model_id, new_model_id=new_model_id)
            conn.commit()

    file_moves = _legacy_review_file_moves(repo_root)
    collisions = [move for move in file_moves if move.target.exists()]
    if collisions:
        for move in collisions[:20]:
            print(f"collision: {move.source} -> {move.target}")
        if len(collisions) > 20:
            print(f"collision: ... {len(collisions) - 20} more")
        raise SystemExit(f"refusing to overwrite {len(collisions)} legacy review file(s)")

    if not args.dry_run:
        for move in file_moves:
            move.source.rename(move.target)

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
            f"gate_reviews={table_counts['gate_reviews']} "
            f"acceptance_events={table_counts['acceptance_events']}"
        )
    print(f"review_runs: {totals['review_runs']}")
    print(f"gate_reviews: {totals['gate_reviews']}")
    print(f"acceptance_events: {totals['acceptance_events']}")
    print(f"legacy_review_files: {len(file_moves)}")
    print(f"mode: {'dry-run' if args.dry_run else 'write'}")


if __name__ == "__main__":
    main()
