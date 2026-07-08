# Epistemic review gates

Layer: assessment.

The review subsystem (note-gate pairs, freshness, acceptance state) supports new gates without new plumbing. Two flavors, kept separate:

## Structural gates (deterministic, validator-checkable)

- Every claim has a source-span.
- Every `contested` claim shows at least one rebuttal edge.
- Every gap is linked from the claim it blocks.

[Reasoning production is not reasoning evaluation](../../notes/reasoning-production-is-not-reasoning-evaluation.md) argues the rebuttal check needs a *decorrelated* reviewer — don't let the pass that wrote the support also grade it.

## Semantic gates (judgment, for the semantic review system)

Complementing the structural set — these are judgment calls, not deterministic checks:

- `source-span-fidelity` — does the claim accurately represent the cited span?
- `scope-creep` — a conclusion exceeds the population, timeframe, method, or source context.
- `rhetorical-overweighting` — prestige, vividness, or narrative force used as if it were direct evidence.
- `missing-countercase` — an assessment that does not represent the strongest serious opposing view.
- `settlement-illusion` — a debate called settled when only social/institutional closure has been shown.
- `correlation-double-counting` — evidence treated as independent when it shares data, authorship, method, or citation ancestry (see [independence clustering](./independence-clustering.md)).
