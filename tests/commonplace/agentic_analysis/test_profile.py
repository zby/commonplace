"""The memory-profile and synthesis checks and their verdicts on local fixture members; no models or publication."""

from __future__ import annotations

from hashlib import sha256

import pytest
import yaml

from commonplace.lib.agentic_analysis.checks import (
    Correction,
    apply_verdict,
    check_candidate,
    refusal_findings,
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    acquisition as local_acquisition,  # noqa: F401 - explicit fixture registration
)
from tests.commonplace.agentic_analysis.execution_fixtures import candidate as boundary
from tests.commonplace.agentic_analysis.execution_fixtures import (
    encoded,
    report,
    synthesis,
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    member_fields as identity,
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    memory_profile as profile,
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    prepared as prepared_checkout,  # noqa: F401 - transitive local fixture
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    prepared_template as prepared_template,  # noqa: PLC0414 - session baseline registration
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    subject_verdict as verdict,
)
from tests.commonplace.agentic_analysis.fixtures import frontmatter, member_fixture
from tests.commonplace.agentic_analysis.test_boundary import (
    analysis as analysis,  # noqa: PLC0414 - explicit fixture registration
)
from tests.commonplace.agentic_analysis.test_boundary import (
    begin as begin,  # noqa: PLC0414 - explicit fixture registration
)
from tests.commonplace.agentic_analysis.test_boundary import checkout, scripted

SUBJECT = {"profile": "memory-profile", "synthesis": "synthesis"}


def members(analysis, stage, **changed: bytes) -> dict[str, bytes]:
    """The accepted members a profile or synthesis stage is checked against, with any role replaced."""
    a = scripted(analysis)
    snapshot = {"boundary": boundary(a).encode(),
                **{name: report(a, name).encode() for name in ("runtime", "memory", "epistemic", "workflow")},
                "reconciliation": encoded(identity(a, "agentic-system-reconciliation-report"),
                                          "# Fixture reconciliation\n\n## Reconciliation\n\nNo amendments.\n")}
    snapshot["runtime"] = snapshot["runtime"].replace(
        b"### Operative objects\n\nnone declared in this member\n",
        b"### Operative objects\n\n#### RT-OBJ-store\n\nLabel: Store\n\nSRC-1 fixes the fixture store.\n",
    )
    snapshot["memory-profile"] = profile(a)
    if stage == "synthesis":
        snapshot.update({name: verdict(a) for name in ("report-verification", "profile-verification")})
        snapshot["synthesis"] = synthesis(a)
    return {**snapshot, **changed}


def subject_findings(analysis, stage, data, correction=None, **changed):
    """The subject's own check of `data` beside the stage's members."""
    role = SUBJECT[stage]
    return check_candidate(analysis.candidate(role, data, members(analysis, stage, **changed)), correction)


def applied(analysis, stage, data, correction=None, **changed):
    """A verdict's own findings and its judgments of the handed subject."""
    return apply_verdict(analysis.candidate(f"{stage}-verification", data, members(analysis, stage, **changed)),
                         correction)


def correction(refusal: bytes, answers: bytes, previous: bytes) -> Correction:
    return Correction(refusal, answers, sha256(previous).hexdigest())


@pytest.mark.slow
@pytest.mark.parametrize("stage", ["profile", "synthesis"])
def test_valid_content_is_accepted(analysis, stage):
    a = scripted(analysis)
    data = profile(a) if stage == "profile" else synthesis(a)
    assert subject_findings(analysis, stage, data) == []


@pytest.mark.slow
@pytest.mark.parametrize("stage", ["profile", "synthesis"])
@pytest.mark.parametrize("defect", ["identity", "grammar", "citation", "utf8"])
def test_invalid_verdict_judges_no_subject(analysis, stage, defect):
    a = scripted(analysis)
    data = {
        "identity": lambda: verdict(a, **{"reviewed-boundary": "wrong"}),
        "grammar": lambda: verdict(a, blockers="a prose blocker is invalid"),
        "citation": lambda: verdict(a, blockers="- [MEM-OBJ-unhanded](memory.md#mem-obj-unhanded) is unsupported."),
        "utf8": lambda: b"\xff",
    }[defect]()
    own, judgments = applied(analysis, stage, data)
    assert own and judgments == []


@pytest.mark.slow
@pytest.mark.parametrize("stage", ["profile", "synthesis"])
@pytest.mark.parametrize("blockers", ["none", "- RT-OBJ-store: materially unsupported conclusion; a caveat cannot contain it.\n  Continued evidence explanation."])
def test_semantic_verdict_judges_the_handed_subject(analysis, stage, blockers):
    a = scripted(analysis)
    # Poison the mutable projection; the verdict is applied to the handed bytes.
    (analysis.run_dir / "artifact" / f"{SUBJECT[stage]}.md").write_bytes(b"newer unhanded bytes")
    own, judgments = applied(analysis, stage, verdict(a, blockers=blockers))
    assert own == []
    (judgment,) = judgments
    assert judgment.role == SUBJECT[stage]
    assert judgment.outcome == ("accepted" if blockers == "none" else "refused")
    if blockers != "none":
        assert "Continued evidence explanation." in judgment.findings
        assert "## Limits" in judgment.findings


@pytest.mark.slow
@pytest.mark.parametrize("stage,apply", [("profile", False), ("synthesis", False), ("profile", True), ("synthesis", True)])
def test_correction_answers_use_exact_delivered_baseline(analysis, stage, apply):
    a = scripted(analysis)
    data = verdict(a) if apply else profile(a) if stage == "profile" else synthesis(a)
    refusal = b"## Blockers\n\n- SRC-1: reconsider the bounded finding.\n"

    def findings(answers: bytes) -> list[str]:
        if apply:
            own, judgments = applied(analysis, stage, data, correction(refusal, answers, data))
            assert not own or judgments == [], "an invalid verifier correction judges no subject"
            return own
        return subject_findings(analysis, stage, data, correction(refusal, answers, data))

    assert any("identical to its predecessor" in finding for finding in findings(b"- corrected: fixed it.\n"))
    assert findings(b"- declined: SRC-1 still warrants the bounded finding.\n") == []


@pytest.mark.slow
def test_structural_synthesis_refusal_preserves_semantic_blockers_and_limits(analysis):
    data = synthesis(scripted(analysis), **{"reviewed-boundary": "wrong"})
    refusal = (b"## Blockers\n\n- RT-OBJ-store: reconsider support.\n\n"
               b"## Limits\n\n- RT-OBJ-store: do not infer complete inventory.\n")
    findings = subject_findings(analysis, "synthesis", data,
                                Correction(refusal, b"- declined: retained the bounded finding.\n", None))
    assert findings
    carried = refusal_findings(findings, member="synthesis", answered=refusal)
    assert "reconsider support" in carried
    assert "## Limits" in carried and "do not infer complete inventory" in carried


@pytest.mark.slow
def test_profile_revision_and_source_identity_are_checked_by_validation(analysis):
    data = profile(scripted(analysis), **{"source-identity": "wrong"})
    fields = yaml.safe_load(data.decode().split("---")[1])
    fields["memory-comparison"].pop("version")
    data = encoded(fields, "# Example System profile\n\n## Comparison rationale\n\nNo evidence added.\n")
    text = "\n".join(subject_findings(analysis, "profile", data))
    assert "'version' is a required property" in text and "source-identity" in text


@pytest.mark.slow
def test_synthesis_limit_traceability_refuses_subject_not_valid_verdict(analysis):
    a = scripted(analysis)
    data = verdict(a, limits="- [RT-OBJ-store](runtime.md#rt-obj-store): missing inspection prevents complete store comparison.")
    own, (judgment,) = applied(analysis, "synthesis", data)
    assert own == []
    assert judgment.outcome == "refused" and "limit not carried" in judgment.findings
    assert "## Limits" in judgment.findings
    # The same verdict, but a synthesis carrying its ID passes.
    carried = synthesis(a, "Store inspection incomplete | [RT-OBJ-store](runtime.md#rt-obj-store) | SRC-1 | complete comparison | inspect store")
    own, (judgment,) = applied(analysis, "synthesis", data, synthesis=carried)
    assert own == [] and judgment.outcome == "accepted", judgment.findings


@pytest.mark.slow
@pytest.mark.parametrize("prior_role", ["report-verification", "profile-verification"])
def test_synthesis_content_check_carries_each_pinned_prior_limit(analysis, prior_role):
    a = scripted(analysis)
    prior = verdict(a, limits="- [RT-OBJ-store](runtime.md#rt-obj-store): incomplete store inspection prevents complete comparison.")
    findings = subject_findings(analysis, "synthesis", synthesis(a), **{prior_role: prior})
    assert any("limit not carried" in finding for finding in findings), findings


@pytest.mark.parametrize("unresolved", ["uninspected", "not-determinable"])
def test_profile_validation_consumer_retains_local_no_as_partial(tmp_path, tmp_library, unresolved):
    """Public role validation, without acquisition, a checkout or analysis state."""
    from copy import deepcopy

    from commonplace.lib.validation import validate_draft_in_role

    directory = member_fixture(tmp_path) / "artifact"
    runtime = directory / "runtime.md"
    runtime.write_text(runtime.read_text().replace(
        "none found within the fixture boundary.",
        "#### RT-ABS-static-branch\n\nLabel: Bounded static branch\n\n"
        "The inspected static branch has no automatic trace-fed write. Evidence: SRC-1.",
    ))
    fields = frontmatter(directory / "memory-profile.md")
    absence = ["runtime.md#rt-abs-static-branch"]
    store = ["runtime.md#rt-obj-store"]
    fields["memory-comparison"]["axes"]["trace_learning"] = {
        "assessment": "partial", "records": absence + store,
        "note": "Static branch classified; opaque writer prevents a system negative.",
        "units": [
            {"scope": "Inspected static branch", "assessment": "known", "records": absence,
             "note": "The absence record covers this branch only.",
             "findings": [{"value": "no", "basis": "wired", "records": absence,
                           "note": "No qualifying write within the inspected branch."}]},
            {"scope": "Included opaque writer", "assessment": unresolved, "records": store,
             "note": "Write path inaccessible; neither learning nor absence established.", "findings": []},
        ],
    }
    body = ("# Example System memory profile\n\n## Comparison rationale\n\n"
            "The local negative does not resolve the included opaque writer or its trace source.\n")
    before = deepcopy(fields)

    def failures():
        return [finding.message for finding in validate_draft_in_role(
            directory, "memory-profile", encoded(fields, body), repo_root=tmp_path,
        ) if not finding.info and not finding.warn]

    assert failures() == []
    assert fields == before
    # A classified local no cannot be hidden under an unresolved aggregate.
    fields["memory-comparison"]["axes"]["trace_learning"]["assessment"] = unresolved
    assert any("empty" in error and "findings" in error for error in failures())
    fields["memory-comparison"]["axes"]["trace_learning"]["assessment"] = "partial"
    # Nor can its absence warrant make the unresolved source inapplicable.
    fields["memory-comparison"]["axes"]["trace_source"].update(
        assessment="inapplicable", records=absence,
    )
    assert any("trace_source: inapplicability requires" in error for error in failures())


@pytest.mark.slow
def test_source_drift_refuses_acceptance(analysis):
    (checkout(analysis) / "README.md").write_text("Dirty frozen source\n")
    findings = subject_findings(analysis, "profile", profile(scripted(analysis)))
    assert any("checkout" in finding for finding in findings), findings
