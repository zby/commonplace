# Writing conventions for kb/articles/ (editorial profile)

Editorial/expository [profile](../reference/text-contract-profiles.md): outward-facing articles distilled from the KB and published on the [documentation site](../reference/documentation-site.md). Adopted by [ADR 057](../reference/adr/057-articles-use-an-editorial-profile-and-excluded-drafts.md).

**Audience and quality goal.** Highly technical readers with no KB context. An article must stand on its own and leave its reader knowing where in the KB to go next — self-containment is the floor, the onward path the obligation.

**Spreadability.** In the sense of Jenkins, Ford, and Green: give readers material worth carrying into their own communities and make its circulation easy.

**Stickiness.** In the sense of Heath and Heath's *Made to Stick*: shape the core idea so it survives retelling — simple, unexpected, concrete, credible, emotional, carried by stories (SUCCESs). Spreadability governs whether the piece circulates; stickiness governs whether the idea arrives intact. Which techniques serve either is the author's call.

**Reader-only body.** Agent-facing structure lives in frontmatter; the body is prose for the reader — no footer link tables, link labels, or graph-traversal glosses. In-prose relative links into `kb/` are deliberate invitations to go deeper; a closing "where to go next" section is welcome.

**Titles and descriptions.** Titles are headlines addressed to the reader, not claim-titles. The frontmatter `description` remains what it is everywhere in this KB — a retrieval filter for agents; the reader-facing abstract is the article's opening paragraph.

**Attribution and lifecycle.** Every article carries a `byline` and a `status` (`draft`, `published`, `superseded`, `withdrawn`). Publication freezes the body: corrections happen by dated annotation, a successor article, or withdrawal — never a silent rewrite. These are editorial conventions, not schema: the [type spec](./types/article.md) starts nearly empty and gains constraints only as failure modes are collected.

**Drafting and publication.** Drafts live under `kb/articles/drafts/`, where this contract and the article type still bind but ProperDocs does not publish or index them. [Publish an article](../instructions/publish-an-article.md) by relocating the finished draft to the collection root, changing `status` to `published`, adding a `published: YYYY-MM-DD` date, and listing it in `README.md`. ProperDocs renders the lifecycle status under the title. A published body is frozen; only a dated annotation may be added in place.

**Lineage.** `source_notes` lists the repo-root paths of the notes the article distils; when present, validation checks that each resolves. There is no freshness registration — find affected articles by search.

## Outbound links

In-prose links to the `external` destination are authorized for primary attribution, canonical sources, and material an external reader should be able to inspect directly; they carry no formal identifier. External prospecting is part of article research, not `cp-skill-connect`.

## Types

| type | file | use for |
|---|---|---|
| `article` | `./types/article.md` | outward-facing dated articles distilled from the KB |

## What does NOT belong here

- Transferable claims and theory → `kb/notes/`
- Shipped-system description → `kb/reference/`
- Procedures and how-to guidance → `kb/instructions/`
- In-flight exploration → `kb/work/`
- Article drafts → `kb/articles/drafts/`
- Captured external material → `kb/sources/`
