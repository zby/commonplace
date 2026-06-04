"""Deterministic validation rules for KB notes."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import unquote, urlsplit

from jsonschema.exceptions import ValidationError

from commonplace.lib.naming import MAX_NOTE_SLUG_LENGTH, MAX_NOTE_TITLE_LENGTH
from commonplace.lib.note_parser import ParsedDocument, parse_document
from commonplace.lib.type_resolver import TypeProfile, resolve_type, validate_instance


# A schema violation fails by default — the schema is the contract, so breaking a
# constraint blocks unless its author explicitly opts down. A subschema lowers its
# own severity with `severity: warn` (read from error.schema below), optionally
# keyed by a stable `ruleId` so it can be re-leveled or referenced later. This is
# the Spectral/Schematron pattern (severity authored on an identified rule); see
# kb/work/review-template-retrofit/severity-belongs-in-schema.md.
_DEFAULT_SCHEMA_SEVERITY = "fail"

# A quote-anchored citation's attribution line: a blockquote line of the form `> --- ...`.
# The trailing group is the attribution (source path or link).
_QUOTE_CITE_ATTR_RE = re.compile(r"^\s*>\s*---\s*(.*\S)?\s*$")
# A source reference inside an attribution: a markdown link or a code span.
_SOURCE_REF_RE = re.compile(r"\[[^\]]+\]\([^)]+\)|`[^`]+`")


@dataclass
class CheckResults:
    note_type: str
    passes: list[str] = field(default_factory=list)
    warns: list[str] = field(default_factory=list)
    fails: list[str] = field(default_factory=list)
    infos: list[str] = field(default_factory=list)


@dataclass
class ParsedNote:
    path: Path
    content: str
    note_type: str
    profile: TypeProfile
    document: ParsedDocument


def parse_note(path: Path, *, repo_root: Path) -> tuple[ParsedNote | None, str | None]:
    content = path.read_text(encoding="utf-8")
    document, parse_error = parse_document(content)
    if parse_error:
        return None, parse_error
    assert document is not None

    try:
        profile = resolve_type(path, document.frontmatter, repo_root=repo_root)
    except (FileNotFoundError, ValueError) as exc:
        return None, str(exc)
    return ParsedNote(
        path=path,
        content=content,
        note_type=profile.type_name,
        profile=profile,
        document=document,
    ), None


def validate_title_and_slug(results: CheckResults, path: Path, document: ParsedDocument) -> None:
    title = document.title.strip()
    title_length = len(title)
    slug_length = len(path.stem)

    if title_length > MAX_NOTE_TITLE_LENGTH:
        results.fails.append(
            f"title: {title_length} chars exceeds limit of {MAX_NOTE_TITLE_LENGTH}"
        )
    else:
        results.passes.append(
            f"title: {title_length} chars (within {MAX_NOTE_TITLE_LENGTH}-char limit)"
        )

    if slug_length > MAX_NOTE_SLUG_LENGTH:
        results.fails.append(
            f"filename slug: {slug_length} chars exceeds limit of {MAX_NOTE_SLUG_LENGTH}"
        )
    else:
        results.passes.append(
            f"filename slug: {slug_length} chars (within {MAX_NOTE_SLUG_LENGTH}-char limit)"
        )


def validate_links_from_document(results: CheckResults, path: Path, links: tuple[str, ...]) -> None:
    missing: list[str] = []
    for link in links:
        parsed = urlsplit(link)
        if parsed.scheme or parsed.netloc:
            continue
        link_path = unquote(parsed.path)
        if not link_path or Path(link_path).is_absolute():
            continue
        target = (path.parent / link_path).resolve()
        if not target.exists():
            missing.append(link)

    if missing:
        for link in missing:
            results.warns.append(f"link health: missing target {link}")
    else:
        results.passes.append("link health: all local relative links resolve")


def validate_quote_citations(results: CheckResults, content: str) -> None:
    """Shape-check quote-anchored citations (a blockquote + `> ---` attribution).

    Resolving the quote against the reviewed source is a write-time concern handled
    by verify-review-quote-grounding; the source is not retained in the KB, so here
    we only confirm each citation is well-formed and names a source.
    """
    lines = content.splitlines()
    found = 0
    flagged = 0
    for index, line in enumerate(lines):
        match = _QUOTE_CITE_ATTR_RE.match(line)
        if not match:
            continue
        found += 1
        problems: list[str] = []
        attribution = (match.group(1) or "").strip()
        if not _SOURCE_REF_RE.search(attribution):
            problems.append("names no source (expected a code-span path or link)")
        previous = lines[index - 1] if index > 0 else ""
        if not previous.lstrip().startswith(">") or _QUOTE_CITE_ATTR_RE.match(previous):
            problems.append("no quoted text above the attribution")
        if problems:
            flagged += 1
            results.warns.append(
                "quote-anchored citation: " + "; ".join(problems) + f": {line.strip()}"
            )
    if found and not flagged:
        results.passes.append(f"quote-anchored citations: {found} well-formed")


def _schema_error_message(error: ValidationError) -> tuple[str, str]:
    path = tuple(str(part) for part in error.absolute_path)
    location = ".".join(path) if path else "document"

    # Severity is a property of the failing constraint: read it from the leaf
    # subschema, defaulting to fail. Same place description/title/contains are read.
    schema = error.schema if isinstance(error.schema, dict) else None
    severity = _DEFAULT_SCHEMA_SEVERITY
    if isinstance(schema, dict) and schema.get("severity") in ("fail", "warn"):
        severity = schema["severity"]

    # Prefer schema-authored description/title when present — lets schema authors
    # make any specific error more readable without touching validator code.
    if isinstance(schema, dict):
        hint = schema.get("description") or schema.get("title")
        if isinstance(hint, str):
            return severity, f"{location}: {hint}"

    # For `contains`, jsonschema's default message doesn't say which const is expected.
    # Extract it from the schema so the error is actionable.
    if error.validator == "contains" and isinstance(schema, dict):
        contains = schema.get("contains")
        if isinstance(contains, dict) and "const" in contains:
            return severity, f"{location}: missing {contains['const']!r}"

    return severity, f"{location}: {error.message}"


def apply_schema_validation(results: CheckResults, parsed: ParsedNote) -> None:
    if parsed.profile.schema_path is None or parsed.profile.schema is None:
        return

    errors = validate_instance(parsed.profile, parsed.document.to_validation_object())
    if not errors:
        results.passes.append(f"type schema: {parsed.note_type} requirements satisfied")
        return

    for error in errors:
        severity, message = _schema_error_message(error)
        if severity == "fail":
            results.fails.append(message)
        else:
            results.warns.append(message)


def validate_note(path: Path, *, repo_root: Path) -> CheckResults:
    parsed, parse_error = parse_note(path, repo_root=repo_root)
    if parse_error:
        return CheckResults(note_type="unknown", fails=[parse_error])

    assert parsed is not None

    if parsed.document.frontmatter is None:
        return CheckResults(note_type="text", passes=["text file: no frontmatter, no structural requirements"])

    results = CheckResults(note_type=parsed.note_type)
    results.passes.append("frontmatter: valid delimiters, well-formed YAML")
    validate_title_and_slug(results, parsed.path, parsed.document)
    validate_links_from_document(results, parsed.path, parsed.document.links)
    if parsed.note_type == "agent-memory-system-review":
        validate_quote_citations(results, parsed.content)
    apply_schema_validation(results, parsed)
    return results


def orphan_info(all_paths: list[Path]) -> dict[Path, bool]:
    inbound: dict[Path, bool] = {path: False for path in all_paths}
    resolved_index: dict[Path, Path] = {path.resolve(): path for path in all_paths}
    for source in all_paths:
        content = source.read_text(encoding="utf-8")
        document, _ = parse_document(content)
        if document is None:
            continue
        source_resolved = source.resolve()
        for link in document.links:
            if re.match(r"^[a-z]+://", link):
                continue
            link_path = link.split("#", 1)[0]
            if not link_path.endswith(".md"):
                continue
            target_resolved = (source.parent / link_path).resolve()
            if target_resolved == source_resolved:
                continue
            key = resolved_index.get(target_resolved)
            if key is not None:
                inbound[key] = True
    return inbound
