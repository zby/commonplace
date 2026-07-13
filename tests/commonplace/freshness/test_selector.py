from __future__ import annotations

from pathlib import Path

from commonplace.freshness.status import load_target_status
from commonplace.review.review_db import connect, ensure_db, snapshot_file
from tests.commonplace.review.pair_helpers import accept_pair, insert_completed_pair


def _seed_baseline(tmp_path: Path) -> Path:
    (tmp_path / "kb/notes").mkdir(parents=True)
    (tmp_path / "kb/instructions/review-gates/prose").mkdir(parents=True)
    note = tmp_path / "kb/notes/example.md"
    gate = tmp_path / "kb/instructions/review-gates/prose/source-residue.md"
    note.write_text("# Example\n", encoding="utf-8")
    gate.write_text("# Gate\n", encoding="utf-8")
    db_path = tmp_path / "kb/reports/commonplace-store.sqlite"
    ensure_db(db_path)
    with connect(db_path) as conn:
        note_snapshot = snapshot_file(conn, repo_root=tmp_path, path="kb/notes/example.md")
        criterion_snapshot = snapshot_file(
            conn,
            repo_root=tmp_path,
            path="kb/instructions/review-gates/prose/source-residue.md",
        )
        pair_id = insert_completed_pair(
            conn,
            note_path="kb/notes/example.md",
            criterion_id="prose/source-residue",
            model_partition="codex",
            outcome="pass",
            completed_at="2026-07-13T00:00:00+00:00",
            reviewed_note_snapshot_id=note_snapshot.snapshot_id,
            reviewed_criterion_snapshot_id=criterion_snapshot.snapshot_id,
        )
        accept_pair(
            conn,
            review_pair_id=pair_id,
            note_path="kb/notes/example.md",
            criterion_id="prose/source-residue",
            model_partition="codex",
            baseline_updated_at="2026-07-13T00:00:00+00:00",
            baseline_note_snapshot_id=note_snapshot.snapshot_id,
            baseline_criterion_snapshot_id=criterion_snapshot.snapshot_id,
        )
        conn.commit()
    return db_path


def test_status_reports_version_error_for_invalid_utf8(tmp_path: Path) -> None:
    db_path = _seed_baseline(tmp_path)
    (tmp_path / "kb/notes/example.md").write_bytes(b"\xff\xfe")

    with connect(db_path) as conn:
        status = load_target_status(conn, repo_root=tmp_path)

    assert status.exit_class == "error"
    changed = status.targets[0].changed_inputs[0]
    assert changed.status == "version-error"
    assert changed.input_role == "note"