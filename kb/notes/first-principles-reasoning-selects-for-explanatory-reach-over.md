---
description: First-principles reasoning selects explanations with explanatory-reach, accountable to observed fit, premise variation, and rival-practice tests
type: kb/types/note.md
traits: [has-external-sources]
tags: [learning-theory, discovery]
---

# First-principles reasoning selects for explanatory-reach over adaptive fit

Commonplace's first-principles methodology is valuable because it selects for explanations with **explanatory-reach**: claims that keep working outside the case that produced them because they capture why a pattern works, not just that it worked. This note treats adaptive fit and explanatory-reach as a local polarity rather than a hard binary.

**Adaptive information** helps a system cope with the world. A genome, a neural network's weights, or a local rule of thumb can encode something useful without explaining why it works or where it stops working.

**Explanatory knowledge** gives a criticizable account of why the pattern works. It can be deliberately varied: change a load-bearing premise, and the explanation should constrain what changes in the conclusion. That variation is what gives an explanation its explanatory-reach.

Partial cases sit between the poles. A rule can transfer across a narrow family of cases because it captures shared structure, while still falling short of a full generative model. The point is not to demote every local observation; local fit is the evidence a later explanation must organize, predict, and improve.

## Why this matters for the KB

When a note derives a design pattern from inherited constraints — finite context, no scoping mechanism, text-in/text-out interpretation — the derivation can be explanatory: it says why the pattern works and predicts where it will fail. Change the constraint, and the conclusion should change with it.

That "can be" matters. First-principles stories become post-hoc rationalization when broad premises can justify several rival practices equally well. A useful derivation should rule out at least one plausible alternative, name the constraint that does the ruling out, or predict a failure that later use can confirm.

The [computational-model](./computational-model-README.md) area is an explanatory-reach bet under audit. Programming-language concepts such as scoping, partial evaluation, and scheduling were developed for compilers, but they reach into KB design when the shared invariant is explicit: bounded processors compose text under constraints, and unscoped composition lets distant bindings interfere. [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) therefore works only if the dynamic-scoping comparison predicts real context failures and useful remedies, not merely because the analogy is elegant.

## The negative test

This adapted distinction provides a quality check orthogonal to the KB's type system. A well-formed note can pass every structural check while still recording a pattern without explaining the mechanism. The test:

1. **Can you vary a load-bearing premise?** If changing one premise lets you predict a constrained change in the conclusion, the note is exposing causal structure. If any premise can move while the conclusion stays rhetorically intact, the derivation may be decorative.
2. **Does it reach?** Would the insight apply in a domain you have not considered, and can you say which invariant carries it there? If yes, the mechanism is deeper than the original case. If no, the note may be context-fitted.
3. **Can it be criticized?** Is there a specific way the explanation could be wrong, not just incomplete? The [falsifier blocks](./mechanistic-constraints-make-popperian-kb-recommendations-actionable.md) practice operationalizes this.
4. **Does observed fit discipline the explanation?** Local success is not second-class residue; it is evidence. If the explanation cannot account for where the pattern actually works, fails, or costs too much to maintain, it has verbal explanatory-reach without operational grip.

The first three tests map to the grading of [what must be recognized](./recognition-not-linking-is-the-hard-problem-in-knowledge-systems.md): shared feature (adaptive), shared structure (partially explanatory), generative model (fully explanatory, with explanatory-reach). The fourth is not a depth — it holds an explanation at any depth accountable to the observed fit it must organize.

## Scope

Explanatory-reach is the quality goal for theoretical notes, not the only kind of KB value. Descriptions need economy, instructions need precision, and logs may preserve local observations before the mechanism is understood. The explanatory-reach filter says when an observation is ready to become a transferable claim; it does not replace the capture layer that supplies the observations.

## Open Questions

- Where in the KB are notes that are well-formed but merely adaptive? Those are candidates for deepening.
- Which first-principles derivations currently rule out a rival practice, and which only explain an already-preferred practice after the fact?
- Which observed transfers would distinguish the four-part test from a persuasive post-hoc story?

---

Relevant Notes:

- [A borrowed pattern transfers only as far as source and target share a mechanism](./borrowed-patterns-transfer-only-over-shared-mechanism.md) — contrasts: gates borrowing on shared mechanism, where this note selects imported explanations for explanatory-reach
- [learning is not only about generality](./learning-is-not-only-about-generality.md) — grounds: the Scope boundary — explanatory-reach is one property of accumulated knowledge, not the only learning value
- [recognition, not linking, is the hard problem in knowledge systems](./recognition-not-linking-is-the-hard-problem-in-knowledge-systems.md) — contrasts: its recognition-cost grading runs parallel to this note's explanatory grading, with the generative-model level matching explanatory-reach
- [mechanistic constraints make Popperian KB recommendations actionable](./mechanistic-constraints-make-popperian-kb-recommendations-actionable.md) — extends: criticism becomes operational through falsifier blocks
- [computational-model](./computational-model-README.md) — exemplifies: programming-language concepts reaching into KB design is an explanatory-reach bet under audit
- [systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](./systematic-prompt-variation-serves-verification-and-diagnosis-not.md) — contrasts: explanatory-reach testing varies an explanation's premises, not an LLM prompt surface
- [SuperARC AIT benchmark](../sources/superarc-ait-benchmark-llm-compression-abstraction.ingest.md) — evidenced-by: reports dramatically higher LLM performance on integer than binary sequences and attributes it to memorized common mathematical sequences; treating that representation-sensitive result as evidence about cue sensitivity or explanatory-reach is local analysis, and it is not load-bearing here
- [A framework rule with a boundary-preserving rival is not an inherited constraint](./a-framework-rule-with-a-boundary-preserving-rival-is-not-inherited.md) — contrasts: a one-way test that demotes framework rules with boundary-preserving rivals; this note explains what first-principles filtering is for
- [Moen, Foundation and History of the PDSA Cycle](https://deming.org/wp-content/uploads/2020/06/PDSA_History_Ron_Moen.pdf) — evidenced-by: the explanatory-reach-over-fit polarity restated from improvement science — a change that improved during one test must still be predicted to improve under the different conditions ahead

Derived into:

- [review-explanatory-reach](../tasks/recurring/review-explanatory-reach.md) — the four-part negative test restated as a recurring review procedure
- [COLLECTION.md](./COLLECTION.md) — the four-part negative test condensed into the "Tests for explanatory-reach" authoring block
