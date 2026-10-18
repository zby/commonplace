"""The checks a code job applies to a model candidate in a typed artifact.

Everything here takes plain values. A `Candidate` carries the candidate at
its role, the partner members it is judged against and the run facts
validation needs (the type's layout and relations, the pinned criteria, the
run values, the artifact directory); nothing in it reaches back to an engine.
The engine's handlers (`handlers`) build one from a code attempt and stage
the judgments these functions return; a workflow script can build one from
files and records.

The functions validate a candidate as a draft at its role against its
partners and the run's pinned criteria, check a frozen source when one
member pins it, check the producer's answers to the refusal it answered,
and scope a judgment over the relations its validation examined.

A refusal's body is Markdown. Its `## Blockers` list holds obligations: the
producer answers each, in order, with `- corrected: ` or `- declined: ` and a
reason. A structural refusal carries the answered refusal's blockers and its
other sections forward, because only the latest refusal is in force.

`apply_verdict` implements the verification protocol: a verifying role's
document has `## Blockers` and `## Limits`, each exactly `none` or a list
with one `- ` entry per finding. With several subjects every blocker starts
with the role it addresses (`- <role>: ...`); with one subject, none does.
A verdict whose Blockers are `none` accepts every handed subject it causes
no finding at. Otherwise each addressed subject is refused with its
blockers, and a subject no blocker addresses is not judged: its gate stays
unsettled until a blocker-free verdict. A subject is also refused, whatever
Blockers says, for verdict-dependent findings: those at its role that appear
with the verdict placed and not without it. A finding the subject shows on
its own belongs to its check, whose refusal carries the subject's answered
blockers forward; repeating it here would replace that refusal. Every
refusal of a subject carries the verdict's Limits.
"""

from __future__ import annotations

import re
from collections.abc import Mapping
from dataclasses import dataclass, field, replace
from pathlib import Path

from commonplace.artifactrun.plan import relation, relation_parts, resolve_dotted
from commonplace.artifactrun.sources import frozen_source_refusals
from commonplace.artifactrun.store import digest
from commonplace.lib.directory_artifact import MANIFEST_NAME, type_manifest
from commonplace.lib.directory_layout import (
    Layout,
    addressee,
    blocker_entries,
    protocol_sections,
)
from commonplace.lib.note_parser import parse_document, section
from commonplace.lib.project_paths import kb_root
from commonplace.lib.type_resolver import CriterionSnapshot
from commonplace.lib.validation import ValidationRun, validate_draft_in_role

ARTIFACT_CHECK_HEADING = "# Artifact check"


def manifest(type_spec: str) -> bytes:
    """A minimal artifact manifest naming the run's type."""
    return type_manifest(type_spec)


@dataclass(frozen=True)
class Candidate:
    """A candidate at its role, the partner members it is judged against, and the run facts.

    `snapshot` holds the present partners at their roles' paths. `source` is
    the frozen source the run may inspect, None when the plan names none or
    the candidate fills that role. `criteria` are the pinned library files
    plus the type's text, keyed by library path. `inputs` are the job's
    declared inputs' bytes, which declared checks read by name. `extensions`
    are the job's declared `checks` and `feedback`, as dotted paths.
    """

    role: str
    data: bytes
    snapshot: dict[str, bytes]
    repo: Path
    source: dict | None
    incumbent: bytes | None = None
    run_dir: Path = field(kw_only=True)
    layout: Layout = field(kw_only=True)
    relations: tuple[tuple[str, str, str], ...] = field(kw_only=True)
    type_spec: str = field(kw_only=True)
    criteria: Mapping[str, bytes] = field(kw_only=True)
    run_values: Mapping[str, str] = field(kw_only=True, default_factory=dict)
    frozen_source: str | None = field(kw_only=True, default=None)
    extensions: Mapping[str, object] = field(kw_only=True, default_factory=dict)
    inputs: Mapping[str, bytes | None] = field(kw_only=True, default_factory=dict)

    @property
    def artifact(self) -> Path:
        """The run's artifact directory, where validation anchors member paths."""
        return self.run_dir / "artifact"

    @property
    def fields(self) -> dict:
        """The candidate's frontmatter; empty when unreadable, which validation reports."""
        try:
            document, _ = parse_document(self.data.decode("utf-8"))
        except UnicodeError:
            return {}
        return (document.frontmatter or {}) if document is not None else {}


@dataclass(frozen=True)
class Correction:
    """What the producer answered: the handed refusal, its answers and its previous version."""

    refusal: bytes | None
    answers: bytes | None
    previous_version: str | None


@dataclass(frozen=True)
class Judgment:
    """A judgment of a handed subject at `role`, for the caller to record."""

    role: str
    outcome: str
    scope: tuple[str, ...]
    findings: str = ""


def source_field(data: bytes) -> dict | None:
    """A member's `source` mapping, or None when it is unreadable or has none."""
    document, error = parse_document(data.decode("utf-8", errors="replace"))
    source = (document.frontmatter or {}).get("source") if document is not None and not error else None
    return source if isinstance(source, dict) else None


def frozen_source(pinned: str | None, role: str, members: Mapping[str, bytes], layout: Layout,
                  *, job: str) -> dict | None:
    """The source the run may inspect: the `source` field of the plan's frozen-source role.

    None when the plan names no frozen source, and for a candidate filling
    that role: `check_candidate` gives such a candidate its own source only
    once the job's declared checks, which bind it to what the run acquired,
    pass. A named role whose member is absent or has no source is an error,
    never a silent unverified check.
    """
    if pinned is None or pinned == role:
        return None
    holder = members.get(layout.path(pinned))
    source = source_field(holder) if holder is not None else None
    if source is None:
        raise TypeError(f"job {job}: the frozen-source member {pinned} has no source field")
    return source


def content_findings(check: Candidate, *, role: str | None = None, data: bytes | None = None,
                    members: dict[str, bytes] | None = None) -> list[str]:
    """Draft-validation failures at a role; warnings and absent partners do not refuse."""
    results = validate_draft_in_role(
        check.artifact, role or check.role,
        check.data if data is None else data, repo_root=check.repo,
        members=check.snapshot if members is None else members, manifest=manifest(check.type_spec),
        criteria=check.criteria, frozen_source=check.source,
        run_values=check.run_values,
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


def extension_findings(check: Candidate) -> list[str]:
    """Reasons from the job's declared checks, each called with the built candidate.

    An entry of the `checks` extension is a dotted path or a mapping with a
    `function`; the inputs a check declares are ordinary job inputs.
    """
    findings = []
    for entry in check.extensions.get("checks", ()):
        path = entry["function"] if isinstance(entry, dict) else entry
        findings += list(resolve_dotted(path)(check))
    return findings


def correction_blockers(refusal: bytes | None, member: str) -> str:
    """Extract preserved blockers; treat unstructured operator findings as one."""
    if refusal is None:
        return "none"
    # The engine's published refusal format: fields as frontmatter, findings as body.
    document, _ = parse_document(refusal.decode("utf-8"))
    findings = (document.body if document is not None else "").strip()
    blockers = protocol_sections(findings)["Blockers"]
    if blockers is not None:
        return blockers or "none"
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
    if previous_version == digest(candidate) and any(line.startswith("- corrected:") for line in entries):
        return ["correction answers: an entry says corrected but the output is identical to its predecessor"]
    return []


def answer_findings(check: Candidate, correction: Correction | None) -> list[str]:
    """The correction findings of a candidate that answered a refusal; none without one."""
    if correction is None:
        return []
    findings = correction_findings(check.data, member=check.role, refusal=correction.refusal,
                                   answers=correction.answers, previous_version=correction.previous_version)
    return ["[correction] " + finding for finding in findings]


def refusal_body(findings: list[str], blockers: str, sections: list[tuple[str, str]] = ()) -> str:
    """A refusal's body: its Findings, its Blockers, then any further sections."""
    body = "## Findings\n\n" + ("\n".join(findings) or "none") + "\n\n## Blockers\n\n" + (blockers or "none") + "\n"
    return body + "".join(f"\n## {title}\n\n{text}\n" for title, text in sections)


def refusal_findings(findings: list[str], *, member: str, answered: bytes | None) -> str:
    """Findings, the answered refusal's blockers, and its other sections carried forward."""
    carried = []
    if answered is not None:
        document, _ = parse_document(answered.decode("utf-8"))
        body = document.body if document is not None else ""
        carried = [(title, section(body, title).strip()) for title in re.findall(r"(?m)^## (.+?)[ \t]*$", body)
                   if title not in ("Findings", "Blockers")]
    return refusal_body(findings, correction_blockers(answered, member), [item for item in carried if item[1]])


def judgment_scope(check: Candidate) -> tuple[str, ...]:
    """The relations a content judgment of the candidate covers.

    The scope is the type's `cites` and `identity` relations from the
    candidate's role to partners in the snapshot. A `verifies` relation is
    never in it: a content check cannot settle a verification gate, which
    only a judgment of the handed subject covers (ADR 114).
    """
    return tuple(name for origin, partner, name in check.relations
                 if origin == check.role and relation_parts(name)[1] != "verifies"
                 and check.layout.path(partner) in check.snapshot)


def check_candidate(check: Candidate, correction: Correction | None = None) -> list[str]:
    """Judge a candidate at its role: content, relations and correction answers.

    The findings refuse the candidate when nonempty. A candidate filling the
    frozen-source role names the source its quotations are checked against:
    its declared checks bind that source to what the run acquired, so only a
    bound candidate's own source is inspected. A declared check may restate a
    finding the standard review made.
    """
    answers = answer_findings(check, correction)
    declared = extension_findings(check)
    if check.frozen_source == check.role:
        if declared:
            return declared + answers
        check = replace(check, source=source_field(check.data))
    return list(dict.fromkeys(review(check) + answers + declared))


def apply_verdict(verdict: Candidate, correction: Correction | None = None,
                  ) -> tuple[list[str], list[Judgment]]:
    """Apply a verdict to the subjects it was handed: its own findings and their judgments.

    The subjects are the roles the verdict's role verifies, read from the
    snapshot; a verified role absent from it was not handed and is not judged.
    A verdict that fails its own check judges nothing. Its own judgment
    covers its cites and identity relations (`judgment_scope`); only the
    subject judgments cover the verifies relations.
    """
    layout = verdict.layout
    verified = layout.roles[verdict.role].verifies
    if not verified:
        raise ValueError(f"role {verdict.role} verifies no role")
    # Review includes the protocol's grammar, a layout finding for a verifying role.
    findings = review(verdict) + answer_findings(verdict, correction) + extension_findings(verdict)
    if findings:
        return findings, []

    document, _ = parse_document(verdict.data.decode("utf-8"))
    sections = protocol_sections(document.body)
    entries = blocker_entries(sections["Blockers"]) if sections["Blockers"] != "none" else []
    limits = sections["Limits"]
    feedback = resolve_dotted(verdict.extensions["feedback"]) if verdict.extensions.get("feedback") else None
    judgments = []
    for role in verified:
        path = layout.path(role)
        if path not in verdict.snapshot:
            continue  # Not handed: nothing to judge.
        alone = content_findings(verdict, role=role, data=verdict.snapshot[path], members=verdict.snapshot)
        beside = content_findings(verdict, role=role, data=verdict.snapshot[path],
                                 members={**verdict.snapshot, layout.path(verdict.role): verdict.data})
        invalid = [finding for finding in beside if finding not in alone]
        own = [entry for entry in entries if len(verified) == 1 or addressee(entry) == role]
        relation_scope = (relation(verdict.role, "verifies", role),)
        if invalid or own:
            packet = refusal_body(invalid, "\n".join(own), [("Limits", limits)])
            if feedback is not None:
                packet += feedback(role, own, verdict)
            judgments.append(Judgment(role, "refused", relation_scope, packet))
        elif not entries:
            judgments.append(Judgment(role, "accepted", relation_scope))
    return [], judgments


def artifact_check(members: Mapping[str, bytes], *, run_dir: Path, repo: Path, source: dict | None,
                   type_spec: str, criteria: Mapping[str, bytes]) -> bytes:
    """Validate the members as one snapshot and write the findings; judge nothing.

    `members` are the present role members at their paths. The findings
    include the artifact-level findings a role's check filters out, so a
    verifier can read them. The result is a document headed
    `# Artifact check` holding `none` or one `- ` line per finding.
    """
    directory = (run_dir / "artifact").resolve()
    run = ValidationRun(
        repo, (), content_overrides={directory / MANIFEST_NAME: manifest(type_spec)},
        member_snapshots={directory: dict(members)},
        criteria=CriterionSnapshot(kb_root(repo), criteria),
        frozen_source=source,
    )
    findings = ["[invocation] " + finding for finding in frozen_source_refusals(source)] if source else []
    findings += [f"{path}: {failure}" for path in sorted(members) for failure in run.validate(directory / path).fails]
    try:
        findings += ["[artifact] " + finding.render() for finding in run.artifact_findings(directory)
                    if not finding.absent and not finding.info]
    except (OSError, UnicodeError, ValueError, TypeError) as exc:
        findings.append(f"[artifact] artifact input cannot be checked: {exc}")
    text = f"{ARTIFACT_CHECK_HEADING}\n\n" + ("\n".join(f"- {finding}" for finding in findings) or "none") + "\n"
    return text.encode("utf-8")
