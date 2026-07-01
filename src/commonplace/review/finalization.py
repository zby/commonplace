"""Finalize review jobs from job-owned output and advance acceptance state."""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

from commonplace.review.artifacts import (
    bundle_artifact_dir,
    repo_relative_path,
    result_paths_by_pair_id,
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


# Preconditions and output loading.


def _completed_pair_count(db_path: Path, review_job_id: int) -> int:
    with review_db.connect(db_path) as conn:
        plan = review_db.load_review_job_plan(conn, review_job_id=review_job_id, require_paths=False)
        if plan is None:
            return 0
        return sum(1 for pair in plan.pairs if pair.decision is not None)


def _job_status(db_path: Path, review_job_id: int) -> str | None:
    with review_db.connect(db_path) as conn:
        plan = review_db.load_review_job_plan(conn, review_job_id=review_job_id, require_paths=False)
        if plan is None:
            return None
        return plan.status


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
    telemetry_json: str | None = None,
    runner: str | None = None,
    runner_model: str | None = None,
    runner_effort: str | None = None,
) -> FinalizeReviewJobOutcome:
    """Finalize one review job from its derived bundle output path."""
    with review_db.connect(db_path) as conn:
        try:
            plan = review_db.load_review_job_plan(conn, review_job_id=review_job_id, require_paths=True)
        except ValueError as exc:
            return _precondition_failure(review_job_id, str(exc))
    if plan is None:
        return _precondition_failure(review_job_id, f"review job not found: {review_job_id}")
    if plan.status not in ACTIVE_REVIEW_JOB_STATUSES:
        return _precondition_failure(review_job_id, f"review job is not finalizable: {plan.status}")
    if runner_model is not None:
        model_partition = build_model_partition(runner_model, runner_effort)
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

    bundle_markdown = bundle_output_path.read_text(encoding="utf-8")
    expected_pairs = tuple((pair.note_path, pair.gate_path) for pair in plan.pairs)
    completed, failure_reason, warnings = finalize_job_bundle_markdown(
        repo_root=repo_root,
        db_path=db_path,
        review_job_id=review_job_id,
        expected_pairs=expected_pairs,
        bundle_markdown=bundle_markdown,
        telemetry_json=telemetry_json,
        runner=runner,
        runner_model=runner_model,
        runner_effort=runner_effort,
    )

    completed_pair_count = _completed_pair_count(db_path, review_job_id)
    job_status = _job_status(db_path, review_job_id)
    failed_tuple = () if failure_reason is None else ((review_job_id, failure_reason),)
    return FinalizeReviewJobOutcome(
        completed=completed,
        state_changed=True,
        review_job_id=review_job_id,
        completed_pair_count=completed_pair_count,
        failed=failed_tuple,
        job_status=job_status,
        warnings=warnings,
    )


# DB completion and acceptance.


def _job_coverage_failure(pairs: Sequence[ReviewPairRow]) -> str | None:
    if not pairs:
        return "review job has no pairs"
    missing = [
        f"{pair.note_path} :: {pair.gate_path}"
        for pair in pairs
        if pair.decision is None
    ]
    if not missing:
        return None
    return f"missing pairs: {', '.join(sorted(missing))}"


def record_and_finalize_job(
    conn: sqlite3.Connection,
    *,
    review_job_id: int,
    review_pairs: Sequence[ReviewPairCompletion] | None = None,
    completed_at: str | None = None,
    telemetry_json: str | None = None,
    runner: str | None = None,
    runner_model: str | None = None,
    runner_effort: str | None = None,
) -> int:
    review_job = review_db.load_review_job(conn, review_job_id=review_job_id)
    if review_job is None:
        raise ValueError(f"review job not found: {review_job_id}")
    if review_job.status not in ACTIVE_REVIEW_JOB_STATUSES:
        raise ValueError(f"review job is not finalizable: {review_job.status}")
    requested_pairs = review_db.load_review_pairs_for_job(conn, review_job_id=review_job_id)
    if not requested_pairs:
        raise ValueError("review job has no pairs")
    expected_keys = {(pair.note_path, pair.gate_path) for pair in requested_pairs}
    completed_keys = {
        (pair.note_path, pair.gate_path)
        for pair in review_pairs or ()
    }
    if completed_keys != expected_keys:
        missing = expected_keys - completed_keys
        extra = completed_keys - expected_keys
        parts: list[str] = []
        if missing:
            parts.append(
                "missing pairs: "
                + ", ".join(f"{note_path} :: {gate_path}" for note_path, gate_path in sorted(missing))
            )
        if extra:
            parts.append(
                "unexpected pairs: "
                + ", ".join(f"{note_path} :: {gate_path}" for note_path, gate_path in sorted(extra))
            )
        raise ValueError("; ".join(parts))

    finished_at = completed_at or iso_now()
    review_db.attach_execution_data(
        conn,
        review_job_id=review_job_id,
        runner=runner,
        telemetry_json=telemetry_json,
        runner_model=runner_model,
        runner_effort=runner_effort,
    )
    review_db.complete_review_pairs(
        conn,
        review_job_id=review_job_id,
        review_pairs=review_pairs or (),
        reviewed_at=finished_at,
    )

    finalized_pairs = review_db.load_review_pairs_for_job(conn, review_job_id=review_job_id)
    failure_reason = _job_coverage_failure(finalized_pairs)
    if failure_reason is not None:
        raise ValueError(failure_reason)
    for pair in finalized_pairs:
        review_db.append_acceptance_event(
            conn,
            note_path=pair.note_path,
            gate_path=pair.gate_path,
            model_partition=review_job.model_partition,
            accepted_review_pair_id=pair.review_pair_id,
            accepted_note_snapshot_id=pair.reviewed_note_snapshot_id,
            accepted_gate_snapshot_id=pair.reviewed_gate_snapshot_id,
            accepted_at=finished_at,
        )

    review_db.complete_review_job(conn, review_job_id=review_job_id, completed_at=finished_at)
    return len(finalized_pairs)


def complete_pairs_and_finalize_job(
    conn: sqlite3.Connection,
    *,
    review_job_id: int,
    review_pairs: Sequence[ReviewPairCompletion],
    completed_at: str | None = None,
    telemetry_json: str | None = None,
    runner: str | None = None,
    runner_model: str | None = None,
    runner_effort: str | None = None,
) -> int:
    return record_and_finalize_job(
        conn,
        review_job_id=review_job_id,
        review_pairs=review_pairs,
        completed_at=completed_at,
        telemetry_json=telemetry_json,
        runner=runner,
        runner_model=runner_model,
        runner_effort=runner_effort,
    )


# Failure marking.


def fail_active_review_jobs(
    *,
    db_path: Path,
    review_job_ids: list[int],
    failure_reason: str,
    telemetry_json: str | None = None,
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
            review_db.attach_execution_data(
                conn,
                review_job_id=int(row["review_job_id"]),
                telemetry_json=telemetry_json,
            )
            review_db.fail_review_job(
                conn,
                review_job_id=int(row["review_job_id"]),
                failure_reason=failure_reason,
                completed_at=completed_at,
            )
        conn.commit()


def fail_job_for_bundle_parse_error(
    conn: sqlite3.Connection,
    *,
    review_job_id: int,
    failure_reason: str,
    telemetry_json: str | None = None,
    runner: str | None = None,
    runner_model: str | None = None,
    runner_effort: str | None = None,
) -> None:
    review_db.attach_execution_data(
        conn,
        review_job_id=review_job_id,
        runner=runner,
        telemetry_json=telemetry_json,
        runner_model=runner_model,
        runner_effort=runner_effort,
    )
    review_db.fail_review_job(
        conn,
        review_job_id=review_job_id,
        failure_reason=failure_reason,
        completed_at=iso_now(),
        telemetry_json=telemetry_json,
    )


# Artifact writes and manifest refresh.


def write_job_manifest_from_db(
    conn: sqlite3.Connection,
    *,
    repo_root: Path,
    review_job_id: int,
) -> None:
    plan = review_db.load_review_job_plan(conn, review_job_id=review_job_id, require_paths=True)
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


def write_finalized_job_result_artifacts(
    conn: sqlite3.Connection,
    *,
    repo_root: Path,
    review_job_id: int,
    parsed: ParsedPairBundle,
) -> None:
    plan = review_db.load_review_job_plan(conn, review_job_id=review_job_id, require_paths=True)
    if plan is None:
        return
    write_pair_result_files_to_derived_paths(
        repo_root=repo_root,
        job=plan,
        pairs=plan.pairs,
        canonical_texts=parsed.canonical_texts,
    )


# Bundle parsing call and finalization orchestration.


def finalize_job_from_pairs(
    conn: sqlite3.Connection,
    *,
    review_job_id: int,
    pairs: tuple[tuple[str, str], ...],
    parsed: ParsedPairBundle,
    telemetry_json: str | None = None,
    runner: str | None = None,
    runner_model: str | None = None,
    runner_effort: str | None = None,
) -> int:
    review_pairs = tuple(
        ReviewPairCompletion(
            note_path=note_path,
            gate_path=gate_path,
            decision=parsed.reviews[(note_path, gate_path)].decision,
        )
        for note_path, gate_path in pairs
    )
    return record_and_finalize_job(
        conn,
        review_job_id=review_job_id,
        review_pairs=review_pairs,
        telemetry_json=telemetry_json,
        runner=runner,
        runner_model=runner_model,
        runner_effort=runner_effort,
    )


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


def _prevalidate_result_paths(repo_root: Path, plan: review_db.ReviewJobPlan) -> None:
    result_paths = result_paths_by_pair_id(
        review_job_id=plan.review_job_id,
        packing=plan.packing,
        pairs=plan.pairs,
    )
    for path in result_paths.values():
        repo_relative_path(repo_root, path, label="result_path")


def _fail_review_job_transaction(
    *,
    db_path: Path,
    review_job_id: int,
    failure_reason: str,
    telemetry_json: str | None = None,
    runner: str | None = None,
    runner_model: str | None = None,
    runner_effort: str | None = None,
) -> None:
    with review_db.connect(db_path) as conn:
        fail_job_for_bundle_parse_error(
            conn,
            review_job_id=review_job_id,
            failure_reason=failure_reason,
            telemetry_json=telemetry_json,
            runner=runner,
            runner_model=runner_model,
            runner_effort=runner_effort,
        )
        conn.commit()


def _refresh_manifest_warning(*, repo_root: Path, db_path: Path, review_job_id: int) -> tuple[str, ...]:
    try:
        with review_db.connect(db_path) as conn:
            write_job_manifest_from_db(conn, repo_root=repo_root, review_job_id=review_job_id)
    except (OSError, ValueError) as exc:
        return (f"manifest refresh failed: {exc}",)
    return ()


def finalize_job_from_parsed(
    *,
    repo_root: Path,
    db_path: Path,
    review_job_id: int,
    expected_pairs: tuple[tuple[str, str], ...],
    parsed: ParsedPairBundle,
    telemetry_json: str | None = None,
    runner: str | None = None,
    runner_model: str | None = None,
    runner_effort: str | None = None,
) -> tuple[bool, str | None, tuple[str, ...]]:
    try:
        review_pairs = _review_pair_completions(expected_pairs=expected_pairs, parsed=parsed)
        with review_db.connect(db_path) as conn:
            plan = review_db.load_review_job_plan(conn, review_job_id=review_job_id, require_paths=True)
            if plan is None:
                raise ValueError(f"review job not found: {review_job_id}")
            _prevalidate_result_paths(repo_root, plan)
    except ValueError as exc:
        failure_reason = str(exc)
        _fail_review_job_transaction(
            db_path=db_path,
            review_job_id=review_job_id,
            failure_reason=failure_reason,
            telemetry_json=telemetry_json,
            runner=runner,
            runner_model=runner_model,
            runner_effort=runner_effort,
        )
        warnings = _refresh_manifest_warning(repo_root=repo_root, db_path=db_path, review_job_id=review_job_id)
        return False, failure_reason, warnings

    with review_db.connect(db_path) as conn:
        try:
            record_and_finalize_job(
                conn,
                review_job_id=review_job_id,
                review_pairs=review_pairs,
                telemetry_json=telemetry_json,
                runner=runner,
                runner_model=runner_model,
                runner_effort=runner_effort,
            )
            write_finalized_job_result_artifacts(
                conn,
                repo_root=repo_root,
                review_job_id=review_job_id,
                parsed=parsed,
            )
        except (OSError, sqlite3.IntegrityError, ValueError) as exc:
            conn.rollback()
            failure_reason = str(exc)
            _fail_review_job_transaction(
                db_path=db_path,
                review_job_id=review_job_id,
                failure_reason=failure_reason,
                telemetry_json=telemetry_json,
                runner=runner,
                runner_model=runner_model,
                runner_effort=runner_effort,
            )
            warnings = _refresh_manifest_warning(repo_root=repo_root, db_path=db_path, review_job_id=review_job_id)
            return False, failure_reason, warnings
        conn.commit()
    warnings = _refresh_manifest_warning(repo_root=repo_root, db_path=db_path, review_job_id=review_job_id)
    return True, None, warnings


def finalize_job_bundle_markdown(
    *,
    repo_root: Path,
    db_path: Path,
    review_job_id: int,
    expected_pairs: tuple[tuple[str, str], ...],
    bundle_markdown: str,
    telemetry_json: str | None = None,
    runner: str | None = None,
    runner_model: str | None = None,
    runner_effort: str | None = None,
) -> tuple[bool, str | None, tuple[str, ...]]:
    try:
        parsed = parse_pair_bundle(bundle_markdown, expected_pairs=expected_pairs)
    except ValueError as exc:
        reason = str(exc)
        _fail_review_job_transaction(
            db_path=db_path,
            review_job_id=review_job_id,
            failure_reason=reason,
            telemetry_json=telemetry_json,
            runner=runner,
            runner_model=runner_model,
            runner_effort=runner_effort,
        )
        warnings = _refresh_manifest_warning(repo_root=repo_root, db_path=db_path, review_job_id=review_job_id)
        return False, reason, warnings

    return finalize_job_from_parsed(
        repo_root=repo_root,
        db_path=db_path,
        review_job_id=review_job_id,
        expected_pairs=expected_pairs,
        parsed=parsed,
        telemetry_json=telemetry_json,
        runner=runner,
        runner_model=runner_model,
        runner_effort=runner_effort,
    )
