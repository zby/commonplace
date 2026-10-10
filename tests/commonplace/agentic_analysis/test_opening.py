"""Drive the opening job in local Git fixtures, never an analysis run.

A restricted declaration stops at a test-owned acquisition handler. Its
"acquisition disabled in opening-only fixture" sentinel is fixture-only; the shipped graph is bound.
No workers, external source acquisition, package installation or publication run.
"""

from __future__ import annotations

import os
import shutil

import pytest

from commonplace.artifactrun import worktree
from commonplace.artifactrun.store import RunStore
from commonplace.lib.agentic_analysis import opening
from tests.commonplace.agentic_analysis.execution_fixtures import (
    PARAMETERS,
    ROOT,
    RUN_ID,
    TOKEN,
    assert_stopped,
    git,
    output,
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    prepared as prepared,  # noqa: PLC0414 - explicit fixture registration
)


def test_opening_commits_metadata_then_stops_before_acquisition(prepared):
    c = prepared.start(parameters={**PARAMETERS, "source-revision": "a" * 40})
    c.advance()
    assert_stopped(c, "acquire", "acquisition disabled in opening-only fixture")
    metadata = output(c)
    assert metadata == {
        "run-id": RUN_ID, "system": "Example System",
        "source-identity": "https://github.com/example/system",
        "source": PARAMETERS["source"], "source-revision": "a" * 40,
        "worker": {"profile": "pi-luna", "harness": "pi", "launch-model": "gpt-6-luna", "effort": "medium"},
        "inputs-commit": prepared.commit, "run-date": metadata["run-date"],
        "command-path": str(prepared.repo / ".venv" / ("Scripts" if os.name == "nt" else "bin")),
        "capture-directory": str(c.run_dir / "sources"),
        "review-path": "kb/agentic-system-analyses/retained/system/overview.md",
        "expected-incumbent-sha256": "absent",
    }
    assert len(metadata["run-date"]) == 10
    assert not (prepared.repo / "related-systems").exists()
    assert not (prepared.repo / "kb/agentic-system-analyses/retained").exists()
    assert {p.name for p in (c.run_dir / "artifact").iterdir()} == {"ARTIFACT.yaml"}


@pytest.mark.parametrize("changes,reason", [
    ({"system": " "}, "nonempty system"),
    ({"source-identity": None}, "nonempty source-identity"),
    ({"source": None}, "nonempty source"),
    ({"system": "System\noutput = /not-authorized"}, "system must be a single-line name"),
    ({"source-identity": ""}, "nonempty source-identity"),
    ({"source": ""}, "nonempty source"),
    ({"source-identity": "/"}, "nonempty single-line identity"),
    ({"source-identity": "identity\ninjected"}, "single-line identity"),
    ({"source-identity": "https://github.com/example/sys\ntem"}, "single-line identity"),
    ({"source-revision": "short"}, "full 40-hex Git commit"),
    ({"source-revision": "a" * 40, "source-identity": "local snapshot"}, "requires a GitHub"),
])
def test_opening_refuses_invalid_or_missing_parameters(prepared, changes, reason):
    parameters = {name: value for name, value in {**PARAMETERS, **changes}.items() if value is not None}
    c = prepared.start(parameters=parameters)
    c.advance()
    assert_stopped(c, "open", reason)
    records = RunStore(c.run_dir).attempt_records()
    assert len(records) == 1 and records[0]["state"] == "failed"
    assert not records[0]["pins"] and "outputs" not in records[0]


@pytest.mark.parametrize("changes,reason", [
    (None, "ready worktree preparation record required"),
    ({"status": "failed"}, "does not name a ready worktree"),
    ({"worktree": "/another/worktree"}, "does not name a ready worktree"),
    ({"token": "short"}, "no valid worktree token"),
    ({"token": "b" * 12}, "does not match the source slug"),
    ({"commit": "b" * 40}, "HEAD differs from its preparation commit"),
])
def test_opening_enforces_ready_preparation_binding(prepared, changes, reason):
    if changes is None:
        prepared.preparation.unlink()
    else:
        prepared.record(**changes)
    c = prepared.start()
    c.advance()
    assert_stopped(c, "open", reason)


@pytest.mark.parametrize("name", (
    "AAS-2026-10-07-system-01",
    f"AAS-2026-10-07-wrong-slug-{TOKEN}-01",
    f"AAS-2026-10-07-system-{'b' * 12}-01",
))
def test_opening_requires_the_token_bearing_source_slug_run_id(prepared, name):
    c = prepared.start(name=name)
    c.advance()
    assert_stopped(c, "open", "does not match the source slug and worktree preparation token")


@pytest.mark.parametrize("path,tracked", [
    ("src/commonplace/artifactrun/engine.py", True),
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
    assert_stopped(c, "acquire", "acquisition disabled in opening-only fixture")
    assert output(c)["inputs-commit"] == prepared.commit


def test_opening_checks_the_executing_package_not_only_the_worktree(prepared, monkeypatch):
    other = prepared.repo.with_name("running-package")
    shutil.copytree(prepared.repo, other)
    (other / "src/commonplace/artifactrun/engine.py").write_text("# Different executing code.\n")
    monkeypatch.setattr(worktree, "running_package_root", lambda: other)
    c = prepared.start()
    c.advance()
    assert_stopped(c, "open", "running commonplace source")
    assert "differs from inputs-commit" in c.stop("open").reason
    assert git(prepared.repo, "status", "--porcelain") == ""


def test_opening_refuses_a_library_outside_the_worktree(prepared):
    # Code and working-directory binding: test_worktree::test_run_code_must_be_the_runs_checkout.
    c = prepared.start(library=ROOT / "kb")
    c.advance()
    assert_stopped(c, "open", "recorded library must be the analysis worktree's")


def test_opening_records_the_inspected_incumbent_digest(prepared, monkeypatch):
    calls = []

    def inspect(**arguments):
        calls.append(arguments)
        return {"exists": True, "expected_incumbent_sha256": "c" * 64}

    monkeypatch.setattr(opening, "inspect_destination", inspect)
    c = prepared.start()
    c.advance()
    assert_stopped(c, "acquire", "acquisition disabled in opening-only fixture")
    assert output(c)["expected-incumbent-sha256"] == "c" * 64
    assert calls == [{
        "repo_root": prepared.repo,
        "generated_destination": "kb/agentic-system-analyses/retained/system/overview.md",
        "source_identity": "https://github.com/example/system",
    }]


@pytest.mark.parametrize("change,reason", [
    ("commit", "HEAD changed during opening"),
    ("dirty", "publication requires a clean worktree"),
])
def test_opening_rechecks_the_worktree_after_incumbent_inspection(prepared, monkeypatch, change, reason):
    original = opening.inspect_destination

    def concurrent(**arguments):
        decision = original(**arguments)
        if change == "commit":
            git(prepared.repo, "commit", "--allow-empty", "--quiet", "-m", "Concurrent commit")
        else:
            (prepared.repo / "src/commonplace/artifactrun/engine.py").write_text("# Concurrent modification.\n")
        return decision

    monkeypatch.setattr(opening, "inspect_destination", concurrent)
    c = prepared.start()
    c.advance()
    assert_stopped(c, "open", reason)
    assert all("outputs" not in r for r in RunStore(c.run_dir).attempt_records())
