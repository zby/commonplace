"""Finalize review jobs from job-owned output and advance acceptance state."""

from __future__ import annotations

import sqlite3
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

from commonplace.review.artifacts import (
    bundle_artifact_dir,
    repo_relative_path,
    write_manifest,
    write_pair_result_files_to_derived_paths,
)
from commonplace.review import review_db
from commonplace.review.clock import iso_now
from commonplace.review.protocol.parser import ParsedPairBundle, parse_pair_bundle
from commonplace.review.review_db import ReviewPairCompletion, ReviewPairRow
from commonplace.review.review_model import build_model_partition


ACTIVE_REVIEW_JOB_STATUSES = frozenset({"queued"})


@dataclass(frozen=True)
class ExecutionMetadata:
    """Optional, per-harness execution provenance recorded at finalize time.

    This is the single seam for worker-provided execution metadata. The core
    stores these fields uninterpreted — ``telemetry_json`` in particular is an
    opaque blob the review system never parses. Harnesses that cannot produce
    provenance leave the fields ``None``; provenance is never required for a
    review's identity, which is ``(note_path, gate_path, model_partition)``.
    """

    runner: str | None = None
    runner_model: str | None = None
    runner_effort: str | None = None
    telemetry_json: str | None = None

    @property
    def is_empty(self) -> bool:
        return (
            self.runner is None
            and self.runner_model is None
            and self.runner_effort is None
            and self.telemetry_json is None
        )

    @property
    def derived_model_partition(self) -> str | None:
        if self.runner_model is None:
            return None
        return build_model_partition(self.runner_model, self.runner_effort)


@dataclass(frozen=True)
class FinalizeReviewJobOutcome:
    completed: bool
    state_changed: bool
    review_job_id: int
    completed_pair_count: int = 0
    failed: tuple[tuple[int, str], ...] = ()
    job_status: str | None = None
    reason: str | None = None
    warnings: tuple[str, ...] = ()

    @property
    def exit_code(self) -> int:
        return 0 if self.completed else 1

    def to_payload(self) -> dict[str, object]:
        if not self.state_changed:
            payload: dict[str, object] = {
                "completed": False,
                "state_changed": False,
                "review_job_id": self.review_job_id,
                "reason": self.reason,
            }
            if self.warnings:
                payload["warnings"] = list(self.warnings)
            return payload
        payload = {
            "completed": self.completed,
            "state_changed": True,
            "review_job_id": self.review_job_id,
            "completed_pair_count": self.completed_pair_count,
            "failed": [
                {"review_job_id": review_job_id, "reason": reason}
                for review_job_id, reason in self.failed
            ],
            "job": {
                "review_job_id": self.review_job_id,
                "status": self.job_status,
            },
        }
        if self.warnings:
            payload["warnings"] = list(self.warnings)
        return payload


@dataclass(frozen=True)
class FinalizedReviewJob:
    pairs: list[ReviewPairRow]
    pruned_review_job_ids: frozenset[int]


# Preconditions and output loading.


def _precondition_failure(review_job_id: int, reason: str) -> FinalizeReviewJobOutcome:
    return FinalizeReviewJobOutcome(
        completed=False,
        state_changed=False,
        review_job_id=review_job_id,
        reason=reason,
    )


def finalize_review_job_from_owned_output(
    *,
    repo_root: Path,
    db_path: Path,
    review_job_id: int,
    execution: ExecutionMetadata = ExecutionMetadata(),
) -> FinalizeReviewJobOutcome:
    """Finalize one review job from its derived bundle output path."""
    with review_db.connect(db_path) as conn:
        try:
            plan = review_db.load_review_job_plan(conn, review_job_id=review_job_id)
        except ValueError as exc:
            return _precondition_failure(review_job_id, str(exc))
        if plan is None:
            return _precondition_failure(review_job_id, f"review job not found: {review_job_id}")
        if plan.status not in ACTIVE_REVIEW_JOB_STATUSES:
            return _precondition_failure(review_job_id, f"review job is not finalizable: {plan.status}")
        model_partition = execution.derived_model_partition
        if model_partition is not None:
            if model_partition != plan.model_partition:
                return _precondition_failure(
                    review_job_id,
                    f"review job model_partition {plan.model_partition!r} does not match supplied partition {model_partition!r}",
                )
        try:
            bundle_output_path = repo_relative_path(
                repo_root,
                plan.bundle_output_path,
                label="bundle output path",
            )
        except ValueError as exc:
            return _precondition_failure(review_job_id, str(exc))
        if not bundle_output_path.is_file():
            return _precondition_failure(
                review_job_id,
                f"bundle output file not found: {plan.bundle_output_path}",
            )

        # Record execution provenance once, up front. It is attached to the job row
        # here so it persists whether the job later completes or fails, and so the
        # finalization pipeline itself carries no execution-metadata plumbing.
        if not execution.is_empty:
            review_db.attach_execution_data(
                conn,
                review_job_id=review_job_id,
                runner=execution.runner,
                runner_model=execution.runner_model,
                runner_effort=execution.runner_effort,
                telemetry_json=execution.telemetry_json,
            )
            conn.commit()
            refreshed_plan = review_db.load_review_job_plan(conn, review_job_id=review_job_id)
            if refreshed_plan is not None:
                plan = refreshed_plan

        bundle_markdown = bundle_output_path.read_text(encoding="utf-8")
        expected_pairs = tuple((pair.note_path, pair.gate_path) for pair in plan.pairs)
        try:
            parsed = parse_pair_bundle(bundle_markdown, expected_pairs=expected_pairs)
            review_pairs = _review_pair_completions(expected_pairs=expected_pairs, parsed=parsed)
            finalized = record_and_finalize_job(
                conn,
                review_job_id=review_job_id,
                review_pairs=review_pairs,
            )
            write_pair_result_files_to_derived_paths(
                repo_root=repo_root,
                job=plan,
                pairs=finalized.pairs,
                canonical_texts=parsed.canonical_texts,
            )
        except (ValueError, OSError, sqlite3.IntegrityError) as exc:
            failure_reason = str(exc)
            warnings = _mark_failed(
                conn,
                repo_root=repo_root,
                review_job_id=review_job_id,
                failure_reason=failure_reason,
            )
            return FinalizeReviewJobOutcome(
                completed=False,
                state_changed=True,
                review_job_id=review_job_id,
                completed_pair_count=0,
                failed=((review_job_id, failure_reason),),
                job_status="failed",
                warnings=warnings,
            )
        conn.commit()
        warnings = (
            *_remove_pruned_job_artifact_dirs(repo_root, finalized.pruned_review_job_ids),
            *_refresh_manifest_warning(conn, repo_root=repo_root, review_job_id=review_job_id),
        )
        return FinalizeReviewJobOutcome(
            completed=True,
            state_changed=True,
            review_job_id=review_job_id,
            completed_pair_count=len(finalized.pairs),
            failed=(),
            job_status="completed",
            warnings=warnings,
        )


# DB completion and acceptance.


def record_and_finalize_job(
    conn: sqlite3.Connection,
    *,
    review_job_id: int,
    review_pairs: Sequence[ReviewPairCompletion] | None = None,
    completed_at: str | None = None,
) -> FinalizedReviewJob:
    """Record trusted completions for a job and return refreshed pair rows.

    The caller owns pair coverage validation before this function runs. This
    function keeps DB-local validation and acceptance writes together, but does
    not re-derive whether the completion set exactly matches the requested job.
    """
    review_job = review_db.load_review_job(conn, review_job_id=review_job_id)
    if review_job is None:
        raise ValueError(f"review job not found: {review_job_id}")
    if review_job.status not in ACTIVE_REVIEW_JOB_STATUSES:
        raise ValueError(f"review job is not finalizable: {review_job.status}")

    finished_at = completed_at or iso_now()
    review_db.complete_review_pairs(
        conn,
        review_job_id=review_job_id,
        review_pairs=review_pairs or (),
        reviewed_at=finished_at,
    )

    finalized_pairs = review_db.load_review_pairs_for_job(conn, review_job_id=review_job_id)
    superseded_acceptances: list[review_db.SupersededAcceptance | None] = []
    for pair in finalized_pairs:
        superseded_acceptances.append(
            review_db.upsert_acceptance(
                conn,
                note_path=pair.note_path,
                gate_path=pair.gate_path,
                model_partition=review_job.model_partition,
                accepted_review_pair_id=pair.review_pair_id,
                accepted_note_snapshot_id=pair.reviewed_note_snapshot_id,
                accepted_gate_snapshot_id=pair.reviewed_gate_snapshot_id,
                accepted_at=finished_at,
            )
        )
    pruned_review_job_ids = review_db.prune_superseded_acceptances(conn, superseded_acceptances)

    review_db.complete_review_job(conn, review_job_id=review_job_id, completed_at=finished_at)
    return FinalizedReviewJob(
        pairs=finalized_pairs,
        pruned_review_job_ids=frozenset(pruned_review_job_ids),
    )


# Failure marking.


def fail_active_review_jobs(
    *,
    db_path: Path,
    review_job_ids: list[int],
    failure_reason: str,
) -> None:
    if not review_job_ids:
        return
    completed_at = iso_now()
    with review_db.connect(db_path) as conn:
        rows = conn.execute(
            f"""
            SELECT review_job_id, status
            FROM review_jobs
            WHERE review_job_id IN ({", ".join("?" for _ in review_job_ids)})
            """,
            review_job_ids,
        ).fetchall()
        for row in rows:
            if row["status"] not in ACTIVE_REVIEW_JOB_STATUSES:
                continue
            review_db.fail_review_job(
                conn,
                review_job_id=int(row["review_job_id"]),
                failure_reason=failure_reason,
                completed_at=completed_at,
            )
        conn.commit()


# Artifact writes and manifest refresh.


def write_job_manifest_from_db(
    conn: sqlite3.Connection,
    *,
    repo_root: Path,
    review_job_id: int,
) -> None:
    plan = review_db.load_review_job_plan(conn, review_job_id=review_job_id)
    if plan is None:
        return
    artifact_dir = bundle_artifact_dir(repo_root, review_job_id)
    write_manifest(
        repo_root=repo_root,
        artifact_dir=artifact_dir,
        review_job_id=review_job_id,
        job_status=plan.status,
        packing=plan.packing,
        prompt_path=plan.prompt_path,
        bundle_output_path=plan.bundle_output_path,
        pairs=plan.pairs,
        failure_reason=plan.failure_reason,
    )


# Bundle parsing call and finalization orchestration.


def _review_pair_completions(
    *,
    expected_pairs: tuple[tuple[str, str], ...],
    parsed: ParsedPairBundle,
) -> tuple[ReviewPairCompletion, ...]:
    if not expected_pairs:
        raise ValueError("review job has no pairs")
    if parsed.missing:
        missing = ", ".join(f"{note_path} :: {gate_path}" for note_path, gate_path in sorted(parsed.missing))
        raise ValueError(f"missing pairs: {missing}")
    return tuple(
        ReviewPairCompletion(
            note_path=note_path,
            gate_path=gate_path,
            decision=parsed.reviews[(note_path, gate_path)].decision,
        )
        for note_path, gate_path in expected_pairs
    )


def _refresh_manifest_warning(
    conn: sqlite3.Connection,
    *,
    repo_root: Path,
    review_job_id: int,
) -> tuple[str, ...]:
    try:
        write_job_manifest_from_db(conn, repo_root=repo_root, review_job_id=review_job_id)
    except (OSError, ValueError) as exc:
        return (f"manifest refresh failed: {exc}",)
    return ()


def _remove_pruned_job_artifact_dirs(repo_root: Path, review_job_ids: frozenset[int]) -> tuple[str, ...]:
    warnings: list[str] = []
    for review_job_id in sorted(review_job_ids):
        artifact_dir = bundle_artifact_dir(repo_root, review_job_id)
        if not artifact_dir.exists():
            continue
        try:
            shutil.rmtree(artifact_dir)
        except OSError as exc:
            warnings.append(f"artifact directory cleanup failed for review job {review_job_id}: {exc}")
    return tuple(warnings)


def _mark_failed(
    conn: sqlite3.Connection,
    *,
    repo_root: Path,
    review_job_id: int,
    failure_reason: str,
) -> tuple[str, ...]:
    conn.rollback()
    review_db.fail_review_job(
        conn,
        review_job_id=review_job_id,
        failure_reason=failure_reason,
        completed_at=iso_now(),
    )
    conn.commit()
    return _refresh_manifest_warning(conn, repo_root=repo_root, review_job_id=review_job_id)
