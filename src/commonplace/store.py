"""Commonplace operational store: connection, schema, and integrity."""

from __future__ import annotations

import os
import sqlite3
from importlib import resources
from pathlib import Path

STORE_SCHEMA_VERSION = 2
SCHEMA_PATH = "store-schema.sql"
DEFAULT_DB_PATH = Path("kb/reports/commonplace-store.sqlite")
LEGACY_DB_PATH = Path("kb/reports/review-store.sqlite")
DB_ENV_VAR = "COMMONPLACE_STORE"
LEGACY_DB_ENV_VAR = "COMMONPLACE_REVIEW_DB"

EXPECTED_TABLES = frozenset(
    {
        "artifact_snapshots",
        "freshness_baselines",
        "freshness_target_generations",
        "freshness_inputs",
        "review_freshness_evidence",
        "review_jobs",
        "review_pairs",
    }
)
EXPECTED_INDEXES = frozenset(
    {
        "idx_freshness_inputs_path",
        "idx_review_jobs_model_partition_created",
        "idx_review_jobs_status",
        "idx_review_pairs_note_criterion",
        "idx_review_pairs_review_job_id",
    }
)
EXPECTED_VIEWS = frozenset({"current_review_freshness_baselines"})


def connect(db_path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def resolve_db_path(repo_root: Path, db_override: str | None = None) -> Path:
    if db_override:
        return Path(db_override).resolve()
    raw = os.environ.get(DB_ENV_VAR, "").strip() or os.environ.get(LEGACY_DB_ENV_VAR, "").strip()
    if raw:
        db_path = Path(raw)
        if not db_path.is_absolute():
            db_path = repo_root / db_path
        return db_path.resolve()
    return (repo_root / DEFAULT_DB_PATH).resolve()


def ensure_db(db_path: Path) -> None:
    if db_path.exists():
        with connect(db_path) as conn:
            _migrate_store(conn)
            _assert_store_version(conn)
            assert_store_integrity(conn)
            conn.commit()
        return

    legacy_hint = db_path.parent / LEGACY_DB_PATH.name
    if legacy_hint.exists() and db_path.name == DEFAULT_DB_PATH.name:
        raise RuntimeError(
            f"migration required: found {legacy_hint} but not {db_path}; "
            "run scripts/migrate-review-db-v7-to-commonplace-store.py"
        )

    db_path.parent.mkdir(parents=True, exist_ok=True)
    with connect(db_path) as conn:
        apply_schema(conn)
        _set_user_version(conn, STORE_SCHEMA_VERSION)
        assert_store_integrity(conn)
        conn.commit()


def apply_schema(conn: sqlite3.Connection) -> None:
    with resources.as_file(resources.files("commonplace") / SCHEMA_PATH) as schema_path:
        conn.executescript(schema_path.read_text(encoding="utf-8"))


def _get_user_version(conn: sqlite3.Connection) -> int:
    row = conn.execute("PRAGMA user_version").fetchone()
    return int(row[0])


def _set_user_version(conn: sqlite3.Connection, version: int) -> None:
    conn.execute(f"PRAGMA user_version = {int(version)}")


def _assert_store_version(conn: sqlite3.Connection) -> None:
    current_version = _get_user_version(conn)
    if current_version != STORE_SCHEMA_VERSION:
        raise RuntimeError(
            f"store schema version {current_version} does not match current "
            f"version {STORE_SCHEMA_VERSION}; recreate or migrate the store"
        )


_GENERATIONS_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS freshness_target_generations (
    target_kind TEXT NOT NULL CHECK (length(target_kind) > 0),
    target_key_json TEXT NOT NULL CHECK (length(target_key_json) > 0),
    next_revision INTEGER NOT NULL CHECK (next_revision >= 1),
    PRIMARY KEY (target_kind, target_key_json)
);
"""


def _migrate_store(conn: sqlite3.Connection) -> None:
    current_version = _get_user_version(conn)
    if current_version == STORE_SCHEMA_VERSION:
        return
    if current_version == 1 and STORE_SCHEMA_VERSION == 2:
        conn.executescript(_GENERATIONS_TABLE_SQL)
        conn.execute(
            """
            INSERT INTO freshness_target_generations (
                target_kind, target_key_json, next_revision
            )
            SELECT target_kind, target_key_json, revision + 1
            FROM freshness_baselines
            """
        )
        _set_user_version(conn, STORE_SCHEMA_VERSION)
        return
    raise RuntimeError(
        f"store schema version {current_version} does not match current "
        f"version {STORE_SCHEMA_VERSION}; recreate or migrate the store"
    )


def _schema_object_names(conn: sqlite3.Connection, object_type: str) -> set[str]:
    rows = conn.execute(
        "SELECT name FROM sqlite_master WHERE type = ?",
        (object_type,),
    ).fetchall()
    return {str(row["name"]) for row in rows}


def _assert_expected_schema_objects(conn: sqlite3.Connection) -> None:
    tables = _schema_object_names(conn, "table")
    missing_tables = EXPECTED_TABLES - tables
    unexpected_tables = tables - EXPECTED_TABLES - {"sqlite_sequence"}
    missing_indexes = EXPECTED_INDEXES - _schema_object_names(conn, "index")
    missing_views = EXPECTED_VIEWS - _schema_object_names(conn, "view")
    if unexpected_tables or missing_tables or missing_indexes or missing_views:
        parts: list[str] = []
        if unexpected_tables:
            parts.append(f"unexpected tables: {', '.join(sorted(unexpected_tables))}")
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


def assert_store_integrity(conn: sqlite3.Connection) -> None:
    _assert_expected_schema_objects(conn)
    _assert_foreign_key_integrity(conn)
    from commonplace.freshness.integrity import assert_review_freshness_integrity

    assert_review_freshness_integrity(conn)