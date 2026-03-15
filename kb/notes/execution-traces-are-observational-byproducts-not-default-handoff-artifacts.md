---
description: Chat systems often treat the execution trace as part of the return protocol, but orchestration usually wants a compressed handoff artifact; traces are valuable for UI and debugging, yet should remain auxiliary unless explicitly distilled
type: note
traits: [has-external-sources]
tags: [computational-model]
status: seedling
---

# Execution traces are observational byproducts, not default handoff artifacts

The chat model makes a specific handoff protocol feel natural: a sub-call returns both its conclusion and the trace of how it got there, folded into one conversational transcript. That is useful for interactive UX, but it is the wrong default for most agent orchestration.

An execution boundary should usually yield two different things:

- a **handoff artifact** for the next stage to consume
- an optional **trace** for humans or monitoring systems to inspect

The first is semantic. The second is observational. Treating the trace as part of the default semantic return blurs the interface between stages and turns orchestration into transcript management.

## Three kinds of trace

"Trace" covers at least three things with different handoff characteristics:

- **Conversation transcript** — the message-by-message exchange between caller and callee. Mixes signal (clarifications, partial results) with noise (misframings, corrections, phatic turns). This is what chat systems preserve by default.
- **Tool/action trace** — the sequence of external calls and their results. More structured, and sometimes the trace *is* the artifact (e.g., "list what you found" where the search log is the answer). But even then, the raw action sequence is rarely the right shape for the next stage.
- **Reasoning trace** — chain-of-thought, planning, deliberation. The most clearly observational: it reveals how the agent thought, not what it concluded. Almost never useful as a handoff artifact.

The rest of this note argues against trace-as-handoff in general, but the argument is sharpest for reasoning traces, strong for conversation transcripts, and most nuanced for tool traces where the action record occasionally *is* the deliverable.

## Why chat systems default to trace-preserving handoff

Raw conversation is the easiest way to preserve maximum information. If the caller does not yet know what matters, returning the whole interaction is the safest first move:

- no premature compression
- no lost false starts or clarifications
- no need to design a return schema upfront
- immediate usefulness for UI, audit, and debugging

This makes transcript return a sensible **exploratory default**. Early in a design, when the real interface between stages is still unknown, preserving the trace minimizes the risk of throwing away the wrong thing.

## Why transcript return breaks down as systems mature

The same property that makes trace-preserving handoff safe early makes it expensive later: it preserves everything.

For orchestration, that is usually the wrong trade:

- the caller receives more than it needs
- local tactical debris survives beyond the stage where it mattered
- downstream stages must re-interpret rather than consume a clean artifact
- interfaces remain implicit, because "the return value" is a transcript rather than a declared object
- context pollution compounds as traces from many steps accumulate

This is the return-value problem from the [scoping note](./llm-context-is-composed-without-scoping.md) in architectural form: if the parent sees the whole internal conversation, the boundary exists structurally (separate invocation, separate context) but not as an information barrier — nothing is actually scoped out.

## The right split: artifact channel vs trace channel

The scheduler usually wants a compact artifact shaped for the next decision:

- a yes/no judgment
- extracted claims
- a scrubbed conclusion
- a compressed episode
- structured data
- symbolic code
- a structured failure or restart signal

The three trace types serve different consumers:

- **Conversation transcripts** → the user interface, audit logs, and onboarding-interview replay
- **Tool/action traces** → debugging tools, telemetry, reproducibility, and sometimes structured extraction (when the action record is close to being the artifact itself)
- **Reasoning traces** → debugging, alignment research, and learning systems that later distill traces into reusable knowledge

These are legitimate uses, but they are not the artifact channel. The trace is evidence about execution. The handoff artifact is what the next stage is supposed to operate on, including recovery decisions such as retry, unwind, or escalation. Keeping the channels separate lets each trace type reach its consumers without polluting the orchestration path.

Failure handling makes the separation especially visible. A bounded execution may return a structured failure artifact without returning the full trace that produced it. The runtime might interpret that artifact directly and choose a retry, unwind, or escalation path. Or it might make a separate bounded LLM call to interpret the failure semantically. In both cases, the important point is the same: the failure becomes an explicit handoff artifact in the loop, not an excuse to promote the whole transcript into orchestration state.

## Execution-boundary compression is a recurring design move

Across the systems and notes above, a recurring move is [compression at the execution boundary](./distillation.md). The execution boundary is the natural place to decide what survives:

- Sub-agents should expose only return values across frames, not internal conversations ([scoping note](./llm-context-is-composed-without-scoping.md))
- When the caller does judgment-heavy selection before dispatch, the callee need not inherit the caller's search trace ([ad-hoc prompts](./ad-hoc-prompts-extend-the-system-without-schema-changes.md))
- [Spacebot](./related-systems/spacebot.md) branches return only a scrubbed conclusion
- [Slate](../sources/slate-moving-beyond-react-and-rlm.ingest.md) workers return compressed episodes rather than full tactical traces

This is not just summarization. It is interface design. The question is not "how do we make the trace shorter?" but "what artifact should cross this boundary?"

## Conversation vs refinement is one instance of the general problem

[Conversation vs prompt refinement in agent-to-agent coordination](./conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) is a local case of this broader protocol choice.

- **Conversation** preserves the trace: misunderstanding, clarification, correction, and intermediate work all remain in-band
- **Prompt refinement** compresses the trace into a new handoff artifact: the caller integrates what mattered and re-dispatches with a cleaner frame
- **Context cloning / forking** preserves a selected trace prefix for multiple children without continuing the same conversation indefinitely

The [conversation-vs-refinement note](./conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) studies when each choice is worth its cost. The more general point here is that these are different answers to the same question: should the execution trace itself be the handoff unit?

## The practical principle

For most orchestration:

- use **trace-preserving return** early, when you do not yet know the right interface
- move toward **artifact-first return** once the caller's real consumption pattern is understood
- keep the **trace as an auxiliary channel** for UI, debugging, audit, or later learning

The default mistake is to let the chat interface decide the orchestration protocol. Chat wants visibility. Orchestration wants clean boundaries.

---

Relevant Notes:

- [llm-context-is-composed-without-scoping](./llm-context-is-composed-without-scoping.md) — foundation: frame boundaries only become real interfaces when the parent sees a return value rather than the internal conversation
- [conversation-vs-prompt-refinement-in-agent-to-agent-coordination](./conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) — special case: conversation preserves trace, prompt refinement compresses it into a cleaner handoff artifact
- [ad hoc prompts extend the system without schema changes](./ad-hoc-prompts-extend-the-system-without-schema-changes.md) — exemplifies: the caller does judgment-heavy selection before dispatch, creating a clean handoff boundary
- [distillation](./distillation.md) — mechanism: execution-boundary compression is distillation targeted at the next stage's needs
- [agent orchestration occupies a multi-dimensional design space](./agent-orchestration-occupies-a-multi-dimensional-design-space.md) — extends: return artifact is a design dimension, and this note argues traces should usually not be that artifact
- [llm frameworks should expose the loop](./llm-frameworks-should-expose-the-loop.md) — extends: recovery logic works best when the runtime can either interpret failure artifacts directly or dispatch a separate bounded call, rather than hiding both inside a framework-owned session
- [Spacebot](./related-systems/spacebot.md) — exemplifies: branches return scrubbed conclusions rather than full reasoning traces
- [Ingest: Slate: Moving Beyond ReAct and RLM](../sources/slate-moving-beyond-react-and-rlm.ingest.md) — exemplifies: episodes are compressed return artifacts, not tactical transcripts
