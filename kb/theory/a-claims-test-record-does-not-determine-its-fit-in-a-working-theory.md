---
description: "Three standings of a claim are separate: whether it is true, what independent tests it has survived so far, and whether it fits a working theory; agreement with the theory is a test only where the claim could have failed"
type: types/note.md
traits: [title-as-claim]
tags: [learning-theory, evaluation, self-improving-systems, theory-builder]
---

# A claim's test record does not determine its fit in a working theory

A working theory is the set of claims a system currently uses to explain, predict, search and modify. Three things can be asked about a claim in it, and no answer to one settles another.

- **Is it true?** Truth does not change with time. For a universal empirical claim it is never established, and a derivation establishes a formal claim only relative to its premises.
- **What is its test record?** The test record (what related notes call "warrant", narrowed here to exclude truth) is the set of independent tests the claim has survived so far. A test is independent when its outcome could have gone against the claim and does not presuppose the claim under test or an auxiliary claim whose acceptance would make the outcome automatic. The kind of test depends on the claim: an observation for an empirical claim, a derivation for a formal one, a check against the source for a source-derived one. A test record carries a date.
- **Does it fit?** A claim fits a working theory when the theory handles its problem better with the claim than without it: the claim is relevant to that problem, is stated at the scope and level the theory's decisions need, agrees with the other retained claims, and changes explanation, prediction, search or modification when used.

## A test record is not truth

A claim that has survived every test so far is still a conjecture. A valid derivation is an exception only in part: it settles a formal claim relative to its premises, and the premises remain conjectures. Popper states the difference directly: truth is timeless, while a claim is corroborated only with respect to the statements accepted up to a particular time, so every appraisal of corroboration carries a date ([*Logic of Scientific Discovery*, §84](../sources/popper-logic-of-scientific-discovery.ingest.md)). A good test record is the best available reason to rely on a claim.

## A good test record does not make a claim fit

A well-tested claim may fit poorly. It can be irrelevant to the problem the theory addresses. It can duplicate a claim already present. It can state the right fact at the wrong level of abstraction, or with a scope that does not match the decisions the theory must guide. It can add detail that increases maintenance without changing any inference the theory needs. Retaining a claim is a decision about what the theory is for. The claim's test record does not make that decision.

## Fit is not an independent test

A false, overgeneral or weakly tested claim may fit smoothly, because the current implementation, the vocabulary or the neighbouring claims already assume it. It may improve local search or repair while it encodes a misconception that a later test exposes. Agreement of this kind measures the theory's own assumptions.

Agreement adds to the claim's test record only where it was an outcome the claim could have failed, without presupposing the claim. Use of a claim inside the theory can therefore be a test, and often it is not. What decides is this condition, not where the evidence was produced. The condition is adapted from Popper's requirement that evidence corroborates a claim only when it reports a sincere attempt to refute it (§82, starred note \*1, and Appendix \*ix of the same work). Popper places the requirement on the tester's sincerity, which he says cannot be formalized; this note places it on the test's outcome.

## The two kinds of evidence inform each other

Evidence about fit can send a claim back for testing. Two cases differ. A claim that is seldom useful in the theory, because it predicts nothing the work needs, has only a fit problem; that says nothing about whether it is true. A claim whose predictions keep failing in use is in doubt. The fault may still lie in another claim used with it, so the failures call for an independent test of the claim itself. A new test result can likewise bear on fit: a claim that survives a severe test may give a reason to restructure the working theory, even when the restructuring makes the theory less convenient.

Neither may be substituted for the other. "This claim helped the system" is not evidence that the claim is true unless the help was a test it could have failed. "This claim is well tested" is not by itself a reason to retain it in this theory.

## A contradiction does not say which claim to give up

When a well-tested new claim contradicts the working theory, logic says only that the claims cannot all be kept. Rejecting the new claim is one repair. The contradiction may instead locate a defect in another claim, a wrong scope, a bad decomposition, or a larger part of the theory that needs revision. Which repair to make is a decision, taken by comparing the test records of the claims involved and what each repair does to the theory's fit to its problem.

## Scope

- Fit has no single scale. Relevance, redundancy, scope, level of abstraction, agreement with other claims and usefulness in operation weigh differently in different working theories.
- Objectives, commitments and grants of authority affect whether a claim belongs in a working theory. Tests of the claim do not settle them.
- The three questions are separate, not statistically independent. A well-tested claim is more likely to fit than an arbitrary one, and a claim that fits is more likely to survive a test.

---

Relevant Notes:

- [System use provides evidence of theory fit and causal usefulness, not an independent test](./system-use-provides-evidence-of-theory-fit-not-an-independent-test.md) — extends: applies the limit on fit as a test to evidence from operating a live system
- [System use is an initial selection environment when theory fit lacks a fixed oracle](./system-use-selects-theory-fit-without-a-fixed-oracle.md) — extends: develops how a live system can expose theory fit when no complete fixed oracle decides it
- [Epistemic stance](../reference/epistemic-stance.md) — grounds: the fallibilism under which a test record is a dated report and never a proof
