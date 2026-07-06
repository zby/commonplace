---
type: kb/types/type-spec.md
name: adr
description: Architecture decision record for implemented system decisions
schema: ./adr.schema.yaml
---

# ADR

## Authoring Instructions

Use an ADR for a concrete architectural decision that has been made and implemented — accepted, superseded, or deprecated. A decision still under consideration is not an ADR; it stays in the workshop layer (`kb/work/`) until decided.

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `description` | Yes | Discriminating retrieval description for the decision record. |
| `type` | Yes | `../types/adr.md` for ADR files under `kb/reference/adr/`. |
| `tags` | No | Navigation tags, usually empty for ADRs. |
| `status` | No | Decision lifecycle: `accepted`, `superseded`, or `deprecated`. |

- The title should start with the numeric ADR prefix used in this collection, then a short decision label.
- `Status` records the decision lifecycle, not the note-writing status.
- `Date` is the decision date.
- `Context` explains the pressure or problem that forces a choice.
- `Decision` states the actual choice, not the surrounding debate.
- `Consequences` should name what becomes easier, harder, riskier, or no longer possible as a result.

## Template

```markdown
---
description: Template for architecture decision records — implemented decisions with Context, Decision, and Consequences sections
type: ../types/adr.md
tags: []
status: accepted
---

# {NNN}-{decision-title}

**Status:** {accepted | superseded | deprecated}
**Date:** {YYYY-MM-DD}

## Context

{Context}

## Decision

{Decision}

## Consequences

{Consequences}
```
