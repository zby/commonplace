---
description: "When revision relies on a rationale to locate a failed premise, a misleading rationale can direct repair to the wrong part; retained rationale is optional for theory refinement"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [learning-theory, discovery, evaluation]
---

# Revision guided by rationale needs faithfulness, not just legibility

Under structured shifts, a retained theory with genuine explanatory reach can be worth more than an equivalent pile of cases because [one theory-level revision can change many downstream conclusions at once](./theory-refinement-may-improve-sample-efficiency-under-shifts.md). A recorded **rationale** can guide that revision by naming supporting observations, assumptions, and expected scope. For example, a dependency-based explanation for skipping integration tests can suggest which condition to revise after a documentation file starts affecting a build. When the learner relies on that explanation to locate the defect, a misleading explanation can direct the repair to the wrong part.

Retained rationale is optional for [theory refinement](./definitions/theory-refinement.md). A learner can diagnose a rule from its consequences, search for a revised condition, and test the candidate without a record of why the rule was adopted. Premises within a rule, evidence supporting it, and the history of its adoption are distinct: repair does not require all three. The claim here concerns the reliability of repair that uses a rationale as its diagnostic guide.

## Legibility is what you get, faithfulness is what you need

A rationale that can be read is legible. A rationale that accurately tracks the basis the theory actually rests on is **faithful**, and the two come apart exactly where it matters. [Jacovi and Goldberg distinguish faithfulness from plausibility](../sources/towards-faithfully-interpretable-nlp-systems.ingest.md): an explanation can convince a reader without representing the process behind the conclusion. [Turpin et al. show the behavioral version](../sources/language-models-dont-always-say-what-they-think.ingest.md) — controlled input features shift an answer while a chain-of-thought omits the feature that moved it. The same divergence appears in retained artifacts specifically: [self-evolving agents' behavior is often not causally grounded in the artifacts they purport to use](https://arxiv.org/html/2601.22436v3).

Without a rationale, the learner must diagnose from the theory and available evidence or reconstruct a candidate explanation. With an unfaithful rationale, it may edit the premise the rationale names while leaving the source of failure untouched. A misleading rationale can therefore be worse than none when the apparent explanation displaces independent diagnosis or checking. A retained explanation does not establish that the proposed repair targets the defect.

## The test is intervention, not inspection

Reading a rationale cannot establish that it is faithful, since reading is what a plausible confabulation is optimized to survive. What separates them is whether operating on the rationale moves the theory's commitments the way the rationale says it should.

[Concept bottleneck models](../sources/concept-bottleneck-models.ingest.md) supply a worked analogy. Their supervised concept layer is a legible intermediate the prediction is supposed to run through. In the paper's experiments, task and concept accuracy alone did not predict whether test-time correction would help: linear concept-to-label maps handled interventions worse than nonlinear ones even when their pre-intervention accuracies were similar. Separately, when the concept-loss weight was too low, joint models learned misaligned representations and intervention increased error. The transfer from this typed intermediate to a retained natural-language rationale is target-side, but the case still shows why inspection alone cannot establish intervention faithfulness.

This gives the property an operational test: edit the rationale's stated premise and check whether downstream commitments move as stated, then test the revised theory against the failure and unaffected cases. The intervention checks the rationale's claimed dependency; it does not by itself establish the historical process that produced the theory. A system using this diagnostic route must test it before attributing a revision advantage to the rationale.

## Scope

- The claim concerns repair guided by rationale. A faithful account can help locate a defect in a bad theory; successful repair still requires candidate generation and evaluation.
- The same condition governs a second consumer: an overseer deciding about a retained change by reading its rationale rather than probing behavior. That saving inherits the asymmetry — an accepted but unfaithful rationale can cut probing while raising confident error. This note does not develop the oversight case.
- A recorded rationale is a claim about the theory, not a transcript of how it was formed. Nothing here assumes a system can introspect its own basis; the rationale is an artifact that may be wrong, which is why the intervention test is load-bearing rather than optional.
- The cited work establishes the faithfulness–plausibility distinction, an intervention-based failure mode in chain-of-thought, and a constructive case in concept bottlenecks. None of it tests natural-language rationales attached to retained theories, which is the setting this claim is about.

## Open Questions

- Whether the intervention test transfers from a supervised concept layer, where the intermediate is a typed variable, to a natural-language rationale whose premises are not separately addressable without an interpreter deciding what its premises are.
- Whether rationales recorded at formation are measurably more faithful than ones reconstructed after the fact, or whether both confabulate often enough that the distinction does not pay for itself.
- Whether keeping many rationales faithful as their theories drift costs more, at library scale, than re-deriving theories from scratch would.

---

Relevant Notes:

- [Theory refinement may improve sample efficiency under structured shifts](./theory-refinement-may-improve-sample-efficiency-under-shifts.md) — grounds: the selective-revision payoff whose rationale-guided realization this note examines
- [Reflection makes retained lessons second-order: a lesson can reject or rescope a prior commitment](./reflection-makes-retained-lessons-second-order.md) — mechanism: the reject/rescope/revise operations a rationale can help guide
- [Abstract an experience into a lesson only when you can state where the lesson stops](./abstract-an-experience-only-when-you-can-state-the-boundary.md) — grounds: the applicability conditions a rationale has to record for rescoping to have a target
- [Reach-assessment](./definitions/reach-assessment.md) — grounds: the capability that tells a sound rationale from a plausible one, which reading does not supply
- [Reasoning production is not reasoning evaluation](./reasoning-production-is-not-reasoning-evaluation.md) — grounds: producing a rationale and validating it are separate capabilities
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — grounds: the domain over which the intervention test can be run bounds where the advantage is real
- [False-positive generation is filtered; false-positive acceptance becomes operative](./false-positive-generation-is-filtered-before-retention.md) — mechanism: revising on an unassessed rationale is false-positive acceptance wearing an explanation
- [Concept bottleneck models](../sources/concept-bottleneck-models.ingest.md) — evidenced-by: intervention benefit is not predicted by task and concept accuracy alone, and a low-concept-loss regime can make correction increase error
- [Towards Faithfully Interpretable NLP Systems](../sources/towards-faithfully-interpretable-nlp-systems.ingest.md) — abstracted-from: the faithfulness/plausibility distinction and the warning that readability does not establish faithfulness
- [Language Models Don't Always Say What They Think](../sources/language-models-dont-always-say-what-they-think.ingest.md) — evidenced-by: chain-of-thought omits an intervened feature that shifted the answer
- [LLM agents are not always faithful self-evolvers](https://arxiv.org/html/2601.22436v3) — evidenced-by: divergence between the artifacts a self-evolving agent purports to use and what causally grounds its behavior
