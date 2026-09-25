---
description: "Procedural Graphs combine localized action guidance with validated graph revision; their experiments separate consumption choices while leaving the surrounding learning machinery fixed."
type: kb/sources/types/ingest-report.md
source: https://arxiv.org/abs/2609.09153
captured: "2026-09-21"
ingested: "2026-09-21"
capture: pdftotext
capture_scope: full-source
doi: "10.48550/arXiv.2609.09153"
genre: scientific-paper
snapshot_sha256: 744632dd6e1db58a0d479d8ae8134e7573416e444eaed517b1c64a471359693c
domains: [context-engineering, procedural-memory, agent-learning]
learning_claims: true
---

# Ingest: Procedural Graphs: Self-Evolving Execution Structures for LLM Agents

## Classification

Scientific paper: an arXiv preprint by Yuxing Lu, Yicheng Chen, Shanchan Wu, and Sercan Ö. Arık, with Google, Georgia Institute of Technology, and Peking University affiliations. It specifies an agent-guidance mechanism, an offline graph-refinement algorithm, benchmark comparisons, construction studies, and a consumption ablation. The authors developed the evaluated system; the reported results are their evidence, not an independent reproduction.

## Summary

[Procedural Graphs](https://arxiv.org/abs/2609.09153) store tool actions, reasoning steps, and states as nodes connected by transitions with conditions, guidance, and pitfalls. At each solver step, exact matching of the last procedure selects a two-hop outgoing neighborhood; a guidance model interprets that neighborhood with the query and recent history, then supplies advice to the solver. Failed matching loads the full graph. An offline refiner proposes graph edits from scored trajectories, retaining structurally valid candidates whose measured validation score does not decrease. With a shared ReAct solver and adapted memory baselines, the combined system ranks first or joint first in 21 of 24 model–benchmark settings. Its most useful design evidence is narrower: holding the graph and solver template fixed, localized generative guidance outperforms full-graph consumption on three benchmark subsets, while still consuming more tokens than the no-graph baseline. Construction studies show that iterative graph revision can repair a harmful expert prior within a fixed tool, guidance, and evaluation setup; they do not test whether that surrounding decomposition is preferable to alternatives.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper supplies empirical evidence for [an action model mattering through its consumption path](../notes/an-action-model-matters-only-through-its-consumption-path.md). Its operative path is graph neighborhood → generated advice → solver prompt → action. Table 3 varies how the same graph enters that path, making consumption a tested design choice. On ALFWorld, full-graph generative guidance scores 54.48% success, below the 72.58% no-graph baseline, while localized generative guidance reaches 81.53%. This supports the importance of the tested access mechanism; it does not establish graph structure itself as the cause or compare every localization/generation combination.

The selector is a concrete instance of [rule-based context selection needing a pre-existing signal](../notes/rule-based-context-selection-needs-a-pre-existing-signal.md): the last procedure's identifier supplies the matching signal, full-graph fallback supplies a bounded superset, and the guidance model performs the remaining situational interpretation. This separates cheap localization from inference about which transition applies.

The retained checkpoint is also evidence for [a retained instruction preserving what testing selected](../notes/a-retained-instruction-preserves-what-testing-selected.md). Candidate procedures come from a frozen model, but validation chooses which graph later tasks consume. The construction results support the usefulness of that retained choice within the tested architecture; they neither validate the refiner's explanations nor establish transfer beyond the measured tasks.

## Learning Claims (our opinion)

The source's learning mechanism is external graph revision. The refiner receives the current graph, scored training trajectories, and serialized rejected candidates. It adds and deletes nodes and edges; replacing an edge revises its textual attributes. Structural checks precede validation rollouts. A candidate is accepted on a non-decreasing mean validation score, including ties; otherwise the incumbent and its cached score remain. Rejection records enter later proposals as negative evidence. The graph is frozen within episodes and during test evaluation. The construction tables' phrase “online evolution” means updates between training batches, not adaptation during deployment.

The graph is a plausible mixed-form [addressable theory](../notes/definitions/addressable-theory.md): procedural commitments can be inspected and edited individually while retaining others. Against the [theory-builder definition](../notes/definitions/theory-builder.md), the graph meets condition 1, and it meets condition 2: the consumption ablation shows that what the graph says, delivered through localized guidance, changes the solver's actions. Condition 3 is unestablished. The refiner proposes edits from scored trajectories and rejection records, and a validation score decides acceptance, so the report does not distinguish a formulated reason bearing on the graph's content from score-driven selection. Formal graph checks compute structural properties, while models interpret prose conditions and advice; task outcomes assess the combined graph-and-consumer configuration without identifying which commitment was wrong. Condition 4 is met within a construction run: the accepted graph and the rejection records are the starting point of later proposals, and each candidate is tested again on validation rollouts. Condition 3 therefore decides: PG is not shown to be a theory builder, and would be one at the grade of rounds within one run if its edits were shown to aim at what the graph says. The graph is then frozen for testing, which ends the builder; runtime guidance applies the retained procedure rather than criticizing it, and cross-solver and cross-interface transfer is future work. Existing-graph revision and construction from a minimal skeleton are both compatible with a theory builder; neither establishes one here. Improved capacity within the tested benchmarks is a separate learning claim, considered next.

The evidence strengthens the claim that editable procedural artifacts can mediate persistent improvement without changing model weights. For example, on the 56-item MultiChallenge construction split, the expert graph reduces success from 87.50% to 58.93%, while iterative refinement reaches 92.86%. That comparison bundles fresh feedback, repeated mutation, and validation gating; it does not isolate which component caused recovery. Rejection memory has a specified consumption path but no separate ablation establishing its benefit.

The effective revision boundary matters, as in [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md). PG exposes graph topology and attributes to change, including tool ordering and memory-tool use. It leaves the tool interface, localization rule, guidance/refiner machinery, evaluation criteria, and data partition outside that loop. The gains show that useful corrections were expressible inside this boundary. They do not show that the fixed choices are mistaken, necessary, or optimal. No revision of Commonplace's definition is required by this evidence; PG provides a concrete case with an explicit boundary and outcome checks.

## Extractable Value

- **Consumption needs its own comparison [quick-win].** Table 3 tests full-graph raw injection, full-graph generated guidance, and localized generated guidance using the same graph and solver template. The local configuration performs best on all three subsets. This is useful evidence for the existing action-model note because it separates retaining a representation from choosing how to consume it. The absent localized raw-injection arm prevents a complete attribution to localization, generation, or their interaction.
- **Rule matching and situational interpretation can occupy different stages [quick-win].** Exact procedure matching retrieves a connected neighborhood; a model then interprets its attributes against recent history. This makes the activation mechanism reusable as a design example where stable action identifiers exist, without assuming they capture all relevant task state.
- **A retained graph can preserve tested procedural corrections [quick-win].** The construction study demonstrates recovery from a harmful expert prior under iterative feedback and validation within the fixed architecture. This supplies an empirical case for retaining evaluated procedures, while preserving the distinction between successful whole-configuration changes and verified explanations of those changes.
- **Guidance has a measurable cost tradeoff [experiment].** Localized guidance uses fewer tokens than full-graph generative guidance but more than the no-graph baseline. On GDPval it reduces solver steps from 28.20 to 18.57 while increasing total tokens by 33.4%; on ALFWorld it reduces steps from 21.84 to 18.80 while increasing tokens by 55.4%. Any Commonplace transfer should compare task quality and total consumption, not treat fewer solver steps as cost savings.

## Limitations (our opinion)

The main comparisons share a solver, tools, and decoding configuration, but change both the stored artifact and its consumption mechanism. They test compound configurations, not a representation-only contrast. The consumption ablation narrows that question but omits localized raw injection and does not report a matched alternative decomposition of the learning system. Baselines are the paper's adaptations; their results should not be read as measurements of every original implementation.

The graph advises the solver; it does not enforce execution conformance. Appendix B.6 checks edge endpoints and reachability to a zero-out-degree terminal, which need not be the node named `End`. Tool-catalog membership is requested in the refiner prompt rather than independently checked by the generic structural validator. Appendix B.5 also states that the illustrated local serializer omits stored relation labels. Stored semantics therefore need not all reach the guidance model.

Validation selects on repeatedly used data and compares a newly measured candidate against a cached incumbent score. A non-decreasing observed score does not guarantee a non-decreasing expected score. The EnterpriseArena evolution study uses only 20 episodes per split; its returned graph achieves 85% test survival, while 95% is an intermediate observed peak and must not replace the returned result. The paper itself treats individual acceptance decisions as a search trace rather than significance tests.

Construction modes bundle iteration with feedback and acceptance safeguards, leaving the independent value of rejection memory and diagnostic explanations unresolved. Some evaluation uses LLM judges. Cross-solver and cross-tool-interface transfer remains future work, and no reported experiment directly tests agent-operated KB authoring or maintenance. This ingest uses the paper only; no implementation was inspected or executed, and the reported outcomes were not reproduced.

## Recommended Next Action

Update [An action model matters only through its consumption path](../notes/an-action-model-matters-only-through-its-consumption-path.md) with the same-graph Table 3 comparison, retaining the missing localized raw-injection arm and guidance-token overhead as limits on what it establishes.
