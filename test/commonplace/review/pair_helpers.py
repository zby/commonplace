from __future__ import annotations

import sqlite3

from commonplace.review import review_db


def insert_completed_pair(
    conn: sqlite3.Connection,
    *,
    note_path: str,
    gate_id: str,
    model_id: str,
    decision: str,
    rationale_markdown: str,
    gate_sha: str,
    reviewed_note_sha: str,
    reviewed_at: str,
    runner: str = "test-runner",
    reviewed_note_commit: str | None = None,
    started_at: str | None = None,
    review_kind: str = "full-review",
) -> int:
    started = started_at or reviewed_at
    review_run_id = review_db.create_run_with_pairs(
        conn,
        model_id=model_id,
        runner=runner,
        started_at=started,
        packing="note",
        pairs=[
            review_db.ReviewPairRequest(
                note_path=note_path,
                gate_id=gate_id,
                gate_sha=gate_sha,
                reviewed_note_sha=reviewed_note_sha,
                reviewed_note_commit=reviewed_note_commit,
                pair_ordinal=0,
                review_kind=review_kind,
            )
        ],
    )
    pair = review_db.PendingReviewPair(
        note_path=note_path,
        gate_id=gate_id,
        decision=decision,
        rationale_markdown=rationale_markdown,
        reviewed_at=reviewed_at,
        review_kind=review_kind,
    )
    review_db.complete_review_pairs(conn, review_run_id=review_run_id, review_pairs=[pair], reviewed_at=reviewed_at)
    review_pair = review_db.load_review_pairs_for_run(conn, review_run_id=review_run_id)[0]
    return review_pair.review_pair_id


def accept_pair(
    conn: sqlite3.Connection,
    *,
    review_pair_id: int | None,
    note_path: str,
    gate_id: str,
    model_id: str,
    accepted_note_sha: str,
    accepted_gate_sha: str,
    accepted_at: str,
    accepted_note_commit: str | None = None,
    acceptance_kind: str = "full-review",
) -> int:
    return review_db.append_acceptance_event(
        conn,
        note_path=note_path,
        gate_id=gate_id,
        model_id=model_id,
        accepted_review_pair_id=review_pair_id,
        accepted_note_sha=accepted_note_sha,
        accepted_note_commit=accepted_note_commit,
        accepted_gate_sha=accepted_gate_sha,
        accepted_at=accepted_at,
        acceptance_kind=acceptance_kind,
    )
