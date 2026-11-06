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

The benefit need not have been selected directly as a maintainability objective. The immediate pressure is to keep programming. General practices such as SOLID leave many of these project-specific choices unresolved.

One possible benefit is compression. If all state changes pass through one function, a contributor can track that rule instead of remembering each path independently. Jürgen Schmidhuber's [Formal Theory of Creativity, Fun, and Intrinsic Motivation](../sources/schmidhuber-formal-theory-creativity.ingest.md) measures compression cost using both the predictor and deviations from its predictions. Applied to code, the conjecture is that a commitment helps when its rule and exceptions cost less to track than the separate facts.

## Reorganizing partial work is a separate capability

The need for structure is one part of the account. Two others are the opportunity to reconsider partial work and the learned response to difficulty.

Human authors can alternate writing with reconsideration: write part, work out what comes next, reorganize, then continue. A model producing a whole change in one pass has fewer opportunities to reorganize unfinished work. Agents can alternate edits and inspection, but checking for errors may leave the design unchanged.

The relevant capability is to notice difficulty continuing, introduce a small local commitment, and resume work under it. Refactoring when explicitly asked starts from a different position: restructuring is already the objective.

A prompt to think before continuing supplies an opportunity; it may not elicit this response. One hypothesis is that training examples favor refactoring as a whole task over these intermediate adjustments. A final diff can show the resulting structure without showing when it was introduced or why. The distribution of such examples in model training is unknown.

## Correctness can leave the structural difference unrewarded

Whichever process produced the code, correct implementations can impose different demands on later contributors. For example, several implementations of a state transition may agree on current behavior while requiring later contributors to find and update each one. A commitment to one owner could reduce that work.

Training that rewards current correctness may provide little incentive for commitments whose benefit appears only during later modification. The [delayed-feedback account](./program-theory-sustains-search-under-delayed-feedback.md) explains why later demands matter to evaluating coherent modification. This note asks what prompts useful structure during construction; the [underselection account](./weakly-discriminated-qualities-tend-to-be-underselected.md) asks whether acceptance favors it once proposed.

## Fresh agents are later contributors

A fresh agent invocation retains general programming competence but must reconstruct project-specific understanding from the context it receives. Human contributors can also lose or disagree about unwritten commitments.

Recording commitments and their reasons could preserve continuity across invocations. Code can show that behavior is centralized without saying whether future changes must keep it centralized. The [rationale-retention note](./design-rationale-must-preserve-unregenerable-decision-premises.md) explains this information gap. The records help when later contributors retrieve and use them.

## Proposed test

An experiment could follow humans and models through a sequence of changes to examine when commitments arise and whether they help later work. Participants would implement the same requirements. The study would retain correct implementations, record when commitments are introduced and what difficulty precedes them, and measure the cost and reliability of later changes by original authors and independent contributors.

With matched resource budgets, the model comparison could include:

- **One-pass construction.** Produce the implementation in one pass.
- **Neutral reconsideration.** Pause to inspect partial work without being asked to add structure.
- **Guided reconsideration.** Pause with explicit guidance to examine and revise local commitments.

The capacity hypothesis predicts that models can handle more interacting behavior than humans before needing comparable commitments. The staged conditions would test whether opportunities and guidance change which commitments models introduce. If only guided reconsideration produces commitments that help later work, a pause alone is insufficient; the cause could still be something other than the proposed training-data gap.

A difference in structure would establish a maintainability benefit only if it improves later modification. If commitments arise only from instructions or conventions, rather than in response to difficulty, that weakens the proposed difficulty-driven mechanism. This is an experiment sketch; measures of interaction complexity, reasoning difficulty, and resource matching remain to be specified.

## Scope

- The comparison concerns initially correct implementations.
- Commitments need not help later work: restrictions that suit one author can hinder others, and elaborate rules with many exceptions can cost more than they save.
- Product requirements and enforced contracts can introduce structure independently of the author's reasoning difficulty.
- New demands may require revising commitments. The [commitment and capacity-building account](./theory-and-capacity-building-make-the-same-kind-of-commitment.md) treats refactoring as backtracking over a design commitment while preserving behavior other commitments depend on.
