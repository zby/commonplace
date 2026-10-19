"""Scripted completion evidence and temporary Git fixtures, not real analyses."""
from __future__ import annotations

import json
import shutil
import subprocess
from hashlib import sha256
from pathlib import Path
from types import SimpleNamespace

import pytest

from commonplace.artifactrun import effects
from commonplace.lib.agentic_analysis import publication
from commonplace.lib.agentic_analysis import worktree as aw
from commonplace.lib.agentic_analysis.plan import PLAN


def git(root: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(root), *args], check=True,
                          capture_output=True, text=True).stdout.strip()


@pytest.fixture
def proof(tmp_path):
    """The run's records are scripted; tree checks use real bytes."""
    root = tmp_path / "repo"
    root.mkdir()
    git(root, "init", "-b", "main")
    git(root, "config", "user.email", "test@example.com")
    git(root, "config", "user.name", "Test")
    (root / ".gitignore").write_text("kb/agentic-system-analyses/state/\n")
    declaration = root / "kb" / PLAN
    declaration.parent.mkdir(parents=True)
    declaration.write_text("scripted declaration\n")
    (root / "kb/type.md").write_text("scripted type\n")
    git(root, "add", ".")
    git(root, "commit", "-m", "Fixture method")
    method = git(root, "rev-parse", "HEAD")
    run = root / aw.STATE_ROOT / "AAS-2026-01-01-example-abcdefabcdef-01"
    run.mkdir(parents=True)
    destination = root / aw.RETAINED_ROOT / "example"
    destination.mkdir(parents=True)
    files = {"overview.md": (f"---\nrun-id: {run.name}\ninputs-commit: {method}\n"
                             "result-disposition: complete\nreviewed-boundary: revision\n---\n").encode(),
             "ARTIFACT.yaml": b"fixture manifest\n", "boundary.md": b"fixture boundary\n"}
    for name, data in files.items():
        (destination / name).write_bytes(data)
    parameters = {"system": "Example", "source": "fixture", "source-identity": "identity",
                  "worker-profile": "pi-luna", "command-path": "/commands"}
    pins = {name: parameters[name] for name in ("system", "source-identity", "source")}
    opening = {"run-id": run.name, "inputs-commit": method, **pins, "source-revision": None,
               "review-path": str(destination), "expected-incumbent-sha256": "absent"}
    receipt = {"published": True, "destination": str(destination), "members": effects.hashes(files),
               "run-id": run.name, "inputs-commit": method, **pins, "source-revision": None,
               "expected-incumbent-sha256": "absent"}
    records = SimpleNamespace(parameters=parameters, opening=opening, receipt=receipt)
    return SimpleNamespace(root=root, method=method, run=run, destination=destination,
                           files=files, records=records, receipt=receipt)


def write_records(proof):
    """Write the run's current records; a record set to None is absent."""
    for path, record in ((aw.PARAMETERS, proof.records.parameters), (aw.OPENING, proof.records.opening),
                         (aw.RECEIPT, proof.records.receipt)):
        target = proof.run / path
        target.unlink(missing_ok=True)
        if record is not None:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(json.dumps(record))


def verify(proof):
    write_records(proof)
    return aw._integration_publication(proof.run, proof.root, proof.method)


def test_exact_publication_proof_is_read_only(proof):
    assert verify(proof) == ([proof.destination.relative_to(proof.root).as_posix()], "revision")
    assert git(proof.root, "diff", "--cached", "--name-only") == ""


@pytest.mark.parametrize("change", ["changed", "extra", "missing", "symlink", "manifest"])
def test_exact_retained_tree_required(proof, change):
    path = proof.destination / ("ARTIFACT.yaml" if change == "manifest" else "boundary.md")
    if change == "missing":
        path.unlink()
    elif change == "extra":
        (proof.destination / "extra.md").write_text("unowned")
    elif change == "symlink":
        path.unlink()
        path.symlink_to(proof.destination / "overview.md")
    else:
        path.write_text("changed")
    with pytest.raises((ValueError, publication.UncertainEffectError)):
        verify(proof)
    assert git(proof.root, "diff", "--cached", "--name-only") == ""


@pytest.mark.parametrize("case", ["no-receipt", "no-opening", "local", "receipt-run-id",
                                  "receipt-method", "opening-method", "receipt-pins"])
def test_publication_records_are_required(proof, case):
    if case == "no-receipt":
        proof.records.receipt = None
    elif case == "no-opening":
        proof.records.opening = None
    elif case == "local":
        proof.records.receipt = {"published": False}
    elif case == "receipt-run-id":
        proof.receipt["run-id"] = "AAS-2026-01-01-example-abcdefabcdef-02"
    elif case == "receipt-method":
        proof.receipt["inputs-commit"] = "0" * 40
    elif case == "opening-method":
        proof.records.opening["inputs-commit"] = "0" * 40
    else:
        proof.receipt["source"] = "a different source"
    with pytest.raises(ValueError):
        verify(proof)


def test_archive_must_equal_the_git_incumbent(proof):
    old_id = "AAS-2025-01-01-example-01"
    old = {"overview.md": f"---\nrun-id: {old_id}\n---\n".encode(), "boundary.md": b"old boundary\n"}
    for path in proof.destination.iterdir():
        path.unlink()
    for name, data in old.items():
        (proof.destination / name).write_bytes(data)
    git(proof.root, "add", str(proof.destination))
    git(proof.root, "commit", "-m", "Fixture incumbent")
    proof.method = git(proof.root, "rev-parse", "HEAD")
    proof.receipt["inputs-commit"] = proof.method
    proof.records.opening["inputs-commit"] = proof.method
    proof.receipt["expected-incumbent-sha256"] = sha256(old["overview.md"]).hexdigest()
    proof.files["overview.md"] = (f"---\nrun-id: {proof.run.name}\ninputs-commit: {proof.method}\n"
                                  "result-disposition: complete\nreviewed-boundary: revision\n---\n").encode()
    archive = proof.root / aw.ARCHIVE_ROOT / old_id
    archive.parent.mkdir(parents=True)
    proof.destination.rename(archive)
    proof.destination.mkdir()
    for name, data in proof.files.items():
        (proof.destination / name).write_bytes(data)
    proof.receipt["members"] = effects.hashes(proof.files)
    assert len(verify(proof)[0]) == 2
    (archive / "boundary.md").write_bytes(b"changed archive")
    with pytest.raises(ValueError, match="exact incumbent"):
        verify(proof)


@pytest.mark.parametrize("case", ["success", "staged", "outside", "dirty-origin", "stale-origin", "conflict"])
def test_integration_git_actions_are_scoped_and_merge(proof, monkeypatch, tmp_path, case):
    """Exercise Git transfer separately from the proof fixture; no real publication."""
    origin = proof.root
    tree = tmp_path / "analysis"
    git(origin, "worktree", "add", "--detach", str(tree), proof.method)
    destination = tree / proof.destination.relative_to(origin)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(proof.destination, destination)
    shutil.rmtree(proof.destination)
    run = tree / proof.run.relative_to(origin)
    run.mkdir(parents=True)
    (run / aw.PARAMETERS).write_text(json.dumps(proof.records.parameters))
    preparation = {"status": "ready", "worktree": str(tree), "origin": str(origin),
                   "commit": proof.method, "token": "abcdefabcdef"}
    tree.with_name(tree.name + ".preparation.json").write_text(json.dumps(preparation))
    monkeypatch.setattr(aw, "require_run_code", lambda *args, **kwargs: None)
    monkeypatch.setattr(aw, "_integration_publication", lambda *args: ([destination.relative_to(tree).as_posix()], "revision"))
    if case == "staged":
        git(tree, "add", str(destination))
    elif case == "outside":
        (tree / "kb/type.md").write_text("unexpected method change")
    elif case == "dirty-origin":
        (origin / "kb/type.md").write_text("operator work")
    elif case == "stale-origin":
        target = origin / destination.relative_to(tree)
        target.mkdir(parents=True)
        (target / "overview.md").write_text("newer publication")
        git(origin, "add", str(target))
        git(origin, "commit", "-m", "Fixture concurrent publication")
    elif case == "conflict":
        real_run = subprocess.run

        def concurrent_merge(args, **kwargs):
            if args[:3] == ["git", "merge", "--no-ff"]:
                target = origin / destination.relative_to(tree)
                target.mkdir(parents=True)
                (target / "overview.md").write_text("racing publication")
                git(origin, "add", str(target))
                git(origin, "commit", "-m", "Fixture racing publication")
            return real_run(args, **kwargs)

        monkeypatch.setattr(subprocess, "run", concurrent_merge)
    if case != "success":
        before = git(tree, "diff", "--cached", "--name-only")
        with pytest.raises(ValueError):
            aw.integrate_analysis(run)
        if case == "conflict":
            assert not (origin / ".git/MERGE_HEAD").exists()
            assert git(tree, "branch", "--show-current") == f"analysis/{run.name}"
        else:
            assert git(tree, "diff", "--cached", "--name-only") == before
            assert git(tree, "branch", "--show-current") == ""
        return
    result = aw.integrate_analysis(run)
    assert result == git(origin, "rev-parse", "HEAD")
    assert (origin / destination.relative_to(tree) / "overview.md").read_bytes() == proof.files["overview.md"]
    changed = git(tree, "diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD").splitlines()
    assert changed and all(name.startswith(destination.relative_to(tree).as_posix() + "/") for name in changed)


def test_a_real_compact_plan_s_fixed_identity_names_the_shipped_file(tmp_path, monkeypatch):
    """The run fixes the expansion; integration compares the plan file the operator shipped."""
    from commonplace.artifactrun import inspect, start_run
    from commonplace.artifactrun.engine import library_root

    library = Path(__file__).resolve().parents[3] / "kb"
    monkeypatch.setattr("commonplace.artifactrun.engine.library_root", lambda: library)
    assert library_root() == library
    run = tmp_path / "run"
    start_run(run, library / PLAN, parameters={"system": "x", "source": "y", "source-identity": "z", "command-path": "/c"})
    fixed = inspect(run)["declaration"]
    shipped = library / PLAN
    assert fixed["plan"] == str(shipped.resolve())
    assert fixed["plan_sha256"] == sha256(shipped.read_bytes()).hexdigest()
    assert fixed["declaration_sha256"] != fixed["plan_sha256"], "the fixed declaration is the expansion, not the file"
