---
description: When intended-path success and fallback success produce the same final task outcome, the outcome cannot establish whether the intended path and its supporting infrastructure were healthy
type: kb/types/note.md
traits: [title-as-claim]
tags: [computational-model, kb-maintenance, learning-theory, observability, tool-loop, deploy-time-learning]
---

# Final task success does not establish intended-path health

When a tool loop can produce the same successful task outcome through either the intended path or a synthesized fallback, that outcome alone cannot establish whether the intended path was healthy. The user may receive an acceptable artifact even though a script, path, credential, or helper workflow failed. Artifact success and infrastructure health are separate facts.

A **framework-owned tool loop** is a framework-managed cycle in which a model issues tool calls, receives results or errors, and decides how to continue. Framework ownership is not necessary for the inference above, but it makes this situation easy to create: the framework can recover inside the loop before the application receives a terminal result.

## What final success leaves unresolved

A tool loop can end in three relevant states:

1. **Primary-path success** — the prescribed tool path ran as intended.
2. **Fallback success** — the primary path failed, but the agent found another way.
3. **Hard failure** — neither the primary path nor fallback worked.

If the runtime exposes the first two only as “success,” the final state does not record which path ran. For example, a platform-fetch helper can fail because of a bad path while the agent retrieves the page another way. The artifact may still be useful, but the final outcome alone reveals neither that failure nor whether provenance or fidelity changed.

Fixed recovery logic selects among paths implemented in advance. A semantic loop can instead synthesize a fallback by reasoning over the task context. This enlarges the fallback space and makes the path taken harder to infer from terminal status. In either case, however, logs or events can preserve the failed attempt; synthesized recovery does not itself erase the signal.

The deduction is therefore conditional. When primary-path and fallback success have the same observable terminal state and no independent execution signal is available, that state cannot identify intended-path health. How often this condition occurs, and how much it reduces predictive reliability in a particular runtime population, remain empirical questions.

## Record path deviation separately from guarantee degradation

Two signals are needed because two different facts can change:

- **Path deviation** records that the prescribed path failed or was bypassed, even if another path produced an acceptable result.
- **Guarantee degradation** records that the actual path weakened a named assurance such as provenance, freshness, completeness, authorization, or reproducibility.

An equivalent fallback can preserve every user-facing guarantee while still revealing a broken helper that needs repair. Conversely, a fallback that changes a guarantee needs a stronger status. Reserve **degraded execution** for that second case: a run that reached an acceptable output through a path with weaker guarantees than the intended path.

A run-level degraded status is one projection over durable tool-attempt events, not a substitute for them. The events support asynchronous detection of primary-path failures; comparing the guarantees of the intended and actual paths supports degraded-execution classification.

## Why framework-owned loops encourage the condition

A framework-owned loop is designed to continue task work inside one conversational runtime. Recovery is cheap when:

- The error message is already in the loop.
- The model is already pursuing the task goal.
- The runtime permits another tool choice instead of treating the error as terminal.

Together, these properties make fallback success possible. The failure is hidden only when the framework's application-facing interface exposes the terminal outcome without the corresponding path event. Visible orchestration is one way to preserve that distinction, but structured telemetry can preserve it without exposing the whole control flow.

## Placement in the runtime model

The [agent runtime decomposition](./agent-runtime-analysis-should-separate-scheduling-context-state.md) places the phenomenon at the scheduler–execution-substrate boundary. The scheduler requests a capability, the substrate attempts the tool call, and runtime policy decides whether an error is terminal or recoverable. Path-deviation events and guarantee classification belong to that execution policy. They do not change the higher-level orchestration model, which can abstract over how one scoped invocation is realized.

## Practical consequences for Commonplace

For Commonplace, an agent-operated knowledge-base framework, the operational requirement is observability rather than automatic interruption. Coding-agent runtimes such as Claude Code or Codex may route around a broken helper, a missing binary, a bad relative path, or a credential failure. The failed attempt along the prescribed path should remain observable even when the task completes.

- **Synchronous reporting** tells the user that the run succeeded through a path with weaker guarantees. Use it when the changed guarantee matters to the current result.
- **Asynchronous observation** scans durable events and surfaces primary-path failures for maintenance. It can be sufficient when an equivalent fallback preserved the result's guarantees.

Without either signal, successful runs can leave broken infrastructure unrepaired.

## Open Questions

- What guarantee-comparison contract is precise enough to classify degraded execution without flagging equivalent fallbacks?
- Which failure classes need synchronous user-visible status, and which can be handled by asynchronous maintenance alerts?

---

Relevant Notes:

- [A checked outcome licenses retaining an episode, not abstracting its explanation](./checked-outcome-licenses-episode-retention-not-abstraction.md) — grounds: an accepted result does not identify the process that produced it
- [A goal-holding interpreter fails soft, and its workarounds tax a bounded budget](./a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget.md) — mechanism: explains how goal-preserving rerouting consumes a failure and allows workarounds to accumulate
- [Diagnostic richness constrains outer-loop learning quality](./diagnostic-richness-constrains-outer-loop-learning-quality.md) — extends: shows why preserving path evidence improves later causal repair
- [silent disambiguation is the semantic analogue of tool fallback](./silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) — extends: the same observability failure appears when the runtime repairs ambiguity in the spec rather than failure in the tool path
- [enforcement without structured recovery is incomplete](./enforcement-without-structured-recovery-is-incomplete.md) — extends: recovery policy also needs an observability path so fallback does not erase maintenance evidence
- [Ingest: The Self-Healing Agent Harness](../sources/the-self-healing-agent-harness-2048912026018484317.ingest.md) — evidenced-by: independently separates final outcome grading from trajectory monitoring for infrastructure health
