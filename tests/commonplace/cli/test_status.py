from __future__ import annotations

import json
from pathlib import Path

from commonplace.cli.status import main as status_main
from commonplace.lib import project_status
from commonplace.lib.project_status import load_review_status
from commonplace.store import ensure_db


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def test_status_omits_review_and_does_not_create_store_by_default(
    tmp_path: Path,
    capsys,
) -> None:
    write(tmp_path / "kb/notes/COLLECTION.md", "# Notes\n")
    write(tmp_path / "kb/notes/example.md", "# Example\n")
    write(tmp_path / "kb/work/README.md", "# Work\n")
    db_path = tmp_path / "kb/reports/state/commonplace-store.sqlite"

    exit_code = status_main(["--json"], cwd=tmp_path)
    payload = json.loads(capsys.readouterr().out)

    assert exit_code == 0
    assert payload["schema"] == "commonplace.status.v1"
    assert payload["status"] == "success"
    assert payload["notes_validation"]["status"] == "success"
    assert payload["lifecycle"]["status"] == "success"
    assert payload["review"] is None
    assert payload["actions"] == []
    assert not db_path.exists()


def test_status_review_flag_reports_missing_store_without_creating_it(
    tmp_path: Path,
    capsys,
) -> None:
    write(tmp_path / "kb/notes/COLLECTION.md", "# Notes\n")
    write(tmp_path / "kb/notes/example.md", "# Example\n")
    write(tmp_path / "kb/work/README.md", "# Work\n")
    db_path = tmp_path / "kb/reports/state/commonplace-store.sqlite"

    exit_code = status_main(["--review", "--json"], cwd=tmp_path)
    payload = json.loads(capsys.readouterr().out)

    assert exit_code == 1
    assert payload["status"] == "failed"
    assert payload["review"]["available"] is False
    assert payload["actions"][0]["action_id"] == "status.review.inspect-store"
    assert not db_path.exists()


def test_review_status_reads_an_existing_empty_store(tmp_path: Path) -> None:
    db_path = tmp_path / "kb/reports/state/commonplace-store.sqlite"
    db_path.parent.mkdir(parents=True)
    ensure_db(db_path)

    status = load_review_status(tmp_path)

    assert status.available is True
    assert status.error is None
    assert status.actionable_warn_findings == 0
    assert status.queued_jobs == 0
    assert status.failed_jobs == 0
    assert status.stale_freshness_targets == 0


def test_status_reports_basic_project_command_version_skew(
    tmp_path: Path,
    monkeypatch,
    capsys,
) -> None:
    write(
        tmp_path / "pyproject.toml",
        '[project]\nname = "example"\nversion = "1.2.3"\n',
    )
    write(tmp_path / "kb/notes/COLLECTION.md", "# Notes\n")
    write(tmp_path / "kb/notes/example.md", "# Example\n")
    write(tmp_path / "kb/work/README.md", "# Work\n")
    monkeypatch.setattr(project_status, "_command_version", lambda: "9.9.9")

    status_main(["--json"], cwd=tmp_path)
    payload = json.loads(capsys.readouterr().out)

    assert payload["actions"][0] == {
        "action_id": "status.version.inspect-skew",
        "command": "commonplace-source",
        "reason": "project version 1.2.3 differs from active command version 9.9.9",
        "severity": "failure",
    }
