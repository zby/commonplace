"""Check explicit agentic-analysis record references without interpreting claims."""

from __future__ import annotations

import re
from collections import Counter

_KINDS = r"(?:SRC|CMP|OBJ|RTE|CLM|ABS|BAP)"
_ID = rf"{_KINDS}-\d+"
_REFERENCE = re.compile(rf"(?<![\w-])({_ID})(?![\w-])")
_DECLARATION = re.compile(
    rf"(?m)^[ \t]*(?:\|[ \t]*|[-*][ \t]+|#{{3,6}}[ \t]+)?[*`]*({_ID})(?![\w-])"
)
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


def _section(body: str, title: str) -> str:
    match = re.search(rf"(?ms)^## {re.escape(title)}[ \t]*\n(.*?)(?=^## |\Z)", body)
    return match[1] if match else ""


def record_reference_errors(body: str, *, memory_report: bool = False) -> list[str]:
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
    local_records = sorted(set(re.findall(
        rf"\b(?:MEM|EPI)-(?:{_ID}|[OCRSAB]\d+)\b", outside_reconciliation
    )))
    if local_records:
        errors.append(
            "record references: unintegrated proposal IDs outside Reconciliation: "
            + ", ".join(local_records)
        )
    shared = _section(prose, "Shared records")
    declarations = _DECLARATION.findall(shared)
    repeated = sorted(key for key, count in Counter(declarations).items() if count > 1)
    if repeated:
        errors.append("record references: duplicate declarations: " + ", ".join(repeated))
    sources = {value for value in _REFERENCE.findall(_section(prose, "Source register"))
               if value.startswith("SRC-")}
    defined = set(declarations) | sources
    unresolved = sorted(set(_REFERENCE.findall(prose)) - defined)
    if unresolved:
        errors.append("record references: unresolved IDs: " + ", ".join(unresolved))
    return errors
