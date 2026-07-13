from __future__ import annotations

import sqlite3
from pathlib import Path

import pytest

from commonplace.cli.store_healthcheck import main as store_healthcheck_main
from commonplace.store import LEGACY_DB_PATH, check_store_health, connect, ensure_db
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


def test_ensure_db_requires_migration_when_legacy_default_exists(tmp_path: Path) -> None:
    reports = tmp_path / "kb/reports"
    reports.mkdir(parents=True)
    legacy = reports / LEGACY_DB_PATH.name
    legacy.write_bytes(b"")
    db_path = reports / "commonplace-store.sqlite"
    with pytest.raises(RuntimeError, match="migration required"):
        ensure_db(db_path)


def test_ensure_db_requires_migration_for_legacy_v7_store(tmp_path: Path) -> None:
    legacy = tmp_path / LEGACY_DB_PATH
    legacy.parent.mkdir(parents=True)
    with sqlite3.connect(legacy) as conn:
        conn.execute("PRAGMA user_version = 7")
    with pytest.raises(RuntimeError, match="migration required.*schema v7"):
        ensure_db(legacy)


def test_ensure_db_requires_migration_when_commonplace_replaced_by_legacy_env(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    legacy = tmp_path / "kb/reports/review-store.sqlite"
    legacy.parent.mkdir(parents=True)
    with sqlite3.connect(legacy) as conn:
        conn.execute("PRAGMA user_version = 7")
    monkeypatch.setenv("COMMONPLACE_REVIEW_DB", str(legacy))
    with pytest.raises(RuntimeError, match="migration required"):
        ensure_db(legacy)


def test_store_healthcheck_cli_reports_healthy(tmp_path: Path, capsys) -> None:
    db_path = tmp_path / "store.sqlite"
    ensure_db(db_path)
    exit_code = store_healthcheck_main(["--db", str(db_path)], cwd=tmp_path)
    assert exit_code == 0
    assert capsys.readouterr().out.strip() == "healthy"