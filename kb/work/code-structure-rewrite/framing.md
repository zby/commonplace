# Code Structure Rewrite Workshop

## Status

Implementation complete as of 2026-04-13.

Baseline before the rewrite: `uv run pytest -q` reported `199 passed`. After implementation: `uv run pytest -q` reported `209 passed`.

## Scope

The non-review Python code: `commonplace.lib` and the non-review CLI commands. The review system (`commonplace.review` and `commonplace.cli.review`) is excluded — it's a separate subsystem with its own rewrite workshop.

## What exists today

### Library modules (`commonplace.lib`)

| Module | Lines | Purpose | Dependencies |
|--------|-------|---------|-------------|
| `frontmatter.py` | 62 | Parse YAML frontmatter from markdown | PyYAML |
| `naming.py` | 41 | Slug/filename helpers | — |
| `note_parser.py` | 102 | Parse markdown into `ParsedDocument` | frontmatter |
| `type_resolver.py` | 204 | Resolve types from scoped JSON Schema | jsonschema, PyYAML |
| `validation.py` | 216 | Deterministic validation pipeline | note_parser, type_resolver, naming |
| `relocation.py` | 831 | Note and directory relocation with link rewriting | naming, **review.review_db**, **review.review_metadata** |

### CLI commands (non-review)

| Command | Lines | Purpose | Calls |
|---------|-------|---------|-------|
| `init_project.py` | 253 | Scaffold a new project | — |
| `validate_notes.py` | 161 | Run validation, format output | lib.validation |
| `generate_notes_index.py` | 103 | Generate directory listing index.md | lib.frontmatter |
| `sync_generated_index.py` | 298 | Rebuild generated sections of index pages | lib.frontmatter |
| `refresh_indexes.py` | 58 | Orchestrate all index refreshes | **cli.generate_notes_index**, **cli.sync_generated_index** |
| `relocate_note.py` | 46 | CLI wrapper for relocation | lib.relocation |
| `relocate_directory.py` | 57 | CLI wrapper for directory relocation | lib.relocation |
| `promotion_candidates.py` | 164 | Find notes ready for promotion | lib.frontmatter, lib.note_parser |
| `github_snapshot.py` | 190 | Snapshot GitHub issues/PRs | lib.naming |
| `x_snapshot.py` | 442 | Snapshot X/Twitter content | lib.naming, xdk |

Total: ~3,230 lines of non-review Python.

## Goals

Six things this code does:

1. **Parse and validate markdown notes** against type-based schemas (frontmatter, note_parser, type_resolver, validation, validate_notes)
2. **Maintain indexes** — directory listings and tag-based generated sections (generate_notes_index, sync_generated_index, refresh_indexes)
3. **Relocate notes and directories** with referential integrity — link rewriting, mkdocs redirects, review DB updates (relocation, relocate_note, relocate_directory)
4. **Scaffold new projects** with correct directory structure and copied templates (init_project)
5. **Snapshot external content** into the KB (github_snapshot, x_snapshot)
6. **Surface promotion candidates** based on link graph analysis (promotion_candidates)

## Constraints

1. **Stdlib-only for core** — PyYAML + jsonschema are the only required dependencies; xdk is optional
2. **CLI entry points** — each command must be invokable as `commonplace-*`
3. **Works from cwd** — no config file; workspace root is the current directory
4. **Collection-scoped type hierarchy** — schemas resolve from the note's top-level collection `types/` directory, then global `kb/types/`
5. **Review system integration** — relocation must update review state, but review is a separate subsystem
6. **Filesystem is the database** — no persistent state beyond files for core operations (SQLite is review-only)
7. **Deterministic** — validation and index generation must produce the same output given the same files

## Structural problems in the current code

### 1. Process-level globals

Three modules bind state to `Path.cwd()` at import time:

- `type_resolver.py`: `WORKSPACE_ROOT = Path.cwd().resolve()`
- `sync_generated_index.py`: `KB_ROOT = Path.cwd().resolve() / "kb"`
- `promotion_candidates.py`: `NOTES_DIR = Path("kb/notes")`

This makes testing require `os.chdir()` or monkeypatching. Functions that need the workspace root receive it via `repo_root` parameters in some places but not others — the pattern is inconsistent.

### 2. Duplicated functions

| Function | Appears in | Notes |
|----------|-----------|-------|
| `is_nested_git_repo_content()` | validation.py, relocation.py | Identical |
| `get_title()` | generate_notes_index.py, sync_generated_index.py | Equivalent to `note_parser.extract_title()` |
| `_dedup_existing_snapshot()` | github_snapshot.py, x_snapshot.py | Nearly identical |
| Link graph traversal | validation.py (`orphan_info`), promotion_candidates.py | Different implementations of the same concept |

### 3. Cross-package coupling

`relocation.py` lives in `commonplace.lib` but imports from `commonplace.review.review_db` and `commonplace.review.review_metadata`. This means the "core" library depends on the review system. Installing commonplace without review support would fail on relocation.

The dependency should flow the other direction: review hooks into relocation, not relocation imports review.

### 4. CLI modules doing library work

`sync_generated_index.py` contains ~200 lines of library logic (collection discovery, tag collection, index building) that `refresh_indexes.py` then imports directly. This is CLI-calling-CLI — the library logic should be extracted.

`generate_notes_index.py` similarly contains the index generation logic alongside CLI argument parsing.

### 5. No shared KB model

Every command that works with the KB independently:
- Discovers markdown files (each with its own glob + filter logic)
- Parses frontmatter
- Resolves paths relative to the workspace root
- Builds its own understanding of collections and their boundaries

There's no shared object encapsulating "this workspace, its collections, and how to find things in it."

### 6. Relocation is overloaded

`relocation.py` (831 lines) handles: note resolution, directory resolution, destination resolution, link parsing, link rewriting (inbound and outbound), mkdocs config updating, review export management, review DB rekeying, file moving, and dry-run reporting. It's effectively a mini-application in one module.

## What works well

These should survive a rewrite:

1. **frontmatter.py, naming.py, note_parser.py** — clean, focused, well-tested. Good foundation modules.
2. **ParsedDocument** — frozen dataclass, good immutable data model.
3. **Validation pipeline** — clear separation of check types (title/slug, links, schema).
4. **Relocation dry-run pattern** — plan-then-execute is good UX.
5. **CLI/lib intention** — the idea of separating CLI from logic is right, just inconsistently applied.
6. **Type resolver's scoped discovery** — collection-local type lookup with global fallback is the right algorithm.

## Next steps

Architecture proposal in [proposed-architecture.md](./proposed-architecture.md).
