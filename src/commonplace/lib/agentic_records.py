"""Check explicit agentic-analysis record references without interpreting claims."""

from __future__ import annotations

import re
from collections import Counter

_KINDS = r"(?:SRC|CMP|OBJ|RTE|CLM|ABS|BAP)"
_ID = rf"{_KINDS}-\d+"
_DECLARATION = re.compile(
    rf"(?m)^[ \t]*(?:\|[ \t]*|[-*][ \t]+|#{{3,6}}[ \t]+)?[*`]*((?:MEM-)?{_ID})(?![\w-])"
)
_ANNOTATION = re.compile(rf"(?m)^[ \t]*#{{3,6}}[ \t]+On[ \t]+({_ID})(?![\w-])")
_PROPOSAL = re.compile(rf"\b(?:MEM|EPI)-(?:{_ID}|[OCRSAB]\d+)\b")
_SHORTHAND = re.compile(
    rf"(?<![\w-])(?:(?:MEM|EPI)-)?{_ID}[*`]*[ \t]*"
    rf"(?:[/,][ \t]*[*`]*(?:[OCRSAB]\d+|{_KINDS}\d+|\d+)"
    rf"|[–—-][ \t]*[*`]*(?:(?:(?:MEM|EPI)-)?{_ID}|[OCRSAB]\d+|\d+))"
    rf"(?![\w-])"
)


def _analysis_prose(body: str) -> str:
    """Source quotations and fenced excerpts are evidence, not record syntax."""
    lines = []
    fence = None
    for line in body.splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            token = marker[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is not None or re.match(r"^\s*>", line):
            continue
        lines.append(line)
    return "\n".join(lines) + "\n"


def section(body: str, title: str) -> str:
    """The text under one level-two heading, or empty when the heading is absent."""
    match = re.search(rf"(?ms)^## {re.escape(title)}[ \t]*\n(.*?)(?=^## |\Z)", body)
    return match[1] if match else ""


def declared_ids(body: str, *, proposals: bool = False) -> list[str]:
    """IDs declared under Shared records, in order, with repeats kept.

    ``proposals`` also counts the ``MEM-`` proposal IDs a specialist's local
    memory report declares. An annotation heading (`#### On OBJ-1 — label`) is
    not a declaration.
    """
    return [
        identifier
        for identifier in _DECLARATION.findall(section(_analysis_prose(body), "Shared records"))
        if proposals or not identifier.startswith("MEM-")
    ]


def annotated_ids(body: str) -> set[str]:
    """IDs a member annotates with `On <ID>` headings without declaring them."""
    return set(_ANNOTATION.findall(_analysis_prose(body)))


def record_reference_errors(body: str, *, memory_report: bool = False) -> list[str]:
    """Check one document's record syntax and declarations.

    ``memory_report`` is the specialist's local report: it may reference
    commissioned IDs it does not declare. A member of a retained set is
    validated alone, so references it makes to records other members declare
    are not resolved here.
    """
    prose = _analysis_prose(body)
    errors = []
    for match in _SHORTHAND.finditer(prose):
        errors.append(
            f"record references: expand shorthand or range {match[0]!r} into complete IDs"
        )
    if memory_report:
        # The parent owns the canonical register; its commissioned IDs need not
        # all be copied into a specialist report. Comparison references have
        # their own shared/proposed-register check.
        return errors
    outside_reconciliation = re.sub(
        r"(?ms)^## Reconciliation[ \t]*\n.*?(?=^## |\Z)", "", prose
    )
    local_records = sorted(set(_PROPOSAL.findall(outside_reconciliation)))
    if local_records:
        errors.append(
            "record references: unintegrated proposal IDs outside Reconciliation: "
            + ", ".join(local_records)
        )
    declarations = declared_ids(body)
    repeated = sorted(key for key, count in Counter(declarations).items() if count > 1)
    if repeated:
        errors.append("record references: duplicate declarations: " + ", ".join(repeated))
    return errors
