---
type: kb/types/type-spec.md
name: note
description: Base structured document type for transferable KB notes with description, status, traits, and tags
schema: kb/types/note.schema.yaml
---

# Note

Use `note` for transferable KB claims, observations, and theory that are worth preserving beyond the current task. A note is a structured markdown artifact with YAML frontmatter, a prose title, and enough body context for an agent to decide how to use it.

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `type` | Yes | `kb/types/note.md` |
| `description` | Yes | Discriminating retrieval filter, not a summary. |
| `traits` | No | Independently checkable review expectations. |
| `tags` | No | Navigation tags used by indexes. |
| `status` | No | Commitment level: `seedling`, `current`, `speculative`, or `outdated`. |

## Description

The description should answer "why this document?" for a future retrieval decision. It should distinguish the note from nearby notes and usually fit in one sentence.

## Status

Status tracks commitment, not structure.

| Status | Meaning |
|---|---|
| `seedling` | Provisional; may be pruned or rewritten. |
| `current` | Reviewed and accepted into the KB. |
| `speculative` | Deliberately retained conjecture. |
| `outdated` | Superseded but kept for reference. |

## Traits

Traits route semantic review. They do not change structural validation.

| Trait | What it asserts |
|---|---|
| `title-as-claim` | The title is a proposition that can be true or false. |
| `definition` | The note pins a term's operational meaning. |
| `has-comparison` | The note compares alternatives. |
| `has-external-sources` | The note cites material outside the project. |
| `has-implementation` | The note includes implementation sketches or code-facing detail. |
| `synthesis` | The note composes multiple cited claims into a unified argument; cite as a unit and expect inline restatement. Waives the default body-composability rule. |

## Writing Shape

- Use the title as the strongest compressed handle for the note.
- Put the main claim or mechanism near the top.
- Link to adjacent notes where the relationship helps traversal.
- Keep design rationale in notes; keep imperative procedure in instructions.

## Template

```markdown
---
description: ""
type: kb/types/note.md
traits: []
tags: []
status: current
---

# {prose-as-title — a proposition, not a topic label}

{Your analysis, reasoning, or exploration. Freeform.}

## Open Questions

- {Unresolved points worth tracking — omit section if none}

---

Relevant Notes:

- [related-note](./related-note.md) — how it relates
```

---

Relevant Notes:

- [text](./text.md) - implicit no-frontmatter capture state that can be promoted to a note
- [document-types-should-be-verifiable](../notes/document-types-should-be-verifiable.md) - design rationale for verifiable types
