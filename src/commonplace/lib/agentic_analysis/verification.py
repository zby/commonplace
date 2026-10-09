"""The report verification's declared check and feedback.

The standard apply handler applies the verdict; these supply what the
analysis adds: a verifier handed structural findings must block, and an
author refused by it reads the peer records its blockers cite.
"""

from __future__ import annotations

from commonplace.artifactrun.checks import Candidate, blocker_entries
from commonplace.artifactrun.handlers import ARTIFACT_CHECK_HEADING
from commonplace.lib.agentic_analysis.records import (
    record_declaration,
    record_references,
)
from commonplace.lib.note_parser import section


def _artifact_check_failed(data: bytes) -> bool:
    text = data.decode("utf-8").strip()
    heading = ARTIFACT_CHECK_HEADING
    if not text.startswith(heading + "\n"):
        raise ValueError(f"handed report-check must be a {heading.removeprefix('# ')} document")
    body = text[len(heading):].strip()
    if body == "none":
        return False
    if not body or not body.startswith("- "):
        raise ValueError("handed report-check must contain none or findings")
    return True


def report_check_gate(check: Candidate) -> list[str]:
    """A verifier handed structural findings must address them with at least one blocker."""
    entries = blocker_entries(section(check.data.decode("utf-8", errors="replace"), "Blockers"))
    if _artifact_check_failed(check.attempt.read("report-check-handed")) and not entries:
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
