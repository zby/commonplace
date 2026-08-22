---
description: Programs whose LLM calls occur in barrier-delimited independent batches can be converted into a select/call loop that preserves call specifications, batch membership, and barrier order
type: kb/types/note.md
traits: [title-as-claim]
tags: [computational-model]
---

# Any barrier-delimited symbolic program with LLM calls is a batched select/call program

## The decomposition lemma

### Claim

Any program whose execution consists of:

- symbolic computation over explicit machine state `K`
- barrier-delimited batches `B = (C_1, ..., C_n)` of one or more LLM calls, with no transition-relevant interaction among members before the barrier

can be mechanically converted into the [base loop](./bounded-context-orchestration-model.md):

```
while (B := select(K)) is not None:
    require independent(B, K)
    R = call_all(B)
    K = transition(K, B, R)
```

`select` is a symbolic function that returns either the next batch or `None`. The transformed program preserves each call specification, which calls share a batch, and the order between batch barriers. A sequential program becomes the special case in which every batch has one member.

Here `K` must contain the full symbolic machine state needed to resume execution: original inputs, prior call results, control location, loop counters, phase tags, pending work items, and any other symbolic locals the program consults between calls.

`call_all(B)` invokes every `call(C_i)` concurrently and returns the aligned result batch `R = (r_1, ..., r_n)` after all members complete. `transition(K, B, R)` then incorporates those results into explicit symbolic state. In the simplest event-sourced case, incorporation is append-only: `K` stores the full trace, and later symbolic steps recompute derived views from it. Implementations may also cache derived state, but those caches are still explicit parts of `K`.

### Construction

`select(K)` runs the program's symbolic transition logic from the current state until the program halts or reaches the next declared call barrier. If the program halts first, `select` returns `None`. Otherwise it emits the indexed call specifications that the original program releases before the next result-dependent transition.

Because execution between barriers is symbolic, the halt-or-next-batch decision is a function of the current symbolic state alone. Iterating this construction reproduces the original program's call specifications, batch membership, and barrier order, so it does not replace concurrent latency with serial latency.

This is not a special property of LLM programs. Operational semantics and abstract machines use the same move: they represent execution as transitions over explicit configurations and turn control state implicit in source structure into explicit data.

### Consequence

Once a program is shown to satisfy the preconditions, the base model's four invariants — per-call context limits, explicit state in `K`, symbolic execution between barriers, and no within-batch interaction — hold **by construction**. After checking those preconditions, no separate invariant proof is needed for each program.

## Why the conversion is useful

In practice, the lemma lets you write in whatever style is natural — sequential phases, parallel maps, pipelines separated by barriers, or nested loops — while guaranteeing a valid batched select/call program. You never need to flatten the program into a monolithic `select` — you just need to know you could.

## Scope

**LLM-mediated scheduling.** The lemma requires symbolic inter-call computation. If the program uses an LLM call to choose its next step (an [LLM-mediated scheduler](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md)), inter-call computation is no longer entirely symbolic, so the symbolic-orchestration invariant no longer follows by construction.

**Concurrency.** Independent fan-out, barriers, and merges fit as batches and transitions without serializing the calls. Staggered overlapping calls without a shared barrier do not fit this construction directly. Nor do calls with mid-call visibility into another in-flight call or dependence on external mutable state not represented in `K`; those need an event-driven or environment-state model.

## Known lineage

The construction uses standard programming-language machinery rather than a theorem specific to LLM systems:

- **Small-step / structural operational semantics** represents execution as transitions over machine configurations.
- **Abstract-machine compilation** reifies control state explicitly so the next transition is a first-order function of the current state.
- **CPS plus defunctionalization** is the classic route for turning control flow into explicit symbolic state.

This note applies that generic compilation move to programs whose only non-symbolic steps are barrier-delimited independent batches of LLM calls.

## Open questions

- The [decomposition heuristics](./decomposition-heuristics-for-bounded-context-scheduling.md) might be expressible as transformations that increase call count while decreasing per-call complexity. The lemma guarantees a valid select/call program only when a transformation preserves explicit state, batch independence, and barrier order.

---

Relevant Notes:

- [orchestration model](./bounded-context-orchestration-model.md) — foundation: the conditional normal form that this lemma establishes for programs meeting its symbolic-state and barriered-batch preconditions
- [decomposition heuristics](./decomposition-heuristics-for-bounded-context-scheduling.md) — consequence: heuristics that preserve the lemma's preconditions become transformations between programs it certifies as valid
- [LLM-mediated schedulers are a degraded variant of the clean model](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — boundary: LLM-mediated scheduling still decomposes but loses the symbolic-orchestration invariant
- [Claude Code dynamic workflows](../agentic-systems/claude-code-dynamic-workflows.md) — evidenced-by: a shipped program whose non-LLM steps (JS control flow, `pipeline`/`parallel`, deterministic transforms over agent returns) are exactly the symbolic-over-`K` steps the lemma converts
