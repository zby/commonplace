---
description: "OpenClerk review: local JSON runner over Markdown vaults with SQLite projections, provenance, synthesis, reports, and optional semantic modules"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-04"
---

# OpenClerk

OpenClerk, from `yazanabuashour/openclerk`, is a local-first agent knowledge-plane runtime for a Markdown vault. It exposes a single `openclerk` CLI with strict JSON domains for configuration, document writes, retrieval, and optional modules; keeps canonical Markdown as the human-readable authority; and stores derived chunks, FTS rows, graph edges, promoted records, decision/service projections, provenance events, and freshness state in local SQLite.

**Repository:** https://github.com/yazanabuashour/openclerk

**Reviewed commit:** [662b276afd84dc8f25436cd66b735011f86265ca](https://github.com/yazanabuashour/openclerk/commit/662b276afd84dc8f25436cd66b735011f86265ca)

**Source directory:** `related-systems/yazanabuashour--openclerk`

## Core Ideas

**The production surface is a local JSON runner.** The CLI dispatches to `capabilities`, `init`, `config`, `module`, `document`, and `retrieval`; the runner type file enumerates document actions such as `create_document`, `ingest_source_url`, `compile_synthesis`, `append_document`, and `replace_section`, plus retrieval actions such as `search`, `document_links`, `records_lookup`, `projection_states`, `memory_router_recall_report`, `semantic_search`, and `maintenance_report` ([cmd/openclerk/main.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/cmd/openclerk/main.go), [internal/runner/types.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/runner/types.go)). The installed skill is an instruction/routing contract that tells agents to stay inside the runner and avoid direct SQLite, vault, HTTP/MCP, source-built, or broad search bypasses for routine work ([skills/openclerk/SKILL.md](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/skills/openclerk/SKILL.md)).

**Canonical Markdown remains the authority; SQLite is a projection layer.** Runtime path resolution binds a local database and vault root; the schema stores documents, metadata, chunks, FTS, graph nodes/edges, records, services, decisions, provenance, projection states, runtime config, and module/profile settings ([internal/runclient/local.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/runclient/local.go), [internal/infra/sqlite/schema.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/infra/sqlite/schema.go), [internal/runclient/profile_config.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/runclient/profile_config.go)). Sync scans Markdown files, parses frontmatter/headings/sections, writes chunks and FTS rows, and records provenance and projection invalidations when content changes ([internal/infra/sqlite/sync.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/infra/sqlite/sync.go)).

**Context efficiency is explicit retrieval and workflow packaging.** Default search is lexical FTS with a token fallback, returning citation-bearing hits rather than loading a whole vault ([internal/infra/sqlite/documents.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/infra/sqlite/documents.go)). Higher-level reports package bounded slices of evidence: relationship reports combine a selected document, canonical relationship text, links, graph neighborhood, projection freshness, and provenance; maintenance and evidence-bundle reports aggregate multiple runner checks into one agent handoff ([internal/runner/graph_context_report.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/runner/graph_context_report.go), [internal/runner/maintenance_report.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/runner/maintenance_report.go)). Complexity is controlled by action selection, limits, path prefixes, doc ids, citations, and report-specific summaries, not by an always-on memory injection layer.

**Writes are approval-aware and provenance-bearing.** Document actions can create, append, replace sections, ingest web/PDF/video sources, and compile synthesis pages; mutating paths use write locks and then resync derived state ([internal/runner/document.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/runner/document.go), [internal/infra/sqlite/documents.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/infra/sqlite/documents.go)). Source ingestion downloads public web/PDF content through runner-owned code, builds Markdown source notes with hashes/citations/assets, and validates indexed citations before returning results ([internal/infra/sqlite/ingest_source.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/infra/sqlite/ingest_source.go)). Candidate and relationship-maintenance actions deliberately return `planned_no_write` requests and approval boundaries before durable mutation ([internal/runner/artifact_candidate_plan.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/runner/artifact_candidate_plan.go), [internal/runner/graph_relationship_maintenance_plan.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/runner/graph_relationship_maintenance_plan.go)).

**Optional modules are verified building blocks, not hidden defaults.** `openclerk module` registers semantic embedding and OCR providers by manifest, redacts provider config, and verifies command boundaries; `semantic_search` reads registered module config and shells out to `semantic-retrieval-adapter` only for an explicit semantic query ([internal/runclient/modules.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/runclient/modules.go), [internal/runner/semantic_search.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/runner/semantic_search.go), [modules/semantic-retrieval-adapter/main.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/modules/semantic-retrieval-adapter/main.go)).

**Memory and autonomous routing are intentionally deferred.** The README says autonomous memory/routing is not supported yet, and the memory-routing decision says it adds no memory-first `remember`/`recall` behavior, autonomous router, public interface, storage API, or runner action beyond evidence/reporting ([README.md](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/README.md), [docs/architecture/memory-routing-reference-decision.md](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/docs/architecture/memory-routing-reference-decision.md)). The implemented `memory_router_recall_report` is read-only packaging over canonical memory-router docs, synthesis freshness, and provenance; it explicitly reports no memory transports, remember/recall actions, autonomous router APIs, graph memory, or hidden authority ranking ([internal/runner/memory_router_recall.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/runner/memory_router_recall.go)).

## Artifact analysis

- **Storage substrate:** `files` `sqlite` — Canonical knowledge persists as Markdown files under the configured vault; local SQLite stores runtime config, document registry, chunks, FTS, graph, record/service/decision projections, provenance, projection freshness, module state, and profile defaults. Optional semantic modules may keep provider-specific cache files outside the core canonical store.
- **Representational form:** `prose` `symbolic` `parametric` — Markdown notes, synthesis pages, source notes, skill instructions, report handoffs, and docs are prose; runner JSON schemas, CLI dispatch, SQLite rows, frontmatter, chunks, FTS rows, graph edges, projection states, provenance events, module manifests, and tests are symbolic; optional embedding modules produce vectors/cache state for explicit semantic retrieval.
- **Lineage:** `authored` `imported` — Vault documents and configuration can be authored through editors or runner writes; source URL/video/artifact intake imports external material into canonical Markdown; chunks, graph, records, services, decisions, synthesis freshness, provenance, and FTS are derived from canonical documents. I did not find a qualifying pipeline that derives durable retained artifacts from agent session logs, tool traces, event streams, or trajectories.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — Retrieved docs, citations, graph reports, evidence bundles, and synthesis pages advise as knowledge; the skill, capabilities manifest, runner action schemas, module manifests, and handoffs instruct agents; approval boundaries, runner validation, path normalization, write locks, module verification, and no-bypass rules enforce; workflow-guide, report selectors, source/candidate planning, graph relationship plans, and memory-router reports route work; layout checks, duplicate reports, source audits, projection freshness, git lifecycle, and retrieval replay validate; lexical/semantic search and report selection rank attention; module registration and retrieval eval capture provide learning/evaluation inputs without changing default memory authority.

**Canonical documents.** Markdown vault files are the source-of-truth knowledge artifacts. The runner writes them through `CreateDocument`, `AppendDocument`, `ReplaceDocumentSection`, source ingestion, and synthesis compilation, then syncs them into SQLite for search and projection ([internal/infra/sqlite/documents.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/infra/sqlite/documents.go), [internal/runner/compile_synthesis.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/runner/compile_synthesis.go)). Their authority is knowledge and, when frontmatter/sections use recognized schemas, source material for projections.

**Projection state and provenance.** `projection_states` and `provenance_events` retain freshness, source refs, invalidation/refreshed events, and write history for documents, graph, records, services, decisions, and synthesis ([internal/infra/sqlite/projections.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/infra/sqlite/projections.go), [internal/infra/sqlite/provenance.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/infra/sqlite/provenance.go), [internal/infra/sqlite/synthesis.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/infra/sqlite/synthesis.go)). This state does not replace Markdown authority; it lets agents audit freshness, derivation, and whether a derived view should still be trusted.

**Graph, records, services, and decisions.** Rebuild code extracts graph edges from links/chunks and extracts promoted record, service, and decision projections from canonical document markup, preserving citations back to source chunks ([internal/infra/sqlite/graph.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/infra/sqlite/graph.go), [internal/infra/sqlite/records.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/infra/sqlite/records.go), [internal/infra/sqlite/services.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/infra/sqlite/services.go), [internal/infra/sqlite/decisions.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/infra/sqlite/decisions.go)). These are promoted symbolic views over prose, useful for routing and lookup but explicitly subordinate to canonical documents.

**Skill and capability contracts.** `skills/openclerk/SKILL.md` and the capabilities output are system-definition artifacts: they tell agents which action to call, what to refuse without tools, and which bypasses are invalid ([skills/openclerk/SKILL.md](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/skills/openclerk/SKILL.md), [cmd/openclerk/main.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/cmd/openclerk/main.go)). Their behavioral authority is instruction, routing, validation, and enforcement; they are stronger than ordinary notes because an agent is expected to obey them before touching a vault.

**Module artifacts.** Module manifests and registrations are symbolic system-definition artifacts; semantic adapter cache files and vectors are parametric retrieval state used only by explicit `semantic_search` ([modules/ollama-embeddings/module.json](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/modules/ollama-embeddings/module.json), [modules/gemini-embeddings/module.json](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/modules/gemini-embeddings/module.json), [modules/semantic-retrieval-adapter/main.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/modules/semantic-retrieval-adapter/main.go)).

Promotion path: authored/imported Markdown is promoted into chunks, FTS, graph edges, records, services, decisions, synthesis freshness, provenance, and optional semantic vectors. OpenClerk also plans candidate write requests and reports, but most generated guidance stays advisory until an explicit approved document write makes it canonical.

## Comparison with Our System

| Dimension | OpenClerk | Commonplace |
|---|---|---|
| Primary purpose | Local agent knowledge-plane runtime over a user's Markdown vault | Methodology KB and framework for agent-operated knowledge bases |
| Canonical substrate | Configured vault Markdown plus SQLite projections | Git-tracked `kb/` collections, type specs, validation, sources, reviews, and indexes |
| Agent interface | Installed skill plus strict JSON CLI runner | Repository instructions, skills, direct file edits, validation commands, review workflows |
| Retrieval | Lexical FTS by default, explicit semantic module, graph/record/decision/provenance reports | `rg`, authored indexes, links, generated indexes, source snapshots, semantic review reports |
| Write governance | Approval-aware runner writes, source refs, provenance, projection freshness, optional git lifecycle reports | Collection/type contracts, citations, validation, semantic QA, git diffs, review lifecycle |
| Memory stance | Explicit recall/reporting; autonomous memory/router surfaces deferred | Mostly explicit pull/navigation, with instructions and skills loaded by the agent harness |

OpenClerk and Commonplace share a strong commitment to file-native authority, citations, source refs, and derived views that remain subordinate to canonical text. OpenClerk is more productized as an agent-facing runtime: it gives hosts a narrow JSON surface with action schemas, handoffs, locks, module registration, and report commands. Commonplace is more library-methodological: its authority lives in collection contracts, type specs, validation, review, source snapshots, and git-visible edits rather than a product runner.

The biggest design divergence is where ceremony is encoded. OpenClerk moves recurring workflows into runner actions such as `graph_context_report`, `duplicate_candidate_report`, `source_audit_report`, `memory_router_recall_report`, and `maintenance_report`. Commonplace tends to encode comparable ceremony in skills, instructions, validation commands, and review gates. OpenClerk's approach reduces repeated tool choreography for agents, but it also requires carefully maintained runner schemas for each promoted workflow.

OpenClerk's derived state is more operational than Commonplace's generated indexes: graph, records, decisions, services, synthesis freshness, and module cache are all queryable through one runtime. Commonplace's stronger side is reviewability of methodology claims; OpenClerk's stronger side is a clean local product boundary for ordinary agents who should not inspect implementation files or SQLite.

### Borrowable Ideas

**Runner-owned workflow actions with handoffs.** Commonplace could promote high-ceremony workflows, such as source audit, duplicate candidate selection, or review-bundle follow-up, into compact commands that return evidence, boundaries, authority limits, and next approved actions. Ready for workflows that already recur and have deterministic validation.

**Projection freshness as a first-class read surface.** Commonplace generated indexes and review reports could expose freshness/source-ref state in a queryable way instead of relying only on regenerated files and human inspection. Ready where source refs are already explicit.

**Approval-before-write candidate plans.** OpenClerk's candidate plans return exact next requests without mutating canonical Markdown. Commonplace could use the same shape for note routing, source ingestion, and relationship maintenance. Ready for narrow create/update decisions.

**Optional modules with manifest verification.** A local semantic or OCR layer for Commonplace should be explicit, manifest-verified, and subordinate to canonical citations. Ready as a constraint, not necessarily as an immediate feature.

**Do not borrow deferred autonomous memory as product authority.** OpenClerk's own decisions keep memory-first recall and autonomous routing out of production until evals prove need. Commonplace should keep the same burden of proof before pushing retained memory automatically.

## Write side

**Write agency:** `manual` `automatic` — Users and agents manually create, append, replace, ingest, and compile Markdown through approved runner actions; OpenClerk automatically syncs vault files, chunks them, rebuilds FTS, extracts graph/record/service/decision/synthesis projections, records provenance, marks projections stale, and appends opt-in retrieval-eval rows.

**Curation operations:** `invalidate` `promote` — Projection invalidation marks graph, records, services, decisions, and synthesis views stale when source documents change, while projection rebuilds promote canonical Markdown into graph edges, promoted records, decision/service records, synthesis freshness, chunks, FTS rows, and optional semantic search state. I did not find automatic deduplication, consolidation, decay, evolution, or generative synthesis over stored entries; duplicate reports and artifact plans are read-only decision support unless an explicit write follows.

## Read-back

**Read-back:** `pull` — Retained vault memory reaches an agent when the agent or host deliberately invokes `openclerk retrieval` or `openclerk document` actions such as search, get, graph/report, records, decisions, provenance, projection states, semantic search, source audit, duplicate candidate, memory-router recall report, or maintenance report. The installed skill and capabilities manifest can instruct the agent to use those pulls, but I did not find an OpenClerk loop that automatically injects retained vault memories into future model invocations without a runner call.

The pull surfaces are broad and structured: lexical search returns cited chunks, graph/report actions package bounded evidence, record/decision/service projections give typed lookup, provenance/projection endpoints support freshness checks, and optional semantic search returns citation-bearing module results only when explicitly requested. Effective downstream use of retrieved context is not tested by the system itself; retrieval eval capture/replay measures result-ref stability, Jaccard, top-1 match, provider posture, and latency, not whether an agent obeyed a recalled memory ([internal/runner/retrieval_eval.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/runner/retrieval_eval.go)).

## Curiosity Pass

**The system looks memory-adjacent but is deliberately not a memory transport.** The name and memory-router reports could imply autonomous memory, but the implementation and architecture docs keep memory as canonical Markdown plus explicit report/read surfaces.

**The strongest retained behavior is the skill contract, not the vault.** Ordinary vault documents advise only after retrieval; the installed skill changes agent behavior immediately by forbidding bypasses and selecting runner actions.

**The graph is navigation evidence, not truth.** Graph reports repeatedly state canonical Markdown remains relationship authority and graph evidence is read-only context, which keeps the graph from becoming an unreviewed semantic store.

**Semantic search is architecturally fenced.** The code supports embedding modules, cache files, Ollama, and Gemini, but default search remains lexical and semantic ranking is explicit, verified, and citation-gated.

**The evaluation layer is careful but not faithfulness testing.** Retrieval replay can catch search regressions, but it does not prove that an agent used a returned note faithfully in its final behavior.

## What to Watch

- Whether memory/router reports become automatic prompt injection or a real `remember`/`recall` transport; that would change read-back from pull to push or both.
- Whether retrieval eval grows into with/without behavioral ablations; that would make faithfulness claims stronger than current result-ref replay.
- Whether projection freshness becomes repair automation rather than reporting; that would increase enforcement authority and curation scope.
- Whether optional semantic modules start altering default search ranking; that would change the retrieval and authority story.
- Whether source ingestion and artifact planning add broader media/web acquisition; that would expand imported lineage and require stronger provenance review.
- Whether graph relationship candidates become durable semantic graph storage; that would move graph state from navigation evidence toward system-definition authority.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - applies: OpenClerk stores and projects vault memory, but read-back is explicit runner-mediated pull.
- [Axes of artifact analysis](../../../notes/axes-of-artifact-analysis.md) - applies: OpenClerk separates Markdown authority, SQLite projections, module manifests, skills, provenance, and optional vector state.
- [Knowledge artifact](../../../notes/definitions/knowledge-artifact.md) - distinguishes: retrieved documents, citations, graph context, evidence bundles, and synthesis pages mostly advise as evidence.
- [System-definition artifact](../../../notes/definitions/system-definition-artifact.md) - distinguishes: skill contracts, runner schemas, module manifests, approval boundaries, and validation gates instruct or constrain behavior.
- [Storage substrate](../../../notes/definitions/storage-substrate.md) - relates: canonical files and SQLite-derived state carry different deletion, versioning, and inspection properties.
- [Context engineering](../../../notes/definitions/context-engineering.md) - frames: OpenClerk's main design work is routing bounded, cited vault evidence into agent-facing JSON surfaces.
