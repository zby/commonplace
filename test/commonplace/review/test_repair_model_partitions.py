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
    review_db.ensure_db(db_path)

    with review_db.connect(db_path) as conn:
        opus_review_pair_id = insert_completed_pair(
            conn,
            note_path="kb/notes/old-note.md",
            gate_id="semantic/internal-consistency",
            model_partition="opus-4-6",
            decision="pass",
            reviewed_at="2026-04-10T10:01:00+02:00",
            runner="claude-code",
        )
        accept_pair(
            conn,
            review_pair_id=opus_review_pair_id,
            note_path="kb/notes/old-note.md",
            gate_id="semantic/internal-consistency",
            model_partition="opus-4-6",
            accepted_at="2026-04-10T10:02:00+02:00",
        )
        fable_review_pair_id = insert_completed_pair(
            conn,
            note_path="kb/notes/fable-note.md",
            gate_id="prose/source-residue",
            model_partition="claude-fable-5",
            decision="pass",
            reviewed_at="2026-04-10T10:03:00+02:00",
            runner="claude-code",
        )
        accept_pair(
            conn,
            review_pair_id=fable_review_pair_id,
            note_path="kb/notes/fable-note.md",
            gate_id="prose/source-residue",
            model_partition="claude-fable-5",
            accepted_at="2026-04-10T10:04:00+02:00",
        )
        conn.commit()

    result = _run_repair(REPO_ROOT, db_path)

    assert "claude-fable-5 -> claude-opus-4.8: total=3" in result.stdout
    assert "opus-4-6 -> claude-opus: total=3" in result.stdout
    assert "mode: write" in result.stdout

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        old_count = conn.execute(
            """
            SELECT (
                SELECT count(*) FROM review_jobs WHERE model_partition = 'opus-4-6'
            ) + (
                SELECT count(*) FROM review_pairs WHERE model_partition = 'opus-4-6'
            ) + (
                SELECT count(*) FROM acceptance_events WHERE model_partition = 'opus-4-6'
            ) + (
                SELECT count(*) FROM review_jobs WHERE model_partition = 'claude-fable-5'
            ) + (
                SELECT count(*) FROM review_pairs WHERE model_partition = 'claude-fable-5'
            ) + (
                SELECT count(*) FROM acceptance_events WHERE model_partition = 'claude-fable-5'
            ) AS count
            """
        ).fetchone()["count"]
        opus_count = conn.execute(
            """
            SELECT (
                SELECT count(*) FROM review_jobs WHERE model_partition = 'claude-opus'
            ) + (
                SELECT count(*) FROM review_pairs WHERE model_partition = 'claude-opus'
            ) + (
                SELECT count(*) FROM acceptance_events WHERE model_partition = 'claude-opus'
            ) AS count
            """
        ).fetchone()["count"]
        opus_48_count = conn.execute(
            """
            SELECT (
                SELECT count(*) FROM review_jobs WHERE model_partition = 'claude-opus-4.8'
            ) + (
                SELECT count(*) FROM review_pairs WHERE model_partition = 'claude-opus-4.8'
            ) + (
                SELECT count(*) FROM acceptance_events WHERE model_partition = 'claude-opus-4.8'
            ) AS count
            """
        ).fetchone()["count"]

    assert old_count == 0
    assert opus_count == 3
    assert opus_48_count == 3
