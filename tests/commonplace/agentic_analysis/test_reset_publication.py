"""Unreleased replacement reuses the ordinary exact-byte publication effect."""
import json
from pathlib import Path

import pytest
import yaml

from commonplace.artifactrun import effects
from commonplace.artifactrun.reset import reset_run
from commonplace.artifactrun.store import RunStore
from commonplace.lib.agentic_analysis import handlers, publication
from tests.commonplace.agentic_analysis.test_publication import (
    ANALYSIS_TYPE,
    ROOT,
    assembled_publish_attempt,
    doc,
    scripted,  # noqa: F401 - fixture used by the assembled attempt
)


@pytest.fixture(params=[False, True])
def published(tmp_path, monkeypatch, request):
    checked = request.getfixturevalue("scripted")
    attempt = assembled_publish_attempt(tmp_path, checked)
    repo = attempt.run_dir.parent
    destination = repo / publication.RETAINED_ROOT / publication.publication_slug(
        attempt.metadata["source-identity"], attempt.metadata["system"])
    attempt.metadata["review-path"] = (destination / "overview.md").relative_to(repo).as_posix()
    old_id = "AAS-2026-10-06-example-0123456789ab-01"
    old = {"overview.md": doc({"run-id": old_id}), "memory.md": b"old memory\r\n"} if request.param else None
    if old:
        destination.mkdir(parents=True)
        for name, data in old.items():
            (destination / name).write_bytes(data)
        attempt.metadata["expected-incumbent-sha256"] = publication._digest(old["overview.md"])
    monkeypatch.setattr(publication, "inspect_destination", lambda **kwargs: {
        "expected_incumbent_sha256": attempt.metadata["expected-incumbent-sha256"],
    })
    receipt = handlers.publish_analysis(attempt)["receipt"]
    store = RunStore(attempt.run_dir)
    store.create({"type": (ROOT / "kb" / ANALYSIS_TYPE).read_text(), "type_spec": ANALYSIS_TYPE,
                  "library": str(repo / "kb"), "plan": "fixture.yaml", "parameters": {},
                  "declaration": yaml.safe_dump({"type": ANALYSIS_TYPE, "jobs": [
                      {"name": "opening", "kind": "code", "handler": "unused.handler", "inputs": {}, "outputs": ["metadata"]},
                      {"name": "publish", "kind": "code", "handler": "commonplace.lib.agentic_analysis.handlers.publish_analysis",
                       "inputs": {"metadata": {"address": "output", "source": "opening:metadata"}}, "outputs": ["receipt"]},
                  ]})})
    store.commit_attempt({"id": "000001-opening", "seq": 1, "job": "opening", "kind": "code", "pins": {},
                          "outputs": {"metadata": store.put(json.dumps(attempt.metadata).encode())}})
    store.commit_attempt({"id": "000002-publish", "seq": 2, "job": "publish", "kind": "code", "pins": {},
                          "outputs": {"receipt": store.put(receipt)}})
    store.write_bytes(store.state / "seq", b"2\n")
    # A source checkout and preparation are fixture-supplied; the actual reset,
    # publication hook, journals, snapshots and install_tree run without mocks.
    origin = tmp_path / "origin"
    monkeypatch.setattr("commonplace.artifactrun.worktree.source_checkout", lambda _: repo)
    monkeypatch.setattr(publication, "preparation_for", lambda _: {"origin": str(origin)})
    return attempt, destination, old, origin


def test_reset_withdraws_and_republishes_new_bytes(published):
    attempt, destination, old, _ = published
    original = effects.tree(destination)
    report = reset_run(attempt.run_dir, "publish")
    assert effects.tree(destination) == old
    assert not (attempt.run_dir / publication.JOURNAL).exists()
    archived = Path(report["archive"])
    assert effects.tree(archived / "effects/0/before") == original
    assert not (attempt.run_dir / "state/attempts/000002-publish.json").exists()
    assert (attempt.run_dir / "state/attempts/000001-opening.json").is_file()
    # Fresh, validated assembly input; no old receipt/journal is repinned.
    attempt.inputs["overview"] += b"\nCorrected unreleased account.\n"
    manifest = yaml.safe_load(attempt.inputs["manifest"])
    manifest["members"]["overview.md"]["sha256"] = publication._digest(attempt.inputs["overview"])
    attempt.inputs["manifest"] = yaml.safe_dump(manifest, sort_keys=False).encode()
    receipt = json.loads(handlers.publish_analysis(attempt)["receipt"])
    assert receipt["published"] is True
    assert effects.tree(destination) != original
    assert effects.hashes(effects.tree(destination)) == receipt["members"]
    journal = json.loads((attempt.run_dir / publication.JOURNAL).read_text())
    assert journal["new"] == receipt["members"] and journal["state"] == "completed"
    assert journal["old"] == effects.hashes(old)


def test_reset_refuses_altered_publication_without_mutation(published):
    attempt, destination, _, _ = published
    (destination / "memory.md").write_bytes(b"unexpected external edit")
    journal = (attempt.run_dir / publication.JOURNAL).read_bytes()
    with pytest.raises(ValueError, match="exact established"):
        reset_run(attempt.run_dir, "publish")
    assert (destination / "memory.md").read_bytes() == b"unexpected external edit"
    assert (attempt.run_dir / publication.JOURNAL).read_bytes() == journal
    assert not (attempt.run_dir.parent / ".reset-history").exists()


def test_reset_refuses_integrated_publication(published):
    attempt, destination, _, origin = published
    integrated = origin / destination.relative_to(attempt.run_dir.parent)
    integrated.mkdir(parents=True)
    (integrated / "overview.md").write_bytes(attempt.inputs["overview"])
    with pytest.raises(ValueError, match="already integrated"):
        reset_run(attempt.run_dir, "publish")
    assert (attempt.run_dir / publication.JOURNAL).exists()


def test_interrupted_publication_reset_does_not_clobber_new_writes(published, monkeypatch):
    from commonplace.artifactrun import reset

    attempt, destination, old, _ = published
    original = reset._replace

    def interrupt(source, target):
        original(source, target)
        raise OSError("interrupted reset")

    monkeypatch.setattr(reset, "_replace", interrupt)
    with pytest.raises(OSError, match="interrupted"):
        reset_run(attempt.run_dir, "publish")
    assert effects.tree(destination) == old
    destination.mkdir(parents=True, exist_ok=True)
    (destination / "unexpected.md").write_bytes(b"a later writer")
    monkeypatch.setattr(reset, "_replace", original)
    with pytest.raises(ValueError, match="changed since preparation"):
        reset_run(attempt.run_dir, "publish")
    assert (destination / "unexpected.md").read_bytes() == b"a later writer"
    (destination / "unexpected.md").unlink()
    if old is None:
        destination.rmdir()
    report = reset_run(attempt.run_dir, "publish")
    assert report["state"] == "completed"
    assert effects.tree(destination) == old
    assert not (attempt.run_dir / publication.JOURNAL).exists()
