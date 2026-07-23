# Writing conventions for kb/articles/ (editorial profile)

Editorial [profile](../notes/definitions/text-contract.md): outward-facing articles distilled from the KB and published on the [documentation site](../reference/documentation-site.md). Worked case of the [external articles collection proposal](../reference/proposals/external-articles-collection.md); not yet promoted to the shared [profile catalogue](../reference/text-contract-profiles.md).

**Audience and quality goal.** Highly technical readers with no KB context. An article must stand on its own and leave its reader knowing where in the KB to go next — self-containment is the floor, the onward path the obligation.

**Spreadability.** In the sense of Jenkins, Ford, and Green: give readers material worth carrying into their own communities and make its circulation easy. Which techniques serve that is the author's call.

**Reader-only body.** Agent-facing structure lives in frontmatter; the body is prose for the reader — no footer link tables, link labels, or graph-traversal glosses. In-prose relative links into `kb/` are deliberate invitations to go deeper; a closing "where to go next" section is welcome.

**Titles and descriptions.** Titles are headlines addressed to the reader, not claim-titles. The frontmatter `description` remains what it is everywhere in this KB — a retrieval filter for agents; the reader-facing abstract is the article's opening paragraph.

**Attribution and lifecycle.** Every article carries a `byline` and a `status` (`draft`, `published`, `superseded`, `withdrawn`). Publication freezes the body: corrections happen by dated annotation, a successor article, or withdrawal — never a silent rewrite. Field-level rules live in the [type spec](./types/article.md).

**Lineage.** `source_notes` lists the repo-root paths of the notes the article distils; validation checks that each resolves. There is no freshness registration — find affected articles by search.

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
