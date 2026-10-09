"""The checks a code job applies to a model candidate in a typed set.

A check validates the candidate as a draft at its role against a snapshot of
partner members and the run's pinned criteria, checks a frozen source when one
member pins it, checks the producer's answers to the refusal it answered, and
judges the candidate over the relations its validation examined.

A refusal's body is Markdown. Its `## Blockers` list holds obligations: the
producer answers each, in order, with `- corrected: ` or `- declined: ` and a
reason. A structural refusal carries the answered refusal's blockers and its
other sections forward, because only the latest refusal is in force.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path

import yaml

from commonplace.lib.note_parser import parse_document, section
from commonplace.lib.validation import validate_draft_at_slot
from commonplace.setrun.sources import frozen_source_refusals
from commonplace.workflow import CodeAttempt


def criterion_bytes(attempt: CodeAttempt) -> dict[str, bytes]:
    """The job's pinned library files plus the set type fixed at start.

    Missing dependencies stay absent; the closed validator rejects them.
    """
    return {**attempt.read_files(), attempt.type_spec: attempt.type_text.encode("utf-8")}


def manifest(attempt: CodeAttempt) -> bytes:
    """A minimal set manifest naming the run's set type."""
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

    @property
    def fields(self) -> dict:
        """The candidate's frontmatter; empty when unreadable, which validation reports."""
        try:
            document, _ = parse_document(self.data.decode("utf-8"))
        except UnicodeError:
            return {}
        return (document.frontmatter or {}) if document is not None else {}


def snapshot(attempt: CodeAttempt, partners: tuple[str, ...], *, seen: bool = False) -> dict[str, bytes]:
    """Partner members at their set paths, from inputs named by role or handed `<role>-seen`."""
    members = {}
    for partner in partners:
        data = attempt.read(f"{partner}-seen" if seen else partner)
        if data is not None:
            members[attempt.layout.path(partner)] = data
    return members


def frozen_source(attempt: CodeAttempt, members: dict[str, bytes], role: str) -> dict:
    """The `source` field of the member at ``role``, which pins the frozen source."""
    document, error = parse_document(members[attempt.layout.path(role)].decode("utf-8"))
    source = (document.frontmatter or {}).get("source") if document is not None and not error else None
    if not isinstance(source, dict):
        raise TypeError(f"checks require a {role} member with a frozen source")
    return source


def candidate(attempt: CodeAttempt, role: str, partners: tuple[str, ...], *, repo: Path,
              seen: bool = False, source_role: str | None = None) -> Candidate:
    """The `candidate` input at ``role`` with its partners, validated in project ``repo``.

    ``source_role`` names the member whose `source` pins the frozen source.
    """
    members = snapshot(attempt, partners, seen=seen)
    source = frozen_source(attempt, members, source_role) if source_role in partners else None
    return Candidate(attempt, role, attempt.read("candidate"), members, repo, source)


def content_reasons(check: Candidate, *, role: str | None = None, data: bytes | None = None,
                    members: dict[str, bytes] | None = None) -> list[str]:
    """Draft-validation failures at a role; warnings and absent partners do not refuse."""
    findings = validate_draft_at_slot(
        check.attempt.run_dir / "set", check.attempt.layout.path(role or check.role),
        check.data if data is None else data, repo_root=check.repo,
        members=check.snapshot if members is None else members, manifest=manifest(check.attempt),
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


def blocker_entries(blockers: str) -> list[str]:
    """The `- ` entries of a Blockers list, continuation lines joined; `none` has none."""
    entries = []
    for line in blockers.splitlines():
        if line.startswith("- "):
            entries.append(line)
        elif entries and line.strip():
            entries[-1] += "\n" + line
    return entries


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


def answer_reasons(check: Candidate, *, record: str, output: str) -> list[str]:
    """Correction answers to the refusal the producer answered."""
    producer = json.loads(check.attempt.read(record))
    return ["[correction] " + reason for reason in correction_findings(
        check.data, member=check.role, refusal=check.attempt.read("answered-refusal"),
        answers=check.attempt.read("answers"), previous_version=producer["previous_outputs"].get(output),
    )]


def refusal_findings(reasons: list[str], *, member: str, answered: bytes | None) -> str:
    """Findings, the answered refusal's blockers, and its other sections carried forward."""
    packet = "## Findings\n\n" + "\n".join(reasons) + "\n\n## Blockers\n\n" + correction_blockers(answered, member) + "\n"
    if answered is not None:
        document, _ = parse_document(answered.decode("utf-8"))
        body = document.body if document is not None else ""
        for title in re.findall(r"(?m)^## (.+?)[ \t]*$", body):
            if title not in ("Findings", "Blockers"):
                text = section(body, title).strip()
                if text:
                    packet += f"\n## {title}\n\n{text}\n"
    return packet


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
