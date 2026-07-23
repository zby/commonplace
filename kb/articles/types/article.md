---
type: kb/types/type-spec.md
name: article
description: Outward-facing dated article distilled from KB notes for external technical readers, with byline, lifecycle status, and validated source-note lineage
schema: kb/articles/types/article.schema.yaml
---

# Article

Use `article` for outward-facing pieces published from the KB: self-contained prose for a technical reader with no KB context, distilled from notes the frontmatter records. The collection contract in [COLLECTION.md](../COLLECTION.md) owns the editorial conventions; this spec owns the structural obligations.

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `type` | Yes | `kb/articles/types/article.md` |
| `description` | Yes | Retrieval filter for agents; not the reader-facing abstract. |
| `status` | Yes | `draft`, `published`, `superseded`, or `withdrawn`. |
| `byline` | Yes | Public attribution; the article is a first-person-committed public statement. |
| `source_notes` | Yes | Repo-root paths of the notes the article distils; every path must resolve. |
| `published` | When status is not `draft` | Publication date, quoted so YAML keeps it a string (`"YYYY-MM-DD"`); setting it freezes the body. |
| `superseded_by` | When status is `superseded` | Repo-root path of the superseding article. |

## Lifecycle rules

- `draft` is the only status under which the body may be freely rewritten.
- Moving to `published` requires the publication date and freezes the body. Corrections after that are a dated annotation under `## Corrections`, a superseding article, or a withdrawal — never a silent rewrite.
- `superseded` requires `superseded_by`; the frozen body stays as the historical record.
- `withdrawn` keeps the frozen body and states the reason in a dated annotation.

## Body rules

The body is reader-only prose (see [COLLECTION.md](../COLLECTION.md)): no footer link tables, no link labels, no agent-facing glosses. In-prose relative links into `kb/` are the onward path and render as site links.
