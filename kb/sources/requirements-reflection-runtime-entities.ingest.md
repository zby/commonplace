---
description: "A 2010 design proposal reifies requirements as runtime objects and synchronizes them with architecture, providing structural lineage—not empirical evidence—for theory-mediated system learning."
source: https://doi.org/10.1145/1810295.1810329
captured: "2026-08-30"
capture: pdftotext
capture_scope: full-source
capture_url: https://publications.aston.ac.uk/id/eprint/19494/1/Requirements_as_runtime_entities.pdf
genre: scientific-paper
snapshot_sha256: e96ce4e4525f08ce520ee35344d44f0774c2013f8ad1125d74fecdb72a2ef1c3
ingested: "2026-08-30"
occasion: "Determine what this source establishes about runtime representations of a software system's own structure, behavior, requirements, goals, or architecture; how those representations are causally connected to adaptation; what remains designer-supplied or fixed; and what evidence supports the claims. This is source ingestion for positioning theory-mediated system learning, not a request to confirm that the source is its predecessor."
type: kb/sources/types/ingest-report.md
domains: [requirements-engineering, self-adaptive-systems, runtime-models, reflection]
---

# Ingest: Requirements Reflection: Requirements as Runtime Entities

## Classification

This is an ICSE 2010 scientific vision and design paper: it defines requirements reflection, sketches a two-stratum runtime architecture, and states research challenges rather than reporting a realized system or controlled evaluation. Author: researchers at Lancaster University and University College London working in requirements engineering, reflective middleware, goal modeling, and self-adaptive systems; the paper locates its proposal within those research literatures and the authors' related modeling work.

## Summary

The paper argues that requirements monitoring leaves a running system with low-level derived artifacts but not the high-level goals, assumptions, alternatives, and relationships that motivated them. It proposes reifying those requirements as first-class runtime entities in a goal-oriented meta-model, exposing operations for inspecting and changing them, and semantically synchronizing that requirements stratum with a reflective architecture stratum so changes on either side can affect or be checked against the other. It also proposes runtime reasoning about uncertainty and interactive multi-objective trade-offs. Read it as a concrete structural agenda for putting a software system's purposes on a causal path to adaptation, not as evidence that the architecture works or that the system learns its own requirements model.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper is the requirements-specific structural-lineage anchor for [Theory-mediated system learning combines runtime self-modeling with empirical theory refinement](../notes/theory-mediated-system-learning-combines-runtime-self-modeling-with-theory-refinement.md): it places an explicit model of a system's purposes and goal relations on a proposed causal path to changes in the running architecture, but supplies neither empirical theory refinement nor delayed read-back. It is also a conceptual precedent for [Reflection buys addressability](../notes/reflection-buys-addressability.md) and [Reflective coverage is graded across representational forms](../notes/reflective-coverage-is-graded-across-representational-forms.md), because its requirements and architecture strata expose different entities, operations, and a required transfer mapping. Compared with [Computational Reflection](./maes-computational-reflection-1988.ingest.md), it specializes causally connected self-representation to requirements and makes cross-stratum synchronization the central unsolved problem.

## Extractable Value

1. **A requirements-level self-model can be causally relevant without being a learned theory** -- The paper proposes runtime objects for goals, refinements, alternatives, assumptions, conflicts, and their links to architecture. This supplies the self-target and adaptation-path half of theory-mediated system learning while keeping the empirical theory-revision half distinct. [quick-win]
2. **The represented vocabulary determines the available questions and interventions** -- A KAOS-like meta-model would let a system navigate goal relations, identify responsible agents, inspect assumptions, and invoke operations such as adding, deleting, replacing, or assigning requirements and goals. This gives a concrete requirements-specific instance of runtime representation creating a control surface. [quick-win]
3. **Causal connection requires an explicit transfer mechanism between representations** -- The proposal separates requirements and architecture into strata, each with base and meta-levels, then requires semantic synchronization so a requirements change can generate architectural changes and an architectural change can be checked against requirements. Merely retaining goals does not establish this connection. [deep-dive]
4. **Most of the effective update space remains designer-supplied** -- The paper leaves the goal language and meta-model, exposed primitives, requirements-to-architecture mapping, monitoring boundary, uncertainty formalism, decision procedure, and human interaction policy to designers. Runtime reprioritization or replacement therefore occurs inside a fixed decomposition rather than revising the machinery that defines valid representations and adaptations. [deep-dive]
5. **The evidence supports historical positioning, not effectiveness** -- The paper offers a motivating vacuum-cleaner scenario, conceptual comparison with prior work, and a research agenda, but no implementation, benchmark, ablation, or outcome data. It can ground a lineage claim and sharpen a baseline; it cannot show that requirements reflection improves adaptation, explanation, safety, or learning. [just-a-reference]

## Limitations (our opinion)

The central mechanism is underspecified and untested. The paper does not define or evaluate the semantic synchronization that would translate a changed goal into safe architectural changes, nor does it show that reverse monitoring can diagnose which requirement should change. Its vacuum-cleaner case is illustrative, not evidence, and the proposed KAOS-derived representation may omit requirements or environmental phenomena that do not fit its designer-chosen ontology. Human participation is proposed for resolving multi-objective conflicts, but the allocation of authority, elicitation of preferences, and behavior under disagreement are not evaluated. Most importantly for theory-mediated system learning, the paper does not learn or empirically revise the requirements meta-model, synchronization rules, monitors, adaptation operators, or evaluation policy; it proposes reasoning and modification within that supplied structure.

## Recommended Next Action

Update [Theory-mediated system learning combines runtime self-modeling with empirical theory refinement](../notes/theory-mediated-system-learning-combines-runtime-self-modeling-with-theory-refinement.md) to replace its bare requirements-reflection DOI with this ingest and state explicitly that the paper supplies a proposed requirements-level self-model and synchronization obligation, while leaving empirical read-back, theory revision, and the adaptation decomposition designer-supplied.
