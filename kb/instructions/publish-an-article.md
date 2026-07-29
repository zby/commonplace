---
description: "Use when a finished kb/articles draft has explicit approval to become a dated public article on the ProperDocs site"
type: kb/types/instruction.md
---

# Publish an article

Turn an approved article draft into the frozen dated artifact published by the ProperDocs deployment. Publication approval applies to the current substantive body; if the body changes afterwards, obtain approval again.

## Prerequisites

- The artifact declares `type: kb/articles/types/article.md` and `status: draft`.
- It carries a byline and resolving `source_notes`.
- Its body satisfies `kb/articles/COLLECTION.md`: self-standing technical prose for an external reader, no agent-facing footer grammar, and a worthwhile onward path into the KB.
- The user has explicitly approved publication. “Nearly ready,” review approval, or a merge approval is not publication approval.

## Publish

1. Run `commonplace-validate {draft-path}` and resolve every failure. Warnings require judgment but do not automatically block publication.
2. If the draft is under `kb/articles/drafts/`, relocate it to `kb/articles/{slug}.md` with `commonplace-relocate-note --to ... --apply`. If it is the transitional first draft already at the collection root, keep its path.
3. Without changing the substantive body, set `status: published` and `published: YYYY-MM-DD` in frontmatter using the publication date supplied by the user, or the current local date when the user says “today.” Do not infer a date for “tomorrow” before that day arrives.
4. Move the article's entry from any draft list into `kb/articles/README.md` under `## Published`, including the publication date. Keep the context phrase reader-facing.
5. Run `commonplace-validate {published-path}` and `commonplace-validate articles`. If relocation changed `properdocs.yml`, run `commonplace-validate redirects` too.
6. Review the diff with the user when the approved body changed or any publication field is uncertain. Otherwise commit the article, collection README, and relocation redirect together. Land that commit on `main` through the repository's normal Git workflow; the Pages deployment is the publication action.

## After publication

Do not silently rewrite the substantive body. Apply a correction as one of:

- a dated annotation that preserves the original text;
- a new article, with the old article set to `superseded` and a visible pointer to its successor; or
- `status: withdrawn` with a visible reason.

A later source-note change does not automatically stale a dated article. Search `source_notes` when investigating impact, then decide explicitly whether the historical article stands, needs an annotation, or warrants a follow-up.

## Verify

- The article is at `kb/articles/{slug}.md`, has `status: published`, and has the intended publication date.
- `kb/articles/README.md` lists it under `## Published` and nowhere as a draft.
- The article and collection validate without failures.
- After the commit reaches `main`, the ProperDocs page renders its status and the article is discoverable from the Articles navigation.

---

Relevant Notes:

- [ADR 057 — Articles use an editorial profile and excluded drafts](../reference/adr/057-articles-use-an-editorial-profile-and-excluded-drafts.md) — operates-on: publication lifecycle and channel this procedure executes
