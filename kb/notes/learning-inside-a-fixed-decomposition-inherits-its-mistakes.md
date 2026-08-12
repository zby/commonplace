---
description: "Why optimization cannot repair consequential distinctions, responses, or mappings outside the effective update space of a fixed task decomposition"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [learning-theory, deploy-time-learning]
---

# Learning inside a fixed decomposition inherits its mistakes

A learning system can change only what its effective update space can express. Before learning begins, a fixed decomposition has already divided the domain into learner-accessible signals and histories, memory units, permitted operations, hypothesis classes, subproblems, or feedback categories. The decomposition contains a consequential mistake when the required correction falls outside that space: no accessible signal or history preserves a needed distinction, no composition of permitted actions produces a needed response, or the hypothesis class cannot express a needed mapping. Optimization can fit every available choice and still cannot repair such an omission.

This is a causal limitation, not merely a validation problem. [Evaluation cannot select a candidate that search never reaches](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md), but a decomposition does more than exclude candidates: it helps determine what can count as a candidate at all. Its effective boundary is therefore broader than its named coordinates. It includes distinctions recoverable from history or learned latent state and responses constructible from the permitted action basis. A stronger learner may enlarge the effective space behind an unchanged interface. The limitation applies only to corrections that remain outside this enlarged space.

## Decomposition errors become unreachable in three ways

An **information omission** collapses cases that require different responses. If every signal and history available to a learner represents two situations identically, even though the objective requires different actions, every policy over that information must treat them alike. More data and a better optimizer can estimate the best compromise more accurately; neither can recover the erased distinction. Equal current observations are not enough to establish this failure, because a recurrent learner may distinguish the situations from their histories. Hand-designed vision features exhibited the stronger failure when their outputs discarded task-relevant information: the detectors could be implemented exactly, while the claim that their outputs retained what seeing required remained a conjectured link to the objective ([exact implementation does not validate an upstream requirement](./exact-implementation-does-not-validate-a-requirement.md)).

An **action-closure omission** preserves enough evidence to recognize the difference but leaves the needed response outside every permitted composition. Merely omitting a response as a primitive is insufficient: if the learner can implement it exactly and reliably by composing its available actions, then the response remains inside its effective space. If only a costly or approximate construction is available, the decomposition may impose a sample-efficiency, robustness, or execution penalty. That is an empirical handicap, not an impossibility.

A **hypothesis-class omission** preserves both the relevant information and the available responses but excludes the mapping between them. A linear policy facing a non-linearly separable target is the simplest case: no input distinction has been erased and no output action is missing, yet the required conditional choice remains unrepresentable. Subproblem boundaries can produce any of these three failures when they block information, credit, actions, or mappings across a seam. In every case, the learner adapts choices *within* the admitted space while the consequential mistake remains outside it.

## Improvement inside a boundary does not test the fixed layer

Successful optimization changes downstream variables while the fixed signals, actions, and hypothesis class remain controlled conditions. Improvement therefore shows that the compound configuration sufficed in that context; it does not isolate which fixed choices were necessary or preferable. As [use tests a decomposition only locally](./use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md), alternatives excluded before the run leave no comparison in its result.

Changing the model behind the same explicit interface becomes informative only after comparing the models’ effective update spaces. Internal memory, learned latent state, general-purpose tools, or reliable action composition may let one model recover distinctions or responses that another cannot. Yet neither result tests whether a different representation, action basis, or partition would work better. When such choices are free rather than imposed by independently supported constraints, they begin without a warranted scope claim and must remain revisable ([an underdetermined choice gives no starting scope warrant, and only discriminating evidence or proof earns scope](./derivation-and-inheritance-give-starting-warrant-earns-scope.md)).

## The relevant Bitter Lesson boundary is the effective update space

The relevant contrast is not human structure versus learning in the abstract. It is structure exposed to revision versus structure treated as an immutable coordinate of learning. [The Bitter Lesson argument selects against generalizations whose reach was asserted rather than tested](./bitter-lesson-selects-against-unearned-reach-not-against-structure.md). Moving search into a controller or harness does not answer that criticism if consequential task categories, distinctions, operations, or mappings remain fixed one layer above it.

The practical unit of analysis is therefore the effective update space. For any learning result, ask which signals and histories can condition behavior, which responses can be composed, which mappings the hypothesis class can express, and which artifacts or partitions can change in response to error. Improvements inside that set do not vindicate choices outside it. If an external choice is consequential and not fixed by the problem, it remains a candidate for broader learning, deliberate redesign, external search, or validated engineering.

## ACM and Meta-Harness expose the fixed layer at different boundaries

[ACM, an agentic context-management approach](../sources/acm-agentic-context-management-for-long-horizon-tasks.ingest.md), learns when to use a supplied two-operation scheme: summarize and archive an earlier chronological prefix, then query archived messages by identifier. Its policy can improve invocation and abstention within that scheme, but it cannot replace chronological prefix compression with a different state representation. The reported gains show that the compound system worked on its benchmarks. Without rival decompositions, they do not show that the supplied operations defined the right learning space.

[Meta-Harness's summaries-hurt ablation](./the-meta-harness-ablation-bounds-summarization-not-theory-formation.md) examines an outer-loop system that searches task-specific LLM harness code. The experiment fixes a different decomposition of evidence: scores only, scores plus a consumer-blind summary that replaces traces, or access to the raw traces. The feedback representation and summarizer remain outside harness search. Here the fixed choice produces an observed failure: the supplied summary treatment underperforms raw traces. This result shows that the summarize-and-discard representation lost useful distinctions for this proposer and task. It does not establish rawness as the general cause or show that every derived representation has the same defect, because episode-backed, query-conditioned, and jointly searched representations were unavailable.

The common structure is not that both systems use summaries. ACM fixes the agent’s context-management actions; Meta-Harness fixes the outer learner’s evidence treatments. Both optimize within an update space while consequential alternatives remain outside the experiment.

## Scope

- Fixed does not mean mistaken. A decomposition derived from constitutive rules, hard dependencies, or independently supported constraints may provide exactly the stability a learner needs. The claim concerns mistakes within fixed decompositions, not fixedness itself.
- A nominally fixed interface may still admit a correction through raw inputs, informative histories, learned latent state, general-purpose tools, or reliable action composition. In those cases, the correction lies inside the effective update space, although reaching it may still carry empirical costs.

## Open Questions

- Can an outer loop learn decompositions without merely relocating the same problem into a fixed meta-decomposition? What evidence would show that its revision boundary is broad enough?

---

Relevant Notes:

- [Diagnostic richness constrains outer-loop learning quality](./diagnostic-richness-constrains-outer-loop-learning-quality.md) — contrasts: distinguishes an inadequate evidence surface from an update space that cannot express the correction
- [Feedback-trained memory management is oracle-dependent even when its operations are hand-designed](./memory-management-policy-is-learnable-but-oracle-dependent.md) — contrasts: separates selection-signal quality from adequacy of the supplied state and action space
- [Machinery persists by warrant, not position, in a reflective loop](./machinery-persists-by-warrant-not-position-in-a-reflective-loop.md) — extends: puts meta-method machinery inside the revisable artifact set while retaining warranted constraints
- [Ingest: Co-Harness: Co-Evolving Harnesses and Model Weights for LLM Agents](../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md) — evidenced-by: broadens the update space across prompts, tools, skills, middleware, memory, and model weights
