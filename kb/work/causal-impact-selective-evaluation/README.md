# Causal impact and selective evaluation

> **Workshop status:** This is an exploratory Commonplace workshop. It is not an HCL or SPADE summary, a validated evaluation method, an implementation proposal, or a safety claim.

This workshop connects two ideas. [Harness Continual Learning (HCL)](../../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md) treats a deployed harness around frozen model weights as revisable, regression-gated state. [SPADE](../../sources/spade-self-play-in-adaptive-synthetic-executable-environments.ingest.md) shows how executable environments can themselves be generated, filtered, and valued for learning. Neither work proposes the causal selective-evaluation method explored here.

## Workshop question

Could a revisable theory of which behavioral functions a harness candidate can affect help decide, candidate by candidate, which costly evidence is worth acquiring?

The working proposal treats a candidate as a semantic intervention under an explicit system boundary. An impact theory predicts affected functions or evaluation obligations; a mapping identifies procedures capable of observing them; and an evidence-acquisition policy selects, adapts, or generates procedures before a commitment rule decides whether to adopt the candidate.

The proposal is conditional. Local selection is plausible only when changes are sparse in a matching decomposition, dependencies and authority paths are explicit, and downstream impact is bounded. Selecting less evidence also changes what acceptance can honestly mean: omitted checks remain unknown unless a separately justified residual-risk rule accounts for them, and that rule remains exposed to errors in the impact theory itself.

## Reading map

- [Reading HCL as deployment-time learning](./hcl-reading.md) — the workshop's interpretation of HCL, its sampled-retention boundary, the conditional evaluator-growth calculation, and why HCL's harness partition is not assumed to be a causal graph.
- [A provisional causal selective-evaluation model](./selective-evaluation-model.md) — the working ontology and objects, selector types, acceptance semantics, theory error, selective-observation problem, and limits of the locality hypothesis.
- [Experiment design for causal selective evaluation](./experiment-design.md) — the SPADE-inspired procedure-generation option and a comparison among full evaluation, sampling, dependency, similarity, and causal selectors.
- [An invitation to the HCL authors](./for-hcl-authors.md) — the shorter HCL-facing account and questions.
- [An invitation to the SPADE authors](./for-spade-authors.md) — the shorter SPADE-facing account and questions about adaptive executable evaluations.

## Current boundary

The workshop has not established that causal selection predicts impacts accurately, lowers total evaluation cost, preserves HCL's retention results, or supports a safety claim. It has not chosen the primary registry object, selection objective, materiality threshold, loss units, prediction horizon, calibration protocol, or final acceptance rule. A controlled comparison needs measured costs, detection coverage, harmful misses, calibration, held-out retention, and deliberate observation of checks the selector would otherwise omit.

## Closing the workshop

This workshop can close in one of three ways:

- **Promote a method claim** only after the ontology and acceptance semantics are explicit and a controlled comparison supplies measured cost, detection coverage, harmful-miss, calibration, expenditure, and retention evidence.
- **Hand off an experiment or proposal** if the maintainer authorizes separately scoped work to gather missing evidence or choose an implementation, without promoting effectiveness claims.
- **Close without promotion** if the evidence is negative, the required assumptions cannot be defended, or the inquiry is not worth continuing.

The maintainer must choose the disposition and any promotion order. A durable note, proposal, experiment, implementation, or external contact is separate work. Author replies would be welcome but are not required for closure.
