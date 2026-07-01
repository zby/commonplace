from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import sqlite3

import pytest

from commonplace.review import review_db, review_schema
from test.commonplace.review.pair_helpers import accept_pair, insert_completed_pair


def test_ensure_db_initializes_current_schema(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"

    review_db.ensure_db(db_path)

    with review_db.connect(db_path) as conn:
        review_pair_id = insert_completed_pair(
            conn,
            note_path="kb/notes/fresh.md",
            gate_id="semantic/internal-consistency",
            model_partition="opus-4-6",
            decision="pass",
            reviewed_at="2026-04-10T10:01:00+02:00",
        )
        accept_pair(
            conn,
            review_pair_id=review_pair_id,
            note_path="kb/notes/fresh.md",
            gate_id="semantic/internal-consistency",
            model_partition="opus-4-6",
            accepted_at="2026-04-10T10:02:00+02:00",
        )
        view_row = conn.execute(
            """
            SELECT
                accepted_review_pair_id,
                accepted_note_snapshot_id,
                accepted_gate_snapshot_id,
                accepted_note_hash,
                accepted_gate_hash
            FROM current_gate_acceptances
            WHERE note_path = 'kb/notes/fresh.md'
            """
        ).fetchone()
        user_version = conn.execute("PRAGMA user_version").fetchone()[0]
        job_columns = {row["name"]: row for row in conn.execute("PRAGMA table_info(review_jobs)").fetchall()}
        pair_columns = {row["name"] for row in conn.execute("PRAGMA table_info(review_pairs)").fetchall()}
        acceptance_columns = {
            row["name"]: row
            for row in conn.execute("PRAGMA table_info(acceptance_events)").fetchall()
        }
        index_names = {
            row["name"]
            for row in conn.execute(
                "SELECT name FROM sqlite_master WHERE type = 'index'"
            ).fetchall()
        }
        table_names = {
            row["name"]
            for row in conn.execute(
                "SELECT name FROM sqlite_master WHERE type = 'table'"
            ).fetchall()
        }

    assert view_row is not None
    assert view_row["accepted_review_pair_id"] == review_pair_id
    assert view_row["accepted_note_snapshot_id"] is None
    assert view_row["accepted_gate_snapshot_id"] is None
    assert view_row["accepted_note_hash"] is None
    assert view_row["accepted_gate_hash"] is None
    assert user_version == review_schema.REVIEW_SCHEMA_VERSION
    assert "created_at" in job_columns
    assert "started_at" not in job_columns
    assert job_columns["runner"]["notnull"] == 0
    assert "runner_model" in job_columns
    assert "runner_effort" in job_columns
    assert "prompt_path" not in job_columns
    assert "bundle_output_path" not in job_columns
    assert "model_partition" not in pair_columns
    assert "result_path" not in pair_columns
    assert acceptance_columns["accepted_review_pair_id"]["notnull"] == 1
    assert "idx_review_pairs_note_gate" in index_names
    assert "idx_review_pairs_note_gate_model_partition" not in index_names
    assert table_names == {
        "acceptance_events",
        "review_file_snapshots",
        "review_jobs",
        "review_pairs",
    }


def test_ensure_db_rejects_stale_review_store_shape(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    db_path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(db_path) as conn:
        conn.execute("CREATE TABLE review_jobs (review_job_id INTEGER PRIMARY KEY)")
        conn.commit()

    with pytest.raises(RuntimeError, match="does not match current version"):
        review_db.ensure_db(db_path)


def test_append_acceptance_event_requires_review_pair(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    review_db.ensure_db(db_path)

    with review_db.connect(db_path) as conn:
        invalid_pair_id = None
        with pytest.raises(ValueError, match="accepted_review_pair_id is required"):
            review_db.append_acceptance_event(
                conn,
                note_path="kb/notes/current.md",
                gate_path="kb/instructions/review-gates/prose/current.md",
                model_partition="opus-4-6",
                accepted_review_pair_id=invalid_pair_id,
                accepted_at="2026-04-10T10:02:00+02:00",
            )


def test_snapshot_file_deduplicates_per_path_and_hashes_exact_utf8(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
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
        gate_snapshot = review_db.snapshot_file(
            conn,
            repo_root=repo,
            path="kb/instructions/review-gates/prose/sample.md",
        )

    assert first.snapshot_id == second.snapshot_id
    assert first.path == "kb/notes/sample.md"
    assert first.content_text == "title\n\ncafe\u0301\n"
    assert first.content_sha256 == sha256("title\n\ncafe\u0301\n".encode("utf-8")).hexdigest()
    assert gate_snapshot.snapshot_id != first.snapshot_id
    assert gate_snapshot.content_sha256 == first.content_sha256


def test_load_review_job_exposes_created_at(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    review_db.ensure_db(db_path)

    with review_db.connect(db_path) as conn:
        review_job_id = review_db.create_job_with_pairs(
            conn,
            model_partition="opus-4-6",
            runner="live-agent",
            created_at="2026-04-10T10:03:00+02:00",
            status="queued",
            packing="note",
            pairs=[
                review_db.ReviewPairRequest(
                    note_path="kb/notes/pending.md",
                    gate_path="kb/instructions/review-gates/prose/pending.md",
                    pair_ordinal=0,
                )
            ],
        )
        review_job = review_db.load_review_job(conn, review_job_id=review_job_id)

    assert review_job is not None
    assert review_job.created_at == "2026-04-10T10:03:00+02:00"
    assert review_job.status == "queued"


def test_snapshot_file_rehydrates_hash_only_snapshot_rows(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    repo = tmp_path / "repo"
    repo.mkdir()
    note = repo / "kb" / "notes" / "sample.md"
    note.parent.mkdir(parents=True)
    note.write_text("rehydrate me\n", encoding="utf-8")

    review_db.ensure_db(db_path)

    with review_db.connect(db_path) as conn:
        first = review_db.snapshot_file(conn, repo_root=repo, path="kb/notes/sample.md")
        conn.execute(
            "UPDATE review_file_snapshots SET content_text = NULL WHERE snapshot_id = ?",
            (first.snapshot_id,),
        )
        second = review_db.snapshot_file(conn, repo_root=repo, path="kb/notes/sample.md")
        stored_text = conn.execute(
            "SELECT content_text FROM review_file_snapshots WHERE snapshot_id = ?",
            (first.snapshot_id,),
        ).fetchone()[0]

    assert second.snapshot_id == first.snapshot_id
    assert second.content_text == "rehydrate me\n"
    assert stored_text == "rehydrate me\n"


def test_prune_obsolete_snapshot_content_keeps_current_and_pending_text(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    repo = tmp_path / "repo"
    repo.mkdir()
    files = {
        "kb/notes/old.md": "old note\n",
        "kb/instructions/review-gates/prose/old.md": "old gate\n",
        "kb/notes/current.md": "current note\n",
        "kb/instructions/review-gates/prose/current.md": "current gate\n",
        "kb/notes/pending.md": "pending note\n",
        "kb/instructions/review-gates/prose/pending.md": "pending gate\n",
    }
    for rel_path, content in files.items():
        path = repo / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    review_db.ensure_db(db_path)

    with review_db.connect(db_path) as conn:
        old_note = review_db.snapshot_file(conn, repo_root=repo, path="kb/notes/old.md")
        old_gate = review_db.snapshot_file(
            conn,
            repo_root=repo,
            path="kb/instructions/review-gates/prose/old.md",
        )
        current_note = review_db.snapshot_file(conn, repo_root=repo, path="kb/notes/current.md")
        current_gate = review_db.snapshot_file(
            conn,
            repo_root=repo,
            path="kb/instructions/review-gates/prose/current.md",
        )
        pending_note = review_db.snapshot_file(conn, repo_root=repo, path="kb/notes/pending.md")
        pending_gate = review_db.snapshot_file(
            conn,
            repo_root=repo,
            path="kb/instructions/review-gates/prose/pending.md",
        )
        review_pair_id = insert_completed_pair(
            conn,
            note_path="kb/notes/current.md",
            gate_id="prose/current",
            model_partition="opus-4-6",
            decision="pass",
            reviewed_at="2026-04-10T10:01:00+02:00",
            reviewed_note_snapshot_id=current_note.snapshot_id,
            reviewed_gate_snapshot_id=current_gate.snapshot_id,
        )
        accept_pair(
            conn,
            review_pair_id=review_pair_id,
            note_path="kb/notes/current.md",
            gate_id="prose/current",
            model_partition="opus-4-6",
            accepted_at="2026-04-10T10:02:00+02:00",
            accepted_note_snapshot_id=current_note.snapshot_id,
            accepted_gate_snapshot_id=current_gate.snapshot_id,
        )
        review_db.create_job_with_pairs(
            conn,
            model_partition="opus-4-6",
            runner="test-runner",
            created_at="2026-04-10T10:03:00+02:00",
            status="running",
            packing="note",
            pairs=[
                review_db.ReviewPairRequest(
                    note_path="kb/notes/pending.md",
                    gate_path="kb/instructions/review-gates/prose/pending.md",
                    pair_ordinal=0,
                    reviewed_note_snapshot_id=pending_note.snapshot_id,
                    reviewed_gate_snapshot_id=pending_gate.snapshot_id,
                )
            ],
        )
        pruned = review_db.prune_obsolete_snapshot_content(conn)
        rows = {
            int(row["snapshot_id"]): row["content_text"]
            for row in conn.execute(
                "SELECT snapshot_id, content_text FROM review_file_snapshots"
            ).fetchall()
        }

    assert pruned == 2
    assert rows[old_note.snapshot_id] is None
    assert rows[old_gate.snapshot_id] is None
    assert rows[current_note.snapshot_id] == "current note\n"
    assert rows[current_gate.snapshot_id] == "current gate\n"
    assert rows[pending_note.snapshot_id] == "pending note\n"
    assert rows[pending_gate.snapshot_id] == "pending gate\n"


def test_current_acceptance_view_exposes_snapshot_hashes(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    repo = tmp_path / "repo"
    repo.mkdir()
    note = repo / "kb" / "notes" / "sample.md"
    gate = repo / "kb" / "instructions" / "review-gates" / "prose" / "sample.md"
    note.parent.mkdir(parents=True)
    gate.parent.mkdir(parents=True)
    note.write_text("note text\n", encoding="utf-8")
    gate.write_text("gate text\n", encoding="utf-8")

    review_db.ensure_db(db_path)

    with review_db.connect(db_path) as conn:
        note_snapshot = review_db.snapshot_file(conn, repo_root=repo, path="kb/notes/sample.md")
        gate_snapshot = review_db.snapshot_file(
            conn,
            repo_root=repo,
            path="kb/instructions/review-gates/prose/sample.md",
        )
        review_pair_id = insert_completed_pair(
            conn,
            note_path="kb/notes/sample.md",
            gate_id="prose/sample",
            model_partition="opus-4-6",
            decision="pass",
            reviewed_at="2026-04-10T10:01:00+02:00",
            reviewed_note_snapshot_id=note_snapshot.snapshot_id,
            reviewed_gate_snapshot_id=gate_snapshot.snapshot_id,
        )
        accept_pair(
            conn,
            review_pair_id=review_pair_id,
            note_path="kb/notes/sample.md",
            gate_id="prose/sample",
            model_partition="opus-4-6",
            accepted_at="2026-04-10T10:02:00+02:00",
            accepted_note_snapshot_id=note_snapshot.snapshot_id,
            accepted_gate_snapshot_id=gate_snapshot.snapshot_id,
        )
        view_row = conn.execute(
            """
            SELECT
                accepted_note_snapshot_id,
                accepted_gate_snapshot_id,
                accepted_note_hash,
                accepted_gate_hash
            FROM current_gate_acceptances
            WHERE note_path = 'kb/notes/sample.md'
            """
        ).fetchone()

    assert view_row["accepted_note_snapshot_id"] == note_snapshot.snapshot_id
    assert view_row["accepted_gate_snapshot_id"] == gate_snapshot.snapshot_id
    assert view_row["accepted_note_hash"] == note_snapshot.content_sha256
    assert view_row["accepted_gate_hash"] == gate_snapshot.content_sha256


def test_snapshot_file_rejects_non_repo_relative_paths(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    repo = tmp_path / "repo"
    repo.mkdir()
    review_db.ensure_db(db_path)

    with review_db.connect(db_path) as conn:
        with pytest.raises(ValueError, match="repo-relative"):
            review_db.snapshot_file(conn, repo_root=repo, path="../outside.md")
