---
description: "Removes the excluded article-draft subtree so every draft circulates from the collection root with a visible authored banner as its only draft-specific circulation requirement"
type: ../types/adr.md
tags: []
status: accepted
---

# 063-All article drafts circulate behind a banner

**Status:** accepted
**Date:** 2026-08-04

## Context

[ADR 057](./057-articles-use-an-editorial-profile-and-excluded-drafts.md) put unfinished articles in a site-excluded subtree; [ADR 062](./062-drafts-may-circulate-at-the-root-behind-a-draft-banner.md) added a second kind of draft at the collection root for comments. The distinction made authors decide placement, visibility, approval, and discovery path before writing or circulating, and made publication relocate the file and repair its links, yet it has no useful case: article drafts are meant to circulate for comments, and the banner already tells readers that claims, structure, and thesis may change without notice. The excluded subtree adds ceremony without strengthening the reader contract.

## Decision

**Every article draft circulates from the collection root.** Drafts live at `kb/articles/{slug}.md`, render through ProperDocs, and use `status: draft`. There is no site-excluded draft subtree.

**The authored draft banner is the only draft-specific circulation requirement.** It appears at the start of every draft body, says that everything may still change, and tells readers where to comment. Drafts need no version handle, revision date, separate circulation approval, or mandatory collection-README entry. Listing remains optional navigation.

**Publication becomes a status transition at a stable path.** With explicit approval naming `working-paper` or `published`, the publication procedure removes the banner, sets the target state's fields, and lists the article under the matching README heading. No relocation or redirect is involved.

Operativity path: `kb/articles/COLLECTION.md` directs authors and collection-conformance reviewers to create every draft at the root and check only its banner as the draft circulation condition; `properdocs.yml` includes those paths in the site; and `kb/instructions/publish-an-article.md` performs the banner-removal and status transition in place.

## Considered alternatives

**Keep both hidden and circulating drafts.** Rejected because the hidden mode has no worked need, while choosing between the two modes creates the placement and approval ceremony this decision removes.

**Add a second lifecycle status for hidden drafts.** Rejected because it preserves the unused distinction in frontmatter and would require new routing and rendering rules rather than simplifying the collection.

**Generate the banner from status.** Deferred. The authored banner works in raw Markdown as well as ProperDocs, and no missing-banner failure has yet justified custom rendering or schema enforcement.

Free choices left open: whether repeated missing or malformed banners should promote the convention into deterministic validation, and whether the collection README should eventually list every draft for convenience.

## Consequences

Easier:

- Drafting, circulation, and publication use one stable path.
- Every draft can receive comments immediately and carries the same visible reader warning.
- Publication no longer requires relocation, backlink repair, or a redirect.
- Authors need not negotiate a separate discovery path before circulating work.

Harder / accepted costs:

- Committing an article draft makes it visible on the public site and in site search.
- An unlisted draft may be found through search without appearing in curated article navigation; the banner, not navigation placement, carries the reader contract.
- Banner presence remains judgment-enforced until a concrete failure warrants mechanical enforcement.

---

Relevant Notes:

- [ADR 057 — Articles use an editorial profile and excluded drafts](./057-articles-use-an-editorial-profile-and-excluded-drafts.md) — supersedes: removes its excluded-draft placement while retaining the local article contract and published-body lifecycle
- [ADR 062 — Drafts may circulate at the root behind a draft banner](./062-drafts-may-circulate-at-the-root-behind-a-draft-banner.md) — supersedes: makes its optional circulating mode the only draft mode and removes its approval and discovery-path gates
- [Publish an article](../../instructions/publish-an-article.md) — implemented-by: executes the stable-path promotion this decision defines
- [Documentation site](../documentation-site.md) — part-of: circulation channel that now renders every article draft
