"""Store integrity checks for freshness baselines."""

from __future__ import annotations

import sqlite3

from commonplace.lib.hashing import content_sha256_for_text


def assert_snapshot_hash_integrity(conn: sqlite3.Connection) -> None:
    rows = conn.execute(
        """
        SELECT snapshot_id, content_sha256, content_text
        FROM artifact_snapshots
        """
    ).fetchall()
    for row in rows:
        if row["content_text"] is None:
            raise RuntimeError(f"artifact snapshot missing text: snapshot_id={row['snapshot_id']}")
        actual = content_sha256_for_text(row["content_text"])
        if actual != row["content_sha256"]:
            raise RuntimeError(f"artifact snapshot hash mismatch: snapshot_id={row['snapshot_id']}")


def assert_queued_pair_cas_integrity(conn: sqlite3.Connection) -> None:
    row = conn.execute(
        """
        SELECT rp.review_pair_id
        FROM review_pairs AS rp
        JOIN review_jobs AS j
          ON j.review_job_id = rp.review_job_id
        WHERE j.status = 'queued'
          AND rp.completed_at IS NULL
          AND NOT (
              (
                  rp.expected_baseline_revision IS NOT NULL
                  AND rp.expected_generation_next_revision IS NULL
              )
              OR (
                  rp.expected_baseline_revision IS NULL
                  AND rp.expected_generation_next_revision IS NOT NULL
              )
          )
        LIMIT 1
        """
    ).fetchone()
    if row is not None:
        raise RuntimeError(
            f"queued pair must populate exactly one CAS field: review_pair_id={row['review_pair_id']}"
        )


def assert_review_freshness_integrity(conn: sqlite3.Connection) -> None:
    assert_snapshot_hash_integrity(conn)
    assert_queued_pair_cas_integrity(conn)
    row = conn.execute(
        """
        SELECT b.target_id
        FROM freshness_baselines AS b
        LEFT JOIN review_freshness_evidence AS e
          ON e.target_id = b.target_id
        LEFT JOIN review_pairs AS rp
          ON rp.review_pair_id = e.evidence_review_pair_id
        LEFT JOIN review_jobs AS j
          ON j.review_job_id = rp.review_job_id
        WHERE b.target_kind = 'review-pair'
          AND (
              e.target_id IS NULL
              OR rp.review_pair_id IS NULL
              OR rp.completed_at IS NULL
              OR (rp.result_kind = 'verdict' AND rp.outcome IS NULL)
              OR (rp.result_kind = 'report' AND rp.outcome IS NOT NULL)
              OR j.review_job_id IS NULL
              OR j.status != 'completed'
              OR j.model_partition != json_extract(b.target_key_json, '$.model_partition')
              OR rp.note_path != json_extract(b.target_key_json, '$.note_path')
              OR rp.criterion_path != json_extract(b.target_key_json, '$.criterion_path')
          )
        LIMIT 1
        """
    ).fetchone()
    if row is not None:
        raise RuntimeError(f"malformed review-pair freshness baseline: target_id={row['target_id']}")

    row = conn.execute(
        """
        SELECT b.target_id
        FROM freshness_baselines AS b
        WHERE b.target_kind = 'review-pair'
          AND (
              SELECT count(*)
              FROM freshness_inputs AS i
              WHERE i.target_id = b.target_id
          ) != 2
        LIMIT 1
        """
    ).fetchone()
    if row is not None:
        raise RuntimeError(f"review-pair baseline missing inputs: target_id={row['target_id']}")

    row = conn.execute(
        """
        SELECT i.target_id
        FROM freshness_inputs AS i
        JOIN freshness_baselines AS b
          ON b.target_id = i.target_id
        LEFT JOIN artifact_snapshots AS s
          ON s.snapshot_id = i.accepted_snapshot_id
         AND s.artifact_path = i.artifact_path
         AND s.version_kind = i.version_kind
        WHERE b.target_kind = 'review-pair'
          AND (
              s.snapshot_id IS NULL
              OR s.content_text IS NULL
              OR (
                  i.input_role = 'note'
                  AND i.artifact_path != json_extract(b.target_key_json, '$.note_path')
              )
              OR (
                  i.input_role = 'criterion'
                  AND i.artifact_path != json_extract(b.target_key_json, '$.criterion_path')
              )
          )
        LIMIT 1
        """
    ).fetchone()
    if row is not None:
        raise RuntimeError(f"review-pair baseline input mismatch: target_id={row['target_id']}")