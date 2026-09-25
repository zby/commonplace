---
description: "A world-models editorial separates information, causal prediction and agency, and points to representation revision without establishing a unified architecture."
type: kb/sources/types/ingest-report.md
source: https://static1.squarespace.com/static/5f29a430a2b6a34680879cc0/t/6a06392b70af613cf631f5d0/1778792747560/rsta.2024.0533.pdf
captured: "2026-09-24"
ingested: "2026-09-25"
capture: pdftotext
capture_scope: full-source
doi: "10.1098/rsta.2024.0533"
genre: conceptual-essay
snapshot_sha256: 9e915aed68252d59918e0b9b9c2f7e3affb3aa1fec3fdc2830de6f687df7b57f
domains: [world-models, learning-theory, agent-architecture, collective-intelligence]
learning_claims: true
---

# Ingest: World models and the hard problems of life–mind continuity

## Classification

A conceptual editorial introducing the 2026 Royal Society theme issue on world models in natural and artificial intelligence. Adam Safron and thirteen coauthors bring research perspectives from neuroscience, cognitive science, AI and complex systems. The article summarizes contributions and interprets their relationships; it supplies no additional data. Its scientific venue and author expertise make it a useful research map, but experiments described here remain secondary reports. The editors explicitly warn that their interpretations may differ from contributors' views.

## Summary

The editorial treats world models as a family of functions rather than one agreed architecture: retaining information about the world, predicting causal transitions, guiding interventions, modelling oneself, coordinating collectives and organizing narratives. It contrasts optimistic accounts of meaning and consciousness in language models with concerns about grounding, coherence and flexible generalization. Contributions span theory-based exploration and planning, goal-dependent representations, self-prediction as regularization, physical regulation, temporal coupling, social-learning incentives and scientific problem formulation. The editors lean toward the view that current foundation models lack sufficiently coherent causal models for human-like generality, while acknowledging that they represent information about the world. For Commonplace, the value is a map of distinct claims and mechanisms to investigate; the article does not establish a unified design or a general impossibility result for language-model agents.

## Quotes

No source quotes have been retained yet.

## Connections Found

The editorial is a conceptual comparison for [action-model consumption](../notes/an-action-model-matters-only-through-its-consumption-path.md): information about a world, prediction of its transitions and use of those predictions to select actions require different evidence. Its broad vocabulary makes the note's demand for an operative consumption path especially useful. The science contribution's distinction between optimization under a given representation and revision of the problem itself compares directly with [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md). This is a conceptual parallel, not an experiment isolating representation revision. Finally, embodiment, self-modelling and temporal coupling supply candidate functions for [human analogies without inherited component boundaries](../notes/human-analogies-suggest-functions-not-component-boundaries.md). Their coexistence in biological systems does not establish how a KB agent should allocate them among models, tools and retained artifacts.

## Learning Claims (our opinion)

The source brings together several learning mechanisms that should remain distinct. Its EMPA summary describes symbolic object and interaction models used to choose informative encounters, generate subgoals and plan through simulated futures. It reports sample-efficiency advantages over deep reinforcement learning baselines within structured video games. The reported comparison evaluates the compound architecture, including its object vocabulary, symbolic state descriptions, planner and exploration controller. It does not isolate those design choices or establish that the learner can replace them. Goal-induced state abstraction supplies a different idea: the summarized “telic states” group experience distributions by equal preference under a goal, making the representation depend on what distinctions matter for action. This is a proposal about how goals organize representation, not evidence that every useful representation must use that construction.

EMPA's operative, revisable symbolic models are a plausible comparison for [conjectural learning](../notes/definitions/conjectural-learning.md), but this editorial does not detail the criticism operations or isolate their contribution to improved capacity. The mapping therefore remains provisional. Symbolic objects and rules could also support [addressable theory](../notes/definitions/addressable-theory.md), but their symbolic form alone does not establish selective diagnosis and repair. Self-prediction regularization and dynamical entrainment are broader adaptation mechanisms; they do not establish formulated theories criticized for what they say. No definition change follows from placing all these mechanisms under world modelling.

The scientific-discovery discussion adds the most relevant conceptual pressure: a learner may optimize within a representation while leaving its domain, constraints and admissible explanations untouched. That matches Commonplace's distinction between improvement inside an effective update space and revision of its boundary. The social-learning simulations add a population-level warning: cheaper copying can reduce the production of fresh information. Their conclusion depends on the supplied learning costs, environmental change and update rules; it does not establish that AI assistance generally weakens knowledge production.

## Extractable Value

- **A vocabulary check for model claims** `[quick-win]`: separate information representation, causal prediction and action-conditioned use when assessing a proposed KB or agent model. The existing action-model note supplies the operative test; this editorial supplies a broad comparison context rather than new causal evidence.
- **Problem formulation as a learning target** `[deep-dive]`: the science contribution distinguishes optimizing a supplied problem from revising its domain and constraints. Its primary argument could sharpen the fixed-decomposition note, particularly what an outer learner must be able to change.
- **A concrete theory-guided learning lead** `[deep-dive]`: EMPA connects model revision, informative exploration and planning. The editorial's reported advantage belongs to that compound architecture in structured games; inspecting the primary study is necessary before treating it as evidence for retained theories or for alternative component boundaries.
- **Goal-relative distinctions and evidence renewal** `[just-a-reference]`: the telic-state and social-learning contributions identify two questions for future KB design work: which distinctions a task requires, and who continues acquiring fresh evidence when reuse becomes cheap. Neither summary establishes a Commonplace implementation choice.

## Limitations (our opinion)

The editorial's breadth is also its central limitation. Information-bearing state, causal understanding, self-prediction, biological self-maintenance and consciousness are not interchangeable properties. The article offers connections among them without one discriminating test that settles those connections. Its interpretations sometimes move from narrower results to claims about general intelligence, autonomous science or existential risk; those extensions are not measured outcomes here.

The summarized studies do not collectively compare alternative complete architectures. Leetspeak failures concern tested models and task conditions; they do not establish the absence of every relevant representation. Neural self-prediction results concern auxiliary training objectives and complexity measures, not demonstrated consciousness or cooperation. Lower error for transition and reward functions than value functions under equal network capacity does not by itself settle total planning cost or robustness. Such narrower comparisons require their primary papers before reuse as design evidence.

The topology argument particularly needs a justified mapping from locally interacting graph models to deployed transformer systems. Sequential token generation does not alone establish the relevant interaction topology, especially when attention, external memory, tools or controllers enter the system boundary. Likewise, a next-token training objective does not by itself characterize every computation a trained system can perform. Biological parallels can motivate functions and experiments, but, as the [human-analogy note](../notes/human-analogies-suggest-functions-not-component-boundaries.md) explains, resemblance does not warrant inherited component boundaries.

## Recommended Next Action

Create a focused ingest of Battleday and Gershman's *Artificial intelligence for science: the easy and hard problems* to assess its primary argument about revising representations against the fixed-decomposition note.
