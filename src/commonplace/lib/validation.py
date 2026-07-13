"""Deterministic validation rules for KB notes."""

from __future__ import annotations

import re
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import unquote, urlsplit

from jsonschema.exceptions import ValidationError

from commonplace.lib.full_pass import (
    FULL_PASS_REPORT_TYPE,
    parse_full_pass_report,
    render_resolution_section,
    resolution_section,
    verify_capture,
)
from commonplace.lib.index_generated import (
    CollectionTagIndex,
    collect_collection_tag_index,
)
from commonplace.lib.naming import MAX_NOTE_SLUG_LENGTH, MAX_NOTE_TITLE_LENGTH
from commonplace.lib.note_parser import ParsedDocument, parse_document
from commonplace.lib.project_paths import (
    collection_for_path,
    is_collection_dir,
    is_type_definition_content,
    iter_visible_markdown_files,
)
from commonplace.lib.quote_verification import verify_content
from commonplace.lib.type_resolver import (
    TypeProfile,
    canonical_type_identity,
    resolve_type_definition,
    resolve_type,
    validate_instance,
)


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

# Generated connect reports preserve the complete source-artifact stem and add
# `.connect` for a stable, reversible mapping. Exempting that derived filename
# assumes these reports remain disposable and gitignored; applying a special
# validator rule is design debt, not a good general naming scheme. The next
# report-filename redesign should budget for suffixes and remove this exception.
_NOTE_SLUG_LIMIT_EXEMPT_TYPES = frozenset({"connect-report"})


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


@dataclass(frozen=True)
class LoadedDocument:
    content: str
    document: ParsedDocument | None
    error: str | None


@dataclass
class ValidationRunResults:
    paths: tuple[Path, ...]
    results: dict[Path, CheckResults]
    collection_structure: list[tuple[Path, str]]


@dataclass
class ValidationRun:
    """Run deterministic checks over one target with shared parse/index caches."""

    repo_root: Path
    paths: tuple[Path, ...]
    collection: Path | None = None
    _documents: dict[Path, LoadedDocument] = field(default_factory=dict, init=False)
    _notes: dict[Path, tuple[ParsedNote | None, str | None]] = field(
        default_factory=dict, init=False
    )
    _collection_indexes: dict[Path, CollectionTagIndex] = field(
        default_factory=dict, init=False
    )

    def __post_init__(self) -> None:
        self.repo_root = self.repo_root.resolve()
        self.paths = tuple(path.resolve() for path in self.paths)
        if self.collection is not None:
            self.collection = self.collection.resolve()

    def load_document(self, path: Path) -> LoadedDocument:
        """Read and parse one Markdown artifact at most once during this run."""
        key = path.resolve()
        if key in self._documents:
            return self._documents[key]
        content = key.read_text(encoding="utf-8")
        document, error = parse_document(content)
        loaded = LoadedDocument(content=content, document=document, error=error)
        self._documents[key] = loaded
        return loaded

    def parse_note(self, path: Path) -> tuple[ParsedNote | None, str | None]:
        """Resolve a cached parsed document's type for deterministic validation."""
        key = path.resolve()
        if key in self._notes:
            return self._notes[key]
        loaded = self.load_document(key)
        if loaded.error:
            result = (None, loaded.error)
            self._notes[key] = result
            return result
        assert loaded.document is not None

        try:
            profile = resolve_type(
                key, loaded.document.frontmatter, repo_root=self.repo_root
            )
        except (FileNotFoundError, ValueError) as exc:
            result = (None, str(exc))
            self._notes[key] = result
            return result

        result = (
            ParsedNote(
                path=key,
                content=loaded.content,
                note_type=profile.type_name,
                profile=profile,
                document=loaded.document,
            ),
            None,
        )
        self._notes[key] = result
        return result

    def collection_index(self, collection: Path) -> CollectionTagIndex:
        """Build tag membership and tag-index entries in one cached scan."""
        key = collection.resolve()
        if key in self._collection_indexes:
            return self._collection_indexes[key]
        index = collect_collection_tag_index(
            key,
            load_document=lambda path: self.load_document(path).document,
        )
        self._collection_indexes[key] = index
        return index

    def impacted_marked_tag_readmes(self, paths: tuple[Path, ...]) -> list[Path]:
        """Return marked tag READMEs whose claims may be affected by paths."""
        seen = {path.resolve() for path in paths}
        impacted: list[Path] = []

        for path in paths:
            parsed, parse_error = self.parse_note(path)
            if parse_error or parsed is None or parsed.document.frontmatter is None:
                continue
            tags = parsed.document.frontmatter.get("tags")
            if not isinstance(tags, list):
                continue
            try:
                collection = collection_for_path(path, self.repo_root)
            except ValueError:
                continue

            for tag in tags:
                if not isinstance(tag, str):
                    continue
                readme = (collection / f"{tag}-README.md").resolve()
                if not readme.is_file() or readme in seen:
                    continue
                readme_parsed, readme_error = self.parse_note(readme)
                if (
                    readme_error
                    or readme_parsed is None
                    or readme_parsed.note_type != "tag-readme"
                ):
                    continue
                frontmatter = readme_parsed.document.frontmatter or {}
                has_checked_mark = frontmatter.get("complete") is True or bool(
                    frontmatter.get("covered_by")
                )
                if not has_checked_mark:
                    continue

                impacted.append(readme)
                seen.add(readme)

        return impacted

    def inbound_info(self, paths: tuple[Path, ...]) -> dict[Path, bool]:
        """Build authored-link inbound presence once for this evaluation."""
        keys = tuple(path.resolve() for path in paths)
        inbound: dict[Path, bool] = {path: False for path in keys}
        resolved_index = {path.resolve(): path for path in keys}
        for source in keys:
            loaded = self.load_document(source)
            if loaded.document is None:
                continue
            for link in loaded.document.links:
                if re.match(r"^[a-z]+://", link):
                    continue
                link_path = link.split("#", 1)[0]
                if not link_path.endswith(".md"):
                    continue
                target = (source.parent / link_path).resolve()
                if target == source:
                    continue
                matched = resolved_index.get(target)
                if matched is not None:
                    inbound[matched] = True

        return inbound

    def validate(self, path: Path) -> CheckResults:
        parsed, parse_error = self.parse_note(path)
        if parse_error:
            return CheckResults(note_type="unknown", fails=[f"[base] {parse_error}"])
        assert parsed is not None
        return _validate_parsed_note(parsed, run=self)

    def evaluate(self) -> ValidationRunResults:
        """Expand explicit impacts and evaluate every anchor in this run."""
        paths = self.paths + tuple(self.impacted_marked_tag_readmes(self.paths))
        inbound = self.inbound_info(paths) if self.collection is not None else {}
        results: dict[Path, CheckResults] = {}

        for path in paths:
            result = self.validate(path)
            if (
                self.collection is not None
                and path in inbound
                and not inbound[path]
                and result.note_type not in {"text", "type-spec"}
            ):
                try:
                    scope = str(self.collection.relative_to(self.repo_root))
                except ValueError:
                    scope = str(self.collection)
                result.infos.append(f"orphan check: no inbound links found in {scope}")
            results[path] = result

        structure = (
            validate_collection_structure(self.collection, repo_root=self.repo_root)
            if self.collection is not None
            else []
        )
        return ValidationRunResults(
            paths=paths,
            results=results,
            collection_structure=structure,
        )


# Type-specific validation rules, registered per canonical type path so adding a
# cross-file validator is a function plus a registration, not another branch
# in validate_note. Rules run after the generic checks and before schema
# validation, in registration order.
TypeRule = Callable[..., None]

_TYPE_RULES: dict[str, list[TypeRule]] = {}


def type_rule(*type_paths: str) -> Callable[[TypeRule], TypeRule]:
    """Register a rule for the given canonical type paths."""

    def register(rule: TypeRule) -> TypeRule:
        for type_path in type_paths:
            _TYPE_RULES.setdefault(type_path, []).append(rule)
        return rule

    return register


def parse_note(path: Path, *, repo_root: Path) -> tuple[ParsedNote | None, str | None]:
    """Parse one note outside a wider run."""
    return ValidationRun(repo_root=repo_root, paths=(path,)).parse_note(path)


def validate_title_and_slug(
    results: CheckResults,
    path: Path,
    document: ParsedDocument,
    *,
    note_type: str,
) -> None:
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

    if note_type in _NOTE_SLUG_LIMIT_EXEMPT_TYPES:
        results.passes.append(
            f"filename slug: {slug_length} chars "
            f"(derived {note_type} name; authored-artifact limit not applied)"
        )
    elif slug_length > MAX_NOTE_SLUG_LENGTH:
        results.fails.append(
            f"filename slug: {slug_length} chars exceeds limit of {MAX_NOTE_SLUG_LENGTH}"
        )
    else:
        results.passes.append(
            f"filename slug: {slug_length} chars (within {MAX_NOTE_SLUG_LENGTH}-char limit)"
        )


def validate_links_from_document(
    results: CheckResults, path: Path, links: tuple[str, ...]
) -> None:
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


def validate_verbatim_quotes(results: CheckResults, content: str, path: Path) -> None:
    """Resolve `verbatim`-marked quotations against the sources they cite.

    A `verbatim` citation claims a quoted span is copied exactly from a linked
    source retained in the KB. That is mechanically decidable, so leaving it
    hand-trusted is the state the derived-copy rule forbids: a false `verbatim`
    claim is a false copy, and false copies fail rather than warn.

    `unresolved` candidates are reported only in notes that demonstrably use the
    convention (they carry at least one resolvable verbatim quote). Prose that
    merely discusses verbatim citation near a link would otherwise warn in every
    KB that never adopted the convention, and a check that cries wolf teaches
    authors to ignore it — which is the failure this check exists to prevent.
    """
    quote_results = verify_content(content, path)
    if not quote_results:
        return

    resolved = [r for r in quote_results if r.status in ("match", "mismatch")]
    mismatches = [r for r in quote_results if r.status == "mismatch"]
    matches = [r for r in quote_results if r.status == "match"]

    for result in mismatches:
        source = result.source.name if result.source else "linked source"
        results.fails.append(
            f"verbatim quote: not found in {source} (line {result.line}): {result.quote!r}"
        )

    if resolved:
        for result in (r for r in quote_results if r.status == "unresolved"):
            results.warns.append(
                f"verbatim quote: {result.detail} (line {result.line})"
            )

    if matches and not mismatches:
        results.passes.append(
            f"verbatim quotes: {len(matches)} resolve against their cited sources"
        )


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


@type_rule("kb/agent-memory-systems/types/agent-memory-system-review.md")
def _quote_citation_rule(
    results: CheckResults, parsed: ParsedNote, *, run: ValidationRun
) -> None:
    validate_quote_citations(results, parsed.content)


@type_rule("kb/types/type-spec.md")
def validate_type_spec_definition(
    results: CheckResults,
    parsed: ParsedNote,
    *,
    run: ValidationRun,
) -> None:
    """Resolve this type-spec as a type definition, including its declared schema."""
    try:
        profile = resolve_type_definition(
            parsed.path,
            repo_root=run.repo_root,
            type_frontmatter=parsed.document.frontmatter,
        )
    except (FileNotFoundError, ValueError) as exc:
        results.fails.append(f"type definition: {exc}")
        return

    if profile.schema_path is None:
        results.passes.append("type definition: schema is explicitly null")
    else:
        results.passes.append(
            f"type definition: declared schema resolves to "
            f"{profile.schema_path.relative_to(run.repo_root)}"
        )


@type_rule("kb/types/tag-readme.md")
def validate_tag_readme(
    results: CheckResults, parsed: ParsedNote, *, run: ValidationRun
) -> None:
    """Enforce the tag-readme type contract: weight gates plus the optional
    `complete` (membership) and `covered_by` (coverage) marks (ADR 026)."""
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
        collection = collection_for_path(parsed.path, run.repo_root)
    except ValueError as exc:
        results.fails.append(f"tag-readme: {exc}")
        return

    source = fm.get("index_source")
    key = str(fm.get("index_key", ""))
    collection_index = run.collection_index(collection)
    notes_by_tag = collection_index.notes_by_tag

    if fm.get("complete") is True:
        if source == "tag":
            members = [(path, title) for path, title, _ in notes_by_tag.get(key, [])]
        else:
            members = [
                (path, title) for path, title, _ in collection_index.tag_index_entries
            ]
        linked = _linked_md_targets(parsed)
        missing = [
            path
            for path, _ in members
            if path.resolve() not in linked and path.resolve() != parsed.path.resolve()
        ]
        if missing:
            for path in missing:
                results.fails.append(
                    f"complete mark: missing entry for {path.relative_to(run.repo_root)} — "
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
            path
            for path, _, _ in notes_by_tag.get(key, [])
            if path.resolve() not in covered_paths
            and path.resolve() != parsed.path.resolve()
        ]
        if uncovered:
            for path in uncovered:
                results.fails.append(
                    f"covered_by: {path.relative_to(run.repo_root)} carries no listed child tag — "
                    f"tag it with one of {covered_by} or revise the list; {_TAG_README_FIX_HINT}"
                )
        else:
            results.passes.append(
                f"covered_by: all tagged notes carry one of {len(covered_by)} children"
            )


@type_rule(FULL_PASS_REPORT_TYPE)
def validate_full_pass_report(
    results: CheckResults, parsed: ParsedNote, *, run: ValidationRun
) -> None:
    """Verify report-owned captures and the canonical resolution projection."""
    try:
        report = parse_full_pass_report(
            parsed.path, parsed.document, repo_root=run.repo_root
        )
    except ValueError as exc:
        results.fails.append(f"full-pass report: {exc}")
        return

    capture_failures = 0
    for guarded_input in report.guarded_inputs:
        _text, actual_sha256, error = verify_capture(
            guarded_input, packet_dir=report.packet_dir
        )
        if error is not None:
            capture_failures += 1
            results.fails.append(
                f"{guarded_input.role} capture: {error}"
                + (f" ({actual_sha256})" if actual_sha256 is not None else "")
            )
    if not capture_failures:
        results.passes.append(
            f"packet captures: all {len(report.guarded_inputs)} present and hash-verified"
        )

    expected_resolution = render_resolution_section(report.frontmatter)
    actual_resolution = resolution_section(report.body)
    if actual_resolution != expected_resolution:
        results.fails.append(
            "resolution projection: body section does not match canonical frontmatter rendering"
        )
    else:
        results.passes.append("resolution projection: body matches frontmatter")


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


def _merge_labelled(dest: CheckResults, src: CheckResults, source: str) -> None:
    """Fold one check group's findings into the result, tagged with its source."""
    for level in ("passes", "warns", "fails", "infos"):
        getattr(dest, level).extend(
            f"[{source}] {message}" for message in getattr(src, level)
        )


def _validate_parsed_note(parsed: ParsedNote, *, run: ValidationRun) -> CheckResults:
    """Validate a parsed note against the base contract, type rules, and schema.

    Every finding is labelled with the source that produced it, because a reader
    who only read the type spec would otherwise get failures from rules that spec
    never mentions. The source is attached here, at dispatch, rather than by each
    check, so it is decided by *where a check runs* and cannot be forgotten.

    Three sources, documented in `kb/reference/validation-contract.md`:

    `base`
        Applies to every typed note whatever its type. Includes the referential
        checks (link health, verbatim quotes), which the schema cannot express
        because JSON Schema cannot dereference.
    `type: <name>`
        Imperative rules the type owns. May dereference (tag-readme marks are
        re-derived from the collection), which is why type-owned and referential
        are independent axes, not two ends of one.
    `schema`
        Declarative constraints the type's schema owns, over frontmatter *and*
        body-derived facts (headings, links, dates).
    """
    if parsed.document.frontmatter is None:
        return CheckResults(
            note_type="text",
            passes=["[base] text file: no frontmatter, no structural requirements"],
        )

    results = CheckResults(note_type=parsed.note_type)

    base = CheckResults(note_type=parsed.note_type)
    base.passes.append("frontmatter: valid delimiters, well-formed YAML")
    validate_title_and_slug(
        base,
        parsed.path,
        parsed.document,
        note_type=parsed.note_type,
    )
    validate_links_from_document(base, parsed.path, parsed.document.links)
    validate_verbatim_quotes(base, parsed.content, parsed.path)
    _merge_labelled(results, base, "base")

    type_identity = canonical_type_identity(parsed.profile)
    for rule in _TYPE_RULES.get(type_identity, []):
        type_results = CheckResults(note_type=parsed.note_type)
        rule(type_results, parsed, run=run)
        _merge_labelled(results, type_results, f"type: {parsed.note_type}")

    schema_results = CheckResults(note_type=parsed.note_type)
    apply_schema_validation(schema_results, parsed)
    _merge_labelled(results, schema_results, "schema")

    return results


def validate_note(path: Path, *, repo_root: Path) -> CheckResults:
    """Run the deterministic pipeline on one note outside a wider run."""
    return ValidationRun(repo_root=repo_root, paths=(path,)).validate(path)


def validate_collection_structure(
    collection: Path, *, repo_root: Path
) -> list[tuple[Path, str]]:
    """Return anchored structural failures for one collection boundary."""
    collection = collection.resolve()
    repo_root = repo_root.resolve()
    if not is_collection_dir(collection):
        return []

    failures: list[tuple[Path, str]] = []
    for path in iter_visible_markdown_files(collection):
        if path.name != "COLLECTION.md" or path.parent == collection:
            continue
        if is_type_definition_content(path, collection):
            continue
        failures.append(
            (
                path,
                "nested COLLECTION.md: "
                f"{path.relative_to(repo_root)} is inside collection "
                f"{collection.relative_to(repo_root)}",
            )
        )
    return failures


def run_validation(
    paths: tuple[Path, ...],
    *,
    repo_root: Path,
    collection: Path | None = None,
) -> ValidationRunResults:
    """Evaluate one validation target with shared parsing and indexes."""
    return ValidationRun(
        repo_root=repo_root,
        paths=paths,
        collection=collection,
    ).evaluate()
