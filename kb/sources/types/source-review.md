---
type: kb/types/type-spec.md
name: source-review
description: Structured extraction and relevance review for an external source
schema: kb/sources/types/source-review.schema.yaml
---

# Source review

## Authoring Instructions

Use `source-review` when you want a structured extraction from an external source.

- Choose it over `snapshot` when you are authoring analysis rather than preserving a captured source verbatim; choose it over `ingest-report` when the artifact should stand as a structured review instead of a snapshot-adjacent connection report.
- `Key Points` should summarize what the source says in neutral terms before adding your judgment.
- `Relevance to the KB` should explain what the source changes for the current knowledge base: what it supports, challenges, or suggests borrowing.
- `Open Questions` should only contain unresolved follow-up questions. Omit the section if there are none.

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `description` | Yes | Retrieval description for what the source review extracts and why it matters. |
| `type` | Yes | `kb/sources/types/source-review.md`. |
| `tags` | No | Navigation tags for the reviewed source or the claims it supports. |
| `status` | No | Lifecycle state, usually `current` for an accepted source review. |

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

## Relevance to the KB

{KB relevance}

## Open Questions

- {Unresolved questions — omit section if none}
```
