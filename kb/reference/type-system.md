---
description: Taxonomy overview — the base types table and migration from old flat types; global field definitions, status, and traits live in kb/types/note.md
type: note
tags: [type-system]
status: current
---

# Document classification

See [note base type](../types/note.md) for the global fields, status ladder, traits, and design principles that all structured types inherit.

## Base types

A document has exactly one type. [text](../types/text.md) has no frontmatter and no requirements. Every other type extends [note](../types/note.md) — it defines the shared fields (description, status, traits, tags) that all structured documents carry.

The `type` field is a free-form string. The table below lists the common values; directory-scoped `types/` folders document the structural expectations for each.

| Base type | Structural test | Verifiability |
|-----------|----------------|---------------|
| `text` | No frontmatter — raw capture | Always valid |
| `note` | Has frontmatter with description | Check for frontmatter, description field |
| `spec` | Implementation-ready detail; has Design/Implementation sections | Check for sections |
| `review` | Examines specific existing code; has Findings; dated | Check for code refs, date |
| `index` | Primarily navigational links | Check link density |
| `adr` | Architecture decision record; has Context/Decision/Consequences | Check for ADR sections |
| `structured-claim` | Developed argument; has Evidence and Reasoning sections | Check for `## Evidence` and `## Reasoning` headings |
| `related-system` | External-system review; has fixed comparison sections and `last-checked` | Check required sections and field |
| `source-review` | Processed source artifact under `kb/sources/` | Check source-specific structure in the source collection |

`structured-claim` extends `note` with required argument sections: `## Evidence`, `## Reasoning`, and optionally `## Caveats`. It represents a fully developed argument scaffold applied to a claim-titled note. The promotion path is `note` → `structured-claim`: when a note's argument matures enough to fill Evidence/Reasoning sections, it earns the type.

Traits are a separate axis from type. They do not define structure; they declare semantic review expectations. Examples: `title-as-claim` routes claim-quality gates, `definition` marks term-pinning notes, and `has-comparison` / `has-external-sources` describe reusable review-relevant properties that can appear across multiple types.

## Migration from old flat types

| Old type | New encoding |
|----------|-------------|
| `design` | `note` (was subject matter, not structure) |
| `insight` | `structured-claim` (developed argument) or `note` (claim title, free-form body) |
| `analysis` | `note` + `has-comparison` |
| `research` | `note` + `has-external-sources` |
| `comparison` | `note` + `has-comparison` |

---

Relevant Notes:

- [note base type](../types/note.md) — defines the global fields, status ladder, traits, and design principles
- [text root type](../types/text.md) — the empty root type: no frontmatter, always valid
- [012-types-for-structure-traits-for-review](./adr/012-types-for-structure-traits-for-review.md) — decision: structural types and review traits are separate axes
- [015-standardize-authored-type-definitions-on-json-schema](./adr/015-standardize-authored-type-definitions-on-json-schema.md) — decision: the current authored type-definition format
