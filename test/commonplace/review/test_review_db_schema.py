from __future__ import annotations

from importlib import resources
import sqlite3
from pathlib import Path

from commonplace.review import review_db


REPO_ROOT = Path(__file__).resolve().parents[3]


def test_ensure_db_does_not_mutate_existing_acceptance_event_schema(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    schema_text = (resources.files("commonplace.review") / "review-schema.sql").read_text(encoding="utf-8")
    old_schema = schema_text.replace("            'gate-migration',\n", "")

    with sqlite3.connect(db_path) as conn:
        conn.executescript(old_schema)
        conn.commit()

    review_db.ensure_db(REPO_ROOT, db_path)

    with review_db.connect(db_path) as conn:
        row = conn.execute(
            """
            SELECT sql
            FROM sqlite_master
            WHERE type = 'table' AND name = 'acceptance_events'
            """
        ).fetchone()

    assert row is not None
    assert "'gate-migration'" not in row["sql"].lower()


def test_ensure_db_initializes_new_db_from_current_schema(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"

    review_db.ensure_db(REPO_ROOT, db_path)

    with review_db.connect(db_path) as conn:
        row = conn.execute(
            """
            SELECT sql
            FROM sqlite_master
            WHERE type = 'table' AND name = 'acceptance_events'
            """
        ).fetchone()

    assert row is not None
    assert "'gate-migration'" in row["sql"].lower()


def test_rekey_note_path_updates_all_review_tables(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    review_db.ensure_db(REPO_ROOT, db_path)

    with review_db.connect(db_path) as conn:
        review_run_id = review_db.insert_review_run(
            conn,
            note_path="kb/notes/old-note.md",
            model_id="opus-4-6",
            runner="codex",
            reviewed_note_sha="note-sha",
            reviewed_note_commit="note-commit",
            started_at="2026-04-10T10:00:00+02:00",
        )
        review_id = review_db.insert_gate_review(
            conn,
            review_run_id=review_run_id,
            note_path="kb/notes/old-note.md",
            gate_id="semantic/internal-consistency",
            model_id="opus-4-6",
            decision="pass",
            rationale_markdown="ok",
            evidence_json=None,
            gate_sha="gate-sha",
            reviewed_note_sha="note-sha",
            reviewed_note_commit="note-commit",
            reviewed_at="2026-04-10T10:01:00+02:00",
        )
        review_db.append_acceptance_event(
            conn,
            note_path="kb/notes/old-note.md",
            gate_id="semantic/internal-consistency",
            model_id="opus-4-6",
            accepted_review_id=review_id,
            accepted_note_sha="note-sha",
            accepted_note_commit="note-commit",
            accepted_gate_sha="gate-sha",
            accepted_at="2026-04-10T10:02:00+02:00",
            acceptance_kind="full-review",
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

    assert counts.review_runs == 1
    assert counts.gate_reviews == 1
    assert counts.acceptance_events == 1
    assert updated == counts
    assert new_counts == counts
    assert old_counts.total == 0
