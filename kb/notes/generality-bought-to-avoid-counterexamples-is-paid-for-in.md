---
description: Widening a claim's vocabulary to survive counterexamples raises universality by spending precision, so content stays flat — and the unreadability that follows is the symptom, not the price of rigor
type: kb/types/note.md
traits: [title-as-claim]
tags: [document-system, failure-modes]
---

# Generality bought to avoid counterexamples is paid for in precision

An agent asked to make a claim more precise will often reach for more abstract vocabulary: "note" becomes "retained artifact", "agent" becomes "bounded consumer", "fails" becomes "exhibits degraded conformance". Each swap is locally defensible, and the note ends up unreadable. The natural diagnosis is that the agent overshot — traded readability for precision and went too far. But it gained no precision. It spent precision to buy generality, and those are separate dials.

## Universality and precision are separate dials

A claim's content is what it rules out. Popper's account (*Logic of Scientific Discovery*, on levels of universality and precision) gives two ways to raise it: assert the claim over a wider class of cases, or assert something sharper about each case. Both raise what the claim forbids, and they can be traded against each other with content held constant. "All orbits are closed curves" is more universal than "planetary orbits are closed curves", and less precise than "all orbits are ellipses".

Defensive abstraction is a pure trade. The agent meets a case its concrete wording does not cover and answers by raising universality — which it can only do by lowering precision, since the sharper term was what excluded the case. Content does not move. Length does: the general term needs scaffolding to stay intelligible, and each round of scaffolding exposes a new edge that invites the next. Every turn of the ratchet is individually justifiable, and no turn is checkable on its own.

The failure is invisible from inside the generating loop, because [an LLM's confidence tracks how typical a continuation is, not whether it is sound](./llm-generation-confidence-tracks-typicality-not-soundness.md) — and hedged abstract prose is maximally typical of the careful-technical register. The move feels like rigor exactly when it buys none.

## Naming is the opposite move with the same surface

Telling agents to avoid abstraction cannot work, because the productive move looks identical. When a user offers a vague thought and the agent finds the word for it, universality and precision rise *together*: the vagueness was noise, not scope. The right name does not merely cover what the fumbling description covered — it excludes cases the fumbling description left open. That is [seeing the particular as an instance of the general](./conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md), and it is the same operation running the other way.

So the two are not points on a spectrum with a correct dose in between. Any rule of the form "abstract, but not too much" treats them as one move and cannot separate them.

## The discriminator is what the new wording forbids

Universality cannot discriminate, since both moves raise it. Content can:

> After abstracting, name a case the new wording rules out that the old wording allowed.

Naming can always answer. Defensive abstraction never can, because not ruling things out was the point of the move. The failure has a positive signature too: pressed for what the new wording forbids, the agent volunteers what it now *covers*. Coverage is not content.

This is the [boundary test](./abstract-an-experience-only-when-you-can-state-the-boundary.md) applied to a claim's vocabulary rather than to an episode — there, whether an abstraction can say where it stops; here, whether it can say what it excludes. An abstraction that can say neither has [adaptive fit rather than reach](./first-principles-reasoning-selects-for-explanatory-reach-over.md).

## Unreadability is a symptom, not a price

A claim with content forbids things; a claim that forbids things is concrete; concrete prose gives a reader something to grip. The readability collapse is therefore not a cost paid for rigor but evidence that none was bought.

That inverts the repair. Treated as a style problem, the fix is to soften the prose while keeping the claim — which preserves the defect. Treated as a content problem, unreadable abstraction is a signal to find the counterexample the agent was fleeing and put it in the note, as a scope line or a stated exception, rather than dissolve it into vocabulary. A counterexample handled in the open costs a sentence; handled by vocabulary it costs the document.

## Abstraction must be localized to be auditable

The failure compounds because it is diffuse: generality smeared across every noun in every sentence leaves no single site where a reviewer can ask whether it was earned. State the general form once, in the sentence where the argument needs it, then write concretely elsewhere and let scope lines and worked instances carry the range. Localized abstraction submits to the forbids-test one term at a time.

`kb/notes/COLLECTION.md` already imposes the mirror of this in the narrowing direction: treat qualifiers as obligations, and drop any that does not change the reasoning. The widening direction needs the same obligation — treat each abstraction as an obligation, and downgrade any whose concrete term would leave the argument intact.

## Scope

The claim is about abstraction adopted *defensively*, against a counterexample the author does not want to concede. Generality reached by argument is untouched: a claim that covers three substrates because its mechanism does not depend on the substrate has earned its vocabulary, and the forbids-test will confirm it. Nor is concreteness a default virtue — a note that stays concrete when its argument supports more fails the reach standard from the other side. The trade is symmetric; only the defensive motive marks the bad direction.

---

Relevant Notes:

- [abstract an experience only when you can state the boundary](./abstract-an-experience-only-when-you-can-state-the-boundary.md) — extends: the boundary test applied to claim vocabulary rather than to episode compression
- [first-principles reasoning selects for explanatory reach over adaptive fit](./first-principles-reasoning-selects-for-explanatory-reach-over.md) — grounds: an abstraction that cannot say what it excludes has fit, not reach
- [conjecture is seeing the particular as an instance of the general](./conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md) — contrasts: the productive direction, where universality and precision rise together
- [llm generation confidence tracks typicality not soundness](./llm-generation-confidence-tracks-typicality-not-soundness.md) — mechanism: why hedged abstract prose feels rigorous to the generator exactly when it is empty
- [reverse compression is when LLM output expands without adding information](./reverse-compression-is-when-llm-output-expands-without-adding.md) — contrasts: measures prose volume against what a bounded reader can extract; this note measures claim vocabulary against what the claim forbids, so a short, link-dense note can still be hollow
- [title as claim exposes commitments enabling Popperian maintenance](./title-as-claim-exposes-commitments-enabling-popperian-maintenance.md) — enables: a claim title is where an unearned abstraction is cheapest to catch
- [unearned generality gate](../instructions/review-gates/semantic/unearned-generality.md) — see-also: the forbids-test operationalized as a review gate
