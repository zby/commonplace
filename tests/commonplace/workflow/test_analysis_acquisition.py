"""Script the acquisition handler with local Git origins and code-only jobs.

Acquisition tests use two code jobs; boundary tests reuse the local-only fixture.
No workers, network sources, target execution, installations or publication.
"""

from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

import pytest
import yaml

from commonplace.lib import agentic_acquisition, agentic_checkout
from commonplace.lib.agentic_acquisition import JOURNAL
from commonplace.lib.agentic_job_set import (
    ACQUIRE_HANDLER,
    ANALYST_CHECK_HANDLERS,
    BOUNDARY_CHECK_HANDLER,
    JOB_SET,
)
from commonplace.workflow import start_run
from commonplace.workflow.engine import inspect
from commonplace.workflow.store import RunStore
from tests.commonplace.workflow.conftest import Coordinator
from tests.commonplace.workflow.test_analysis_opening import (
    PARAMETERS,
    RUN_ID,
    Prepared,
    git,
)
from tests.commonplace.workflow.test_analysis_opening import (
    prepared as prepared_checkout,  # noqa: F401 - shared local fixture
)

IDENTITY = "https://github.com/example/system"


@dataclass
class Acquisition:
    prepared: Prepared
    upstream: Path
    coordinator: Coordinator
    freezes: list[dict] = field(default_factory=list)

    @property
    def checkout(self) -> Path:
        return self.prepared.repo / "related-systems/example--system"

    @property
    def journal(self) -> Path:
        return self.coordinator.run_dir / JOURNAL

    def source(self):
        store = RunStore(self.coordinator.run_dir)
        records = [r for r in store.attempt_records() if r["job"] == "acquire" and r["state"] == "completed"]
        assert len(records) == 1
        return json.loads(store.get(records[0]["outputs"]["source"]))

    def advance(self):
        status = self.coordinator.advance()
        assert not status.handouts and not status.open_attempts and not status.publishable
        return status

    def stop(self, reason, *, uncertain=False):
        (stop,) = self.coordinator.status.stops
        assert stop.job == "acquire" and reason in stop.reason and stop.uncertain is uncertain
        return stop


def advance_upstream(upstream: Path) -> str:
    (upstream / "NEW.md").write_text("New local fixture revision.\n")
    git(upstream, "add", "NEW.md")
    git(upstream, "commit", "--quiet", "-m", "Advance the local source")
    return git(upstream, "rev-parse", "HEAD")


@pytest.fixture
def acquisition(request, monkeypatch, tmp_path):
    prepared = request.getfixturevalue("prepared_checkout")
    upstream = tmp_path / "local-upstream"
    upstream.mkdir()
    git(upstream, "init", "--quiet")
    git(upstream, "config", "user.name", "Fixture")
    git(upstream, "config", "user.email", "fixture@example.invalid")
    (upstream / "README.md").write_text("Local source fixture; never execute it.\n")
    git(upstream, "add", "README.md")
    git(upstream, "commit", "--quiet", "-m", "Pin the local source")
    original_run = subprocess.run
    original_origin = agentic_checkout.canonical_origin

    def local_only(args, *positional, **kwargs):
        args = list(args)
        if args[:3] == ["git", "clone", "--quiet"] and args[3] == IDENTITY:
            args[3] = str(upstream)
        # Every fetch origin is a local directory established by that clone.
        # Refuse network addresses instead of accidentally exercising the web.
        if args and args[0] == "git":
            assert not any(str(arg).startswith(("https://", "http://", "ssh://", "git@")) for arg in args)
        return original_run(args, *positional, **kwargs)

    monkeypatch.setattr(subprocess, "run", local_only)
    monkeypatch.setattr(agentic_checkout, "canonical_origin", lambda value: (
        IDENTITY if original_origin(value) == str(upstream) else original_origin(value)
    ))

    def start(*, revision=None, identity=None, boundary=False, analysts=False, production=False):
        # No actual workers. Boundary scripts bind its check only in a restricted
        # declaration; the migration declaration blocks unported runtime hand-outs.
        data = yaml.safe_load((prepared.repo / "kb" / JOB_SET).read_text())
        if not production:
            data["jobs"] = data["jobs"][:10 if analysts else 4 if boundary else 2]
        data["jobs"][1]["handler"] = ACQUIRE_HANDLER
        if boundary or analysts:
            assert not production
            data["jobs"][3]["handler"] = BOUNDARY_CHECK_HANDLER
        if analysts:
            for job in data["jobs"]:
                if job["name"].startswith("check-") and job["name"][6:] in ANALYST_CHECK_HANDLERS:
                    job["handler"] = ANALYST_CHECK_HANDLERS[job["name"][6:]]
        declaration = tmp_path / "code-only-acquisition.yaml"
        declaration.write_text(yaml.safe_dump(data), encoding="utf-8")
        parameters = dict(PARAMETERS)
        if revision is not None:
            parameters["source-revision"] = revision
        if identity is not None:
            parameters["source-identity"] = identity
        monkeypatch.setenv("COMMONPLACE_LIBRARY_ROOT", str(prepared.repo / "kb"))
        run_dir = prepared.repo / "kb/agentic-system-analyses/state" / RUN_ID
        if identity is not None:
            run_dir = run_dir.with_name(RUN_ID.replace("-system-", "-example-system-"))
        start_run(run_dir, declaration, parameters=parameters)
        c = Coordinator(run_dir, declaration.parent, tmp_path / "handlers.log")
        a = Acquisition(prepared, upstream, c)
        original_freeze = agentic_checkout.freeze_checkout

        def freeze(*args, **kwargs):
            a.freezes.append(kwargs)
            return original_freeze(*args, **kwargs)

        monkeypatch.setattr(agentic_checkout, "freeze_checkout", freeze)
        return a

    return start, upstream


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


def test_non_git_source_is_explicitly_left_for_the_boundary(acquisition):
    start, _ = acquisition
    a = start(identity="local capture fixture")
    assert not a.advance().stops
    assert a.source() is None
    assert not a.freezes and not a.journal.exists() and not a.checkout.exists()


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


@pytest.mark.parametrize("requested", (False, True))
def test_interrupted_new_clone_is_recognized_without_refetching(acquisition, monkeypatch, requested):
    start, upstream = acquisition
    revision = git(upstream, "rev-parse", "HEAD")
    a = start(revision=revision if requested else None)
    original = agentic_acquisition._write_journal

    def interrupt(path, record):
        if record["state"] == "completed":
            raise KeyboardInterrupt("after installation, before completion journal")
        original(path, record)

    monkeypatch.setattr(agentic_acquisition, "_write_journal", interrupt)
    with pytest.raises(KeyboardInterrupt):
        a.advance()
    assert json.loads(a.journal.read_text())["state"] == "started"
    advance_upstream(upstream)
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


def test_acquisition_rechecks_preparation_token_on_resume(acquisition, monkeypatch):
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
    before = a.journal.read_bytes()
    monkeypatch.setattr(RunStore, "commit_attempt", original)
    a.prepared.record(token="b" * 12)
    a.advance()
    a.stop("preparation token differs from the opened run")
    assert a.journal.read_bytes() == before and len(a.freezes) == 1
    a.prepared.record()
    assert not a.advance().stops and a.source()["kind"] == "git"


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


def test_interrupted_pinned_existing_checkout_is_recognized(acquisition, monkeypatch):
    start, upstream = acquisition
    initial = git(upstream, "rev-parse", "HEAD")
    revision = advance_upstream(upstream)
    a = start(revision=revision)
    a.checkout.parent.mkdir()
    git(a.prepared.repo, "clone", "--quiet", str(upstream), str(a.checkout))
    git(a.checkout, "checkout", "--quiet", "--detach", initial)
    original = agentic_acquisition._write_journal

    def interrupt(path, record):
        if record["state"] == "completed":
            raise KeyboardInterrupt()
        original(path, record)

    monkeypatch.setattr(agentic_acquisition, "_write_journal", interrupt)
    with pytest.raises(KeyboardInterrupt):
        a.advance()
    monkeypatch.setattr(agentic_acquisition, "_write_journal", original)
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
