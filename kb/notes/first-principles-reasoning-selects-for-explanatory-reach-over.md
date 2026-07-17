---
description: Adapts Deutsch's adaptive-vs-explanatory distinction to KB design — first-principles reasoning selects explanations with reach, accountable to observed fit and rival-practice tests
type: kb/types/note.md
traits: [has-external-sources]
tags: [learning-theory, discovery]
---

# First-principles reasoning selects for explanatory reach over adaptive fit

Commonplace's first-principles methodology is valuable because it selects for explanations with **reach**: claims that keep working outside the case that produced them because they capture why a pattern works, not just that it worked. This note adapts David Deutsch's adaptive-vs-explanatory distinction for KB design, treating adaptive fit and explanatory reach as a polarity rather than a hard binary.

**Adaptive information** helps a system cope with the world. A genome, a neural network's weights, or a local rule of thumb can encode something useful without explaining why it works or where it stops working.

**Explanatory knowledge** gives a criticizable account of why the pattern works. It can be deliberately varied: change a load-bearing premise, and the explanation should constrain what changes in the conclusion. That variation is what gives an explanation reach.

Partial cases sit between the poles. A rule can transfer across a narrow family of cases because it captures shared structure, while still falling short of a full generative model. The point is not to demote every local observation; local fit is the evidence a later explanation must organize, predict, and improve.

## Why this matters for the KB

When a note derives a design pattern from inherited constraints — finite context, no scoping mechanism, text-in/text-out interpretation — the derivation can be explanatory: it says why the pattern works and predicts where it will fail. Change the constraint, and the conclusion should change with it.

That "can be" matters. First-principles stories become post-hoc rationalization when broad premises can justify several rival practices equally well. A useful derivation should rule out at least one plausible alternative, name the constraint that does the ruling out, or predict a failure that later use can confirm.

The [computational-model](./computational-model-README.md) area is a reach bet under audit. Programming-language concepts such as scoping, partial evaluation, and scheduling were developed for compilers, but they reach into KB design when the shared invariant is explicit: bounded processors compose text under constraints, and unscoped composition lets distant bindings interfere. [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) therefore works only if the dynamic-scoping comparison predicts real context failures and useful remedies, not merely because the analogy is elegant.

## The negative test

This adapted distinction provides a quality check orthogonal to the KB's type system. A well-formed note can pass every structural check while still recording a pattern without explaining the mechanism. The test:

1. **Can you vary a load-bearing premise?** If changing one premise lets you predict a constrained change in the conclusion, the note is exposing causal structure. If any premise can move while the conclusion stays rhetorically intact, the derivation may be decorative.
2. **Does it reach?** Would the insight apply in a domain you have not considered, and can you say which invariant carries it there? If yes, the mechanism is deeper than the original case. If no, the note may be context-fitted.
3. **Can it be criticized?** Is there a specific way the explanation could be wrong, not just incomplete? The [falsifier blocks](./mechanistic-constraints-make-popperian-kb-recommendations-actionable.md) practice operationalizes this.
4. **Does observed fit discipline the explanation?** Local success is not second-class residue; it is evidence. If the explanation cannot account for where the pattern actually works, fails, or costs too much to maintain, it has verbal reach without operational grip.

The first three tests map to the three depths in [discovery](./conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md): shared feature (adaptive), shared structure (partially explanatory), generative model (fully explanatory with reach). The fourth is not a depth — it holds an explanation at any depth accountable to the observed fit it must organize.

## Scope

Reach is the quality goal for theoretical notes, not the only kind of KB value. Descriptions need economy, instructions need precision, and logs may preserve local observations before the mechanism is understood. The reach filter says when an observation is ready to become a transferable claim; it does not replace the capture layer that supplies the observations.

## Open Questions

- Where in the KB are notes that are well-formed but merely adaptive? Those are candidates for deepening.
- Which first-principles derivations currently rule out a rival practice, and which only explain an already-preferred practice after the fact?
- Should this note keep a direct Deutsch source, or is the adapted distinction enough if the KB-specific test stands on its own?

---

Relevant Notes:

- [design methodology — borrow widely, filter by first principles](./programming-patterns-get-a-fast-pass-but-other-borrowed-ideas-must.md) — grounds: first-principles filtering selects for explanatory reach when the borrowed pattern is tied back to inherited constraints
- [learning is not only about generality](./learning-is-not-only-about-generality.md) — grounds: the Scope boundary — reach is one property of accumulated knowledge, not the only learning value
- [conjecture is seeing the particular as an instance of the general](./conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md) — parallels: the generative model depth maps to explanatory knowledge with reach
- [mechanistic constraints make Popperian KB recommendations actionable](./mechanistic-constraints-make-popperian-kb-recommendations-actionable.md) — extends: criticism becomes operational through falsifier blocks
- [computational-model](./computational-model-README.md) — exemplifies: programming-language concepts reaching into KB design is a reach bet under audit
- [systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](./systematic-prompt-variation-serves-verification-and-diagnosis-not.md) — contrasts: reach testing varies an explanation's premises, not an LLM prompt surface
- [SuperARC AIT benchmark](../sources/superarc-ait-benchmark-llm-compression-abstraction.ingest.md) — evidence: integer-vs-binary sequence performance is suggestive for cue sensitivity and algorithmic-compression reach, but not load-bearing here
- [First principles are inherited constraints, not design choices](./first-principles-are-inherited-constraints-not-design-choices.md) — contrasts: defines which constraints count as first principles; this note explains what first-principles filtering is for

Derived into:

- [review-explanatory-reach](../tasks/recurring/review-explanatory-reach.md) — the four-part negative test restated as a recurring review procedure
- [COLLECTION.md](./COLLECTION.md) — the four-part negative test condensed into the "Tests for reach" authoring block
