"""Call the acquisition effect with local Git origins and a journal in a scratch run directory.

No workers, network sources, target execution, installations or publication.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

import pytest

from commonplace.lib.agentic_analysis import sources
from commonplace.lib.agentic_analysis.sources import (
    AcquisitionUncertainError,
    CheckoutError,
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    IDENTITY,
    advance_upstream,
    git,
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    acquisition as local_acquisition,  # noqa: F401 - explicit fixture registration
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    prepared as prepared_checkout,  # noqa: F401 - transitive local fixture
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    prepared_template as prepared_template,  # noqa: PLC0414 - session baseline registration
)
from tests.commonplace.link_helpers import symlink_or_skip

DIGEST = "d" * 64


@dataclass
class Acquiring:
    """One run's acquisition: the prepared repo, its run directory, the local upstream and freeze calls."""

    repo: Path
    run_dir: Path
    upstream: Path
    freezes: list = field(default_factory=list)

    @property
    def checkout(self) -> Path:
        return self.repo / sources.github_checkout_path(IDENTITY)

    @property
    def journal(self) -> Path:
        return self.run_dir / sources.JOURNAL

    def acquire(self, revision: str | None = None) -> dict | None:
        data = sources.acquire(self.repo, self.run_dir, identity=IDENTITY, revision=revision, inputs_digest=DIGEST)
        return json.loads(data)

    def clone(self) -> None:
        """An operator's existing checkout of the upstream at the declared path."""
        self.checkout.parent.mkdir(parents=True)
        git(self.repo, "clone", "--quiet", str(self.upstream), str(self.checkout))


@pytest.fixture
def acquiring(request, tmp_path, monkeypatch) -> Acquiring:
    upstream = request.getfixturevalue("local_acquisition")
    prepared = request.getfixturevalue("prepared_checkout")
    run_dir = tmp_path / "run"
    run_dir.mkdir()
    a = Acquiring(prepared.repo, run_dir, upstream)
    original = sources.freeze_checkout

    def counted(*args, **kwargs):
        a.freezes.append(kwargs)
        return original(*args, **kwargs)

    monkeypatch.setattr(sources, "freeze_checkout", counted)
    return a


def test_checkout_refusal_is_a_domain_value_error_without_side_effects(tmp_path):
    path = tmp_path / "not-a-checkout"
    path.write_bytes(b"keep this file")
    with pytest.raises(CheckoutError, match="not a Git checkout") as raised:
        sources.refreeze(path, origin="https://example.invalid/source", revision="a" * 40)
    assert isinstance(raised.value, ValueError)
    assert path.read_bytes() == b"keep this file"


@pytest.mark.slow
def test_clone_freezes_the_local_default_tip_and_records_the_effect(acquiring):
    a = acquiring
    revision = advance_upstream(a.upstream)
    source = a.acquire()
    assert source == {"kind": "git", "identity": IDENTITY, "revision": revision,
                      "path": str(a.checkout), "sha256": None}
    assert git(a.checkout, "rev-parse", "HEAD") == revision
    assert git(a.checkout, "rev-parse", "--abbrev-ref", "HEAD") == "HEAD"
    assert git(a.checkout, "status", "--porcelain") == ""
    record = json.loads(a.journal.read_text())
    assert record["state"] == "completed" and record["source"] == source
    assert record["path-existed"] is False and record["initial-head"] is None
    assert len(a.freezes) == 1
    # A completed journal is recognized, not replayed, even when the upstream moved on.
    git(a.upstream, "commit", "--quiet", "--allow-empty", "-m", "Advance again")
    assert a.acquire() == source
    assert len(a.freezes) == 1


@pytest.mark.slow
def test_requested_older_commit_is_frozen_not_the_current_tip(acquiring):
    a = acquiring
    older = git(a.upstream, "rev-parse", "HEAD")
    latest = advance_upstream(a.upstream)
    assert a.acquire(older)["revision"] == older != latest
    assert not (a.checkout / "NEW.md").exists()


@pytest.mark.slow
def test_matching_requested_checkout_keeps_its_branch(acquiring):
    a = acquiring
    revision = git(a.upstream, "rev-parse", "HEAD")
    a.clone()
    branch = git(a.checkout, "rev-parse", "--abbrev-ref", "HEAD")
    assert a.acquire(revision)["revision"] == revision
    assert git(a.checkout, "rev-parse", "--abbrev-ref", "HEAD") == branch


@pytest.mark.slow
def test_existing_checkout_fetches_and_freezes_the_new_default_tip(acquiring):
    a = acquiring
    a.clone()
    initial = git(a.checkout, "rev-parse", "HEAD")
    revision = advance_upstream(a.upstream)
    assert a.acquire()["revision"] == revision != initial
    assert json.loads(a.journal.read_text())["initial-head"] == initial


@pytest.mark.slow
@pytest.mark.parametrize("condition,reason", [
    ("dirty", "local changes or untracked files"),
    ("foreign", "does not have the origin"),
    ("not-git", "not the Git checkout root"),
    ("symlink", "must not redirect"),
])
def test_preflight_failure_changes_no_source_and_records_no_effect(acquiring, condition, reason):
    a = acquiring
    if condition == "not-git":
        a.checkout.mkdir(parents=True)
    elif condition == "symlink":
        a.checkout.parent.mkdir(parents=True)
        symlink_or_skip(a.checkout, a.upstream, directory=True)
    else:
        a.clone()
        if condition == "dirty":
            (a.checkout / "KEEP.md").write_bytes(b"Preserve this local change.\n")
        else:
            git(a.checkout, "remote", "set-url", "origin", "/not-the-origin")
    with pytest.raises(ValueError, match=reason):
        a.acquire()
    assert not a.journal.exists() and not a.freezes
    if condition == "dirty":
        assert (a.checkout / "KEEP.md").read_bytes() == b"Preserve this local change.\n"


@pytest.mark.slow
def test_unavailable_explicit_commit_is_an_ordinary_retryable_failure(acquiring):
    a = acquiring
    for _ in range(2):
        with pytest.raises(CheckoutError, match="requested commit"):
            a.acquire("0" * 40)
        assert json.loads(a.journal.read_text())["state"] == "started"
        assert not a.checkout.exists()
    assert len(a.freezes) == 2


@pytest.mark.slow
def test_interrupted_intent_with_no_installed_checkout_is_safe_to_retry(acquiring, monkeypatch):
    a = acquiring
    original = sources._write_journal

    def interrupt(path, record):
        original(path, record)
        raise KeyboardInterrupt("after intent, before mutation")

    monkeypatch.setattr(sources, "_write_journal", interrupt)
    with pytest.raises(KeyboardInterrupt):
        a.acquire()
    assert not a.checkout.exists() and not a.freezes
    monkeypatch.setattr(sources, "_write_journal", original)
    assert a.acquire()["kind"] == "git"
    assert len(a.freezes) == 1


@pytest.mark.slow
@pytest.mark.parametrize("case", ("new-default", "new-requested", "existing-requested"))
def test_interrupted_installation_is_recognized_without_refetching(acquiring, monkeypatch, case):
    a = acquiring
    initial = git(a.upstream, "rev-parse", "HEAD")
    requested = None
    if case == "existing-requested":
        requested = advance_upstream(a.upstream)
        a.clone()
        git(a.checkout, "checkout", "--quiet", "--detach", initial)
    elif case == "new-requested":
        requested = initial
    revision = requested or initial
    original = sources._write_journal

    def interrupt(path, record):
        if record["state"] == "completed":
            raise KeyboardInterrupt("after installation, before completion journal")
        original(path, record)

    monkeypatch.setattr(sources, "_write_journal", interrupt)
    with pytest.raises(KeyboardInterrupt):
        a.acquire(requested)
    assert json.loads(a.journal.read_text())["state"] == "started"
    if case != "existing-requested":
        advance_upstream(a.upstream)  # The installed result, not the new tip, is recognized.
    monkeypatch.setattr(sources, "_write_journal", original)
    assert a.acquire(requested)["revision"] == revision
    assert len(a.freezes) == 1


@pytest.mark.slow
def test_interrupted_existing_default_snapshot_is_uncertain(acquiring, monkeypatch):
    a = acquiring
    a.clone()
    advance_upstream(a.upstream)
    original = sources._write_journal

    def interrupt(path, record):
        if record["state"] == "completed":
            raise KeyboardInterrupt("default snapshot not journaled")
        original(path, record)

    monkeypatch.setattr(sources, "_write_journal", interrupt)
    with pytest.raises(KeyboardInterrupt):
        a.acquire()
    before = a.journal.read_bytes(), a.checkout.joinpath(".git/HEAD").read_bytes()
    monkeypatch.setattr(sources, "_write_journal", original)
    for _ in range(2):
        with pytest.raises(AcquisitionUncertainError, match="which default-branch snapshot"):
            a.acquire()
    assert len(a.freezes) == 1
    assert (a.journal.read_bytes(), a.checkout.joinpath(".git/HEAD").read_bytes()) == before


@pytest.mark.slow
def test_completion_journal_write_failure_is_uncertain_then_recognized(acquiring, monkeypatch):
    a = acquiring
    original = sources._write_journal

    def fail_completion(path, record):
        if record["state"] == "completed":
            raise OSError("scripted storage failure")
        original(path, record)

    monkeypatch.setattr(sources, "_write_journal", fail_completion)
    with pytest.raises(AcquisitionUncertainError, match="cannot record acquisition completion"):
        a.acquire()
    assert a.checkout.exists() and json.loads(a.journal.read_text())["state"] == "started"
    monkeypatch.setattr(sources, "_write_journal", original)
    assert a.acquire()["kind"] == "git"
    assert len(a.freezes) == 1


@pytest.mark.slow
def test_explicit_revision_failure_before_mutation_can_retry_the_original_checkout(acquiring, monkeypatch):
    a = acquiring
    initial = git(a.upstream, "rev-parse", "HEAD")
    revision = advance_upstream(a.upstream)
    a.clone()
    git(a.checkout, "checkout", "--quiet", "--detach", initial)
    counted = sources.freeze_checkout

    def fail_once(*args, **kwargs):
        if not a.freezes:
            a.freezes.append(kwargs)
            raise RuntimeError("temporary local fixture condition")
        return counted(*args, **kwargs)

    monkeypatch.setattr(sources, "freeze_checkout", fail_once)
    with pytest.raises(RuntimeError, match="temporary local fixture condition"):
        a.acquire(revision)
    assert git(a.checkout, "rev-parse", "HEAD") == initial
    assert a.acquire(revision)["revision"] == revision
    assert len(a.freezes) == 2


@pytest.mark.slow
def test_an_exception_after_atomic_installation_is_recognized_not_repeated(acquiring, monkeypatch):
    a = acquiring
    revision = git(a.upstream, "rev-parse", "HEAD")
    counted = sources.freeze_checkout

    def install_then_fail(*args, **kwargs):
        counted(*args, **kwargs)
        raise RuntimeError("scripted failure after installation")

    monkeypatch.setattr(sources, "freeze_checkout", install_then_fail)
    assert a.acquire()["revision"] == revision
    assert json.loads(a.journal.read_text())["state"] == "completed"


@pytest.mark.slow
@pytest.mark.parametrize("damage", ("dirty", "missing", "foreign", "symlink", "malformed-journal", "different-inputs"))
def test_recovery_preserves_unverifiable_completed_effects(acquiring, damage):
    a = acquiring
    a.acquire()
    if damage == "dirty":
        (a.checkout / "KEEP.md").write_text("Keep this evidence.\n")
    elif damage == "missing":
        a.checkout.rename(a.checkout.with_name("moved-checkout"))
    elif damage == "foreign":
        git(a.checkout, "remote", "set-url", "origin", "/not-the-origin")
    elif damage == "symlink":
        moved = a.checkout.with_name("moved-checkout")
        a.checkout.rename(moved)
        symlink_or_skip(a.checkout, moved, directory=True)
    elif damage == "malformed-journal":
        a.journal.write_bytes(b"not JSON; preserve me\n")
    else:
        record = json.loads(a.journal.read_text())
        record["metadata-sha256"] = "f" * 64
        a.journal.write_text(json.dumps(record))
    before = a.journal.read_bytes(), a.journal.stat().st_mtime_ns
    with pytest.raises(AcquisitionUncertainError):
        a.acquire()
    assert len(a.freezes) == 1
    assert (a.journal.read_bytes(), a.journal.stat().st_mtime_ns) == before
