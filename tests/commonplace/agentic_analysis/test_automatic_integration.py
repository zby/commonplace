"""Git effect boundaries over isolated publications; no providers or live runs."""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import threading
from pathlib import Path

import pytest

from commonplace.lib.agentic_analysis import integration as transfer
from commonplace.lib.agentic_analysis import worktree as aw
from tests.commonplace.agentic_analysis.test_integration import git
from tests.commonplace.agentic_analysis.test_integration import (
    proof as proof,  # noqa: PLC0414 - fixture registration
)


@pytest.fixture
def publication(proof, tmp_path):
    origin = proof.root
    tree = tmp_path / "analysis"
    git(origin, "worktree", "add", "--detach", str(tree), proof.method)
    destination = tree / proof.destination.relative_to(origin)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(proof.destination, destination)
    shutil.rmtree(proof.destination)
    proof.run = tree / proof.run.relative_to(origin)
    proof.run.mkdir(parents=True)
    proof.receipt["destination"] = str(destination)
    for name, data in ((aw.PARAMETERS, proof.records.parameters), (aw.OPENING, proof.records.opening),
                       (aw.RECEIPT, proof.receipt)):
        path = proof.run / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data))
    tree.with_name(tree.name + ".preparation.json").write_text(json.dumps({
        "status": "ready", "worktree": str(tree), "origin": str(origin), "commit": proof.method,
        "token": "abcdefabcdef"}))
    proof.tree = tree
    proof.destination = destination
    return proof


@pytest.mark.parametrize("point", ["intent", "branch", "stage", "commit", "commit-record", "merge", "merge-record"])
def test_crash_windows_are_recognized_or_fail_closed(publication, monkeypatch, point):
    p = publication
    original_git, original_save = transfer.git, transfer.save
    triggered = False

    def crash_git(repo, *args, **kwargs):
        nonlocal triggered
        value = original_git(repo, *args, **kwargs)
        command = {"switch": "branch", "add": "stage", "commit": "commit", "merge": "merge"}.get(args[0])
        if command == point and not triggered:
            triggered = True
            raise RuntimeError("simulated controller death after Git effect")
        return value

    def crash_save(path, record):
        nonlocal triggered
        original_save(path, record)
        state = {"pending": "intent", "committed": "commit-record", "integrated": "merge-record"}[record["state"]]
        if state == point and not triggered:
            triggered = True
            raise RuntimeError("simulated controller death after journal effect")

    monkeypatch.setattr(transfer, "git", crash_git)
    monkeypatch.setattr(transfer, "save", crash_save)
    receipt = (p.run / aw.RECEIPT).read_bytes()
    with pytest.raises(RuntimeError, match="simulated controller death"):
        transfer.integrate(p.run, model="initiating-agent")
    assert triggered
    monkeypatch.setattr(transfer, "git", original_git)
    monkeypatch.setattr(transfer, "save", original_save)
    inspection = transfer.inspect_integration(p.run)
    if point == "stage":
        assert inspection["state"] == "operator-attention"
        assert "staged" in inspection["error"]
        with pytest.raises(ValueError, match="staged"):
            transfer.integrate(p.run)
        assert git(p.root, "rev-parse", "main") == p.method
    else:
        merge = transfer.integrate(p.run)
        assert transfer.integrate(p.run) == merge
        assert transfer.inspect_integration(p.run)["state"] == "integrated"
        assert git(p.root, "rev-list", "--count", f"{p.method}..main") == "2"
        assert "Model: initiating-agent" in git(p.tree, "show", "-s", "--format=%B", "HEAD")
        with pytest.raises(ValueError, match="attribution"):
            transfer.integrate(p.run, model="another-agent")
    assert (p.run / aw.RECEIPT).read_bytes() == receipt


def test_unknown_branch_has_no_transfer_authority(publication):
    p = publication
    git(p.tree, "branch", f"analysis/{p.run.name}")
    with pytest.raises(ValueError, match="without integration intent"):
        transfer.integrate(p.run)
    assert not (p.run / transfer.JOURNAL).exists()
    assert git(p.root, "rev-parse", "main") == p.method


@pytest.mark.parametrize("kind", ["filter", "hook"])
def test_git_cannot_change_publication_bytes(publication, kind):
    p = publication
    if kind == "filter":
        git(p.tree, "config", "filter.replace.clean", "printf 'different bytes'")
        git(p.tree, "config", "filter.replace.required", "true")
        (p.root / ".git/info/attributes").write_text("kb/agentic-system-analyses/retained/** filter=replace\n")
    else:
        hook = p.root / ".git/hooks/pre-commit"
        hook.write_text(f"#!/bin/sh\nprintf 'different bytes' > '{p.destination / 'boundary.md'}'\n"
                        f"git add -- '{p.destination / 'boundary.md'}'\n")
        hook.chmod(0o755)
    with pytest.raises(ValueError, match="exact Git bytes"):
        transfer.integrate(p.run)
    assert git(p.root, "rev-parse", "main") == p.method
    assert (p.run / aw.RECEIPT).is_file()
    assert transfer.inspect_integration(p.run)["state"] == "operator-attention"


@pytest.mark.parametrize("state,unsettled,allowed", [
    ("failed", False, True), ("complete", False, True), ("skipped", False, True),
    ("running", False, False), ("interrupted", False, False), ("failed", True, False),
])
def test_audit_content_is_advisory_but_ownership_is_not(publication, monkeypatch, state, unsettled, allowed):
    p = publication
    from commonplace.headless import jobs

    directory = p.run / "audit/snapshot"
    directory.mkdir(parents=True)
    (p.run / "audit/status.json").write_text(json.dumps({"state": state, "directory": str(directory),
                                                        "findings": "adverse"}))
    original = jobs.recorded_calls
    monkeypatch.setattr(jobs, "recorded_calls", lambda root: [{"unsettled": ["orphan"]}] if
                        root == directory and unsettled else original(root))
    if allowed:
        transfer.integrate(p.run)
        assert not (p.root / "audit").exists()
    else:
        with pytest.raises(ValueError, match="ownership"):
            transfer.integrate(p.run)
        assert git(p.root, "rev-parse", "main") == p.method


def test_smudge_filter_cannot_hide_different_origin_checkout_bytes(publication):
    p = publication
    git(p.tree, "config", "filter.smudge-test.clean",
        "python3 -c \"import sys; sys.stdout.buffer.write(sys.stdin.buffer.read().removesuffix(b'SMUDGED'))\"")
    git(p.tree, "config", "filter.smudge-test.smudge", "cat; printf SMUDGED")
    relative = p.destination.relative_to(p.tree).as_posix()
    (p.root / ".git/info/attributes").write_text(f"{relative}/boundary.md filter=smudge-test\n")
    with pytest.raises(ValueError, match="exact origin checkout bytes"):
        transfer.integrate(p.run)
    # Git's normal status hides the reversible working-tree transformation.
    assert git(p.root, "status", "--porcelain") == ""
    assert transfer.inspect_integration(p.run)["state"] == "operator-attention"
    assert (p.run / aw.RECEIPT).is_file()


def test_common_directory_lock_serializes_worktrees_and_manual_transfer(publication):
    p = publication
    entered, finished = threading.Event(), threading.Event()
    failures = []

    def manual():
        entered.set()
        try:
            transfer.integrate(p.run)
        except Exception as exc:  # noqa: BLE001 - rethrow worker failure in test thread
            failures.append(exc)
        finally:
            finished.set()

    with transfer.origin_lock(p.root):
        thread = threading.Thread(target=manual)
        thread.start()
        assert entered.wait(5)
        assert not finished.wait(.2)
        assert git(p.root, "rev-parse", "main") == p.method
    thread.join(10)
    assert not failures and finished.is_set()
    assert transfer.inspect_integration(p.run)["state"] == "integrated"


def test_competing_worktrees_never_merge_two_stale_publications(publication, tmp_path):
    p = publication
    other = tmp_path / "second-tree"
    git(p.root, "worktree", "add", "--detach", str(other), p.method)
    token = "fedcbafedcba"
    run = other / aw.STATE_ROOT / p.run.name.replace("abcdefabcdef", token)
    run.mkdir(parents=True)
    destination = other / p.destination.relative_to(p.tree)
    shutil.copytree(p.destination, destination)
    overview = destination / "overview.md"
    overview.write_bytes(overview.read_bytes().replace(p.run.name.encode(), run.name.encode()))
    from commonplace.lib.agentic_analysis.effects import hashes, tree

    opening = {**p.records.opening, "run-id": run.name}
    receipt = {**p.receipt, "run-id": run.name, "destination": str(destination), "members": hashes(tree(destination))}
    for name, record in ((aw.PARAMETERS, p.records.parameters), (aw.OPENING, opening), (aw.RECEIPT, receipt)):
        path = run / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(record))
    other.with_name(other.name + ".preparation.json").write_text(json.dumps({
        "status": "ready", "worktree": str(other), "origin": str(p.root), "commit": p.method, "token": token}))
    barrier = threading.Barrier(2)
    results, errors = [], []

    def integrate(candidate):
        barrier.wait(timeout=10)
        try:
            results.append(transfer.integrate(candidate))
        except ValueError as error:
            errors.append(str(error))

    threads = [threading.Thread(target=integrate, args=(candidate,)) for candidate in (p.run, run)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join(20)
        assert not thread.is_alive()
    assert len(results) == len(errors) == 1
    assert "origin paths changed" in errors[0]
    assert git(p.root, "rev-list", "--count", f"{p.method}..main") == "2"
    assert git(p.root, "status", "--porcelain") == ""
    assert (p.run / aw.RECEIPT).is_file() and (run / aw.RECEIPT).is_file()


def test_origin_lock_survives_into_orphan_git_child(publication, tmp_path):
    """Use a Git alias to hold an actual mutating-command descendant at a barrier."""
    p = publication
    ready, release = tmp_path / "ready", tmp_path / "release"
    alias = f"!touch {ready}; while ! test -f {release}; do sleep .02; done"
    git(p.root, "config", "alias.wait-fixture", alias)
    root = Path(__file__).resolve().parents[3]
    script = (
        "import sys\nfrom pathlib import Path\n"
        f"sys.path.insert(0, {str(root / 'src')!r})\n"
        "from commonplace.lib.agentic_analysis.integration import origin_lock, git\n"
        f"with origin_lock(Path({str(p.tree)!r})):\n"
        f"    git(Path({str(p.tree)!r}), 'wait-fixture')\n"
    )
    process = subprocess.Popen([sys.executable, "-c", script], start_new_session=True)
    try:
        from tests.commonplace.agentic_analysis.test_automation import wait_for

        wait_for(ready.exists)
        process.kill()
        process.wait(timeout=10)
        import fcntl

        path = p.root / ".git/commonplace-analysis-integration.lock"
        fd = os.open(path, os.O_RDWR)
        try:
            with pytest.raises(BlockingIOError):
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        finally:
            os.close(fd)
    finally:
        release.touch()
        if process.poll() is None:
            process.kill()
        process.wait(timeout=10)
