#!/usr/bin/env python3
"""Helpers for the canonical review-store SQLite database."""

from __future__ import annotations

import os
import sqlite3
from dataclasses import dataclass
from importlib import resources
from pathlib import Path
from typing import Sequence

from commonplace.review.protocol.decisions import normalize_review_decision

DEFAULT_DB_PATH = Path("kb/reports/review-store.sqlite")
SCHEMA_PATH = "review-schema.sql"
DB_ENV_VAR = "COMMONPLACE_REVIEW_DB"
PACKING_VALUES = frozenset({"note", "gate"})
REVIEW_KIND_VALUES = frozenset({"full-review"})


@dataclass(frozen=True)
class AcceptanceState:
    note_path: str
    gate_id: str
    model_id: str
    accepted_review_pair_id: int | None
    accepted_note_sha: str
    accepted_note_commit: str | None
    accepted_gate_sha: str
    accepted_at: str
    acceptance_kind: str


@dataclass(frozen=True)
class ReviewRunRow:
    review_run_id: int
    model_id: str
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
    gate_id: str
    model_id: str
    pair_ordinal: int
    pair_status: str
    decision: str | None
    rationale_markdown: str | None
    evidence_json: str | None
    gate_sha: str
    reviewed_note_sha: str
    reviewed_note_commit: str | None
    reviewed_at: str | None
    review_kind: str


@dataclass(frozen=True)
class ReviewPairRequest:
    note_path: str
    gate_id: str
    gate_sha: str
    reviewed_note_sha: str
    reviewed_note_commit: str | None
    pair_ordinal: int
    review_kind: str = "full-review"


@dataclass(frozen=True)
class PendingReviewPair:
    note_path: str
    gate_id: str
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
class ModelIdUpdateCounts:
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
        init_db(db_path, schema_path)


def prepare_review_db(repo_root: Path, db_override: str | None = None) -> Path:
    """Resolve the review DB path (honoring --db override) and ensure its schema."""
    db_path = resolve_db_path(repo_root, db_override)
    ensure_db(repo_root, db_path)
    return db_path


def apply_schema(conn: sqlite3.Connection, schema_path: Path) -> None:
    conn.executescript(schema_path.read_text(encoding="utf-8"))


def init_db(db_path: Path, schema_path: Path) -> None:
    if db_path.exists():
        return
    db_path.parent.mkdir(parents=True, exist_ok=True)
    with connect(db_path) as conn:
        apply_schema(conn, schema_path)
        conn.commit()


def _review_run_from_row(row: sqlite3.Row) -> ReviewRunRow:
    return ReviewRunRow(
        review_run_id=row["review_run_id"],
        model_id=row["model_id"],
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
        gate_id=row["gate_id"],
        model_id=row["model_id"],
        pair_ordinal=row["pair_ordinal"],
        pair_status=row["pair_status"],
        decision=row["decision"],
        rationale_markdown=row["rationale_markdown"],
        evidence_json=row["evidence_json"],
        gate_sha=row["gate_sha"],
        reviewed_note_sha=row["reviewed_note_sha"],
        reviewed_note_commit=row["reviewed_note_commit"],
        reviewed_at=row["reviewed_at"],
        review_kind=row["review_kind"],
    )


def create_run(
    conn: sqlite3.Connection,
    *,
    model_id: str,
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
            model_id,
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
            model_id,
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
    model_id: str,
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
                gate_id,
                model_id,
                pair_ordinal,
                pair_status,
                gate_sha,
                reviewed_note_sha,
                reviewed_note_commit,
                review_kind
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                review_run_id,
                pair.note_path,
                pair.gate_id,
                model_id,
                pair.pair_ordinal,
                pair_status,
                pair.gate_sha,
                pair.reviewed_note_sha,
                pair.reviewed_note_commit,
                pair.review_kind,
            ),
        )
        review_pair_ids.append(int(cursor.lastrowid))
    return review_pair_ids


def create_run_with_pairs(
    conn: sqlite3.Connection,
    *,
    model_id: str,
    runner: str,
    started_at: str,
    packing: str,
    pairs: Sequence[ReviewPairRequest],
) -> int:
    review_run_id = create_run(
        conn,
        model_id=model_id,
        runner=runner,
        started_at=started_at,
        packing=packing,
        status="running",
    )
    create_review_pairs(conn, review_run_id=review_run_id, model_id=model_id, pairs=pairs)
    return review_run_id


def load_review_run(conn: sqlite3.Connection, *, review_run_id: int) -> ReviewRunRow | None:
    row = conn.execute(
        """
        SELECT
            review_run_id,
            model_id,
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
            gate_id,
            model_id,
            pair_ordinal,
            pair_status,
            decision,
            rationale_markdown,
            evidence_json,
            gate_sha,
            reviewed_note_sha,
            reviewed_note_commit,
            reviewed_at,
            review_kind
        FROM review_pairs
        WHERE review_run_id = ?
        ORDER BY pair_ordinal, note_path, gate_id
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
            gate_id,
            model_id,
            accepted_review_pair_id,
            accepted_note_sha,
            accepted_note_commit,
            accepted_gate_sha,
            accepted_at,
            acceptance_kind
        FROM current_gate_acceptances
        """
    ).fetchall()
    return {
        (row["note_path"], row["gate_id"], row["model_id"]): AcceptanceState(
            note_path=row["note_path"],
            gate_id=row["gate_id"],
            model_id=row["model_id"],
            accepted_review_pair_id=row["accepted_review_pair_id"],
            accepted_note_sha=row["accepted_note_sha"],
            accepted_note_commit=row["accepted_note_commit"],
            accepted_gate_sha=row["accepted_gate_sha"],
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


def rekey_review_run_model(
    conn: sqlite3.Connection,
    *,
    review_run_id: int,
    model_id: str,
) -> None:
    conn.execute(
        """
        UPDATE review_runs
        SET model_id = ?
        WHERE review_run_id = ?
        """,
        (model_id, review_run_id),
    )
    conn.execute(
        """
        UPDATE review_pairs
        SET model_id = ?
        WHERE review_run_id = ?
        """,
        (model_id, review_run_id),
    )


def complete_review_pairs(
    conn: sqlite3.Connection,
    *,
    review_run_id: int,
    review_pairs: Sequence[PendingReviewPair],
    reviewed_at: str,
) -> list[int]:
    requested = {
        (pair.note_path, pair.gate_id): pair
        for pair in load_review_pairs_for_run(conn, review_run_id=review_run_id)
    }
    completed_pair_ids: list[int] = []
    seen: set[tuple[str, str]] = set()
    for review_pair in review_pairs:
        if review_pair.review_kind not in REVIEW_KIND_VALUES:
            raise ValueError(f"invalid review kind: {review_pair.review_kind}")
        key = (review_pair.note_path, review_pair.gate_id)
        if key in seen:
            raise ValueError(f"duplicate completed pair: {review_pair.note_path} :: {review_pair.gate_id}")
        seen.add(key)
        requested_pair = requested.get(key)
        if requested_pair is None:
            raise ValueError(
                f"pair {review_pair.note_path} :: {review_pair.gate_id} is not part of review run {review_run_id}"
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
    for note_path, gate_id in pairs:
        cursor = conn.execute(
            """
            UPDATE review_pairs
            SET pair_status = 'missing'
            WHERE review_run_id = ?
              AND note_path = ?
              AND gate_id = ?
              AND pair_status != 'completed'
            """,
            (review_run_id, note_path, gate_id),
        )
        count += int(cursor.rowcount or 0)
    return count


def append_acceptance_event(
    conn: sqlite3.Connection,
    *,
    note_path: str,
    gate_id: str,
    model_id: str,
    accepted_review_pair_id: int | None,
    accepted_note_sha: str,
    accepted_note_commit: str | None,
    accepted_gate_sha: str,
    accepted_at: str,
    acceptance_kind: str,
) -> int:
    cursor = conn.execute(
        """
        INSERT INTO acceptance_events (
            note_path,
            gate_id,
            model_id,
            accepted_review_pair_id,
            accepted_note_sha,
            accepted_note_commit,
            accepted_gate_sha,
            accepted_at,
            acceptance_kind
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            note_path,
            gate_id,
            model_id,
            accepted_review_pair_id,
            accepted_note_sha,
            accepted_note_commit,
            accepted_gate_sha,
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


def count_model_id_records(
    conn: sqlite3.Connection,
    *,
    model_id: str,
) -> ModelIdUpdateCounts:
    def count_rows(table: str) -> int:
        row = conn.execute(
            f"SELECT COUNT(*) AS count FROM {table} WHERE model_id = ?",
            (model_id,),
        ).fetchone()
        return int(row["count"]) if row is not None else 0

    return ModelIdUpdateCounts(
        review_runs=count_rows("review_runs"),
        review_pairs=count_rows("review_pairs"),
        acceptance_events=count_rows("acceptance_events"),
    )


def rekey_model_id(
    conn: sqlite3.Connection,
    *,
    old_model_id: str,
    new_model_id: str,
) -> ModelIdUpdateCounts:
    if old_model_id == new_model_id:
        return ModelIdUpdateCounts()

    def update_rows(table: str) -> int:
        cursor = conn.execute(
            f"UPDATE {table} SET model_id = ? WHERE model_id = ?",
            (new_model_id, old_model_id),
        )
        return int(cursor.rowcount or 0)

    return ModelIdUpdateCounts(
        review_runs=update_rows("review_runs"),
        review_pairs=update_rows("review_pairs"),
        acceptance_events=update_rows("acceptance_events"),
    )


def load_review_pairs_for_note(
    conn: sqlite3.Connection,
    *,
    note_path: str,
    model_id: str,
) -> list[ReviewPairRow]:
    rows = conn.execute(
        """
        SELECT
            review_pair_id,
            review_run_id,
            note_path,
            gate_id,
            model_id,
            pair_ordinal,
            pair_status,
            decision,
            rationale_markdown,
            evidence_json,
            gate_sha,
            reviewed_note_sha,
            reviewed_note_commit,
            reviewed_at,
            review_kind
        FROM review_pairs
        WHERE note_path = ? AND model_id = ?
        ORDER BY gate_id, reviewed_at, review_pair_id
        """,
        (note_path, model_id),
    ).fetchall()
    return [_review_pair_from_row(row) for row in rows]


def load_latest_completed_review_pair(
    conn: sqlite3.Connection,
    *,
    note_path: str,
    gate_id: str,
    model_id: str,
) -> ReviewPairRow | None:
    row = conn.execute(
        """
        SELECT
            review_pair_id,
            review_run_id,
            note_path,
            gate_id,
            model_id,
            pair_ordinal,
            pair_status,
            decision,
            rationale_markdown,
            evidence_json,
            gate_sha,
            reviewed_note_sha,
            reviewed_note_commit,
            reviewed_at,
            review_kind
        FROM review_pairs
        WHERE note_path = ?
          AND gate_id = ?
          AND model_id = ?
          AND pair_status = 'completed'
        ORDER BY reviewed_at DESC, review_pair_id DESC
        LIMIT 1
        """,
        (note_path, gate_id, model_id),
    ).fetchone()
    if row is None:
        return None
    return _review_pair_from_row(row)


def load_effective_review_pair_map(
    conn: sqlite3.Connection,
    *,
    note_path: str | None = None,
    model_id: str | None,
) -> dict[tuple[str, str, str], ReviewPairRow]:
    where_clauses: list[str] = []
    params: list[str] = []
    if model_id is not None:
        where_clauses.append("a.model_id = ?")
        params.append(model_id)
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
                    PARTITION BY rp.note_path, rp.gate_id, rp.model_id
                    ORDER BY rp.reviewed_at DESC, rp.review_pair_id DESC
                ) AS rn
            FROM review_pairs AS rp
            WHERE rp.pair_status = 'completed'
        )
        SELECT
            COALESCE(accepted.review_pair_id, latest.review_pair_id) AS review_pair_id,
            COALESCE(accepted.review_run_id, latest.review_run_id) AS review_run_id,
            COALESCE(accepted.note_path, latest.note_path) AS note_path,
            COALESCE(accepted.gate_id, latest.gate_id) AS gate_id,
            COALESCE(accepted.model_id, latest.model_id) AS model_id,
            COALESCE(accepted.pair_ordinal, latest.pair_ordinal) AS pair_ordinal,
            COALESCE(accepted.pair_status, latest.pair_status) AS pair_status,
            COALESCE(accepted.decision, latest.decision) AS decision,
            COALESCE(accepted.rationale_markdown, latest.rationale_markdown) AS rationale_markdown,
            COALESCE(accepted.evidence_json, latest.evidence_json) AS evidence_json,
            COALESCE(accepted.gate_sha, latest.gate_sha) AS gate_sha,
            COALESCE(accepted.reviewed_note_sha, latest.reviewed_note_sha) AS reviewed_note_sha,
            COALESCE(accepted.reviewed_note_commit, latest.reviewed_note_commit) AS reviewed_note_commit,
            COALESCE(accepted.reviewed_at, latest.reviewed_at) AS reviewed_at,
            COALESCE(accepted.review_kind, latest.review_kind) AS review_kind
        FROM current_gate_acceptances AS a
        LEFT JOIN review_pairs AS accepted
          ON accepted.review_pair_id = a.accepted_review_pair_id
        LEFT JOIN latest_review_pairs AS latest
          ON latest.note_path = a.note_path
         AND latest.gate_id = a.gate_id
         AND latest.model_id = a.model_id
         AND latest.rn = 1
        {where_sql}
        """,
        tuple(params),
    ).fetchall()
    result: dict[tuple[str, str, str], ReviewPairRow] = {}
    for row in rows:
        if row["review_pair_id"] is None:
            continue
        key = (row["note_path"], row["gate_id"], row["model_id"])
        result[key] = _review_pair_from_row(row)
    return result
