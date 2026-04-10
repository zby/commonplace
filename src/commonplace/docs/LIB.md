# Commonplace Library (`commonplace.lib`)

Shared library modules used by CLI commands and the review system. `frontmatter` and `type_resolver` require `PyYAML`; `type_resolver` also requires `jsonschema` (which transitively brings in `referencing`).

## Module overview

```
frontmatter.py     Parse/validate markdown frontmatter (strict YAML subset)
 naming.py         Shared note title and filename-slug constraints
note_parser.py     Parse markdown notes into a schema-friendly document model
type_resolver.py   Resolve note types from scoped JSON Schema definitions
```

Dependencies: `note_parser` → `frontmatter`. `type_resolver` is independent of the other lib modules (but requires external packages).

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

**`extract_body_dates(body: str) -> tuple[str, ...]`**
Deduplicated ISO dates found in body text.

**`remove_fenced_code_blocks(text: str) -> str`** / **`remove_code_regions(text: str) -> str`**
Strip fenced code blocks, or both fenced and inline code. Used internally before heading/link extraction to avoid false matches.

**`strip_frontmatter(content: str) -> str`**
Delegates to `frontmatter.strip()`.

---

## type_resolver

Resolve structural note types from scoped JSON Schema definitions. Uses hierarchical schema discovery — schemas are searched from most-specific scope to workspace root.

### Schema discovery

Schemas live in `types/` directories at each scope level under `kb/`. For a note at `kb/work/my-project/foo.md`, the search order is:

1. `kb/work/my-project/types/{type}.schema.yaml`
2. `kb/work/types/{type}.schema.yaml`
3. `kb/types/{type}.schema.yaml`

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
- `definition_path: Path | None` — path to `.schema.yaml` file
- `schema: dict | None` — parsed JSON Schema
- `required_headings: tuple[str, ...]` — headings that must appear
- `any_headings: tuple[str, ...]` — at least one must appear
- `required_fields: tuple[str, ...]` — required frontmatter fields (excluding `type`)
- `allowed_status: tuple[str, ...]` — valid status enum values
- `requires_date: bool` — whether a date is required
- `min_links: int | None` — minimum link count

**`resolve_type(file_path: Path, frontmatter: dict | None, *, repo_root: Path | None = None) -> TypeProfile`**
Main entry point. Determines type, locates schema, loads and extracts constraints. Handles `$ref` resolution and `allOf` composition across schema inheritance chains.

**`validate_instance(profile: TypeProfile, instance: dict) -> list[ValidationError]`**
Validate a document instance (from `ParsedDocument.to_validation_object()`) against the type's JSON Schema. Returns errors sorted by document path. Returns empty list for types without schemas (e.g., `"text"`).

### Caching

Schema loading (`_load_schema`) and validator construction (`_validator_for_path`) use `@lru_cache`. Schemas are loaded on demand, not at startup.
