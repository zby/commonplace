"""Call the opening and acquisition code jobs in a local prepared checkout.

No workers, external source acquisition, package installation or publication run.
"""

from __future__ import annotations

import json
import shutil

import pytest

from commonplace.lib.agentic_analysis import opening, preparation
from commonplace.lib.agentic_analysis.preparation import RUNTIME_MARKER
from tests.commonplace.agentic_analysis.execution_fixtures import (
    PARAMETERS,
    ROOT,
    RUN_ID,
    TOKEN,
    git,
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    prepared as prepared,  # noqa: PLC0414 - explicit fixture registration
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    prepared_template as prepared_template,  # noqa: PLC0414 - session baseline registration
)

WORKER_PROFILES = "kb/agentic-system-analyses/instructions/analyse-agentic-system/worker-profiles.yaml"


def open_directly(prepared, parameters=PARAMETERS, *, name=RUN_ID, library=None):
    """Open a run named `name` under the prepared checkout's state root; return (metadata, run_dir)."""
    run_dir = prepared.repo / "kb/agentic-system-analyses/state" / name
    run_dir.mkdir(parents=True, exist_ok=True)
    profiles = (prepared.repo / WORKER_PROFILES).read_bytes()
    library = prepared.repo / "kb" if library is None else library
    return opening.open_analysis(parameters, profiles, run_dir, library), run_dir


def test_opening_returns_pinned_metadata_without_acquiring(prepared):
    metadata, _ = open_directly(prepared, {**PARAMETERS, "source-revision": "a" * 40})
    assert metadata.endswith(b"\n")
    record = json.loads(metadata)
    assert record == {
        "run-id": RUN_ID, "system": "Example System",
        "source-identity": "https://github.com/example/system",
        "source": PARAMETERS["source"], "source-revision": "a" * 40,
        "worker": {"profile": "pi-luna", "harness": "pi", "launch-model": "gpt-6-luna", "effort": "medium"},
        "inputs-commit": prepared.commit, "run-date": record["run-date"],
        "review-path": "kb/agentic-system-analyses/retained/example--system/overview.md",
        "expected-incumbent-sha256": "absent",
    }
    assert len(record["run-date"]) == 10
    assert not (prepared.repo / "related-systems").exists()
    assert not (prepared.repo / "kb/agentic-system-analyses/retained").exists()


@pytest.mark.parametrize("changes,reason", [
    ({"system": " "}, "nonempty system"),
    ({"source-identity": None}, "nonempty source-identity"),
    ({"source": None}, "nonempty source"),
    ({"system": "System\noutput = /not-authorized"}, "system must be a single-line name"),
    ({"source-identity": ""}, "nonempty source-identity"),
    ({"source": ""}, "nonempty source"),
    ({"source-identity": "/"}, "nonempty single-line identity"),
    ({"source-identity": " HTTPS://GITHUB.COM/example/system.git/ "},
     "given normalized, as 'https://github.com/example/system'"),
    ({"source-identity": "identity\ninjected"}, "single-line identity"),
    ({"source-identity": "https://github.com/example/sys\ntem"}, "single-line identity"),
    ({"source-revision": "short"}, "full 40-hex Git commit"),
    ({"source-revision": "a" * 40, "source-identity": "local snapshot"}, "requires a GitHub"),
])
def test_opening_refuses_invalid_or_missing_parameters(prepared, changes, reason):
    parameters = {name: value for name, value in {**PARAMETERS, **changes}.items() if value is not None}
    with pytest.raises(ValueError, match=reason):
        open_directly(prepared, parameters)


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
    with pytest.raises(ValueError, match=reason):
        open_directly(prepared)


@pytest.mark.parametrize("name", (
    "AAS-2026-10-07-system-01",
    f"AAS-2026-10-07-wrong-slug-{TOKEN}-01",
    f"AAS-2026-10-07-system-{'b' * 12}-01",
))
def test_opening_requires_the_token_bearing_source_slug_run_id(prepared, name):
    with pytest.raises(ValueError, match="does not match the source slug and worktree preparation token"):
        open_directly(prepared, name=name)


@pytest.mark.parametrize("path,tracked", [
    (RUNTIME_MARKER, True),
    ("kb/untracked.md", False),
])
def test_opening_refuses_an_unpublishable_worktree(prepared, path, tracked):
    target = prepared.repo / path
    old = target.read_bytes() if tracked else None
    target.write_text("Uncommitted method content.\n")
    with pytest.raises(ValueError, match="publication requires a clean worktree"):
        open_directly(prepared)
    if tracked:
        target.write_bytes(old)
    else:
        target.unlink()
    metadata, _ = open_directly(prepared)
    assert json.loads(metadata)["inputs-commit"] == prepared.commit


def test_opening_checks_the_executing_package_not_only_the_worktree(prepared, monkeypatch):
    other = prepared.repo.with_name("running-package")
    shutil.copytree(prepared.repo, other)
    (other / RUNTIME_MARKER).write_text("# Different executing code.\n")
    monkeypatch.setattr(preparation, "running_package_root", lambda: other)
    with pytest.raises(ValueError, match="running commonplace source") as refused:
        open_directly(prepared)
    assert "differs from inputs-commit" in str(refused.value)
    assert git(prepared.repo, "status", "--porcelain") == ""


def test_opening_refuses_a_library_outside_the_worktree(prepared):
    # Code and working-directory binding: test_worktree::test_run_code_must_be_the_runs_checkout.
    with pytest.raises(ValueError, match="recorded library must be the analysis worktree's"):
        open_directly(prepared, library=ROOT / "kb")


def test_opening_records_the_inspected_incumbent_digest(prepared, monkeypatch):
    calls = []

    def inspect(**arguments):
        calls.append(arguments)
        return {"exists": True, "expected_incumbent_sha256": "c" * 64}

    monkeypatch.setattr(opening, "inspect_destination", inspect)
    metadata, _ = open_directly(prepared)
    assert json.loads(metadata)["expected-incumbent-sha256"] == "c" * 64
    assert calls == [{
        "repo_root": prepared.repo,
        "generated_destination": "kb/agentic-system-analyses/retained/example--system/overview.md",
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
            (prepared.repo / RUNTIME_MARKER).write_text("# Concurrent modification.\n")
        return decision

    monkeypatch.setattr(opening, "inspect_destination", concurrent)
    with pytest.raises(ValueError, match=reason):
        open_directly(prepared)


def test_acquire_analysis_returns_a_null_source_for_a_non_git_identity(prepared):
    # Git acquisition from a local origin: test_acquisition.
    opened, run_dir = open_directly(prepared)
    metadata = json.dumps({**json.loads(opened), "source-identity": "local snapshot"}).encode()
    assert opening.acquire_analysis(metadata, run_dir) == b"null\n"
    assert not (prepared.repo / "related-systems").exists()
