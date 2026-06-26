from __future__ import annotations

from hashlib import sha256
from pathlib import Path

import pytest

from commonplace.review import review_db
from test.commonplace.review.pair_helpers import accept_pair, insert_completed_pair


REPO_ROOT = Path(__file__).resolve().parents[3]


def test_ensure_db_initializes_schema_that_can_store_current_acceptance(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"

    review_db.ensure_db(REPO_ROOT, db_path)

    with review_db.connect(db_path) as conn:
        review_pair_id = insert_completed_pair(
            conn,
            note_path="kb/notes/fresh.md",
            gate_id="semantic/internal-consistency",
            model_partition="opus-4-6",
            decision="pass",
            rationale_markdown="ok",
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
                accepted_note_snapshot_id,
                accepted_gate_snapshot_id,
                accepted_note_hash,
                accepted_gate_hash
            FROM current_gate_acceptances
            WHERE note_path = 'kb/notes/fresh.md'
            """
        ).fetchone()
        migration_table = conn.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type = 'table'
              AND name = 'review_schema_migrations'
            """
        ).fetchone()

    assert view_row is not None
    assert view_row["accepted_note_snapshot_id"] is None
    assert view_row["accepted_gate_snapshot_id"] is None
    assert view_row["accepted_note_hash"] is None
    assert view_row["accepted_gate_hash"] is None
    assert migration_table is None


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

    review_db.ensure_db(REPO_ROOT, db_path)

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


def test_snapshot_file_rehydrates_hash_only_snapshot_rows(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    repo = tmp_path / "repo"
    repo.mkdir()
    note = repo / "kb" / "notes" / "sample.md"
    note.parent.mkdir(parents=True)
    note.write_text("rehydrate me\n", encoding="utf-8")

    review_db.ensure_db(REPO_ROOT, db_path)

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

    review_db.ensure_db(REPO_ROOT, db_path)

    with review_db.connect(db_path) as conn:
        old_note = review_db.snapshot_file(conn, repo_root=repo, path="kb/notes/old.md")
        old_gate = review_db.snapshot_file(conn, repo_root=repo, path="kb/instructions/review-gates/prose/old.md")
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
        review_db.append_acceptance_event(
            conn,
            note_path="kb/notes/current.md",
            gate_path="kb/instructions/review-gates/prose/current.md",
            model_partition="opus-4-6",
            accepted_review_pair_id=None,
            accepted_note_snapshot_id=current_note.snapshot_id,
            accepted_gate_snapshot_id=current_gate.snapshot_id,
            accepted_at="2026-04-10T10:02:00+02:00",
        )
        review_db.create_run_with_pairs(
            conn,
            model_partition="opus-4-6",
            runner="test-runner",
            started_at="2026-04-10T10:03:00+02:00",
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

    review_db.ensure_db(REPO_ROOT, db_path)

    with review_db.connect(db_path) as conn:
        note_snapshot = review_db.snapshot_file(conn, repo_root=repo, path="kb/notes/sample.md")
        gate_snapshot = review_db.snapshot_file(
            conn,
            repo_root=repo,
            path="kb/instructions/review-gates/prose/sample.md",
        )
        acceptance_event_id = accept_pair(
            conn,
            review_pair_id=None,
            note_path="kb/notes/sample.md",
            gate_id="prose/sample",
            model_partition="opus-4-6",
            accepted_at="2026-04-10T10:02:00+02:00",
        )
        conn.execute(
            """
            UPDATE acceptance_events
            SET accepted_note_snapshot_id = ?,
                accepted_gate_snapshot_id = ?
            WHERE acceptance_event_id = ?
            """,
            (note_snapshot.snapshot_id, gate_snapshot.snapshot_id, acceptance_event_id),
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
    review_db.ensure_db(REPO_ROOT, db_path)

    with review_db.connect(db_path) as conn:
        with pytest.raises(ValueError, match="repo-relative"):
            review_db.snapshot_file(conn, repo_root=repo, path="../outside.md")


def test_rekey_note_path_updates_all_review_tables(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    review_db.ensure_db(REPO_ROOT, db_path)

    with review_db.connect(db_path) as conn:
        review_pair_id = insert_completed_pair(
            conn,
            note_path="kb/notes/old-note.md",
            gate_id="semantic/internal-consistency",
            model_partition="opus-4-6",
            decision="pass",
            rationale_markdown="ok",
            reviewed_at="2026-04-10T10:01:00+02:00",
        )
        accept_pair(
            conn,
            review_pair_id=review_pair_id,
            note_path="kb/notes/old-note.md",
            gate_id="semantic/internal-consistency",
            model_partition="opus-4-6",
            accepted_at="2026-04-10T10:02:00+02:00",
        )

        counts = review_db.count_note_path_records(conn, note_path="kb/notes/old-note.md")
        updated = review_db.rekey_note_path(
            conn,
            old_note_path="kb/notes/old-note.md",
            new_note_path="kb/notes/archive/new-note.md",
        )
        conn.commit()

        new_counts = review_db.count_note_path_records(conn, note_path="kb/notes/archive/new-note.md")
        old_counts = review_db.count_note_path_records(conn, note_path="kb/notes/old-note.md")

    assert counts.review_pairs == 1
    assert counts.acceptance_events == 1
    assert updated == counts
    assert new_counts == counts
    assert old_counts.total == 0
