# Gate Data Structure Design

This is a concrete data-structure sketch for the first gate-based review implementation. It now incorporates two additional needs from the review-revise workshop:

- gates should be stored as individual reusable files, not only as checks embedded inside review bundles
- today's bundled review instructions should survive as thin user-facing dispatch layers while gate files become the canonical check definitions

## Design goals

The first version should satisfy these constraints:

- gates are stored as plain markdown files, one gate per file
- extracted gates from manual edits can enter the same store as hand-authored gates
- selector reads cheap derived indexes rather than reparsing every file
- bundle membership is still supported, but bundle files are not the canonical storage unit
- staleness is gate-local, not bundle-local
- the design can later move into SQLite without changing the conceptual model

This design intentionally avoids:

- arbitrary rule evaluation from gate files
- event sourcing
- dynamic bundle-diff staleness
- a second storage system for "experimental" vs "real" gates
- full SQL-first normalization

## Canonical entities

There are five entities:

1. `GateDefinition`
   The durable definition of one gate.

2. `BundleDefinition`
   The user-facing review bundle shell: purpose, output contract, shared preamble.

3. `BundleMembership`
   The mapping from a bundle to the gates it includes.

4. `GateReview`
   One accepted review artifact for one `(note_path, gate_id)` pair.

5. `GateSelectionRecord`
   The selector's computed result for one `(note_path, gate_id)` pair.

## 1. GateDefinition

This is the canonical stored definition of one check.

Suggested markdown location:

```text
kb/instructions/review-gates/{lens}/{gate-name}.md
```

Suggested frontmatter:

```yaml
---
gate_id: frontmatter/title-body-alignment
lens: frontmatter
name: Title-body alignment
status: active
summary: Flags notes whose title no longer matches what the body actually establishes.
comparator: title_and_body_major_rewrite
contract_version: 1
contract_fingerprint: auto
invalidate_fields: [title]
body_rewrite_threshold: 0.5
age_threshold_days:
default_severity: WARN
origin_refs:
  - kb/work/review-revise/change-catalogue.md#A1
tags: [metadata, titles]
---
```

Suggested body shape:

```md
## Failure mode

## What to check

## Report when WARN

## Report when INFO

## Anti-goals

## Examples

## Provenance
```

### Required fields

- `gate_id`
  Stable machine id. Never derived from display name at runtime.

- `lens`
  Logical family such as `frontmatter`, `prose`, `semantic`, `accessibility`, `sentence`.

- `name`
  Human-facing label.

- `status`
  Suggested values: `candidate`, `active`, `quarantined`, `retired`.

- `summary`
  One-line description used in indexes and selection prompts.

- `comparator`
  One of the supported primitive stale comparators.

- `contract_version`
  Human-bumped integer for meaning-changing updates.

### Optional fields

- `invalidate_fields`
  Additional scope hints for comparators like frontmatter-field equality.

- `body_rewrite_threshold`
  Needed only for rewrite-sensitive comparators.

- `age_threshold_days`
  Optional expiry.

- `default_severity`
  Useful for reporting or future prioritization, not required by the selector.

- `origin_refs`
  Provenance for extracted gates. Lets us connect a reusable gate back to the edit or workshop evidence that produced it.

- `tags`
  Human and future retrieval aid.

### `contract_fingerprint`

Do not author this by hand. Generate it from the machine-relevant contract surface:

- `gate_id`
- `comparator`
- `contract_version`
- `invalidate_fields`
- `body_rewrite_threshold`
- `age_threshold_days`

Do not include prose body text in this fingerprint. Editorial cleanup, better examples, or clearer recommendations should not invalidate accepted reviews.

### Candidate lifecycle

The review-revise workshop implies that many gates will begin life as extracted hypotheses from one concrete edit. The storage should not special-case that.

Recommendation:

- extracted gates start as `status: candidate`
- hand-authored gates may also start as `candidate` if they have not been exercised yet
- promotion to `active` happens after repeated useful hits or human approval

This keeps one canonical store while still distinguishing trusted gates from newly extracted ones.

## 2. BundleDefinition

Bundles should still exist, but as user-facing review entry points rather than as the canonical place where checks live.

Suggested markdown location:

```text
kb/instructions/review-bundles/{bundle-id}.md
```

During migration, the current top-level files can continue to exist at their current paths and serve as compatibility wrappers:

```text
kb/instructions/frontmatter-review.md
kb/instructions/prose-review.md
kb/instructions/semantic-review.md
kb/instructions/complexity-review.md
```

Suggested frontmatter:

```yaml
---
bundle_id: frontmatter-review
name: Frontmatter review
status: active
summary: Checks retrieval and composability metadata quality.
output_format: standard-review-block
max_gates: 8
---
```

Suggested body shape:

```md
## What this bundle is for

## Shared prerequisites

## Bundle-level cautions

## Output contract
```

The important rule is structural:

- bundle files define shared framing, not the check list
- bundle membership lives in `review_bundles.csv`
- gate files hold the actual review logic

That lets us keep named entry points like `frontmatter-review` without preserving monolithic review documents as the source of truth.

## 3. BundleMembership

Bundle membership is derived, but it should be explicit rather than inferred from directory layout or from the body text of a bundle file.

Suggested CSV:

```text
kb/reports/reviews/csv/review_bundles.csv
```

Columns:

- `bundle_id`
- `gate_id`
- `required`
- `order`
- `enabled`

Example:

```csv
bundle_id,gate_id,required,order,enabled
frontmatter-review,frontmatter/description-discrimination,true,10,true
frontmatter-review,frontmatter/title-composability,true,20,true
frontmatter-review,frontmatter/claim-strength,true,30,true
frontmatter-review,frontmatter/title-body-alignment,true,40,true
```

For the first version:

- treat this table as static input
- do not use bundle membership changes as a stale reason

## 4. GateReview

This is one accepted review artifact for one note and one gate.

Suggested path:

```text
kb/reports/reviews/gates/{encoded-note-path}/{gate-id}.md
```

Example:

```text
kb/reports/reviews/gates/kb__notes__backlinks_md/frontmatter__title-body-alignment.md
```

The path encoding only needs to be:

- collision-safe
- reversible
- stable across scripts

### Gate review metadata block

Suggested leading metadata comment:

```md
<!-- GATE-REVIEW-METADATA
note-path: kb/notes/backlinks.md
gate-id: frontmatter/title-body-alignment
bundle-id: frontmatter-review
gate-contract-version: 1
gate-contract-fingerprint: 7a4d...
accepted-note-sha: 435bea...
accepted-note-commit: cfa5a8...
accepted-scope-fingerprint: 21c9...
accepted-at: 2026-03-26T10:15:00+01:00
acceptance-kind: full-review
review-status: active
-->
```

### Required metadata fields

- `note-path`
- `gate-id`
- `gate-contract-version`
- `gate-contract-fingerprint`
- `accepted-note-sha`
- `accepted-scope-fingerprint`
- `accepted-at`

### Optional metadata fields

- `bundle-id`
- `accepted-note-commit`
- `acceptance-kind`
- `review-status`

### Review body

The first version does not need a universal prose template beyond:

- one heading naming note + gate
- optional WARN / INFO / CLEAN finding blocks
- an overall outcome

The selector should rely on metadata for stale detection, not on parsing the prose body.

## 5. GateSelectionRecord

This is not a stored canonical artifact. It is the engine result.

Suggested Python dataclass:

```python
from dataclasses import dataclass


@dataclass
class GateSelectionRecord:
    note_path: str
    gate_id: str
    bundle_id: str | None
    review_path: str | None
    status: str
    reason: str
    comparator: str
    contract_version: int | None
    contract_fingerprint: str | None
    accepted_note_sha: str | None
    accepted_scope_fingerprint: str | None
    accepted_at: str | None
    diff_kind: str = "none"
    diff: str | None = None
```

Suggested `status` values:

- `stale`
- `fresh`
- `error`

Suggested `reason` values:

- `missing-gate-review`
- `gate-updated`
- `scope-changed`
- `note-changed`
- `expired`
- `missing-metadata`
- `invalid-accepted-note-sha`
- `unreadable-review`

## Derived indexes

The selector should not crawl markdown directly at runtime when the gate count grows.

### `gate_definitions.csv`

Suggested path:

```text
kb/reports/reviews/csv/gate_definitions.csv
```

Columns:

- `gate_id`
- `lens`
- `name`
- `status`
- `summary`
- `comparator`
- `contract_version`
- `contract_fingerprint`
- `invalidate_fields`
- `body_rewrite_threshold`
- `age_threshold_days`

### `bundle_definitions.csv`

Suggested path:

```text
kb/reports/reviews/csv/bundle_definitions.csv
```

Columns:

- `bundle_id`
- `name`
- `status`
- `summary`
- `output_format`
- `max_gates`

### `gate_reviews.csv`

Suggested path:

```text
kb/reports/reviews/csv/gate_reviews.csv
```

Columns:

- `note_path`
- `gate_id`
- `bundle_id`
- `review_path`
- `gate_contract_version`
- `gate_contract_fingerprint`
- `accepted_note_sha`
- `accepted_note_commit`
- `accepted_scope_fingerprint`
- `accepted_at`
- `acceptance_kind`
- `review_status`

These tables are enough for the first selector implementation.

## Comparator primitives

Keep this list small and hardcoded.

Suggested initial set:

- `full_text_exact`
- `frontmatter_fields_exact`
- `title_exact`
- `title_status_exact`
- `title_and_body_major_rewrite`
- `frontmatter_and_body_major_rewrite`
- `age_threshold`

### Comparator parameter model

Some comparators need parameters. Keep them as explicit fields rather than free-form blobs.

Examples:

- `frontmatter_fields_exact`
  Uses `invalidate_fields`

- `title_and_body_major_rewrite`
  Uses `body_rewrite_threshold`

- `age_threshold`
  Uses `age_threshold_days`

## Scope fingerprints

`accepted_note_sha` alone is too coarse for gate-level freshness. Each gate review also needs `accepted_scope_fingerprint`.

Suggested meaning:

- fingerprint of only the note features the gate comparator cares about

Examples:

- `title_exact`
  hash of `title`

- `title_status_exact`
  hash of `title`, `type`, `status`

- `frontmatter_fields_exact(title,description)`
  hash of those exact fields

- `title_and_body_major_rewrite`
  hash of `title` plus accepted body snapshot identity

The selector can then distinguish:

- note blob changed, but gate scope did not
- gate scope changed directly
- body rewrite exceeded threshold

## Minimal Python-side structs

These are the minimal structs the implementation agent should have in mind.

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class GateContract:
    gate_id: str
    comparator: str
    contract_version: int
    contract_fingerprint: str
    invalidate_fields: tuple[str, ...] = ()
    body_rewrite_threshold: float | None = None
    age_threshold_days: int | None = None


@dataclass(frozen=True)
class GateDefinition:
    gate_id: str
    lens: str
    name: str
    status: str
    summary: str
    contract: GateContract


@dataclass(frozen=True)
class BundleDefinition:
    bundle_id: str
    name: str
    status: str
    summary: str
    output_format: str
    max_gates: int | None = None


@dataclass(frozen=True)
class BundleMembership:
    bundle_id: str
    gate_id: str
    required: bool
    order: int
    enabled: bool


@dataclass
class GateReviewState:
    note_path: str
    gate_id: str
    bundle_id: str | None
    review_path: str | None
    gate_contract_version: int | None
    gate_contract_fingerprint: str | None
    accepted_note_sha: str | None
    accepted_note_commit: str | None
    accepted_scope_fingerprint: str | None
    accepted_at: str | None
    acceptance_kind: str | None
    load_error: str | None
```

## First-version selector flow

For a bundle request like `frontmatter-review`:

1. Read `bundle_definitions.csv` and confirm the bundle exists.
2. Read `review_bundles.csv` and get enabled required gates.
3. Read `gate_definitions.csv` for those gates.
4. Read `gate_reviews.csv` for the requested notes and gates.
5. For each `(note, gate)`:
   - if no review row: `missing-gate-review`
   - if review metadata invalid: error
   - if contract version or fingerprint mismatches current definition: `gate-updated`
   - else run comparator against current note state
   - else if expired by age: `expired`
   - else mark fresh
6. Return gate-level stale records.
7. Optionally group stale records by note or bundle for execution.

## Migration from current bundles

The current bundle files should not remain the canonical check definitions, but they also should not be deleted immediately.

Recommended migration stance:

1. Decompose each bundled review into individual gate files.
2. Keep named bundles such as `frontmatter-review` and `prose-review` as thin wrappers with shared framing, prerequisites, and output contract.
3. Move membership knowledge into `review_bundles.csv`, not bundle prose.
4. During transition, allow an adapter to synthesize temporary gate rows from legacy bundle review artifacts.
5. Retire monolithic check bodies only after gate-native execution and historical review reading both work.

What not to do:

- do not keep bundle docs and gate files as two parallel canonical check stores
- do not make users invoke dozens of individual gates directly for common workflows
- do not invalidate accepted reviews just because wrapper prose changed

## Non-goals for the first version

Do not add these yet:

- stale reason: bundle membership changed
- historical many-review versions per `(note, gate)`
- automatic gate promotion / retirement logic
- arbitrary comparator code loaded from markdown
- SQL storage

## Copyable recommendation

If another agent is implementing the gates mechanism now, the practical instruction is:

1. Treat `GateDefinition`, `BundleDefinition`, `BundleMembership`, and `GateReviewState` as the primary models.
2. Keep gate definitions in markdown, but generate `gate_definitions.csv`, `bundle_definitions.csv`, `review_bundles.csv`, and `gate_reviews.csv`.
3. Put staleness logic on `GateContract`, not on bundle id.
4. Store both `accepted_note_sha` and `accepted_scope_fingerprint`.
5. Keep comparators hardcoded and few.
6. Keep current bundle names as thin dispatch layers until the migration is complete.
7. Ignore bundle-membership-change invalidation until a later phase.
