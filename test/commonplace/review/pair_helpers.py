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
    rationale_markdown: str,
    reviewed_at: str,
    runner: str = "test-runner",
    reviewed_note_snapshot_id: int | None = None,
    reviewed_gate_snapshot_id: int | None = None,
    started_at: str | None = None,
    review_kind: str = "full-review",
) -> int:
    started = started_at or reviewed_at
    gate_path = source_gate_path(gate_id)
    review_run_id = review_db.create_run_with_pairs(
        conn,
        model_partition=model_partition,
        runner=runner,
        started_at=started,
        packing="note",
        pairs=[
            review_db.ReviewPairRequest(
                note_path=note_path,
                gate_path=gate_path,
                pair_ordinal=0,
                reviewed_note_snapshot_id=reviewed_note_snapshot_id,
                reviewed_gate_snapshot_id=reviewed_gate_snapshot_id,
                review_kind=review_kind,
            )
        ],
    )
    pair = review_db.PendingReviewPair(
        note_path=note_path,
        gate_path=gate_path,
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
    model_partition: str,
    accepted_at: str,
    accepted_note_snapshot_id: int | None = None,
    accepted_gate_snapshot_id: int | None = None,
    acceptance_kind: str = "full-review",
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
        acceptance_kind=acceptance_kind,
    )
