from __future__ import annotations

import json
from pathlib import Path

from commonplace.cli.freshness_status import main as freshness_status_main
from commonplace.review.review_db import connect, ensure_db, snapshot_file
from tests.commonplace.review.pair_helpers import accept_pair, insert_completed_pair


def _seed_fresh_baseline(tmp_path: Path) -> None:
    (tmp_path / "kb/notes").mkdir(parents=True)
    (tmp_path / "kb/instructions/review-gates/prose").mkdir(parents=True)
    (tmp_path / "kb/notes/example.md").write_text("# Example\n", encoding="utf-8")
    (tmp_path / "kb/instructions/review-gates/prose/source-residue.md").write_text("# Gate\n", encoding="utf-8")
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


def test_freshness_status_reports_fresh(tmp_path: Path, capsys) -> None:
    _seed_fresh_baseline(tmp_path)
    exit_code = freshness_status_main(["--json", "--all"], cwd=tmp_path)
    assert exit_code == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["schema"] == "commonplace-freshness-status/1"
    assert payload["exit_class"] == "fresh"
    assert len(payload["targets"]) == 1
    assert payload["targets"][0]["changed_inputs"] == []


def test_freshness_status_reports_stale_after_note_edit(tmp_path: Path, capsys) -> None:
    _seed_fresh_baseline(tmp_path)
    (tmp_path / "kb/notes/example.md").write_text("# Changed\n", encoding="utf-8")
    exit_code = freshness_status_main(["--json"], cwd=tmp_path)
    assert exit_code == 1
    payload = json.loads(capsys.readouterr().out)
    assert payload["exit_class"] == "stale"
    changed = payload["targets"][0]["changed_inputs"][0]
    assert changed["status"] == "input-changed"
    assert changed["input_role"] == "note"