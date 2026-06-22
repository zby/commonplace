"""Finalize review runs and advance acceptance state."""

from __future__ import annotations

import sqlite3
from typing import Sequence

from commonplace.review import review_db
from commonplace.review.review_db import PendingReviewPair, ReviewPairRow
from commonplace.review.review_metadata import iso_now


def _run_coverage_failure(pairs: Sequence[ReviewPairRow]) -> str | None:
    if not pairs:
        return "review run has no pairs"
    missing = [
        f"{pair.note_path} :: {pair.gate_id}"
        for pair in pairs
        if pair.pair_status != "completed"
    ]
    if not missing:
        return None
    return f"missing pairs: {', '.join(sorted(missing))}"


def record_and_finalize_run(
    conn: sqlite3.Connection,
    *,
    review_run_id: int,
    review_pairs: Sequence[PendingReviewPair] | None = None,
    actual_model_id: str | None = None,
    completed_at: str | None = None,
    telemetry_json: str | None = None,
    raw_bundle_markdown: str | None = None,
    debug_log: str | None = None,
) -> int:
    review_run = review_db.load_review_run(conn, review_run_id=review_run_id)
    if review_run is None:
        raise ValueError(f"review run not found: {review_run_id}")
    if review_run.status != "running":
        raise ValueError(f"review run is not finalizable: {review_run.status}")

    finished_at = completed_at or iso_now()
    try:
        review_db.attach_execution_data(
            conn,
            review_run_id=review_run_id,
            telemetry_json=telemetry_json,
            raw_bundle_markdown=raw_bundle_markdown,
            debug_log=debug_log,
        )

        final_model_id = review_run.model_id
        if actual_model_id is not None and actual_model_id != review_run.model_id:
            review_db.rekey_review_run_model(conn, review_run_id=review_run_id, model_id=actual_model_id)
            final_model_id = actual_model_id

        if review_pairs is not None:
            review_db.complete_review_pairs(
                conn,
                review_run_id=review_run_id,
                review_pairs=review_pairs,
                reviewed_at=finished_at,
            )

        finalized_pairs = review_db.load_review_pairs_for_run(conn, review_run_id=review_run_id)
        completed_pairs = [pair for pair in finalized_pairs if pair.pair_status == "completed"]
        for pair in completed_pairs:
            review_db.append_acceptance_event(
                conn,
                note_path=pair.note_path,
                gate_id=pair.gate_id,
                model_id=final_model_id,
                accepted_review_pair_id=pair.review_pair_id,
                accepted_note_sha=pair.reviewed_note_sha,
                accepted_note_commit=pair.reviewed_note_commit,
                accepted_gate_sha=pair.gate_sha,
                accepted_at=finished_at,
                acceptance_kind="full-review",
            )

        failure_reason = _run_coverage_failure(finalized_pairs)
        if failure_reason is not None:
            review_db.mark_missing_pairs(conn, review_run_id=review_run_id)
            raise ValueError(failure_reason)

        review_db.complete_review_run(conn, review_run_id=review_run_id, completed_at=finished_at)
        return len(completed_pairs)
    except (sqlite3.IntegrityError, ValueError) as exc:
        review_db.fail_review_run(
            conn,
            review_run_id=review_run_id,
            failure_reason=str(exc),
            completed_at=finished_at,
        )
        raise ValueError(str(exc)) from exc


def complete_pairs_and_finalize_run(
    conn: sqlite3.Connection,
    *,
    review_run_id: int,
    review_pairs: Sequence[PendingReviewPair],
    actual_model_id: str | None = None,
    completed_at: str | None = None,
    telemetry_json: str | None = None,
    raw_bundle_markdown: str | None = None,
    debug_log: str | None = None,
) -> int:
    return record_and_finalize_run(
        conn,
        review_run_id=review_run_id,
        review_pairs=review_pairs,
        actual_model_id=actual_model_id,
        completed_at=completed_at,
        telemetry_json=telemetry_json,
        raw_bundle_markdown=raw_bundle_markdown,
        debug_log=debug_log,
    )
