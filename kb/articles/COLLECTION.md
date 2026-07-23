# Writing conventions for kb/articles/ (editorial profile)

## Text contract

Editorial (expository) [profile](../notes/definitions/text-contract.md): outward-facing articles distilled from the KB, published on the [documentation site](../reference/documentation-site.md) for readers outside the project. This is the worked case of the [external articles collection proposal](../reference/proposals/external-articles-collection.md); it is not yet in the shared [profile catalogue](../reference/text-contract-profiles.md).

The audience is highly technical — researchers and builders of agent and knowledge systems. Self-contained means "no KB context assumed", never "simplified".

**Quality goal: a self-contained article with a clear onward path.** An article stands on its own and leaves the reader knowing where in the KB to go next; in-prose relative links into `kb/` are that path (the site renders them as working links). Write pieces worth carrying onward — spreadability is an editorial aim, not a checklist.

## Conventions

- The body is reader-only prose. Agent-facing structure (lineage, status) lives in frontmatter; no footer link tables or link labels.
- Titles are headlines addressed to the reader, not claim-titles. The frontmatter `description` stays an agent retrieval filter; the human-facing abstract is the article's opening paragraph.
- An article carries a `byline` and a lifecycle `status`. A published article is a dated, frozen record: corrections are dated annotations or follow-up articles, never silent rewrites. Structural details live in the [type spec](./types/article.md).
- `source_notes` lists the repo-root paths of the notes the article distils; validation checks each path resolves.

## Types

| type | file | use for |
|---|---|---|
| `article` | `./types/article.md` | outward-facing dated articles distilled from the KB |

## What does NOT belong here

- Transferable claims and theory → `kb/notes/`
- Shipped-system description → `kb/reference/`
- Procedures and how-to guidance → `kb/instructions/`
- In-flight exploration → `kb/work/`
- Captured external material → `kb/sources/`
