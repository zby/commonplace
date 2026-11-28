"""Call the acquisition effect with local Git origins and a journal in a scratch run directory.

No workers, network sources, target execution, installations or publication.
"""

from __future__ import annotations

import json
from concurrent.futures import ThreadPoolExecutor
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
        return sources.checkout_root(self.repo) / sources.github_checkout_name(IDENTITY)

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
    original = sources.clone

    def counted(*args, **kwargs):
        a.freezes.append(kwargs)
        return original(*args, **kwargs)

    monkeypatch.setattr(sources, "clone", counted)
    return a


def test_checkout_refusal_is_a_domain_value_error_without_side_effects(tmp_path):
    path = tmp_path / "not-a-checkout"
    path.write_bytes(b"keep this file")
    with pytest.raises(CheckoutError, match="not a regular checkout") as raised:
        sources._checkout_head(path, IDENTITY)
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
    assert record["revision"] == revision
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
def test_existing_checkout_fetches_and_freezes_the_new_default_tip(acquiring):
    a = acquiring
    a.clone()
    initial = git(a.checkout, "rev-parse", "HEAD")
    revision = advance_upstream(a.upstream)
    assert a.acquire()["revision"] == revision != initial
    assert git(a.checkout, "rev-parse", "HEAD") == initial
    assert git(Path(a.acquire()["path"]), "rev-parse", "HEAD") == revision


@pytest.mark.slow
@pytest.mark.parametrize("condition,reason", [
    ("dirty", "local changes or untracked files"),
    ("foreign", "does not have the origin"),
    ("not-git", "not the Git checkout root"),
    ("symlink", "not a regular checkout"),
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
@pytest.mark.parametrize("case", ("new-default", "existing-requested"))
def test_interrupted_installation_is_recognized_without_refetching(acquiring, monkeypatch, case):
    a = acquiring
    initial = git(a.upstream, "rev-parse", "HEAD")
    requested = None
    if case == "existing-requested":
        requested = advance_upstream(a.upstream)
        a.clone()
        git(a.checkout, "checkout", "--quiet", "--detach", initial)
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
def test_interrupted_existing_checkout_keeps_its_journaled_default_revision(acquiring, monkeypatch):
    a = acquiring
    a.clone()
    pinned = advance_upstream(a.upstream)
    original = sources._write_journal

    def interrupt(path, record):
        if record["state"] == "completed":
            raise KeyboardInterrupt("default snapshot not journaled")
        original(path, record)

    monkeypatch.setattr(sources, "_write_journal", interrupt)
    with pytest.raises(KeyboardInterrupt):
        a.acquire()
    git(a.upstream, "commit", "--quiet", "--allow-empty", "-m", "Advance again")
    monkeypatch.setattr(sources, "_write_journal", original)
    assert a.acquire()["revision"] == pinned
    assert len(a.freezes) == 1


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
    counted = sources.clone

    def fail_once(*args, **kwargs):
        if not a.freezes:
            a.freezes.append(kwargs)
            raise RuntimeError("temporary local fixture condition")
        return counted(*args, **kwargs)

    monkeypatch.setattr(sources, "clone", fail_once)
    with pytest.raises(RuntimeError, match="temporary local fixture condition"):
        a.acquire(revision)
    assert git(a.checkout, "rev-parse", "HEAD") == initial
    assert a.acquire(revision)["revision"] == revision
    assert len(a.freezes) == 2


@pytest.mark.slow
def test_an_exception_after_atomic_installation_is_recognized_not_repeated(acquiring, monkeypatch):
    a = acquiring
    revision = git(a.upstream, "rev-parse", "HEAD")
    counted = sources.clone

    def install_then_fail(*args, **kwargs):
        counted(*args, **kwargs)
        raise RuntimeError("scripted failure after installation")

    monkeypatch.setattr(sources, "clone", install_then_fail)
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


@pytest.mark.slow
@pytest.mark.parametrize("external", [False, True])
def test_linked_worktrees_share_persistent_revision_checkouts(acquiring, tmp_path, external):
    a = acquiring
    linked = tmp_path / "linked"
    root = a.repo / "related-systems"
    if external:
        root = tmp_path / "external disk" / "sources"
        git(a.repo, "config", "--local", "commonplace.relatedSystemsDir", str(root))
    git(a.repo, "worktree", "add", "--detach", str(linked))

    def run(tree, name, revision=None):
        return json.loads(sources.acquire(tree, tree / name, identity=IDENTITY,
                                          revision=revision, inputs_digest=DIGEST))

    with ThreadPoolExecutor(max_workers=2) as pool:
        linked_run = pool.submit(run, linked, "first")
        main_run = pool.submit(run, a.repo, "same")
        first = linked_run.result()
        assert main_run.result() == first
    assert Path(first["path"]).parent == root
    assert len(a.freezes) == 1
    updated = advance_upstream(a.upstream)
    second = run(a.repo, "next")
    assert second["revision"] == updated
    assert Path(second["path"]).is_relative_to(root)
    assert run(linked, "first") == first
    assert run(linked, "second", updated) == second
    assert len(a.freezes) == 2
    git(a.repo, "worktree", "remove", "--force", str(linked))
    for source in (first, second):
        assert sources.frozen_source_refusals(source) == []


@pytest.mark.slow
def test_relative_storage_configuration_is_rejected(acquiring):
    git(acquiring.repo, "config", "--local", "commonplace.relatedSystemsDir", "../relative")
    with pytest.raises(CheckoutError, match="absolute path"):
        acquiring.acquire()
    assert not acquiring.journal.exists()
