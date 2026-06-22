---
description: Compiling a coordination strategy into a workflow makes the steps a prompt drives by inference explicit; with no new side-effect channels it expands capacity but not the authority boundary
type: kb/types/note.md
traits: [title-as-claim]
tags: [computational-model, tool-loop]
status: seedling
---

# Compiling a coordination strategy expands capacity, not authority

A prompt that drives a multi-step task does its coordination through repeated inference: the model selects agent A, reads the result, selects B as the next step, loops, and eventually returns. Each coordination step is paid for with a fresh inference pass, and the strategy that links them is inferred again at each turn. A workflow — in this case, a [Claude Code dynamic workflow](../agentic-systems/claude-code-dynamic-workflows.md), a sandboxed script-over-agents workflow system — is the **compiled** form of that same coordination: the call-A-then-B-then-loop logic is lifted out of repeated inference and written down as an explicit external artifact that a runtime executes directly.

The entry intuition is the compiler analogy. A prompt-driven run is interpretation — the coordination plan is recomputed on every step. A workflow is compilation — the plan is fixed once in an artifact and then run. This is [codification](./definitions/codification.md) of the strategy for choosing the next agent or tool call in a [bounded-context orchestration model](./bounded-context-orchestration-model.md): the coordination logic crosses from prose that each turn asks the model to infer into a symbolic artifact a runtime consumes.

## The side-effect-free execution boundary

The load-bearing claim is about what compilation does and does not move.

**Authority does not expand because the workflow runs side-effect-free.** The script can compute, branch, loop, and coordinate, but it cannot itself touch the filesystem, the shell, the network, or external services. Every effectful operation must be delegated through agents and tools that the original prompt could already call. So the workflow preserves authority relative to those delegated channels: both the prompt-driven coordinator and the compiled workflow reach the world only through mediated effect channels governed by the surrounding security model.

The direct guarantee in the Claude Code dynamic-workflow case is narrower than a whole-system safety claim. The workflow source establishes that the script has no direct filesystem, shell, or network APIs; delegated agents still bring their own inherited allowlists and permission behavior. The security argument is therefore relative to those agents: compilation removes some practical coordination limits while adding no separate side-effect path outside the delegated channels.

**Capacity expands anyway.** A compiled artifact is more than a cached prompt execution. Being external and symbolic, it can store state across steps, exceed a single context window, coordinate many agents, and run far longer than any single inference. None of these are available to a strategy that lives only inside one model's turn-by-turn reasoning. The act of writing the strategy down buys a strictly larger computational envelope — this is the same persistence dividend the [host-language scheduler](./the-practical-scheduler-is-the-host-language.md) collects by letting code, not conversation, hold the run.

The two properties therefore have different sources. Capacity comes from the artifact being **external and persistent** — it escapes the single-context, single-turn envelope. Authority is fixed by the artifact being **sandboxed and channel-less** — every real-world effect is delegated to a pre-existing tool or agent. A restricted execution environment can grant the first while withholding the second. That is why compiling a coordination strategy can be safe to do automatically: it does not widen the security boundary because it holds no side-effect channels to widen it with.

This is the same boundary the [different-tools forcing case](./subtasks-that-need-different-tools-force-loop-exposure-in-agent.md) draws between an action alphabet and bookkeeping. A workflow gets to compose calls and project state — bookkeeping over authorized channels — but the action alphabet of any actual effect is still set by the agents and tools it dispatches to. It selects from the authorized surface; it does not construct a new action primitive.

## Why the analogy is imperfect — in the capacity direction only

Calling a workflow a "compiled prompt" undersells it on capacity. A cached execution would only replay what one inference did; a workflow is a genuinely more powerful object because persistence and externality give it state, scale, multi-agent coordination, and duration a single inference cannot have. So the analogy understates what compilation gains.

But the analogy is *exact* on authority, and that exactness is the point. Both the interpreted prompt and the compiled workflow reach the world only through the same delegated channels. The thing that grows is the coordination machinery; the thing that stays put is the set of side-effects the system is permitted to cause.

## General form

A workflow is a **compiled coordination strategy** — explicit, reusable, persistent. Compiling a coordination strategy into an external artifact expands the system's computational capacity: state, window, agent count, and duration. It preserves authority only when the compiled artifact runs in a side-effect-free environment and must delegate every effect through channels the un-compiled strategy already had. The proviso is what makes the preservation hold: it is the restricted execution environment, not the act of compilation, that pins authority in place. Lift that restriction — let the artifact open its own files, shell, or sockets — and the guarantee is gone, because then the compiled form can reach the world by paths the prompt never could.

This reframes the [system-definition artifact](./system-definition-artifacts-are-crystallized-reasoning-under-context.md) view — artifacts the system consumes as binding instruction, configuration, or routing — from the authority side. Crystallizing reasoning into an artifact addresses context scarcity; crystallizing a *coordination* strategy additionally buys execution capacity — but neither move, on its own, touches behavioral authority. Authority is a separate axis, governed by what channels the artifact can reach, not by whether the strategy is interpreted or compiled.

## Open Questions

- Does the guarantee degrade gracefully, or is it all-or-nothing? A workflow with a single non-delegated side-effect channel (say, a raw network primitive) seems to lose the whole property — is there a partial-authority middle ground worth modeling?
- How should the preservation claim account for delegated agents' own enforcement? Compilation preserves the boundary *relative to* those agents, so a bad inherited allowlist or permission model remains bad after compilation.
- Can sequencing previously isolated calls compose their individual authorities into an emergent one? The side-effect-free script adds no primitive action, but it may make combinations easier to express and repeat.

---

Relevant Notes:

- [Claude Code dynamic workflows](../agentic-systems/claude-code-dynamic-workflows.md) — derived-from: the shipped sandboxed-script-over-agents system whose "the script coordinates, agents act" division is the concrete case this claim abstracts
- [bounded-context orchestration model](./bounded-context-orchestration-model.md) — grounds: the choose-next-step / perform-call decomposition; the coordination being compiled is the choose-next-step logic
- [orchestration strategies and run-state have opposite persistence economics](./orchestration-strategies-and-run-state-have-opposite-persistence.md) — extends: the compiled coordination strategy is exactly the recurring choose-next-step fragment that note marks as the high-value promotion target
- [system-definition artifacts are crystallized reasoning under context scarcity](./system-definition-artifacts-are-crystallized-reasoning-under-context.md) — extends: crystallizing reasoning fixes the operative part at write-time; this note adds that crystallizing coordination also buys capacity while still leaving authority on a separate axis
