---
description: Any symbolic program with bounded LLM calls can be mechanically converted into the select/call loop with the same calls — the model's invariants hold by construction for all such programs
type: note
tags: [computational-model]
status: seedling
---

# Any symbolic program with bounded calls is a select/call program

## The decomposition lemma

**Claim.** Any program whose operations are (a) symbolic computation over state `K` and (b) bounded LLM calls `r = call(P)` can be mechanically converted into the [base loop](./bounded-context-orchestration-model.md):

```
while not satisfied(K):
    P  = select(K)
    r  = call(P)
    K  = K + r
```

with `select` a symbolic function and the *same sequence of bounded calls*.

**Why.** At each call site, everything available to decide the next prompt is the original inputs plus prior call results — exactly `K`. So `select(K)` can reproduce the prompt by encoding the original program's logic (conditionals, loop counters, phase tracking) as dispatch over `K`. This is the same sense in which any program can be refactored into a state-machine loop.

**Consequence.** The base model's three invariants — bounded context per call, explicit state in `K`, symbolic orchestration — hold **by construction** for any program satisfying the preconditions. No per-program verification needed.

## The ergonomic direction

The practical value runs opposite to the conversion: write in whatever style is natural (sequential phases, map/filter pipelines, nested loops) and the lemma guarantees it's a valid select/call program. You never need to flatten into a monolithic `select` — you just need to know you could.

## Scope

**LLM-mediated scheduling.** The lemma requires inter-call computation to be symbolic. When the program uses an LLM call to decide what to do next (an [LLM-mediated scheduler](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md)), precondition (a) is violated and the symbolic-orchestration invariant no longer holds by construction.

**Concurrent shared state.** Independent fan-out fits the model fine. But calls that need mid-flight visibility into each other's results require synchronisation that the sequential base loop doesn't express.

## Open questions

- The [decomposition heuristics](./decomposition-heuristics-for-bounded-context-scheduling.md) might be expressible as transformations that increase call count while decreasing per-call complexity — the lemma guarantees the transformed program is still a valid select/call program.

---

Relevant Notes:

- [bounded-context orchestration model](./bounded-context-orchestration-model.md) — foundation: the base model whose universality the lemma establishes
- [decomposition heuristics for bounded-context scheduling](./decomposition-heuristics-for-bounded-context-scheduling.md) — consequence: the heuristics become transformations between programs the lemma certifies as valid
- [LLM-mediated schedulers are a degraded variant of the clean model](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — boundary: LLM-mediated scheduling still decomposes but loses symbolic-orchestration invariant
