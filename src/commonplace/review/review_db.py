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
from typing import Callable, Sequence

from commonplace.review.paths import normalize_gate_path
from commonplace.review.paths import gate_id_from_stored_path
from commonplace.review.protocol.decisions import normalize_review_decision

DEFAULT_DB_PATH = Path("kb/reports/review-store.sqlite")
SCHEMA_PATH = "review-schema.sql"
DB_ENV_VAR = "COMMONPLACE_REVIEW_DB"
PACKING_VALUES = frozenset({"note", "gate"})
REVIEW_KIND_VALUES = frozenset({"full-review"})
BASELINE_SCHEMA_MIGRATION = "review-pairs-v1"
MIGRATIONS_TABLE = "review_schema_migrations"


@dataclass(frozen=True)
class SchemaMigration:
    migration_name: str
    apply: Callable[[sqlite3.Connection, Path], None]


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
    accepted_note_sha: str
    accepted_note_commit: str | None
    accepted_gate_sha: str
    accepted_note_snapshot_id: int | None
    accepted_gate_snapshot_id: int | None
    accepted_note_hash: str | None
    accepted_gate_hash: str | None
    accepted_note_text: str | None
    accepted_gate_text: str | None
    accepted_at: str
    acceptance_kind: str

    @property
    def gate_id(self) -> str:
        return gate_id_from_stored_path(self.gate_path)


@dataclass(frozen=True)
class ReviewRunRow:
    review_run_id: int
    model_partition: str
    runner: str
    started_at: str
    completed_at: str | None
    status: str
    failure_reason: str | None
    telemetry_json: str | None
    raw_bundle_markdown: str | None
    debug_log: str | None
    packing: str


@dataclass(frozen=True)
class ReviewPairRow:
    review_pair_id: int
    review_run_id: int
    note_path: str
    gate_path: str
    model_partition: str
    pair_ordinal: int
    pair_status: str
    decision: str | None
    rationale_markdown: str | None
    evidence_json: str | None
    gate_sha: str
    reviewed_note_sha: str
    reviewed_note_commit: str | None
    reviewed_note_snapshot_id: int | None
    reviewed_gate_snapshot_id: int | None
    reviewed_at: str | None
    review_kind: str

    @property
    def gate_id(self) -> str:
        return gate_id_from_stored_path(self.gate_path)


@dataclass(frozen=True)
class ReviewPairRequest:
    note_path: str
    gate_path: str
    gate_sha: str
    reviewed_note_sha: str
    reviewed_note_commit: str | None
    pair_ordinal: int
    reviewed_note_snapshot_id: int | None = None
    reviewed_gate_snapshot_id: int | None = None
    review_kind: str = "full-review"


@dataclass(frozen=True)
class PendingReviewPair:
    note_path: str
    gate_path: str
    decision: str
    rationale_markdown: str
    evidence_json: str | None = None
    reviewed_at: str | None = None
    review_kind: str = "full-review"


@dataclass(frozen=True)
class NotePathUpdateCounts:
    review_pairs: int = 0
    acceptance_events: int = 0

    @property
    def total(self) -> int:
        return self.review_pairs + self.acceptance_events


@dataclass(frozen=True)
class ModelPartitionUpdateCounts:
    review_runs: int = 0
    review_pairs: int = 0
    acceptance_events: int = 0

    @property
    def total(self) -> int:
        return self.review_runs + self.review_pairs + self.acceptance_events


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


def ensure_db(repo_root: Path, db_path: Path) -> None:
    with resources.as_file(resources.files("commonplace.review") / SCHEMA_PATH) as schema_path:
        init_db(db_path, schema_path, repo_root=repo_root)


def prepare_review_db(repo_root: Path, db_override: str | None = None) -> Path:
    """Resolve the review DB path (honoring --db override) and ensure its schema."""
    db_path = resolve_db_path(repo_root, db_override)
    ensure_db(repo_root, db_path)
    return db_path


def apply_schema(conn: sqlite3.Connection, schema_path: Path) -> None:
    conn.executescript(schema_path.read_text(encoding="utf-8"))


def init_db(db_path: Path, schema_path: Path, *, repo_root: Path) -> None:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    with connect(db_path) as conn:
        if not _table_exists(conn, "review_runs"):
            apply_schema(conn, schema_path)
        apply_schema_migrations(conn, repo_root=repo_root)
        conn.commit()


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


def _migration_table_columns(conn: sqlite3.Connection) -> set[str]:
    return {row["name"] for row in conn.execute(f"PRAGMA table_info({MIGRATIONS_TABLE})").fetchall()}


def _table_columns(conn: sqlite3.Connection, table_name: str) -> set[str]:
    return {row["name"] for row in conn.execute(f"PRAGMA table_info({table_name})").fetchall()}


def _create_migration_table(conn: sqlite3.Connection) -> None:
    conn.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {MIGRATIONS_TABLE} (
            migration_name TEXT PRIMARY KEY,
            applied_at TEXT NOT NULL
        )
        """
    )


def _normalize_migration_table(conn: sqlite3.Connection) -> None:
    if not _table_exists(conn, MIGRATIONS_TABLE):
        _create_migration_table(conn)
        return

    columns = _migration_table_columns(conn)
    if {"migration_name", "applied_at"}.issubset(columns):
        return
    if {"version", "applied_at"}.issubset(columns):
        legacy_table = f"{MIGRATIONS_TABLE}_legacy_version"
        conn.execute(f"ALTER TABLE {MIGRATIONS_TABLE} RENAME TO {legacy_table}")
        _create_migration_table(conn)
        conn.execute(
            f"""
            INSERT OR IGNORE INTO {MIGRATIONS_TABLE} (migration_name, applied_at)
            SELECT version, applied_at
            FROM {legacy_table}
            """
        )
        conn.execute(f"DROP TABLE {legacy_table}")
        return

    raise RuntimeError(f"unsupported {MIGRATIONS_TABLE} shape: {sorted(columns)}")


def _record_migration(conn: sqlite3.Connection, migration_name: str) -> None:
    conn.execute(
        f"""
        INSERT OR IGNORE INTO {MIGRATIONS_TABLE} (migration_name, applied_at)
        VALUES (?, ?)
        """,
        (migration_name, _now_utc_iso()),
    )


def _applied_migration_names(conn: sqlite3.Connection) -> set[str]:
    rows = conn.execute(f"SELECT migration_name FROM {MIGRATIONS_TABLE}").fetchall()
    return {row["migration_name"] for row in rows}


def _add_column_if_missing(conn: sqlite3.Connection, table_name: str, column_name: str, column_sql: str) -> None:
    if column_name in _table_columns(conn, table_name):
        return
    conn.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_sql}")


def _model_partition_column(conn: sqlite3.Connection, table_name: str) -> str:
    columns = _table_columns(conn, table_name)
    if "model_partition" in columns:
        return "model_partition"
    if "model_id" in columns:
        return "model_id"
    raise RuntimeError(f"{table_name} has no model partition column")


def _gate_path_column(conn: sqlite3.Connection, table_name: str) -> str:
    columns = _table_columns(conn, table_name)
    if "gate_path" in columns:
        return "gate_path"
    if "gate_id" in columns:
        return "gate_id"
    raise RuntimeError(f"{table_name} has no gate path column")


def _create_current_acceptance_views(conn: sqlite3.Connection) -> None:
    gate_column = _gate_path_column(conn, "acceptance_events")
    model_column = _model_partition_column(conn, "acceptance_events")
    conn.executescript(
        f"""
        CREATE VIEW current_gate_acceptances AS
        SELECT
            e.note_path,
            e.{gate_column} AS {gate_column},
            e.{model_column} AS {model_column},
            e.accepted_review_pair_id,
            e.accepted_note_sha,
            e.accepted_note_commit,
            e.accepted_gate_sha,
            e.accepted_note_snapshot_id,
            e.accepted_gate_snapshot_id,
            note_snapshot.content_sha256 AS accepted_note_hash,
            gate_snapshot.content_sha256 AS accepted_gate_hash,
            note_snapshot.content_text AS accepted_note_text,
            gate_snapshot.content_text AS accepted_gate_text,
            e.accepted_at,
            e.acceptance_kind
        FROM acceptance_events AS e
        LEFT JOIN review_file_snapshots AS note_snapshot
          ON e.accepted_note_snapshot_id = note_snapshot.snapshot_id
        LEFT JOIN review_file_snapshots AS gate_snapshot
          ON e.accepted_gate_snapshot_id = gate_snapshot.snapshot_id
        JOIN (
            SELECT
                note_path,
                {gate_column},
                {model_column},
                MAX(acceptance_event_id) AS max_id
            FROM acceptance_events
            GROUP BY note_path, {gate_column}, {model_column}
        ) AS latest
          ON e.acceptance_event_id = latest.max_id;

        CREATE VIEW stale_gate_pairs AS
        SELECT
            a.note_path,
            a.{gate_column} AS {gate_column},
            a.{model_column} AS {model_column},
            a.accepted_note_sha,
            a.accepted_gate_sha,
            a.accepted_note_snapshot_id,
            a.accepted_gate_snapshot_id,
            a.accepted_note_hash,
            a.accepted_gate_hash,
            a.accepted_note_text,
            a.accepted_gate_text
        FROM current_gate_acceptances AS a;
        """
    )


def _migrate_review_file_snapshots(conn: sqlite3.Connection, repo_root: Path) -> None:
    del repo_root
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS review_file_snapshots (
            snapshot_id INTEGER PRIMARY KEY,
            path TEXT NOT NULL,
            content_sha256 TEXT NOT NULL,
            content_text TEXT,
            captured_at TEXT NOT NULL,
            UNIQUE (path, content_sha256)
        )
        """
    )
    _add_column_if_missing(
        conn,
        "review_pairs",
        "reviewed_note_snapshot_id",
        "reviewed_note_snapshot_id INTEGER REFERENCES review_file_snapshots(snapshot_id)",
    )
    _add_column_if_missing(
        conn,
        "review_pairs",
        "reviewed_gate_snapshot_id",
        "reviewed_gate_snapshot_id INTEGER REFERENCES review_file_snapshots(snapshot_id)",
    )
    _add_column_if_missing(
        conn,
        "acceptance_events",
        "accepted_note_snapshot_id",
        "accepted_note_snapshot_id INTEGER REFERENCES review_file_snapshots(snapshot_id)",
    )
    _add_column_if_missing(
        conn,
        "acceptance_events",
        "accepted_gate_snapshot_id",
        "accepted_gate_snapshot_id INTEGER REFERENCES review_file_snapshots(snapshot_id)",
    )
    conn.executescript(
        """
        DROP VIEW IF EXISTS stale_gate_pairs;
        DROP VIEW IF EXISTS current_gate_acceptances;
        """
    )
    _create_current_acceptance_views(conn)


def _rename_column_if_present(
    conn: sqlite3.Connection,
    *,
    table_name: str,
    old_name: str,
    new_name: str,
) -> None:
    columns = _table_columns(conn, table_name)
    if new_name in columns:
        return
    if old_name not in columns:
        raise RuntimeError(f"{table_name} has neither {old_name} nor {new_name}")
    conn.execute(f"ALTER TABLE {table_name} RENAME COLUMN {old_name} TO {new_name}")


def _migrate_model_partition(conn: sqlite3.Connection, repo_root: Path) -> None:
    del repo_root
    gate_column = _gate_path_column(conn, "review_pairs")
    conn.executescript(
        """
        DROP VIEW IF EXISTS stale_gate_pairs;
        DROP VIEW IF EXISTS current_gate_acceptances;
        DROP INDEX IF EXISTS idx_review_runs_model_started;
        DROP INDEX IF EXISTS idx_review_pairs_note_gate_model;
        DROP INDEX IF EXISTS idx_acceptance_events_note_gate_model;
        DROP INDEX IF EXISTS idx_acceptance_events_latest_by_key;
        """
    )
    _rename_column_if_present(
        conn,
        table_name="review_runs",
        old_name="model_id",
        new_name="model_partition",
    )
    _rename_column_if_present(
        conn,
        table_name="review_pairs",
        old_name="model_id",
        new_name="model_partition",
    )
    _rename_column_if_present(
        conn,
        table_name="acceptance_events",
        old_name="model_id",
        new_name="model_partition",
    )
    conn.executescript(
        f"""
        CREATE INDEX IF NOT EXISTS idx_review_runs_model_partition_started
        ON review_runs(model_partition, started_at DESC);

        CREATE INDEX IF NOT EXISTS idx_review_pairs_note_gate_model_partition
        ON review_pairs(note_path, {gate_column}, model_partition);

        CREATE INDEX IF NOT EXISTS idx_acceptance_events_note_gate_model_partition
        ON acceptance_events(note_path, {gate_column}, model_partition, accepted_at DESC);

        CREATE INDEX IF NOT EXISTS idx_acceptance_events_latest_by_key
        ON acceptance_events(note_path, {gate_column}, model_partition, acceptance_event_id DESC);
        """
    )
    _create_current_acceptance_views(conn)


def _legacy_gate_id_values(conn: sqlite3.Connection) -> list[str]:
    values: set[str] = set()
    for table_name in ("review_pairs", "acceptance_events"):
        if "gate_id" not in _table_columns(conn, table_name):
            continue
        rows = conn.execute(f"SELECT DISTINCT gate_id FROM {table_name}").fetchall()
        values.update(row["gate_id"] for row in rows if row["gate_id"])
    return sorted(values)


def _resolve_legacy_gate_ids(repo_root: Path, gate_ids: Sequence[str]) -> dict[str, str]:
    mapping: dict[str, str] = {}
    unresolved: list[str] = []
    for gate_id in gate_ids:
        try:
            mapping[gate_id] = normalize_gate_path(repo_root, gate_id)
        except (FileNotFoundError, ValueError):
            unresolved.append(gate_id)
    if unresolved:
        formatted = ", ".join(unresolved)
        raise ValueError(f"cannot resolve legacy review gate_id value(s): {formatted}")
    return mapping


def _migrate_gate_path(conn: sqlite3.Connection, repo_root: Path) -> None:
    gate_mapping = _resolve_legacy_gate_ids(repo_root, _legacy_gate_id_values(conn))
    conn.executescript(
        """
        DROP VIEW IF EXISTS stale_gate_pairs;
        DROP VIEW IF EXISTS current_gate_acceptances;
        DROP INDEX IF EXISTS idx_review_pairs_note_gate_model;
        DROP INDEX IF EXISTS idx_review_pairs_note_gate_model_partition;
        DROP INDEX IF EXISTS idx_acceptance_events_note_gate_model;
        DROP INDEX IF EXISTS idx_acceptance_events_note_gate_model_partition;
        DROP INDEX IF EXISTS idx_acceptance_events_latest_by_key;
        """
    )
    _rename_column_if_present(
        conn,
        table_name="review_pairs",
        old_name="gate_id",
        new_name="gate_path",
    )
    _rename_column_if_present(
        conn,
        table_name="acceptance_events",
        old_name="gate_id",
        new_name="gate_path",
    )
    for legacy_gate_id, gate_path in gate_mapping.items():
        conn.execute(
            """
            UPDATE review_pairs
            SET gate_path = ?
            WHERE gate_path = ?
            """,
            (gate_path, legacy_gate_id),
        )
        conn.execute(
            """
            UPDATE acceptance_events
            SET gate_path = ?
            WHERE gate_path = ?
            """,
            (gate_path, legacy_gate_id),
        )
    conn.executescript(
        """
        CREATE INDEX IF NOT EXISTS idx_review_pairs_note_gate_model_partition
        ON review_pairs(note_path, gate_path, model_partition);

        CREATE INDEX IF NOT EXISTS idx_acceptance_events_note_gate_model_partition
        ON acceptance_events(note_path, gate_path, model_partition, accepted_at DESC);

        CREATE INDEX IF NOT EXISTS idx_acceptance_events_latest_by_key
        ON acceptance_events(note_path, gate_path, model_partition, acceptance_event_id DESC);
        """
    )
    _create_current_acceptance_views(conn)


SCHEMA_MIGRATIONS: tuple[SchemaMigration, ...] = (
    SchemaMigration("review-file-snapshots-v1", _migrate_review_file_snapshots),
    SchemaMigration("review-model-partition-v1", _migrate_model_partition),
    SchemaMigration("review-gate-path-v1", _migrate_gate_path),
)


def apply_schema_migrations(conn: sqlite3.Connection, *, repo_root: Path) -> None:
    _normalize_migration_table(conn)
    if _table_exists(conn, "review_runs"):
        _record_migration(conn, BASELINE_SCHEMA_MIGRATION)

    applied = _applied_migration_names(conn)
    for migration in SCHEMA_MIGRATIONS:
        if migration.migration_name in applied:
            continue
        migration.apply(conn, repo_root)
        _record_migration(conn, migration.migration_name)
        applied.add(migration.migration_name)


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


def _review_run_from_row(row: sqlite3.Row) -> ReviewRunRow:
    return ReviewRunRow(
        review_run_id=row["review_run_id"],
        model_partition=row["model_partition"],
        runner=row["runner"],
        started_at=row["started_at"],
        completed_at=row["completed_at"],
        status=row["status"],
        failure_reason=row["failure_reason"],
        telemetry_json=row["telemetry_json"],
        raw_bundle_markdown=row["raw_bundle_markdown"],
        debug_log=row["debug_log"],
        packing=row["packing"],
    )


def _review_pair_from_row(row: sqlite3.Row) -> ReviewPairRow:
    return ReviewPairRow(
        review_pair_id=row["review_pair_id"],
        review_run_id=row["review_run_id"],
        note_path=row["note_path"],
        gate_path=row["gate_path"],
        model_partition=row["model_partition"],
        pair_ordinal=row["pair_ordinal"],
        pair_status=row["pair_status"],
        decision=row["decision"],
        rationale_markdown=row["rationale_markdown"],
        evidence_json=row["evidence_json"],
        gate_sha=row["gate_sha"],
        reviewed_note_sha=row["reviewed_note_sha"],
        reviewed_note_commit=row["reviewed_note_commit"],
        reviewed_note_snapshot_id=row["reviewed_note_snapshot_id"],
        reviewed_gate_snapshot_id=row["reviewed_gate_snapshot_id"],
        reviewed_at=row["reviewed_at"],
        review_kind=row["review_kind"],
    )


def create_run(
    conn: sqlite3.Connection,
    *,
    model_partition: str,
    runner: str,
    started_at: str,
    packing: str,
    completed_at: str | None = None,
    status: str = "running",
    failure_reason: str | None = None,
    telemetry_json: str | None = None,
    raw_bundle_markdown: str | None = None,
    debug_log: str | None = None,
) -> int:
    if packing not in PACKING_VALUES:
        raise ValueError(f"invalid review run packing: {packing}")
    cursor = conn.execute(
        """
        INSERT INTO review_runs (
            model_partition,
            runner,
            started_at,
            completed_at,
            status,
            failure_reason,
            telemetry_json,
            raw_bundle_markdown,
            debug_log,
            packing
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            model_partition,
            runner,
            started_at,
            completed_at,
            status,
            failure_reason,
            telemetry_json,
            raw_bundle_markdown,
            debug_log,
            packing,
        ),
    )
    return int(cursor.lastrowid)


def create_review_pairs(
    conn: sqlite3.Connection,
    *,
    review_run_id: int,
    model_partition: str,
    pairs: Sequence[ReviewPairRequest],
    pair_status: str = "pending",
) -> list[int]:
    review_pair_ids: list[int] = []
    for pair in pairs:
        if pair.review_kind not in REVIEW_KIND_VALUES:
            raise ValueError(f"invalid review kind: {pair.review_kind}")
        cursor = conn.execute(
            """
            INSERT INTO review_pairs (
                review_run_id,
                note_path,
                gate_path,
                model_partition,
                pair_ordinal,
                pair_status,
                gate_sha,
                reviewed_note_sha,
                reviewed_note_commit,
                reviewed_note_snapshot_id,
                reviewed_gate_snapshot_id,
                review_kind
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                review_run_id,
                pair.note_path,
                pair.gate_path,
                model_partition,
                pair.pair_ordinal,
                pair_status,
                pair.gate_sha,
                pair.reviewed_note_sha,
                pair.reviewed_note_commit,
                pair.reviewed_note_snapshot_id,
                pair.reviewed_gate_snapshot_id,
                pair.review_kind,
            ),
        )
        review_pair_ids.append(int(cursor.lastrowid))
    return review_pair_ids


def create_run_with_pairs(
    conn: sqlite3.Connection,
    *,
    model_partition: str,
    runner: str,
    started_at: str,
    packing: str,
    pairs: Sequence[ReviewPairRequest],
) -> int:
    review_run_id = create_run(
        conn,
        model_partition=model_partition,
        runner=runner,
        started_at=started_at,
        packing=packing,
        status="running",
    )
    create_review_pairs(conn, review_run_id=review_run_id, model_partition=model_partition, pairs=pairs)
    return review_run_id


def load_review_run(conn: sqlite3.Connection, *, review_run_id: int) -> ReviewRunRow | None:
    row = conn.execute(
        """
        SELECT
            review_run_id,
            model_partition,
            runner,
            started_at,
            completed_at,
            status,
            failure_reason,
            telemetry_json,
            raw_bundle_markdown,
            debug_log,
            packing
        FROM review_runs
        WHERE review_run_id = ?
        """,
        (review_run_id,),
    ).fetchone()
    if row is None:
        return None
    return _review_run_from_row(row)


def load_review_pairs_for_run(conn: sqlite3.Connection, *, review_run_id: int) -> list[ReviewPairRow]:
    rows = conn.execute(
        """
        SELECT
            review_pair_id,
            review_run_id,
            note_path,
            gate_path,
            model_partition,
            pair_ordinal,
            pair_status,
            decision,
            rationale_markdown,
            evidence_json,
            gate_sha,
            reviewed_note_sha,
            reviewed_note_commit,
            reviewed_note_snapshot_id,
            reviewed_gate_snapshot_id,
            reviewed_at,
            review_kind
        FROM review_pairs
        WHERE review_run_id = ?
        ORDER BY pair_ordinal, note_path, gate_path
        """,
        (review_run_id,),
    ).fetchall()
    return [_review_pair_from_row(row) for row in rows]


def load_completed_review_pairs_for_run(conn: sqlite3.Connection, *, review_run_id: int) -> list[ReviewPairRow]:
    return [pair for pair in load_review_pairs_for_run(conn, review_run_id=review_run_id) if pair.pair_status == "completed"]


def load_current_acceptances(conn: sqlite3.Connection) -> dict[tuple[str, str, str], AcceptanceState]:
    rows = conn.execute(
        """
        SELECT
            note_path,
            gate_path,
            model_partition,
            accepted_review_pair_id,
            accepted_note_sha,
            accepted_note_commit,
            accepted_gate_sha,
            accepted_note_snapshot_id,
            accepted_gate_snapshot_id,
            accepted_note_hash,
            accepted_gate_hash,
            accepted_note_text,
            accepted_gate_text,
            accepted_at,
            acceptance_kind
        FROM current_gate_acceptances
        """
    ).fetchall()
    return {
        (row["note_path"], row["gate_path"], row["model_partition"]): AcceptanceState(
            note_path=row["note_path"],
            gate_path=row["gate_path"],
            model_partition=row["model_partition"],
            accepted_review_pair_id=row["accepted_review_pair_id"],
            accepted_note_sha=row["accepted_note_sha"],
            accepted_note_commit=row["accepted_note_commit"],
            accepted_gate_sha=row["accepted_gate_sha"],
            accepted_note_snapshot_id=row["accepted_note_snapshot_id"],
            accepted_gate_snapshot_id=row["accepted_gate_snapshot_id"],
            accepted_note_hash=row["accepted_note_hash"],
            accepted_gate_hash=row["accepted_gate_hash"],
            accepted_note_text=row["accepted_note_text"],
            accepted_gate_text=row["accepted_gate_text"],
            accepted_at=row["accepted_at"],
            acceptance_kind=row["acceptance_kind"],
        )
        for row in rows
    }


def attach_execution_data(
    conn: sqlite3.Connection,
    *,
    review_run_id: int,
    telemetry_json: str | None = None,
    raw_bundle_markdown: str | None = None,
    debug_log: str | None = None,
) -> None:
    conn.execute(
        """
        UPDATE review_runs
        SET telemetry_json = COALESCE(?, telemetry_json),
            raw_bundle_markdown = COALESCE(?, raw_bundle_markdown),
            debug_log = COALESCE(?, debug_log)
        WHERE review_run_id = ?
        """,
        (telemetry_json, raw_bundle_markdown, debug_log, review_run_id),
    )


def complete_review_run(
    conn: sqlite3.Connection,
    *,
    review_run_id: int,
    completed_at: str,
    raw_bundle_markdown: str | None = None,
    debug_log: str | None = None,
    telemetry_json: str | None = None,
) -> None:
    conn.execute(
        """
        UPDATE review_runs
        SET status = 'completed',
            completed_at = ?,
            raw_bundle_markdown = COALESCE(?, raw_bundle_markdown),
            debug_log = COALESCE(?, debug_log),
            telemetry_json = COALESCE(?, telemetry_json),
            failure_reason = NULL
        WHERE review_run_id = ?
        """,
        (completed_at, raw_bundle_markdown, debug_log, telemetry_json, review_run_id),
    )


def fail_review_run(
    conn: sqlite3.Connection,
    *,
    review_run_id: int,
    failure_reason: str,
    completed_at: str,
    raw_bundle_markdown: str | None = None,
    debug_log: str | None = None,
    telemetry_json: str | None = None,
) -> None:
    conn.execute(
        """
        UPDATE review_runs
        SET status = 'failed',
            completed_at = ?,
            failure_reason = ?,
            raw_bundle_markdown = COALESCE(?, raw_bundle_markdown),
            debug_log = COALESCE(?, debug_log),
            telemetry_json = COALESCE(?, telemetry_json)
        WHERE review_run_id = ?
        """,
        (
            completed_at,
            failure_reason,
            raw_bundle_markdown,
            debug_log,
            telemetry_json,
            review_run_id,
        ),
    )


def complete_review_pairs(
    conn: sqlite3.Connection,
    *,
    review_run_id: int,
    review_pairs: Sequence[PendingReviewPair],
    reviewed_at: str,
) -> list[int]:
    requested = {
        (pair.note_path, pair.gate_path): pair
        for pair in load_review_pairs_for_run(conn, review_run_id=review_run_id)
    }
    completed_pair_ids: list[int] = []
    seen: set[tuple[str, str]] = set()
    for review_pair in review_pairs:
        if review_pair.review_kind not in REVIEW_KIND_VALUES:
            raise ValueError(f"invalid review kind: {review_pair.review_kind}")
        key = (review_pair.note_path, review_pair.gate_path)
        if key in seen:
            raise ValueError(f"duplicate completed pair: {review_pair.note_path} :: {review_pair.gate_path}")
        seen.add(key)
        requested_pair = requested.get(key)
        if requested_pair is None:
            raise ValueError(
                f"pair {review_pair.note_path} :: {review_pair.gate_path} is not part of review run {review_run_id}"
            )
        normalized_decision = normalize_review_decision(review_pair.decision)
        if normalized_decision is None:
            raise ValueError(f"invalid review decision: {review_pair.decision}")
        conn.execute(
            """
            UPDATE review_pairs
            SET pair_status = 'completed',
                decision = ?,
                rationale_markdown = ?,
                evidence_json = ?,
                reviewed_at = ?,
                review_kind = ?
            WHERE review_pair_id = ?
            """,
            (
                normalized_decision,
                review_pair.rationale_markdown,
                review_pair.evidence_json,
                review_pair.reviewed_at or reviewed_at,
                review_pair.review_kind,
                requested_pair.review_pair_id,
            ),
        )
        completed_pair_ids.append(requested_pair.review_pair_id)
    return completed_pair_ids


def mark_missing_pairs(
    conn: sqlite3.Connection,
    *,
    review_run_id: int,
    pairs: Sequence[tuple[str, str]] | None = None,
) -> int:
    if pairs is None:
        cursor = conn.execute(
            """
            UPDATE review_pairs
            SET pair_status = 'missing'
            WHERE review_run_id = ?
              AND pair_status != 'completed'
            """,
            (review_run_id,),
        )
        return int(cursor.rowcount or 0)

    count = 0
    for note_path, gate_path in pairs:
        cursor = conn.execute(
            """
            UPDATE review_pairs
            SET pair_status = 'missing'
            WHERE review_run_id = ?
              AND note_path = ?
              AND gate_path = ?
              AND pair_status != 'completed'
            """,
            (review_run_id, note_path, gate_path),
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
    accepted_note_sha: str,
    accepted_note_commit: str | None,
    accepted_gate_sha: str,
    accepted_note_snapshot_id: int | None = None,
    accepted_gate_snapshot_id: int | None = None,
    accepted_at: str,
    acceptance_kind: str,
) -> int:
    cursor = conn.execute(
        """
        INSERT INTO acceptance_events (
            note_path,
            gate_path,
            model_partition,
            accepted_review_pair_id,
            accepted_note_sha,
            accepted_note_commit,
            accepted_gate_sha,
            accepted_note_snapshot_id,
            accepted_gate_snapshot_id,
            accepted_at,
            acceptance_kind
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            note_path,
            gate_path,
            model_partition,
            accepted_review_pair_id,
            accepted_note_sha,
            accepted_note_commit,
            accepted_gate_sha,
            accepted_note_snapshot_id,
            accepted_gate_snapshot_id,
            accepted_at,
            acceptance_kind,
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
        review_runs=count_rows("review_runs"),
        review_pairs=count_rows("review_pairs"),
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
        review_runs=update_rows("review_runs"),
        review_pairs=update_rows("review_pairs"),
        acceptance_events=update_rows("acceptance_events"),
    )


def load_review_pairs_for_note(
    conn: sqlite3.Connection,
    *,
    note_path: str,
    model_partition: str,
) -> list[ReviewPairRow]:
    rows = conn.execute(
        """
        SELECT
            review_pair_id,
            review_run_id,
            note_path,
            gate_path,
            model_partition,
            pair_ordinal,
            pair_status,
            decision,
            rationale_markdown,
            evidence_json,
            gate_sha,
            reviewed_note_sha,
            reviewed_note_commit,
            reviewed_note_snapshot_id,
            reviewed_gate_snapshot_id,
            reviewed_at,
            review_kind
        FROM review_pairs
        WHERE note_path = ? AND model_partition = ?
        ORDER BY gate_path, reviewed_at, review_pair_id
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
            review_pair_id,
            review_run_id,
            note_path,
            gate_path,
            model_partition,
            pair_ordinal,
            pair_status,
            decision,
            rationale_markdown,
            evidence_json,
            gate_sha,
            reviewed_note_sha,
            reviewed_note_commit,
            reviewed_note_snapshot_id,
            reviewed_gate_snapshot_id,
            reviewed_at,
            review_kind
        FROM review_pairs
        WHERE note_path = ?
          AND gate_path = ?
          AND model_partition = ?
          AND pair_status = 'completed'
        ORDER BY reviewed_at DESC, review_pair_id DESC
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
                rp.*,
                ROW_NUMBER() OVER (
                    PARTITION BY rp.note_path, rp.gate_path, rp.model_partition
                    ORDER BY rp.reviewed_at DESC, rp.review_pair_id DESC
                ) AS rn
            FROM review_pairs AS rp
            WHERE rp.pair_status = 'completed'
        )
        SELECT
            COALESCE(accepted.review_pair_id, latest.review_pair_id) AS review_pair_id,
            COALESCE(accepted.review_run_id, latest.review_run_id) AS review_run_id,
            COALESCE(accepted.note_path, latest.note_path) AS note_path,
            COALESCE(accepted.gate_path, latest.gate_path) AS gate_path,
            COALESCE(accepted.model_partition, latest.model_partition) AS model_partition,
            COALESCE(accepted.pair_ordinal, latest.pair_ordinal) AS pair_ordinal,
            COALESCE(accepted.pair_status, latest.pair_status) AS pair_status,
            COALESCE(accepted.decision, latest.decision) AS decision,
            COALESCE(accepted.rationale_markdown, latest.rationale_markdown) AS rationale_markdown,
            COALESCE(accepted.evidence_json, latest.evidence_json) AS evidence_json,
            COALESCE(accepted.gate_sha, latest.gate_sha) AS gate_sha,
            COALESCE(accepted.reviewed_note_sha, latest.reviewed_note_sha) AS reviewed_note_sha,
            COALESCE(accepted.reviewed_note_commit, latest.reviewed_note_commit) AS reviewed_note_commit,
            COALESCE(accepted.reviewed_note_snapshot_id, latest.reviewed_note_snapshot_id) AS reviewed_note_snapshot_id,
            COALESCE(accepted.reviewed_gate_snapshot_id, latest.reviewed_gate_snapshot_id) AS reviewed_gate_snapshot_id,
            COALESCE(accepted.reviewed_at, latest.reviewed_at) AS reviewed_at,
            COALESCE(accepted.review_kind, latest.review_kind) AS review_kind
        FROM current_gate_acceptances AS a
        LEFT JOIN review_pairs AS accepted
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
