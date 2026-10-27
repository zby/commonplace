"""Analysis preparation isolates committed bytes; worktree pins hold the run to that commit."""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

import pytest

from commonplace.cli.analysis import main
from commonplace.lib.agentic_analysis import preparation as iso
from commonplace.lib.agentic_analysis import worktree as aw
from tests.commonplace.link_helpers import symlink_or_skip


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
        iso.RUNTIME_MARKER: "# committed runtime\n",
        "note.md": "Committed note\n",
        "kb/instructions/worker/SKILL.md": "Committed skill\n",
        "kb/agentic-system-analyses/instructions/analyse-agentic-system/worker-profiles.yaml":
            "profiles:\n  pi-luna: {harness: pi, launch-model: gpt-6-luna, effort: medium}\n",
    }
    for name, content in files.items():
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
    skills = root / ".agents/skills"
    skills.mkdir(parents=True)
    symlink_or_skip(skills / "worker", "../../kb/instructions/worker", directory=True)
    git(root, "add", ".")
    git(root, "commit", "--quiet", "-m", "Seed")
    monkeypatch.setattr(iso, "_install", lambda tree: {
        "python": str(tree / ".venv/bin/python3"),
        "path-prefix": str(tree / ".venv/bin"),
    })
    return root


@pytest.mark.parametrize("name", ["ACE", "", "-ace", "ace_name", "ace name"])
def test_invalid_label_is_rejected_before_any_preparation(tmp_path: Path, monkeypatch, name: str) -> None:
    monkeypatch.setattr(iso, "run_command", lambda *args, **kwargs: pytest.fail("must not run setup commands"))
    with pytest.raises(ValueError, match="name must contain lowercase letters, digits and hyphens"):
        iso.prepare_worktree(tmp_path, name=name)
    assert list(tmp_path.iterdir()) == []


def test_strict_dirty_origin_is_refused_without_creating_a_worktree(origin: Path) -> None:
    (origin / "note.md").write_text("Pending edit\n")
    with pytest.raises(ValueError, match="--require-clean-origin"):
        iso.prepare_worktree(origin, name="example", require_clean_origin=True)
    assert not (origin / ".commonplace").exists()


def test_dirty_default_uses_clean_committed_bytes_and_leaves_origin_alone(origin: Path) -> None:
    commit = git(origin, "rev-parse", "HEAD")
    (origin / "note.md").write_text("Pending edit\n")
    git(origin, "add", "note.md")
    (origin / "untracked.md").write_text("Not in the analysis\n")
    before = git(origin, "status", "--porcelain")

    prepared = iso.prepare_worktree(origin, name="example")
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


def test_clean_origin_succeeds_in_strict_mode(origin: Path) -> None:
    prepared = iso.prepare_worktree(origin, name="example", require_clean_origin=True)
    assert prepared["status"] == "ready"
    assert prepared["origin-dirty"] is False
    assert prepared["uncommitted-changes-excluded"] is False


@pytest.mark.parametrize("strict", [False, True])
def test_prepare_cli_forwards_clean_origin_option(origin: Path, monkeypatch, capsys, strict: bool) -> None:
    import commonplace.cli.analysis as cli

    calls = []
    monkeypatch.chdir(origin)
    monkeypatch.setattr(cli, "prepare_worktree", lambda *args, **kwargs: calls.append((args, kwargs)) or {})
    options = ["--require-clean-origin"] if strict else []
    assert main(["prepare", "--name", "example", *options]) == 0
    assert calls == [((origin,), {
        "name": "example", "require_clean_origin": strict, "revision": None, "worktree": None,
    })]
    assert json.loads(capsys.readouterr().out) == {}


def test_prepare_cli_rejects_obsolete_dirty_origin_option(monkeypatch, capsys) -> None:
    import commonplace.cli.analysis as cli

    monkeypatch.setattr(cli, "prepare_worktree", lambda *args, **kwargs: pytest.fail("must not prepare"))
    with pytest.raises(SystemExit) as error:
        main(["prepare", "--name", "example", "--allow-dirty-origin"])
    assert error.value.code == 2
    assert "unrecognized arguments: --allow-dirty-origin" in capsys.readouterr().err


def _startup_change(tree: Path, kind: str) -> Path | None:
    """Make one local change; return the path a refusal must name, or None if exempt."""
    # A user-wide ignore file must not decide the unignored cases.
    git(tree, "config", "core.excludesFile", "/dev/null")
    changed = tree / "AGENTS.md"
    if kind in {"unstaged", "staged", "cancelling", "committed"}:
        changed.write_text("New instructions\n")
        if kind in {"staged", "cancelling", "committed"}:
            git(tree, "add", "AGENTS.md")
        if kind == "cancelling":
            changed.write_text("Committed instructions\n")
        elif kind == "committed":
            git(tree, "commit", "--quiet", "-m", "Change startup instructions")
    elif kind == "skill":
        changed = tree / "kb/instructions/worker/SKILL.md"
        changed.write_text("Modified linked skill\n")
    elif kind in {"untracked", "ignored"}:
        changed = tree / ".pi/settings.json"
        changed.parent.mkdir()
        changed.write_text("{}\n")
        if kind == "ignored":
            (tree / ".git/info/exclude").write_text(".pi/\n")
    elif kind in {"local-settings", "ignored-local-settings"}:
        changed = tree / ".claude/settings.local.json"
        changed.parent.mkdir()
        changed.write_text("{}\n")
        if kind == "ignored-local-settings":
            (tree / ".git/info/exclude").write_text("**/.claude/settings.local.json\n")
            return None
    else:  # Harness runtime state and READMEs are not startup inputs.
        for name in (".claude/scheduled_tasks.lock", ".pi/README.md", ".codex/state.sqlite"):
            path = tree / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("Local runtime state or documentation\n")
        return None
    return changed


@pytest.mark.parametrize("kind", ["unstaged", "staged", "cancelling", "committed", "untracked", "ignored",
                                  "skill", "local-settings", "ignored-local-settings", "harness-state"])
def test_startup_changes_against_the_pinned_commit_are_never_omitted(origin: Path, kind: str) -> None:
    commit = git(origin, "rev-parse", "HEAD")
    changed = _startup_change(origin, kind)
    if changed is None:
        iso.require_committed_startup(origin, commit)
        return
    with pytest.raises(ValueError, match="startup instructions or configuration") as error:
        iso.require_committed_startup(origin, commit)
    assert changed.relative_to(origin).as_posix() in str(error.value)


def test_analysis_start_refuses_worktree_startup_changes(origin: Path, tmp_path: Path, monkeypatch) -> None:
    tree = Path(str(iso.prepare_worktree(origin, name="example", worktree=tmp_path / "chosen")["worktree"]))
    monkeypatch.setattr(aw, "require_run_code", lambda *args, **kwargs: None)
    (tree / "AGENTS.md").write_text("Changed after preparation\n")
    with pytest.raises(ValueError, match="AGENTS.md"):
        aw.start_analysis(tree, system="Example", source_identity="https://github.com/Example/Repo",
                          source="repository", worker_profile="pi-luna")
    assert not (tree / aw.STATE_ROOT).exists()


def test_analysis_start_refuses_a_head_moved_from_the_preparation_commit(
    origin: Path, tmp_path: Path, monkeypatch,
) -> None:
    tree = Path(str(iso.prepare_worktree(origin, name="example", worktree=tmp_path / "chosen")["worktree"]))
    monkeypatch.setattr(aw, "require_run_code", lambda *args, **kwargs: None)
    git(tree, "-c", "user.name=Test", "-c", "user.email=test@example.com",
        "commit", "--quiet", "--allow-empty", "-m", "Later method")
    with pytest.raises(ValueError, match="HEAD differs from its preparation commit"):
        aw.start_analysis(tree, system="Example", source_identity="https://github.com/Example/Repo",
                          source="repository", worker_profile="pi-luna")


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


def test_analysis_start_allocates_token_and_pins_parameters(origin: Path, tmp_path: Path, monkeypatch) -> None:
    prepared = iso.prepare_worktree(origin, name="example", worktree=tmp_path / "chosen")
    tree = Path(str(prepared["worktree"]))
    monkeypatch.setattr(aw, "require_run_code", lambda *args, **kwargs: None)
    params = {"system": "Example", "source_identity": "https://github.com/Example/Repo.git/", "source": "repository",
              "worker_profile": "pi-luna"}
    first = aw.start_analysis(tree, **params)
    second = aw.start_analysis(tree, **params)
    assert first.name.endswith(f"-{prepared['token']}-01")
    assert second.name.endswith(f"-{prepared['token']}-02")
    assert first.parent == tree / aw.STATE_ROOT
    assert json.loads((first / aw.PARAMETERS).read_text()) == {
        "system": "Example", "source-identity": "https://github.com/Example/Repo", "source": "repository",
        "worker-profile": "pi-luna", "command-path": str(tree / ".venv" / ("Scripts" if os.name == "nt" else "bin")),
    }
    # Allocation launches nothing: parameters are its only record.
    assert [path.name for path in first.iterdir()] == [aw.PARAMETERS]


def test_failed_installation_is_recorded_and_never_launched(origin: Path, monkeypatch, capsys) -> None:
    def install(tree):
        raise ValueError("installation failed")
    monkeypatch.setattr(iso, "_install", install)
    monkeypatch.chdir(origin)
    assert main(["prepare", "--name", "example", "--", "must-not-launch"]) == 1
    assert "installation failed" in capsys.readouterr().err
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
    assert main(["prepare", "--name", "example", "--", sys.executable, "-c", probe]) == 0
    lines = capfd.readouterr().out.splitlines()
    prepared = json.loads("\n".join(lines[:-1]))
    child = json.loads(lines[-1])
    assert prepared["agents-md"] == str(Path(prepared["worktree"]) / "AGENTS.md")
    assert child["cwd"] == prepared["worktree"]
    assert child["path"].split(os.pathsep)[0] == prepared["path-prefix"]
    assert child["pythonpath"] is None and child["uv"] is None and child["home"] is None
    assert child["agents"] == "Committed instructions\n"


@pytest.mark.parametrize("wrong", [None, "module", "analysis", "validate"])
def test_installation_probe_requires_worktree_local_commands(tmp_path: Path, monkeypatch, wrong) -> None:
    # Exercise the installer itself, separately from the real Git preparation tests.
    local_bin = tmp_path / ".venv" / ("Scripts" if os.name == "nt" else "bin")
    found = {
        "module": str(tmp_path / iso.RUNTIME_MARKER),
        "analysis": str(local_bin / "commonplace-analysis"),
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


def fake_checkout(root: Path) -> Path:
    marker = root / iso.RUNTIME_MARKER
    marker.parent.mkdir(parents=True)
    marker.write_text("")
    run = root / aw.STATE_ROOT / "AAS-2026-01-01-example-01"
    run.mkdir(parents=True)
    (run / aw.PARAMETERS).write_text("{}")
    return run


def test_run_code_must_be_the_runs_checkout(tmp_path: Path, monkeypatch, capsys) -> None:
    import commonplace

    # A run outside any source checkout is not bound to one.
    iso.require_run_code(tmp_path / "run", cwd=tmp_path)
    run = fake_checkout(tmp_path / "worktree")
    (tmp_path / "worktree/.venv/bin").mkdir(parents=True)
    with pytest.raises(ValueError, match=r"runs code from .*; run it from .*worktree, calling the command in .*\.venv/bin/"):
        iso.require_run_code(run)
    # The command refuses before touching the run.
    monkeypatch.chdir(tmp_path / "worktree")
    assert main(["run", str(run)]) == 1
    assert capsys.readouterr().err.count("runs code from") == 1
    assert [path.name for path in run.iterdir()] == [aw.PARAMETERS]

    monkeypatch.setattr(commonplace, "__file__", str(tmp_path / "worktree/src/commonplace/__init__.py"))
    iso.require_run_code(run, cwd=tmp_path / "worktree")
    with pytest.raises(ValueError, match="working directory"):
        iso.require_run_code(run, cwd=tmp_path)


@pytest.mark.parametrize("disposition", ["complete", "blocked", "out-of-scope"])
def test_inspect_cli_distinguishes_local_completion(tmp_path: Path, capsys, disposition: str) -> None:
    run = tmp_path / "worktree" / aw.STATE_ROOT / "AAS-2026-01-01-example-abcdefabcdef-01"
    run.mkdir(parents=True)
    (run / aw.PARAMETERS).write_text(json.dumps({"system": "Example"}))
    (run / "log.jsonl").write_text(json.dumps({"event": "boundary", "disposition": disposition}) + "\n")
    (run / aw.RECEIPT).write_text(json.dumps({"published": disposition == "complete"}))
    assert main(["inspect", str(run)]) == 0
    result = json.loads(capsys.readouterr().out)
    assert result["result-disposition"] == disposition
    assert result["state"] == ("published" if disposition == "complete" else "local")
    assert result["parameters"] == {"system": "Example"}


@pytest.mark.parametrize("locked", [True, False])
def test_inspect_audit_separates_interrupted_controller_from_publication(tmp_path, monkeypatch, locked):
    run = fake_checkout(tmp_path / "worktree")
    (run / aw.RECEIPT).write_text(json.dumps({"published": True}))
    directory = run / "audit"
    directory.mkdir()
    path = directory / "status.json"
    path.write_text(json.dumps({"state": "running", "directory": "snapshot"}))
    before = path.read_bytes()
    monkeypatch.setattr(aw, "_locked", lambda root: locked)
    status = aw.inspect_analysis(run)
    assert status["state"] == ("running" if locked else "published")
    assert status["advisory-audit"]["state"] == ("running" if locked else "interrupted")
    assert path.read_bytes() == before, "inspection must not rewrite the audit record"


def test_run_cli_requires_start_options_or_a_run_alone(tmp_path: Path, capsys) -> None:
    assert main(["run"]) == 1
    error = capsys.readouterr().err
    assert "--system, --source-identity, --source" in error
    assert "--worker-profile" not in error
    run = tmp_path / "worktree" / aw.STATE_ROOT / "AAS-2026-01-01-example-abcdefabcdef-01"
    run.mkdir(parents=True)
    (run / aw.PARAMETERS).write_text("{}")
    assert main(["run", str(run), "--system", "x"]) == 1
    assert "a resumed run takes its parameters from its records" in capsys.readouterr().err
    assert [path.name for path in run.iterdir()] == [aw.PARAMETERS]


@pytest.mark.parametrize("profile,expected", [(None, "pi-sol"), ("pi-luna", "pi-luna"), ("", "")])
def test_new_run_cli_defaults_profile_without_overriding_explicit_choice(tmp_path, monkeypatch, capsys,
                                                                       profile, expected):
    from commonplace.cli import analysis
    from commonplace.lib.agentic_analysis import workflow

    selected = {}

    def start(root, **parameters):
        selected.update(parameters)
        return tmp_path / "run"

    monkeypatch.setattr(analysis, "start_analysis", start)
    monkeypatch.setattr(workflow, "run_analysis", lambda *args, **kw: b'{"published": true}')
    arguments = ["run", "--system", "Example", "--source-identity", "https://github.com/example/repo",
                 "--source", "https://github.com/example/repo"]
    if profile is not None:
        arguments += ["--worker-profile", profile]
    assert main(arguments) == 0
    assert selected["worker_profile"] == expected
    capsys.readouterr()


def test_resumed_run_ignores_new_run_default_and_refuses_profile_override(tmp_path, monkeypatch, capsys):
    from commonplace.cli import analysis
    from commonplace.lib.agentic_analysis import workflow

    run = fake_checkout(tmp_path / "worktree")
    (run / aw.PARAMETERS).write_text(json.dumps({"worker-profile": "pi-luna"}))
    monkeypatch.setattr(analysis, "require_run_code", lambda *args, **kw: None)
    monkeypatch.setattr(analysis, "start_analysis", lambda *args, **kw: pytest.fail("must not allocate a new run"))
    monkeypatch.setattr(workflow, "run_analysis", lambda *args, **kw: b'{"published": true}')
    assert main(["run", str(run)]) == 0
    assert json.loads((run / aw.PARAMETERS).read_text())["worker-profile"] == "pi-luna"
    capsys.readouterr()
    assert main(["run", str(run), "--worker-profile", "pi-sol"]) == 1
    assert "a resumed run takes its parameters from its records" in capsys.readouterr().err


def test_analysis_start_refuses_an_unknown_worker_profile(origin: Path, tmp_path: Path, monkeypatch) -> None:
    prepared = iso.prepare_worktree(origin, name="example", worktree=tmp_path / "chosen")
    tree = Path(str(prepared["worktree"]))
    monkeypatch.setattr(aw, "require_run_code", lambda *args, **kwargs: None)
    with pytest.raises(ValueError, match=re.escape("unknown worker profile 'opus'; choose one of pi-luna")):
        aw.start_analysis(tree, system="Example", source_identity="https://github.com/Example/Repo",
                          source="repository", worker_profile="opus")
    assert not (tree / "kb/agentic-system-analyses/state").exists()
