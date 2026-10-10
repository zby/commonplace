"""The checks a code job applies to a model candidate in a typed artifact.

The standard handlers (`handlers`) build a `Candidate` from a job's declared
inputs; these functions validate it as a draft at its role against its
partners and the run's pinned criteria, check a frozen source when one
member pins it, check the producer's answers to the refusal it answered,
and judge it over the relations its validation examined.

A refusal's body is Markdown. Its `## Blockers` list holds obligations: the
producer answers each, in order, with `- corrected: ` or `- declined: ` and a
reason. A structural refusal carries the answered refusal's blockers and its
other sections forward, because only the latest refusal is in force.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path

import yaml

from commonplace.artifactrun import CodeAttempt
from commonplace.artifactrun.plan import relation_parts
from commonplace.artifactrun.sources import frozen_source_refusals
from commonplace.lib.directory_layout import blocker_entries
from commonplace.lib.note_parser import parse_document, section
from commonplace.lib.validation import validate_draft_in_role


def criterion_bytes(attempt: CodeAttempt) -> dict[str, bytes]:
    """The job's pinned library files plus the type fixed at start.

    Missing dependencies stay absent; the closed validator rejects them.
    """
    return {**attempt.read_files(), attempt.type_spec: attempt.type_text.encode("utf-8")}


def manifest(attempt: CodeAttempt) -> bytes:
    """A minimal artifact manifest naming the run's type."""
    return yaml.safe_dump({"type": attempt.type_spec}).encode()


@dataclass(frozen=True)
class Candidate:
    """A candidate at its role and the partner members it is judged against."""

    attempt: CodeAttempt
    role: str
    data: bytes
    snapshot: dict[str, bytes]
    repo: Path
    source: dict | None
    incumbent: bytes | None = None

    @property
    def fields(self) -> dict:
        """The candidate's frontmatter; empty when unreadable, which validation reports."""
        try:
            document, _ = parse_document(self.data.decode("utf-8"))
        except UnicodeError:
            return {}
        return (document.frontmatter or {}) if document is not None else {}


def content_findings(check: Candidate, *, role: str | None = None, data: bytes | None = None,
                    members: dict[str, bytes] | None = None) -> list[str]:
    """Draft-validation failures at a role; warnings and absent partners do not refuse."""
    results = validate_draft_in_role(
        check.attempt.run_dir / "artifact", role or check.role,
        check.data if data is None else data, repo_root=check.repo,
        members=check.snapshot if members is None else members, manifest=manifest(check.attempt),
        criteria=criterion_bytes(check.attempt), frozen_source=check.source,
        run_values=check.attempt.run_values,
        incumbent=check.incumbent if role in (None, check.role) and data is None else None,
    )
    return ["[artifact] " + finding.render() for finding in results
            if not finding.info and not finding.warn and not finding.absent]


def review(check: Candidate) -> list[str]:
    """Content failures and frozen-source refusals."""
    findings = content_findings(check)
    if check.source is not None:
        findings += ["[invocation] " + refusal for refusal in frozen_source_refusals(check.source)]
    return findings


def correction_blockers(refusal: bytes | None, member: str) -> str:
    """Extract preserved blockers; treat unstructured operator findings as one."""
    if refusal is None:
        return "none"
    # The engine's published refusal format: fields as frontmatter, findings as body.
    document, _ = parse_document(refusal.decode("utf-8"))
    findings = (document.body if document is not None else "").strip()
    if re.search(r"(?m)^## Blockers[ \t]*$", findings):
        return section(findings, "Blockers").strip() or "none"
    if not findings:
        return "none"
    lines = findings.splitlines()
    return f"- {member}: {lines[0]}" + "".join(f"\n  {line}" for line in lines[1:])


def correction_findings(candidate: bytes, *, member: str, refusal: bytes | None,
                        answers: bytes | None, previous_version: str | None = None) -> list[str]:
    """Check the answers to the exact handed refusal."""
    wanted = len(blocker_entries(correction_blockers(refusal, member)))
    try:
        answer_text = "" if answers is None else answers.decode("utf-8")
    except UnicodeError:
        return ["correction answers: output-answers must be UTF-8 text"]
    entries = [line for line in answer_text.splitlines() if line.startswith("- ")]
    if len(entries) != wanted or any(re.match(r"- (corrected|declined): \S", line) is None for line in entries):
        return [(
            f"correction answers: output-answers needs exactly {wanted} entries in blocker order, "
            "each starting `- corrected: ` or `- declined: ` with its reason"
        )]
    if previous_version == hashlib.sha256(candidate).hexdigest() and any(line.startswith("- corrected:") for line in entries):
        return ["correction answers: an entry says corrected but the output is identical to its predecessor"]
    return []


def refusal_findings(findings: list[str], *, member: str, answered: bytes | None) -> str:
    """Findings, the answered refusal's blockers, and its other sections carried forward."""
    packet = "## Findings\n\n" + "\n".join(findings) + "\n\n## Blockers\n\n" + correction_blockers(answered, member) + "\n"
    if answered is not None:
        document, _ = parse_document(answered.decode("utf-8"))
        body = document.body if document is not None else ""
        for title in re.findall(r"(?m)^## (.+?)[ \t]*$", body):
            if title not in ("Findings", "Blockers"):
                text = section(body, title).strip()
                if text:
                    packet += f"\n## {title}\n\n{text}\n"
    return packet


def judge(check: Candidate, findings: list[str], *, answered: str | None = "answered-refusal") -> None:
    """Judge the candidate over the relations its validation examined.

    The scope is the type's `cites` and `identity` relations from the
    candidate's role to partners in the snapshot. A `verifies` relation is
    never in it: a content check cannot settle a verification gate, which
    only a judgment of the handed subject covers (ADR 114). ``answered``
    names the input holding the refusal the producer answered, or None.
    """
    layout = check.attempt.layout
    scope = tuple(name for origin, partner, name in check.attempt.relations
                  if origin == check.role and relation_parts(name)[1] != "verifies"
                  and layout.path(partner) in check.snapshot)
    packet = refusal_findings(
        findings, member=check.role, answered=check.attempt.read(answered) if answered else None,
    ) if findings else ""
    check.attempt.judge("candidate", outcome="refused" if findings else "accepted", scope=scope, findings=packet)
