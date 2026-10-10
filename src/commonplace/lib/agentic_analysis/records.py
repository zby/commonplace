"""Record declarations and the citations that link to them, without interpreting claims.

A record is declared by a heading that is exactly its ID, `#### RT-OBJ-store`.
The renderer's automatic slug of that heading is the ID in lower case,
`rt-obj-store`, so a citation is an ordinary Markdown link to it:
`[RT-OBJ-store](runtime.md#rt-obj-store)` from another member, or
`[RT-OBJ-store](#rt-obj-store)` within one. The layout's `cites` is the
schema of this relation and each citation an instance edge. A bare ID in
prose is literal text, never a citation. Source IDs (`SRC-1`) are declared by
Source register rows and cited bare.
"""

from __future__ import annotations

import re
from collections import Counter
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from posixpath import normpath
from urllib.parse import unquote, urlsplit

from commonplace.lib.note_parser import find_markdown_links_with_text, section

# A record ID carries the prefix of the analyst that established it, for the
# life of the artifact: `RT-`, `MEM-`, or `EPI-`.
_PREFIX = r"(?:RT|MEM|EPI)-"
_KIND = r"(?:CMP|OBJ|RTE|CLM|ABS|BAP)"
_NAME = r"[a-z][a-z0-9]*(?:-[a-z][a-z0-9]*){0,2}"
_RECORD_ID = rf"{_PREFIX}{_KIND}-{_NAME}"
_ANCHOR = rf"(?:rt|mem|epi)-(?:cmp|obj|rte|clm|abs|bap)-{_NAME}"
_DECLARATION = re.compile(rf"(?m)^####[ \t]+({_RECORD_ID})[ \t]*$")
_ANNOTATION = re.compile(r"(?m)^####[ \t]+On[ \t]+(\S[^\n]*?)[ \t]*$")
# A heading that names a record but carries more than its ID.
_LABELLED_DECLARATION = re.compile(rf"(?m)^####[ \t]+({_RECORD_ID})[ \t]+\S[^\n]*$")
_SOURCE_DECLARATION = re.compile(r"(?m)^\|[ \t]*(SRC-\d+)[ \t]*\|")
_SOURCE = re.compile(r"(?<![\w-])SRC-\d+(?![\w-])")
# Only numbered source IDs retain interval syntax refusals.
_RANGE = re.compile(
    r"(?<![\w-])(?:SRC-\d+`?[ \t]*(?:through|[–—-])[ \t]*`?"
    r"(?:SRC-\d+|\d+)|SRC-\d+[–-][RO]?\d+)(?![\w-])"
)


def anchor(identifier: str) -> str:
    """The fragment that addresses a record's declaration: its ID in lower case."""
    return identifier.lower()


def identifier_from_anchor(fragment: str) -> str | None:
    """The record ID an anchor addresses, or None when it is no record anchor."""
    if re.fullmatch(_ANCHOR, fragment) is None:
        return None
    prefix, kind, name = fragment.split("-", 2)
    return f"{prefix.upper()}-{kind.upper()}-{name}"


@dataclass(frozen=True)
class RecordLink:
    """One record citation as written: its label, the member it names ('' for
    its own member) and the fragment."""

    label: str
    member: str
    fragment: str

    @property
    def identifier(self) -> str | None:
        """The record ID its fragment addresses."""
        return identifier_from_anchor(self.fragment)


def _record_link(label: str, target: str) -> RecordLink | None:
    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc:
        return None
    label = label.strip().strip("`")
    if identifier_from_anchor(parsed.fragment) is None and re.fullmatch(_RECORD_ID, label) is None:
        return None  # An ordinary link: a whole member, a source or another heading.
    member = normpath(unquote(parsed.path)) if parsed.path else ""
    return RecordLink(label, "" if member == "." else member, parsed.fragment)


def record_links(text: str) -> list[RecordLink]:
    """The record citations a text makes, in order.

    A link is a record citation when its fragment is a record anchor or its
    label is a record ID. Quotations, fenced and inline code are excluded.
    """
    return [link for label, target in find_markdown_links_with_text(text)
            if (link := _record_link(label, target)) is not None]


def _sources(prose: str) -> set[str]:
    return set(_SOURCE.findall(prose))


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

    A declaration is a level-four heading that is exactly a record ID; an
    annotation heading (`#### On [ID](...)`) is not one.
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
    """IDs a member annotates with `#### On [ID](member.md#anchor)` headings."""
    return {link.identifier for heading in _ANNOTATION.findall(_analysis_prose(body))
            for link in record_links(heading) if link.identifier}


def is_absence(identifier: str) -> bool:
    """Whether a record ID names an evidenced absence, whichever analyst declared it."""
    return re.fullmatch(rf"{_PREFIX}ABS-{_NAME}", identifier) is not None


def _paragraphs(body: str) -> list[str]:
    # A wrapped paragraph is one statement.
    return re.split(r"\n[ \t]*\n", _analysis_prose(body))


def amendment_index(body: str) -> str:
    """The overview's navigation line for records changed by reconciliation."""
    identifiers = sorted({
        links[0].identifier for paragraph in _paragraphs(body) if paragraph.startswith("Amendment:")
        if (links := record_links(paragraph)) and links[0].identifier
    })
    return (
        "Amended or superseded records: " + (", ".join(identifiers) or "none")
        + "; [reconciliation](reconciliation.md)."
    )


def record_references(text: str) -> set[str]:
    """The record IDs a text cites by link; bare IDs are not citations."""
    return {link.identifier for link in record_links(text) if link.identifier}


def record_declaration(body: str, identifier: str) -> str | None:
    """A record's declaration as written: its heading and the text up to the
    next heading of the same or a higher level, or None when the body does not
    declare it."""
    match = re.search(rf"(?m)^(#{{3,6}})[ \t]+{re.escape(identifier)}[ \t]*$", body)
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
    cited = rf"\[{_RECORD_ID}\]\([^)\s]*\)"
    supersession = re.compile(rf"Amendment: {cited} is superseded by {cited}")
    return [
        paragraph.splitlines()[0] for paragraph in _paragraphs(body)
        if paragraph.startswith("Amendment:") and supersession.match(" ".join(paragraph.split())) is None
    ]


def _citation_errors(text: str) -> list[str]:
    """A record citation's label is the ID its fragment addresses."""
    errors = []
    for link in record_links(text):
        if link.identifier is None:
            errors.append(f"record citations: [{link.label}] links to #{link.fragment}, which is not a record "
                          f"anchor; link to #{anchor(link.label)}")
        elif link.label != link.identifier:
            errors.append(f"record citations: [{link.label}] links to the record {link.identifier}; "
                          "use that record's ID as the label")
    return errors


def _record_syntax_errors(body: str) -> list[str]:
    """Check declarations, labels, part fields and citation labels without resolving them."""
    prose = _analysis_prose(body)
    errors = [
        f"source references: ranges are not expanded: {match[0]}; list every full SRC ID"
        for match in _RANGE.finditer(prose)
    ]
    errors.extend(_citation_errors(prose))
    records = section(prose, "Shared records")
    errors.extend(
        f"record declarations: {identifier}: the heading is exactly the record ID; "
        "put the label on the record's first line as 'Label: <label>'"
        for identifier in _LABELLED_DECLARATION.findall(records)
    )
    for heading in _ANNOTATION.findall(prose):
        if len(record_links(heading)) != 1:
            errors.append(f"record annotations: 'On {heading}' must link exactly one record, "
                          "as 'On [ID](member.md#anchor)'")
    # Each declaration opens with its label; a Part of field belongs to a declaration.
    owner = None
    in_records = False
    expect_label = None
    part_owners = set()
    for line in prose.splitlines():
        if line.startswith("## "):
            in_records = line == "## Shared records"
            owner = None
        elif re.match(r"^#{3,6}[ \t]", line):
            if expect_label:
                errors.append(f"record declarations: {expect_label}: missing 'Label: <label>' first line")
            declaration = _DECLARATION.fullmatch(line)
            owner = declaration[1] if in_records and declaration else None
            expect_label = owner
            continue
        if expect_label and line.strip():
            if not re.fullmatch(r"Label:[ \t]+\S.*", line):
                errors.append(f"record declarations: {expect_label}: missing 'Label: <label>' first line")
            expect_label = None
        if re.match(r"^[ \t]*(?:-[ \t]+)?Part of:", line):
            if not line.startswith("Part of:"):
                errors.append("record references: use an unindented 'Part of: [ID](member.md#anchor)' line")
                continue
            if owner is None:
                errors.append("record references: Part of: must belong to a declared record")
                continue
            if owner in part_owners:
                errors.append(f"record references: {owner}: duplicate Part of: field")
            part_owners.add(owner)
            links = record_links(line)
            if len(links) != 1:
                errors.append(f"record references: {owner}: Part of: requires exactly one record citation")
            elif links[0].identifier == owner:
                errors.append(f"record references: {owner}: Part of: cannot name itself")
    if expect_label:
        errors.append(f"record declarations: {expect_label}: missing 'Label: <label>' first line")
    return errors


def record_reference_errors(body: str) -> list[str]:
    """Check local syntax and declarations; resolve citations at artifact level."""
    errors = _record_syntax_errors(body)
    repeated = sorted(
        key for key, count in Counter(declared_ids(body)).items() if count > 1
    )
    if repeated:
        errors.append("record references: duplicate declarations: " + ", ".join(repeated))
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
                errors.append(f"{prefix}: missing field; supply it with an answer or an explicit evidence limit")
            elif len(values) != 1:
                errors.append(f"{prefix}: duplicate field; keep one line with this label")
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


def artifact_declarations(sources: str, bodies: Mapping[str, str]) -> dict[str, list[str]]:
    """Each body's record declarations; ``sources`` also declares its Source register."""
    declarations = {name: declared_ids(body) for name, body in bodies.items()}
    if sources in bodies:
        declarations[sources] = [*declarations[sources], *source_register_ids(bodies[sources])]
    return declarations


def _destination(name: str, link: RecordLink) -> str:
    """The member a citation in member ``name`` addresses; members share one directory."""
    return name if not link.member else link.member.removeprefix("./")


DUPLICATE_REPAIR = "keep one declaration per ID and give distinct records distinct names"
CITATION_REPAIR = ("link to the member that declares the record, within this role's citation scope; "
                   "remove unsupported references")
SOURCE_REPAIR = "cite a source ID the boundary's Source register declares, or register the source there"


def artifact_record_findings(
    sources: str, bodies: Mapping[str, str], *, cites: Mapping[str, Sequence[str]] | None = None,
) -> tuple[set[str], list[tuple[str | None, str, str]]]:
    """Resolve every record citation to its declaration, and source IDs to the register.

    ``bodies`` maps artifact member names to bodies. A citation resolves when
    the member it names is present and among those its member may cite (with
    ``cites``; every member otherwise), declares the addressed record, and the
    label is that record's ID. Each finding is the body it belongs to, its
    message and its repair. Member rules report what one member shows alone:
    syntax, a record declared twice in one member, and links leaving the
    artifact directory.
    """
    declared = artifact_declarations(sources, bodies)
    known = {identifier for identifiers in declared.values() for identifier in identifiers}
    findings: list[tuple[str | None, str, str]] = []
    holders = Counter(identifier for identifiers in declared.values() for identifier in set(identifiers))
    for name, identifiers in declared.items():
        findings.extend(
            (name, f"{name}: duplicate artifact declaration: {identifier}", DUPLICATE_REPAIR)
            for identifier in dict.fromkeys(identifiers) if holders[identifier] > 1
        )
    for name, body in bodies.items():
        scope = set(bodies) if cites is None or name not in cites else set(cites[name])
        prose = _analysis_prose(body)
        for link in record_links(prose):
            identifier = link.identifier
            if identifier is None or link.label != identifier:
                continue  # The label finding above is sufficient.
            member = _destination(name, link)
            where = f"[{identifier}]({link.member}#{link.fragment})"
            if "/" in member:
                continue  # The member link rule reports a link leaving the directory.
            if member not in scope:
                findings.append((name, (f"{name}: record citation {where}: {member} is not among the "
                                        f"documents this one may cite: {', '.join(sorted(scope)) or 'none'}"),
                                 CITATION_REPAIR))
            elif member not in bodies:
                findings.append((name, f"{name}: record citation {where}: member {member} is not present",
                                 CITATION_REPAIR))
            elif identifier not in declared.get(member, ()):
                elsewhere = sorted(other for other, ids in declared.items() if identifier in ids)
                hint = f"; it is declared in {', '.join(elsewhere)}" if elsewhere else ""
                findings.append((name, (f"{name}: unresolved record citation {where}: {member} declares "
                                        f"no {identifier}{hint}"), CITATION_REPAIR))
        for identifier in sorted(_sources(prose)):
            if sources not in scope:
                findings.append((name, (f"{name}: unresolved source {identifier}; the Source register is "
                                        f"outside the documents this one may cite: {', '.join(sorted(scope)) or 'none'}"),
                                 SOURCE_REPAIR))
            elif sources in bodies and identifier not in declared.get(sources, ()):
                findings.append((name, (f"{name}: unresolved source {identifier}; the Source register "
                                        "does not declare it"), SOURCE_REPAIR))
    return known, findings
