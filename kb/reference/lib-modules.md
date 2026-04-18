---
description: Internal API reference for commonplace.lib - frontmatter, naming, note_parser, type_resolver, validation, and relocation modules used by CLI commands and the review system
type: note
tags: []
status: current
---

# Commonplace library (`commonplace.lib`)

Shared library modules used by CLI commands and the review system. `frontmatter` and `type_resolver` require `PyYAML`; `type_resolver` also requires `jsonschema` (which transitively brings in `referencing`).

## Module overview

```
frontmatter.py    Parse/validate markdown frontmatter (strict YAML subset)
naming.py         Shared note title and filename-slug constraints
note_parser.py    Parse markdown notes into a schema-friendly document model
type_resolver.py  Resolve note types from scoped JSON Schema definitions
validation.py     Deterministic validation rules for KB notes (commonplace-validate lib)
relocation.py     Move/rename a KB note: rewrite backlinks, mkdocs config, review exports, DB rekey
```

Dependencies:
- `note_parser` → `frontmatter`
- `validation` → `note_parser`, `type_resolver`, `naming`
- `relocation` → `naming`, `commonplace.review.review_db`, `commonplace.review.review_metadata`
- `type_resolver` is otherwise independent (but requires external packages)

---

## naming

Shared naming rules and slug helpers.

### Public API

**Constants**
- `MAX_NOTE_TITLE_LENGTH = 100`
- `MAX_NOTE_SLUG_LENGTH = 100`

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
All `[text](url)` links as `(text, url)` pairs, ignoring links inside code regions. Used by `commonplace.review.run_review_bundle` when it needs to render link tables in prompts.

**`extract_body_dates(body: str) -> tuple[str, ...]`**
Deduplicated ISO dates found in body text.

**`remove_fenced_code_blocks(text: str) -> str`** / **`remove_code_regions(text: str) -> str`**
Strip fenced code blocks, or both fenced and inline code. Used internally before heading extraction and other text scans to avoid false matches.

**`strip_frontmatter(content: str) -> str`**
Delegates to `frontmatter.strip()`.

---

## type_resolver

Resolve structural note types from scoped JSON Schema definitions. Uses collection-scoped schema discovery — schemas are searched from the owning collection first, then the global KB type layer.

### Schema discovery

Schemas live in the global `kb/types/` directory and in optional collection-local `types/` directories. For a workshop artifact at `kb/work/my-project/foo.md`, the search order is:

1. `kb/work/types/{type}.schema.yaml`
2. `kb/types/{type}.schema.yaml`

For an instruction at `kb/instructions/foo.md`:

1. `kb/instructions/types/{type}.schema.yaml`
2. `kb/types/{type}.schema.yaml`

In the shipped scaffold, plain instructions and review gates use the global `instruction` type at `kb/types/instruction.schema.yaml`.

For a report at `kb/reports/connect/foo.connect.md`:

1. `kb/reports/types/{type}.schema.yaml`
2. `kb/types/{type}.schema.yaml`

For a source ingest report at `kb/sources/foo.ingest.md`:

1. `kb/sources/types/{type}.schema.yaml`
2. `kb/types/{type}.schema.yaml`

For a note at `kb/notes/bar.md`:

1. `kb/notes/types/{type}.schema.yaml`
2. `kb/types/{type}.schema.yaml`

### Type resolution logic

1. If the note has frontmatter with a `type` field → use that type name
2. If the note has frontmatter but no `type` → default to `"note"`
3. If the note has no frontmatter → `"text"` (no schema, no validation)
4. If the type's schema file isn't found → fall back to `"note"` (except `"note"` itself, which raises `FileNotFoundError`)

### Public API

**`TypeProfile`** — frozen dataclass describing a resolved type:
- `resolved_type: str` — type name
- `definition_path: Path | None` — path to the `.schema.yaml` file (or `None` for `"text"`)
- `schema: dict | None` — parsed JSON Schema (or `None` for `"text"`)

The schema itself is the single source of truth for required headings, status enums, required fields, etc. There is no separate metadata extraction layer; all such checks happen by running the schema against `ParsedDocument.to_validation_object()`.

**`resolve_type(file_path: Path, frontmatter: dict | None, *, repo_root: Path | None = None) -> TypeProfile`**
Main entry point. Determines the type name, locates the schema by walking the scope hierarchy, and loads it. Handles `$ref` resolution and `allOf` composition through `jsonschema`'s registry.

**`validate_instance(profile: TypeProfile, instance: dict) -> list[ValidationError]`**
Validate a document instance (from `ParsedDocument.to_validation_object()`) against the type's JSON Schema. Returns errors sorted by document path. Returns empty list for types without schemas (e.g., `"text"`).

### Caching

Schema loading (`_load_schema`) and validator construction (`_validator_for_path`) use `@lru_cache`. Schemas are loaded on demand, not at startup.

---

## validation

Deterministic validation rules for KB notes. Used by `commonplace-validate`. The schema (loaded via `type_resolver`) is the single source of truth for content rules; this module only adds checks the schema cannot express (filesystem-level constraints) plus a thin translator that turns raw `jsonschema` errors into user-facing messages.

### Public API

**`CheckResults`** — mutable dataclass holding pass/warn/fail/info string lists for one note. Constructed once per validation run.

**`ParsedNote`** — dataclass bundling a note's `path`, `content`, `note_type`, `profile` (`TypeProfile`), and `document` (`ParsedDocument`).

**`list_kb_note_paths(notes_root: Path) -> list[Path]`**
Return all `.md` files under `notes_root`, skipping nested git repositories and `types/` template directories.

**`is_nested_git_repo_content(path: Path, notes_root: Path) -> bool`** / **`is_type_definition_content(path: Path, notes_root: Path) -> bool`**
Predicates used by `list_kb_note_paths` for the two skip rules.

**`parse_note(path: Path, *, repo_root: Path) -> tuple[ParsedNote | None, str | None]`**
Read a note, parse its frontmatter and body, resolve its type. Returns `(parsed, None)` on success or `(None, error_message)` on parse failure.

**`validate_note(path: Path, *, repo_root: Path) -> CheckResults`**
Run the full deterministic validation pipeline on one note: title/slug length, link health, then schema validation. Returns the populated `CheckResults`.

**`validate_title_and_slug(results, path, document)`**
Filesystem naming check: title length and slug length against `MAX_NOTE_TITLE_LENGTH` / `MAX_NOTE_SLUG_LENGTH`.

**`validate_links_from_document(results, path, links)`**
Filesystem link health: verify each local relative link target actually exists.

**`apply_schema_validation(results, parsed)`**
Run the parsed document through `validate_instance(...)` and translate each `jsonschema` error via `_schema_error_message` (severity from a 2-element fail-path set, with `contains` extraction for missing headings and an optional `description`/`title` hint from the schema).

**`orphan_info(all_paths: list[Path]) -> dict[Path, bool]`**
Batch cross-note analysis: for each note in the list, return `True` if any other note in the list contains a relative `.md` link resolving to it. Used by the CLI to flag orphaned notes after a full sweep.

---

## relocation

Move or rename a KB note: rewrite inbound and outbound links across the repo, update `mkdocs.yml` redirects, move the review export directory, rewrite review-metadata blocks, and rekey the review SQLite database. Used by `commonplace-relocate-note`.

### Public API

**`relocate_note(*, repo_root: Path, note_arg: str, new_name: str | None = None, dest_path: str | None = None, apply: bool = False) -> int`**
Top-level orchestrator. Resolves the source note from a path or unique stem, computes the destination, walks all repo markdown files to plan link rewrites, plans the review-export move and DB rekey, and either prints a dry-run plan or executes everything (file move via `git mv` if available, link rewrites, mkdocs update, DB rekey). Returns a process exit code.

**`resolve_note(arg, *, repo_root, kb_root)`**
Find a note by absolute path, repo-relative path, full filename, or unique stem. Searches the entire `kb/` tree, not just `kb/notes/`, so notes can be relocated between collections.

**`resolve_destination_path(source, new_name, dest_path, *, repo_root, kb_root)`**
Compute the destination path from either a `--to` argument (file or directory) or a positional new title. Enforces the slug length limit.

**`rewrite_links_to_relocated_note(content, source_file, old_path, new_path) -> tuple[str, list[str]]`**
For each markdown link in `content` whose target resolves to `old_path`, rewrite it to point at `new_path`. Skips links inside fenced or inline code regions. Returns the updated text and a list of human-readable change descriptions.

**`rebase_relative_markdown_links(content, old_source_file, new_source_file) -> tuple[str, list[str]]`**
For the note that's being moved: rewrite each of its outbound relative links so they still resolve from the new location. Self-referential links update to the new filename; existing-target links rebase to the new directory.

**`update_mkdocs_config(content, old_docs_path, new_docs_path) -> tuple[str, list[str]]`**
Update `mkdocs.yml` in place: rewrite any matching `nav` entries and `redirect_maps` targets, and append a new redirect entry from `old_docs_path` to `new_docs_path`. Preserves indentation and quoting style.

**`collect_review_export_updates(source, destination, *, repo_root, kb_root)`**
Plan the review-export directory move: returns the source dir, destination dir, and a dict of `{review_file: rewritten_content}` for any review files whose `<!-- REVIEW-METADATA -->` block references the old note path.

**`move_path(source, destination, *, repo_root)`** / **`move_note(source, destination, *, repo_root)`**
Move a path on disk, preferring `git mv` and falling back to `Path.rename` if git isn't available. `move_note` is a thin wrapper kept separate so tests can monkeypatch it.

The smaller helpers (`format_relative_link`, `iter_markdown_tokens`, `split_link_target`, `is_relative_markdown_target`, `find_repo_markdown_files`, `reviews_root`, `repo_relative_note_path`, `encode_review_export_dir`, `review_export_dir_for_note`, `rewrite_review_export_metadata`, `is_nested_git_repo_content`) are exported but rarely interesting outside the orchestrator.
