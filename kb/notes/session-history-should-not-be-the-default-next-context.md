---
description: Storing execution history and loading it into the next agent call are separate decisions; chat and framework-owned tool loops conflate them by making session history the default next context
type: kb/types/note.md
traits: [has-external-sources, title-as-claim]
tags: [computational-model, tool-loop]
status: seedling
---

# Session history should not be the default next context

An execution boundary — any point where one LLM call ends and another begins — creates two distinct decisions:

1. **What to persist** in external state
2. **What to load** into the next call's context

These are not the same decision. Persistence is cheap; context window space is expensive. In the [bounded-context orchestration model](./bounded-context-orchestration-model.md), the scheduler's state can store everything — but the prompt for the next call should be assembled by a deliberate selection step, not inherited from the last session. Storing a trace is fine — the mistake is letting stored history automatically become the next call's context.

## How the conflation arises

With raw SDK calls, there is no transcript problem. Application code assembles a prompt, calls the model, stores the result, and decides what to do next. The trouble begins when a higher-level interface changes the primitive:

- **Chat sessions** make message history the natural carrier of state
- **Framework-owned tool loops** make intermediate progression happen inside a hidden runtime
- **Continuing agent sessions** encourage "just keep talking to the same thing" instead of rebuilding the next context deliberately

The [tool loop index](./tool-loop-index.md) describes the framework-level packaging. The downstream consequence is that the packaging layer starts deciding what later calls inherit — and it defaults to "everything."

Why does it default this way? Because [raw history is the easiest way to preserve maximum information](./the-chat-history-model-trades-context-efficiency-for-implementation-simplicity.md) when the caller does not yet know what matters: no premature compression, no lost false starts, no need to design a return schema upfront, immediate usefulness for UI and debugging. This makes transcript inheritance a sensible **exploratory default** — early in a design, preserving the trace minimizes the risk of throwing away the wrong thing.

## Why transcript inheritance breaks down

The same property that makes trace-preserving handoff safe early makes it expensive later: it preserves everything. LLMs [degrade with context complexity](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) — every token spent parsing irrelevant history is cognitive budget not spent on the actual task:

- local tactical debris survives beyond the stage where it mattered
- the model must re-interpret prior interaction rather than consume a clean artifact
- interfaces remain implicit — "the return value" is a transcript rather than a declared object
- context pollution compounds as traces from many steps accumulate

In a [properly scoped system](./llm-context-is-composed-without-scoping.md), each sub-agent gets a clean frame and the caller sees only the return value, not the internal conversation. Transcript inheritance defeats that discipline — and it also conflates several trace types (conversation transcripts, tool/action logs, reasoning chains) that are each worth storing but rarely worth loading. The next call should see a representation chosen for its task, not the raw record of how the previous call got there.

## Execution-boundary compression is a recurring design move

Across several systems, the shared move is [compression at the execution boundary](./definitions/distillation.md):

- Sub-agents should expose only return values across frames, not internal conversations ([scoping note](./llm-context-is-composed-without-scoping.md))
- When the caller does judgment-heavy selection before dispatch, the callee need not inherit the caller's search trace ([ad-hoc prompts](./ad-hoc-prompts-extend-the-system-without-schema-changes.md))
- [Spacebot](../agent-memory-systems/reviews/spacebot.md) branches return only a scrubbed conclusion
- [Slate](https://randomlabs.ai/blog/slate) workers return compressed episodes rather than full tactical traces
- [Conversation vs. prompt refinement](./conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) is a local case: conversation preserves the trace in-band, refinement compresses it into a cleaner handoff artifact, and forking preserves a selected trace prefix for multiple children

Compression at the boundary produces the artifact; the selection step decides whether and how much of it to load into the next call. But the compression itself should be goal-oriented rather than uniform. A fixed strategy — "summarize what happened" — produces a general-purpose artifact that serves no consumer particularly well. Distillation targeted at a specific next stage can produce a much tighter result: a structured failure signal for a retry decision, a claim list for a synthesis step, a status line for a progress report. The same execution trace might warrant different compressions for different consumers.

## Tension: Slate's episodes sit between traces and artifacts

Random Labs' Slate is the main tension case. From the [public description](https://randomlabs.ai/blog/slate), workers return **episodes** — compressed representations of what happened during a bounded action. These are not raw transcripts, so they fit the anti-transcript argument. But they are more trace-shaped than a narrow result like `yes/no` or `found X`.

What we cannot tell from public evidence is the loading policy around episodes: how much is later loaded into context, whether episodes are further summarized before reuse, and whether full traces are kept elsewhere. Slate appears to prefer compressed handoff artifacts over raw transcript inheritance. Whether that compression boundary is the right one remains unknown.

## The practical principle

For most orchestration:

- **Store more than you load** — persistence is cheap, context is not
- Use **trace-preserving storage** early, when you do not yet know the right interface or what later learning may need
- Move toward **artifact-first loading** once the caller's real consumption pattern is understood
- "Artifact-first" does not mean "minimal" — a compressed episode that also serves memory and learning is still an artifact, not a transcript
- Keep the **raw trace as an auxiliary substrate** for UI, debugging, audit, or later learning unless a specific call truly needs it

Failure handling makes the separation especially visible. A bounded execution may return a structured failure artifact while the raw trace is stored separately. The runtime interprets the failure artifact to choose retry, unwind, or escalation — the existence of a trace does not imply that the trace should be loaded into the recovery prompt.

The default mistake is to let a chat interface or framework-owned tool loop decide what the next call should inherit. Interactive sessions want continuity and visibility. Orchestration wants selective loading.

---

Relevant Notes:

- [llm-context-is-composed-without-scoping](./llm-context-is-composed-without-scoping.md) — foundation: frame boundaries only become real interfaces when the parent sees a return value rather than the internal conversation
- [bounded-context orchestration model](./bounded-context-orchestration-model.md) — foundation: `K` can store more artifacts than any one prompt should load; the real control point is `select(K)`
- [the chat-history model trades context efficiency for implementation simplicity](./the-chat-history-model-trades-context-efficiency-for-implementation-simplicity.md) — grounds: explains why transcript inheritance is attractive early and why it becomes costly as architectures mature
- [tool loop](./tool-loop-index.md) — foundation: the trace problem appears when bounded calls are repackaged into framework-owned sessions that hide progression and make history inheritance the path of least resistance
- [conversation-vs-prompt-refinement-in-agent-to-agent-coordination](./conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) — special case: conversation preserves trace, prompt refinement compresses it into a cleaner handoff artifact
- [ad hoc prompts extend the system without schema changes](./ad-hoc-prompts-extend-the-system-without-schema-changes.md) — exemplifies: the caller does judgment-heavy selection before dispatch, creating a clean handoff boundary
- [distillation](./definitions/distillation.md) — mechanism: execution-boundary compression is distillation targeted at the next stage's needs
- [agent orchestration occupies a multi-dimensional design space](./agent-orchestration-occupies-a-multi-dimensional-design-space.md) — extends: return artifact is a design dimension, and this note argues traces should usually not be that artifact
- [codification and relaxing navigate the bitter lesson boundary](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — tension: compressed trace artifacts may preserve more reusable learning signal than narrow result artifacts, even when they are less minimal as interfaces
- [Spacebot](../agent-memory-systems/reviews/spacebot.md) — exemplifies: branches return scrubbed conclusions rather than full reasoning traces
- [Ingest: Slate: Moving Beyond ReAct and RLM](https://randomlabs.ai/blog/slate) — exemplifies: episodes are compressed return artifacts, not tactical transcripts

Distilled into:

- [the chat-history model trades context efficiency for implementation simplicity](./the-chat-history-model-trades-context-efficiency-for-implementation-simplicity.md) — higher-level architectural tradeoff extracted from this mechanism-level note
