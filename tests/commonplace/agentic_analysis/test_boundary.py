"""Script the engine boundary hand-out/check; no analytical workers or network."""

from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path

import pytest

from commonplace.workflow import AttemptResult, judge
from commonplace.workflow.state import Run
from commonplace.workflow.store import RunStore
from tests.commonplace.agentic_analysis.execution_fixtures import (
    acquisition as local_acquisition,  # noqa: F401 - shared local-only acquisition fixture
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    boundary as boundary,  # noqa: PLC0414 - explicit fixture registration
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    candidate,
    judgment,
    parameters,
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    prepared as prepared_checkout,  # noqa: F401 - transitive local Git fixture
)


@pytest.fixture
def acquisition(request):
    return request.getfixturevalue("local_acquisition")


@pytest.mark.slow
def test_handout_is_context_complete_and_uses_engine_names(boundary):
    a = boundary
    h = a.coordinator.handout("boundary")
    p = parameters(h)
    assert "jobs-engine/fix-boundary.md" in h.prompt.read_text()
    assert "jobs-engine/follow-worker-rules.md" in h.prompt.read_text()
    assert "## Input reading batches" in h.prompt.read_text()
    assert p["refusal"] == "absent"
    assert p["output"] == str(h.outputs["boundary"])
    assert p["validation-set"] == str(a.coordinator.run_dir / "set")
    assert p["validation-member"] == "boundary.md"
    assert json.loads(Path(p["source"]).read_bytes()) == a.source()
    metadata = json.loads(Path(p["opening"]).read_bytes())
    assert metadata["capture-directory"] == str(a.coordinator.run_dir / "sources")
    assert not (a.coordinator.run_dir / "sources").exists(), "opening names but does not create capture storage"


@pytest.mark.slow
@pytest.mark.parametrize("disposition", ["complete", "blocked", "out-of-scope"])
def test_accepts_pinned_boundary_without_claiming_downstream_coverage(boundary, disposition):
    a = boundary
    text = candidate(a, disposition)
    status = a.coordinator.complete("boundary", text)
    assert not status.stops and not status.handouts and not status.publishable
    record = judgment(a)
    assert record["outcome"] == "accepted" and record["installs"]
    assert record["findings"] == ""
    assert record["scope"] == []  # Self-citations are content checks, not cross-role coverage.
    assert (a.coordinator.run_dir / "set/boundary.md").read_text() == text
    assert {"candidate", "metadata", "source", "producer-attempt", "answered-refusal", "note-type"} <= record["basis"].keys()
    assert not (a.coordinator.run_dir / "output").exists()


@pytest.mark.slow
@pytest.mark.parametrize("changes,reason", [
    ({"run-id": "AAS-2026-10-07-other-0123456789ab-01"}, "member identity: run-id"),
    ({"reviewed-boundary": "b" * 40}, "exactly the checkout code froze"),
    # A non-complete disposition does not authorize dropping code's source pin.
    ({"result-disposition": "blocked", "source": None, "reviewed-boundary": None}, "exactly the checkout code froze"),
    ({"result-disposition": "not-a-disposition"}, "[set]"),
    ({"extra": "not allowed"}, "[set]"),
    ({"type": "types/note.md"}, "[set]"),
])
def test_refuses_bad_content_or_invocation(boundary, changes, reason):
    a = boundary
    text = candidate(a, **changes)
    status = a.coordinator.complete("boundary", text)
    assert not status.stops and a.coordinator.handed() == {"boundary"}
    record = judgment(a)
    assert record["outcome"] == "refused" and not record["installs"]
    assert reason in record["findings"]
    assert not (a.coordinator.run_dir / "set/boundary.md").exists()


@pytest.mark.slow
def test_unreadable_candidate_is_a_refusal_not_a_failed_check(boundary):
    a = boundary
    h = a.coordinator.handout("boundary")
    h.outputs["boundary"].write_bytes(b"\xff")
    status = a.coordinator.advance(AttemptResult(h.attempt, model="test-model", effort="low"))
    assert not status.stops and a.coordinator.handed() == {"boundary"}
    assert judgment(a)["outcome"] == "refused"
    assert "[set]" in judgment(a)["findings"]


@pytest.mark.slow
def test_dirty_frozen_checkout_is_refused_without_cleaning_it(boundary):
    a = boundary
    readme = a.checkout / "README.md"
    original = readme.read_bytes()
    readme.write_text("Altered after acquisition.\n")
    a.coordinator.complete("boundary", candidate(a))
    assert judgment(a)["outcome"] == "refused"
    assert "exactly the commit's files" in judgment(a)["findings"]
    assert readme.read_text() == "Altered after acquisition.\n"
    readme.write_bytes(original)
    a.coordinator.complete("boundary", candidate(a) + "\nRechecked the unchanged pin.\n")
    assert judgment(a)["outcome"] == "accepted"


@pytest.mark.slow
@pytest.mark.parametrize("disposition", ["blocked", "out-of-scope"])
def test_no_source_is_valid_only_for_noncomplete_boundary(acquisition, disposition):
    start, _ = acquisition
    a = start(boundary=True, identity="local capture identity")
    a.coordinator.advance()
    assert a.source() is None and not a.freezes
    assert not a.journal.exists() and not a.checkout.exists()
    status = a.coordinator.complete("boundary", candidate(a, disposition))
    assert not status.stops and not status.handouts and not status.publishable
    assert judgment(a)["outcome"] == "accepted"


@pytest.mark.slow
def test_capture_in_the_supplied_directory_is_accepted_and_survives_cleanup(acquisition):
    start, _ = acquisition
    a = start(boundary=True, identity="local capture identity")
    a.coordinator.advance()
    h = a.coordinator.handout("boundary")
    opening = json.loads(Path(parameters(h)["opening"]).read_bytes())
    capture = Path(opening["capture-directory"]) / "capture.txt"
    capture.parent.mkdir()
    capture.write_bytes(b"Local capture fixture; no web request.\n")
    source = {"kind": "capture", "identity": "local capture identity", "revision": "capture-1",
              "path": str(capture), "sha256": sha256(capture.read_bytes()).hexdigest()}
    text = candidate(a, source=source, **{"reviewed-boundary": "capture-1", "evidence-tier": "doc-grounded"})
    a.coordinator.complete("boundary", text)
    assert judgment(a)["outcome"] == "accepted"
    assert capture.is_file() and not h.prompt.parent.exists(), "capture survives closed hand-out cleanup"
    assert not a.freezes


@pytest.mark.slow
def test_accepted_capture_pin_cannot_change_on_boundary_correction(acquisition):
    start, _ = acquisition
    a = start(boundary=True, identity="local capture identity")
    a.coordinator.advance()
    root = a.coordinator.run_dir / "sources"
    root.mkdir()
    capture = root / "original.txt"
    capture.write_bytes(b"Original capture.\n")
    source = {"kind": "capture", "identity": "local capture identity", "revision": "capture-1",
              "path": str(capture), "sha256": sha256(capture.read_bytes()).hexdigest()}
    text = candidate(a, source=source, **{"reviewed-boundary": "capture-1"})
    a.coordinator.complete("boundary", text)
    assert judgment(a)["outcome"] == "accepted"
    judge(a.coordinator.run_dir, role="boundary", outcome="refused", findings="Clarify the boundary prose.")
    a.coordinator.advance()
    assert a.coordinator.handed() == {"boundary"}
    replacement = root / "replacement.txt"
    replacement.write_bytes(b"A different capture is not a prose correction.\n")
    changed = {**source, "path": str(replacement), "revision": "capture-2",
               "sha256": sha256(replacement.read_bytes()).hexdigest()}
    a.coordinator.complete("boundary", candidate(a, source=changed, **{"reviewed-boundary": "capture-2"}))
    assert judgment(a)["outcome"] == "refused"
    assert "preserve the incumbent boundary's frozen capture" in judgment(a)["findings"]
    assert (a.coordinator.run_dir / "set/boundary.md").read_text() == text
    assert capture.read_bytes() == b"Original capture.\n"


@pytest.mark.slow
def test_current_shipped_declaration_hands_out_translated_runtime(acquisition):
    start, _ = acquisition
    a = start(production=True)
    a.coordinator.advance()
    assert a.coordinator.handed() == {"boundary"}
    status = a.coordinator.complete("boundary", candidate(a))
    assert not status.stops and not status.publishable
    assert a.coordinator.handed() == {"runtime"}
    assert "jobs-engine/trace-runtime.md" in a.coordinator.handout("runtime").prompt.read_text()
    assert set(Run(RunStore(a.coordinator.run_dir)).members()) == {"boundary"}
