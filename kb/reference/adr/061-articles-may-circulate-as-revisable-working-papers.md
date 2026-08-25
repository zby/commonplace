---
description: "Articles gain a second public lifecycle state — a revisable, versioned working paper that circulates while its claims are open — alongside the frozen published record"
type: ../types/adr.md
tags: []
status: accepted
---

# 061-Articles may circulate as revisable working papers

**Status:** accepted
**Date:** 2026-07-31

## Context

[ADR 057](./057-articles-use-an-editorial-profile-and-excluded-drafts.md) gave `kb/articles/` one public state: publication freezes the substantive body, and later corrections use a dated annotation, a successor article, or withdrawal. That decision left "whether a later living-page article mode deserves freshness registration" as an explicit free choice, so a revisable public state was anticipated but not designed.

The first article is now ready to circulate, and its value depends on what comes back. It ends by asking readers to apply a diagnostic test to their own systems and to contest boundary cases — an invitation that only pays off if the answers can reach the text. Under freeze semantics the smallest unit of correction is a whole successor article, so an incoming counterexample either waits for one or goes unrecorded, and the frozen label tells readers their criticism has nowhere to land.

The remaining state does not fit either. `draft` is excluded from the site by placement, not by status, so a circulated draft is a contradiction: moving it to the root *is* publication. "Draft" also understates a reviewed article and invites readers to discount what they are being asked to use and criticize.

## Decision

**`kb/articles/` gains `working-paper` as a second public lifecycle state.** A working paper lives at the collection root, renders on the site, and is listed in the collection README under its own heading. It is revisable in place: each substantive revision bumps `version` and sets `revised: YYYY-MM-DD`, so a reader who cited the text can tell that it moved. Its body states what it invites — counterexamples, boundary cases, disputed classifications.

**Freeze semantics narrow to `published`, and the two states differ only in whether the body may change.** Both are equally public and both require explicit approval naming the target state. A working paper may remain one indefinitely or freeze into a published article at the same path, keeping its original `published` date and dropping `version` and `revised`. Freezing is one-way: a published body cannot reopen without withdrawing what readers were told they could cite.

**No schema and no rendering change.** `status` stays an editorial-convention field, and `version` and `revised` join it under [COLLECTION.md](../../articles/COLLECTION.md) rather than the type spec, under ADR 057's rule that the article schema gains constraints only from a demonstrated mechanical failure.

Operativity path: `kb/articles/COLLECTION.md` binds authoring and collection-conformance review with the lifecycle clause and the working-paper review test; the prescriptive [publication procedure](../../instructions/publish-an-article.md) executes the draft→working-paper, revision, and working-paper→published transitions; `kb/articles/README.md` carries the public listing that separates the two states for readers; and the ProperDocs metadata line renders the status on the page.

## Considered alternatives

**Publish frozen and absorb criticism through successor articles.** The status quo under ADR 057. Rejected because the correction unit is far larger than the corrections expected: a counterexample or a contested classification is a paragraph of work, and requiring a successor article for each one means most never land. It also mislabels the article's own stance, which is that several of its claims are conjectures awaiting exactly this evidence.

**Circulate the existing `draft`.** Rejected because ADR 057 deliberately made placement the exclusion mechanism, so a draft is either site-excluded and unreachable or relocated to the root and thereby published. Keeping the `draft` label on a rooted, circulated article would leave the status field describing neither its visibility nor its revisability.

**A separate living-page collection or article mode.** Rejected because everything else is shared: same contract, same type, same path, same review, same rendering. Only revision semantics differ, which is one field's worth of difference against duplicating ADR 057's placement, validation, and navigation machinery.

**Register working papers for freshness against `source_notes`.** Deferred, and still the free choice ADR 057 named. A revisable article has a stronger case for it than a frozen one, since it can actually act on source drift, but no drift case has occurred yet. Search-based lineage stays until one does.

**Constrain `status`, `version`, and `revised` in the article schema.** Rejected under the worked-failure rule ADR 057 applied to the same fields. The marks doctrine — enforced or omitted — argues against adding lifecycle state that nothing validates, but the conventions bind through collection-conformance review today, and a mechanical failure would be the evidence that promotes them.

Free choices left open: whether a working paper must eventually freeze or may stay open indefinitely (nothing forces the transition now); whether the version and revision date should also appear in the body rather than only in frontmatter, which depends on how the rendered metadata line reads in practice; and freshness registration as above.

## Consequences

Easier:

- An article can circulate while its claims are still open, which is the honest state for a piece whose conjectures are labelled as such.
- Incoming counterexamples have a route into the text at their own size, instead of accumulating until a successor article is worth writing.
- The freeze decision can wait until the argument stops moving, rather than being forced by the act of publishing.
- Readers get a version handle, so a disagreement can name which text it disputes.

Harder / accepted costs:

- A revisable public text can change under a reader who cited it. `version` and `revised` make the change visible but do not preserve the earlier text; only git history does, and readers are not pointed at it.
- The publication procedure now branches on target state, and the collection README must keep two public sections accurate.
- Two public states are two chances to mislabel one. The conformance review gains a test, but nothing mechanical catches a working paper whose `revised` date lags its last substantive edit.

---

Relevant Notes:

- [ADR 057 — Articles use an editorial profile and excluded drafts](./057-articles-use-an-editorial-profile-and-excluded-drafts.md) — extends: adds the second public state its lifecycle anticipated but left undesigned
- [Publish an article](../../instructions/publish-an-article.md) — implemented-by: executes the transitions this decision defines
- [Documentation site](../documentation-site.md) — part-of: rendering channel that surfaces the lifecycle status to readers
- [Document types should be verifiable](../../notes/document-types-should-be-verifiable.md) — rests-on: why the new lifecycle fields stay contract-enforced until a mechanical failure warrants schema
