"""Check explicit agentic-analysis record references without interpreting claims."""

from __future__ import annotations

import re
from collections import Counter
from difflib import get_close_matches

# A record ID carries the prefix of the analyst that established it, for the
# life of the set: `RT-`, `MEM-`, or `EPI-`. Archived results written with
# bare runtime IDs are not read by current code.
_PREFIX = r"(?:RT|MEM|EPI)-"
_KIND = r"(?:CMP|OBJ|RTE|CLM|ABS|BAP)"
_NAME = r"[a-z][a-z0-9]*(?:-[a-z][a-z0-9]*){0,2}"
_RECORD_ID = rf"{_PREFIX}{_KIND}-{_NAME}"
# Scan whole candidates first, including malformed names and kind codes.
_RECORD_TOKEN = rf"{_PREFIX}[A-Z]+-[\w-]*"
_DECLARATION = re.compile(
    rf"(?m)^####[ \t]+({_RECORD_ID})[ \t]+—[ \t]+\S[^\n]*$"
)
_ANNOTATION = re.compile(
    rf"(?m)^####[ \t]+On[ \t]+({_RECORD_ID})[ \t]+—[ \t]+\S[^\n]*$"
)
_UNPREFIXED_DECLARATION = re.compile(
    rf"(?m)^####[ \t]+({_KIND}-[\w-]+)[ \t]+—[ \t]+\S[^\n]*$"
)
_SOURCE_DECLARATION = re.compile(r"(?m)^\|[ \t]*(SRC-\d+)[ \t]*\|")
_REFERENCE = re.compile(rf"(?<![\w-])(?:SRC-\d+|{_RECORD_TOKEN})(?![\w-])")
# Only numbered source IDs retain interval syntax refusals.
_RANGE = re.compile(
    r"(?<![\w-])(?:SRC-\d+`?[ \t]*(?:through|[–—-])[ \t]*`?"
    r"(?:SRC-\d+|\d+)|SRC-\d+[–-][RO]?\d+)(?![\w-])"
)


def _references(prose: str) -> set[str]:
    # An ASCII dash between two full IDs is grouping punctuation. A lowercase
    # attached word stays in the token, so sheet-based cannot resolve as sheet.
    separated = re.sub(r"-(?=(?:RT|MEM|EPI)-[A-Z]+-)", " ", prose)
    return set(_REFERENCE.findall(separated))


def _prefix_collisions(identifiers: list[str]) -> list[str]:
    names = sorted(set(identifiers))
    return [
        f"record IDs: {long} extends declared ID {short}; use names neither of which is the other plus a hyphenated word"
        for short in names for long in names if long.startswith(short + "-")
    ]


ROUTE_FIELDS = (
    "Immediate return",
    "Later read-back",
    "Delegated visibility",
    "Selection predicate",
    "Invalidation or expiry",
    "Activation or effect",
    "Evidence limits",
)
CONCLUSION_STATUSES = frozenset({
    "absent", "inapplicable", "uninspected", "claimed", "afforded", "wired",
    "observed", "causally supported",
})
_STATUS_FIELD = re.compile(
    r"(?im)^(?:- )?((?:[\w-]+ )*conclusion status):[ \t]*([^\n]*)$"
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

    An annotation heading (`#### On RT-OBJ-store — label`) is not a declaration.
    """
    return _DECLARATION.findall(section(_analysis_prose(body), "Shared records"))


def source_register_ids(body: str) -> list[str]:
    """Source IDs declared by register rows, in order, with repeats kept."""
    return _SOURCE_DECLARATION.findall(
        section(_analysis_prose(body), "Source register")
    )


def annotated_ids(body: str) -> set[str]:
    """IDs a member annotates with `On <ID>` headings without declaring them."""
    return set(_ANNOTATION.findall(_analysis_prose(body)))


def is_absence(identifier: str) -> bool:
    """Whether a record ID names an evidenced absence, whichever analyst declared it."""
    return re.fullmatch(rf"{_PREFIX}ABS-{_NAME}", identifier) is not None


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


def _record_syntax_errors(body: str) -> list[str]:
    """Check ranges and part fields without resolving cross-member references."""
    prose = _analysis_prose(body)
    errors = [
        f"source references: ranges are not expanded: {match[0]}; list every full SRC ID"
        for match in _RANGE.finditer(prose)
    ]
    errors.extend(
        f"record IDs: invalid ID {identifier}; use RT-, MEM- or EPI-, a registered kind, and one to three lowercase words starting with a letter (digits may follow letters)"
        for identifier in sorted(_references(prose))
        if not identifier.startswith("SRC-") and re.fullmatch(_RECORD_ID, identifier) is None
    )
    # A Part of field belongs to a declaration, not an annotation or prose section.
    owner = None
    in_records = False
    part_owners = set()
    for line in prose.splitlines():
        if line.startswith("## "):
            in_records = line == "## Shared records"
            owner = None
        elif re.match(r"^#{3,6}[ \t]", line):
            declaration = _DECLARATION.fullmatch(line)
            owner = declaration[1] if in_records and declaration else None
        if re.match(r"^[ \t]*(?:-[ \t]+)?Part of:", line):
            if not line.startswith("Part of:"):
                errors.append("record references: use an unindented 'Part of: <full record ID>' line")
                continue
            target = line.removeprefix("Part of:").strip()
            if owner is None:
                errors.append("record references: Part of: must belong to a declared record")
            else:
                if owner in part_owners:
                    errors.append(f"record references: {owner}: duplicate Part of: field")
                part_owners.add(owner)
                if re.fullmatch(_RECORD_ID, target) is None:
                    errors.append(f"record references: {owner}: Part of: requires exactly one full record ID")
                elif target == owner:
                    errors.append(f"record references: {owner}: Part of: cannot name itself")
    return errors


def record_reference_errors(body: str) -> list[str]:
    """Check local syntax and declarations; resolve other members' IDs at set level."""
    errors = _record_syntax_errors(body)
    records = section(_analysis_prose(body), "Shared records")
    unprefixed = _UNPREFIXED_DECLARATION.findall(records)
    if unprefixed:
        errors.append(
            "record references: declarations without an analyst prefix: "
            + ", ".join(unprefixed) + "; use RT-, MEM- or EPI-"
        )
    repeated = sorted(
        key for key, count in Counter(declared_ids(body)).items() if count > 1
    )
    if repeated:
        errors.append("record references: duplicate declarations: " + ", ".join(repeated))
    errors.extend(_prefix_collisions(declared_ids(body)))
    return errors


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
            rf"{_PREFIX}RTE-{_NAME}", declaration[1]
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


def conclusion_status_errors(body: str) -> list[str]:
    """Check labelled conclusion statuses, without inferring them from prose."""
    prose = _analysis_prose(body)
    errors = []
    for label, value in _STATUS_FIELD.findall(prose):
        if value.strip().strip("`") not in CONCLUSION_STATUSES:
            errors.append(
                f"conclusion status: {label}: invalid value {value.strip()!r}; "
                "use one of " + ", ".join(sorted(CONCLUSION_STATUSES))
            )
    records = section(prose, "Shared records")
    headings = list(re.finditer(r"(?m)^#{3,6}[ \t]+[^\n]+$", records))
    for index, heading in enumerate(headings):
        declaration = _DECLARATION.fullmatch(heading[0])
        if declaration is None or not re.fullmatch(
            rf"{_PREFIX}RTE-{_NAME}", declaration[1]
        ):
            continue
        end = headings[index + 1].start() if index + 1 < len(headings) else len(records)
        fields = _STATUS_FIELD.findall(records[heading.end():end])
        if not fields:
            errors.append(
                f"conclusion status: {declaration[1]}: missing labelled field; "
                "write '- implementation conclusion status: <value>' and label "
                "any other assessed layer separately"
            )
        labels = Counter(label.casefold() for label, _ in fields)
        for label, count in labels.items():
            if count > 1:
                errors.append(f"conclusion status: {declaration[1]}: duplicate {label} field")
    return errors


def set_record_errors(bodies: dict[str, str]) -> tuple[set[str], list[str]]:
    """Resolve references against the set's declarations, excluding source excerpts.

    ``bodies`` maps set names to bodies and includes ``overview.md``, whose
    Source register declares the ``SRC-*`` records.
    """
    declarations = []
    for body in bodies.values():
        declarations.extend(declared_ids(body))
    declarations.extend(source_register_ids(bodies["overview.md"]))
    known = set(declarations)
    errors = [
        f"duplicate set declaration: {identifier}"
        for identifier, count in Counter(declarations).items() if count > 1
    ]
    errors.extend(_prefix_collisions([identifier for identifier in declarations if not identifier.startswith("SRC-")]))
    for name, body in bodies.items():
        errors.extend(f"{name}: {error}" for error in _record_syntax_errors(body))
        references = _references(_analysis_prose(body))
        for identifier in sorted(references - known):
            if not identifier.startswith("SRC-") and re.fullmatch(_RECORD_ID, identifier) is None:
                continue  # the whole-token grammar diagnostic above is sufficient
            hint = ""
            if re.fullmatch(_RECORD_ID, identifier):
                suffix = identifier.split("-", 1)[1]
                alternatives = sorted(candidate for candidate in known
                                      if re.fullmatch(_RECORD_ID, candidate)
                                      and candidate.split("-", 1)[1] == suffix)
                if alternatives:
                    hint = "; declared with another analyst prefix: " + ", ".join(alternatives)
            if not hint:
                candidates = sorted(candidate for candidate in known
                                    if candidate.startswith("SRC-") == identifier.startswith("SRC-"))
                labels = {candidate.split("-", 2)[-1]: candidate for candidate in candidates
                          if candidate.split("-", 2)[:2] == identifier.split("-", 2)[:2]}
                closest = get_close_matches(identifier.split("-", 2)[-1], sorted(labels), n=1, cutoff=0.6)
                if closest:
                    hint = "; nearest declared ID: " + labels[closest[0]]
            errors.append(f"{name}: unresolved record {identifier}{hint}")
    return known, errors
