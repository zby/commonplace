# Migration plan: bundle reviews to gate-native reviews

This is the working plan for moving from today's monolithic review bundles to a gate-native data structure.

## Phase 1: establish canonical storage

Create the canonical entities without changing user-facing review names yet.

- add gate definition files under `kb/instructions/review-gates/{lens}/`
- add bundle definition shells for the existing named reviews
- materialize `bundle_definitions.csv`, `review_bundles.csv`, `gate_definitions.csv`, and `gate_reviews.csv`
- treat current top-level review docs as compatibility wrapper locations while the new structure settles

The key outcome of phase 1 is conceptual: check definitions move out of bundle prose and into individual gate files.

## Phase 2: decompose existing bundles

Convert the current stable bundles into explicit gate memberships.

- split `frontmatter-review.md` into four gate files
- split `prose-review.md` into its eight checks
- split `semantic-review.md` into its three major checks
- decide whether `complexity-review.md` stays a small bundle or a single-note-level bundle with four gates

Rules for decomposition:

- preserve existing check wording where it already works
- keep shared prerequisites and output format at the bundle layer
- do not duplicate check prose in both bundle files and gate files

The goal is that the bundle still exists as an invocation target, but the bundle file no longer owns the canonical check list.

## Phase 3: bridge legacy accepted reviews

The selector should become gate-native before every historical artifact has been rewritten.

- read legacy bundle review artifacts
- synthesize virtual gate review rows from the shared accepted note metadata
- evaluate freshness per gate using each gate's comparator
- emit stale `(note, gate)` records even when the accepted artifact was bundle-sized

This prevents migration from blocking on historical backfill.

## Phase 4: gate-native execution

Once selector and storage are stable, change execution and acceptance.

- execute reviews at gate granularity
- optionally regroup stale gates into a bundle-sized execution packet for prompt efficiency
- write one accepted artifact per `(note, gate)`
- update `gate_reviews.csv` from those artifacts

This is the point where gate-level freshness and gate-level acceptance finally align.

## Phase 5: reduce wrapper weight

After gate-native execution is proven:

- trim bundle wrappers to purpose, prerequisites, cautions, and output contract
- remove duplicated check sections from bundle files
- move any remaining selection hints into bundle metadata or explicit selector config

At the end of this phase, bundle files are wrappers, not shadow copies of gate logic.

## Review-revise intake

The review-revise experiments should feed this system through the same gate store.

- gates extracted from manual before/after edits enter as `candidate`
- provenance points back to the benchmark artifact or change catalogue entry
- repeated useful hits or explicit review promotes a candidate gate to `active`

This avoids inventing a second mechanism for "learned" gates.

## Ordering recommendation

The safest order is:

1. define gate and bundle data structures
2. decompose current stable bundles
3. add legacy review adapter
4. switch selector to gate-native freshness
5. switch execution to per-gate artifacts

Doing execution before storage and selector semantics stabilise would make migration harder, not easier.
