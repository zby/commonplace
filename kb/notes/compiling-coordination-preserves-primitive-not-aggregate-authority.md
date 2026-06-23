---
description: Compiling a coordination strategy preserves the primitive action alphabet but expands aggregate authority — the single-context envelope it escapes bounded both compute and effect volume
type: kb/types/note.md
traits: [title-as-claim]
tags: [computational-model, tool-loop]
status: seedling
---

# Compiling a coordination strategy preserves primitive authority but expands aggregate authority

A prompt that drives a multi-step task does its coordination through repeated inference: the model selects agent A, reads the result, selects B as the next step, loops, and eventually returns. Each coordination step is paid for with a fresh inference pass, and the strategy that links them is inferred again at each turn. In the Claude Code case, the workflow is a [dynamic workflow](../agentic-systems/claude-code-dynamic-workflows.md), a sandboxed script-over-agents system. It is the **compiled** form of the same coordination: the call-A-then-B-then-loop logic is lifted out of repeated inference and written as an explicit external artifact that a runtime executes directly.

The entry intuition is the compiler analogy. A prompt-driven run is interpretation — the coordination plan is recomputed on every step. A workflow is compilation — the plan is fixed once in an artifact and then run. This is [codification](./definitions/codification.md) of the strategy for choosing the next agent or tool call in a [bounded-context orchestration model](./bounded-context-orchestration-model.md), a view of orchestration as repeated choices about the next context-limited agent or tool call: the coordination logic crosses from prose that each turn asks the model to infer into a symbolic artifact a runtime consumes.

## What compilation preserves, and what it does not

The load-bearing distinction is between two things "authority" can mean, which the compiler move splits apart.

**The primitive action alphabet is preserved.** The script can compute, branch, loop, and coordinate, but it cannot itself touch the filesystem, the shell, the network, or external services. Every effectful operation must be delegated through agents and tools that the original prompt could already call. So the compiled form adds no new *primitive effect channel*: the set of operations that can touch the world is exactly the set the un-compiled strategy already had. This is the genuine guarantee, and it follows from the artifact being **sandboxed and channel-less** — every real-world effect is delegated to a pre-existing tool or agent. This is the same boundary the [different-tools forcing case](./subtasks-that-need-different-tools-force-loop-exposure-in-agent.md) draws between an action alphabet — the authorized set of effectful operations agents and tools can perform — and bookkeeping. A workflow gets to compose calls and project state; the alphabet of any actual effect is still set by the agents and tools it dispatches to. It selects from the authorized surface; it does not construct a new action primitive.

**Aggregate authority is not preserved — it expands, on the same axis as capacity.** It is tempting to say compilation expands *capacity* (state, context window, agent count, duration) while leaving *authority* untouched, treating them as orthogonal axes with different sources. That separation does not hold. A single inference turn / single context window was bounding two things at once: how much the coordinator could **compute** and how many effectful calls it could **emit** before the turn ended. The context envelope was a security control as much as a compute limit. Compilation's entire value proposition is escaping that envelope — and every capacity gain it lists is also a magnitude-of-harm dimension:

- store state across steps and run long → sustained, low-and-slow effect sequences
- exceed a single context window → exfiltration volume the turn could not stage
- coordinate many agents (a documented 1,000-agent cap) → effect at machine scale
- run far longer than any single inference → dwell time and rate-based-detection evasion

"Delete one file when asked" and "delete files in a loop until the tree is empty" are the same primitive and wildly different authorities. A delegated channel governed by a permission model is almost always governed *per call*, not *per aggregate* — so the per-call gate that authorizes each delegated effect does nothing to bound their sum. The only thing that bounded the sum was the context envelope, and compilation removes it. So capacity and aggregate authority are not two axes; they are one axis, freed together. This is the same persistence dividend the [host-language scheduler](./the-practical-scheduler-is-the-host-language.md) collects — except that the dividend is paid in reachable effect, not only in reachable compute.

## Where a preservation claim still holds

A preservation result survives, but a narrower one. Authority in the sense that matters to security is the *practically reachable set of world effects*, and by that measure the compiled form reaches combinations and volumes the prompt never practically could — that is exactly what the capacity gains above amount to. So "channels the un-compiled strategy already had" is true only as a claim about the primitive alphabet, not about reachable effect.

The aggregate boundary is preserved only for a specific channel class: **non-composable, per-call-saturating channels** — those whose own per-call authorization already bounds their aggregate use (a delegate that rate-limits itself, enforces a quota, or is idempotent). For those, looping buys nothing. For everything else, compilation expands what the system can cause. The documented dynamic-workflows case is *not* in that class: delegates carry inherited session allowlists and per-call permission only, with no aggregate policy. The direct guarantee there is narrower than a whole-system safety claim: the script has no direct filesystem, shell, or network APIs, and delegated agents bring their own enforcement — but that enforcement is per-call, so the aggregate is exactly what stays unbounded.

## Why the compiler analogy leaks on both axes

Calling a workflow a "compiled prompt" undersells it on capacity: a cached execution would only replay what one inference did, whereas persistence and externality give the workflow state, scale, multi-agent coordination, and duration a single inference cannot have. So the analogy understates what compilation gains.

The analogy is not *exact* on authority either. Real optimizing compilers change effective authority routinely — dead-store elimination removing a `memset` that zeroed a secret is a shipped security regression; reordering and vectorization produce machine-level effect sequences the source never expressed. "Compilation preserves semantics" fails precisely at the edges that matter for security. What compilation preserves here is the *primitive alphabet*; what it changes — like a real compiler — is the effect sequence the alphabet can be driven through.

## General form

A workflow is a **compiled coordination strategy** — explicit, reusable, persistent. Compiling a coordination strategy into an external artifact preserves the primitive action alphabet: it adds no new effect channel and must delegate every effect through channels the un-compiled strategy already had. But it expands two things that turn out to be one — computational capacity and aggregate authority — because the single-context envelope it escapes was bounding both the compute and the effect-volume of a run. Authority in the primitive sense (what *kinds* of effect are reachable) is pinned by the sandbox; authority in the aggregate sense (what *magnitude* of effect is reachable) moves with capacity. The clean preservation result holds only for delegated channels whose per-call authorization already bounds their aggregate use; lift the sandbox entirely and even the primitive alphabet is gone.

This reframes the [system-definition artifact](./system-definition-artifacts-are-crystallized-reasoning-under-context.md) view — artifacts the system consumes as binding instruction, configuration, or routing — from the authority side. Crystallizing reasoning into an artifact addresses context scarcity; crystallizing a *coordination* strategy additionally buys execution capacity — but that capacity is not authority-neutral. It pins the primitive alphabet while moving aggregate authority, because the same persistence that buys compute also buys effect-volume.

## Open Questions

- Sequencing previously isolated calls is sometimes posed as *composing* individual authorities into an emergent one (read-secret then network-post = exfiltration). In this system the coordinator already bridges isolated agents — it reads one result and passes it to the next across turns — so the trajectory was already reachable in interpreted form; compilation makes it cheaper and repeatable, which is the aggregate-scale point above, not a separate composition primitive. Is there a system where inter-agent isolation *is* the boundary, so composition manufactures genuinely new primitive authority?
- Can the per-call-saturating channel class be characterized precisely enough to validate it — i.e. given a delegate, decide whether looping it expands reachable effect? That is what a real preservation theorem would need.
- The script is not strictly side-effect-free even before delegation: it spends a shared token `budget`, schedules concurrent agents to a hard cap, and journals results — observable resource effects (denial-of-wallet, resource exhaustion) that are themselves a form of aggregate authority. How should these be folded into the boundary model?

---

Relevant Notes:

- [Claude Code dynamic workflows](../agentic-systems/claude-code-dynamic-workflows.md) — derived-from: the shipped sandboxed-script-over-agents system whose "the script coordinates, agents act" division is the concrete case this claim abstracts
- [bounded-context orchestration model](./bounded-context-orchestration-model.md) — grounds: the choose-next-step / perform-call decomposition; the coordination being compiled is the choose-next-step logic
- [orchestration strategies and run-state have opposite persistence economics](./orchestration-strategies-and-run-state-have-opposite-persistence.md) — extends: the compiled coordination strategy is exactly the recurring choose-next-step fragment that note marks as the high-value promotion target
- [system-definition artifacts are crystallized reasoning under context scarcity](./system-definition-artifacts-are-crystallized-reasoning-under-context.md) — extends: takes write-time crystallization as the base case and adds coordination capacity while keeping the primitive action alphabet on a separate axis from aggregate effect
