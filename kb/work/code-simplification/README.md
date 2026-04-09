# Workshop: Code Simplification After Packaging

## Question

Now that Commonplace is a real Python package and the new type system has landed, which parts of the codebase can still be simplified by:

- depending on small, well-scoped libraries where that removes bespoke parsing or glue code
- consolidating repeated helpers into package modules
- deleting compatibility scaffolding that only existed because scripts had to stay stdlib-only and file-local

The motivating example is frontmatter handling. We already have a shared parser in `src/commonplace/lib/frontmatter.py`, but several commands still carry regex parsing or wrapper logic that predates the package boundary.

## Why this workshop exists

The repo crossed an architectural boundary:

- commands are installed from `pyproject.toml`
- reusable code now lives under `src/commonplace/`
- package data and scaffolding are already shipped through the package

That changes the economics. When everything had to run as ad-hoc scripts, every extra dependency and shared module had a higher coordination cost. With a package, some of that cost disappears:

- prerequisites can be declared once
- one library module can serve many commands
- tests can target stable imports instead of script-local functions

The risk is replacing one kind of complexity with another. This workshop exists to find the simplifications that genuinely reduce code and maintenance burden rather than just moving code around.

## Status

This workshop is now partly complete.

The largest package-enabled simplification already landed:

- authored type definitions moved from a custom DSL to JSON Schema in YAML syntax
- runtime dependencies now include `jsonschema` and `PyYAML`
- `src/commonplace/lib/type_resolver.py` centralizes scoped schema lookup and validation
- `src/commonplace/lib/note_parser.py` centralizes parsed-note extraction for validation
- `src/commonplace/cli/validate_notes.py` already routes through the shared parsed-note and type-resolution path

That changes the remaining question. The next wins are no longer "how should the new type system work?" The next wins are "what duplication or dead code still remains now that the type layer is real?"

## Current grounding

- [ADR-014: scripts as Python package, one-tree model](../../notes/adr/014-scripts-as-python-package-one-tree-model.md) — the accepted packaging transition that makes new prerequisites viable
- [ADR-015: standardize authored type definitions on JSON Schema](../../notes/adr/015-standardize-authored-type-definitions-on-json-schema.md) — the accepted type-definition design that retired the custom profile DSL
- [INSTALL.md](../../../INSTALL.md) — the implemented installation flow that replaced the workshop plan
- [`pyproject.toml`](../../../pyproject.toml) — current dependency surface: base runtime deps now include `jsonschema` and `PyYAML`
- [`src/commonplace/lib/frontmatter.py`](../../../src/commonplace/lib/frontmatter.py) — current shared frontmatter parser
- [`src/commonplace/lib/note_parser.py`](../../../src/commonplace/lib/note_parser.py) — shared parsed-note model and markdown helpers
- [`src/commonplace/lib/type_resolver.py`](../../../src/commonplace/lib/type_resolver.py) — shared scoped schema resolution over `.schema.yaml` files
- [`src/commonplace/cli/validate_notes.py`](../../../src/commonplace/cli/validate_notes.py) — already uses the shared parsed-note and type-resolution path
- `commonplace-sync-topic-links` — deleted as obsolete `areas` / `Topics` tooling after ADR-004
- [`src/commonplace/cli/promotion_candidates.py`](../../../src/commonplace/cli/promotion_candidates.py) — has another local frontmatter wrapper
- [`src/commonplace/review/resolve_gates.py`](../../../src/commonplace/review/resolve_gates.py) — strips frontmatter with another regex instead of the shared helper
- [`src/commonplace/review/run_review_bundle.py`](../../../src/commonplace/review/run_review_bundle.py) — still carries local markdown link parsing because it needs link text as well as targets

## What landed since this workshop started

The biggest package-enabled simplification already shipped in the type layer:

- Commonplace no longer owns a custom authored type-definition DSL
- type definitions are standard JSON Schema documents, scoped by directory
- validation now runs over a shared parsed document model instead of ad hoc command-local checks

That was the right big simplification. It removed more bespoke semantics than any parser swap alone would have.

## Revised hypothesis

The highest-value remaining opportunities are now narrower and more concrete:

- finish routing note-parsing and frontmatter-stripping through shared helpers
- centralize the few markdown helpers that still exist in parallel implementations
- audit for any remaining stale product surface left behind by superseded repo conventions

The likely candidates fall into three buckets:

### 1. Shared parsing and markdown helpers

- frontmatter parse / strip / field access
- title extraction
- markdown link extraction and filtering
- note classification helpers (`text` vs `note`, reviewable note discovery, index skipping)

### 2. Package-surface cleanup

- move command-local helpers into `commonplace.lib`
- make commands thin orchestration layers over reusable functions
- reduce places that assume repo-local script execution instead of installed package execution

### 3. Residual stale-surface cleanup

- remove or rewrite docs and notes that still describe deleted `areas` / `Topics` machinery as live
- keep historical references only where they are explicitly framed as historical

## Evaluation criteria

A simplification is worth doing if it improves at least two of:

- less total code
- fewer duplicated parsing rules
- fewer places that define the same filesystem convention
- clearer error behavior
- easier tests
- easier future changes to note schema or markdown conventions

A simplification is not worth doing if it mostly adds abstraction layers, broad dependencies, or hidden behavior without deleting comparable complexity.

## Deliverables

- a concrete inventory of simplification candidates
- an updated view of which earlier simplification questions are now already resolved by the JSON Schema type system
- a decision on the remaining frontmatter strategy: keep the strict local parser, wrap a third-party parser, or replace the local parser
- a short migration sequence for the highest-value deletions
- one or more promoted notes or ADRs if the conclusions stabilize beyond this workshop

## Artifacts

- `candidate-inventory.md` — specific simplification opportunities and likely payoff
- `document-validation-model.md` — current position on note frontmatter, type-definition schemas, and validation layering
- `frontmatter-options.md` — focused comparison of frontmatter strategies now that dependencies are possible
- `library-survey.md` — current external-library options and recommendation

## Open questions

- Should the repo keep the strict frontmatter subset for markdown notes now that `PyYAML` is already a runtime dependency for schemas?
- Which remaining parsing helpers should move into `commonplace.lib`, and which should stay local because they genuinely need richer output than the shared helpers provide?
- Should the next simplification pass focus first on `promotion_candidates.py` and review-side helpers, or on shared markdown-link extraction?
