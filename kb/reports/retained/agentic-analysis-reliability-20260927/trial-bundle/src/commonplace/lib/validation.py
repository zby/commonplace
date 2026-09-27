"""Deterministic validation rules for KB artifacts and repository invariants."""

from __future__ import annotations

import hashlib
import re
import subprocess
from collections.abc import Callable, Collection
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml
from jsonschema.exceptions import ValidationError

from commonplace.lib import frontmatter
from commonplace.lib.agentic_analysis import (
    AGENTIC_ANALYSIS_RUN_TYPE,
    parse_agentic_analysis_run_state,
    verify_agentic_analysis_run_state,
)
from commonplace.lib.full_pass import (
    FULL_PASS_REPORT_TYPE,
    parse_full_pass_report,
    render_resolution_section,
    resolution_section,
    verify_capture,
)
from commonplace.lib.index_generated import (
    TagSpace,
    collect_tag_space,
    head_path,
    tag_for_head,
    tags_collection,
)
from commonplace.lib.naming import (
    MAX_NOTE_SLUG_LENGTH,
    MAX_NOTE_TITLE_LENGTH,
    WRITE_BRIEF_TYPE,
    is_write_brief_path,
    write_brief_name_for,
    write_brief_target_for,
)
from commonplace.lib.note_parser import (
    ParsedDocument,
    find_markdown_links_with_text,
    parse_document,
)
from commonplace.lib.project_paths import (
    collection_for_path,
    is_collection_dir,
    is_type_definition_content,
    iter_validation_markdown_files,
    kb_root,
)
from commonplace.lib.quote_verification import (
    INGEST_QUOTES_HEADING_RE,
    NEXT_H2_RE,
    QuoteResult,
    normalize_text,
    verify_content,
)
from commonplace.lib.type_resolver import (
    TypeProfile,
    canonical_type_identity,
    resolve_type,
    resolve_type_definition,
    validate_instance,
)

TAG_README_TYPE = "types/tag-readme.md"
# Weight gates for tag-readme artifacts: the type contract is that a tag's
# curated head stays a cheap whole-read surface (ADR 026). Bytes gate; entry
# count is reported as diagnosis only.
TAG_README_SOFT_BYTES = 8 * 1024
TAG_README_HARD_BYTES = 16 * 1024
# Validator messages must name the fixing instruction so the maintenance loop
# is self-routing (ADR 026).
_TAG_README_FIX_HINT = "see kb/instructions/maintain-curated-indexes.md"

# Artifact-side grounding bound: a note may cite at most this many distinct
# tracked sources without a verified verbatim quotation paired to each, so
# that its grounding review fits one pass. Note links are exempt;
# `(snapshot required)` sources always count.
MAX_UNQUOTED_SOURCES = 5
_UNQUOTED_SOURCES_FIX_HINT = (
    "quote the supporting passage verbatim via cp-skill-ground, or split the claim"
)

# Generated connect reports preserve the complete source-artifact stem and add
# `.connect` for a stable, reversible mapping. Exempting that derived filename
# assumes these reports remain disposable and gitignored; applying a special
# validator rule is design debt, not a good general naming scheme. The next
# report-filename redesign should budget for suffixes and remove this exception.
# A write brief's name is derived from its target's stem (ADR 092), so the
# target's slug limit already bounds it.
_NOTE_SLUG_LIMIT_EXEMPT_TYPES = frozenset({"connect-report", "write-brief"})

_PROPOSAL_ARCHIVE_RELATIVE_PATH = Path("kb/reference/proposals/archive")


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
    collection_warnings: list[tuple[Path, str]]


@dataclass
class ValidationRun:
    """Run deterministic checks over one target with shared parse/index caches."""

    repo_root: Path
    paths: tuple[Path, ...]
    collection: Path | None = None
    content_overrides: dict[Path, str] = field(default_factory=dict)
    _documents: dict[Path, LoadedDocument] = field(default_factory=dict, init=False)
    _notes: dict[Path, tuple[ParsedNote | None, str | None]] = field(
        default_factory=dict, init=False
    )
    _tag_space: TagSpace | None = field(default=None, init=False)
    _git_ignored: dict[Path, bool] = field(default_factory=dict, init=False)
    _verbatim_quotes: dict[Path, list[QuoteResult]] = field(
        default_factory=dict, init=False
    )
    _snapshot_dirs: dict[Path, SnapshotDirectory] = field(
        default_factory=dict, init=False
    )

    def __post_init__(self) -> None:
        self.repo_root = self.repo_root.resolve()
        self.paths = tuple(path.resolve() for path in self.paths)
        if self.collection is not None:
            self.collection = self.collection.resolve()
        self.content_overrides = {
            path.resolve(): content for path, content in self.content_overrides.items()
        }

    def load_document(self, path: Path) -> LoadedDocument:
        """Read and parse one Markdown artifact at most once during this run."""
        key = path.resolve()
        if key in self._documents:
            return self._documents[key]
        content = self.content_overrides.get(key)
        if content is None:
            content = key.read_text(encoding="utf-8")
        document, error = parse_document(content)
        loaded = LoadedDocument(content=content, document=document, error=error)
        self._documents[key] = loaded
        return loaded

    def load_frontmatter(self, path: Path) -> frontmatter.FrontmatterResult:
        """Serve type-spec frontmatter from this run's parse cache."""
        loaded = self.load_document(path)
        if loaded.error:
            return frontmatter.FrontmatterResult(errors=[loaded.error])
        assert loaded.document is not None
        return frontmatter.FrontmatterResult(data=loaded.document.frontmatter or {})

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
                key,
                loaded.document.frontmatter,
                repo_root=self.repo_root,
                load_frontmatter=self.load_frontmatter,
            )
        except (FileNotFoundError, TypeError, ValueError) as exc:
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

    def tag_space(self) -> TagSpace:
        """Scan the KB's tag space once per run (ADR 089)."""
        if self._tag_space is None:
            self._tag_space = collect_tag_space(
                self.repo_root,
                load_document=lambda path: self.load_document(path).document,
            )
        return self._tag_space

    def verbatim_quotes(self, parsed: ParsedNote) -> list[QuoteResult]:
        """Resolve a note's verbatim quotes once for every check that reads them."""
        if parsed.path not in self._verbatim_quotes:
            self._verbatim_quotes[parsed.path] = verify_content(
                parsed.content,
                parsed.path,
                load_source=lambda path: self.load_document(path).content,
            )
        return self._verbatim_quotes[parsed.path]

    def snapshots(self, directory: Path) -> SnapshotDirectory:
        """Share one snapshot-cache scan across every check in this run."""
        key = directory.resolve()
        if key not in self._snapshot_dirs:
            self._snapshot_dirs[key] = SnapshotDirectory(key)
        return self._snapshot_dirs[key]

    def prime_git_ignored(self, paths: tuple[Path, ...]) -> None:
        """Cache which paths Git actually excludes from version control.

        Git-ignored files can still be validated explicitly. They retain the
        structural pipeline, but authored-library length limits do not apply to
        them. A missing Git executable or non-worktree root fails closed: the
        ordinary authored limits remain in force.
        """
        pending: dict[str, Path] = {}
        for path in paths:
            key = path.resolve()
            if key in self._git_ignored:
                continue
            try:
                relative = key.relative_to(self.repo_root).as_posix()
            except ValueError:
                self._git_ignored[key] = False
                continue
            pending[relative] = key

        if not pending:
            return

        for key in pending.values():
            self._git_ignored[key] = False

        try:
            result = subprocess.run(
                ["git", "check-ignore", "-z", "--stdin"],
                cwd=self.repo_root,
                check=False,
                capture_output=True,
                input="\0".join(pending) + "\0",
                text=True,
                timeout=10,
            )
        except (OSError, subprocess.SubprocessError):
            return
        if result.returncode not in {0, 1}:
            return

        for relative in result.stdout.split("\0"):
            key = pending.get(relative)
            if key is not None:
                self._git_ignored[key] = True

    def is_git_ignored(self, path: Path) -> bool:
        """Return whether Git excludes one artifact from version control."""
        key = path.resolve()
        self.prime_git_ignored((key,))
        return self._git_ignored[key]

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
            tag_space = self.tag_space()
            if not tag_space.is_participating(path):
                continue

            for tag in tags:
                if not isinstance(tag, str):
                    continue
                readme = tag_space.heads.get(tag)
                if readme is None or readme in seen:
                    continue
                readme_parsed, readme_error = self.parse_note(readme)
                if (
                    readme_error
                    or readme_parsed is None
                    or canonical_type_identity(readme_parsed.profile)
                    != TAG_README_TYPE
                ):
                    continue
                frontmatter = readme_parsed.document.frontmatter or {}
                if frontmatter.get("complete") is not True:
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
                target = _resolve_local_link_target(source, link)
                if target is None or target.suffix != ".md":
                    continue
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
        self.prime_git_ignored(paths)
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
        collection_warnings = (
            validate_source_snapshot_cache(
                self.collection,
                repo_root=self.repo_root,
                snapshots=self.snapshots(self.collection / ".snapshots"),
            )
            if self.collection is not None
            else []
        )
        return ValidationRunResults(
            paths=paths,
            results=results,
            collection_structure=structure,
            collection_warnings=collection_warnings,
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


def validate_title_and_slug(
    results: CheckResults,
    path: Path,
    document: ParsedDocument,
    *,
    note_type: str,
    git_ignored: bool,
) -> None:
    title = document.title.strip()
    title_length = len(title)
    slug_length = len(path.stem)

    if git_ignored:
        results.passes.append(
            f"title: {title_length} chars "
            "(git-ignored artifact; authored-artifact limit not applied)"
        )
    elif title_length > MAX_NOTE_TITLE_LENGTH:
        results.fails.append(
            f"title: {title_length} chars exceeds limit of {MAX_NOTE_TITLE_LENGTH}"
        )
    else:
        results.passes.append(
            f"title: {title_length} chars (within {MAX_NOTE_TITLE_LENGTH}-char limit)"
        )

    if git_ignored:
        results.passes.append(
            f"filename slug: {slug_length} chars "
            "(git-ignored artifact; authored-artifact limit not applied)"
        )
    elif note_type in _NOTE_SLUG_LIMIT_EXEMPT_TYPES:
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


def _resolve_local_link_target(source: Path, link: str) -> Path | None:
    """Resolve a local relative link target with URL syntax normalized once."""
    parsed = urlsplit(link)
    if parsed.scheme or parsed.netloc:
        return None
    link_path = unquote(parsed.path)
    if not link_path or Path(link_path).is_absolute():
        return None
    return (source.parent / link_path).resolve()


def validate_links_from_document(
    results: CheckResults,
    path: Path,
    links: tuple[str, ...],
    *,
    available_paths: Collection[Path] = (),
) -> None:
    """Resolve links against disk and normalized paths supplied by this validation run."""
    missing: list[str] = []
    for link in links:
        target = _resolve_local_link_target(path, link)
        if target is None:
            continue
        if target not in available_paths and not target.exists():
            missing.append(link)

    if missing:
        for link in missing:
            results.warns.append(f"link health: missing target {link}")
    else:
        results.passes.append("link health: all local relative links resolve")


def validate_proposal_archive_links(
    results: CheckResults,
    path: Path,
    links: tuple[str, ...],
    *,
    repo_root: Path,
) -> None:
    """Keep archived proposals from becoming load-bearing library sources.

    The boundary is crossed only from outside (ADR 056): a link from one
    archived file to another stays inside the frozen set and re-admits
    nothing to the frontier, so archive-internal links are not checked here.
    """
    source = path.resolve()
    kb = kb_root(repo_root).resolve()
    archive = (repo_root / _PROPOSAL_ARCHIVE_RELATIVE_PATH).resolve()
    archive_readme = archive / "README.md"
    work = kb / "work"

    for exempt_root in (work, archive):
        try:
            source.relative_to(exempt_root)
            return
        except ValueError:
            pass

    if source == archive_readme:
        return

    try:
        collection_for_path(source, repo_root)
    except ValueError:
        if not is_type_definition_content(source, kb):
            return

    forbidden: list[str] = []
    for link in links:
        target = _resolve_local_link_target(source, link)
        if target is None or target == archive_readme:
            continue
        try:
            target.relative_to(archive)
        except ValueError:
            continue
        forbidden.append(link)

    if forbidden:
        for link in forbidden:
            results.fails.append(
                "proposal archive boundary: library artifact links to "
                f"archived proposal {link}"
            )
    else:
        results.passes.append(
            "proposal archive boundary: no links to archived proposal files"
        )


def validate_quote_citations(results: CheckResults, content: str) -> None:
    """Shape-check quote-anchored citations (a blockquote + `> ---` attribution).

    Main-review publication resolves generated quote anchors against its frozen
    source. The source is not retained in the KB, so standing validation only
    confirms that each citation is well-formed and names a source.
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


def validate_verbatim_quotes(
    results: CheckResults, quote_results: list[QuoteResult]
) -> None:
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


INGEST_QUOTE_RE = re.compile(
    r"^\s*-\s*\*\*Source extract \(verbatim\):\*\*\s*(?P<text>.+?)\s*$",
    re.MULTILINE,
)
EMPTY_INGEST_QUOTES_SENTENCE = "No source quotes have been retained yet."
SNAPSHOT_REQUIRED_MARKER = "(snapshot required)"
SNAPSHOT_SHA256_RE = re.compile(
    r"^snapshot_sha256:\s*(?P<checksum>[0-9a-f]{64})\s*$",
    re.MULTILINE,
)
ORIGINAL_SNAPSHOT_SHA256_RE = re.compile(
    r"^original_snapshot_sha256:\s*(?P<checksum>[0-9a-f]{64})\s*$",
    re.MULTILINE,
)


def _name_paired_snapshot(path: Path) -> Path:
    slug = path.name[: -len(".ingest.md")]
    return path.parent / ".snapshots" / f"{slug}.md"


def _content_outside_ingest_quotes(content: str) -> str:
    heading = INGEST_QUOTES_HEADING_RE.search(content)
    if heading is None:
        return content
    next_heading = NEXT_H2_RE.search(content, heading.end())
    section_end = next_heading.start() if next_heading is not None else len(content)
    return content[: heading.start()] + content[section_end:]


def _display_snapshot_path(path: Path, sources_dir: Path) -> str:
    try:
        return str(path.resolve().relative_to(sources_dir.resolve()))
    except ValueError:
        return str(path)


def _http_source_from_content(content: str) -> str | None:
    source = frontmatter.parse(content).data.get("source")
    if not isinstance(source, str) or not source.startswith(("http://", "https://")):
        return None
    return source


@dataclass(frozen=True)
class SnapshotFacts:
    """Identity facts of one local snapshot file: exact bytes and source URL."""

    sha256: str | None = None
    source: str | None = None
    error: str | None = None


class SnapshotDirectory:
    """Read each snapshot in one flat cache directory at most once."""

    def __init__(self, directory: Path) -> None:
        self.directory = directory
        self._facts: dict[Path, SnapshotFacts] = {}
        self._scanned = False

    def read(self, path: Path) -> SnapshotFacts:
        key = path.resolve()
        if key not in self._facts:
            try:
                data = key.read_bytes()
            except OSError as error:
                self._facts[key] = SnapshotFacts(error=str(error))
            else:
                self._facts[key] = SnapshotFacts(
                    sha256=hashlib.sha256(data).hexdigest(),
                    source=_http_source_from_content(
                        data.decode("utf-8", errors="replace")
                    ),
                )
        return self._facts[key]

    def all(self) -> dict[Path, SnapshotFacts]:
        if not self._scanned:
            for path in sorted(self.directory.glob("*.md")):
                if path.is_file():
                    self.read(path)
            self._scanned = True
        return self._facts

    def with_sha256(self, checksum: str) -> tuple[Path, ...]:
        return tuple(p for p, f in self.all().items() if f.sha256 == checksum)

    def with_source(self, source: str | None) -> tuple[Path, ...]:
        if source is None:
            return ()
        return tuple(p for p, f in self.all().items() if f.source == source)


def validate_ingest_snapshot_pairing(
    results: CheckResults,
    content: str,
    path: Path,
    *,
    snapshots: SnapshotDirectory | None = None,
) -> None:
    """Diagnose retained snapshot bytes that are not name-paired to an ingest.

    Snapshot absence remains valid because the cache is ignored. When local
    bytes are present, however, the ingest's durable checksum can distinguish a
    missing cache entry from filename drift without authorizing the alternate
    path for grounding or mutation.
    """
    recorded = SNAPSHOT_SHA256_RE.search(content)
    # A missing checksum is the ingest schema's required-field failure.
    if not path.name.endswith(".ingest.md") or recorded is None:
        return

    expected = _name_paired_snapshot(path)
    if snapshots is None:
        snapshots = SnapshotDirectory(expected.parent)
    source = _http_source_from_content(content)
    checksum = recorded.group("checksum")
    shown = _display_snapshot_path(expected, path.parent)

    def located(paths: tuple[Path, ...]) -> str:
        return ", ".join(_display_snapshot_path(match, path.parent) for match in paths)

    def warn(message: str) -> None:
        results.warns.append(f"snapshot pairing: {message}")

    if expected.is_file():
        facts = snapshots.read(expected)
        if facts.error is not None:
            warn(f"{shown} is unreadable ({facts.error})")
        elif facts.sha256 == checksum:
            if source is not None and facts.source not in (None, source):
                warn(
                    f"{shown} matches snapshot_sha256 but its source URL "
                    "differs from the ingest"
                )
        elif exact := tuple(
            match for match in snapshots.with_sha256(checksum)
            if match != expected.resolve()
        ):
            warn(
                f"{shown} does not match snapshot_sha256; the exact recorded "
                f"bytes are at {located(exact)}"
            )
        else:
            by_url = snapshots.with_source(source)
            detail = f"; the source URL matches {located(by_url)}" if by_url else ""
            warn(
                f"{shown} does not match snapshot_sha256 and no exact local "
                f"match was found{detail}"
            )
        return

    exact = snapshots.with_sha256(checksum)
    if len(exact) == 1:
        warn(
            f"expected {shown} is absent; snapshot_sha256 locates the exact "
            f"recorded bytes at {located(exact)}"
        )
    elif exact:
        warn(
            f"expected {shown} is absent; snapshot_sha256 matches multiple "
            f"local files ({located(exact)})"
        )
    elif by_url := snapshots.with_source(source):
        warn(
            f"expected {shown} is absent; its source URL matches "
            f"{located(by_url)}, but snapshot_sha256 identifies different bytes"
        )


def validate_ingest_quotes(
    results: CheckResults,
    content: str,
    path: Path,
    *,
    snapshots: SnapshotDirectory | None = None,
) -> None:
    """Resolve an ingest's retained quotes against its name-paired snapshot.

    A `Source extract (verbatim)` asserts the span occurs in the observation the
    ingest's `snapshot_sha256` names. That is mechanically decidable whenever the
    snapshot is present, so leaving it hand-trusted is the state the derived-copy
    rule forbids — and a measured sweep found five false extracts that the
    grounding instruction, the ingest skill's append path, and ADR 073 all
    require to be checked while no code checked any of them.

    The check is *conditional* on retention, because `kb/sources/.snapshots/` is
    ignored: a fresh clone has the ingest and the checksum but not the bytes.
    Absent snapshot is silence, not a finding. A checksum that disagrees warns
    rather than fails, because the local file is then not the recorded
    observation and the extracts cannot be judged against it either way.
    ADR 023 settled this split for code-grounded quotes; this is the
    `kb/sources/` half it named and deferred.
    """
    if not path.name.endswith(".ingest.md"):
        # Instructions and type specs display the quote template; only a tracked
        # ingest report asserts one. Warning on the others is the cries-wolf
        # failure ADR 046 names, and it teaches authors to ignore the check.
        return

    extracts = [m.group("text") for m in INGEST_QUOTE_RE.finditer(content)]
    if not extracts:
        return

    outside_quotes = _content_outside_ingest_quotes(content)
    if EMPTY_INGEST_QUOTES_SENTENCE in outside_quotes:
        results.fails.append(
            "source quotes: populated Quotes section conflicts with "
            f"{EMPTY_INGEST_QUOTES_SENTENCE!r} elsewhere in the ingest"
        )
    if SNAPSHOT_REQUIRED_MARKER in outside_quotes:
        results.warns.append(
            "source quotes: populated Quotes section coexists with "
            f"{SNAPSHOT_REQUIRED_MARKER!r}; verify the marker still names a claim "
            "that needs broader snapshot context"
        )

    recorded = SNAPSHOT_SHA256_RE.search(content)
    if recorded is None:
        return

    # The pairing check owns missing, unreadable, and mismatched snapshot
    # diagnostics independently of whether Quotes happens to be populated.
    snapshot = _name_paired_snapshot(path)
    if not snapshot.is_file():
        return
    if snapshots is None:
        snapshots = SnapshotDirectory(snapshot.parent)
    if snapshots.read(snapshot).sha256 != recorded.group("checksum"):
        return
    try:
        snapshot_text = snapshot.read_text(encoding="utf-8")
    except OSError:
        return

    haystack = normalize_text(snapshot_text)
    missing = [e for e in extracts if normalize_text(e) not in haystack]
    for extract in missing:
        results.fails.append(
            f"source quote: not found in the checksum-verified snapshot: {extract!r}"
        )
    if not missing:
        results.passes.append(
            f"source quotes: {len(extracts)} resolve against the pinned snapshot"
        )


def _linked_md_targets(parsed: ParsedNote) -> set[Path]:
    """Resolve the note's local markdown links to absolute paths."""
    targets: set[Path] = set()
    for link in parsed.document.links:
        target = _resolve_local_link_target(parsed.path, link)
        if target is None or target.suffix != ".md":
            continue
        targets.add(target)
    return targets


@type_rule("types/snapshot.md")
def _snapshot_body_rule(
    results: CheckResults, parsed: ParsedNote, *, run: ValidationRun
) -> None:
    del run
    first_nonblank = next(
        (line.strip() for line in parsed.document.body.splitlines() if line.strip()),
        None,
    )
    starts_with_h1 = first_nonblank is not None and re.fullmatch(
        r"#(?!#)[ \t]+\S.*", first_nonblank
    ) is not None
    if not starts_with_h1:
        results.fails.append(
            "snapshot structure: first nonblank body line must be an H1 title"
        )
        return
    results.passes.append("snapshot structure: body starts with an H1 title")


@type_rule("agent-memory-systems/types/agent-memory-system-review.md")
def _quote_citation_rule(
    results: CheckResults, parsed: ParsedNote, *, run: ValidationRun
) -> None:
    validate_quote_citations(results, parsed.content)


@type_rule("types/agentic-system-analysis-result.md")
@type_rule("types/agent-memory-analysis-report.md")
def _agentic_evidence_and_references_rule(
    results: CheckResults, parsed: ParsedNote, *, run: ValidationRun
) -> None:
    from commonplace.lib.agentic_analysis import _quote_citations
    from commonplace.lib.agentic_records import record_reference_errors

    metadata = parsed.document.frontmatter or {}
    is_report = metadata.get("type") == "types/agent-memory-analysis-report.md"
    errors = record_reference_errors(parsed.document.body, memory_report=is_report)
    results.fails.extend(errors)
    if not errors:
        results.passes.append("record references: explicit IDs and declarations checked")
    validate_quote_citations(results, parsed.content)
    disposition = metadata.get("report-status" if is_report else "result-disposition")
    if disposition == "complete" and not any(
        quote and attribution for _, quote, attribution in _quote_citations(parsed.document.body)
    ):
        results.fails.append(
            "source evidence: complete analysis requires quoted source evidence; "
            "bare file and line citations are insufficient"
        )


@type_rule("types/agentic-system-analysis-result.md")
def _agentic_comparison_rule(
    results: CheckResults, parsed: ParsedNote, *, run: ValidationRun
) -> None:
    from commonplace.lib.systems_matrix import validate_comparison

    metadata = parsed.document.frontmatter or {}
    if "memory-comparison" not in metadata:
        return
    try:
        validate_comparison(metadata["memory-comparison"], parsed.document.body)
    except ValueError as exc:
        results.fails.append(f"memory comparison: {exc}")
    else:
        results.passes.append("memory comparison: assessments and canonical references resolve")


@type_rule("types/agent-memory-analysis-report.md")
def _memory_report_comparison_rule(
    results: CheckResults, parsed: ParsedNote, *, run: ValidationRun
) -> None:
    from commonplace.lib.systems_matrix import validate_comparison

    metadata = parsed.document.frontmatter or {}
    try:
        validate_comparison(
            metadata.get("memory-comparison"), parsed.document.body,
            memory_report=True,
        )
    except ValueError as exc:
        results.fails.append(f"memory comparison: {exc}")
    else:
        results.passes.append(
            "memory comparison: assessments and shared or proposed references resolve"
        )


@type_rule("types/type-spec.md")
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
            load_frontmatter=run.load_frontmatter,
        )
    except (FileNotFoundError, TypeError, ValueError) as exc:
        results.fails.append(f"type definition: {exc}")
        return

    if profile.schema_path is None:
        results.passes.append("type definition: schema is explicitly null")
    else:
        results.passes.append(
            f"type definition: declared schema resolves to "
            f"{profile.schema_path.relative_to(run.repo_root)}"
        )


@type_rule(TAG_README_TYPE)
def validate_tag_readme(
    results: CheckResults, parsed: ParsedNote, *, run: ValidationRun
) -> None:
    """Enforce the tag-readme type contract: the head's place and identity
    (ADR 089), weight gates, and the optional `complete` mark, which claims the
    head reaches every member in one hop (ADR 026 as amended by ADR 090)."""
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

    tag = tag_for_head(parsed.path)
    expected_dir = tags_collection(run.repo_root).resolve()
    if tag is None or parsed.path.resolve().parent != expected_dir:
        results.fails.append(
            "tag head: a head is kb/tags/<tag>-README.md and nothing else — "
            f"{parsed.path.relative_to(run.repo_root)} is not; move it with "
            f"commonplace-relocate-note; {_TAG_README_FIX_HINT}"
        )
        return
    results.passes.append(f"tag head: names the tag `{tag}` by its filename")

    tag_space = run.tag_space()
    if tag_space.declaration_error:
        results.warns.append(
            f"tag space: {tag_space.declaration_error} — marks checked against no members"
        )
    members = tag_space.notes_by_tag.get(tag, [])

    if fm.get("complete") is True:
        linked = _linked_md_targets(parsed)
        linked_heads = [
            child
            for target in linked
            if target.parent == expected_dir and (child := tag_for_head(target))
        ]
        covered = {
            path.resolve()
            for child in linked_heads
            for path, _, _ in tag_space.notes_by_tag.get(child, [])
        }
        missing = [
            path
            for path, _, _ in members
            if path.resolve() not in linked
            and path.resolve() not in covered
            and path.resolve() != parsed.path.resolve()
        ]
        if missing:
            for path in missing:
                results.fails.append(
                    f"complete mark: missing entry for {path.relative_to(run.repo_root)} — "
                    "link it with a context phrase, link its tag's head, or drop the mark; "
                    f"{_TAG_README_FIX_HINT}"
                )
        else:
            results.passes.append(
                f"complete mark: all {len(members)} members linked or reached "
                f"through {len(linked_heads)} linked heads"
            )


@type_rule("articles/types/article.md")
def validate_article(
    results: CheckResults, parsed: ParsedNote, *, run: ValidationRun
) -> None:
    """Enforce the article type's lineage contract: every source_notes path
    resolves to a file under the repo root. Field shape is the schema's job."""
    fm = parsed.document.frontmatter or {}
    source_notes = fm.get("source_notes")
    if not isinstance(source_notes, list) or not source_notes:
        return

    missing = [
        entry
        for entry in source_notes
        if not isinstance(entry, str) or not (run.repo_root / entry).is_file()
    ]
    if missing:
        results.fails.append(
            f"source_notes: {len(missing)} of {len(source_notes)} paths do not "
            f"resolve from the repo root: {', '.join(map(str, missing))}"
        )
    else:
        results.passes.append(
            f"source_notes: all {len(source_notes)} paths resolve"
        )


@type_rule(
    "types/note.md",
    "notes/types/structured-claim.md",
    "articles/types/article.md",
)
def validate_unquoted_sources(
    results: CheckResults, parsed: ParsedNote, *, run: ValidationRun
) -> None:
    """Bound the tracked sources a note cites without a verified verbatim quote.

    Each unquoted tracked source is a full read a grounding reviewer has to
    perform; past the bound the review no longer fits one pass. A source marked
    `(snapshot required)` counts even when a quote resolves, because the claim
    it carries needs the snapshot rather than the retained extract.
    """
    repo_root = run.repo_root.resolve()
    targets: dict[Path, bool] = {}
    for text, link in find_markdown_links_with_text(parsed.document.body):
        target = _resolve_local_link_target(parsed.path, link)
        if target is None or not target.name.endswith(".ingest.md"):
            continue
        try:
            relative = target.relative_to(repo_root)
        except ValueError:
            continue
        if not relative.as_posix().startswith("kb/sources/"):
            continue
        targets[target] = targets.get(target, False) or (
            SNAPSHOT_REQUIRED_MARKER in text
        )

    # Most notes cite no tracked source; a pass line there would be noise.
    if not targets:
        return

    quoted = {
        result.source
        for result in run.verbatim_quotes(parsed)
        if result.status == "match"
    }
    unquoted = sorted(
        (
            target
            for target, snapshot_required in targets.items()
            if snapshot_required or target not in quoted
        ),
        key=lambda target: target.name,
    )

    if len(unquoted) > MAX_UNQUOTED_SOURCES:
        names = ", ".join(target.name for target in unquoted)
        results.fails.append(
            f"unquoted sources: {len(unquoted)} distinct tracked sources cited "
            f"without a verified verbatim quote (limit {MAX_UNQUOTED_SOURCES}); "
            f"{_UNQUOTED_SOURCES_FIX_HINT}: {names}"
        )
    else:
        results.passes.append(
            f"unquoted sources: {len(unquoted)} of {len(targets)} tracked sources "
            f"need a full read (limit {MAX_UNQUOTED_SOURCES})"
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
    for capture in report.captures:
        _text, actual_sha256, error = verify_capture(
            capture, packet_dir=report.packet_dir
        )
        if error is not None:
            capture_failures += 1
            results.fails.append(
                f"{capture.role} capture: {error}"
                + (f" ({actual_sha256})" if actual_sha256 is not None else "")
            )
    if not capture_failures:
        results.passes.append(
            f"packet captures: all {len(report.captures)} present and hash-verified"
        )

    expected_resolution = render_resolution_section(report.frontmatter)
    actual_resolution = resolution_section(report.body)
    if actual_resolution != expected_resolution:
        results.fails.append(
            "resolution projection: body section does not match canonical frontmatter rendering"
        )
    else:
        results.passes.append("resolution projection: body matches frontmatter")


@type_rule(AGENTIC_ANALYSIS_RUN_TYPE)
def validate_agentic_analysis_run_state(
    results: CheckResults, parsed: ParsedNote, *, run: ValidationRun
) -> None:
    """Verify the source and output identities of one analysis run."""
    try:
        state = parse_agentic_analysis_run_state(
            parsed.path, parsed.document, repo_root=run.repo_root
        )
    except ValueError as exc:
        results.fails.append(f"agentic-system analysis run state: {exc}")
        return

    passes, failures = verify_agentic_analysis_run_state(
        state,
        content_overrides=run.content_overrides,
    )
    results.passes.extend(passes)
    results.fails.extend(failures)
    if not failures:
        results.passes.append(
            f"run state: {state.status} source and output identities verified"
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


def _merge_labelled(dest: CheckResults, src: CheckResults, source: str) -> None:
    """Fold one check group's findings into the result, tagged with its source."""
    for level in ("passes", "warns", "fails", "infos"):
        getattr(dest, level).extend(
            f"[{source}] {message}" for message in getattr(src, level)
        )


def validate_tag_heads(
    results: CheckResults, parsed: ParsedNote, *, run: ValidationRun
) -> None:
    """Every tag in use within the tag space has a head (ADR 089).

    Applies to artifacts in participating collections that carry a `tags:`
    list. Tags outside the tag space are not read, so nothing is reported for
    them. A missing or malformed tag-space declaration is a warning, because
    the artifact cannot fix it.
    """
    fm = parsed.document.frontmatter or {}
    tags = fm.get("tags")
    if not isinstance(tags, list) or not tags:
        return
    tag_space = run.tag_space()
    if tag_space.declaration_error and not tag_space.participating:
        results.warns.append(f"tags unchecked: {tag_space.declaration_error}")
        return
    if not tag_space.is_participating(parsed.path):
        return
    headless = [
        tag for tag in tags if isinstance(tag, str) and tag not in tag_space.heads
    ]
    for tag in headless:
        results.fails.append(
            f"tag `{tag}`: no head at "
            f"{head_path(run.repo_root, tag).relative_to(run.repo_root)} — "
            "write one or drop the tag (ADR 089)"
        )
    if not headless:
        results.passes.append(f"tags: all {len(tags)} have heads in kb/tags/")


def _file_available(path: Path, run: ValidationRun) -> bool:
    return path.resolve() in run.content_overrides or path.is_file()


def validate_write_brief_pairing(
    results: CheckResults, parsed: ParsedNote, *, run: ValidationRun
) -> None:
    """Enforce the write-brief sidecar pairing in both directions (ADR 092).

    A document's `brief:` must be exactly its own `<stem>.brief.md` and name an
    existing sibling of the write-brief type. A `.brief.md` file must be of that
    type and be declared by its sibling `<stem>.md`. The suffix and the type
    must agree. Forbidden fields inside a brief are the brief schema's job.
    """
    frontmatter_data = parsed.document.frontmatter
    is_typed = frontmatter_data is not None
    type_identity = canonical_type_identity(parsed.profile) if is_typed else None
    name = parsed.path.name

    if is_write_brief_path(parsed.path):
        if type_identity != WRITE_BRIEF_TYPE:
            results.fails.append(
                f"write brief: {name} has the .brief.md suffix but is not of type "
                f"{WRITE_BRIEF_TYPE}; rename it or fix its type"
            )
            return
        target = write_brief_target_for(parsed.path)
        if not _file_available(target, run):
            results.fails.append(
                f"write brief: {name} has no sibling document {target.name}"
            )
            return
        loaded = run.load_document(target)
        declared = (
            (loaded.document.frontmatter or {}).get("brief")
            if loaded.document is not None
            else None
        )
        if declared != name:
            results.fails.append(
                f"write brief: sibling {target.name} does not declare "
                f"`brief: {name}`"
            )
            return
        results.passes.append(f"write brief: declared by sibling {target.name}")
        return

    if type_identity == WRITE_BRIEF_TYPE:
        results.fails.append(
            f"write brief: {name} is of type {WRITE_BRIEF_TYPE} but its name "
            f"lacks the .brief.md suffix; name it <target-stem>.brief.md"
        )
        return

    if not is_typed or "brief" not in frontmatter_data:
        return
    value = frontmatter_data["brief"]
    expected = write_brief_name_for(parsed.path)
    if value != expected:
        results.fails.append(
            f"brief: value {value!r} must be the document's own sibling "
            f"filename {expected!r}"
        )
        return
    brief_path = parsed.path.parent / expected
    if not _file_available(brief_path, run):
        results.fails.append(f"brief: {expected} does not exist")
        return
    brief_parsed, error = run.parse_note(brief_path)
    if error or brief_parsed is None:
        results.fails.append(f"brief: {expected} cannot be resolved: {error}")
        return
    if (
        brief_parsed.document.frontmatter is None
        or canonical_type_identity(brief_parsed.profile) != WRITE_BRIEF_TYPE
    ):
        results.fails.append(
            f"brief: {expected} is not of type {WRITE_BRIEF_TYPE}"
        )
        return
    results.passes.append(f"brief: {expected} resolves to a write brief")


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
        results = CheckResults(
            note_type="text",
            passes=["[base] text file: no frontmatter, no structural requirements"],
        )
        base = CheckResults(note_type="text")
        validate_proposal_archive_links(
            base,
            parsed.path,
            parsed.document.links,
            repo_root=run.repo_root,
        )
        validate_write_brief_pairing(base, parsed, run=run)
        _merge_labelled(results, base, "base")
        return results

    results = CheckResults(note_type=parsed.note_type)

    base = CheckResults(note_type=parsed.note_type)
    base.passes.append("frontmatter: valid delimiters, well-formed YAML")
    validate_title_and_slug(
        base,
        parsed.path,
        parsed.document,
        note_type=parsed.note_type,
        git_ignored=run.is_git_ignored(parsed.path),
    )
    validate_links_from_document(
        base,
        parsed.path,
        parsed.document.links,
        available_paths=run.content_overrides,
    )
    validate_proposal_archive_links(
        base,
        parsed.path,
        parsed.document.links,
        repo_root=run.repo_root,
    )
    validate_tag_heads(base, parsed, run=run)
    validate_write_brief_pairing(base, parsed, run=run)
    validate_verbatim_quotes(base, run.verbatim_quotes(parsed))
    snapshots = run.snapshots(parsed.path.parent / ".snapshots")
    validate_ingest_snapshot_pairing(
        base, parsed.content, parsed.path, snapshots=snapshots
    )
    validate_ingest_quotes(base, parsed.content, parsed.path, snapshots=snapshots)
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


def validate_note_text_at_path(
    content: str,
    *,
    path: Path,
    repo_root: Path,
    content_overrides: dict[Path, str] | None = None,
) -> CheckResults:
    """Validate supplied bytes as though they occupied their intended path."""
    overrides = dict(content_overrides or {})
    overrides[path] = content
    return ValidationRun(
        repo_root=repo_root,
        paths=(path,),
        content_overrides=overrides,
    ).validate(path)


def validate_collection_structure(
    collection: Path, *, repo_root: Path
) -> list[tuple[Path, str]]:
    """Return anchored structural failures for one collection boundary."""
    collection = collection.resolve()
    repo_root = repo_root.resolve()
    if not is_collection_dir(collection):
        return []

    failures: list[tuple[Path, str]] = []
    for path in iter_validation_markdown_files(collection):
        if path.name != "COLLECTION.md" or path.parent == collection:
            continue
        if is_type_definition_content(path, collection):
            continue
        failures.append(
            (
                path,
                (
                    "nested COLLECTION.md: "
                    f"{path.relative_to(repo_root)} is inside collection "
                    f"{collection.relative_to(repo_root)}"
                ),
            )
        )
    return failures


def validate_source_snapshot_cache(
    collection: Path,
    *,
    repo_root: Path,
    snapshots: SnapshotDirectory | None = None,
) -> list[tuple[Path, str]]:
    """Warn about retained cache files that no ingest-pair check can own.

    A checksum-matching snapshot at the wrong path is reported on the ingest by
    ``validate_ingest_snapshot_pairing``. This collection check uses source URL
    independently of checksum so a changed observation is not mislabeled as
    unrelated. It also reports redundant alternate copies whose
    checksum owner already has a valid name-paired snapshot.
    """
    collection = collection.resolve()
    repo_root = repo_root.resolve()
    if collection != (kb_root(repo_root) / "sources").resolve():
        return []

    snapshot_dir = collection / ".snapshots"
    if not snapshot_dir.is_dir():
        return []
    if snapshots is None:
        snapshots = SnapshotDirectory(snapshot_dir)

    checksum_owners: dict[str, list[Path]] = {}
    original_checksums: set[str] = set()
    source_owners: dict[str, list[Path]] = {}
    valid_pairs: set[Path] = set()
    for ingest in sorted(collection.glob("*.ingest.md")):
        try:
            content = ingest.read_text(encoding="utf-8")
        except OSError:
            continue
        source = _http_source_from_content(content)
        if source is not None:
            source_owners.setdefault(source, []).append(ingest)
        original = ORIGINAL_SNAPSHOT_SHA256_RE.search(content)
        if original is not None:
            original_checksums.add(original.group("checksum"))
        recorded = SNAPSHOT_SHA256_RE.search(content)
        if recorded is None:
            continue
        checksum = recorded.group("checksum")
        checksum_owners.setdefault(checksum, []).append(ingest)
        expected = _name_paired_snapshot(ingest)
        if expected.is_file() and snapshots.read(expected).sha256 == checksum:
            valid_pairs.add(ingest)

    def names(owners: list[Path]) -> str:
        return ", ".join(str(owner.relative_to(repo_root)) for owner in owners)

    warnings: list[tuple[Path, str]] = []
    for snapshot, facts in sorted(snapshots.all().items()):
        # Its ingest-level pairing check owns missing, unreadable, and
        # checksum-mismatch diagnostics at the expected path.
        if (collection / f"{snapshot.stem}.ingest.md").is_file():
            continue
        if facts.error is not None:
            warnings.append(
                (snapshot, f"unpaired local snapshot: unreadable ({facts.error})")
            )
            continue

        # A derived observation such as a translation can own both its primary
        # snapshot and the exact precursor bytes from which it was produced.
        # The precursor has no name-paired ingest of its own, but it is not an
        # unaccounted cache file once the derivation records its checksum.
        if facts.sha256 in original_checksums:
            continue

        owners = checksum_owners.get(facts.sha256 or "", [])
        if any(owner not in valid_pairs for owner in owners):
            # Each owner locates this exact file in its artifact-level warning;
            # do not report the same path drift twice in a collection sweep.
            continue

        url_owners = source_owners.get(facts.source or "", [])
        if owners:
            warning = (
                "no same-stem ingest; its checksum duplicates the valid "
                f"name-paired snapshot for {names(owners)}"
            )
        elif url_owners:
            warning = (
                f"no same-stem ingest; its source URL matches {names(url_owners)}, "
                "but no matching ingest records these exact bytes"
            )
        else:
            warning = (
                "no same-stem ingest and no ingest matches its source URL or checksum"
            )
        warnings.append((snapshot, f"unpaired local snapshot: {warning}"))

    return warnings


def validate_collection_landings(*, repo_root: Path) -> CheckResults:
    """Validate curated landings for collections directly under ``kb/``."""
    repo_root = repo_root.resolve()
    docs_root = kb_root(repo_root).resolve()
    results = CheckResults(note_type="collection-landings")

    if not docs_root.is_dir():
        results.fails.append("[repository] collection landings: kb/ does not exist")
        return results

    collections = sorted(
        child
        for child in docs_root.iterdir()
        if not child.name.startswith(".") and is_collection_dir(child)
    )
    if not collections:
        results.fails.append(
            "[repository] collection landings: no top-level collections found"
        )
        return results

    missing = [
        collection / "README.md"
        for collection in collections
        if not (collection / "README.md").is_file()
    ]
    if missing:
        results.fails.extend(
            "[repository] collection landing does not exist: "
            f"{path.relative_to(repo_root)}"
            for path in missing
        )
    else:
        results.passes.append(
            "[repository] collection landings: "
            f"all {len(collections)} top-level collections have README.md"
        )

    collisions = [
        collection
        for collection in collections
        if (collection / "README.md").is_file()
        and (collection / "index.md").is_file()
    ]
    if collisions:
        results.fails.extend(
            "[repository] collection landing collision: "
            f"{collection.relative_to(repo_root)} contains both README.md and index.md"
            for collection in collisions
        )
    else:
        results.passes.append("[repository] collection landing collisions: none")

    return results


def validate_redirect_map(*, repo_root: Path) -> CheckResults:
    """Validate the live ProperDocs redirect map when the site is configured."""
    repo_root = repo_root.resolve()
    config_path = repo_root / "properdocs.yml"
    results = CheckResults(note_type="redirect-map")

    if not config_path.is_file():
        results.infos.append(
            "[repository] properdocs.yml: not configured; redirect validation skipped"
        )
        return results

    try:
        config = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        results.fails.append(f"[repository] properdocs.yml: cannot load config: {exc}")
        return results

    if not isinstance(config, dict):
        results.fails.append("[repository] properdocs.yml: root must be a mapping")
        return results

    docs_dir_value = config.get("docs_dir")
    if not isinstance(docs_dir_value, str) or not docs_dir_value.strip():
        results.fails.append("[repository] docs_dir: expected a non-empty path")
        return results
    docs_dir = (repo_root / docs_dir_value).resolve()

    plugins = config.get("plugins")
    if not isinstance(plugins, list):
        results.fails.append("[repository] plugins: expected a list")
        return results
    redirect_plugins = [
        plugin["redirects"]
        for plugin in plugins
        if isinstance(plugin, dict) and "redirects" in plugin
    ]
    if len(redirect_plugins) != 1:
        results.fails.append(
            "[repository] redirects plugin: expected exactly one configured entry"
        )
        return results

    redirect_plugin = redirect_plugins[0]
    if not isinstance(redirect_plugin, dict):
        results.fails.append("[repository] redirects plugin: expected a mapping")
        return results
    redirect_maps = redirect_plugin.get("redirect_maps")
    if not isinstance(redirect_maps, dict):
        results.fails.append("[repository] redirect_maps: expected a mapping")
        return results
    if not all(isinstance(old, str) and isinstance(new, str) for old, new in redirect_maps.items()):
        results.fails.append("[repository] redirect_maps: keys and targets must be paths")
        return results

    broken = sorted(
        f"{old} -> {new}"
        for old, new in redirect_maps.items()
        if not (docs_dir / new).is_file()
    )
    if broken:
        results.fails.extend(
            f"[repository] redirect target does not exist: {redirect}" for redirect in broken
        )
    else:
        results.passes.append(
            f"[repository] redirect targets: all {len(redirect_maps)} resolve"
        )

    shadowed = sorted(old for old in redirect_maps if (docs_dir / old).exists())
    if shadowed:
        results.fails.extend(
            f"[repository] redirect key shadows a live page: {old}" for old in shadowed
        )
    else:
        results.passes.append("[repository] redirect keys: none shadow live pages")

    chained = sorted(
        f"{old} -> {new}" for old, new in redirect_maps.items() if new in redirect_maps
    )
    if chained:
        results.fails.extend(
            f"[repository] redirect chain is not flat: {redirect}" for redirect in chained
        )
    else:
        results.passes.append("[repository] redirect topology: flat")

    return results


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
