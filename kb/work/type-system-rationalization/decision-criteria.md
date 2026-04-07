# Decision criteria: type vs trait

When a new artifact distinction emerges, this test determines whether it should be a type or a trait.

## The rule

**Type** = the distinction changes required structure (sections, fields, template).

**Trait** = the distinction changes semantic review expectations without changing structure.

A type says "this document must have these structural affordances." A trait says "review this document with these semantic expectations." Types are checked by the deterministic validator. Traits route semantic review gates.

## The test

Given a candidate distinction X:

1. Does X require sections, fields, or a template that `core.note` does not have?
   - Yes → X is a type. Define it in the relevant `types/` directory.
   - No → go to 2.

2. Does X change which semantic review gates should fire, or what those gates should expect?
   - Yes → X is a trait. Add it to the traits vocabulary.
   - No → X is not a real distinction yet. It may be a tag, a convention, or premature.

## Why this works

The type system serves two independent systems:

- **Deterministic validation** — checks structure. Needs to know required headings, required fields, allowed field vocabularies. These are structural properties that can be verified symbolically.
- **Semantic review** — checks content quality. Needs to know what expectations to apply: is the title a claim? Is there a comparison that should be substantive? Are external sources grounded correctly?

Types and traits map cleanly to these two systems. Mixing structural and semantic concerns in a single signal (as `core.claim` attempted) forces awkward justifications — "this type is structurally identical to its parent but semantically different" — and complicates the inheritance model.

## Applying the test to current distinctions

### Types (structural)

| Distinction | Required structure beyond `core.note` | Type id |
|---|---|---|
| structured-claim | `## Evidence`, `## Reasoning` sections | `notes.structured-claim` |
| ADR | `## Context`, `## Decision`, `## Consequences`; decision-status vocabulary | `notes.adr` |
| index | navigational structure, link density, context phrases | `notes.index` |
| related-system review | `## Core Ideas`, `## Comparison`, `## Borrowable Ideas`, `## Curiosity Pass`, `## What to Watch`; `last-checked` field | `notes.related-system` |
| source-review | source-specific required sections | `sources.source-review` |

### Traits (semantic review routing)

| Distinction | Review gates it triggers | Trait name |
|---|---|---|
| Title functions as a claim | claim-strength, title-body-alignment, stricter composability | `title-as-claim` |
| Contains a comparison | comparison quality (substantive, honest, dimensional) | `has-comparison` |
| References external sources | grounding-alignment (attribution accuracy, inference validity) | `has-external-sources` |
| Contains code/API proposals | (existing, not yet gate-routed) | `has-implementation` |
| Defines a term | term precision, boundary coverage, usage consistency | `definition` |

### The `core.claim` case

The earlier workshop design proposed `core.claim` as a type that is structurally identical to `core.note` but semantically distinct. Under this decision criterion, that fails the test: no structural difference → not a type.

The semantic expectations that `core.claim` was meant to carry (claim-strength review, stricter title-body alignment) belong to the `title-as-claim` trait instead. A `core.note` with `title-as-claim` gets exactly the review scrutiny that `core.claim` was designed for, without thickening the global type layer.

This also simplifies inheritance. `notes.structured-claim` no longer needs to extend a phantom `core.claim` — it extends `core.note` directly. In the initial migration, these notes also get explicit `traits: [title-as-claim]` in frontmatter. The structural requirement (Evidence/Reasoning sections) comes from the type; the semantic expectation (claim-strength review) comes from the trait.

## Type/trait composition

Some types and traits compose naturally — `notes.structured-claim` pairs with `title-as-claim`, and `notes.related-system` pairs with `has-comparison` and `has-external-sources`.

In the initial migration, this composition is expressed explicitly in frontmatter so the review system can stay simple. If the system later adds type-implied traits, the composition can become automatic without changing the boundary test in this note.

## Boundary cases

**What if a distinction needs both structure and review routing?** That's a type plus one or more traits. `notes.related-system` requires specific sections (type) and pairs naturally with comparison-oriented traits. No conflict — types and traits compose.

**What if a structural requirement is very lightweight — just one optional section?** Prefer a trait unless the section is truly required (validator should reject its absence). If the section is "recommended but not enforced," that's review guidance, not structure.

**What if a trait eventually develops required structure?** Promote it to a type. `has-claim` → `structured-claim` already happened once. The promotion is: add a template to `types/`, define required sections, update the validator. The trait may persist alongside the type as an explicit frontmatter trait during migration, and could become implied later if tooling grows that capability.

---

Workshop context:

- [design.md](./design.md) — the broader type system design; this note refines the "when is something a type?" question that design.md left open
- [current-state.md](./current-state.md) — inventories the inconsistencies this criterion helps resolve (especially inconsistency 1: `related-system` template encoding `type: note`)
- [resolution-algorithm.md](./resolution-algorithm.md) — the resolver consumes types for structural validation; initial review routing reads explicit frontmatter traits
