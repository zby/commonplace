"""Script the engine boundary hand-out/check; no analytical workers or network."""

from __future__ import annotations

import json
import os
from hashlib import sha256
from pathlib import Path

import pytest
import yaml

from commonplace.lib import agentic_job_handlers
from commonplace.workflow import AttemptResult, judge
from commonplace.workflow.state import Run
from commonplace.workflow.store import RunStore
from tests.commonplace.workflow.test_analysis_acquisition import (
    IDENTITY,
    Acquisition,
    prepared_checkout,  # noqa: F401 - transitive local Git fixture
)
from tests.commonplace.workflow.test_analysis_acquisition import (
    acquisition as local_acquisition,  # noqa: F401 - shared local-only acquisition fixture
)


@pytest.fixture
def acquisition(request):
    return request.getfixturevalue("local_acquisition")


def parameters(handout) -> dict[str, str]:
    return dict(line.split(" = ", 1) for line in handout.prompt.read_text().splitlines() if " = " in line)


def candidate(a: Acquisition, disposition="complete", **changes) -> str:
    source = a.source()
    fields = {
        "type": "agentic-system-analyses/types/agentic-system-boundary.md",
        "description": "Example System at the frozen local fixture boundary",
        "run-id": a.coordinator.run_dir.name,
        "result-disposition": disposition,
        "target-class": "returning computation",
        "boundary-kind": "subsystem-only",
        "reviewed-boundary": None if source is None else source["revision"],
        "analysis-cutoff": "2026-10-07",
        "evidence-tier": "code-grounded",
        "source": source,
        **changes,
    }
    source = fields["source"]
    body = "# Example System boundary\n\n## Boundary and evidence\n\nLocal fixture only.\n\n## Source register\n\n"
    if source is not None:
        body += (
            f"| SRC-1 | {source['kind']} | `{source['identity']}` | `{source['revision']}` | implementation "
            "| README.md | `README.md` | none |\n"
        )
    if disposition != "complete":
        body += "\n## Not reached\n\nNo analytical model was run; the fixture establishes no system findings.\n"
    return "---\n" + yaml.safe_dump(fields, sort_keys=False) + "---\n\n" + body


def judgment(a):
    store = RunStore(a.coordinator.run_dir)
    judgments = [j for j in store.judgment_records() if j["job"] == "check-boundary"]
    assert judgments
    return judgments[-1]


@pytest.fixture
def boundary(acquisition):
    start, _ = acquisition
    a = start(boundary=True)
    status = a.coordinator.advance()
    assert not status.stops and a.coordinator.handed() == {"boundary"}
    return a


def test_handout_is_context_complete_and_uses_engine_names(boundary):
    a = boundary
    h = a.coordinator.handout("boundary")
    p = parameters(h)
    assert h.prompt.read_text().startswith("Follow ")
    assert "jobs-engine/fix-boundary.md" in h.prompt.read_text()
    assert "jobs-engine/follow-worker-rules.md" in h.prompt.read_text()
    assert "## Input reading batches" in h.prompt.read_text()
    assert p["refusal"] == "absent"
    assert p["output"] == str(h.outputs["boundary"])
    assert p["validation-set"] == str(a.coordinator.run_dir / "set")
    assert p["validation-member"] == "boundary.md"
    assert not {"run-state", "read-first", "previous-output", "round", "requests"} & p.keys()
    assert json.loads(Path(p["source"]).read_bytes()) == a.source()
    metadata = json.loads(Path(p["opening"]).read_bytes())
    assert metadata["source-identity"] == IDENTITY
    assert "output = /not-authorized" in metadata["source"]
    assert metadata["command-path"] == str(a.prepared.repo / ".venv" / ("Scripts" if os.name == "nt" else "bin"))
    assert metadata["capture-directory"] == str(a.coordinator.run_dir / "sources")
    assert not (a.coordinator.run_dir / "sources").exists(), "opening names but does not create capture storage"
    assert not (a.coordinator.run_dir / "output").exists()


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


@pytest.mark.parametrize("changes,reason", [
    ({"run-id": "AAS-2026-10-07-other-0123456789ab-01"}, "member identity: run-id"),
    ({"reviewed-boundary": "b" * 40}, "exactly the checkout code froze"),
    ({"source": None}, "exactly the checkout code froze"),
    ({"result-disposition": "not-a-disposition"}, "[set]"),
    ({"extra": "not allowed"}, "[set]"),
    ({"type": "types/note.md"}, "[set]"),
])
def test_refuses_bad_content_or_invocation_and_hands_repair_inputs(boundary, changes, reason):
    a = boundary
    text = candidate(a, **changes)
    status = a.coordinator.complete("boundary", text)
    assert not status.stops and a.coordinator.handed() == {"boundary"}
    record = judgment(a)
    assert record["outcome"] == "refused" and not record["installs"]
    assert reason in record["findings"]
    assert not (a.coordinator.run_dir / "set/boundary.md").exists()
    p = parameters(a.coordinator.handout("boundary"))
    assert Path(p["previous-boundary"]).read_text() == text
    assert record["id"] in Path(p["refusal"]).read_text()
    assert record["subject"]["version"] in Path(p["refusal"]).read_text()
    status = a.coordinator.complete("boundary", candidate(a))
    assert not status.stops and not status.handouts
    assert judgment(a)["outcome"] == "accepted"
    assert len(a.freezes) == 1, "repair must not acquire a different source"


def test_noncomplete_disposition_cannot_drop_the_acquired_pin(boundary):
    a = boundary
    a.coordinator.complete("boundary", candidate(a, "blocked", source=None, **{"reviewed-boundary": None}))
    assert judgment(a)["outcome"] == "refused"
    assert "exactly the checkout code froze" in judgment(a)["findings"]


@pytest.mark.parametrize("defect", ["identity", "revision", "path", "digest"])
def test_cannot_substitute_any_part_of_the_acquisition_object(boundary, defect):
    a = boundary
    source = a.source()
    source[{"digest": "sha256"}.get(defect, defect)] = "b" * 40
    a.coordinator.complete("boundary", candidate(a, source=source))
    assert judgment(a)["outcome"] == "refused"
    assert "exactly the checkout code froze" in judgment(a)["findings"]


def test_unreadable_candidate_is_a_refusal_not_a_failed_check(boundary):
    a = boundary
    h = a.coordinator.handout("boundary")
    h.outputs["boundary"].write_bytes(b"\xff")
    status = a.coordinator.advance(AttemptResult(h.attempt, model="test-model", effort="low"))
    assert not status.stops and a.coordinator.handed() == {"boundary"}
    assert judgment(a)["outcome"] == "refused"
    assert "[set]" in judgment(a)["findings"]


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


def test_redirected_checkout_is_refused_without_following_or_repairing_it(boundary):
    a = boundary
    moved = a.checkout.with_name("moved-system")
    a.checkout.rename(moved)
    a.checkout.symlink_to(moved, target_is_directory=True)
    a.coordinator.complete("boundary", candidate(a))
    assert judgment(a)["outcome"] == "refused"
    assert "redirected through a symlink" in judgment(a)["findings"]
    assert a.checkout.is_symlink() and moved.is_dir()


def test_check_reads_pinned_bytes_not_handout_or_set_copies(boundary, monkeypatch):
    a = boundary
    h = a.coordinator.handout("boundary")
    text = candidate(a)
    original = agentic_job_handlers.check_boundary

    def tamper_then_check(attempt):
        # Closed hand-outs are swept before checks; recreate an irrelevant copy.
        h.outputs["boundary"].parent.mkdir(parents=True, exist_ok=True)
        h.outputs["boundary"].write_text("changed after completion\n")
        directory = a.coordinator.run_dir / "set"
        (directory / "boundary.md").write_text("not the candidate\n")
        (directory / "intruder.md").write_text("---\ntype: [broken\n---\n")
        (directory / "ARTIFACT.yaml").write_text("invalid: [manifest\n")
        return original(attempt)

    monkeypatch.setattr(agentic_job_handlers, "check_boundary", tamper_then_check)
    a.coordinator.complete("boundary", text)
    assert judgment(a)["outcome"] == "accepted"
    assert (a.coordinator.run_dir / "set/boundary.md").read_text() == text
    assert judgment(a)["subject"]["version"] == sha256(text.encode()).hexdigest()


@pytest.mark.parametrize("disposition", ["blocked", "out-of-scope"])
def test_no_source_is_valid_only_for_noncomplete_boundary(acquisition, disposition):
    start, _ = acquisition
    a = start(boundary=True, identity="local capture identity")
    a.coordinator.advance()
    assert a.source() is None and not a.freezes
    status = a.coordinator.complete("boundary", candidate(a, disposition))
    assert not status.stops and not status.handouts and not status.publishable
    assert judgment(a)["outcome"] == "accepted"


@pytest.mark.parametrize("defect", [None, "digest", "label", "identity"])
def test_capture_is_checked_by_identity_label_and_exact_bytes(acquisition, defect):
    start, _ = acquisition
    a = start(boundary=True, identity="local capture identity")
    a.coordinator.advance()
    h = a.coordinator.handout("boundary")
    opening = json.loads(Path(parameters(h)["opening"]).read_bytes())
    capture = Path(opening["capture-directory"]) / "capture.txt"
    capture.parent.mkdir()
    capture.write_bytes(b"Local capture fixture; no web request.\n")
    source = {"kind": "capture", "identity": "other identity" if defect == "identity" else "local capture identity",
              "revision": "capture-1", "path": str(capture),
              "sha256": "0" * 64 if defect == "digest" else sha256(capture.read_bytes()).hexdigest()}
    text = candidate(a, source=source, **{
        "reviewed-boundary": "different label" if defect == "label" else "capture-1", "evidence-tier": "doc-grounded",
    })
    a.coordinator.complete("boundary", text)
    record = judgment(a)
    assert record["outcome"] == ("refused" if defect else "accepted")
    if defect:
        assert {"digest": "source.sha256", "label": "frozen capture's label", "identity": "source.identity"}[defect] in record["findings"]
    assert capture.is_file() and not h.prompt.parent.exists(), "capture survives closed hand-out cleanup"
    assert not a.freezes


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


def test_capture_cannot_use_storage_outside_the_supplied_directory(acquisition, tmp_path):
    start, _ = acquisition
    a = start(boundary=True, identity="local capture identity")
    a.coordinator.advance()
    capture = tmp_path / "unowned-capture.txt"
    capture.write_bytes(b"Verifiable bytes do not grant write authority here.\n")
    source = {"kind": "capture", "identity": "local capture identity", "revision": "capture-1",
              "path": str(capture), "sha256": sha256(capture.read_bytes()).hexdigest()}
    a.coordinator.complete("boundary", candidate(a, source=source, **{"reviewed-boundary": "capture-1"}))
    assert judgment(a)["outcome"] == "refused"
    assert "supplied capture-directory" in judgment(a)["findings"]


def test_boundary_check_rechecks_preparation_and_can_resume_without_a_new_worker(boundary):
    a = boundary
    text = candidate(a)
    a.prepared.record(token="b" * 12)
    status = a.coordinator.complete("boundary", text)
    (stop,) = status.stops
    assert stop.job == "check-boundary" and "preparation token differs" in stop.reason
    assert not stop.uncertain
    assert not RunStore(a.coordinator.run_dir).judgment_records()
    a.prepared.record()
    status = a.coordinator.advance()
    assert not status.stops and not status.handouts and judgment(a)["outcome"] == "accepted"
    assert (a.coordinator.run_dir / "set/boundary.md").read_text() == text
    assert len(a.freezes) == 1


def test_boundary_unchanged_refusal_answer_fails_and_bound_does_not_reset(boundary):
    a = boundary
    text = candidate(a, **{"run-id": "AAS-2026-10-07-other-0123456789ab-01"})
    a.coordinator.complete("boundary", text)
    assert judgment(a)["outcome"] == "refused"
    status = a.coordinator.complete("boundary", text)
    assert status.stops and status.stops[0].job == "boundary"
    assert "unchanged" in status.stops[0].reason
    assert len(RunStore(a.coordinator.run_dir).judgment_records()) == 1
    status = a.coordinator.advance()
    assert not status.handouts and status.stops[0].job == "boundary"
    assert "max attempts" in status.stops[0].reason


def test_migration_declaration_stops_before_legacy_runtime_handout(acquisition):
    start, _ = acquisition
    a = start(production=True)
    a.coordinator.advance()
    assert a.coordinator.handed() == {"boundary"}
    status = a.coordinator.complete("boundary", candidate(a))
    assert not status.handouts and not status.open_attempts and not status.publishable
    (stop,) = status.stops
    assert stop.job == "check-boundary" and "handlers are not ported" in stop.reason
    assert Run(RunStore(a.coordinator.run_dir)).members() == {}
