import json
import os
import shlex
from pathlib import Path

import pytest

from commonplace.cli.validate_notes import main, resolve_validation_target


def write(path: Path, text: str = "# Capture\n") -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    return path


@pytest.mark.parametrize("name", ["claims", "teams/claims"])
def test_collection_names_use_generic_target_resolution(tmp_path: Path, name: str):
    root = tmp_path / "kb" / name
    write(root / "COLLECTION.md", "---\ntype: types/collection-contract.md\n---\n# Contract\n")
    note = write(root / "capture.md")
    target = resolve_validation_target(name, repo_root=tmp_path)
    assert target.collection == root
    assert target.paths == (note,)


@pytest.mark.parametrize("target_name", ["today", "recent"])
def test_recent_requires_explicit_scope_and_preserves_validation_boundaries(
    tmp_path: Path, target_name: str,
):
    root = tmp_path / "kb/teams/claims"
    write(root / "COLLECTION.md")
    current = write(root / "current.md")
    old = write(root / "old.md")
    os.utime(old, (1, 1))
    write(root / "captured/.commonplace-validation-ignore", "")
    write(root / "captured/pinned.md")
    write(root / ".hidden/invisible.md")
    write(tmp_path / "kb/elsewhere/out-of-scope.md")
    artifact = root / "packet"
    write(artifact / "ARTIFACT.yaml", "type: example/types/packet.md\n")
    with pytest.raises(ValueError, match="requires --collection"):
        resolve_validation_target(target_name, repo_root=tmp_path)
    target = resolve_validation_target(
        target_name, repo_root=tmp_path, collection="teams/claims",
    )
    assert target.paths == (current, artifact)
    assert target.collection == root
    assert target.ignored_dirs == (root / "captured",)


def test_full_collection_warns_for_each_visible_directory_without_readme(tmp_path, monkeypatch, capsys):
    root = tmp_path / "kb/claims"
    write(root / "COLLECTION.md", "---\ntype: types/collection-contract.md\n---\n# Contract\n")
    (root / "group/empty").mkdir(parents=True)
    write(root / "captured/.commonplace-validation-ignore", "")
    write(root / ".hidden/note.md")
    monkeypatch.chdir(tmp_path)

    def missing(*args):
        assert main([*args, "--json"]) == 0
        return [d["subject"] for d in json.loads(capsys.readouterr().out)["diagnostics"]
                if d["id"] == "validation.collection-warning.missing-readme-md" and d["severity"] == "warning"]

    assert missing("claims") == ["kb/claims", "kb/claims/group", "kb/claims/group/empty"]
    write(root / "group/README.md")
    assert missing("kb/claims") == ["kb/claims", "kb/claims/group/empty"]
    for args in [("kb/claims/group",), ("kb/claims/group/README.md",), ("recent", "--collection", "claims")]:
        assert not missing(*args)


def test_collection_option_is_rejected_for_nonrecent_targets(tmp_path: Path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    for target in ("landings", "redirects", "lifecycle", "types", "claims"):
        with pytest.raises(SystemExit) as exc:
            main([target, "--collection", "claims"])
        assert exc.value.code == 2


def test_recent_drilldown_keeps_collection_scope(tmp_path: Path, monkeypatch, capsys):
    root = tmp_path / "kb/teams/claims space"
    write(root / "COLLECTION.md", "---\ntype: types/collection-contract.md\n---\n# Contract\n")
    write(root / "capture.md")
    monkeypatch.chdir(tmp_path)
    assert main(["recent", "--collection", "teams/claims space", "--json"]) == 0
    payload = json.loads(capsys.readouterr().out)
    command = payload["details_command"]
    assert shlex.split(command) == [
        "commonplace-validate", "--full", "recent", "--collection", "kb/teams/claims space",
    ]
    assert main(shlex.split(command)[1:]) == 0
    assert "Files analysed: 1" in capsys.readouterr().out
