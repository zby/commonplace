"""`commonplace-status`: the selected validation scope, version skew, and the review summary over result files."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from commonplace.cli.status import main
from commonplace.lib import library, project_status
from commonplace.lib.review_workflows import results


def test_status_validates_only_explicit_collection_and_reports_scope(tmp_path: Path, capsys):
    root = tmp_path / "kb/teams/claims"
    root.mkdir(parents=True)
    (root / "COLLECTION.md").write_text("---\ntype: types/collection-contract.md\n---\n# Contract\n")
    (root / "capture.md").write_text("# Capture\n")
    # A broken unrelated collection must not become part of the selected validation.
    elsewhere = tmp_path / "kb/inbox"
    elsewhere.mkdir()
    (elsewhere / "COLLECTION.md").write_text("# Missing type\n")
    assert main(["--collection", "teams/claims", "--json"], cwd=tmp_path) == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["notes_validation"]["scope"] == "kb/teams/claims"
    assert payload["notes_validation"]["subjects"] == 1
    assert payload["notes_validation"]["details_command"] == "commonplace-validate kb/teams/claims"
    assert payload["lifecycle"]["scope"] == "kb/work and kb/tasks"
    assert not (tmp_path / "kb/notes").exists()
    assert not (tmp_path / "kb/theory").exists()
    assert not (tmp_path / "kb/reports").exists()


@pytest.mark.parametrize("args", [[], ["--collection", "missing"]])
def test_status_requires_a_valid_explicit_collection(tmp_path: Path, args: list[str]):
    with pytest.raises(SystemExit) as exc:
        main(args, cwd=tmp_path)
    assert exc.value.code == 2
    assert not (tmp_path / "kb/reports").exists()


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def project(root: Path) -> None:
    write(root / "kb/notes/COLLECTION.md", "---\ntype: types/collection-contract.md\n---\n\n# Notes\n")
    write(root / "kb/notes/example.md", "# Example\n")
    write(root / "kb/work/README.md", "# Work\n")


def status(root: Path, capsys, *args: str) -> tuple[int, dict]:
    code = main(["--collection", "notes", "--json", *args], cwd=root)
    return code, json.loads(capsys.readouterr().out)


def test_status_omits_review_by_default_and_writes_nothing(tmp_path: Path, capsys) -> None:
    project(tmp_path)
    code, payload = status(tmp_path, capsys)
    assert code == 0
    assert (payload["schema"], payload["status"], payload["review"], payload["actions"]) == (
        "commonplace.status.v2", "success", None, [])
    code, payload = status(tmp_path, capsys, "--review")
    assert code == 0 and payload["actions"] == []
    assert payload["review"] == {"results": 0, "fresh": 0, "stale": 0, "orphaned": 0, "warn": 0, "fail": 0,
                                 "error": None}
    assert not (tmp_path / "kb/reports").exists()


def test_status_review_summary_names_review_commands(tmp_path: Path, capsys, monkeypatch) -> None:
    project(tmp_path)
    monkeypatch.setattr(library, "_library_root", lambda _override: (tmp_path / "kb").resolve())
    gate = write(tmp_path / "kb/instructions/review-gates/prose/residue.md", "---\nwatches: [body]\n---\n# R\n")
    other = write(tmp_path / "kb/instructions/review-gates/prose/hedging.md", "# Hedging\n")
    note = tmp_path / "kb/notes/example.md"
    for criterion, outcome in ((gate, "warn"), (other, "fail")):
        results.write_result(tmp_path, results.make_result(
            "kb/notes/example.md", note.read_text(), criterion.relative_to(tmp_path).as_posix(), criterion.read_text(),
            outcome=outcome, profile={}, model=None, run="r", launch="l", completed_at="t", body=""))
    write(other, "# Hedging, revised\n")

    code, payload = status(tmp_path, capsys, "--review")
    assert code == 0
    assert payload["review"] == {"results": 2, "fresh": 1, "stale": 1, "orphaned": 0, "warn": 1, "fail": 0,
                                 "error": None}
    assert [(a["action_id"], a["command"]) for a in payload["actions"]] == [
        ("status.review.triage-warnings", "commonplace-review status --fresh --outcome warn"),
        ("status.review.rerun-stale", "commonplace-review status --stale")]

    next(tmp_path.joinpath(results.RESULTS).rglob("hedging.md")).write_text("not a result\n")
    code, payload = status(tmp_path, capsys, "--review")
    assert code == 1 and payload["status"] == "failed"
    assert payload["actions"][0]["action_id"] == "status.review.inspect-results"
    assert "hedging.md" in payload["review"]["error"]


def test_status_reports_project_command_version_skew(tmp_path: Path, monkeypatch, capsys) -> None:
    write(tmp_path / "pyproject.toml", '[project]\nname = "example"\nversion = "1.2.3"\n')
    project(tmp_path)
    monkeypatch.setattr(project_status, "_command_version", lambda: "9.9.9")
    _, payload = status(tmp_path, capsys)
    assert payload["actions"][0] == {
        "action_id": "status.version.inspect-skew",
        "command": "commonplace-source",
        "reason": "project version 1.2.3 differs from active command version 9.9.9",
        "severity": "failure",
    }
