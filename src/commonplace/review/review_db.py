#!/usr/bin/env python3
"""Helpers for the canonical review-store SQLite database."""

from __future__ import annotations

import os
import sqlite3
from hashlib import sha256
from dataclasses import dataclass
from datetime import UTC, datetime
from importlib import resources
from pathlib import Path
from typing import Callable, Mapping, Sequence

from commonplace.review.paths import gate_id_from_stored_path
from commonplace.review.protocol.decisions import normalize_review_decision

DEFAULT_DB_PATH = Path("kb/reports/review-store.sqlite")
SCHEMA_PATH = "review-schema.sql"
DB_ENV_VAR = "COMMONPLACE_REVIEW_DB"
PACKING_VALUES = frozenset({"note", "gate"})
JOB_STATUS_VALUES = frozenset({"queued", "running", "completed", "failed"})
BUNDLE_ARTIFACTS_ROOT = Path("kb/reports/bundle-reviews")
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


@dataclass(frozen=True)
class ReviewFileSnapshot:
    snapshot_id: int
    path: str
    content_sha256: str
    content_text: str


@dataclass(frozen=True)
class AcceptanceState:
    note_path: str
    gate_path: str
    model_partition: str
    accepted_review_pair_id: int | None
    accepted_note_snapshot_id: int | None
    accepted_gate_snapshot_id: int | None
    accepted_note_hash: str | None
    accepted_gate_hash: str | None
    accepted_note_text: str | None
    accepted_gate_text: str | None
    accepted_at: str

    @property
    def gate_id(self) -> str:
        return gate_id_from_stored_path(self.gate_path)


@dataclass(frozen=True)
class ReviewJobRow:
    review_job_id: int
    model_partition: str
    runner: str | None
    runner_model: str | None
    runner_effort: str | None
    created_at: str
    started_at: str | None
    completed_at: str | None
    status: str
    failure_reason: str | None
    telemetry_json: str | None
    prompt_path: str | None
    bundle_output_path: str | None
    packing: str


@dataclass(frozen=True)
class ReviewPairRow:
    review_pair_id: int
    review_job_id: int
    note_path: str
    gate_path: str
    model_partition: str
    pair_ordinal: int
    pair_status: str
    decision: str | None
    result_path: str | None
    reviewed_note_snapshot_id: int | None
    reviewed_gate_snapshot_id: int | None
    reviewed_at: str | None

    @property
    def gate_id(self) -> str:
        return gate_id_from_stored_path(self.gate_path)


@dataclass(frozen=True)
class ReviewPairRequest:
    note_path: str
    gate_path: str
    pair_ordinal: int
    reviewed_note_snapshot_id: int | None = None
    reviewed_gate_snapshot_id: int | None = None


@dataclass(frozen=True)
class ReviewPairCompletion:
    note_path: str
    gate_path: str
    decision: str
    reviewed_at: str | None = None


@dataclass(frozen=True)
class NotePathUpdateCounts:
    review_pairs: int = 0
    acceptance_events: int = 0

    @property
    def total(self) -> int:
        return self.review_pairs + self.acceptance_events


@dataclass(frozen=True)
class ModelPartitionUpdateCounts:
    review_jobs: int = 0
    acceptance_events: int = 0

    @property
    def total(self) -> int:
        return self.review_jobs + self.acceptance_events


@dataclass(frozen=True)
class ReviewJobPlan:
    review_job_id: int
    model_partition: str
    runner: str | None
    runner_model: str | None
    runner_effort: str | None
    created_at: str
    started_at: str | None
    completed_at: str | None
    status: str
    failure_reason: str | None
    telemetry_json: str | None
    prompt_path: str | None
    bundle_output_path: str | None
    packing: str
    pairs: tuple[ReviewPairRow, ...]


def connect(db_path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def resolve_db_path(repo_root: Path, db_override: str | None = None) -> Path:
    if db_override:
        return Path(db_override).resolve()
    raw = os.environ.get(DB_ENV_VAR, "").strip()
    if raw:
        db_path = Path(raw)
        if not db_path.is_absolute():
            db_path = repo_root / db_path
        return db_path
    return repo_root / DEFAULT_DB_PATH


def ensure_db(db_path: Path) -> None:
    with resources.as_file(resources.files("commonplace.review") / SCHEMA_PATH) as schema_path:
        init_db(db_path, schema_path)


def prepare_review_db(repo_root: Path, db_override: str | None = None) -> Path:
    """Resolve the review DB path (honoring --db override) and ensure its schema."""
    db_path = resolve_db_path(repo_root, db_override)
    ensure_db(db_path)
    return db_path


def apply_schema(conn: sqlite3.Connection, schema_path: Path) -> None:
    conn.executescript(schema_path.read_text(encoding="utf-8"))


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


def init_db(db_path: Path, schema_path: Path) -> None:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = connect(db_path)
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


def _now_utc_iso() -> str:
    return datetime.now(UTC).isoformat()


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


def review_job_artifact_dir_rel(review_job_id: int) -> str:
    return (BUNDLE_ARTIFACTS_ROOT / f"review-job-{review_job_id}").as_posix()


def snapshot_file(conn: sqlite3.Connection, *, repo_root: Path, path: str) -> ReviewFileSnapshot:
    normalized_path = Path(path).as_posix()
    path_parts = Path(normalized_path).parts
    if (
        Path(normalized_path).is_absolute()
        or normalized_path == "."
        or normalized_path.startswith("../")
        or ".." in path_parts
    ):
        raise ValueError(f"snapshot path must be repo-relative: {path}")
    content_text = (repo_root / normalized_path).read_text(encoding="utf-8")
    content_sha256 = sha256(content_text.encode("utf-8")).hexdigest()
    captured_at = _now_utc_iso()
    conn.execute(
        """
        INSERT OR IGNORE INTO review_file_snapshots (
            path,
            content_sha256,
            content_text,
            captured_at
        ) VALUES (?, ?, ?, ?)
        """,
        (normalized_path, content_sha256, content_text, captured_at),
    )
    conn.execute(
        """
        UPDATE review_file_snapshots
        SET content_text = ?,
            captured_at = ?
        WHERE path = ?
          AND content_sha256 = ?
          AND content_text IS NULL
        """,
        (content_text, captured_at, normalized_path, content_sha256),
    )
    row = conn.execute(
        """
        SELECT snapshot_id, path, content_sha256, content_text
        FROM review_file_snapshots
        WHERE path = ?
          AND content_sha256 = ?
        """,
        (normalized_path, content_sha256),
    ).fetchone()
    if row is None:
        raise RuntimeError(f"failed to load review file snapshot: {normalized_path}")
    return ReviewFileSnapshot(
        snapshot_id=row["snapshot_id"],
        path=row["path"],
        content_sha256=row["content_sha256"],
        content_text=row["content_text"],
    )


def _review_job_from_row(row: sqlite3.Row) -> ReviewJobRow:
    return ReviewJobRow(
        review_job_id=row["review_job_id"],
        model_partition=row["model_partition"],
        runner=row["runner"],
        runner_model=row["runner_model"],
        runner_effort=row["runner_effort"],
        created_at=row["created_at"],
        started_at=row["started_at"],
        completed_at=row["completed_at"],
        status=row["status"],
        failure_reason=row["failure_reason"],
        telemetry_json=row["telemetry_json"],
        prompt_path=row["prompt_path"],
        bundle_output_path=row["bundle_output_path"],
        packing=row["packing"],
    )


def _review_pair_from_row(row: sqlite3.Row) -> ReviewPairRow:
    return ReviewPairRow(
        review_pair_id=row["review_pair_id"],
        review_job_id=row["review_job_id"],
        note_path=row["note_path"],
        gate_path=row["gate_path"],
        model_partition=row["model_partition"],
        pair_ordinal=row["pair_ordinal"],
        pair_status=row["pair_status"],
        decision=row["decision"],
        result_path=row["result_path"],
        reviewed_note_snapshot_id=row["reviewed_note_snapshot_id"],
        reviewed_gate_snapshot_id=row["reviewed_gate_snapshot_id"],
        reviewed_at=row["reviewed_at"],
    )


def create_job(
    conn: sqlite3.Connection,
    *,
    model_partition: str,
    runner: str | None,
    created_at: str,
    started_at: str | None,
    packing: str,
    status: str,
    runner_model: str | None = None,
    runner_effort: str | None = None,
    completed_at: str | None = None,
    failure_reason: str | None = None,
    telemetry_json: str | None = None,
    prompt_path: str | None = None,
    bundle_output_path: str | None = None,
) -> int:
    if packing not in PACKING_VALUES:
        raise ValueError(f"invalid review job packing: {packing}")
    if status not in JOB_STATUS_VALUES:
        raise ValueError(f"invalid review job status: {status}")
    cursor = conn.execute(
        """
        INSERT INTO review_jobs (
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
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
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
            packing,
        ),
    )
    return int(cursor.lastrowid)


def create_review_pairs(
    conn: sqlite3.Connection,
    *,
    review_job_id: int,
    pairs: Sequence[ReviewPairRequest],
    pair_status: str = "pending",
) -> list[int]:
    review_pair_ids: list[int] = []
    for pair in pairs:
        cursor = conn.execute(
            """
            INSERT INTO review_pairs (
                review_job_id,
                note_path,
                gate_path,
                pair_ordinal,
                pair_status,
                reviewed_note_snapshot_id,
                reviewed_gate_snapshot_id
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                review_job_id,
                pair.note_path,
                pair.gate_path,
                pair.pair_ordinal,
                pair_status,
                pair.reviewed_note_snapshot_id,
                pair.reviewed_gate_snapshot_id,
            ),
        )
        review_pair_ids.append(int(cursor.lastrowid))
    return review_pair_ids


def create_job_with_pairs(
    conn: sqlite3.Connection,
    *,
    model_partition: str,
    runner: str | None,
    created_at: str,
    started_at: str | None,
    status: str,
    packing: str,
    pairs: Sequence[ReviewPairRequest],
    runner_model: str | None = None,
    runner_effort: str | None = None,
    prompt_path: str | None = None,
    bundle_output_path: str | None = None,
) -> int:
    review_job_id = create_job(
        conn,
        model_partition=model_partition,
        runner=runner,
        runner_model=runner_model,
        runner_effort=runner_effort,
        created_at=created_at,
        started_at=started_at,
        packing=packing,
        status=status,
        prompt_path=prompt_path,
        bundle_output_path=bundle_output_path,
    )
    create_review_pairs(conn, review_job_id=review_job_id, pairs=pairs)
    return review_job_id


def load_review_job(conn: sqlite3.Connection, *, review_job_id: int) -> ReviewJobRow | None:
    row = conn.execute(
        """
        SELECT
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
        FROM review_jobs
        WHERE review_job_id = ?
        """,
        (review_job_id,),
    ).fetchone()
    if row is None:
        return None
    return _review_job_from_row(row)


def load_review_pairs_for_job(conn: sqlite3.Connection, *, review_job_id: int) -> list[ReviewPairRow]:
    rows = conn.execute(
        """
        SELECT
            rp.review_pair_id,
            rp.review_job_id,
            rp.note_path,
            rp.gate_path,
            j.model_partition AS model_partition,
            rp.pair_ordinal,
            rp.pair_status,
            rp.decision,
            rp.result_path,
            rp.reviewed_note_snapshot_id,
            rp.reviewed_gate_snapshot_id,
            rp.reviewed_at
        FROM review_pairs AS rp
        JOIN review_jobs AS j
          ON j.review_job_id = rp.review_job_id
        WHERE rp.review_job_id = ?
        ORDER BY rp.pair_ordinal, rp.note_path, rp.gate_path
        """,
        (review_job_id,),
    ).fetchall()
    return [_review_pair_from_row(row) for row in rows]


def load_completed_review_pairs_for_job(conn: sqlite3.Connection, *, review_job_id: int) -> list[ReviewPairRow]:
    return [pair for pair in load_review_pairs_for_job(conn, review_job_id=review_job_id) if pair.pair_status == "completed"]


def _job_plan_from_job(conn: sqlite3.Connection, job: ReviewJobRow, *, require_paths: bool) -> ReviewJobPlan:
    pairs = tuple(load_review_pairs_for_job(conn, review_job_id=job.review_job_id))
    if require_paths:
        missing: list[str] = []
        if job.prompt_path is None:
            missing.append("prompt_path")
        if job.bundle_output_path is None:
            missing.append("bundle_output_path")
        missing_pair_ids = [str(pair.review_pair_id) for pair in pairs if pair.result_path is None]
        if missing_pair_ids:
            missing.append(f"result_path for review_pair_id(s): {', '.join(missing_pair_ids)}")
        if missing:
            raise ValueError(
                f"review job {job.review_job_id} is missing load-bearing path(s): {', '.join(missing)}"
            )
    return ReviewJobPlan(
        review_job_id=job.review_job_id,
        model_partition=job.model_partition,
        runner=job.runner,
        runner_model=job.runner_model,
        runner_effort=job.runner_effort,
        created_at=job.created_at,
        started_at=job.started_at,
        completed_at=job.completed_at,
        status=job.status,
        failure_reason=job.failure_reason,
        telemetry_json=job.telemetry_json,
        prompt_path=job.prompt_path,
        bundle_output_path=job.bundle_output_path,
        packing=job.packing,
        pairs=pairs,
    )


def load_review_job_plan(
    conn: sqlite3.Connection,
    *,
    review_job_id: int,
    require_paths: bool = False,
) -> ReviewJobPlan | None:
    job = load_review_job(conn, review_job_id=review_job_id)
    if job is None:
        return None
    return _job_plan_from_job(conn, job, require_paths=require_paths)


def list_review_job_plans(
    conn: sqlite3.Connection,
    *,
    status: str | None = None,
    model_partition: str | None = None,
    require_paths: bool = False,
) -> list[ReviewJobPlan]:
    where_clauses: list[str] = []
    params: list[str] = []
    if status is not None:
        where_clauses.append("status = ?")
        params.append(status)
    if model_partition is not None:
        where_clauses.append("model_partition = ?")
        params.append(model_partition)
    where_sql = f"WHERE {' AND '.join(where_clauses)}" if where_clauses else ""
    rows = conn.execute(
        f"""
        SELECT
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
        FROM review_jobs
        {where_sql}
        ORDER BY created_at ASC, review_job_id ASC
        """,
        tuple(params),
    ).fetchall()
    return [
        _job_plan_from_job(conn, _review_job_from_row(row), require_paths=require_paths)
        for row in rows
    ]


def set_job_artifact_paths(
    conn: sqlite3.Connection,
    *,
    review_job_id: int,
    prompt_path: str | None = None,
    bundle_output_path: str | None = None,
    result_paths: Mapping[int, str] | None = None,
) -> None:
    if prompt_path is not None:
        conn.execute(
            """
            UPDATE review_jobs
            SET prompt_path = ?
            WHERE review_job_id = ?
            """,
            (prompt_path, review_job_id),
        )
    if bundle_output_path is not None:
        conn.execute(
            """
            UPDATE review_jobs
            SET bundle_output_path = ?
            WHERE review_job_id = ?
            """,
            (bundle_output_path, review_job_id),
        )
    for review_pair_id, path in (result_paths or {}).items():
        conn.execute(
            """
            UPDATE review_pairs
            SET result_path = ?
            WHERE review_job_id = ?
              AND review_pair_id = ?
            """,
            (path, review_job_id, review_pair_id),
        )


def load_current_acceptances(conn: sqlite3.Connection) -> dict[tuple[str, str, str], AcceptanceState]:
    rows = conn.execute(
        """
        SELECT
            note_path,
            gate_path,
            model_partition,
            accepted_review_pair_id,
            accepted_note_snapshot_id,
            accepted_gate_snapshot_id,
            accepted_note_hash,
            accepted_gate_hash,
            accepted_note_text,
            accepted_gate_text,
            accepted_at
        FROM current_gate_acceptances
        """
    ).fetchall()
    return {
        (row["note_path"], row["gate_path"], row["model_partition"]): AcceptanceState(
            note_path=row["note_path"],
            gate_path=row["gate_path"],
            model_partition=row["model_partition"],
            accepted_review_pair_id=row["accepted_review_pair_id"],
            accepted_note_snapshot_id=row["accepted_note_snapshot_id"],
            accepted_gate_snapshot_id=row["accepted_gate_snapshot_id"],
            accepted_note_hash=row["accepted_note_hash"],
            accepted_gate_hash=row["accepted_gate_hash"],
            accepted_note_text=row["accepted_note_text"],
            accepted_gate_text=row["accepted_gate_text"],
            accepted_at=row["accepted_at"],
        )
        for row in rows
    }


def attach_execution_data(
    conn: sqlite3.Connection,
    *,
    review_job_id: int,
    telemetry_json: str | None = None,
    runner_model: str | None = None,
    runner_effort: str | None = None,
) -> None:
    conn.execute(
        """
        UPDATE review_jobs
        SET telemetry_json = COALESCE(?, telemetry_json),
            runner_model = COALESCE(?, runner_model),
            runner_effort = COALESCE(?, runner_effort)
        WHERE review_job_id = ?
        """,
        (telemetry_json, runner_model, runner_effort, review_job_id),
    )


def complete_review_job(
    conn: sqlite3.Connection,
    *,
    review_job_id: int,
    completed_at: str,
    telemetry_json: str | None = None,
) -> None:
    conn.execute(
        """
        UPDATE review_jobs
        SET status = 'completed',
            completed_at = ?,
            telemetry_json = COALESCE(?, telemetry_json),
            failure_reason = NULL
        WHERE review_job_id = ?
        """,
        (completed_at, telemetry_json, review_job_id),
    )


def fail_review_job(
    conn: sqlite3.Connection,
    *,
    review_job_id: int,
    failure_reason: str,
    completed_at: str,
    telemetry_json: str | None = None,
) -> None:
    conn.execute(
        """
        UPDATE review_jobs
        SET status = 'failed',
            completed_at = ?,
            failure_reason = ?,
            telemetry_json = COALESCE(?, telemetry_json)
        WHERE review_job_id = ?
        """,
        (
            completed_at,
            failure_reason,
            telemetry_json,
            review_job_id,
        ),
    )


def complete_review_pairs(
    conn: sqlite3.Connection,
    *,
    review_job_id: int,
    review_pairs: Sequence[ReviewPairCompletion],
    reviewed_at: str,
) -> list[int]:
    requested = {
        (pair.note_path, pair.gate_path): pair
        for pair in load_review_pairs_for_job(conn, review_job_id=review_job_id)
    }
    completed_pair_ids: list[int] = []
    seen: set[tuple[str, str]] = set()
    for review_pair in review_pairs:
        key = (review_pair.note_path, review_pair.gate_path)
        if key in seen:
            raise ValueError(f"duplicate completed pair: {review_pair.note_path} :: {review_pair.gate_path}")
        seen.add(key)
        requested_pair = requested.get(key)
        if requested_pair is None:
            raise ValueError(
                f"pair {review_pair.note_path} :: {review_pair.gate_path} is not part of review job {review_job_id}"
            )
        normalized_decision = normalize_review_decision(review_pair.decision)
        if normalized_decision is None:
            raise ValueError(f"invalid review decision: {review_pair.decision}")
        conn.execute(
            """
            UPDATE review_pairs
            SET pair_status = 'completed',
                decision = ?,
                reviewed_at = ?
            WHERE review_pair_id = ?
            """,
            (
                normalized_decision,
                review_pair.reviewed_at or reviewed_at,
                requested_pair.review_pair_id,
            ),
        )
        completed_pair_ids.append(requested_pair.review_pair_id)
    return completed_pair_ids


def mark_missing_pairs(
    conn: sqlite3.Connection,
    *,
    review_job_id: int,
    pairs: Sequence[tuple[str, str]] | None = None,
) -> int:
    if pairs is None:
        cursor = conn.execute(
            """
            UPDATE review_pairs
            SET pair_status = 'missing'
            WHERE review_job_id = ?
              AND pair_status != 'completed'
            """,
            (review_job_id,),
        )
        return int(cursor.rowcount or 0)

    count = 0
    for note_path, gate_path in pairs:
        cursor = conn.execute(
            """
            UPDATE review_pairs
            SET pair_status = 'missing'
            WHERE review_job_id = ?
              AND note_path = ?
              AND gate_path = ?
              AND pair_status != 'completed'
            """,
            (review_job_id, note_path, gate_path),
        )
        count += int(cursor.rowcount or 0)
    return count


def append_acceptance_event(
    conn: sqlite3.Connection,
    *,
    note_path: str,
    gate_path: str,
    model_partition: str,
    accepted_review_pair_id: int | None,
    accepted_note_snapshot_id: int | None = None,
    accepted_gate_snapshot_id: int | None = None,
    accepted_at: str,
) -> int:
    cursor = conn.execute(
        """
        INSERT INTO acceptance_events (
            note_path,
            gate_path,
            model_partition,
            accepted_review_pair_id,
            accepted_note_snapshot_id,
            accepted_gate_snapshot_id,
            accepted_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            note_path,
            gate_path,
            model_partition,
            accepted_review_pair_id,
            accepted_note_snapshot_id,
            accepted_gate_snapshot_id,
            accepted_at,
        ),
    )
    return int(cursor.lastrowid)


def count_note_path_records(
    conn: sqlite3.Connection,
    *,
    note_path: str,
) -> NotePathUpdateCounts:
    def count_rows(table: str) -> int:
        row = conn.execute(
            f"SELECT COUNT(*) AS count FROM {table} WHERE note_path = ?",
            (note_path,),
        ).fetchone()
        return int(row["count"]) if row is not None else 0

    return NotePathUpdateCounts(
        review_pairs=count_rows("review_pairs"),
        acceptance_events=count_rows("acceptance_events"),
    )


def rekey_note_path(
    conn: sqlite3.Connection,
    *,
    old_note_path: str,
    new_note_path: str,
) -> NotePathUpdateCounts:
    if old_note_path == new_note_path:
        return NotePathUpdateCounts()

    def update_rows(table: str) -> int:
        cursor = conn.execute(
            f"UPDATE {table} SET note_path = ? WHERE note_path = ?",
            (new_note_path, old_note_path),
        )
        return int(cursor.rowcount or 0)

    return NotePathUpdateCounts(
        review_pairs=update_rows("review_pairs"),
        acceptance_events=update_rows("acceptance_events"),
    )


def count_model_partition_records(
    conn: sqlite3.Connection,
    *,
    model_partition: str,
) -> ModelPartitionUpdateCounts:
    def count_rows(table: str) -> int:
        row = conn.execute(
            f"SELECT COUNT(*) AS count FROM {table} WHERE model_partition = ?",
            (model_partition,),
        ).fetchone()
        return int(row["count"]) if row is not None else 0

    return ModelPartitionUpdateCounts(
        review_jobs=count_rows("review_jobs"),
        acceptance_events=count_rows("acceptance_events"),
    )


def rekey_model_partition(
    conn: sqlite3.Connection,
    *,
    old_model_partition: str,
    new_model_partition: str,
) -> ModelPartitionUpdateCounts:
    if old_model_partition == new_model_partition:
        return ModelPartitionUpdateCounts()

    def update_rows(table: str) -> int:
        cursor = conn.execute(
            f"UPDATE {table} SET model_partition = ? WHERE model_partition = ?",
            (new_model_partition, old_model_partition),
        )
        return int(cursor.rowcount or 0)

    return ModelPartitionUpdateCounts(
        review_jobs=update_rows("review_jobs"),
        acceptance_events=update_rows("acceptance_events"),
    )


def prune_obsolete_snapshot_content(conn: sqlite3.Connection) -> int:
    """Drop retained text for snapshots not needed for freshness or in-flight prompts."""
    conn.execute(
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
        UPDATE review_file_snapshots
        SET content_text = NULL
        WHERE content_text IS NOT NULL
          AND snapshot_id NOT IN (
              SELECT snapshot_id
              FROM retained_snapshots
          )
        """
    )
    row = conn.execute("SELECT changes() AS changed_rows").fetchone()
    return int(row["changed_rows"])


def load_review_pairs_for_note(
    conn: sqlite3.Connection,
    *,
    note_path: str,
    model_partition: str,
) -> list[ReviewPairRow]:
    rows = conn.execute(
        """
        SELECT
            rp.review_pair_id,
            rp.review_job_id,
            rp.note_path,
            rp.gate_path,
            j.model_partition AS model_partition,
            rp.pair_ordinal,
            rp.pair_status,
            rp.decision,
            rp.result_path,
            rp.reviewed_note_snapshot_id,
            rp.reviewed_gate_snapshot_id,
            rp.reviewed_at
        FROM review_pairs AS rp
        JOIN review_jobs AS j
          ON j.review_job_id = rp.review_job_id
        WHERE rp.note_path = ? AND j.model_partition = ?
        ORDER BY rp.gate_path, rp.reviewed_at, rp.review_pair_id
        """,
        (note_path, model_partition),
    ).fetchall()
    return [_review_pair_from_row(row) for row in rows]


def load_latest_completed_review_pair(
    conn: sqlite3.Connection,
    *,
    note_path: str,
    gate_path: str,
    model_partition: str,
) -> ReviewPairRow | None:
    row = conn.execute(
        """
        SELECT
            rp.review_pair_id,
            rp.review_job_id,
            rp.note_path,
            rp.gate_path,
            j.model_partition AS model_partition,
            rp.pair_ordinal,
            rp.pair_status,
            rp.decision,
            rp.result_path,
            rp.reviewed_note_snapshot_id,
            rp.reviewed_gate_snapshot_id,
            rp.reviewed_at
        FROM review_pairs AS rp
        JOIN review_jobs AS j
          ON j.review_job_id = rp.review_job_id
        WHERE rp.note_path = ?
          AND rp.gate_path = ?
          AND j.model_partition = ?
          AND rp.pair_status = 'completed'
        ORDER BY rp.reviewed_at DESC, rp.review_pair_id DESC
        LIMIT 1
        """,
        (note_path, gate_path, model_partition),
    ).fetchone()
    if row is None:
        return None
    return _review_pair_from_row(row)


def load_effective_review_pair_map(
    conn: sqlite3.Connection,
    *,
    note_path: str | None = None,
    model_partition: str | None,
) -> dict[tuple[str, str, str], ReviewPairRow]:
    where_clauses: list[str] = []
    params: list[str] = []
    if model_partition is not None:
        where_clauses.append("a.model_partition = ?")
        params.append(model_partition)
    if note_path is not None:
        where_clauses.append("a.note_path = ?")
        params.append(note_path)
    where_sql = ""
    if where_clauses:
        where_sql = "WHERE " + " AND ".join(where_clauses)
    rows = conn.execute(
        f"""
        WITH latest_review_pairs AS (
            SELECT
                rp.review_pair_id,
                rp.review_job_id,
                rp.note_path,
                rp.gate_path,
                j.model_partition AS model_partition,
                rp.pair_ordinal,
                rp.pair_status,
                rp.decision,
                rp.result_path,
                rp.reviewed_note_snapshot_id,
                rp.reviewed_gate_snapshot_id,
                rp.reviewed_at,
                ROW_NUMBER() OVER (
                    PARTITION BY rp.note_path, rp.gate_path, j.model_partition
                    ORDER BY rp.reviewed_at DESC, rp.review_pair_id DESC
                ) AS rn
            FROM review_pairs AS rp
            JOIN review_jobs AS j
              ON j.review_job_id = rp.review_job_id
            WHERE rp.pair_status = 'completed'
        ),
        accepted_review_pairs AS (
            SELECT
                rp.review_pair_id,
                rp.review_job_id,
                rp.note_path,
                rp.gate_path,
                j.model_partition AS model_partition,
                rp.pair_ordinal,
                rp.pair_status,
                rp.decision,
                rp.result_path,
                rp.reviewed_note_snapshot_id,
                rp.reviewed_gate_snapshot_id,
                rp.reviewed_at
            FROM review_pairs AS rp
            JOIN review_jobs AS j
              ON j.review_job_id = rp.review_job_id
        )
        SELECT
            COALESCE(accepted.review_pair_id, latest.review_pair_id) AS review_pair_id,
            COALESCE(accepted.review_job_id, latest.review_job_id) AS review_job_id,
            COALESCE(accepted.note_path, latest.note_path) AS note_path,
            COALESCE(accepted.gate_path, latest.gate_path) AS gate_path,
            COALESCE(accepted.model_partition, latest.model_partition, a.model_partition) AS model_partition,
            COALESCE(accepted.pair_ordinal, latest.pair_ordinal) AS pair_ordinal,
            COALESCE(accepted.pair_status, latest.pair_status) AS pair_status,
            COALESCE(accepted.decision, latest.decision) AS decision,
            COALESCE(accepted.result_path, latest.result_path) AS result_path,
            COALESCE(accepted.reviewed_note_snapshot_id, latest.reviewed_note_snapshot_id) AS reviewed_note_snapshot_id,
            COALESCE(accepted.reviewed_gate_snapshot_id, latest.reviewed_gate_snapshot_id) AS reviewed_gate_snapshot_id,
            COALESCE(accepted.reviewed_at, latest.reviewed_at) AS reviewed_at
        FROM current_gate_acceptances AS a
        LEFT JOIN accepted_review_pairs AS accepted
          ON accepted.review_pair_id = a.accepted_review_pair_id
        LEFT JOIN latest_review_pairs AS latest
          ON latest.note_path = a.note_path
         AND latest.gate_path = a.gate_path
         AND latest.model_partition = a.model_partition
         AND latest.rn = 1
        {where_sql}
        """,
        tuple(params),
    ).fetchall()
    result: dict[tuple[str, str, str], ReviewPairRow] = {}
    for row in rows:
        if row["review_pair_id"] is None:
            continue
        key = (row["note_path"], row["gate_path"], row["model_partition"])
        result[key] = _review_pair_from_row(row)
    return result
