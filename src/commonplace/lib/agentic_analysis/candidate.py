"""The shared skeleton of the analysis checks that judge a model candidate.

A check validates the candidate as a draft at its role against a snapshot of
partner members and the pinned criteria, checks the boundary's frozen source
and the producer's correction answers, then judges the candidate. Handlers
add only their domain checks. Identity fields are type relations, so draft
validation enforces them against the snapshot's boundary, which the boundary
check bound to the opening.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from commonplace.lib.agentic_analysis.boundary import frozen_source_refusals
from commonplace.lib.agentic_analysis.checks import (
    correction_findings,
    refusal_findings,
)
from commonplace.lib.agentic_analysis.sets import SET_TYPE
from commonplace.lib.agentic_analysis.validation import criterion_bytes
from commonplace.lib.agentic_analysis.worktree import source_checkout
from commonplace.lib.note_parser import parse_document
from commonplace.lib.validation import validate_draft_at_slot
from commonplace.workflow import CodeAttempt

MANIFEST = f"type: {SET_TYPE}\n".encode()


@dataclass(frozen=True)
class Candidate:
    """A candidate at its role and the partner members it is judged against."""

    attempt: CodeAttempt
    role: str
    data: bytes
    snapshot: dict[str, bytes]
    repo: Path
    source: dict | None

    @property
    def fields(self) -> dict:
        """The candidate's frontmatter; empty when unreadable, which validation reports."""
        try:
            document, _ = parse_document(self.data.decode("utf-8"))
        except UnicodeError:
            return {}
        return (document.frontmatter or {}) if document is not None else {}


def checkout(attempt: CodeAttempt) -> Path:
    repo = source_checkout(attempt.run_dir)
    if repo is None:
        raise ValueError("analysis jobs must run inside their analysis checkout")
    return repo


def snapshot(attempt: CodeAttempt, partners: tuple[str, ...], *, seen: bool = False) -> dict[str, bytes]:
    """Partner members at their set paths, from inputs named by role or handed `<role>-seen`."""
    members = {}
    for partner in partners:
        data = attempt.read(f"{partner}-seen" if seen else partner)
        if data is not None:
            members[attempt.layout.path(partner)] = data
    return members


def frozen_source(attempt: CodeAttempt, members: dict[str, bytes]) -> dict:
    boundary, error = parse_document(members[attempt.layout.path("boundary")].decode("utf-8"))
    source = (boundary.frontmatter or {}).get("source") if boundary is not None and not error else None
    if not isinstance(source, dict):
        raise TypeError("analysis checks require a boundary with a frozen source")
    return source


def candidate(attempt: CodeAttempt, role: str, partners: tuple[str, ...], *, seen: bool = False) -> Candidate:
    members = snapshot(attempt, partners, seen=seen)
    source = frozen_source(attempt, members) if "boundary" in partners else None
    return Candidate(attempt, role, attempt.read("candidate"), members, checkout(attempt), source)


def content_reasons(check: Candidate, *, role: str | None = None, data: bytes | None = None,
                    members: dict[str, bytes] | None = None) -> list[str]:
    """Draft-validation failures at a role; warnings and absent partners do not refuse."""
    findings = validate_draft_at_slot(
        check.attempt.run_dir / "set", check.attempt.layout.path(role or check.role),
        check.data if data is None else data, repo_root=check.repo,
        members=check.snapshot if members is None else members, manifest=MANIFEST,
        criteria=criterion_bytes(check.attempt), frozen_source=check.source,
    )
    return ["[set] " + finding.render() for finding in findings
            if not finding.info and not finding.warn and not finding.absent]


def review(check: Candidate) -> list[str]:
    """Content failures and frozen-source refusals."""
    reasons = content_reasons(check)
    if check.source is not None:
        reasons += ["[invocation] " + reason for reason in frozen_source_refusals(check.source)]
    return reasons


def answer_reasons(check: Candidate, *, record: str, output: str, incumbent: str | None = None) -> list[str]:
    """Correction answers to the refusal the producer answered."""
    producer = json.loads(check.attempt.read(record))
    return ["[correction] " + reason for reason in correction_findings(
        check.data, member=check.role, incumbent=check.attempt.read(incumbent) if incumbent else None,
        refusal=check.attempt.read("answered-refusal"), answers=check.attempt.read("answers"),
        previous_version=producer["previous_outputs"].get(output),
    )]


def judge(check: Candidate, reasons: list[str], *, subjects: tuple[str, ...] = ()) -> None:
    """Judge the candidate over the relations its validation examined.

    The scope is the type's relations from the candidate's role to partners in
    the snapshot. A verdict leaves out its subjects: its content acceptance
    does not cover their semantic gates, which are judged separately.
    """
    layout = check.attempt.layout
    scope = tuple(name for origin, partner, name in check.attempt.relations
                  if origin == check.role and partner not in subjects
                  and layout.path(partner) in check.snapshot)
    findings = refusal_findings(
        reasons, member=check.role, answered=check.attempt.read("answered-refusal"),
    ) if reasons else ""
    check.attempt.judge("candidate", outcome="refused" if reasons else "accepted", scope=scope, findings=findings)
