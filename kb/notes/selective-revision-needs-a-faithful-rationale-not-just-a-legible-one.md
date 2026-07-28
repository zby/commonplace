---
description: "Revision reaches the premise that broke only through the theory's recorded rationale, so a readable but unfaithful rationale makes repair confidently wrong rather than merely uninformed"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [learning-theory, discovery, evaluation]
---

# Selective revision needs a faithful rationale, not just a legible one

A retained theory is worth more than an equivalent pile of cases because [one theory-level revision can change many downstream conclusions at once](./theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md). That operation needs something the theory's claim does not contain. To narrow "skip integration tests when only documentation files changed" at the premise that actually broke, rather than deleting it, the system must have on hand *why* it held the theory: which observations supported it, which assumptions it rested on, where it was expected to stop. That record is the theory's **rationale**.

So the rationale is not commentary attached to a theory. It is the surface revision operates on. A theory without one can be deleted and re-derived; it cannot be repaired.

## Legibility is what you get, faithfulness is what you need

A rationale that can be read is legible. A rationale that accurately tracks the basis the theory actually rests on is **faithful**, and the two come apart exactly where it matters. [Jacovi and Goldberg distinguish faithfulness from plausibility](../sources/towards-faithfully-interpretable-nlp-systems.ingest.md): an explanation can convince a reader without representing the process behind the conclusion. [Turpin et al. show the behavioral version](../sources/language-models-dont-always-say-what-they-think.ingest.md) — controlled input features shift an answer while a fluent chain-of-thought omits the feature that moved it. The same divergence appears in retained artifacts specifically: [self-evolving agents' behavior is often not causally grounded in the artifacts they purport to use](../sources/llm-agents-are-not-always-faithful-self-evolvers.md).

The failure this produces is not symmetric with having no rationale at all, and that asymmetry is the whole claim. With no rationale, a counterexample forces wholesale replacement — expensive, but the broken theory does not survive. With an unfaithful one, the system edits the premise the rationale names, the theory reads as repaired, and the premise that actually carried the failure is untouched. The result is a theory that has been *confidently* revised in the wrong place, and the revision itself removes the pressure that would have caught it. A wrong rationale is worse than none precisely because it is actionable.

## The test is intervention, not inspection

Reading a rationale cannot establish that it is faithful, since reading is what a plausible confabulation is optimized to survive. What separates them is whether operating on the rationale moves the theory's commitments the way the rationale says it should.

[Concept bottleneck models](../sources/concept-bottleneck-models.ingest.md) supply the worked case. Their concept layer is the rationale made explicit — a legible intermediate the prediction is supposed to run through. Where the concept loss is weighted too low, that layer stays fully readable and keeps competitive accuracy on both the task and the concepts, and intervening on it makes predictions *worse*. Legible, accurate, and unfaithful at once, with the divergence invisible to inspection and obvious to intervention.

This gives the property an operational shape rather than a rhetorical one: edit the rationale's stated premise and check whether the theory's downstream commitments move as stated. It is the same operation as selective revision. Faithfulness is therefore not a precondition checked before revising — it is what revising correctly consists of, which is why a system that cannot test it cannot claim the revision advantage either.

## Scope

- The claim is about repair, not about whether the theory is good. A faithful rationale for a bad theory supports *rejecting* it precisely; faithfulness makes revision reliable, not favorable.
- The same condition governs a second consumer: an overseer deciding about a retained change by reading its rationale rather than probing behavior. That saving inherits the asymmetry — an accepted but unfaithful rationale can cut probing while raising confident error. This note does not develop the oversight case.
- A recorded rationale is a claim about the theory, not a transcript of how it was formed. Nothing here assumes a system can introspect its own basis; the rationale is an artifact that may be wrong, which is why the intervention test is load-bearing rather than optional.
- The cited work establishes the faithfulness–plausibility distinction, an intervention-based failure mode in chain-of-thought, and a constructive case in concept bottlenecks. None of it tests natural-language rationales attached to retained theories, which is the setting this claim is about.

## Open Questions

- Whether the intervention test transfers from a supervised concept layer, where the intermediate is a typed variable, to a natural-language rationale whose premises are not separately addressable without an interpreter deciding what its premises are.
- Whether rationales recorded at formation are measurably more faithful than ones reconstructed after the fact, or whether both confabulate often enough that the distinction does not pay for itself.
- Whether keeping many rationales faithful as their theories drift costs more, at library scale, than re-deriving theories from scratch would.

---

Relevant Notes:

- [Theory-mediated learning may improve sample efficiency under structured shifts](./theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) — grounds: the selective-revision advantage this note states the condition on
- [Reflection makes retained lessons second-order: a lesson can reject or rescope a prior commitment](./reflection-makes-retained-lessons-second-order.md) — mechanism: the reject/rescope/revise operations a rationale makes available
- [Abstract an experience into a lesson only when you can state where the lesson stops](./abstract-an-experience-only-when-you-can-state-the-boundary.md) — grounds: the applicability conditions a rationale has to record for rescoping to have a target
- [Reach-assessment](./definitions/reach-assessment.md) — grounds: the capability that tells a sound rationale from a plausible one, which reading does not supply
- [Reasoning production is not reasoning evaluation](./reasoning-production-is-not-reasoning-evaluation.md) — grounds: producing a rationale and validating it are separate capabilities
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — grounds: the domain over which the intervention test can be run bounds where the advantage is real
- [False-positive generation is filtered; false-positive acceptance becomes operative](./false-positive-generation-is-filtered-before-retention.md) — mechanism: revising on an unassessed rationale is false-positive acceptance wearing an explanation
- [Concept bottleneck models](../sources/concept-bottleneck-models.ingest.md) — evidenced-by: a legible, accurate intermediate whose interventions degrade predictions — legibility and faithfulness separated constructively
- [Towards Faithfully Interpretable NLP Systems](../sources/towards-faithfully-interpretable-nlp-systems.ingest.md) — abstracted-from: the faithfulness/plausibility distinction and the warning that readability does not establish faithfulness
- [Language Models Don't Always Say What They Think](../sources/language-models-dont-always-say-what-they-think.ingest.md) — evidenced-by: fluent chain-of-thought omits an intervened feature that shifted the answer
- [LLM agents are not always faithful self-evolvers](../sources/llm-agents-are-not-always-faithful-self-evolvers.md) — evidenced-by: divergence between the artifacts a self-evolving agent purports to use and what causally grounds its behavior
