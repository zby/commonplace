"""Deterministic validation rules for KB notes."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from jsonschema.exceptions import ValidationError

from commonplace.lib.naming import MAX_NOTE_SLUG_LENGTH, MAX_NOTE_TITLE_LENGTH
from commonplace.lib.note_parser import ParsedDocument, parse_document
from commonplace.lib.project_paths import list_kb_note_paths, list_notes_collection_paths
from commonplace.lib.type_resolver import TypeProfile, resolve_type, validate_instance


_FAIL_PATHS: frozenset[tuple[str, ...]] = frozenset({
    ("frontmatter", "description"),
    ("frontmatter", "type"),
})

_REQUIRED_PROPERTY_RE = re.compile(r"'([^']+)' is a required property")


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

    profile = resolve_type(path, document.frontmatter, repo_root=repo_root)
    return ParsedNote(
        path=path,
        content=content,
        note_type=profile.resolved_type,
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
        if re.match(r"^[a-z]+://", link):
            continue
        if not link.endswith(".md"):
            continue
        target = (path.parent / link).resolve()
        if not target.exists():
            missing.append(link)

    if missing:
        for link in missing:
            results.warns.append(f"link health: missing target {link}")
    else:
        results.passes.append("link health: all relative markdown links resolve")


def _schema_error_message(error: ValidationError) -> tuple[str, str]:
    path = tuple(str(part) for part in error.absolute_path)

    # `required` violations report at the parent path; the missing field is in the message.
    # For severity lookup, treat the missing field as if it were at path + (field_name,).
    effective_path = path
    if error.validator == "required":
        match = _REQUIRED_PROPERTY_RE.search(error.message)
        if match:
            effective_path = path + (match.group(1),)

    severity = "fail" if effective_path in _FAIL_PATHS else "warn"
    location = ".".join(path) if path else "document"

    # Prefer schema-authored description/title when present — lets schema authors
    # make any specific error more readable without touching validator code.
    schema = error.schema if isinstance(error.schema, dict) else None
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
    if parsed.profile.definition_path is None or parsed.profile.schema is None:
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
