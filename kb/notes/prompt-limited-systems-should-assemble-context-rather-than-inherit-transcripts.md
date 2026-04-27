---
description: Agent systems doing recurring work should treat prompts as assembled projections of explicit state, making selection and distillation architectural work.
type: kb/types/note.md
traits: [synthesis, title-as-claim]
tags: [computational-model, context-engineering, agent-memory]
status: seedling
---

# Prompt-limited systems should assemble context rather than inherit transcripts

Every piece of knowledge an LLM can use must enter through a bounded prompt. Once that is the cost model, the prompt is not a continuation of the past by default. It is an assembled projection of explicit system state: selected tokens, in a selected form, for a selected call.

That changes the design question. The issue is not "how do we add memory to chat?" It is "which state should this bounded call receive, at what resolution, and with what framing?"

The chat-history model remains attractive because [it trades context efficiency for implementation simplicity](./the-chat-history-model-trades-context-efficiency-for-implementation-simplicity.md). Appending messages preserves information before the builder knows which interface, return artifact, or selection policy will matter. Transcript inheritance is therefore a good exploratory default. It becomes the wrong architectural default once the system has recurring tasks, stable artifacts, or enough history that irrelevant context competes with the active work.

The alternative is bounded-context orchestration. External stores hold more state than any one call should load, and a scheduler assembles each prompt from selected state. In the [bounded-context orchestration model](./bounded-context-orchestration-model.md), this is the `select(K)` step: choosing and framing the subset of stored state that a bounded call can use. The prompt is an assembly target.

## External State Is Primary

In a transcript-centered architecture, the conversation is the state. In a prompt-limited architecture, the knowledge base, work artifacts, source snapshots, indexes, and generated reports are the state. The prompt is a temporary view over them.

[Session history should not be the default next context](./session-history-should-not-be-the-default-next-context.md) gives the mechanism-level rule: storing execution history and loading it into the next call are separate decisions. A system may keep the transcript for audit, debugging, or later extraction without treating it as the next prompt's substrate.

Bigger context windows do not remove this problem. Larger windows raise the volume ceiling, but [effective context is task-relative and complexity-relative](./effective-context-is-task-relative-and-complexity-relative-not-a-fixed-model-constant.md). Raw history is still organized by time rather than by task relevance, and irrelevant material still imposes interpretation cost. The architecture has to reduce effective cost through selection, scoping, framing, and distillation.

## Knowledge Must Be Shaped Before Loading

Raw transcripts are weak future context because they preserve the local path of discovery rather than the reusable result. They mix conclusions with false starts, corrections, abandoned branches, politeness, and incidental phrasing. A prompt-limited system therefore turns experience into artifacts before it expects reuse: notes, decisions, schemas, instructions, reports, tests, or compressed episodes.

This is the memory version of [raw accumulation does not create usable memory](./raw-accumulation-does-not-create-usable-memory.md). Accumulated material becomes usable only when it has handles, scope, relationships, provenance, trust signals, and lifecycle pressure. For a KB, descriptions and indexes are not ornamentation; they are the metadata that lets a future `select` step decide without opening every artifact.

The same rule applies to learning. Continuous learning in an agent system does not require every lesson to enter weights. It requires a durable substrate that can change future action capacity. [Designing a memory system for LLM-based agents](./designing-agent-memory-systems.md) frames this as effect-based memory: remembered material matters when it changes answering, acting, artifact creation, review, or behavior under bounded context.

## Loading Needs A Hierarchy

Prompt assembly is not one retrieval call. Different material has different read frequency, volatility, and failure cost. Always-loaded context should be slim routing and invariants. Frequently referenced definitions and constraints should load when triggered. Detailed procedures and evidence should load on demand. [Instruction specificity should match loading frequency](./instruction-specificity-should-match-loading-frequency.md) states this cache-tier rule directly.

This makes progressive disclosure part of the runtime architecture. A good system prompt is a map, not a manual. A skill description is a compact affordance, not the whole procedure. An index gives discriminating descriptions, not full note bodies. Each layer exists because the next layer is too expensive to keep permanently live.

## Boundaries Are Distillation Points

Every execution boundary asks what crosses into the next bounded context. Passing a full conversation across the boundary preserves maximum information, but it spends the next call's budget on reconstructing what the previous call already knew. Passing a result artifact makes the boundary an interface.

The artifact can be narrow, such as a return value, or richer, such as a compressed episode. The important property is that it is shaped for a consumer. [Distillation](./definitions/distillation.md) is directed context compression, so boundary artifacts should be distilled toward their next use: retry signal, claim list, decision record, evidence summary, plan, or status line. Uniform "summarize the transcript" compression is usually too generic to serve the next call well.

## Selection Is The Critical Path

Once state is external and prompts are assembled, selection becomes the real bottleneck. The system must decide what is relevant, at what resolution, with what framing, and under which source assumptions. That is harder than appending the transcript, but it is also where most context efficiency is recovered.

This reframes [context engineering](./definitions/context-engineering.md) (getting the right knowledge into bounded context at the right time). The prompt window is to agent systems what algorithmic complexity is to ordinary software: a cost model that pervades data structures, cache tiers, communication protocols, state representation, and decomposition. The engineering problem is not a local prompt-optimization step. It is the architecture that determines what can be selected cheaply enough for the next bounded call.

## Open Questions

The architectural direction still leaves design questions:

- **Selection intelligence.** How much semantic judgment should `select(K)` perform before a bounded call, and how much should be delegated to the call itself?
- **Exploratory loading.** Conversations sometimes surface useful unexpected connections because they wander. A strict selection architecture needs an explicit exploration mode or it may optimize away serendipity.
- **Cold start.** An empty or thin knowledge base may be worse than transcript inheritance. The useful threshold is the minimum viable artifact set that makes assembly cheaper than continuation.
- **Curation economics.** Structured memory only beats transcripts when the future value of selection and reuse exceeds the ongoing cost of curation, validation, and retirement.
- **Hybrid operation.** Short-term interaction may remain chat-shaped while session boundaries distill durable artifacts. The unresolved question is when that hybrid should still be considered chat with memory rather than prompt-limited architecture.

## Scope

This claim does not say interactive chat should disappear. Short, focused conversations are efficient enough, and early exploration benefits from trace preservation. The claim applies when a system expects recurring work, cross-session learning, multi-step orchestration, or durable memory. At that point, transcript inheritance should become an auxiliary trace for audit, debugging, and later extraction, not the default substrate for the next prompt.

---

Relevant Notes:

- [the chat-history model trades context efficiency for implementation simplicity](./the-chat-history-model-trades-context-efficiency-for-implementation-simplicity.md) - grounds: explains why transcript inheritance is attractive and where the tradeoff changes
- [session history should not be the default next context](./session-history-should-not-be-the-default-next-context.md) - mechanism: separates persistence from next-context loading at execution boundaries
- [bounded-context orchestration model](./bounded-context-orchestration-model.md) - mechanism: `select(K)` is the prompt-assembly operation this note makes architectural
- [context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) - grounds: context scarcity is the cost pressure behind assembly, scoping, and distillation
- [effective context is task-relative and complexity-relative not a fixed model constant](./effective-context-is-task-relative-and-complexity-relative-not-a-fixed-model-constant.md) - grounds: larger windows do not remove task-shaped effective-cost pressure
- [raw accumulation does not create usable memory](./raw-accumulation-does-not-create-usable-memory.md) - extends: storage only becomes memory after handles, provenance, trust, and lifecycle work
- [designing a memory system for LLM-based agents](./designing-agent-memory-systems.md) - extends: memory earns its place by changing downstream contextual competence, not by merely existing
- [instruction specificity should match loading frequency](./instruction-specificity-should-match-loading-frequency.md) - mechanism: prompt assembly requires cache-tiered loading rather than flat context
- [distillation](./definitions/distillation.md) - defined-in: execution-boundary artifacts are directed context compression
- [context engineering](./definitions/context-engineering.md) - defined-in: names the routing, loading, scoping, and maintenance problem this note reframes
- [agents navigate by deciding what to read next](./agents-navigate-by-deciding-what-to-read-next.md) - mechanism: selection depends on metadata that makes loading decisions cheap
