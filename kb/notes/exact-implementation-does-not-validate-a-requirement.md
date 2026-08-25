---
description: "An artifact can exactly implement a requirement while the requirement remains a conjectured proxy for a declared objective; assess each named path separately, and attribute failure to the link without erasing local correctness"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, constraining]
---

# Exact implementation does not validate a requirement against its objective

An artifact can be perfectly correct relative to its immediate requirement yet still be wrong for the system-level problem. Exactness belongs to the artifact–requirement link; proxyhood belongs to the requirement–objective link above it. Confusing the two makes local verification look like upstream validation.

The unit of analysis is a single named artifact–requirement–objective path within a declared boundary. Real requirement structures branch: the same artifact may exactly implement one adopted requirement while serving as a conjectured proxy under another objective. Artifact-level phrases such as “exact-spec artifact” are safe shorthand only when the relevant path is named or every path in scope has the same status.

Arithmetic, sorting, schema validation, and legal move generation in chess illustrate locally exact requirements once the intended variant, input encoding, and output contract are fixed. Vision features such as SIFT, Haar cascades, and Canny edge detection likewise had precise mathematical specifications and useful invariants. They implemented those specifications exactly. What remained conjectural was the link from edge maps and keypoints to seeing: a theory about what seeing requires, not a definition of seeing.

## A commitment creates a local floor, not a chain endpoint

At the highest link in scope, an analysis encounters either an adopted commitment or a conjectured decomposition. That is a boundary chosen for the analysis, not the top of an objective hierarchy.

An adopted commitment [creates ground truth for the levels below it](./commitment-not-derivation-creates-new-ground-truth.md). A schema is the contract because the project adopted it; chess move generation is exact because the rules constitute the game. Below the commitment sits conformance, checkable against the adopted requirement. Above it sits a different question: whether adopting that requirement serves a further objective. Adoption settles who or what defines local correctness; it does not establish that the choice is useful, stable, legitimate, or cheap to reverse.

A conjectured decomposition instead posits that satisfying one requirement contributes to a capability nobody defined. “Detect edges” was a theory about what seeing requires. The machinery could be checked against the edge-detection specification, but the link from that requirement to seeing needed separate evidence.

These questions require different checks. A hard oracle can make conformance cheap without showing that its target is the right target. Evidence for the requirement–objective link must instead come from an explicitly constitutive scope, outcome data, predictive tests, ablations, or composition. [Oracle strength](./oracle-strength-spectrum.md) is therefore one confidence factor in hardening a conjectured link, alongside coverage, failure cost, reversibility, volatility, and external dependencies.

## A failed proxy link preserves local correctness, not necessarily artifact value

The vision story invalidates less than it first appears to. Edge detection remains exact relative to its own requirement and useful wherever edges are genuinely wanted, such as document deskewing or industrial inspection. What failed was the broad conjecture that the requirement would compose into seeing—the kind of unsupported proxy scope that [may explain a structured method's loss in a scaling comparison](./bitter-lesson-selects-against-unearned-reach-not-against-structure.md).

That diagnosis preserves a fact, not an asset. The artifact still conforms locally, but retaining it depends on whether anyone wants the narrower requirement and whether reuse is cheaper than replacement or removal. The logical repair is to retract the failed requirement–objective claim and rescope any surviving use; disposal remains appropriate when the narrower capability has no value.

## Composition tests what local conformance cannot

Local checks test the artifact–requirement link. End-to-end composition tests whether the chosen requirements jointly serve the capability above them. Where no earlier oracle directly exposes a conjectured link, composition may be its first strong test, so locally correct components that systematically fail together are evidence against the decomposition.

Composition failure is not unique to proxy theories. Incompatible interfaces, inconsistent composed specifications, omitted resource limits, and execution defects can produce the same symptom. Conversely, a proxy can compose successfully over the observed range. Diagnose those alternatives before attributing failure upward. The key point is narrower: passing every local check cannot validate a link that none of those checks addresses.

## Diagnose one path at a time

Three questions inform confidence; none determines the classification alone:

1. **Is the immediate requirement constitutive of the declared objective?** If satisfying the requirement is what the bounded analysis means by success, there is no additional proxy link inside that boundary. If the requirement only stands in for a larger capability, the link remains conjectural.
2. **What does the available oracle establish?** A deterministic checker establishes conformance to its target. Human judgment, outcome measures, and proxy scores may bear on the upstream link, but their verdicts remain limited to their stated domains.
3. **Where do failures surface?** Local errors implicate the artifact or immediate specification. Repeated objective failure despite local passes implicates a higher link only after competing integration causes have been ruled out.

The practical posture is provisional [codification](./definitions/codification.md): crossing from natural-language guidance into a symbolic artifact with formal semantics. Harden local conformance when the gain in reliability, speed, or cost exceeds the expected costs of change and failure; adoption supplies authority, not prudence. Harden a conjectured link only to the degree its evidence warrants, keeping the artifact inspectable, tested, and easy to relax.

[Spec mining](./spec-mining-as-codification.md) strengthens the evidence by extracting candidate requirements from working behavior rather than inventing decompositions upfront. [Operational relaxing signals](./operational-signals-that-a-component-is-a-relaxing-candidate.md) help detect when a hardened link has stopped fitting. When a link fails, record which reach claim was retracted, preserve whatever local correctness remains, and reassess the narrower artifact on its actual value.

---

Relevant Notes:

- [A proximate target is checked for achievement, not for warrant](./a-proximate-target-is-checked-for-achievement-not-for-warrant.md) — extends: carries the proxy relation upward into the objective, target, criterion, and oracle levels and declares where the analysis stops
- [Derivation and inheritance give starting warrant; discriminating evidence or proof earns scope](./derivation-and-inheritance-give-starting-warrant-earns-scope.md) — extends: explains what warrants a conjectured decomposition and how its claimed scope can be earned
- [The readable-artifact loop is the tractable unit for continual learning](./readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) — extends: situates provisional hardening and relaxing inside durable artifact evolution
- [Feedback-trained memory management is oracle-dependent even when its operations are hand-designed](./memory-management-policy-is-learnable-but-oracle-dependent.md) — exemplifies: memory operations admit local specifications while the policy composing them remains outcome-dependent
- [Fintool production-agent report](../sources/lessons-from-building-ai-agents-for-financial-services.ingest.md) — evidenced-by: the author reports mapping ambiguous company-specific fiscal-period labels to absolute date ranges through a 10,000-plus-company calendar database, with 200-plus period-extraction tests; this bounded case does not show that every semantic period requirement is fully specified or validate downstream financial analysis
- [MAKER million-step decomposition study](../sources/meyerson-maker-million-step-llm-zero-errors.ingest.md) — evidenced-by: on a 20-disk Towers of Hanoi demonstration, maximal decomposition, a red-flagging parser, and at least three responses per step at `k_min = 3` accompanied more than one million LLM-generated steps with zero observed errors
- [SuperARC algorithmic-compression benchmark](../sources/superarc-ait-benchmark-llm-compression-abstraction.ingest.md) — evidenced-by: on 100 binary-sequence tasks under SuperARC's compression-weighted metric, its AIXI/BDM/CTM baseline scored 1.000 while the best listed frontier LLM scored 0.042; this does not validate the metric as a proxy for general abstraction
- [Induction-bias state-tracking study](../sources/induction-bias-sequence-models-ebrahimi-2026.ingest.md) — evidenced-by: more than 190,000 runs on synthetic modular-addition state tracking found orders-of-magnitude sample-efficiency advantages for the tested recurrent architectures over transformers in the outcome-supervision regime; the authors bound the study to a limited model and task set
