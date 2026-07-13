---
description: Internal API reference for commonplace.lib parsing, indexing, type resolution, validation, and relocation modules used by CLI commands and review
type: kb/types/note.md
tags: []
---

# Commonplace library (`commonplace.lib`)

Shared library modules used by CLI commands and the review system. `frontmatter` and `type_resolver` require `PyYAML`; `type_resolver` also requires `jsonschema` (which transitively brings in `referencing`).

## Module overview

```
frontmatter.py    Parse/validate markdown frontmatter (strict YAML subset)
naming.py         Shared note title and filename-slug constraints
note_parser.py    Parse markdown notes into a schema-friendly document model
index_generated.py Build generated tag sections and shared collection tag indexes
type_resolver.py  Resolve note types from scoped JSON Schema definitions
validation.py     Deterministic validation rules for KB notes (commonplace-validate lib)
relocation.py     Move/rename a KB note or directory: rewrite backlinks and mkdocs config
```

Dependencies:
- `note_parser` → `frontmatter`
- `index_generated` → `note_parser`, `project_paths`
- `validation` → `index_generated`, `note_parser`, `type_resolver`, `naming`
- `relocation` → `naming`, `project_paths`
- `type_resolver` is otherwise independent (but requires external packages)

---

## naming

Shared naming rules and slug helpers.

### Public API

**Constants**
- `MAX_NOTE_TITLE_LENGTH = 100`
- `MAX_NOTE_SLUG_LENGTH = 70`

**`slugify_text(text: str, *, max_len: int | None = None, default: str | None = None) -> str`**
Convert free text into a lowercase hyphenated slug, optionally truncate it, and optionally fall back to a default when the input contains no slug-worthy characters.

**`ensure_note_slug_length(slug: str) -> None`**
Raise `ValueError` when a note filename slug exceeds the hard length limit.

**`slugify_note_filename(text: str) -> str`**
Convert a title or filename-like string into a lowercase hyphenated note slug and enforce the hard slug limit.

---

## frontmatter

Parse markdown frontmatter by extracting the block between `---` delimiters and handing it to `yaml.safe_load`.

### Public API

**`FrontmatterResult`** — dataclass holding parse results:
- `data: dict[str, Any]` — parsed key-value pairs
- `errors: list[str]` — parse/validation error messages
- `ok: bool` — property, `True` if no errors

**`parse(content: str) -> FrontmatterResult`**
Full parse: extracts the raw frontmatter block, parses it with `yaml.safe_load`, and returns a mapping or parse errors.

**`strip(content: str) -> str`**
Remove the frontmatter block from content, returning the body.

---

## note_parser

Parse markdown notes into a structured `ParsedDocument` for validation and indexing.

### Public API

**`ParsedDocument`** — frozen dataclass:
- `frontmatter: dict[str, Any] | None` — parsed frontmatter or `None` for plain text
- `body: str` — markdown body after frontmatter
- `headings: tuple[str, ...]` — all headings with hash prefixes (`"## Foo"`)
- `links: tuple[str, ...]` — all markdown link URLs
- `body_dates: tuple[str, ...]` — ISO dates (YYYY-MM-DD) found in body
- `title: str` — first H1 heading, or `"Untitled"`
- `to_validation_object() -> dict` — returns `{frontmatter, body, headings, links, body_dates}` for JSON Schema validation

**`parse_document(content: str) -> tuple[ParsedDocument | None, str | None]`**
Main entry point. Returns `(doc, error)` — if frontmatter parsing fails, `doc` is `None` and `error` describes the problem.

**`extract_title(body: str) -> str`**
First H1 heading text, or `"Untitled"`.

**`extract_headings(body: str) -> tuple[str, ...]`**
All markdown headings, ignoring those inside fenced code blocks.

**`find_markdown_links(body: str) -> tuple[str, ...]`**
All `[text](url)` link URLs, ignoring links inside code regions.

**`find_markdown_links_with_text(body: str) -> tuple[tuple[str, str], ...]`**
All `[text](url)` links as `(text, url)` pairs, ignoring links inside code regions. Used by review prompt preparation when rendering link tables in prompts.

**`extract_body_dates(body: str) -> tuple[str, ...]`**
Deduplicated ISO dates found in body text.

**`remove_fenced_code_blocks(text: str) -> str`** / **`remove_code_regions(text: str) -> str`**
Strip fenced code blocks, or both fenced and inline code. Used internally before heading extraction and other text scans to avoid false matches.

**`strip_frontmatter(content: str) -> str`**
Delegates to `frontmatter.strip()`.

---

## type_resolver

Resolve structural note types from path-valued type-spec documents and their declared JSON Schemas.

### Schema discovery

Type resolution now starts from the path stored in frontmatter. There is no collection-scoped enum lookup.

### Type resolution logic

1. If the file has no frontmatter, treat it as implicit `text` and skip schema validation.
2. If the file has frontmatter, require `type:` to be a markdown path under `kb/`, either repository-relative (`kb/...`) or file-relative (`./...` or `../...`).
3. Open the referenced type-spec doc and verify it declares `type: kb/types/type-spec.md`.
4. Read the type spec's `name`, `description`, and `schema` fields.
5. If `schema` is a path, resolve it the same way from the type-spec doc, load that JSON Schema YAML file, and validate the parsed document against it. If `schema: null`, skip schema validation.

Bare enum values, missing type files, missing `schema` fields in type specs, absolute paths, URLs, and paths outside `kb/` are validation errors.

### Public API

**`TypeProfile`** — frozen dataclass describing a resolved type:
- `type_path: str` — canonical repo-relative path for the resolved type, or `text` for implicit no-frontmatter files
- `type_doc_path: Path | None` — resolved filesystem path to the type-spec doc
- `type_name: str` — `name` from type-spec frontmatter
- `schema_path: Path | None` — resolved schema path, or `None` when `schema: null`
- `schema: dict | None` — parsed JSON Schema mapping, or `None`


**`resolve_type(file_path: Path, frontmatter: dict | None, *, repo_root: Path, load_type_frontmatter=None) -> TypeProfile`**
Note-oriented entry point. Validates the path-valued `type:` and delegates the referenced type document to `resolve_type_definition`. A validation run supplies its cached frontmatter loader; standalone callers omit it and the resolver reads the type document directly.

**`resolve_type_definition(type_doc_path: Path, *, repo_root: Path, type_frontmatter: dict | None = None) -> TypeProfile`**
Load an identified type-spec document and its declared schema directly. Callers that already parsed the document may supply its frontmatter to avoid reopening it; ordinary note resolution omits the mapping and loads the type document itself.

**`canonical_type_identity(profile: TypeProfile) -> str`**
Return the portable path identity used by schemas and imperative type-rule dispatch. Installed framework paths under `kb/commonplace/` normalize to their source `kb/` identity; collection-local paths remain distinct.

**`validate_instance(profile: TypeProfile, instance: dict) -> list[ValidationError]`**
Validate a document instance (from `ParsedDocument.to_validation_object()`) against the type's JSON Schema. Returns errors sorted by document path. Returns an empty list for implicit `text` and for type specs with `schema: null`.

### Caching

Schema loading (`_load_schema`) and validator construction (`_validator_for_path`) use `@lru_cache`. Schemas are loaded on demand, not at startup.

---

## index_generated

Build generated tag-index sections and provide the collection tag inventory shared with validation.

### Public API

**`CollectionTagIndex`** — frozen dataclass containing `notes_by_tag` and `tag_index_entries` from one collection scan.

**`collect_collection_tag_index(collection_dir, *, load_document=None) -> CollectionTagIndex`**
Scan visible collection artifacts once. The optional loader lets a validation run supply cached `ParsedDocument` values; without one, the collector reads and parses the artifacts itself.

**`collect_notes_by_tag(collection_dir)`** / **`collect_tag_index_entries(collection_dir, root)`**
Convenience projections of the shared collection index used by generated-page consumers.

---

## validation

Deterministic validation execution and rules for KB notes. Used by `commonplace-validate`. A library-owned run caches parsed artifacts and collection indexes, expands explicit impacts, evaluates per-artifact checks, and returns anchored results; the CLI resolves targets and presents them.

### Public API

**`CheckResults`** — mutable dataclass holding pass/warn/fail/info string lists for one note.

**`ParsedNote`** — dataclass bundling a note's `path`, `content`, `note_type`, `profile` (`TypeProfile`), and `document` (`ParsedDocument`).

**`ValidationRun`** — one target's execution context. Caches loaded `ParsedDocument` and resolved `ParsedNote` values by path, lazily caches `CollectionTagIndex` values, runs explicit marked-tag-README impact selection, builds collection inbound-link information once, and evaluates the unchanged base → imperative type rules → schema pipeline.

**`ValidationRunResults`** — expanded path tuple, per-path `CheckResults` mapping, and collection-structure findings as `(anchor_path, message)` tuples.

**`run_validation(paths, *, repo_root, collection=None) -> ValidationRunResults`**
Primary batch entry point. The optional collection is explicit target semantics: it enables authored-link orphan information and collection-structure checks. Direct files, `recent`, and `types` remain non-collection runs.

**`list_collection_note_paths(collection: Path) -> list[Path]`**
Return visible Markdown artifacts under one collection, including everything under `types/`. Skips collection metadata, replaced archives, hidden entries, and nested git repositories. Filename suffixes such as `*.template.md` and `*.instructions.md` have no special meaning. Visibility is package-owned (`project_paths.walk_visible`); gitignore rules have no effect on what the tools see.

**`list_type_spec_paths(root: Path) -> list[Path]`**
Return Markdown artifacts under `kb/**/types/*.md`, excluding only `text.md`, the implicit no-frontmatter root rather than a type-spec artifact. Used by the `commonplace-validate types` target.

**`is_type_definition_content(path: Path, boundary: Path) -> bool`**
Return whether a path is inside a `types/` directory beneath the supplied boundary. Consumers such as generated indexes use it when their domain excludes contracts; validation does not categorically exclude type definitions.

**`parse_note(path: Path, *, repo_root: Path) -> tuple[ParsedNote | None, str | None]`**
One-path convenience wrapper around the run parser. Returns `(parsed, None)` on success or `(None, error_message)` on parse/type-resolution failure.

**`validate_note(path: Path, *, repo_root: Path) -> CheckResults`**
One-path convenience wrapper around `ValidationRun.validate`.

**`type_rule(*type_paths)`**
Decorator registering a type-specific rule `(results, parsed, *, run) -> None` for canonical type paths. The run supplies repository identity and shared referential inputs; matching rules still execute between generic checks and schema validation. Current registrations: quote-citation shape checks for `kb/agent-memory-systems/types/agent-memory-system-review.md`, declared-schema resolution for `kb/types/type-spec.md`, and weight/completeness/coverage gates for `kb/types/tag-readme.md`.

**`validate_title_and_slug(results, path, document)`**
Filesystem naming check: title length and slug length against `MAX_NOTE_TITLE_LENGTH` / `MAX_NOTE_SLUG_LENGTH`.

**`validate_links_from_document(results, path, links)`**
Filesystem link health: verify each local relative link target actually exists.

**`apply_schema_validation(results, parsed)`**
Run the parsed document through `validate_instance(...)` and translate each `jsonschema` error via `_schema_error_message` (severity from a 2-element fail-path set, with `contains` extraction for missing headings and an optional `description`/`title` hint from the schema).

**`validate_collection_structure(collection, *, repo_root) -> list[tuple[Path, str]]`**
Return nested-collection failures anchored on the offending `COLLECTION.md`. `ValidationRun.evaluate` includes these in its result; the CLI retains their batch presentation.

---

## relocation

Move or rename a KB note: rewrite inbound and outbound links across the repo and update `mkdocs.yml` redirects. Review state is path-keyed and is not relocated. Used by `commonplace-relocate-note`.

### Public API

**`relocate_note(*, root: Path, note_arg: str, new_name: str | None = None, dest_path: str | None = None, apply: bool = False) -> int`**
Top-level orchestrator. Resolves the source note from a path or unique stem, computes the destination, walks all repo markdown files to plan link rewrites, and either prints a dry-run plan or executes everything (file move, link rewrites, mkdocs update). The mkdocs step is skipped when the project has no `mkdocs.yml`. Returns a process exit code.

**`resolve_note(arg, *, root)`**
Find a note by absolute path, repo-relative path, full filename, or unique stem. Searches the entire `kb/` tree, not just `kb/notes/`, so notes can be relocated between collections.

**`resolve_destination_path(source, new_name, dest_path, *, repo_root, kb_root)`**
Compute the destination path from either a `--to` argument (file or directory) or a positional new title. Enforces the slug length limit.

**`rewrite_links_to_moved_files(content, source_file, moves) -> tuple[str, list[str]]`**
For each markdown link in `content` whose target resolves to a key of `moves` (a `{old_resolved_path: new_path}` dict), rewrite it to point at the new location. Skips links inside fenced or inline code regions. Returns the updated text and a list of human-readable change descriptions. Single-note relocation is the one-entry-dict case.

**`rebase_and_rewrite_in_moved_file(content, old_source_file, new_source_file, moves) -> tuple[str, list[str]]`**
For a file that is itself being moved: rewrite each of its outbound relative links so they still resolve from the new location, mapping targets that are also in `moves` to their new locations.

**`update_mkdocs_config(content, old_docs_path, new_docs_path) -> tuple[str, list[str]]`**
Update `mkdocs.yml` in place: rewrite any matching `nav` entries and `redirect_maps` targets, and append a new redirect entry from `old_docs_path` to `new_docs_path`. Preserves indentation and quoting style. A config without a `redirect_maps:` section still gets its values rewritten; the redirect entry is skipped.

**`move_path(source, destination)`**
Move a path on disk with `Path.rename`, creating the destination's parent directories first. Git is not involved; it detects the rename on commit.

The smaller helpers (`format_relative_link`, `split_link_target`, `is_relative_markdown_target`, `resolve_directory`, `add_single_redirect`) are exported but rarely interesting outside the orchestrator.
