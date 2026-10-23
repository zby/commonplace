import json
from pathlib import Path

import pytest

from commonplace.cli.status import main


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
