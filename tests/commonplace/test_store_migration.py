from __future__ import annotations

from pathlib import Path

from commonplace.review.review_db import connect, ensure_db
from commonplace.store import STORE_SCHEMA_VERSION


def _downgrade_store_to_v2(db_path: Path) -> None:
    with connect(db_path) as conn:
        conn.execute("ALTER TABLE review_pairs DROP COLUMN expected_generation_next_revision")
        conn.execute(f"PRAGMA user_version = {STORE_SCHEMA_VERSION - 1}")
        conn.commit()


def _insert_unguarded_queued_job(conn) -> int:
    cursor = conn.execute(
        """
        INSERT INTO review_jobs (
            model_partition, created_at, status, grouping
        ) VALUES ('codex', '2026-07-13T00:00:00+00:00', 'queued', 'note')
        """
    )
    job_id = int(cursor.lastrowid)
    conn.execute(
        """
        INSERT INTO review_pairs (
            review_job_id,
            note_path,
            criterion_path,
            pair_ordinal,
            result_kind,
            expected_baseline_revision
        ) VALUES (?, 'kb/notes/example.md', 'kb/instructions/gate.md', 1, 'verdict', NULL)
        """,
        (job_id,),
    )
    return job_id


def _insert_guarded_queued_job(conn, *, expected_baseline_revision: int) -> int:
    cursor = conn.execute(
        """
        INSERT INTO review_jobs (
            model_partition, created_at, status, grouping
        ) VALUES ('codex', '2026-07-13T00:00:00+00:00', 'queued', 'note')
        """
    )
    job_id = int(cursor.lastrowid)
    conn.execute(
        """
        INSERT INTO review_pairs (
            review_job_id,
            note_path,
            criterion_path,
            pair_ordinal,
            result_kind,
            expected_baseline_revision
        ) VALUES (?, 'kb/notes/example.md', 'kb/instructions/gate.md', 1, 'verdict', ?)
        """,
        (job_id, expected_baseline_revision),
    )
    return job_id


def test_v2_to_v3_migration_fails_unguarded_queued_jobs(tmp_path: Path) -> None:
    db_path = tmp_path / "store.sqlite"
    ensure_db(db_path)
    _downgrade_store_to_v2(db_path)

    with connect(db_path) as conn:
        job_id = _insert_unguarded_queued_job(conn)
        conn.commit()

    ensure_db(db_path)

    with connect(db_path) as conn:
        version = conn.execute("PRAGMA user_version").fetchone()[0]
        assert version == STORE_SCHEMA_VERSION
        job = conn.execute(
            "SELECT status, failure_reason FROM review_jobs WHERE review_job_id = ?",
            (job_id,),
        ).fetchone()
        pair = conn.execute(
            """
            SELECT expected_baseline_revision, expected_generation_next_revision
            FROM review_pairs
            WHERE review_job_id = ?
            """,
            (job_id,),
        ).fetchone()
        assert job["status"] == "failed"
        assert job["failure_reason"] == "unguarded-queued-cas"
        assert pair["expected_baseline_revision"] is None
        assert pair["expected_generation_next_revision"] is None


def test_v2_to_v3_migration_preserves_guarded_queued_jobs(tmp_path: Path) -> None:
    db_path = tmp_path / "store.sqlite"
    ensure_db(db_path)
    _downgrade_store_to_v2(db_path)

    with connect(db_path) as conn:
        job_id = _insert_guarded_queued_job(conn, expected_baseline_revision=2)
        conn.commit()

    ensure_db(db_path)

    with connect(db_path) as conn:
        job = conn.execute(
            "SELECT status, failure_reason FROM review_jobs WHERE review_job_id = ?",
            (job_id,),
        ).fetchone()
        pair = conn.execute(
            """
            SELECT expected_baseline_revision, expected_generation_next_revision
            FROM review_pairs
            WHERE review_job_id = ?
            """,
            (job_id,),
        ).fetchone()
        assert job["status"] == "queued"
        assert job["failure_reason"] is None
        assert pair["expected_baseline_revision"] == 2
        assert pair["expected_generation_next_revision"] is None