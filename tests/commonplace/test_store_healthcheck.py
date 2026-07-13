from __future__ import annotations

from pathlib import Path

import pytest

from commonplace.cli.store_healthcheck import main as store_healthcheck_main
from commonplace.store import check_store_health, connect, ensure_db
from commonplace.review.review_db import snapshot_file


def test_ensure_db_skips_snapshot_hash_verification(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    note = repo / "kb/notes/example.md"
    note.parent.mkdir(parents=True)
    note.write_text("# Example\n", encoding="utf-8")
    db_path = tmp_path / "store.sqlite"
    ensure_db(db_path)

    with connect(db_path) as conn:
        snapshot_file(conn, repo_root=repo, path="kb/notes/example.md")
        conn.execute(
            """
            UPDATE artifact_snapshots
            SET content_sha256 = ?
            WHERE artifact_path = 'kb/notes/example.md'
            """,
            ("0" * 64,),
        )
        conn.commit()

    ensure_db(db_path)
    with pytest.raises(RuntimeError, match="hash mismatch"):
        check_store_health(db_path)


def test_store_healthcheck_cli_reports_healthy(tmp_path: Path, capsys) -> None:
    db_path = tmp_path / "store.sqlite"
    ensure_db(db_path)
    exit_code = store_healthcheck_main(["--db", str(db_path)], cwd=tmp_path)
    assert exit_code == 0
    assert capsys.readouterr().out.strip() == "healthy"