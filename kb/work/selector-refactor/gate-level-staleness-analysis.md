# Analysis: gate-level staleness in the selector

This is a separate analysis for the "split reviews into individual gates" feature. It does not change the refactor plan yet.

## The core design change

Today the selector answers:

- for review type `X`
- compare the current note against one accepted review artifact
- decide changed / unchanged

If reviews split into gates, that model is too coarse. The selector needs to answer:

- for bundle `X`
- which gates currently belong to that bundle
- for each `(note, gate)` pair, is the accepted gate result still fresh
- then optionally re-bundle stale gates into one execution packet

The important shift is from **bundle freshness** to **gate freshness**.

## What "stale" should mean

For gate-level review, "stale" is not one condition. It is the union of several independent invalidation paths:

1. **Missing gate review**
   The bundle now expects gate `G`, but there is no accepted `(note, G)` artifact.

2. **Note changed in a way that matters to gate `G`**
   This is the current selector problem, but now it must be gate-specific rather than review-type-specific.

3. **Gate contract changed**
   The gate definition was edited in a way that changes what "pass/warn/info" means. Old acceptances for that gate should no longer count as current.

4. **Time-based expiry**
   Some gates should go stale after age threshold even if the note is unchanged.

5. **Broken metadata / unresolved baseline**
   Missing metadata, unreadable accepted blob, invalid contract version, broken path mapping.

If the selector only compares note blobs, it will miss cases 3 and 4 entirely.

For the first version, do not treat bundle membership changes as their own stale reason. Keep bundle composition static at selection time and leave "bundle changed underneath accepted gate coverage" for a follow-on phase.

## Why frontmatter is the complication

The current `frontmatter-review` already proves that freshness is not the same as full-text equality:

- frontmatter changes always stale the review
- body changes only stale it when they are large enough to risk title/body misalignment

That policy is reasonable for the bundle, but once frontmatter review is split into gates, different checks want different invalidation rules.

Examples:

- `description-discrimination`
  Mainly depends on `title`, `description`, and sometimes body drift if the note's real scope changed enough that the description is now misleading.

- `title-composability`
  Depends almost entirely on the title.

- `claim-strength`
  Depends on title, and maybe `type` / `status` because the current instruction explicitly exempts some note classes.

- `title-body-alignment`
  Depends on title plus substantive body change.

So the selector cannot keep one policy called `frontmatter-review`. It needs **gate-local invalidation policies**.

## Recommendation: make invalidation policy part of gate metadata

Each gate definition should carry a small machine-readable contract saying what makes prior acceptance stale.

Not full logic in prose. A compact declarative contract.

Example shape:

```yaml
gate_id: frontmatter/title-body-alignment
bundle: frontmatter-review
contract_version: 1
invalidate_on:
  - title
  - body_major_rewrite
body_rewrite_threshold: 0.5
```

Another:

```yaml
gate_id: frontmatter/title-composability
bundle: frontmatter-review
contract_version: 1
invalidate_on:
  - title
```

And for a full-text semantic gate:

```yaml
gate_id: semantic/completeness-boundary-cases
bundle: semantic-review
contract_version: 1
invalidate_on:
  - full_text
```

This is the key design move. The selector should evaluate stale state against the gate's invalidation contract, not against the bundle name.

## Do not use raw gate file hashes as the freshness contract

If gate files become editable standalone artifacts, they will change often:

- wording cleanup
- examples added
- better recommendation phrasing
- metadata normalization

Most of those edits should not invalidate all historical reviews.

So the selector should not say "gate markdown file changed -> stale".

Instead, each gate should expose a small explicit contract surface:

- `gate_id`
- `contract_version`
- invalidation fields / comparator
- thresholds
- maybe severity policy if that affects interpretation

The selector can fingerprint just that contract surface, or simpler: trust `contract_version` and require humans to bump it when the meaning changes.

That keeps "easy to evolve" from turning into "every edit invalidates the world."

## Minimal interim storage model

Markdown remains the canonical inspectable artifact. CSV tables become derived indexes that let the selector avoid reparsing hundreds of files every run.

### 1. Gate definition files

Suggested shape:

```text
kb/instructions/review-gates/
  frontmatter/
    description-discrimination.md
    title-composability.md
    claim-strength.md
    title-body-alignment.md
  prose/
    source-residue.md
    pseudo-formalism.md
    ...
  semantic/
    completeness-boundary-cases.md
    grounding-alignment.md
    internal-consistency.md
```

These are the durable definitions.

### 2. Bundle membership table

Keep bundling separate from gate definition.

Example CSV:

```text
kb/reports/reviews/csv/review_bundles.csv
```

Columns:

- `bundle_id`
- `gate_id`
- `required`
- `order`
- `enabled`

This lets us recompose `frontmatter-review` or `summary-review` later without making the bundle the storage primitive.

### 3. Gate review artifacts

Each accepted gate result should be its own markdown file.

One possible layout:

```text
kb/reports/reviews/gates/{encoded-note-path}/{gate-id}.md
```

The exact path encoding is less important than these properties:

- collision-safe for nested notes
- stable across scripts
- directly mappable from `(note_path, gate_id)`

### 4. Gate review index table

Derived CSV:

```text
kb/reports/reviews/csv/gate_reviews.csv
```

Columns:

- `note_path`
- `gate_id`
- `review_path`
- `accepted_note_sha`
- `accepted_note_commit`
- `accepted_at`
- `acceptance_kind`
- `gate_contract_version`
- `gate_contract_fingerprint`
- `accepted_scope_fingerprint`
- `status`

This is the table the selector should read first.

### 5. Gate definition index table

Derived CSV:

```text
kb/reports/reviews/csv/gate_definitions.csv
```

Columns:

- `gate_id`
- `bundle_id`
- `contract_version`
- `contract_fingerprint`
- `comparator`
- `threshold`
- `enabled`

This avoids opening every gate definition file during selection.

## The missing concept: accepted scope fingerprint

For full-text gates, `accepted_note_sha` is often enough.

For split gates, it is not always enough, because some gates care about only part of the note.

The selector should therefore track both:

- `accepted_note_sha`
- `accepted_scope_fingerprint`

Examples:

- `title-composability`
  Scope fingerprint can be hash(`title`)

- `claim-strength`
  Scope fingerprint can be hash(`title`, `type`, `status`)

- `description-discrimination`
  Scope fingerprint can be hash(`title`, `description`)
  Conservative variant: also include a cheap body summary signal if we learn that large body shifts often invalidate this gate.

- `title-body-alignment`
  Scope fingerprint cannot be just frontmatter. It needs the accepted note blob or accepted body lines because the selector must measure rewrite ratio against the accepted body.

This is the main reason the selector should model comparators explicitly rather than inferring them from `review_type`.

## Comparator primitives are enough for now

We do not need a full rule engine yet. A small fixed set of comparator primitives should cover the first version:

- `full_text_exact`
- `frontmatter_fields_exact`
- `title_exact`
- `title_status_exact`
- `title_and_body_major_rewrite`
- `frontmatter_and_body_major_rewrite`
- `age_threshold`

Each gate chooses one primitive plus parameters.

That is much simpler than embedding arbitrary Python in gate metadata, and it maps cleanly onto the current selector architecture.

## Suggested frontmatter gate policies

These are conservative defaults, not a final ontology:

| Gate | Comparator |
|---|---|
| `description-discrimination` | `frontmatter_fields_exact(title, description)` |
| `title-composability` | `title_exact` |
| `claim-strength` | `title_status_exact(title, type, status)` |
| `title-body-alignment` | `title_and_body_major_rewrite(threshold=0.5)` |

The only risky one is `description-discrimination`. In principle the body can drift while title/description stay fixed, making the description stale. But that is exactly why `title-body-alignment` exists. For a first version, it is acceptable to let that gate carry the body-sensitive invalidation rather than making every frontmatter gate body-sensitive.

That keeps the model legible.

## Selector algorithm at gate level

Given a bundle request like `frontmatter-review`:

1. Load reviewable notes.
2. Load required gates for bundle `frontmatter-review` from `review_bundles.csv`.
3. Load gate contracts for those gates from `gate_definitions.csv`.
4. For each `(note, gate)`:
   - resolve gate review artifact from `gate_reviews.csv`
   - if missing: stale = `missing-gate-review`
   - if gate contract version/fingerprint mismatch: stale = `gate-updated`
   - else evaluate note freshness using the gate comparator
   - if age threshold exceeded: stale = `expired`
5. Emit stale gate records.
6. Optionally collapse stale gate records back into a per-note or per-bundle queue for execution.

That last collapse step is where future bundling belongs. The freshness check itself should stay gate-native.

## Why CSV is enough before SQL

The near-term need is not complex transactions. It is cheap joins across three entities:

- gate definitions
- bundle membership
- accepted gate reviews

CSV is enough if we treat it as a materialized index generated from markdown.

That buys:

- inspectability
- no schema migration burden yet
- cheap selector reads
- a natural later path into SQLite because the tables already exist conceptually

The SQL move becomes necessary when we need one or more of these:

- concurrent writes
- historical gate-review events rather than latest-state only
- multi-hop queries across note -> bundle -> gate -> outcome -> provenance
- richer analytics than current summary tables

Until then, markdown + derived CSV is a reasonable midpoint.

## Consequences for the current selector refactor

If we expect gate splitting soon, the selector refactor should avoid baking in these assumptions:

1. `review_type` uniquely identifies one comparator policy.
2. one review file is the unit of freshness.
3. `last-accepted-note-sha` is always the right stale baseline.

Instead the seams should be:

- inventory of notes
- inventory of required review units
- gate contract lookup
- accepted-state lookup
- comparator evaluation
- optional bundling / rendering

That architecture still works for today's bundle-sized review files. It also works once the unit becomes `(note, gate)`.

## Recommendation

Design the selector around **gate-local freshness contracts** now, even if the first implementation still reads today's bundle-level review files.

Concretely:

- add an abstraction for "review unit" that is not hardcoded to review type
- make comparator policy attach to the review unit, not the CLI argument
- introduce explicit contract-version / comparator metadata
- introduce derived CSV tables for gate definitions, bundle membership, and accepted gate reviews

If we do not do this, the selector will need a second structural rewrite as soon as the monolithic reviews are decomposed.
