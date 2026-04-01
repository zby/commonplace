# Gate selector flexibility brief

This workshop starts from the current system in [REVIEW-SYSTEM.md](../../../scripts/REVIEW-SYSTEM.md): freshness is filesystem-based, the stored artifact is one review file per `(note, gate, model)`, and selector output is a stale `(note, gate)` queue.

The redesign target is not "make the selector abstract." The target is: make new selection workflows cheap to express without reintroducing the complexity that the review-system simplification removed.

## What the current selector does well

[review_target_selector.py](../../../scripts/review_target_selector.py) is easy to understand because it has one direct pipeline:

1. discover gates from a bundle directory or from all gate files
2. discover reviewable notes from top-level `kb/notes/`
3. evaluate freshness for every `(note, gate)` pair
4. optionally attach a git diff for `note-changed`
5. print grouped text or JSON

This matches the current sweep instructions well. There is little hidden state and almost no configuration surface.

## Where the current selector is too rigid

The selector currently hardcodes multiple independent decisions into one script:

- **Inventory policy** — only top-level notes with frontmatter are reviewable
- **Gate scope policy** — gates come from one lens directory or all gates
- **Execution priority** — results are lexicographically sorted, not ranked for operational usefulness
- **Diff policy** — note diffs are only attached in JSON mode and only for `note-changed`
- **Output contract** — the only outputs are grouped text and raw JSON

Those choices were reasonable defaults for the first version. They become constraints once we want queues like:

- recurse into specific note subdirectories but not all of `kb/notes/`
- select only gates matching a lens, tag, or explicit ids
- ask for "all stale pairs for one note" versus "highest-signal stale work across the KB"
- emit grouped execution packets instead of flat stale pairs
- emit stats or counts for planning without materializing all diffs
- reuse the same selector engine for sweep, audit, triage, and warning-maintenance workflows

## Design constraint

Do not reopen the simplified review architecture.

This workshop should preserve these properties from [REVIEW-SYSTEM.md](../../../scripts/REVIEW-SYSTEM.md):

- freshness remains mtime-based
- ack remains `touch`
- review files remain the source of truth
- gate files remain plain markdown in bundle directories
- the selector still answers freshness by comparing note, gate, and review mtimes

If the redesign requires new indexes, hashes, or metadata bookkeeping just to express common selection modes, it is probably regressing toward the older overengineered designs.

## Flexibility axes to support

### 1. Inventory

The selector should separate "which notes are candidates?" from freshness evaluation.

Candidate inventory likely needs a few explicit modes:

- top-level reviewable notes
- recursive under one path prefix
- explicit note paths
- maybe current-note subsets such as one tag or one directory family

This is not about making arbitrary query language. It is about decoupling note discovery from stale checking.

### 2. Gate scope

The selector should accept gate scopes more specific than "one bundle" or "all gates."

Useful scopes:

- one bundle
- multiple bundles
- explicit gate ids
- all gates

Bundle resolution should stay cheap and filesystem-native. It does not need a database or declarative policy engine.

### 3. Freshness evaluation

The freshness rules themselves are currently simple and should remain simple:

- missing review
- gate changed
- note changed

What should change is the packaging around evaluation:

- let callers request records with or without diffs
- keep raw freshness records separate from rendered output
- make it easy to post-process records into grouped execution units

### 4. Ranking and grouping

A flat stale list is not always the right operational view.

Different workflows want different shapes:

- flat stale pairs for audit
- grouped by note for sweep execution
- grouped by `(note, lens)` for review packet creation
- counts by reason for planning
- maybe prioritized views where `missing-review` sorts before `note-changed`

This suggests the selector should produce a neutral record set first, then apply grouping or ranking as a separate layer.

### 5. Output renderers

The CLI should be able to render at least these shapes without changing freshness logic:

- grouped text
- JSON stale records
- grouped JSON packets
- summary stats

Renderers are presentation policy. They should not be fused to note discovery or freshness checks.

## Proposed architecture

Keep this minimal:

1. **Inventory layer**
   Returns candidate note paths.

2. **Gate scope layer**
   Returns gate ids and gate paths.

3. **Freshness layer**
   Evaluates one `(note, gate)` pair into a neutral stale record.

4. **Post-processing layer**
   Applies optional diff loading, grouping, ranking, and filtering on stale reasons.

5. **Renderer layer**
   Prints plain text, JSON, packets, or stats.

This is enough structure to make the selector flexible without turning it into a policy framework.

## Non-goals

- no database
- no persisted derived indexes
- no gate-local DSL for freshness rules
- no plugin system
- no attempt to unify `review_target_selector.py` and `warn_selector.py` unless the shared abstraction falls out naturally

The selector only needs to become modular enough that adding a new queue shape or input scope is a local change.

## Immediate design questions

1. Should bundle resolution keep using bare directory names like `prose`, or should the CLI standardize on bundle ids like `prose-review` and map them internally?
2. Should recursive inventory be path-driven (`--dir kb/notes/definitions --recursive`) or collection-driven (`--scope definitions`)?
3. Should diffs be computed only on demand per record, or should JSON renderers be allowed to force eager diff loading for the whole result set?
4. What is the smallest shared record shape that both sweep instructions and future maintenance tools can consume without re-parsing CLI text output?

## Success criterion

Adding a new selection mode should mean composing inventory, gate scope, grouping, or rendering pieces, not editing one large function that mixes all four concerns.
