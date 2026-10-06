from __future__ import annotations

from hashlib import sha256
from pathlib import Path

import pytest
import yaml

from commonplace.lib.agentic_finalize import build_manifest, start_manifest
from commonplace.lib.agentic_set import SET_TYPE

REPO_ROOT = Path(__file__).resolve().parents[3]


def test_manifest_pins_the_members_present(tmp_path: Path) -> None:
    output = tmp_path / "output"
    output.mkdir()
    (output / "boundary.md").write_text("boundary", encoding="utf-8")
    (output / "overview.md").write_text("overview", encoding="utf-8")
    (output / "runtime.md").write_text("runtime", encoding="utf-8")
    (output / "notes.md").write_text("not a member", encoding="utf-8")

    text = build_manifest(tmp_path)

    manifest = yaml.safe_load((output / "ARTIFACT.yaml").read_text(encoding="utf-8"))
    assert manifest == yaml.safe_load(text)
    assert manifest["type"] == "agentic-system-analyses/types/agentic-system-analysis-set.md"
    assert list(manifest["members"]) == ["boundary.md", "overview.md", "runtime.md"]
    assert manifest["members"]["runtime.md"] == {"sha256": sha256(b"runtime").hexdigest()}


def test_manifest_names_the_worker_from_run_metadata(tmp_path: Path) -> None:
    output = tmp_path / "output"
    output.mkdir()
    (output / "boundary.md").write_text("boundary", encoding="utf-8")
    (output / "overview.md").write_text("overview", encoding="utf-8")
    (tmp_path / "run-metadata.json").write_text(
        '{"inputs-commit": "abc", "run-date": "2026-10-06", "model": "claude-fable-5-1", "effort": ""}',
        encoding="utf-8")

    manifest = yaml.safe_load(build_manifest(tmp_path))

    assert manifest["worker"] == {"model": "claude-fable-5-1"}
    assert list(manifest) == ["type", "members", "worker"]


def test_manifest_needs_the_members_every_set_has(tmp_path: Path) -> None:
    (tmp_path / "output").mkdir()
    (tmp_path / "output" / "overview.md").write_text("overview", encoding="utf-8")

    with pytest.raises(ValueError, match="missing: .*boundary.md"):
        build_manifest(tmp_path)


def test_a_working_manifest_names_the_type_and_survives_a_replay(tmp_path: Path) -> None:
    start_manifest(tmp_path)
    manifest = tmp_path / "output" / "ARTIFACT.yaml"
    assert yaml.safe_load(manifest.read_text()) == {"type": SET_TYPE}
    manifest.write_text("pinned\n", encoding="utf-8")
    start_manifest(tmp_path)
    assert manifest.read_text() == "pinned\n"


class _State:
    def __init__(self, run_dir: Path, status: str = "running") -> None:
        self.run_dir = run_dir
        self.status = status


def _cli(monkeypatch, tmp_path: Path, state: _State, *argv: str) -> int:
    from commonplace.cli import agentic_analysis_finalize

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(agentic_analysis_finalize, "load_run_state", lambda *a, **k: state)
    return agentic_analysis_finalize.main([*argv, "run-state.md"])


@pytest.mark.usefixtures("tmp_library")
def test_command_pins_a_running_run(tmp_path: Path, monkeypatch) -> None:
    spec = tmp_path / "kb" / SET_TYPE
    spec.parent.mkdir(parents=True)
    spec.write_bytes((REPO_ROOT / "kb" / SET_TYPE).read_bytes())
    run_dir = tmp_path / "run"
    (run_dir / "output").mkdir(parents=True)
    for name in ("boundary.md", "overview.md", "memory.md"):
        (run_dir / "output" / name).write_text(f"---\ntype: t\n---\n\n{name}", encoding="utf-8")

    assert _cli(monkeypatch, tmp_path, _State(run_dir), "manifest") == 0
    assert "memory.md" in yaml.safe_load((run_dir / "output" / "ARTIFACT.yaml").read_text())["members"]


@pytest.mark.usefixtures("tmp_library")
def test_command_refuses_a_run_that_is_not_running(tmp_path: Path, monkeypatch, capsys) -> None:
    assert _cli(monkeypatch, tmp_path, _State(tmp_path, "complete"), "manifest") == 1
    assert "not running" in capsys.readouterr().err
