"""A completed publication merges once; a stale sibling keeps main intact."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

import pytest

from commonplace.lib.analysis_worktree import integrate_analysis


def git(root: Path, *args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(root), *args], check=True, capture_output=True, text=True
    ).stdout.strip()


def overview(run_id: str, method: str = "") -> str:
    return (
        "---\n"
        f"run-id: {run_id}\n"
        f"inputs-commit: {method}\n"
        "reviewed-boundary: source-123\n"
        "---\n\n# Overview\n"
    )


def prepared_run(origin: Path, method: str, token: str) -> tuple[Path, str]:
    tree = origin / ".commonplace/worktrees" / token
    tree.parent.mkdir(parents=True, exist_ok=True)
    git(origin, "worktree", "add", "--quiet", "--detach", str(tree), method)
    record = {"status": "ready", "worktree": str(tree), "origin": str(origin),
              "commit": method, "token": token}
    tree.with_name(tree.name + ".preparation.json").write_text(json.dumps(record))
    run_id = f"AAS-2026-10-05-example-{token}-01"
    state = tree / "kb/agentic-system-analyses/state" / run_id
    state.mkdir(parents=True)
    destination = "kb/agentic-system-analyses/retained/example/overview.md"
    (state / "run-state.md").write_text(
        "---\n"
        f"run-id: {run_id}\n"
        "run-status: complete\n"
        f"generated-review:\n  path: {destination}\n"
        "---\n\n# Run\n"
    )
    retained = tree / "kb/agentic-system-analyses/retained/example"
    archived = tree / "kb/agentic-system-analyses/retained-archive/AAS-2026-10-04-example-01"
    archived.parent.mkdir(parents=True)
    retained.rename(archived)
    retained.mkdir()
    (retained / "overview.md").write_text(overview(run_id, method))
    (retained / "ARTIFACT.yaml").write_text(f"run: {run_id}\n")
    return state, run_id


def test_replacement_merges_and_stale_sibling_conflicts(tmp_path: Path) -> None:
    origin = tmp_path / "origin"
    origin.mkdir()
    git(origin, "init", "--quiet", "-b", "main")
    git(origin, "config", "user.email", "test@example.com")
    git(origin, "config", "user.name", "Test")
    (origin / ".gitignore").write_text(".commonplace/\nkb/agentic-system-analyses/state/\n")
    retained = origin / "kb/agentic-system-analyses/retained/example"
    retained.mkdir(parents=True)
    (retained / "overview.md").write_text(overview("AAS-2026-10-04-example-01", "old"))
    (retained / "ARTIFACT.yaml").write_text("run: old\n")
    git(origin, "add", ".gitignore", "kb/agentic-system-analyses/retained/example")
    git(origin, "commit", "--quiet", "-m", "Method")
    method = git(origin, "rev-parse", "HEAD")
    first, first_id = prepared_run(origin, method, "a" * 12)
    second, second_id = prepared_run(origin, method, "b" * 12)

    merged = integrate_analysis(first, model="test-model")
    assert merged == git(origin, "rev-parse", "HEAD")
    assert first_id in (retained / "overview.md").read_text()
    assert (origin / "kb/agentic-system-analyses/retained-archive/AAS-2026-10-04-example-01/overview.md").is_file()
    assert git(first.parents[3], "show", "-s", "--format=%B", f"analysis/{first_id}").endswith("Model: test-model")

    before = git(origin, "rev-parse", "HEAD")
    with pytest.raises(ValueError, match="publication branch kept"):
        integrate_analysis(second)
    assert git(origin, "rev-parse", "HEAD") == before
    assert first_id in (retained / "overview.md").read_text()
    assert git(second.parents[3], "rev-parse", f"analysis/{second_id}")
    assert second.is_dir()
    assert not (origin / ".git/MERGE_HEAD").exists()

    third, third_id = prepared_run(origin, method, "c" * 12)
    (third.parents[3] / ".gitignore").write_text("changed startup rules\n")
    with pytest.raises(ValueError, match="tracked changes outside publication paths"):
        integrate_analysis(third)
    assert git(origin, "rev-parse", "HEAD") == before
    assert subprocess.run(
        ["git", "show-ref", "--verify", "--quiet", f"refs/heads/analysis/{third_id}"],
        cwd=origin, check=False,
    ).returncode != 0
