---
description: Direct reply to “LLMs can’t jump” arguing that later interconnected knowledge can make a formerly abductive discovery deductively reconstructible, then extending the claim to safety and continual learning
source: https://yongzx.github.io/blog/2026/08/08/llm-can-jump
captured: "2026-08-20"
capture: web-fetch
genre: conceptual-essay
snapshot_sha256: 310a317234cb8076895890852ef8c88468df603b0d64da60bffa63f4e53aeeac
ingested: "2026-08-20"
type: kb/sources/types/ingest-report.md
domains: [scientific-discovery, knowledge-reconstruction, AI-safety, continual-learning]
---

# Ingest: Hot Take: LLM can 'jump'

## Classification

A personal technical response that develops a counterargument through a historical reconstruction, selected model examples, and cited studies rather than reporting an original experiment.

Author: Yong Zheng-Xin presents this as a provisional “hot take” and explicitly concedes both that reconstructing a known result is easier than discovering it and that the broader prediction may be wrong. The essay's value comes from that carefully bounded counterexample and its links to primary material. It does not present peer review, original measurements, or an author credential that independently establishes the wider scientific, safety, or continual-learning claims.

## Summary

Zheng-Xin replies to [Tom Zahavy's argument](llms-cant-jump.ingest.md) that text-only LLMs lack the sensory-grounded abduction Einstein used to formulate general relativity. The response does not claim that an LLM could reproduce Einstein's route from Einstein-era knowledge. Instead, it cites a Feynman-style route in which later knowledge -- special relativity, quantum field theory, and empirical properties of gravity -- constrains a massless spin-2 theory toward general relativity. It generalizes this into an interconnected-knowledge account of discovery: cross-domain facts constrain and suggest hypotheses, while code, formal proof, simulations, and experiments check them. The essay then argues that harmful facts removed from training may be reconstructed from retained indirect information and predicts that broader model knowledge will make both weight updates and non-parametric use of new information easier. Its strongest contribution is the narrower distinction between original invention and later deductive reconstruction; the safety and continual-learning extensions are plausible conjectures with much thinner support.

## Quotes

No source quotes have been retained yet.

## Connections Found

This source is the direct counterpoint to [LLMs can’t jump](llms-cant-jump.ingest.md), but the disagreement is asymmetric. Zahavy asks whether a system given Einstein-era knowledge could originate the missing premises; Zheng-Xin asks whether later quantum-field-theory knowledge supplies another route to the same theory. The response weakens the claim that sensory abduction is the only route to general relativity. It does not answer the narrower prospective-invention question.

That distinction places the Feynman example under [known-target discovery benchmarks show reachability, not discovery closure](../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md). The essay itself concedes that Feynman knew the target. It shows that general relativity is plausibly reachable from a later premise set, not that a model would select the problem, construct that premise set, recognize the result, and validate it before the target was known. Its proposal-generation and checking loop otherwise fits the conjecture, consequence, and test stages of the [discovery lifecycle](../notes/definitions/discovery-lifecycle.md).

The interconnected-knowledge account usefully qualifies [learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md). Dense cross-domain knowledge, long histories, and general-purpose tools can enlarge a system's effective hypothesis and action space even when its visible interface is unchanged. The Feynman route is a candidate composition inside such an enlarged space. It does not establish that every required representational change is expressible, nor validate the fixed ontology, tool basis, and search procedure that make the route available.

The essay's scientific agent is explicitly a model plus code execution, Lean, simulators, and possible laboratory feedback, supporting [the deployed system, not the model alone, is the unit of learning](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md). Its continual-learning terminology is less compatible with the KB: it counts task-time use of supplied information even if nothing persists. [Continual learning requires governing behaviour-changing writes](../notes/continual-learning-requires-governing-behaviour-changing-writes.md) reserves the term for durable, evidence-responsive change, while [Machine Studying](machine-studying.ingest.md) supplies a more discriminating boundary for corpus-only preparation before downstream tasks.

## Extractable Value

1. **A discovery claim needs an explicit knowledge-time boundary.** “Could a model derive this theory?” changes meaning when the inputs move from knowledge available before the discovery to concepts developed decades later. Stating the cutoff separates prospective invention, historical backcast, and later reconstruction before capability evidence is compared. [quick-win]

2. **A route can rebut uniqueness without establishing original reachability.** The spin-2 route is useful evidence against “Einstein's embodied thought experiment was the only possible path.” Because the endpoint and later premise set were already known, it does not show that the path would be found prospectively. This is a clean application of the KB's reachability-versus-discovery distinction. [quick-win]

3. **Scientific capability belongs to a model-tool system.** Hypothesis proposal, program execution, formal proof, simulation, and laboratory intervention expose different signals and operations. Evaluating the bare language model erases the action space that the essay's own discovery account requires. [quick-win]

4. **Test interconnected-knowledge discovery by varying the premise boundary, not only model strength.** A useful experiment would hold the target hidden, supply temporally valid premise sets of increasing cross-domain breadth, and measure problem selection, hypothesis proposal, recognition, and verification separately. Include distractor domains and targets whose representational vocabulary is absent, so success inside a supplied ontology is not mistaken for invention of that ontology. [experiment]

5. **Knowledge deletion and inferential closure are different safety properties.** Removing direct statements can leave enough retained relations to reconstruct them. The cited controlled studies make this a concrete warning, but only inside fixed fact or relation spaces; extending it to open-ended harmful capabilities requires a specified threat model, reconstruction budget, and success oracle. For this KB, the point is a source-side caution about treating absence from stored content as proof of non-derivability, not yet a general memory-redaction rule. [deep-dive]

6. **The continual-learning prediction must be split by retained form.** Easier task-time use of new context, durable artifact creation, and weight-space adaptation are different outcomes with different plasticity, verification, and governance costs. The essay's “interconnected knowledge” hypothesis could be tested across those three routes, but success in one does not establish the others. [experiment]

## Limitations (our opinion)

This is editorial judgment, not the author's own caveats.

**The response changes the task rather than defeating Zahavy's narrow case.** General relativity derived from later quantum field theory is not general relativity invented from the knowledge available to Einstein. The example establishes an alternative reconstruction route and challenges a claim of path uniqueness. It does not establish that a current model can make the sensory-to-axiom jump Zahavy isolates.

**The endpoint is known and may shape the route.** Feynman already knew general relativity, and the cited derivation is presented as recovering it under selected consistency requirements. Knowing the destination makes premise selection, stopping, and recognition easier. The essay acknowledges this, but its headline still invites a stronger reading than the example supports.

**“Interconnected knowledge” is not yet a mechanism.** The framing does not specify which facts and histories the model can access, how it selects domain transfers, which hypotheses it can express, how much search is allowed, or which verifier rejects candidates. Without those commitments, the account can explain almost any successful discovery after the fact and does not predict where connection-making will fail.

**The empirical safety evidence operates inside fixed decompositions.** The cited studies expose models to indirect observations or synthetic graph relations and score recovery of known target facts or rules. Their input representation, relation vocabulary, target space, prompts, training procedure, and oracle remain fixed outside the learner's update space. Those results can show reconstruction within the tested schema; they do not show that arbitrary censored knowledge or an operational harmful capability will be reconstructed from real corpora.

**The flagship capability example is not independently evaluated here.** The Astra unit-distance result may demonstrate a useful cross-domain transfer in a formal problem, but the essay relies on an organization announcement and does not inspect the proof, model inputs, tool scaffold, human involvement, or failed attempts. Even if accepted, one known formal problem does not establish open-ended paradigm formation.

**Verification is described more cheaply than real science permits.** Code, Lean, and simulators provide strong oracles only for suitably formalized targets. Wet-lab evidence is costly, noisy, slow, and dependent on experimental design. Listing these tools does not solve candidate triage or the translation from a conjecture into a testable formal commitment.

**The continual-learning conclusion is mostly definitional and predictive.** Counting correct use of new context as learning makes the claim easier to satisfy but collapses ephemeral in-context adaptation into durable system change. The stronger predictions -- easier weight updates and models inventing their own plasticity remedies -- have no direct evidence in the essay and leave retention, regression, and authority governance unspecified.

## Recommended Next Action

Consider revising [the existing “LLMs can’t jump” ingest](llms-cant-jump.ingest.md) to add this response as its direct `compares-with` counterpoint, explicitly separating invention from Einstein-era premises from reconstruction using later quantum-field-theory knowledge.
