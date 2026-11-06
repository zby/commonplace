---
description: "Conjecture about structural differences between correct human and model implementations: reasoning needs may introduce commitments whose value appears during later changes."
type: types/note.md
traits: [title-as-claim]
tags: [architecture, evaluation, agent-memory, learning-theory]
---

# Reasoning limits may select for design commitments

Consider human-written and model-written code that both meet the current requirements. A human may need additional structure to understand the code well enough to write the next part. An LLM may produce a larger correct change without needing the same structure. Maintainability could therefore be a by-product of the human author's reasoning needs, even when it is not an explicit goal.

A **design commitment** restricts acceptable future implementations: one component owns a state transition, validation happens at a particular boundary, or two subsystems remain independent despite duplicated code. An unwritten commitment is one the author relies on without recording it as a shared requirement. The author may never have stated it as a rule.

The proposed human–LLM difference is an untested conjecture.

## The need to continue can produce useful structure

An author may find it difficult to track all the interactions involved in a change. Boundaries, conventions, or abstractions can make that work manageable. The author then relies on these commitments to continue constructing correct code.

The benefit need not have been selected directly as a maintainability objective. The immediate pressure is to make the next part of the implementation possible. General practices such as SOLID leave many of these project-specific choices unresolved.

One possible benefit is compression. If all state changes pass through one function, a contributor can track that rule instead of remembering each path independently. Jürgen Schmidhuber's [Formal Theory of Creativity, Fun, and Intrinsic Motivation](../sources/schmidhuber-formal-theory-creativity.ingest.md) measures compression cost using both the predictor and deviations from its predictions. Our application is that a commitment helps when its rule and exceptions cost less to track than the separate facts.

## Correctness can leave the structural difference unrewarded

A model that can construct a correct solution without the commitments a human needs lacks that immediate reason to introduce them. Both solutions meet the current requirements, but they may leave different amounts of reasoning for the next contributor. For example, several implementations of a state transition may agree on all current behavior while leaving later contributors responsible for finding and updating each one.

Training that rewards current correctness may provide little incentive for commitments whose benefit appears only during later modification. The [delayed-feedback account](./program-theory-sustains-search-under-delayed-feedback.md) explains why later demands matter to evaluating coherent modification. This note asks what prompts useful structure during construction; the [underselection account](./weakly-discriminated-qualities-tend-to-be-underselected.md) asks whether acceptance favors it once proposed.

## Fresh agents are later contributors

A fresh agent invocation retains general programming competence but must reconstruct project-specific understanding from the context it receives. Human contributors can also lose or disagree about unwritten commitments.

Recording commitments and their reasons could preserve continuity across invocations. Code can show that behavior is centralized without saying whether future changes must keep it centralized. The [rationale-retention note](./design-rationale-must-preserve-unregenerable-decision-premises.md) explains this information gap. The records help when later contributors retrieve and use them.

## Test later work on correct implementations

Compare humans and models implementing the same requirements, retaining implementations that actually meet those requirements. Record when authors introduce commitments and what reasoning difficulty precedes them. Then compare the cost and reliability of further changes, including work by independent contributors, at comparable total cost.

The conjecture predicts that humans introduce useful commitments at a lower level of interaction complexity than models need them. It also predicts that those commitments reduce later modification cost or errors. Evidence for the first without the second would explain a difference in construction without establishing a maintainability benefit. If commitments arise only from instructions or learned conventions, rather than in response to difficulty, the proposed mechanism loses support.

## Scope

- The comparison concerns initially correct implementations.
- Commitments need not help later work: restrictions that suit one author can hinder others, and elaborate rules with many exceptions can cost more than they save.
- Product requirements and enforced contracts can introduce structure independently of the author's reasoning difficulty.
- New demands may require revising commitments. The [commitment and capacity-building account](./theory-and-capacity-building-make-the-same-kind-of-commitment.md) treats refactoring as backtracking over a design commitment while preserving behavior other commitments depend on.
