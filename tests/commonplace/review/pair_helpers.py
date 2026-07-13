from __future__ import annotations

import sqlite3
from hashlib import sha256

from commonplace.review import review_db


def source_criterion_path(gate: str) -> str:
    normalized = gate.strip().removesuffix(".md")
    if normalized.startswith("kb/"):
        return gate.strip()
    return f"kb/instructions/review-gates/{normalized}.md"


def insert_completed_pair(
    conn: sqlite3.Connection,
    *,
    note_path: str,
    criterion_id: str,
    model_partition: str,
    outcome: str,
    completed_at: str,
    runner: str = "test-runner",
    reviewed_note_snapshot_id: int | None = None,
    reviewed_criterion_snapshot_id: int | None = None,
) -> int:
    criterion_path = source_criterion_path(criterion_id)
    review_job_id = review_db.create_job_with_pairs(
        conn,
        model_partition=model_partition,
        runner=runner,
        created_at=completed_at,
        status="queued",
        grouping="note",
        pairs=[
            review_db.ReviewPairRequest(
                note_path=note_path,
                criterion_path=criterion_path,
                pair_ordinal=1,
                result_kind="verdict",
                reviewed_note_snapshot_id=reviewed_note_snapshot_id,
                reviewed_criterion_snapshot_id=reviewed_criterion_snapshot_id,
            )
        ],
    )
    pair = review_db.ReviewPairCompletion(
        note_path=note_path,
        criterion_path=criterion_path,
        outcome=outcome,
        completed_at=completed_at,
    )
    review_db.complete_review_pairs(conn, review_job_id=review_job_id, review_pairs=[pair], completed_at=completed_at)
    review_db.complete_review_job(conn, review_job_id=review_job_id, completed_at=completed_at)
    review_pair = review_db.load_review_pairs_for_job(conn, review_job_id=review_job_id)[0]
    return review_pair.review_pair_id


def accept_pair(
    conn: sqlite3.Connection,
    *,
    review_pair_id: int,
    note_path: str,
    criterion_id: str,
    model_partition: str,
    baseline_updated_at: str,
    baseline_note_snapshot_id: int | None = None,
    baseline_criterion_snapshot_id: int | None = None,
) -> review_db.SupersededFreshnessBaseline | None:
    criterion_path = source_criterion_path(criterion_id)
    if baseline_note_snapshot_id is None:
        baseline_note_snapshot_id = _synthetic_snapshot(
            conn,
            path=note_path,
            captured_at=baseline_updated_at,
        )
    if baseline_criterion_snapshot_id is None:
        baseline_criterion_snapshot_id = _synthetic_snapshot(
            conn,
            path=criterion_path,
            captured_at=baseline_updated_at,
        )
    from commonplace.freshness import baselines as freshness_baselines

    return review_db.upsert_freshness_baseline(
        conn,
        note_path=note_path,
        criterion_path=criterion_path,
        model_partition=model_partition,
        evidence_review_pair_id=review_pair_id,
        baseline_note_snapshot_id=baseline_note_snapshot_id,
        baseline_criterion_snapshot_id=baseline_criterion_snapshot_id,
        baseline_updated_at=baseline_updated_at,
        expected_baseline_revision=freshness_baselines.load_expected_baseline_revision(
            conn,
            note_path=note_path,
            criterion_path=criterion_path,
            model_partition=model_partition,
        ),
        capture_refresh=True,
    )


def _synthetic_snapshot(conn: sqlite3.Connection, *, path: str, captured_at: str) -> int:
    content_text = f"synthetic snapshot for {path}\n"
    content_hash = sha256(content_text.encode("utf-8")).hexdigest()
    conn.execute(
        """
        INSERT OR IGNORE INTO artifact_snapshots (
            artifact_path, version_kind, content_sha256, content_text, captured_at
        ) VALUES (?, 'file-text', ?, ?, ?)
        """,
        (path, content_hash, content_text, captured_at),
    )
    row = conn.execute(
        """
        SELECT snapshot_id FROM artifact_snapshots
        WHERE artifact_path = ? AND version_kind = 'file-text' AND content_sha256 = ?
        """,
        (path, content_hash),
    ).fetchone()
    assert row is not None
    return int(row["snapshot_id"])
