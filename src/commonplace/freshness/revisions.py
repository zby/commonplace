"""Monotonic revision allocation across baseline retire and recreate."""

from __future__ import annotations

import sqlite3


def load_generation_next_revision(
    conn: sqlite3.Connection,
    *,
    target_kind: str,
    target_key_json: str,
) -> int:
    """Return the next revision the generation ledger would allocate."""
    row = conn.execute(
        """
        SELECT next_revision
        FROM freshness_target_generations
        WHERE target_kind = ? AND target_key_json = ?
        """,
        (target_kind, target_key_json),
    ).fetchone()
    return int(row["next_revision"]) if row is not None else 1


def allocate_initial_revision(
    conn: sqlite3.Connection,
    *,
    target_kind: str,
    target_key_json: str,
) -> int:
    """Allocate the revision for a newly registered baseline."""
    row = conn.execute(
        """
        SELECT next_revision
        FROM freshness_target_generations
        WHERE target_kind = ? AND target_key_json = ?
        """,
        (target_kind, target_key_json),
    ).fetchone()
    revision = int(row["next_revision"]) if row is not None else 1
    _record_next_revision(
        conn,
        target_kind=target_kind,
        target_key_json=target_key_json,
        next_revision=revision + 1,
    )
    return revision


def allocate_successor_revision(
    conn: sqlite3.Connection,
    *,
    target_kind: str,
    target_key_json: str,
    current_revision: int,
) -> int:
    """Allocate the revision that supersedes an existing baseline."""
    revision = current_revision + 1
    _record_next_revision(
        conn,
        target_kind=target_kind,
        target_key_json=target_key_json,
        next_revision=revision + 1,
    )
    return revision


def _record_next_revision(
    conn: sqlite3.Connection,
    *,
    target_kind: str,
    target_key_json: str,
    next_revision: int,
) -> None:
    conn.execute(
        """
        INSERT INTO freshness_target_generations (
            target_kind, target_key_json, next_revision
        ) VALUES (?, ?, ?)
        ON CONFLICT(target_kind, target_key_json) DO UPDATE SET
            next_revision = excluded.next_revision
        """,
        (target_kind, target_key_json, next_revision),
    )