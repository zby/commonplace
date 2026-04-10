#!/usr/bin/env python3
"""Helpers for the canonical review-store SQLite database."""

from __future__ import annotations

import os
import sqlite3
from importlib import resources
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

from commonplace.review.review_decisions import normalize_review_decision
from commonplace.review.review_metadata import iso_now

GATES_ROOT = Path("kb/instructions/review-gates")
DEFAULT_DB_PATH = Path("kb/reports/review-store.sqlite")
SCHEMA_PATH = "review-schema.sql"
DB_ENV_VAR = "COMMONPLACE_REVIEW_DB"


@dataclass(frozen=True)
class AcceptanceState:
    note_path: str
    gate_id: str
    model_id: str
    accepted_review_id: int | None
    accepted_note_sha: str
    accepted_note_commit: str | None
    accepted_gate_sha: str
    accepted_at: str
    acceptance_kind: str


@dataclass(frozen=True)
class GateReviewRow:
    id: int
    review_run_id: int | None
    note_path: str
    gate_id: str
    model_id: str
    decision: str
    rationale_markdown: str
    evidence_json: str | None
    gate_sha: str
    reviewed_note_sha: str
    reviewed_note_commit: str | None
    reviewed_at: str
    review_kind: str


@dataclass(frozen=True)
class ReviewRunRow:
    id: int
    note_path: str
    model_id: str
    runner: str
    reviewed_note_sha: str
    reviewed_note_commit: str | None
    started_at: str
    completed_at: str | None
    status: str
    failure_reason: str | None
    telemetry_json: str | None
    raw_bundle_markdown: str | None
    debug_log: str | None


@dataclass(frozen=True)
class ReviewRunGateRow:
    review_run_id: int
    gate_id: str
    gate_sha: str
    ordinal: int


@dataclass(frozen=True)
class PendingGateReview:
    gate_id: str
    decision: str
    rationale_markdown: str
    evidence_json: str | None = None
    reviewed_at: str | None = None
    review_kind: str = "full-review"


def connect(db_path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
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


def load_current_acceptances(conn: sqlite3.Connection) -> dict[tuple[str, str, str], AcceptanceState]:
    rows = conn.execute(
        """
        SELECT
            note_path,
            gate_id,
            model_id,
            accepted_review_id,
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
            accepted_review_id=row["accepted_review_id"],
            accepted_note_sha=row["accepted_note_sha"],
            accepted_note_commit=row["accepted_note_commit"],
            accepted_gate_sha=row["accepted_gate_sha"],
            accepted_at=row["accepted_at"],
            acceptance_kind=row["acceptance_kind"],
        )
        for row in rows
    }


def insert_gate_review(
    conn: sqlite3.Connection,
    *,
    review_run_id: int | None = None,
    note_path: str,
    gate_id: str,
    model_id: str,
    decision: str,
    rationale_markdown: str,
    evidence_json: str | None,
    gate_sha: str,
    reviewed_note_sha: str,
    reviewed_note_commit: str | None,
    reviewed_at: str,
    review_kind: str = "full-review",
) -> int:
    normalized_decision = normalize_review_decision(decision)
    if normalized_decision is None:
        raise ValueError(f"invalid review decision: {decision}")
    cursor = conn.execute(
        """
        INSERT INTO gate_reviews (
            review_run_id,
            note_path,
            gate_id,
            model_id,
            decision,
            rationale_markdown,
            evidence_json,
            gate_sha,
            reviewed_note_sha,
            reviewed_note_commit,
            reviewed_at,
            review_kind
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            review_run_id,
            note_path,
            gate_id,
            model_id,
            normalized_decision,
            rationale_markdown,
            evidence_json,
            gate_sha,
            reviewed_note_sha,
            reviewed_note_commit,
            reviewed_at,
            review_kind,
        ),
    )
    return int(cursor.lastrowid)


def insert_review_run(
    conn: sqlite3.Connection,
    *,
    note_path: str,
    model_id: str,
    runner: str,
    reviewed_note_sha: str,
    reviewed_note_commit: str | None,
    started_at: str,
    completed_at: str | None = None,
    status: str = "running",
    failure_reason: str | None = None,
    telemetry_json: str | None = None,
    raw_bundle_markdown: str | None = None,
    debug_log: str | None = None,
) -> int:
    cursor = conn.execute(
        """
        INSERT INTO review_runs (
            note_path,
            model_id,
            runner,
            reviewed_note_sha,
            reviewed_note_commit,
            started_at,
            completed_at,
            status,
            failure_reason,
            telemetry_json,
            raw_bundle_markdown,
            debug_log
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            note_path,
            model_id,
            runner,
            reviewed_note_sha,
            reviewed_note_commit,
            started_at,
            completed_at,
            status,
            failure_reason,
            telemetry_json,
            raw_bundle_markdown,
            debug_log,
        ),
    )
    return int(cursor.lastrowid)


def insert_review_run_gates(
    conn: sqlite3.Connection,
    *,
    review_run_id: int,
    gates: list[tuple[str, str, int]],
) -> None:
    conn.executemany(
        """
        INSERT INTO review_run_gates (
            review_run_id,
            gate_id,
            gate_sha,
            ordinal
        ) VALUES (?, ?, ?, ?)
        """,
        [(review_run_id, gate_id, gate_sha, ordinal) for gate_id, gate_sha, ordinal in gates],
    )


def create_run(
    conn: sqlite3.Connection,
    *,
    note_path: str,
    model_id: str,
    runner: str,
    reviewed_note_sha: str,
    reviewed_note_commit: str | None,
    started_at: str,
    gates: Sequence[tuple[str, str, int]],
) -> int:
    review_run_id = insert_review_run(
        conn,
        note_path=note_path,
        model_id=model_id,
        runner=runner,
        reviewed_note_sha=reviewed_note_sha,
        reviewed_note_commit=reviewed_note_commit,
        started_at=started_at,
        status="running",
    )
    insert_review_run_gates(conn, review_run_id=review_run_id, gates=list(gates))
    return review_run_id


def load_review_run(conn: sqlite3.Connection, *, review_run_id: int) -> ReviewRunRow | None:
    row = conn.execute(
        """
        SELECT
            id,
            note_path,
            model_id,
            runner,
            reviewed_note_sha,
            reviewed_note_commit,
            started_at,
            completed_at,
            status,
            failure_reason,
            telemetry_json,
            raw_bundle_markdown,
            debug_log
        FROM review_runs
        WHERE id = ?
        """,
        (review_run_id,),
    ).fetchone()
    if row is None:
        return None
    return ReviewRunRow(
        id=row["id"],
        note_path=row["note_path"],
        model_id=row["model_id"],
        runner=row["runner"],
        reviewed_note_sha=row["reviewed_note_sha"],
        reviewed_note_commit=row["reviewed_note_commit"],
        started_at=row["started_at"],
        completed_at=row["completed_at"],
        status=row["status"],
        failure_reason=row["failure_reason"],
        telemetry_json=row["telemetry_json"],
        raw_bundle_markdown=row["raw_bundle_markdown"],
        debug_log=row["debug_log"],
    )


def load_review_run_gates(conn: sqlite3.Connection, *, review_run_id: int) -> list[ReviewRunGateRow]:
    rows = conn.execute(
        """
        SELECT
            review_run_id,
            gate_id,
            gate_sha,
            ordinal
        FROM review_run_gates
        WHERE review_run_id = ?
        ORDER BY ordinal, gate_id
        """,
        (review_run_id,),
    ).fetchall()
    return [
        ReviewRunGateRow(
            review_run_id=row["review_run_id"],
            gate_id=row["gate_id"],
            gate_sha=row["gate_sha"],
            ordinal=row["ordinal"],
        )
        for row in rows
    ]


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
        WHERE id = ?
        """,
        (completed_at, raw_bundle_markdown, debug_log, telemetry_json, review_run_id),
    )


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
        WHERE id = ?
        """,
        (telemetry_json, raw_bundle_markdown, debug_log, review_run_id),
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
        WHERE id = ?
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


def _rekey_review_run_model(
    conn: sqlite3.Connection,
    *,
    review_run_id: int,
    model_id: str,
) -> None:
    conn.execute(
        """
        UPDATE review_runs
        SET model_id = ?
        WHERE id = ?
        """,
        (model_id, review_run_id),
    )
    conn.execute(
        """
        UPDATE gate_reviews
        SET model_id = ?
        WHERE review_run_id = ?
        """,
        (model_id, review_run_id),
    )


def _review_run_coverage_failure(
    conn: sqlite3.Connection,
    *,
    review_run_id: int,
) -> tuple[str | None, list[ReviewRunGateRow], dict[str, GateReviewRow]]:
    run_gates = load_review_run_gates(conn, review_run_id=review_run_id)
    if not run_gates:
        return f"review run has no gates: {review_run_id}", [], {}

    gate_reviews = load_gate_reviews_for_run(conn, review_run_id=review_run_id)
    run_gate_map = {row.gate_id: row for row in run_gates}
    written_gate_map = {row.gate_id: row for row in gate_reviews}

    missing = [row.gate_id for row in run_gates if row.gate_id not in written_gate_map]
    mismatched = [
        row.gate_id
        for row in gate_reviews
        if row.gate_id not in run_gate_map or row.gate_sha != run_gate_map[row.gate_id].gate_sha
    ]
    if not missing and not mismatched:
        return None, run_gates, written_gate_map

    reason_parts: list[str] = []
    if missing:
        reason_parts.append(f"missing gates: {', '.join(sorted(missing))}")
    if mismatched:
        reason_parts.append(f"gate provenance mismatch: {', '.join(sorted(mismatched))}")
    return "; ".join(reason_parts), run_gates, written_gate_map


def record_and_finalize_run(
    conn: sqlite3.Connection,
    *,
    review_run_id: int,
    gate_reviews: Sequence[PendingGateReview] | None = None,
    actual_model_id: str | None = None,
    completed_at: str | None = None,
    telemetry_json: str | None = None,
    raw_bundle_markdown: str | None = None,
    debug_log: str | None = None,
) -> int:
    review_run = load_review_run(conn, review_run_id=review_run_id)
    if review_run is None:
        raise ValueError(f"review run not found: {review_run_id}")
    if review_run.status != "running":
        raise ValueError(f"review run is not finalizable: {review_run.status}")

    finished_at = completed_at or iso_now()
    try:
        attach_execution_data(
            conn,
            review_run_id=review_run_id,
            telemetry_json=telemetry_json,
            raw_bundle_markdown=raw_bundle_markdown,
            debug_log=debug_log,
        )

        run_gates = {row.gate_id: row for row in load_review_run_gates(conn, review_run_id=review_run_id)}
        if gate_reviews is not None:
            for gate_review in gate_reviews:
                run_gate = run_gates.get(gate_review.gate_id)
                if run_gate is None:
                    raise ValueError(f"gate {gate_review.gate_id} is not part of review run {review_run_id}")
                insert_gate_review(
                    conn,
                    review_run_id=review_run_id,
                    note_path=review_run.note_path,
                    gate_id=gate_review.gate_id,
                    model_id=review_run.model_id,
                    decision=gate_review.decision,
                    rationale_markdown=gate_review.rationale_markdown,
                    evidence_json=gate_review.evidence_json,
                    gate_sha=run_gate.gate_sha,
                    reviewed_note_sha=review_run.reviewed_note_sha,
                    reviewed_note_commit=review_run.reviewed_note_commit,
                    reviewed_at=gate_review.reviewed_at or iso_now(),
                    review_kind=gate_review.review_kind,
                )

        final_model_id = review_run.model_id
        if actual_model_id is not None and actual_model_id != review_run.model_id:
            _rekey_review_run_model(conn, review_run_id=review_run_id, model_id=actual_model_id)
            final_model_id = actual_model_id

        failure_reason, finalized_run_gates, written_gate_map = _review_run_coverage_failure(
            conn,
            review_run_id=review_run_id,
        )
        if failure_reason is not None:
            raise ValueError(failure_reason)

        complete_review_run(conn, review_run_id=review_run_id, completed_at=finished_at)
        for run_gate in finalized_run_gates:
            gate_review = written_gate_map[run_gate.gate_id]
            append_acceptance_event(
                conn,
                note_path=review_run.note_path,
                gate_id=run_gate.gate_id,
                model_id=final_model_id,
                accepted_review_id=gate_review.id,
                accepted_note_sha=review_run.reviewed_note_sha,
                accepted_note_commit=review_run.reviewed_note_commit,
                accepted_gate_sha=run_gate.gate_sha,
                accepted_at=finished_at,
                acceptance_kind="full-review",
            )
        return len(finalized_run_gates)
    except (sqlite3.IntegrityError, ValueError) as exc:
        fail_review_run(
            conn,
            review_run_id=review_run_id,
            failure_reason=str(exc),
            completed_at=finished_at,
        )
        raise ValueError(str(exc)) from exc


def append_acceptance_event(
    conn: sqlite3.Connection,
    *,
    note_path: str,
    gate_id: str,
    model_id: str,
    accepted_review_id: int | None,
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
            accepted_review_id,
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
            accepted_review_id,
            accepted_note_sha,
            accepted_note_commit,
            accepted_gate_sha,
            accepted_at,
            acceptance_kind,
        ),
    )
    return int(cursor.lastrowid)

def load_gate_reviews_for_note(
    conn: sqlite3.Connection,
    *,
    note_path: str,
    model_id: str,
) -> list[GateReviewRow]:
    rows = conn.execute(
        """
        SELECT
            id,
            review_run_id,
            note_path,
            gate_id,
            model_id,
            decision,
            rationale_markdown,
            evidence_json,
            gate_sha,
            reviewed_note_sha,
            reviewed_note_commit,
            reviewed_at,
            review_kind
        FROM gate_reviews
        WHERE note_path = ? AND model_id = ?
        ORDER BY gate_id, reviewed_at, id
        """,
        (note_path, model_id),
    ).fetchall()
    return [
        GateReviewRow(
            id=row["id"],
            review_run_id=row["review_run_id"],
            note_path=row["note_path"],
            gate_id=row["gate_id"],
            model_id=row["model_id"],
            decision=row["decision"],
            rationale_markdown=row["rationale_markdown"],
            evidence_json=row["evidence_json"],
            gate_sha=row["gate_sha"],
            reviewed_note_sha=row["reviewed_note_sha"],
            reviewed_note_commit=row["reviewed_note_commit"],
            reviewed_at=row["reviewed_at"],
            review_kind=row["review_kind"],
        )
        for row in rows
    ]


def load_gate_reviews_for_run(
    conn: sqlite3.Connection,
    *,
    review_run_id: int,
) -> list[GateReviewRow]:
    rows = conn.execute(
        """
        SELECT
            id,
            review_run_id,
            note_path,
            gate_id,
            model_id,
            decision,
            rationale_markdown,
            evidence_json,
            gate_sha,
            reviewed_note_sha,
            reviewed_note_commit,
            reviewed_at,
            review_kind
        FROM gate_reviews
        WHERE review_run_id = ?
        ORDER BY gate_id, reviewed_at, id
        """,
        (review_run_id,),
    ).fetchall()
    return [
        GateReviewRow(
            id=row["id"],
            review_run_id=row["review_run_id"],
            note_path=row["note_path"],
            gate_id=row["gate_id"],
            model_id=row["model_id"],
            decision=row["decision"],
            rationale_markdown=row["rationale_markdown"],
            evidence_json=row["evidence_json"],
            gate_sha=row["gate_sha"],
            reviewed_note_sha=row["reviewed_note_sha"],
            reviewed_note_commit=row["reviewed_note_commit"],
            reviewed_at=row["reviewed_at"],
            review_kind=row["review_kind"],
        )
        for row in rows
    ]


def load_effective_gate_review_map(
    conn: sqlite3.Connection,
    *,
    note_path: str | None = None,
    model_id: str | None,
) -> dict[tuple[str, str, str], GateReviewRow]:
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
        WITH latest_gate_reviews AS (
            SELECT
                gr.*,
                ROW_NUMBER() OVER (
                    PARTITION BY gr.note_path, gr.gate_id, gr.model_id
                    ORDER BY gr.reviewed_at DESC, gr.id DESC
                ) AS rn
            FROM gate_reviews AS gr
        )
        SELECT
            COALESCE(accepted.id, latest.id) AS id,
            COALESCE(accepted.review_run_id, latest.review_run_id) AS review_run_id,
            COALESCE(accepted.note_path, latest.note_path) AS note_path,
            COALESCE(accepted.gate_id, latest.gate_id) AS gate_id,
            COALESCE(accepted.model_id, latest.model_id) AS model_id,
            COALESCE(accepted.decision, latest.decision) AS decision,
            COALESCE(accepted.rationale_markdown, latest.rationale_markdown) AS rationale_markdown,
            COALESCE(accepted.evidence_json, latest.evidence_json) AS evidence_json,
            COALESCE(accepted.gate_sha, latest.gate_sha) AS gate_sha,
            COALESCE(accepted.reviewed_note_sha, latest.reviewed_note_sha) AS reviewed_note_sha,
            COALESCE(accepted.reviewed_note_commit, latest.reviewed_note_commit) AS reviewed_note_commit,
            COALESCE(accepted.reviewed_at, latest.reviewed_at) AS reviewed_at,
            COALESCE(accepted.review_kind, latest.review_kind) AS review_kind
        FROM current_gate_acceptances AS a
        LEFT JOIN gate_reviews AS accepted
          ON accepted.id = a.accepted_review_id
        LEFT JOIN latest_gate_reviews AS latest
          ON latest.note_path = a.note_path
         AND latest.gate_id = a.gate_id
         AND latest.model_id = a.model_id
         AND latest.rn = 1
        {where_sql}
        """,
        tuple(params),
    ).fetchall()
    result: dict[tuple[str, str, str], GateReviewRow] = {}
    for row in rows:
        if row["id"] is None:
            continue
        key = (row["note_path"], row["gate_id"], row["model_id"])
        result[key] = GateReviewRow(
            id=row["id"],
            review_run_id=row["review_run_id"],
            note_path=row["note_path"],
            gate_id=row["gate_id"],
            model_id=row["model_id"],
            decision=row["decision"],
            rationale_markdown=row["rationale_markdown"],
            evidence_json=row["evidence_json"],
            gate_sha=row["gate_sha"],
            reviewed_note_sha=row["reviewed_note_sha"],
            reviewed_note_commit=row["reviewed_note_commit"],
            reviewed_at=row["reviewed_at"],
            review_kind=row["review_kind"],
        )
    return result
