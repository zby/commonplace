"""Freshness baseline read/write for review-pair targets."""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass

from commonplace.freshness.keys import review_pair_target_key
from commonplace.review.review_model import normalize_model_partition

REVIEW_PAIR_KIND = "review-pair"


@dataclass(frozen=True)
class TargetRow:
    target_id: int
    revision: int
    accepted_at: str


def load_review_target(
    conn: sqlite3.Connection,
    *,
    note_path: str,
    criterion_path: str,
    model_partition: str,
) -> TargetRow | None:
    model_partition = normalize_model_partition(model_partition)
    target_key_json = review_pair_target_key(
        note_path=note_path,
        criterion_path=criterion_path,
        model_partition=model_partition,
    )
    row = conn.execute(
        """
        SELECT target_id, revision, accepted_at
        FROM freshness_baselines
        WHERE target_kind = ?
          AND target_key_json = ?
        """,
        (REVIEW_PAIR_KIND, target_key_json),
    ).fetchone()
    if row is None:
        return None
    return TargetRow(
        target_id=int(row["target_id"]),
        revision=int(row["revision"]),
        accepted_at=row["accepted_at"],
    )


def load_expected_baseline_revision(
    conn: sqlite3.Connection,
    *,
    note_path: str,
    criterion_path: str,
    model_partition: str,
) -> int | None:
    target = load_review_target(
        conn,
        note_path=note_path,
        criterion_path=criterion_path,
        model_partition=model_partition,
    )
    if target is None:
        return None
    return target.revision


def _assert_capture_revision(
    conn: sqlite3.Connection,
    *,
    note_path: str,
    criterion_path: str,
    model_partition: str,
    expected_baseline_revision: int | None,
) -> TargetRow | None:
    current = load_review_target(
        conn,
        note_path=note_path,
        criterion_path=criterion_path,
        model_partition=model_partition,
    )
    if expected_baseline_revision is None:
        if current is not None:
            raise ValueError("stale-baseline-revision: baseline already exists")
        return None
    if current is None:
        raise ValueError("stale-baseline-revision: expected baseline but none registered")
    if current.revision != expected_baseline_revision:
        raise ValueError(
            f"stale-baseline-revision: expected {expected_baseline_revision}, "
            f"current {current.revision}"
        )
    return current


def refresh_review_baseline_from_captures(
    conn: sqlite3.Connection,
    *,
    note_path: str,
    criterion_path: str,
    model_partition: str,
    evidence_review_pair_id: int,
    baseline_note_snapshot_id: int,
    baseline_criterion_snapshot_id: int,
    expected_baseline_revision: int | None,
    accepted_at: str,
) -> tuple[int | None, int | None]:
    """Return (superseded_evidence_pair_id, superseded_target_id) or Nones."""
    previous = _assert_capture_revision(
        conn,
        note_path=note_path,
        criterion_path=criterion_path,
        model_partition=model_partition,
        expected_baseline_revision=expected_baseline_revision,
    )
    superseded_evidence_pair_id: int | None = None
    superseded_target_id: int | None = None
    if previous is not None:
        evidence_row = conn.execute(
            """
            SELECT evidence_review_pair_id
            FROM review_freshness_evidence
            WHERE target_id = ?
            """,
            (previous.target_id,),
        ).fetchone()
        if evidence_row is not None:
            superseded_evidence_pair_id = int(evidence_row["evidence_review_pair_id"])
        superseded_target_id = previous.target_id

    target_key_json = review_pair_target_key(
        note_path=note_path,
        criterion_path=criterion_path,
        model_partition=model_partition,
    )
    if previous is None:
        cursor = conn.execute(
            """
            INSERT INTO freshness_baselines (
                target_kind, target_key_json, revision, accepted_at
            ) VALUES (?, ?, 1, ?)
            """,
            (REVIEW_PAIR_KIND, target_key_json, accepted_at),
        )
        target_id = int(cursor.lastrowid)
        revision = 1
    else:
        target_id = previous.target_id
        revision = previous.revision + 1
        conn.execute(
            """
            UPDATE freshness_baselines
            SET revision = ?, accepted_at = ?
            WHERE target_id = ?
            """,
            (revision, accepted_at, target_id),
        )
        conn.execute(
            "DELETE FROM freshness_inputs WHERE target_id = ?",
            (target_id,),
        )

    for role, snapshot_id, artifact_path in (
        ("note", baseline_note_snapshot_id, note_path),
        ("criterion", baseline_criterion_snapshot_id, criterion_path),
    ):
        conn.execute(
            """
            INSERT INTO freshness_inputs (
                target_id, input_role, artifact_path, version_kind, accepted_snapshot_id
            ) VALUES (?, ?, ?, 'file-text', ?)
            """,
            (target_id, role, artifact_path, snapshot_id),
        )

    conn.execute(
        "DELETE FROM review_freshness_evidence WHERE target_id = ?",
        (target_id,),
    )
    conn.execute(
        """
        INSERT INTO review_freshness_evidence (target_id, evidence_review_pair_id)
        VALUES (?, ?)
        """,
        (target_id, evidence_review_pair_id),
    )
    return superseded_evidence_pair_id, superseded_target_id


def refresh_review_baseline_from_observation(
    conn: sqlite3.Connection,
    *,
    note_path: str,
    criterion_path: str,
    model_partition: str,
    evidence_review_pair_id: int,
    baseline_note_snapshot_id: int,
    baseline_criterion_snapshot_id: int,
    accepted_at: str,
) -> int | None:
    """Ack-style refresh: CAS on current revision, preserve evidence pair id."""
    current = load_review_target(
        conn,
        note_path=note_path,
        criterion_path=criterion_path,
        model_partition=model_partition,
    )
    if current is None:
        raise ValueError("no freshness baseline to acknowledge")
    superseded_evidence_pair_id, _ = refresh_review_baseline_from_captures(
        conn,
        note_path=note_path,
        criterion_path=criterion_path,
        model_partition=model_partition,
        evidence_review_pair_id=evidence_review_pair_id,
        baseline_note_snapshot_id=baseline_note_snapshot_id,
        baseline_criterion_snapshot_id=baseline_criterion_snapshot_id,
        expected_baseline_revision=current.revision,
        accepted_at=accepted_at,
    )
    return superseded_evidence_pair_id