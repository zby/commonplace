---
description: "Use when a circulating kb/articles draft has explicit approval to become a working paper or frozen dated article on the ProperDocs site"
type: kb/types/instruction.md
---

# Publish an article

Promote an approved circulating draft on the ProperDocs deployment to either a revisable **working paper** or a frozen dated **published** article. Publication approval applies to the current substantive body and to the target state; if either changes afterwards, obtain approval again.

## Prerequisites

- The artifact declares `type: kb/articles/types/article.md` and `status: draft`.
- It lives at `kb/articles/{slug}.md` and opens with the draft banner.
- It carries a byline and resolving `source_notes`.
- Its body satisfies `kb/articles/COLLECTION.md`: self-standing technical prose for an external reader, no agent-facing footer grammar, and a worthwhile onward path into the KB.
- The user has explicitly approved publication **and named the target state**. “Nearly ready,” review approval, or a merge approval is not publication approval.
- For a working paper, the body says what it invites — counterexamples, boundary cases, disputed classifications.

## Publish

1. Run `commonplace-validate {draft-path}` and resolve every failure. Warnings require judgment but do not automatically block publication.
2. Remove the draft banner without changing the substantive body.
3. Set the frontmatter for the approved target state, using the date supplied by the user, or the current local date when the user says “today.” Do not infer a date for “tomorrow” before that day arrives.
   - Working paper: `status: working-paper`, `published: YYYY-MM-DD` for the first public date, `version: 1`, and `revised: YYYY-MM-DD` matching the publication date.
   - Published: `status: published` and `published: YYYY-MM-DD`.
4. Move the article's entry from any draft list into `kb/articles/README.md` under `## Working papers` or `## Published`, including the date. Keep the context phrase reader-facing.
5. Run `commonplace-validate {published-path}` and `commonplace-validate articles`. If relocation changed `properdocs.yml`, run `commonplace-validate redirects` too.
6. Review the diff with the user when the approved body changed or any publication field is uncertain. Otherwise commit the article, collection README, and relocation redirect together. Land that commit on `main` through the repository's normal Git workflow; the Pages deployment is the publication action.

## Revising a working paper

A working paper is revisable in place, which is the point of the state. For each substantive revision — a changed claim, a new or withdrawn qualification, a restructured argument — bump `version`, set `revised` to the revision date, and re-run `commonplace-validate`. Typo and link fixes do not bump the version.

Freeze the working paper into a dated record only with explicit approval: set `status: published`, keep the original `published` date, drop `version` and `revised`, and move its README entry to `## Published`. The path does not change. Freezing is one-way — a published body cannot reopen as a working paper.

## After publication

A published body is frozen. Do not silently rewrite it. Apply a correction as one of:

- a dated annotation that preserves the original text;
- a new article, with the old article set to `superseded` and a visible pointer to its successor; or
- `status: withdrawn` with a visible reason.

A later source-note change does not automatically stale a dated article. Search `source_notes` when investigating impact, then decide explicitly whether the historical article stands, needs an annotation, or warrants a follow-up.

## Verify

- The article is at `kb/articles/{slug}.md`, carries the approved status, and has the intended dates — plus `version` and `revised` for a working paper.
- The draft banner is gone.
- `kb/articles/README.md` lists it under the matching public heading and nowhere as a draft.
- The article and collection validate without failures.
- After the commit reaches `main`, the ProperDocs page renders its status and the article is discoverable from the Articles navigation.

---

Relevant Notes:

- [ADR 057 — Articles use an editorial profile and excluded drafts](../reference/adr/057-articles-use-an-editorial-profile-and-excluded-drafts.md) — operates-on: publication lifecycle and channel this procedure executes
- [ADR 063 — All article drafts circulate behind a banner](../reference/adr/063-all-article-drafts-circulate-behind-a-banner.md) — operates-on: root-only draft placement and the banner-removal transition this procedure executes
