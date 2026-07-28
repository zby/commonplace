---
description: "A model supplies content from weights or context; a fact that reached neither is unavailable at any capability. The clean case is a commitment, which pre-decision evidence does not entail; once recorded, a local fact can be learned"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, deploy-time-learning, agent-memory]
---

# Unobserved local information cannot be recovered by capability alone

A model can supply content from exactly two places: its weights, which hold what some training corpus contained, and its context, which holds what some channel delivered. Capability — scale, reasoning, sample efficiency — improves what a model can *infer* from those sources; it cannot substitute for a fact that reached neither. The gap an unobserved fact leaves is missing information, not missing intelligence, and no model upgrade closes it.

The clean case is a commitment. Since [commitment, not derivation, creates new ground truth](./commitment-not-derivation-creates-new-ground-truth.md), the state of the world before a decision does not entail which option was picked: however complete the pre-decision corpus and however strong the model reading it, the resolution exists nowhere until it is recorded. Other local facts — this cluster runs three shards, this flag is off in staging — are the ordinary case: entailed by the deployment, but out of reach for any model that never observed the deployment.

The claim is channel-conditioned, not permanent. Once recorded, a local fact is text like any other: it can enter a public corpus, a deployment-local fine-tune, or a continually trained adapter, and then be supplied unaided — [whether the copy can stand in for the record is a separate question](./parametric-reproduction-cannot-replace-an-authoritative-record.md). What the claim fixes is the order of operations: observation and recording come first, and they are work of the deployment, not of the model. A retention layer's first job is to be that channel, capturing local facts at production time — [the one chance history has to become checkable](./history-has-one-chance-to-become-checkable.md). Stronger models make captured facts more valuable, because more of them become actionable, and remove none of the capture work.

Closing the channel through training relocates it rather than removing it: a deployment that continually trains on its own records has built a slower, coarser retention layer inside the weights — the same relocation [in-context learning presupposes context engineering](./in-context-learning-presupposes-context-engineering.md) finds when continual learning is declared unnecessary.

## Scope

- The claim is relative to a fixed model artifact and its declared observation, input, and update channels. It forecasts nothing about which content a next model generation will hold.
- Being learnable is weaker than being reliably supplied: [knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md), so even a learned local fact may still need the explicit record for dependable delivery in a bounded context.
- Recoverability is one axis of retention economics, not the whole judgment. Update latency, staleness tolerance, and governance force divide content independently of whether a model could in principle learn it; a redundancy claim should name which axis it rests on.
- An earlier note claimed the categorical form — deployment-local state can *never* be absorbed, "by construction" absent from every corpus — and was deleted on review (full-pass `20260728T121249Z-a3f7`). The error: non-entailment holds before the record exists, and the categorical claim needed the record to also stay out of every later training stream, which nothing guarantees. This note and [parametric reproduction cannot replace an authoritative mutable record](./parametric-reproduction-cannot-replace-an-authoritative-record.md) carry what survived.

## Open Questions

- When does a general artifact's redundancy clock actually start? Availability of the content somewhere in a model's capability is not sufficient while bounded-context activation, fidelity, and retrieval remain material — and absorption forecasts in the wild are typically unfalsifiable as stated.

---

Relevant Notes:

- [Commitment, not derivation, creates new ground truth](./commitment-not-derivation-creates-new-ground-truth.md) — grounds: why pre-decision evidence cannot entail a decision, making commitments the clean case of unobserved local information
- [Parametric reproduction cannot replace an authoritative mutable record](./parametric-reproduction-cannot-replace-an-authoritative-record.md) — extends: what remains after the channel closes — a learned copy still cannot do the record's job
- [History has one chance to become checkable](./history-has-one-chance-to-become-checkable.md) — grounds: capture happens at production time or the information is gone, for models as for any later reader
- [In-context learning presupposes context engineering](./in-context-learning-presupposes-context-engineering.md) — extends: the relocation move — closing an observation channel through training rebuilds the retention layer in a slower substrate
- [Knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md) — grounds: why "entered a corpus" does not yet mean "supplied unaided where needed"
- [Lessons from building AI agents for financial services](../sources/lessons-from-building-ai-agents-for-financial-services.ingest.md) — evidenced-by: an unfalsifiable "models will absorb basic skills" forecast, the failure mode the channel-conditioned form avoids
