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
- For decisions dated 2026-07-24 or later, the ADR must also name the decision's operativity path: what consumes the changed organization, through which channel, and with what force — in `Consequences`, or in `Decision` when the path is itself part of the choice. A decision without a named consumer is recorded but inert, and the record is where that should become visible. ADRs dated earlier predate this requirement and are not retrofitted.

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

---

Relevant Notes:

- [Operative change](../../notes/definitions/operative-change.md) — rationale: the operativity-path requirement — a decided change reaches later behavior only through a consumer, channel, and force
- [Where change candidates come from in Commonplace](../where-change-candidates-come-from-in-commonplace.md) — rationale: instrumented ADRs are the ongoing evidence stream for how the system's organization actually changes
