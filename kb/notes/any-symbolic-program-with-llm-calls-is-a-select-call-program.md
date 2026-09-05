---
description: "Explains the LLM-call projection preserved when symbolic programs are converted to batched select/call form, and the additional semantics needed for effects and mutable harness configuration"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [computational-model]
---

# Any barrier-delimited symbolic program with LLM calls is a batched select/call program

## The decomposition lemma

Any program whose execution consists of:

- symbolic computation over explicit machine state `K_total`
- finite, nonempty, barrier-delimited batches `B = (C_1, ..., C_n)` of LLM calls, with no transition-relevant interaction among members before the shared barrier

can be mechanically converted into the [base loop](./bounded-context-orchestration-model.md):

```
while (B := select(K_total)) is not None:
    require independent(B, K_total)
    R = call_all(B)
    K_total = transition(K_total, B, R)
```

`select` runs symbolic transition logic until the program halts or reaches the next barrier. It then returns `None` or the indexed calls released before the next result-dependent transition. `call_all` invokes the batch concurrently and returns aligned results only after all members finish. `transition` records those results in explicit state. Sequential execution is the special case in which each batch has one member.

`K_total` contains everything the fixed machine needs to resume: run inputs, prior results, control position, pending work, derived caches, and any other transition-relevant state. An append-only event log is one possible representation, but not a requirement.

Each call specification `C` must include every coordinate whose change can alter the request's meaning, the provider's interpretation, the result distribution, the actions exposed to the model, or the response contract. This normally includes the provider or adapter, model, complete messages or prompt, task and response contract, tool schemas or other exposed capabilities, and behavior-changing parameters. The list is provider-dependent. Tool schemas belong to `C`; tool execution does not. A host stop rule belongs to the symbolic transition unless it is part of the model invocation itself.

Because the work between barriers is symbolic, the halt-or-next-batch decision is a function of `K_total`. Iteration therefore reproduces the original complete call specifications, batch membership, and barrier order without serializing independent members of a batch.

## What the lemma preserves

The result is LLM-call projection equivalence. Represent a run's projection as a sequence of indexed batches. Two runs have the same projection when corresponding positions contain equal complete `C` values and the same barrier sequence. An index aligns concurrent members for comparison; it does not impose a wall-clock completion order within the batch.

When a later call depends on an earlier result, compare the runs under aligned returned results. Equal requests do not guarantee equal results: provider state, nondeterminism, and failures may still differ.

The lemma does not establish operational equivalence. It does not by itself preserve non-LLM effects, observations, failures, timing, emissions, or final external state. Once the preconditions hold, the call-oriented select/call invariants follow by construction. Any stronger equivalence still needs its own observer, effect, and lifecycle semantics.

## Non-LLM effects need separate semantics

Pure symbolic computation over `K_total` can be absorbed into `select` or `transition`. A filesystem read, network request, timer, tool execution, process operation, or independently changing environment instead produces an observation, an external effect, or both. Calling such work part of `select` would change the model without defining the added operations.

Exact resumption or operational equivalence requires the relevant operation, arguments, outcome or failure, causal position, and later-observable state changes to be explicit. Retry, duplication, ordering, and commit behavior must also be defined where they can change observations. An independently mutable environment must be mediated, checkpointed, or represented by recorded events under a stated replay rule. Merely naming it in `K_total` is not enough. A session log can replay recorded decisions without replaying the world those decisions affected.

These are necessary conditions, not a general sufficiency theorem. “Same effects” remains undefined until the relevant observer, emissions, failures, and final state are named.

## Mutable programs require a fixed interpreter

Active program and configuration state can be included in explicit state. It is useful to distinguish it as `Gamma_h` while defining:

`K_total = (K_run, Gamma_h, lifecycle/effect state)`.

A fixed meta-interpreter `U` interprets `Gamma_h`, advances `K_total`, and issues operations. Exact resumption requires the active executable artifacts, or immutable references to them, plus configuration, component and dependency composition, control position, migration state, and any in-flight operation that must still land. A generation label without stable artifacts is not complete state.

Each dispatched `C` and the generation that will interpret its result must remain fixed through its barrier. A change that can alter an in-flight call, reroute partial output, or expose effects before that barrier needs an event-driven extension rather than this batch loop.

Treating `Gamma_h` as data does not remove the fixed layer. If `U`, the host-language semantics, the call primitive, or the lifecycle/effect semantics also change, another fixed interpreter is required or the single-machine claim ends. “Everything is a plugin” does not eliminate that remainder.

## A control judgment is not control execution

An LLM may decide or recommend what should happen next without violating the form. Its plan or control token returns in `R`; a fixed symbolic transition records it in `K_total`; later symbolic code interprets and executes it.

That differs from progression retained inside a model-mediated conversation or opaque tool loop. [Externalizing state does not make hidden transition logic symbolic](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md). Such a loop may still have an LLM-call projection once its call boundaries and hidden state are exposed, but it does not satisfy the clean scheduler condition while the conversation owns transition-relevant state or continuation.

This distinction concerns architecture, not policy quality. A returned control token followed by deterministic dispatch is mechanically representable even when its scheduling policy is poor. A good model judgment does not turn hidden progression into symbolic execution.

## Cordis witnesses the additional machinery

The [Cordis formal model](../sources/a-programming-paradigm-for-spatiotemporal-composability.ingest.md) does not prove the call-site transformation. It is a mechanism-level witness for the extra semantics needed when the host machine itself changes. Cordis tracks a location only when the system can modify it exclusively and restore its prior state. An operation outside that mediated boundary is not tracked or recovered merely because the program can name it.

State-specific inverses, reactive coeffects, committed dependency views, guarded withdrawal, and recovery after an in-flight iteration show what explicit recovery, dependency, and lifecycle state can look like. The guarantees depend on correct inverses and, for whole-system results, independence, acyclic dependencies, bounded iterations, finite fibers, total provisions, and absence of failed fibers. The confluence result concerns quiescent state, not external emissions, and failures may diverge by schedule.

Cordis therefore witnesses additional machinery and its limits. It does not make arbitrary effects reversible, prove the select/call lemma or arbitrary mid-call replacement, or validate a self-evolving harness. Dynamic components remain interpreted by a fixed Cordis meta-machine; Cordis is not shown to replace that machine itself.

## Why the conversion is useful

The lemma permits sequential phases, parallel maps, barrier-separated pipelines, and nested loops to remain in their natural source form. They need not be implemented as one monolithic `select`; the claim is that they can be represented by the loop when its preconditions hold.

## Scope

- Independent fan-out, shared barriers, and explicit merges fit. Streaming interaction, staggered overlap without a common barrier, calls that observe one another's partial effects, and independently mutable external state do not fit directly. Serializing them would not preserve their concurrency semantics.
- The complete-`C` rule is a necessary analytic definition, not a provider-independent theorem. Equal `C` values do not guarantee equal stochastic results.
- Folding mutable code into `K_total` requires stable artifacts and a fixed interpreter. The sources provide no general migration proof for arbitrary changing code or a changing meta-interpreter.
- The construction does not decide whether an LLM-produced policy, scheduler, or harness change is beneficial.

## Known lineage

The construction uses standard programming-language machinery. Small-step operational semantics represents execution as transitions over machine configurations. Abstract-machine compilation reifies control state. CPS plus defunctionalization is the classic route from implicit control flow to explicit symbolic state. This note applies that move where the only distinguished non-symbolic steps are independent, barrier-delimited LLM-call batches.

## Open questions

- The [decomposition heuristics](./decomposition-heuristics-for-bounded-context-scheduling.md) might be expressible as transformations that increase call count while decreasing per-call complexity. The lemma certifies the transformed program only when explicit state, batch independence, and barrier order are preserved.
- Effectful or event-driven programs may admit another normal form, but this lemma does not supply it.

---

Relevant Notes:

- [orchestration model](./bounded-context-orchestration-model.md) — grounds: supplies the conditional loop and call-oriented invariants used by the lemma
- [decomposition heuristics](./decomposition-heuristics-for-bounded-context-scheduling.md) — extends: develops transformations between programs that retain the lemma's preconditions
- [LLM-mediated schedulers are a degraded variant of the clean model](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — contrasts: separates an explicit symbolic handoff from progression retained inside a model-mediated loop
- [Claude Code dynamic workflows](../agentic-systems/reviews/claude-code-dynamic-workflows.md) — evidenced-by: describes a shipped barrier-oriented workflow with symbolic host control
