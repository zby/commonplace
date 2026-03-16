---
description: When framework-owned tool loops recover from broken tools via agent workarounds, final success stops being a reliable signal that the underlying scripts and workflows are healthy
type: note
traits: []
tags: [computational-model, kb-maintenance, learning-theory, observability]
status: seedling
---

# Apparent success is an unreliable health signal in framework-owned tool loops

In a framework-owned tool loop, a task can end in visible success even when part of the intended execution path failed. If the agent recovers by improvising a workaround, the user still gets a useful artifact — but that outcome is no longer good evidence that the underlying scripts, paths, credentials, and helper workflows are healthy. Success at the artifact layer and success at the infrastructure layer have come apart.

## Why the health signal degrades

The standard tool loop merges three different outcomes into one visible state:

1. **Primary-path success** — the prescribed tool path ran as intended.
2. **Fallback success** — the primary path failed, but the agent found another way.
3. **Hard failure** — neither the primary path nor fallback worked.

Frameworks typically compress the first two into "success." A snapshot skill whose X fetch script fails because of a bad path can still produce something by browsing the page directly. The user sees completion, but the system no longer knows from the final outcome whether the prescribed path worked, whether provenance changed, or whether fidelity dropped.

Programmers trained on traditional systems are particularly vulnerable to this. As [traditional debugging intuitions break when tool loops can recover semantically](./traditional-debugging-intuitions-break-when-tool-loops-can-recover-semantically.md) develops: in traditional software, broken infrastructure usually fails loudly enough that success remains a rough proxy for mechanism health. Semantic recovery weakens that proxy without making the change obvious.

## Why framework-owned loops encourage this

A framework-owned tool loop is optimized for task completion inside one conversational runtime. Tool errors are not terminal events; they are just more context for the next model turn. That makes recovery cheap:

- the error message is already in the loop
- the model is already tasked with "keep going"
- the framework usually prefers not to interrupt the user if progress is still possible

This is one reason [LLM frameworks should expose the loop](./llm-frameworks-should-expose-the-loop.md). When orchestration is hidden, failure handling is hidden with it. The application cannot easily separate "the user got an acceptable result" from "the intended execution path succeeded." The framework has implicitly made that policy decision on the user's behalf.

## Practical consequences for commonplace

The real requirement is **observability**, not necessarily inline interruption. If Claude Code or Codex can route around a broken helper, missing binary, or bad relative path, the defect persists until someone inspects logs. There are two ways to recover the missing signal:

- **Synchronous reporting** — the run tells the user it succeeded through a degraded path. Appropriate when fallback changes guarantees the user is relying on directly.
- **Asynchronous observation** — a later process scans logs and surfaces hidden failures for maintenance. Often sufficient when the goal is infrastructure repair rather than immediate user awareness.

Without either, the system trains us to trust outcomes while the infrastructure underneath drifts.

## Theoretical placement

The [agent runtime decomposition](./agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md) places the phenomenon at the boundary between scheduler and execution substrate. The scheduler asks for a capability; the substrate attempts the tool call; the runtime decides whether the error is terminal or recoverable.

Current frameworks often encode only that binary. What is missing is a first-class notion of **degraded execution**: a run that reached an acceptable output through a path with weaker guarantees than the intended one.

This does not modify the [bounded-context orchestration model](./bounded-context-orchestration-model.md) — the clean model abstracts over how a bounded call is realised. The issue is one layer down, in execution substrate policy.

It also sharpens [enforcement without structured recovery is incomplete](./enforcement-without-structured-recovery-is-incomplete.md): recovery strategy is only half the problem. The other half is observability. A fallback chain invisible to both user and operator increases short-term convenience at the cost of long-term drift, because it lowers the chance the underlying defect is ever repaired.

## Open Questions

- Which classes of tool failure require synchronous user-visible degraded-execution reporting, and which can be handled by asynchronous log observation?
- Is `AGENTS.md` the right place to encode reporting norms, or should that contract live in framework/runtime policy so skills do not each reinvent it?
- What is the right maintenance artifact here: a periodic log-sweep instruction, a script that extracts tool-call failures from Claude/Codex logs, or both?
- How should test strategy split between instruction tests that mock the tool boundary and integration checks that catch path, environment, and credential failures the mocks will miss?

---

Relevant Notes:

- [bounded-context orchestration model](./bounded-context-orchestration-model.md) — boundary: the clean scheduler model survives; this note targets what final success can and cannot tell you about runtime health
- [LLM frameworks should expose the loop](./llm-frameworks-should-expose-the-loop.md) — extends: hidden orchestration also hides the distinction between acceptable result and healthy execution path
- [traditional debugging intuitions break when tool loops can recover semantically](./traditional-debugging-intuitions-break-when-tool-loops-can-recover-semantically.md) — consequence: explains why programmers systematically over-trust successful outcomes in this regime
- [LLM-mediated schedulers are a degraded variant of the clean model](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — refines: degradation is not only context-bounded scheduling but also loss of observability about how the run succeeded
- [agent runtimes decompose into scheduler context engine and execution substrate](./agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md) — locates: the weakened health signal appears at the boundary between scheduler intent and substrate behavior
- [enforcement without structured recovery is incomplete](./enforcement-without-structured-recovery-is-incomplete.md) — complements: corrective/fallback/escalation needs an observability layer so recovery does not erase evidence of the original failure
- [unit testing LLM instructions requires mocking the tool boundary](./unit-testing-llm-instructions-requires-mocking-the-tool-boundary.md) — limits: mocked tool tests catch instruction regressions but not broken paths, missing binaries, or credential failures in the real runtime
