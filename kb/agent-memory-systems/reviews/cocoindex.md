---
description: "CocoIndex review: incremental Python dataflow framework for keeping vector, graph, file, and database targets fresh for agent context"
type: ../types/agent-memory-system-review.md
status: current
last-checked: "2026-06-01"
---

# CocoIndex

CocoIndex, from cocoindex-io, is an open-source Python framework with a Rust core for declarative incremental data pipelines. It is agent-memory-adjacent rather than an agent memory runtime: users write `TargetState = Transform(SourceState)` pipelines that keep external vector stores, graph databases, relational tables, files, or streams fresh for later retrieval by AI agents and LLM applications.

**Repository:** https://github.com/cocoindex-io/cocoindex

**Reviewed commit:** [57ea82a87bea41a515e987e387849139702cf1da](https://github.com/cocoindex-io/cocoindex/commit/57ea82a87bea41a515e987e387849139702cf1da)

**Last checked:** 2026-06-01

## Core Ideas

**The central retained unit is declared target state.** CocoIndex applications read sources, transform data, and declare what should exist in external systems; the engine compares the new declarations with prior runs and creates, updates, or removes only the changed target states ([core concepts](https://github.com/cocoindex-io/cocoindex/blob/57ea82a87bea41a515e987e387849139702cf1da/docs/src/content/docs/programming_guide/core_concepts.mdx), [target state docs](https://github.com/cocoindex-io/cocoindex/blob/57ea82a87bea41a515e987e387849139702cf1da/docs/src/content/docs/programming_guide/target_state.mdx), [target state API](https://github.com/cocoindex-io/cocoindex/blob/57ea82a87bea41a515e987e387849139702cf1da/python/cocoindex/_internal/target_state.py)). For agent memory, this means the durable memory surface is usually not CocoIndex itself, but the target store it keeps synchronized.

**Processing components give ownership and cleanup semantics.** `mount`, `use_mount`, and `mount_each` create stable component paths; when a component disappears, its owned target states can be cleaned up ([Python mount API](https://github.com/cocoindex-io/cocoindex/blob/57ea82a87bea41a515e987e387849139702cf1da/python/cocoindex/_internal/api.py), [AGENTS.md](https://github.com/cocoindex-io/cocoindex/blob/57ea82a87bea41a515e987e387849139702cf1da/AGENTS.md)). This is stronger than a one-shot indexing script because deletion and schema drift are part of the contract, not a later janitor job.

**Memoization tracks code, inputs, and selected context.** The `@coco.fn` decorator makes functions visible to change detection; `memo=True` replays cached return values and prior target declarations when the function's logic, arguments, and change-detected context values have not changed ([function docs](https://github.com/cocoindex-io/cocoindex/blob/57ea82a87bea41a515e987e387849139702cf1da/docs/src/content/docs/programming_guide/function.mdx), [function implementation](https://github.com/cocoindex-io/cocoindex/blob/57ea82a87bea41a515e987e387849139702cf1da/python/cocoindex/_internal/function.py)). The engine stores component memoization, function memoization, tracking info, and target ownership in LMDB ([internal storage docs](https://github.com/cocoindex-io/cocoindex/blob/57ea82a87bea41a515e987e387849139702cf1da/docs/src/content/docs/advanced_topics/internal_storage.mdx), [Rust schema](https://github.com/cocoindex-io/cocoindex/blob/57ea82a87bea41a515e987e387849139702cf1da/rust/core/src/state/db_schema.rs)).

**Live mode keeps target stores fresh but does not read them back to agents.** Catch-up mode scans and exits; live mode keeps the app running while live sources such as file watchers or Kafka feeds deliver incremental updates through `LiveMapView`, `LiveMapFeed`, or `auto_refresh` ([live mode docs](https://github.com/cocoindex-io/cocoindex/blob/57ea82a87bea41a515e987e387849139702cf1da/docs/src/content/docs/programming_guide/live_mode.mdx), [live component implementation](https://github.com/cocoindex-io/cocoindex/blob/57ea82a87bea41a515e987e387849139702cf1da/python/cocoindex/_internal/live_component.py), [localfs source](https://github.com/cocoindex-io/cocoindex/blob/57ea82a87bea41a515e987e387849139702cf1da/python/cocoindex/connectors/localfs/_source.py)). From the agent's perspective, this is freshness infrastructure, not activation.

**Connectors embody reconciliation policy.** Target connectors turn declared desired state into create/update/delete actions, tracking records, child handlers, and child invalidation outcomes. The local filesystem target uses content fingerprints; database and vector connectors use row/table handlers with schema and child invalidation logic ([localfs target](https://github.com/cocoindex-io/cocoindex/blob/57ea82a87bea41a515e987e387849139702cf1da/python/cocoindex/connectors/localfs/_target.py), [Postgres target](https://github.com/cocoindex-io/cocoindex/blob/57ea82a87bea41a515e987e387849139702cf1da/python/cocoindex/connectors/postgres/_target.py), [connector tree](https://github.com/cocoindex-io/cocoindex/tree/57ea82a87bea41a515e987e387849139702cf1da/python/cocoindex/connectors)). This makes the indexing layer more like a small state-reconciliation engine than a library of ad hoc ingestion helpers.

**Agent-facing context appears as shipped documentation, not runtime memory.** The repo includes a `skills/cocoindex/` agent skill and docs for installing it into Claude Code, Cursor, AGENTS.md, or custom RAG stacks so coding agents use the v1 API correctly ([AI coding agents docs](https://github.com/cocoindex-io/cocoindex/blob/57ea82a87bea41a515e987e387849139702cf1da/docs/src/content/docs/getting_started/ai_coding_agents.mdx), [CocoIndex skill](https://github.com/cocoindex-io/cocoindex/blob/57ea82a87bea41a515e987e387849139702cf1da/skills/cocoindex/SKILL.md)). That skill is a system-definition artifact for agents writing CocoIndex code, separate from the indexing engine.

**Context efficiency is indirect.** CocoIndex reduces reprocessing cost and keeps retrieval substrates fresh. It can help an agent avoid loading a whole corpus by maintaining chunks, embeddings, metadata tables, and knowledge graphs, but it does not itself impose a token budget, choose top-k, rerank for a task, or inject selected records into a model context. Selection and context complexity remain the host application's responsibility.

## Artifact analysis

- **Storage substrate:** `files` — Project files containing Python apps, dataclasses, context keys, connector configuration, and `@coco.fn` boundaries
- **Representational form:** `prose` `symbolic` — Symbolic Python plus typed schemas and occasional prose prompts
- **Lineage:** `authored` `imported` — Application developers author pipeline definitions and skills, while source connectors import external file, database, object-store, stream, and target-state material
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` — Pipeline code, connector reconciliation, memoization state, target schemas, cleanup behavior, and agent skills define or govern synchronization, while target rows can advise downstream agents

**User-authored pipeline definitions.** Storage substrate: project files containing Python apps, dataclasses, context keys, connector configuration, and `@coco.fn` boundaries. Representational form: symbolic Python plus typed schemas and occasional prose prompts. Lineage: authored by application developers; invalidated by source-code, `version`, `deps`, argument, or change-detected context changes. Behavioral authority: system-definition artifact because the pipeline defines sources, transforms, memoization boundaries, target schemas, and cleanup behavior.

**Internal engine state.** Storage substrate: LMDB under the configured CocoIndex database path. Representational form: symbolic serialized records for stable paths, component memoization, function memoization, tracking info, target-state ownership, target-state records, child existence, and ID sequencer state. Lineage: generated by prior app runs from the pipeline, source state, component paths, and connector tracking records; regenerated or invalidated by updates, drops, full reprocess, schema changes, logic fingerprints, memo keys, and target reconciliation. Behavioral authority: system-definition artifact with cache, ranking-none, reconciliation, deletion, and ownership authority; it decides what work can be skipped and which external target states should be touched.

**External target states.** Storage substrate: user-selected systems such as Postgres/pgvector, SQLite/sqlite-vec, LanceDB, Qdrant, SurrealDB, Neo4j, FalkorDB, Doris, Turbopuffer, Kafka/Iggy, or local files. Representational form: mixed, depending on the pipeline: prose chunks, symbolic rows, graph nodes and edges, vectors, JSON payloads, or generated files. Lineage: derived from source connectors and transform code; CocoIndex tracks enough ownership to update/delete rows and can preserve memo lineage for recomputation, but individual target rows are not automatically promoted into cited, reviewed claims. Behavioral authority: usually knowledge artifact for downstream agents or applications when used as evidence, context, or retrieval material; the target schema and connector reconciliation rules carry system-definition authority.

**Live source adapters.** Storage substrate: source services and runtime watchers rather than a single durable artifact. Representational form: symbolic keyed events and file metadata. Lineage: imported from filesystem events, Kafka topics, object stores, or polling wrappers; the source event causes remounting or deletion of affected components. Behavioral authority: system-definition artifact at the pipeline boundary because it schedules update work and deletion, but not an agent-facing memory by itself.

**Official CocoIndex skill.** Storage substrate: repository Markdown files under `skills/cocoindex/`. Representational form: prose instructions plus code examples and reference snippets. Lineage: authored alongside the framework and versioned with the source. Behavioral authority: system-definition artifact when installed into an agent's skill/rules/instructions surface; it instructs coding agents how to write correct CocoIndex pipelines. It is not trace-derived memory.

There is no built-in promotion path from retrieved corpus fragments to higher-authority notes, rules, validators, or instructions. A host application could build one with CocoIndex, but the framework's own contract stops at source-to-target synchronization.

## Comparison with Our System

| Dimension | CocoIndex | Commonplace |
|---|---|---|
| Primary purpose | Incrementally maintain external target stores for AI/search/data pipelines | Agent-operated methodology KB with durable notes, sources, instructions, reviews, ADRs, indexes, and validation |
| Storage substrate | User repo pipeline files, LMDB internal state, and external target systems | Git-tracked Markdown, source snapshots, type specs, schemas, generated indexes, scripts |
| Representational form | Symbolic Python/data schemas, serialized engine state, rows, vectors, graphs, files, streams | Mostly prose/frontmatter with symbolic schemas, links, commands, review outputs, and validation code |
| Lineage | Source-to-target recomputation and ownership metadata; memo invalidation by code/input/context | Source-pinned citations, review metadata, status lifecycle, replacement archives, validation and review gates |
| Activation | Host applications query target stores; live mode keeps targets fresh | Agents deliberately use `rg`, indexes, links, skills, instructions, validation, and review workflows |
| Behavioral authority | Pipeline code and engine state govern synchronization; target records advise downstream consumers | Artifacts can advise, instruct, route, validate, review, or govern future work |

CocoIndex and Commonplace share the belief that retained artifacts should be reproducible from explicit source material and machinery. The difference is the layer. CocoIndex is a state reconciliation engine for target stores; Commonplace is a curated knowledge base whose artifacts are meant to be read, cited, reviewed, and governed directly.

CocoIndex is stronger where the problem is freshness at scale. It can avoid re-embedding unchanged chunks, clean up rows when a file disappears, and keep graph/vector stores current in live mode. Commonplace is stronger where the problem is semantic authority: a note or review has a type, status, explicit source claims, authored links, and validation/review lifecycle.

The most useful comparison is lineage. CocoIndex can tell the engine what component owns a target state and whether source/code/context changes require recomputation. That is excellent operational lineage for rebuilding indexes. It is weaker epistemic lineage for agents: a retrieved vector row or graph edge may not carry the source citation, extraction rationale, confidence, contradiction policy, or review state needed before it becomes a durable methodology claim.

**Read-back:** `pull` — As reviewed. CocoIndex can keep vector, graph, and table targets fresh, but agent context arrives through host queries, database/vector-client searches, or downstream applications; the framework does not itself perform relevance-gated push activation into an agent

### Borrowable Ideas

**State reconciliation for generated indexes.** Ready conceptually. Commonplace already regenerates directory indexes, but CocoIndex's target-state framing is a useful way to think about generated artifacts as owned desired state: if a source artifact disappears, its derived navigation entries should disappear by construction.

**Logic/input/context invalidation vocabulary.** Ready now for design language. CocoIndex cleanly separates code logic, explicit dependencies, function inputs, and context values as invalidation causes. Commonplace could use the same split when describing when generated notes, indexes, or reviews become stale.

**Preview before applying target changes.** Useful with a concrete workflow. CocoIndex's app API and CLI include preview/update/drop modes around target actions ([app implementation](https://github.com/cocoindex-io/cocoindex/blob/57ea82a87bea41a515e987e387849139702cf1da/python/cocoindex/_internal/app.py), [CLI](https://github.com/cocoindex-io/cocoindex/blob/57ea82a87bea41a515e987e387849139702cf1da/python/cocoindex/cli.py)). A Commonplace analogue would preview generated index or migration changes before writing them.

**Agent skill packaged with the implementation.** Ready now as a publishing pattern. CocoIndex ships the skill that teaches agents how to use the current API. Commonplace already has skills; the borrowable pattern is keeping a public agent-facing instruction bundle versioned with the code it explains.

**Do not borrow opaque target rows as KB claims.** CocoIndex examples can build useful vector stores and knowledge graphs, but Commonplace should not treat retrieved rows as promoted notes without review, citations, and authority assignment.

## Curiosity Pass

The interesting part is that CocoIndex looks like an ingestion framework but behaves more like a reconciliation runtime. Its most memory-relevant mechanism is not embedding or graph extraction; it is the ownership model that lets declared target states be updated and deleted safely.

The README's agent-memory language is broader than the core implementation. The code supports building fresh context substrates for agents, and the examples include AI session search and conversation-to-knowledge pipelines ([entire session search](https://github.com/cocoindex-io/cocoindex/tree/57ea82a87bea41a515e987e387849139702cf1da/examples/entire_session_search), [conversation to knowledge](https://github.com/cocoindex-io/cocoindex/tree/57ea82a87bea41a515e987e387849139702cf1da/examples/conversation_to_knowledge)). But those examples do not make the framework itself a trace-derived learning system; they show that a user can index or extract from such corpora.

The strongest read-back-adjacent feature is live mode, but it pushes updates into target stores, not memories into model context. This distinction matters because freshness can be excellent while activation remains entirely manual or host-defined.

The internal LMDB state is powerful but intentionally not the human review surface. For Commonplace purposes, it is closer to a build cache and reconciliation ledger than a knowledge base.

## What to Watch

- Whether the marketed CocoIndex-code MCP server becomes source-visible in this repository; if it wires target-store retrieval into coding-agent prompts, the read-back placement may need revision.
- Whether connectors add source-citation or extraction-lineage columns as first-class conventions for vector/graph rows; that would move CocoIndex closer to reviewable knowledge artifacts.
- Whether the agent skill grows from static instructions into a generated, version-checked context bundle; that would be a useful pattern for keeping agent instructions synchronized with framework APIs.
- Whether live mode and target stores gain an official query/rerank/inject layer; that would change CocoIndex from context substrate maintenance into an activation system.

Relevant Notes:

- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: CocoIndex separates authored pipeline code, internal engine state, target rows, live adapters, and agent skills into different substrates, forms, lineage paths, and authorities.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: external target rows, vectors, and graph records usually advise downstream agents as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: pipeline code, memoization state, connector handlers, live adapters, and installed skills can instruct, route, validate, reconcile, or rank behavior.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - illustrates: fresh vector or graph storage is not the same as agent read-back.
- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - contrasts: CocoIndex can index session traces in examples, but the framework does not itself distill traces into durable behavior-shaping artifacts.
