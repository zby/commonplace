"""Opt-in reconciliation checks and record verdict application, not CLI bindings.

Snapshots are made solely from declared inputs. Structural checks cover content
relations; only a valid, blocker-free verifier verdict settles semantic gates.
Environment guards are the same consumer-owned guards as the analyst checks.
"""

from __future__ import annotations

import json

from commonplace.lib.agentic_analysis.boundary import frozen_source_refusals
from commonplace.lib.agentic_analysis.checks import refusal_findings
from commonplace.lib.agentic_analysis.handlers import (
    _locate,
)
from commonplace.lib.agentic_analysis.records import (
    record_declaration,
    record_references,
    section,
)
from commonplace.lib.agentic_analysis.sets import SET_TYPE
from commonplace.lib.agentic_analysis.validation import criterion_bytes
from commonplace.lib.directory_artifact import MANIFEST_NAME
from commonplace.lib.note_parser import parse_document
from commonplace.lib.project_paths import kb_root
from commonplace.lib.type_resolver import CriterionSnapshot
from commonplace.lib.validation import ValidationRun, validate_draft_at_slot
from commonplace.workflow import CodeAttempt

ANALYSTS = ("runtime", "memory", "epistemic")
RECORDS = (*ANALYSTS, "reconciliation")
PARTNERS = ("boundary", *RECORDS)
MANIFEST = f"type: {SET_TYPE}\n".encode()


def _required(attempt: CodeAttempt, name: str) -> bytes:
    data = attempt.read(name)
    if data is None:
        raise ValueError(f"record check requires {name}")
    return data


def _path(attempt: CodeAttempt, role: str) -> str:
    return attempt.layout.path(role)


def _snapshot(attempt: CodeAttempt, roles: tuple[str, ...], suffix: str = "") -> dict[str, bytes]:
    return {_path(attempt, role): _required(attempt, role + suffix) for role in roles}


def _source(snapshot: dict[str, bytes]) -> dict:
    boundary, error = parse_document(snapshot["boundary.md"].decode("utf-8"))
    if boundary is None or error or not isinstance((boundary.frontmatter or {}).get("source"), dict):
        raise ValueError("record check requires a boundary with a frozen source")
    return boundary.frontmatter["source"]


def _source_reasons(snapshot: dict[str, bytes]) -> list[str]:
    return ["[invocation] " + reason for reason in frozen_source_refusals(_source(snapshot))]


def _candidate_reasons(attempt, repo, metadata, role, candidate, snapshot):
    findings = validate_draft_at_slot(
        attempt.run_dir / "set", _path(attempt, role), candidate,
        repo_root=repo, members=snapshot, manifest=MANIFEST,
        criteria=criterion_bytes(attempt), frozen_source=_source(snapshot),
    )
    reasons = ["[set] " + finding.render() for finding in findings
               if not finding.info and not finding.warn and not finding.absent]
    reasons += _source_reasons(snapshot)
    try:
        document, _ = parse_document(candidate.decode("utf-8"))
    except UnicodeError:
        document = None
    if document is not None and (document.frontmatter or {}).get("run-id") != metadata["run-id"]:
        reasons.append("[invocation] run-id must be the opening's run identity")
    return reasons


def check_reconcile(attempt: CodeAttempt) -> dict[str, bytes]:
    """Check reconciliation content against pinned reports, without semantic acceptance."""
    metadata, repo = _locate(attempt)
    candidate = _required(attempt, "candidate")
    snapshot = _snapshot(attempt, ("boundary", *ANALYSTS))
    reasons = _candidate_reasons(attempt, repo, metadata, "reconciliation", candidate, snapshot)
    answered = attempt.read("answered-refusal")
    attempt.judge(
        "candidate", outcome="refused" if reasons else "accepted",
        scope=tuple(f"reconciliation:cites:{role}" for role in ("boundary", *ANALYSTS))
        + ("reconciliation:identity:boundary",),
        findings=refusal_findings(reasons, member="reconciliation", answered=answered) if reasons else "",
    )
    return {}


def set_check(attempt: CodeAttempt) -> dict[str, bytes]:
    """Set_check returns record content and relation findings from one pinned snapshot."""
    _, repo = _locate(attempt)
    snapshot = _snapshot(attempt, PARTNERS)
    directory = (attempt.run_dir / "set").resolve()
    run = ValidationRun(
        repo, (), content_overrides={directory / MANIFEST_NAME: MANIFEST},
        member_snapshots={directory: snapshot},
        criteria=CriterionSnapshot(kb_root(repo), criterion_bytes(attempt)),
        frozen_source=_source(snapshot),
    )
    reasons = _source_reasons(snapshot)
    # Ordinary member content checks are not replaced by directory relation checks.
    for role in RECORDS:
        result = run.validate(directory / _path(attempt, role))
        reasons += [f"{_path(attempt, role)}: {failure}" for failure in result.fails]
    try:
        reasons += ["[set] " + finding.render() for finding in run.artifact_findings(directory)
                    if not finding.absent and not finding.info]
    except (OSError, UnicodeError, ValueError, TypeError) as exc:
        reasons.append(f"[set] set input cannot be checked: {exc}")
    text = "# Record set check\n\n" + ("\n".join(f"- {reason}" for reason in reasons) or "none") + "\n"
    return {"findings": text.encode("utf-8")}


def _blockers(text: str) -> tuple[list[str], list[str]]:
    """Require explicit routing grammar, including nonempty findings and continuations."""
    value = section(text, "Blockers").strip()
    if value == "none":
        return [], []
    lines = [line for line in value.splitlines() if line.strip()]
    if not lines or not lines[0].startswith("- ") or any(
        not line.startswith(("- ", " ", "\t")) for line in lines
    ):
        return [], ["Blockers must be exactly none or a Markdown list"]
    entries = _entries(value)
    if any(_addressee(entry) is None for entry in entries):
        return [], ["each record blocker needs runtime:, memory:, epistemic: or reconciliation: followed by a finding"]
    return entries, []


def _entries(value: str) -> list[str]:
    entries = []
    for line in value.splitlines():
        if line.startswith("- "):
            entries.append(line)
        elif entries and line.strip():
            entries[-1] += "\n" + line
    return entries


def _addressee(entry: str) -> str | None:
    for role in RECORDS:
        if entry.startswith(f"- {role}: ") and entry[len(role) + 4:].strip():
            return role
    return None


def _feedback(role: str, verifier: str, entries: list[str], bodies: dict[str, str]) -> str:
    own = [entry for entry in entries if _addressee(entry) == role]
    fragments = []
    prefixes = {"runtime": "RT-", "memory": "MEM-", "epistemic": "EPI-"}
    for identifier in sorted(record_references("\n".join(own))):
        for peer, prefix in prefixes.items():
            if peer != role and identifier.startswith(prefix):
                declaration = record_declaration(bodies[peer], identifier)
                if declaration is not None:
                    fragments.append(f"From the {peer} report:\n\n{declaration}")
    return (
        f"# Correction feedback for the {role} report\n\n"
        f"The record verification attempt `{verifier}` addressed these blockers to this report.\n\n"
        "## Blockers\n\n" + "\n".join(own)
        + "\n\n## Cited records from other reports\n\n" + ("\n".join(fragments) or "none\n")
    )


def _set_check_failed(data: bytes) -> bool:
    text = data.decode("utf-8").strip()
    heading = "# Record set check"
    if not text.startswith(heading + "\n"):
        raise ValueError("handed set-check must be a Record set check document")
    body = text[len(heading):].strip()
    if body == "none":
        return False
    if not body or not body.startswith("- "):
        raise ValueError("handed set-check must contain none or findings")
    return True


def apply_verify(attempt: CodeAttempt) -> dict[str, bytes]:
    """Apply a verdict only to the exact subjects its completed verifier was handed.

    The declaration must include verifier-attempt even when verdict bytes match
    an earlier verdict. The engine owns late-subject installation and refusal
    delivery. No explicit overrides or current-member discovery are used here.
    """
    metadata, repo = _locate(attempt)
    producer = json.loads(_required(attempt, "verifier-attempt"))
    candidate = _required(attempt, "candidate")
    snapshot = _snapshot(attempt, PARTNERS, "-seen")
    reasons = _candidate_reasons(attempt, repo, metadata, "record-verification", candidate, snapshot)
    try:
        entries, malformed = _blockers(candidate.decode("utf-8"))
    except UnicodeError:
        entries, malformed = [], ["verification must be UTF-8 text"]
    reasons += malformed
    if _set_check_failed(_required(attempt, "set-check-seen")) and not entries:
        reasons.append("structural failures require explicit blockers (code requires at least one; the verifier must address every finding)")
    if reasons:
        attempt.judge("candidate", outcome="refused", findings="\n".join(reasons))
        return {}
    # A verifier with blockers is a valid verdict document, not an acceptance
    # of the defective reports. Its content acceptance must not cover their gates.
    scope = ("record-verification:cites:boundary", "record-verification:identity:boundary")
    attempt.judge("candidate", outcome="accepted", scope=scope)
    if entries:
        bodies = {role: snapshot[_path(attempt, role)].decode("utf-8") for role in ANALYSTS}
        owners = {_addressee(entry) for entry in entries}
        for role in RECORDS:
            if role in owners:
                attempt.judge(
                    role + "-seen", outcome="refused",
                    scope=(f"record-verification:cites:{role}",),
                    findings=_feedback(role, producer["id"], entries, bodies),
                )
    else:
        for role in RECORDS:
            attempt.judge(role + "-seen", outcome="accepted", scope=(f"record-verification:cites:{role}",))
    return {}
