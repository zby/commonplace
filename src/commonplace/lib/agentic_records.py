"""Check explicit agentic-analysis record references without interpreting claims."""

from __future__ import annotations

import re
from collections import Counter

# A record ID carries the prefix of the analyst that established it, for the
# life of the set: none for the runtime analyst, `MEM-` for the memory analyst,
# `EPI-` for the epistemic analyst.
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
ROUTE_FIELDS = (
    "Immediate return",
    "Later read-back",
    "Delegated visibility",
    "Selection predicate",
    "Invalidation or expiry",
    "Activation or effect",
    "Evidence limits",
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


def declared_ids(body: str) -> list[str]:
    """IDs declared under Shared records, in order, with repeats kept.

    An annotation heading (`#### On OBJ-1 — label`) is not a declaration.
    """
    return _DECLARATION.findall(section(_analysis_prose(body), "Shared records"))


def annotated_ids(body: str) -> set[str]:
    """IDs a member annotates with `On <ID>` headings without declaring them."""
    return set(_ANNOTATION.findall(_analysis_prose(body)))


def is_absence(identifier: str) -> bool:
    """Whether a record ID names an evidenced absence, whichever analyst declared it."""
    return re.fullmatch(r"(?:(?:MEM|EPI)-)?ABS-\d+", identifier) is not None


def amendment_index(body: str) -> str:
    """The overview's navigation line for records changed by reconciliation."""
    identifiers = sorted(set(re.findall(
        rf"(?m)^Amendment:[ \t]+`?({_RECORD_ID})(?![\w-])",
        _analysis_prose(body),
    )))
    return (
        "Amended or superseded records: " + (", ".join(identifiers) or "none")
        + "; [reconciliation](reconciliation.md)."
    )


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


def route_field_errors(body: str) -> list[str]:
    """Check unconditional route fields, without judging their answers.

    Each declaration owns its fields. An adjacent annotation, another record,
    source quotation or fenced excerpt cannot supply a missing answer.
    """
    prose = section(_analysis_prose(body), "Shared records")
    headings = list(re.finditer(r"(?m)^#{3,6}[ \t]+[^\n]+$", prose))
    errors = []
    for index, heading in enumerate(headings):
        declaration = _DECLARATION.fullmatch(heading[0])
        if declaration is None or not re.fullmatch(
            r"(?:(?:MEM|EPI)-)?RTE-\d+", declaration[1]
        ):
            continue
        end = headings[index + 1].start() if index + 1 < len(headings) else len(prose)
        record = prose[heading.end():end]
        for label in ROUTE_FIELDS:
            values = re.findall(
                rf"(?m)^- {re.escape(label)}:[ \t]*([^\n]*)$", record
            )
            prefix = f"route fields: {declaration[1]}: {label}"
            if not values:
                errors.append(f"{prefix}: missing field")
            elif len(values) != 1:
                errors.append(f"{prefix}: duplicate field")
            elif not values[0].strip():
                errors.append(f"{prefix}: empty field")
            elif re.match(r"(?i)^(inapplicable|uninspected)\b", values[0]) and not re.fullmatch(
                r"(inapplicable|uninspected) — \S.*", values[0].strip()
            ):
                errors.append(f"{prefix}: use 'inapplicable — reason' or 'uninspected — reason'")
    return errors


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
