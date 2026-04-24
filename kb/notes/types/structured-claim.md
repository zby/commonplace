---
type: kb/types/type-spec.md
name: structured-claim
description: Developed argument note with explicit Evidence and Reasoning sections
schema: ./structured-claim.schema.yaml
---

# Structured claim

## Authoring Instructions

Use `structured-claim` for arguments where separating evidence from reasoning genuinely clarifies the case.

- The title should be a claim and should carry the `title-as-claim` trait.
- The opening paragraph should state the claim plainly and explain why it matters.
- `Evidence` is for observations, facts, citations, or examples.
- `Reasoning` is for the principle that connects the evidence to the claim.
- `Caveats` is for scope limits, assumptions, counterarguments, and failure cases.

Do not force this scaffold onto arguments it does not fit.

- Definitional or classification claims often work better as plain `note`s.
- If the evidence and reasoning are inseparable, splitting them can make the argument harder to follow rather than clearer.

## Template

```markdown
---
description: Template for developed arguments — claim-titled notes with explicit Evidence, Reasoning, and optional Caveats sections
type: ./types/structured-claim.md
traits: [title-as-claim]
tags: []
status: seedling
---

# {Claim as title — an assertion, not a topic label}

{Opening paragraph}

## Evidence

{Evidence}

## Reasoning

{Reasoning}

## Caveats

- {Scope limits}
- {Assumptions}
- {Counterarguments}
```
