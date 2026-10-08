"""Pure analyst correction checks and the consumer-owned refusal packet format."""

from __future__ import annotations

import hashlib
import re

from commonplace.lib.agentic_analysis.records import declared_ids, section
from commonplace.lib.note_parser import parse_document


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


def correction_findings(
    candidate: bytes, *, member: str, incumbent: bytes | None,
    refusal: bytes | None, answers: bytes | None, previous_version: str | None = None,
) -> list[str]:
    """Keep accepted record IDs and check answers to the exact handed refusal."""
    try:
        text = candidate.decode("utf-8")
    except UnicodeError:
        return []  # Content validation owns unreadable candidate diagnostics.
    reasons = []
    if incumbent is not None:
        dropped = sorted(set(declared_ids(incumbent.decode("utf-8"))) - set(declared_ids(text)))
        if dropped:
            reasons.append(
                "record declarations: keep every record the accepted predecessor declared: "
                + ", ".join(dropped) + "; correct its finding without changing its referent"
            )
    wanted = sum(line.startswith("- ") for line in correction_blockers(refusal, member).splitlines())
    try:
        answer_text = "" if answers is None else answers.decode("utf-8")
    except UnicodeError:
        return [*reasons, "correction answers: output-answers must be UTF-8 text"]
    entries = [line for line in answer_text.splitlines() if line.startswith("- ")]
    if len(entries) != wanted or any(re.match(r"- (corrected|declined): \S", line) is None for line in entries):
        reasons.append(
            f"correction answers: output-answers needs exactly {wanted} entries in blocker order, "
            "each starting `- corrected: ` or `- declined: ` with its reason"
        )
    elif previous_version == hashlib.sha256(candidate).hexdigest() and any(line.startswith("- corrected:") for line in entries):
        reasons.append("correction answers: an entry says corrected but the report is identical to its predecessor")
    return reasons


def refusal_findings(reasons: list[str], *, member: str, answered: bytes | None) -> str:
    """Carry correction obligations through a structural refusal without rerouting."""
    blockers = correction_blockers(answered, member)
    cited = "none" if answered is None else section(answered.decode("utf-8"), "Cited records from other reports").strip() or "none"
    return (
        "## Findings\n\n" + "\n".join(reasons)
        + "\n\n## Blockers\n\n" + blockers
        + "\n\n## Cited records from other reports\n\n" + cited + "\n"
    )
