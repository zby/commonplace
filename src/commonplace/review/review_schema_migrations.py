#!/usr/bin/env python3
"""Schema creation and migrations for the canonical review-store database."""

from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Callable

LATEST_REVIEW_SCHEMA_VERSION = 3
EXPECTED_REVIEW_TABLES = frozenset(
    {
        "review_jobs",
        "review_file_snapshots",
        "review_pairs",
        "acceptance_events",
    }
)
EXPECTED_REVIEW_INDEXES = frozenset(
    {
        "idx_review_jobs_model_partition_created",
        "idx_review_jobs_status",
        "idx_review_pairs_note_gate",
        "idx_review_pairs_review_job_id",
        "idx_review_pairs_pair_status",
        "idx_acceptance_events_note_gate_model_partition",
        "idx_acceptance_events_latest_by_key",
    }
)
EXPECTED_REVIEW_INDEXES_V2 = frozenset(
    {
        "idx_review_jobs_model_partition_created",
        "idx_review_jobs_status",
        "idx_review_pairs_note_gate_model_partition",
        "idx_review_pairs_review_job_id",
        "idx_review_pairs_pair_status",
        "idx_acceptance_events_note_gate_model_partition",
        "idx_acceptance_events_latest_by_key",
    }
)
EXPECTED_REVIEW_VIEWS = frozenset({"current_gate_acceptances", "stale_gate_pairs"})


def init_db(db_path: Path, schema_path: Path) -> None:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = _connect(db_path)
    try:
        has_review_jobs = _table_exists(conn, "review_jobs")
        has_review_runs = _table_exists(conn, "review_runs")
        if has_review_jobs and has_review_runs:
            raise RuntimeError("review DB contains both review_jobs and legacy review_runs tables")
        if not has_review_jobs and not has_review_runs:
            apply_schema(conn, schema_path)
            _set_user_version(conn, LATEST_REVIEW_SCHEMA_VERSION)
            _assert_review_store_integrity(conn)
            conn.commit()
            return

        current_version = _get_user_version(conn)
        if has_review_jobs and current_version < 2:
            raise RuntimeError(
                f"review DB has review_jobs table but user_version={current_version}; expected 2"
            )
        if current_version > LATEST_REVIEW_SCHEMA_VERSION:
            raise RuntimeError(
                f"review DB schema version {current_version} is newer than supported "
                f"{LATEST_REVIEW_SCHEMA_VERSION}"
            )
        for target_version in range(current_version + 1, LATEST_REVIEW_SCHEMA_VERSION + 1):
            migration = REVIEW_SCHEMA_MIGRATIONS.get(target_version)
            if migration is None:
                raise RuntimeError(f"missing review DB migration for version {target_version}")
            migration(conn)
            migrated_version = _get_user_version(conn)
            if migrated_version != target_version:
                raise RuntimeError(
                    f"review DB migration {target_version} left user_version={migrated_version}"
                )
        _assert_review_store_integrity(conn)
        conn.commit()
    finally:
        conn.close()


def apply_schema(conn: sqlite3.Connection, schema_path: Path) -> None:
    conn.executescript(schema_path.read_text(encoding="utf-8"))


def _connect(db_path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def _get_user_version(conn: sqlite3.Connection) -> int:
    row = conn.execute("PRAGMA user_version").fetchone()
    return int(row[0])


def _set_user_version(conn: sqlite3.Connection, version: int) -> None:
    conn.execute(f"PRAGMA user_version = {int(version)}")


def _schema_object_names(conn: sqlite3.Connection, object_type: str) -> set[str]:
    rows = conn.execute(
        """
        SELECT name
        FROM sqlite_master
        WHERE type = ?
        """,
        (object_type,),
    ).fetchall()
    return {str(row["name"]) for row in rows}


def _assert_expected_schema_objects(
    conn: sqlite3.Connection,
    *,
    expected_indexes: frozenset[str] | None = None,
) -> None:
    if expected_indexes is None:
        expected_indexes = EXPECTED_REVIEW_INDEXES
    missing_tables = EXPECTED_REVIEW_TABLES - _schema_object_names(conn, "table")
    missing_indexes = expected_indexes - _schema_object_names(conn, "index")
    missing_views = EXPECTED_REVIEW_VIEWS - _schema_object_names(conn, "view")
    if missing_tables or missing_indexes or missing_views:
        parts: list[str] = []
        if missing_tables:
            parts.append(f"missing tables: {', '.join(sorted(missing_tables))}")
        if missing_indexes:
            parts.append(f"missing indexes: {', '.join(sorted(missing_indexes))}")
        if missing_views:
            parts.append(f"missing views: {', '.join(sorted(missing_views))}")
        raise RuntimeError("; ".join(parts))


def _assert_foreign_key_integrity(conn: sqlite3.Connection) -> None:
    violations = conn.execute("PRAGMA foreign_key_check").fetchall()
    if violations:
        details = [
            f"{row['table']} rowid={row['rowid']} parent={row['parent']} fkid={row['fkid']}"
            for row in violations
        ]
        raise RuntimeError(f"foreign key check failed: {'; '.join(details)}")


def _assert_review_store_integrity(
    conn: sqlite3.Connection,
    *,
    expected_indexes: frozenset[str] | None = None,
) -> None:
    _assert_expected_schema_objects(conn, expected_indexes=expected_indexes)
    _assert_foreign_key_integrity(conn)


def _count_table_rows(conn: sqlite3.Connection, table_name: str) -> int:
    row = conn.execute(f"SELECT COUNT(*) AS count FROM {table_name}").fetchone()
    return int(row["count"]) if row is not None else 0


def _table_exists(conn: sqlite3.Connection, table_name: str) -> bool:
    row = conn.execute(
        """
        SELECT 1
        FROM sqlite_master
        WHERE type = 'table'
          AND name = ?
        """,
        (table_name,),
    ).fetchone()
    return row is not None


def _migrate_review_schema_v1(conn: sqlite3.Connection) -> None:
    review_run_count = _count_table_rows(conn, "review_runs")
    review_pair_count = _count_table_rows(conn, "review_pairs")
    conn.execute("PRAGMA foreign_keys = OFF")
    try:
        conn.execute("BEGIN IMMEDIATE")
        conn.execute(
            """
            CREATE TABLE review_runs_new (
                review_run_id INTEGER PRIMARY KEY,
                model_partition TEXT NOT NULL,
                runner TEXT NOT NULL,
                created_at TEXT NOT NULL,
                started_at TEXT,
                completed_at TEXT,
                status TEXT NOT NULL CHECK (
                    status IN ('queued', 'running', 'completed', 'failed')
                ),
                failure_reason TEXT,
                telemetry_json TEXT,
                bundle_output_path TEXT,
                packing TEXT NOT NULL CHECK (
                    packing IN ('note', 'gate')
                )
            )
            """
        )
        conn.execute(
            """
            INSERT INTO review_runs_new (
                review_run_id,
                model_partition,
                runner,
                created_at,
                started_at,
                completed_at,
                status,
                failure_reason,
                telemetry_json,
                bundle_output_path,
                packing
            )
            SELECT
                review_run_id,
                model_partition,
                runner,
                started_at AS created_at,
                started_at,
                completed_at,
                status,
                failure_reason,
                telemetry_json,
                bundle_output_path,
                packing
            FROM review_runs
            """
        )
        if _count_table_rows(conn, "review_runs_new") != review_run_count:
            raise RuntimeError("review_runs migration row count mismatch")
        conn.execute("DROP TABLE review_runs")
        conn.execute("ALTER TABLE review_runs_new RENAME TO review_runs")
        conn.execute(
            """
            CREATE INDEX idx_review_runs_model_partition_created
            ON review_runs(model_partition, created_at DESC)
            """
        )
        conn.execute(
            """
            CREATE INDEX idx_review_runs_status
            ON review_runs(status)
            """
        )
        if _count_table_rows(conn, "review_runs") != review_run_count:
            raise RuntimeError("review_runs row count changed during migration")
        if _count_table_rows(conn, "review_pairs") != review_pair_count:
            raise RuntimeError("review_pairs row count changed during migration")
        _set_user_version(conn, 1)
        _assert_foreign_key_integrity(conn)
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.execute("PRAGMA foreign_keys = ON")
    _assert_foreign_key_integrity(conn)


def _migrate_review_schema_v2(conn: sqlite3.Connection) -> None:
    review_job_count = _count_table_rows(conn, "review_runs")
    review_pair_count = _count_table_rows(conn, "review_pairs")
    conn.execute("PRAGMA legacy_alter_table = OFF")
    legacy_alter_table = conn.execute("PRAGMA legacy_alter_table").fetchone()
    if int(legacy_alter_table[0]) != 0:
        raise RuntimeError("review DB migration 2 requires PRAGMA legacy_alter_table = OFF")
    try:
        conn.execute("BEGIN IMMEDIATE")
        conn.execute("DROP INDEX IF EXISTS idx_review_runs_model_partition_created")
        conn.execute("DROP INDEX IF EXISTS idx_review_runs_status")
        conn.execute("DROP INDEX IF EXISTS idx_review_pairs_review_run_id")
        conn.execute("ALTER TABLE review_runs RENAME TO review_jobs")
        conn.execute("ALTER TABLE review_jobs RENAME COLUMN review_run_id TO review_job_id")
        conn.execute("ALTER TABLE review_pairs RENAME COLUMN review_run_id TO review_job_id")
        conn.execute(
            """
            CREATE INDEX idx_review_jobs_model_partition_created
            ON review_jobs(model_partition, created_at DESC)
            """
        )
        conn.execute(
            """
            CREATE INDEX idx_review_jobs_status
            ON review_jobs(status)
            """
        )
        conn.execute(
            """
            CREATE INDEX idx_review_pairs_review_job_id
            ON review_pairs(review_job_id)
            """
        )
        if _count_table_rows(conn, "review_jobs") != review_job_count:
            raise RuntimeError("review_jobs row count changed during migration")
        if _count_table_rows(conn, "review_pairs") != review_pair_count:
            raise RuntimeError("review_pairs row count changed during migration")
        if _table_exists(conn, "review_runs"):
            raise RuntimeError("review_runs table still exists after migration")
        _set_user_version(conn, 2)
        _assert_review_store_integrity(conn, expected_indexes=EXPECTED_REVIEW_INDEXES_V2)
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.execute("PRAGMA foreign_keys = ON")
    _assert_foreign_key_integrity(conn)


def _recreate_review_store_indexes_and_views(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE INDEX idx_review_jobs_model_partition_created
        ON review_jobs(model_partition, created_at DESC)
        """
    )
    conn.execute(
        """
        CREATE INDEX idx_review_jobs_status
        ON review_jobs(status)
        """
    )
    conn.execute(
        """
        CREATE INDEX idx_review_pairs_note_gate
        ON review_pairs(note_path, gate_path)
        """
    )
    conn.execute(
        """
        CREATE INDEX idx_review_pairs_review_job_id
        ON review_pairs(review_job_id)
        """
    )
    conn.execute(
        """
        CREATE INDEX idx_review_pairs_pair_status
        ON review_pairs(pair_status)
        """
    )
    conn.execute(
        """
        CREATE INDEX idx_acceptance_events_note_gate_model_partition
        ON acceptance_events(note_path, gate_path, model_partition, accepted_at DESC)
        """
    )
    conn.execute(
        """
        CREATE INDEX idx_acceptance_events_latest_by_key
        ON acceptance_events(note_path, gate_path, model_partition, acceptance_event_id DESC)
        """
    )
    conn.execute(
        """
        CREATE VIEW current_gate_acceptances AS
        SELECT
            e.note_path,
            e.gate_path,
            e.model_partition,
            e.accepted_review_pair_id,
            e.accepted_note_snapshot_id,
            e.accepted_gate_snapshot_id,
            note_snapshot.content_sha256 AS accepted_note_hash,
            gate_snapshot.content_sha256 AS accepted_gate_hash,
            note_snapshot.content_text AS accepted_note_text,
            gate_snapshot.content_text AS accepted_gate_text,
            e.accepted_at
        FROM acceptance_events AS e
        LEFT JOIN review_file_snapshots AS note_snapshot
          ON e.accepted_note_snapshot_id = note_snapshot.snapshot_id
        LEFT JOIN review_file_snapshots AS gate_snapshot
          ON e.accepted_gate_snapshot_id = gate_snapshot.snapshot_id
        JOIN (
            SELECT
                note_path,
                gate_path,
                model_partition,
                MAX(acceptance_event_id) AS max_id
            FROM acceptance_events
            GROUP BY note_path, gate_path, model_partition
        ) AS latest
          ON e.acceptance_event_id = latest.max_id
        """
    )
    conn.execute(
        """
        CREATE VIEW stale_gate_pairs AS
        SELECT
            a.note_path,
            a.gate_path,
            a.model_partition,
            a.accepted_note_snapshot_id,
            a.accepted_gate_snapshot_id,
            a.accepted_note_hash,
            a.accepted_gate_hash,
            a.accepted_note_text,
            a.accepted_gate_text
        FROM current_gate_acceptances AS a
        """
    )


def _migrate_review_schema_v3(conn: sqlite3.Connection) -> None:
    review_job_count = _count_table_rows(conn, "review_jobs")
    review_pair_count = _count_table_rows(conn, "review_pairs")
    conn.execute("PRAGMA foreign_keys = OFF")
    try:
        conn.execute("BEGIN IMMEDIATE")
        conn.execute("DROP VIEW IF EXISTS stale_gate_pairs")
        conn.execute("DROP VIEW IF EXISTS current_gate_acceptances")
        conn.execute("DROP INDEX IF EXISTS idx_review_jobs_model_partition_created")
        conn.execute("DROP INDEX IF EXISTS idx_review_jobs_status")
        conn.execute("DROP INDEX IF EXISTS idx_review_pairs_note_gate_model_partition")
        conn.execute("DROP INDEX IF EXISTS idx_review_pairs_review_job_id")
        conn.execute("DROP INDEX IF EXISTS idx_review_pairs_pair_status")
        conn.execute("DROP INDEX IF EXISTS idx_acceptance_events_note_gate_model_partition")
        conn.execute("DROP INDEX IF EXISTS idx_acceptance_events_latest_by_key")
        conn.execute(
            """
            CREATE TABLE review_jobs_new (
                review_job_id INTEGER PRIMARY KEY,
                model_partition TEXT NOT NULL,
                runner TEXT,
                runner_model TEXT,
                runner_effort TEXT,
                created_at TEXT NOT NULL,
                started_at TEXT,
                completed_at TEXT,
                status TEXT NOT NULL CHECK (
                    status IN ('queued', 'running', 'completed', 'failed')
                ),
                failure_reason TEXT,
                telemetry_json TEXT,
                prompt_path TEXT,
                bundle_output_path TEXT,
                packing TEXT NOT NULL CHECK (
                    packing IN ('note', 'gate')
                )
            )
            """
        )
        conn.execute(
            """
            INSERT INTO review_jobs_new (
                review_job_id,
                model_partition,
                runner,
                runner_model,
                runner_effort,
                created_at,
                started_at,
                completed_at,
                status,
                failure_reason,
                telemetry_json,
                prompt_path,
                bundle_output_path,
                packing
            )
            SELECT
                review_job_id,
                model_partition,
                runner,
                NULL AS runner_model,
                NULL AS runner_effort,
                created_at,
                started_at,
                completed_at,
                status,
                failure_reason,
                telemetry_json,
                NULL AS prompt_path,
                bundle_output_path,
                packing
            FROM review_jobs
            """
        )
        conn.execute(
            """
            CREATE TABLE review_pairs_new (
                review_pair_id INTEGER PRIMARY KEY,
                review_job_id INTEGER NOT NULL REFERENCES review_jobs(review_job_id) ON DELETE CASCADE,
                note_path TEXT NOT NULL,
                gate_path TEXT NOT NULL,
                pair_ordinal INTEGER NOT NULL,
                pair_status TEXT NOT NULL CHECK (
                    pair_status IN ('pending', 'completed', 'missing')
                ),
                decision TEXT CHECK (
                    decision IN ('pass', 'warn', 'fail', 'error', 'unknown')
                ),
                result_path TEXT,
                reviewed_note_snapshot_id INTEGER REFERENCES review_file_snapshots(snapshot_id),
                reviewed_gate_snapshot_id INTEGER REFERENCES review_file_snapshots(snapshot_id),
                reviewed_at TEXT,
                UNIQUE (review_job_id, note_path, gate_path),
                UNIQUE (review_job_id, pair_ordinal)
            )
            """
        )
        conn.execute(
            """
            INSERT INTO review_pairs_new (
                review_pair_id,
                review_job_id,
                note_path,
                gate_path,
                pair_ordinal,
                pair_status,
                decision,
                result_path,
                reviewed_note_snapshot_id,
                reviewed_gate_snapshot_id,
                reviewed_at
            )
            SELECT
                review_pair_id,
                review_job_id,
                note_path,
                gate_path,
                pair_ordinal,
                pair_status,
                decision,
                result_path,
                reviewed_note_snapshot_id,
                reviewed_gate_snapshot_id,
                reviewed_at
            FROM review_pairs
            """
        )
        if _count_table_rows(conn, "review_jobs_new") != review_job_count:
            raise RuntimeError("review_jobs migration row count mismatch")
        if _count_table_rows(conn, "review_pairs_new") != review_pair_count:
            raise RuntimeError("review_pairs migration row count mismatch")
        conn.execute("DROP TABLE review_pairs")
        conn.execute("DROP TABLE review_jobs")
        conn.execute("ALTER TABLE review_jobs_new RENAME TO review_jobs")
        conn.execute("ALTER TABLE review_pairs_new RENAME TO review_pairs")
        _recreate_review_store_indexes_and_views(conn)
        if _count_table_rows(conn, "review_jobs") != review_job_count:
            raise RuntimeError("review_jobs row count changed during migration")
        if _count_table_rows(conn, "review_pairs") != review_pair_count:
            raise RuntimeError("review_pairs row count changed during migration")
        _set_user_version(conn, 3)
        _assert_review_store_integrity(conn)
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.execute("PRAGMA foreign_keys = ON")
    _assert_foreign_key_integrity(conn)


REVIEW_SCHEMA_MIGRATIONS: dict[int, Callable[[sqlite3.Connection], None]] = {
    1: _migrate_review_schema_v1,
    2: _migrate_review_schema_v2,
    3: _migrate_review_schema_v3,
}
