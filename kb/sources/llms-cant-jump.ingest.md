---
description: Position paper separating deduction within supplied axioms from abductive premise invention, using Einstein's path to general relativity to motivate action-controllable world models
source: https://www.tomzahavy.com/files/llms-cant-jump.pdf
captured: "2026-08-20"
capture: pdf-read
genre: scientific-paper
snapshot_sha256: 7a3cb7297f3ea4e925b84367f63f6dddcf136bcb4582ba202c4443b6b13ef74a
ingested: "2026-08-20"
type: kb/sources/types/ingest-report.md
domains: [scientific-discovery, learning-theory, world-models, evaluation]
---

# Ingest: LLMs can’t jump

## Classification

A position paper that interprets a historical case through a computational account of scientific invention. It proposes a research direction but reports no experiment that tests its central capability claim.

Author: Tom Zahavy is a Google DeepMind researcher whose doctoral and professional work focuses on AI and deep reinforcement learning. He has a physics and electrical-engineering BSc and has co-authored physics papers, but explicitly disclaims expertise as a physicist or historian. That background supports the paper's AI-system comparisons more strongly than its reconstruction of Einstein's cognition. The author also discloses using Gemini to refine and rephrase parts of the text.

## Summary

Zahavy uses Einstein's sense-experience → jump → axiom → deduction diagram to separate three functions in scientific invention. Induction learns patterns from observations, deduction derives consequences from supplied premises, and abduction proposes an explanatory premise. On the paper's reconstruction, Einstein did not reach general relativity by fitting a large anomalous dataset: Newtonian gravity still predicted most observations well, while the equivalence principle arose from an imagined experience of free fall. The paper therefore argues that a modern LLM might derive and check general relativity after receiving Einstein's postulates yet still lack the sensory-grounded, manipulative simulation needed to formulate those postulates. It proposes physically consistent, action-controllable world models as a substrate for counterfactual intervention and for translating simulated experience into formal axioms. This is a conceptual research hypothesis, not a demonstrated architectural impossibility or a result showing that world models supply the missing mechanism.

## Connections Found

The source's strongest role is as a proposed scientific-invention case for [learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) and [a proposal-selection improvement loop requires search, evaluation, and operative retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md). Deduction can evaluate or unfold only premises that its search space can express. Zahavy's additional claim is that a text-trained symbolic space omits the sensory-to-concept mapping needed to produce some physical premises. The first part follows from the existing notes; the claimed omission remains the paper's conjecture.

[Hot Take: LLM can 'jump'](hot-take-llm-can-jump.ingest.md) is the direct `compares-with` counterpoint. It changes the knowledge-time boundary: instead of asking whether a system could originate general relativity from Einstein-era premises, it argues that later quantum-field-theory knowledge supplies a largely deductive reconstruction route. This weakens the claim that sensory abduction is the only route to the theory, but it does not answer Zahavy's narrower prospective-invention question.

The paper also gives [the discovery lifecycle](../notes/definitions/discovery-lifecycle.md) a worked historical rendering of abduction, consequence derivation, and test. Its distinction between generating an axiom and deriving a known axiom's consequences supports [known-target discovery benchmarks show reachability, not discovery closure](../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md): supplying the target premise moves the task downstream and cannot establish prospective premise invention.

Its formalization boundary matches [formal symbolic systems assess explanatory-reach only through causal and proof obligations](../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md). A proof can show what follows from a formal premise without showing that the premise faithfully represents physical experience. The proposed world-model remedy, however, has a different role from [world models assess explanatory-reach through action-conditioned prediction](../notes/world-models-assess-explanatory-reach-through-action-conditioned.md). That note uses intervention to test a retained model; Zahavy wants interactive simulation to generate candidate premises before formal testing begins.

The source is a useful challenge to [the boundary of automation is the boundary of verification](../notes/the-boundary-of-automation-is-the-boundary-of-verification.md). Verification can bind only after candidate generation reaches something worth checking. [Model Discovery Agent](./model-discovery-agent-bayesian-experiment-design.ingest.md), [DiscoverPhysics](./discoverphysics-benchmarking-llms-out-of-the-box-scientific.ingest.md), and [FALSIFYBENCH](./falsifybench-inductive-reasoning-rule-discovery-games.ingest.md) provide empirical pressure against reading the title categorically: LLM agents can propose and revise hypotheses in controlled interactive settings. Their supplied grammars, simulators, target spaces, and oracles also leave Zahavy's stronger question -- invention of a new physical representation without symbolic precedent -- open.

## Extractable Value

1. **Premise generation and consequence derivation are separate capability targets.** A system can become much better at theorem proving or verification without improving its ability to formulate the premises that make a new theory possible. This is a precise way to prevent deductive benchmark gains from being reported as closure of scientific discovery. [quick-win]

2. **A candidate-generation boundary can bind before an oracle boundary.** Verification limits selection only after search can express a relevant candidate. If the effective hypothesis space omits the required representation, improving the verifier does not reach it. This qualifies, rather than rejects, verification-boundary accounts of automation. [quick-win]

3. **Interactive world models can serve two distinct functions.** Action-conditioned counterfactuals may assess the reach of an existing model, or they may supply observations from which a system proposes a new model. Keeping assessment and generation separate prevents evidence for one function from being treated as evidence for the other. [deep-dive]

4. **The paper suggests a direct experiment that it does not run.** Compare text-only, passive-video, and action-controllable agents in held-out counterfactual worlds where success requires proposing a new latent entity or law, then score premise formation separately from prediction and formal derivation. The important ablation is whether intervention expands the effective hypothesis space, not merely whether it improves trajectory accuracy. [experiment]

5. **"Abduction" needs a declared sense.** The paper alternates between Peirce's Rule + Result → Case pattern, inference to the best explanation, and invention of a new rule or axiom. These are related but not interchangeable capability claims. Future notes should say whether abduction means case inference, explanatory hypothesis proposal, or representational change. [quick-win]

6. **Einstein's path is a vivid reference case, not decisive evidence.** The distinction between the free-fall thought experiment, the equivalence principle, and later mathematical derivation is a useful teaching example for discovery-stage separation as long as the retrospective cognitive reconstruction is not treated as an identified mechanism. [just-a-reference]

## Limitations (our opinion)

This is editorial judgment, not the author's own caveats.

**The categorical conclusion outruns the evidence.** One retrospective reconstruction of Einstein's work cannot establish that current LLMs are structurally incapable of abduction. The paper gives no operational test of "the jump," no comparison between architectures, and no impossibility argument connecting next-token training to an unreachable hypothesis class. Its claim is best retained as a proposed generation-side boundary.

**The unit of analysis shifts between an isolated model and an AI system.** A bare text model has no sensorimotor agency, but contemporary scientific agents can include tools, simulators, search procedures, memory, and formal checkers. The paper itself proposes adding an interactive world model. That supports a claim about missing components in current systems more readily than the title's claim about what LLMs cannot do.

**The "no error signal" argument is too narrow.** Einstein lacked a large supervised dataset favoring general relativity, but he did have strong constraints: conflict between Newtonian action at a distance and field theories, the equivalence of inertial and gravitational mass, the demand for general covariance, the Newtonian limit, and Mercury's anomaly. Search and optimization can be guided by consistency constraints, priors, novelty objectives, or self-generated experiments rather than a prediction-loss gradient over observations. The absence of one learning signal does not show the absence of every search signal.

**The historical story does not identify the computational mechanism.** Einstein's reports of non-verbal thought and the elevator thought experiment show that imagery mattered to him. They do not establish that remembered bodily sensation caused the equivalence principle, that symbolic reasoning could not have reached it, or that the same route is necessary for other discoveries. The author's explicit historical-expertise caveat is material here.

**Controlled hypothesis formation already exists below the paper's target.** LLM agents can infer and revise hidden rules in bounded games and simulated worlds. Those results do not settle unconstrained axiom invention, but they do show that "abduction" cannot be denied wholesale without specifying the supplied representation, intervention space, and oracle.

**Action-controllable prediction is neither shown necessary nor sufficient.** A world model may enable counterfactual experiments while still learning shortcuts, inheriting a fixed ontology, or failing to translate latent states into explicit premises. The proposed bridge from interactive simulation to novel formal axioms is the paper's central missing mechanism, not a demonstrated consequence of existing systems such as Genie.

## Recommended Next Action

Consider revising [learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) to add this paper as a bounded scientific-invention case: deductive and verification strength cannot recover a premise outside the effective hypothesis space. Preserve the important qualification that the paper argues, but does not demonstrate, that sensory-grounded simulation is required to expand that space.
