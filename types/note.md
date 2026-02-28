---
description: Base type for all structured documents — defines the global fields (description, status, traits, areas), status ladder, traits system, and design principles that all typed documents inherit
type: spec
areas: [document-system]
status: current
---

# note

The base structured type. A markdown file with YAML frontmatter containing at least a `description` field.

All other typed documents extend `note` — they inherit these global fields and add their own structural requirements. [text](./text.md) stands outside the hierarchy (no frontmatter = no fields).

See [document-types-should-be-verifiable](../kb/notes/document-types-should-be-verifiable.md) for the design rationale. See [document-classification](../kb/notes/document-classification.md) for the taxonomy overview of all types.

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
| `areas` | No | Array of area index names this document belongs to |
| `status` | No | Commitment level (see Status below). Defaults to `seedling`. |

### description

The most important field. It's a retrieval filter, not a summary — it helps agents decide whether to load the full document. A good description answers "why THIS document?" not "what is this document about?"

### type

A free-form string. Convention establishes common values (`note`, `structured-claim`, `spec`, `review`, `index`, `adr`), but the field is not validated against an enum. Directory-scoped `types/` folders document the structural expectations for each value. New type values can be introduced by adding a template to the relevant `types/` directory.

## Status

Status tracks **commitment** — whether a document has been reviewed and endorsed. It is orthogonal to type: a document can be structurally complete while still being provisional.

| Status | Meaning |
|--------|---------|
| `seedling` | Provisional — we haven't decided to keep this. May be pruned. |
| `current` | Endorsed — reviewed and accepted into the KB. |
| `speculative` | Exploratory — deliberately kept as open conjecture. |
| `outdated` | Superseded — kept for reference but no longer the active view. |

The initial status is `seedling`, not "draft" — a draft implies commitment to develop it, while a seedling may simply be pruned.

[text](./text.md) files have implicit `status: seedling`. When a text file gains frontmatter (promotion to `note`), status should be set explicitly. `/connect` promotes structure (`text` → `note`) but preserves provisionality by setting `status: seedling`, not `status: current`. Human review flips the status to `current`.

**Finding seedlings that need review:**
```bash
rg '^status: seedling' kb/notes/
```

## Traits

Traits are independently checkable properties. A document can have zero or more traits regardless of its type. Stored in the `traits` frontmatter field as a list.

| Trait | What it asserts | Verifiability |
|-------|----------------|---------------|
| `has-comparison` | Structured evaluation of alternatives (tables, option lists) | Grep for comparison tables |
| `has-external-sources` | References material outside the project | Grep for URLs/citations |
| `has-implementation` | Contains code sketches or concrete API proposals | Grep for code blocks with API surface |

> **Retired:** `has-claim` was replaced by the `structured-claim` type. Claim-style titles remain a convention for any note (see [title-as-claim](../kb/notes/title-as-claim-enables-traversal-as-reasoning.md)); developed arguments use `type: structured-claim` instead of a trait.

## Design principles

**Types are fuzzy.** They are assigned by agents and humans, not compilers. The system must tolerate misclassification — nothing breaks if a type or trait is wrong. Types are search aids, not enforcement boundaries.

**Types are verifiable.** Each type and trait asserts a structural property you can check. The question is "what structural property am I asserting?" not "what is this about?" Subject matter belongs in `areas`.

**Types mature through stabilisation.** Content can start as [text](./text.md) and get promoted to `note` by adding frontmatter, then to more specific types as structure develops. A text file that persists without promotion is a candidate for pruning.

**Status is orthogonal to type.** Structure and commitment are independent axes. A document can be structurally complete and connected while still being a seedling — meaning "we haven't decided to keep this."

## Frontmatter example

```yaml
---
description: Storing an LLM output collapses a distribution to a point
type: note
traits: [has-comparison]
areas: [index]
status: seedling
---
```

---

Relevant Notes:
- [text](./text.md) — the root type that note extends; promotion from text to note is the first structural step
- [document-classification](../kb/notes/document-classification.md) — taxonomy overview: the base types table and migration history
- [document-types-should-be-verifiable](../kb/notes/document-types-should-be-verifiable.md) — design rationale for verifiable types

Topics:
- [document-system](../kb/notes/document-system.md)
