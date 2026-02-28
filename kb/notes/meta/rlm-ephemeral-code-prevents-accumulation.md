---
description: RLM discards generated code after each run — the single design choice that separates it from llm-do
areas: []
status: current
---

# RLM ephemeral code prevents accumulation

Both RLM and llm-do let LLMs write and execute code. The central difference is what happens to that code afterward.

## The fork

In RLM, generated code is **ephemeral**. The LLM writes a Python snippet, the REPL executes it, the result feeds back into the conversation, and the code is discarded. Next query, next user — same problem, re-derived from scratch.

In llm-do, generated code is **persistent by default**. An LLM-generated tool lands in a file, enters version control, and becomes available to every future run. The code accumulates.

```
RLM:    generate → execute → discard
llm-do: generate → execute → save → test → version → reuse
```

## What RLM's design buys

RLM makes two coupled choices: ephemeral code (discard after execution) and purely functional tools (no side effects — no filesystem, no network, no state mutation). Together they buy significant simplicity:

- **No approval problem.** This comes from functional isolation, not ephemerality. Code that can only compute and return values needs no gating. Ephemeral code that could call `rm -rf` would still need approval. But the two choices reinforce each other — ephemeral code is easier to keep side-effect-free because there's no temptation to build on previous state.
- **No state management.** Each run is a clean slate. No lifecycle hooks, no resource cleanup, no isolation between nested calls.
- **No maintenance burden.** Code that doesn't exist can't go stale, break, or accumulate tech debt.

The no-side-effects constraint does limit what RLM can do in practice — it can't write files, call APIs, or modify databases. For analytical workloads (data analysis, computation, visualization) this is fine. For agentic workloads that need to act on the world, it's a hard ceiling.

Still, this is a legitimate design point. Many useful tasks are purely analytical, and for those, RLM's simplicity is a real advantage.

## What ephemeral code costs

Every pattern the LLM discovers must be rediscovered on the next run. This means:

- **No learning across runs.** A good decomposition strategy for a data analysis task is lost the moment the session ends. The system cannot get better at recurring problems.
- **No testing.** You can't write a unit test for code that doesn't exist between runs. Correctness is verified per-execution or not at all.
- **No review.** There is no artifact for a human to inspect, approve, or improve. The LLM's reasoning is a black box that produces results.
- **No reuse.** Two users with the same question trigger two independent generations. Shared solutions require re-derivation.

## The crystallisation alternative

llm-do treats code generation as the first step of [crystallisation](../deploy-time-learning-the-missing-middle.md) — converting stochastic LLM behavior into deterministic, testable infrastructure. An LLM might generate a tool during a session; that tool then enters the standard software lifecycle (version control, testing, code review). Over time, the system gets better because its solutions accumulate.

This is not free. Persistent code requires approval gates for side effects, lifecycle management for stateful tools, and maintenance effort to keep things current. But it means the system *learns* — not through weight updates, but through the repo.

## The question each project answers

**RLM asks:** How do I solve this problem right now, as powerfully as possible?

**llm-do asks:** How do I solve this problem in a way that makes the next problem easier?

The answer to the first question is ephemeral code. The answer to the second is versioned infrastructure.

---

Relevant Notes:
- [RLM Implementations vs llm-do](../related_works/rlm-comparison.md) — comprehensive five-divergence comparison
- [RLM explained](../related_works/rlm-explained.md) — what the RLM pattern is and how it works
- [deploy-time-learning](../deploy-time-learning-the-missing-middle.md) — the three timescales framework that motivates versioned code
- [storing-llm-outputs-is-stabilization](../storing-llm-outputs-is-stabilization.md) — extends this: even storing an LLM's raw output is a form of stabilization
