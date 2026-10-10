"""Exercise the repository hook without recursively running the real suite."""
from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

import pytest

HOOK = Path(__file__).resolve().parents[3] / ".githooks/pre-push"
pytestmark = pytest.mark.skipif(os.name == "nt", reason="Requires a POSIX shell")


def git(repo: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-C", str(repo), *args], check=True, capture_output=True, text=True
    )


@pytest.fixture
def checkout(tmp_path, monkeypatch):
    # A real Git hook inherits repository-local environment variables.
    for name in subprocess.check_output(
        ["git", "rev-parse", "--local-env-vars"], text=True
    ).splitlines():
        monkeypatch.delenv(name, raising=False)
    repo = tmp_path / "repo"
    repo.mkdir()
    git(repo, "init")
    git(repo, "config", "user.name", "Hook Test")
    git(repo, "config", "user.email", "hook@example.invalid")
    git(repo, "config", "commit.gpgsign", "false")
    (repo / "tracked").write_text("baseline\n")
    (repo / ".githooks").mkdir()
    shutil.copy2(HOOK, repo / ".githooks/pre-push")
    git(repo, "add", "tracked", ".githooks/pre-push")
    git(repo, "commit", "-m", "Create test checkout")
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    log = tmp_path / "uv.log"
    uv = bin_dir / "uv"
    uv.write_text(
        '#!/bin/sh\n'
        'printf "%s\\n" "$PWD" "$@" > "$HOOK_TEST_LOG"\n'
        'case "${HOOK_TEST_ACTION:-}" in\n'
        '  dirty) echo changed >> tracked ;;\n'
        '  head) git commit --allow-empty -m changed >/dev/null ;;\n'
        'esac\n'
        'exit "${HOOK_TEST_EXIT:-0}"\n'
    )
    uv.chmod(0o755)
    monkeypatch.setenv("PATH", str(bin_dir) + os.pathsep + os.environ["PATH"])
    monkeypatch.setenv("HOOK_TEST_LOG", str(log))
    return repo, log


def run_hook(repo: Path, cwd: Path | None = None):
    return subprocess.run(
        [str(repo / ".githooks/pre-push"), "origin", "unused"],
        cwd=cwd or repo, input="", capture_output=True, text=True, check=False,
    )


def test_runs_full_suite_from_root(checkout):
    repo, log = checkout
    nested = repo / "nested"
    nested.mkdir()  # Git does not track empty directories.
    result = run_hook(repo, nested)
    assert result.returncode == 0, result.stderr
    assert log.read_text().splitlines() == [str(repo), "run", "pytest", "-m", ""]
    assert "verification passed" in result.stderr


@pytest.mark.parametrize("exit_code", [1, 130])
def test_failure_or_interruption_blocks_push(checkout, monkeypatch, exit_code):
    repo, _ = checkout
    monkeypatch.setenv("HOOK_TEST_EXIT", str(exit_code))
    result = run_hook(repo)
    assert result.returncode == exit_code
    assert "verification passed" not in result.stderr


@pytest.mark.parametrize("state", ["unstaged", "staged", "untracked"])
def test_dirty_checkout_is_rejected_before_tests(checkout, state):
    repo, log = checkout
    path = repo / ("untracked" if state == "untracked" else "tracked")
    path.write_text("changed\n")
    if state == "staged":
        git(repo, "add", "tracked")
    result = run_hook(repo)
    assert result.returncode != 0
    assert "commit or stash" in result.stderr
    assert not log.exists()


@pytest.mark.parametrize("action", ["dirty", "head"])
def test_checkout_changes_during_verification_block_push(checkout, monkeypatch, action):
    repo, _ = checkout
    monkeypatch.setenv("HOOK_TEST_ACTION", action)
    result = run_hook(repo)
    assert result.returncode != 0
    assert "verification blocked" in result.stderr


@pytest.mark.parametrize("exit_code", [0, 1])
def test_git_push_obeys_installed_hook(checkout, monkeypatch, tmp_path, exit_code):
    repo, log = checkout
    remote = tmp_path / "remote.git"
    subprocess.run(["git", "init", "--bare", str(remote)], check=True, capture_output=True)
    git(repo, "config", "core.hooksPath", ".githooks")
    monkeypatch.setenv("HOOK_TEST_EXIT", str(exit_code))
    result = subprocess.run(
        ["git", "-C", str(repo), "push", str(remote), "HEAD:refs/heads/test"],
        capture_output=True, text=True, check=False,
    )
    assert (result.returncode == 0) == (exit_code == 0), result.stderr
    assert log.exists()
    refs = git(remote, "for-each-ref", "--format=%(refname)").stdout
    assert ("refs/heads/test" in refs) == (exit_code == 0)
