---
description: "Link review: local Markdown wiki memory with raw captures, reviewed memory pages, bounded query packets, MCP/CLI skills, validation, and local viewer"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
status: current
last-checked: "2026-06-18"
---

# Link

Link, by Gowtham S, is a local agent-memory layer that stores raw sources and structured Markdown wiki pages on disk, then exposes bounded recall through a Python CLI, MCP server, official skills, and local web viewer. At the reviewed commit it implements source-backed wiki pages, explicit reviewable memory pages, session capture and memory proposal flows, lexical/SQLite-FTS search, graph-neighborhood context, validation, operation journals, local backup, team-sync guidance, and agent integration installers.

**Repository:** https://github.com/gowtham0992/link

**Reviewed commit:** [a1aaa55050a0c9db221771e4424ab4f7a56b3e2a](https://github.com/gowtham0992/link/commit/a1aaa55050a0c9db221771e4424ab4f7a56b3e2a)

**Last checked:** 2026-06-18

## Core Ideas

**The wiki is the shared memory substrate.** Link's top-level contract divides memory into immutable `raw/`, structured `wiki/`, and `LINK.md` schema instructions; the README describes the wiki as the storage layer and durable local memory as the product ([LINK.md](https://github.com/gowtham0992/link/blob/a1aaa55050a0c9db221771e4424ab4f7a56b3e2a/LINK.md), [README.md](https://github.com/gowtham0992/link/blob/a1aaa55050a0c9db221771e4424ab4f7a56b3e2a/README.md)). The system is deliberately multi-surface: CLI, MCP tools, skills, and the web viewer all read and write the same local files rather than maintaining separate agent profiles ([mcp_package/link_mcp/server.py](https://github.com/gowtham0992/link/blob/a1aaa55050a0c9db221771e4424ab4f7a56b3e2a/mcp_package/link_mcp/server.py), [skills/link-memory/SKILL.md](https://github.com/gowtham0992/link/blob/a1aaa55050a0c9db221771e4424ab4f7a56b3e2a/skills/link-memory/SKILL.md)).

**Memory pages are explicit durable state, not hidden chat summaries.** `write_memory_page()` creates Markdown pages under `wiki/memories/` with typed frontmatter for memory type, scope, visibility, status, source, review state, optional review/expiry dates, and tags; it refuses likely duplicates or conflicts unless the caller opts in, appends to `wiki/log.md`, updates the index, and rebuilds backlinks when wired ([mcp_package/link_core/memory.py](https://github.com/gowtham0992/link/blob/a1aaa55050a0c9db221771e4424ab4f7a56b3e2a/mcp_package/link_core/memory.py)). Updates append to the memory body, increment `update_count`, clear prior review metadata, and mark the memory pending review again.

**Context efficiency is budgeted packet construction.** `query_link()` does not answer the user; it returns a compact context packet combining relevant memories, ranked wiki search results, and graph-neighborhood pages under small/medium/large budgets, with trimmed primary/neighbor text, estimated tokens, `has_more` flags, and follow-up tool suggestions ([mcp_package/link_core/query.py](https://github.com/gowtham0992/link/blob/a1aaa55050a0c9db221771e4424ab4f7a56b3e2a/mcp_package/link_core/query.py)). Search uses exact/title/alias/tag/TLDR/full-text scoring plus an optional in-memory SQLite FTS index rebuilt from Markdown, while `get_context()` expands from the best page to inbound and forward wikilinks rather than dumping the whole wiki ([mcp_package/link_core/search.py](https://github.com/gowtham0992/link/blob/a1aaa55050a0c9db221771e4424ab4f7a56b3e2a/mcp_package/link_core/search.py), [mcp_package/link_core/wiki.py](https://github.com/gowtham0992/link/blob/a1aaa55050a0c9db221771e4424ab4f7a56b3e2a/mcp_package/link_core/wiki.py)).

**Trace capture is review-first.** `capture_session()` saves long chat/session notes as raw Markdown under `raw/memory-captures/` and returns proposals, but its MCP docstring states that it does not create durable memory pages; `accept_capture()` later recomputes proposals from the saved capture and writes only the selected item through the duplicate/conflict-safe memory creation path ([mcp_package/link_core/capture.py](https://github.com/gowtham0992/link/blob/a1aaa55050a0c9db221771e4424ab4f7a56b3e2a/mcp_package/link_core/capture.py), [mcp_package/link_mcp/server.py](https://github.com/gowtham0992/link/blob/a1aaa55050a0c9db221771e4424ab4f7a56b3e2a/mcp_package/link_mcp/server.py)). That makes the trace-derived loop durable but approval-gated.

**Trust is mostly structural and provenance-oriented.** Link validates required paths, frontmatter fields, page-directory type alignment, required sections, dead wikilinks, backlinks freshness, review dates, expiry dates, and secret-looking values; readiness also checks schema markers, pending operation journals, memory counts, and validation state ([mcp_package/link_core/validation.py](https://github.com/gowtham0992/link/blob/a1aaa55050a0c9db221771e4424ab4f7a56b3e2a/mcp_package/link_core/validation.py), [mcp_package/link_core/status.py](https://github.com/gowtham0992/link/blob/a1aaa55050a0c9db221771e4424ab4f7a56b3e2a/mcp_package/link_core/status.py), [mcp_package/link_core/operations.py](https://github.com/gowtham0992/link/blob/a1aaa55050a0c9db221771e4424ab4f7a56b3e2a/mcp_package/link_core/operations.py)). The code verifies shape and lifecycle, not whether a remembered claim is semantically true.

**Adoption affordances are practical and local-first.** The product ships an MCP package, official skills, per-agent installers, a local viewer, backups, snapshots, team-sync guidance, and sharing visibility checks, while keeping raw sources and wiki pages inspectable as ordinary files ([mcp_package/README.md](https://github.com/gowtham0992/link/blob/a1aaa55050a0c9db221771e4424ab4f7a56b3e2a/mcp_package/README.md), [mcp_package/link_core/team_sync.py](https://github.com/gowtham0992/link/blob/a1aaa55050a0c9db221771e4424ab4f7a56b3e2a/mcp_package/link_core/team_sync.py), [integrations/README.md](https://github.com/gowtham0992/link/blob/a1aaa55050a0c9db221771e4424ab4f7a56b3e2a/integrations/README.md)).

## Artifact analysis

- **Storage substrate:** `files` `sqlite` `in-memory` — Durable state is local Markdown, JSON, logs, raw captures, backups, generated indexes, and schema markers under the Link root; SQLite FTS and Python indexes are derived in-memory access structures rebuilt from files.
- **Representational form:** `prose` `symbolic` — Wiki bodies, memory text, raw captures, source summaries, and skills are prose, while frontmatter, wikilinks, page categories, review fields, schema markers, operation journals, backlinks JSON, MCP tool schemas, and search indexes are symbolic.
- **Lineage:** `authored` `imported` `trace-extracted` — Pages and memories are authored by humans or agents, raw sources are imported into the workspace, and session captures plus accepted memory proposals are extracted from conversation/session traces.
- **Behavioral authority:** `knowledge` `instruction` `validation` `routing` `ranking` `learning` — Retrieved pages and memories advise future agents; `LINK.md`, skills, installers, and MCP tool instructions guide use; validators and operation journals gate shape/readiness; search, budgets, graph expansion, scope, review status, and project filters route and rank recall; capture/proposal flows turn traces into candidate durable memory.

**Wiki pages.** Storage substrate: `wiki/**/*.md` plus `_backlinks.json`, `index.md`, `log.md`, and `_link_schema.json`. Representational form: prose pages with symbolic frontmatter, wikilinks, types, aliases, tags, source counts, maturity, dates, and graph indexes. Lineage: authored or imported into the wiki from raw sources, then indexed from current file contents. Behavioral authority: knowledge when returned through `search_wiki`, `get_context`, `query_link`, or the viewer; routing/ranking when titles, aliases, tags, and links select later context.

**Memory pages.** Storage substrate: `wiki/memories/*.md`. Representational form: prose memory bodies wrapped in symbolic frontmatter for `memory_type`, `scope`, `visibility`, `status`, `review_status`, project, source, review/expiry dates, and tags. Lineage: authored through explicit `remember_memory`/CLI calls or trace-extracted from accepted capture proposals. Behavioral authority: knowledge and personalization context; review status, active/stale/archive state, expiry, project scope, and visibility affect recall and sharing.

**Raw captures and proposals.** Storage substrate: `raw/memory-captures/*.md` and transient proposal payloads returned by CLI/MCP. Representational form: prose captured notes plus symbolic frontmatter and proposal records. Lineage: trace-extracted from chat/session notes; accepted proposals become memory pages with the capture path as source. Behavioral authority: learning and review input until accepted, then knowledge.

**Search, graph, and packet caches.** Storage substrate: `.link-cache/wiki-cache-v*.json`, in-memory token indexes, optional SQLite FTS tables, `_backlinks.json`, and runtime cache variables in the MCP server. Representational form: symbolic page signatures, normalized text, token/metadata indexes, snippets, graph nodes/edges, scores, and packet budgets. Lineage: derived from current wiki files and invalidated by signatures, mtimes, cache checks, or explicit rebuilds. Behavioral authority: ranking and routing for pull retrieval.

**Instruction and integration surfaces.** Storage substrate: `LINK.md`, `skills/link-*`, MCP server tool descriptions, integration installer scripts, and generated agent config/instructions. Representational form: prose instructions plus symbolic commands, tool names, and installer/config data. Lineage: authored package artifacts installed into agent environments. Behavioral authority: instruction and routing, because they tell agents when to call `health`, `brief`, `query`, `remember`, `validate`, and repair tools.

Promotion path: Link has a practical progression from raw capture to proposal to reviewed memory page, and from free wiki pages to schema-validated, backlink-indexed, queryable context. It does not promote memories into executable validators, hard gates on agent behavior, learned model weights, or automatic semantic contradiction repair.

## Comparison with Our System

| Dimension | Link | Commonplace |
|---|---|---|
| Primary purpose | Local multi-agent memory for preferences, project context, sources, and query packets | Git-native methodology KB for agent-operated knowledge-base design |
| Canonical artifact | Markdown wiki page or memory page under `wiki/` | Typed Markdown artifact under collection/type contracts |
| Source layer | `raw/` plus `wiki/sources/` pages and source-backed provenance | `kb/sources/` snapshots, reviews, citations, and source-grounded notes |
| Write path | Explicit remember/update/capture/accept/ingest flows with duplicate/conflict checks and review status | Agent/human edits, skills, validation, semantic review, indexes |
| Read path | MCP/CLI pull packets, memory brief, search, context graph, local viewer | Mostly pull through `rg`, indexes, links, skills, and loaded instructions |
| Governance | Schema marker, page validation, operation journals, review inbox, visibility/team-sync checks | Type specs, collection contracts, validators, semantic gates, review archives |

Link and Commonplace share the local-file bet: memory is inspectable, scriptable, and not locked inside a vendor conversation store. Link is more productized for day-to-day agent adoption: installers, MCP registry packaging, local viewer, skills, status checks, backup/snapshot, capture inbox, and sharing guidance are all first-class. Commonplace is stricter as a knowledge methodology corpus: each artifact belongs to a collection contract, citations are review obligations, and semantic review is part of the maintenance model.

The main divergence is granularity of authority. Link's memory pages can strongly influence a future agent, but their authority is encoded mainly by frontmatter, review state, tool guidance, and the host agent's obedience. Commonplace gives more files direct system-definition force through skills, type specs, validators, and review gates, while keeping theoretical notes explicitly advisory.

### Borrowable Ideas

**Make compact query packets a first-class CLI/MCP output.** Ready now. Commonplace already has indexes and search conventions, but a bounded packet with provenance, estimated size, and follow-up actions would reduce ad hoc full-file loading.

**Separate `scope` from `visibility`.** Ready now if Commonplace adds project/team sharing workflows. Link's split between relevance scope and sharing intent is cleaner than overloading one field for both.

**Use operation journals around multi-file writes.** Ready for risky commands. Link's pending/failed marker pattern gives status and doctor commands a concrete recovery surface after interrupted writes.

**Borrow capture inbox as a workshop intake pattern.** Needs a concrete workflow. Session captures that stay raw until accepted would fit Commonplace's workshop layer, especially for transforming long agent sessions into notes without making every transcript durable library content.

**Keep duplicate/conflict refusal in write tools.** Ready now for memory-like commands. Link's write path returns candidates and asks the agent to update or inspect before creating another memory.

**Do not borrow purely structural validation as semantic quality.** Link's validation is useful, but Commonplace should keep semantic gates for claims that become methodology guidance.

## Write side

**Write agency:** `manual` `automatic` — Humans and agents explicitly create/update/review/archive/forget memories, ingest raw sources, rebuild indexes, and validate the wiki; automatic code paths write operation markers, logs, generated backlinks/indexes, raw captures, and proposal payloads around those explicit commands.

**Curation operations:** `none` — Link performs duplicate/conflict detection, review-state changes, expiry/stale filtering, archive/forget lifecycle changes, and access-structure rebuilds, but I did not find an automatic operation that consolidates, deduplicates, evolves, synthesizes, invalidates, decays, or promotes already-stored memory without an explicit caller action.

### Trace-derived learning

**Trace source:** `session-logs` — `capture_session()` stores chat/session notes as raw capture files, and `propose_memories()`/`accept_capture()` can extract durable memory candidates from those notes.

**Learning scope:** `per-project` `cross-task` — Captures and accepted memories live in the local Link root or project-scoped wiki and can guide later sessions, tools, and agents.

**Learning timing:** `staged` — Trace material is saved, proposed, reviewed, and accepted in separate steps; Link does not silently learn durable memory from every live turn.

**Distilled form:** `prose` `symbolic` — Accepted memories become prose memory pages with symbolic frontmatter, review state, scope, visibility, tags, source, and lifecycle metadata.

**Extraction.** The extraction oracle is deterministic and conservative: `classify_memory_segment()` looks for explicit preference, decision, project-context, and user-fact cues, ignores uncertain language such as "maybe" or "not sure", assigns confidence scores, and attaches duplicate/conflict-aware follow-up actions ([mcp_package/link_core/memory.py](https://github.com/gowtham0992/link/blob/a1aaa55050a0c9db221771e4424ab4f7a56b3e2a/mcp_package/link_core/memory.py)). The durable write still goes through `remember_memory`, `update_memory`, or `accept_capture`.

**Survey fit.** Link fits the trace-to-reviewed-memory family: raw session traces are retained as source material, then a staged proposal/approval step distills a subset into memory pages. It strengthens the survey distinction between trace acquisition and autonomous curation: Link acquires and proposes from traces but does not automatically rewrite the standing memory store.

## Read-back

**Read-back:** `both` — Link memory normally reaches agents by pull through `query_link`, `memory_brief`, `recall_memory`, `search_wiki`, and `get_context`, but `memory_brief` is explicitly intended for session-start or pre-task priming and can push recent/relevant memory into the receiving agent when host instructions tell the agent to call it before work.

**Read-back signal:** `coarse` `inferred / lexical` — Startup briefs use coarse recent/type ordering when no query is supplied, while query briefs and `query_link` use lexical matching over memory/page titles, TLDRs, tags, bodies, wiki metadata, and optional SQLite FTS.

**Faithfulness tested:** `no` — The repository tests tool contracts, query packets, memory lifecycle, validation, MCP setup, and web views, but I did not find a with/without behavioral test proving that recalled memories change an agent's later behavior.

**Targeting and signal.** Pull retrieval is the strongest path: `query_link()` combines `recall_memories()`, wiki search, and graph context under budgets; `get_context()` expands the best page to inbound and forward links; `memory_brief(query=...)` returns query-relevant memory plus review warnings. The push-like path is mediated by instructions and agent workflow rather than a daemon that injects memory automatically into every model call: MCP instructions and skills tell agents to call `memory_brief` before personalized/project work, and a no-query brief selects recent active preferences, decisions, and project memories.

**Injection point.** Read-back happens before the answering or coding action, when an agent or host calls the MCP/CLI tool and inserts the returned JSON/text into context. Logs, backlinks, operation markers, captures, review-state updates, and cache rebuilds after writes are maintenance for future reads, not post-action read-back.

**Selection, scope, and complexity.** Selection is bounded by explicit limits: memory brief caps relevant memories, query budgets cap memory/search/context counts and character budgets, graph summaries bound node and edge counts, and `search_wiki` limits results. Complexity remains visible because packets include provenance, why-selected reasons, review warnings, follow-up actions, and budget reports. Recall quality is lexical and metadata-driven, not embedding or LLM-judgment based.

**Authority at consumption.** Retrieved memory and wiki pages are advisory knowledge unless the host agent treats a remembered preference or decision as a stronger instruction. MCP tool descriptions and Link skills carry higher instruction authority by telling agents when not to write memory, when to validate, and when to treat unreviewed memories as provisional.

**Faithfulness.** Link tests the structures that make read-back possible, but it does not measure whether an agent follows recalled preferences, avoids stale memory, or changes task behavior after memory is injected. Effective obedience remains a host-agent property.

**Other consumers.** Humans consume the same store through the local web viewer, health pages, graph pages, memory inbox, audit exports, backups, team-sync readiness, and plain Markdown files. That matters because review and sharing are human-governed even when agents perform the writes.

## Curiosity Pass

**The name hides a fairly complete lifecycle system.** Link is not only a search wrapper over Markdown; it has raw capture, review inbox, operation journals, schema migration, validation, local backup, visibility checks, and team-sync guidance.

**The trace-derived loop is intentionally conservative.** The extraction code uses cues and confidence scores, then asks for approval or update, rather than letting a summarizer continuously rewrite memory. That lowers autonomy but makes provenance and consent easier to audit.

**The review state affects trust more than retrieval.** Reviewed memories get a ranking boost and pending memories trigger guidance, but unreviewed active memories can still be recalled. Operators should not confuse "pending review surfaced" with "pending review excluded."

**The FTS index is an access structure, not a hidden source of truth.** SQLite is used in memory for retrieval over files; Markdown and JSON remain the durable memory substrate.

**`LINK.md` is a local schema by instruction, not an enforced parser.** Validators check broad type/section/frontmatter requirements, but the full page templates in `LINK.md` still depend on agent compliance.

## What to Watch

- Whether Link adds automatic prompt hooks that call `memory_brief` or `query_link` before every agent invocation; that would make read-back more clearly push rather than instruction-mediated.
- Whether memory review becomes a hard recall gate for high-impact preferences or decisions; that would change review status from guidance/ranking into enforcement.
- Whether proposal extraction moves from deterministic cue matching to LLM judgment; that would change the trace-derived oracle and likely require stronger provenance and review controls.
- Whether Link adds automatic consolidation or contradiction repair over existing memories; that would introduce real curation operations beyond acquisition and explicit lifecycle edits.
- Whether team-sync workflows start enforcing visibility through Git hooks or command gates rather than read-only guidance.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Link stores a local wiki, but memory affects agents only when CLI/MCP/skill read-back places it in context.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Link's wiki pages, memory pages, raw captures, indexes, skills, and operation journals carry different substrates, forms, lineages, and authorities.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: recalled memories, source pages, query packets, and graph context mostly advise later agents.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: `LINK.md`, validators, MCP tool descriptions, skills, schema markers, and operation journals configure or constrain behavior.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: Link turns saved session traces into proposal candidates and accepted durable memory pages.
