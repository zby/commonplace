---
description: Compiling a coordination strategy into a workflow makes the steps a prompt drives by inference explicit; with no new side-effect channels it expands capacity but not the authority boundary
type: kb/types/note.md
traits: [title-as-claim]
tags: [computational-model, tool-loop]
status: seedling
---

# Compiling a coordination strategy expands capacity, not authority

A prompt that drives a multi-step task does its coordination through repeated inference: the model decides to call agent A, reads the result, decides to pass it to B, loops, and eventually returns. Each coordination step is paid for with a fresh inference pass, and the strategy that links them exists only as a pattern the model re-derives turn by turn. A workflow — in this case, a [Claude Code dynamic workflow](../agentic-systems/claude-code-dynamic-workflows.md) — is the **compiled** form of that same coordination: the call-A-then-B-then-loop logic is lifted out of repeated inference and written down as an explicit external artifact that a runtime executes directly.

The entry intuition is the compiler analogy. A prompt-driven run is interpretation — the coordination plan is recomputed by the model on every step. A workflow is compilation — the plan is fixed once in an artifact and then run. This is [codification](./definitions/codification.md) of a [`select`-strategy](./bounded-context-orchestration-model.md): the coordination logic crosses from prose the model reinterprets each turn into a symbolic artifact a runtime consumes.

## The capacity/authority split

The load-bearing claim is about what compilation does and does not move.

**Capacity expands.** A compiled artifact is more than a cached prompt execution. Being external and symbolic, it can store state across steps, exceed a single context window, coordinate many agents, and run far longer than any single inference. None of these are available to a strategy that lives only inside one model's turn-by-turn reasoning. The act of writing the strategy down buys a strictly larger computational envelope — this is the same persistence dividend the [host-language scheduler](./the-practical-scheduler-is-the-host-language.md) collects by letting code, not conversation, hold the run.

**Authority does not.** A workflow runs in a **restricted environment with no power to create new side-effect channels of its own.** The script coordinates; it cannot itself touch the filesystem, the shell, or the network. Every interaction with the outside world still flows through the same agents and tools the original prompt could already reach — the workflow can only sequence and combine those existing channels, never invent one. So the set of effects the system can produce is unchanged: anything the workflow can cause, the prompt could already have caused by driving the same agents by hand. Compilation rearranges *how* the authorized channels are invoked; it adds none.

The split is clean because the two properties have different sources. Capacity comes from the artifact being **external and persistent** — it escapes the single-context, single-turn envelope. Authority is fixed by the artifact being **sandboxed and channel-less** — every real-world effect is delegated to a pre-existing tool or agent. A restricted execution environment can grant the first while withholding the second, which is exactly why compiling a coordination strategy is safe to do automatically: it cannot widen the security boundary because it holds no side-effect channels to widen it with.

This is the same boundary the [different-tools forcing case](./subtasks-that-need-different-tools-force-loop-exposure-in-agent.md) draws between an action alphabet and bookkeeping. A workflow gets to compose calls and project state — bookkeeping over authorized channels — but the action alphabet of any actual effect is still set by the agents and tools it dispatches to. It selects from the authorized surface; it does not construct a new one.

## Why the analogy is imperfect — in the capacity direction only

Calling a workflow a "compiled prompt" undersells it on capacity. A cached execution would only replay what one inference did; a workflow is a genuinely more powerful object because persistence and externality give it state, scale, multi-agent coordination, and duration a single inference cannot have. So the analogy understates what compilation gains.

But the analogy is *exact* on authority, and that exactness is the point. Both the interpreted prompt and the compiled workflow reach the world only through the same delegated channels. The thing that grows is the coordination machinery; the thing that stays put is the set of side-effects the system is permitted to cause.

## General form

A workflow is a **compiled coordination strategy** — explicit, reusable, persistent. Compiling a coordination strategy into an external artifact expands the system's computational capacity (state, window, agent count, duration) while preserving its capacity/authority boundary, *provided* the compiled artifact runs in an environment that holds no side-effect channels and must delegate every effect through the channels the un-compiled strategy already had. The proviso is what makes the preservation hold: it is the restricted environment, not the act of compilation, that pins authority in place. Lift that restriction — let the artifact open its own files, shell, or sockets — and the guarantee is gone, because then the compiled form can reach the world by paths the prompt never could.

This reframes the [system-definition artifact](./system-definition-artifacts-are-crystallized-reasoning-under-context.md) view from the authority side. Crystallizing reasoning into an artifact addresses context scarcity; crystallizing a *coordination* strategy additionally buys execution capacity — but neither move, on its own, touches behavioral authority. Authority is a separate axis, governed by what channels the artifact can reach, not by whether the strategy is interpreted or compiled.

## Open Questions

- Does the guarantee degrade gracefully, or is it all-or-nothing? A workflow with a single non-delegated channel (say, a raw network primitive) seems to lose the whole property — is there a partial-authority middle ground worth modeling?
- The argument assumes the delegated agents enforce their own authority correctly. Compilation preserves the boundary *relative to* those agents; it says nothing about whether sequencing previously-isolated calls composes their individual authorities into an emergent one.

---

Relevant Notes:

- [Claude Code dynamic workflows](../agentic-systems/claude-code-dynamic-workflows.md) — derived-from: the shipped sandboxed-script-over-agents system whose "the script coordinates, agents act" division is the concrete case this claim abstracts
- [codification](./definitions/codification.md) — mechanism: compiling a coordination strategy into an external artifact is codification of a `select`-strategy — prose the model reinterprets becomes a symbolic artifact a runtime runs
- [bounded-context orchestration model](./bounded-context-orchestration-model.md) — grounds: the `select`/`call` decomposition; the coordination being compiled is the `select` logic
- [the practical scheduler is the host language](./the-practical-scheduler-is-the-host-language.md) — extends: the capacity dividend (state, window, duration) this note attributes to externalisation is the same one host-language code collects by holding the run
- [orchestration strategies and run-state have opposite persistence economics](./orchestration-strategies-and-run-state-have-opposite-persistence.md) — extends: the compiled coordination strategy is exactly the recurring `select`-fragment that note marks as the high-value promotion target
- [system-definition artifacts are crystallized reasoning under context scarcity](./system-definition-artifacts-are-crystallized-reasoning-under-context.md) — extends: crystallizing reasoning fixes the operative part at write-time; this note adds that crystallizing coordination also buys capacity while still leaving authority on a separate axis
- [subtasks that need different tools force loop exposure in agent frameworks](./subtasks-that-need-different-tools-force-loop-exposure-in-agent.md) — mechanism: the action-alphabet vs bookkeeping boundary; a workflow composes over authorized channels but never constructs a new action alphabet
