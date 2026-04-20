---
type: kb/types/type-spec.md
name: source-review
description: Structured extraction and relevance review for an external source
schema: kb/sources/types/source-review.schema.yaml
---

# Source review

## Authoring Instructions

Use `source-review` when you want a structured extraction from an external source.

- `Key Points` should summarize what the source says in neutral terms before adding your judgment.
- `Relevance to llm-do` should explain what the source changes for the project: what it supports, challenges, or suggests borrowing.
- `Open Questions` should only contain unresolved follow-up questions. Omit the section if there are none.

## Template

```markdown
---
description: ""
type: kb/sources/types/source-review.md
tags: []
status: current
---

# {source title or key claim}

**Source:** {URL or citation}

## Key Points

- {Neutral summary}

## Relevance to llm-do

{Project relevance}

## Open Questions

- {Unresolved questions — omit section if none}
```
