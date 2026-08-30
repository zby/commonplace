---
description: "A 2010 research agenda extends requirements reflection into runtime model evolution, uncertainty, trade-offs, and explanation, supplying structural lineage rather than outcome evidence."
source: https://doi.org/10.1109/RE.2010.21
captured: "2026-08-30"
capture: pdftotext
capture_scope: full-source
capture_url: https://publications.aston.ac.uk/id/eprint/19491/1/Requirements_aware_systems.pdf
genre: scientific-paper
snapshot_sha256: 9c607c857eee482bb1aa921541059d040ab9fc50bcf9fee22bf9734f72a8c34a
ingested: "2026-08-30"
occasion: "Determine what this source establishes about runtime representations of a software system's own structure, behavior, requirements, goals, or architecture; how those representations are causally connected to adaptation; what remains designer-supplied or fixed; and what evidence supports the claims. This is source ingestion for positioning theory-mediated system learning, not a request to confirm that the source is its predecessor."
type: kb/sources/types/ingest-report.md
domains: [requirements-engineering, self-adaptive-systems, runtime-models, reflection]
---

# Ingest: Requirements-Aware Systems: A Research Agenda

## Classification

This is a scientific research-agenda paper from the 2010 IEEE Requirements Engineering Conference. It synthesizes prior requirements-engineering and self-adaptive-systems work into a proposed architecture and five research challenges; it does not report an implementation or an evaluation of requirements reflection. Author: five Lancaster University and University College London researchers working across requirements engineering, goal modeling, reflective middleware, and self-adaptive systems, with the paper's argument grounded in those literatures and the authors' related RELAX work.

## Summary

The paper argues that a self-adaptive system operating in a volatile, imperfectly understood environment should keep its requirements model as a runtime entity rather than as passive design-time documentation. Its proposed requirements stratum exposes goals, assumptions, alternatives, conflicts, responsibilities, and satisfaction relations for inspection and manipulation, while semantic synchronization with a reflective architecture stratum is meant to carry requirements changes into system reconfiguration and check architectural changes against requirements. The resulting agenda covers runtime representation, model evolution and synchronization, uncertainty, multi-objective choice, and self-explanation. Read it as a detailed conceptual map of requirements-aware adaptation and its unresolved dependencies, not as evidence that the proposed causal loop works.

## Quotes

No source quotes have been retained yet.

## Connections Found

Its primary role is a companion expansion of [Requirements Reflection: Requirements as Runtime Entities](./requirements-reflection-runtime-entities.ingest.md), not an independent confirmation: it substantially repeats the runtime-object and two-stratum proposal while adding a five-part agenda and fuller treatments of uncertainty, interactive trade-offs, and explanation. For [Theory-mediated system learning combines runtime self-modeling with empirical theory refinement](../notes/theory-mediated-system-learning-combines-runtime-self-modeling-with-theory-refinement.md), it is a requirements-specific structural basis and limitation: a representation of the running system's own goals and assumptions is placed on a proposed causal path to architectural change, but no empirical theory-refinement or independently evaluated read-back loop is supplied. Its designer-set modeling language, monitors, transformation operators, and cross-stratum mappings also make it a concrete comparison for [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md).

## Extractable Value

1. **The proposed runtime self-representation is broader than a list of requirements** -- A goal-oriented meta-model is expected to represent stakeholder goals, functional and non-functional requirements, alternative operationalizations, domain assumptions, scenarios, risks, obstacles, conflicts, responsible agents, and traceable relationships. This identifies the aspects of the system's purposes that the paper wants humans and software to address at runtime. [quick-win]
2. **Causal connection requires a closed path through monitoring, choice, enactment, and synchronization** -- Environmental and behavioral observations update judgments about requirement satisfaction; the system then evaluates available adaptations and trade-offs, enacts an architectural change, and monitors its effects. A separate semantic mapping must propagate requirements changes into architecture and check architecture changes against requirements, so storing or querying a goal model alone does not realize requirements reflection. [deep-dive]
3. **The effective update space includes goal operations but excludes most adaptation machinery** -- The proposed primitives can add, delete, or replace requirements and goals, reassign agents, choose alternatives, relax satisfaction, and trigger component reconfiguration. The goal language and meta-model, sensed variables, monitoring boundary, valid component set, transformation library, requirements-to-architecture semantics, uncertainty formalism, decision procedure, and explanation policy remain designer-supplied; the paper gives no mechanism for learning or replacing them from outcomes. [deep-dive]
4. **The paper's distinct value over its same-year predecessor is agenda breadth** -- It organizes requirements awareness into five linked challenges and develops the roles of graded conformance, user-involved multi-objective choice, traceable adaptation histories, and why/why-not explanation. This makes it the better source for unresolved research obligations, while the earlier paper already owns the core runtime-object architecture in the KB. [quick-win]
5. **The evidence establishes a motivated proposal, not adaptive effectiveness** -- The paper combines prior literature, illustrative systems and scenarios, a proposed meta-object structure, and RELAX's formal semantics. It reports no requirements-reflection implementation, benchmark, ablation, or outcome data; it explicitly notes that RELAX had no runtime-monitoring implementation, and the cited explanation experiment evaluates another context-aware-system setting rather than this architecture. [just-a-reference]

## Limitations (our opinion)

The causal center of the proposal—semantic synchronization between changing requirements and a running architecture—is named but neither specified enough to implement nor tested. The examples show why runtime trade-offs could be useful, not that the proposed representation selects safe or effective adaptations. RELAX contributes a designer-authored uncertainty vocabulary and formal semantics, but the paper says its runtime monitoring was not implemented. Evidence cited for explanation preferences comes from a different kind of context-aware system and cannot establish that explanations derived from interacting goal and architecture models improve trust or understanding. The agenda also assumes that designers can expose the relevant goals, assumptions, measurable parameters, candidate adaptations, and model relationships; it places wholly unframeable uncertainty outside scope and does not show how genuinely new requirements or defects in that decomposition would be discovered. It therefore cannot support claims of system learning, empirical theory revision, safety, or performance improvement.

## Recommended Next Action

Revise the runtime-self-modeling section of [Theory-mediated system learning combines runtime self-modeling with empirical theory refinement](../notes/theory-mediated-system-learning-combines-runtime-self-modeling-with-theory-refinement.md) to cite this ingest alongside the earlier requirements-reflection ingest and distinguish this paper's five-part research agenda from the shared, still-unevaluated runtime-object architecture.
