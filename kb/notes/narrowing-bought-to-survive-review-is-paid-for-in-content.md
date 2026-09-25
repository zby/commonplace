---
description: "Repairing a defeated claim by shrinking its subject is justified at every step, but shrinking the subject into the predicate's own extension yields an analytic title that passes every gate and says nothing."
type: types/note.md
traits: [title-as-claim]
tags: [document-system, failure-modes]
---

# Narrowing bought to survive review is paid for in content

When review defeats a claim — counterexamples show its subject is too wide — the natural repair is to narrow the subject until the counterexamples fall outside. Narrowing is often the right disposition: a true narrower claim beats a false wide one. But a repair loop whose acceptance criterion is "the gates pass" has a cheaper move available: narrow the subject *by redefinition*, restricting it to whatever satisfies the predicate. The limit of that move is an analytic claim — true by construction, immune to every counterexample, and empty.

## The mechanism

A claim's content is what it forbids. [Generality bought to avoid counterexamples is paid for in precision](./generality-bought-to-avoid-counterexamples-is-paid-for-in.md) describes the widening escape: meet a counterexample by abstracting vocabulary, so the claim covers more while forbidding no more. Narrowing is the symmetric escape. Shrinking to an independently identifiable subject lowers content honestly — the narrower claim still forbids something about that subject. Shrinking to a subject defined by the predicate lowers content to zero: "unifying conjectures unify" forbids nothing, because a case that failed the predicate would not count as the subject.

As in the widening direction, each step is individually justified — it answers a real counterexample — and the emptiness only exists in the accumulated result. The two failures also share a generator: repair that optimizes defensibility. Gates measure what a claim gets wrong, overstates, or leaves unsupported, and an analytic claim is maximally defensible. A loop that only answers gate findings will therefore drift toward it.

## What an exact repair loop holds fixed

Counterexample-guided synthesis shows the structure this drift exploits. In [SKETCH](../sources/combinatorial-sketching-finite-programs.ingest.md), a synthesizer proposes values for the holes in a partial program. A verifier checks the result against a separate reference specification on all inputs, and each counterexample becomes a constraint that every later candidate must also pass. The loop cannot repair by redefinition, because the specification is outside what the revise step can write. When no candidate fits, it reports that the sketch has no valid completion instead of returning a weaker target. A review/revise loop over a claim lacks both features. The claim is both specification and candidate, so narrowing its subject edits the target, and the loop has no "cannot be repaired within this claim" exit. SKETCH is the exact-oracle limit. Whether a natural-language loop can hold an equivalent fixed reference is this note's conjecture; the citer test below proposes one.

## A witness

A 2026 full improvement pass in this repository defeated the universal claim "conjecture is seeing the particular as an instance of the general" — singular hypotheses and predictions are conjectures that unify nothing. The repair narrowed the title to "unifying conjecture makes a general and its instances intelligible together," while the note's own opening defined a unifying conjecture as one that recasts particulars as instances of a proposed general. Every closing gate passed, including the claim-strength gate whose job is to reject uncontestable titles: read against the note's local definition, the title looked substantive. The pass's report did record the warranted contribution as *weakened* — but that judgment had no force, because no gate fails on it.

Meanwhile the note's inbound citers told a different story: nearly all of them cited claims the repair had deleted or hedged — that recognition is the expensive step in connecting knowledge, and that naming a structure amortizes it. The repair had preserved the defeated subject and discarded the imported content. The eventual fix was a different claim, not a shrunk one: the note was rebuilt around what its citers used, as [recognition, not linking, is the hard problem in knowledge systems](./recognition-not-linking-is-the-hard-problem-in-knowledge-systems.md).

## Two guards

**The refuter test** — the narrowing-direction mirror of the forbids-test. After narrowing, name a possible case that would still refute the new claim. An honestly narrowed claim can answer, because some conceivable member of its subject could fail the predicate. A subject defined by the predicate cannot answer, and the repair should be rejected.

**The citer test.** What inbound citers import is a note's revealed contribution. Before accepting a repair, check whether the claims citers actually cite survive it. A repair that keeps the title's subject but drops what citers import has repaired the wrong thing, and the right disposition may be rebuilding around the imported claims rather than rescuing the defeated ones.

## Scope

The failure marks are specific: the narrowed subject has no predicate-independent identification, or the surviving claim no longer supports its inbound uses. Narrowing that avoids both marks is ordinary, legitimate repair. Nor is the lesson to weaken review — the gates in the witness episode found real defects. The missing piece is a contribution check with the same force as the gates: a warranted-contribution judgment of "near zero" should be able to fail a repair even when every gate passes, since [warranted reader update is the objective of substantive writing](./warranted-reader-update-is-the-objective-of-substantive-writing.md) and an analytic claim updates no reader.

---

Relevant Notes:

- [generality bought to avoid counterexamples is paid for in precision](./generality-bought-to-avoid-counterexamples-is-paid-for-in.md) — contrasts: the widening escape from counterexamples; there content stays flat while length grows, here content goes to zero while defensibility grows
- [title as claim exposes commitments enabling Popperian maintenance](./title-as-claim-exposes-commitments-enabling-popperian-maintenance.md) — enables: a claim title is where analytic emptiness is cheapest to catch, if the reader asks what the title forbids
- [warranted reader update is the objective of substantive writing](./warranted-reader-update-is-the-objective-of-substantive-writing.md) — grounds: contribution is a warranted change to a reader's prior, and a true-by-construction claim changes none
- [claim-strength gate](../instructions/review-gates/frontmatter/claim-strength.md) — evidenced-by: the gate that passed the analytic title in the witness episode, showing per-note gates can miss redefinition-based narrowing
- [Combinatorial sketching for finite programs](../sources/combinatorial-sketching-finite-programs.ingest.md) — evidenced-by: an exact propose-and-counterexample loop stays honest because the specification is outside the revise step and "no completion" is a reportable outcome
- [Decorrelated reviewers still share the field's prior, so read their findings by the claim's stance](./reviewers-share-the-fields-prior-so-interpret-findings-by-stance.md) — extends: why review pressure concentrates on the most original claims, and the stance declaration that separates costly narrowing from ordinary repair
