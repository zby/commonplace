"""Behavioral coverage for review data persistence."""

from __future__ import annotations

import sqlite3
from hashlib import sha256
from pathlib import Path

import pytest

from commonplace.review import review_db
from tests.commonplace.review.pair_helpers import accept_pair, insert_completed_pair


def test_ensure_db_rejects_stale_review_store_shape(tmp_path: Path) -> None:
    db_path = tmp_path / "commonplace-store.sqlite"
    db_path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(db_path) as conn:
        conn.execute("CREATE TABLE review_jobs (review_job_id INTEGER PRIMARY KEY)")
        conn.commit()

    with pytest.raises(RuntimeError, match="does not match current version"):
        review_db.ensure_db(db_path)


def test_upsert_freshness_baseline_requires_review_pair(tmp_path: Path) -> None:
    db_path = tmp_path / "commonplace-store.sqlite"
    review_db.ensure_db(db_path)

    with review_db.connect(db_path) as conn:
        invalid_pair_id = None
        with pytest.raises(ValueError, match="evidence_review_pair_id is required"):
            review_db.upsert_freshness_baseline(
                conn,
                note_path="kb/notes/current.md",
                criterion_path="kb/instructions/review-gates/prose/current.md",
                model_partition="opus-4-6",
                evidence_review_pair_id=invalid_pair_id,
                baseline_note_snapshot_id=1,
                baseline_criterion_snapshot_id=2,
                baseline_updated_at="2026-04-10T10:02:00+02:00",
            )


def test_freshness_baseline_rejects_pair_from_incomplete_job(tmp_path: Path) -> None:
    db_path = tmp_path / "commonplace-store.sqlite"
    review_db.ensure_db(db_path)

    with review_db.connect(db_path) as conn:
        queued_job_id = review_db.create_job_with_pairs(
            conn,
            model_partition="opus-4-6",
            runner="test-runner",
            created_at="2026-04-10T10:03:00+02:00",
            status="queued",
            grouping="note",
            pairs=[
                review_db.ReviewPairRequest(
                    note_path="kb/notes/queued.md",
                    criterion_path="kb/instructions/review-gates/semantic/internal-consistency.md",
                    pair_ordinal=1,
                    result_kind="verdict",
                )
            ],
        )
        review_db.complete_review_pairs(
            conn,
            review_job_id=queued_job_id,
            review_pairs=[
                review_db.ReviewPairCompletion(
                    note_path="kb/notes/queued.md",
                    criterion_path="kb/instructions/review-gates/semantic/internal-consistency.md",
                    outcome="warn",
                    completed_at="2026-04-10T10:03:30+02:00",
                )
            ],
            completed_at="2026-04-10T10:03:30+02:00",
        )
        queued_pair_id = review_db.load_review_pairs_for_job(conn, review_job_id=queued_job_id)[0].review_pair_id
        with pytest.raises(ValueError, match="job is not completed"):
            accept_pair(
                conn,
                review_pair_id=queued_pair_id,
                note_path="kb/notes/queued.md",
                criterion_id="semantic/internal-consistency",
                model_partition="opus-4-6",
                baseline_updated_at="2026-04-10T10:04:00+02:00",
            )
        assert conn.execute("SELECT count(*) FROM freshness_baselines").fetchone()[0] == 0


def test_job_cannot_complete_until_every_pair_completes(tmp_path: Path) -> None:
    db_path = tmp_path / "commonplace-store.sqlite"
    review_db.ensure_db(db_path)

    with review_db.connect(db_path) as conn:
        review_job_id = review_db.create_job_with_pairs(
            conn,
            model_partition="test-model",
            runner=None,
            created_at="2026-04-10T10:03:00+02:00",
            status="queued",
            grouping="note",
            pairs=[
                review_db.ReviewPairRequest(
                    note_path="kb/notes/current.md",
                    criterion_path="kb/instructions/review-gates/prose/current.md",
                    pair_ordinal=1,
                    result_kind="verdict",
                )
            ],
        )

        with pytest.raises(ValueError, match="incomplete pairs"):
            review_db.complete_review_job(
                conn,
                review_job_id=review_job_id,
                completed_at="2026-04-10T10:04:00+02:00",
            )

        job = review_db.load_review_job(conn, review_job_id=review_job_id)
        assert job is not None
        assert job.status == "queued"


def test_snapshot_file_deduplicates_per_path_and_hashes_exact_utf8(tmp_path: Path) -> None:
    db_path = tmp_path / "commonplace-store.sqlite"
    repo = tmp_path / "repo"
    repo.mkdir()
    note = repo / "kb" / "notes" / "sample.md"
    gate = repo / "kb" / "instructions" / "review-gates" / "prose" / "sample.md"
    note.parent.mkdir(parents=True)
    gate.parent.mkdir(parents=True)
    note.write_text("title\n\ncafe\u0301\n", encoding="utf-8")
    gate.write_text("title\n\ncafe\u0301\n", encoding="utf-8")

    review_db.ensure_db(db_path)

    with review_db.connect(db_path) as conn:
        first = review_db.snapshot_file(conn, repo_root=repo, path="kb/notes/sample.md")
        second = review_db.snapshot_file(conn, repo_root=repo, path="kb/notes/sample.md")
        criterion_snapshot = review_db.snapshot_file(
            conn,
            repo_root=repo,
            path="kb/instructions/review-gates/prose/sample.md",
        )

    assert first.snapshot_id == second.snapshot_id
    assert first.path == "kb/notes/sample.md"
    assert first.content_text == "title\n\ncafe\u0301\n"
    assert first.content_sha256 == sha256("title\n\ncafe\u0301\n".encode("utf-8")).hexdigest()
    assert criterion_snapshot.snapshot_id != first.snapshot_id
    assert criterion_snapshot.content_sha256 == first.content_sha256


def test_prune_superseded_freshness_baselines_deletes_unreferenced_snapshots(tmp_path: Path) -> None:
    db_path = tmp_path / "commonplace-store.sqlite"
    repo = tmp_path / "repo"
    repo.mkdir()
    files = {
        "kb/notes/sample.md": "old note\n",
        "kb/instructions/review-gates/prose/sample.md": "old gate\n",
    }
    for rel_path, content in files.items():
        path = repo / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    review_db.ensure_db(db_path)

    with review_db.connect(db_path) as conn:
        old_note = review_db.snapshot_file(conn, repo_root=repo, path="kb/notes/sample.md")
        old_gate = review_db.snapshot_file(
            conn,
            repo_root=repo,
            path="kb/instructions/review-gates/prose/sample.md",
        )
        old_pair_id = insert_completed_pair(
            conn,
            note_path="kb/notes/sample.md",
            criterion_id="prose/sample",
            model_partition="opus-4-6",
            outcome="pass",
            completed_at="2026-04-10T10:01:00+02:00",
            reviewed_note_snapshot_id=old_note.snapshot_id,
            reviewed_criterion_snapshot_id=old_gate.snapshot_id,
        )
        accept_pair(
            conn,
            review_pair_id=old_pair_id,
            note_path="kb/notes/sample.md",
            criterion_id="prose/sample",
            model_partition="opus-4-6",
            baseline_updated_at="2026-04-10T10:02:00+02:00",
            baseline_note_snapshot_id=old_note.snapshot_id,
            baseline_criterion_snapshot_id=old_gate.snapshot_id,
        )

        (repo / "kb/notes/sample.md").write_text("current note\n", encoding="utf-8")
        (repo / "kb/instructions/review-gates/prose/sample.md").write_text("current gate\n", encoding="utf-8")
        current_note = review_db.snapshot_file(conn, repo_root=repo, path="kb/notes/sample.md")
        current_gate = review_db.snapshot_file(
            conn,
            repo_root=repo,
            path="kb/instructions/review-gates/prose/sample.md",
        )
        current_pair_id = insert_completed_pair(
            conn,
            note_path="kb/notes/sample.md",
            criterion_id="prose/sample",
            model_partition="opus-4-6",
            outcome="pass",
            completed_at="2026-04-10T10:03:00+02:00",
            reviewed_note_snapshot_id=current_note.snapshot_id,
            reviewed_criterion_snapshot_id=current_gate.snapshot_id,
        )
        old_job_id = conn.execute(
            "SELECT review_job_id FROM review_pairs WHERE review_pair_id = ?",
            (old_pair_id,),
        ).fetchone()["review_job_id"]
        superseded = accept_pair(
            conn,
            review_pair_id=current_pair_id,
            note_path="kb/notes/sample.md",
            criterion_id="prose/sample",
            model_partition="opus-4-6",
            baseline_updated_at="2026-04-10T10:04:00+02:00",
            baseline_note_snapshot_id=current_note.snapshot_id,
            baseline_criterion_snapshot_id=current_gate.snapshot_id,
        )
        deleted_job_ids = review_db.prune_superseded_freshness_baselines(conn, [superseded])
        remaining_snapshot_ids = {
            int(row["snapshot_id"])
            for row in conn.execute("SELECT snapshot_id FROM artifact_snapshots").fetchall()
        }
        old_pair = conn.execute(
            "SELECT review_pair_id FROM review_pairs WHERE review_pair_id = ?",
            (old_pair_id,),
        ).fetchone()
        current_pair = conn.execute(
            "SELECT review_pair_id FROM review_pairs WHERE review_pair_id = ?",
            (current_pair_id,),
        ).fetchone()

    assert deleted_job_ids == {old_job_id}
    assert old_pair is None
    assert current_pair is not None
    assert old_note.snapshot_id not in remaining_snapshot_ids
    assert old_gate.snapshot_id not in remaining_snapshot_ids
    assert current_note.snapshot_id in remaining_snapshot_ids
    assert current_gate.snapshot_id in remaining_snapshot_ids


def test_snapshot_file_rejects_non_repo_relative_paths(tmp_path: Path) -> None:
    db_path = tmp_path / "commonplace-store.sqlite"
    repo = tmp_path / "repo"
    repo.mkdir()
    review_db.ensure_db(db_path)

    with review_db.connect(db_path) as conn, pytest.raises(
        ValueError, match="repo-relative"
    ):
        review_db.snapshot_file(conn, repo_root=repo, path="../outside.md")
