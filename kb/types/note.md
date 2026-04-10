---
description: Base type for all structured documents — defines the global fields (description, status, traits, tags), status ladder, trait vocabulary, and design principles that all typed documents inherit
type: spec
tags: [document-system]
status: current
---

# note

The base structured type. A markdown file with YAML frontmatter containing at least a `description` field.

All other typed documents extend `note` — they inherit these global fields and add their own structural requirements. [text](./text.md) stands outside the hierarchy (no frontmatter = no fields).

See [document-types-should-be-verifiable](../notes/document-types-should-be-verifiable.md) for the design rationale. See [document-classification](../reference/type-system.md) for the taxonomy overview of all types.

## Structural test

- File starts with `---` (YAML frontmatter delimiter)
- Frontmatter contains a `description` field with a non-empty value

## Global fields

These fields are available to all types that extend `note`.

| Field | Required | Constraints |
|-------|----------|------------|
| `description` | Yes | Max 200 chars, must discriminate this note from similar ones. A retrieval filter, not a summary. |
| `type` | No | Free-form string identifying the document type. Defaults to `note` if absent. |
| `traits` | No | Array of independently checkable properties (see Traits below) |
| `tags` | No | Array of tag names for navigation — each generates a link to the tag's index page |
| `status` | No | Commitment level (see Status below). Defaults to `seedling`. |

### description

The most important field. It's a retrieval filter, not a summary — it helps agents decide whether to load the full document. A good description answers "why THIS document?" not "what is this document about?"

### type

A free-form string. Convention establishes common values (`note`, `structured-claim`, `spec`, `review`, `index`, `adr`, `related-system`, `source-review`), but the field is not validated against an enum. Directory-scoped `types/` folders document the structural expectations for each value. New type values can be introduced by adding a template and companion YAML definition in the relevant `types/` directory.

## Status

Status tracks **commitment** — whether a document has been reviewed and endorsed. It is orthogonal to type: a document can be structurally complete while still being provisional.

| Status | Meaning |
|--------|---------|
| `seedling` | Provisional — we haven't decided to keep this. May be pruned. |
| `current` | Endorsed — reviewed and accepted into the KB. |
| `speculative` | Exploratory — deliberately kept as open conjecture. |
| `outdated` | Superseded — kept for reference but no longer the active view. |

The initial status is `seedling`, not "draft" — a draft implies commitment to develop it, while a seedling may simply be pruned.

[text](./text.md) files have implicit `status: seedling`. When a text file gains frontmatter (promotion to `note`), status should be set explicitly. `/cp-skill-connect` promotes structure (`text` → `note`) but preserves provisionality by setting `status: seedling`, not `status: current`. Human review flips the status to `current`.

**Finding seedlings that need review:**
```bash
rg '^status: seedling' kb/notes/
```

## Traits

Traits are independently checkable properties. A document can have zero or more traits regardless of its type. Stored in the `traits` frontmatter field as a list. Traits do not change structural validation; they route semantic review expectations.

| Trait | What it asserts | Verifiability |
|-------|----------------|---------------|
| `title-as-claim` | The title is a proposition that can be true or false | Review gate checks whether the title is actually claim-shaped |
| `definition` | The note is pinning a term's meaning rather than making a broader argument | Check location/scope and review definition-specific expectations |
| `has-comparison` | Structured evaluation of alternatives (tables, option lists) | Grep for comparison tables |
| `has-external-sources` | References material outside the project | Grep for URLs/citations |
| `has-implementation` | Contains code sketches or concrete API proposals | Grep for code blocks with API surface |

`title-as-claim` is the replacement for the old idea of a dedicated "claim" trait. Claim-style titles remain available to any note; `structured-claim` is the stronger structural type for notes that also commit to Evidence/Reasoning sections.

## Design principles

**Types are structural.** A distinction earns type status only when it changes required fields or sections. Subject matter belongs in tags; semantic expectations belong in traits and review gates.

**Types are verifiable.** Each type and trait asserts a structural property you can check. The question is "what structural property am I asserting?" not "what is this about?" Subject matter belongs in `tags`.

**Types mature through constraining.** Content can start as [text](./text.md) and get promoted to `note` by adding frontmatter, then to more specific types as structure develops. A text file that persists without promotion is a candidate for pruning.

**Status is orthogonal to type.** Structure and commitment are independent axes. A document can be structurally complete and connected while still being a seedling — meaning "we haven't decided to keep this."

## Frontmatter example

```yaml
---
description: Storing an LLM output collapses a distribution to a point
type: note
traits: [has-comparison]
tags: [index]
status: seedling
---
```

---

Relevant Notes:

- [text](./text.md) — the root type that note extends; promotion from text to note is the first structural step
- [document-classification](../reference/type-system.md) — taxonomy overview: the base types table and migration history
- [document-types-should-be-verifiable](../notes/document-types-should-be-verifiable.md) — design rationale for verifiable types
