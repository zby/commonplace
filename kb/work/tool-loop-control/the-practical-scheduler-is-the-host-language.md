---
description: The simplest practical orchestration library demotes the tool loop to a returning, per-call-parameterized function and lets ordinary host-language code play select and K — reifying K only when the run must outlive its process or outgrow its memory
type: kb/types/note.md
traits: [title-as-claim]
tags: [computational-model, context-engineering]
status: seedling
---

# The practical scheduler is the host language, not a reified select

The [bounded-context orchestration model](../../notes/bounded-context-orchestration-model.md) gives the general shape of any system that drives bounded LLM calls: `while (P := select(K)) is not None: r = call(P); K = K + r`. As a model it is complete. As the basis for a library it is impractical for one specific reason: it asks you to **reify `select` and `K` as explicit objects** — author a selection function, maintain an explicit state blob, and assemble each prompt by hand. That is far more machinery than most work needs.

The framework-owned tool loop sits at the opposite pole: it reifies *nothing*. But it buys that convenience by [freezing `select`](./llm-frameworks-should-keep-the-tool-loop-optional.md) to one policy — append the tool result, re-ask with the same tools — and thereby owning progression. The application can no longer change the tool surface, project state selectively, branch, or decide when to halt.

The simplest mechanism that escapes both poles does not pick a better `select`. It **declines to reify `select` and `K` at all, and lets the host language play both roles.** Concretely, demote the tool loop to an ordinary returning function:

```python
result = agent(prompt, tools, stop)   # runs the frozen loop internally, then RETURNS
```

Relative to the frozen loop, two changes are enough:

1. **It returns control** to the caller instead of auto-continuing to a fixed next step.
2. **Its three parameters — prompt, capability surface, stop condition — are supplied per call**, not fixed for the whole run. (The frozen loop already takes a prompt and tools; what is new is that all three vary call to call, and the stop condition becomes a caller-supplied predicate rather than the hardcoded "model emitted no tool call.")

These two changes suffice because they restore both halves of `select` to the caller: returning hands control back, and per-call parameters let host code decide what the next call sees and does. Together they put the halt/continue and framing decisions in the caller's hands — which is exactly what owning `select` means.

And once those decisions are the caller's, there is nothing left for a library to reify. The host program's control flow already *realizes* `select`, distributed across its branches and loops; its live variables already *hold* `K`. This is not a departure from the model but an instance of it: [any symbolic program with LLM calls is a select/call program](../../notes/any-symbolic-program-with-llm-calls-is-a-select-call-program.md). That lemma says any such program can be mechanically converted into an explicit `select`/`K` loop with the same calls in the same order — so `select` and `K` are *already present* in the host program, latent in its control state and locals, and could be reified at any point. The practical move is to leave them latent. The library's job is not to supply `select`; it is to hand back a loop the host language can call, then get out of the way.

## What falls out of composition

Every forcing case the tool-loop family enumerates is then recovered by ordinary host-language composition, with no scheduler abstraction:

- **sub-agent / recursive decomposition** → call `agent()` recursively; "spawn another tool loop" is a function call, so [a child loop with its own surface](../../notes/agent-is-a-tool-loop.md) is just re-invocation
- **different capability surface** → pass a different `tools` argument (the central forcing case)
- **selective state projection** → build the next prompt from your own variables; nothing is inherited unless you pass it, which is why [session history need not be the default next context](../../notes/session-history-should-not-be-the-default-next-context.md)
- **branch and merge** → call `agent()` twice, reconcile in code
- **a [semantic sub-goal too big for one window](../../notes/semantic-sub-goals-that-exceed-one-context-window-become-scheduling.md)** → a `for` loop over `agent()` calls plus a code-side aggregate

None of these require a scheduler object, an explicit `K`, or an authored `select`. They are loops, branches, and variables in the host language.

## The minimal surface is one primitive plus one hook

The convenience loop everyone uses today is just the **degenerate call** `agent(prompt, tools, stop=model_finished)` with a fixed tool set. It is not a separate layer beneath or above the orchestration interface — it is the same primitive with a trivial stop and constant arguments. So the practical library needs only:

1. `agent(prompt, tools, stop) -> result` — a returning, per-call-parameterized tool loop; sub-agents are recursive calls.
2. A **tool-execution middleware hook** — for the dispatch-side interventions (logging, budgets, projection of tool *results*, deterministic transforms) that wrap a single execution and never justify a fresh call.

The hook is not absolutely irreducible — a caller could in principle wrap each tool function before passing it in. What makes it a distinct surface is *where the interposition point lives*: `agent()` runs the inner dispatch loop itself, so the moment between "model requested tool X" and "tool X runs" is inside the primitive, not in the caller's code. The hook is the one point of entry into that interior; without it the caller cannot uniformly observe or modify dispatch across every tool the loop drives. So the two surfaces partition cleanly by *what they reach*: `agent()`'s parameters control the next call's action alphabet, while the hook reaches inside the current call's execution and changes nothing about what the next step may do. This is the same boundary that distinguishes hidden bookkeeping from capability-surface change, and the interposition point is the lifecycle hook that appears independently across harness designs.

The subtle part to get right is the **stop condition**. The frozen loop hardcodes it to "model emitted no tool call." The minimal generalization is a **caller-supplied predicate**: model finished, budget exceeded, step cap reached, a designated submit tool called, or a structured output validated. Prompt and tools are trivial to expose, but the stop predicate is how application code reclaims the halt/continue decision the frozen loop swallowed — so it is where a library earns or loses its practicality.

## Scope

The host language stands in for `K` for free under one condition: a single process holds the whole run in live memory from start to finish. Two things break that condition. The first is a **lifetime mismatch** — the run must outlive the process that started it: a process that can die mid-run and resume, a pause for human approval, or work spread across machines. The second is a **capacity mismatch** — `K` outgrows what the process can hold, so it must spill to external storage even within one synchronous run. In either case the call stack and local variables can no longer carry `K`, so it must become checkpointable, externally-addressable state again, and reifying it is no longer optional.

(Wanting an audit or observability record of `K` does *not* by itself force reification: a logged copy can sit beside an otherwise-ephemeral run. Reification is forced only when the *operative* `K` — the state the next step actually reads — can no longer live in the process.)

That boundary is the principled reason a heavier durable-execution or externalized-state framework is justified later: not because the loop abstraction was wrong, but because the host language can no longer stand in for `K`.

---

Relevant Notes:

- [bounded-context orchestration model](../../notes/bounded-context-orchestration-model.md) — grounds: the general select/call loop whose `select`/`K` this note argues a practical library should not reify
- [llm frameworks should keep the tool loop optional](./llm-frameworks-should-keep-the-tool-loop-optional.md) — extends: sharpens "keep the loop optional" into "make the loop a returning value and let the host language be select and K"
- ["agent" is a tool loop](../../notes/agent-is-a-tool-loop.md) — mechanism: the unit this primitive returns; sub-agents are recursive calls to it
- [any symbolic program with LLM calls is a select/call program](../../notes/any-symbolic-program-with-llm-calls-is-a-select-call-program.md) — grounds: why the host program already is the symbolic scheduler
- [llm-mediated schedulers are a degraded variant of the clean model](../../notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — contrasts: not reifying `K` in code is the opposite failure mode from pushing `K` back into the conversation
- [semantic sub-goals that exceed one context window become scheduling problems](../../notes/semantic-sub-goals-that-exceed-one-context-window-become-scheduling.md) — exemplifies: a forcing case that becomes an ordinary host-language loop once `agent()` returns
