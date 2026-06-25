#!/usr/bin/env python3
"""Prune superseded review-pair rows and whole-run artifacts."""

from __future__ import annotations

import argparse
import shutil
import sqlite3
from dataclasses import dataclass
from pathlib import Path

from commonplace.review.executor import bundle_artifact_dir
from commonplace.review.review_db import connect, prepare_review_db, prune_obsolete_snapshot_content


@dataclass(frozen=True)
class ObsoleteReviewPair:
    review_pair_id: int
    review_run_id: int


@dataclass(frozen=True)
class PrunePlan:
    obsolete_acceptance_event_ids: tuple[int, ...]
    obsolete_review_pairs: tuple[ObsoleteReviewPair, ...]
    obsolete_run_ids: tuple[int, ...]
    obsolete_run_artifact_dirs: tuple[Path, ...]
    obsolete_snapshot_content_rows: int


def _placeholders(values: tuple[int, ...]) -> str:
    return ", ".join("?" for _ in values)


def _current_acceptance_event_ids(conn: sqlite3.Connection) -> tuple[int, ...]:
    rows = conn.execute(
        """
        WITH ranked AS (
            SELECT
                acceptance_event_id,
                ROW_NUMBER() OVER (
                    PARTITION BY note_path, gate_path, model_partition
                    ORDER BY acceptance_event_id DESC
                ) AS rn
            FROM acceptance_events
        )
        SELECT acceptance_event_id
        FROM ranked
        WHERE rn = 1
        ORDER BY acceptance_event_id
        """
    ).fetchall()
    return tuple(int(row["acceptance_event_id"]) for row in rows)


def _current_review_pair_ids(conn: sqlite3.Connection) -> tuple[int, ...]:
    """Return the retained review pair for each current acceptance key.

    Current acceptance rows may have accepted_review_pair_id=NULL for pure
    acknowledgements. Those keys read through to the latest completed pair for
    the same (note_path, gate_path, model_partition), so pruning must retain that pair.
    """
    rows = conn.execute(
        """
        WITH latest_acceptance AS (
            SELECT
                acceptance_event_id,
                note_path,
                gate_path,
                model_partition,
                accepted_review_pair_id,
                ROW_NUMBER() OVER (
                    PARTITION BY note_path, gate_path, model_partition
                    ORDER BY acceptance_event_id DESC
                ) AS rn
            FROM acceptance_events
        ),
        latest_review_pair AS (
            SELECT
                review_pair_id,
                note_path,
                gate_path,
                model_partition,
                ROW_NUMBER() OVER (
                    PARTITION BY note_path, gate_path, model_partition
                    ORDER BY reviewed_at DESC, review_pair_id DESC
                ) AS rn
            FROM review_pairs
            WHERE pair_status = 'completed'
        )
        SELECT COALESCE(a.accepted_review_pair_id, rp.review_pair_id) AS review_pair_id
        FROM latest_acceptance AS a
        LEFT JOIN latest_review_pair AS rp
          ON rp.note_path = a.note_path
         AND rp.gate_path = a.gate_path
         AND rp.model_partition = a.model_partition
         AND rp.rn = 1
        WHERE a.rn = 1
          AND COALESCE(a.accepted_review_pair_id, rp.review_pair_id) IS NOT NULL
        ORDER BY review_pair_id
        """
    ).fetchall()
    return tuple(sorted({int(row["review_pair_id"]) for row in rows}))


def _obsolete_acceptance_event_ids(
    conn: sqlite3.Connection,
    current_acceptance_event_ids: tuple[int, ...],
) -> tuple[int, ...]:
    if not current_acceptance_event_ids:
        rows = conn.execute("SELECT acceptance_event_id FROM acceptance_events ORDER BY acceptance_event_id").fetchall()
        return tuple(int(row["acceptance_event_id"]) for row in rows)
    rows = conn.execute(
        f"""
        SELECT acceptance_event_id
        FROM acceptance_events
        WHERE acceptance_event_id NOT IN ({_placeholders(current_acceptance_event_ids)})
        ORDER BY acceptance_event_id
        """,
        current_acceptance_event_ids,
    ).fetchall()
    return tuple(int(row["acceptance_event_id"]) for row in rows)


def _obsolete_review_pairs(
    conn: sqlite3.Connection,
    current_review_pair_ids: tuple[int, ...],
) -> tuple[ObsoleteReviewPair, ...]:
    if not current_review_pair_ids:
        return ()
    rows = conn.execute(
        f"""
        SELECT rp.review_pair_id, rp.review_run_id
        FROM review_pairs AS rp
        JOIN review_pairs AS current
          ON current.note_path = rp.note_path
         AND current.gate_path = rp.gate_path
         AND current.model_partition = rp.model_partition
        WHERE current.review_pair_id IN ({_placeholders(current_review_pair_ids)})
          AND rp.review_pair_id NOT IN ({_placeholders(current_review_pair_ids)})
          AND rp.pair_status != 'pending'
        ORDER BY rp.review_pair_id
        """,
        (*current_review_pair_ids, *current_review_pair_ids),
    ).fetchall()
    return tuple(
        ObsoleteReviewPair(
            review_pair_id=int(row["review_pair_id"]),
            review_run_id=int(row["review_run_id"]),
        )
        for row in rows
    )


def _obsolete_run_ids(conn: sqlite3.Connection, obsolete_review_pair_ids: tuple[int, ...]) -> tuple[int, ...]:
    if not obsolete_review_pair_ids:
        return ()
    rows = conn.execute(
        f"""
        WITH obsolete_pairs AS (
            SELECT review_pair_id, review_run_id
            FROM review_pairs
            WHERE review_pair_id IN ({_placeholders(obsolete_review_pair_ids)})
        ),
        candidate_runs AS (
            SELECT DISTINCT review_run_id
            FROM obsolete_pairs
        ),
        retained_pairs AS (
            SELECT rp.review_run_id
            FROM review_pairs AS rp
            JOIN candidate_runs AS cr
              ON cr.review_run_id = rp.review_run_id
            WHERE rp.review_pair_id NOT IN ({_placeholders(obsolete_review_pair_ids)})
        )
        SELECT cr.review_run_id
        FROM candidate_runs AS cr
        LEFT JOIN retained_pairs AS retained
          ON retained.review_run_id = cr.review_run_id
        WHERE retained.review_run_id IS NULL
        ORDER BY cr.review_run_id
        """,
        (*obsolete_review_pair_ids, *obsolete_review_pair_ids),
    ).fetchall()
    return tuple(int(row["review_run_id"]) for row in rows)


def build_prune_plan(repo_root: Path, conn: sqlite3.Connection) -> PrunePlan:
    current_acceptance_event_ids = _current_acceptance_event_ids(conn)
    current_review_pair_ids = _current_review_pair_ids(conn)
    obsolete_acceptance_event_ids = _obsolete_acceptance_event_ids(conn, current_acceptance_event_ids)
    obsolete_review_pairs = _obsolete_review_pairs(conn, current_review_pair_ids)
    obsolete_review_pair_ids = tuple(pair.review_pair_id for pair in obsolete_review_pairs)
    obsolete_run_ids = _obsolete_run_ids(conn, obsolete_review_pair_ids)

    run_artifact_dirs: list[Path] = []
    for review_run_id in obsolete_run_ids:
        artifact_dir = bundle_artifact_dir(repo_root, review_run_id)
        if artifact_dir.exists():
            run_artifact_dirs.append(artifact_dir)

    return PrunePlan(
        obsolete_acceptance_event_ids=obsolete_acceptance_event_ids,
        obsolete_review_pairs=obsolete_review_pairs,
        obsolete_run_ids=obsolete_run_ids,
        obsolete_run_artifact_dirs=tuple(sorted(run_artifact_dirs, key=lambda path: path.as_posix())),
        obsolete_snapshot_content_rows=_obsolete_snapshot_content_row_count(conn),
    )


def _obsolete_snapshot_content_row_count(conn: sqlite3.Connection) -> int:
    row = conn.execute(
        """
        WITH retained_snapshots AS (
            SELECT accepted_note_snapshot_id AS snapshot_id
            FROM current_gate_acceptances
            WHERE accepted_note_snapshot_id IS NOT NULL

            UNION

            SELECT accepted_gate_snapshot_id AS snapshot_id
            FROM current_gate_acceptances
            WHERE accepted_gate_snapshot_id IS NOT NULL

            UNION

            SELECT reviewed_note_snapshot_id AS snapshot_id
            FROM review_pairs
            WHERE pair_status != 'completed'
              AND reviewed_note_snapshot_id IS NOT NULL

            UNION

            SELECT reviewed_gate_snapshot_id AS snapshot_id
            FROM review_pairs
            WHERE pair_status != 'completed'
              AND reviewed_gate_snapshot_id IS NOT NULL
        )
        SELECT COUNT(*) AS count
        FROM review_file_snapshots
        WHERE content_text IS NOT NULL
          AND snapshot_id NOT IN (
              SELECT snapshot_id
              FROM retained_snapshots
          )
        """
    ).fetchone()
    return int(row["count"] if row is not None else 0)


def _delete_ids(conn: sqlite3.Connection, table: str, id_column: str, ids: tuple[int, ...]) -> None:
    if not ids:
        return
    conn.execute(
        f"DELETE FROM {table} WHERE {id_column} IN ({_placeholders(ids)})",
        ids,
    )


def apply_prune_plan(repo_root: Path, conn: sqlite3.Connection, plan: PrunePlan) -> None:
    conn.execute("PRAGMA foreign_keys = ON")
    obsolete_review_pair_ids = tuple(pair.review_pair_id for pair in plan.obsolete_review_pairs)
    _delete_ids(conn, "acceptance_events", "acceptance_event_id", plan.obsolete_acceptance_event_ids)
    _delete_ids(conn, "review_pairs", "review_pair_id", obsolete_review_pair_ids)
    _delete_ids(conn, "review_runs", "review_run_id", plan.obsolete_run_ids)
    prune_obsolete_snapshot_content(conn)
    conn.commit()

    for path in plan.obsolete_run_artifact_dirs:
        shutil.rmtree(path, ignore_errors=True)


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Prune superseded review-pair rows and whole-run artifacts. "
            "Keeps the current accepted pair per (note, gate, model)."
        )
    )
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="Report candidates without deleting them. This is the default.")
    mode.add_argument("--apply", action="store_true", help="Apply the cleanup.")
    args = parser.parse_args(argv)

    repo_root = cwd if cwd is not None else Path.cwd()
    db_path = prepare_review_db(repo_root, args.db)

    with connect(db_path) as conn:
        plan = build_prune_plan(repo_root, conn)
        if args.apply:
            apply_prune_plan(repo_root, conn, plan)

    print(f"obsolete_acceptance_events: {len(plan.obsolete_acceptance_event_ids)}")
    print(f"obsolete_review_pairs: {len(plan.obsolete_review_pairs)}")
    print(f"obsolete_review_runs: {len(plan.obsolete_run_ids)}")
    print(f"obsolete_run_artifact_dirs: {len(plan.obsolete_run_artifact_dirs)}")
    print(f"obsolete_snapshot_content_rows: {plan.obsolete_snapshot_content_rows}")
    print(f"mode: {'apply' if args.apply else 'dry-run'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
