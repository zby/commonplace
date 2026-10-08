"""Script the three analyst interfaces against real types and local Git only."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml

from commonplace.lib.agentic_analysis.checks import correction_findings
from commonplace.workflow import judge
from commonplace.workflow.store import RunStore
from tests.commonplace.workflow.test_analysis_acquisition import (
    acquisition as local_acquisition,  # noqa: F401 - shared local fixture
)
from tests.commonplace.workflow.test_analysis_acquisition import (
    prepared_checkout,  # noqa: F401 - transitive local fixture
)
from tests.commonplace.workflow.test_analysis_boundary import (
    candidate as boundary_candidate,
)
from tests.commonplace.workflow.test_analysis_boundary import parameters

REPORT_TYPES = {
    "runtime": "agentic-system-runtime-report", "memory": "agent-memory-analysis-report",
    "epistemic": "agentic-system-epistemic-report",
}
KINDS = ["Components", "Operative objects", "Routes", "Claims", "Evidenced absences", "Behavioral-authority paths"]


@pytest.fixture
def analysts(request):
    start, _ = request.getfixturevalue("local_acquisition")
    a = start(analysts=True)
    a.coordinator.advance()
    a.coordinator.complete("boundary", boundary_candidate(a))
    assert a.coordinator.handed() == {"runtime"}
    return a


def report(a, member, **changes):
    fields = {
        "type": f"agentic-system-analyses/types/{REPORT_TYPES[member]}.md",
        "description": f"Example System {member} report at the frozen local fixture boundary",
        "run-id": a.coordinator.run_dir.name,
        "reviewed-boundary": a.source()["revision"],
    }
    if member == "memory":
        fields["source-identity"] = a.source()["identity"]
    fields.update(changes)
    sections = {
        "runtime": ["Runtime account", "Shared records", "Annotations"],
        "memory": ["Boundary and evidence", "Core ideas", "Shared records", "Write side", "Read-back",
                   "Integration issues", "Limitations and checks"],
        "epistemic": ["Source-and-claim boundary", "Epistemic-object inventory", "Authority-route ledger",
                      "System-claim versus route comparison", "Bounded conclusion", "Shared records"],
    }[member]
    body = f"# Example System {member} report\n\n"
    for title in sections:
        body += f"## {title}\n\n"
        if title == "Shared records":
            body += "".join(f"### {kind}\n\nnone declared in this member\n\n" for kind in KINDS)
        elif title == "Authority-route ledger":
            body += "no route found within boundary\n\n"
        elif title in ("Annotations", "Integration issues"):
            body += "none\n\n"
        else:
            body += "Local fixture only; no analytical model was run. SRC-1 fixes the evidence.\n\n"
    return "---\n" + yaml.safe_dump(fields, sort_keys=False) + "---\n\n" + body


def judgments(a, member):
    return [j for j in RunStore(a.coordinator.run_dir).judgment_records() if j["job"] == f"check-{member}"]


def through_analysts(a):
    c = a.coordinator
    c.complete("runtime", report(a, "runtime"), answers="")
    assert c.handed() == {"memory", "epistemic"}
    c.advance(c.result("memory", report(a, "memory"), answers=""),
              c.result("epistemic", report(a, "epistemic"), answers=""))
    assert not c.status.stops


def test_three_analysts_install_pinned_members_and_cover_present_relations(analysts):
    a = analysts
    through_analysts(a)
    for member in REPORT_TYPES:
        j = judgments(a, member)[-1]
        assert j["outcome"] == "accepted", j["findings"]
        assert f"{member}:identity:boundary" in {r["relation"] for r in j["scope"]}
        assert {"candidate", "producer-attempt", "answered-refusal", "incumbent-report"} <= j["basis"].keys()
        assert (a.coordinator.run_dir / "set" / f"{member}.md").read_text() == report(a, member)
    assert not a.coordinator.status.handouts and not a.coordinator.status.publishable


@pytest.mark.parametrize("member", list(REPORT_TYPES))
def test_new_handout_has_metadata_answers_and_no_legacy_parameters(analysts, member):
    a = analysts
    if member != "runtime":
        a.coordinator.complete("runtime", report(a, "runtime"), answers="")
    h = a.coordinator.handout(member)
    p = parameters(h)
    assert "jobs-engine/" in h.prompt.read_text()
    assert "output-answers" in p and "opening" in p
    assert not {"round", "requests", "run-state"} & p.keys()
    opening = json.loads(Path(p["opening"]).read_bytes())
    assert opening["run-id"] == a.coordinator.run_dir.name
    assert Path(p["boundary"]).read_text() == boundary_candidate(a)


def test_decline_keeps_report_and_rechecks_exact_handed_refusal(analysts):
    a = analysts
    through_analysts(a)
    text = report(a, "runtime")
    refusal = judge(a.coordinator.run_dir, role="runtime", outcome="refused", findings="Reconsider the supported finding.")
    a.coordinator.advance()
    assert a.coordinator.handed() == {"runtime"}
    p = parameters(a.coordinator.handout("runtime"))
    assert refusal in Path(p["refusal"]).read_text()
    assert Path(p["previous-report"]).read_text() == text
    a.coordinator.complete("runtime", text, answers="- declined: the frozen evidence still supports this finding.\n")
    assert not a.coordinator.status.stops
    assert judgments(a, "runtime")[-1]["outcome"] == "accepted"
    assert (a.coordinator.run_dir / "set/runtime.md").read_text() == text


def test_corrected_answer_cannot_keep_identical_report(analysts):
    a = analysts
    through_analysts(a)
    judge(a.coordinator.run_dir, role="runtime", outcome="refused", findings="Correct the finding.")
    a.coordinator.advance()
    a.coordinator.complete("runtime", report(a, "runtime"), answers="- corrected: changed the finding.\n")
    j = judgments(a, "runtime")[-1]
    assert j["outcome"] == "refused" and "identical to its predecessor" in j["findings"]
    assert "## Blockers" in j["findings"] and "Correct the finding." in j["findings"]


def test_structural_repair_retains_original_semantic_blockers(analysts):
    a = analysts
    through_analysts(a)
    judge(a.coordinator.run_dir, role="runtime", outcome="refused", findings=(
        "## Blockers\n\n- runtime: reconsider SRC-1.\n\n## Cited records from other reports\n\nnone\n"
    ))
    a.coordinator.advance()
    malformed = report(a, "runtime", **{"reviewed-boundary": "b" * 40})
    a.coordinator.complete("runtime", malformed, answers="- declined: checked SRC-1.\n")
    assert judgments(a, "runtime")[-1]["outcome"] == "refused"
    p = parameters(a.coordinator.handout("runtime"))
    assert "- runtime: reconsider SRC-1." in Path(p["refusal"]).read_text()
    repaired = report(a, "runtime").replace(
        "Local fixture only;", "Restored the reviewed boundary from the supplied boundary;",
    )
    a.coordinator.complete("runtime", repaired, answers="")
    assert "exactly 1 entries" in judgments(a, "runtime")[-1]["findings"]


@pytest.mark.parametrize("member,changes,reason", [
    ("runtime", {"run-id": "AAS-2026-10-07-other-0123456789ab-01"}, "run-id"),
    ("memory", {"source-identity": "wrong identity"}, "source-identity"),
    ("epistemic", {"reviewed-boundary": "b" * 40}, "identity"),
])
def test_member_identity_is_checked_against_pinned_inputs(analysts, member, changes, reason):
    a = analysts
    if member != "runtime":
        a.coordinator.complete("runtime", report(a, "runtime"), answers="")
    if member == "runtime":
        a.coordinator.complete(member, report(a, member, **changes), answers="")
    else:
        peer = "memory" if member == "epistemic" else "epistemic"
        a.coordinator.advance(
            a.coordinator.result(member, report(a, member, **changes), answers=""),
            a.coordinator.result(peer, report(a, peer), answers=""),
        )
    j = judgments(a, member)[-1]
    assert j["outcome"] == "refused" and reason in j["findings"]


def test_runtime_revision_rechecks_specialists_without_new_model_attempts(analysts):
    a = analysts
    through_analysts(a)
    before = {member: len([r for r in RunStore(a.coordinator.run_dir).attempt_records()
                          if r["job"] == member]) for member in ("memory", "epistemic")}
    judge(a.coordinator.run_dir, role="runtime", outcome="refused", findings="Clarify the account.")
    a.coordinator.advance()
    revised = report(a, "runtime").replace("Local fixture only;", "Clarified the local fixture account;")
    a.coordinator.complete("runtime", revised, answers="- corrected: clarified the account.\n")
    assert not a.coordinator.status.stops and not a.coordinator.status.handouts
    for member, count in before.items():
        assert len([r for r in RunStore(a.coordinator.run_dir).attempt_records() if r["job"] == member]) == count
        assert judgments(a, member)[-1]["outcome"] == "accepted"
        assert judgments(a, member)[-1]["basis"]["runtime"]["version"] != judgments(a, member)[0]["basis"]["runtime"]["version"]


def test_accepted_record_ids_cannot_be_dropped_on_correction(analysts):
    a = analysts
    original = report(a, "runtime").replace(
        "### Operative objects\n\nnone declared in this member\n",
        "### Operative objects\n\n#### RT-OBJ-store — Fixture store\n\nA symbolic fixture object in README.md at SRC-1.\n",
    )
    a.coordinator.complete("runtime", original, answers="")
    assert judgments(a, "runtime")[-1]["outcome"] == "accepted"
    a.coordinator.advance(
        a.coordinator.result("memory", report(a, "memory"), answers=""),
        a.coordinator.result("epistemic", report(a, "epistemic"), answers=""),
    )
    judge(a.coordinator.run_dir, role="runtime", outcome="refused", findings="Correct the object finding.")
    a.coordinator.advance()
    a.coordinator.complete("runtime", report(a, "runtime"), answers="- corrected: removed the object.\n")
    assert judgments(a, "runtime")[-1]["outcome"] == "refused"
    assert "RT-OBJ-store" in judgments(a, "runtime")[-1]["findings"]
    assert (a.coordinator.run_dir / "set/runtime.md").read_text() == original


def test_repeated_decline_is_no_progress_and_every_attempt_counts(analysts):
    a = analysts
    through_analysts(a)
    text = report(a, "runtime")
    answers = "- declined: checked SRC-1 and retained the finding.\n"
    judge(a.coordinator.run_dir, role="runtime", outcome="refused", findings="Reconsider the finding.")
    a.coordinator.advance()
    a.coordinator.complete("runtime", text, answers=answers)
    assert judgments(a, "runtime")[-1]["outcome"] == "accepted"
    judge(a.coordinator.run_dir, role="runtime", outcome="refused", findings="Reconsider again.")
    a.coordinator.advance()
    a.coordinator.complete("runtime", text, answers=answers)
    assert any("no new auxiliary version" in s.reason for s in a.coordinator.status.stops)
    a.coordinator.advance()
    assert any("max attempts (3) exhausted" in s.reason for s in a.coordinator.status.stops)
    assert not a.coordinator.status.handouts


def test_untracked_projection_cannot_supply_a_citation_partner(analysts):
    a = analysts
    projected = a.coordinator.run_dir / "set/memory.md"
    projected.write_text(
        report(a, "memory").replace("### Components\n\nnone declared in this member\n",
                                   "### Components\n\n#### MEM-CMP-unseen — Untracked component\n\nSRC-1.\n"),
    )
    text = report(a, "runtime").replace("SRC-1 fixes the evidence.", "MEM-CMP-unseen fixes the evidence.")
    a.coordinator.complete("runtime", text, answers="")
    j = judgments(a, "runtime")[-1]
    assert j["outcome"] == "refused" and "MEM-CMP-unseen" in j["findings"]
    assert j["basis"]["memory"]["version"] is None
    assert not any(r["relation"] == "runtime:cites:memory" for r in j["scope"])


def test_producer_records_the_previous_outputs_actually_delivered(analysts):
    a = analysts
    through_analysts(a)
    records = [r for r in RunStore(a.coordinator.run_dir).attempt_records() if r["job"] == "runtime"]
    assert records[0]["previous_outputs"] == {}
    judge(a.coordinator.run_dir, role="runtime", outcome="refused", findings="Check the finding.")
    a.coordinator.advance()
    opened = [r for r in RunStore(a.coordinator.run_dir).attempt_records() if r["job"] == "runtime"][-1]
    assert opened["previous_outputs"] == records[0]["outputs"]
    p = parameters(a.coordinator.handout("runtime"))
    assert Path(p["previous-report"]).read_text() == report(a, "runtime")
    assert Path(p["previous-answers"]).read_bytes() == b""


def test_structural_repair_can_restore_original_bytes_with_fresh_declines(analysts):
    a = analysts
    through_analysts(a)
    original = report(a, "runtime")
    judge(a.coordinator.run_dir, role="runtime", outcome="refused", findings=(
        "## Blockers\n\n- runtime: reconsider SRC-1.\n"
    ))
    a.coordinator.advance()
    a.coordinator.complete(
        "runtime", report(a, "runtime", **{"reviewed-boundary": "b" * 40}),
        answers="- declined: retained the SRC-1 finding.\n",
    )
    assert judgments(a, "runtime")[-1]["outcome"] == "refused"
    a.coordinator.complete(
        "runtime", original,
        answers="- declined: restored the pinned boundary and rechecked SRC-1; the finding remains supported.\n",
    )
    assert not a.coordinator.status.stops and not a.coordinator.status.handouts
    assert judgments(a, "runtime")[-1]["outcome"] == "accepted"
    assert (a.coordinator.run_dir / "set/runtime.md").read_text() == original


def test_record_preservation_is_a_pure_correction_check():
    original = "## Shared records\n\n### Operative objects\n\n#### RT-OBJ-store — Store\n\noriginal finding\n".encode()
    lost = b"## Shared records\n\nnone declared in this member\n"
    reasons = correction_findings(lost, member="runtime", incumbent=original, refusal=None, answers=b"")
    assert any("RT-OBJ-store" in reason for reason in reasons)
    changed = original.replace(b"original", b"corrected")
    assert not correction_findings(changed, member="runtime", incumbent=original, refusal=None, answers=b"")
