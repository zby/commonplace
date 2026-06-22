from __future__ import annotations

import sqlite3
from pathlib import Path

from commonplace.review import review_db
from test.commonplace.review.pair_helpers import accept_pair, insert_completed_pair

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
        review_pair_id = insert_completed_pair(
            conn,
            note_path="kb/notes/old-note.md",
            gate_id="semantic/internal-consistency",
            model_id="opus-4-6",
            decision="pass",
            rationale_markdown="ok\n\n## Result: PASS\n",
            gate_sha="gate-sha",
            reviewed_note_sha="note-sha",
            reviewed_note_commit=None,
            reviewed_at="2026-04-10T10:01:00+02:00",
            runner="claude-code",
        )
        accept_pair(
            conn,
            review_pair_id=review_pair_id,
            note_path="kb/notes/old-note.md",
            gate_id="semantic/internal-consistency",
            model_id="opus-4-6",
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
                SELECT count(*) FROM review_pairs WHERE model_id = 'opus-4-6'
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
                SELECT count(*) FROM review_pairs WHERE model_id = 'claude-opus-4-6'
            ) + (
                SELECT count(*) FROM acceptance_events WHERE model_id = 'claude-opus-4-6'
            ) AS count
            """
        ).fetchone()["count"]

    assert old_count == 0
    assert new_count == 3
