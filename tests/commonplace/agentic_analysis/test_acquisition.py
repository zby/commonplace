"""Script the acquisition handler with local Git origins and code-only jobs.

Acquisition tests use two code jobs; boundary tests reuse the local-only fixture.
No workers, network sources, target execution, installations or publication.
"""

from __future__ import annotations

import json

import pytest

from commonplace.lib.agentic_analysis import acquisition as agentic_acquisition
from commonplace.lib.agentic_analysis import checkout as agentic_checkout
from commonplace.lib.agentic_analysis.checkout import CheckoutError
from commonplace.workflow.engine import inspect
from commonplace.workflow.store import RunStore
from tests.commonplace.agentic_analysis.execution_fixtures import (
    IDENTITY,
    advance_upstream,
    git,
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    acquisition as acquisition,  # noqa: PLC0414 - explicit fixture registration
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    prepared as prepared_checkout,  # noqa: F401 - shared local fixture
)


def test_checkout_refusal_is_a_domain_value_error_without_side_effects(tmp_path):
    path = tmp_path / "not-a-checkout"
    path.write_bytes(b"keep this file")
    with pytest.raises(CheckoutError, match="not a Git checkout") as raised:
        agentic_checkout.refreeze(path, origin="https://example.invalid/source", revision="a" * 40)
    assert isinstance(raised.value, ValueError)
    assert path.read_bytes() == b"keep this file"


def test_clone_freezes_the_local_default_tip_and_records_the_effect(acquisition):
    start, upstream = acquisition
    revision = advance_upstream(upstream)
    a = start()
    assert not a.advance().stops
    assert a.source() == {"kind": "git", "identity": IDENTITY, "revision": revision,
                          "path": str(a.checkout), "sha256": None}
    assert git(a.checkout, "rev-parse", "HEAD") == revision
    assert git(a.checkout, "rev-parse", "--abbrev-ref", "HEAD") == "HEAD"
    assert git(a.checkout, "status", "--porcelain") == ""
    record = json.loads(a.journal.read_text())
    assert record["state"] == "completed" and record["source"] == a.source()
    assert record["path-existed"] is False and record["initial-head"] is None
    assert len(a.freezes) == 1
    a.advance()
    assert len(a.freezes) == 1, "a completed attempt is not replayed"
    assert not (a.coordinator.run_dir / "output").exists()
    assert not (a.prepared.repo / "kb/agentic-system-analyses/retained").exists()


def test_requested_older_commit_is_frozen_not_the_current_tip(acquisition):
    start, upstream = acquisition
    older = git(upstream, "rev-parse", "HEAD")
    latest = advance_upstream(upstream)
    a = start(revision=older)
    assert not a.advance().stops
    assert a.source()["revision"] == older != latest
    assert not (a.checkout / "NEW.md").exists()


def test_matching_requested_checkout_keeps_its_branch(acquisition):
    start, upstream = acquisition
    revision = git(upstream, "rev-parse", "HEAD")
    a = start(revision=revision)
    a.checkout.parent.mkdir()
    git(a.prepared.repo, "clone", "--quiet", str(upstream), str(a.checkout))
    branch = git(a.checkout, "rev-parse", "--abbrev-ref", "HEAD")
    assert not a.advance().stops
    assert git(a.checkout, "rev-parse", "--abbrev-ref", "HEAD") == branch
    assert a.source()["revision"] == revision


def test_existing_checkout_fetches_and_freezes_the_new_default_tip(acquisition):
    start, upstream = acquisition
    a = start()
    a.checkout.parent.mkdir()
    git(a.prepared.repo, "clone", "--quiet", str(upstream), str(a.checkout))
    initial = git(a.checkout, "rev-parse", "HEAD")
    revision = advance_upstream(upstream)
    assert not a.advance().stops
    assert a.source()["revision"] == revision != initial
    assert json.loads(a.journal.read_text())["initial-head"] == initial


@pytest.mark.parametrize("condition,reason", [
    ("dirty", "local changes or untracked files"),
    ("foreign", "does not have the origin"),
    ("not-git", "not the Git checkout root"),
    ("symlink", "must not redirect"),
])
def test_preflight_failure_changes_no_source_and_records_no_effect(acquisition, condition, reason):
    start, upstream = acquisition
    a = start()
    a.checkout.parent.mkdir()
    if condition == "not-git":
        a.checkout.mkdir()
    elif condition == "symlink":
        a.checkout.symlink_to(upstream, target_is_directory=True)
    else:
        git(a.prepared.repo, "clone", "--quiet", str(upstream), str(a.checkout))
        if condition == "dirty":
            (a.checkout / "KEEP.md").write_bytes(b"Preserve this local change.\n")
        else:
            git(a.checkout, "remote", "set-url", "origin", "/not-the-origin")
    a.advance()
    a.stop(reason)
    assert not a.journal.exists() and not a.freezes
    if condition == "dirty":
        assert (a.checkout / "KEEP.md").read_bytes() == b"Preserve this local change.\n"


def test_unavailable_explicit_commit_is_an_ordinary_retryable_failure(acquisition):
    start, _ = acquisition
    a = start(revision="0" * 40)
    a.advance()
    a.stop("requested commit")
    assert json.loads(a.journal.read_text())["state"] == "started"
    assert not a.checkout.exists()
    a.advance()
    a.stop("requested commit")
    assert len(a.freezes) == 2


def test_interrupted_intent_with_no_installed_checkout_is_safe_to_retry(acquisition, monkeypatch):
    start, _ = acquisition
    a = start()
    original = agentic_acquisition._write_journal

    def interrupt(path, record):
        original(path, record)
        raise KeyboardInterrupt("after intent, before mutation")

    monkeypatch.setattr(agentic_acquisition, "_write_journal", interrupt)
    with pytest.raises(KeyboardInterrupt):
        a.advance()
    assert not a.checkout.exists() and not a.freezes
    monkeypatch.setattr(agentic_acquisition, "_write_journal", original)
    assert not a.advance().stops
    assert len(a.freezes) == 1 and a.source()["kind"] == "git"


@pytest.mark.parametrize("case", ("new-default", "new-requested", "existing-requested"))
def test_interrupted_installation_is_recognized_without_refetching(acquisition, monkeypatch, case):
    start, upstream = acquisition
    initial = git(upstream, "rev-parse", "HEAD")
    if case == "existing-requested":
        revision = advance_upstream(upstream)
        a = start(revision=revision)
        a.checkout.parent.mkdir()
        git(a.prepared.repo, "clone", "--quiet", str(upstream), str(a.checkout))
        git(a.checkout, "checkout", "--quiet", "--detach", initial)
    else:
        revision = initial
        a = start(revision=revision if case == "new-requested" else None)
    original = agentic_acquisition._write_journal

    def interrupt(path, record):
        if record["state"] == "completed":
            raise KeyboardInterrupt("after installation, before completion journal")
        original(path, record)

    monkeypatch.setattr(agentic_acquisition, "_write_journal", interrupt)
    with pytest.raises(KeyboardInterrupt):
        a.advance()
    assert json.loads(a.journal.read_text())["state"] == "started"
    if case != "existing-requested":
        advance_upstream(upstream)  # The installed result, not the new tip, is recognized.
    monkeypatch.setattr(agentic_acquisition, "_write_journal", original)
    assert not a.advance().stops
    assert a.source()["revision"] == revision
    assert len(a.freezes) == 1


def test_interrupted_existing_default_snapshot_stops_as_uncertain(acquisition, monkeypatch):
    start, upstream = acquisition
    a = start()
    a.checkout.parent.mkdir()
    git(a.prepared.repo, "clone", "--quiet", str(upstream), str(a.checkout))
    advance_upstream(upstream)
    original = agentic_acquisition._write_journal

    def interrupt(path, record):
        if record["state"] == "completed":
            raise KeyboardInterrupt("default snapshot not journaled")
        original(path, record)

    monkeypatch.setattr(agentic_acquisition, "_write_journal", interrupt)
    with pytest.raises(KeyboardInterrupt):
        a.advance()
    before = a.journal.read_bytes(), a.checkout.joinpath(".git/HEAD").read_bytes()
    monkeypatch.setattr(agentic_acquisition, "_write_journal", original)
    a.advance()
    stop = a.stop("which default-branch snapshot", uncertain=True)
    assert inspect(a.coordinator.run_dir)["failed_attempts"] == [stop]
    a.advance()
    a.stop("which default-branch snapshot", uncertain=True)
    assert len(a.freezes) == 1
    assert (a.journal.read_bytes(), a.checkout.joinpath(".git/HEAD").read_bytes()) == before


def test_completion_journal_write_failure_is_visible_as_uncertain(acquisition, monkeypatch):
    start, _ = acquisition
    a = start()
    original = agentic_acquisition._write_journal

    def fail_completion(path, record):
        if record["state"] == "completed":
            raise OSError("scripted storage failure")
        original(path, record)

    monkeypatch.setattr(agentic_acquisition, "_write_journal", fail_completion)
    a.advance()
    a.stop("cannot record acquisition completion", uncertain=True)
    assert a.checkout.exists() and json.loads(a.journal.read_text())["state"] == "started"
    monkeypatch.setattr(agentic_acquisition, "_write_journal", original)
    assert not a.advance().stops
    assert a.source()["kind"] == "git" and len(a.freezes) == 1


def test_completed_journal_recovers_a_lost_attempt_without_moving_the_pin(acquisition, monkeypatch):
    start, upstream = acquisition
    a = start()
    revision = git(upstream, "rev-parse", "HEAD")
    original = RunStore.commit_attempt

    def interrupt(self, record, judgments=()):
        if record["job"] == "acquire":
            raise KeyboardInterrupt("after effect completion, before attempt commit")
        return original(self, record, judgments)

    monkeypatch.setattr(RunStore, "commit_attempt", interrupt)
    with pytest.raises(KeyboardInterrupt):
        a.advance()
    assert json.loads(a.journal.read_text())["state"] == "completed"
    assert not any(r["job"] == "acquire" for r in RunStore(a.coordinator.run_dir).attempt_records())
    advance_upstream(upstream)
    monkeypatch.setattr(RunStore, "commit_attempt", original)
    assert not a.advance().stops
    assert a.source()["revision"] == revision and len(a.freezes) == 1


def test_explicit_revision_failure_before_mutation_can_retry_the_original_checkout(acquisition, monkeypatch):
    start, upstream = acquisition
    initial = git(upstream, "rev-parse", "HEAD")
    revision = advance_upstream(upstream)
    a = start(revision=revision)
    a.checkout.parent.mkdir()
    git(a.prepared.repo, "clone", "--quiet", str(upstream), str(a.checkout))
    git(a.checkout, "checkout", "--quiet", "--detach", initial)
    original = agentic_checkout.freeze_checkout
    calls = []

    def fail_once(*args, **kwargs):
        calls.append(kwargs)
        if len(calls) == 1:
            raise RuntimeError("temporary local fixture condition")
        return original(*args, **kwargs)

    monkeypatch.setattr(agentic_checkout, "freeze_checkout", fail_once)
    a.advance()
    a.stop("temporary local fixture condition")
    assert git(a.checkout, "rev-parse", "HEAD") == initial
    assert not a.advance().stops
    assert a.source()["revision"] == revision and len(calls) == 2


def test_an_exception_after_atomic_installation_is_recognized_not_repeated(acquisition, monkeypatch):
    start, upstream = acquisition
    revision = git(upstream, "rev-parse", "HEAD")
    a = start()
    original = agentic_checkout.freeze_checkout

    def install_then_fail(*args, **kwargs):
        original(*args, **kwargs)
        raise RuntimeError("scripted failure after installation")

    monkeypatch.setattr(agentic_checkout, "freeze_checkout", install_then_fail)
    assert not a.advance().stops
    assert a.source()["revision"] == revision
    assert json.loads(a.journal.read_text())["state"] == "completed"


@pytest.mark.parametrize("damage", ("dirty", "missing", "foreign", "symlink", "malformed-journal", "different-inputs"))
def test_recovery_preserves_unverifiable_completed_effects(acquisition, monkeypatch, damage):
    start, _ = acquisition
    a = start()
    original = RunStore.commit_attempt

    def interrupt(self, record, judgments=()):
        if record["job"] == "acquire":
            raise KeyboardInterrupt()
        return original(self, record, judgments)

    monkeypatch.setattr(RunStore, "commit_attempt", interrupt)
    with pytest.raises(KeyboardInterrupt):
        a.advance()
    monkeypatch.setattr(RunStore, "commit_attempt", original)
    if damage == "dirty":
        (a.checkout / "KEEP.md").write_text("Keep this evidence.\n")
    elif damage == "missing":
        a.checkout.rename(a.checkout.with_name("moved-checkout"))
    elif damage == "foreign":
        git(a.checkout, "remote", "set-url", "origin", "/not-the-origin")
    elif damage == "symlink":
        moved = a.checkout.with_name("moved-checkout")
        a.checkout.rename(moved)
        a.checkout.symlink_to(moved, target_is_directory=True)
    elif damage == "malformed-journal":
        a.journal.write_bytes(b"not JSON; preserve me\n")
    else:
        record = json.loads(a.journal.read_text())
        record["metadata-sha256"] = "f" * 64
        a.journal.write_text(json.dumps(record))
    before = a.journal.read_bytes(), a.journal.stat().st_mtime_ns
    a.advance()
    a.stop("AcquisitionUncertainError", uncertain=True)
    assert len(a.freezes) == 1
    assert (a.journal.read_bytes(), a.journal.stat().st_mtime_ns) == before
