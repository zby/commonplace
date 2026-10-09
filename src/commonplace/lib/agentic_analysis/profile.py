"""Profile/synthesis checks and application of exact handed verdicts.

Content is checked against declared byte snapshots, never mutable set members.
Semantic support and completeness are the independent verifier's judgment;
code enforces type validation, correction answers and limit traceability only.
The declaration must supply all criterion files read by content validation.
"""

from __future__ import annotations

from commonplace.lib.agentic_analysis.guards import checkout
from commonplace.lib.note_parser import parse_document, section
from commonplace.setrun.checks import (
    answer_reasons,
    candidate,
    content_reasons,
    judge,
    review,
)
from commonplace.workflow import CodeAttempt

_RECORDS = ("boundary", "runtime", "memory", "epistemic", "reconciliation")
_PRIOR_VERDICTS = ("record-verification", "profile-verification")


def _check(attempt: CodeAttempt, *, role: str, output: str) -> dict[str, bytes]:
    roles = _RECORDS if role == "memory-profile" else (*_RECORDS, *_PRIOR_VERDICTS)
    check = candidate(attempt, role, roles, repo=checkout(attempt.run_dir), source_role="boundary")
    # These stages declare no records. Record preservation applies to analysts;
    # retaining supported profile values and prose is judged semantically.
    reasons = review(check) + answer_reasons(check, record="producer-attempt", output=output)
    if role == "memory-profile" and check.fields:
        comparison = check.fields.get("memory-comparison")
        if (not isinstance(comparison, dict) or type(comparison.get("version")) is not int
                or comparison["version"] != 2):
            reasons.append("[invocation] new workflow profiles require memory-comparison version: 2")
    judge(check, reasons)
    return {}


def check_profile(attempt: CodeAttempt) -> dict[str, bytes]:
    """Check the pinned revision-2 profile and its exact correction answers."""
    return _check(attempt, role="memory-profile", output="profile")


def check_synthesize(attempt: CodeAttempt) -> dict[str, bytes]:
    """Check the pinned synthesis, prior limit traceability and correction answers."""
    return _check(attempt, role="synthesis", output="synthesis")


def _apply(attempt: CodeAttempt, *, stage: str) -> dict[str, bytes]:
    role = f"{stage}-verification"
    subject_role = "memory-profile" if stage == "profile" else "synthesis"
    roles = (*_RECORDS, subject_role)
    if stage == "synthesis":
        roles += _PRIOR_VERDICTS
    check = candidate(attempt, role, roles, repo=checkout(attempt.run_dir), seen=True, source_role="boundary")
    reasons = review(check) + answer_reasons(check, record="verifier-attempt", output="verification")
    # Content acceptance of the verdict cannot cover the semantic gate of its
    # subject. Only the separate blocker-free subject acceptance covers that.
    judge(check, reasons, subjects=(subject_role,))
    if reasons:
        # A malformed verdict has no semantic authority over any partner.
        return {}
    document, _ = parse_document(check.data.decode("utf-8"))
    blockers = section(document.body, "Blockers").strip()
    missing_limits = []
    if stage == "synthesis":
        # Validate the handed synthesis with this exact verdict, not the latest
        # mutable synthesis. Only limit traceability belongs to this apply step;
        # the independent verifier judges its substantive support.
        path = attempt.layout.path
        missing_limits = [reason for reason in content_reasons(
            check, role=subject_role, data=check.snapshot[path(subject_role)],
            members={**check.snapshot, path(role): check.data},
        ) if "limit not carried:" in reason]
    findings = ("## Blockers\n\n" + blockers + "\n") if blockers != "none" else ""
    if missing_limits:
        if not findings:
            findings = "## Blockers\n\n"
        findings += "".join(f"- {reason}\n" for reason in missing_limits)
    if findings:
        findings += "\n## Limits\n\n" + section(document.body, "Limits").strip() + "\n"
    attempt.judge(f"{subject_role}-seen", outcome="refused" if findings else "accepted",
                  scope=(f"{role}:cites:{subject_role}",), findings=findings)
    return {}


def apply_verify_profile(attempt: CodeAttempt) -> dict[str, bytes]:
    """Apply a valid semantic profile verdict only to the exact handed profile."""
    return _apply(attempt, stage="profile")


def apply_verify_synthesis(attempt: CodeAttempt) -> dict[str, bytes]:
    """Apply a valid synthesis verdict and carried limits to the handed synthesis."""
    return _apply(attempt, stage="synthesis")
