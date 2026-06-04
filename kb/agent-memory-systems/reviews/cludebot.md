---
description: "Clude review: cognitive memory SDK and MCP server with SQLite/Supabase stores, hybrid recall, dream-cycle synthesis, memory packs, and prompt-file push surfaces"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
status: current
last-checked: "2026-06-04"
---

# Clude

Clude, by sebbsssss, is a TypeScript memory engine, MCP server, hosted Cortex API, and autonomous Cludebot codebase. At the reviewed commit it stores typed memories, summaries, tags, concepts, embeddings, links, decay state, owner scope, provenance, and dream logs; serves recall through SDK, HTTP, MCP, CLI, and dashboard routes; and uses dream/action-learning loops to turn stored episodes and action outcomes into semantic, procedural, and self-model memories.

**Repository:** https://github.com/sebbsssss/cludebot

**Reviewed commit:** [e4df0881b88223699930147631db3660d5c1f4e7](https://github.com/sebbsssss/cludebot/commit/e4df0881b88223699930147631db3660d5c1f4e7)

**Last checked:** 2026-06-04

## Core Ideas

**The product boundary is broader than one store.** The README presents Clude as a memory SDK plus hosted, self-hosted, local, dashboard, CLI, MCP, and Cludebot surfaces; the package manifest publishes `@clude/sdk` with CLI, MCP, Supabase, SQLite, embeddings, Solana, and model-provider dependencies ([README.md](https://github.com/sebbsssss/cludebot/blob/e4df0881b88223699930147631db3660d5c1f4e7/README.md), [package.json](https://github.com/sebbsssss/cludebot/blob/e4df0881b88223699930147631db3660d5c1f4e7/package.json)). That makes the system a memory platform rather than only an embedded library.

**Memory units are typed records with differential persistence.** The core `Memory` model records `episodic`, `semantic`, `procedural`, `self_model`, and `introspective` memories with content, summary, tags, concepts, source fields, related user/wallet fields, evidence ids, decay factor, hash ids, compaction markers, encryption/delegation state, and access counters ([packages/brain/src/memory/memory.ts](https://github.com/sebbsssss/cludebot/blob/e4df0881b88223699930147631db3660d5c1f4e7/packages/brain/src/memory/memory.ts), [packages/database/supabase-schema.sql](https://github.com/sebbsssss/cludebot/blob/e4df0881b88223699930147631db3660d5c1f4e7/packages/database/supabase-schema.sql)). Type-specific decay and reinforcement make the stored row itself a living ranking object, not just an immutable note.

**Read efficiency is explicitly engineered through staged retrieval.** Full Supabase recall expands queries, runs memory-level and fragment-level vector search, BM25, metadata filters, knowledge seeds, entity expansion, bond traversal, type diversity, owner guards, and access reinforcement before returning top-k memories; summary recall and hydration provide a progressive-disclosure path ([packages/brain/src/memory/memory.ts](https://github.com/sebbsssss/cludebot/blob/e4df0881b88223699930147631db3660d5c1f4e7/packages/brain/src/memory/memory.ts)). The local SQLite path is smaller but still scores by similarity, importance, recency, and decay, with `sqlite-vec` fallback to keyword ranking ([packages/brain/src/storage/sqlite-store.ts](https://github.com/sebbsssss/cludebot/blob/e4df0881b88223699930147631db3660d5c1f4e7/packages/brain/src/storage/sqlite-store.ts)).

**Automatic curation is centered on dream cycles.** `Cortex.dream()` and `startDreamSchedule()` wire to a cycle that consolidates recent episodic memories, compacts old faded episodes, reflects into self-model memories, resolves contradictions, runs action-learning, predicts deep links, and stores an emergence thought ([packages/brain/src/sdk/cortex.ts](https://github.com/sebbsssss/cludebot/blob/e4df0881b88223699930147631db3660d5c1f4e7/packages/brain/src/sdk/cortex.ts), [packages/brain/src/memory/dream/cycle.ts](https://github.com/sebbsssss/cludebot/blob/e4df0881b88223699930147631db3660d5c1f4e7/packages/brain/src/memory/dream/cycle.ts)). The hosted worker runs a lighter scheduled consolidation/procedural path per active agent ([packages/brain/src/memory/hosted-dreams.ts](https://github.com/sebbsssss/cludebot/blob/e4df0881b88223699930147631db3660d5c1f4e7/packages/brain/src/memory/hosted-dreams.ts)).

**Adoption happens through MCP tools, prompt-file generation, and instruction injection.** The MCP server exposes recall, store, stats, clinamen, delete, update, list, and skill-extraction surfaces across SQLite, hosted, self-hosted, and JSON-local modes ([packages/brain/src/mcp/server.ts](https://github.com/sebbsssss/cludebot/blob/e4df0881b88223699930147631db3660d5c1f4e7/packages/brain/src/mcp/server.ts)). Setup and injection commands add host instructions telling agents to recall at session start and store learned information, while `sync` and `export` can render selected memories into ChatGPT/Gemini-style prompt files ([packages/brain/src/cli/setup.ts](https://github.com/sebbsssss/cludebot/blob/e4df0881b88223699930147631db3660d5c1f4e7/packages/brain/src/cli/setup.ts), [packages/brain/src/cli/sync.ts](https://github.com/sebbsssss/cludebot/blob/e4df0881b88223699930147631db3660d5c1f4e7/packages/brain/src/cli/sync.ts), [packages/brain/src/cli/export.ts](https://github.com/sebbsssss/cludebot/blob/e4df0881b88223699930147631db3660d5c1f4e7/packages/brain/src/cli/export.ts)).

**Trust is partly structural, partly claimed.** The code has owner scoping, encryption/delegation fields, revocation paths, MemoryPack signing/verification, content hashes, optional Solana anchoring, confidence-gate experiments, and route tests ([packages/brain/src/memory/memory-encryption.ts](https://github.com/sebbsssss/cludebot/blob/e4df0881b88223699930147631db3660d5c1f4e7/packages/brain/src/memory/memory-encryption.ts), [packages/brain/src/memory/memory-revoke.ts](https://github.com/sebbsssss/cludebot/blob/e4df0881b88223699930147631db3660d5c1f4e7/packages/brain/src/memory/memory-revoke.ts), [packages/memorypack/src/types.ts](https://github.com/sebbsssss/cludebot/blob/e4df0881b88223699930147631db3660d5c1f4e7/packages/memorypack/src/types.ts), [packages/brain/src/experimental/confidence-gate.ts](https://github.com/sebbsssss/cludebot/blob/e4df0881b88223699930147631db3660d5c1f4e7/packages/brain/src/experimental/confidence-gate.ts)). I did not verify the README's benchmark claims from source; the review treats them as product claims, not observed behavior.

## Artifact analysis

- **Storage substrate:** `sqlite` — The primary local MCP default creates `~/.clude/brain.db` through `SqliteStore`; secondary substrates include Supabase/Postgres + pgvector for self-hosted and hosted Cortex, `~/.clude/memories.json` for explicit JSON-local mode, generated prompt/export files, MemoryPack directories/tarballs, Solana anchors, dashboard/server service objects, and process-local embedding caches.
- **Representational form:** `prose` `symbolic` `parametric` — Memory content, summaries, prompt exports, dream outputs, and instructions are prose; types, tags, concepts, source fields, evidence ids, links, decay factors, schemas, MCP tool contracts, pack manifests, hashes, signatures, owner scope, and queue rows are symbolic; embeddings, vector indexes, optional rerankers, and JEPA-predicted links are parametric retrieval signals.
- **Lineage:** `authored` `imported` `trace-extracted` — SDK/MCP/CLI/API calls author memories directly; import commands and MemoryPack readers bring external memories into the store; dream cycles, action/outcome tracking, social-outcome tracking, compaction, reflection, contradiction resolution, procedural extraction, embeddings, links, and generated prompt files derive from stored traces or prior retained artifacts.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — Recalled records and dashboard views advise as knowledge; generated AGENTS/CLAUDE sections and prompt exports instruct host agents; schema checks, owner guards, encryption delegation, route validation, and revocation functions enforce or validate boundaries; recall pipelines, MCP schemas, graph traversal, and pack/topic categorization route access; scores, embeddings, decay, type boosts, and links rank memory; dream/action-learning loops update learned behavior.

**SQLite memory store.** Storage substrate: `~/.clude/brain.db` with `memories`, `links`, `dream_queue`, optional `memory_embeddings`, and schema-version tables. Representational form: symbolic rows plus prose content/summary and optional local vectors. Lineage: authored by MCP `store_memory` and maintained by update/delete/list/recall calls. Behavioral authority: knowledge and ranking for MCP recall; queue rows are learning inputs, but the SQLite implementation exposes queue primitives more than a full local dream worker ([packages/brain/src/storage/schema.ts](https://github.com/sebbsssss/cludebot/blob/e4df0881b88223699930147631db3660d5c1f4e7/packages/brain/src/storage/schema.ts), [packages/brain/src/storage/sqlite-store.ts](https://github.com/sebbsssss/cludebot/blob/e4df0881b88223699930147631db3660d5c1f4e7/packages/brain/src/storage/sqlite-store.ts)).

**Supabase Cortex store.** Storage substrate: Postgres tables and RPCs for memories, fragments, links, dream logs, entity graph, encryption keys/wraps, agent keys, rate limits, and indexes. Representational form: prose records plus symbolic schema and parametric pgvector embeddings. Lineage: authored through SDK/API/MCP routes, imported through CLI/MemoryPack flows, and trace-extracted through dream/action loops. Behavioral authority: knowledge, routing, ranking, learning, validation, and owner-isolation enforcement ([packages/database/supabase-schema.sql](https://github.com/sebbsssss/cludebot/blob/e4df0881b88223699930147631db3660d5c1f4e7/packages/database/supabase-schema.sql), [packages/shared/src/core/database.ts](https://github.com/sebbsssss/cludebot/blob/e4df0881b88223699930147631db3660d5c1f4e7/packages/shared/src/core/database.ts)).

**Memory records and fragments.** Storage substrate: database rows in `memories` and `memory_fragments`. Representational form: prose `content`/`summary`, symbolic metadata and provenance, and parametric embeddings. Lineage: authored or imported at write time; fragments, content tokens, concept tags, semantic pack tags, content hashes, Solana signatures, and links are derived views of the same memory. Behavioral authority: knowledge when recalled, ranking through decay/importance/access/embedding scores, learning input for dream cycles, and sometimes instruction when exported into prompt files ([packages/brain/src/memory/memory.ts](https://github.com/sebbsssss/cludebot/blob/e4df0881b88223699930147631db3660d5c1f4e7/packages/brain/src/memory/memory.ts)).

**Dream logs and distilled memories.** Storage substrate: `dream_logs` plus new memory rows with sources such as `consolidation`, `compaction`, `reflection`, `contradiction_resolution`, `strategy_refiner`, and `emergence`. Representational form: prose syntheses inside symbolic provenance fields and links. Lineage: trace-extracted from prior episodic, semantic, action, outcome, and self-model memories. Behavioral authority: knowledge and learning immediately; procedural and self-model outputs can become stronger instruction-like material when recalled or exported ([packages/brain/src/memory/dream/cycle.ts](https://github.com/sebbsssss/cludebot/blob/e4df0881b88223699930147631db3660d5c1f4e7/packages/brain/src/memory/dream/cycle.ts), [packages/brain/src/memory/action-learning.ts](https://github.com/sebbsssss/cludebot/blob/e4df0881b88223699930147631db3660d5c1f4e7/packages/brain/src/memory/action-learning.ts)).

**MCP and SDK interfaces.** Storage substrate: repository code plus host MCP config entries; runtime state lives in whichever memory backend the mode selects. Representational form: symbolic tool schemas and TypeScript APIs plus prose tool descriptions. Lineage: authored integration surface. Behavioral authority: routing and instruction affordances; tools do not push recalled memory by themselves, but host instructions can require agents to call them ([packages/brain/src/mcp/server.ts](https://github.com/sebbsssss/cludebot/blob/e4df0881b88223699930147631db3660d5c1f4e7/packages/brain/src/mcp/server.ts), [packages/brain/src/sdk/cortex.ts](https://github.com/sebbsssss/cludebot/blob/e4df0881b88223699930147631db3660d5c1f4e7/packages/brain/src/sdk/cortex.ts)).

**Prompt and instruction exports.** Storage substrate: generated `CLAUDE.md`/`AGENTS.md` sections and prompt files such as `clude-prompt.txt`. Representational form: prose instructions and selected memory summaries grouped by type. Lineage: derived from existing memories and setup templates. Behavioral authority: instruction and push read-back when the host always loads the generated file, but lineage can drift because the prompt file is a compiled view rather than the source store ([packages/brain/src/cli/setup.ts](https://github.com/sebbsssss/cludebot/blob/e4df0881b88223699930147631db3660d5c1f4e7/packages/brain/src/cli/setup.ts), [packages/brain/src/cli/sync.ts](https://github.com/sebbsssss/cludebot/blob/e4df0881b88223699930147631db3660d5c1f4e7/packages/brain/src/cli/sync.ts), [packages/brain/src/cli/export.ts](https://github.com/sebbsssss/cludebot/blob/e4df0881b88223699930147631db3660d5c1f4e7/packages/brain/src/cli/export.ts)).

**MemoryPack artifacts.** Storage substrate: directory or `.tar.zst` packs with manifest, JSONL records, signatures, anchors, revocations, revocation anchors, and blobs. Representational form: symbolic manifests/proofs and prose record content, with optional encrypted payloads and embeddings. Lineage: imported/exported snapshots of memory records. Behavioral authority: knowledge transfer and validation/audit, not live recall unless a runtime imports the pack ([packages/memorypack/README.md](https://github.com/sebbsssss/cludebot/blob/e4df0881b88223699930147631db3660d5c1f4e7/packages/memorypack/README.md), [packages/memorypack/src/types.ts](https://github.com/sebbsssss/cludebot/blob/e4df0881b88223699930147631db3660d5c1f4e7/packages/memorypack/src/types.ts), [packages/memorypack/src/reader.ts](https://github.com/sebbsssss/cludebot/blob/e4df0881b88223699930147631db3660d5c1f4e7/packages/memorypack/src/reader.ts), [packages/memorypack/src/writer.ts](https://github.com/sebbsssss/cludebot/blob/e4df0881b88223699930147631db3660d5c1f4e7/packages/memorypack/src/writer.ts)).

Promotion path: Clude has a strong trace-to-authority ladder. Raw authored/imported/interaction memories can become compacted semantic summaries, procedural lessons, self-model reflections, contradiction resolutions, strengthened links, decayed or compacted old episodes, MemoryPack exports, and always-loaded prompt text. The code has provenance fields and some structural checks, but it does not show a Commonplace-style semantic review gate before generated lessons or prompt exports affect later agents.

## Comparison with Our System

| Dimension | Clude | Commonplace |
|---|---|---|
| Primary purpose | Operational cognitive memory SDK/platform for agents and Cludebot | Git-native methodology KB for agent-operated knowledge bases |
| Canonical artifact | Typed memory row plus embeddings, links, decay, provenance, and generated views | Typed Markdown artifact plus citations, links, indexes, validation, and review state |
| Source of truth | SQLite/Supabase memory store, with prompt/export files as compiled views | Repository files; generated indexes/reports are derived |
| Write path | SDK/MCP/API/CLI writes, imports, dream cycles, action learning, compaction, contradiction resolution | Direct authored edits, snapshots, review workflows, validation, index refresh |
| Read-back | Pull recall/search plus optional prompt-file and always-loaded instruction push | Mostly explicit pull through search, indexes, links, skills, and loaded instructions |
| Governance | Schemas, owner scoping, encryption/revocation, confidence experiments, signatures, tests | Collection/type contracts, schema validation, git diff, semantic gates, review archives |

Clude is much more ambitious as an autonomous operational memory engine. It has automatic recall ranking, embeddings, decay, reinforcement, dream cycles, strategy learning, MCP tools, hosted onboarding, and export/import portability. Commonplace is much stronger as a reviewable knowledge base: durable claims live in readable files with collection contracts, citations, validation, and semantic review before they become high-authority artifacts.

The design tension is authority. Clude quickly turns traces into remembered behavior, and it offers convenience paths that push summaries into host prompt files. That is useful for agent continuity, but it gives generated memory a fast route to instruction-like force. Commonplace deliberately makes promotion slower because reviewability and source alignment matter more than adaptation speed in this repository.

### Borrowable Ideas

**Progressive disclosure as a first-class API.** Ready now. Commonplace already uses indexes before full files; Clude's explicit `recallSummaries()`/`hydrate()` split is a useful API shape for future machine-readable search layers.

**Treat prompt files as compiled memory views.** Ready as a constraint. If Commonplace emits assistant-specific memory surfaces, they should carry lineage to source artifacts and be regenerated, not hand-maintained as independent truth.

**Separate memory portability from runtime.** Ready now. MemoryPack shows a narrow portable artifact format can be useful without importing the whole memory engine; Commonplace source bundles could follow that pattern for external review exchange.

**Use decay and access reinforcement only for operational recall.** Needs a concrete use case. Clude's decay/access scoring is useful for agent memory, but Commonplace should not let recency or access frequency upgrade methodology truth.

**Automatic contradiction resolution needs review before authority.** Ready as a design warning. Clude's contradiction cycle is a useful candidate generator, but Commonplace should route such outputs into review/workshop state before they become instructions or durable claims.

## Write side

**Write agency:** `manual` `automatic` — Manual writes come from SDK, API, MCP, CLI, dashboard/import, and direct setup/export operations; automatic writes include embeddings, fragments, content tokens, semantic tags, Solana/content-hash metadata, links, access reinforcement, decay, dream logs, compacted memories, reflection/self-model memories, contradiction resolutions, procedural strategies, hosted dream outputs, and prompt-file regeneration.

**Curation operations:** `consolidate` `dedup` `evolve` `synthesize` `invalidate` `decay` `promote` — Dream consolidation and compaction create smaller higher-level memories; high-frequency `shiro_` writes are deduplicated; semantic tagging, access counts, link strengths, strategy importance, and memory updates evolve existing state; consolidation/reflection/action-learning synthesize new semantic/procedural/self-model entries; contradiction resolution marks weaker beliefs by accelerating decay and links a resolution; daily decay lowers retained salience; importance, access, knowledge-seed boosts, links, and prompt exports promote some memories into future context.

### Trace-derived learning

**Trace source:** `session-logs` `tool-traces` `event-streams` — Stored episodic memories, action records, outcome records, MCP/API writes, chat/user interactions, social engagement measurements, and event-bus `memory:stored` signals feed durable memory changes.

**Learning scope:** `per-project` `cross-task` — Local SQLite and JSON stores are user/machine scoped; hosted/self-hosted Cortex scopes by owner wallet/API key and supports cross-session, cross-agent, and dashboard/API use.

**Learning timing:** `online` `offline` `staged` — Store-time embeddings, tags, links, access reinforcement, event-triggered reflection, and MCP writes can happen online; local SQLite/JSON and MemoryPack operations can run offline; dream cycles, compaction, social-outcome tracking, prompt sync, import/export, and hosted workers are staged or scheduled.

**Distilled form:** `prose` `symbolic` `parametric` — Traces become prose summaries, semantic insights, procedural lessons, self-reflections, and prompt files; symbolic rows, tags, evidence ids, links, decay flags, hashes, signatures, and revocation states; and parametric embeddings/vector indexes used for later retrieval.

**Extraction.** The main extraction loop starts with stored memories rather than raw transcript files: events are first represented as episodic/action/outcome memory records, then dream phases query and transform those records into semantic, procedural, self-model, and contradiction-resolution memories. Evidence ids and links preserve some provenance, but the LLM-generated text itself is not semantically reviewed before insertion.

**Scope and timing.** The dream scheduler can run every six hours, trigger from accumulated episodic importance, and apply daily decay. Hosted dreams are lighter and agent-scoped; self-hosted dreams include fuller compaction, reflection, contradiction resolution, learning, deep connection, and emergence phases.

**Survey fit.** Clude strengthens the trace-derived survey's point that readable artifacts, symbolic metadata, and parametric retrieval often coexist. It also highlights a risk: generated procedural and self-model memories can be exported into prompt surfaces, so low-review trace extraction can become instruction-like authority through a compiled view.

## Read-back

**Read-back:** `both` — Most retained memory reaches agents by pull through SDK `recall`, MCP `recall_memories`, HTTP `/api/cortex/recall`, CLI status/export/import, dashboard routes, and direct MemoryPack reads, while generated AGENTS/CLAUDE instructions, `sync` prompt files, and repository-local required memory instructions can push retained memory or memory-use policy into host context without a fresh recall decision by the receiving model.

**Read-back signal:** `coarse` `inferred / lexical` `inferred / embedding` — Prompt files and injected instructions are coarse always-load/read-at-start surfaces; MCP/SDK recall uses inferred lexical and embedding signals when called; `sync` selects by type and importance/recency before writing the prompt surface.

**Faithfulness tested:** `no` — I found tests for storage, schema, retrieval mechanics, encryption, MCP/routes, proof routes, confidence scoring, and experimental retrieval pieces, but not a with/without behavioral ablation showing that pushed prompt-file memory or recalled memories reliably change agent behavior as intended.

**Direction edge cases.** MCP `recall_memories`, `find_clinamen`, SDK `recall`, `recallSummaries`, and dashboard/API browsing are pull from the agent or user perspective when explicitly called. A generated `AGENTS.md`, `CLAUDE.md`, or prompt file is push if the host loads it automatically. The setup-injected sentence "At the start of every session, call `recall_memories`" is a coarse pushed instruction to perform a later pull, not direct injection of all matching memories.

**Targeting and signal.** Runtime recall is instance-targeted when the caller supplies a query, tags, type filters, user/wallet filters, min-importance, or min-decay. Selection can be lexical, embedding-based, metadata-filtered, entity-aware, graph-expanded, type-diversified, or anomaly-oriented. Generated prompt exports are less targeted: they group by memory type and cap counts/words, then rely on the host context to carry the result.

**Injection point.** Pull recall returns before a model call only when an agent/tool/user asks for it and then chooses to include the result. `sync` writes a prompt file on demand or interval; the read-back happens later when a host includes that file in prompt assembly. Dream cycles, embedding writes, decay, compaction, link reinforcement, and strategy refinement are write-side maintenance for later reads.

**Selection, scope, and complexity.** Supabase recall has many controls: query expansion, vector thresholds, fragment search, BM25, metadata filters, top-k limits, min decay, owner guards, knowledge seeds, entity expansion, graph traversal, internal-source penalties, type diversity, and summary/hydrate staging. Complexity can still be high because a single result set may combine raw episodes, generated reflections, procedural lessons, knowledge seeds, graph neighbors, and internal dream outputs. Local SQLite and JSON modes are simpler and more inspectable but weaker in curation and retrieval depth.

**Authority at consumption.** Recalled memories are advisory knowledge until the host prompt tells an agent to obey them. Generated AGENTS/CLAUDE instructions are soft system-definition artifacts. Prompt exports can become always-loaded instructions or context, depending on where the operator places them. Effective authority depends on host behavior and model compliance, not just Clude's store.

**Other consumers.** Humans and services consume the same memory through dashboard timelines/graphs, server routes, CLI status/export/import/sync, MemoryPack verification, mobile/web/chat apps, Solana proofs, and the autonomous Cludebot runtime.

## Curiosity Pass

**The default MCP mode is not the README's simplest table.** The README says MCP local mode uses `~/.clude/memories.json`, but the server code defaults to SQLite unless `--local` or `CLUDE_LOCAL=true` is set; JSON is now an explicit local mode.

**Dream cycles are both impressive and authority-risky.** The code preserves evidence ids and links, but generated semantic/procedural/self-model claims can become future recall material without a review state.

**Compiled prompt files are the quiet high-authority surface.** The database may be well-scoped, but a stale generated prompt file can keep shaping an agent after the source memory store changes.

**Parametric state is mostly access structure, not source of truth.** Embeddings and vectors strongly affect recall, but memory records, summaries, tags, evidence ids, links, hashes, signatures, and revocations remain inspectable symbolic/prose artifacts.

**The platform mixes personal memory, product telemetry, and public bot identity.** Owner scoping and encryption are present, but imports, exports, dashboards, prompt sync, social-outcome tracking, and hosted dreams create many places where memory authority and privacy need explicit operator policy.

## What to Watch

- Whether local SQLite gains a full local dream/compaction worker; that would make the zero-setup path closer to the advertised cognitive architecture.
- Whether generated prompt files get source hashes or regeneration metadata; without that, compiled memory views can drift from the live store.
- Whether dream outputs gain review state or confidence gates before prompt export; that would make trace-derived procedural/self-model memories safer to treat as instruction.
- Whether hosted dreams expand from lightweight consolidation/procedural extraction into the full self-hosted dream cycle; that changes the authority of hosted memory.
- Whether behavioral faithfulness tests are added for prompt-file push and recalled context; that would separate actual activation from successful retrieval.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Clude stores many memories, but only recall calls, host instructions, and prompt-file loading determine whether they enter context.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Clude's memory rows, embeddings, links, dream logs, prompt files, MemoryPacks, and proofs have different lineage and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: recalled memories, summaries, dream logs, dashboard views, and MemoryPack records mostly advise as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: MCP schemas, injected AGENTS/CLAUDE instructions, prompt exports, validation schemas, and ranking policies shape behavior with stronger force.
- [Keep Lineage And Compiled Views From Drifting](../../notes/agent-memory-requirements/keep-compiled-views-aligned.md) - warns: generated prompt files and assistant instructions need source alignment because they can outlive the memory state that produced them.
- [Use Trace-Derived Extraction As Meta-Learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: Clude turns action/session traces into semantic insights, procedural lessons, and self-model memories.
