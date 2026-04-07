# Review integration with types and traits

How the review system should consume types and traits after the type-system rationalization.

## Current state

All gates apply universally to all notes.

- The selector (`review_target_selector.py`) picks stale `(note, gate)` pairs based on SHA freshness, with no awareness of note type or traits.
- Direct note-local bundle runs (`create_review_run.py`, `run_review_bundle.py`) expand bundles to gate ids with no trait filtering.

Every note gets every gate unless a human manually narrows the gate list.

## Design

### Gate applicability

Gates fall into two categories:

**Universal gates** — apply to every note regardless of type or traits. This is the majority: prose, sentence, structural, accessibility, complexity gates, plus most frontmatter and semantic gates. These check writing quality, not content-kind.

**Trait-gated gates** — only apply when the note carries a specific trait. In the initial migration, traits are read explicitly from frontmatter. Type-implied traits are deferred.

### Mechanism

Gate frontmatter gains an optional `requires_trait` field:

```yaml
---
gate_id: frontmatter/title-as-claim
requires_trait: title-as-claim
---
```

If `requires_trait` is absent, the gate is universal. If present, the review tooling must check whether the note carries that trait before including the gate.

### Trait computation

Initial migration rule: review tooling reads traits from the note's frontmatter `traits:` field. That's it.

This means the migration must bulk-add `title-as-claim` to existing `structured-claim` notes and to existing plain `note` files whose titles are already claim-shaped. The review system does not infer that trait from `type: structured-claim` yet.

Type-implied traits are a future optimization. They would save authors from listing traits that their type always carries, but they are not part of the first implementation pass.

### Gate changes

#### New gate: `frontmatter/title-as-claim`

Requires trait: `title-as-claim`

Checks one thing: **is this title actually a proposition?** The title must read as an assertion that can be true or false. Topic labels ("knowledge management"), artifact names ("LACP"), and category headers ("learning theory index") are not claims. If the title is not a proposition, the note should not carry the `title-as-claim` trait.

This gate verifies the trait's promise — it catches misapplied traits, not weak claims.

#### Updated: `frontmatter/claim-strength`

Gains `requires_trait: title-as-claim`. The gate already only makes sense for claims — its current exemption list (specs, frameworks, definitional notes, indexes, exploratory seedlings) is exactly the set of notes that would not carry the trait. The trait-gating replaces the prose exemption list with a machine-readable filter.

#### Trait-gated: `semantic/explanatory-reach`

Requires trait: `title-as-claim`

"Does this explain *why*, not just *what*?" is a claim-quality check. Indexes, definitions, related-system reviews, and ADRs are not trying to explain a mechanism — applying this gate to them produces false positives, not useful signal.

#### Trait-gated: `frontmatter/title-composability`

Requires trait: `title-as-claim`

Composability ("does the title work as `since [title]...`?") only matters when the title is a claim meant to be linked as an inline prose fragment. Index titles ("learning theory"), artifact names ("LACP"), and definition titles don't need to pass this test.

#### Complete gate inventory

Every gate reviewed against the trait-gating criterion. Gates not listed in the trait-gated sections above are universal.

**Frontmatter (4 gates)**

| Gate | Applicability | Rationale |
|---|---|---|
| `claim-strength` | `title-as-claim` | Only makes sense for claims; prose exemption list replaced by trait filter |
| `title-as-claim` (new) | `title-as-claim` | Verifies the trait's promise: is the title actually a proposition? |
| `description-discrimination` | Universal | Every note has a description |
| `title-body-alignment` | Universal | Checks both claim drift and scope drift — scope drift applies to any note |
| `title-composability` | `title-as-claim` | See above |

**Semantic (4 gates)**

| Gate | Applicability | Rationale |
|---|---|---|
| `completeness-boundary-cases` | Universal | Any note with enumerations, frameworks, or taxonomies — not claim-specific |
| `explanatory-reach` | `title-as-claim` | See above |
| `grounding-alignment` | Universal | Applies to internal and external source references alike |
| `internal-consistency` | Universal | Any note can contradict itself |

**Prose (9 gates)**

| Gate | Applicability | Rationale |
|---|---|---|
| `anthropomorphic-framing` | Universal | Writing quality — any note can misattribute agency to models |
| `bridge-paragraph-duplication` | Universal | Structural writing issue independent of content kind |
| `confidence-miscalibration` | Universal | Any note can present speculation as established or vice versa |
| `orphan-references` | Universal | Any note can have unsourced empirical claims |
| `proportion-mismatch` | Universal | References "core claim" but really checks section balance — applies to any structured note |
| `pseudo-formalism` | Universal | Decorative notation can appear in any note |
| `redundant-restatement` | Universal | Section-level restatement is a writing issue |
| `source-residue` | Universal | Any generalized note can leak source-domain framing |
| `unbridged-cross-domain` | Universal | Cross-domain evidence transfer is a general concern |

**Sentence (6 gates)**

| Gate | Applicability | Rationale |
|---|---|---|
| `clause-packing` | Universal | Sentence-level writing quality |
| `concept-attribution` | Universal | Any note can misattribute concepts to linked notes |
| `framing-mismatch` | Universal | Sentence framing can misdirect in any note |
| `misleading-link-text` | Universal | Any note with links |
| `parsing-ambiguity` | Universal | Syntactic clarity |
| `stock-phrases` | Universal | LLM-pattern filler can appear in any note |

**Structural (3 gates)**

| Gate | Applicability | Rationale |
|---|---|---|
| `bullet-capitalization` | Universal | Formatting |
| `compound-bullet` | Universal | Formatting |
| `general-before-specific` | Universal | Section ordering |

**Accessibility (4 gates)**

| Gate | Applicability | Rationale |
|---|---|---|
| `jargon-persistence` | Universal | KB vocabulary can appear in any note |
| `notation-opacity` | Universal | Formal notation can appear in any note |
| `undefined-terms` | Universal | Terms need glossing regardless of note kind |
| `unidentified-references` | Universal | Named systems need identification regardless |

**Complexity (4 gates)**

| Gate | Applicability | Rationale |
|---|---|---|
| `claim-to-section-ratio` | Universal | References "claims" but really checks whether sections justify their existence |
| `connection-inflation` | Universal | Relevant Notes inflation can happen in any note |
| `could-be-a-paragraph` | Universal | Over-complex structure is independent of content kind |
| `framework-decoration` | Universal | Decorative frameworks can appear anywhere |

### Summary

Of 30 current gates:
- **27 universal** — no change needed
- **3 trait-gated** (`claim-strength`, `title-composability`, `explanatory-reach`) — gain `requires_trait: title-as-claim`

Plus 1 new gate: `frontmatter/title-as-claim` (trait-gated) — verifies the trait's promise.

Net result: 1 new gate, 3 updated, 27 unchanged.

### Current state: only one trait matters for review

All current gates are either universal or require `title-as-claim`. No existing gate fires on `has-comparison`, `has-external-sources`, `has-implementation`, or `definition`. Those traits exist in the vocabulary but have no review-system consumers yet.

This means the initial migration only needs to check one trait value. The general `requires_trait` mechanism is still the right design (it extends naturally when future gates need other traits), but the first implementation is simple: read `traits:` from frontmatter, check whether `title-as-claim` is present.

### Where trait filtering lives

There are two entry points that need note-aware applicability:

1. **Direct note-local bundle runs** — `create_review_run.py` and `run_review_bundle.py`
2. **Sweep selection** — `review_target_selector.py`

Do not overload the current `resolve_to_gate_ids(args, gates_dir)` helper with note-aware filtering. Its job is just bundle expansion: requested names in, gate ids out.

Instead, split the logic into two steps:

1. requested gate expansion: bundle name → gate ids
2. note-aware applicability filtering: `(note_path, gate_ids)` → applicable gate ids

Implement the second step in a shared helper in `resolve_gates.py`. That helper:

- reads gate frontmatter for `requires_trait`
- reads note frontmatter for `traits`
- excludes non-applicable trait-gated gates

Then:

- direct note-local bundle runs call the shared helper once for the target note
- the selector calls the same helper inside its per-note loop when computing stale `(note, gate)` pairs

This applies to both bundling directions:

- **Note-local bundle** (multiple gates on one note) — the shared note-aware applicability helper filters which gates apply to the note. A note without `title-as-claim` skips `claim-strength`, `title-composability`, `explanatory-reach`, and the new `title-as-claim` gate.
- **Gate sweep** (one gate across many notes) — the selector filters which notes are eligible for the gate. A sweep of `claim-strength` only returns notes that carry `title-as-claim`.

Everything downstream (review runs, write_gate_review, acceptance, ack) stays unchanged.

### Sweep scope

The selector should discover frontmatter-bearing notes recursively under `kb/notes/**`, not just top-level `kb/notes/*.md`.

Without recursive discovery, definitions and related-system reviews stay outside sweep scope, which makes trait-gating parity checks misleading.

### Schema impact

The SQLite schema does not need to change. Trait-gating is a selection-time filter, not a storage concern. A gate review for a `(note, gate)` pair is still a gate review — whether the gate was applicable is the selector's job, not the database's.

## What this does NOT change

- Gate definitions remain markdown files in `review-gates/`
- The review execution flow (create run → review → write → finalize) is unchanged
- Acceptance and ack semantics are unchanged
- Staleness computation is unchanged
- Bundle organization (gates grouped by lens) is unchanged
- Universal gates (the large majority) are completely unaffected

## Future possibilities

If more trait-gated gates emerge, the `requires_trait` mechanism extends naturally. Some possibilities:

- A `definition` trait could gate a future term-precision gate
- `has-comparison` could gate a comparison-quality gate (currently comparison quality is checked by `notes.related-system`'s Curiosity Pass section, not by a standalone gate)
- `has-implementation` could gate a code-quality gate

The `definition` trait should be added to the vocabulary now — notes in `kb/notes/definitions/` should carry `traits: [definition]` during migration. The gate can come later as the first extension that proves the `requires_trait` mechanism generalizes beyond `title-as-claim`.

Other trait-gated gates are not needed now — build them when the review system reveals the need.

## Migration order

Within the broader type-system migration:

1. Bulk-add explicit `title-as-claim` traits to existing `structured-claim` notes and claim-shaped plain `note` files
2. Add a shared note-aware applicability helper used by both direct bundle runs and the selector
3. Expand sweep note discovery to recurse under `kb/notes/**`
4. Write the `frontmatter/title-as-claim` gate definition
5. Add `requires_trait: title-as-claim` to `claim-strength`, `title-composability`, `explanatory-reach`
6. Run trait-gated gates on notes that carry `title-as-claim` in their frontmatter traits

---

Workshop context:

- [design.md](./design.md) — types for structure, traits for semantic review routing
- [decision-criteria.md](./decision-criteria.md) — type vs trait boundary test
- [resolution-algorithm.md](./resolution-algorithm.md) — overall type/trait resolution steps; implied traits deferred from the initial migration
