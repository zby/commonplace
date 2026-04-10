# Candidate Inventory

## 1. Delete obsolete areas / Topics tooling

### Current state

- [ADR-004: replace areas with tags](../../reference/adr/004-replace-areas-with-tags.md) says removing Topics should eliminate `sync_topic_links.py`
- there are no live `areas:` fields or `Topics:` footers in active `kb/notes/`, `kb/sources/`, or `kb/work/` content
- this deletion has now been executed: the package entry point, implementation file, and package docs were removed

### Simplification

- keep historical migration support as one-off tooling if needed, not as a maintained end-user command
- clean up remaining active notes that still describe the deleted command as present

### Why it matters

This is deletion rather than refactoring:

- removes dead code outright
- removes stale docs that advertise a superseded convention
- reduces pressure to broaden the frontmatter parser for a command that may no longer belong in the product

### Likely first step

Follow through on the stale-knowledge cleanup so active notes stop describing the deleted command as a current part of the system.

## 2. Finish consolidating note parsing around shared helpers

### Current state

- [`validate_notes.py`](../../../src/commonplace/cli/validate_notes.py) already uses [`note_parser.py`](../../../src/commonplace/lib/note_parser.py) plus [`type_resolver.py`](../../../src/commonplace/lib/type_resolver.py)
- [`promotion_candidates.py`](../../../src/commonplace/cli/promotion_candidates.py) still has its own `parse_frontmatter()`, title extraction, and markdown-link extraction
- [`resolve_gates.py`](../../../src/commonplace/review/resolve_gates.py) still has its own regex-based `strip_frontmatter()`
- review-side commands import that local strip helper, so one duplicate implementation leaks into multiple review commands

### Simplification

- make `note_parser` and `frontmatter.strip()` the default path for note-like markdown handling
- remove command-local wrappers where the shared API is already sufficient
- keep local helpers only where a command genuinely needs richer output than the current shared module exposes

### Why it matters

The shared parsed-note model now exists. Not using it is pure duplication.

### Likely first step

Refactor `promotion_candidates.py` onto `note_parser`, and switch `resolve_gates.py` to `frontmatter.strip()`. This is low-risk because the target helpers already exist and are exercised by validation tests.

## 3. Centralize markdown link extraction where semantics actually match

### Current state

- [`note_parser.find_markdown_links()`](../../../src/commonplace/lib/note_parser.py) returns link targets only
- [`promotion_candidates.py`](../../../src/commonplace/cli/promotion_candidates.py) currently reimplements target extraction locally
- [`run_review_bundle.py`](../../../src/commonplace/review/run_review_bundle.py) reimplements link parsing because it needs both link text and target after stripping code regions

### Simplification

- either:
  - route simple target-only cases through `note_parser.find_markdown_links()`
- or:
  - add one richer shared helper that returns `(text, target)` pairs and make both note-parser and review code build on it

### Why it matters

The link graph is already becoming infrastructure for validation, promotion, and review. Divergent parsers will turn into latent bugs.

## 4. Separate library code from CLI code more aggressively

### Current state

Several commands still mix:

- argument parsing
- filesystem traversal
- markdown parsing
- business rules

inside one file.

### Simplification

Commands become thin `argparse` entry points over library functions in `commonplace.lib` or domain modules like `commonplace.review`.

### Why it matters

This makes tests cheaper and reduces the pressure to duplicate helpers between commands.

## 5. Revisit markdown-frontmatter strategy separately from the type system

### Current state

- base runtime dependencies are no longer empty: [`pyproject.toml`](../../../pyproject.toml) now includes `jsonschema` and `PyYAML`
- `PyYAML` is already justified by authored JSON Schema loading in [`type_resolver.py`](../../../src/commonplace/lib/type_resolver.py)
- markdown frontmatter still uses the strict local parser in [`frontmatter.py`](../../../src/commonplace/lib/frontmatter.py)

### Simplification

- treat markdown frontmatter as its own decision:
  - keep the strict parser
  - wrap `PyYAML` but preserve the narrower contract
  - or switch to standard YAML frontmatter entirely

### Why it matters

The dependency question for type definitions is already settled. The remaining question is whether broader YAML buys enough simplification on the markdown side to justify changing the note contract.

## 6. Audit path and root discovery helpers

### Current state

Multiple commands still infer repo roots and KB roots ad hoc from `Path.cwd()` and local constants.

### Simplification

Add one shared project-root / KB-root helper and use it consistently.

### Why it matters

The package transition moved us away from repo-local scripts. Root-discovery logic should reflect that same design instead of remaining implicit in every command.
