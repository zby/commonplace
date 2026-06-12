"""Deterministic validation rules for KB notes."""

from __future__ import annotations

import re
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import unquote, urlsplit

from jsonschema.exceptions import ValidationError

from commonplace.lib.naming import MAX_NOTE_SLUG_LENGTH, MAX_NOTE_TITLE_LENGTH
from commonplace.lib.note_parser import ParsedDocument, parse_document
from commonplace.lib.type_resolver import TypeProfile, resolve_type, validate_instance


# Weight gates for tag-readme artifacts: the type contract is that a tag's
# curated head stays a cheap whole-read surface (ADR 026). Bytes gate; entry
# count is reported as diagnosis only.
TAG_README_SOFT_BYTES = 8 * 1024
TAG_README_HARD_BYTES = 16 * 1024
# Soft fan-out limit for covered_by: routing value needs the alternatives held
# in mind at once; past this, group children under intermediate tags.
TAG_README_MAX_FANOUT = 7
# Validator messages must name the fixing instruction so the maintenance loop
# is self-routing (ADR 026).
_TAG_README_FIX_HINT = "see kb/instructions/maintain-curated-indexes.md"


# A schema violation fails by default — the schema is the contract, so breaking a
# constraint blocks unless its author explicitly opts down. A subschema lowers its
# own severity with `severity: warn` (read from error.schema below), optionally
# keyed by a stable `ruleId` so it can be re-leveled or referenced later. This is
# the Spectral/Schematron pattern (severity authored on an identified rule); see
# kb/reference/adr/024-schema-severity-is-per-constraint-fail-by-default.md.
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


# Type-specific validation rules, registered per type name so adding a
# cross-file validator is a function plus a registration, not another branch
# in validate_note. Rules run after the generic checks and before schema
# validation, in registration order.
TypeRule = Callable[..., None]

_TYPE_RULES: dict[str, list[TypeRule]] = {}


def type_rule(*type_names: str) -> Callable[[TypeRule], TypeRule]:
    """Register a rule `(results, parsed, *, repo_root) -> None` for the given type names."""

    def register(rule: TypeRule) -> TypeRule:
        for type_name in type_names:
            _TYPE_RULES.setdefault(type_name, []).append(rule)
        return rule

    return register


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


def _linked_md_targets(parsed: ParsedNote) -> set[Path]:
    """Resolve the note's local markdown links to absolute paths."""
    targets: set[Path] = set()
    for link in parsed.document.links:
        parsed_url = urlsplit(link)
        if parsed_url.scheme or parsed_url.netloc:
            continue
        link_path = unquote(parsed_url.path)
        if not link_path.endswith(".md") or Path(link_path).is_absolute():
            continue
        targets.add((parsed.path.parent / link_path).resolve())
    return targets


@type_rule("agent-memory-system-review")
def _quote_citation_rule(results: CheckResults, parsed: ParsedNote, *, repo_root: Path) -> None:
    validate_quote_citations(results, parsed.content)


@type_rule("tag-readme")
def validate_tag_readme(results: CheckResults, parsed: ParsedNote, *, repo_root: Path) -> None:
    """Enforce the tag-readme type contract: weight gates plus the optional
    `complete` (membership) and `covered_by` (coverage) marks (ADR 026)."""
    from commonplace.lib.index_generated import (
        collect_notes_by_tag,
        collect_tag_index_entries,
    )
    from commonplace.lib.project_paths import collection_for_path

    fm = parsed.document.frontmatter or {}

    size = len(parsed.content.encode("utf-8"))
    entry_count = len(re.findall(r"^\s*- \[", parsed.content, re.MULTILINE))
    if size > TAG_README_HARD_BYTES:
        results.fails.append(
            f"weight gate: {size} B exceeds hard limit {TAG_README_HARD_BYTES} B "
            f"({entry_count} entries) — curate harder, split the tag, or narrow it; {_TAG_README_FIX_HINT}"
        )
    elif size > TAG_README_SOFT_BYTES:
        results.warns.append(
            f"weight gate: {size} B exceeds soft limit {TAG_README_SOFT_BYTES} B "
            f"({entry_count} entries) — plan the exit; {_TAG_README_FIX_HINT}"
        )
    else:
        results.passes.append(
            f"weight gate: {size} B within {TAG_README_SOFT_BYTES} B soft limit ({entry_count} entries)"
        )

    try:
        collection = collection_for_path(parsed.path, repo_root)
    except ValueError as exc:
        results.fails.append(f"tag-readme: {exc}")
        return

    source = fm.get("index_source")
    key = str(fm.get("index_key", ""))
    notes_by_tag = collect_notes_by_tag(collection)

    if fm.get("complete") is True:
        if source == "tag":
            members = [(path, title) for path, title, _ in notes_by_tag.get(key, [])]
        else:
            members = [(path, title) for path, title, _ in collect_tag_index_entries(collection, repo_root)]
        linked = _linked_md_targets(parsed)
        missing = [
            path for path, _ in members
            if path.resolve() not in linked and path.resolve() != parsed.path.resolve()
        ]
        if missing:
            for path in missing:
                results.fails.append(
                    f"complete mark: missing entry for {path.relative_to(repo_root)} — "
                    f"add it with a context phrase or drop the mark; {_TAG_README_FIX_HINT}"
                )
        else:
            results.passes.append(f"complete mark: all {len(members)} members linked")

    covered_by = fm.get("covered_by")
    if isinstance(covered_by, list) and covered_by:
        if len(covered_by) > TAG_README_MAX_FANOUT:
            results.warns.append(
                f"covered_by fan-out: {len(covered_by)} children exceeds ~{TAG_README_MAX_FANOUT} — "
                f"group children under intermediate tags; {_TAG_README_FIX_HINT}"
            )
        covered_paths = {
            path.resolve()
            for child in covered_by
            for path, _, _ in notes_by_tag.get(str(child), [])
        }
        uncovered = [
            path for path, _, _ in notes_by_tag.get(key, [])
            if path.resolve() not in covered_paths and path.resolve() != parsed.path.resolve()
        ]
        if uncovered:
            for path in uncovered:
                results.fails.append(
                    f"covered_by: {path.relative_to(repo_root)} carries no listed child tag — "
                    f"tag it with one of {covered_by} or revise the list; {_TAG_README_FIX_HINT}"
                )
        else:
            results.passes.append(
                f"covered_by: all tagged notes carry one of {len(covered_by)} children"
            )


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
    for rule in _TYPE_RULES.get(parsed.note_type, []):
        rule(results, parsed, repo_root=repo_root)
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
