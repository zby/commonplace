from __future__ import annotations

import sqlite3

from commonplace.review import review_db


def source_gate_path(gate: str) -> str:
    normalized = gate.strip().removesuffix(".md")
    if normalized.startswith("kb/"):
        return gate.strip()
    return f"kb/instructions/review-gates/{normalized}.md"


def insert_completed_pair(
    conn: sqlite3.Connection,
    *,
    note_path: str,
    gate_id: str,
    model_partition: str,
    decision: str,
    reviewed_at: str,
    runner: str = "test-runner",
    reviewed_note_snapshot_id: int | None = None,
    reviewed_gate_snapshot_id: int | None = None,
) -> int:
    gate_path = source_gate_path(gate_id)
    review_job_id = review_db.create_job_with_pairs(
        conn,
        model_partition=model_partition,
        runner=runner,
        created_at=reviewed_at,
        status="queued",
        packing="note",
        pairs=[
            review_db.ReviewPairRequest(
                note_path=note_path,
                gate_path=gate_path,
                pair_ordinal=0,
                reviewed_note_snapshot_id=reviewed_note_snapshot_id,
                reviewed_gate_snapshot_id=reviewed_gate_snapshot_id,
            )
        ],
    )
    pair = review_db.ReviewPairCompletion(
        note_path=note_path,
        gate_path=gate_path,
        decision=decision,
        reviewed_at=reviewed_at,
    )
    review_db.complete_review_pairs(conn, review_job_id=review_job_id, review_pairs=[pair], reviewed_at=reviewed_at)
    review_db.complete_review_job(conn, review_job_id=review_job_id, completed_at=reviewed_at)
    review_pair = review_db.load_review_pairs_for_job(conn, review_job_id=review_job_id)[0]
    return review_pair.review_pair_id


def accept_pair(
    conn: sqlite3.Connection,
    *,
    review_pair_id: int,
    note_path: str,
    gate_id: str,
    model_partition: str,
    accepted_at: str,
    accepted_note_snapshot_id: int | None = None,
    accepted_gate_snapshot_id: int | None = None,
) -> int:
    return review_db.append_acceptance_event(
        conn,
        note_path=note_path,
        gate_path=source_gate_path(gate_id),
        model_partition=model_partition,
        accepted_review_pair_id=review_pair_id,
        accepted_note_snapshot_id=accepted_note_snapshot_id,
        accepted_gate_snapshot_id=accepted_gate_snapshot_id,
        accepted_at=accepted_at,
    )
