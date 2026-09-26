---
description: "Wikipedia summary of Popper's Logic of Scientific Discovery; its two Popper quotes (falsification asymmetry, reproducible refuting effect) bear on what counts as a genuine counterexample."
source: https://en.wikipedia.org/wiki/The_Logic_of_Scientific_Discovery
captured: "2026-09-26"
capture: trafilatura
capture_scope: full-source
genre: reference-article
snapshot_sha256: 1b87862391175f4662eaee3b594b15f61c2ee2a144a1cf3245a302aea9ddfe4d
ingested: "2026-09-26"
type: types/ingest-report.md
domains: [epistemology, scientific-method, falsifiability, claim-modality]
learning_claims: true
---

# Ingest: The Logic of Scientific Discovery (Wikipedia)

## Classification

An encyclopedia entry: a short tertiary summary of a book, followed by a reception survey. It makes no argument of its own. Its substantive content is two verbatim quotations from Popper with page citations to the 2002 Routledge edition; everything else is a compilation of other writers' opinions of the book. Author: Wikipedia contributors, anonymous and collective. The quotes are checkable against the cited pages; the reception claims rest on the cited secondary works, which this capture does not include.

## Summary

The article describes Popper's 1959 English rewrite of *Logik der Forschung* (1934) and reduces its argument to two points, each given in Popper's words. First, verification and falsification are asymmetric: universal statements can never be derived from singular statements but can be contradicted by them (p. 19). Second, a refutation needs a reproducible effect: a few stray basic statements that contradict a theory do not make Popper treat it as falsified (p. 66). The reception section lists admirers and critics (Guntrip, Kuhn and Harré as partial dissenters, Jung, Ricœur, Gay, Magee on logical positivism, Sokal and Bricmont on an "irrationalist drift", Taleb on confirmation bias) without developing any of their arguments. The article does not cover the book's treatment of levels of universality and precision, degrees of corroboration, or probability. A reader who needs Popper's account itself should go to a primary text; this entry is useful only as a pointer to two quotable passages.

## Quotes

No source quotes have been retained yet.

## Connections Found

The source's role is a thin secondary witness for two Popper passages that bear on how the KB treats refutation. Its strongest connection is to [claim modality is the inference form of the refuter](../notes/claim-modality-is-the-inference-form-of-the-refuter.md), which it is evidence for at both ends. That note, like the modality paragraph in the notes collection contract, says a universal claim is refuted by modus tollens on "one genuine instance" but never defines "genuine." The p. 19 asymmetry supports the deductive form: a singular statement can contradict a universal statement, while no set of singular statements can derive one. The p. 66 passage qualifies "genuine": Popper does not count stray contradicting reports as falsification and requires a reproducible refuting effect. Whether the KB's "genuine" should mean "reproducible" is not settled by this ingest.

The same p. 66 condition is moderate evidence for the routing in [discovery lifecycle](../notes/definitions/discovery-lifecycle.md), which sends later counterevidence against an integrated claim to a new instance at observation / anomaly rather than to immediate rejection. The evidence is only moderate because that definition's lineage is Peircean, not Popperian.

It compares with [Popper, Conjectures and Refutations](./popper-conjectures-and-refutations.ingest.md) on the axis of where the falsifiability account is stated and at what fidelity: that ingest holds a primary Popper text, while this one holds a tertiary summary. Anyone grounding a falsifiability claim should prefer the primary source. It also compares with [POPPER: automated hypothesis validation with sequential falsifications](./automated-hypothesis-validation-sequential-falsifications.ingest.md) on what counts as a refutation: that system turns falsification into sequential statistical tests with error control, while Popper's p. 66 condition makes refutation a methodological decision about reproducible effects.

The only KB note that cites the book by name, [generality bought to avoid counterexamples is paid for in precision](../notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md), cites its treatment of levels of universality and precision. This article does not cover that material, so it cannot support that citation.

## Learning Claims (our opinion)

On the article's account, Popper's mechanism for the growth of scientific knowledge is methodological: theories are never proven, but reproducible observations can refute them, so science advances by exposing theories to refuting tests. The article states this only as a demarcation and method principle; it does not present the conjecture-and-refutation cycle, background knowledge, or corroboration.

Against the [theory-builder definition](../notes/definitions/theory-builder.md), the article touches only condition 3, criticism, and adds one qualification to it: a test result counts against a theory's content only when it is a reproducible effect, not a stray report. This is a statement about what a criticism must establish before it refutes, and it fits the definition's point that a criticism can itself be criticized, for example by blaming the data. The article says nothing usable about localized content, consumption, or iteration, and nothing about whether applying the method improves capacity for future action; those judgments stay with the primary Popper ingests. The mapping to Commonplace is our interpretation, and the evidence is two short quotations in a tertiary source, so it supports at most a gloss on existing concepts, not a revision of them.

## Extractable Value

1. **"Genuine counterexample" has a Popperian reading: a reproducible refuting effect.** The notes collection's universal mode and claim-modality leave "genuine" undefined. Popper's p. 66 condition would make a single unreproduced counterexample report an anomaly to investigate rather than a refuter. This changes how a review pass should treat one reported failure of a universal claim. It needs a deliberate decision, because in a KB of prose claims many counterexamples are arguments, not observations, and reproducibility may not apply to them. [experiment]
2. **The asymmetry quote is a compact citation for why every retained theory stays tentative.** The p. 19 passage states the logical reason that no accumulation of passing reviews verifies a universal claim. The [tentative theory](../notes/definitions/tentative-theory.md) definition is already grounded in primary Popper texts, so this adds a quotable page reference, not new content. [just-a-reference]
3. **The reception section is secondary opinion only.** The Kuhn, Magee, Sokal and Bricmont, and Taleb mentions are one-sentence attributions without argument and should not ground KB claims. [just-a-reference]

## Limitations (our opinion)

This is an encyclopedia entry, so no generic genre lens fully fits; the relevant questions are fidelity and selection. The two quotations are the only content that could carry weight, and they are extracted from a 500-page book without their surrounding argument. In particular, the p. 66 passage belongs to Popper's discussion of basic statements and methodological decisions; read alone, it could be taken as a weaker claim than he makes, or as licensing indefinite dismissal of inconvenient counterevidence, which the article does not qualify. The article's selection of what to summarize is editorial, and its omission of corroboration, universality and precision, and probability means it cannot stand for the book. The reception list is a collection of attributions whose framing depends on unnamed editors and on secondary works not captured here. Wikipedia text changes over time; the analysis applies only to this captured revision. Transferring Popper's condition from physical experiments to prose KB claims is our step, and what "reproducible" means for an argued counterexample remains open.

## Recommended Next Action

Snapshot and ingest a primary text of *The Logic of Scientific Discovery* (at least the chapters around pp. 19 and 66 and the chapter on levels of universality and precision), then use cp-skill-ground to retain the p. 66 reproducible-effect passage from it for [claim modality is the inference form of the refuter](../notes/claim-modality-is-the-inference-form-of-the-refuter.md); this Wikipedia ingest is a fallback grounding target only if the primary text cannot be captured.

---

Relevant Notes:

- [The Logic of Scientific Discovery (Wikipedia)](https://en.wikipedia.org/wiki/The_Logic_of_Scientific_Discovery) — derived-from: this analysis is worked out from the captured article
- [claim modality is the inference form of the refuter](../notes/claim-modality-is-the-inference-form-of-the-refuter.md) — is-evidence-for: the asymmetry supports the deductive refuter; the reproducible-effect condition qualifies "genuine instance"
- [discovery lifecycle](../notes/definitions/discovery-lifecycle.md) — is-evidence-for: a single contradicting report routes to anomaly, not rejection
- [Popper, Conjectures and Refutations](./popper-conjectures-and-refutations.ingest.md) — compares-with: primary versus tertiary statement of the falsifiability account
- [POPPER: automated hypothesis validation with sequential falsifications](./automated-hypothesis-validation-sequential-falsifications.ingest.md) — compares-with: what counts as a refutation
