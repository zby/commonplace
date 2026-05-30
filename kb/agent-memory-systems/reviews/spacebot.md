---
description: "Rust concurrent agent framework with process-isolated channels, branches, workers, cortex synthesis, typed graph memory, and trace-derived persistence"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-05-16"
---

# Spacebot

Spacebot is a Rust agent runtime whose memory design is tied to its process model. The system separates channels, branches, workers, a compactor, and cortex into distinct process types, gives each process type different tools and context, and stores durable memory as typed SQLite records with graph edges and a LanceDB vector/FTS sidecar. Its strongest memory-system lesson is not just the store: it is the way runtime traces are filtered into several artifact layers with different behavioral authority.

**Repository:** <https://github.com/spacedriveapp/spacebot>  
**Reviewed commit:** [ac52277404d3813045aa053b78c95810ab85e7c5](https://github.com/spacedriveapp/spacebot/commit/ac52277404d3813045aa053b78c95810ab85e7c5)  
**Last checked:** 2026-05-16

## Core Ideas

**Process types are first-class runtime objects, not just prompt roles.** Spacebot defines five process types, `Channel`, `Branch`, `Worker`, `Compactor`, and `Cortex`, and routes events, LLM profiles, and tools around that enum ([`src/lib.rs`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/lib.rs), [`README.md`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/README.md)). Channels own the conversation loop and dispatch branches and workers through explicit spawn paths with concurrency checks, task reservation, and readiness warmup ([`src/agent/channel_dispatch.rs`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/agent/channel_dispatch.rs)). Branches fork channel history into isolated reasoning runs ([`src/agent/branch.rs`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/agent/branch.rs)). Workers execute longer tasks with their own tool server, injected context, segment limits, transient retry policy, and wall-clock timeout ([`src/agent/worker.rs`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/agent/worker.rs)).

**Tool and runtime boundaries encode behavioral authority.** The tool topology gives channels user-facing response and delegation tools, branches memory and recall tools, workers file/shell/browser/task tools, and cortex memory-save tools ([`src/tools.rs`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/tools.rs)). That topology is a system-definition artifact: it enforces which process can speak, mutate memory, run tools, or spawn other work. Direct mode can deliberately widen channel authority, but the default design keeps user conversation, memory extraction, and execution in separate capability surfaces.

**Context isolation is enforced by forking, compaction, and scoped history.** Branches receive a cloned channel history and run without sending user-visible output, while workers do not inherit the full channel transcript unless a dispatch path explicitly injects context ([`src/agent/branch.rs`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/agent/branch.rs), [`src/agent/worker.rs`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/agent/worker.rs)). The compactor is a monitor and summarization mechanism, not a free-running agent: it estimates token pressure, runs LLM compaction for background/aggressive thresholds, and performs emergency truncation when necessary ([`src/agent/compactor.rs`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/agent/compactor.rs)). The thresholds and working-memory budgets are configuration artifacts ([`src/config/types.rs`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/config/types.rs)).

**Durable memory is a typed graph plus a derived retrieval index.** Canonical memory records live in SQLite with `MemoryType` values for facts, preferences, decisions, identity, events, observations, goals, and todos; associations use edge labels such as `updates`, `contradicts`, `caused_by`, and `part_of` ([`src/memory/types.rs`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/memory/types.rs), [`migrations/20260211000001_memories.sql`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/migrations/20260211000001_memories.sql)). The store handles CRUD, access counts, soft forgetting, association rewiring, and atomic merges ([`src/memory/store.rs`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/memory/store.rs)). LanceDB holds embeddings and FTS rows as a derived search index that can be rebuilt from SQLite ([`src/memory/lance.rs`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/memory/lance.rs)). Hybrid search fuses FTS, vector, and graph-neighborhood signals ([`src/memory/search.rs`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/memory/search.rs)).

**Trace-derived memory is implemented, but skill learning is not.** A silent memory-persistence branch can be triggered by message count, time, or event density; it receives channel history, recalls existing memory first, calls `memory_save`, and must finish through a contract tool that verifies the saved memory IDs and optional working-memory events ([`src/agent/channel.rs`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/agent/channel.rs), [`src/agent/channel_dispatch.rs`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/agent/channel_dispatch.rs), [`prompts/en/memory_persistence.md.j2`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/prompts/en/memory_persistence.md.j2), [`src/tools/memory_persistence_complete.rs`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/tools/memory_persistence_complete.rs)). Spacebot also loads and installs skills, and workers can read them, but the current codebase has no implemented path for the agent to write a new skill from experience; the design document calls that gap out explicitly ([`src/skills.rs`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/skills.rs), [`src/tools/read_skill.rs`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/tools/read_skill.rs), [`src/tools/install_skill.rs`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/tools/install_skill.rs), [`docs/design-docs/skill-authoring.md`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/docs/design-docs/skill-authoring.md)).

**Cortex turns runtime activity into layered context.** Cortex maps process events into signals, supervises branch and worker timeouts, opens circuit breakers after repeated failures, refreshes memory bulletins, runs memory maintenance, synthesizes working-memory batches, and regenerates knowledge synthesis when memory changes ([`src/agent/cortex.rs`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/agent/cortex.rs)). Working memory stores process-level events and synthesized day summaries in SQLite; the migration comments explicitly separate these events from raw user messages or agent responses ([`src/memory/working.rs`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/memory/working.rs), [`migrations/20260319000001_working_memory.sql`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/migrations/20260319000001_working_memory.sql)). The cortex bulletin and knowledge synthesis are behavior-shaping knowledge artifacts because they are injected as context, but they are not the canonical memory store.

**Scheduling and circuit breakers are part of the memory architecture.** Cron jobs are durable scheduling artifacts with prompts, cron or interval timing, delivery targets, active hours, timeouts, execution records, and consecutive failure counts; after three failures the scheduler disables the job ([`src/cron/scheduler.rs`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/cron/scheduler.rs), [`src/cron/store.rs`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/cron/store.rs)). Cortex has its own circuit breakers for bulletin refresh and maintenance failures ([`src/agent/cortex.rs`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/agent/cortex.rs)). These are system-definition artifacts because they decide when future agent loops run or stop running.

**Multi-user message coalescing is a channel-level context control.** Channels buffer fast multi-user input, apply debounce and maximum wait windows, persist each incoming message separately, then present a formatted batch as one user turn with a coalescing hint ([`src/agent/channel.rs`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/agent/channel.rs), [`src/agent/channel_history.rs`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/agent/channel_history.rs), [`prompts/en/fragments/coalesce_hint.md.j2`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/prompts/en/fragments/coalesce_hint.md.j2)). This keeps raw conversation records available while shaping the live context differently from the storage substrate.

**Model routing is process-aware.** The LLM routing layer chooses models by process type, allows task overrides for workers and branches, carries fallback chains, and stores per-process thinking effort ([`src/llm/routing.rs`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/llm/routing.rs)). This makes model selection another system-definition artifact rather than an implementation detail hidden inside calls.

## Comparison with Our System

| Lens | Spacebot | Commonplace relevance |
| --- | --- | --- |
| Process model | Runtime process types with isolated tools, histories, channels, and supervisors. | Strong reference for making agent roles operational rather than rhetorical. |
| Memory substrate | SQLite canonical records, graph edges, working-memory tables, LanceDB vector/FTS sidecar, runtime bulletins. | Useful separation of canonical knowledge artifacts from derived search indexes and prompt-time summaries. |
| Trace use | Channel history and process events are mined into durable memory records and working-memory summaries. | Directly relevant to [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md). |
| Behavioral authority | Tool topology, prompts, routing config, cron jobs, and circuit breakers enforce what future loops may do. | Good example for applying [behavioral authority](../../notes/definitions/behavioral-authority.md) beyond "memory" as storage. |
| Lineage | Memories have type, source, channel, timestamps, and associations; summaries have event counts and windows. | Better than opaque summaries, but LLM synthesis still has weak citation-level lineage. |
| Codification | Many policies are Rust code and SQL schema; prompts remain high-authority prose. | Similar split to Commonplace's code-backed validation plus prose conventions. |

Spacebot is closer to a live autonomous runtime than to a repository knowledge base. Commonplace accumulates reviewed artifacts for later agents; Spacebot maintains online conversation, task, and autonomy state for a running assistant. The overlap is in the artifact taxonomy: both systems need to distinguish a knowledge artifact that informs an agent from a system-definition artifact that constrains or schedules it.

## Borrowable Ideas

- Use process-specific tool servers as explicit authority boundaries. Spacebot's channel/branch/worker/cortex split is clearer than a single omnibus tool menu.
- Treat automatic memory extraction as a contract-bearing background process. The `memory_persistence_complete` tool prevents a branch from vaguely claiming it saved memories when it did not.
- Keep canonical memory and retrieval indexes separate. SQLite remains the source of truth while LanceDB is a rebuildable vector/FTS sidecar.
- Preserve raw traces and synthesized traces as different artifact layers. Conversation messages, working-memory events, intraday syntheses, daily summaries, and cortex bulletins have different review and invalidation needs.
- Coalesce multi-user bursts before model invocation while still storing each raw message separately.
- Record absence carefully. The repo advertises learning skills from experience, but at this commit skill writing is not implemented; that should not be collapsed into the implemented memory system.

## Trace-derived learning placement

Spacebot belongs in the trace-derived category because current code can mine live channel traces into durable memories and process traces into working-memory syntheses. This is artifact learning, not model-weight learning.

**Trace sources.** The relevant traces are channel histories, user messages, branch and worker completions, task updates, cron executions, memory-save events, errors, decisions, and other `ProcessEvent` or working-memory event records ([`src/lib.rs`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/lib.rs), [`src/memory/working.rs`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/memory/working.rs)). Runtime cortex signals are mostly transient control inputs; only selected events become durable working-memory rows.

**Extraction path.** A memory-persistence branch reads recent channel context, recalls existing memories, saves selected facts or preferences through `memory_save`, and reports completion through a validating terminal tool ([`src/tools/memory_save.rs`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/tools/memory_save.rs), [`src/tools/memory_recall.rs`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/tools/memory_recall.rs), [`src/tools/memory_persistence_complete.rs`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/tools/memory_persistence_complete.rs)). Cortex separately synthesizes intraday and daily working-memory summaries, regenerates knowledge synthesis after memory changes, and refreshes a memory bulletin used for warm context ([`src/agent/cortex.rs`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/agent/cortex.rs)).

**Storage substrate.** Durable state spans SQLite memory, association, conversation, cron, task, and working-memory tables; LanceDB vector and FTS tables; prompt templates on disk; installed skill files; and runtime `ArcSwap` strings for bulletin and synthesis state. Event buses and cortex signal buffers are runtime substrate, not durable memory.

**Representational form.** Memory content, summaries, bulletins, and prompts are prose. Memory types, edges, tool schemas, schedules, process enums, and SQL schemas are symbolic. Embeddings in LanceDB are distributed-parametric retrieval artifacts, but they do not constitute learned policy.

**Lineage.** Individual memories carry source, channel, timestamps, access metadata, type, importance, and graph associations. Working-memory events carry day/type/detail fields, and summaries carry time windows and counts. The weak point is LLM synthesis lineage: a daily summary or knowledge synthesis may be behavior-shaping without preserving fine-grained citations back to every originating event.

**Behavioral authority.** Raw logs, conversation records, memory rows, working-memory events, and summaries are knowledge artifacts. Prompt templates, routing config, tool topology, cron jobs, task records, skill files, and circuit breakers are system-definition artifacts. Memory bulletins and knowledge synthesis sit in the middle: their content is a knowledge artifact, but the injection machinery that places them into future contexts has system-definition authority.

**Non-evidence.** The current code does not show model fine-tuning, policy-gradient learning, or implemented agent-written skill capture. The trace-derived claim rests on memory persistence and working-memory synthesis, not on the README's broader skill-learning language.

## Curiosity Pass

The interesting design move is that Spacebot refuses to make "memory" one layer. It has raw conversation logs, process events, durable typed memories, graph edges, vector rows, working-memory syntheses, memory bulletins, knowledge synthesis, prompt templates, skills, cron jobs, and circuit breakers. Those artifacts all shape behavior differently. A review that calls them all "memory" would miss the main architecture.

The risk is quality control. Memory persistence is LLM-mediated, and the save tool verifies structure, embeddings, and associations but not semantic truth. Cortex summaries are useful context artifacts, yet their lineage is weaker than the underlying event rows. Memory maintenance can decay, prune, and merge records algorithmically ([`src/memory/maintenance.rs`](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/memory/maintenance.rs)); that is valuable for keeping the store small, but it also means future behavior depends on heuristic retention policy.

Spacebot is especially useful for Commonplace because it makes behavioral authority visible. The tool server answers "who may mutate what?" The router answers "which model acts?" The scheduler answers "when does an agent run?" The cortex loop answers "which traces become active context?" Those are the same questions behind [knowledge artifact](../../notes/definitions/knowledge-artifact.md), [system-definition artifact](../../notes/definitions/system-definition-artifact.md), and [behavioral authority](../../notes/definitions/behavioral-authority.md).

## What to Watch

- Whether a real `write_skill` or experience-to-skill path is implemented after this commit.
- Whether memory-persistence branches gain stronger evidence citation or review hooks.
- Whether cortex knowledge synthesis becomes canonical state or remains a derived prompt-time artifact.
- Whether graph associations become LLM-generated beyond memory-save calls and merge rewiring.
- How dormant cortex mode, wake signals, and bulletin refresh behave in long-running deployments.
- Whether direct mode is used often enough to weaken the clean channel/branch/worker boundary.

## Bottom Line

Spacebot is a strong related-system reference for concurrent agent memory because it connects memory to process isolation, scheduling, tool authority, and context synthesis. It should be classified as trace-derived: channel traces and process traces can become durable memory records and synthesized working-memory artifacts. The classification should not rely on the unimplemented skill-learning claim; the implemented evidence is memory persistence, working-memory synthesis, and cortex-driven prompt activation.

## Relevant Notes

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md)
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md)
- [Agent statelessness means the context engine should inject context automatically](../../notes/agent-statelessness-means-the-context-engine-should-inject-context.md)
- [A functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md)
- [GBrain](./gbrain.md)
- [WUPHF](./wuphf.md)
- [Playground](./playground.md)
- [SignetAI](./signetai.md)
