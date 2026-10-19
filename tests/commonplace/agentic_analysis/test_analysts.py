"""The analyst reports' checks against real types and local Git only: identity, records, corrections."""

from __future__ import annotations

from hashlib import sha256

import pytest

from commonplace.lib.agentic_analysis.checks import (
    Correction,
    check_candidate,
    refusal_findings,
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    acquisition as local_acquisition,  # noqa: F401 - shared local fixture
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
    report,
)
from tests.commonplace.agentic_analysis.test_boundary import (
    analysis as analysis,  # noqa: PLC0414 - explicit fixture registration
)
from tests.commonplace.agentic_analysis.test_boundary import (
    begin as begin,  # noqa: PLC0414 - explicit fixture registration
)
from tests.commonplace.agentic_analysis.test_boundary import scripted

pytestmark = pytest.mark.slow


def members(analysis, **changed: str) -> dict[str, bytes]:
    """The accepted boundary and runtime report, with any role replaced."""
    a = scripted(analysis)
    texts = {"boundary": boundary_candidate(a), "runtime": report(a, "runtime"), **changed}
    return {role: text.encode() for role, text in texts.items()}


def findings(analysis, role, text, correction=None, **changed):
    return check_candidate(analysis.candidate(role, text.encode(), members(analysis, **changed)), correction)


def correction(refusal: str, answers: str, previous: str | None = None) -> Correction:
    return Correction(refusal.encode(), answers.encode(),
                      None if previous is None else sha256(previous.encode()).hexdigest())


@pytest.mark.parametrize("member", ["runtime", "memory", "epistemic", "workflow"])
def test_reports_pass_against_the_pinned_boundary(analysis, member):
    assert findings(analysis, member, report(scripted(analysis), member)) == []


def test_corrected_answer_cannot_keep_identical_report(analysis):
    text = report(scripted(analysis), "runtime")
    refusal = "Correct the finding."
    result = findings(analysis, "runtime", text, correction(refusal, "- corrected: changed the finding.\n", text))
    assert any("identical to its predecessor" in finding for finding in result)
    carried = refusal_findings(result, member="runtime", answered=refusal.encode())
    assert "## Blockers" in carried and "- runtime: Correct the finding." in carried


def test_structural_repair_retains_original_semantic_blockers(analysis):
    a = scripted(analysis)
    refusal = "## Blockers\n\n- runtime: reconsider SRC-1.\n\n## Cited records from other reports\n\nnone\n"
    malformed = report(a, "runtime", **{"reviewed-boundary": "b" * 40})
    result = findings(analysis, "runtime", malformed, correction(refusal, "- declined: checked SRC-1.\n"))
    assert result
    structural = refusal_findings(result, member="runtime", answered=refusal.encode())
    assert "- runtime: reconsider SRC-1." in structural
    assert "## Cited records from other reports" in structural
    repaired = report(a, "runtime").replace(
        "Local fixture only;", "Restored the reviewed boundary from the supplied boundary;",
    )
    result = findings(analysis, "runtime", repaired, correction(structural, ""))
    assert any("exactly 1 entries" in finding for finding in result)


def test_structural_repair_can_restore_original_bytes_with_fresh_declines(analysis):
    a = scripted(analysis)
    original = report(a, "runtime")
    malformed = report(a, "runtime", **{"reviewed-boundary": "b" * 40})
    refusal = "## Blockers\n\n- runtime: reconsider SRC-1.\n"
    answers = "- declined: restored the pinned boundary and rechecked SRC-1; the finding remains supported.\n"
    assert findings(analysis, "runtime", original, correction(refusal, answers, malformed)) == []


@pytest.mark.parametrize("member,changes,reason", [
    ("runtime", {"run-id": "AAS-2026-10-07-other-0123456789ab-01"}, "run-id"),
    ("memory", {"source-identity": "wrong identity"}, "identity field source-identity 'wrong identity' does not match the run"),
    ("epistemic", {"reviewed-boundary": "b" * 40}, "identity"),
    ("workflow", {"reviewed-boundary": "b" * 40}, "identity"),
])
def test_member_identity_is_checked_against_pinned_inputs(analysis, member, changes, reason):
    result = findings(analysis, member, report(scripted(analysis), member, **changes))
    assert any(reason in finding for finding in result), result


@pytest.mark.parametrize("member,prefix", [("runtime", "RT"), ("workflow", "WF")])
def test_accepted_record_ids_cannot_be_dropped_on_correction(analysis, member, prefix):
    a = scripted(analysis)
    identifier = f"{prefix}-OBJ-store"
    original = report(a, member).replace(
        "### Operative objects\n\nnone declared in this member\n",
        f"### Operative objects\n\n#### {identifier}\n\nLabel: Fixture store\n\nA symbolic fixture object in README.md at SRC-1.\n",
    )
    assert findings(analysis, member, original, **{member: original}) == []
    answers = "- corrected: removed the object.\n"
    result = findings(analysis, member, report(a, member), correction("Correct the object finding.", answers, original),
                      **{member: original})
    assert any(identifier in finding for finding in result), result


def test_untracked_projection_cannot_supply_a_citation_partner(analysis):
    a = scripted(analysis)
    (analysis.run_dir / "artifact/memory.md").write_text(
        report(a, "memory").replace("### Components\n\nnone declared in this member\n",
                                    "### Components\n\n#### MEM-CMP-unseen\n\nLabel: Untracked component\n\nSRC-1.\n"),
    )
    text = report(a, "runtime").replace("SRC-1 fixes the evidence.",
                                        "[MEM-CMP-unseen](memory.md#mem-cmp-unseen) fixes the evidence.")
    assert any("MEM-CMP-unseen" in finding for finding in findings(analysis, "runtime", text))
