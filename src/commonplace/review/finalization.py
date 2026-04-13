"""Finalize review runs and advance acceptance state."""

from __future__ import annotations

import sqlite3
from typing import Sequence

from commonplace.review import review_db
from commonplace.review.review_db import GateReviewRow, PendingGateReview, ReviewRunGateRow
from commonplace.review.review_metadata import iso_now


def _review_run_coverage_failure(
    conn: sqlite3.Connection,
    *,
    review_run_id: int,
) -> tuple[str | None, list[ReviewRunGateRow], dict[str, GateReviewRow]]:
    run_gates = review_db.load_review_run_gates(conn, review_run_id=review_run_id)
    if not run_gates:
        return f"review run has no gates: {review_run_id}", [], {}

    gate_reviews = review_db.load_gate_reviews_for_run(conn, review_run_id=review_run_id)
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

        run_gates = {row.gate_id: row for row in review_db.load_review_run_gates(conn, review_run_id=review_run_id)}
        if gate_reviews is not None:
            for gate_review in gate_reviews:
                run_gate = run_gates.get(gate_review.gate_id)
                if run_gate is None:
                    raise ValueError(f"gate {gate_review.gate_id} is not part of review run {review_run_id}")
                review_db.insert_gate_review(
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
            review_db.rekey_review_run_model(conn, review_run_id=review_run_id, model_id=actual_model_id)
            final_model_id = actual_model_id

        failure_reason, finalized_run_gates, written_gate_map = _review_run_coverage_failure(
            conn,
            review_run_id=review_run_id,
        )
        if failure_reason is not None:
            raise ValueError(failure_reason)

        review_db.complete_review_run(conn, review_run_id=review_run_id, completed_at=finished_at)
        for run_gate in finalized_run_gates:
            gate_review = written_gate_map[run_gate.gate_id]
            review_db.append_acceptance_event(
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
        review_db.fail_review_run(
            conn,
            review_run_id=review_run_id,
            failure_reason=str(exc),
            completed_at=finished_at,
        )
        raise ValueError(str(exc)) from exc
