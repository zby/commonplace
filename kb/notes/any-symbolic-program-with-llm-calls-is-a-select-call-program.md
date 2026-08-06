---
description: Any program whose non-LLM steps are symbolic computation over explicit machine state K can be mechanically converted into the select/call loop with the same LLM calls in the same order
type: kb/types/note.md
traits: [title-as-claim]
tags: [computational-model]
---

# Any symbolic program with LLM calls is a select/call program

## The decomposition lemma

### Claim

Any program whose execution consists of:

- symbolic computation over explicit machine state `K`
- LLM calls `r = call(P)`

can be mechanically converted into the [base loop](./bounded-context-orchestration-model.md):

```
while (P := select(K)) is not None:
    r  = call(P)
    K  = K + r
```

`select` is a symbolic function that returns either the next prompt or `None`; the transformed program makes the *same LLM calls in the same order*.

Here `K` must contain the full symbolic machine state needed to resume execution: original inputs, prior call results, control location, loop counters, phase tags, pending work items, and any other symbolic locals the program consults between calls.

`K + r` means incorporating the call result into explicit symbolic state. In the simplest event-sourced case, incorporation is append-only: `K` stores the full trace, and later symbolic steps recompute derived views from it. Implementations may also cache derived state, but those caches are still explicit parts of `K`.

### Construction

`select(K)` runs the program's symbolic transition logic from the current state until the program halts or reaches the next LLM call site. If the program halts first, `select` returns `None`. If the program reaches a call site first, `select` emits its prompt `P`.

Because all inter-call computation is symbolic, this check is exact. The halt-or-next-prompt decision is therefore a function of the current symbolic state alone. Iterating this construction reproduces the original program's call order and prompt contents, so the transformed loop makes the same LLM calls in the same order.

This is not a special property of LLM programs. Operational semantics and abstract machines use the same move: they represent execution as transitions over explicit configurations and turn control state implicit in source structure into explicit data.

### Consequence

Once a program is shown to satisfy the preconditions, the base model's three invariants — per-call context limits, explicit state in `K`, symbolic orchestration — hold **by construction**. After checking those preconditions, no separate invariant proof is needed for each program.

## Why the conversion is useful

In practice, the lemma lets you write in whatever style is natural — sequential phases, map/filter pipelines, or nested loops — while guaranteeing a valid select/call program. You never need to flatten into a monolithic `select` — you just need to know you could.

## Scope

**LLM-mediated scheduling.** The lemma requires symbolic inter-call computation. If the program uses an LLM call to choose its next step (an [LLM-mediated scheduler](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md)), inter-call computation is no longer entirely symbolic, so the symbolic-orchestration invariant no longer follows by construction.

**Concurrency.** Independent fan-out, barriers, and merges still fit the model: pending tasks and partial results can be represented in `K`, and the scheduler can serialize the coordination logic without changing which LLM calls occur. Concurrency itself is not the boundary. The boundary is interaction that cannot be reduced to symbolic state transitions between calls — for example, mid-call visibility into another in-flight call or dependence on external mutable state not represented in `K`.

## Known lineage

The construction uses standard programming-language machinery rather than a theorem specific to LLM systems:

- **Small-step / structural operational semantics** represents execution as transitions over machine configurations.
- **Abstract-machine compilation** reifies control state explicitly so the next transition is a first-order function of the current state.
- **CPS plus defunctionalization** is the classic route for turning control flow into explicit symbolic state.

This note applies that generic compilation move to programs whose only non-symbolic steps are LLM calls.

## Open questions

- The [decomposition heuristics](./decomposition-heuristics-for-bounded-context-scheduling.md) might be expressible as transformations that increase call count while decreasing per-call complexity. The lemma guarantees that the transformed program remains a valid select/call program.

---

Relevant Notes:

- [orchestration model](./bounded-context-orchestration-model.md) — foundation: the base model whose universality the lemma establishes
- [decomposition heuristics](./decomposition-heuristics-for-bounded-context-scheduling.md) — consequence: the heuristics become transformations between programs the lemma certifies as valid
- [LLM-mediated schedulers are a degraded variant of the clean model](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — boundary: LLM-mediated scheduling still decomposes but loses the symbolic-orchestration invariant
- [Claude Code dynamic workflows](../agentic-systems/claude-code-dynamic-workflows.md) — evidenced-by: a shipped program whose non-LLM steps (JS control flow, `pipeline`/`parallel`, deterministic transforms over agent returns) are exactly the symbolic-over-`K` steps the lemma converts
