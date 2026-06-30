"""Finalize review jobs and advance acceptance state."""

from __future__ import annotations

import sqlite3
from typing import Sequence

from commonplace.review import review_db
from commonplace.review.review_db import ReviewPairCompletion, ReviewPairRow
from commonplace.review.clock import iso_now


def _job_coverage_failure(pairs: Sequence[ReviewPairRow]) -> str | None:
    if not pairs:
        return "review job has no pairs"
    missing = [
        f"{pair.note_path} :: {pair.gate_path}"
        for pair in pairs
        if pair.pair_status != "completed"
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
) -> int:
    review_job = review_db.load_review_job(conn, review_job_id=review_job_id)
    if review_job is None:
        raise ValueError(f"review job not found: {review_job_id}")
    if review_job.status not in {"queued", "running"}:
        raise ValueError(f"review job is not finalizable: {review_job.status}")

    finished_at = completed_at or iso_now()
    try:
        review_db.attach_execution_data(
            conn,
            review_job_id=review_job_id,
            telemetry_json=telemetry_json,
        )

        if review_pairs is not None:
            review_db.complete_review_pairs(
                conn,
                review_job_id=review_job_id,
                review_pairs=review_pairs,
                reviewed_at=finished_at,
            )

        finalized_pairs = review_db.load_review_pairs_for_job(conn, review_job_id=review_job_id)
        completed_pairs = [pair for pair in finalized_pairs if pair.pair_status == "completed"]
        for pair in completed_pairs:
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

        failure_reason = _job_coverage_failure(finalized_pairs)
        if failure_reason is not None:
            review_db.mark_missing_pairs(conn, review_job_id=review_job_id)
            raise ValueError(failure_reason)

        review_db.complete_review_job(conn, review_job_id=review_job_id, completed_at=finished_at)
        return len(completed_pairs)
    except (sqlite3.IntegrityError, ValueError) as exc:
        review_db.fail_review_job(
            conn,
            review_job_id=review_job_id,
            failure_reason=str(exc),
            completed_at=finished_at,
        )
        raise ValueError(str(exc)) from exc


def complete_pairs_and_finalize_job(
    conn: sqlite3.Connection,
    *,
    review_job_id: int,
    review_pairs: Sequence[ReviewPairCompletion],
    completed_at: str | None = None,
    telemetry_json: str | None = None,
) -> int:
    return record_and_finalize_job(
        conn,
        review_job_id=review_job_id,
        review_pairs=review_pairs,
        completed_at=completed_at,
        telemetry_json=telemetry_json,
    )
