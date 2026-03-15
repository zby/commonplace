---
description: Storing execution history and loading it into the next agent call are separate decisions; chat creates the expectation that history is state, and frameworks harden that expectation by automatically carrying session history forward as next context
type: note
traits: [has-external-sources]
tags: [computational-model]
status: seedling
---

# Session history should not be the default next context

The [bounded-context orchestration model](./bounded-context-orchestration-model.md) does **not** require chat history or a tool loop. It only requires bounded calls whose outputs are written into external symbolic state. The trace problem arises one layer up, when systems package those bounded calls as chat sessions or framework-managed tool loops and then treat the resulting history as the natural state to carry forward. That is useful for interactive UX, but it is the wrong default substrate for most agent orchestration.

An execution boundary usually creates two different questions:

- what should be stored in external symbolic state
- what should actually be loaded into the next bounded call

These are not the same decision. In the [bounded-context orchestration model](./bounded-context-orchestration-model.md), storage in `K` is cheap; bounded context is expensive. The mistake is not necessarily storing a trace. The mistake is letting a session runtime decide that stored history should automatically become the next call's context instead of letting `select(K)` choose what the next call should see.

## Where the problem actually appears

With raw SDK calls, there is no built-in transcript problem. Application code assembles a prompt `P`, calls the model, stores the result in `K`, and decides what to do next. The trouble begins when a higher-level interface changes the primitive:

- **chat sessions** make message history the natural carrier of state
- **framework-owned tool loops** make intermediate progression happen inside a hidden runtime
- **continuing agent sessions** encourage "just keep talking to the same thing" instead of rebuilding the next bounded context deliberately

This is the framework-level issue described in [llm frameworks should expose the loop](./llm-frameworks-should-expose-the-loop.md). This note is about what goes wrong once that packaging layer starts deciding what later calls inherit.

## Why chat sessions and tool loops default to trace-preserving state

Raw history is the easiest way to preserve maximum information. If the caller does not yet know what matters, carrying the whole interaction forward is the safest first move:

- no premature compression
- no lost false starts or clarifications
- no need to design a return schema upfront
- immediate usefulness for UI, audit, and debugging

This makes transcript inheritance a sensible **exploratory default** inside chat-shaped systems. Early in a design, when the real interface between stages is still unknown, preserving the trace minimizes the risk of throwing away the wrong thing.

## Why transcript inheritance breaks down

The same property that makes trace-preserving handoff safe early makes it expensive later: it preserves everything.

For orchestration, that is usually the wrong trade:

- the caller receives more than it needs
- local tactical debris survives beyond the stage where it mattered
- downstream stages must re-interpret rather than consume a clean artifact
- interfaces remain implicit, because "the return value" is a transcript rather than a declared object
- context pollution compounds as traces from many steps accumulate

This is the return-value problem from the [scoping note](./llm-context-is-composed-without-scoping.md) in architectural form. In clean bounded orchestration, each call sees only the prompt assembled by `select(K)`, and the boundary is real. The discipline breaks when implementations package many bounded steps as one continuing session, letting history inheritance replace selective loading.

## The right split: storage vs next-context loading

The scheduler can afford to keep many artifact kinds in external symbolic state:

- a yes/no judgment
- extracted claims
- a scrubbed conclusion
- a compressed episode
- structured data
- symbolic code
- a structured failure or restart signal
- and, when useful, raw traces for audit or later analysis

What matters is that the next bounded call usually wants a much stricter projection. "History" conflates at least three trace types with different storage and loading profiles:

- **Conversation transcripts** — message-by-message exchanges that mix signal (clarifications, partial results) with noise (misframings, corrections, phatic turns). Worth storing for UI, audit, and onboarding replay — but rarely the right material for the next prompt.
- **Tool/action traces** — sequences of external calls and their results. More structured, and sometimes the trace *is* the deliverable. Worth storing for debugging, telemetry, and reproducibility — and occasionally close enough to serve as the loaded artifact itself.
- **Reasoning traces** — chain-of-thought, planning, deliberation. Reveals how the agent thought, not what it concluded. Worth storing for debugging, alignment research, and learning — but almost never worth loading into the next call.

The argument against loading traces as next-context is sharpest for reasoning traces, strong for conversation transcripts, and most nuanced for tool traces. All three may belong in external state. But they are rarely the right default material for the next prompt.

The key separation is not "store vs discard" but **"persist in symbolic state vs load into bounded context."** In the clean model, loading happens through `select(K)`, not by inheriting a session log. The next bounded call should see a representation chosen for its task — including when the next decision is whether to retry, unwind, or escalate.

Failure handling makes the separation especially visible. A bounded execution may return a structured failure artifact while the raw trace is stored separately in symbolic state. The runtime might interpret that failure artifact directly and choose a retry, unwind, or escalation path. Or it might make a separate bounded LLM call to interpret the failure semantically. Either way, the existence of a trace does not imply that the trace should be loaded into the recovery prompt.

## Tension: compressed episodes are visible, but the rest of the policy is not

Slate is the main tension case for this note. From the public blog post, we can tell that its workers do not return the full tactical trace; they return an **episode** — a compressed representation of what happened during the bounded action. That episode is still not the raw transcript, so it fits the anti-transcript argument above. But it is more trace-shaped than a narrow result such as `yes/no` or `found X`.

What we cannot tell from the public description is the rest of the policy around that artifact:

- how much of an episode is later loaded into bounded context
- whether episodes are further summarized, indexed, or selectively projected before reuse
- whether full traces are still kept elsewhere in symbolic state
- whether the compression discards information that later turns out to matter

So the strongest claim this note can make is narrow: Slate appears to prefer compressed handoff artifacts over raw transcript inheritance. That may be a good orchestration interface. It may also be a lossy projection that works only because other parts of the runtime recover what the blog post does not describe. From the public post alone, we cannot know.

The architectural tradeoff remains real. A minimal return artifact keeps the immediate interface clean but may leave later stages with too little reusable detail. A compressed episode preserves more of what happened without forcing the full transcript into the next bounded call. But this note should not treat that as proof that Slate's compression boundary is the right one; it is only a visible design choice from limited public evidence.

## Execution-boundary compression is a recurring design move

Across these systems, the shared move is [compression at the execution boundary](./distillation.md). The execution boundary is the natural place to decide what survives:

- Sub-agents should expose only return values across frames, not internal conversations ([scoping note](./llm-context-is-composed-without-scoping.md))
- When the caller does judgment-heavy selection before dispatch, the callee need not inherit the caller's search trace ([ad-hoc prompts](./ad-hoc-prompts-extend-the-system-without-schema-changes.md))
- [Spacebot](./related-systems/spacebot.md) branches return only a scrubbed conclusion
- [Slate](../sources/slate-moving-beyond-react-and-rlm.ingest.md) workers return compressed episodes rather than full tactical traces

This is not just summarization. It is interface design. The deeper question is what `select` should load from stored state into the next bounded context — not just what should cross the execution boundary.

## Conversation vs refinement is one instance of the general problem

[Conversation vs prompt refinement in agent-to-agent coordination](./conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) is a local case of this broader protocol choice.

- **Conversation** preserves the trace: misunderstanding, clarification, correction, and intermediate work all remain in-band
- **Prompt refinement** compresses the trace into a new handoff artifact: the caller integrates what mattered and re-dispatches with a cleaner frame
- **Context cloning / forking** preserves a selected trace prefix for multiple children without continuing the same conversation indefinitely

The [conversation-vs-refinement note](./conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) studies when each choice is worth its cost. The more general point is that these are different answers to the same question: should session history be the unit that later calls inherit?

## The practical principle

For most orchestration:

- it is often fine to **store more than you load**
- use **trace-preserving storage** early, when you do not yet know the right interface or what later learning may need
- move toward **artifact-first loading** once the caller's real consumption pattern is understood — but "artifact-first" does not mean "minimal"; a compressed episode that also serves memory and learning is still an artifact, not a transcript
- keep the **raw trace as an auxiliary substrate** for UI, debugging, audit, or later learning unless a specific bounded call truly needs it

The default mistake is to let a chat interface or framework-owned tool loop decide what the next bounded call should inherit. Interactive sessions want continuity and visibility. Orchestration wants selective loading.

---

Relevant Notes:

- [llm-context-is-composed-without-scoping](./llm-context-is-composed-without-scoping.md) — foundation: frame boundaries only become real interfaces when the parent sees a return value rather than the internal conversation
- [bounded-context orchestration model](./bounded-context-orchestration-model.md) — foundation: `K` can store more artifacts than any one prompt should load; the real control point is `select(K)`
- [llm frameworks should expose the loop](./llm-frameworks-should-expose-the-loop.md) — foundation: the trace problem appears when bounded calls are repackaged into framework-owned sessions that hide progression and make history inheritance the path of least resistance
- [conversation-vs-prompt-refinement-in-agent-to-agent-coordination](./conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) — special case: conversation preserves trace, prompt refinement compresses it into a cleaner handoff artifact
- [ad hoc prompts extend the system without schema changes](./ad-hoc-prompts-extend-the-system-without-schema-changes.md) — exemplifies: the caller does judgment-heavy selection before dispatch, creating a clean handoff boundary
- [distillation](./distillation.md) — mechanism: execution-boundary compression is distillation targeted at the next stage's needs
- [agent orchestration occupies a multi-dimensional design space](./agent-orchestration-occupies-a-multi-dimensional-design-space.md) — extends: return artifact is a design dimension, and this note argues traces should usually not be that artifact
- [codification and relaxing navigate the bitter lesson boundary](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — tension: compressed trace artifacts may preserve more reusable learning signal than narrow result artifacts, even when they are less minimal as interfaces
- [Spacebot](./related-systems/spacebot.md) — exemplifies: branches return scrubbed conclusions rather than full reasoning traces
- [Ingest: Slate: Moving Beyond ReAct and RLM](../sources/slate-moving-beyond-react-and-rlm.ingest.md) — exemplifies: episodes are compressed return artifacts, not tactical transcripts
