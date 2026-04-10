"""Deterministic validation rules for KB notes."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from jsonschema.exceptions import ValidationError

from commonplace.lib.naming import MAX_NOTE_SLUG_LENGTH, MAX_NOTE_TITLE_LENGTH
from commonplace.lib.note_parser import ParsedDocument, parse_document
from commonplace.lib.type_resolver import TypeProfile, resolve_type, validate_instance


VALID_TRAITS = {
    "definition",
    "has-comparison",
    "has-external-sources",
    "has-implementation",
    "title-as-claim",
}


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


def is_nested_git_repo_content(path: Path, notes_root: Path) -> bool:
    current = path.parent
    while current != notes_root and notes_root in current.parents:
        if (current / ".git").exists():
            return True
        current = current.parent
    return False


def list_kb_note_paths(notes_root: Path) -> list[Path]:
    return sorted(
        path
        for path in notes_root.rglob("*.md")
        if not is_nested_git_repo_content(path, notes_root)
    )


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


def validate_description(results: CheckResults, description: Any) -> None:
    if description in (None, ""):
        results.fails.append("description: missing or empty")
        return

    if not isinstance(description, str):
        results.fails.append("description: must be a string")
        return

    desc = description.strip()
    if not desc:
        results.fails.append("description: missing or empty")
        return

    results.passes.append(f"description: present, {len(desc)} chars")


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


def validate_type_traits_status(
    results: CheckResults,
    frontmatter: dict[str, Any],
    note_type: str,
    profile: TypeProfile,
) -> None:
    if "type" in frontmatter:
        if not isinstance(frontmatter["type"], str) or not frontmatter["type"].strip():
            results.fails.append("type: must be a non-empty string")
        else:
            results.passes.append(f'type: "{frontmatter["type"]}" — valid')

    traits = frontmatter.get("traits")
    if traits is not None:
        if not isinstance(traits, list):
            results.fails.append("traits: must be a list")
        else:
            invalid = [trait for trait in traits if trait not in VALID_TRAITS]
            if invalid:
                for trait in invalid:
                    results.warns.append(f'traits: invalid trait "{trait}"')
            else:
                results.passes.append("traits: valid")

    status = frontmatter.get("status")
    if status is not None and profile.allowed_status:
        if status not in profile.allowed_status:
            results.warns.append(f'status: "{status}" is not one of {sorted(profile.allowed_status)}')
        else:
            results.passes.append(f'status: "{status}" — valid')

    if note_type == "note" and frontmatter.get("traits") == []:
        results.infos.append("bare note type: type=note with empty traits")


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


def validate_structure(
    results: CheckResults, note_type: str, document: ParsedDocument, profile: TypeProfile
) -> None:
    if profile.required_headings:
        missing = [heading for heading in profile.required_headings if heading not in document.headings]
        if missing:
            results.warns.append(f"structure: missing headings {', '.join(missing)}")
        else:
            results.passes.append(f"structure: required {note_type} headings present")

    if profile.any_headings:
        if all(heading not in document.headings for heading in profile.any_headings):
            results.warns.append(f"structure: {note_type} should contain {' or '.join(profile.any_headings)}")
        else:
            results.passes.append(f"structure: {note_type} has required heading")

    extra_required_fields = [name for name in profile.required_fields if name != "description"]
    frontmatter = document.frontmatter or {}
    missing_fields = [name for name in extra_required_fields if frontmatter.get(name) in (None, "", [])]
    if missing_fields:
        results.warns.append(f"frontmatter: missing required fields {', '.join(missing_fields)}")
    elif extra_required_fields:
        results.passes.append(f"frontmatter: required {note_type} fields present")

    if profile.requires_date:
        has_date = any(key in frontmatter for key in ("date", "last-checked")) or bool(document.body_dates)
        if not has_date:
            results.warns.append("structure: review should include a date in frontmatter or body")
        else:
            results.passes.append("structure: review has date")

    if profile.min_links is not None:
        if len(document.links) < profile.min_links:
            results.warns.append(f"structure: index should be primarily navigational (found {len(document.links)} links)")
        else:
            results.passes.append("structure: index has navigational link density")


def _missing_required_property(error: ValidationError) -> str | None:
    match = re.search(r"'([^']+)' is a required property", error.message)
    return match.group(1) if match else None


def _schema_error_message(error: ValidationError, profile: TypeProfile, document: ParsedDocument) -> tuple[str, str] | None:
    path = tuple(str(part) for part in error.absolute_path)

    if error.validator == "required" and path == ("frontmatter",):
        missing = _missing_required_property(error)
        if missing == "description":
            return "fail", "description: missing or empty"
        if missing == "type":
            return "fail", "type: must be a non-empty string"
        if missing is not None:
            return "warn", f"frontmatter: missing required fields {missing}"

    if path == ("frontmatter", "description"):
        if error.validator == "type":
            return "fail", "description: must be a string"
        if error.validator == "minLength":
            return "fail", "description: missing or empty"

    if path == ("frontmatter", "type"):
        if error.validator == "type":
            return "fail", "type: must be a non-empty string"
        if error.validator == "const":
            actual = None if document.frontmatter is None else document.frontmatter.get("type")
            return "fail", f'type: "{actual}" does not match required value "{error.validator_value}"'

    if path == ("frontmatter", "status") and error.validator == "enum":
        status = None if document.frontmatter is None else document.frontmatter.get("status")
        return "warn", f'status: "{status}" is not one of {sorted(profile.allowed_status)}'

    if error.validator == "format" and len(path) == 2 and path[0] == "frontmatter":
        return "warn", f"frontmatter: {path[1]} must be a valid {error.validator_value}"

    if error.validator in {"contains", "anyOf", "minItems", "enum", "required"}:
        return None

    location = ".".join(path) if path else "document"
    return "warn", f"{location}: {error.message}"


def apply_schema_validation(results: CheckResults, parsed: ParsedNote) -> None:
    messages = {
        ("pass", item) for item in results.passes
    } | {
        ("warn", item) for item in results.warns
    } | {
        ("fail", item) for item in results.fails
    }

    for error in validate_instance(parsed.profile, parsed.document.to_validation_object()):
        translated = _schema_error_message(error, parsed.profile, parsed.document)
        if translated is None:
            continue
        severity, message = translated
        key = (severity, message)
        if key in messages:
            continue
        if severity == "fail":
            results.fails.append(message)
        else:
            results.warns.append(message)
        messages.add(key)


def validate_note(path: Path, *, repo_root: Path) -> CheckResults:
    parsed, parse_error = parse_note(path, repo_root=repo_root)
    if parse_error:
        return CheckResults(note_type="unknown", fails=[parse_error])

    assert parsed is not None

    if parsed.document.frontmatter is None:
        return CheckResults(note_type="text", passes=["text file: no frontmatter, no structural requirements"])

    results = CheckResults(note_type=parsed.note_type)
    results.passes.append("frontmatter: valid delimiters, well-formed YAML")
    validate_description(results, parsed.document.frontmatter.get("description"))
    validate_title_and_slug(results, parsed.path, parsed.document)
    validate_type_traits_status(results, parsed.document.frontmatter, parsed.note_type, parsed.profile)
    validate_links_from_document(results, parsed.path, parsed.document.links)
    validate_structure(results, parsed.note_type, parsed.document, parsed.profile)
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
