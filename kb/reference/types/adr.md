---
type: kb/types/type-spec.md
name: adr
description: Architecture decision record for accepted or proposed system decisions
schema: ./adr.schema.yaml
---

# ADR

## Authoring Instructions

Use an ADR for a concrete architectural decision that has been proposed, accepted, superseded, or deprecated.

- The title should start with the numeric ADR prefix used in this collection, then a short decision label.
- `Status` records the decision lifecycle, not the note-writing status.
- `Date` is the decision date.
- `Context` explains the pressure or problem that forces a choice.
- `Decision` states the actual choice, not the surrounding debate.
- `Consequences` should name what becomes easier, harder, riskier, or no longer possible as a result.

## Template

```markdown
---
description: Template for architecture decision records — accepted/proposed decisions with Context, Decision, and Consequences sections
type: ../types/adr.md
tags: []
status: accepted
---

# {NNN}-{decision-title}

**Status:** {proposed | accepted | superseded | deprecated}
**Date:** {YYYY-MM-DD}

## Context

{Context}

## Decision

{Decision}

## Consequences

{Consequences}
```
