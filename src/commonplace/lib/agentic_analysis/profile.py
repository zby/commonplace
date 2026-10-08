"""Opt-in profile/synthesis checks and application of exact handed verdicts.

Content is checked against declared byte snapshots, never mutable set members.
Semantic support and completeness are the independent verifier's judgment;
code enforces identity, shape, correction answers and limit traceability only.
The declaration must supply all criterion files read by content validation.
"""

from __future__ import annotations

import json

from commonplace.lib.agentic_analysis.boundary import frozen_source_refusals
from commonplace.lib.agentic_analysis.checks import (
    correction_findings,
    refusal_findings,
)
from commonplace.lib.agentic_analysis.handlers import (
    _analysis_layout,
    _locate,
)
from commonplace.lib.agentic_analysis.records import section
from commonplace.lib.agentic_analysis.sets import SET_TYPE
from commonplace.lib.agentic_analysis.validation import criterion_bytes
from commonplace.lib.note_parser import parse_document
from commonplace.lib.validation import validate_draft_at_slot
from commonplace.workflow import CodeAttempt

_RECORDS = ("boundary", "runtime", "memory", "epistemic", "reconciliation")
_PRIOR_VERDICTS = ("record-verification", "profile-verification")


def _snapshot(attempt: CodeAttempt, roles: tuple[str, ...], *, seen: bool = False) -> dict[str, bytes]:
    snapshot = {}
    for role in roles:
        name = "profile" if seen and role == "memory-profile" else role
        name += "-seen" if seen else ""
        data = attempt.read(name)
        if data is None:
            raise ValueError(f"profile/synthesis check requires {name}")
        snapshot[_analysis_layout(attempt).path(role)] = data
    return snapshot


def _content(attempt: CodeAttempt, repo, role: str, candidate: bytes, snapshot: dict[str, bytes]) -> list[str]:
    boundary, error = parse_document(snapshot["boundary.md"].decode("utf-8"))
    source = (boundary.frontmatter or {}).get("source") if boundary is not None and not error else None
    return ["[set] " + finding.render() for finding in validate_draft_at_slot(
        attempt.run_dir / "set", _analysis_layout(attempt).path(role), candidate,
        repo_root=repo, members=snapshot, manifest=f"type: {SET_TYPE}\n".encode(),
        criteria=criterion_bytes(attempt), frozen_source=source,
    ) if not finding.info and not finding.warn and not finding.absent]


def _identity(metadata: dict, candidate: bytes, snapshot: dict[str, bytes], *, profile: bool = False) -> list[str]:
    boundary, error = parse_document(snapshot["boundary.md"].decode("utf-8"))
    if boundary is None or error or not isinstance((boundary.frontmatter or {}).get("source"), dict):
        raise ValueError("profile/synthesis check requires a boundary with a frozen source")
    fields = boundary.frontmatter
    source = fields["source"]
    reasons = ["[invocation] " + reason for reason in frozen_source_refusals(source)]
    if fields.get("run-id") != metadata["run-id"] or source.get("identity") != metadata["source-identity"]:
        reasons.append("[invocation] handed boundary must match the opened run and source identity")
    if fields.get("reviewed-boundary") != source.get("revision"):
        reasons.append("[invocation] handed boundary must retain its frozen source revision")
    try:
        document, _ = parse_document(candidate.decode("utf-8"))
    except UnicodeError:
        document = None  # The content check owns unreadable candidate diagnostics.
    if document is not None:
        candidate_fields = document.frontmatter or {}
        if candidate_fields.get("run-id") != metadata["run-id"]:
            reasons.append("[invocation] run-id must be the opening's run identity")
        if candidate_fields.get("reviewed-boundary") != fields.get("reviewed-boundary"):
            reasons.append("[invocation] reviewed-boundary must match the handed boundary")
        if profile:
            comparison = candidate_fields.get("memory-comparison")
            if (not isinstance(comparison, dict) or type(comparison.get("version")) is not int
                    or comparison["version"] != 2):
                reasons.append("[invocation] new workflow profiles require memory-comparison version: 2")
            if candidate_fields.get("source-identity") != metadata["source-identity"]:
                reasons.append("[invocation] source-identity must be the opening's normalized source identity")
    return reasons


def _answers(attempt: CodeAttempt, candidate: bytes, *, member: str, record: str, output: str) -> list[str]:
    data = attempt.read(record)
    if data is None:
        raise ValueError(f"{member} check requires {record}")
    producer = json.loads(data)
    # These stages declare no records. Record preservation applies to analysts;
    # retaining supported profile values and prose is judged semantically.
    return ["[correction] " + reason for reason in correction_findings(
        candidate, member=member, incumbent=None, refusal=attempt.read("answered-refusal"),
        answers=attempt.read("answers"), previous_version=producer["previous_outputs"].get(output),
    )]


def _check(attempt: CodeAttempt, *, role: str, output: str) -> dict[str, bytes]:
    job = f"{role} check"
    metadata, repo = _locate(attempt)
    candidate = attempt.read("candidate")
    if candidate is None:
        raise ValueError(f"{job} requires a candidate")
    roles = _RECORDS if role == "memory-profile" else (*_RECORDS, *_PRIOR_VERDICTS)
    snapshot = _snapshot(attempt, roles)
    reasons = _content(attempt, repo, role, candidate, snapshot)
    reasons += _identity(metadata, candidate, snapshot, profile=role == "memory-profile")
    reasons += _answers(attempt, candidate, member=role, record="producer-attempt", output=output)
    cites = ("runtime", "memory", "epistemic") if role == "memory-profile" else _RECORDS[:-1]
    scope = [*(f"{role}:cites:{partner}" for partner in cites), f"{role}:identity:boundary"]
    if role == "memory-profile":
        scope.append("memory-profile:identity:memory")
    answered = attempt.read("answered-refusal")
    findings = refusal_findings(reasons, member=role, answered=answered) if reasons else ""
    if findings and answered is not None:
        limits = section(answered.decode("utf-8"), "Limits").strip()
        if limits:
            # Structural repair must not lose the semantic verdict's limits.
            findings += "\n## Limits\n\n" + limits + "\n"
    attempt.judge("candidate", outcome="refused" if reasons else "accepted", scope=tuple(scope),
                  findings=findings)
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
    subject = f"{stage}-seen"
    job = f"{role} application"
    metadata, repo = _locate(attempt)
    candidate = attempt.read("candidate")
    if candidate is None:
        raise ValueError(f"{job} requires a candidate")
    roles = (*_RECORDS, subject_role)
    if stage == "synthesis":
        roles += _PRIOR_VERDICTS
    snapshot = _snapshot(attempt, roles, seen=True)
    reasons = _content(attempt, repo, role, candidate, snapshot)
    reasons += _identity(metadata, candidate, snapshot)
    reasons += _answers(attempt, candidate, member=role, record="verifier-attempt", output="verification")
    if reasons:
        # A malformed verdict has no semantic authority over any partner.
        # No automatic scope override may cancel an earlier semantic refusal.
        attempt.judge("candidate", outcome="refused", findings=refusal_findings(
            reasons, member=role, answered=attempt.read("answered-refusal"),
        ))
        return {}
    document, _ = parse_document(candidate.decode("utf-8"))
    blockers = section(document.body, "Blockers").strip()
    # Content acceptance of the verdict cannot cover the semantic gate of its
    # subject. Only the separate blocker-free subject acceptance covers that.
    cites = ("runtime", "memory", "epistemic") if stage == "profile" else (
        "boundary", "runtime", "memory", "epistemic",
    )
    scope = (*(f"{role}:cites:{partner}" for partner in cites), f"{role}:identity:boundary")
    attempt.judge("candidate", outcome="accepted", scope=scope)
    missing_limits = []
    if stage == "synthesis":
        # Validate the handed synthesis with this exact verdict, not the latest
        # mutable synthesis. Only limit traceability belongs to this apply step;
        # the independent verifier judges its substantive support.
        with_verdict = {**snapshot, _analysis_layout(attempt).path(role): candidate}
        missing_limits = [reason for reason in _content(
            attempt, repo, subject_role, snapshot["synthesis.md"], with_verdict,
        ) if "limit not carried:" in reason]
    findings = ("## Blockers\n\n" + blockers + "\n") if blockers != "none" else ""
    if missing_limits:
        if not findings:
            findings = "## Blockers\n\n"
        findings += "".join(f"- {reason}\n" for reason in missing_limits)
    if findings:
        findings += "\n## Limits\n\n" + section(document.body, "Limits").strip() + "\n"
    attempt.judge(subject, outcome="refused" if findings else "accepted",
                  scope=(f"{role}:cites:{subject_role}",), findings=findings)
    return {}


def apply_verify_profile(attempt: CodeAttempt) -> dict[str, bytes]:
    """Apply a valid semantic profile verdict only to the exact handed profile."""
    return _apply(attempt, stage="profile")


def apply_verify_synthesis(attempt: CodeAttempt) -> dict[str, bytes]:
    """Apply a valid synthesis verdict and carried limits to the handed synthesis."""
    return _apply(attempt, stage="synthesis")
