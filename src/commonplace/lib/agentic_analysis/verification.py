"""Reconciliation checks, the record check and record verdict application.

Snapshots are made solely from declared inputs. Structural checks cover content
relations; only a valid, blocker-free verifier verdict settles semantic gates.
"""

from __future__ import annotations

import json

from commonplace.artifactrun import CodeAttempt
from commonplace.artifactrun.checks import (
    Candidate,
    blocker_entries,
    candidate,
    criterion_bytes,
    frozen_source,
    judge,
    manifest,
    review,
    snapshot,
)
from commonplace.artifactrun.handlers import SET_CHECK_HEADING
from commonplace.artifactrun.sources import frozen_source_refusals
from commonplace.lib.agentic_analysis.guards import checkout
from commonplace.lib.agentic_analysis.records import (
    record_declaration,
    record_references,
)
from commonplace.lib.directory_artifact import MANIFEST_NAME
from commonplace.lib.note_parser import section
from commonplace.lib.project_paths import kb_root
from commonplace.lib.type_resolver import CriterionSnapshot
from commonplace.lib.validation import ValidationRun

ANALYSTS = ("runtime", "memory", "epistemic")
RECORDS = (*ANALYSTS, "reconciliation")
PARTNERS = ("boundary", *RECORDS)


def check_reconcile(attempt: CodeAttempt) -> dict[str, bytes]:
    """Check reconciliation content against pinned reports, without semantic acceptance."""
    check = candidate(attempt, "reconciliation", ("boundary", *ANALYSTS), repo=checkout(attempt.run_dir),
                      source_role="boundary")
    judge(check, review(check))
    return {}


def record_check(attempt: CodeAttempt) -> dict[str, bytes]:
    """Record_check returns record content and relation findings from one pinned snapshot."""
    members = snapshot(attempt, PARTNERS)
    source = frozen_source(attempt, members, "boundary")
    directory = (attempt.run_dir / "artifact").resolve()
    repo = checkout(attempt.run_dir)
    run = ValidationRun(
        repo, (), content_overrides={directory / MANIFEST_NAME: manifest(attempt)},
        member_snapshots={directory: members},
        criteria=CriterionSnapshot(kb_root(repo), criterion_bytes(attempt)),
        frozen_source=source,
    )
    reasons = ["[invocation] " + reason for reason in frozen_source_refusals(source)]
    # Ordinary member content checks are not replaced by directory relation checks.
    for role in RECORDS:
        path = attempt.layout.path(role)
        reasons += [f"{path}: {failure}" for failure in run.validate(directory / path).fails]
    try:
        reasons += ["[artifact] " + finding.render() for finding in run.artifact_findings(directory)
                    if not finding.absent and not finding.info]
    except (OSError, UnicodeError, ValueError, TypeError) as exc:
        reasons.append(f"[artifact] artifact input cannot be checked: {exc}")
    text = "# Record check\n\n" + ("\n".join(f"- {reason}" for reason in reasons) or "none") + "\n"
    return {"findings": text.encode("utf-8")}


def _addressee(entry: str) -> str:
    """The report a blocker names; the verification type's validation enforces the prefix."""
    return entry[2:].partition(":")[0]


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


def _record_check_failed(data: bytes) -> bool:
    text = data.decode("utf-8").strip()
    heading = "# Record check"
    if not text.startswith(heading + "\n"):
        raise ValueError("handed record-check must be a Record check document")
    body = text[len(heading):].strip()
    if body == "none":
        return False
    if not body or not body.startswith("- "):
        raise ValueError("handed record-check must contain none or findings")
    return True


def apply_verify(attempt: CodeAttempt) -> dict[str, bytes]:
    """Apply a verdict only to the exact subjects its completed verifier was handed.

    The declaration must include verifier-attempt even when verdict bytes match
    an earlier verdict. The engine owns late-subject installation and refusal
    delivery. No explicit overrides or current-member discovery are used here.
    """
    producer = json.loads(attempt.read("verifier-attempt"))
    check = candidate(attempt, "record-verification", PARTNERS, repo=checkout(attempt.run_dir), seen=True,
                      source_role="boundary")
    # Validation refuses Blockers that are not none or addressed list entries.
    reasons = review(check)
    entries = blocker_entries(section(check.data.decode("utf-8", errors="replace"), "Blockers"))
    if _record_check_failed(attempt.read("record-check-seen")) and not entries:
        reasons.append("structural failures require explicit blockers (code requires at least one; the verifier must address every finding)")
    # A verifier with blockers is a valid verdict document, not an acceptance
    # of the defective reports: its content acceptance covers its citations,
    # never the verifies relations, which only the judgments below cover.
    judge(check, reasons)
    if reasons:
        return {}
    if entries:
        bodies = {role: check.snapshot[attempt.layout.path(role)].decode("utf-8") for role in ANALYSTS}
        owners = {_addressee(entry) for entry in entries}
        for role in RECORDS:
            if role in owners:
                attempt.judge(
                    role + "-seen", outcome="refused",
                    scope=(f"record-verification:verifies:{role}",),
                    findings=_feedback(role, producer["id"], entries, bodies),
                )
    else:
        for role in RECORDS:
            attempt.judge(role + "-seen", outcome="accepted", scope=(f"record-verification:verifies:{role}",))
    return {}


# Declared check and feedback for the compact plan's record verification.


def _set_check_failed(data: bytes) -> bool:
    text = data.decode("utf-8").strip()
    heading = SET_CHECK_HEADING
    if not text.startswith(heading + "\n"):
        raise ValueError(f"handed record-check must be a {heading.removeprefix('# ')} document")
    body = text[len(heading):].strip()
    if body == "none":
        return False
    if not body or not body.startswith("- "):
        raise ValueError("handed record-check must contain none or findings")
    return True


def record_check_gate(check: Candidate) -> list[str]:
    """A verifier handed structural findings must address them with at least one blocker."""
    entries = blocker_entries(section(check.data.decode("utf-8", errors="replace"), "Blockers"))
    if _set_check_failed(check.attempt.read("record-check-seen")) and not entries:
        return [("structural failures require explicit blockers (code requires at least one; "
                 "the verifier must address every finding)")]
    return []


def cited_records(role: str, blockers: list[str], verdict: Candidate) -> str:
    """Peer record declarations the blockers addressed to `role` cite, for the author to read."""
    layout = verdict.attempt.layout
    prefixes = {"runtime": "RT-", "memory": "MEM-", "epistemic": "EPI-"}
    fragments = []
    for identifier in sorted(record_references("\n".join(blockers))):
        for peer, prefix in prefixes.items():
            body = verdict.snapshot.get(layout.path(peer))
            if peer != role and identifier.startswith(prefix) and body is not None:
                declaration = record_declaration(body.decode("utf-8"), identifier)
                if declaration is not None:
                    fragments.append(f"From the {peer} report:\n\n{declaration}")
    return "\n## Cited records from other reports\n\n" + ("\n".join(fragments) or "none") + "\n"
