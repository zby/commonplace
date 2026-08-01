# Case packet

Neutral case identifier: case-de38abeca27643

The possible directed relationship from Artifact A to Artifact B is under review.

## Artifact A

# The practical scheduler is the host language, not a reified select

The [bounded-context orchestration model] gives the general shape of any system that drives bounded LLM calls: `while (P := select(K)) is not None: r = call(P); K = K + r`. As a model it is complete. As the basis for a library it is impractical for one specific reason: it asks you to **reify `select` and `K` as explicit objects** — author a selection function, maintain an explicit state blob, and assemble each prompt by hand. That is far more machinery than most work needs.

The framework-owned tool loop sits at the opposite pole: it reifies *nothing*. But it buys that convenience by [freezing `select`] to one policy — append the tool result, re-ask with the same tools — and thereby owning progression. The application can no longer change the tool surface, project state selectively, branch, or decide when to halt.

The simplest mechanism that escapes both poles does not pick a better `select`. It **declines to reify `select` and `K` at all, and lets the host language play both roles.** Concretely, demote the tool loop to an ordinary returning function:

```python
result = agent(prompt, tools, stop)   # runs the frozen loop internally, then RETURNS
```

Relative to the frozen loop, two changes are enough:

1. **It returns control** to the caller instead of auto-continuing to a fixed next step.
2. **Its three parameters — prompt, capability surface, stop condition — are supplied per call**, not fixed for the whole run. (The frozen loop already takes a prompt and tools; what is new is that all three vary call to call, and the stop condition becomes a caller-supplied predicate rather than the hardcoded "model emitted no tool call.")

These two changes suffice because they restore both halves of `select` to the caller: returning hands control back, and per-call parameters let host code decide what the next call sees and does. Together they put the halt/continue and framing decisions in the caller's hands — which is exactly what owning `select` means.

And once those decisions are the caller's, there is nothing left for a library to reify. The host program's control flow already *realizes* `select`, distributed across its branches and loops; its live variables already *hold* `K`. This is not a departure from the model but an instance of it: [any symbolic program with LLM calls is a select/call program]. That lemma says any such program can be mechanically converted into an explicit `select`/`K` loop with the same calls in the same order — so `select` and `K` are *already present* in the host program, latent in its control state and locals, and could be reified at any point. The practical move is to leave them latent. The library's job is not to supply `select`; it is to hand back a loop the host language can call, then get out of the way.

## What falls out of composition

Every forcing case the tool-loop family enumerates is then recovered by ordinary host-language composition, with no scheduler abstraction:

- **sub-agent / recursive decomposition** → call `agent()` recursively; "spawn another tool loop" is a function call, so [a child loop with its own surface] is just re-invocation
- **different capability surface** → pass a different `tools` argument (the central forcing case)
- **selective state projection** → build the next prompt from your own variables; nothing is inherited unless you pass it, which is why [session history need not be the default next context]
- **branch and merge** → call `agent()` twice, reconcile in code
- **a [semantic sub-goal too big for one window]** → a `for` loop over `agent()` calls plus a code-side aggregate

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

## Artifact B

# Any symbolic program with LLM calls is a select/call program

## The decomposition lemma

**Claim.** Any program whose execution consists of:

- symbolic computation over explicit machine state `K`
- LLM calls `r = call(P)`

can be mechanically converted into the [base loop]:

```
while (P := select(K)) is not None:
    r  = call(P)
    K  = K + r
```

with `select` a symbolic function that returns either the next prompt or `None`, and with the *same LLM calls in the same order*.

Here `K` must contain the full symbolic machine state needed to resume execution: original inputs, prior call results, control location, loop counters, phase tags, pending work items, and any other symbolic locals the program consults between calls.

`K + r` means incorporating the call result into explicit symbolic state. In the simplest event-sourced case this is append-only: `K` stores the full trace, and later symbolic steps recompute derived views from it. Implementations may also cache derived state, but those caches are still explicit parts of `K`.

**Why.** Define `select(K)` as: run the program's symbolic transition logic from the current machine state until either program halt or the next LLM call site is reached. If symbolic execution reaches halt first, return `None`. If it reaches an LLM call site first, emit that prompt `P`.

Because all inter-call computation is symbolic, this check is exact. The halt-or-next-prompt decision is therefore a function of the current symbolic state alone. Iterating this construction reproduces the original program's call order and prompt contents, so the transformed loop makes the same LLM calls in the same order.

This is not a special property of LLM programs. It is the standard move behind operational semantics and abstract machines: execution is represented as transitions over explicit configurations, and control state that was implicit in source structure is reified into data.

**Consequence.** Once a program is shown to satisfy the preconditions, the base model's three invariants — per-call context limits, explicit state in `K`, symbolic orchestration — hold **by construction**. No additional invariant proof is needed for each program beyond checking those preconditions.

## The ergonomic direction

The practical value runs opposite to the conversion: write in whatever style is natural (sequential phases, map/filter pipelines, nested loops) and the lemma guarantees it's a valid select/call program. You never need to flatten into a monolithic `select` — you just need to know you could.

## Scope

**LLM-mediated scheduling.** The lemma requires inter-call computation to be symbolic. When the program uses an LLM call to decide what to do next (an [LLM-mediated scheduler]), that symbolic-computation precondition is violated and the symbolic-orchestration invariant no longer holds by construction.

**Concurrency.** Independent fan-out, barriers, and merges still fit the model: pending tasks and partial results can be represented in `K`, and the scheduler can serialize the coordination logic without changing which LLM calls occur. The real boundary is not concurrency itself but interaction that cannot be reduced to symbolic state transitions between calls — for example, mid-call visibility into another in-flight call, or dependence on external mutable state that is not represented in `K`.

## Known lineage

The basis for the construction is standard programming-languages machinery rather than a special theorem about LLM systems:

- **Small-step / structural operational semantics** represents execution as transitions over machine configurations.
- **Abstract-machine compilation** reifies control state explicitly so the next transition is a first-order function of the current state.
- **CPS plus defunctionalization** is the classic route when control flow needs to be turned into explicit symbolic state.

This note applies that generic compilation move to the specific case where the only non-symbolic steps are LLM calls.

## Open questions

- The [decomposition heuristics] might be expressible as transformations that increase call count while decreasing per-call complexity — the lemma guarantees the transformed program is still a valid select/call program.

---

Relevant Notes:

## Under-review context phrase

why the host program already is the symbolic scheduler
