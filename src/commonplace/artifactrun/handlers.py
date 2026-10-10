"""Standard handlers for the code jobs most plans repeat.

A plan names them by dotted path like any handler. Each learns what it
judges from the job's declared inputs, never from per-job configuration:

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

`apply_verification` implements the verification protocol: a verifying role's
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

import importlib
import json
import re
from collections.abc import Callable, Mapping
from dataclasses import replace

from commonplace.artifactrun import CodeAttempt
from commonplace.artifactrun.checks import (
    Candidate,
    blocker_entries,
    content_findings,
    correction_findings,
    criterion_bytes,
    judge,
    manifest,
    review,
)
from commonplace.artifactrun.sources import frozen_source_refusals
from commonplace.lib.directory_artifact import MANIFEST_NAME
from commonplace.lib.note_parser import parse_document
from commonplace.lib.project_paths import kb_root
from commonplace.lib.type_resolver import CriterionSnapshot
from commonplace.lib.validation import ValidationRun

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
    # The role's accepted version, when the job reads it: a correction keeps its declarations.
    incumbent = next((attempt.read(name) for name, spec in attempt.inputs.items()
                      if spec.address == "role" and spec.source == role), None)
    return Candidate(attempt, role, data, members, attempt.library.parent,
                     frozen_source(attempt, role, members), incumbent)


def _source_field(data: bytes) -> dict | None:
    document, error = parse_document(data.decode("utf-8", errors="replace"))
    source = (document.frontmatter or {}).get("source") if document is not None and not error else None
    return source if isinstance(source, dict) else None


def frozen_source(attempt: CodeAttempt, role: str, members: Mapping[str, bytes]) -> dict | None:
    """The source the run may inspect: the `source` field of the `frozen-source` option's role.

    None when the plan names no frozen source, and for a candidate filling
    that role: `check` gives such a candidate its own source only once the
    job's declared checks, which bind it to what the run acquired, pass. A
    named role whose member is absent or has no source is an error, never a
    silent unverified check.
    """
    pinned = attempt.frozen_source
    if pinned is None or pinned == role:
        return None
    holder = members.get(attempt.layout.path(pinned))
    source = _source_field(holder) if holder is not None else None
    if source is None:
        raise TypeError(f"job {attempt.job.name}: the frozen-source member {pinned} has no source field")
    return source


def _resolve(path: str) -> Callable:
    module, _, attribute = path.rpartition(".")
    return getattr(importlib.import_module(module), attribute)


def extension_findings(check: Candidate) -> list[str]:
    """Reasons from the job's declared checks, each called with the built candidate.

    An entry of the `checks` option is a dotted path or a mapping with a
    `function`; the inputs a check declares are ordinary job inputs.
    """
    findings = []
    for entry in check.attempt.extensions.get("checks", ()):
        path = entry["function"] if isinstance(entry, dict) else entry
        findings += list(_resolve(path)(check))
    return findings


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
    declared = extension_findings(built)
    if attempt.frozen_source == built.role:
        # The candidate names the source its quotations are checked against.
        # Its declared checks bind that source to what the run acquired; only
        # a bound candidate's own source is inspected.
        if declared:
            judge(built, declared + answers, answered=answered)
            return {}
        built = replace(built, source=_source_field(built.data))
    # A declared check may restate a finding the standard review made.
    findings = list(dict.fromkeys(review(built) + answers + declared))
    judge(built, findings, answered=answered)
    return {}


PROTOCOL_SECTIONS = ("Blockers", "Limits")


def _sections(body: str) -> dict[str, str | None]:
    """Each protocol section's text; None when its heading is absent."""
    found = {}
    for title in PROTOCOL_SECTIONS:
        match = re.search(rf"(?ms)^## {title}[ \t]*\n(.*?)(?=^## |\Z)", body)
        found[title] = match[1].strip() if match else None
    return found


def protocol_findings(verdict: bytes, subjects: tuple[str, ...]) -> list[str]:
    """Why a verdict does not follow the verification protocol for ``subjects``."""
    document, error = parse_document(verdict.decode("utf-8", errors="replace"))
    if document is None:
        return [f"[protocol] verdict cannot be read: {error}"]
    findings = []
    for title, text in _sections(document.body).items():
        if text is None:
            findings.append(f"[protocol] ## {title} is missing")
        elif text != "none" and any(line.strip() and not line.startswith(("- ", " ", "\t"))
                                    for line in text.splitlines()) or text != "none" and not text.startswith("- "):
            findings.append(f"[protocol] ## {title} must be exactly none or a list of - entries")
    blockers = _sections(document.body)["Blockers"]
    if blockers and blockers != "none" and len(subjects) > 1:
        for entry in blocker_entries(blockers):
            if addressee(entry) not in subjects:
                findings.append(f"[protocol] blocker addresses none of {', '.join(subjects)}: {entry.splitlines()[0]}")
    return findings


def addressee(entry: str) -> str:
    """The role a `- <role>: ...` blocker addresses."""
    return entry[2:].partition(":")[0].strip()


def apply_verification(attempt: CodeAttempt) -> Mapping[str, bytes]:
    """Apply a verdict to the exact subject versions its verifier was handed.

    The candidate is the verdict at the verifier's role; the subjects are the
    roles that role verifies, read from the handed inputs. The verdict's own
    judgment covers its cites and identity relations; only the subject
    judgments cover the verifies relations.
    """
    verdict = candidate(attempt)
    layout = attempt.layout
    verified = layout.roles[verdict.role].verifies
    if not verified:
        raise ValueError(f"role {verdict.role} verifies no role")
    handed = {role: name for role, name in partners(attempt, exclude=verdict.role).items() if role in verified}
    missing = [role for role in verified if role not in handed]
    if missing:
        raise ValueError(f"job {attempt.job.name}: no handed input for verified roles {', '.join(missing)}")
    answers, answered = correction(attempt, verdict)
    findings = review(verdict) + answers + protocol_findings(verdict.data, verified) + extension_findings(verdict)
    judge(verdict, findings, answered=answered)
    if findings:
        return {}  # A verdict that fails its own check judges nothing.

    document, _ = parse_document(verdict.data.decode("utf-8"))
    sections = _sections(document.body)
    entries = blocker_entries(sections["Blockers"]) if sections["Blockers"] != "none" else []
    limits = sections["Limits"]
    feedback = _resolve(attempt.extensions["feedback"]) if attempt.extensions.get("feedback") else None
    for role in verified:
        path = layout.path(role)
        if path not in verdict.snapshot:
            continue  # Not handed: nothing to judge.
        alone = content_findings(verdict, role=role, data=verdict.snapshot[path], members=verdict.snapshot)
        beside = content_findings(verdict, role=role, data=verdict.snapshot[path],
                                 members={**verdict.snapshot, layout.path(verdict.role): verdict.data})
        invalid = [finding for finding in beside if finding not in alone]
        own = [entry for entry in entries if len(verified) == 1 or addressee(entry) == role]
        relation = (f"{verdict.role}:verifies:{role}",)
        if invalid or own:
            packet = ("## Findings\n\n" + ("\n".join(invalid) or "none")
                      + "\n\n## Blockers\n\n" + ("\n".join(own) or "none")
                      + "\n\n## Limits\n\n" + limits + "\n")
            if feedback is not None:
                packet += feedback(role, own, verdict)
            attempt.judge(handed[role], outcome="refused", scope=relation, findings=packet)
        elif not entries:
            attempt.judge(handed[role], outcome="accepted", scope=relation)
    return {}


ARTIFACT_CHECK_HEADING = "# Artifact check"


def artifact_check(attempt: CodeAttempt) -> Mapping[str, bytes]:
    """Validate the role inputs as one snapshot and write the findings; judge nothing.

    The findings include the artifact-level findings a role's check filters
    out, so a verifier can read them. The output `findings` is a document
    headed `# Artifact check` holding `none` or one `- ` line per finding.
    """
    layout = attempt.layout
    members = {}
    for name in attempt.inputs:
        role = attempt.input_role(name)
        data = attempt.read(name) if role is not None else None
        if data is not None:
            members[layout.path(role)] = data
    directory = (attempt.run_dir / "artifact").resolve()
    repo = attempt.library.parent
    pinned = attempt.frozen_source
    source = frozen_source(attempt, "", members) if pinned is not None else None
    run = ValidationRun(
        repo, (), content_overrides={directory / MANIFEST_NAME: manifest(attempt)},
        member_snapshots={directory: members},
        criteria=CriterionSnapshot(kb_root(repo), criterion_bytes(attempt)),
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
    return {"findings": text.encode("utf-8")}
