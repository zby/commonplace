---
description: "Why authors may invent structure to keep programming, why immediate-success training may miss its value, and what fresh agents must recover."
type: types/note.md
traits: [title-as-claim]
tags: [architecture, evaluation, agent-memory, learning-theory]
---

# Reasoning limits may select for design commitments

A programmer may introduce rules about how code is organized because they need those rules to write the next part. Maintainability can then be a by-product of making the code understandable to its author.

A **design commitment** restricts acceptable future implementations: one component owns a state transition, validation happens at a particular boundary, or two subsystems remain independent despite duplicated code. An unwritten commitment is one the author relies on without recording it as a shared requirement. The author may never have stated it as a rule.

This is a conjecture about how useful structure arises. The proposed human–LLM difference remains untested.

## The author's difficulty can select useful structure

When an author can no longer reliably track the interactions needed for a change, boundaries, conventions, or abstractions may make further work manageable. The author can then continue by relying on those commitments. Where later contributors can use them too, the same structure helps maintenance.

The benefit need not have been selected directly as a maintainability objective. The immediate pressure is to make the next change possible. General practices such as SOLID leave many of these project-specific choices unresolved.

The proposed benefit depends on what the author invents: restrictions that suit one person can hinder others, and difficulty can produce bad abstractions or mistakes.

One possible benefit is compression. If all state changes pass through one function, a contributor can track that rule instead of remembering each path independently. Jürgen Schmidhuber's [Formal Theory of Creativity, Fun, and Intrinsic Motivation](../sources/schmidhuber-formal-theory-creativity.ingest.md) measures compression cost using both the predictor and deviations from its predictions. Our application is that a design commitment can make code easier to model when the rule and its exceptions cost less to track than the separate facts. Elaborate rules with many exceptions can cost more than they save.

## Capacity and feedback timing are rival explanations

An LLM may be able to make a larger change without commitments a human needs to keep track of the code. If so, the model has less immediate need to introduce them. Alternatively, it may encounter similar difficulty but produce a change whose incoherence appears only during later work. Immediate checks could accept either result.

The [delayed-feedback account](./program-theory-sustains-search-under-delayed-feedback.md) explains why passing a narrow check can conceal damage to the program's organization. Training on immediate success may leave the later cost unrewarded. These are different questions: what prompts an author to generate useful structure, and [whether acceptance favors that structure](./weakly-discriminated-qualities-tend-to-be-underselected.md).

## Test continued modification

Follow humans and models through successive changes and recovery. Track when they introduce commitments, when reasoning failures appear, and whether those commitments help an independent contributor make later changes at comparable total cost.

The capacity explanation predicts reliable progress through more demanding changes before comparable commitments become necessary. The feedback-timing explanation predicts that follow-up work exposes failures the initial checks missed. Both effects could occur. If commitments arise only from instructions or learned conventions, rather than in response to difficulty, the proposed mechanism loses support.

## Consequence for fresh agents

A fresh agent invocation is already a later contributor. It retains general programming competence but must reconstruct project-specific understanding from the context it receives. Human contributors can also lose or disagree about unwritten commitments.

Writing commitments and their reasons down could preserve continuity. Code can show that behavior is centralized without saying whether future changes must keep it centralized. The [rationale-retention note](./design-rationale-must-preserve-unregenerable-decision-premises.md) explains this information gap. The records help when later contributors retrieve and use them.

## Scope

- Product requirements and enforced contracts can introduce structure independently of the author's reasoning difficulty.
- New demands may require revising commitments. The [commitment and capacity-building account](./theory-and-capacity-building-make-the-same-kind-of-commitment.md) treats refactoring as backtracking over a design commitment while preserving behavior other commitments depend on.
