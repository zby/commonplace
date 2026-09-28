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


def _section(body: str, title: str) -> str:
    match = re.search(rf"(?ms)^## {re.escape(title)}[ \t]*\n(.*?)(?=^## |\Z)", body)
    return match[1] if match else ""


def declared_ids(body: str) -> list[str]:
    """IDs declared under Shared records, in order, with repeats kept.

    An annotation heading (`#### On OBJ-1 — label`) is not a declaration.
    """
    return _DECLARATION.findall(_section(_analysis_prose(body), "Shared records"))


def annotated_ids(body: str) -> set[str]:
    """IDs a member annotates with `On <ID>` headings without declaring them."""
    return set(_ANNOTATION.findall(_analysis_prose(body)))


def source_ids(body: str) -> set[str]:
    return {value for value in _REFERENCE.findall(
        _section(_analysis_prose(body), "Source register")
    ) if value.startswith("SRC-")}


def referenced_ids(body: str) -> set[str]:
    return set(_REFERENCE.findall(_analysis_prose(body)))


def record_reference_errors(
    body: str, *, memory_report: bool = False, member: bool = False
) -> list[str]:
    """Check one document's record syntax.

    ``memory_report`` is the specialist's local report: it may reference
    commissioned IDs it does not declare. ``member`` is one member of a
    retained set validated alone: its declarations and syntax are checked,
    but references are resolved only against the whole set by
    ``set_record_errors``.
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
    declarations = _DECLARATION.findall(_section(prose, "Shared records"))
    repeated = sorted(key for key, count in Counter(declarations).items() if count > 1)
    if repeated:
        errors.append("record references: duplicate declarations: " + ", ".join(repeated))
    if member:
        return errors
    defined = set(declarations) | source_ids(body)
    unresolved = sorted(set(_REFERENCE.findall(prose)) - defined)
    if unresolved:
        errors.append("record references: unresolved IDs: " + ", ".join(unresolved))
    return errors


def set_record_errors(members: dict[str, str], *, register_body: str) -> list[str]:
    """Check declarations and references across the members of one retained set.

    ``members`` maps a member's display name to its body. ``register_body`` is
    the overview body whose Source register declares the ``SRC-*`` IDs. Every
    other ID is declared exactly once across the members; every reference in
    any member resolves to a declaration in the set; no proposal ID survives
    finalization in any member.
    """
    errors: list[str] = []
    owners: dict[str, list[str]] = {}
    for name, body in members.items():
        for identifier in declared_ids(body):
            owners.setdefault(identifier, []).append(name)
    for identifier, names in sorted(owners.items()):
        if len(names) > 1:
            errors.append(
                f"record references: {identifier} declared in more than one member: "
                + ", ".join(names)
            )
    defined = set(owners) | source_ids(register_body)
    for name, body in members.items():
        leaked = sorted(set(_PROPOSAL.findall(_analysis_prose(body))))
        if leaked:
            errors.append(
                f"record references: {name}: proposal IDs survive finalization: "
                + ", ".join(leaked)
            )
        unresolved = sorted(referenced_ids(body) - defined)
        if unresolved:
            errors.append(
                f"record references: {name}: unresolved IDs: " + ", ".join(unresolved)
            )
    return errors
