---
description: "AI-Context-OS review: filesystem-first Markdown memory with L0/L1/L2 context loading, generated adapters, MCP/chat read-back, and trace-derived optimization suggestions"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-04"
tags: [trace-derived]
---

# AI-Context-OS

AI-Context-OS, also branded MEMM, is a Tauri desktop app by alexdcd for turning a local workspace folder into a tool-agnostic agent memory layer. At the reviewed public snapshot, the canonical memory model is Markdown files with YAML frontmatter and L0/L1/L2 body sections, served through generated router files, a Tauri chat path, and MCP tools; SQLite is used for observability and optimization signals rather than as the canonical memory store.

**Repository:** https://github.com/alexdcd/AI-Context-OS

**Reviewed commit:** [f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5](https://github.com/alexdcd/AI-Context-OS/commit/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5)

**Last checked:** 2026-06-04

## Core Ideas

**Canonical memory is local Markdown, not an integration-side database.** The README says the workspace file tree is the source of truth, and the code implements that through `MemoryMeta`, frontmatter parsing, L1/L2 splitting, recursive scans, and file writes ([README.md](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/README.md), [src-tauri/src/core/types.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/core/types.rs), [src-tauri/src/core/frontmatter.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/core/frontmatter.rs), [src-tauri/src/core/memory.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/core/memory.rs)). Moving a memory does not change its semantic type; scanning enriches metadata from the path but classification comes from frontmatter.

**Context efficiency is explicit and progressive.** Each memory has an L0 summary, L1 operational summary, and L2 detail body. `execute_context_query` scores all memories, caps L2 to the top cluster, greedily allocates L0/L1/L2 under a token budget, and records unloaded-but-available memories separately ([src-tauri/src/core/engine.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/core/engine.rs), [src-tauri/src/core/levels.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/core/levels.rs)). The context package is therefore bounded by both volume and complexity: summaries are cheap, details are reserved for high-scoring memories, and the agent can see references to omitted candidates in the MCP package.

**Retrieval is deterministic hybrid scoring, not vector search.** The scoring path combines tag/L0/ontology heuristics, BM25 over expanded lexical queries, recency, authored importance, access frequency, and graph proximity from Personalized PageRank seeded by the first pass ([docs/algorithms-and-scoring.md](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/docs/algorithms-and-scoring.md), [src-tauri/src/core/scoring.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/core/scoring.rs), [src-tauri/src/core/search.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/core/search.rs), [src-tauri/src/core/graph.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/core/graph.rs)). This makes ranking inspectable and cheap, but effective semantic relevance is not proven by the code.

**Adapters are generated views over the same canonical store.** Router regeneration scans memories, builds a neutral manifest, writes `claude.md`, `.cursorrules`, `.windsurfrules`, `.ai/index.yaml`, and `.ai/catalog.md`, and reuses adapter renderers for tool-specific wrapper text ([src-tauri/src/commands/router.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/commands/router.rs), [src-tauri/src/core/router.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/core/router.rs), [src-tauri/src/core/compat.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/core/compat.rs)). The adoption affordance is strong: agents can degrade to ordinary files even when MCP is unavailable.

**Observability is separate from canonical memory.** MCP context requests are logged to `{workspace}/.cache/observability.db`, including loaded and not-loaded memories, and a separate usage JSON tracks last access and access counts ([src-tauri/src/core/mcp.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/core/mcp.rs), [src-tauri/src/core/observability.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/core/observability.rs), [src-tauri/src/core/usage.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/core/usage.rs)). Optimization analysis derives pending suggestions from those traces, but application is currently status-tracking or human-mediated rather than automatic rewriting of memories.

## Artifact analysis

- **Storage substrate:** `files` — Canonical memories, router artifacts, inbox items, proposals, journal logs, tasks, scratch, and adapter files live in the workspace file tree; context-request telemetry, served-memory records, health snapshots, and optimization records live in SQLite under `.cache/observability.db` as support state.
- **Representational form:** `prose` `symbolic` — Memory content and rules are prose Markdown; frontmatter, L0/L1/L2 markers, generated YAML/catalog/router files, MCP schemas, scoring records, graph edges, proposals, tasks, and observability rows are symbolic control surfaces.
- **Lineage:** `authored` `imported` `trace-extracted` — Users author memories and rules, import inbox/link/file material, and the system derives usage counters, context-request logs, served/not-loaded rows, daily operational events, and optimization suggestions from runtime traces.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` `learning` — Memories and sources are evidence/context; `.ai/rules`, generated router files, and MCP prelude text instruct agents; frontmatter, folder contracts, graph links, skills, and adapters route work; protected-memory checks and governance surfaces validate or warn; scoring ranks read-back; observability-derived suggestions provide learning input for future maintenance.

**Markdown memories.** A memory file combines YAML frontmatter (`id`, `type`, `l0`, importance, tags, links, `requires`, `optional`, `protected`, `derived_from`) with L1/L2 prose sections. The operative split is important: the prose is agent-readable knowledge, while the frontmatter is routing, ranking, dependency, and validation metadata.

**Generated router and adapter artifacts.** `claude.md`, `.cursorrules`, `.windsurfrules`, `.ai/index.yaml`, and `.ai/catalog.md` are derived views over the file store. They have system-definition authority for agents that load them, but they are explicitly overwritten and should not be treated as canonical memory.

**Context scoring records.** `ScoreBreakdown`, `ScoredMemory`, `LoadedMemory`, and `UnloadedMemory` are transient symbolic artifacts produced per query. They decide what reaches the next model call, but they do not persist except where MCP observability logs the served/not-loaded result.

**Observability and optimization artifacts.** SQLite `context_requests`, `memories_served`, and `memories_not_loaded` are raw trace records for context use. `OptimizationRecord` rows are distilled symbolic/prose suggestions such as compressing large L1 summaries, archiving unused memories, promoting low-importance memories that are frequently served, reviewing always-L2 memories, merging tag-overlap candidates, or nudging near-threshold memories ([src-tauri/src/core/optimizer.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/core/optimizer.rs)). The promotion path is trace-derived suggestion to human/system action; the inspected code updates suggestion status but does not itself rewrite the target memory.

**Inbox proposals.** Inbox items and `IngestProposal` JSON files are a governed staging layer: heuristics or provider inference classify captured material as promote, route to sources, update, discard, or needs-review, and applying a proposal writes a memory/source file plus daily-log entry ([src-tauri/src/commands/inbox.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/commands/inbox.rs)). This is a real promotion path from imported material to canonical Markdown, but it is proposal-mediated rather than autonomous memory curation.

## Comparison with Our System

AI-Context-OS and Commonplace share a file-first premise: durable knowledge should remain inspectable, diffable, and usable without a metered vendor backend. Both systems also distinguish canonical artifacts from generated navigation surfaces. Commonplace puts more weight on typed library artifacts, validation, review gates, and methodology-level curation; AI-Context-OS puts more weight on desktop UX, live context assembly, MCP/chat serving, and trace-derived operational telemetry.

The strongest divergence is authority. Commonplace's collection contracts, type specs, and validation commands are explicit governance over the KB. AI-Context-OS has protected-memory checks, folder contracts, conflict/decay/consolidation suggestions, and optimization records, but most governance remains advisory. That makes it friendlier as a user-facing app, but weaker as an enforced methodology substrate.

The strongest alignment is context-budget discipline. AI-Context-OS's L0/L1/L2 allocation is a concrete implementation of progressive disclosure, while Commonplace mostly relies on indexes, links, collection routing, and agent judgment. The reviewed code shows how a prose-first store can still have deterministic serve-time budget policy without vector infrastructure.

### Borrowable Ideas

**Progressive detail levels as a serving contract.** Commonplace could distinguish one-line retrieval summaries, operational summaries, and full notes more mechanically for high-volume collections. Ready for agent-memory-system reviews or source snapshots; broader use needs a migration path.

**Generated adapter files as compatibility surfaces.** Commonplace could generate tool-specific bootstrap files from canonical instructions without making those files authoritative. Ready if multiple host tools need slightly different entrypoints.

**Served/not-loaded observability.** Recording which artifacts were considered, loaded, omitted, and why would make Commonplace review bundles and agent sessions easier to audit. Ready for commands that already assemble bounded context.

**Optimization suggestions as pending records.** AI-Context-OS keeps maintenance advice as reviewable records instead of silently rewriting memory. Commonplace could use the same pattern for stale notes, oversized summaries, near-duplicate artifacts, and underused but repeatedly matched notes. Ready where deterministic evidence is available.

**Use deterministic scoring before embeddings.** The code gets useful ranking signals from frontmatter, lexical match, graph links, recency, importance, and usage. Commonplace should exhaust those inspectable signals before adding opaque ranking. Ready as a design constraint.

## Write side

**Write agency:** `manual` `automatic` — Users and agents can create/update/delete Markdown memories through the UI and MCP `save_memory`; the system also writes generated router/adapters, usage counters, context telemetry, inbox proposals, daily/session logs, and optimization suggestion records.

**Curation operations:** `synthesize` — Automatic proposal and optimization paths create new derived records about what should be promoted, compressed, archived, merged, or reweighted. The inspected code does not automatically perform those edits on canonical memories; consolidation, decay, deduplication, and promotion mostly appear as suggestions or user-mediated proposal application.

### Trace-derived learning

**Trace source:** `event-streams` `session-logs` — MCP context requests produce context-request, served-memory, and not-loaded rows; access recording updates `.cache/memory-usage.json`; MCP `log_session` and inbox/journal operations append JSONL operational events.

**Extraction.** Optimization analysis queries recent request/served/not-loaded traces plus the current memory store, then writes pending `OptimizationRecord` rows for compression, archival, importance promotion, L2 review, decayed-memory removal, merge candidates, and near-threshold memories. The oracle is deterministic heuristic evidence, not an LLM judge, and the curation policy stops at pending suggestions unless another UI action applies or dismisses them.

**Learning scope:** `per-project` — The traces and suggestions are rooted in one workspace.

**Learning timing:** `staged` — The trace store updates online during context serving, but optimization records are produced when `run_optimization_analysis` is invoked.

**Distilled form:** `prose` `symbolic` — Suggestions are symbolic records with typed fields plus prose descriptions, evidence, impact, and estimated token savings.

This is trace-derived learning, but a modest form: it learns maintenance pressure and ranking/summary hygiene from usage traces. It does not distill full agent transcripts into new rules, procedures, or validated memories.

## Read-back

**Read-back:** `both` — MCP `get_context`, `get_skill`, simulation, and preview commands are pull interfaces; generated adapter files and chat auto-assembly can put retained memory into an agent/model context without that receiving agent making a separate lookup.

**Read-back signal:** `coarse` `identifier` `inferred / lexical` — Generated adapter files provide coarse always-present router/index context; skill dependency loading follows `requires` and `optional` identifiers once a skill is selected; query-time read-back uses lexical BM25, tag/L0/ontology heuristics, graph proximity, recency, importance, and access frequency rather than embeddings or LLM relevance judgment.

**Faithfulness tested:** `no` — The code logs and displays what was served, but it does not run with/without ablations or post-answer audits to prove the model used the injected memory faithfully.

MCP read-back returns a Markdown package with workspace rules, loaded L1/L2 memories, and unloaded L0 candidates. Chat read-back injects `context_prompt` as an extra user message before the conversation for OpenAI-compatible and Anthropic providers; if the frontend omits context while vault context is enabled, the backend re-runs `execute_context_query` on the latest user message and assembles context before provider invocation ([src-tauri/src/commands/scoring.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/commands/scoring.rs), [src-tauri/src/commands/inbox.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/commands/inbox.rs)). Effective precision, recall, and context dilution are not verified from code.

## Curiosity Pass

The README's "universal memory layer" framing is broader than the current integration depth. The inspected snapshot does have a universal core model and several adapters, but the README itself notes that bridge-tier connector flows are copy/handoff rather than full remote-native integration.

The system calls its heuristic tag/L0/ontology score "semantic"; the implementation is deliberately interpretable and embedding-free. That is a strength for governance and local-first operation, but it should not be read as neural semantic retrieval.

The generated `claude.md` path is both a compatibility win and a potential authority hazard. It is a derived file that tells agents how to read and write the workspace; if edited manually, the code will overwrite it, so any durable policy belongs in canonical memories or app code.

Trace-derived optimization is promising but conservative. The system notices usage patterns and writes pending suggestions; it does not close the loop by editing summaries, changing importance, merging notes, or deleting decayed memory automatically. That restraint is probably correct for an inspectable local memory app.

## What to Watch

- Whether optimization suggestions gain concrete apply handlers that rewrite canonical memories; that would change the write-side curation classification from suggestion synthesis toward promote, consolidate, dedup, or decay.
- Whether chat-context observability reaches parity with MCP in the implemented path; the architecture doc calls out asymmetry, and the code logs structured observability for MCP but not the auto-assembled chat fallback.
- Whether embeddings or provider-based relevance judgment are added; that would change read-back signal classification and the trust story around deterministic ranking.
- Whether adapter integrations move from generated files and copy/handoff flows to live host hooks; that would strengthen the push side and raise harder faithfulness questions.
- Whether folder contracts become enforced gates rather than warnings; that would make governance more Commonplace-like.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes AI-Context-OS's file store from the MCP/chat/generated-adapter paths that actually serve memory into context.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - supports separating Markdown memories, generated adapters, scoring records, observability rows, and proposals by substrate, form, lineage, and authority.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - describes the authority carried by generated routers, rules, MCP tools, scoring policy, and validation checks.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - describes the evidence/context role of ordinary Markdown memories, sources, journal entries, and observability records.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - frames AI-Context-OS's usage-derived optimization suggestions as a modest trace-derived loop rather than transcript-to-rule learning.
