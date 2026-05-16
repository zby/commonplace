---
description: Counting lower bound on summary-based memory — exact universal answering over a rich query family requires summary space at least as large as the query-induced state partition
type: kb/notes/types/structured-claim.md
traits: []
tags: [computational-model, context-engineering, learning-theory]
status: seedling
---

# No universal distillation preserves all task-relevant structure

[Distillation](../../notes/definitions/distillation.md) works because it targets a specific consumer-task pair. The source persists because the distillate is lossy. This note makes that necessity explicit. Fix a state space `X`, a family of downstream queries `Q`, and a summary budget of `b` bits. A **universal distillation** for `Q` is a summary map `sigma: X -> {0,1}^b` plus a decoder `delta` such that for every state `x` and every downstream query `q in Q`, the answer `q(x)` can be recovered from `sigma(x)` and `q` alone. Such a distillation exists only if the summary space is large enough to separate all query-relevant distinctions in `X`. Equivalently: if `Q` induces more than `2^b` distinct answer profiles over `X`, then no `b`-bit universal distillation exists. In particular, for sufficiently rich query families on growing states, no bounded-size summary can preserve all task-relevant structure.

## Evidence

- The KB's own definition of [distillation](../../notes/definitions/distillation.md) already says the target is always a specific consumer-task pair and that multiple distillations of the same source are normal. This theorem explains why that targeting is not just practical advice but a structural necessity.
- The right notion of "task-relevant structure" is not every detail of `x`, but the partition of states induced by `Q`. Two states are equivalent if every query in `Q` gives the same answer on both. Any exact summary only needs to preserve the equivalence class, not the raw state.
- A summary with `b` bits has at most `2^b` possible outputs. So it can distinguish at most `2^b` equivalence classes or answer profiles.
- Rich query families can induce exponentially many profiles. Canonical example: `X = {0,1}^N`, `Q = {q_i(x) = x_i : i in [N]}` together with arbitrary downstream Boolean functions of the bits, or simply `Q = {q_S(x) = x_S : S subseteq [N]}`. Then distinct states have distinct answer profiles, so exact universal summarization requires `Omega(N)` bits.

## Reasoning

For each state `x in X`, define its **answer profile** under `Q` as

`A_Q(x) = (q(x))_(q in Q)`.

Two states are task-equivalent exactly when they have the same answer profile. An exact universal distillation needs only to preserve `A_Q(x)`, but it must preserve that profile completely.

Suppose there are more than `2^b` distinct answer profiles but the summary has only `2^b` possible outputs. By the pigeonhole principle, there exist two states `x != y` such that

- `sigma(x) = sigma(y)`, but
- `A_Q(x) != A_Q(y)`.

Since the profiles differ, there exists at least one query `q in Q` such that `q(x) != q(y)`.

Now run the decoder on that query. Because `sigma(x) = sigma(y)`, the decoder sees exactly the same inputs in both cases: the same summary and the same query. So it must produce the same output on both inputs:

`delta(sigma(x), q) = delta(sigma(y), q)`.

But exactness requires that output to equal `q(x)` in one world and `q(y)` in the other, and those values differ. Contradiction.

Therefore any exact universal distillation for `Q` needs at least as many summary codes as there are distinct query-induced answer profiles. In bit terms, the minimum summary size is at least

`log_2 |{A_Q(x) : x in X}|`.

This yields the promised impossibility statement. If the number of query-induced profiles grows without bound with state size while the summary budget stays fixed, then eventually the summary space is too small and a universal distillation becomes impossible.

The practical consequence is that "compress once and discard the originals" is sound only for a restricted downstream query family known in advance. General-purpose memory does not have that property: future tasks may ask queries that separate states the summary collapsed. So a general memory system must either keep the originals, keep pointers back to them, or accept re-distillation and lossy failure on some future tasks.

## Caveats

- The theorem is about **exact worst-case universal** preservation. Approximate summaries, probabilistic guarantees, or task distributions can still be useful in practice.
- The lower bound is only as strong as the downstream query family. If `Q` is coarse, a very small summary may be enough. This is not an anti-distillation result; it is a formal statement that distillation must be targeted.
- Keeping a bounded summary plus access to the original state does not violate the theorem. The impossibility is about the summary being sufficient on its own after the originals are discarded.
- Interactive recovery changes the model. A system that can go back to storage, reopen sources, or ask additional bounded calls is no longer relying on one fixed summary artifact to answer every future query.

---

Relevant Notes:

- [distillation](../../notes/definitions/distillation.md) — foundation: this theorem formalizes why distillation must be targeted to a consumer-task pair rather than treated as lossless compression
- [evolving understanding needs re-distillation not composition](../../notes/evolving-understanding-needs-re-distillation-not-composition.md) — consequence: when downstream needs change, the right response is re-distillation, not faith that one old summary preserved every future distinction
- [bounded-context orchestration model](../../notes/bounded-context-orchestration-model.md) — context: compaction of symbolic state is a summary map, so the theorem identifies the structural limit of "summarize K and keep going"
- [LLM-mediated schedulers are a degraded variant of the clean model](../../notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — instance: conversation compaction is precisely the kind of bounded summary this theorem says cannot be universally sufficient
- [exact retrieval over semantically opaque items requires linear inspection](./exact-retrieval-over-semantically-opaque-items-requires-linear.md) — parallel lower bound: one rules out universal compression, the other rules out universal pruning without semantic inspection
