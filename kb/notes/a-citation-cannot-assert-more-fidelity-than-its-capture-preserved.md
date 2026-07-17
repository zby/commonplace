---
description: "Capture is layered (verbatim / paraphrase / second-hand) by forced constraints; a citation's fidelity is bounded by which layer holds the passage, and no notation can raise it — only re-capture"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [document-system, context-engineering]
---

# A citation cannot assert more fidelity than its capture preserved

A claim that cites a captured source can be no better grounded than the capture step left it. Fidelity is fixed at ingest and is **non-increasing** downstream: no citation syntax, no locator type, no review gate can promote a passage to a grade its capture did not preserve. The only operation that raises fidelity is re-capture.

This is a claim about **fidelity**, not authority, and the two move in opposite directions — worth stating plainly, because [trace-extracted memory earns authority per operation, not at capture](./trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) asserts the complement. *Authority* — how much weight a reader should give a claim — is earned by post-capture work: verify, abstract, consult. *Fidelity* — what grade of provenance evidence a passage carries, whether the source's own words or somebody's restatement — is spent at capture and never replenished. The two compose: capture sets a ceiling, and post-capture operations earn authority beneath it. A heavily verified rule can still rest on a second-hand passage; a pristine verbatim quote can sit unverified indefinitely.

## Capture is layered because it is forced to be

The layering is not a design choice. It arrives in the constraint packet of commitments the framework has already made, which is what makes it a [first principle rather than a position](./first-principles-are-inherited-constraints-not-design-choices.md): a long source cannot be captured verbatim into markdown at full fidelity, because the consumer's context window is finite, because copyright forces trims, and because provider output filters block mass verbatim reproduction. Any framework whose consumer is an LLM and whose sources are real documents inherits all three. So a snapshot of a long source is not a copy — it is an *extraction*, and it stratifies:

- **Verbatim layer** — the source's own words, reproduced. A claim may quote, and a machine can string-match the quote back against the snapshot.
- **Paraphrase layer** — the snapshot's own-words summary of a passage. A claim may cite it, but must not use quotation marks, and verification requires going back to the authoritative artifact (the sibling PDF).
- **Second-hand** — the captured text is itself another party's restatement (a court restating a complaint; a news article quoting an order whose original is no longer served). The citation must name the intermediary, because the provenance chain has a party in the middle whose fidelity is an assumption.

## Why notation cannot repair it

The temptation is to fix provenance downstream — a richer citation format, a structured span locator, a stricter gate. It cannot work, and the reason is exact rather than merely practical. [A derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) requires a *mechanical derivation rule* before a copy may be trusted. A verbatim-layer quote has one: substring match. A paraphrase-layer passage has no such rule — there is no mechanical comparison between a paraphrase and its source, only judgment. So marking a paraphrase-layer passage `verbatim` does not make it verbatim; it produces precisely the hand-maintained-and-trusted copy that rule forbids, with a stronger trust signal attached than the unmarked version would carry. Notation can *express* the fidelity bound. It cannot move it.

This is the citation-fidelity instance of a general rule: [history has one chance to become checkable](./history-has-one-chance-to-become-checkable.md). The one chance here is ingest, and what was not preserved verbatim then is permanently downgraded — recoverable only by returning to the authoritative artifact and capturing again.

## Corollary: a locator must carry the layer, not just the span

It follows that a source-span locator encoding only *position* is underspecified. **Two spans at the same file offset can differ in provenance quality by a full layer** — one lifted from the snapshot's verbatim block, one from its paraphrase summary. A position-only locator would render them identical, which is the one distinction a consumer of the citation most needs. Any locator design must encode the layer.

## Scope

Change the premise and the conclusion moves, which is where the claim earns its boundaries. If a source is short enough to capture losslessly — a tweet, a short abstract, a commit message — the layers collapse to one, the bound goes vacuous, and *position* becomes the binding constraint again. In that regime a structured span locator earns its keep; the corollary above is out of scope rather than in conflict with that design. The claim bites exactly where capture is lossy, which is to say wherever the sources are long.

The practical consequence is that provenance quality is decided *before any note is written*. If a passage will be load-bearing, it must be promoted into the snapshot's verbatim layer at capture time, or the author must return to the authoritative artifact and quote-mine it. Because the debt is fixed at ingest and visible in the citation, it can at least be made explicit and repaid deliberately rather than discovered later.

## Open Questions

- Does forum-thread or transcript sourcing — many small utterances rather than a few long papers — change the natural grain, since each utterance *is* losslessly capturable while the corpus is not?
- Fidelity is a ceiling on verification, but is it a ceiling on *usefulness*? A well-attributed paraphrase may serve a reader better than a verbatim fragment shorn of context.

---

Evidence for the layering and for the failure of naive `verbatim` marking comes from both epistack casebook work in the sibling `epistack-casebooks` repository and from [ADR 046](../reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md): the shipped verbatim-quote checker, run over that corpus, found eighteen of eighty-seven `verbatim`-marked spans that did not appear in their cited snapshot, with no false mismatches on manual audit.

Relevant Notes:

- [History has one chance to become checkable](./history-has-one-chance-to-become-checkable.md)
- [A derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md)
- [First principles are inherited constraints, not design choices](./first-principles-are-inherited-constraints-not-design-choices.md)
- [Trace-extracted memory earns authority per operation, not at capture](./trace-extracted-memory-earns-authority-per-operation-not-at-capture.md)
- [Structure inference needs capture at the decision surface](./structure-inference-needs-capture-at-the-decision-surface.md) — decision rationale rather than quote fidelity
- [ADR 046 — Verbatim quotes are validated against their cited source](../reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md)
- [Text contract profiles](../reference/text-contract-profiles.md) — dialectical/evidential profile ships the grounding-layer marker
