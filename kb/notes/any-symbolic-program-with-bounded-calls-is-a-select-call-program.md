---
description: Any program whose symbolic execution between bounded LLM calls can be reified as explicit state can be mechanically converted into the select/call loop with the same call sequence
type: note
tags: [computational-model]
status: seedling
---

# Any symbolic program with bounded calls is a select/call program

## The decomposition lemma

**Claim.** Any program whose execution consists of:

- symbolic computation over explicit machine state `K`
- bounded LLM calls `r = call(P)`

can be mechanically converted into the [base loop](./bounded-context-orchestration-model.md):

```
while not satisfied(K):
    P  = select(K)
    r  = call(P)
    K  = K + r
```

with `select` a symbolic function and the *same sequence of bounded calls*.

Here `K` must contain the full symbolic machine state needed to resume execution: original inputs, prior call results, control location, loop counters, phase tags, pending work items, and any other symbolic locals the program consults between calls.

**Why.** First define `satisfied(K)` to mean: starting from machine state `K`, symbolic execution reaches program halt before encountering another LLM call site.

Then, for any state with `not satisfied(K)`, define `select(K)` as: run the program's symbolic transition logic from the current machine state until the next LLM call site is reached, and emit that prompt `P`.

Because all inter-call computation is symbolic, both checks are exact. On non-halting states, the next prompt is therefore a function of the current symbolic state alone. Iterating this construction reproduces the original program's call order and prompt contents, so the transformed loop makes the same bounded calls in the same sequence.

This is not a special property of LLM programs. It is the standard move behind operational semantics and abstract machines: execution is represented as transitions over explicit configurations, and control state that was implicit in source structure is reified into data.

**Consequence.** Once a program is shown to satisfy the preconditions, the base model's three invariants — bounded context per call, explicit state in `K`, symbolic orchestration — hold **by construction**. No additional invariant proof is needed for each program beyond checking those preconditions.

## The ergonomic direction

The practical value runs opposite to the conversion: write in whatever style is natural (sequential phases, map/filter pipelines, nested loops) and the lemma guarantees it's a valid select/call program. You never need to flatten into a monolithic `select` — you just need to know you could.

## Scope

**LLM-mediated scheduling.** The lemma requires inter-call computation to be symbolic. When the program uses an LLM call to decide what to do next (an [LLM-mediated scheduler](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md)), that symbolic-computation precondition is violated and the symbolic-orchestration invariant no longer holds by construction.

**Concurrency.** Independent fan-out, barriers, and merges still fit the model: pending tasks and partial results can be represented in `K`, and the scheduler can serialize the coordination logic without changing which bounded calls occur. The real boundary is not concurrency itself but interaction that cannot be reduced to symbolic state transitions between calls — for example, mid-call visibility into another in-flight call, or dependence on external mutable state that is not represented in `K`.

## Known lineage

The basis for the construction is standard programming-languages machinery rather than a special theorem about LLM systems:

- **Small-step / structural operational semantics** represents execution as transitions over machine configurations.
- **Abstract-machine compilation** reifies control state explicitly so the next transition is a first-order function of the current state.
- **CPS plus defunctionalization** is the classic route when control flow needs to be turned into explicit symbolic state.

This note applies that generic compilation move to the specific case where the only non-symbolic steps are bounded LLM calls.

## Open questions

- The [decomposition heuristics](./decomposition-heuristics-for-bounded-context-scheduling.md) might be expressible as transformations that increase call count while decreasing per-call complexity — the lemma guarantees the transformed program is still a valid select/call program.

---

Relevant Notes:

- [bounded-context orchestration model](./bounded-context-orchestration-model.md) — foundation: the base model whose universality the lemma establishes
- [decomposition heuristics for bounded-context scheduling](./decomposition-heuristics-for-bounded-context-scheduling.md) — consequence: the heuristics become transformations between programs the lemma certifies as valid
- [LLM-mediated schedulers are a degraded variant of the clean model](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — boundary: LLM-mediated scheduling still decomposes but loses symbolic-orchestration invariant
