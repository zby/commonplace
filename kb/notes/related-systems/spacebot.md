---
description: Rust concurrent agent framework whose process-type architecture (channels, branches, workers, cortex) is the cleanest production implementation of code-level scheduling over bounded LLM calls among reviewed systems
type: note
tags: [related-systems]
status: current
last-checked: 2026-03-09
---

# Spacebot

A concurrent AI agent framework in Rust for multi-user chat (Discord, Slack, Telegram), built by the Spacedrive team. The distinguishing choice is a typed process architecture — five process kinds with distinct tool sets and lifecycle guarantees, supervised by a Rust-level cortex that never delegates scheduling to an LLM. Among reviewed systems, this is the cleanest production implementation of the [clean scheduling model](../bounded-context-orchestration-model.md).

**Repository:** https://github.com/spacedriveapp/spacebot

## Architecture: Five Process Types

The system splits agent functionality across five typed process kinds, each with its own tool set and concurrency rules:

- **Channels** handle user-facing conversation. They never block and carry the running context for a chat session.
- **Branches** fork a channel's context for independent reasoning. A branch deep-clones the channel's history at fork time, runs up to `max_turns` (default 5) in isolation, and returns only a scrubbed conclusion. Branches can think and save memories but cannot reply to users or spawn workers.
- **Workers** execute deterministic tasks (shell, file I/O, browser, web search) in a fresh context with no inherited conversation history.
- **Compactor** monitors context usage and triggers summarisation at graduated thresholds (see below).
- **Cortex** supervises everything else: health monitoring, circuit breakers, memory bulletins, signal aggregation.

Tool-set isolation enforces the separation. Branches get memory tools but no reply tool; workers get execution tools but no branching. The boundaries are in the type system, not in prompt instructions.

## Cortex as Symbolic Scheduler

The cortex is pure Rust — no LLM calls for scheduling decisions. It tracks process health via a 100-item rolling signal buffer (`BranchStarted`, `WorkerCompleted`, `ToolStarted`, etc.), enforces per-process-type timeouts, and trips circuit breakers after 3 consecutive failures (60s cooldown, exponential backoff to 30min). The scheduling policy lives in code, not in a prompt.

This maps directly onto the [bounded-context orchestration model](../bounded-context-orchestration-model.md): the cortex is the symbolic scheduler, channels and branches are bounded LLM calls, and workers are deterministic tool executions outside any context window.

## Branches as a Scoping Mechanism

Branches are the most architecturally interesting process type. LLM context is normally [composed without scoping](../llm-context-is-composed-without-scoping.md) — everything in the conversation is globally visible, and there is no mechanism for a sub-computation to limit what it inherits or to prevent its output from polluting the parent. Branches provide exactly that mechanism: the branch inherits the parent's context at fork time (dynamic scope) but executes in an independent frame that cannot write back to the parent (lexical scope). If context is already at 70% capacity before the first turn, the branch proactively compacts 50%.

This is the closest production analogue to lexical scoping in an agent system we have reviewed. The fork-think-return pattern — inherit context, reason independently, return only the conclusion — is the mechanism the scoping note identifies as missing from most agent architectures.

## Three-Tier Context Overflow Recovery

The compactor monitors token usage (chars/4 heuristic, intentionally overestimates) and acts at three thresholds:

- **80%** — background compaction: summarise oldest 30% via a worker.
- **85%** — aggressive compaction: summarise 50%.
- **95%** — emergency synchronous truncation: drop oldest 50% immediately, no LLM call.

Workers independently check context every 15 turns, deduplicating stale tool results on overflow before force-compacting 75%. The key design insight is that background compaction and emergency truncation are different operations requiring different strategies — graceful summarisation when there is time, hard truncation when there is not.

## Memory

Eight memory types (Fact, Preference, Decision, Identity, Event, Observation, Goal, Todo) with per-type default importance scores (Identity=1.0, Observation=0.3). Six edge types (RelatedTo, Updates, Contradicts, CausedBy, ResultOf, PartOf) stored in SQLite with a `UNIQUE(source, target, relation)` constraint. Retrieval uses Reciprocal Rank Fusion across three sources: vector similarity (LanceDB/HNSW), full-text search (Tantivy), and graph traversal (iterative BFS up to depth 3 from high-importance seed nodes).

The memory is typed but unified — all eight types live in one store, searched through one API. This is a middle ground between flat accumulation (Mem0) and full structural separation. Whether the unified store produces the cross-contamination failures predicted by [three-space memory separation](../three-space-memory-separation-predicts-measurable-failure-modes.md) is an open question; the graph edges (Updates, Contradicts) may partially mitigate search pollution by giving the retriever relationship-aware traversal paths.

## Secondary Mechanisms

**Message coalescing.** In multi-user channels, messages arriving within a configurable debounce window (default 1.5s, hard cap 5s) are batched into a single LLM turn with sender attribution and relative timestamps. The LLM sees `[alice] (+0ms): hey can you refactor auth? [bob] (+300ms): also add tests` and responds once. DMs, system messages, and slash commands bypass coalescing.

**Memory bulletin.** The cortex periodically generates a structured briefing (goals, recent activity, key facts) and injects it into every channel's system prompt. A readiness contract (warm state + embedding model ready + fresh bulletin) gates dispatch, and a circuit breaker prevents bulletin generation from cascading on failure. This is push-based context priming — an alternative to on-demand retrieval.

**Four-level model routing.** Process-type defaults (sonnet for channels, haiku for workers) -> task-type overrides (coding tasks get sonnet) -> sub-millisecond keyword-based complexity scoring -> fallback chains on 429/502 with rate-limit cooldown. All deterministic Rust.

## Comparison with Commonplace

Spacebot is a runtime agent framework; commonplace is a knowledge system with agent-operated methodology. The meaningful comparison is in shared architectural concerns.

| Dimension | Spacebot | Commonplace |
|---|---|---|
| Scheduling | Rust cortex (code-level symbolic scheduler) | Agent loads instructions per task (instruction-routed) |
| Context isolation | Branches: deep-cloned, independently compacted | Sub-agents with fresh context per skill invocation |
| Memory | Typed records in SQLite + LanceDB, graph edges, hybrid search | Typed markdown files in git, area indexes, link semantics |
| Knowledge evolution | Soft delete (forgotten flag), Updates/Contradicts edges | Status field, type transitions (text -> seedling -> note) |
| Overflow | Compactor with 3 thresholds, LLM summarisation | Progressive disclosure (description first, full content on demand) |
| Multi-user | First-class: message coalescing, per-channel state, concurrent processes | Single-user (agent per session) |

**Where Spacebot is stronger.** Process-type separation gives channels, branches, and workers distinct tool sets and lifecycle guarantees enforced by the type system. The three-tier overflow recovery is more robust than anything in our system — we have no runtime safety net for context exhaustion. Message coalescing is a genuine multi-user concurrency pattern we have no equivalent for.

**Where commonplace is stronger.** Knowledge has a lifecycle — notes mature through status transitions, link semantics articulate relationships, descriptions serve as retrieval filters. Spacebot's memory is accumulate-and-search with no maturation path. Our progressive disclosure (load descriptions first, full content on demand) addresses [context efficiency](../context-efficiency-is-the-central-design-concern-in-agent-systems.md) proactively rather than reactively compacting after overflow.

## Borrowable Ideas

**Branches as scoping primitive.** The fork-think-return pattern maps directly onto what our system needs for sub-agent isolation. In commonplace this would be a sub-agent that inherits specific context files (not the full conversation) and returns a structured result. The deep-clone-and-isolate model is immediately applicable. *Ready to borrow.*

**Graduated overflow recovery.** Our system relies on progressive disclosure to prevent overflow. For long sessions, a safety net with separated thresholds — background compaction at one level, emergency truncation at another — would prevent hard failures without requiring the full three-tier implementation. *Needs a use case first — our sessions rarely hit overflow.*

**Memory bulletin as session priming.** Injecting a structured briefing at session start is a push-based alternative to on-demand retrieval. For commonplace, this would mean generating a summary of recent KB changes and active areas when a session begins. *Needs a use case first — CLAUDE.md already serves a similar routing function, though not a recency-aware one.*

**Coalescing for batch operations.** The principle — debounce rapid input, batch into a single turn with metadata — could apply to bulk operations where multiple file changes should be processed as one unit rather than individually. Not directly applicable to single-user sessions.

## What to Watch

- Whether the five fixed process types survive as stronger models emerge. The [multi-agent future prediction](../../sources/voooooogel-multi-agent-future.ingest.md) suggests fixed roles dissolve, but Spacebot's types encode concurrency guarantees and tool-set isolation, not persona-style roles — structural constraints may prove more durable than role assignments.
- Whether the typed-but-unified memory produces the search pollution and identity scatter predicted by [three-space separation](../three-space-memory-separation-predicts-measurable-failure-modes.md). The graph edges may mitigate these, making this a natural test case for the three-space claim.
- Whether the cortex's signal buffer evolves beyond observability. The 100-item rolling window of process events is currently used for health checks and circuit breakers. If it starts informing adaptive scheduling (learning which branch configurations succeed), it becomes a deploy-time learning mechanism.

---

Relevant Notes:

- [bounded-context-orchestration-model](../bounded-context-orchestration-model.md) — exemplifies: Spacebot's cortex is the cleanest production implementation of the clean scheduling model; channels and branches are bounded LLM calls, workers are deterministic tool executions
- [llm-context-is-composed-without-scoping](../llm-context-is-composed-without-scoping.md) — exemplifies: branches inherit channel context (dynamic scope) but execute in independent frames (lexical scope), demonstrating a production scoping mechanism
- [context-efficiency-is-the-central-design-concern-in-agent-systems](../context-efficiency-is-the-central-design-concern-in-agent-systems.md) — exemplifies: addresses both context cost dimensions — compactor handles volume, branches provide complexity isolation
- [three-space-agent-memory-maps-to-tulving-taxonomy](../three-space-agent-memory-maps-to-tulving-taxonomy.md) — tests: typed-but-unified memory with 8 types in a single store is a middle ground between flat storage and full three-space separation
- [agentic-memory-systems-comparative-review](./agentic-memory-systems-comparative-review.md) — extends: Spacebot adds a new position (Rust-level process separation, concurrent multi-user, graph-edged typed memory) not covered by existing entries
