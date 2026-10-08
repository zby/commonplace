"""Analysis preparation isolates committed bytes without weakening startup checks."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

from commonplace.cli.run import main as run_main
from commonplace.cli.workflow import main
from commonplace.lib.agentic_analysis import worktree as aw
from commonplace.setrun import isolation as iso


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
        "src/commonplace/workflow/engine.py": "# committed runtime\n",
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
    monkeypatch.setattr(iso, "_install", lambda tree: {
        "python": str(tree / ".venv/bin/python3"),
        "path-prefix": str(tree / ".venv/bin"),
    })
    return root


def test_dirty_origin_is_refused_without_creating_a_worktree(origin: Path) -> None:
    (origin / "note.md").write_text("Pending edit\n")
    with pytest.raises(ValueError, match="--allow-dirty-origin"):
        iso.prepare_worktree(origin, name="example")
    assert not (origin / ".commonplace").exists()


def test_dirty_exception_uses_clean_committed_bytes_and_leaves_origin_alone(origin: Path) -> None:
    commit = git(origin, "rev-parse", "HEAD")
    (origin / "note.md").write_text("Pending edit\n")
    git(origin, "add", "note.md")
    (origin / "untracked.md").write_text("Not in the analysis\n")
    before = git(origin, "status", "--porcelain")

    prepared = iso.prepare_worktree(origin, name="example", allow_dirty_origin=True)
    tree = Path(str(prepared["worktree"]))

    assert tree.parent == origin / ".commonplace/worktrees"
    assert prepared["commit"] == commit
    assert prepared["origin-dirty"] is True
    assert prepared["uncommitted-changes-excluded"] is True
    assert prepared["status"] == "ready"
    assert len(prepared["token"]) == 12
    assert tree.name.endswith("-" + prepared["token"])
    assert iso.preparation_for(tree) == prepared
    assert (tree / "note.md").read_text() == "Committed note\n"
    assert not (tree / "untracked.md").exists()
    assert git(tree, "status", "--porcelain") == ""
    assert git(tree, "rev-parse", "--show-toplevel") == str(tree)
    assert git(origin, "status", "--porcelain") == before
    assert json.loads(Path(str(prepared["record"])).read_text()) == prepared


def _startup_change(origin: Path, kind: str) -> Path | None:
    """Make one local change; return the path a refusal must name, or None if exempt."""
    # A user-wide ignore file must not decide the unignored cases.
    git(origin, "config", "core.excludesFile", "/dev/null")
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
    elif kind in {"untracked", "ignored"}:
        changed = origin / ".pi/settings.json"
        changed.parent.mkdir()
        changed.write_text("{}\n")
        if kind == "ignored":
            (origin / ".git/info/exclude").write_text(".pi/\n")
    elif kind in {"local-settings", "ignored-local-settings"}:
        changed = origin / ".claude/settings.local.json"
        changed.parent.mkdir()
        changed.write_text("{}\n")
        if kind == "ignored-local-settings":
            (origin / ".git/info/exclude").write_text("**/.claude/settings.local.json\n")
            return None
    else:  # Harness runtime state and READMEs are not startup inputs.
        for name in (".claude/scheduled_tasks.lock", ".pi/README.md", ".codex/state.sqlite"):
            path = origin / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("Local runtime state or documentation\n")
        return None
    return changed


@pytest.mark.parametrize("kind", ["unstaged", "staged", "cancelling", "untracked", "ignored", "skill",
                                  "local-settings", "ignored-local-settings", "harness-state"])
def test_startup_changes_are_never_omitted(origin: Path, kind: str) -> None:
    changed = _startup_change(origin, kind)
    if changed is None:
        assert iso.prepare_worktree(origin, name="example", allow_dirty_origin=True)["status"] == "ready"
        return
    with pytest.raises(ValueError, match="startup instructions or configuration") as error:
        iso.prepare_worktree(origin, name="example", allow_dirty_origin=True)
    assert changed.relative_to(origin).as_posix() in str(error.value)
    assert not (origin / ".commonplace").exists()


def test_selected_revision_must_match_the_origins_startup_instructions(origin: Path) -> None:
    old = git(origin, "rev-parse", "HEAD")
    (origin / "AGENTS.md").write_text("New committed instructions\n")
    git(origin, "add", "AGENTS.md")
    git(origin, "commit", "--quiet", "-m", "Change startup instructions")
    with pytest.raises(ValueError, match="AGENTS.md"):
        iso.prepare_worktree(origin, name="example", revision=old, allow_dirty_origin=True)


def test_an_existing_destination_is_never_reused(origin: Path, tmp_path: Path) -> None:
    destination = tmp_path / "existing"
    destination.mkdir()
    with pytest.raises(ValueError, match="already exists"):
        iso.prepare_worktree(origin, name="example", worktree=destination)


def test_override_keeps_a_separate_token_and_rejects_a_foreign_record(origin: Path, tmp_path: Path) -> None:
    destination = tmp_path / "chosen"
    prepared = iso.prepare_worktree(origin, name="example", worktree=destination)
    assert len(prepared["token"]) == 12
    record_path = Path(str(prepared["record"]))
    record = json.loads(record_path.read_text())
    record["worktree"] = str(origin)
    record_path.write_text(json.dumps(record))
    with pytest.raises(ValueError, match="does not name"):
        iso.preparation_for(destination)


def test_analysis_start_allocates_token_without_advancing(origin: Path, tmp_path: Path, monkeypatch) -> None:
    import commonplace.workflow
    from commonplace.lib.agentic_analysis.declaration import JOB_SET

    prepared = iso.prepare_worktree(origin, name="example", worktree=tmp_path / "chosen")
    tree = Path(str(prepared["worktree"]))
    calls = []
    monkeypatch.setattr(aw, "require_run_code", lambda *args, **kwargs: None)
    monkeypatch.setattr(commonplace.workflow, "start_run", lambda *args, **kwargs: calls.append((args, kwargs)))
    monkeypatch.setattr(commonplace.workflow, "advance", lambda *args, **kwargs: pytest.fail("must not advance"))
    params = {"system": "Example", "source_identity": "https://github.com/Example/Repo.git/", "source": "repository"}
    first = aw.start_analysis(tree, **params)
    second = aw.start_analysis(tree, **params)
    assert first.name.endswith(f"-{prepared['token']}-01")
    assert second.name.endswith(f"-{prepared['token']}-02")
    assert calls[0][0] == (first, tree / "kb" / JOB_SET)
    assert calls[0][1]["parameters"]["source-identity"] == "https://github.com/Example/Repo"
    assert list(first.iterdir()) == []


@pytest.mark.parametrize("failure,message", [
    ("installation", "installation failed"), ("startup-change", "AGENTS.md"),
])
def test_failed_setup_is_recorded_and_never_launched(origin: Path, monkeypatch, capsys,
                                                     failure: str, message: str) -> None:
    def install(tree):
        if failure == "installation":
            raise ValueError("installation failed")
        (origin / "AGENTS.md").write_text("Changed during setup\n")
        return {}
    monkeypatch.setattr(iso, "_install", install)
    monkeypatch.chdir(origin)
    assert main(["prepare-analysis", "--name", "example", "--", "must-not-launch"]) == 1
    assert message in capsys.readouterr().err
    (record_path,) = (origin / ".commonplace/worktrees").glob("*.preparation.json")
    record = json.loads(record_path.read_text())
    assert record["status"] == "failed"
    assert Path(record["worktree"]).is_dir()


def test_launcher_binds_cwd_commands_and_committed_agents(origin: Path, monkeypatch, capfd) -> None:
    monkeypatch.chdir(origin)
    for key in ("PYTHONPATH", "PYTHONHOME", "UV_WORKING_DIR"):
        monkeypatch.setenv(key, "/wrong/runtime")
    probe = (
        "import json, os; from pathlib import Path; "
        "print(json.dumps({'cwd': str(Path.cwd()), 'path': os.environ['PATH'], "
        "'pythonpath': os.environ.get('PYTHONPATH'), 'uv': os.environ.get('UV_WORKING_DIR'), "
        "'home': os.environ.get('PYTHONHOME'), "
        "'agents': Path('AGENTS.md').read_text()}))"
    )
    assert main(["prepare-analysis", "--name", "example", "--", sys.executable, "-c", probe]) == 0
    lines = capfd.readouterr().out.splitlines()
    prepared = json.loads("\n".join(lines[:-1]))
    child = json.loads(lines[-1])
    assert prepared["agents-md"] == str(Path(prepared["worktree"]) / "AGENTS.md")
    assert child["cwd"] == prepared["worktree"]
    assert child["path"].split(os.pathsep)[0] == prepared["path-prefix"]
    assert child["pythonpath"] is None and child["uv"] is None and child["home"] is None
    assert child["agents"] == "Committed instructions\n"


@pytest.mark.parametrize("wrong", [None, "module", "workflow", "run", "validate"])
def test_installation_probe_requires_worktree_local_commands(tmp_path: Path, monkeypatch, wrong) -> None:
    # Exercise the installer itself, separately from the real Git preparation tests.
    local_bin = tmp_path / ".venv" / ("Scripts" if os.name == "nt" else "bin")
    found = {
        "module": str(tmp_path / iso.RUNTIME_MARKER),
        "workflow": str(local_bin / "commonplace-workflow"),
        "run": str(local_bin / "commonplace-run"),
        "validate": str(local_bin / "commonplace-validate"),
    }
    if wrong is not None:
        found[wrong] = "/shared/main/runtime"
    monkeypatch.setattr(iso, "run_command", lambda args, **kwargs: "" if args[0] == "uv" else json.dumps(found))
    if wrong is None:
        assert iso._install(tmp_path)["path-prefix"] == str(local_bin)
        return
    with pytest.raises(ValueError, match="outside"):
        iso._install(tmp_path)


def test_implicit_head_behind_the_default_branch_is_refused(origin: Path) -> None:
    git(origin, "branch", "-M", "main")
    first = git(origin, "rev-parse", "HEAD")
    (origin / "note.md").write_text("Later method\n")
    git(origin, "commit", "--quiet", "-am", "Later")
    git(origin, "checkout", "--quiet", "--detach", first)
    with pytest.raises(ValueError, match="1 commits behind main"):
        iso.prepare_worktree(origin, name="example")
    assert not (origin / ".commonplace").exists()
    # A deliberate selection of the same revision is the operator's choice.
    assert iso.prepare_worktree(origin, name="example", revision=first)["commit"] == first


def fake_checkout(root: Path) -> Path:
    marker = root / iso.RUNTIME_MARKER
    marker.parent.mkdir(parents=True)
    marker.write_text("")
    run = root / "kb/agentic-system-analyses/state/AAS-2026-01-01-example-01"
    run.mkdir(parents=True)
    return run


def test_run_code_must_be_the_runs_checkout(tmp_path: Path, monkeypatch, capsys) -> None:
    import commonplace

    # A run outside any source checkout is not bound to one.
    aw.require_run_code(tmp_path / "run", cwd=tmp_path)
    run = fake_checkout(tmp_path / "worktree")
    (tmp_path / "worktree/.venv/bin").mkdir(parents=True)
    with pytest.raises(ValueError, match=r"runs code from .*; run it from .*worktree, calling the command in .*\.venv/bin/"):
        aw.require_run_code(run)
    # The workflow refuses before touching the run.
    monkeypatch.chdir(tmp_path / "worktree")
    assert run_main(["advance", str(run)]) == 1
    assert capsys.readouterr().err.count("runs code from") == 1
    assert list(run.iterdir()) == []

    monkeypatch.setattr(commonplace, "__file__", str(tmp_path / "worktree/src/commonplace/__init__.py"))
    aw.require_run_code(run, cwd=tmp_path / "worktree")
    with pytest.raises(ValueError, match="working directory"):
        aw.require_run_code(run, cwd=tmp_path)


@pytest.mark.parametrize("disposition", ["complete", "blocked", "out-of-scope"])
def test_report_cli_distinguishes_local_completion(tmp_path: Path, monkeypatch, capsys, disposition: str) -> None:
    from hashlib import sha256

    from commonplace.setrun import report

    boundary = f"---\nresult-disposition: {disposition}\n---\n".encode()
    (tmp_path / "set").mkdir()
    (tmp_path / "set" / "boundary.md").write_bytes(boundary)
    monkeypatch.setattr(report, "render_engine_run_report", lambda run, **kw: json.dumps({
        "state": "completed", "set": str(tmp_path / "set"), "members": {"boundary": sha256(boundary).hexdigest()},
        "effects": {"publish": {"verified": False}},
    }))
    assert main(["report-analysis", str(tmp_path)]) == 0
    result = json.loads(capsys.readouterr().out)
    assert result["result-disposition"] == disposition
    assert result["completion"] == ("publication-job-completed" if disposition == "complete" else "local")
    assert result["effects"]["publish"]["verified"] is False

