"""Standard handlers for the code jobs most plans repeat.

A plan names them by dotted path like any handler. Each is a thin adapter:
it builds the plain `Candidate` of `checks` from the attempt's pinned
inputs, calls the plain check and stages the judgments it returns. Each
learns what it judges from the job's declared inputs, never from per-job
configuration:

- the candidate is the input named `candidate`; its role is the role of the
  job whose primary output it is;
- the partners are the other inputs that hold a role by declaration, each
  placed at its role's path in the snapshot the candidate is validated
  against; a read of the candidate's own role is its incumbent, whose
  declared identifiers the candidate must keep;
- the producer's correction answers are checked when the job declares the
  producer's attempt record: the answered refusal is that record's handed
  `refusal`, and the answers are the producer's other declared output.

Validation runs in the project the run's library belongs to, against the
job's pinned criteria.

The plan's `frozen-source` names the role whose `source` field pins the
checkout the run may inspect. A job's `extensions`, fixed with the plan,
extend the standard handlers: `checks` lists functions called with the built candidate,
each returning refusal findings; `feedback` names a function the verdict
application calls for each refused subject with the role, the blockers
addressed to it and the verdict's candidate, appending the text it returns.
The verification protocol itself is `checks.apply_verdict`.
"""

from __future__ import annotations

import json
from collections.abc import Mapping

from commonplace.artifactrun import CodeAttempt
from commonplace.artifactrun.checks import (
    ARTIFACT_CHECK_HEADING,
    Candidate,
    Correction,
    apply_verdict,
    check_candidate,
    frozen_source,
    judgment_scope,
    refusal_findings,
    source_field,
)
from commonplace.artifactrun.checks import (
    artifact_check as check_artifact,
)

__all__ = ["ARTIFACT_CHECK_HEADING", "source_field"]

CANDIDATE = "candidate"


def partners(attempt: CodeAttempt, *, exclude: str) -> dict[str, str]:
    """Inputs holding a role other than ``exclude``, by role; one input per role."""
    found: dict[str, str] = {}
    for name in attempt.inputs:
        role = attempt.input_role(name)
        if name == CANDIDATE or role is None or role == exclude:
            continue
        if role in found:
            raise ValueError(f"job {attempt.job.name}: inputs {found[role]} and {name} both hold role {role}")
        found[role] = name
    return found


def snapshot(attempt: CodeAttempt, inputs: Mapping[str, str]) -> dict[str, bytes]:
    """The present members of ``inputs`` (role to input name), at their roles' paths."""
    members = {}
    for role, name in inputs.items():
        data = attempt.read(name)
        if data is not None:
            members[attempt.layout.path(role)] = data
    return members


def criterion_bytes(attempt: CodeAttempt) -> dict[str, bytes]:
    """The job's pinned library files plus the type fixed at start.

    Missing dependencies stay absent; the closed validator rejects them.
    """
    return {**attempt.read_files(), attempt.type_spec: attempt.type_text.encode("utf-8")}


def candidate(attempt: CodeAttempt) -> Candidate:
    """The `candidate` input at its declared role, with its partners present."""
    role = attempt.input_role(CANDIDATE)
    if role is None:
        raise ValueError(f"job {attempt.job.name}: input {CANDIDATE} must be a role-filling job's primary output")
    data = attempt.read(CANDIDATE)
    if data is None:
        raise ValueError(f"job {attempt.job.name}: no {CANDIDATE} to check")
    members = snapshot(attempt, partners(attempt, exclude=role))
    # The role's accepted version, when the job reads it: a correction keeps its declarations.
    incumbent = next((attempt.read(name) for name, spec in attempt.inputs.items()
                      if spec.address == "role" and spec.source == role), None)
    return Candidate(
        role, data, members, attempt.library.parent,
        frozen_source(attempt.frozen_source, role, members, attempt.layout, job=attempt.job.name), incumbent,
        run_dir=attempt.run_dir, layout=attempt.layout, relations=attempt.relations,
        type_spec=attempt.type_spec, criteria=criterion_bytes(attempt), run_values=attempt.run_values,
        frozen_source=attempt.frozen_source, extensions=attempt.extensions,
        inputs={name: attempt.read(name) for name in attempt.inputs},
    )


def _named(attempt: CodeAttempt, address: str, source: str) -> str | None:
    return next((name for name, spec in attempt.inputs.items()
                 if spec.address == address and spec.source == source), None)


def correction(attempt: CodeAttempt) -> tuple[Correction | None, str | None]:
    """The producer's correction, and the name of the input holding the answered refusal.

    Nothing is checked when the job does not declare the producer's attempt
    record or its answers output.
    """
    producer, _, output = attempt.inputs[CANDIDATE].source.partition(":")
    record = _named(attempt, "attempt", producer)
    if record is None:
        return None, None
    answered = _named(attempt, "handed", f"{record}:refusal")
    answers = next((name for name, spec in attempt.inputs.items()
                    if spec.address == "output" and name != CANDIDATE
                    and attempt.producer(name) == producer), None)
    record_data = attempt.read(record)
    if answers is None or record_data is None:
        return None, answered
    previous = json.loads(record_data)["previous_outputs"].get(output)
    return Correction(attempt.read(answered) if answered else None, attempt.read(answers), previous), answered


def judge(attempt: CodeAttempt, check: Candidate, findings: list[str], *, answered: str | None) -> None:
    """Stage the candidate's own judgment over the relations its validation examined.

    ``answered`` names the input holding the refusal the producer answered,
    or None; a refusal carries that refusal's blockers forward.
    """
    packet = refusal_findings(
        findings, member=check.role, answered=attempt.read(answered) if answered else None,
    ) if findings else ""
    attempt.judge(CANDIDATE, outcome="refused" if findings else "accepted",
                  scope=judgment_scope(check), findings=packet)


def check(attempt: CodeAttempt) -> Mapping[str, bytes]:
    """Judge a candidate at its role: content, relations and correction answers."""
    built = candidate(attempt)
    answered_correction, answered = correction(attempt)
    judge(attempt, built, check_candidate(built, answered_correction), answered=answered)
    return {}


def apply_verification(attempt: CodeAttempt) -> Mapping[str, bytes]:
    """Apply a verdict to the exact subject versions its verifier was handed."""
    verdict = candidate(attempt)
    verified = attempt.layout.roles[verdict.role].verifies
    if not verified:
        raise ValueError(f"role {verdict.role} verifies no role")
    handed = {role: name for role, name in partners(attempt, exclude=verdict.role).items() if role in verified}
    missing = [role for role in verified if role not in handed]
    if missing:
        raise ValueError(f"job {attempt.job.name}: no handed input for verified roles {', '.join(missing)}")
    answered_correction, answered = correction(attempt)
    findings, judgments = apply_verdict(verdict, answered_correction)
    judge(attempt, verdict, findings, answered=answered)
    for judgment in judgments:
        attempt.judge(handed[judgment.role], outcome=judgment.outcome, scope=judgment.scope,
                      findings=judgment.findings)
    return {}


def artifact_check(attempt: CodeAttempt) -> Mapping[str, bytes]:
    """Validate the role inputs as one snapshot and write the findings; judge nothing."""
    members = snapshot(attempt, {attempt.input_role(name): name for name in attempt.inputs
                                 if attempt.input_role(name) is not None})
    pinned = attempt.frozen_source
    source = frozen_source(pinned, "", members, attempt.layout, job=attempt.job.name) if pinned is not None else None
    return {"findings": check_artifact(members, run_dir=attempt.run_dir, repo=attempt.library.parent,
                                       source=source, type_spec=attempt.type_spec,
                                       criteria=criterion_bytes(attempt))}
