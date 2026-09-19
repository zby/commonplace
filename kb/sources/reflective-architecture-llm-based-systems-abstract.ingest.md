---
description: "An abstract proposes formal social expectations and self-simulation around LLM decisions; theory revision and the reported alignment gains remain unestablished by the retained evidence."
source: https://www.trustworthyai.ca/publication/a-reflective-architecture-for-llm-based-systems/
captured: "2026-09-19"
capture: trafilatura
capture_scope: abstract
doi: "10.1109/ACSOS-C66519.2025.00029"
genre: scientific-paper
snapshot_sha256: 01c7bd0ac0a81c2cf7fade2e41d9f974317a8c343805cab27815c6b60e7ccd4d
ingested: "2026-09-19"
occasion: "Reconsider the learning paradigm from Popperian epistemology: compare the epistemic process, computational realization, changeable representations and tests, fixed-model learning, reflection, and supporting evidence."
type: kb/sources/types/ingest-report.md
learning_claims: true
domains: [computational-reflection, learning-theory, formal-expectations]
---

# Ingest: A Reflective Architecture for LLM-Based Systems

## Classification

An author-hosted abstract of a scientific paper published in the 2025 IEEE ACSOS Companion proceedings, pp. 61–68. It proposes an architecture and reports improved alignment without retaining the experimental methods or results.
Author: Parisa Salmani and Peter R. Lewis. The page supplies authorship, venue, and DOI; it does not provide enough information to assess the study's execution.

## Summary

Salmani and Lewis propose combining LLMs with formal models of social expectations and self-simulation. Expectation event calculus (EEC) represents expectations, events, and derived outcomes; simulation predicts consequences of possible actions so the agent can evaluate and revise a decision before acting. The authors frame this as reflection beyond linguistic self-commentary and claim improved alignment with human expectations. The abstract does not identify the tested comparison, effect size, assessment method, or which architectural choices were fixed, so the reported improvement cannot establish the contribution of EEC, simulation, or their combination.

## Quotes

No source quotes have been retained yet.

## Connections Found

This is a comparison case for [Reflective system](../notes/definitions/reflective-system.md), useful for separating an architecture that evaluates its decisions from one that revises its own theory. The abstract names an intended path from represented expectations and simulated consequences to changed decisions. It does not establish which system aspects are self-represented or how changes in those aspects update the representation. [Maes's computational reflection account](./maes-computational-reflection-1988.ingest.md) supplies that causal-connection test. The source therefore sharpens a reading question for the learning-paradigm comparison; it does not yet supply an established example of reflective theory refinement.

## Learning Claims (our opinion)

On the source's terms, adaptation occurs when internally predicted consequences and formal expectations cause the agent to refine a decision. This identifies a proposed decision-evaluation mechanism, not a documented learning rule. Neither persistent changes across decisions nor changes to LLM weights are specified.

Relative to [Theory refinement](../notes/definitions/theory-refinement.md), changing a decision after applying an expectation model may be theory use rather than theory revision. EEC supplies a formal representation, but the abstract does not state that expectation rules, simulation assumptions, or evaluation criteria are candidate repair locations. It also does not say whether any such edits persist. A Popperian interpretation would require distinguishing criticism of a proposed action from criticism of the expectations or predictive model used to assess it. Simulated consequences expose implications of a model; they do not alone establish an empirical error in that model. The capture leaves the relation between predicted consequences, observed outcomes, and revised commitments unresolved.

The [fixed-decomposition limitation](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) is consequently a question for the full paper, not a demonstrated defect. The abstract exposes possible actions and their predicted outcomes as inputs to evaluation but does not specify accessible histories, action compositions, permitted edits, or the effective hypothesis class. It is unknown whether the formal expectations and simulator can change. A fixed LLM could participate in a larger learning system through changing external representations, but this abstract establishes neither fixed weights nor that external learning path. It adds a concrete proposed realization of prospective decision criticism without warranting a revision of Commonplace's distinction between reflection, theory use, and theory refinement.

## Extractable Value

1. **Locate what criticism can change.** The proposed architecture makes candidate decisions answerable to formal expectations and simulated consequences. For the learning-paradigm comparison, it is a useful reference for asking whether criticism changes only the decision or also the representation and assessment criteria. The abstract leaves the latter open. [just-a-reference]
2. **Separate formal assessment from evidence about assessment.** EEC gives expectations an explicit representational role, but the reported alignment gain lacks a retained comparison and cannot identify the benefit of that choice. Examining the full study could distinguish conformance to encoded expectations from independently assessed human alignment. [deep-dive]

## Limitations (our opinion)

The retained source is only an abstract. It cannot establish the formal update rules, LLM configuration, simulation implementation, causal connection, persistence, benchmarks, controls, or human assessment procedure. No experimental contrast or ablation is recoverable, so no component can be credited with the claimed improvement. The central result might be explained by explicit constraint checking or extra decision effort; the capture supplies no comparison that rules those explanations out.

The authors' broad claim that LLM reflection is merely linguistic is a framing claim here, not an argument supported by retained evidence. Likewise, formal expectations need not be accurate or complete representations of human expectations. A system may reliably comply with encoded expectations while failing outside their scope. The abstract does not show whether disagreements can challenge those expectations or only reject candidate actions. These are limits on this ingest's evidence, not findings that the complete paper lacks the relevant mechanisms or tests.

## Recommended Next Action

Obtain a full-paper capture for a distinct ingest focused on whether observed failures revise EEC expectations or simulation assumptions, and on the experimental comparison supporting the alignment claim.
