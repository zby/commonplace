"""Cooperating analysis publishers in temporary trees only."""
from __future__ import annotations

import fcntl
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from threading import Event
from types import SimpleNamespace

import pytest
import yaml

from commonplace.lib.agentic_analysis import effects, guards, publication
from commonplace.lib.agentic_analysis.analyses import ANALYSIS_TYPE, publication_slug
from commonplace.lib.directory_artifact import MANIFEST_NAME
from commonplace.lib.directory_layout import type_layout

ROOT = Path(__file__).resolve().parents[3]
LOCK_PATH = "kb/agentic-system-analyses/state/.publication.lock"


def assert_locked(repo):
    with open(repo / LOCK_PATH, "a") as handle, pytest.raises(BlockingIOError):
        fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)


def publisher(repo, monkeypatch, name="fixture"):
    """A run whose publication has every guard but the lock and the effect scripted away."""
    run = repo / f"run-{name}"
    run.mkdir()
    layout = type_layout((ROOT / "kb" / ANALYSIS_TYPE).read_text(), ANALYSIS_TYPE)
    identity = f"https://example.invalid/{name}"
    destination = repo / "kb/agentic-system-analyses/retained" / publication_slug(identity, name)
    members = {"boundary": b"boundary", "overview": b"overview"}
    worker = {"profile": "fixture", "harness": "fixture", "launch-model": "fixture/model",
              "model": "fixture-model-1", "effort": "high"}
    manifest = publication._manifest(layout, ANALYSIS_TYPE, members, worker)
    metadata = {"system": name, "source-identity": identity,
                "review-path": (destination / "overview.md").relative_to(repo).as_posix(),
                "expected-incumbent-sha256": "absent"}

    def publish():
        return publication.publish_analysis(
            members, metadata=json.dumps(metadata).encode(), source=None, provenance={}, manifest=manifest,
            layout=layout, type_spec=ANALYSIS_TYPE, criteria={}, run_dir=run, library=repo / "kb")

    fixture = SimpleNamespace(run_dir=run, metadata=metadata, publish=publish)
    monkeypatch.setattr(publication, "_classified_boundary", lambda *a: SimpleNamespace(
        frontmatter={"result-disposition": "complete"}))
    monkeypatch.setattr(publication, "_opened_environment", lambda metadata, *a, **kw: (json.loads(metadata), repo))
    monkeypatch.setattr(publication, "_environment", lambda *a, **kw: None)
    monkeypatch.setattr(publication, "_provenance", lambda *a: worker)
    monkeypatch.setattr(publication, "validate_pinned_artifact", lambda *a, **kw: None)
    monkeypatch.setattr(publication, "_require_opened_method", lambda *a, **kw: None)
    return fixture, destination


def test_publishers_share_lock_across_runs_and_destinations(tmp_path, monkeypatch):
    first, first_destination = publisher(tmp_path, monkeypatch, "first")
    second, second_destination = publisher(tmp_path, monkeypatch, "second")
    validating, release, waiting, inspecting = Event(), Event(), Event(), Event()
    original_lock = publication.publication_lock

    def enter_lock(repo):
        if validating.is_set():
            waiting.set()
        return original_lock(repo)

    def inspect(**kw):
        assert_locked(tmp_path)
        if kw["generated_destination"] == first.metadata["review-path"]:
            validating.set()
            assert release.wait(5)
        else:
            inspecting.set()
        return {"expected_incumbent_sha256": "absent"}

    original_record = effects.write_json

    def record(path, value):
        assert_locked(tmp_path)  # Both started and completed journal writes.
        original_record(path, value)

    monkeypatch.setattr(publication, "publication_lock", enter_lock)
    monkeypatch.setattr(publication, "inspect_destination", inspect)
    monkeypatch.setattr(effects, "write_json", record)
    with ThreadPoolExecutor(max_workers=2) as pool:
        first_result = pool.submit(first.publish)
        try:
            assert validating.wait(5)
            second_result = pool.submit(second.publish)
            assert waiting.wait(5)
            assert not inspecting.wait(0.1)
            assert not first_destination.exists()
            assert not second_destination.exists()
        finally:
            release.set()
        for result in (first_result, second_result):
            assert json.loads(result.result(timeout=5))["published"] is True
    assert inspecting.is_set()
    for destination in (first_destination, second_destination):
        assert yaml.safe_load((destination / MANIFEST_NAME).read_bytes())["type"] == ANALYSIS_TYPE
        assert (destination / "overview.md").read_bytes() == b"overview"
    # Replay recognition, not only fresh incumbent inspection, holds the lock.
    original_effect = publication.install_tree

    def replay(**kwargs):
        assert_locked(tmp_path)
        return original_effect(**kwargs)

    monkeypatch.setattr(publication, "install_tree", replay)
    monkeypatch.setattr(publication, "inspect_destination", lambda **kw: pytest.fail("replay reinspected"))
    assert json.loads(second.publish())["published"] is True
    with guards.publication_lock(tmp_path):
        assert_locked(tmp_path)


def test_failure_keeps_lock_through_rollback_and_releases_it(tmp_path, monkeypatch):
    original_write = effects.atomic_write

    def write(path, data):
        assert_locked(tmp_path)
        if path.name == "overview.md":
            raise OSError("fixture write failure")
        original_write(path, data)

    original_remove = effects.shutil.rmtree

    def remove(path):
        assert_locked(tmp_path)
        original_remove(path)

    monkeypatch.setattr(effects.shutil, "rmtree", remove)
    run, destination = publisher(tmp_path, monkeypatch)
    monkeypatch.setattr(publication, "inspect_destination", lambda **kw: {
        "expected_incumbent_sha256": "absent"})
    monkeypatch.setattr(effects, "atomic_write", write)
    with pytest.raises(OSError, match="fixture write failure"):
        run.publish()
    assert not destination.exists()
    assert b'"rolled-back"' in (run.run_dir / publication.JOURNAL).read_bytes()
    with open(tmp_path / LOCK_PATH, "a") as handle:
        fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        fcntl.flock(handle, fcntl.LOCK_UN)
