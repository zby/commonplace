# Workshop: Code Simplification After Packaging

## Question

Now that Commonplace is a real Python package rather than a pile of repo-local scripts, which parts of the codebase can be simplified by:

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

## Current grounding

- [Plan: scripts as a Python package, project initialized locally](../installation-simplification/python-packaging-plan.md) — the package transition that makes new prerequisites viable
- [`pyproject.toml`](../../../pyproject.toml) — current dependency surface: no base runtime deps, small optional groups
- [`src/commonplace/lib/frontmatter.py`](../../../src/commonplace/lib/frontmatter.py) — current shared frontmatter parser
- [`src/commonplace/cli/validate_notes.py`](../../../src/commonplace/cli/validate_notes.py) — still wraps the shared parser with command-local helpers
- [`src/commonplace/cli/sync_topic_links.py`](../../../src/commonplace/cli/sync_topic_links.py) — still parses frontmatter with bespoke regexes
- [`src/commonplace/cli/promotion_candidates.py`](../../../src/commonplace/cli/promotion_candidates.py) — has another local frontmatter wrapper
- [`src/commonplace/review/resolve_gates.py`](../../../src/commonplace/review/resolve_gates.py) — strips frontmatter with another regex instead of the shared helper

## Initial hypothesis

The biggest simplification opportunities are not new features. They are places where the package boundary lets us remove duplicated parsing, duplicated discovery rules, and duplicated filesystem conventions.

The likely candidates fall into three buckets:

### 1. Shared parsing and markdown helpers

- frontmatter parse / strip / field access
- title extraction
- markdown link extraction and filtering
- note classification helpers (`text` vs `note`, reviewable note discovery, index skipping)

### 2. Dependency-enabled replacements

- adopt a maintained frontmatter or YAML parser if it deletes enough custom code and edge-case handling
- add narrow runtime prerequisites when they replace repeated regex logic with a clearer contract

### 3. Package-surface cleanup

- move command-local helpers into `commonplace.lib`
- make commands thin orchestration layers over reusable functions
- reduce places that assume repo-local script execution instead of installed package execution

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
- a decision on frontmatter strategy: keep the strict local parser, wrap a third-party parser, or replace the local parser
- a short migration sequence for the highest-value deletions
- one or more promoted notes or ADRs if the conclusions stabilize beyond this workshop

## Artifacts

- `candidate-inventory.md` — specific simplification opportunities and likely payoff
- `document-validation-model.md` — current position on note frontmatter, type-definition schemas, and validation layering
- `frontmatter-options.md` — focused comparison of frontmatter strategies now that dependencies are possible
- `library-survey.md` — current external-library options and recommendation

## Open questions

- Should the repo keep the strict frontmatter subset as part of the KB contract even if a third-party parser is used underneath?
- Is `pyyaml` enough, or would a frontmatter-specific library actually remove more code?
- Which duplicated helpers should move into `commonplace.lib`, and which should stay command-local because they are truly one-off?
- How much simplification should happen before adding more commands or more type-system logic?
