# Causal impact and selective evaluation

> **Workshop status:** This is an exploratory Commonplace workshop. It is not an HCL or SPADE summary, a validated evaluation method, an implementation proposal, or a safety claim.

This workshop asks how evidence from real-world tasks could train a deployed agent system. Here, training means using task outcomes, feedback, failures, and later consequences to propose and select persistent changes to behavior-shaping system state. It does not require updating the base model's weights, and a task result is evidence for an update rather than an update by itself.

[Harness Continual Learning (HCL)](../../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md) develops useful techniques in controlled benchmark streams: isolated harness candidates, reject-capable evaluation, sampled retention checks, and atomic commitment. The workshop asks how those techniques might govern learning from real-world task evidence. [SPADE](../../sources/spade-self-play-in-adaptive-synthetic-executable-environments.ingest.md) supplies a separate precedent for generating, filtering, and valuing executable environments. Neither work studies the causal selective-evaluation method proposed here, and HCL does not establish the controlled-to-deployment transfer.

## Workshop question

Could a revisable theory of which behavioral functions a harness candidate can affect help decide, candidate by candidate, which costly evidence is worth acquiring?

The working proposal treats a candidate as a semantic intervention under an explicit system boundary. An impact theory predicts affected functions or evaluation obligations; a mapping identifies procedures capable of observing them; and an evidence-acquisition policy selects, adapts, or generates procedures before a commitment rule decides whether to adopt the candidate.

The proposal is conditional. Local selection is plausible only when changes are sparse in a matching decomposition, dependencies and authority paths are explicit, and downstream impact is bounded. Selecting less evidence also changes what acceptance can honestly mean: omitted checks remain unknown unless a separately justified residual-risk rule accounts for them, and that rule remains exposed to errors in the impact theory itself.

## Reading map

- [From controlled HCL benchmarks to deployment-time learning](./hcl-reading.md) — the proposed transfer, HCL's sampled-retention boundary, the conditional evaluator-growth calculation, and why its harness partition is not assumed to be a causal graph.
- [A provisional causal selective-evaluation model](./selective-evaluation-model.md) — the working ontology and objects, selector types, acceptance semantics, theory error, selective-observation problem, and limits of the locality hypothesis.
- [Experiment design for causal selective evaluation](./experiment-design.md) — the SPADE-inspired procedure-generation option and a comparison among full evaluation, sampling, dependency, similarity, and causal selectors.
- [An invitation to the HCL authors](./for-hcl-authors.md) — the shorter HCL-facing account and questions.
- [An invitation to the SPADE authors](./for-spade-authors.md) — the shorter SPADE-facing account and questions about adaptive executable evaluations.

## Current boundary

The workshop has not established that HCL's controlled techniques transfer to learning from real-world tasks, that causal selection predicts impacts accurately or lowers total evaluation cost, or that either supports a safety claim. It has not chosen the primary registry object, selection objective, materiality threshold, loss units, prediction horizon, calibration protocol, or final acceptance rule. A controlled comparison needs measured costs, detection coverage, harmful misses, calibration, held-out retention, and deliberate observation of checks the selector would otherwise omit. Evidence of deployment value would require a later study in the target setting.

## Closing the workshop

This workshop can close in one of three ways:

- **Promote a method claim** only after the ontology and acceptance semantics are explicit and a controlled comparison supplies measured cost, detection coverage, harmful-miss, calibration, expenditure, and retention evidence.
- **Hand off an experiment or proposal** if the maintainer authorizes separately scoped work to gather missing evidence or choose an implementation, without promoting effectiveness claims.
- **Close without promotion** if the evidence is negative, the required assumptions cannot be defended, or the inquiry is not worth continuing.

The maintainer must choose the disposition and any promotion order. A durable note, proposal, experiment, implementation, or external contact is separate work. Author replies would be welcome but are not required for closure.
