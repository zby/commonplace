# Explanatory theories for selective evaluation

> **Workshop status:** This is an exploratory Commonplace workshop. It is not an HCL or SPADE summary, a validated evaluation method, an implementation proposal, or a safety claim.

This workshop asks how evidence from real-world tasks could train a deployed agent system. Here, training means using task outcomes, feedback, failures, and later consequences to propose and select persistent changes to behavior-shaping system state. It does not require updating the base model's weights, and a task result is evidence for an update rather than an update by itself.

[Harness Continual Learning (HCL)](../../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md) develops useful techniques in controlled benchmark streams: isolated harness candidates, reject-capable evaluation, sampled retention checks, and atomic commitment. The workshop asks how those techniques might govern learning from real-world task evidence. [SPADE](../../sources/spade-self-play-in-adaptive-synthetic-executable-environments.ingest.md) supplies a separate precedent for generating, filtering, and valuing executable environments. Neither work studies the theory-guided selective-evaluation proposal developed here, and HCL does not establish the controlled-to-deployment transfer.

## Workshop question

Could a revisable theory of system behavior with genuine [explanatory-reach](../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) derive candidate-specific impact claims well enough to decide which costly evidence is worth acquiring?

The working proposal separates a retained system theory `T` from the impact projection it supports. For a candidate `Delta` under an explicit boundary `S`, `I_T(S, Delta)` contains theory-derived claims or beliefs about affected functions and evaluation obligations. A mapping identifies procedures capable of observing them; an evidence-acquisition policy selects, adapts, or generates procedures; and a commitment rule decides what the acquired evidence warrants.

The impact question is intervention-shaped, so causal theories are an important route to `I_T`. They are not the umbrella. A theory may instead or additionally expose dependency and authority paths, invariants or proofs, compositional program structure, semantic contracts, or action-conditioned predictions. What makes selection theory-guided is that its candidate-specific projection follows from a criticizable account of why the system behaves as it does. Calling the account causal or explanatory does not establish explanatory-reach; that remains an empirical and argumentative liability.

The proposal is conditional. Local selection is plausible only when changes are sparse in a matching decomposition, dependencies and authority paths are explicit, and downstream impact is bounded. A sound theory may also project broad impact and correctly recommend running most or all checks. Selecting less evidence changes what acceptance can honestly mean: omitted checks remain unknown unless a separately justified residual-risk rule accounts for them, and that rule remains exposed to errors in the theory, its scope, or the derivation of its impact projection.

## Reading map

- [From controlled HCL benchmarks to deployment-time learning](./hcl-reading.md) — the proposed transfer, HCL's sampled-retention boundary, the conditional evaluator-growth calculation, and why its harness partition is not assumed to be a complete explanatory decomposition or causal graph.
- [A provisional theory-guided selective-evaluation model](./selective-evaluation-model.md) — the system-theory/impact-projection distinction, derivation routes and baselines, acceptance semantics, theory error, selective-observation problem, and limits of the locality hypothesis.
- [Experiment design for theory-guided selective evaluation](./experiment-design.md) — a comparison among full evaluation, sampling, similarity, structural, causal, and mixed explanatory-theory selectors, with SPADE-inspired procedure generation as a separate factor.
- [An invitation to the HCL authors](./for-hcl-authors.md) — the shorter HCL-facing account and questions.
- [An invitation to the SPADE authors](./for-spade-authors.md) — the shorter SPADE-facing account and questions about adaptive executable evaluations.

## Current boundary

The workshop has not established that HCL's controlled techniques transfer to learning from real-world tasks, that any candidate system theory has genuine explanatory-reach, that theory-derived impact projections are accurate, that theory-guided selection lowers total evaluation cost, or that any of these claims supports a safety conclusion. It has not chosen the primary registry object, selection objective, materiality threshold, loss units, prediction horizon, assessment protocol, or final acceptance rule. A controlled comparison needs measured costs, detection coverage, harmful misses, route-appropriate calibration or soundness checks, held-out retention, deliberate observation of checks the selector would otherwise omit, and tests that vary load-bearing premises and distinguish rival theories on unseen change families. Evidence of deployment value would require a later study in the target setting.

## Closing the workshop

This workshop can close in one of three ways:

- **Promote a method claim** only after the ontology and acceptance semantics are explicit and a controlled comparison supplies evidence for the proposed explanatory mechanism as well as measured cost, detection coverage, harmful-miss, route-appropriate calibration or soundness, expenditure, and retention results.
- **Hand off an experiment or proposal** if the maintainer authorizes separately scoped work to gather missing evidence or choose an implementation, without promoting effectiveness claims.
- **Close without promotion** if the evidence is negative, the required assumptions cannot be defended, or the inquiry is not worth continuing.

The maintainer must choose the disposition and any promotion order. A durable note, proposal, experiment, implementation, or external contact is separate work. Author replies would be welcome but are not required for closure.
