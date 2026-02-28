---
description: Taxonomy overview — the base types table and migration from old flat types; global field definitions, status, and traits live in types/note.md
type: spec
areas: [document-system]
status: current
---

# Document classification

See [document-types-should-be-verifiable](./document-types-should-be-verifiable.md) for the design rationale. See [note base type](../../types/note.md) for the global fields, status ladder, traits, and design principles that all structured types inherit.

## Base types

A document has exactly one type. [text](../../types/text.md) has no frontmatter and no requirements. Every other type extends [note](../../types/note.md) — it defines the shared fields (description, status, traits, areas) that all structured documents carry.

The `type` field is a free-form string. The table below lists the common values; directory-scoped `types/` folders document the structural expectations for each.

| Base type | Structural test | Verifiability |
|-----------|----------------|---------------|
| `text` | No frontmatter — raw capture | Always valid |
| `note` | Has frontmatter with description | Check for frontmatter, description field |
| `spec` | Implementation-ready detail; has Design/Implementation sections | Check for sections |
| `review` | Examines specific existing code; has Findings; dated | Check for code refs, date |
| `index` | Primarily navigational links | Check link density |
| `adr` | Architecture decision record; has Context/Decision/Consequences | Check for ADR sections |
| `structured-claim` | Title is an assertion; has Evidence and Reasoning sections | Check for `## Evidence` and `## Reasoning` headings |

`structured-claim` extends `note` with required argument sections: `## Evidence`, `## Reasoning`, and optionally `## Caveats`. It represents a fully developed argument — the [Toulmin scaffold](./claim-notes-should-use-toulmin-derived-sections-for-structured-argument.md) applied to a claim-titled note. The promotion path is `note` → `structured-claim`: when a note's argument matures enough to fill Evidence/Reasoning sections, it earns the type.

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
- [note base type](../../types/note.md) — defines the global fields, status ladder, traits, and design principles
- [text root type](../../types/text.md) — the empty root type: no frontmatter, always valid
- [document-types-should-be-verifiable](./document-types-should-be-verifiable.md) — design rationale for verifiable types
- [directory-scoped-types-are-cheaper-than-global-types](./directory-scoped-types-are-cheaper-than-global-types.md) — the economic argument for thin global types

Topics:
- [document-system](./document-system.md)
