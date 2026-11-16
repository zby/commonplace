---
description: "Zave and Jackson ground requirements in environmental phenomena and derive implementable specifications using domain assumptions, without settling goal authority or assumption revision."
source: https://www.pamelazave.com/4dc.pdf
captured: "2026-11-16"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: c099591707df1352d907aca025aff617e9464d096a3c09585f569746b68e3704
ingested: "2026-11-16"
occasion: "What can requirements engineering contribute, and what are its limits, for understanding operationalization, goal authority, and revisable knowledge in agent-operated knowledge work?"
type: types/ingest-report.md
domains: [requirements-engineering, environmental-assumptions, operationalization, control-and-observability]
---

# Ingest: Four Dark Corners of Requirements Engineering

## Classification

A theoretical software-engineering paper supported by formal distinctions, worked examples, and criticism of existing specification approaches, not an empirical evaluation. Authors: Pamela Zave and Michael Jackson, affiliated in the captured manuscript with AT&T Research and, for Jackson, MAJ Consulting Limited. The capture is their manuscript dated 16 July 1996; it does not establish the exact text or pagination of the subsequently published 1997 article.

## Summary

Zave and Jackson argue that requirements engineering should describe the environment of a proposed computer-based machine, rather than its internal implementation. Primitive terms need written informal meanings grounded in environmental phenomena, called designations; formally defined terms derive their meanings from those primitives. Statements distinguish indicative properties, describing environmental facts or assumptions, from optative properties, describing desired environmental behavior. Actions must separately identify control and observability. These distinctions explain how requirements R become implementable specifications S through domain knowledge K, with the central obligation S, K ⊢ R. The paper diagnoses three obstacles to direct implementation: constraining environment-controlled actions, depending on unshared information, and referring to the future. Turnstile, lift, banking, inventory, and telephone examples show how environmental relationships can bridge these gaps, or force requirements to change. Its completion criteria combine informal validation of R and K with implementability, satisfaction, and consistency checks. Formal completion therefore remains conditional on the environmental descriptions and customer judgments being adequate.

## Contribution assessment (our opinion)

The paper appears to make a substantial conceptual contribution to a foundational problem: a specification can be internally precise yet omit the environmental relationships needed for its implementation to achieve the desired result. Its strongest addition is the integration of grounding, grammatical mood, control, and observability into explicit satisfaction and completion obligations. The examples expose concrete errors in conflating assumptions with machine constraints and distinguish several reasons a requirement is not implementable. Comparisons with contemporary formalisms help make these claims criticizable, but do not independently establish the authors' priority claim or universal applicability. The absence of empirical evaluation limits claims about practical effectiveness, not the usefulness of the distinctions themselves; the broader claim of a complete foundation remains conditional on informal validation and the proposed environment–machine boundary.

## Quotes

No source quotes have been retained yet.

## Connections Found

For the occasion, this source is a **formal boundary comparison** with [Exact implementation does not validate a requirement against its objective](../theory/exact-implementation-does-not-validate-a-requirement.md). It makes one intervening obligation explicit: even a correct implementation of S needs environmental knowledge K to establish R. Its completion criteria then require separate informal validation of both customer requirements and environmental assumptions. This supports separating local conformance from upstream adequacy, but does not settle the note's further question of whether the adopted requirement serves a larger objective. The zoo goal-regress example bounds the engineering subject matter; it does not confer authority to choose that boundary or resolve competing goals.

It also **compares with** [Morgan's specification statement](./morgan-the-specification-statement.ingest.md) on where formal derivation begins. Morgan gives a semantics and refinement relation for specifications and programs. Zave and Jackson explain the environmental reasoning needed to reach an implementable specification in the first place. Their “requirements refinement” is not interchangeable with program refinement: it can add domain assumptions, and failed observability can require changing the requirement rather than deriving an equivalent executable form.

## Extractable Value

1. **Operationalization needs an environmental warrant, not just executable instructions.** Separate the desired outcome R, implementable behavior S, and assumptions K linking them. The source's three obstacles—environment constraint, unshared information, and future reference—give specific questions for inspecting an agent workflow. This adds a diagnostic layer to the exact-implementation note: identify the missing control, observation, or prediction relationship before treating a procedural rewrite as sufficient. The transfer is conceptual, not a tested agent-workflow method. [quick-win]
2. **Subject-matter boundaries stop goal regress without legitimating goals.** Designating zoo-entrance phenomena limits the alternatives an engineering project considers. For agent-operated knowledge work, an explicit scope can likewise bound a task, but scope does not establish who may adopt or revise its goals. The paper brackets customer conflict and supplies no account of delegated authority; use it to clarify the boundary, not to justify the authority on either side. [quick-win]
3. **Separate a maintained estimate from the phenomenon it represents.** The warehouse example distinguishes actual inventory from quantities computed from recorded events. When theft, delay, or error breaks equivalence, the paper calls for changed requirements, failure handling, and periodic inventories. This offers a concrete warning for KB status fields and derived records: a deterministic update can preserve the estimate while its relation to the world fails. It does not supply a general method for revising explanations or deciding when to abandon an assumption. [experiment]
4. **Written meanings preserve the difference between a definition and a world claim.** A definition extends vocabulary; an assertion relating independently designated phenomena can be false. This is useful when formalizing KB terminology: making an assertion true by redefining its terms can remove the empirical claim instead of validating it. The source contributes a precise diagnostic, not a requirement that every natural-language KB statement be formalized. [quick-win]

## Limitations (our opinion)

The paper explicitly excludes sociological questions such as communicating with customers and resolving their conflicts. Its requirement set is validated as expressing the customer's desires, so its formal account cannot decide whose desires count, whether the customer is authorized, or whether satisfying those desires serves a wider objective. The [exact-implementation note](../theory/exact-implementation-does-not-validate-a-requirement.md) retains that additional distinction.

The formal guarantee depends on K being true and on the chosen phenomena and boundary being adequate. The paper recognizes probable rather than exceptionless assumptions, such as lift users pressing a button and telephone users dialing within a timeout. Those cases yield conditional or approximate satisfaction, not an unconditional guarantee from the completion formula. Its inventory example shows how a failed correspondence can force redesign, but it supplies no continuing process for detecting stale assumptions, adjudicating criticism, or revising a body of knowledge. It is not a theory of learning or knowledge growth.

The proposed categories and examples are analytical evidence, not a controlled comparison of development methods. There is no measured improvement in defect rates, engineering cost, or agent performance. The two-actor environment–machine decomposition and a located interface organize the argument; applicability to multi-agent knowledge work requires explicitly locating that boundary and identifying controlled and observable phenomena. Informal or contested success criteria may remain outside the formal account until made precise. Implementability in principle also does not establish practical feasibility under resource limits.

## Recommended Next Action

Review [Exact implementation does not validate a requirement against its objective](../theory/exact-implementation-does-not-validate-a-requirement.md) for a bounded addition distinguishing the S-plus-K-to-R satisfaction obligation from informal validation of K and R, while preserving its separate requirement–objective and authority questions.
