---
description: "Signet AI review: local-first daemon memory with SQLite, FTS/vector/graph recall, hook injection, transcript lineage, and guarded repair paths"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-learning]
last-checked: "2026-06-05"
---

# Signet AI

Signet AI, from `Signet-AI/signetai`, is a local-first context layer for agent harnesses. At the reviewed commit it ships a Rust daemon workspace plus TypeScript surfaces, a SQLite memory store, FTS/vector/graph recall, session hooks, MCP tools, filesystem connectors, transcript and compaction lineage, repair APIs, and several partly staged autonomous memory paths. The current native daemon is the most important implementation surface: it owns HTTP routes, MCP tools, the Rust memory pipeline, scoped multi-agent reads and writes, and lifecycle hooks for harnesses.

**Repository:** https://github.com/Signet-AI/signetai

**Reviewed commit:** [9e8909e7d210644caad27bf88c603cf322b6fb12](https://github.com/Signet-AI/signetai/commit/9e8909e7d210644caad27bf88c603cf322b6fb12)

**Last checked:** 2026-06-05

## Core Ideas

**Local-first custody is the product boundary.** The README frames Signet as an owned memory layer: SQLite database, readable workspace files, transcripts, source records, identity files, dashboard, daemon APIs, MCP, SDK, and harness integrations ([README.md](https://github.com/Signet-AI/signetai/blob/9e8909e7d210644caad27bf88c603cf322b6fb12/README.md)). The Rust service installer resolves `$SIGNET_PATH`/`~/.agents`, writes user-level systemd or launchd units, and runs the same local daemon binary rather than routing memory through a hosted API ([service.rs](https://github.com/Signet-AI/signetai/blob/9e8909e7d210644caad27bf88c603cf322b6fb12/platform/daemon-rs/crates/signet-daemon/src/service.rs)).

**The standing memory substrate is SQLite plus search indexes, not just a vector store.** Memory rows carry content, type, confidence, source fields, tags, project/session lineage, content hashes, versions, deletion state, pinning, importance, access counts, agent scope, visibility, and optional embeddings ([types.rs](https://github.com/Signet-AI/signetai/blob/9e8909e7d210644caad27bf88c603cf322b6fb12/platform/daemon-rs/crates/signet-core/src/types.rs), [memory.rs](https://github.com/Signet-AI/signetai/blob/9e8909e7d210644caad27bf88c603cf322b6fb12/platform/daemon-rs/crates/signet-core/src/queries/memory.rs)). FTS5 triggers and sqlite-vec tables provide access structures; graph and entity tables extend the semantic layer through later migrations ([001-baseline.sql](https://github.com/Signet-AI/signetai/blob/9e8909e7d210644caad27bf88c603cf322b6fb12/platform/daemon-rs/crates/signet-core/src/sql/001-baseline.sql)).

**Read-back is split between explicit tools and hook-time injection.** MCP exposes `memory_search`, `memory_store`, `memory_modify`, `memory_forget`, feedback, graph expansion, and cross-agent tools ([tools.rs](https://github.com/Signet-AI/signetai/blob/9e8909e7d210644caad27bf88c603cf322b6fb12/platform/daemon-rs/crates/signet-daemon/src/mcp/tools.rs)). Hook routes can inject a system prompt at session start, recover recent project/session context, and inject compact entity/aspect context before a user prompt when known entities or aliases match and attribute scoring clears the gate ([hooks.rs](https://github.com/Signet-AI/signetai/blob/9e8909e7d210644caad27bf88c603cf322b6fb12/platform/daemon-rs/crates/signet-daemon/src/routes/hooks.rs)).

**Context efficiency is gating before loading.** Pull recall has explicit limits, FTS sanitization, vector/keyword score merging, optional rehearsal and graph boosts, filters by agent/project/scope/type/tags/time, and access tracking ([search.rs](https://github.com/Signet-AI/signetai/blob/9e8909e7d210644caad27bf88c603cf322b6fb12/platform/daemon-rs/crates/signet-core/src/search.rs)). Push recall is narrower: prompt-submit first detects known entities/aliases, then selects current structured attributes by lexical and optional embedding signals and caps the injected block ([hooks.rs](https://github.com/Signet-AI/signetai/blob/9e8909e7d210644caad27bf88c603cf322b6fb12/platform/daemon-rs/crates/signet-daemon/src/routes/hooks.rs)). This is a context-engineering choice: Signet avoids generic per-turn vector injection and mostly pushes structured current context only when a symbol is available.

**The write path is raw-first, then optionally curated.** Explicit remember calls insert normalized, deduplicated memories and history rows, optionally chunk long content, upsert embeddings, persist structured payloads, and queue extraction jobs unless the extraction path is blocked ([write.rs](https://github.com/Signet-AI/signetai/blob/9e8909e7d210644caad27bf88c603cf322b6fb12/platform/daemon-rs/crates/signet-daemon/src/routes/write.rs), [transactions.rs](https://github.com/Signet-AI/signetai/blob/9e8909e7d210644caad27bf88c603cf322b6fb12/platform/daemon-rs/crates/signet-services/src/transactions.rs), [memory_embeddings.rs](https://github.com/Signet-AI/signetai/blob/9e8909e7d210644caad27bf88c603cf322b6fb12/platform/daemon-rs/crates/signet-daemon/src/routes/memory_embeddings.rs)). Hook session-end and compaction-complete preserve canonical transcript/summary artifacts before or alongside DB memories, making source lineage an explicit part of the system rather than an afterthought ([hooks.rs](https://github.com/Signet-AI/signetai/blob/9e8909e7d210644caad27bf88c603cf322b6fb12/platform/daemon-rs/crates/signet-daemon/src/routes/hooks.rs)).

**Some autonomous memory claims are implemented as stages, not full mutation loops.** The Rust pipeline extracts facts and entities with an LLM, runs decision proposals, applies a write gate, persists extracted entities, and marks extraction complete ([worker.rs](https://github.com/Signet-AI/signetai/blob/9e8909e7d210644caad27bf88c603cf322b6fb12/platform/daemon-rs/crates/signet-pipeline/src/worker.rs), [extraction.rs](https://github.com/Signet-AI/signetai/blob/9e8909e7d210644caad27bf88c603cf322b6fb12/platform/daemon-rs/crates/signet-pipeline/src/extraction.rs), [decision.rs](https://github.com/Signet-AI/signetai/blob/9e8909e7d210644caad27bf88c603cf322b6fb12/platform/daemon-rs/crates/signet-pipeline/src/decision.rs), [write_gate.rs](https://github.com/Signet-AI/signetai/blob/9e8909e7d210644caad27bf88c603cf322b6fb12/platform/daemon-rs/crates/signet-pipeline/src/write_gate.rs)). I did not find the native worker inserting ADD proposals as new memories in that path; it counts gate-passing proposals and writes graph entities. This is a material divergence from the broader documentation's "controlled writes" language ([docs/PIPELINE.md](https://github.com/Signet-AI/signetai/blob/9e8909e7d210644caad27bf88c603cf322b6fb12/docs/PIPELINE.md)).

## Artifact analysis

- **Storage substrate:** `sqlite` `files` `graph` `vector` `service-object` — The active substrate is SQLite tables for memories, history, jobs, entities, attributes, documents, connectors, transcripts, sessions, and auth; workspace files hold canonical transcripts, projections, identity/instruction documents, and harness config; graph tables and sqlite-vec/embedding rows provide structured and parametric access; daemon services and hooks are the live consumption surface.
- **Representational form:** `prose` `symbolic` `parametric` — Memories, transcripts, summaries, source documents, reflection answers, prompts, and MEMORY.md projections are prose; memory metadata, types, tags, scopes, visibility, agents, jobs, entity/aspect/attribute rows, connector configs, hook payloads, and MCP schemas are symbolic; embeddings and vector distances are parametric retrieval structures.
- **Lineage:** `authored` `imported` `trace-extracted` — Humans, agents, APIs, MCP tools, and hooks author memories and repairs; filesystem connectors import files into document rows and document-ingest jobs; session transcripts, compaction summaries, checkpoint deltas, LLM-extracted facts/entities, reflection answers, and dream promotions derive from agent traces or prior memories.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — Memory rows and documents advise as knowledge; session-start prompt text, MEMORY.md projections, skills, and hook injections instruct; auth, scope, visibility, mutation freeze, soft-delete, pinning, confirmation, and version checks enforce; agent/project/scope/entity/connector/session IDs route; schemas, extraction parsing, contradiction/write gates, and repair checks validate; FTS/vector/graph/rehearsal scores rank; extraction, summary, dream, feedback, and promotion paths learn from traces.

**Memory rows and history.** The central behavior-shaping record is the `memories` row plus `memory_history`. Inserts normalize and hash content, deduplicate within agent/scope/visibility, record source metadata, and write a creation event ([transactions.rs](https://github.com/Signet-AI/signetai/blob/9e8909e7d210644caad27bf88c603cf322b6fb12/platform/daemon-rs/crates/signet-services/src/transactions.rs)). Modify, forget, and recover paths are versioned and auditable, with pinned-memory protections on delete ([memory.rs](https://github.com/Signet-AI/signetai/blob/9e8909e7d210644caad27bf88c603cf322b6fb12/platform/daemon-rs/crates/signet-core/src/queries/memory.rs)).

**Search and recall indexes.** FTS5, embeddings, sqlite-vec, entity links, graph traversal, and access counters are access structures over the memory rows. They have ranking authority but should not be confused with the source of truth. Recall can degrade when vector or graph paths are absent because keyword search still works ([search.rs](https://github.com/Signet-AI/signetai/blob/9e8909e7d210644caad27bf88c603cf322b6fb12/platform/daemon-rs/crates/signet-core/src/search.rs)).

**Session lineage artifacts.** Session-end writes transcript audits and canonical transcript artifacts, normalizes transcript content for summary jobs, and can enqueue session summary work when the pipeline is enabled ([hooks.rs](https://github.com/Signet-AI/signetai/blob/9e8909e7d210644caad27bf88c603cf322b6fb12/platform/daemon-rs/crates/signet-daemon/src/routes/hooks.rs)). Compaction-complete writes a compaction artifact first, then ingests a `session_summary` memory and updates the temporal head/projection ([hooks.rs](https://github.com/Signet-AI/signetai/blob/9e8909e7d210644caad27bf88c603cf322b6fb12/platform/daemon-rs/crates/signet-daemon/src/routes/hooks.rs)). These traces are not merely logs; they become read-back and distillation inputs.

**Pipeline proposals and graph writes.** The native worker leases `memory_jobs`, runs significance gating, extraction, decision, write gating, entity persistence, and extraction status updates ([worker.rs](https://github.com/Signet-AI/signetai/blob/9e8909e7d210644caad27bf88c603cf322b6fb12/platform/daemon-rs/crates/signet-pipeline/src/worker.rs)). The implemented durable effect visible in that worker is graph/entity persistence and extraction state; ADD/UPDATE/DELETE decision proposals are not directly applied there in the inspected code. The proposal machinery still matters as a policy surface, but its authority is partly latent unless another route applies it.

**Structured graph and epistemic assertions.** Entity, aspect, attribute, dependency, and epistemic assertion tables give Signet a structured current-knowledge layer that prompt-submit can push by entity/aspect path ([051-epistemic-assertions.sql](https://github.com/Signet-AI/signetai/blob/9e8909e7d210644caad27bf88c603cf322b6fb12/platform/daemon-rs/crates/signet-core/src/sql/051-epistemic-assertions.sql), [hooks.rs](https://github.com/Signet-AI/signetai/blob/9e8909e7d210644caad27bf88c603cf322b6fb12/platform/daemon-rs/crates/signet-daemon/src/routes/hooks.rs)). Dream promotion can mechanically convert high-confidence preference memories into structured attributes, superseding earlier active attributes in the same claim slot ([dream.rs](https://github.com/Signet-AI/signetai/blob/9e8909e7d210644caad27bf88c603cf322b6fb12/platform/daemon-rs/crates/signet-daemon/src/routes/dream.rs)).

**Connector documents.** The Rust filesystem connector registers connector rows, walks allowed files, filters by glob/ignore/max-size, writes `documents` rows, and enqueues `document_ingest` jobs ([connectors.rs](https://github.com/Signet-AI/signetai/blob/9e8909e7d210644caad27bf88c603cf322b6fb12/platform/daemon-rs/crates/signet-daemon/src/routes/connectors.rs)). `github-docs` and `gdrive` are accepted provider names at registration but return "not yet supported" on sync in the native route.

Promotion path: Signet has several paths from weak to stronger authority: raw hook/API memory -> extracted graph/entity structure -> prompt-submit injected entity context; session transcript -> compaction/session summary memory -> MEMORY.md projection; high-confidence preference memory -> dream-promoted structured attribute; repaired memory -> versioned history plus fresh embedding. The missing piece is a fully closed native loop from extraction decision proposal to durable fact update.

## Comparison with Our System

| Dimension | Signet AI | Commonplace |
|---|---|---|
| Primary purpose | Runtime memory/context infrastructure under many harnesses | Git-native methodology KB for agents and maintainers |
| Canonical artifact | SQLite rows plus workspace files and daemon state | Typed Markdown artifacts, source snapshots, indexes, validation reports |
| Read-back | Both: explicit MCP/CLI/API recall plus hook-time injection | Mostly pull through search, indexes, links, and loaded instructions |
| Write path | API/MCP/hooks, transcripts, compactions, connectors, repair, pipeline workers | Authored Markdown, snapshots, reviews, validation, review gates |
| Governance | Auth/scopes, visibility, history, soft delete/recover, write gates, mutation freeze | Collection contracts, type specs, deterministic validation, semantic review, git diff |

Signet is stronger where Commonplace deliberately does little: it owns a live daemon, lifecycle hooks, multi-agent scoping, MCP tools, connector sync, retrieval ranking, and runtime push context. Commonplace is stronger where inspectability and durable argument quality matter: the main artifacts are plain Markdown under git with explicit type contracts and validation. Signet can get context into an agent before it asks; Commonplace usually requires the agent to search or load the relevant artifact.

The deepest design difference is authority. Signet lets runtime state become prompt context or structured entity context with service-level policy. That is useful for continuity, but it makes runtime faithfulness, stale-context repair, and provenance enforcement central concerns. Commonplace delays authority by forcing durable notes and instructions through collection contracts and validation. Signet's repair APIs are closer to Commonplace than most memory systems because edits, soft deletes, recoveries, reasons, and history are first-class.

### Borrowable Ideas

**Entity-gated prompt-submit injection.** Ready as a workshop experiment. Commonplace could test a tiny hook that injects only structured current context when a prompt names a known project/artifact/entity and an authored index confirms the relation.

**Raw-first transcript lineage before summaries.** Ready now as a convention. Signet's "canonical artifact before summary/ingest" discipline maps well to Commonplace source snapshots: preserve the trace, then derive reviewable notes.

**Repair APIs as ordinary memory operations.** Ready as vocabulary. Commonplace already has validation/review gates; Signet's modify/forget/recover model suggests a clearer "repair event" record for note revisions and source invalidation.

**Dream promotion should stay gated.** Needs a concrete Commonplace use case. Promoting high-confidence preference-like memories into structured attributes is useful, but Commonplace should land those as review candidates or workshop artifacts before they affect instructions.

**Do not borrow silent runtime state as library authority.** Signet's hook injection is appropriate for a runtime memory product. Commonplace should keep durable methodology claims in files, with hook-like injection only for low-risk navigation or session continuity.

## Write side

**Write agency:** `manual` `automatic` — Users, agents, MCP clients, APIs, dashboard/repair paths, and connectors can create, modify, forget, recover, and import memories; automatic paths capture session transcripts, ingest compaction summaries, enqueue extraction/document jobs, persist extracted graph entities, update access counts/feedback, apply retention, and mechanically promote some preferences through the dream route.

**Curation operations:** `dedup` `evolve` `invalidate` `decay` `promote` — Content hashes deduplicate scoped memories and chunks; modify/repair and dream promotion can update or supersede existing memory/attribute state; forget soft-deletes and recover/hard-delete retention implement invalidation; rehearsal/importance/retention paths downweight or purge stale state; dream promotion converts high-confidence prose preferences into structured attributes. The native extraction worker has a write gate for candidate facts, but I did not find it inserting gated ADD proposals into `memories`.

### Trace-learning

**Trace source:** `session-logs` `tool-traces` `event-streams` — Hook routes consume session starts, prompts, remembers, recalls, session ends, compactions, checkpoints, and transcripts; MCP feedback records relevance judgments; canonical transcript and compaction artifacts feed later summaries/projections.

**Learning scope:** `per-task` `per-project` `cross-task` — Session artifacts are per session/task, project keys and runtime paths scope continuity, and agent-scoped memories/structured attributes can affect later tasks for the same agent or shared policy.

**Learning timing:** `online` `staged` — Explicit remember/modify/forget and hook writes happen online around agent sessions; extraction jobs, document ingest, compaction artifacts, MEMORY.md projection, dream promotion, retention, and repair are staged background or operator-triggered paths.

**Distilled form:** `prose` `symbolic` `parametric` — Distilled outputs include prose memories, session summaries, reflection answers, MEMORY.md projections, structured entity/aspect/attribute rows, connector/document metadata, graph relations, memory hints in older/parallel docs, and embeddings for ranking.

**Extraction.** The Rust extraction stage asks an LLM for self-contained facts and entity relations, validates and caps outputs, strips fences and model think blocks, and filters by confidence ([extraction.rs](https://github.com/Signet-AI/signetai/blob/9e8909e7d210644caad27bf88c603cf322b6fb12/platform/daemon-rs/crates/signet-pipeline/src/extraction.rs)). The decision stage retrieves existing scoped candidates by BM25/vector, asks an LLM for ADD/UPDATE/DELETE/NONE proposals, and rejects hallucinated target IDs ([decision.rs](https://github.com/Signet-AI/signetai/blob/9e8909e7d210644caad27bf88c603cf322b6fb12/platform/daemon-rs/crates/signet-pipeline/src/decision.rs)). The write gate then measures novelty/surprisal when embeddings exist and bypasses for decisions, constraints, and errors ([write_gate.rs](https://github.com/Signet-AI/signetai/blob/9e8909e7d210644caad27bf88c603cf322b6fb12/platform/daemon-rs/crates/signet-pipeline/src/write_gate.rs)).

**Distillation trigger and policy.** Raw API/hook memories enqueue extraction jobs; session-end and compaction-complete write lineage artifacts and summary memory; checkpoint extraction handles long-lived sessions by transcript deltas; dream promotion can dry-run or apply preference-attribute operations from recent memories ([hooks.rs](https://github.com/Signet-AI/signetai/blob/9e8909e7d210644caad27bf88c603cf322b6fb12/platform/daemon-rs/crates/signet-daemon/src/routes/hooks.rs), [dream.rs](https://github.com/Signet-AI/signetai/blob/9e8909e7d210644caad27bf88c603cf322b6fb12/platform/daemon-rs/crates/signet-daemon/src/routes/dream.rs)). Reflection generation is disabled in the native route, but answering a reflection writes a new memory linked to the reflection row ([reflections.rs](https://github.com/Signet-AI/signetai/blob/9e8909e7d210644caad27bf88c603cf322b6fb12/platform/daemon-rs/crates/signet-daemon/src/routes/reflections.rs)).

**Survey placement.** Signet belongs in the trace-to-runtime-memory family, with stronger lineage and repair affordances than simple chat memory. It also exposes a useful caution for the survey: docs may describe a full controlled-write loop while the current native worker only implements some stages. The reviewable distinction is raw trace retention, derived graph/summary artifacts, and actual mutation authority.

## Read-back

**Read-back:** `both` — Agents can pull memories through CLI/API/MCP recall, graph expansion, session search, and list/get tools; hooks can push retained session recovery and structured entity/aspect context into the prompt before the agent acts.

**Read-back signal:** `identifier` `inferred / lexical` `inferred / embedding` — Push context is selected by session/project/agent/entity/alias identifiers, lexical overlap between prompt terms and structured attributes, and optional embedding scores against linked memory content. Pull recall separately uses FTS, vector, graph, filters, and explicit query text.

**Faithfulness tested:** `no` — The repo has many route and behavior tests for hook selection, memory writes, session lineage, embeddings, connector sync, and pipeline mechanics, but I did not find a with/without injected-memory ablation or post-action audit proving that pushed context changed agent behavior faithfully.

**Direction edge cases.** The always-injected Signet "memory active" prompt and Memory Check Loop are baseline instructions, not retained memory read-back. The retained push path is the project/session recovery and entity-context injection that comes from stored session and graph state. Prompt-submit does not run broad recall when there is no known entity or no gated attribute match; it returns empty injection, leaving explicit recall as the pull path.

**Targeting and signal.** Session-start recovery is scoped by session/project identity. Prompt-submit requires a known entity or alias in the user prompt, filters generic/role-like entity phrases, selects at most a small number of entities and aspects, and emits up to a capped number of lines. The actual content selection combines identifier availability with lexical and optional embedding relevance.

**Injection point.** Hook read-back is pre-invocation: session-start before a new session and user-prompt-submit before a user turn reaches the model. Session-end, compaction-complete, checkpoint extraction, connector sync, retention, and dream promotion are write-side maintenance; their outputs affect later reads.

**Selection, scope, and complexity.** Pull recall has limit clamps, top-k search, min-score filters, scope/project/agent visibility, type/tag/who/pinned/time filters, and fallback behavior. Push entity context caps injected characters and selected lines. Effective context dilution is not proven from code, but the design is explicitly bounded and avoids unfiltered vector snippets on every prompt.

**Authority at consumption.** Hook-injected context is advisory/instructional prompt context. MCP and API recall results are tool outputs the agent must choose to use. Structured attributes can become stronger than ordinary snippets because the hook emits them as current entity context, but the repo does not test whether the receiving agent follows them.

**Other consumers.** Humans consume the same state through the dashboard, CLI, API, history routes, connector health, repair endpoints, reflection routes, and source/session artifact files. Background workers, MCP tools, graph expansion, retention, and dream promotion are non-agent consumers of the memory store.

## Curiosity Pass

**The native daemon is ahead of a simple memory API and behind parts of its own docs.** It has serious infrastructure: auth, hooks, MCP, scoping, repair, transcript lineage, connectors, graph tables, and staging workers. But the native extraction worker's ADD proposal path appears not to create new memory rows yet.

**Prompt-submit is a symbol-availability bet.** The push path is strong when the prompt names a known entity or alias and the graph has current attributes. It deliberately does little for prompts that are semantically related but lack a usable symbol.

**Connector behavior is narrower than the provider vocabulary.** Filesystem sync is implemented in Rust. `github-docs` and `gdrive` are accepted provider names but return unsupported on sync, so they are configuration vocabulary rather than implemented import behavior in the native daemon.

**Repairability is the most borrowable product idea.** Signet treats bad memory as normal operational state: modify, forget, recover, history, duplicate checks, confirmation tokens, pinned-memory protections, and mutation freezes are not bolted-on review features.

**Dreaming is partly a route, partly an aspiration.** The native dream status says the worker is not running, but dream promotion can still mechanically promote high-confidence preference memories into structured attribute slots. That is useful, but narrower than a general autonomous graph-consolidation agent.

## What to Watch

- Whether the Rust extraction worker starts applying ADD/UPDATE/DELETE proposals to durable memories through `transactions::ingest`, `modify`, and `forget`. That would materially strengthen the write-side `evolve`/`invalidate` claim.
- Whether the native dream worker becomes active rather than reporting "Dreaming worker not running"; that would move graph consolidation from route-level promotion to scheduled autonomous curation.
- Whether `github-docs` and `gdrive` connector syncs become implemented in the native daemon. That would expand imported lineage beyond local filesystem documents.
- Whether prompt-submit gains behavioral faithfulness tests or runtime audits for injected entity context. That would make the push read-back claim stronger than structural injection.
- Whether extraction decisions and write-gate outcomes are persisted as first-class proposal/history rows in the Rust path. That would make blocked/skipped/generated facts inspectable enough for repair workflows.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Signet combines pull recall with hook-time pushed retained context.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Signet's memory rows, files, graph attributes, embeddings, jobs, hooks, and connectors differ by substrate, form, lineage, and authority.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - applies: Signet derives summaries, graph structure, and candidate facts from session and memory traces.
- [Symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - explains: Signet's prompt-submit push works when known entities or aliases are present.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: memory rows, documents, transcripts, summaries, and recall results mostly advise as evidence/context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: hooks, MCP schemas, auth/scoping policies, write gates, connector configs, and generated harness instructions shape behavior with stronger authority.
- [Lineage](../../notes/definitions/lineage.md) - frames: Signet's source-backed recall, transcript artifacts, memory history, and compaction lineage.
