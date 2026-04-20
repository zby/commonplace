from __future__ import annotations

import sqlite3
from pathlib import Path

from commonplace.review import review_db

from ._run_cli import run_cli


REPO_ROOT = Path(__file__).resolve().parents[3]


def _run_repair(repo_root: Path, db_path: Path, *, check: bool = True):
    return run_cli(
        "migrations.repair_model_partitions",
        cwd=repo_root,
        db_path=db_path,
        check=check,
    )


def test_repair_model_partitions_rekeys_known_aliases(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    review_db.ensure_db(REPO_ROOT, db_path)

    with review_db.connect(db_path) as conn:
        review_run_id = review_db.insert_review_run(
            conn,
            note_path="kb/notes/old-note.md",
            model_id="opus-4-6",
            runner="claude-code",
            reviewed_note_sha="note-sha",
            reviewed_note_commit=None,
            started_at="2026-04-10T10:00:00+02:00",
        )
        review_id = review_db.insert_gate_review(
            conn,
            review_run_id=review_run_id,
            note_path="kb/notes/old-note.md",
            gate_id="semantic/internal-consistency",
            model_id="opus-4-6",
            decision="pass",
            rationale_markdown="ok\n\n## Result: PASS\n",
            evidence_json=None,
            gate_sha="gate-sha",
            reviewed_note_sha="note-sha",
            reviewed_note_commit=None,
            reviewed_at="2026-04-10T10:01:00+02:00",
        )
        review_db.append_acceptance_event(
            conn,
            note_path="kb/notes/old-note.md",
            gate_id="semantic/internal-consistency",
            model_id="opus-4-6",
            accepted_review_id=review_id,
            accepted_note_sha="note-sha",
            accepted_note_commit=None,
            accepted_gate_sha="gate-sha",
            accepted_at="2026-04-10T10:02:00+02:00",
            acceptance_kind="full-review",
        )
        conn.commit()

    result = _run_repair(REPO_ROOT, db_path)

    assert "opus-4-6 -> claude-opus-4-6: total=3" in result.stdout
    assert "mode: write" in result.stdout

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        old_count = conn.execute(
            """
            SELECT (
                SELECT count(*) FROM review_runs WHERE model_id = 'opus-4-6'
            ) + (
                SELECT count(*) FROM gate_reviews WHERE model_id = 'opus-4-6'
            ) + (
                SELECT count(*) FROM acceptance_events WHERE model_id = 'opus-4-6'
            ) AS count
            """
        ).fetchone()["count"]
        new_count = conn.execute(
            """
            SELECT (
                SELECT count(*) FROM review_runs WHERE model_id = 'claude-opus-4-6'
            ) + (
                SELECT count(*) FROM gate_reviews WHERE model_id = 'claude-opus-4-6'
            ) + (
                SELECT count(*) FROM acceptance_events WHERE model_id = 'claude-opus-4-6'
            ) AS count
            """
        ).fetchone()["count"]

    assert old_count == 0
    assert new_count == 3


def test_repair_model_partitions_renames_legacy_review_files(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    review_db.ensure_db(REPO_ROOT, db_path)
    legacy_path = (
        tmp_path
        / "kb"
        / "reports"
        / "reviews"
        / "kb__notes__sample"
        / "prose__source-residue.opus-4-6.md"
    )
    legacy_path.parent.mkdir(parents=True)
    legacy_path.write_text("legacy review\n", encoding="utf-8")
    target_path = legacy_path.with_name("prose__source-residue.claude-opus-4-6.md")

    result = _run_repair(tmp_path, db_path)

    assert "legacy_review_files: 1" in result.stdout
    assert not legacy_path.exists()
    assert target_path.read_text(encoding="utf-8") == "legacy review\n"


def test_repair_model_partitions_refuses_to_overwrite_legacy_review_files(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    review_db.ensure_db(REPO_ROOT, db_path)
    reports_dir = tmp_path / "kb" / "reports" / "reviews" / "kb__notes__sample"
    reports_dir.mkdir(parents=True)
    legacy_path = reports_dir / "prose__source-residue.opus-4-6.md"
    target_path = reports_dir / "prose__source-residue.claude-opus-4-6.md"
    legacy_path.write_text("legacy review\n", encoding="utf-8")
    target_path.write_text("canonical review\n", encoding="utf-8")

    result = _run_repair(tmp_path, db_path, check=False)

    assert result.returncode != 0
    assert "refusing to overwrite 1 legacy review file(s)" in result.stderr
    assert legacy_path.read_text(encoding="utf-8") == "legacy review\n"
    assert target_path.read_text(encoding="utf-8") == "canonical review\n"
