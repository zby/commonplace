---
description: Types define structural requirements checked by validation; traits route semantic review gates; type definitions split into prose template and machine-readable YAML
type: adr
tags: [document-system]
status: proposed
---

# 012-types-for-structure-traits-for-review

**Status:** proposed
**Date:** 2026-04-07

## Context

The type system had accumulated inconsistencies: `related-system` template said `type: note` despite being a distinct artifact kind, the validator hard-coded type profiles while docs said "add a template, get a type," and there was no principled boundary between what should be a type vs a trait vs a directory convention. Semantic checks (description quality, title composability) lived in `/validate` alongside structural checks, blurring the validation/review boundary.

## Decision

**Types are structural.** A type defines required sections, fields, and templates. The validator checks these deterministically. A distinction is a type only if it changes required structure beyond `note`.

**Traits route semantic review.** A trait declares which review gates apply. The gate frontmatter gains `requires_trait`; review tooling filters gates by checking the note's explicit frontmatter `traits:` field. Current trait-gated gates: `claim-strength`, `title-composability`, `explanatory-reach` (all require `title-as-claim`). One new gate: `frontmatter/title-as-claim`. All other gates are universal.

**Validation is purely structural.** No semantic checks in the validator. Description quality, composability, and other judgment calls live in review gates.

**Type definitions are two files.** Each type has `{type}.md` (prose template for agents) and `{type}.yaml` (machine-readable definition for the validator) in its `types/` directory. The YAML replaces the validator's hard-coded `TYPE_HEADINGS` map.

**Bare type names.** Qualified canonical ids (e.g. `notes.related-system`) deferred — bare names are unambiguous today.

**`core.claim` dropped.** Its semantic expectations belong to the `title-as-claim` trait, not a type.

## Consequences

**Easier:**
- Clear boundary for new distinctions: does it change structure? → type. Does it change review expectations? → trait.
- Validator reads type definitions from YAML — adding a type no longer requires code changes.
- Review gates can be selectively applied — no more prose exemption lists inside gate definitions.
- `related-system` becomes a real type with `type: related-system` in its template.

**Harder:**
- Every type needs a companion `.yaml` file written alongside the prose template.
- Authors must declare traits explicitly in frontmatter (implied traits from types deferred).
- Existing `structured-claim` notes and existing plain notes with claim-shaped titles need `title-as-claim` added to their `traits:` field.

---

Relevant Notes:

- [document-types-should-be-verifiable](../document-types-should-be-verifiable.md) — strengthened: types are purely structural, making verifiability the defining criterion
- [deterministic-validation-should-be-a-script](../deterministic-validation-should-be-a-script.md) — extends: the "soft oracle stays in skill" tier is removed; all semantic checks move to review
- [document-classification](../document-classification.md) — extends: adds the type/trait boundary test
- [type-system-rationalization workshop](../../work/type-system-rationalization/README.md) — source: full design exploration behind this decision
