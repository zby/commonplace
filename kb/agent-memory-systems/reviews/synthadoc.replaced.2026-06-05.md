---
description: "Synthadoc review: ingest-time LLM wiki compiler with Markdown pages, SQLite audit/provenance, lifecycle states, routing, and context packs"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: []
status: outdated
last-checked: "2026-06-03"
---

# Synthadoc

> Replaced 2026-06-05. See [Synthadoc](./synthadoc.md) for the current review.

Synthadoc, by `axoviq-ai`, is a Python knowledge-compilation engine that turns source documents, URLs, web searches, and media into a persistent local Markdown wiki. The inspected repository ships a Typer CLI, FastAPI server, Obsidian plugin, built-in extraction skills, optional vector reranking, SQLite-backed jobs/cache/audit/provenance state, lifecycle governance, routing, candidate staging, and context-pack/export surfaces.

**Repository:** https://github.com/axoviq-ai/synthadoc

**Reviewed commit:** [22b4412df8089e5628eb7a7c9e568711a3ce82f8](https://github.com/axoviq-ai/synthadoc/commit/22b4412df8089e5628eb7a7c9e568711a3ce82f8)

**Last checked:** 2026-06-03

## Core Ideas

**The wiki is compiled at ingest time.** Ingest jobs extract text through a skill, run an analysis pass, retrieve existing candidate pages with BM25, ask an LLM for a create/update/flag/skip decision, annotate new sections with source-line citations, write Markdown pages, update the overview, and record audit rows ([ingest_agent.py](https://github.com/axoviq-ai/synthadoc/blob/22b4412df8089e5628eb7a7c9e568711a3ce82f8/synthadoc/agents/ingest_agent.py), [orchestrator.py](https://github.com/axoviq-ai/synthadoc/blob/22b4412df8089e5628eb7a7c9e568711a3ce82f8/synthadoc/core/orchestrator.py)). The durable artifact is the wiki page, not a transient answer.

**Plain Markdown carries the knowledge surface, while SQLite carries operational memory.** Wiki pages live under `wiki/` with YAML frontmatter for title, tags, status, confidence, sources, aliases, categories, contradiction notes, and lint warnings ([wiki.py](https://github.com/axoviq-ai/synthadoc/blob/22b4412df8089e5628eb7a7c9e568711a3ce82f8/synthadoc/storage/wiki.py)). SQLite sidecars hold jobs, response cache, embeddings, ingest/query/audit rows, claim citations, page states, lifecycle events, scheduled runs, and cost history ([queue.py](https://github.com/axoviq-ai/synthadoc/blob/22b4412df8089e5628eb7a7c9e568711a3ce82f8/synthadoc/core/queue.py), [cache.py](https://github.com/axoviq-ai/synthadoc/blob/22b4412df8089e5628eb7a7c9e568711a3ce82f8/synthadoc/core/cache.py), [log.py](https://github.com/axoviq-ai/synthadoc/blob/22b4412df8089e5628eb7a7c9e568711a3ce82f8/synthadoc/storage/log.py), [search.py](https://github.com/axoviq-ai/synthadoc/blob/22b4412df8089e5628eb7a7c9e568711a3ce82f8/synthadoc/storage/search.py)).

**Context efficiency is mostly frontloaded and scoped.** Ingest decisions read a cached short analysis, top BM25 candidates, and `purpose.md` scope rather than the whole corpus. Query decomposes complex questions, merges top results, optionally scopes through `ROUTING.md`, clips page bodies to short excerpts, and uses gap detection to avoid false confidence ([query_agent.py](https://github.com/axoviq-ai/synthadoc/blob/22b4412df8089e5628eb7a7c9e568711a3ce82f8/synthadoc/agents/query_agent.py), [routing.py](https://github.com/axoviq-ai/synthadoc/blob/22b4412df8089e5628eb7a7c9e568711a3ce82f8/synthadoc/core/routing.py)). Context packs make the budget explicit by packing retrieved excerpts until a token cap is reached ([context_agent.py](https://github.com/axoviq-ai/synthadoc/blob/22b4412df8089e5628eb7a7c9e568711a3ce82f8/synthadoc/agents/context_agent.py)).

**Governance is implemented as lint, provenance, lifecycle, and staging.** Lint removes dangling links, detects orphans, reviews contradicted pages, can run an adversarial warning pass, validates citation markers against extracted source sidecars, and runs the five-state lifecycle checks ([lint_agent.py](https://github.com/axoviq-ai/synthadoc/blob/22b4412df8089e5628eb7a7c9e568711a3ce82f8/synthadoc/agents/lint_agent.py)). Candidate staging keeps generated pages outside the main wiki until promotion, and lifecycle transitions are exposed through CLI/HTTP/Obsidian paths ([candidates.py](https://github.com/axoviq-ai/synthadoc/blob/22b4412df8089e5628eb7a7c9e568711a3ce82f8/synthadoc/cli/candidates.py), [http_server.py](https://github.com/axoviq-ai/synthadoc/blob/22b4412df8089e5628eb7a7c9e568711a3ce82f8/synthadoc/integration/http_server.py)).

**Adoption is through familiar knowledge-work surfaces.** The engine exposes the same wiki through CLI, HTTP, MCP, Obsidian modals, export formats, and local files. Built-in and installed skills extend source extraction through `SKILL.md` manifests and importable Python entry scripts ([skill_agent.py](https://github.com/axoviq-ai/synthadoc/blob/22b4412df8089e5628eb7a7c9e568711a3ce82f8/synthadoc/agents/skill_agent.py), [registry.py](https://github.com/axoviq-ai/synthadoc/blob/22b4412df8089e5628eb7a7c9e568711a3ce82f8/synthadoc/skills/registry.py), [main.ts](https://github.com/axoviq-ai/synthadoc/blob/22b4412df8089e5628eb7a7c9e568711a3ce82f8/obsidian-plugin/src/main.ts), [export_agent.py](https://github.com/axoviq-ai/synthadoc/blob/22b4412df8089e5628eb7a7c9e568711a3ce82f8/synthadoc/agents/export_agent.py)).

## Artifact analysis

- **Storage substrate:** `files` - The central retained knowledge artifact is a directory of Markdown wiki pages and related files; SQLite sidecars provide audit, cache, queue, citation, embedding, and lifecycle state around that file corpus.
- **Representational form:** `prose` `symbolic` `parametric` - Prose Markdown is combined with YAML frontmatter, `[[wikilinks]]`, citation markers, lifecycle enums, routing lists, skill manifests, SQLite schemas, vectors, and exported graph formats.
- **Lineage:** `authored` `imported` - Pages are compiled from imported sources and source sidecars, while skills, routing, lifecycle policy, integration code, and user-installed overrides are authored system-definition artifacts.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` - Wiki pages answer queries and fill context packs as knowledge; status, lint, candidates, routing, search/rerank, lifecycle, skills, hooks, and provider/config surfaces shape inclusion, validation, ordering, and workflow behavior.

**Compiled wiki pages.** Storage substrate: files under `wiki/`, with candidate pages staged under `wiki/candidates/` when the staging policy is active. Representational form: mixed prose and symbolic Markdown/YAML; `status`, `confidence`, `sources`, `aliases`, `categories`, `lint_warnings`, citations, and `[[wikilinks]]` are machine-consumed. Lineage: LLM-derived from imported sources, with source hashes and extracted sidecars recording where the content came from; re-ingest or lint can update status and page body. Behavioral authority: mostly knowledge artifact authority when pages answer queries, fill context packs, export to `llms-full.txt`, or support human reading. Status, lint warnings, and candidate placement add system-definition authority because they gate inclusion, review, lifecycle, and export filters.

**Extracted source sidecars and claim citations.** Storage substrate: `.synthadoc/extracted/` text and pagemap sidecars plus `audit.db` `claim_citations` rows. Representational form: prose source text, symbolic line ranges, and SQLite rows. Lineage: imported source documents are the source material; citation markers are derived by the ingest citation pass and validated later by lint. Behavioral authority: evidence and audit authority. They let humans and tools inspect whether compiled claims can be traced back, but the citation pass is fail-open: on LLM or parse failure it returns the original section with no citations, so "every claim is cited" is an aspiration rather than a hard invariant ([ingest_agent.py](https://github.com/axoviq-ai/synthadoc/blob/22b4412df8089e5628eb7a7c9e568711a3ce82f8/synthadoc/agents/ingest_agent.py), [lint_agent.py](https://github.com/axoviq-ai/synthadoc/blob/22b4412df8089e5628eb7a7c9e568711a3ce82f8/synthadoc/agents/lint_agent.py)).

**Search, routing, and context-pack artifacts.** Storage substrate: in-memory BM25 corpus cache, optional `embeddings.db`, `ROUTING.md`, and generated context-pack Markdown/JSON. Representational form: symbolic route headings and slugs, distributed-vector embeddings, and prose excerpts. Lineage: derived from current wiki page text, alias frontmatter, routing files, and query goals. Behavioral authority: ranking, filtering, and context-selection authority. These artifacts decide which retained pages reach an answer prompt or external agent context, but they do not by themselves promote a claim's trust status.

**Audit, job, cache, lifecycle, logs, and telemetry.** Storage substrate: SQLite databases and log files under `.synthadoc/` plus `log.md`. Representational form: symbolic rows and JSON/log prose. Lineage: runtime operations, scheduled runs, source hashes, token/cost accounting, query calls, lifecycle transitions, citation failures, and job outcomes. Behavioral authority: orchestration, retry, cost, governance, and audit authority. Query history is retained, but in the inspected code it is not distilled into future behavior; it is an operator record rather than trace-derived learning.

**Skills, hooks, providers, and integration code.** Storage substrate: repository files, wiki/global skill folders, config files, Obsidian plugin code, and hook commands. Representational form: executable code plus symbolic manifests and prose `SKILL.md` bodies. Lineage: authored system-definition artifacts, with optional user-installed skill overrides. Behavioral authority: extraction routing, provider choice, hook firing, API access, and UI workflow authority.

**Promotion path.** Synthadoc has a clear promotion path from imported source -> draft wiki page or candidate -> lint/adversarial/citation/lifecycle review -> active page -> exported/context-packed knowledge. It has a weaker promotion path from "retrieved often" or "queried often" into future behavior: query logs and telemetry are retained, but they do not currently update routing, ranking, or page authority.

## Comparison with Our System

| Dimension | Synthadoc | Commonplace |
|---|---|---|
| Primary purpose | End-user wiki compiler for arbitrary source documents and local knowledge bases | Methodology KB for agent-operated knowledge-base design |
| Main substrate | Markdown wiki files plus SQLite operational sidecars | Git-tracked Markdown artifacts, type specs, schemas, generated indexes, review gates |
| Retrieval | BM25, optional vector rerank, query decomposition, routing branches, LLM answer synthesis, context packs | `rg`, curated indexes, descriptions, authored links, skills, review workflows |
| Governance | Lint, citation validation, lifecycle states, candidate staging, audit DB, Obsidian modals | Collection contracts, source-pinned reviews, validation, semantic gates, link vocabulary |
| Activation | Explicit query/search/context/export calls | Mostly explicit pull through search/index/link/skill workflows |

Synthadoc is closest to Commonplace in its commitment to durable, inspectable artifacts. Both systems reject "memory equals opaque vector store" as the primary design. Synthadoc is more productized around end-user UX: Obsidian modals, source-view citation chips, lifecycle dashboards, background jobs, HTTP routes, exports, and provider configuration are first-class. Commonplace is more explicit about type-level semantics, collection contracts, link vocabulary, and code-grounded review artifacts.

The largest divergence is authority. Synthadoc is willing to let an LLM compile source documents directly into a wiki, then use lint and lifecycle machinery to clean up the result. Commonplace slows promotion by requiring type contracts, source review, citation discipline, and explicit validation before claims gain durable methodological weight. Synthadoc's approach is attractive for operational ingestion, but it needs strong guardrails because page prose can become the user's apparent source of truth.

**Read-back:** `pull` - Retained wiki content returns through explicit query, search, context-pack, export, CLI, HTTP, MCP, or Obsidian actions; hooks emit operation events and `AGENTS.md` supplies static domain instructions, but the inspected code does not push accumulated wiki memory into an agent before it asks for it.

### Borrowable Ideas

**Claim citations as UI-native evidence handles.** Ready as a design pattern. Synthadoc's `^[file:L-L]` markers plus Source Viewer chip show how provenance can be visible at reading time without loading the whole source into every context. Commonplace could borrow the display idea while keeping stronger source-pinned review checks.

**Candidate staging for generated artifacts.** Ready for generated notes and reviews. A `candidates/` quarantine that is excluded from retrieval until promotion is a practical way to let agents draft aggressively without polluting the canonical KB.

**Lifecycle states with an audit trail.** Worth borrowing selectively. Commonplace has `status` frontmatter and archive conventions; Synthadoc's explicit page-state table and lifecycle-event log would help if note lifecycle transitions become frequent enough to justify a sidecar.

**Routing branches as an optional context-selection layer.** Needs a concrete large-corpus use case. `ROUTING.md` is a compact, inspectable selector between free-text search and fully typed routing. Commonplace could use an analogous branch map for large collections, but only if it stays reviewable and does not replace authored links.

**Context packs as handoff artifacts.** Ready for read-only workflows. A goal -> decomposed searches -> budgeted excerpts pack is a good shape for giving another agent bounded evidence without turning the whole KB into prompt stuffing.

**Do not borrow fail-open provenance as trust.** Synthadoc correctly favors ingest completion, but Commonplace should not let missing citation annotation silently preserve the same authority as fully grounded claims.

## Write-side placement

**Write agency:** `automatic` `manual` — the review describes system-driven generation, extraction, consolidation, or update of retained artifacts rather than only manual authoring.

**Curation operations:** `dedup` `synthesize` `invalidate` `decay` `promote` — the existing review evidence identifies automatic store-changing operations matching these curation classes.

## Curiosity Pass

The most important implementation caveat is the MCP adapter. At this commit, `create_mcp_server()` calls `Orchestrator.ingest(source, auto_confirm=True)` even though `Orchestrator.ingest()` accepts only `source` and `force`; it also treats `Orchestrator.lint()` as if it returned a lint report rather than a job id ([mcp_server.py](https://github.com/axoviq-ai/synthadoc/blob/22b4412df8089e5628eb7a7c9e568711a3ce82f8/synthadoc/integration/mcp_server.py), [orchestrator.py](https://github.com/axoviq-ai/synthadoc/blob/22b4412df8089e5628eb7a7c9e568711a3ce82f8/synthadoc/core/orchestrator.py)). Treat MCP as an intended surface, not a verified working memory channel in this revision.

The README's "autonomous self-optimization" framing is stronger than the code-grounded mechanism. The code has caches, routing, query decomposition, lifecycle checks, staging, and lint; I did not find a loop that learns durable new behavior from query/session traces. That is why this review does not carry `trace-derived`.

The citation system is unusually concrete for an LLM wiki, but it is not a proof system. Citation annotation is an LLM pass over truncated numbered source text, with fallback to unannotated content. Lint can catch malformed, broken, or out-of-range markers; it cannot prove every substantive paragraph has a correct support line.

Candidate promotion is simple file movement plus optional index update. That is good for inspectability, but it means promotion authority depends on surrounding workflows to refresh indexes, embeddings, audit state, and lifecycle state consistently.

The query gap detector is more elaborate than ordinary BM25 thresholding. Its extra lexical heuristics are useful, but they also encode domain-language assumptions; multilingual/CJK handling is explicitly special-cased.

## What to Watch

- Whether the MCP server API mismatch is fixed. If MCP becomes reliable, Synthadoc becomes a more direct agent-memory surface; if not, the real adoption path remains CLI/HTTP/Obsidian.
- Whether citation coverage becomes measurable as a first-class quality metric, not just marker validation. That would determine whether compiled pages can safely carry stronger authority.
- Whether query logs, job histories, or telemetry begin to update routing, ranking, scaffold, or lint policy. That would change the trace-derived placement.
- Whether candidate promotion updates embedding, lifecycle, audit, and routing state consistently across CLI, HTTP, and Obsidian entry points.
- Whether `ROUTING.md` remains an inspectable operator artifact or becomes LLM-maintained hidden state. The former is borrowable; the latter would be harder to review.
- Whether context packs get source-line provenance threaded through the excerpt output, not just page-level source/confidence metadata.

Relevant Notes:

- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Synthadoc separates wiki pages, citations, search/routing state, audit logs, skill manifests, and integration code by substrate, form, lineage, and authority.
- [Import External Knowledge Into Agent Memory](../../notes/agent-memory-requirements/import-external-knowledge.md) - exemplifies: Synthadoc's core loop imports external documents into a durable agent-readable wiki.
- [Preserve Evidence Without Loading History](../../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md) - exemplifies: claim citations and source sidecars preserve evidence handles without loading raw sources by default.
- [Keep Compiled Views Aligned With Source Artifacts](../../notes/agent-memory-requirements/keep-compiled-views-aligned.md) - relates: lifecycle stale/archive checks track when compiled pages drift from source files.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Synthadoc stores a wiki, but memory read-back is still mostly explicit pull.
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) - illustrates: Synthadoc frontloads compilation and uses retrieval/routing/context packs to limit prompt volume.
