# Candidate Inventory

## 1. Consolidate frontmatter handling

### Current state

- [`validate_notes.py`](../../../src/commonplace/cli/validate_notes.py) has local `strip_frontmatter()` and `parse_frontmatter()` wrappers
- [`promotion_candidates.py`](../../../src/commonplace/cli/promotion_candidates.py) has another `parse_frontmatter()` wrapper
- [`resolve_gates.py`](../../../src/commonplace/review/resolve_gates.py) has its own regex-based `strip_frontmatter()`
- [`sync_topic_links.py`](../../../src/commonplace/cli/sync_topic_links.py) parses `areas:` with bespoke regexes instead of using the shared parser

### Simplification

Pick one frontmatter path and make everything use it:

- `commonplace.lib.frontmatter` stays the canonical parser, with a few ergonomic helpers added
- or a third-party parser becomes the canonical parser, wrapped by `commonplace.lib.frontmatter`

Either way, commands should stop carrying their own regex parsers and wrappers unless they are doing something genuinely schema-specific.

### Why it matters

Frontmatter is cross-cutting. Duplicated handling means schema changes or bug fixes spread across many commands.

### Likely first step

Refactor `sync_topic_links.py` and `resolve_gates.py` to consume shared helpers. This deletes the clearest duplication without committing yet to any external dependency.

## 2. Introduce a schema-aware metadata accessor

### Current state

Commands repeatedly answer small questions from raw frontmatter data:

- does this file have frontmatter?
- what is the note type?
- what is the status?
- what are the traits?
- what are the areas?

Each command currently re-derives those answers from dicts or regexes.

### Simplification

Add a small package-level helper layer, for example a `commonplace.lib.notes` module that exposes:

- parse note metadata
- return stripped body
- return title
- normalize common fields like `traits`, `areas`, and `status`

### Why it matters

The simplification is not abstraction for its own sake. It centralizes document-shape assumptions that already exist in multiple commands.

## 3. Centralize markdown link extraction

### Current state

`validate_notes.py` and `promotion_candidates.py` both parse markdown links locally. Their rules are close, but not obviously identical.

### Simplification

Move link extraction and target resolution helpers into a shared module.

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

## 5. Revisit the "no runtime dependencies" assumption

### Current state

Base `project.dependencies` is empty even though the repo is now packaged. Optional groups already exist, including `pyyaml` inside `all`.

### Simplification

Treat "no dependency" as a tradeoff to justify, not a default law. A small dependency is acceptable when it:

- deletes bespoke parser code
- improves correctness materially
- is stable and low-risk

### Why it matters

The package boundary changed the installation story. The constraint should be "dependency weight must pay for itself", not "stdlib only everywhere forever".

## 6. Decide whether `sync_topic_links.py` should remain special-case logic

### Current state

`sync_topic_links.py` has its own parser for `areas:` because it only needs one field and currently supports both inline and block-list YAML forms.

### Simplification options

1. Keep it bespoke and document why.
2. Make it consume the shared parser and only support the KB's strict frontmatter subset.
3. Adopt a YAML/frontmatter dependency so both forms are handled by shared infrastructure.

### Why it matters

This file is the clearest test case for the broader question. If the shared parser cannot serve a real command without awkward workarounds, that is evidence the frontmatter strategy needs to change.

## 7. Audit path and root discovery helpers

### Current state

Multiple commands still infer repo roots and KB roots ad hoc from `Path.cwd()` and local constants.

### Simplification

Add one shared project-root / KB-root helper and use it consistently.

### Why it matters

The package transition moved us away from repo-local scripts. Root-discovery logic should reflect that same design instead of remaining implicit in every command.
