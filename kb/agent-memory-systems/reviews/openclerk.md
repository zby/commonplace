---
description: "OpenClerk review: local-first JSON runner over markdown vaults, SQLite projections, provenance, synthesis, modules, and pull-only agent read-back"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-03"
---

# OpenClerk

OpenClerk, from `yazanabuashour/openclerk`, is a local-first knowledge-plane runtime for agents working over a markdown vault. Its public agent surface is an installed `openclerk` binary plus `skills/openclerk/SKILL.md`; routine agents send strict JSON to `openclerk document`, `openclerk retrieval`, `openclerk config`, and `openclerk module` rather than reading SQLite, vault files, module caches, HTTP/MCP internals, or source-tree binaries directly.

**Repository:** https://github.com/yazanabuashour/openclerk

**Reviewed commit:** [662b276afd84dc8f25436cd66b735011f86265ca](https://github.com/yazanabuashour/openclerk/commit/662b276afd84dc8f25436cd66b735011f86265ca)

**Last checked:** 2026-06-03

## Core Ideas

**The product is a narrow runner contract, not a memory daemon.** `cmd/openclerk/main.go` exposes `capabilities`, `init`, `config`, `module`, `document`, and `retrieval`; the static capabilities manifest describes a local-first building-block surface whose boundaries include canonical markdown authority, no direct SQLite, no hidden backend variants, and lexical search as the default retrieval mode ([cmd/openclerk/main.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/cmd/openclerk/main.go)). The architecture doc says the public contract is the installed runner plus the skill, with memory and routing deferred until docs, synthesis, and truth-sync layers are reliable ([docs/architecture/agent-knowledge-plane.md](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/docs/architecture/agent-knowledge-plane.md)).

**Markdown remains the claimed authority, while SQLite is the operational projection.** The README presents the vault markdown as canonical and the database as storage for the runner; the SQLite schema keeps documents, metadata, chunks, FTS rows, graph nodes/edges, records, services, decisions, provenance events, projection states, and runtime config in one local database ([README.md](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/README.md), [internal/infra/sqlite/schema.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/infra/sqlite/schema.go)). Vault sync scans markdown files, parses frontmatter/headings into stable document and chunk records, rebuilds FTS/projections when documents change, and prunes missing paths from the registry ([internal/infra/sqlite/sync.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/infra/sqlite/sync.go), [internal/infra/sqlite/markdown.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/infra/sqlite/markdown.go)).

**Agent writes are approval-shaped document actions.** `openclerk document` supports validation, create, append, section replacement, public-source/video ingestion, source-linked synthesis, artifact planning, web-search planning, layout inspection, and git lifecycle reporting. Mutating paths run under a write lock; many adjacent workflows return read-only plans or `agent_handoff` blocks instead of writing immediately ([internal/runner/document.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/runner/document.go), [skills/openclerk/SKILL.md](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/skills/openclerk/SKILL.md)).

**Context efficiency is primarily runner-side selection and workflow compression.** Core search is bounded, citation-bearing SQLite FTS over parsed chunks, with path, tag, and metadata filters plus a lexical-token fallback ([internal/infra/sqlite/documents.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/infra/sqlite/documents.go), [internal/runner/retrieval.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/runner/retrieval.go)). Higher-level reports compress multi-step routines into one JSON response with citations, projection freshness, validation boundaries, authority limits, and follow-up guidance; examples include evidence bundles, duplicate candidate reports, graph relationship reports, search diagnostics, and maintenance reports ([internal/runner/graph_context_report.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/runner/graph_context_report.go), [internal/runner/search_diagnostics_report.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/runner/search_diagnostics_report.go), [internal/runner/maintenance_report.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/runner/maintenance_report.go)). There is no token-budgeted context packer, automatic per-task memory push, or semantic search fallback.

**Source-linked synthesis is the main durable compounding path.** `compile_synthesis` assembles or replaces a markdown synthesis document with frontmatter, `## Sources`, and `## Freshness`, then reports duplicate status, provenance refs, projection freshness, validation boundaries, and authority limits ([internal/runner/compile_synthesis.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/runner/compile_synthesis.go)). The synthesis projection marks generated synthesis fresh or stale by checking source refs, missing refs, superseded refs, replacements, and source/update timestamps ([internal/infra/sqlite/synthesis.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/infra/sqlite/synthesis.go)).

**Optional modules are verified building blocks, not hidden core behavior.** Semantic retrieval and OCR are shipped as separately installed modules with manifests and skills. Core `semantic_search` verifies an installed/enabled module, validates provider posture, runs `semantic-retrieval-adapter`, requires citation-bearing output, and returns blocked results rather than falling back silently ([internal/runclient/modules.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/runclient/modules.go), [internal/runner/semantic_search.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/runner/semantic_search.go), [modules/semantic-retrieval-adapter/README.md](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/modules/semantic-retrieval-adapter/README.md), [modules/ollama-embeddings/module.json](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/modules/ollama-embeddings/module.json), [modules/gemini-embeddings/module.json](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/modules/gemini-embeddings/module.json)).

**It has evaluation and maintenance surfaces, but not trace-derived memory.** `retrieval_eval_capture` appends explicit local JSONL regression cases containing sanitized query/action/filter/result refs, provider status, latency, and timestamps; replay compares Jaccard, top-1, and latency ([internal/runner/retrieval_eval.go](https://github.com/yazanabuashour/openclerk/blob/662b276afd84dc8f25436cd66b735011f86265ca/internal/runner/retrieval_eval.go)). That is useful governance evidence for retrieval behavior, but it does not distill agent transcripts, tool traces, or trajectories into future prompt rules or memory artifacts.

## Artifact analysis

- **Storage substrate:** `sqlite` — The central operational substrate is the local OpenClerk SQLite database under `${XDG_DATA_HOME:-~/.local/share}/openclerk/openclerk.sqlite`, with markdown vault files as the canonical document substrate and optional rebuildable caches outside the committed vault.
- **Representational form:** `prose` `symbolic` `parametric` — OpenClerk mixes prose markdown and skills, symbolic runner contracts, SQLite tables, FTS indexes, projection state, module manifests, and optional semantic/vector caches.
- **Lineage:** `authored` `imported` — Canonical markdown can be authored, imported, or runner-created, while SQLite projections, synthesis state, provenance, module state, caches, and eval captures derive from vault files, runner actions, source refs, and explicit captures.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` — Markdown and synthesis advise agents, while skills, capabilities manifests, projection state, provenance, module config, retrieval indexes, and eval captures instruct, route, audit, gate, and rank lookup behavior.

**Canonical vault documents.** The durable knowledge artifacts are markdown files under the configured vault root. Their storage substrate is ordinary files, but their runner-visible identity, chunks, headings, metadata, and citations are mirrored into SQLite. Their representational form is prose markdown with symbolic frontmatter and paths. Their lineage is authored, imported, or runner-created through approved document actions; source ingestion and synthesis attach citations, source refs, and provenance. Their behavioral authority is knowledge-artifact authority for source answers and system-definition authority only when a document's content is intentionally consumed as instruction by an external agent workflow.

**SQLite registry, chunks, FTS, and lookup tables.** The `documents`, `document_metadata`, `chunks`, and `chunk_fts` tables are derived projections over vault markdown. Their storage substrate is SQLite. Their representational form is symbolic rows plus indexed prose text. Their lineage is current vault files parsed by sync or updated after runner writes. Their behavioral authority is retrieval and ranking influence: they choose which markdown chunks the agent sees, but they do not outrank cited canonical markdown.

**Promoted graph, records, services, and decisions.** The graph, generic records, services, and decisions tables are typed projections derived from canonical markdown. Their storage substrate is SQLite. Their representational form is symbolic records with citations back to source documents. Their lineage is derived and refreshable from current markdown; projection states and provenance events expose freshness. Their behavioral authority is structured lookup and navigation, not independent truth. The code and docs repeatedly frame canonical markdown as the authority over graph evidence, service rows, record rows, and decision projections.

**Synthesis documents and synthesis projection state.** Synthesis pages are markdown documents, usually under `synthesis/`, generated or updated through `compile_synthesis`. Their storage substrate is vault files plus SQLite projection state. Their representational form is prose markdown with symbolic frontmatter and source refs. Their lineage is user/agent-authored synthesis compiled from cited source refs; the projection marks staleness when sources change, disappear, or become superseded. Their behavioral authority is durable knowledge-artifact authority subordinate to canonical sources, with projection freshness acting as an audit trigger.

**Provenance events and projection states.** The `provenance_events` and `projection_states` tables are symbolic audit artifacts in SQLite. Their lineage is runner writes, projection rebuilds, source ingestion, and invalidation/refresh operations. Their behavioral authority is audit and governance: future agents can inspect derivation, freshness, stale dependents, and source refs before making claims or approving repairs.

**OpenClerk skill and capabilities manifest.** `skills/openclerk/SKILL.md` and the `capabilities` JSON are prose/symbolic system-definition artifacts. Their storage substrate is the installed skill file and runner binary/source release. Their lineage is authored product policy. Their behavioral authority is instruction and routing: they tell agents which runner surface to use, which bypasses are unsupported, when to ask for approval, and when to answer from `agent_handoff`.

**Module manifests, module config, and semantic caches.** Module manifests are repo files; installed module state and redacted provider config live in SQLite `runtime_config`; semantic adapter caches are rebuildable user-cache artifacts outside the committed repo. Their representational form is symbolic JSON/config plus optional cached vectors. Their lineage is manifest-verified installation and explicit configuration. Their behavioral authority is capability gating and retrieval ranking for explicit module calls only; they are not allowed to change default search or become the authority layer.

**Retrieval eval captures.** Retrieval eval rows are local JSONL artifacts outside the vault by default. Their representational form is symbolic JSON with sanitized query/action/filter/result refs, provider status, and latency. Their lineage is explicit user-invoked capture of search or semantic-search output. Their behavioral authority is evaluation evidence for retrieval regressions, not memory read-back or source authority.

**Promotion path.** OpenClerk's main promotion path is canonical/source markdown -> retrieval evidence -> source-linked synthesis -> projection freshness/provenance -> approved repair or reuse. A second path promotes structured facts from markdown into records/services/decisions, but the promoted rows stay subordinate to cited source documents. There is no implemented promotion path from agent traces to durable prompt rules or autonomous memory routing.

## Comparison with Our System

| Dimension | OpenClerk | Commonplace |
|---|---|---|
| Primary purpose | Local JSON runner over a markdown vault for agent document/retrieval workflows | Typed methodology KB for agents and maintainers |
| Canonical substrate | User vault markdown, accessed through runner-visible ids/chunks/citations | Git-tracked markdown collections under `kb/` |
| Operational substrate | SQLite registry, FTS, projections, provenance, config, optional modules | Files plus generated indexes, validation scripts, review reports, and skills |
| Agent interface | Installed `openclerk` commands and skill routing to JSON actions | Direct file/search workflow, collection contracts, `cp-skill-*`, validation/review commands |
| Retrieval | Bounded lexical FTS by default; explicit module-gated semantic search | `rg`, indexes, descriptions, links, reports; no standing DB in the core KB |
| Governance | Approval-aware runner actions, provenance, projection freshness, module verification, eval captures | Schemas, collection contracts, deterministic validation, semantic gates, git review, archive/replacement |

OpenClerk is closer to "Commonplace packaged as a product runtime" than to a memory library. Both systems are file-first in authority and treat indexes as derived aids. The major difference is that OpenClerk hides the operational complexity behind a single runner contract, while Commonplace deliberately exposes the repo as the working substrate because methodology authors and agents are expected to inspect and edit the KB directly.

The strongest alignment is the source/projection split. OpenClerk keeps canonical markdown and citations visible while letting SQLite carry FTS, graph, records, provenance, and projection freshness. Commonplace has the same source-of-truth instinct, but currently implements more of the projection layer as generated markdown indexes, validation outputs, and review artifacts rather than a local operational database.

The biggest divergence is authority packaging. Commonplace's artifact types and collection contracts are authored as the library itself; OpenClerk's types are product behaviors encoded in runner actions, SQLite schema, capabilities output, skill policy, and module manifests. That gives OpenClerk a cleaner routine agent UX, but it also means important semantics live in code and response contracts rather than in first-class KB artifacts.

**Read-back:** `pull` — Retained vault knowledge reaches an agent only when the agent or user invokes `openclerk retrieval` or `openclerk document` actions; the skill is static routing policy, and the checked implementation has no automatic memory push, session hook, situation-triggered recall, or query-independent prompt injection of accumulated vault knowledge.

### Borrowable Ideas

**Runner responses with `agent_handoff`.** Ready as a design pattern for promoted Commonplace commands. OpenClerk's workflow actions do not just return raw data; they include answer summaries, evidence, validation boundaries, authority limits, and follow-up primitive guidance. Commonplace review/report commands could make their handoff fields more uniform for agents.

**Projection freshness as a first-class query.** Ready for synthesis and source reviews. OpenClerk's `projection_states` table makes staleness inspectable instead of burying it in generated text. Commonplace could borrow the same explicit freshness vocabulary for source-derived artifacts and generated indexes before adding a database.

**Optional modules as verified building blocks.** Ready for future retrieval extensions. OpenClerk's semantic modules are explicit, manifest-verified, and forbidden from changing default search. Commonplace should use the same boundary if it adds embeddings, OCR, or external providers.

**Read-only maintenance reports.** Ready as a command shape. `maintenance_report` packages layout, projection freshness, duplicate risk, module posture, relationship context, and git posture without repairing anything. Commonplace has separate validation and review tools; a compact "doctor" report could improve operator handoff without changing authority.

**Approval-shaped write plans.** Needs a concrete workflow first. OpenClerk often returns exact next write requests with `planned_no_write` and approval boundaries. Commonplace could use that for risky source ingestion, relationship maintenance, or archive replacement, but only where the existing file-edit workflow is too error-prone.

**SQLite as an operational projection layer.** Needs scale pressure before adoption. OpenClerk shows how a local database can hold FTS, projection state, provenance, and config while leaving markdown as authority. Commonplace should not add this until generated indexes and command outputs become too slow or too hard to compose.

## Write-side placement

**Write agency:** `automatic` `manual` — the review describes system-driven generation, extraction, consolidation, or update of retained artifacts rather than only manual authoring.

**Curation operations:** `consolidate` `dedup` `synthesize` `invalidate` `decay` `promote` — the existing review evidence identifies automatic store-changing operations matching these curation classes.

## Curiosity Pass

**The strongest memory mechanism is governance, not recall.** OpenClerk's distinctive move is not a novel retriever; it is the repeated insistence that agents use a narrow runner, preserve citations, avoid raw storage bypasses, and keep writes approval-shaped.

**The database is both derived and operational.** SQLite is not the declared authority, but it is still the working substrate for routine reads, ids, FTS, projections, provenance, and module config. If the projection layer drifts, the agent-facing product can misbehave even while markdown remains readable.

**`SKILL.md` is intentionally thin but still high-authority.** The architecture says the skill is not the workflow engine, yet the skill's no-tools and bypass rules strongly shape agent behavior. That makes the skill a compact system-definition artifact, not just documentation.

**Semantic retrieval is implemented as a process boundary.** The core runner shells out to a verified adapter command and validates its JSON response. That is a pragmatic extension boundary, but module behavior is only as trustworthy as manifest verification, command resolution, and the adapter contract.

**Retrieval eval capture is close to trace-derived learning but stops short.** It stores sanitized evidence of retrieval behavior for replay. It does not mine trajectories into rules, update prompts, or change future retrieval policy automatically, so it belongs under evaluation governance rather than trace-derived memory.

## What to Watch

- Whether memory and routing remain deferred or become implemented public surfaces. That would change OpenClerk from a pull-only knowledge plane into a stronger memory activation system.
- Whether source-linked synthesis gains per-claim citations or review states. Current synthesis has source refs and freshness, but claim-level auditability would matter if synthesis becomes high-authority.
- Whether projection rebuild/freshness semantics remain explainable as graph, records, services, decisions, and synthesis expand. The more projections do, the more agents will need precise stale/derived/current distinctions.
- Whether semantic modules keep their no-default-ranking boundary after users install them. Silent semantic fallback would weaken the canonical markdown/citation discipline.
- Whether retrieval eval captures start feeding automatic ranking changes. That would move evaluation artifacts toward learning inputs and should trigger a trace-derived review update.
- Whether document lifecycle and rollback become runner-visible. That would close a governance gap for agent-authored durable writes without making Git alone carry review semantics.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - exemplifies: OpenClerk stores and indexes vault knowledge, but future agents still need explicit runner retrieval to bring it back.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: OpenClerk separates vault markdown, SQLite projections, provenance, modules, skills, and eval captures by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: canonical docs, retrieval hits, synthesis pages, and eval evidence mostly advise or evidence future work.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: runner actions, capabilities output, skills, module manifests, approval boundaries, and projection freshness policies configure agent behavior.
- [Symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - aligns: OpenClerk relies on explicit paths, ids, filters, and runner actions as the symbols that make pull retrieval possible.
