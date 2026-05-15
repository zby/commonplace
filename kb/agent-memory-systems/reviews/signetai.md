---
description: "Local-first cross-harness memory daemon with SQLite/FTS/vector/graph recall, trace-derived fact extraction, transcript retention, MCP tools, and connector packaging"
type: ../types/agent-memory-system-review.md
traits: [has-comparison, has-implementation, has-external-sources]
tags: [related-systems, trace-derived]
status: current
last-checked: "2026-04-24"
---

# SignetAI

SignetAI is Signet AI's local-first context layer for coding and agent harnesses. The inspected repository is a Bun/TypeScript monorepo that packages a daemon, CLI, MCP server, SDK, dashboard, connectors for Claude Code/Codex/OpenCode/OpenClaw/Pi/Hermes/Gemini, and an in-repo MemoryBench harness. Its central bet is that durable agent context should live below any one harness: sessions are captured through hooks, stored in SQLite plus readable workspace artifacts, refined by an asynchronous memory pipeline, and recalled through hooks, CLI, HTTP, MCP, and connector surfaces.

**Repository:** https://github.com/Signet-AI/signetai

**Reviewed commit:** https://github.com/Signet-AI/signetai/commit/966db78e6eca800a3853f50a9c611646e6065516

## Core Ideas

**Cross-harness continuity is the product boundary.** Signet is not a chat app or an agent harness; it is a shared context substrate installed underneath existing tools. The README explicitly frames it as "bring your own context" across Claude Code, OpenCode, OpenClaw, Codex, Hermes Agent, Pi, and planned Gemini CLI support, while the package layout backs that up with separate connector packages plus the publishable `signetai` bundle ([README.md](https://github.com/Signet-AI/signetai/blob/966db78e6eca800a3853f50a9c611646e6065516/README.md), [package.json](https://github.com/Signet-AI/signetai/blob/966db78e6eca800a3853f50a9c611646e6065516/package.json), [packages/signetai/package.json](https://github.com/Signet-AI/signetai/blob/966db78e6eca800a3853f50a9c611646e6065516/packages/signetai/package.json)). The Codex connector, for example, writes Codex lifecycle hooks and MCP configuration rather than asking Codex to adopt a new runtime ([packages/connector-codex/src/index.ts](https://github.com/Signet-AI/signetai/blob/966db78e6eca800a3853f50a9c611646e6065516/packages/connector-codex/src/index.ts)).

**Daemon-owned SQLite memory, with raw-first writes.** The memory system stores records in `$SIGNET_WORKSPACE/memory/memories.db`; each memory can have FTS5, vector embeddings through `sqlite-vec`, content hashes, source metadata, version/audit history, and agent/scope visibility. The core database wrapper loads Bun SQLite or `better-sqlite3`, runs migrations, and degrades vector search when the extension is unavailable ([packages/core/src/database.ts](https://github.com/Signet-AI/signetai/blob/966db78e6eca800a3853f50a9c611646e6065516/packages/core/src/database.ts), [packages/core/src/migrations/001-baseline.ts](https://github.com/Signet-AI/signetai/blob/966db78e6eca800a3853f50a9c611646e6065516/packages/core/src/migrations/001-baseline.ts)). The docs' "raw-first" claim is visible in the worker design: user content is persisted and extraction work is queued rather than making LLM extraction part of the initial commit ([docs/PIPELINE.md](https://github.com/Signet-AI/signetai/blob/966db78e6eca800a3853f50a9c611646e6065516/docs/PIPELINE.md), [packages/daemon/src/pipeline/worker.ts](https://github.com/Signet-AI/signetai/blob/966db78e6eca800a3853f50a9c611646e6065516/packages/daemon/src/pipeline/worker.ts)).

**Two-pass LLM refinement with conservative controlled writes.** Pipeline V2 runs extraction first, asking an LLM for atomic facts and entity relations, then runs a decision pass that compares each extracted fact against top candidate memories and proposes `add`, `update`, `delete`, or `none` ([packages/daemon/src/pipeline/extraction.ts](https://github.com/Signet-AI/signetai/blob/966db78e6eca800a3853f50a9c611646e6065516/packages/daemon/src/pipeline/extraction.ts), [packages/daemon/src/pipeline/decision.ts](https://github.com/Signet-AI/signetai/blob/966db78e6eca800a3853f50a9c611646e6065516/packages/daemon/src/pipeline/decision.ts)). The worker then applies proposals only after confidence, dedupe, embedding, write-gate, and contradiction checks. `add` is the normal autonomous path; `update`/`delete` are present in code behind `allowUpdateDelete`, with archive and soft-delete paths, while docs still describe destructive mutation as more future-facing. That docs/code mismatch is important: the implementation is more advanced than some prose says, but the governance boundary remains conservative.

**Recall is traversal-shaped hybrid search, not only vector lookup.** Recall combines FTS5 BM25, vector similarity, graph-linked IDs, optional traversal from focal entities, structured evidence shaping, dampening, reranking, and transcript expansion ([packages/daemon/src/memory-search.ts](https://github.com/Signet-AI/signetai/blob/966db78e6eca800a3853f50a9c611646e6065516/packages/daemon/src/memory-search.ts), [packages/daemon/src/pipeline/graph-search.ts](https://github.com/Signet-AI/signetai/blob/966db78e6eca800a3853f50a9c611646e6065516/packages/daemon/src/pipeline/graph-search.ts), [packages/daemon/src/pipeline/graph-traversal.ts](https://github.com/Signet-AI/signetai/blob/966db78e6eca800a3853f50a9c611646e6065516/packages/daemon/src/pipeline/graph-traversal.ts)). The knowledge-architecture docs are unusually explicit about why the graph exists: not as an end in itself, but to form a bounded candidate pool before flatter retrieval and learned ranking ([docs/KNOWLEDGE-ARCHITECTURE.md](https://github.com/Signet-AI/signetai/blob/966db78e6eca800a3853f50a9c611646e6065516/docs/KNOWLEDGE-ARCHITECTURE.md)).

**Lossless session lineage sits under extracted memory.** Migration 040 adds `session_transcripts`, and the daemon keeps transcript search/fallback paths separate from extracted memories ([packages/core/src/migrations/040-session-transcripts.ts](https://github.com/Signet-AI/signetai/blob/966db78e6eca800a3853f50a9c611646e6065516/packages/core/src/migrations/040-session-transcripts.ts), [packages/daemon/src/session-transcripts.ts](https://github.com/Signet-AI/signetai/blob/966db78e6eca800a3853f50a9c611646e6065516/packages/daemon/src/session-transcripts.ts)). The `memory-lineage` module also writes summary/transcript/compaction/manifest artifacts and renders bounded projections for working memory ([packages/daemon/src/memory-lineage.ts](https://github.com/Signet-AI/signetai/blob/966db78e6eca800a3853f50a9c611646e6065516/packages/daemon/src/memory-lineage.ts)). This gives Signet a useful two-layer story: extracted facts optimize context, while transcript artifacts preserve auditability and recovery.

**Procedural memory is modeled as graph-addressable skills.** Installed skills are not only filesystem files; migration 018 adds `skill_meta`, and the skill graph pipeline installs skill nodes, enriches thin frontmatter, embeds trigger text, and optionally extracts body entities ([packages/core/src/migrations/018-skill-meta.ts](https://github.com/Signet-AI/signetai/blob/966db78e6eca800a3853f50a9c611646e6065516/packages/core/src/migrations/018-skill-meta.ts), [docs/PROCEDURAL-MEMORY.md](https://github.com/Signet-AI/signetai/blob/966db78e6eca800a3853f50a9c611646e6065516/docs/PROCEDURAL-MEMORY.md)). This makes skills part of the same retrieval substrate as facts, which is a stronger procedural-memory integration than systems that merely ship prompt files.

**MCP exposes the memory substrate as an agent tool plane.** The daemon's MCP server registers search, store, get/list/modify/forget/feedback, knowledge expansion, session expansion, secret execution, cross-agent messaging, marketplace MCP routing, and code-context tools; handlers call the daemon API so CLI, HTTP, and MCP surfaces share behavior ([docs/MCP.md](https://github.com/Signet-AI/signetai/blob/966db78e6eca800a3853f50a9c611646e6065516/docs/MCP.md), [packages/daemon/src/mcp/tools.ts](https://github.com/Signet-AI/signetai/blob/966db78e6eca800a3853f50a9c611646e6065516/packages/daemon/src/mcp/tools.ts)). This is product-heavy, but it matters architecturally: Signet does not require every harness to speak a bespoke memory protocol.

**Benchmarking is first-class and self-critical.** `memorybench/` is a bundled provider-comparison framework for LongMemEval/LoCoMo/ConvoMem-style evaluation, with checkpointed phases and provider adapters ([memorybench/README.md](https://github.com/Signet-AI/signetai/blob/966db78e6eca800a3853f50a9c611646e6065516/memorybench/README.md), [docs/BENCHMARKING.md](https://github.com/Signet-AI/signetai/blob/966db78e6eca800a3853f50a9c611646e6065516/docs/BENCHMARKING.md)). The docs also call out a Supermemory adapter contract mismatch instead of only publishing a leaderboard claim, which is a useful sign: benchmark shape is treated as part of the system boundary, not just marketing.

## Comparison with Our System

| Dimension | SignetAI | Commonplace |
|---|---|---|
| Primary substrate | SQLite daemon plus workspace markdown/projection artifacts | Markdown files in git |
| Integration boundary | Hooks, CLI, HTTP API, MCP server, SDK, harness connectors | Skills, instructions, filesystem conventions, validation commands |
| Source trace | Session lifecycle hooks, prompt submissions, explicit remembers, transcripts, feedback | Human/agent edits, source snapshots, workshop artifacts, review outputs |
| Learned artifact | Memory rows, facts, graph entities/aspects/attributes, transcript artifacts, skill nodes, predictor pairs | Notes, indexes, instructions, ADRs, semantic links |
| Retrieval | Hybrid FTS/vector, graph traversal, structured evidence, reranking, transcript fallback | Grep/semantic search, indexes, description scanning, link traversal |
| Governance | Shadow mode, write gates, confidence thresholds, mutation freeze, audit history, auth scopes | Git history, frontmatter schemas, validation, review gates, explicit link semantics |
| Curation model | Automated extraction and ranking, with repair surfaces | Human+agent authoring, review, promotion, and semantic linking |
| Portability | Cross-harness local daemon and publishable npm package | Plain files and repository-native operations |

Signet is stronger as runtime infrastructure. It solves problems commonplace mostly treats as outside the library layer: lifecycle hook capture, daemon API surface, authentication, cross-harness installation, MCP tools, benchmark harnesses, transcript retention, and local secret execution. It is the most complete reviewed example so far of a memory substrate that tries to travel with the user across many agent runtimes.

Commonplace is stronger as an accumulated knowledge medium. Signet extracts and ranks durable facts, but most learned state remains database-shaped: rows, scores, graph attributes, embeddings, and audit records. Commonplace's notes are slower and more manual, but they can carry explicit argument structure, source links, semantic relationship labels, review status, and durable interpretive claims. Signet improves what enters the next prompt; commonplace improves the library an agent reasons from.

The deepest design split is between automatic continuity and deliberate distillation. Signet correctly assumes that agent statelessness means context should be injected automatically, but its autonomous pipeline must infer what is worth keeping from traces. Commonplace assumes valuable knowledge needs explicit authoring and review, so it makes mutation expensive but inspectable. A practical future system probably needs both: Signet-like capture for raw operational continuity, commonplace-like promotion for high-reach knowledge.

## Borrowable Ideas

**Raw-first capture with derived facts layered above it.** Ready to borrow for workshop/session capture. The core pattern is strong: commit the raw trace or transcript before any LLM extraction, then create derived memories as separate artifacts with source pointers rather than overwriting the trace.

**Shadow mode for knowledge mutation.** Ready to borrow. Signet's pipeline can run extraction and decision-making while writing only proposals to history. A commonplace analogue would let new ingest/connect/rewrite heuristics accumulate proposed edits before they are allowed to mutate library notes.

**Write gates with explicit skip reasons.** Ready to borrow when automation grows. Low confidence, duplicate hash, empty normalized content, low surprisal, destructive mutation disabled, and contradiction risk are all recorded as distinct outcomes. That is better than silent non-writes because it creates an audit trail for tuning.

**Session transcript table plus rendered projection artifacts.** Needs a use case first. Commonplace already has source snapshots and work notes, but not a general "session lineage" substrate. Signet's split between transcripts, summaries, manifests, and bounded working projection is a concrete design reference for a workshop capture layer.

**Procedural memory as retrievable skill nodes.** Ready to borrow conceptually. Commonplace skills already exist as files, but Signet's model suggests indexing skills as first-class graph nodes with trigger embeddings, usage counts, and relation edges so agents can discover procedures by context rather than exact name.

**Benchmark contract discipline.** Ready to borrow for evaluation work. The MemoryBench docs emphasize provider limits, context token counts, answer prompts, and unfair adapter advantages. That framing transfers directly to any future KB retrieval benchmark: the adapter contract is part of the claim.

## Trace-derived learning placement

**Trace source.** Signet consumes session lifecycle events and prompt submissions from harness hooks, explicit `remember` calls, MCP memory writes, session-end transcripts, and feedback on injected memories. The source traces are live agent/user interaction streams, not only imported documents.

**Extraction.** The main extraction oracle is an LLM pass that emits structured facts and entity relations from raw memory content. A second LLM pass proposes add/update/delete/none decisions against existing memory candidates. Deterministic gates then decide what can be committed: confidence thresholds, dedupe hashes, write-gate surprisal, mutation flags, contradiction checks, scope/visibility, and transaction boundaries.

**Representational form.** The learned state is mixed symbolic/prose/opaque. Memory rows and graph attributes are symbolic database records; transcript and projection artifacts are prose/file records; embeddings and predictor training pairs are opaque or numeric runtime state.

**Behavioral authority.** Extracted memories mostly play a knowledge-artifact use: they are retrieved and injected as facts, preferences, decisions, and procedures. Skills-as-graph-nodes move closer to system-definition because retrieved skill content can change what the agent does. Predictor feedback and training pairs are system-definition candidates, but the inspected code treats the predictor as a sidecar/WIP path rather than the core memory mechanism.

**Scope.** Scope is per-agent, per-project, per-session, or shared/group depending on visibility and auth policy. It is not only per-task benchmark memory; the product target is persistent cross-harness user/workspace memory.

**Timing.** The loop is online and staged: hooks store or recall during live sessions, background workers extract and decide asynchronously, maintenance/synthesis workers refine later, and benchmark runs can checkpoint ingestion and evaluation phases.

**Survey placement.** Signet strengthens the trace-derived survey's "artifact learning beats raw trace replay for operational memory" axis, but splits the usual artifact category. The durable artifact is not one readable rulebook or note set; it is a graph/database substrate with file-backed transcript lineage and MCP-facing tools. That makes it closer to Memori, Cludebot, and Hindsight than to Reflexion or ExpeL, but with much stronger local-first and cross-harness packaging.

## Curiosity Pass

**The docs/code mismatch around destructive mutation is revealing.** `docs/PIPELINE.md` still describes update/delete as blocked or future-facing, while `worker.ts` contains real update/delete paths under `allowUpdateDelete`, including cold archival, soft deletion, semantic contradiction checks, and audit metadata. The safer interpretation is that destructive mutation exists but is not the stable default operating mode yet.

**"Readable record" mostly means inspectable source and projections, not that primary memory is file-native.** Signet keeps transcripts and rendered artifacts, but the source of truth for memory is SQLite. That is not a flaw; it is a different substrate choice. It does mean Signet is not evidence for the strongest files-first claim in the same way Napkin, engraph, or commonplace are.

**The graph's value depends on candidate shaping, not graph existence.** The docs understand this, and the code implements graph boosts/traversal. The open question is empirical: when does traversal beat a strong hybrid search with transcript expansion? The bundled MemoryBench machinery is the right place to answer that, but the review should not treat the graph itself as proof of better memory.

**The strongest practical mechanism may be installation breadth.** Many systems have fact extraction and vector search. Fewer make the capture/recall loop portable across Codex, Claude Code, OpenCode, Pi, OpenClaw, Hermes, MCP, CLI, and HTTP. If Signet succeeds, distribution and lifecycle hooks may matter as much as the memory algorithm.

**Automatic extraction still hits the curation ceiling.** Signet has better gates than most systems: shadow mode, write gates, history, mutation freeze, confidence, dedupe, transcript fallback. Even so, the system cannot know whether a derived fact is a durable high-reach insight or merely a locally useful operational memory without a stronger review/promotion layer.

## What to Watch

- Whether Signet's destructive update/delete path becomes a documented stable default or remains guarded behind operator flags
- Whether MemoryBench publishes reproducible full-run artifacts for the advertised LongMemEval score, including provider contract, prompt, limit, and context-token details
- Whether graph traversal and structured evidence are shown to improve recall over hybrid FTS/vector plus transcript expansion
- Whether procedural memory retrieval reaches the point where skills are selected by graph/context, not only installed and indexed
- Whether predictor training pairs become an active local scorer that changes injection policy, or remain telemetry for later training
- Whether the local-first daemon keeps working cleanly as team auth, marketplace MCP routing, secrets, and cross-agent sharing increase the trusted surface area

---

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — extends: Signet is a live-session trace-to-symbolic-memory system with unusually broad runtime integration and local-first packaging
- [files-not-database](../../notes/files-not-database.md) — contrasts: Signet preserves readable artifacts, but the primary memory substrate is SQLite plus derived indexes rather than files as source of truth
- [a functioning kb needs a workshop layer](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — exemplifies: Signet's transcript/summary/manifest lineage is a concrete runtime analogue of a workshop layer feeding durable memory
- [agent statelessness means the context engine should inject context automatically](../../notes/agent-statelessness-means-the-context-engine-should-inject-context-automatically.md) — exemplifies: Signet's hooks inject context at lifecycle boundaries instead of waiting for the user to rebuild state
- [context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — exemplifies: Signet spends extraction, graph, and ranking work before prompt time to keep injected context bounded
- [distillation](../../notes/definitions/distillation.md) — qualifies: Signet performs automated trace compression into facts and graph records, but high-reach synthesis still needs curation
- [automating-kb-learning-is-an-open-problem](../../notes/automating-kb-learning-is-an-open-problem.md) — supports: Signet's gates show how much machinery is needed before autonomous memory writes become plausible
- [Memori](./Memori.md) — compares: both intercept live agent interactions and mine them into structured service memory, but Signet exposes more local daemon/storage/control-plane code
- [Hindsight](./hindsight.md) — compares: both use database-backed extracted facts, graph/temporal retrieval, and consolidation-like loops, but Signet emphasizes cross-harness local ownership
- [Sig](../source-only/sig.md) — updates landscape: the earlier source-only Sig coverage made a files-first workplace-memory claim; SignetAI now provides inspectable code for a related but daemon/database-centered context layer
