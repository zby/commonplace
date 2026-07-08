---
description: Types define structural requirements checked by validation; traits route semantic review gates; the traits-only semantic boundary is amended by ADR-038/041, which make both contracts conformance gates
type: ../types/adr.md
tags: []
status: accepted
---

# 012-types-for-structure-traits-for-review

**Status:** accepted
**Date:** 2026-04-08

The structural core of this ADR remains current: validation is deterministic and structural, frontmatter `type` is authoritative for artifact identity, and traits route trait-scoped review gates. Its boundary claim — that semantic review expectations attach *only* to traits, so "types are structural" full stop — was amended by [ADR-038](./038-type-conformance-reviews-use-the-type-spec-as-the-gate.md) and [ADR-041](./041-collection-conformance-reviews-use-collection-md-as-the-gate.md): a type spec's authoring instructions are now semantically enforced through a type-conformance review pair, and a collection's `COLLECTION.md` contract through a collection-conformance pair. Types carry semantic value alongside structure; traits remain an additional, opt-in semantic axis rather than the only one. Read the boundary test below ("does it change structure? → type; does it change review expectations? → trait") in that light: it still decides where a *new distinction* lives, but no longer implies that types have no reviewed semantics.

## Context

The type system had accumulated inconsistencies: `related-system` template said `type: note` despite being a distinct artifact kind, the validator hard-coded type profiles while docs said "add a template, get a type," and there was no principled boundary between what should be a type vs a trait vs a directory convention. Semantic checks (description quality, title composability) lived in `/validate` alongside structural checks, blurring the validation/review boundary.

There was also a deeper identity problem: artifact kind was being inferred from three competing signals at once:

- frontmatter `type`
- directory-local `types/` templates
- path-based collection conventions and exemptions

That made it unclear whether moving a file between directories changed its type or only its storage location. The decision needed to separate artifact identity from definition lookup and placement rules.

## Decision

**Types are structural.** A type defines required sections, fields, and templates. The validator checks these deterministically. A distinction is a type only if it changes required structure beyond `note`.

**Traits route semantic review.** A trait declares which review gates apply. The gate frontmatter gains `requires_trait`; review tooling filters gates by checking the note's explicit frontmatter `traits:` field. Current trait-gated gates: `claim-strength`, `title-composability`, `explanatory-reach` (all require `title-as-claim`). One new gate: `frontmatter/title-as-claim`. All other gates are universal. Type-specific review gates can also declare `requires-type` when a gate only applies to one artifact type, such as a definition-only or related-system-only gate.

**Validation is purely structural.** No semantic checks in the validator. Description quality, composability, and other judgment calls live in review gates.

**Frontmatter `type` is authoritative for library artifact identity.** Directory-local `types/` directories remain load-bearing, but they scope definition lookup rather than replacing the type system. Path and collection placement stay separate from type identity.

**Type definitions are two files.** Each type has `{type}.template.md` (prose template for agents) plus `{type}.instructions.md` (how to fill it in), and a machine-readable schema in its `types/` directory. ADR-015 later standardized that schema as JSON Schema in YAML syntax. The schema replaces the validator's hard-coded `TYPE_HEADINGS` map.

**Bare type names.** Qualified canonical ids (e.g. `notes.related-system`) deferred — bare names are unambiguous today, and qualification would add readability cost before it solves a real collision.

**`core.claim` dropped.** Its semantic expectations belong to the `title-as-claim` trait, not a type.

## Consequences

**Easier:**
- Clear boundary for new distinctions: does it change structure? → type. Does it change review expectations? → trait.
- Validator reads type definitions from schemas rather than a hard-coded map — adding a type no longer requires code changes.
- Review gates can be selectively applied — no more prose exemption lists inside gate definitions.
- `related-system` becomes a real type with `type: related-system` in its template.
- Moving a file no longer silently changes its artifact kind. Type identity comes from frontmatter; directories determine where definitions are found and where artifacts belong.

**Harder:**
- Every type needs a companion machine-readable schema written alongside the prose template.
- Authors must declare traits explicitly in frontmatter (implied traits from types deferred).
- Existing `structured-claim` notes and existing plain notes with claim-shaped titles need `title-as-claim` added to their `traits:` field.

---

Relevant Notes:

- [available types](../available-types.md) — extends: adds the type/trait boundary test
- [type-loading](../type-loading.md) — the shipped loading model that implements the structural side of this decision
- [ADR-038: type-conformance reviews use the type spec as the gate](./038-type-conformance-reviews-use-the-type-spec-as-the-gate.md) — amended-by: makes the type contract itself semantically reviewable
- [ADR-041: collection-conformance reviews use COLLECTION.md as the gate](./041-collection-conformance-reviews-use-collection-md-as-the-gate.md) — amended-by: extends the same enforcement to the collection contract surface
