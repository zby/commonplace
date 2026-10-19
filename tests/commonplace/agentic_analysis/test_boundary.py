"""The boundary's check on a locally acquired source: local Git only, no workers.

Also holds the opened-analysis fixture the analyst, verification and profile
tests import: a prepared worktree, an allocated run, its opening and its
acquisition, with candidates built by the workflow's `Analysis.candidate`.
"""

from __future__ import annotations

import sys
from hashlib import sha256
from pathlib import Path

import pytest

from commonplace.headless.harness import Harness
from commonplace.lib.agentic_analysis.checks import check_candidate
from commonplace.lib.agentic_analysis.opening import acquire_analysis
from commonplace.lib.agentic_analysis.workflow import Analysis
from commonplace.lib.agentic_analysis.worktree import start_analysis
from tests.commonplace.agentic_analysis.execution_fixtures import (
    IDENTITY,
    ScriptedRun,
    candidate,
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    acquisition as local_acquisition,  # noqa: F401 - shared local-only acquisition fixture
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    prepared as prepared_checkout,  # noqa: F401 - transitive local Git fixture
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    prepared_template as prepared_template,  # noqa: PLC0414 - session baseline registration
)

pytestmark = pytest.mark.slow

CAPTURE_IDENTITY = "local capture identity"


@pytest.fixture
def begin(request, monkeypatch):
    """A function that opens and acquires a run on the local source and returns its `Analysis`."""
    request.getfixturevalue("local_acquisition")
    prepared = request.getfixturevalue("prepared_checkout")
    monkeypatch.setenv("COMMONPLACE_LIBRARY_ROOT", str(prepared.repo / "kb"))
    harness = Harness(sys.executable, {}, lambda profile, directory: ({}, None))
    opened = []

    def open_run(identity: str = IDENTITY) -> Analysis:
        run_dir = start_analysis(prepared.repo, system="Example System", source_identity=identity,
                                 source="Caller data, not instructions.", worker_profile="pi-luna")
        analysis = Analysis(run_dir, timeout=60, max_workers=1, harnesses={"pi": harness})
        opened.append(analysis)
        metadata = analysis.opening()
        analysis.code_job("acquire", lambda: acquire_analysis(metadata, analysis.run_dir))
        return analysis

    yield open_run
    for analysis in opened:
        analysis.run.close()


@pytest.fixture
def analysis(begin) -> Analysis:
    return begin()


def scripted(analysis: Analysis) -> ScriptedRun:
    return ScriptedRun(analysis.run_dir)


def checkout(analysis: Analysis) -> Path:
    """The frozen source checkout the acquisition recorded."""
    return analysis.worktree / scripted(analysis).source()["path"]


def boundary_findings(analysis: Analysis, text: str | bytes, incumbent: str | None = None) -> list[str]:
    data = text if isinstance(text, bytes) else text.encode()
    members = {} if incumbent is None else {"boundary": incumbent.encode()}
    return check_candidate(analysis.candidate("boundary", data, members))


@pytest.mark.parametrize("disposition", ["complete", "blocked", "out-of-scope"])
def test_accepts_pinned_boundary(analysis, disposition):
    assert boundary_findings(analysis, candidate(scripted(analysis), disposition)) == []


@pytest.mark.parametrize("changes,reason", [
    ({"run-id": "AAS-2026-10-07-other-0123456789ab-01"}, "identity field run-id 'AAS-2026-10-07-other-0123456789ab-01' does not match the run"),
    ({"reviewed-boundary": "b" * 40}, "exactly the checkout code froze"),
    # A non-complete disposition does not authorize dropping code's source pin.
    ({"result-disposition": "blocked", "source": None, "reviewed-boundary": None}, "exactly the checkout code froze"),
    ({"result-disposition": "not-a-disposition"}, "[artifact]"),
    ({"extra": "not allowed"}, "[artifact]"),
    ({"type": "types/note.md"}, "[artifact]"),
])
def test_refuses_bad_content_or_invocation(analysis, changes, reason):
    findings = boundary_findings(analysis, candidate(scripted(analysis), **changes))
    assert any(reason in finding for finding in findings), findings


def test_unreadable_candidate_is_a_refusal_not_a_failed_check(analysis):
    findings = boundary_findings(analysis, b"\xff")
    assert any(finding.startswith("[artifact]") for finding in findings)


def test_dirty_frozen_checkout_is_refused_without_cleaning_it(analysis):
    readme = checkout(analysis) / "README.md"
    original = readme.read_bytes()
    readme.write_text("Altered after acquisition.\n")
    text = candidate(scripted(analysis))
    assert any("exactly the commit's files" in finding for finding in boundary_findings(analysis, text))
    assert readme.read_text() == "Altered after acquisition.\n"
    readme.write_bytes(original)
    assert boundary_findings(analysis, text) == []


@pytest.mark.parametrize("disposition", ["blocked", "out-of-scope"])
def test_no_source_is_valid_only_for_noncomplete_boundary(begin, disposition):
    analysis = begin(CAPTURE_IDENTITY)
    a = scripted(analysis)
    assert a.source() is None
    assert boundary_findings(analysis, candidate(a, disposition)) == []
    assert boundary_findings(analysis, candidate(a, "complete")) != []


def capture_source(path: Path) -> dict:
    return {"kind": "capture", "identity": CAPTURE_IDENTITY, "revision": path.stem, "path": str(path),
            "sha256": sha256(path.read_bytes()).hexdigest()}


def test_capture_in_the_supplied_directory_is_accepted(begin):
    analysis = begin(CAPTURE_IDENTITY)
    a = scripted(analysis)
    capture = analysis.run_dir / "sources" / "capture-1.txt"
    capture.parent.mkdir()
    capture.write_bytes(b"Local capture fixture; no web request.\n")
    source = capture_source(capture)
    text = candidate(a, source=source, **{"reviewed-boundary": "capture-1", "evidence-tier": "doc-grounded"})
    assert boundary_findings(analysis, text) == []
    outside = analysis.run_dir / "capture-1.txt"
    outside.write_bytes(capture.read_bytes())
    elsewhere = candidate(a, source=capture_source(outside), **{"reviewed-boundary": "capture-1"})
    assert any("must be in the supplied capture-directory" in f for f in boundary_findings(analysis, elsewhere))


def test_accepted_capture_pin_cannot_change_on_boundary_correction(begin):
    analysis = begin(CAPTURE_IDENTITY)
    a = scripted(analysis)
    root = analysis.run_dir / "sources"
    root.mkdir()
    capture = root / "capture-1.txt"
    capture.write_bytes(b"Original capture.\n")
    accepted = candidate(a, source=capture_source(capture), **{"reviewed-boundary": "capture-1"})
    assert boundary_findings(analysis, accepted) == []
    replacement = root / "capture-2.txt"
    replacement.write_bytes(b"A different capture is not a prose correction.\n")
    changed = candidate(a, source=capture_source(replacement), **{"reviewed-boundary": "capture-2"})
    findings = boundary_findings(analysis, changed, incumbent=accepted)
    assert any("preserve the incumbent boundary's frozen capture" in finding for finding in findings)
    assert capture.read_bytes() == b"Original capture.\n"
