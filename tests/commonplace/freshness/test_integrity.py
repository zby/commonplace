from __future__ import annotations

from pathlib import Path

from commonplace.review.review_db import connect, ensure_db, snapshot_file
from commonplace.store import assert_store_integrity


def test_empty_file_snapshot_passes_integrity(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    empty = repo / "kb/notes/empty.md"
    empty.parent.mkdir(parents=True)
    empty.write_text("", encoding="utf-8")
    db_path = tmp_path / "store.sqlite"
    ensure_db(db_path)

    with connect(db_path) as conn:
        snapshot_file(conn, repo_root=repo, path="kb/notes/empty.md")
        conn.commit()

    with connect(db_path) as conn:
        assert_store_integrity(conn)