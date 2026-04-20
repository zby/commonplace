---
description: Storing execution history and loading it into the next agent call are separate decisions; chat and framework-owned tool loops conflate them by making session history the default next context
type: kb/types/note.md
traits: [has-external-sources]
tags: [computational-model, tool-loop]
status: seedling
---

# Session history should not be the default next context

An execution boundary — any point where one LLM call ends and another begins — usually creates two different questions:

- What should be stored in persistent state
- What should actually be loaded into the next call

These are not the same decision. In the [bounded-context orchestration model](./bounded-context-orchestration-model.md), storing artifacts in the scheduler's state is cheap; loading them into a prompt is expensive. Storing a trace is fine — the mistake is letting a session runtime decide that stored history should automatically become the next call's context instead of letting a selection function choose what the next call should see.

The conflation arises one layer above the model itself. The orchestration model only requires calls whose outputs are written into persistent state — it does not require chat history or a tool loop. But when higher-level interfaces package those calls as chat sessions or framework-managed tool loops, session history becomes the path of least resistance for passing state forward.

## Where the problem actually appears

With raw SDK calls, there is no built-in transcript problem — though application code can recreate the same pattern by manually persisting and prepending the full message array between calls. The trouble begins when a higher-level interface changes the primitive:

- **Chat sessions** make message history the natural carrier of state
- **Framework-owned tool loops** make intermediate progression happen inside a hidden runtime
- **Continuing agent sessions** encourage "just keep talking to the same thing" instead of rebuilding the next context deliberately

The [tool loop index](./tool-loop-index.md) describes the framework-level packaging. The downstream consequence is that the packaging layer starts deciding what later calls inherit — and it defaults to "everything."

## Why chat sessions and tool loops default to trace-preserving state

[The chat-history model trades context efficiency for implementation simplicity](./the-chat-history-model-trades-context-efficiency-for-implementation-simplicity.md). Raw history is the easiest way to preserve maximum information when the caller does not yet know what matters: no premature compression, no lost false starts, no need to design a return schema upfront, immediate usefulness for UI and debugging.

This makes transcript inheritance a sensible **exploratory default**. Early in a design, when the real interface between stages is still unknown, preserving the trace minimizes the risk of throwing away the wrong thing.

## Why transcript inheritance breaks down

The same property that makes trace-preserving handoff safe early makes it expensive later: it preserves everything.

For any consumer under a context budget, that is usually the wrong trade:

- The caller receives more than it needs
- Local tactical debris survives beyond the stage where it mattered
- Downstream stages must re-interpret rather than consume a clean artifact
- Interfaces remain implicit, because "the return value" is a transcript rather than a declared object
- Context pollution compounds as traces from many steps accumulate

This is the return-value problem from the [scoping note](./llm-context-is-composed-without-scoping.md) in architectural form. In deliberate-loading orchestration, each call sees only a prompt assembled by a selection function over stored state, and the boundary is real. The discipline breaks when implementations package many steps as one continuing session, letting history inheritance replace selective loading.

## Execution-boundary compression is a recurring design move

Across these systems, the shared move is [compression at the execution boundary](./definitions/distillation.md):

- Sub-agents should expose only return values across frames, not internal conversations ([scoping note](./llm-context-is-composed-without-scoping.md))
- Ad hoc prompts let the caller construct a focused task frame in natural language, creating a clean handoff boundary where the sub-agent inherits nothing beyond what the caller explicitly passed ([ad-hoc prompts](./ad-hoc-prompts-extend-the-system-without-schema-changes.md))
- [Spacebot](./related-systems/spacebot.md), a concurrent agent framework built by the Spacedrive team, uses branches that return only a scrubbed conclusion
- [Slate](../sources/slate-moving-beyond-react-and-rlm.ingest.md), an agent orchestration system built by Random Labs, uses workers that return compressed episodes rather than full tactical traces

The execution boundary is the natural place to compress, but the deeper question is what the selection function should load from stored state into the next context. Compression at the boundary produces the artifact; the selection function decides whether and how much to load.

## Tension: compressed episodes are visible, but the rest of the policy is not

Slate is the main tension case. From the [public description](../sources/slate-moving-beyond-react-and-rlm.ingest.md), workers return **episodes** — compressed representations of what happened during a bounded action. These are not raw transcripts, so they fit the anti-transcript argument. But they are more trace-shaped than a narrow result like `yes/no` or `found X`.

What we cannot tell from public evidence is the policy around episodes: how much is later loaded into context, whether episodes are further summarized or projected before reuse, and whether full traces are kept elsewhere. The strongest claim is that Slate appears to prefer compressed handoff artifacts over raw transcript inheritance. Whether that compression boundary is the right one — or whether other runtime mechanisms recover what the blog post does not describe — remains unknown.

## The right split: storage vs next-context loading

The scheduler can afford to keep many artifact kinds in persistent state — judgments, extracted claims, scrubbed conclusions, compressed episodes, structured data, symbolic code, failure signals, and raw traces for audit. What matters is that the next call usually wants a much stricter projection.

"History" conflates at least three trace types with different loading profiles:

- **Conversation transcripts** — message-by-message exchanges mixing signal (clarifications, partial results) with noise (misframings, corrections, phatic turns). Worth storing for UI, audit, and replay — rarely the right material for the next prompt.
- **Tool/action traces** — sequences of external calls and their results. More structured; sometimes the trace *is* the deliverable. Worth storing for debugging and reproducibility — occasionally close enough to load directly.
- **Reasoning traces** — chain-of-thought, planning, deliberation. Reveals how the agent reasoned, not what it concluded. Worth storing for debugging and alignment research — almost never worth loading into the next call.

In practice, these types blend: a multi-step debugging session interleaves reasoning about a tool result with the next tool call. The loading heuristic applies to the dominant character of a trace segment, not to entire sessions.

The argument against loading traces as next-context is sharpest for reasoning traces, strong for conversation transcripts, and most nuanced for tool traces. All three may belong in persistent state. But they are rarely the right default material for the next prompt.

The key separation is not "store vs discard" but **"persist in stored state vs load into the next context."** In deliberate-loading orchestration, loading happens through a selection function over stored state, not by inheriting a session log. The next call should see a representation chosen for its task — including when the next decision is whether to retry, unwind, or escalate.

Failure handling makes the separation especially visible. A bounded execution may return a structured failure artifact while the raw trace is stored separately in persistent state. The runtime might interpret that failure artifact directly and choose a retry, unwind, or escalation path. Or it might make a separate LLM call to interpret the failure semantically. Either way, the existence of a trace does not imply that the trace should be loaded into the recovery prompt.

## Conversation vs refinement is one instance of the general problem

[Conversation vs prompt refinement in agent-to-agent coordination](./conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) is a local case of this broader protocol choice.

- **Conversation** preserves the trace: misunderstanding, clarification, correction, and intermediate work all remain in-band
- **Prompt refinement** compresses the trace into a new handoff artifact: the caller integrates what mattered and re-dispatches with a cleaner frame
- **Context cloning / forking** preserves a selected trace prefix for multiple children without continuing the same conversation indefinitely

The [conversation-vs-refinement note](./conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) studies when each choice is worth its cost. The more general point is that these are different answers to the same question: should session history be the unit that later calls inherit?

## The practical principle

For most orchestration:

- It is often fine to **store more than you load**
- Use **trace-preserving storage** early, when you do not yet know the right interface or what later learning may need
- Move toward **artifact-first loading** once the caller's real consumption pattern is understood
- "Artifact-first" does not mean "minimal"; a compressed episode that also serves memory and learning is still an artifact, not a transcript
- Keep the **raw trace as an auxiliary substrate** for UI, debugging, audit, or later learning unless a specific call truly needs it

The default mistake is to let a chat interface or framework-owned tool loop decide what the next call should inherit. Interactive sessions are optimized for continuity and visibility. Orchestration wants selective loading.

---

Relevant Notes:

- [llm-context-is-composed-without-scoping](./llm-context-is-composed-without-scoping.md) — foundation: frame boundaries only become real interfaces when the parent sees a return value rather than the internal conversation
- [bounded-context orchestration model](./bounded-context-orchestration-model.md) — foundation: the scheduler's state can store more artifacts than any one prompt should load; the real control point is the selection function
- [the chat-history model trades context efficiency for implementation simplicity](./the-chat-history-model-trades-context-efficiency-for-implementation-simplicity.md) — grounds: explains why transcript inheritance is attractive early and why it becomes costly as architectures mature
- [tool loop](./tool-loop-index.md) — foundation: the trace problem appears when calls are repackaged into framework-owned sessions that hide progression and make history inheritance the path of least resistance
- [conversation-vs-prompt-refinement-in-agent-to-agent-coordination](./conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) — special case: conversation preserves trace, prompt refinement compresses it into a cleaner handoff artifact
- [agent orchestration occupies a multi-dimensional design space](./agent-orchestration-occupies-a-multi-dimensional-design-space.md) — extends: return artifact is a design dimension, and this note argues traces should usually not be that artifact
- [codification and relaxing navigate the bitter lesson boundary](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — tension: compressed trace artifacts may preserve more reusable learning signal than narrow result artifacts, even when they are less minimal as interfaces
- [distillation](./definitions/distillation.md) — mechanism: execution-boundary compression is distillation targeted at the next stage's needs

Distilled into:

- [the chat-history model trades context efficiency for implementation simplicity](./the-chat-history-model-trades-context-efficiency-for-implementation-simplicity.md) — higher-level architectural tradeoff extracted from this mechanism-level note
