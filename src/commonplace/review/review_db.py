#!/usr/bin/env python3
"""Helpers for the canonical review-store SQLite database."""

from __future__ import annotations

import os
import sqlite3
from dataclasses import asdict, dataclass
from importlib import resources
from pathlib import Path
from typing import Sequence

from commonplace.lib.hashing import content_sha256_for_text
from commonplace.review.artifacts import job_output_path_rel, prompt_path_rel, result_path
from commonplace.review.clock import iso_now
from commonplace.review.paths import criterion_id_from_stored_path, normalize_repo_relative_path
from commonplace.review.review_model import build_model_partition, normalize_model_partition, normalize_reasoning_effort
from commonplace.review.review_schema import connect as connect
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
class FreshnessBaseline:
    note_path: str
    criterion_path: str
    model_partition: str
    evidence_review_pair_id: int
    baseline_note_snapshot_id: int
    baseline_criterion_snapshot_id: int
    baseline_note_hash: str
    baseline_criterion_hash: str
    baseline_note_text: str
    baseline_criterion_text: str
    baseline_updated_at: str
    result_kind: str
    outcome: str | None

    @property
    def criterion_id(self) -> str:
        return criterion_id_from_stored_path(self.criterion_path)


@dataclass(frozen=True)
class SupersededFreshnessBaseline:
    note_path: str
    criterion_path: str
    model_partition: str
    evidence_review_pair_id: int
    baseline_note_snapshot_id: int | None
    baseline_criterion_snapshot_id: int | None


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
    grouping: str


@dataclass(frozen=True)
class ReviewPairRow:
    review_pair_id: int
    review_job_id: int
    note_path: str
    criterion_path: str
    model_partition: str
    pair_ordinal: int
    result_kind: str
    outcome: str | None
    result_path: str | None
    reviewed_note_snapshot_id: int | None
    reviewed_criterion_snapshot_id: int | None
    completed_at: str | None

    @property
    def criterion_id(self) -> str:
        return criterion_id_from_stored_path(self.criterion_path)

    def to_payload(self) -> dict[str, object]:
        return {
            "review_pair_id": self.review_pair_id,
            "note_path": self.note_path,
            "criterion_path": self.criterion_path,
            "criterion_id": self.criterion_id,
            "pair_ordinal": self.pair_ordinal,
            "result_kind": self.result_kind,
            "outcome": self.outcome,
            "result_path": self.result_path,
        }


@dataclass(frozen=True)
class ReviewPairRequest:
    note_path: str
    criterion_path: str
    pair_ordinal: int
    result_kind: str
    reviewed_note_snapshot_id: int | None = None
    reviewed_criterion_snapshot_id: int | None = None


@dataclass(frozen=True)
class ReviewPairCompletion:
    note_path: str
    criterion_path: str
    outcome: str | None
    completed_at: str | None = None


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
    job_output_path: str
    grouping: str
    pairs: tuple[ReviewPairRow, ...]

    def to_payload(self, *, include_timestamps: bool = False) -> dict[str, object]:
        ordered_pairs = sorted(self.pairs, key=lambda pair: pair.pair_ordinal)
        pair_items = [pair.to_payload() for pair in ordered_pairs]
        payload: dict[str, object] = {
            "review_job_id": self.review_job_id,
            "status": self.status,
            "model_partition": self.model_partition,
            "runner": self.runner,
            "runner_model": self.runner_model,
            "runner_effort": self.runner_effort,
            "grouping": self.grouping,
            "prompt_path": self.prompt_path,
            "job_output_path": self.job_output_path,
            "pair_count": len(self.pairs),
            "pairs": pair_items,
        }
        if include_timestamps:
            payload.update(
                {
                    "created_at": self.created_at,
                    "completed_at": self.completed_at,
                    "failure_reason": self.failure_reason,
                }
            )
            for item, pair in zip(pair_items, ordered_pairs, strict=True):
                item["completed_at"] = pair.completed_at
        return payload


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
    normalized_path = normalize_repo_relative_path(path, label="snapshot path")
    content_text = (repo_root / normalized_path).read_text(encoding="utf-8")
    content_sha256 = content_sha256_for_text(content_text)
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
        grouping=row["grouping"],
    )


_PAIR_SELECT = """
    rp.review_pair_id,
    rp.review_job_id,
    rp.note_path,
    rp.criterion_path,
    j.model_partition AS model_partition,
    j.grouping AS grouping,
    rp.pair_ordinal,
    rp.result_kind,
    rp.outcome,
    rp.reviewed_note_snapshot_id,
    rp.reviewed_criterion_snapshot_id,
    rp.completed_at
"""


def _review_pair_from_row(row: sqlite3.Row) -> ReviewPairRow:
    return ReviewPairRow(
        review_pair_id=row["review_pair_id"],
        review_job_id=row["review_job_id"],
        note_path=row["note_path"],
        criterion_path=row["criterion_path"],
        model_partition=row["model_partition"],
        pair_ordinal=row["pair_ordinal"],
        result_kind=row["result_kind"],
        outcome=row["outcome"],
        result_path=result_path(
            review_job_id=row["review_job_id"],
            grouping=row["grouping"],
            note_path=row["note_path"],
            criterion_path=row["criterion_path"],
            pair_ordinal=row["pair_ordinal"],
        ),
        reviewed_note_snapshot_id=row["reviewed_note_snapshot_id"],
        reviewed_criterion_snapshot_id=row["reviewed_criterion_snapshot_id"],
        completed_at=row["completed_at"],
    )


def _review_pairs_from_rows(rows: Sequence[sqlite3.Row]) -> list[ReviewPairRow]:
    return [_review_pair_from_row(row) for row in rows]


def create_job(
    conn: sqlite3.Connection,
    *,
    model_partition: str,
    runner: str | None,
    created_at: str,
    grouping: str,
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
            grouping
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
            grouping,
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
                criterion_path,
                pair_ordinal,
                result_kind,
                reviewed_note_snapshot_id,
                reviewed_criterion_snapshot_id
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                review_job_id,
                pair.note_path,
                pair.criterion_path,
                pair.pair_ordinal,
                pair.result_kind,
                pair.reviewed_note_snapshot_id,
                pair.reviewed_criterion_snapshot_id,
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
    grouping: str,
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
        grouping=grouping,
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
            grouping
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
        f"""
        SELECT {_PAIR_SELECT}
        FROM review_pairs AS rp
        JOIN review_jobs AS j
          ON j.review_job_id = rp.review_job_id
        WHERE rp.review_job_id = ?
        ORDER BY rp.pair_ordinal, rp.note_path, rp.criterion_path
        """,
        (review_job_id,),
    ).fetchall()
    return _review_pairs_from_rows(rows)


def _job_plan_from_job(conn: sqlite3.Connection, job: ReviewJobRow) -> ReviewJobPlan:
    return ReviewJobPlan(
        **asdict(job),
        prompt_path=prompt_path_rel(job.review_job_id),
        job_output_path=job_output_path_rel(job.review_job_id),
        pairs=tuple(load_review_pairs_for_job(conn, review_job_id=job.review_job_id)),
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
            grouping
        FROM review_jobs
        {where_sql}
        ORDER BY created_at ASC, review_job_id ASC
        """,
        tuple(params),
    ).fetchall()
    return [_job_plan_from_job(conn, _review_job_from_row(row)) for row in rows]


def load_current_freshness_baselines(conn: sqlite3.Connection) -> dict[tuple[str, str, str], FreshnessBaseline]:
    rows = conn.execute(
        """
        SELECT
            note_path,
            criterion_path,
            model_partition,
            evidence_review_pair_id,
            baseline_note_snapshot_id,
            baseline_criterion_snapshot_id,
            baseline_note_hash,
            baseline_criterion_hash,
            baseline_note_text,
            baseline_criterion_text,
            baseline_updated_at,
            result_kind,
            outcome
        FROM current_freshness_baselines
        """
    ).fetchall()
    return {
        (row["note_path"], row["criterion_path"], row["model_partition"]): FreshnessBaseline(
            note_path=row["note_path"],
            criterion_path=row["criterion_path"],
            model_partition=row["model_partition"],
            evidence_review_pair_id=row["evidence_review_pair_id"],
            baseline_note_snapshot_id=row["baseline_note_snapshot_id"],
            baseline_criterion_snapshot_id=row["baseline_criterion_snapshot_id"],
            baseline_note_hash=row["baseline_note_hash"],
            baseline_criterion_hash=row["baseline_criterion_hash"],
            baseline_note_text=row["baseline_note_text"],
            baseline_criterion_text=row["baseline_criterion_text"],
            baseline_updated_at=row["baseline_updated_at"],
            result_kind=row["result_kind"],
            outcome=row["outcome"],
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
            raise ValueError(f"review job not found: {review_job_id}")
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
    counts = conn.execute(
        """
        SELECT
            count(*) AS pair_count,
            sum(
                CASE
                    WHEN completed_at IS NULL THEN 1
                    WHEN result_kind = 'verdict' AND outcome IS NULL THEN 1
                    WHEN result_kind = 'report' AND outcome IS NOT NULL THEN 1
                    ELSE 0
                END
            ) AS incomplete_count
        FROM review_pairs
        WHERE review_job_id = ?
        """,
        (review_job_id,),
    ).fetchone()
    if counts is None or counts["pair_count"] == 0:
        raise ValueError(f"review job has no pairs: {review_job_id}")
    if counts["incomplete_count"]:
        raise ValueError(f"review job has incomplete pairs: {review_job_id}")
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
        SET outcome = NULL,
            completed_at = NULL
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
    completed_at: str,
) -> list[int]:
    requested = {
        (pair.note_path, pair.criterion_path): pair
        for pair in load_review_pairs_for_job(conn, review_job_id=review_job_id)
    }
    completed_pair_ids: list[int] = []
    seen: set[tuple[str, str]] = set()
    for review_pair in review_pairs:
        key = (review_pair.note_path, review_pair.criterion_path)
        if key in seen:
            raise ValueError(f"duplicate completed pair: {review_pair.note_path} :: {review_pair.criterion_path}")
        seen.add(key)
        requested_pair = requested.get(key)
        if requested_pair is None:
            raise ValueError(
                f"pair {review_pair.note_path} :: {review_pair.criterion_path} is not part of review job {review_job_id}"
            )
        if requested_pair.result_kind == "verdict" and review_pair.outcome is None:
            raise ValueError(f"verdict pair requires an outcome: {review_pair.note_path} :: {review_pair.criterion_path}")
        if requested_pair.result_kind == "report" and review_pair.outcome is not None:
            raise ValueError(f"report pair cannot have an outcome: {review_pair.note_path} :: {review_pair.criterion_path}")
        conn.execute(
            """
            UPDATE review_pairs
            SET outcome = ?,
                completed_at = ?
            WHERE review_pair_id = ?
            """,
            (
                review_pair.outcome,
                review_pair.completed_at or completed_at,
                requested_pair.review_pair_id,
            ),
        )
        completed_pair_ids.append(requested_pair.review_pair_id)
    return completed_pair_ids


def upsert_freshness_baseline(
    conn: sqlite3.Connection,
    *,
    note_path: str,
    criterion_path: str,
    model_partition: str,
    evidence_review_pair_id: int,
    baseline_note_snapshot_id: int,
    baseline_criterion_snapshot_id: int,
    baseline_updated_at: str,
) -> SupersededFreshnessBaseline | None:
    if evidence_review_pair_id is None:
        raise ValueError("evidence_review_pair_id is required")
    model_partition = normalize_model_partition(model_partition)
    row = conn.execute(
        """
        SELECT
            rp.note_path,
            rp.criterion_path,
            rp.result_kind,
            rp.outcome,
            rp.completed_at,
            j.model_partition,
            j.status AS job_status
        FROM review_pairs AS rp
        JOIN review_jobs AS j
          ON j.review_job_id = rp.review_job_id
        WHERE rp.review_pair_id = ?
        """,
        (evidence_review_pair_id,),
    ).fetchone()
    if row is None:
        raise ValueError(f"evidence review pair not found: {evidence_review_pair_id}")
    completed = row["completed_at"] is not None and (
        row["result_kind"] == "report" or row["outcome"] is not None
    )
    if not completed:
        raise ValueError(f"evidence review pair is incomplete: {evidence_review_pair_id}")
    if row["job_status"] != "completed":
        raise ValueError(f"evidence review pair job is not completed: {evidence_review_pair_id}")
    if (
        row["note_path"] != note_path
        or row["criterion_path"] != criterion_path
        or row["model_partition"] != model_partition
    ):
        raise ValueError(f"evidence review pair does not match freshness baseline key: {evidence_review_pair_id}")
    snapshot_rows = conn.execute(
        """
        SELECT snapshot_id, path, content_text
        FROM review_file_snapshots
        WHERE snapshot_id IN (?, ?)
        """,
        (baseline_note_snapshot_id, baseline_criterion_snapshot_id),
    ).fetchall()
    snapshots = {int(snapshot["snapshot_id"]): snapshot for snapshot in snapshot_rows}
    note_snapshot = snapshots.get(baseline_note_snapshot_id)
    criterion_snapshot = snapshots.get(baseline_criterion_snapshot_id)
    if note_snapshot is None or note_snapshot["path"] != note_path or note_snapshot["content_text"] is None:
        raise ValueError("baseline note snapshot is missing or does not match the note path")
    if (
        criterion_snapshot is None
        or criterion_snapshot["path"] != criterion_path
        or criterion_snapshot["content_text"] is None
    ):
        raise ValueError("baseline criterion snapshot is missing or does not match the criterion path")
    previous = conn.execute(
        """
        SELECT
            note_path,
            criterion_path,
            model_partition,
            evidence_review_pair_id,
            baseline_note_snapshot_id,
            baseline_criterion_snapshot_id
        FROM freshness_baselines
        WHERE note_path = ?
          AND criterion_path = ?
          AND model_partition = ?
        """,
        (note_path, criterion_path, model_partition),
    ).fetchone()
    conn.execute(
        """
        INSERT INTO freshness_baselines (
            note_path,
            criterion_path,
            model_partition,
            evidence_review_pair_id,
            baseline_note_snapshot_id,
            baseline_criterion_snapshot_id,
            baseline_updated_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(note_path, criterion_path, model_partition)
        DO UPDATE SET
            evidence_review_pair_id = excluded.evidence_review_pair_id,
            baseline_note_snapshot_id = excluded.baseline_note_snapshot_id,
            baseline_criterion_snapshot_id = excluded.baseline_criterion_snapshot_id,
            baseline_updated_at = excluded.baseline_updated_at
        """,
        (
            note_path,
            criterion_path,
            model_partition,
            evidence_review_pair_id,
            baseline_note_snapshot_id,
            baseline_criterion_snapshot_id,
            baseline_updated_at,
        ),
    )
    if previous is None:
        return None
    return SupersededFreshnessBaseline(
        note_path=previous["note_path"],
        criterion_path=previous["criterion_path"],
        model_partition=previous["model_partition"],
        evidence_review_pair_id=previous["evidence_review_pair_id"],
        baseline_note_snapshot_id=previous["baseline_note_snapshot_id"],
        baseline_criterion_snapshot_id=previous["baseline_criterion_snapshot_id"],
    )


def prune_superseded_freshness_baselines(
    conn: sqlite3.Connection,
    superseded: Sequence[SupersededFreshnessBaseline | None],
) -> set[int]:
    """Delete superseded review evidence and return whole jobs deleted from the DB."""
    superseded_rows = [row for row in superseded if row is not None]
    if not superseded_rows:
        return set()

    candidate_snapshot_ids: set[int] = {
        snapshot_id
        for row in superseded_rows
        for snapshot_id in (row.baseline_note_snapshot_id, row.baseline_criterion_snapshot_id)
        if snapshot_id is not None
    }
    candidate_pair_ids = tuple(sorted({row.evidence_review_pair_id for row in superseded_rows}))
    obsolete_pair_rows: list[sqlite3.Row] = []
    if candidate_pair_ids:
        obsolete_pair_rows = conn.execute(
            f"""
            SELECT
                review_pair_id,
                review_job_id,
                reviewed_note_snapshot_id,
                reviewed_criterion_snapshot_id
            FROM review_pairs AS rp
            WHERE review_pair_id IN ({_placeholders(candidate_pair_ids)})
              AND NOT EXISTS (
                  SELECT 1
                  FROM freshness_baselines AS a
                  WHERE a.evidence_review_pair_id = rp.review_pair_id
              )
            ORDER BY review_pair_id
            """,
            candidate_pair_ids,
        ).fetchall()

    obsolete_pair_ids = tuple(int(row["review_pair_id"]) for row in obsolete_pair_rows)
    candidate_job_ids = tuple(sorted({int(row["review_job_id"]) for row in obsolete_pair_rows}))
    for row in obsolete_pair_rows:
        for snapshot_id in (row["reviewed_note_snapshot_id"], row["reviewed_criterion_snapshot_id"]):
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
                  FROM freshness_baselines AS a
                  WHERE a.baseline_note_snapshot_id = review_file_snapshots.snapshot_id
                     OR a.baseline_criterion_snapshot_id = review_file_snapshots.snapshot_id
              )
              AND NOT EXISTS (
                  SELECT 1
                  FROM review_pairs AS rp
                  WHERE rp.reviewed_note_snapshot_id = review_file_snapshots.snapshot_id
                     OR rp.reviewed_criterion_snapshot_id = review_file_snapshots.snapshot_id
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
        f"""
        SELECT {_PAIR_SELECT}
        FROM review_pairs AS rp
        JOIN review_jobs AS j
          ON j.review_job_id = rp.review_job_id
        WHERE rp.note_path = ? AND j.model_partition = ?
        ORDER BY rp.criterion_path, rp.completed_at, rp.review_pair_id
        """,
        (note_path, model_partition),
    ).fetchall()
    return _review_pairs_from_rows(rows)


def load_latest_completed_review_pair(
    conn: sqlite3.Connection,
    *,
    note_path: str,
    criterion_path: str,
    model_partition: str,
) -> ReviewPairRow | None:
    row = conn.execute(
        f"""
        SELECT {_PAIR_SELECT}
        FROM review_pairs AS rp
        JOIN review_jobs AS j
          ON j.review_job_id = rp.review_job_id
        WHERE rp.note_path = ?
          AND rp.criterion_path = ?
          AND j.model_partition = ?
          AND j.status = 'completed'
          AND rp.completed_at IS NOT NULL
          AND (rp.result_kind = 'report' OR rp.outcome IS NOT NULL)
        ORDER BY rp.completed_at DESC, rp.review_pair_id DESC
        LIMIT 1
        """,
        (note_path, criterion_path, model_partition),
    ).fetchone()
    if row is None:
        return None
    pairs = _review_pairs_from_rows([row])
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
        SELECT {_PAIR_SELECT}
        FROM current_freshness_baselines AS a
        JOIN review_pairs AS rp
          ON rp.review_pair_id = a.evidence_review_pair_id
        JOIN review_jobs AS j
          ON j.review_job_id = rp.review_job_id
         AND j.model_partition = a.model_partition
        {where_sql}
        """,
        tuple(params),
    ).fetchall()
    result: dict[tuple[str, str, str], ReviewPairRow] = {}
    for pair in _review_pairs_from_rows(rows):
        key = (pair.note_path, pair.criterion_path, pair.model_partition)
        result[key] = pair
    return result
