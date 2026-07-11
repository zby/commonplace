#!/usr/bin/env python3
"""Migrate a populated Commonplace review store directly from schema v5 to v7."""

from __future__ import annotations

import argparse
import sqlite3
from pathlib import Path


TARGET_SCHEMA = """
CREATE TABLE review_jobs_new (
    review_job_id INTEGER PRIMARY KEY,
    model_partition TEXT NOT NULL,
    runner TEXT,
    runner_model TEXT,
    runner_effort TEXT,
    created_at TEXT NOT NULL,
    completed_at TEXT,
    status TEXT NOT NULL CHECK (status IN ('queued', 'completed', 'failed')),
    failure_reason TEXT,
    telemetry_json TEXT,
    grouping TEXT NOT NULL CHECK (grouping IN ('note', 'criterion')),
    CHECK (
        (status = 'queued' AND completed_at IS NULL AND failure_reason IS NULL)
        OR (status = 'completed' AND completed_at IS NOT NULL AND failure_reason IS NULL)
        OR (status = 'failed' AND completed_at IS NOT NULL AND failure_reason IS NOT NULL)
    )
);
CREATE TABLE review_pairs_new (
    review_pair_id INTEGER PRIMARY KEY,
    review_job_id INTEGER NOT NULL REFERENCES review_jobs_new(review_job_id) ON DELETE CASCADE,
    note_path TEXT NOT NULL,
    criterion_path TEXT NOT NULL,
    pair_ordinal INTEGER NOT NULL,
    result_kind TEXT NOT NULL CHECK (result_kind IN ('verdict', 'report')),
    outcome TEXT CHECK (outcome IN ('pass', 'warn', 'fail')),
    reviewed_note_snapshot_id INTEGER REFERENCES review_file_snapshots(snapshot_id),
    reviewed_criterion_snapshot_id INTEGER REFERENCES review_file_snapshots(snapshot_id),
    completed_at TEXT,
    CHECK (
        (completed_at IS NULL AND outcome IS NULL)
        OR (
            completed_at IS NOT NULL
            AND (
                (result_kind = 'verdict' AND outcome IS NOT NULL)
                OR (result_kind = 'report' AND outcome IS NULL)
            )
        )
    ),
    UNIQUE (review_job_id, note_path, criterion_path),
    UNIQUE (review_job_id, pair_ordinal)
);
CREATE TABLE freshness_baselines (
    note_path TEXT NOT NULL,
    criterion_path TEXT NOT NULL,
    model_partition TEXT NOT NULL,
    evidence_review_pair_id INTEGER NOT NULL REFERENCES review_pairs_new(review_pair_id),
    baseline_note_snapshot_id INTEGER NOT NULL REFERENCES review_file_snapshots(snapshot_id),
    baseline_criterion_snapshot_id INTEGER NOT NULL REFERENCES review_file_snapshots(snapshot_id),
    baseline_updated_at TEXT NOT NULL
);
"""

TARGET_INDEXES_AND_VIEW = """
CREATE INDEX idx_review_jobs_model_partition_created
ON review_jobs(model_partition, created_at DESC);
CREATE INDEX idx_review_jobs_status ON review_jobs(status);
CREATE INDEX idx_review_pairs_note_criterion
ON review_pairs(note_path, criterion_path);
CREATE INDEX idx_review_pairs_review_job_id ON review_pairs(review_job_id);
CREATE UNIQUE INDEX idx_freshness_baselines_note_criterion_model_partition
ON freshness_baselines(note_path, criterion_path, model_partition);
CREATE VIEW current_freshness_baselines AS
SELECT
    b.note_path,
    b.criterion_path,
    b.model_partition,
    b.evidence_review_pair_id,
    b.baseline_note_snapshot_id,
    b.baseline_criterion_snapshot_id,
    note_snapshot.content_sha256 AS baseline_note_hash,
    criterion_snapshot.content_sha256 AS baseline_criterion_hash,
    note_snapshot.content_text AS baseline_note_text,
    criterion_snapshot.content_text AS baseline_criterion_text,
    b.baseline_updated_at,
    rp.result_kind,
    rp.outcome
FROM freshness_baselines AS b
JOIN review_pairs AS rp
  ON rp.review_pair_id = b.evidence_review_pair_id
 AND rp.note_path = b.note_path
 AND rp.criterion_path = b.criterion_path
JOIN review_jobs AS j
  ON j.review_job_id = rp.review_job_id
 AND j.model_partition = b.model_partition
JOIN review_file_snapshots AS note_snapshot
  ON b.baseline_note_snapshot_id = note_snapshot.snapshot_id
JOIN review_file_snapshots AS criterion_snapshot
  ON b.baseline_criterion_snapshot_id = criterion_snapshot.snapshot_id
WHERE j.status = 'completed'
  AND rp.completed_at IS NOT NULL
  AND (rp.result_kind = 'report' OR rp.outcome IS NOT NULL);
"""


def _count(conn: sqlite3.Connection, table: str) -> int:
    return int(conn.execute(f"SELECT count(*) FROM {table}").fetchone()[0])


def _execute_statements(conn: sqlite3.Connection, sql: str) -> None:
    for statement in sql.split(";"):
        if statement.strip():
            conn.execute(statement)


def _validate_v5_evidence(conn: sqlite3.Connection) -> None:
    error_count = int(
        conn.execute("SELECT count(*) FROM review_pairs WHERE decision = 'error'").fetchone()[0]
    )
    if error_count:
        raise RuntimeError(
            f"schema v5 contains {error_count} ERROR pair(s); migration refused because ERROR is not completed evidence"
        )
    malformed = conn.execute(
        """
        SELECT a.note_path, a.gate_path, a.model_partition
        FROM acceptance AS a
        LEFT JOIN review_pairs AS rp
          ON rp.review_pair_id = a.accepted_review_pair_id
        LEFT JOIN review_jobs AS j
          ON j.review_job_id = rp.review_job_id
        LEFT JOIN review_file_snapshots AS note_snapshot
          ON note_snapshot.snapshot_id = a.accepted_note_snapshot_id
        LEFT JOIN review_file_snapshots AS gate_snapshot
          ON gate_snapshot.snapshot_id = a.accepted_gate_snapshot_id
        WHERE rp.review_pair_id IS NULL
           OR rp.note_path != a.note_path
           OR rp.gate_path != a.gate_path
           OR rp.reviewed_at IS NULL
           OR (rp.result_kind = 'verdict' AND rp.decision IS NULL)
           OR (rp.result_kind = 'report' AND rp.decision IS NOT NULL)
           OR j.review_job_id IS NULL
           OR j.status != 'completed'
           OR j.model_partition != a.model_partition
           OR note_snapshot.snapshot_id IS NULL
           OR note_snapshot.path != a.note_path
           OR note_snapshot.content_text IS NULL
           OR gate_snapshot.snapshot_id IS NULL
           OR gate_snapshot.path != a.gate_path
           OR gate_snapshot.content_text IS NULL
        LIMIT 1
        """
    ).fetchone()
    if malformed is not None:
        raise RuntimeError(
            "schema v5 contains a malformed acceptance row: "
            f"{malformed[0]} :: {malformed[1]} :: {malformed[2]}"
        )


def migrate(db_path: Path) -> None:
    conn = sqlite3.connect(db_path, isolation_level=None)
    try:
        conn.execute("PRAGMA foreign_keys = OFF")
        version = int(conn.execute("PRAGMA user_version").fetchone()[0])
        if version != 5:
            raise RuntimeError(f"expected review schema version 5, found {version}; migration refused")
        violations = conn.execute("PRAGMA foreign_key_check").fetchall()
        if violations:
            raise RuntimeError(f"source foreign key check failed: {violations}")
        _validate_v5_evidence(conn)
        source_counts = {
            "review_jobs": _count(conn, "review_jobs"),
            "review_pairs": _count(conn, "review_pairs"),
            "review_file_snapshots": _count(conn, "review_file_snapshots"),
            "freshness_baselines": _count(conn, "acceptance"),
        }

        conn.execute("BEGIN IMMEDIATE")
        try:
            conn.execute("DROP VIEW current_gate_acceptances")
            for index_name in (
                "idx_review_jobs_model_partition_created",
                "idx_review_jobs_status",
                "idx_review_pairs_note_gate",
                "idx_review_pairs_review_job_id",
                "idx_acceptance_note_gate_model_partition",
            ):
                conn.execute(f"DROP INDEX {index_name}")
            _execute_statements(conn, TARGET_SCHEMA)
            conn.execute(
                """
                INSERT INTO review_jobs_new
                SELECT
                    review_job_id, model_partition, runner, runner_model,
                    runner_effort, created_at, completed_at, status,
                    failure_reason, telemetry_json,
                    CASE packing WHEN 'gate' THEN 'criterion' ELSE packing END
                FROM review_jobs
                """
            )
            conn.execute(
                """
                INSERT INTO review_pairs_new
                SELECT
                    review_pair_id, review_job_id, note_path, gate_path,
                    pair_ordinal, result_kind, decision,
                    reviewed_note_snapshot_id, reviewed_gate_snapshot_id, reviewed_at
                FROM review_pairs
                """
            )
            conn.execute(
                """
                INSERT INTO freshness_baselines
                SELECT
                    note_path, gate_path, model_partition,
                    accepted_review_pair_id, accepted_note_snapshot_id,
                    accepted_gate_snapshot_id, accepted_at
                FROM acceptance
                """
            )
            conn.execute("DROP TABLE acceptance")
            conn.execute("DROP TABLE review_pairs")
            conn.execute("DROP TABLE review_jobs")
            conn.execute("ALTER TABLE review_jobs_new RENAME TO review_jobs")
            conn.execute("ALTER TABLE review_pairs_new RENAME TO review_pairs")
            _execute_statements(conn, TARGET_INDEXES_AND_VIEW)
            target_counts = {
                "review_jobs": _count(conn, "review_jobs"),
                "review_pairs": _count(conn, "review_pairs"),
                "review_file_snapshots": _count(conn, "review_file_snapshots"),
                "freshness_baselines": _count(conn, "freshness_baselines"),
            }
            if target_counts != source_counts:
                raise RuntimeError(f"row counts changed: source={source_counts}, target={target_counts}")
            violations = conn.execute("PRAGMA foreign_key_check").fetchall()
            if violations:
                raise RuntimeError(f"target foreign key check failed: {violations}")
            if conn.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
                raise RuntimeError("target integrity check failed")
            conn.execute("PRAGMA user_version = 7")
            conn.execute("COMMIT")
        except Exception:
            conn.execute("ROLLBACK")
            raise
    finally:
        conn.execute("PRAGMA foreign_keys = ON")
        conn.close()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "database",
        nargs="?",
        type=Path,
        default=Path("kb/reports/review-store.sqlite"),
        help="Review-store SQLite path (default: kb/reports/review-store.sqlite).",
    )
    args = parser.parse_args(argv)
    try:
        migrate(args.database)
    except (OSError, sqlite3.Error, RuntimeError) as exc:
        parser.error(str(exc))
    print(f"migrated {args.database} directly from review schema v5 to v7")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
