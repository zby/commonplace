"""The report verification protocol on local fixture members: no model or publication.

A verdict is applied with `apply_verdict` to the members it was handed; the
report check is `artifact_check` over the pinned members.
"""

from __future__ import annotations

from hashlib import sha256

import pytest

from commonplace.lib.agentic_analysis.checks import (
    Correction,
    apply_verdict,
    artifact_check,
    check_candidate,
    refusal_findings,
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    acquisition as local_acquisition,  # noqa: F401 - explicit fixture registration
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    candidate as boundary_candidate,
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    prepared as prepared_checkout,  # noqa: F401 - transitive local fixture
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    prepared_template as prepared_template,  # noqa: PLC0414 - session baseline registration
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    reconciliation,
    report,
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    report_verdict as verdict,
)
from tests.commonplace.agentic_analysis.test_boundary import (
    analysis as analysis,  # noqa: PLC0414 - explicit fixture registration
)
from tests.commonplace.agentic_analysis.test_boundary import (
    begin as begin,  # noqa: PLC0414 - explicit fixture registration
)
from tests.commonplace.agentic_analysis.test_boundary import checkout, scripted

pytestmark = pytest.mark.slow

RECORDS = ("runtime", "memory", "epistemic", "workflow", "reconciliation")
"""The roles report verification verifies."""
CLEAN = b"# Artifact check\n\nnone\n"


@pytest.fixture
def records(analysis):
    """The accepted boundary, reports and reconciliation; a clean report check is handed."""
    a = scripted(analysis)
    texts = {"boundary": boundary_candidate(a), **{role: report(a, role) for role in RECORDS[:4]},
             "reconciliation": reconciliation(a)}
    analysis.members = {role: text.encode() for role, text in texts.items()}
    analysis.code["report-check"] = CLEAN
    return analysis


def apply(analysis, text, **handed):
    members = {**analysis.members, **{role: data.encode() for role, data in handed.items()}}
    return apply_verdict(analysis.candidate("report-verification", text.encode(), members))


def report_check(analysis, **changed):
    members = {**analysis.members, **changed}
    layout = analysis.layout
    snapshot = {layout.path(role): data for role, data in members.items()}
    return artifact_check(snapshot, run_dir=analysis.run_dir, repo=analysis.worktree,
                          source=scripted(analysis).source(), type_spec=analysis.method.type_spec,
                          criteria=analysis.criteria).decode()


def test_clean_members_pass_the_report_check_and_a_blocker_free_verdict_accepts_all(records):
    assert report_check(records) == CLEAN.decode()
    own, judgments = apply(records, verdict(scripted(records)))
    assert own == []
    assert {(j.role, j.outcome) for j in judgments} == {(role, "accepted") for role in RECORDS}


@pytest.mark.parametrize("body,changes,reason", [
    ("Amendment: RT-OBJ-missing now has a stronger value.", {}, "Amendment"),
    ("Unknown [RT-OBJ-missing](runtime.md#rt-obj-missing) is used.", {}, "unresolved record citation"),
    ("SRC-1", {"reviewed-boundary": "b" * 40}, "identity"),
    ("SRC-1", {"run-id": "AAS-2026-10-07-other-0123456789ab-01"}, "run-id"),
])
def test_reconciliation_content_is_not_a_semantic_verdict(records, body, changes, reason):
    text = reconciliation(scripted(records), body, **changes).encode()
    findings = check_candidate(records.candidate("reconciliation", text))
    assert any(reason in finding for finding in findings), findings


@pytest.mark.parametrize("blockers,changes,reason", [
    ("- boundary: change target.", {}, "addresses none of"),
    ("- runtime:", {}, "finding"),
    ("not a list", {}, "Markdown list"),
    ("none", {"reviewed-boundary": "b" * 40}, "identity"),
])
def test_malformed_verdict_never_judges_records(records, blockers, changes, reason):
    own, judgments = apply(records, verdict(scripted(records), blockers, **changes))
    assert judgments == []
    assert any(reason in finding for finding in own), own


def test_routes_only_addressed_blockers_and_preserves_continuations(records):
    blockers = "- runtime: reconsider SRC-1.\n  The reader inference is unsupported.\n- reconciliation: clarify the relation."
    own, judgments = apply(records, verdict(scripted(records), blockers))
    assert own == []
    assert [(j.role, j.outcome) for j in judgments] == [("runtime", "refused"), ("reconciliation", "refused")], \
        "a subject no blocker addresses is not judged"
    runtime = judgments[0].findings
    assert "The reader inference is unsupported." in runtime
    assert "clarify the relation" not in runtime
    assert "## Cited records from other reports" in runtime


def test_declined_answer_may_keep_the_exact_report(records):
    a = scripted(records)
    blocker = "- workflow: reconsider SRC-1."
    _, (judgment,) = apply(records, verdict(a, blocker))
    text = report(a, "workflow")
    correction = Correction(judgment.findings.encode(), b"- declined: SRC-1 still supports the bounded finding.\n",
                            sha256(text.encode()).hexdigest())
    assert check_candidate(records.candidate("workflow", text.encode()), correction) == []


def test_report_check_uses_pinned_content_not_projection_or_later_members(records):
    baseline = report_check(records)
    (records.run_dir / "artifact/runtime.md").write_text("untracked malformed projection")
    (records.run_dir / "artifact/synthesis.md").write_text("untracked later member")
    assert report_check(records) == baseline
    bad = report(scripted(records), "runtime").replace("## Runtime account", "## Wrong section").encode()
    findings = report_check(records, runtime=bad)
    assert "Runtime account" in findings
    assert "synthesis" not in findings and "overview" not in findings


def test_handed_report_check_failure_cannot_be_ignored(records):
    records.code["report-check"] = b"# Artifact check\n\n- runtime.md: fixture failure\n"
    own, judgments = apply(records, verdict(scripted(records)))
    assert judgments == []
    assert any("structural failures require explicit blockers" in finding for finding in own)
    own, judgments = apply(records, verdict(scripted(records), "- runtime: repair the structural failure."))
    assert own == [] and [j.role for j in judgments] == ["runtime"]


def test_per_addressee_peer_fragments_are_cut_from_handed_reports(records):
    a = scripted(records)
    memory = report(a, "memory").replace(
        "### Operative objects\n\nnone declared in this member\n",
        "### Operative objects\n\n#### MEM-OBJ-store\n\nLabel: Fixture store\n\nPinned peer finding at SRC-1.\n",
    )
    text = verdict(a, "- runtime: reconsider [MEM-OBJ-store](memory.md#mem-obj-store) and SRC-1.\n"
                   "- epistemic: reconsider SRC-1.")
    own, judgments = apply(records, text, memory=memory)
    assert own == []
    runtime = next(j.findings for j in judgments if j.role == "runtime")
    epistemic = next(j.findings for j in judgments if j.role == "epistemic")
    assert "#### MEM-OBJ-store\n\nLabel: Fixture store" in runtime
    assert "Pinned peer finding at SRC-1." in runtime
    assert "MEM-OBJ-store" not in epistemic
    assert "## Boundary and evidence" not in runtime


def test_reconciliation_structural_repair_preserves_semantic_feedback(records):
    a = scripted(records)
    _, (judgment,) = apply(records, verdict(a, "- reconciliation: clarify SRC-1 relations."))
    malformed = reconciliation(a, "Amendment: RT-OBJ-missing has a new value.").encode()
    answers = b"- corrected: clarified the relations.\n"
    findings = check_candidate(records.candidate("reconciliation", malformed),
                               Correction(judgment.findings.encode(), answers, None))
    assert findings
    structural = refusal_findings(findings, member="reconciliation", answered=judgment.findings.encode())
    assert "- reconciliation: clarify SRC-1 relations." in structural
    assert "## Limits" in structural, "the verdict's Limits are carried forward"
    repaired = reconciliation(a, "Clarified the fixture relations at SRC-1.").encode()
    assert check_candidate(records.candidate("reconciliation", repaired),
                           Correction(structural.encode(), answers, None)) == []


def test_source_drift_is_a_report_check_finding(records):
    (checkout(records) / "DIRTY.md").write_text("Local source drift; never execute.\n")
    assert "does not hold exactly" in report_check(records)
