"""Check explicit agentic-analysis record references without interpreting claims."""

from __future__ import annotations

import re
from collections import Counter

# A record ID carries the prefix of the pass that established it, for the life
# of the set: none for the runtime pass, `MEM-` for the memory lens, `EPI-` for
# the epistemic lens.
_RECORD_ID = r"(?:(?:MEM|EPI)-)?(?:CMP|OBJ|RTE|CLM|ABS|BAP)-\d+"
_ID = rf"(?:SRC-\d+|{_RECORD_ID})"
_DECLARATION = re.compile(
    rf"(?m)^####[ \t]+({_RECORD_ID})[ \t]+—[ \t]+\S[^\n]*$"
)
_ANNOTATION = re.compile(
    rf"(?m)^####[ \t]+On[ \t]+({_RECORD_ID})[ \t]+—[ \t]+\S[^\n]*$"
)
_SOURCE_DECLARATION = re.compile(r"(?m)^\|[ \t]*(SRC-\d+)[ \t]*\|")
_REFERENCE = re.compile(rf"(?<![\w-]){_ID}(?![\w-])")


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


def declared_ids(body: str) -> list[str]:
    """IDs declared under Shared records, in order, with repeats kept.

    An annotation heading (`#### On OBJ-1 — label`) is not a declaration.
    """
    return _DECLARATION.findall(section(_analysis_prose(body), "Shared records"))


def annotated_ids(body: str) -> set[str]:
    """IDs a member annotates with `On <ID>` headings without declaring them."""
    return set(_ANNOTATION.findall(_analysis_prose(body)))


def is_absence(identifier: str) -> bool:
    """Whether a record ID names an evidenced absence, whichever pass declared it."""
    return re.fullmatch(r"(?:(?:MEM|EPI)-)?ABS-\d+", identifier) is not None


def record_reference_errors(body: str) -> list[str]:
    """Check one document's declarations.

    A member of a set is validated alone, so references it makes to records
    other members declare are not resolved here.
    """
    repeated = sorted(
        key for key, count in Counter(declared_ids(body)).items() if count > 1
    )
    if repeated:
        return ["record references: duplicate declarations: " + ", ".join(repeated)]
    return []


def set_record_errors(bodies: dict[str, str]) -> tuple[set[str], list[str]]:
    """Resolve references against the set's declarations, excluding source excerpts.

    ``bodies`` maps set names to bodies and includes ``overview.md``, whose
    Source register declares the ``SRC-*`` records.
    """
    declarations = []
    for body in bodies.values():
        declarations.extend(declared_ids(body))
    declarations.extend(
        _SOURCE_DECLARATION.findall(
            section(_analysis_prose(bodies["overview.md"]), "Source register")
        )
    )
    known = set(declarations)
    errors = [
        f"duplicate set declaration: {identifier}"
        for identifier, count in Counter(declarations).items() if count > 1
    ]
    for name, body in bodies.items():
        references = set(_REFERENCE.findall(_analysis_prose(body)))
        for identifier in sorted(references - known):
            errors.append(f"{name}: unresolved record {identifier}")
    return known, errors
