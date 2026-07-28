---
description: DiscoverPhysics authors 22 counterfactual physics worlds to defeat recall; agents that predict trajectories well still explain badly — a third target construction and an accuracy/explanation split
source_snapshot: discoverphysics-benchmarking-llms-out-of-the-box-scientific-thinking.md
ingested: "2026-07-26"
type: kb/sources/types/ingest-report.md
domains: [scientific-discovery, evaluation, oracle-theory, learning-theory]
---

# Ingest: DiscoverPhysics: Benchmarking LLMs for Out-of-the-Box Scientific Thinking

Source: discoverphysics-benchmarking-llms-out-of-the-box-scientific-thinking.md
Captured: 2026-07-26
From: https://arxiv.org/abs/2605.26087

## Classification

Genre: **scientific-paper** -- an arXiv benchmark paper with a constructed task suite, an agent protocol, and an evaluation across eleven frontier models. The capture is the abstract page, not the full paper.

Domains: scientific-discovery, evaluation, oracle-theory, learning-theory

Author: a seven-author group mixing astrophysics/cosmology and machine-learning researchers, including Andrew Gordon Wilson and Pavel Izmailov, both established ML researchers with prior work on uncertainty and generalization. The domain pairing is the right one for authoring physically coherent counterfactual worlds, which is the load-bearing construction here.

## Summary

DiscoverPhysics builds 22 simulated worlds whose laws of motion deliberately deviate from ours -- screened and fractional-power gravity, multi-species couplings, hidden dark-matter-like particles, non-coordinate-free dynamics, time-varying interactions -- and asks an LLM agent to discover the governing law by proposing rounds of experiments and observing raw trajectory data. The agent submits two artifacts for the same inferred law: a natural-language explanation and a Python implementation. Across eleven frontier models, the strongest agents pass roughly half the worlds, failures concentrate on discovering latent structure, open-source models trail commercial ones, and -- the finding that matters most here -- strong predictive accuracy does not guarantee a good conceptual explanation. The benchmark's contribution is less "can LLMs do science" than a clean experimental separation of two things this KB already treats as distinct: passing an empirical test on the outputs, and holding a mechanism that reaches.

## Connections Found

This source's role in the KB is **evidence for the reach-assessment cluster**, with a secondary role as a **new exemplar for the discovery-benchmark cluster**.

Its sharpest contribution is to [reach-assessment](../notes/definitions/reach-assessment.md). That definition's exclusions say reach-assessment is not empirical testing alone, and its scope says the assessment route must match the [representational form](../notes/definitions/representational-form.md) carrying the commitment. DiscoverPhysics collects a prose artifact and a symbolic artifact for the *same* commitment, tests the symbolic one empirically against the simulator, and then reports that the two come apart -- the exclusion measured rather than argued. The same finding is the adaptive-fit-versus-reach polarity of [first-principles reasoning](../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) instrumented on a machine, and it is an independent report of the accuracy/mechanism separation that [theory-mediated learning may improve sample efficiency under structured shifts](../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) predicts but currently supports only from transfer literature.

Secondarily, it is a third target construction for [known-target discovery benchmarks show reachability, not discovery closure](../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md), whose "Two target constructions" section has [GIANTS](./giants-generative-insight-anticipation-scientific-literature.md) as its only worked exemplar. Where GIANTS uses temporal provenance as the leakage control and buys a soft similarity oracle, DiscoverPhysics authors a counterfactual world: leakage control is structural rather than temporal, and the oracle on the predictive half is hard and executable. The methodological sibling among captured sources is [EsoLang-Bench](./esolang-bench-evaluating-genuine-reasoning-via-esoteric-programming.md), which defeats recall the same way by moving the task into a domain the training corpus cannot contain.

One connection is a tension rather than support: [the boundary of automation is the boundary of verification](../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) predicts automation stalls where verification is expensive, yet here verification is cheap and hard and agents still fail about half the worlds. That points at a generation-side bound the verification framing does not cover.

## Extractable Value

1. **A counterfactual authored world is a third target construction, with structural rather than temporal leakage control.** [Known-target benchmarks](../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) currently splits backcast (historical ordering does the control work) from reinvention (authored inputs must be kept neutral). Authoring the world itself makes canonical-phrase leakage structurally impossible -- there is no literature about a world that does not exist -- while still yielding an executable oracle. That is a distinct third cell the note does not have, and it explains *why* the construction works rather than recording that it does. [quick-win]

2. **Predictive accuracy and explanation quality dissociate inside a single task.** This is the empirical instance of [reach-assessment](../notes/definitions/reach-assessment.md)'s exclusion "reach-assessment is not empirical testing alone." Passing every trajectory check is compatible with failing the conceptual account, which is exactly the gap the definition names and had no measurement for. High reach: the mechanism does not depend on physics. [quick-win]

3. **Oracle strength may be per-property, not per-task.** The benchmark carries two oracles of different strength simultaneously -- hard and executable on prediction, soft and human on explanation. [Oracle strength spectrum](../notes/oracle-strength-spectrum.md) treats strength as one gradient per task, and [automated synthesis is missing good oracles](../notes/automated-synthesis-is-missing-good-oracles.md) carries a scope parenthetical granting that formal domains get cheap synthesis verification. Simulated physics is a formal domain where the cheap checker still does not close the explanation gap, which strains that parenthetical. [deep-dive]

4. **Cheap hard verification does not imply automation: the bound can be generative.** Best agents fail ~half the worlds despite a run-it-against-the-simulator verifier. Either [the boundary of automation is the boundary of verification](../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) needs a stated scope ("verification bounds automation where it binds; generation can bind first"), or this is a counterexample worth arguing with. Either way it is a scope question about a load-bearing note, not a new claim. [deep-dive]

5. **A shipped controlled-shift family that separates accuracy from mechanism.** [Theory-mediated learning](../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) asks in "What would test it" for controlled shifts of distinct kinds and warns that target accuracy alone will not separate the arms. Twenty-two authored worlds spanning distinct deviation families are that shift design, already built and already reporting the separation. Usable as a design template even without the paper's data. [experiment]

6. **"Make the domain counterfactual so pretraining recall cannot carry the score" is an unnamed recurring design move.** Present now in at least three captured sources -- non-standard physics here, esoteric languages in [EsoLang-Bench](./esolang-bench-evaluating-genuine-reasoning-via-esoteric-programming.md), unusual encodings in [SuperARC](./superarc-ait-benchmark-llm-compression-abstraction.md) -- and named nowhere in `kb/notes/`. Naming it would give the anti-recall control a handle separate from leakage control for authored targets. [experiment]

7. **Failures concentrate on latent structure.** Agents handle law-fitting over observed quantities better than positing an unobserved particular (a hidden dark-matter-like species) that the observed trajectories require. This is [conjecture is seeing the particular as an instance of the general](../notes/conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md)'s "the hard problem is recognition" with a machine-side measurement attached. [just-a-reference]

## Limitations (our opinion)

This is editorial judgment, not the authors' own caveats.

**The capture is an abstract page, and the load-bearing finding needs the full paper.** The accuracy/explanation dissociation is the most valuable thing here, and how "explanation quality" was scored is not visible. If it is an LLM judge, the dissociation is a hard oracle disagreeing with a soft one, which is a weaker and much more ordinary result than a hard oracle disagreeing with the truth. Every use of item 2 above should be checked against the paper's rubric before it is written into a note.

**"Out of the box" may be less out-of-the-box than the framing suggests.** Screened gravity, fractional-power force laws, multi-species couplings, and dark-matter-like species are all live terms in published theoretical physics. The worlds are counterfactual as *instances* but drawn from a *space* the training corpus discusses at length. That is a weaker anti-recall control than the framing implies, and it means the benchmark plausibly tests "recombine known modifications" rather than genuinely novel law discovery. The anti-recall move in item 6 should be stated with this caveat attached.

**No human or symbolic-regression baseline is visible in the capture.** Without one, "~half the worlds" is uninterpretable: it may measure model deficiency, benchmark difficulty, or experiment-budget parsimony. Item 4's tension with [the automation-boundary note](../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) is only as strong as the claim that the worlds are solvable at all by something -- and the capture does not establish that. A symbolic-regression baseline in particular could show that the hard part is search, not scientific reasoning, which is the simpler account of the whole result.

**Agent scaffold is a confound for the cross-model comparison.** Results in an interactive protocol depend on rounds allowed, tool loop, context handling, and prompt. "Open-source models underperform" may be partly "this harness suits commercial models," and no per-model harness tuning is described in the capture. Treat the model ranking as the least transferable finding here.

**Simulated worlds strip the parts of real discovery that are usually binding.** Experiments are free, observations are noiseless or cleanly noised, and the state space is fully specified by the simulator. Real experimental design is dominated by cost, instrument error, and not knowing what to measure. The benchmark isolates the inference step cleanly, which is its value -- but that isolation is also why success or failure here does not license claims about scientific discovery in the wild.

## Recommended Next Action

Revise [known-target discovery benchmarks show reachability, not discovery closure](../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) to add a third target construction to its "Two target constructions" section: the **counterfactual authored world**, where the experimenter authors the environment rather than selecting a historical or authored target, so leakage control is structural rather than temporal and the resulting oracle is hard and executable rather than a similarity judgement. Cite this snapshot as `evidenced-by`, and state the reachability reading it supports -- the target law is still known in advance, so the benchmark still measures reachability, but on a strictly stronger leakage control than the backcast branch. Carry the "counterfactual as instance, familiar as space" caveat from Limitations into the note rather than dropping it.
