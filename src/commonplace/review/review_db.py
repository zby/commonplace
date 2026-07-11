#!/usr/bin/env python3
"""Helpers for the canonical review-store SQLite database."""

from __future__ import annotations

import os
import sqlite3
from dataclasses import dataclass
from hashlib import sha256
from importlib import resources
from pathlib import Path
from typing import Sequence

from commonplace.review.artifacts import bundle_output_path_rel, prompt_path_rel, result_paths_by_pair_id
from commonplace.review.clock import iso_now
from commonplace.review.paths import gate_id_from_stored_path
from commonplace.review.review_model import build_model_partition, normalize_model_partition, normalize_reasoning_effort
from commonplace.review.review_schema import init_db

DEFAULT_DB_PATH = Path("kb/reports/review-store.sqlite")
SCHEMA_PATH = "review-schema.sql"
DB_ENV_VAR = "COMMONPLACE_REVIEW_DB"
JOB_STATUS_VALUES = frozenset({"queued", "completed", "failed"})


def _validated_runner_effort(
    *,
    model_partition: str,
    runner_model: str | None,
    runner_effort: str | None,
) -> str | None:
    if runner_effort is not None:
        normalized_effort = normalize_reasoning_effort(runner_effort)
        if normalized_effort is None:
            raise ValueError(f"invalid runner effort: {runner_effort}")
        runner_effort = normalized_effort
    if runner_model is None:
        if runner_effort is not None:
            raise ValueError("runner_effort requires runner_model")
        return None

    supplied_partition = build_model_partition(runner_model, runner_effort)
    expected_partition = normalize_model_partition(model_partition)
    if supplied_partition != expected_partition:
        raise ValueError(
            f"runner model/effort partition {supplied_partition!r} "
            f"does not match model_partition {expected_partition!r}"
        )
    return runner_effort


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
    accepted_review_pair_id: int
    accepted_note_snapshot_id: int | None
    accepted_gate_snapshot_id: int | None
    accepted_note_hash: str | None
    accepted_gate_hash: str | None
    accepted_note_text: str | None
    accepted_gate_text: str | None
    accepted_at: str
    result_kind: str
    decision: str | None

    @property
    def gate_id(self) -> str:
        return gate_id_from_stored_path(self.gate_path)


@dataclass(frozen=True)
class SupersededAcceptance:
    note_path: str
    gate_path: str
    model_partition: str
    accepted_review_pair_id: int
    accepted_note_snapshot_id: int | None
    accepted_gate_snapshot_id: int | None


@dataclass(frozen=True)
class ReviewJobRow:
    review_job_id: int
    model_partition: str
    runner: str | None
    runner_model: str | None
    runner_effort: str | None
    created_at: str
    completed_at: str | None
    status: str
    failure_reason: str | None
    telemetry_json: str | None
    packing: str


@dataclass(frozen=True)
class ReviewPairRow:
    review_pair_id: int
    review_job_id: int
    note_path: str
    gate_path: str
    model_partition: str
    pair_ordinal: int
    result_kind: str
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
    result_kind: str
    reviewed_note_snapshot_id: int | None = None
    reviewed_gate_snapshot_id: int | None = None


@dataclass(frozen=True)
class ReviewPairCompletion:
    note_path: str
    gate_path: str
    decision: str | None
    reviewed_at: str | None = None


@dataclass(frozen=True)
class _ReviewPairPathInput:
    review_pair_id: int
    note_path: str
    gate_path: str
    pair_ordinal: int


@dataclass(frozen=True)
class ReviewJobPlan:
    review_job_id: int
    model_partition: str
    runner: str | None
    runner_model: str | None
    runner_effort: str | None
    created_at: str
    completed_at: str | None
    status: str
    failure_reason: str | None
    telemetry_json: str | None
    prompt_path: str
    bundle_output_path: str
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


def _placeholders(values: Sequence[object]) -> str:
    return ", ".join("?" for _ in values)


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
    conn.execute(
        """
        INSERT OR IGNORE INTO review_file_snapshots (
            path,
            content_sha256,
            content_text,
            captured_at
        ) VALUES (?, ?, ?, ?)
        """,
        (normalized_path, content_sha256, content_text, iso_now()),
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
        completed_at=row["completed_at"],
        status=row["status"],
        failure_reason=row["failure_reason"],
        telemetry_json=row["telemetry_json"],
        packing=row["packing"],
    )


def _review_pair_from_row(row: sqlite3.Row, *, result_path: str | None) -> ReviewPairRow:
    return ReviewPairRow(
        review_pair_id=row["review_pair_id"],
        review_job_id=row["review_job_id"],
        note_path=row["note_path"],
        gate_path=row["gate_path"],
        model_partition=row["model_partition"],
        pair_ordinal=row["pair_ordinal"],
        result_kind=row["result_kind"],
        decision=row["decision"],
        result_path=result_path,
        reviewed_note_snapshot_id=row["reviewed_note_snapshot_id"],
        reviewed_gate_snapshot_id=row["reviewed_gate_snapshot_id"],
        reviewed_at=row["reviewed_at"],
    )


def _result_paths_for_review_jobs(conn: sqlite3.Connection, review_job_ids: set[int]) -> dict[int, str]:
    if not review_job_ids:
        return {}
    placeholders = ", ".join("?" for _ in review_job_ids)
    rows = conn.execute(
        f"""
        SELECT
            rp.review_pair_id,
            rp.review_job_id,
            rp.note_path,
            rp.gate_path,
            rp.pair_ordinal,
            j.packing
        FROM review_pairs AS rp
        JOIN review_jobs AS j
          ON j.review_job_id = rp.review_job_id
        WHERE rp.review_job_id IN ({placeholders})
        ORDER BY rp.review_job_id, rp.pair_ordinal, rp.note_path, rp.gate_path
        """,
        tuple(sorted(review_job_ids)),
    ).fetchall()
    grouped: dict[int, tuple[str, list[_ReviewPairPathInput]]] = {}
    for row in rows:
        review_job_id = int(row["review_job_id"])
        packing = str(row["packing"])
        if review_job_id not in grouped:
            grouped[review_job_id] = (packing, [])
        grouped[review_job_id][1].append(
            _ReviewPairPathInput(
                review_pair_id=int(row["review_pair_id"]),
                note_path=str(row["note_path"]),
                gate_path=str(row["gate_path"]),
                pair_ordinal=int(row["pair_ordinal"]),
            )
        )

    result: dict[int, str] = {}
    for review_job_id, (packing, pairs) in grouped.items():
        result.update(
            result_paths_by_pair_id(
                review_job_id=review_job_id,
                packing=packing,
                pairs=pairs,
            )
        )
    return result


def _review_pairs_from_rows(conn: sqlite3.Connection, rows: Sequence[sqlite3.Row]) -> list[ReviewPairRow]:
    result_paths = _result_paths_for_review_jobs(
        conn,
        {int(row["review_job_id"]) for row in rows},
    )
    return [
        _review_pair_from_row(
            row,
            result_path=result_paths.get(int(row["review_pair_id"])),
        )
        for row in rows
    ]


def create_job(
    conn: sqlite3.Connection,
    *,
    model_partition: str,
    runner: str | None,
    created_at: str,
    packing: str,
    status: str,
    runner_model: str | None = None,
    runner_effort: str | None = None,
    completed_at: str | None = None,
    failure_reason: str | None = None,
    telemetry_json: str | None = None,
) -> int:
    model_partition = normalize_model_partition(model_partition)
    runner_effort = _validated_runner_effort(
        model_partition=model_partition,
        runner_model=runner_model,
        runner_effort=runner_effort,
    )
    cursor = conn.execute(
        """
        INSERT INTO review_jobs (
            model_partition,
            runner,
            runner_model,
            runner_effort,
            created_at,
            completed_at,
            status,
            failure_reason,
            telemetry_json,
            packing
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            model_partition,
            runner,
            runner_model,
            runner_effort,
            created_at,
            completed_at,
            status,
            failure_reason,
            telemetry_json,
            packing,
        ),
    )
    return int(cursor.lastrowid)


def create_review_pairs(
    conn: sqlite3.Connection,
    *,
    review_job_id: int,
    pairs: Sequence[ReviewPairRequest],
) -> list[int]:
    result_kinds = {pair.result_kind for pair in pairs}
    invalid_result_kinds = result_kinds - {"verdict", "report"}
    if invalid_result_kinds:
        raise ValueError(f"invalid result kind: {sorted(invalid_result_kinds)}")
    if len(result_kinds) > 1:
        raise ValueError("review job cannot mix result kinds")
    review_pair_ids: list[int] = []
    for pair in pairs:
        cursor = conn.execute(
            """
            INSERT INTO review_pairs (
                review_job_id,
                note_path,
                gate_path,
                pair_ordinal,
                result_kind,
                reviewed_note_snapshot_id,
                reviewed_gate_snapshot_id
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                review_job_id,
                pair.note_path,
                pair.gate_path,
                pair.pair_ordinal,
                pair.result_kind,
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
    status: str,
    packing: str,
    pairs: Sequence[ReviewPairRequest],
    runner_model: str | None = None,
    runner_effort: str | None = None,
) -> int:
    review_job_id = create_job(
        conn,
        model_partition=model_partition,
        runner=runner,
        runner_model=runner_model,
        runner_effort=runner_effort,
        created_at=created_at,
        packing=packing,
        status=status,
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
            completed_at,
            status,
            failure_reason,
            telemetry_json,
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
            rp.result_kind,
            rp.decision,
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
    return _review_pairs_from_rows(conn, rows)


def _job_plan_from_job(conn: sqlite3.Connection, job: ReviewJobRow) -> ReviewJobPlan:
    pairs = tuple(load_review_pairs_for_job(conn, review_job_id=job.review_job_id))
    return ReviewJobPlan(
        review_job_id=job.review_job_id,
        model_partition=job.model_partition,
        runner=job.runner,
        runner_model=job.runner_model,
        runner_effort=job.runner_effort,
        created_at=job.created_at,
        completed_at=job.completed_at,
        status=job.status,
        failure_reason=job.failure_reason,
        telemetry_json=job.telemetry_json,
        prompt_path=prompt_path_rel(job.review_job_id),
        bundle_output_path=bundle_output_path_rel(job.review_job_id),
        packing=job.packing,
        pairs=pairs,
    )


def load_review_job_plan(
    conn: sqlite3.Connection,
    *,
    review_job_id: int,
) -> ReviewJobPlan | None:
    job = load_review_job(conn, review_job_id=review_job_id)
    if job is None:
        return None
    return _job_plan_from_job(conn, job)


def list_review_job_plans(
    conn: sqlite3.Connection,
    *,
    status: str | None = None,
    model_partition: str | None = None,
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
            completed_at,
            status,
            failure_reason,
            telemetry_json,
            packing
        FROM review_jobs
        {where_sql}
        ORDER BY created_at ASC, review_job_id ASC
        """,
        tuple(params),
    ).fetchall()
    return [_job_plan_from_job(conn, _review_job_from_row(row)) for row in rows]


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
            accepted_at,
            result_kind,
            decision
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
            result_kind=row["result_kind"],
            decision=row["decision"],
        )
        for row in rows
    }


def attach_execution_data(
    conn: sqlite3.Connection,
    *,
    review_job_id: int,
    runner: str | None = None,
    telemetry_json: str | None = None,
    runner_model: str | None = None,
    runner_effort: str | None = None,
) -> None:
    if runner_model is not None or runner_effort is not None:
        row = conn.execute(
            """
            SELECT model_partition, runner_model, runner_effort
            FROM review_jobs
            WHERE review_job_id = ?
            """,
            (review_job_id,),
        ).fetchone()
        if row is None:
            return
        effective_model = runner_model if runner_model is not None else row["runner_model"]
        effective_effort = runner_effort if runner_effort is not None else row["runner_effort"]
        normalized_effort = _validated_runner_effort(
            model_partition=row["model_partition"],
            runner_model=effective_model,
            runner_effort=effective_effort,
        )
        if runner_effort is not None:
            runner_effort = normalized_effort
    conn.execute(
        """
        UPDATE review_jobs
        SET runner = COALESCE(?, runner),
            telemetry_json = COALESCE(?, telemetry_json),
            runner_model = COALESCE(?, runner_model),
            runner_effort = COALESCE(?, runner_effort)
        WHERE review_job_id = ?
        """,
        (runner, telemetry_json, runner_model, runner_effort, review_job_id),
    )


def complete_review_job(
    conn: sqlite3.Connection,
    *,
    review_job_id: int,
    completed_at: str,
) -> None:
    conn.execute(
        """
        UPDATE review_jobs
        SET status = 'completed',
            completed_at = ?,
            failure_reason = NULL
        WHERE review_job_id = ?
        """,
        (completed_at, review_job_id),
    )


def fail_review_job(
    conn: sqlite3.Connection,
    *,
    review_job_id: int,
    failure_reason: str,
    completed_at: str,
) -> None:
    conn.execute(
        """
        UPDATE review_pairs
        SET decision = NULL,
            reviewed_at = NULL
        WHERE review_job_id = ?
        """,
        (review_job_id,),
    )
    conn.execute(
        """
        UPDATE review_jobs
        SET status = 'failed',
            completed_at = ?,
            failure_reason = ?
        WHERE review_job_id = ?
        """,
        (
            completed_at,
            failure_reason,
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
        if requested_pair.result_kind == "verdict" and review_pair.decision is None:
            raise ValueError(f"verdict pair requires a decision: {review_pair.note_path} :: {review_pair.gate_path}")
        if requested_pair.result_kind == "report" and review_pair.decision is not None:
            raise ValueError(f"report pair cannot have a decision: {review_pair.note_path} :: {review_pair.gate_path}")
        conn.execute(
            """
            UPDATE review_pairs
            SET decision = ?,
                reviewed_at = ?
            WHERE review_pair_id = ?
            """,
            (
                review_pair.decision,
                review_pair.reviewed_at or reviewed_at,
                requested_pair.review_pair_id,
            ),
        )
        completed_pair_ids.append(requested_pair.review_pair_id)
    return completed_pair_ids


def upsert_acceptance(
    conn: sqlite3.Connection,
    *,
    note_path: str,
    gate_path: str,
    model_partition: str,
    accepted_review_pair_id: int,
    accepted_note_snapshot_id: int | None = None,
    accepted_gate_snapshot_id: int | None = None,
    accepted_at: str,
) -> SupersededAcceptance | None:
    if accepted_review_pair_id is None:
        raise ValueError("accepted_review_pair_id is required")
    model_partition = normalize_model_partition(model_partition)
    row = conn.execute(
        """
        SELECT
            rp.note_path,
            rp.gate_path,
            rp.result_kind,
            rp.decision,
            rp.reviewed_at,
            j.model_partition
        FROM review_pairs AS rp
        JOIN review_jobs AS j
          ON j.review_job_id = rp.review_job_id
        WHERE rp.review_pair_id = ?
        """,
        (accepted_review_pair_id,),
    ).fetchone()
    if row is None:
        raise ValueError(f"accepted review pair not found: {accepted_review_pair_id}")
    completed = row["reviewed_at"] is not None and (
        row["result_kind"] == "report" or row["decision"] is not None
    )
    if not completed:
        raise ValueError(f"accepted review pair is incomplete: {accepted_review_pair_id}")
    if (
        row["note_path"] != note_path
        or row["gate_path"] != gate_path
        or row["model_partition"] != model_partition
    ):
        raise ValueError(f"accepted review pair does not match acceptance key: {accepted_review_pair_id}")
    previous = conn.execute(
        """
        SELECT
            note_path,
            gate_path,
            model_partition,
            accepted_review_pair_id,
            accepted_note_snapshot_id,
            accepted_gate_snapshot_id
        FROM acceptance
        WHERE note_path = ?
          AND gate_path = ?
          AND model_partition = ?
        """,
        (note_path, gate_path, model_partition),
    ).fetchone()
    conn.execute(
        """
        INSERT INTO acceptance (
            note_path,
            gate_path,
            model_partition,
            accepted_review_pair_id,
            accepted_note_snapshot_id,
            accepted_gate_snapshot_id,
            accepted_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(note_path, gate_path, model_partition)
        DO UPDATE SET
            accepted_review_pair_id = excluded.accepted_review_pair_id,
            accepted_note_snapshot_id = excluded.accepted_note_snapshot_id,
            accepted_gate_snapshot_id = excluded.accepted_gate_snapshot_id,
            accepted_at = excluded.accepted_at
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
    if previous is None:
        return None
    return SupersededAcceptance(
        note_path=previous["note_path"],
        gate_path=previous["gate_path"],
        model_partition=previous["model_partition"],
        accepted_review_pair_id=previous["accepted_review_pair_id"],
        accepted_note_snapshot_id=previous["accepted_note_snapshot_id"],
        accepted_gate_snapshot_id=previous["accepted_gate_snapshot_id"],
    )


def prune_superseded_acceptances(
    conn: sqlite3.Connection,
    superseded: Sequence[SupersededAcceptance | None],
) -> set[int]:
    """Delete superseded review evidence and return whole jobs deleted from the DB."""
    superseded_rows = [row for row in superseded if row is not None]
    if not superseded_rows:
        return set()

    candidate_snapshot_ids: set[int] = {
        snapshot_id
        for row in superseded_rows
        for snapshot_id in (row.accepted_note_snapshot_id, row.accepted_gate_snapshot_id)
        if snapshot_id is not None
    }
    candidate_pair_ids = tuple(sorted({row.accepted_review_pair_id for row in superseded_rows}))
    obsolete_pair_rows: list[sqlite3.Row] = []
    if candidate_pair_ids:
        obsolete_pair_rows = conn.execute(
            f"""
            SELECT
                review_pair_id,
                review_job_id,
                reviewed_note_snapshot_id,
                reviewed_gate_snapshot_id
            FROM review_pairs AS rp
            WHERE review_pair_id IN ({_placeholders(candidate_pair_ids)})
              AND NOT EXISTS (
                  SELECT 1
                  FROM acceptance AS a
                  WHERE a.accepted_review_pair_id = rp.review_pair_id
              )
            ORDER BY review_pair_id
            """,
            candidate_pair_ids,
        ).fetchall()

    obsolete_pair_ids = tuple(int(row["review_pair_id"]) for row in obsolete_pair_rows)
    candidate_job_ids = tuple(sorted({int(row["review_job_id"]) for row in obsolete_pair_rows}))
    for row in obsolete_pair_rows:
        for snapshot_id in (row["reviewed_note_snapshot_id"], row["reviewed_gate_snapshot_id"]):
            if snapshot_id is not None:
                candidate_snapshot_ids.add(int(snapshot_id))

    deleted_job_ids: set[int] = set()
    if obsolete_pair_ids:
        conn.execute(
            f"""
            DELETE FROM review_pairs
            WHERE review_pair_id IN ({_placeholders(obsolete_pair_ids)})
            """,
            obsolete_pair_ids,
        )
    if candidate_job_ids:
        deletable_job_rows = conn.execute(
            f"""
            SELECT review_job_id
            FROM review_jobs AS j
            WHERE review_job_id IN ({_placeholders(candidate_job_ids)})
              AND NOT EXISTS (
                  SELECT 1
                  FROM review_pairs AS rp
                  WHERE rp.review_job_id = j.review_job_id
              )
            ORDER BY review_job_id
            """,
            candidate_job_ids,
        ).fetchall()
        deleted_job_ids = {int(row["review_job_id"]) for row in deletable_job_rows}
        deleted_job_id_tuple = tuple(sorted(deleted_job_ids))
        if deleted_job_id_tuple:
            conn.execute(
                f"""
                DELETE FROM review_jobs
                WHERE review_job_id IN ({_placeholders(deleted_job_id_tuple)})
                """,
                deleted_job_id_tuple,
            )

    candidate_snapshot_id_tuple = tuple(sorted(candidate_snapshot_ids))
    if candidate_snapshot_id_tuple:
        conn.execute(
            f"""
            DELETE FROM review_file_snapshots
            WHERE snapshot_id IN ({_placeholders(candidate_snapshot_id_tuple)})
              AND NOT EXISTS (
                  SELECT 1
                  FROM acceptance AS a
                  WHERE a.accepted_note_snapshot_id = review_file_snapshots.snapshot_id
                     OR a.accepted_gate_snapshot_id = review_file_snapshots.snapshot_id
              )
              AND NOT EXISTS (
                  SELECT 1
                  FROM review_pairs AS rp
                  WHERE rp.reviewed_note_snapshot_id = review_file_snapshots.snapshot_id
                     OR rp.reviewed_gate_snapshot_id = review_file_snapshots.snapshot_id
              )
            """,
            candidate_snapshot_id_tuple,
        )
    return deleted_job_ids


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
            rp.result_kind,
            rp.decision,
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
    return _review_pairs_from_rows(conn, rows)


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
            rp.result_kind,
            rp.decision,
            rp.reviewed_note_snapshot_id,
            rp.reviewed_gate_snapshot_id,
            rp.reviewed_at
        FROM review_pairs AS rp
        JOIN review_jobs AS j
          ON j.review_job_id = rp.review_job_id
        WHERE rp.note_path = ?
          AND rp.gate_path = ?
          AND j.model_partition = ?
          AND j.status = 'completed'
          AND rp.reviewed_at IS NOT NULL
          AND (rp.result_kind = 'report' OR rp.decision IS NOT NULL)
        ORDER BY rp.reviewed_at DESC, rp.review_pair_id DESC
        LIMIT 1
        """,
        (note_path, gate_path, model_partition),
    ).fetchone()
    if row is None:
        return None
    pairs = _review_pairs_from_rows(conn, [row])
    return pairs[0]


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
        SELECT
            rp.review_pair_id,
            rp.review_job_id,
            rp.note_path,
            rp.gate_path,
            j.model_partition AS model_partition,
            rp.pair_ordinal,
            rp.result_kind,
            rp.decision,
            rp.reviewed_note_snapshot_id,
            rp.reviewed_gate_snapshot_id,
            rp.reviewed_at
        FROM current_gate_acceptances AS a
        JOIN review_pairs AS rp
          ON rp.review_pair_id = a.accepted_review_pair_id
        JOIN review_jobs AS j
          ON j.review_job_id = rp.review_job_id
         AND j.model_partition = a.model_partition
        {where_sql}
        """,
        tuple(params),
    ).fetchall()
    result: dict[tuple[str, str, str], ReviewPairRow] = {}
    for pair in _review_pairs_from_rows(conn, rows):
        key = (pair.note_path, pair.gate_path, pair.model_partition)
        result[key] = pair
    return result
