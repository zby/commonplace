---
description: "Adds a third public article state: a root-placed draft circulating for comments behind a visible banner, with no version handles and no stability promise"
type: ../types/adr.md
tags: []
status: superseded
---

# 062-Drafts may circulate at the root behind a draft banner

**Status:** superseded by [ADR 063](./063-all-article-drafts-circulate-behind-a-banner.md)
**Date:** 2026-08-04

## Context

[ADR 057](./057-articles-use-an-editorial-profile-and-excluded-drafts.md) made placement the exclusion mechanism: relocating a draft to the collection root is publication. [ADR 061](./061-articles-may-circulate-as-revisable-working-papers.md) added the working paper for circulating an article whose claims are open, and rejected circulating a `draft` because the status would then describe neither visibility nor revisability.

Operating the first two articles surfaced a need neither state serves. The operator wants outside comments while an article's central thesis is still moving — the reflective self-improvement article changed its thesis several times within days. The working-paper contract is wrong for that text twice over: its `version`/`revised` handles advertise a stability the text does not have, and its framing invites reference to claims the collection is not yet willing to stand behind. What was missing is a public state that promises nothing: visible, commentable, and free to pivot silently.

## Decision

**A draft may be relocated to the collection root to request comments.** Placement governs visibility — the `drafts/` subtree stays site-excluded, and moving a draft to the root is a public act requiring explicit operator approval, as for the other public states. Status governs the reader contract: `draft` at the root means the claims, structure, and central thesis may change without notice, with no `version` or `revised` obligations and silent rewrites expected.

**Every root-placed draft opens with an authored draft banner.** A short blockquote before the body states that everything may still change and where to send comments. It must not promise stability: no version handles, no revision log, no language that invites treating the text as a fixed reference. The banner is authored rather than generated, keeping ADR 057's no-custom-rendering stance; a status-driven generated banner can return if a forgotten banner ever ships (the worked-failure rule).

**Each root-placed draft has a deliberate discovery path.** A draft intended as a collection entry point is listed in `kb/articles/README.md` under "In draft". A supporting draft may instead remain unlisted when a listed root article links to it deliberately. This revises ADR 057's rejected "rendered but unlisted" alternative: an authored incoming link makes the placement deliberate.

**The lifecycle gains one forward step.** Excluded draft → root draft (request for comments) → working paper (claims stable enough for version handles) → published (frozen). Each transition needs explicit approval naming the target state. This answers ADR 061's objection to circulated drafts: status describes revisability and maturity, placement describes visibility, and the banner makes the combination legible on the page itself.

Operativity path: `kb/articles/COLLECTION.md` binds authoring and collection-conformance review with the banner, discovery-path, and no-stability-promise clauses; `kb/articles/README.md` carries the "In draft" listing; the ProperDocs metadata line continues to render status, and the site's page-bottom comments system receives the feedback each banner invites.

## Considered alternatives

**Circulate as working papers (ADR 061's route).** Rejected for these texts. The version/revised contract is a stability promise; while a thesis is still pivoting the promise either goes stale or generates noise revisions, and the state's framing advertises a maturity the collection does not claim yet.

**Keep drafts excluded and gather comments off-site.** Rejected: no stable URL, no resolved links into the KB, and a commenter cannot point at the passage they dispute.

**Generate the banner from `status` in the build.** Deferred under the worked-failure rule ADR 057 applied to rendering: an authored blockquote is inspectable in the source file and works today; forgetting it is a conformance-review catch until a mechanical failure proves otherwise.

Free choices left open: whether a working paper may demote back to a root draft when its thesis reopens (no case yet); whether the banner wording should standardize beyond its two required elements (everything-may-change, where to comment).

## Consequences

Easier:

- Comments can arrive while the argument is still being formed, which is when they are cheapest to act on.
- The label is honest: a pivoting text is presented as a pivoting text.
- The working-paper decision waits until the thesis stops moving, instead of being forced by the desire for feedback.

Harder / accepted costs:

- Three public states to keep accurately labelled and deliberately discoverable; conformance review gains banner and discovery-path checks, and nothing mechanical enforces them yet.
- A disagreement with a root draft cannot name which text it disputes — there is no version handle by design. Accepted: that is inherent to requesting comments on a moving draft.
- Readers who ignore the banner may still treat the text as settled; the banner bounds the collection's promise, not reader behavior.

---

Relevant Notes:

- [ADR 057 — Articles use an editorial profile and excluded drafts](./057-articles-use-an-editorial-profile-and-excluded-drafts.md) — extends: revises its placement-is-publication rule into placement-governs-visibility, status-governs-the-reader-contract
- [ADR 061 — Articles may circulate as revisable working papers](./061-articles-may-circulate-as-revisable-working-papers.md) — extends: adds the no-promise public state below the working paper, answering its objection to circulated drafts with the banner
- [Publish an article](../../instructions/publish-an-article.md) — implemented-by: gains the draft-circulation transition alongside the existing ones
- [Documentation site](../documentation-site.md) — part-of: rendering channel that surfaces status and banner to readers
- [ADR 063 — All article drafts circulate behind a banner](./063-all-article-drafts-circulate-behind-a-banner.md) — superseded-by: removes the excluded-draft state and makes circulation the only draft mode
