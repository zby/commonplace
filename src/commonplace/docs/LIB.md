# Commonplace Library (`commonplace.lib`)

Shared library modules used by CLI commands and the review system. All modules are stdlib-only except `type_resolver`, which requires `jsonschema` (which transitively brings in `referencing`) and `pyyaml`.

## Module overview

```
frontmatter.py     Parse/validate markdown frontmatter (strict YAML subset)
note_parser.py     Parse markdown notes into a schema-friendly document model
type_resolver.py   Resolve note types from scoped JSON Schema definitions
```

Dependencies: `note_parser` → `frontmatter`. `type_resolver` is independent of the other lib modules (but requires external packages).

---

## frontmatter

Parse and validate markdown frontmatter using a strict, stdlib-only YAML subset. No dependency on PyYAML.

### Grammar rules

- Keys: `[a-z][a-z0-9_-]*` (lowercase only, no nesting)
- Values: inline lists `[item, item]`, quoted strings, or unquoted scalars
- Boolean coercion: `true`/`false` → `bool`
- Digit-only strings → `int`
- Empty values → `""`
- Unsupported: block lists, multi-line scalars, anchors, YAML tags, nested structures

### Public API

**`FrontmatterResult`** — dataclass holding parse results:
- `data: dict[str, Any]` — parsed key-value pairs
- `raw: str` — raw frontmatter text between delimiters
- `errors: list[str]` — parse/validation error messages
- `ok: bool` — property, `True` if no errors

**`extract_raw(content: str) -> str | None`**
Extract the raw frontmatter text between `---` delimiters. Returns `None` if no frontmatter block found.

**`parse(content: str) -> FrontmatterResult`**
Full parse: extracts frontmatter, validates each line against the grammar, detects duplicate keys and unsupported syntax. Collects all errors (not just the first).

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

**`parse_frontmatter(content: str) -> tuple[dict | None, str | None]`**
Parse frontmatter only. Returns `(data, error)`.

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

Schemas live in `types/` directories at each scope level. For a note at `kb/work/my-project/foo.md`, the search order is:

1. `kb/work/my-project/types/{type}.schema.yaml`
2. `kb/types/{type}.schema.yaml`
3. `{workspace_root}/types/{type}.schema.yaml`

For a note at `kb/notes/bar.md`:

1. `kb/notes/types/{type}.schema.yaml`
2. `kb/types/{type}.schema.yaml`
3. `{workspace_root}/types/{type}.schema.yaml`

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
