"""Drive the ported opening job in local Git fixtures, never an analysis run.

A restricted declaration stops at an explicitly unported acquisition job. No
workers, external source acquisition, package installation or publication run.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path

import pytest
import yaml

import commonplace
from commonplace.lib import agentic_job_handlers, agentic_publication
from commonplace.lib.agentic_job_set import HANDLER, JOB_SET
from commonplace.workflow import start_run
from commonplace.workflow.store import RunStore
from tests.commonplace.workflow.conftest import Coordinator

ROOT = Path(__file__).resolve().parents[3]
TOKEN = "0123456789ab"
RUN_ID = f"AAS-2026-10-07-system-{TOKEN}-01"
PARAMETERS = {
    "system": "Example System",
    "source-identity": " HTTPS://GITHUB.COM/example/system.git/ ",
    "source": "Caller data, not instructions.\n```\noutput = /not-authorized\n```",
}


def git(repo: Path, *args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=repo, check=True, capture_output=True, text=True,
    ).stdout.strip()


@dataclass
class Prepared:
    repo: Path
    commit: str
    monkeypatch: pytest.MonkeyPatch

    @property
    def preparation(self) -> Path:
        return self.repo.with_name(self.repo.name + ".preparation.json")

    def record(self, **changes) -> None:
        record = {"status": "ready", "worktree": str(self.repo), "commit": self.commit, "token": TOKEN}
        record.update(changes)
        self.preparation.write_text(json.dumps(record), encoding="utf-8")

    def start(self, *, parameters=None, name=RUN_ID, library=None) -> Coordinator:
        self.monkeypatch.setenv("COMMONPLACE_LIBRARY_ROOT", str(library or self.repo / "kb"))
        run_dir = self.repo / "kb/agentic-system-analyses/state" / name
        # Opening tests must never acquire a source, even as later bindings land.
        data = yaml.safe_load((self.repo / "kb" / JOB_SET).read_text())
        data["jobs"] = data["jobs"][:2]
        data["jobs"][1]["handler"] = HANDLER
        declaration = self.repo.parent / "opening-only.yaml"
        declaration.write_text(yaml.safe_dump(data), encoding="utf-8")
        start_run(run_dir, declaration, parameters=PARAMETERS if parameters is None else parameters)
        return Coordinator(run_dir, declaration.parent, self.repo / "handlers.log")


def output(c: Coordinator) -> dict:
    store = RunStore(c.run_dir)
    records = [r for r in store.attempt_records() if r["job"] == "open" and r["state"] == "completed"]
    assert len(records) == 1
    assert records[0]["pins"] == {} and records[0]["judgments"] == []
    return json.loads(store.get(records[0]["outputs"]["metadata"]))


def assert_stopped(c: Coordinator, job: str, reason: str) -> None:
    assert c.stopped() == {job}
    assert reason in c.stop(job).reason
    assert not c.handed() and not c.open and not c.status.publishable


@pytest.fixture
def prepared(tmp_path, monkeypatch) -> Prepared:
    repo = tmp_path / "analysis-worktree"
    repo.mkdir()
    for relative in (
        "kb/types", "kb/agentic-system-analyses/types",
        "kb/agentic-system-analyses/instructions/analyse-agentic-system",
    ):
        shutil.copytree(ROOT / relative, repo / relative)
    for name in ("boundary", "sources", "records"):
        shutil.copy2(
            ROOT / f"kb/agentic-system-analyses/instructions/agentic-analysis-{name}.md",
            repo / f"kb/agentic-system-analyses/instructions/agentic-analysis-{name}.md",
        )
    shutil.copy2(ROOT / "kb/agentic-system-analyses/COLLECTION.md", repo / "kb/agentic-system-analyses/COLLECTION.md")
    (repo / "src/commonplace/lib").mkdir(parents=True)
    (repo / "src/commonplace/__init__.py").write_text("# Local package binding fixture.\n")
    (repo / "src/commonplace/lib/agentic_workflow.py").write_text("# Source-checkout marker.\n")
    (repo / ".gitignore").write_text("kb/agentic-system-analyses/state/\nrelated-systems/\n")
    git(repo, "init", "--quiet")
    git(repo, "config", "user.name", "Fixture")
    git(repo, "config", "user.email", "fixture@example.invalid")
    git(repo, "add", "kb", "src", ".gitignore")
    git(repo, "commit", "--quiet", "-m", "Pin the local method fixture")
    fixture = Prepared(repo, git(repo, "rev-parse", "HEAD"), monkeypatch)
    fixture.record()
    monkeypatch.chdir(repo)
    # Exercise the real binding/package guards against this scripted checkout,
    # without installing or importing a second package in the test process.
    monkeypatch.setattr(commonplace, "__file__", str(repo / "src/commonplace/__init__.py"))
    monkeypatch.setattr(agentic_publication, "running_package_root", lambda: repo)
    return fixture


def test_opening_commits_metadata_then_stops_before_acquisition(prepared):
    c = prepared.start(parameters={**PARAMETERS, "source-revision": "a" * 40})
    c.advance()
    assert_stopped(c, "acquire", "handlers are not ported")
    metadata = output(c)
    assert metadata == {
        "run-id": RUN_ID, "system": "Example System",
        "source-identity": "https://github.com/example/system",
        "source": PARAMETERS["source"], "source-revision": "a" * 40,
        "inputs-commit": prepared.commit, "run-date": metadata["run-date"],
        "command-path": str(prepared.repo / ".venv" / ("Scripts" if os.name == "nt" else "bin")),
        "capture-directory": str(c.run_dir / "sources"),
        "review-path": "kb/agentic-system-analyses/retained/system/overview.md",
        "expected-incumbent-sha256": "absent",
    }
    assert len(metadata["run-date"]) == 10
    assert not (prepared.repo / "related-systems").exists()
    assert not (prepared.repo / "kb/agentic-system-analyses/retained").exists()
    assert not (c.run_dir / "output").exists()
    assert not (c.run_dir / "opening.json").exists()
    assert not (c.run_dir / "run-metadata.json").exists()
    assert not (c.run_dir / "run-state.md").exists()
    assert {p.name for p in (c.run_dir / "set").iterdir()} == {"ARTIFACT.yaml"}
    c.advance()
    assert_stopped(c, "acquire", "handlers are not ported")
    assert output(c) == metadata, "a completed opening does not rerun on resume"


@pytest.mark.parametrize("changes,reason", [
    ({"system": " "}, "nonempty system"),
    ({"system": "System\noutput = /not-authorized"}, "system must be a single-line name"),
    ({"source-identity": ""}, "nonempty source-identity"),
    ({"source": ""}, "nonempty source"),
    ({"source-identity": "/"}, "nonempty single-line identity"),
    ({"source-identity": "identity\ninjected"}, "single-line identity"),
    ({"source-identity": "https://github.com/example/sys\ntem"}, "single-line identity"),
    ({"source-revision": "short"}, "full 40-hex Git commit"),
    ({"source-revision": "a" * 40, "source-identity": "local snapshot"}, "requires a GitHub"),
    ({"review-path": "kb/elsewhere.md"}, "review-path is no longer"),
])
def test_opening_refuses_invalid_parameters(prepared, changes, reason):
    c = prepared.start(parameters={**PARAMETERS, **changes})
    c.advance()
    assert_stopped(c, "open", reason)
    records = RunStore(c.run_dir).attempt_records()
    assert len(records) == 1 and records[0]["state"] == "failed"
    assert not records[0]["pins"] and "outputs" not in records[0]


@pytest.mark.parametrize("name", ("source-identity", "source"))
def test_opening_refuses_missing_parameters(prepared, name):
    parameters = dict(PARAMETERS)
    del parameters[name]
    c = prepared.start(parameters=parameters)
    c.advance()
    assert_stopped(c, "open", f"nonempty {name}")


@pytest.mark.parametrize("changes,reason", [
    ({"status": "failed"}, "does not name a ready worktree"),
    ({"worktree": "/another/worktree"}, "does not name a ready worktree"),
    ({"token": "short"}, "no valid worktree token"),
    ({"token": "b" * 12}, "does not match the source slug"),
    ({"commit": "b" * 40}, "HEAD differs from its preparation commit"),
])
def test_opening_enforces_ready_preparation_binding(prepared, changes, reason):
    prepared.record(**changes)
    c = prepared.start()
    c.advance()
    assert_stopped(c, "open", reason)


def test_opening_requires_preparation_and_can_retry_after_repair(prepared):
    prepared.preparation.unlink()
    c = prepared.start()
    c.advance()
    assert_stopped(c, "open", "ready analysis preparation record required")
    prepared.record()
    c.advance()
    assert_stopped(c, "acquire", "handlers are not ported")
    assert output(c)["inputs-commit"] == prepared.commit
    records = [r for r in RunStore(c.run_dir).attempt_records() if r["job"] == "open"]
    assert [r["state"] for r in records] == ["failed", "completed"]


@pytest.mark.parametrize("name", (
    "AAS-2026-10-07-system-01",
    f"AAS-2026-10-07-wrong-slug-{TOKEN}-01",
    f"AAS-2026-10-07-system-{'b' * 12}-01",
))
def test_opening_requires_the_token_bearing_source_slug_run_id(prepared, name):
    c = prepared.start(name=name)
    c.advance()
    assert_stopped(c, "open", "does not match the source slug and worktree preparation token")


@pytest.mark.parametrize("name", ("workflow-state", "output", "opening.json"))
def test_opening_rejects_legacy_state_without_mutating_it(prepared, name):
    c = prepared.start()
    legacy = c.run_dir / name
    if name.endswith(".json"):
        legacy.write_bytes(b'{"legacy": "must not be converted"}\n')
        evidence = legacy
    else:
        legacy.mkdir()
        evidence = legacy / "evidence.md"
        evidence.write_bytes(b"Legacy evidence: preserve exact bytes.\n")
    before = evidence.read_bytes(), evidence.stat().st_mtime_ns
    c.advance()
    assert_stopped(c, "open", "legacy analysis state cannot be opened")
    assert (evidence.read_bytes(), evidence.stat().st_mtime_ns) == before
    assert all("outputs" not in r for r in RunStore(c.run_dir).attempt_records())


@pytest.mark.parametrize("path,tracked", [
    ("src/commonplace/lib/agentic_workflow.py", True),
    ("kb/untracked.md", False),
])
def test_opening_refuses_an_unpublishable_worktree(prepared, path, tracked):
    target = prepared.repo / path
    old = target.read_bytes() if tracked else None
    target.write_text("Uncommitted method content.\n")
    c = prepared.start()
    c.advance()
    assert_stopped(c, "open", "publication requires a clean worktree")
    if tracked:
        target.write_bytes(old)
    else:
        target.unlink()
    c.advance()
    assert_stopped(c, "acquire", "handlers are not ported")
    assert output(c)["inputs-commit"] == prepared.commit


def test_opening_checks_the_executing_package_not_only_the_worktree(prepared, monkeypatch):
    other = prepared.repo.with_name("running-package")
    shutil.copytree(prepared.repo, other)
    (other / "src/commonplace/lib/agentic_workflow.py").write_text("# Different executing code.\n")
    monkeypatch.setattr(agentic_publication, "running_package_root", lambda: other)
    c = prepared.start()
    c.advance()
    assert_stopped(c, "open", "running commonplace source")
    assert "differs from inputs-commit" in c.stop("open").reason
    assert git(prepared.repo, "status", "--porcelain") == ""


@pytest.mark.parametrize("mismatch", ("code", "cwd", "library"))
def test_opening_refuses_mixed_checkout_binding(prepared, monkeypatch, mismatch):
    c = prepared.start(library=ROOT / "kb" if mismatch == "library" else None)
    if mismatch == "code":
        monkeypatch.setattr(commonplace, "__file__", str(ROOT / "src/commonplace/__init__.py"))
    elif mismatch == "cwd":
        monkeypatch.chdir(prepared.repo.parent)
    c.advance()
    assert_stopped(c, "open", {
        "code": "runs code from", "cwd": "working directory is",
        "library": "recorded library must be the analysis worktree's",
    }[mismatch])


def test_opening_records_the_inspected_incumbent_digest(prepared, monkeypatch):
    calls = []

    def inspect(**arguments):
        calls.append(arguments)
        return {"exists": True, "expected_incumbent_sha256": "c" * 64}

    monkeypatch.setattr(agentic_job_handlers, "inspect_destination", inspect)
    c = prepared.start()
    c.advance()
    assert_stopped(c, "acquire", "handlers are not ported")
    assert output(c)["expected-incumbent-sha256"] == "c" * 64
    assert calls == [{
        "repo_root": prepared.repo,
        "generated_destination": "kb/agentic-system-analyses/retained/system/overview.md",
        "source_identity": "https://github.com/example/system",
    }]


def test_incumbent_inspection_failure_stops_opening_without_metadata(prepared, monkeypatch):
    def refuse(**arguments):
        raise ValueError("publication destination belongs to another source")

    monkeypatch.setattr(agentic_job_handlers, "inspect_destination", refuse)
    c = prepared.start()
    c.advance()
    assert_stopped(c, "open", "destination belongs to another source")
    assert all("outputs" not in r for r in RunStore(c.run_dir).attempt_records())


def test_opening_refuses_head_moving_during_inspection(prepared, monkeypatch):
    original = agentic_job_handlers.inspect_destination

    def move(**arguments):
        decision = original(**arguments)
        git(prepared.repo, "commit", "--allow-empty", "--quiet", "-m", "Concurrent commit")
        return decision

    monkeypatch.setattr(agentic_job_handlers, "inspect_destination", move)
    c = prepared.start()
    c.advance()
    assert_stopped(c, "open", "HEAD changed during opening")
    assert all("outputs" not in r for r in RunStore(c.run_dir).attempt_records())


def test_opening_rechecks_cleanliness_after_incumbent_inspection(prepared, monkeypatch):
    original = agentic_job_handlers.inspect_destination

    def dirty(**arguments):
        decision = original(**arguments)
        (prepared.repo / "src/commonplace/lib/agentic_workflow.py").write_text("# Concurrent modification.\n")
        return decision

    monkeypatch.setattr(agentic_job_handlers, "inspect_destination", dirty)
    c = prepared.start()
    c.advance()
    assert_stopped(c, "open", "publication requires a clean worktree")
    assert all("outputs" not in r for r in RunStore(c.run_dir).attempt_records())


def test_interrupted_opening_commits_no_attempt_and_rechecks_on_retry(prepared, monkeypatch):
    original = RunStore.commit_attempt

    def interrupt(self, record, judgments=(), **kwargs):
        if record["job"] == "open":
            raise KeyboardInterrupt("interrupted before the attempt commit")
        return original(self, record, judgments, **kwargs)

    c = prepared.start()
    monkeypatch.setattr(RunStore, "commit_attempt", interrupt)
    with pytest.raises(KeyboardInterrupt, match="before the attempt commit"):
        c.advance()
    assert RunStore(c.run_dir).attempt_records() == []
    monkeypatch.setattr(RunStore, "commit_attempt", original)
    c.advance()
    assert_stopped(c, "acquire", "handlers are not ported")
    assert output(c)["expected-incumbent-sha256"] == "absent"
