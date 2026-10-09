"""Standard handlers for the code jobs most plans repeat.

A plan names them by dotted path like any handler. Each learns what it
judges from the job's declared inputs, never from per-job configuration:

- the candidate is the input named `candidate`; its role is the role of the
  job whose primary output it is;
- the partners are the other inputs that hold a role by declaration, each
  placed at its role's path in the snapshot the candidate is validated
  against;
- the producer's correction answers are checked when the job declares the
  producer's attempt record: the answered refusal is that record's handed
  `refusal`, and the answers are the producer's other declared output.

Validation runs in the project the run's library belongs to, against the
job's pinned criteria.
"""

from __future__ import annotations

import json
from collections.abc import Mapping

from commonplace.artifactrun import CodeAttempt
from commonplace.artifactrun.checks import (
    Candidate,
    correction_findings,
    judge,
    review,
)

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


def candidate(attempt: CodeAttempt) -> Candidate:
    """The `candidate` input at its declared role, with its partners present."""
    role = attempt.input_role(CANDIDATE)
    if role is None:
        raise ValueError(f"job {attempt.job.name}: input {CANDIDATE} must be a role-filling job's primary output")
    data = attempt.read(CANDIDATE)
    if data is None:
        raise ValueError(f"job {attempt.job.name}: no {CANDIDATE} to check")
    members = {}
    for partner, name in partners(attempt, exclude=role).items():
        member = attempt.read(name)
        if member is not None:
            members[attempt.layout.path(partner)] = member
    return Candidate(attempt, role, data, members, attempt.library.parent, None)


def _named(attempt: CodeAttempt, address: str, source: str) -> str | None:
    return next((name for name, spec in attempt.inputs.items()
                 if spec.address == address and spec.source == source), None)


def correction(attempt: CodeAttempt, check: Candidate) -> tuple[list[str], str | None]:
    """Answer findings and the name of the input holding the answered refusal.

    Nothing is checked when the job does not declare the producer's attempt
    record or its answers output.
    """
    producer, _, output = attempt.inputs[CANDIDATE].source.partition(":")
    record = _named(attempt, "attempt", producer)
    if record is None:
        return [], None
    answered = _named(attempt, "handed", f"{record}:refusal")
    answers = next((name for name, spec in attempt.inputs.items()
                    if spec.address == "output" and name != CANDIDATE
                    and attempt.producer(name) == producer), None)
    record_data = attempt.read(record)
    if answers is None or record_data is None:
        return [], answered
    previous = json.loads(record_data)["previous_outputs"].get(output)
    findings = correction_findings(
        check.data, member=check.role, refusal=attempt.read(answered) if answered else None,
        answers=attempt.read(answers), previous_version=previous,
    )
    return ["[correction] " + finding for finding in findings], answered


def check(attempt: CodeAttempt) -> Mapping[str, bytes]:
    """Judge a candidate at its role: content, relations and correction answers.

    The judgment covers the type's cites and identity relations to the
    partners present; it never covers a verifies relation.
    """
    built = candidate(attempt)
    answers, answered = correction(attempt, built)
    judge(built, review(built) + answers, answered=answered)
    return {}
