"""Check explicit agentic-analysis record references without interpreting claims."""

from __future__ import annotations

import re
from collections import Counter
from collections.abc import Mapping, Sequence
from difflib import get_close_matches

from commonplace.lib.note_parser import section

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


def source_register_rows(body: str) -> list[list[str]]:
    """Declared source rows, excluding quoted and fenced examples."""
    register = section(_analysis_prose(body), "Source register")
    return [
        [cell.strip().replace(r"\|", "|") for cell in re.split(r"(?<!\\)\|", line.strip()[1:].removesuffix("|"))]
        for line in register.splitlines() if _SOURCE_DECLARATION.match(line)
    ]


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


def record_references(text: str) -> set[str]:
    """The well-formed record IDs a text refers to, excluding source IDs."""
    return {
        identifier for identifier in _references(_analysis_prose(text))
        if re.fullmatch(_RECORD_ID, identifier)
    }


def record_declaration(body: str, identifier: str) -> str | None:
    """A record's declaration as written: its heading and the text up to the
    next heading of the same or a higher level, or None when the body does not
    declare it."""
    match = re.search(
        rf"(?m)^(#{{3,6}})[ \t]+{re.escape(identifier)}[ \t]+—[ \t]+\S[^\n]*$", body,
    )
    if match is None:
        return None
    level = len(match[1])
    following = re.compile(rf"(?m)^#{{1,{level}}}[ \t]").search(body, match.end())
    return body[match.start():following.start() if following else len(body)].rstrip() + "\n"


def value_amendments(body: str) -> list[str]:
    """The first line of each `Amendment:` paragraph that is not a supersession.

    Reconciliation states identity between declared records. A changed value
    belongs in the declaring analyst's report.
    """
    supersession = re.compile(
        rf"Amendment:[ \t]+`?{_RECORD_ID}`?[ \t]+is superseded by[ \t]+`?{_RECORD_ID}(?![\w-])"
    )
    # A wrapped paragraph is one statement.
    paragraphs = re.split(r"\n[ \t]*\n", _analysis_prose(body))
    return [
        paragraph.splitlines()[0] for paragraph in paragraphs
        if paragraph.startswith("Amendment:")
        and supersession.match(" ".join(paragraph.split())) is None
    ]


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
    # One repeated mistake is one finding: name every place it occurs.
    invalid: dict[tuple[str, str], list[str]] = {}
    all_headings = list(re.finditer(r"(?m)^#{2,6}[ \t]+([^\n]+)$", prose))
    for field in _STATUS_FIELD.finditer(prose):
        label, value = field[1], field[2].strip()
        if value.strip("`") in CONCLUSION_STATUSES:
            continue
        heading = next((h for h in reversed(all_headings) if h.start() < field.start()), None)
        declaration = _DECLARATION.fullmatch(heading[0]) if heading else None
        place = declaration[1] if declaration else (
            f"under '{heading[1].strip()}'" if heading else "before the first heading"
        )
        invalid.setdefault((label, value), []).append(place)
    for (label, value), places in invalid.items():
        errors.append(
            f"conclusion status: {label}: invalid value {value!r} in "
            + ", ".join(dict.fromkeys(places))
            + (f" ({len(places)} fields)" if len(places) > 1 else "")
            + "; use one of " + ", ".join(sorted(CONCLUSION_STATUSES))
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


def set_declarations(sources: str, bodies: Mapping[str, str]) -> dict[str, list[str]]:
    """Each body's record declarations; ``sources`` also declares its Source register."""
    declarations = {name: declared_ids(body) for name, body in bodies.items()}
    if sources in bodies:
        declarations[sources] = [*declarations[sources], *source_register_ids(bodies[sources])]
    return declarations


def set_record_findings(
    sources: str, bodies: Mapping[str, str], *, cites: Mapping[str, Sequence[str]] | None = None,
) -> tuple[set[str], list[tuple[str | None, str]]]:
    """Resolve references against declarations, excluding source excerpts.

    ``bodies`` maps set names to bodies. The Source register of ``sources``
    declares the ``SRC-*`` records. With ``cites``, a body's references resolve
    only against the declarations of the names it cites; a body it does not
    list resolves against every declaration. Each finding names the body it
    belongs to.
    """
    declared = set_declarations(sources, bodies)
    known = {identifier for identifiers in declared.values() for identifier in identifiers}
    findings: list[tuple[str | None, str]] = []
    counts = Counter(identifier for identifiers in declared.values() for identifier in identifiers)
    for name, identifiers in declared.items():
        findings.extend(
            (name, f"{name}: duplicate set declaration: {identifier}")
            for identifier in dict.fromkeys(identifiers) if counts[identifier] > 1
        )
    owners = {identifier: name for name, identifiers in declared.items() for identifier in identifiers}
    for error in _prefix_collisions([identifier for identifier in known if not identifier.startswith("SRC-")]):
        longer = error.split(" ", 3)[2]
        findings.append((owners.get(longer), error))
    for name, body in bodies.items():
        findings.extend((name, f"{name}: {error}") for error in _record_syntax_errors(body))
        scope_counts = counts if cites is None or name not in cites else Counter(
            identifier for cited in set(cites[name]) for identifier in declared.get(cited, ())
        )
        scope = set(scope_counts)
        references = _references(_analysis_prose(body))
        for identifier in sorted(references & scope):
            if scope_counts[identifier] > 1 and identifier not in declared[name]:
                # Declaring members already have a duplicate finding. Consumers
                # need their own finding so candidate-only filtering preserves it.
                findings.append((name, (
                    f"{name}: ambiguous record {identifier}; "
                    "multiple declarations in the documents this one may cite"
                )))
        for identifier in sorted(references - scope):
            if not identifier.startswith("SRC-") and re.fullmatch(_RECORD_ID, identifier) is None:
                continue  # the whole-token grammar diagnostic above is sufficient
            if identifier in known:
                findings.append((name, (
                    f"{name}: unresolved record {identifier}; it is declared outside "
                    f"the documents this one may cite: {', '.join(cites[name]) or 'none'}"
                )))
                continue
            hint = ""
            if re.fullmatch(_RECORD_ID, identifier):
                suffix = identifier.split("-", 1)[1]
                alternatives = sorted(candidate for candidate in scope
                                      if re.fullmatch(_RECORD_ID, candidate)
                                      and candidate.split("-", 1)[1] == suffix)
                if alternatives:
                    hint = "; declared with another analyst prefix: " + ", ".join(alternatives)
            if not hint:
                candidates = sorted(candidate for candidate in scope
                                    if candidate.startswith("SRC-") == identifier.startswith("SRC-"))
                labels = {candidate.split("-", 2)[-1]: candidate for candidate in candidates
                          if candidate.split("-", 2)[:2] == identifier.split("-", 2)[:2]}
                closest = get_close_matches(identifier.split("-", 2)[-1], sorted(labels), n=1, cutoff=0.6)
                if closest:
                    hint = "; nearest declared ID: " + labels[closest[0]]
            findings.append((name, f"{name}: unresolved record {identifier}{hint}"))
    return known, findings


def set_record_errors(
    sources: str, bodies: Mapping[str, str], *, cites: Mapping[str, Sequence[str]] | None = None,
) -> tuple[set[str], list[str]]:
    """``set_record_findings`` without attribution."""
    known, findings = set_record_findings(sources, bodies, cites=cites)
    return known, [message for _, message in findings]
