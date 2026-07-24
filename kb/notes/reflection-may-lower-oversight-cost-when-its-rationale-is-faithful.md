---
description: "Conjecture: a retained rationale can lower oversight probing when sufficiently faithful to the decision; an accepted, decision-relevant mismatch can instead invite confident error"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, self-improving-systems, evaluation]
---

# Reflection may lower oversight cost when its rationale is faithful

A reflective improvement pathway routes changes through the system's own [causally connected self-representation](./definitions/reflective-system.md). Among the expected advantages of that routing, **explanation** is the one that promises a payoff in **oversight cost** — the work an external consumer, a person or another process, must do to decide correctly about a retained change: accept it, reject it, rescope it, or rely on it downstream. A change that can be read can carry a **rationale** — the stated reason it was made and the basis it relies on — [since reflection buys addressability](./reflection-buys-addressability.md). The promise is that the overseer can then discharge the decision by *reading* the change rather than by *probing* its behavior.

The conjecture, narrowed to what could be measured and could be wrong: **a retained change carrying an addressable rationale lets an overseer reach a correct decision with fewer behavioral probes than an opaque change of matched effect — when the rationale is faithful to the change's actual basis, the overseer can assess it rather than only read it, and it is retrieved.** Each clause is a condition and each can fail on its own: a rationale that misstates the basis is a failure of faithfulness; an overseer who cannot tell a sound rationale from a plausible-but-wrong one is a failure of assessment; a rationale nothing surfaces is a failure of the retrieval wire.

## The condition is faithfulness, not legibility

Legibility — the rationale can be read — is what addressability guarantees. **Faithfulness** — how accurately the rationale tracks the change's actual basis and decision-relevant dependencies — is what the saving needs, and the two come apart exactly where oversight matters most. The required degree is relative to the decision; this claim does not require a globally exact transcript. [Jacovi and Goldberg distinguish faithfulness from plausibility](../sources/towards-faithfully-interpretable-nlp-systems.ingest.md): an explanation may convince a reader without accurately representing the process behind a decision. A rationale that reads cleanly but misstates something material to the decision can be worse than none when the overseer accepts it: it invites the overseer to close the decision by reading, and to close it *confidently wrong*. A self-reported rationale is a claim about the change, not a transcript of it. [Turpin et al. show the behavioral failure](../sources/language-models-dont-always-say-what-they-think.ingest.md): controlled input features can systematically shift an answer while the model's fluent chain-of-thought omits the intervened feature. The neighboring gap has already been observed in this KB's captured evidence: [self-evolving agents' behavior is often not causally grounded in the retained artifacts they purport to use](../sources/llm-agents-are-not-always-faithful-self-evolvers.md) — purported and operative roles of an artifact can diverge, and a rationale is exactly such an artifact.

## What is distinct is a native rationale, not having one at all

An opaque change is not beyond explanation: interpretability tooling can attach a story to a weight update, and a model can be prompted to narrate its behavior after the fact. What reflective retention adds is that the rationale is **native** — recorded at acceptance, retained with the change as a system-readable object, retrievable without re-deriving it. Native status removes the reconstruction step and its cost, not the faithfulness question: a recorded reason can misstate the operative reason just as a reconstructed one can.

## The saving has its own costs

The claim is a probe-count claim; producing the rationale, keeping it faithful as its change evolves, retrieving it, and assessing it are costs on the same budget, and the comparison must count them. Retrieval is a real discount, [since retrieval failure is reflection failure](./retrieval-failure-is-reflection-failure.md): a rationale nothing surfaces to the overseer contributes nothing. And assessment is not free: telling a faithful rationale from a plausible confabulation is verification work, so the saving is real only in the domain where the overseer can do it — [warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md). Accepting a change on an unassessed rationale relocates trust without earning it: [false-positive acceptance](./false-positive-generation-is-filtered-before-retention.md) wearing an explanation.

## What would test it

Take retained changes whose ground-truth quality is known, some subtly bad in ways behavior does not advertise, and compare an overseer's probe count and decision accuracy with a sufficiently faithful rationale, with a fluent rationale containing a decision-relevant mismatch, and with probing alone. Record whether the overseer accepts, detects, or disregards each rationale. The directional prediction: **a sufficiently faithful rationale reaches correct decisions with fewer probes; an accepted rationale that is unfaithful in a decision-relevant way may also cut probes, but by degrading accuracy and inflating confident errors relative to no rationale.**

## Scope

- This is the oversight sibling of the [target-data payoff](./reflection-may-improve-sample-efficiency-under-structured-shifts.md): both narrow one bullet of the addressability affordance to a measurable claim, and both turn on a condition addressability does not itself supply — there, a structured shift the commitment's explanatory-reach covers; here, a faithful rationale the overseer can assess.
- The claim is about oversight cost, not about whether the change is good. A faithful rationale for a bad change lets the overseer *reject* it cheaply; faithfulness makes the decision reliable, not favorable.
- The cited studies establish the faithfulness–plausibility distinction and an intervention-based failure mode for model explanations and chain-of-thought. They do not directly test native rationales retained with changes, human probe counts, or oversight accuracy; applying their result here is a hypothesis this note's proposed experiment must test.

## Open Questions

- Whether native rationales are measurably more faithful than post-hoc reconstructions, or both routes confabulate often enough that the distinction does not pay.
- Whether an overseer's ability to assess a prose rationale's faithfulness can itself be established, given that [reach-assessment for prose is observed only in LLM-mediated evaluation without a theory for why](./definitions/reach-assessment.md).
- Whether the saving survives at library scale, where keeping many rationales faithful as their changes drift may cost more than probing would.

---

Relevant Notes:

- [Reflection buys addressability](./reflection-buys-addressability.md) — grounds: supplies the explanation affordance this note sharpens into a conditional oversight-cost hypothesis
- [Reflection may improve sample efficiency under structured shifts](./reflection-may-improve-sample-efficiency-under-structured-shifts.md) — contrasts: the sibling payoff developed from the same addressability bullet list, narrowing reuse-and-transfer instead of explanation
- [Reach-assessment](./definitions/reach-assessment.md) — grounds: the assessment capability the overseer needs to tell faithful rationale from plausible confabulation, which reading does not supply
- [Retrieval failure is reflection failure](./retrieval-failure-is-reflection-failure.md) — mechanism: the retrieval clause — a rationale nothing surfaces to the overseer contributes nothing
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — grounds: the domain over which an overseer can warrant a decision from a rationale bounds where the saving is real
- [False-positive generation is filtered; false-positive acceptance becomes operative](./false-positive-generation-is-filtered-before-retention.md) — mechanism: accepting a change on an unassessed rationale is the false-positive acceptance this payoff must avoid
- [Reflective system](./definitions/reflective-system.md) — defined-in: the causally connected self-representation the retained rationale must be part of for the payoff to bear on reflection
- [Towards Faithfully Interpretable NLP Systems](../sources/towards-faithfully-interpretable-nlp-systems.ingest.md) — abstracted-from: generalizes the faithfulness/plausibility distinction and the warning that utility or readability does not establish faithfulness to retained-change oversight
- [Language Models Don't Always Say What They Think](../sources/language-models-dont-always-say-what-they-think.ingest.md) — evidence: controlled biasing interventions show fluent chain-of-thought can omit an intervened feature whose presence shifted an answer
- [LLM agents are not always faithful self-evolvers](../sources/llm-agents-are-not-always-faithful-self-evolvers.md) — evidence: observed divergence between the artifacts a self-evolving agent purports to use and what causally grounds its behavior
