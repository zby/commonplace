---
description: "Synthadoc review: local LLM wiki compiler with Markdown pages, provenance, lifecycle audit, query agents, routing, SSE UI, and context packs"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-05"
---

# Synthadoc

Synthadoc, from `axoviq-ai/synthadoc`, is a local-first LLM wiki engine. It ingests source documents and URLs into a persistent Markdown wiki, maintains citations, lifecycle state, audit records, routing, and query surfaces, and exposes the same knowledge store through CLI, HTTP, SSE web chat, MCP, and an Obsidian plugin.

**Repository:** https://github.com/axoviq-ai/synthadoc

**Reviewed commit:** [a77bdaeace7b3a461837936090624462690ee4ed](https://github.com/axoviq-ai/synthadoc/commit/a77bdaeace7b3a461837936090624462690ee4ed)

**Last checked:** 2026-06-05

## Core Ideas

**The wiki is the compiled memory artifact.** Synthadoc's own framing is that it compiles knowledge at ingest time rather than synthesizing everything at query time; the durable output is a folder of Markdown pages with YAML frontmatter, wikilinks, lifecycle state, confidence, sources, and citation markers ([README.md](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/README.md), [synthadoc/storage/wiki.py](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/synthadoc/storage/wiki.py)).

**Ingest is a multi-pass agent pipeline.** `IngestAgent` extracts source text through skills, analyzes entities/tags/summary, searches existing pages, asks an LLM to choose create/update/flag/skip, writes or stages pages, adds line-range citations, updates overview/index/routing when applicable, and records ingest and citation metadata in `audit.db` ([synthadoc/agents/ingest_agent.py](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/synthadoc/agents/ingest_agent.py), [synthadoc/skills/registry.py](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/synthadoc/skills/registry.py)).

**The system treats provenance and lifecycle as first-class store state.** `audit.db` has tables for ingests, audit events, queries, claim citations, page states, lifecycle events, scheduled runs, chat sessions, and chat messages; lint validates citation markers, promotes drafts, marks stale or archived pages, syncs manual frontmatter edits, and stores adversarial warnings in page frontmatter ([synthadoc/storage/log.py](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/synthadoc/storage/log.py), [synthadoc/agents/lint_agent.py](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/synthadoc/agents/lint_agent.py)).

**Querying is retrieval plus live operational context.** `QueryAgent` decomposes questions, optionally selects `ROUTING.md` branches, expands aliases, runs BM25 with optional vector re-ranking, adds `purpose.md`, product knowledge guides, and live audit/queue/lifecycle snapshots when the question asks for them, then synthesizes an answer with citations and gap detection ([synthadoc/agents/query_agent.py](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/synthadoc/agents/query_agent.py), [synthadoc/storage/search.py](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/synthadoc/storage/search.py), [synthadoc/core/routing.py](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/synthadoc/core/routing.py)).

**Action agents blur query and operation.** Before ordinary retrieval, `QueryAgent` can invoke `ActionAgent`, which regex-detects action intent, asks an LLM to parse parameters, and dispatches lint, ingest, scaffold, schedule, and lifecycle operations through the orchestrator or local stores ([synthadoc/agents/action_agent.py](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/synthadoc/agents/action_agent.py), [synthadoc/core/orchestrator.py](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/synthadoc/core/orchestrator.py)).

**Context efficiency is engineered as precompiled pages plus scoped retrieval.** Synthadoc keeps source-scale detail out of the live prompt by compiling it into pages and sidecars, then assembling only top candidate excerpts, `purpose.md`, live data, or help pages for a query. It also has query decomposition, route scoping, optional vector re-ranking, cache invalidation by wiki epoch, and a separate context-pack builder with token budgets ([synthadoc/agents/query_agent.py](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/synthadoc/agents/query_agent.py), [synthadoc/agents/context_agent.py](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/synthadoc/agents/context_agent.py), [synthadoc/core/cache.py](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/synthadoc/core/cache.py)).

**Adoption surfaces are unusually broad for a local wiki.** The same store is exposed by CLI commands, localhost FastAPI endpoints, SSE streaming chat, MCP tools, web UI hints, Obsidian commands, export formats, scheduling, and candidate staging ([synthadoc/integration/http_server.py](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/synthadoc/integration/http_server.py), [synthadoc/integration/mcp_server.py](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/synthadoc/integration/mcp_server.py), [obsidian-plugin/src/main.ts](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/obsidian-plugin/src/main.ts), [web-ui/src/useQueryStream.ts](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/web-ui/src/useQueryStream.ts)).

## Artifact analysis

- **Storage substrate:** `files` `sqlite` `vector` - The central store is wiki Markdown plus sidecar extracted text and logs under the wiki root; `.synthadoc/audit.db`, `jobs.db`, `cache.db`, and optional `embeddings.db` hold audit, queue, cache, session, citation, and vector-ranking state ([synthadoc/storage/wiki.py](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/synthadoc/storage/wiki.py), [synthadoc/storage/log.py](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/synthadoc/storage/log.py), [synthadoc/core/queue.py](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/synthadoc/core/queue.py), [synthadoc/storage/search.py](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/synthadoc/storage/search.py)).
- **Representational form:** `prose` `symbolic` `parametric` - Page bodies, generated summaries, product guides, hints, and AGENTS guidance are prose; frontmatter, citations, queue rows, lifecycle rows, route tables, cache keys, and configs are symbolic; optional fastembed vectors are parametric ranking artifacts ([synthadoc/knowledge/synthadoc-overview.md](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/synthadoc/knowledge/synthadoc-overview.md), [synthadoc/agents/hint_engine.py](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/synthadoc/agents/hint_engine.py), [synthadoc/storage/search.py](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/synthadoc/storage/search.py)).
- **Lineage:** `authored` `imported` `trace-extracted` - Config, skills, guides, hints, routing, and scaffold prompts are authored; wiki pages and source sidecars are imported and LLM-derived from user documents, URLs, transcripts, web search results, or manual edits; audit/query/job/chat/lifecycle rows are trace-extracted from system operation and user interaction ([synthadoc/agents/ingest_agent.py](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/synthadoc/agents/ingest_agent.py), [synthadoc/storage/log.py](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/synthadoc/storage/log.py), [synthadoc/integration/http_server.py](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/synthadoc/integration/http_server.py)).
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` - Wiki pages, citations, sidecars, logs, and exported packs advise as knowledge; `AGENTS.md`, bundled guides, hints, skills, and action parsing instruct; job status, lifecycle transitions, source-scope checks, content-size limits, and blocked-domain handling enforce operational constraints; `ROUTING.md` and aliases route retrieval; lint and citation checks validate; BM25/vector scores and route selection rank query context ([synthadoc/agents/query_agent.py](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/synthadoc/agents/query_agent.py), [synthadoc/agents/lint_agent.py](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/synthadoc/agents/lint_agent.py), [synthadoc/core/orchestrator.py](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/synthadoc/core/orchestrator.py)).

**Wiki pages.** Storage substrate: Markdown files under `wiki/`. Representational form: prose body plus symbolic YAML frontmatter. Lineage: imported and LLM-derived from source text, with `sources` frontmatter and claim citation markers back to extracted text. Behavioral authority: knowledge artifact in ordinary query and export paths, with weak system-definition authority where lifecycle state, confidence, categories, aliases, and orphan flags affect retrieval, lint, UI, and routing.

**Source sidecars and citation rows.** Storage substrate: `.synthadoc/extracted/*.txt`, PDF pagemap files, and `claim_citations` / citation-failure rows in `audit.db`. Representational form: prose source text plus symbolic line ranges and failure metadata. Lineage: imported from source extraction and generated citation annotation. Behavioral authority: provenance evidence for humans, Obsidian provenance UI, audit CLI, lint validation, and repair decisions.

**Audit, queue, cache, and session tables.** Storage substrate: SQLite databases under `.synthadoc`. Representational form: symbolic rows with JSON payloads, costs, timestamps, lifecycle states, progress, chat messages, and query records. Lineage: trace-extracted from system operation. Behavioral authority: knowledge for live-data answers, status endpoints, job control, session-mode selection, and cache reuse; not promoted into durable wiki claims unless a user explicitly ingests or writes such material.

**Routing, scaffold, and guides.** Storage substrate: `ROUTING.md`, `wiki/index.md`, `wiki/purpose.md`, root `AGENTS.md`, bundled `synthadoc/knowledge/*.md`, and `hints.json`. Representational form: prose plus symbolic link/category/keyword structures. Lineage: authored or scaffold-generated from domain and current page slugs. Behavioral authority: instruction, routing, and coarse context; query and ingest agents read these surfaces to decide scope, retrieval branches, help-answer context, and web UI suggestions.

**Search indexes and embeddings.** Storage substrate: in-memory BM25 corpus cache and optional `embeddings.db`. Representational form: symbolic tokens plus parametric vectors. Lineage: derived from current wiki pages and invalidated or rebuilt after writes. Behavioral authority: ranking and selection of read-back context, not standalone knowledge.

Promotion path: the strongest path is imported source -> draft wiki page with citations -> lint/adversarial/citation/lifecycle checks -> active page -> routed query/export/context-pack surface. Candidate staging adds a review gate before new generated pages influence the main wiki.

## Comparison with Our System

| Dimension | Synthadoc | Commonplace |
|---|---|---|
| Primary purpose | Compile arbitrary source material into a local domain wiki | Maintain methodology knowledge for agent-operated KBs |
| Main artifact | Markdown wiki page with frontmatter, citations, lifecycle state | Typed Markdown note/review/instruction/source with collection contract |
| Storage substrate | Wiki files plus SQLite operational databases and optional embeddings | Repository files, Git history, generated indexes, validation outputs |
| Write path | LLM ingest, scaffold, lint, lifecycle, schedule, candidates, manual edits | Human/agent authored artifacts, snapshots, indexes, validation, review gates |
| Read-back | Both: query-time context injection plus explicit search/context/export tools | Mostly explicit pull through `rg`, indexes, links, skills, and instructions |
| Governance | Citation markers, lifecycle rows, lint/adversarial checks, audit DB | Type specs, collection contracts, citations, review gates, deterministic validation, Git |

Synthadoc is closer to Commonplace than most RAG systems because it believes the durable artifact should be human-readable Markdown, not hidden chunks. The difference is authority and source of truth. Synthadoc's wiki pages are LLM-compiled operational knowledge products; Commonplace artifacts are typed claims, procedures, references, and reviews whose shape is constrained by collection and type contracts.

The most valuable contrast is that Synthadoc makes provenance operational at product scale: citations, sidecars, lifecycle rows, audit endpoints, and Obsidian provenance surfaces all ship together. Commonplace has stronger artifact typing and review contracts, but weaker end-user product surfaces for asking "which claim came from which source line?" or "which pages are stale right now?"

The risk is that Synthadoc gives generated pages a large role in the knowledge graph before semantic review comparable to Commonplace's review gates. Its adversarial lint is a useful second-model check, but it stores warnings rather than proving that each generated claim is faithful to its source.

### Borrowable Ideas

**Claim-provenance as a queryable database.** Ready for a concrete source-review workflow. Commonplace could keep Markdown citations as the canonical artifact while also emitting a local citation table for filtering by source, broken reference, or reviewed claim.

**Lifecycle rows separate from page frontmatter.** Needs a use case. Commonplace currently relies on frontmatter and Git; a small audit table could help for high-volume source snapshots or review reruns, but it should not displace Git as source of truth.

**Candidate staging for generated pages.** Ready for trace/source-derived drafts. Synthadoc's `wiki/candidates/` is a useful boundary: generated material can be visible for review without immediately entering retrieval, lint, or curated navigation.

**Context packs as a first-class export.** Ready now. Commonplace could expose a `commonplace context build` command that assembles note excerpts under a token budget with confidence, source, and omitted-item metadata.

**Adaptive UI hints from store state.** Needs a product surface. Synthadoc's hint engine is simple, but using lifecycle, gap, or recent-query signals to suggest next actions would make a KB feel more operated than merely browsed.

**Do not borrow generated AGENTS guidance without review.** Synthadoc can regenerate `AGENTS.md` from current wiki state; Commonplace should keep instruction artifacts behind explicit review because they have high behavioral authority.

## Write side

**Write agency:** `manual` `automatic` - Users can edit Markdown, frontmatter, candidates, lifecycle state, routing, config, and schedules manually; the system also creates, updates, flags, stages, annotates, promotes, archives, embeds, caches, routes, scaffolds, and logs artifacts through ingest, lint, query, scheduler, and action-agent paths.

**Curation operations:** `consolidate` `evolve` `synthesize` `invalidate` `promote` - `_update_overview` and scaffold consolidate wiki state into overview/index/purpose/guidance surfaces; ingest evolves existing pages by appending new sections from new sources; scaffold can synthesize new navigation and guidance artifacts from current wiki state; ingest/lint mark pages contradicted, stale, archived, or unresolved; lint promotes clean drafts to active and candidate promotion moves staged pages into the queryable wiki ([synthadoc/agents/ingest_agent.py](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/synthadoc/agents/ingest_agent.py), [synthadoc/agents/lint_agent.py](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/synthadoc/agents/lint_agent.py), [synthadoc/agents/scaffold_agent.py](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/synthadoc/agents/scaffold_agent.py), [synthadoc/integration/http_server.py](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/synthadoc/integration/http_server.py)).

Automatic writes are not primarily agent-trace learning. They are source-ingest and store-maintenance operations. The code records chat, query, job, audit, and lifecycle traces, and some of those traces can be read as live data, but I did not find a durable distillation loop that turns agent/session traces into new policies, skills, validators, routing rules, or learned parameters. For that reason this review does not carry the `trace-derived` tag.

## Read-back

**Read-back:** `both` - Stored memory is pulled explicitly through CLI/HTTP/MCP search, query, export, context-pack, audit, and provenance commands; it is also pushed to the answering model by the query pipeline, which assembles selected pages, `purpose.md`, live data, product guides, and citations before the model call.

**Read-back signal:** `coarse` `identifier` `inferred / lexical` `inferred / embedding` `inferred / judgment` - `purpose.md` and system help can be coarse context; aliases, lifecycle/job keywords, citation/source filters, and `ROUTING.md` branches provide identifier-like narrowing; BM25 and trigger keywords are lexical; optional fastembed vectors re-rank candidates; decomposition and route-branch selection use LLM judgment ([synthadoc/agents/query_agent.py](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/synthadoc/agents/query_agent.py), [synthadoc/storage/search.py](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/synthadoc/storage/search.py), [synthadoc/agents/_routing.py](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/synthadoc/agents/_routing.py)).

**Faithfulness tested:** `no` - The repository has tests for mechanics, storage, streaming, routing, hints, query paths, citation validation, and lifecycle behavior, but I did not find a WITH/WITHOUT or perturbation test showing that injected wiki context is faithfully used by the model rather than merely present.

**Direction edge cases.** A user asking `synthadoc query` is pull at the application boundary, but push for the answering model because `QueryAgent` has already retrieved and assembled memory into the synthesis prompt. MCP `synthadoc_search`, context packs, exports, provenance endpoints, and audit commands remain ordinary pull surfaces because the consumer deliberately asks for stored material.

**Injection point.** Query read-back happens before the provider call: context is assembled into the synthesis prompt and then passed to `provider.complete` or `provider.complete_stream`. SSE streaming is the transport for status/tokens/citations/gap/hints back to the UI; it is not a separate post-action memory read-back path ([synthadoc/agents/query_agent.py](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/synthadoc/agents/query_agent.py), [synthadoc/integration/http_server.py](https://github.com/axoviq-ai/synthadoc/blob/a77bdaeace7b3a461837936090624462690ee4ed/synthadoc/integration/http_server.py)).

**Selection, scope, and complexity.** The default query path keeps only top candidates and truncates each page to an excerpt, but complexity can still be high: `purpose.md`, product knowledge pages, live audit state, route branches, aliases, page snippets, citations, gap suggestions, and action results can all change the answer path. Context packs make the budget explicit by returning selected and omitted pages with estimated tokens.

**Authority at consumption.** Retrieved pages and live data are advisory context for the synthesis prompt. Action-agent dispatch has stronger operational authority because a natural-language request can enqueue ingest/lint/scaffold jobs or mutate lifecycle state after LLM parameter extraction. Lifecycle states and citation failures can also constrain what humans and tools trust, but they do not enforce answer faithfulness by themselves.

**Other consumers.** Humans consume the same store through Obsidian, web UI, CLI reports, provenance modals, lifecycle pages, candidate review, GraphML/JSON exports, and logs. Those surfaces matter for adoption and governance, but they are consumer surfaces rather than additional model read-back directions.

## Curiosity Pass

**The most distinctive part is not the query agent.** The query agent is a competent hybrid retrieval/synthesis pipeline, but the more unusual design is the ingest-time compilation plus lifecycle/provenance machinery around plain Markdown.

**The action agent turns chat into a control surface.** Natural-language requests can start jobs and change lifecycle state. That makes the query UI more useful, but it also raises the authority of action parsing: a false positive is no longer just a bad answer.

**The bundled knowledge guides are baseline documentation, not accumulated memory.** They help answer questions about Synthadoc itself, but they should not be confused with read-back from a user's wiki.

**Session storage is underused as memory.** The HTTP server records chat sessions and messages and uses session existence to choose a UI mode, but the query code marks `session_id` as reserved for future history and does not feed prior chat messages into answers at this commit.

**The provenance model is stronger structurally than semantically.** Line-range citation markers and broken-citation lint are valuable, but the Pass 4 annotator can only be as faithful as the LLM output and the sanity check. Static code shows the mechanism, not citation correctness in generated pages.

## What to Watch

- Whether query sessions start reading prior `chat_messages`; that would turn web chat from single-turn wiki query into conversational memory and change the artifact analysis for session rows.
- Whether citation annotation gains quote-span verification or source-snippet display in the generated Markdown itself; that would narrow the gap between structural provenance and semantic citation faithfulness.
- Whether adversarial lint findings become gates that block activation instead of warnings in frontmatter; that would strengthen the validation/enforcement authority of generated pages.
- Whether `ROUTING.md` maintenance becomes evidence-aware rather than slug/category based; that would make route selection a stronger context-engineering primitive.
- Whether generated `AGENTS.md` guidance gets review, diff, or rollback semantics; that file can shape future ingest/query behavior more strongly than ordinary wiki pages.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Synthadoc stores a wiki, but only selected query/context/action paths make stored material affect a model call.
- [Axes of artifact analysis](../../../notes/axes-of-artifact-analysis.md) - applies: Synthadoc's pages, audit rows, citations, route tables, guides, and embeddings differ by substrate, form, lineage, and authority.
- [Context efficiency is the central design concern in agent systems](../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) - exemplifies: Synthadoc shifts work to ingest-time compilation and bounded query/context-pack assembly.
- [Use trace-derived extraction as meta-learning](../../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - boundary case: Synthadoc records operational traces, but this commit does not distill them into durable learned behavior.
- [Knowledge artifact](../../../notes/definitions/knowledge-artifact.md) - classifies: wiki pages, citations, sidecars, query logs, and exported context packs mostly advise as evidence or context.
- [System-definition artifact](../../../notes/definitions/system-definition-artifact.md) - classifies: routing, lifecycle, lint rules, generated `AGENTS.md`, action parsing, and scheduler/config surfaces can instruct, route, validate, or constrain behavior.
- [Behavioral authority](../../../notes/definitions/behavioral-authority.md) - applies: the same retained page can be advisory in a query, ranked by retrieval, validated by lint, or suppressed by lifecycle state.
- [Lineage](../../../notes/definitions/lineage.md) - applies: source refs, hashes, line citations, audit rows, and lifecycle events determine invalidation and provenance.
