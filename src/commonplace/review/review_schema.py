#!/usr/bin/env python3
"""Schema creation and integrity checks for the canonical review-store database."""

from __future__ import annotations

import sqlite3
from pathlib import Path

REVIEW_SCHEMA_VERSION = 6
EXPECTED_REVIEW_TABLES = frozenset(
    {
        "review_jobs",
        "review_file_snapshots",
        "review_pairs",
        "acceptance",
    }
)
EXPECTED_REVIEW_INDEXES = frozenset(
    {
        "idx_review_jobs_model_partition_created",
        "idx_review_jobs_status",
        "idx_review_pairs_note_criterion",
        "idx_review_pairs_review_job_id",
        "idx_acceptance_note_criterion_model_partition",
    }
)
EXPECTED_REVIEW_VIEWS = frozenset({"current_criterion_acceptances"})


def init_db(db_path: Path, schema_path: Path) -> None:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = _connect(db_path)
    try:
        existing_tables = _schema_object_names(conn, "table")
        review_tables = {
            table_name
            for table_name in existing_tables
            if table_name.startswith("review_") or table_name == "acceptance"
        }
        if not review_tables:
            apply_schema(conn, schema_path)
            _set_user_version(conn, REVIEW_SCHEMA_VERSION)
            _assert_review_store_integrity(conn)
            conn.commit()
            return

        current_version = _get_user_version(conn)
        if current_version != REVIEW_SCHEMA_VERSION:
            raise RuntimeError(
                f"review DB schema version {current_version} does not match current "
                f"version {REVIEW_SCHEMA_VERSION}; recreate the review store"
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


def _assert_expected_schema_objects(conn: sqlite3.Connection) -> None:
    tables = _schema_object_names(conn, "table")
    review_tables = {
        table_name
        for table_name in tables
        if table_name.startswith("review_") or table_name == "acceptance"
    }
    unexpected_tables = review_tables - EXPECTED_REVIEW_TABLES
    missing_tables = EXPECTED_REVIEW_TABLES - tables
    missing_indexes = EXPECTED_REVIEW_INDEXES - _schema_object_names(conn, "index")
    missing_views = EXPECTED_REVIEW_VIEWS - _schema_object_names(conn, "view")
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


def _assert_review_store_integrity(conn: sqlite3.Connection) -> None:
    _assert_expected_schema_objects(conn)
    _assert_foreign_key_integrity(conn)
