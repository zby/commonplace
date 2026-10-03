"""Analysis preparation isolates committed bytes without weakening startup checks."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

from commonplace.cli.workflow import main
from commonplace.lib import analysis_worktree as aw


def git(root: Path, *args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(root), *args], check=True, capture_output=True, text=True
    ).stdout.strip()


@pytest.fixture
def origin(tmp_path: Path, monkeypatch) -> Path:
    root = tmp_path / "origin"
    root.mkdir()
    git(root, "init", "--quiet")
    git(root, "config", "user.email", "test@example.com")
    git(root, "config", "user.name", "Test")
    files = {
        ".gitignore": ".venv/\n/.commonplace/worktrees/\n",
        "AGENTS.md": "Committed instructions\n",
        "pyproject.toml": '[project]\nname = "llm-commonplace"\n',
        "uv.lock": "version = 1\n",
        "src/commonplace/lib/agentic_workflow.py": "# committed runtime\n",
        "note.md": "Committed note\n",
        "kb/instructions/worker/SKILL.md": "Committed skill\n",
    }
    for name, content in files.items():
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
    skills = root / ".agents/skills"
    skills.mkdir(parents=True)
    (skills / "worker").symlink_to("../../kb/instructions/worker", target_is_directory=True)
    git(root, "add", ".")
    git(root, "commit", "--quiet", "-m", "Seed")
    monkeypatch.setattr(aw, "_install", lambda tree: {
        "python": str(tree / ".venv/bin/python3"),
        "path-prefix": str(tree / ".venv/bin"),
    })
    return root


def test_dirty_origin_is_refused_without_creating_a_worktree(origin: Path) -> None:
    (origin / "note.md").write_text("Pending edit\n")
    with pytest.raises(ValueError, match="--allow-dirty-origin"):
        aw.prepare_analysis(origin, name="example")
    assert not (origin / ".commonplace").exists()


def test_dirty_exception_uses_clean_committed_bytes_and_leaves_origin_alone(origin: Path) -> None:
    commit = git(origin, "rev-parse", "HEAD")
    (origin / "note.md").write_text("Pending edit\n")
    git(origin, "add", "note.md")
    (origin / "untracked.md").write_text("Not in the analysis\n")
    before = git(origin, "status", "--porcelain")

    prepared = aw.prepare_analysis(origin, name="example", allow_dirty_origin=True)
    tree = Path(str(prepared["worktree"]))

    assert tree.parent == origin / ".commonplace/worktrees"
    assert prepared["commit"] == commit
    assert prepared["origin-dirty"] is True
    assert prepared["uncommitted-changes-excluded"] is True
    assert prepared["status"] == "ready"
    assert (tree / "note.md").read_text() == "Committed note\n"
    assert not (tree / "untracked.md").exists()
    assert git(tree, "status", "--porcelain") == ""
    assert git(tree, "rev-parse", "--show-toplevel") == str(tree)
    assert git(origin, "status", "--porcelain") == before
    assert json.loads(Path(str(prepared["record"])).read_text()) == prepared


@pytest.mark.parametrize("kind", ["unstaged", "staged", "cancelling", "untracked", "ignored", "skill"])
def test_startup_changes_are_never_omitted(origin: Path, kind: str) -> None:
    changed = origin / "AGENTS.md"
    if kind in {"unstaged", "staged", "cancelling"}:
        changed.write_text("New instructions\n")
        if kind in {"staged", "cancelling"}:
            git(origin, "add", "AGENTS.md")
        if kind == "cancelling":
            changed.write_text("Committed instructions\n")
    elif kind == "skill":
        changed = origin / "kb/instructions/worker/SKILL.md"
        changed.write_text("Modified linked skill\n")
    else:
        changed = origin / ".pi/settings.json"
        changed.parent.mkdir()
        changed.write_text("{}\n")
        if kind == "ignored":
            (origin / ".git/info/exclude").write_text(".pi/\n")
    with pytest.raises(ValueError, match="startup instructions or configuration") as error:
        aw.prepare_analysis(origin, name="example", allow_dirty_origin=True)
    assert changed.relative_to(origin).as_posix() in str(error.value)
    assert not (origin / ".commonplace").exists()


def test_selected_revision_must_match_the_origins_startup_instructions(origin: Path) -> None:
    old = git(origin, "rev-parse", "HEAD")
    (origin / "AGENTS.md").write_text("New committed instructions\n")
    git(origin, "add", "AGENTS.md")
    git(origin, "commit", "--quiet", "-m", "Change startup instructions")
    with pytest.raises(ValueError, match="AGENTS.md"):
        aw.prepare_analysis(origin, name="example", revision=old, allow_dirty_origin=True)


def test_harness_runtime_state_and_readmes_are_not_startup_inputs(origin: Path) -> None:
    for name in (".claude/scheduled_tasks.lock", ".pi/README.md", ".codex/state.sqlite"):
        path = origin / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("Local runtime state or documentation\n")
    prepared = aw.prepare_analysis(origin, name="example", allow_dirty_origin=True)
    assert prepared["status"] == "ready"


def test_an_existing_destination_is_never_reused(origin: Path, tmp_path: Path) -> None:
    destination = tmp_path / "existing"
    destination.mkdir()
    with pytest.raises(ValueError, match="already exists"):
        aw.prepare_analysis(origin, name="example", worktree=destination)


def test_failed_installation_is_recorded_and_never_launched(origin: Path, monkeypatch, capsys) -> None:
    def fail(tree):
        raise ValueError("installation failed")
    monkeypatch.setattr(aw, "_install", fail)
    monkeypatch.chdir(origin)
    assert main(["prepare-analysis", "--name", "example", "--", "must-not-launch"]) == 1
    assert "installation failed" in capsys.readouterr().err
    (record_path,) = (origin / ".commonplace/worktrees").glob("*.preparation.json")
    record = json.loads(record_path.read_text())
    assert record["status"] == "failed"
    assert Path(record["worktree"]).is_dir()


def test_startup_change_during_setup_prevents_launch(origin: Path, monkeypatch, capsys) -> None:
    def changed(tree):
        (origin / "AGENTS.md").write_text("Changed during setup\n")
        return {}
    monkeypatch.setattr(aw, "_install", changed)
    monkeypatch.chdir(origin)
    assert main(["prepare-analysis", "--name", "example", "--", "must-not-launch"]) == 1
    assert "AGENTS.md" in capsys.readouterr().err
    (record_path,) = (origin / ".commonplace/worktrees").glob("*.preparation.json")
    assert json.loads(record_path.read_text())["status"] == "failed"


def test_launcher_binds_cwd_commands_and_committed_agents(origin: Path, monkeypatch, capfd) -> None:
    monkeypatch.chdir(origin)
    monkeypatch.setenv("PYTHONPATH", "/wrong/runtime")
    probe = (
        "import json, os; from pathlib import Path; "
        "print(json.dumps({'cwd': str(Path.cwd()), 'path': os.environ['PATH'], "
        "'pythonpath': os.environ.get('PYTHONPATH'), 'agents': Path('AGENTS.md').read_text()}))"
    )
    assert main(["prepare-analysis", "--name", "example", "--", sys.executable, "-c", probe]) == 0
    lines = capfd.readouterr().out.splitlines()
    prepared = json.loads("\n".join(lines[:-1]))
    child = json.loads(lines[-1])
    assert prepared["agents-md"] == str(Path(prepared["worktree"]) / "AGENTS.md")
    assert child["cwd"] == prepared["worktree"]
    assert child["path"].split(os.pathsep)[0] == prepared["path-prefix"]
    assert child["pythonpath"] is None
    assert child["agents"] == "Committed instructions\n"


def test_command_environment_clears_inherited_python_overrides(tmp_path: Path, monkeypatch) -> None:
    for key in ("PYTHONPATH", "PYTHONHOME", "UV_WORKING_DIR"):
        monkeypatch.setenv(key, "/origin")
    env = aw.command_environment(tmp_path)
    assert all(key not in env for key in ("PYTHONPATH", "PYTHONHOME", "UV_WORKING_DIR"))
    assert env["PATH"].split(os.pathsep)[0] == str(tmp_path / ".venv" / ("Scripts" if os.name == "nt" else "bin"))


@pytest.mark.parametrize("wrong", ["module", "workflow", "validate"])
def test_installation_probe_rejects_a_shared_command_or_package(tmp_path: Path, monkeypatch, wrong: str) -> None:
    # Exercise the installer itself, separately from the real Git preparation tests.
    local_bin = tmp_path / ".venv" / ("Scripts" if os.name == "nt" else "bin")
    found = {
        "module": str(tmp_path / "src/commonplace/lib/agentic_workflow.py"),
        "workflow": str(local_bin / "commonplace-workflow"),
        "validate": str(local_bin / "commonplace-validate"),
    }
    found[wrong] = "/shared/main/runtime"
    monkeypatch.setattr(aw, "_run", lambda args, **kwargs: "" if args[0] == "uv" else json.dumps(found))
    with pytest.raises(ValueError, match="outside"):
        aw._install(tmp_path)
