---
description: "Wason 2-4-6 benchmark over 12 LLMs; lands as first behavioural evidence that falsification-seeking discriminates hypothesis-formers, and a process-scored counter-case to the known-target critique"
source: https://arxiv.org/abs/2606.04751
captured: "2026-07-26"
capture: web-fetch
genre: scientific-paper
snapshot_sha256: f82893347f93366a4c1088844fe46df390b875d3b64387fc81230c29be9fb46b
ingested: "2026-07-26"
type: kb/sources/types/ingest-report.md
domains: [scientific-discovery, evaluation, reasoning, learning-theory]
---

# Ingest: FALSIFYBENCH: Evaluating Inductive Reasoning in LLMs with Rule Discovery Games

## Classification

An arXiv (cs.AI) benchmark paper introducing an evaluation framework and reporting results across 12 models; the capture is abstract-level, so the genre is read from the artifact's form rather than from inspected methods.
Author: Leonardo Bertolazzi, Katya Tentori, Raffaella Bernardi (University of Trento). Bernardi is an established computational-semantics researcher and Tentori works on probabilistic reasoning and confirmation in cognitive psychology; the pairing is the right one for porting a Wason paradigm to LLMs. Independent academic group, no vendor stake in the result.

## Summary

FALSIFYBENCH adapts the Wason 2-4-6 rule-discovery game into an interactive benchmark: an agent must identify a hidden semantic property by repeatedly proposing example instances and reading back whether each satisfies the rule. The paradigm exercises hypothesis generation, evidence gathering, and belief revision under both confirming and disconfirming feedback, in a closed loop where the agent chooses its own probes. Across 12 models spanning families and scales, reasoning models outscore instruction-tuned models but none approach optimal play. The paper's headline result is about *how* rather than *how well*: the primary driver of success is the capacity for negative testing — models that actively construct probes intended to falsify their current hypothesis consistently beat models that mostly propose confirming instances. A turn-level analysis, which the authors present as neglected in prior work, ties failure to identifiable patterns in how models traverse the hypothesis space rather than to a single aggregate score. Worth reading in full for anyone who needs the operationalization of "negative testing" or the failure taxonomy; the abstract alone already carries the load-bearing claim.

## Quotes

- **Source extract (verbatim):** This paper introduces FALSIFYBENCH, an evaluation framework designed to assess hypothesis-driven reasoning in large language models. The framework draws inspiration from the classic Wason 2-4-6 task, where agents discover hidden properties by proposing examples and receiving iterative feedback.
  - **Source location:** Abstract.
- **Source extract (verbatim):** Key findings from evaluating 12 LLMs include:
  - **Source location:** Abstract, result-population lead-in.
- **Source extract (verbatim):** "The primary driver of success is the capacity for negative testing" — models actively seeking to falsify hypotheses outperform those seeking confirmation
  - **Source location:** Abstract, second findings bullet.

## Connections Found

The KB has a live casebook here, and this source's role in it is **process-level evidence for the falsification premise the discovery cluster currently asserts without external grounding**. Three of its landing points are load-bearing rather than decorative.

Its strongest role is as evidence for [first-principles reasoning selects for explanatory-reach over adaptive fit](../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md), whose third negative test ("can it be criticized?") and its operationalization in [mechanistic constraints make Popperian KB recommendations actionable](../notes/mechanistic-constraints-make-popperian-kb-recommendations-actionable.md) both rest on an untested premise about model behaviour: that criticism must be structurally forced because models will not seek disconfirmation ambiently. This paper is the first external measurement bearing on that premise, and it cuts both ways — falsification-seeking is confirmed as the discriminating behaviour, but the reasoning-model result shows the ambient capacity is real and varies by model rather than being uniformly absent. The Popperian note carries no external sources at all today, so this is its first empirical leg.

Second, it is a worked instance for [known-target discovery benchmarks show reachability, not discovery closure](../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md), which currently runs on a single case ([GIANTS](https://giants-insights.github.io/), the backcast construction). FALSIFYBENCH is the authored-hidden-target construction the note distinguishes but does not instantiate — and it is a partial counter-case to the note's own framing, because the scored quantity is the agent's test-selection policy, not its recovery of the planted rule. Planting the target here buys a measurable *process* signal rather than converting discovery into target reconstruction.

Third, it measures the transition [discovery lifecycle](../notes/definitions/discovery-lifecycle.md) posits between consequence derivation and test — stating what would count against a conjecture, then going and looking. That phase boundary has been justified by Peirce and PDSA analogues; this is the first LLM-side data on whether the step actually happens in a closed loop.

Among sources it pairs most usefully with [DiscoverPhysics](https://arxiv.org/abs/2605.26087) — same closed experimentation loop, concrete simulated worlds instead of an abstract rule, same "best agents well short of optimal" shape — and with [An Enigma of Artificial Reason](https://arxiv.org/abs/2606.01462), which finds the same confirmation-bias family at the evaluation locus where this paper finds it at the generation locus.

## Extractable Value

1. **Falsification-seeking is the discriminating behaviour, not just a rhetorical virtue** -- the KB's explanatory-reach machinery (the four-part negative test, falsifier blocks, the reach-assessment criterion) has argued this from first principles with no external support. A measured, cross-model result that negative testing is *the primary driver* of rule-discovery success upgrades that from asserted design taste to a claim with a behavioural correlate. [quick-win]
2. **A known-target benchmark can score the search policy instead of the answer** -- this is the highest-reach item and the KB has not stated it. Where no outcome oracle for discovery exists, planting a target makes the agent's *test selection* measurable even though the final rule recovery is the trivially-known part. That partially escapes the "the benchmark already knows what counts as success" critique and generalizes past this paper: it is a construction rule for building oracles in oracle-poor domains, with FALSIFYBENCH and DiscoverPhysics as two worked cases. [deep-dive]
3. **Turn-level failure patterns beat aggregate scores for diagnosing hypothesis-space navigation** -- the authors flag turn-level analysis as neglected in prior work. For a KB that cares about where a reasoning loop breaks rather than whether it passed, this is a reusable evaluation method: instrument the trajectory, taxonomize the transitions, and treat the aggregate as a summary of the trajectory rather than the measurement. [experiment]
4. **Ambient criticism capacity is model-dependent and non-zero** -- "reasoning models are generally stronger scientific reasoners than instruction-tuned models, although no model comes close to optimal" bounds the structural-scaffolding argument from both sides. Structure is still needed (nobody is near optimal), but the premise that models never self-criticize without scaffolding is too strong, and which model runs a review gate is partly an empirical selection question. This bears directly on [reach-assessment](../notes/definitions/reach-assessment.md), which names the natural-language route to reach judgment as an open problem. [quick-win]
5. **A second Wason paradigm for the human-to-LLM transfer question** -- the KB's transfer-boundary reasoning in [human writing structures transfer to LLMs because failure modes overlap](../notes/human-writing-structures-transfer-to-llms-because-failure-modes.md) leans on the Wason *selection* task via Lampinen. The 2-4-6 rule-discovery task is the other paradigm in the family, and confirmation bias is the classic human failure on it, so the per-convention transfer question can now be asked on two tasks rather than one. Weakened by the capture reporting no human baseline. [just-a-reference]
6. **"Negative testing" as retrieval vocabulary** -- a compact, greppable name for the behaviour the KB has been circling with "criticizability", "falsifier block", and "what would defeat this claim". Useful for discussion and search even where nothing else is imported. [just-a-reference]

## Limitations (our opinion)

Editorial judgment, and constrained by a thin capture: the snapshot is abstract-level, with no methods, model list, numbers, or human baseline. Everything below is a caution about the claim as stated, not a finding about the paper's actual internals.

The load-bearing worry is that the headline result is at risk of being partly definitional. If "negative testing" is operationalized as proposing instances that fall outside the current hypothesis, then on a 2-4-6-style task where the hidden rule is characteristically *broader* than the natural first guess, probes outside the hypothesis are also the only probes that carry information. A model that tests outside its hypothesis would then score better because it gathered more evidence per turn, not because it holds a falsificationist disposition. That simpler account — negative testing as an information-gain proxy rather than an epistemic virtue — predicts the same correlation, and the abstract does not distinguish them. Whether the finding is hard to vary depends on details the capture does not carry: whether the authors controlled for probe informativeness, and whether the result survives rules where confirming probes are equally informative. Anyone citing this as support for the KB's [negative test](../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) should read the operationalization before leaning on it.

Second, what was not tested, as far as the capture shows: a single task family. The 2-4-6 paradigm has a known quirk — the canonical hidden rule is deliberately more general than the seed example invites — and results on it have historically been sensitive to that framing. Twelve models across families is decent coverage, but one paradigm is not, and generalizing from "LLMs under-use negative testing on abstract semantic rule games" to "LLMs under-criticize their own natural-language claims" is a jump the paper does not license. The KB's own [systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md) makes the parallel point about what varying an instance does and does not establish.

Third, no human baseline appears in the capture. Humans fail the 2-4-6 task badly and famously; without a baseline, "no model comes close to optimal" is a comparison to an optimal-play ceiling, not evidence that models are worse hypothesis-testers than people. Do not read it as the latter, and do not write that the paper compares LLM confirmation bias against the human literature — the capture does not support that claim.

## Recommended Next Action

Update [known-target discovery benchmarks show reachability, not discovery closure](../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md): add FALSIFYBENCH to the "Two target constructions" section as the reinvention-construction worked case beside GIANTS, and — the substantive edit — address the partial counter-case it raises, that a planted target can make the *search policy* scorable rather than only the reconstruction. That single revision lands the source's highest-reach contribution and gives the note the second instance it currently lacks; the reverse `evidenced-by` edges from the explanatory-reach and Popperian notes can follow once the operationalization has been read in the full paper.

---

- [known-target discovery benchmarks show reachability, not discovery closure](../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) — abstracted-from: FALSIFYBENCH is the authored-hidden-target construction the note distinguishes, and a partial counter-case because it scores test selection rather than target recovery
- [first-principles reasoning selects for explanatory-reach over adaptive fit](../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) — is-evidence-for: the four-part negative test's criticizability criterion gets its first behavioural correlate
- [mechanistic constraints make Popperian KB recommendations actionable](../notes/mechanistic-constraints-make-popperian-kb-recommendations-actionable.md) — is-evidence-for: bears on the note's premise that criticism must be structural because it will not happen ambiently
- [discovery lifecycle](../notes/definitions/discovery-lifecycle.md) — is-evidence-for: first LLM-side measurement of the consequence-derivation to test transition
- [reach-assessment](../notes/definitions/reach-assessment.md) — is-evidence-for: the natural-language route to reach judgment varies measurably across models
- [recognition, not linking, is the hard problem in knowledge systems](../notes/recognition-not-linking-is-the-hard-problem-in-knowledge-systems.md) — is-evidence-for: turn-level data on how the posit-and-recognize loop breaks
- [DiscoverPhysics](https://arxiv.org/abs/2605.26087) — compares-with: the same closed experimentation loop in simulated worlds rather than an abstract rule game
- [An Enigma of Artificial Reason](https://arxiv.org/abs/2606.01462) — compares-with: confirmation bias measured when models evaluate supplied reasoning rather than generate their own probes
- [GIANTS](https://giants-insights.github.io/) — compares-with: the backcast construction of a known-target discovery benchmark
- [Language Models, Like Humans, Show Content Effects on Reasoning Tasks](https://academic.oup.com/pnasnexus/article/3/7/pgae233/7712372) — compares-with: the KB's other Wason-family source, on the selection task
