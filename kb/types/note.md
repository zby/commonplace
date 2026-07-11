---
type: kb/types/type-spec.md
name: note
description: Base structured document type for transferable KB notes with optional committed human verification
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
| `user-verified` | No | May only be `true`; records explicit human attestation to the current substantive contents. |

## Description

The description should answer "why this document?" for a future retrieval decision. It should distinguish the note from nearby notes and usually fit in one sentence.

## User verification

`user-verified: true` means a human user explicitly attests that the artifact's current substantive contents have been verified. Absence means only that there is no current user attestation; it says nothing about truth, maturity, currency, or review history.

Never add the field during creation, conversion, deterministic validation, or semantic review. A substantive edit must remove it. Preserve it only for a mechanical change covered by an explicit human-approved trivial-change workflow.

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
| `design-proposal` | The note describes an unadopted design: problem, option space, forces, free choices marked — no decision. Reviewed for design quality, not contestability; waives claim-title expectations. |

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
