---
type: kb/types/type-spec.md
name: article
description: Outward-facing article distilled from KB notes for external technical readers; deliberately minimal spec that gains constraints only as failure modes are collected
schema: kb/articles/types/article.schema.yaml
---

# Article

Use `article` for outward-facing pieces published from the KB: self-contained prose for a technical reader with no KB context. The collection contract in [COLLECTION.md](../COLLECTION.md) owns the editorial conventions; this spec is deliberately nearly empty and gains a constraint only when a collected failure mode motivates it.

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `type` | Yes | `kb/articles/types/article.md` |
| `description` | Yes | Retrieval filter for agents; not the reader-facing abstract. |
| `source_notes` | No | Repo-root paths of the notes the article distils; when present, every path must resolve. |

Everything else (`byline`, `status`, `published`, …) is editorial convention governed by [COLLECTION.md](../COLLECTION.md), unconstrained here for now.
