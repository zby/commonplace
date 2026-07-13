from __future__ import annotations

from pathlib import Path

import pytest

from commonplace.freshness.integrity import assert_queued_pair_cas_integrity
from commonplace.review.review_db import connect, ensure_db, snapshot_file
from commonplace.store import assert_store_integrity


def test_empty_file_snapshot_passes_integrity(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    empty = repo / "kb/notes/empty.md"
    empty.parent.mkdir(parents=True)
    empty.write_text("", encoding="utf-8")
    db_path = tmp_path / "store.sqlite"
    ensure_db(db_path)

    with connect(db_path) as conn:
        snapshot_file(conn, repo_root=repo, path="kb/notes/empty.md")
        conn.commit()

    with connect(db_path) as conn:
        assert_store_integrity(conn)


def test_healthcheck_rejects_unguarded_queued_pair(tmp_path: Path) -> None:
    db_path = tmp_path / "store.sqlite"
    ensure_db(db_path)
    with connect(db_path) as conn:
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
                expected_baseline_revision,
                expected_generation_next_revision
            ) VALUES (?, 'kb/notes/example.md', 'kb/instructions/gate.md', 1, 'verdict', NULL, NULL)
            """,
            (job_id,),
        )
        conn.commit()

    with connect(db_path) as conn:
        with pytest.raises(RuntimeError, match="exactly one CAS field"):
            assert_queued_pair_cas_integrity(conn)


def test_healthcheck_rejects_dual_populated_queued_pair(tmp_path: Path) -> None:
    db_path = tmp_path / "store.sqlite"
    ensure_db(db_path)
    with connect(db_path) as conn:
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
                expected_baseline_revision,
                expected_generation_next_revision
            ) VALUES (?, 'kb/notes/example.md', 'kb/instructions/gate.md', 1, 'verdict', 1, 2)
            """,
            (job_id,),
        )
        conn.commit()

    with connect(db_path) as conn:
        with pytest.raises(RuntimeError, match="exactly one CAS field"):
            assert_queued_pair_cas_integrity(conn)