# Resolution algorithm

How tooling resolves a document's type and traits to determine which validation rules and review gates apply.

## Current design

With qualified canonical ids deferred, resolution is simpler: bare type names are unambiguous, and each type name maps to exactly one definition file in a known location.

## Inputs

For a given file:

- repo-relative path
- parsed frontmatter (if any)

## Resolution steps

### 1. Determine type

If the file has no frontmatter:

- type is `text`

If the file has frontmatter but no explicit `type` field:

- type is `note`

If it has a `type` field:

- use the bare value directly: `note`, `structured-claim`, `adr`, `index`, `related-system`, `source-review`, etc.

### 2. Locate type definition

Each bare type name maps to two files — a prose template (`.md`) for agents and a machine-readable definition (`.yaml`) for the validator:

| Type | Template | Definition |
|---|---|---|
| `text` | `types/text.md` | `types/text.yaml` |
| `note` | `types/note.md` | `types/note.yaml` |
| `structured-claim` | `kb/notes/types/structured-claim.md` | `kb/notes/types/structured-claim.yaml` |
| `adr` | `kb/notes/types/adr.md` | `kb/notes/types/adr.yaml` |
| `index` | `kb/notes/types/index.md` | `kb/notes/types/index.yaml` |
| `spec` | none (legacy compatibility type) | `kb/notes/types/spec.yaml` |
| `review` | none (legacy compatibility type) | `kb/notes/types/review.yaml` |
| `related-system` | `kb/notes/types/related-system.md` | `kb/notes/types/related-system.yaml` |
| `source-review` | `kb/sources/types/source-review.md` | `kb/sources/types/source-review.yaml` |

Since bare names are currently unambiguous, this is a simple lookup table. If ambiguity ever arises (two collections defining a type with the same name), qualified names can be introduced for just the conflicting types.

### 3. Determine structural validation profile

The validator uses the type to decide which structural checks apply:

| Type | Structural checks beyond `note` base |
|---|---|
| `note` | Generic: frontmatter shape, description exists, links resolve |
| `structured-claim` | Require `## Evidence`, `## Reasoning` |
| `spec` | Require `## Design` or `## Implementation` |
| `review` | Require `## Findings`; require date metadata |
| `adr` | Require `## Context`, `## Decision`, `## Consequences`; allow ADR-specific status values |
| `index` | Navigation markers, link density |
| `related-system` | Require `## Core Ideas`, `## Comparison`, `## Borrowable Ideas`, `## Curiosity Pass`, `## What to Watch`; require `last-checked` field |
| `source-review` | Source-specific required sections |

All types inherit the `note` base checks. The validator reads structural requirements from `.yaml` type definition files, replacing the current hard-coded `TYPE_HEADINGS` map.

### 4. Determine traits

Read `traits:` from frontmatter. That's the full trait set for now.

Future: type definitions could declare implied traits (e.g. `structured-claim` always carries `title-as-claim`). This is a convenience optimization, not needed for the mechanism to work.

### 5. Determine applicable review gates

For each gate:

- If the gate has no `requires_trait` field: it applies (universal gate)
- If the gate has `requires_trait: X`: it applies only if `X` is in the note's trait set

This applicability check should live in a shared note-aware helper used by both direct note-local bundle runs and sweep selection. Bundle expansion alone is not enough because applicability depends on the note being reviewed.

## Inheritance

All structured types extend `note`:

- `text` has no parent
- `note` is the base structured type
- `structured-claim`, `spec`, `review`, `adr`, `index`, `related-system`, `source-review` all extend `note`

Extending `note` means inheriting its structural checks. Specialized types add checks on top.

## What's deferred

- **Qualified canonical ids** — bare names work while they're unambiguous. Add qualification if/when name collisions arise.
- **Type resolver as a library** — resolved. Validation now uses a shared resolver that reads scoped YAML definitions.
- **Implied traits from types** — authors declare traits explicitly in frontmatter for now. Existing `structured-claim` notes and claim-shaped plain notes are migrated by bulk frontmatter edits rather than inferred dynamically.
- **Machine-readable type definitions** — resolved. Each type gets a companion `.yaml` file alongside the prose `.md` template. Validator reads YAML; agents read prose.
- **Storage compatibility checks** — checking whether a file's location matches its type's expected directory. Useful but not blocking.

---

Workshop context:

- [design.md](./design.md) — types for structure, traits for semantic review routing
- [decision-criteria.md](./decision-criteria.md) — type vs trait boundary test
- [review-integration.md](./review-integration.md) — how the review system consumes traits for gate filtering
