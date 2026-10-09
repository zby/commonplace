"""Script the three analyst interfaces against real types and local Git only."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from commonplace.artifactrun import judge
from tests.commonplace.agentic_analysis.execution_fixtures import (
    REPORT_TYPES,
    judgments,
    parameters,
    report,
    through_analysts,
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    acquisition as local_acquisition,  # noqa: F401 - shared local fixture
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    analysts as analysts,  # noqa: PLC0414 - explicit fixture registration
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    candidate as boundary_candidate,
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    prepared as prepared_checkout,  # noqa: F401 - transitive local fixture
)


@pytest.mark.slow
def test_three_analysts_install_pinned_members_and_cover_present_relations(analysts):
    a = analysts
    through_analysts(a)
    for member in REPORT_TYPES:
        j = judgments(a, member)[-1]
        assert j["outcome"] == "accepted", j["findings"]
        assert f"{member}:identity:boundary" in {r["relation"] for r in j["scope"]}
        assert {"candidate", "producer-attempt", "answered-refusal", "incumbent-report"} <= j["basis"].keys()
        assert (a.coordinator.run_dir / "artifact" / f"{member}.md").read_text() == report(a, member)
    assert not a.coordinator.status.handouts and not a.coordinator.status.publishable


@pytest.mark.slow
def test_analyst_handouts_carry_opening_answers_and_pinned_boundary(analysts):
    a = analysts
    for member in REPORT_TYPES:
        if member == "memory":
            a.coordinator.complete("runtime", report(a, "runtime"), answers="")
        h = a.coordinator.handout(member)
        p = parameters(h)
        assert "jobs-engine/" in h.prompt.read_text()
        assert "## Input reading batches" in h.prompt.read_text()
        assert "output-answers" in p
        opening = json.loads(Path(p["opening"]).read_bytes())
        assert opening["run-id"] == a.coordinator.run_dir.name
        assert Path(p["boundary"]).read_text() == boundary_candidate(a)


@pytest.mark.slow
def test_corrected_answer_cannot_keep_identical_report(analysts):
    a = analysts
    through_analysts(a)
    judge(a.coordinator.run_dir, role="runtime", outcome="refused", findings="Correct the finding.")
    a.coordinator.advance()
    a.coordinator.complete("runtime", report(a, "runtime"), answers="- corrected: changed the finding.\n")
    j = judgments(a, "runtime")[-1]
    assert j["outcome"] == "refused" and "identical to its predecessor" in j["findings"]
    assert "## Blockers" in j["findings"] and "Correct the finding." in j["findings"]


@pytest.mark.slow
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


@pytest.mark.slow
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


@pytest.mark.slow
def test_accepted_record_ids_cannot_be_dropped_on_correction(analysts):
    a = analysts
    original = report(a, "runtime").replace(
        "### Operative objects\n\nnone declared in this member\n",
        "### Operative objects\n\n#### RT-OBJ-store\n\nLabel: Fixture store\n\nA symbolic fixture object in README.md at SRC-1.\n",
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
    assert (a.coordinator.run_dir / "artifact/runtime.md").read_text() == original


@pytest.mark.slow
def test_untracked_projection_cannot_supply_a_citation_partner(analysts):
    a = analysts
    projected = a.coordinator.run_dir / "artifact/memory.md"
    projected.write_text(
        report(a, "memory").replace("### Components\n\nnone declared in this member\n",
                                   "### Components\n\n#### MEM-CMP-unseen\n\nLabel: Untracked component\n\nSRC-1.\n"),
    )
    text = report(a, "runtime").replace("SRC-1 fixes the evidence.", "[MEM-CMP-unseen](memory.md#mem-cmp-unseen) fixes the evidence.")
    a.coordinator.complete("runtime", text, answers="")
    j = judgments(a, "runtime")[-1]
    assert j["outcome"] == "refused" and "MEM-CMP-unseen" in j["findings"]
    assert j["basis"]["memory"]["version"] is None
    assert not any(r["relation"] == "runtime:cites:memory" for r in j["scope"])


@pytest.mark.slow
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
    assert (a.coordinator.run_dir / "artifact/runtime.md").read_text() == original
