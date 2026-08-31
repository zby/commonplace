---
description: "Rainbow makes a runtime architectural model causally active in adaptation while leaving its vocabulary, goals, constraints, and strategies designer-supplied."
source: https://doi.org/10.1109/MC.2004.175
captured: "2026-08-30"
capture: pdftotext
capture_scope: full-source
capture_url: https://www.cs.cmu.edu/afs/cs/project/able/ftp/computer04/article.pdf
genre: scientific-paper
snapshot_sha256: 536a0d36c01cc849beae6a8353cb2082b0cdd6c8d8eadd4ebd663edc224b5841
ingested: "2026-08-30"
occasion: "Determine what this source establishes about runtime representations of a software system's own structure, behavior, requirements, goals, or architecture; how those representations are causally connected to adaptation; what remains designer-supplied or fixed; and what evidence supports the claims. This is source ingestion for positioning theory-mediated system learning, not a request to confirm that the source is its predecessor."
type: kb/sources/types/ingest-report.md
domains: [self-adaptive-systems, runtime-models, software-architecture, control-loops]
---

# Ingest: Rainbow: Architecture-Based Self-Adaptation with Reusable Infrastructure

## Classification

This is a scientific paper presenting an implemented software framework, two prototype case studies, a code-size reuse estimate, and a small controlled performance experiment.
Author: David Garlan, Shang-Wen Cheng, An-Cheng Huang, Bradley Schmerl, and Peter Steenkiste were Carnegie Mellon researchers in software architecture, self-adaptive systems, networking, and distributed systems; the article appeared in *IEEE Computer*.

## Summary

Rainbow moves a software architecture from design-time documentation into an external runtime control loop: probes and gauges update an architectural graph of components, connectors, properties, and constraints; a constraint evaluator detects undesirable states; and an adaptation engine executes prescribed strategies through translated operators and system effectors. The framework separates reusable monitoring, modeling, evaluation, and translation infrastructure from system-specific styles, concerns, mappings, operators, and strategies. Two prototypes illustrate this split, while a client-server testbed experiment reports recovery from overload and timing measurements show that the approach is best suited to slower, systemwide changes in systems that expose monitoring and modification hooks.

## Quotes

No source quotes have been retained yet.

## Connections Found

Rainbow is a technical basis and boundary case for [theory-mediated system learning](../notes/theory-mediated-learning-joins-self-modeling-and-theory-refinement.md): its runtime architectural model mediates observation, constraint evaluation, strategy choice, and intervention, but Rainbow does not revise the theory that determines what the model represents or how adaptation is chosen. It directly supports the claim that [an action model matters through its consumption path](../notes/an-action-model-matters-only-through-its-consumption-path.md), because gauges, the constraint evaluator, the adaptation engine, translators, and effectors form the causal path from represented state to system change. It also gives concrete evidence that [runtime structure determines governance control surfaces](../notes/runtime-structure-determines-governance-control-surfaces.md): probes, effectors, mappings, and system hooks delimit what the external controller can observe and alter. As a counterpoint to [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), its successful repairs occur inside developer-chosen types, properties, constraints, operators, strategies, thresholds, and system concerns; the evaluation does not compare or revise those choices.

## Extractable Value

1. **The runtime representation is structurally explicit but selective.** Rainbow represents components, connectors, hierarchy, current properties, and architectural constraints. Dynamic behavior is represented through prescribed operators and strategies; requirements and goals are encoded indirectly as selected system concerns, properties, thresholds, invariants, and strategy logic rather than as first-class revisable runtime entities. [quick-win]
2. **The architectural model is causally connected to adaptation.** System probes feed gauges, gauges update model properties, a constraint evaluator triggers the adaptation engine, strategies compose architectural operators, and translation mappings dispatch corresponding effector operations to the running system. This is an operational consumption path, not merely runtime documentation. [quick-win]
3. **Rainbow adapts configuration rather than learning its controller.** The effective update space contains model property values and permitted changes to the live system topology. There is no learned hypothesis class: the expressible observation-to-action mappings come from designer-authored constraints and strategy programs, and the model vocabulary, action basis, mappings, policies, thresholds, and centralized loop remain outside runtime revision. [deep-dive]
4. **Reuse stops at explicit system and concern boundaries.** The generic infrastructure is reused across both prototypes, while effectors and much adaptation knowledge remain system-specific; properties, mappings, types, rules, and operators become reusable only when architectural styles or concerns match. This makes the designer-supplied decomposition visible instead of treating the whole controller as generic. [just-a-reference]
5. **The evidence supports feasibility within the fixed design, not the design's necessity.** The paper reports two working prototypes, about 1.8 KLoC of nonreused adaptation and mapping material within a 102 KLoC framework, latency recovery in one overloaded client-server testbed, and layer-level adaptation timings for videoconferencing. It does not ablate the architectural representation, property set, operators, strategies, or external-control design, so improvement cannot establish that those fixed choices were preferable to alternatives. [experiment]
6. **Access and timescale are substantive control limits.** Rainbow assumes usable monitoring and modification hooks, relies on a centralized controller, and incurs seconds-scale detection and repair plus measured layer delays. The paper therefore positions architecture-based control for longer-term systemwide trends, not every kind of runtime response. [quick-win]

## Limitations (our opinion)

The evaluation is too narrow to support broad claims that an architectural model or reusable external controller is generally the best basis for adaptation. The two prototypes were built within the Rainbow decomposition, code size is only an approximation of reuse, and the reported performance intervention uses one client-server testbed and specific loads; no matched comparison isolates the architectural representation, prescribed strategies, or external control from simpler alternatives. The improvement therefore shows that the compound configuration could repair the tested system, not that its fixed signals, action basis, or observation-to-action mappings were necessary or well chosen, as [learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) cautions. The paper also leaves conflicts among concerns unresolved, assumes target-system access hooks, and acknowledges centralized control, scalability, single-point-failure, and repair-latency limits.

## Recommended Next Action

Update [Theory-mediated system learning combines runtime self-modeling with theory refinement](../notes/theory-mediated-learning-joins-self-modeling-and-theory-refinement.md) to route its Rainbow lineage claim through this ingest and distinguish Rainbow's fixed-model runtime adaptation from learning that can revise the theory defining the model and adaptation policy.
