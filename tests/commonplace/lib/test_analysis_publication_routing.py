"""Publication routing and cooperating-writer coordination in temporary trees only."""
from __future__ import annotations

import fcntl
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from threading import Event
from types import SimpleNamespace

import pytest
import yaml

from commonplace.lib import agentic_finalize as finalize
from commonplace.lib import agentic_job_publication as engine
from commonplace.lib import agentic_publication as legacy
from commonplace.lib.agentic_set import SET_TYPE, source_slug
from commonplace.lib.directory_artifact import MANIFEST_NAME
from commonplace.workflow.state import _parse_type

ROOT = Path(__file__).resolve().parents[3]
LOCK_PATH = "kb/agentic-system-analyses/state/.publication.lock"


def assert_locked(repo):
    with open(repo / LOCK_PATH, "a") as handle, pytest.raises(BlockingIOError):
        fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)


@pytest.mark.parametrize("operation", [finalize.start_manifest, finalize.build_manifest])
@pytest.mark.parametrize("marker", ["run.json", "state", "both", "mixed"])
def test_legacy_manifest_refuses_engine_before_creating_or_changing_twin(tmp_path, operation, marker):
    run = tmp_path / "run"
    run.mkdir()
    if marker != "state":
        (run / "run.json").write_text("{}")
    if marker in ("state", "both", "mixed"):
        (run / "state").mkdir()
    (run / "set").mkdir()
    (run / "set" / MANIFEST_NAME).write_bytes(b"engine manifest")
    if marker == "mixed":
        (run / "output").mkdir()
        (run / "output" / MANIFEST_NAME).write_bytes(b"legacy manifest")
    before = {path.relative_to(run): path.read_bytes() for path in run.rglob("*") if path.is_file()}
    with pytest.raises(ValueError, match="new-engine or mixed"):
        operation(run)
    assert {path.relative_to(run): path.read_bytes() for path in run.rglob("*") if path.is_file()} == before
    assert (run / "output").exists() == (marker == "mixed")
    assert not (run / "run-state.md").exists()


def legacy_fixture(repo):
    state = repo / "legacy-run/run-state.md"
    state.parent.mkdir()
    state.write_bytes(b"old state")
    retained = repo / "kb/agentic-system-analyses/retained/legacy"
    spec = legacy.PublicationSpec(repo, state, state.parent / "output/overview.md",
                                  "kb/agentic-system-analyses/retained/legacy/overview.md", "absent")
    checked = SimpleNamespace(
        spec=spec, final_state_text="completed state", generated_bytes=b"overview",
        retained_paths={MANIFEST_NAME: retained / MANIFEST_NAME},
        incumbent=legacy._Incumbent(),
        member_set=SimpleNamespace(artifact=SimpleNamespace(content=b"manifest"),
                                   documents=[SimpleNamespace(name="overview.md", content=b"overview")]),
    )
    return spec, checked


def engine_fixture(repo, monkeypatch):
    run = repo / "engine-run"
    run.mkdir()
    layout, _ = _parse_type((ROOT / "kb" / SET_TYPE).read_text(), SET_TYPE)
    identity = "https://example.invalid/fixture"
    destination = repo / "kb/agentic-system-analyses/retained" / source_slug(identity, "Fixture")
    members = {"boundary": b"boundary", "overview": b"overview"}
    worker = {"model": "fixture/model"}
    manifest = engine._manifest(layout, members, worker)
    metadata = {"system": "Fixture", "source-identity": identity,
                "review-path": (destination / "overview.md").relative_to(repo).as_posix(),
                "expected-incumbent-sha256": "absent"}
    attempt = SimpleNamespace(run_dir=run, read=lambda name: manifest if name == "manifest" else None)
    monkeypatch.setattr(engine, "_snapshot", lambda *a, **kw: (
        layout, (), members, SimpleNamespace(frontmatter={"result-disposition": "complete"})))
    monkeypatch.setattr(engine, "_environment", lambda *a, **kw: (metadata, repo))
    monkeypatch.setattr(engine, "_provenance", lambda *a: worker)
    monkeypatch.setattr(engine, "validate_pinned_set", lambda *a, **kw: None)
    monkeypatch.setattr(engine, "_require_opened_method", lambda *a, **kw: None)
    return attempt, destination


def test_legacy_and_engine_publishers_share_lock_across_runs_and_destinations(tmp_path, monkeypatch):
    spec, checked = legacy_fixture(tmp_path)
    attempt, destination = engine_fixture(tmp_path, monkeypatch)
    validating, release, waiting, inspecting = Event(), Event(), Event(), Event()
    original_lock = engine.publication_lock

    def enter_lock(repo):
        waiting.set()
        return original_lock(repo)

    def check_set(_):
        assert_locked(tmp_path)
        validating.set()
        assert release.wait(5)
        return checked

    def inspect(**kw):
        assert_locked(tmp_path)
        inspecting.set()
        return {"expected_incumbent_sha256": "absent"}

    original_record = engine._write_record

    def record(path, value):
        assert_locked(tmp_path)  # Both started and completed journal writes.
        original_record(path, value)

    monkeypatch.setattr(legacy, "_check_set", check_set)
    monkeypatch.setattr(engine, "publication_lock", enter_lock)
    monkeypatch.setattr(engine, "inspect_destination", inspect)
    monkeypatch.setattr(engine, "_write_record", record)
    with ThreadPoolExecutor(max_workers=2) as pool:
        old = pool.submit(legacy.publish_publication, spec)
        try:
            assert validating.wait(5)
            new = pool.submit(engine.publish_analysis, attempt)
            assert waiting.wait(5)
            assert not inspecting.wait(0.1)
            assert not destination.exists()
        finally:
            release.set()
        assert old.result(timeout=5).cleanup_warnings == ()
        assert new.result(timeout=5) == {}
    assert inspecting.is_set()
    assert yaml.safe_load((destination / MANIFEST_NAME).read_bytes())["type"] == SET_TYPE
    assert (destination / "overview.md").read_bytes() == b"overview"
    # Replay recognition, not only fresh incumbent inspection, holds the lock.
    monkeypatch.setattr(engine, "inspect_destination", lambda **kw: pytest.fail("replay reinspected"))
    assert engine.publish_analysis(attempt) == {}
    with legacy.publication_lock(tmp_path):
        assert_locked(tmp_path)


@pytest.mark.parametrize("publisher", ["legacy", "engine"])
def test_failure_keeps_lock_through_rollback_and_releases_it(tmp_path, monkeypatch, publisher):
    original_write = legacy.atomic_write

    def write(path, data):
        assert_locked(tmp_path)
        if path.name == "overview.md":
            raise OSError("fixture write failure")
        original_write(path, data)

    original_remove = legacy.shutil.rmtree

    def remove(path):
        assert_locked(tmp_path)
        original_remove(path)

    monkeypatch.setattr(legacy.shutil, "rmtree", remove)
    if publisher == "legacy":
        spec, checked = legacy_fixture(tmp_path)
        monkeypatch.setattr(legacy, "_check_set", lambda _: (assert_locked(tmp_path), checked)[1])
        monkeypatch.setattr(legacy, "atomic_write", write)
        publish = lambda: legacy.publish_publication(spec)
        destination = checked.retained_paths[MANIFEST_NAME].parent
    else:
        attempt, destination = engine_fixture(tmp_path, monkeypatch)
        monkeypatch.setattr(engine, "inspect_destination", lambda **kw: {
            "expected_incumbent_sha256": "absent"})
        monkeypatch.setattr(engine, "atomic_write", write)
        publish = lambda: engine.publish_analysis(attempt)
    with pytest.raises(OSError, match="fixture write failure"):
        publish()
    assert not destination.exists()
    if publisher == "legacy":
        assert spec.run_state_path.read_bytes() == b"old state"
    else:
        assert b'"rolled-back"' in (attempt.run_dir / engine.JOURNAL).read_bytes()
    with open(tmp_path / LOCK_PATH, "a") as handle:
        fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        fcntl.flock(handle, fcntl.LOCK_UN)
