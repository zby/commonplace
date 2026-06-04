---
description: "Origin review: local AI-work memory daemon with sourced captures, distilled wiki pages, hybrid retrieval, review gates, git-backed Markdown, and MCP/Claude Code read-back"
type: ../types/agent-memory-system-review.md
status: current
last-checked: "2026-06-03"
tags: [trace-derived, push-activation]
---

# Origin

Origin, from `7xuanlu/origin`, is a local-first memory system for AI work sessions. At the reviewed commit it ships a Rust daemon, CLI, MCP server, and Claude Code plugin over one local store: agents capture atomic memories, import or hand off session traces, distill related memories into source-backed wiki pages, and read the result back through recall, context, brief, page, review, and distill tools.

**Repository:** https://github.com/7xuanlu/origin

**Reviewed commit:** [0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb](https://github.com/7xuanlu/origin/commit/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb)

**Last checked:** 2026-06-03

## Core Ideas

**The daemon owns memory behavior; clients are thin surfaces.** The README's repo map is accurate at this commit: `origin-server` owns the local database, embeddings, distill cycles, graph, pages, and HTTP API, while the MCP server, CLI, and Claude Code plugin call into that daemon ([README.md](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/README.md), [crates/origin-core/README.md](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/crates/origin-core/README.md), [crates/origin-server/src/router.rs](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/crates/origin-server/src/router.rs), [crates/origin-mcp/src/tools.rs](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/crates/origin-mcp/src/tools.rs)). That boundary keeps storage/search/classification/page logic in Rust rather than scattering it across plugin prompts.

**The first-class write unit is an atomic, typed memory.** `capture` posts a complete statement plus optional type, space, entity, confidence, structured fields, retrieval cue, and supersession target to `/api/memory/store`; the server creates a `mem_*` source id, computes confidence/stability, runs a pre-store quality gate, writes chunks with embeddings/FTS metadata, logs agent activity, and spawns asynchronous classification and post-ingest enrichment ([crates/origin-mcp/src/tools.rs](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/crates/origin-mcp/src/tools.rs), [crates/origin-server/src/memory_routes.rs](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/crates/origin-server/src/memory_routes.rs), [crates/origin-core/src/quality_gate.rs](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/crates/origin-core/src/quality_gate.rs), [crates/origin-core/src/post_ingest.rs](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/crates/origin-core/src/post_ingest.rs)). The Claude Code `/capture` skill makes the agent choose one of six memory types when no daemon LLM is available ([plugin/skills/capture/SKILL.md](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/plugin/skills/capture/SKILL.md)).

**Distilled pages are sourced, versioned wiki artifacts rather than free summaries.** Page creation rejects empty source lists, checks every source memory id exists, runs a hallucination guard against cited sources, writes Markdown when a knowledge path is configured, inserts the page into the DB, resolves orphan links, verifies self-retrieval, and logs page creation. Page updates require source ids, bump version, append changelog entries, clear stale state through the DB update path, optionally rewrite the Markdown export, and can use compare-and-swap behavior for stale refreshes ([crates/origin-core/src/post_write.rs](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/crates/origin-core/src/post_write.rs), [crates/origin-types/src/pages.rs](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/crates/origin-types/src/pages.rs), [plugin/skills/distill/SKILL.md](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/plugin/skills/distill/SKILL.md)).

**Context efficiency is engineered at both retrieval and compilation time.** Raw memories are chunked and indexed in libSQL with FTS5 and vector indexes; recall uses explicit limits and optional cross-encoder reranking. The `context` endpoint loads identity/preference/decision/correction tiers, searches memories up to `max_chunks`, gates pages by overlap with returned source memory ids, and can include a disabled-by-default corpus prelude from summary nodes ([crates/origin-core/src/db.rs](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/crates/origin-core/src/db.rs), [crates/origin-server/src/routes.rs](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/crates/origin-server/src/routes.rs), [crates/origin-core/src/pages.rs](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/crates/origin-core/src/pages.rs), [crates/origin-mcp/src/tools.rs](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/crates/origin-mcp/src/tools.rs)). This is not unbounded transcript replay: the high-volume trace is compressed into memories, pages, and scoped context packets.

**Review before trust is implemented as gates and pending states, not only advice.** The pre-store quality gate rejects noise, credential leaks, too-short content, and near-duplicates before database insertion. Protected memories that topic-match a new capture become pending revisions rather than being silently overwritten; MCP exposes `list_pending`, `list_pending_revisions`, `accept_revision`, `dismiss_revision`, `list_refinements`, and related review tools ([crates/origin-core/src/quality_gate.rs](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/crates/origin-core/src/quality_gate.rs), [crates/origin-server/src/memory_routes.rs](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/crates/origin-server/src/memory_routes.rs), [crates/origin-core/src/post_write.rs](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/crates/origin-core/src/post_write.rs), [crates/origin-server/src/refinery_routes.rs](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/crates/origin-server/src/refinery_routes.rs), [plugin/skills/brief/SKILL.md](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/plugin/skills/brief/SKILL.md)).

**The trace-derived path is plural.** Direct captures are user/agent-authored memories, but Origin also has chat-export import that ingests conversation exports as raw memories and runs background enrichment, plus `/handoff`, which instructs the agent to infer session decisions/lessons/gotchas from conversation and git state, store granular captures, and write session/status files ([crates/origin-server/src/import_routes.rs](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/crates/origin-server/src/import_routes.rs), [crates/origin-core/src/importer.rs](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/crates/origin-core/src/importer.rs), [plugin/skills/handoff/SKILL.md](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/plugin/skills/handoff/SKILL.md)). Distillation then promotes clusters of those memories into pages.

**Local inspectability is real but not pure file-first.** The daemon initializes `~/.origin/` as a git repository when possible, ignores DB/bin/log internals, writes pages and session files under the Origin directory, and commits logical batches through skills; the operational source of truth is still libSQL plus generated Markdown mirrors, not Markdown alone ([crates/origin-server/src/main.rs](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/crates/origin-server/src/main.rs), [plugin/skills/handoff/SKILL.md](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/plugin/skills/handoff/SKILL.md)).

## Artifact analysis

- **Storage substrate:** `sqlite` — The central retained state lives in a local libSQL database: memories, embeddings, FTS, entities, observations, relations, pages, source links, access logs, agent registry, spaces, import state, rejected memories, and review/refinement queues. Markdown pages, session files, and a git repo under `~/.origin/` are important mirrored and human-facing artifacts, but the daemon routes reads/writes through the database.
- **Representational form:** `prose` `symbolic` `parametric` — Origin combines prose memories and page bodies, symbolic metadata/schemas/status fields/tool contracts, graph relations, FTS indexes, vector embeddings, optional reranker/model outputs, Markdown files, shell hooks, and skill instructions.
- **Lineage:** `authored` `imported` `trace-extracted` — memories and system-definition artifacts are authored through captures, tools, skills, and shipped code; chat exports are imported; handoff/session artifacts and extracted records are trace-derived.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — retrieved memories and pages advise as knowledge; skills and MCP tools instruct and route; gates and review states enforce or validate trust; graph/search/reranking select context; distillation and enrichment learn from retained traces.

**Atomic memory records.** Storage substrate: libSQL `memories` rows with FTS5 triggers, vector embeddings, metadata columns, access logs, and optional child vectors. Representational form: prose content plus symbolic memory type, space, source agent, confidence, confirmation, stability, supersession, structured fields, retrieval cue, quality, pending revision, and distributed-parametric embeddings. Lineage: authored by MCP/CLI capture, imported from chat exports, inferred by `/handoff`, or produced by importer/refinery paths; later enrichment can classify, extract structured fields, link entities, enrich titles, mark revision state, or grow pages. Behavioral authority: knowledge artifacts when retrieved as evidence/context; learning inputs for distillation and graph extraction; system-definition candidates when protected-memory revision or supersession state controls what should be trusted.

**Knowledge graph records.** Storage substrate: libSQL `entities`, `observations`, `relations`, aliases, memory-entity links, and vector indexes. Representational form: symbolic graph edges and observations with prose content and embeddings. Lineage: agent-supplied entity/relation calls, LLM/entity extraction in post-ingest and import paths, and auto-linking by vector similarity. Behavioral authority: routing/ranking and context-selection authority when graph-adjacent memories and observations are selected; knowledge-artifact authority when humans or agents inspect the graph.

**Distilled pages.** Storage substrate: DB `pages` rows plus source-memory join data and Markdown exports under the configured knowledge path. Representational form: prose Markdown wiki pages with symbolic page ids, source_memory_ids, version/status, stale_reason, user_edited, changelog, links, embeddings, and summaries. Lineage: created from clusters or agent-synthesized `/distill` payloads, refreshed from source memories, grown by post-ingest matching, or manually/API edited. Source memories invalidate or refresh pages through `stale_reason`, `sources_updated_count`, changelog, and distill/update routes. Behavioral authority: knowledge artifacts when returned by recall/context/search; system-definition refresh policy lives in source-id requirements, hallucination guard, stale locks, CAS, shrink guard, and page-update code.

**Plugin skills, MCP tools, and hooks.** Storage substrate: repository plugin files installed into Claude Code plus MCP server tool definitions and local shell helpers. Representational form: prose instructions, JSON manifests, shell scripts, and Rust tool schemas. Lineage: authored system-definition artifacts shipped with the package; installation copies/wires them into the host. Behavioral authority: instruction/routing authority for agents using `/brief`, `/capture`, `/handoff`, `/distill`, `/recall`, `/review`, and related tools. These artifacts decide when memory is captured, how spaces are resolved, what sources are authoritative, and which MCP calls are made.

**Session logs and project status files.** Storage substrate: Markdown/JSON files under `~/.origin/sessions/` and `~/.origin/sessions/_status/`, with git history when available. Representational form: prose session narrative plus symbolic project/status/timestamp fields. Lineage: trace-derived by the `/handoff` skill from conversation, git state, and current work context. Behavioral authority: the status file has stronger session-start authority than memory search in `/brief`; it frames "what is next" before background memories are loaded.

**Import and trace records.** Storage substrate: import_state rows, imported `memories` rows, metadata such as import source/batch, and the source export ZIP only by path at import time. Representational form: parsed prose memories with symbolic import metadata, then enriched classifications/entities/relations. Lineage: derived from chat-export ZIPs parsed by vendor-specific dispatch and bulk-ingested before background classification/enrichment. Behavioral authority: mostly knowledge artifacts and learning inputs until retrieved, distilled, or promoted into pages/status.

**Review, rejection, revision, and refinement state.** Storage substrate: `rejected_memories`, pending_revision flags, supersession chains, refinement queues, page stale flags, and changelogs. Representational form: symbolic statuses plus prose rejection/revision/refinement payloads. Lineage: generated by quality gates, topic-match checks, page contradiction checks, refinement proposal paths, and user/agent review actions. Behavioral authority: validation, audit, pruning, and trust-routing authority. These records can block insertion, suppress originals, keep revisions pending, or prevent user-edited pages from being overwritten.

**Promotion path.** Origin promotes raw work traces and authored captures into typed memories, memories into graph-linked and enriched records, related memories into sourced pages, pages/status files into session-start context, and review decisions back into trust state. The strongest authority jump is from trace/capture to session-start context: remembered material becomes the next agent's working background through `/brief` and `context`.

## Comparison with Our System

| Dimension | Origin | Commonplace |
|---|---|---|
| Primary purpose | Local memory daemon for AI work across sessions, tools, spaces, and projects | Git-native methodology KB for agent-operated knowledge bases |
| Main substrate | libSQL database with FTS/vector/graph/page state, plus Markdown/git mirrors | Repository Markdown, type specs, generated indexes, validation reports, source snapshots |
| Core artifact | Atomic memories and source-backed distilled pages | Typed notes, reviews, instructions, ADRs, sources, indexes, skills, reports |
| Write path | Capture/import/handoff, quality gate, async enrichment, graph/page growth, distill | Deliberate writing from collection contracts, source capture, review gates, validation |
| Read-back | Recall/search pull plus `/brief` and `context` scoped memory push through MCP/plugin | Mostly explicit pull through `rg`, indexes, links, skills, and loaded instructions |
| Governance | Quality gate, protected-memory revision, pending confirmations, stale pages, source IDs, hallucination guard, local git | Schemas, collection contracts, deterministic validation, semantic review bundles, archive/replacement discipline |
| Context efficiency | Query limits, typed tiers, space filters, FTS/vector/graph retrieval, page source-overlap gating, distilled pages | Progressive disclosure through frontmatter/indexes/links/search, explicit artifact selection, review reports |

Origin is closer to Commonplace than vector-only memory systems because it treats memory as durable artifacts with source links, review states, refresh policy, Markdown exports, and git history. Its strongest design signal is the split between atomic captures and distilled pages: the system does not ask every future agent to consume raw work history, but also does not let summary pages float free of their source memory ids.

The main divergence is the operational substrate. Commonplace keeps the reviewable artifact itself as the canonical repository file. Origin's canonical operational state is a database; Markdown pages and sessions are exported surfaces over that state. That gives Origin better runtime search, incremental enrichment, and client integration, but weaker plain-git inspectability than Commonplace's library layer.

The other divergence is authority timing. Commonplace promotes high-authority instructions by deliberate artifact edits and validation. Origin makes capture and read-back easy enough that low-friction memories can reach the next session quickly, then relies on quality gates, pending revision states, source ids, and user review to control damage. That is pragmatic for personal AI work memory; for methodology claims, Commonplace's slower publication discipline is still safer.

**Read-back:** `both` — Agents and users can pull memories/pages through recall, search, list, and get-page tools, while `/brief` and `context` provide engineered session/topic/space-scoped memory packets to the acting agent before work continues.

### Borrowable Ideas

**Source-backed page distillation.** Commonplace already writes sourced reviews and notes, but Origin's `source_memory_ids` requirement plus stale-source refresh loop is a sharper operational pattern. Ready as vocabulary and perhaps as future metadata for notes generated from work artifacts.

**Separate atomic memory from compiled page.** Origin keeps small captures and distilled pages distinct. Commonplace can borrow this for workshop logs: keep raw session findings as temporary/evidence artifacts, then promote only coherent synthesis into library notes. Ready now as workflow discipline.

**Page relevance by source overlap.** Origin avoids returning a page just because its embedding is similar; it requires overlap with source memories already selected for the query. Commonplace could use a similar rule when a future search layer returns synthesized notes alongside source snapshots. Needs a search/index layer first.

**Pending revision instead of silent overwrite.** Protected memories that topic-match new contrary content become review items. Commonplace could apply the same shape to high-authority instructions or definitions: new contradictory evidence opens a revision candidate rather than editing the artifact immediately. Ready for review-system design.

**Session status file outranking semantic memory.** `/brief` treats the handoff-maintained project status file as the live ledger and memories as background. Commonplace workshops could adopt this distinction for long-running investigations: one current status file, many searchable notes. Ready now.

**Local git for generated memory artifacts.** Origin's daemon initializes a git repo for user-facing memory artifacts. Commonplace already has git; the borrowable idea is committing generated session/page batches at logical boundaries so users can inspect memory evolution. Needs a concrete generated-artifact lane.

**Do not borrow database opacity into the library layer.** Origin's DB makes sense for a daemon. Commonplace's methodology artifacts should remain file-native and reviewable; a DB would be useful only as an operational index, not as canonical knowledge.

## Trace-derived learning placement

- **Trace source:** `session-logs` — chat exports, conversation history, session summaries, and session/status files are the trace sources named in the review.
- **Learning scope:** `per-project` `cross-task` — Origin scopes memory by project/space/session surfaces while carrying context across sessions and future work.
- **Learning timing:** `online` `offline` `staged` — capture can happen during work, chat import is staged offline, and enrichment/distillation/handoff run asynchronously or at session boundaries.
- **Distilled form:** `prose` `symbolic` `parametric` — atomic traces become prose memories/pages/status files, symbolic metadata/graph/review state, and indexed embeddings/reranker outputs.

**Trace source.** Origin qualifies as trace-derived. The implemented sources include chat-export ZIPs parsed into conversation memories, `/handoff` session context synthesized from conversation history and git state, session/status files written at session end, and user/agent captures that can be distilled into pages. The source trace is not one uniform event log; it is a mix of explicit memory calls, chat exports, session summaries, git diffs/logs, and current project context.

**Extraction.** Extraction is layered. Import parsing strips list/date/type prefixes, skips section headers and short entries, deduplicates exact content, then stores imported memories and runs background classification plus post-ingest enrichment. `/handoff` delegates extraction judgment to the active agent: infer decisions, lessons, gotchas, corrections, facts, and open threads from the just-finished session, then store atomic captures and write narrative/status files. Distillation clusters related memories and either daemon-synthesizes pages when a daemon LLM is available or returns pending clusters for the calling agent to synthesize and post back.

**Scope and timing.** Scope is by space, project, entity, page target, memory type, source agent, and session status file. Timing is mixed: capture is online during work; post-ingest enrichment is asynchronous after writes; chat import is staged offline; `/handoff` is end-of-session; `/brief` is session-start read-back; `/distill` can be explicit or background/self-evolving depending on daemon configuration and caller path.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), Origin belongs in the trace-to-memory-record and trace-to-sourced-wiki-page families. It strengthens the survey's raw/distilled split: imported conversations and session histories become atomic memories first; pages and status files are later behavior-shaping distilled artifacts with stronger read-back authority.

## Read-back placement

**Direction.** Origin is both pull and push. `recall`, `search_pages`, `get_page`, `get_page_sources`, `list_memories`, and review/list tools are explicit pull surfaces. `/brief` and `context` push retained memory into the acting agent's session when invoked by the user or session-start workflow, and the status file is rendered before semantic context.

**Read-back signal:** `identifier` `inferred / lexical` `inferred / embedding` — `context` narrows by space, type, source/page/entity/project identifiers while combining FTS, vector retrieval, optional reranking, and page-source overlap; `/brief` uses project identity for status before broader context.

**Read-back timing:** `pre-action` — `/brief` is session-start context, and `context` is called at session start or topic shift before the next work move; capture, enrichment, import, page growth, and handoff affect later reads rather than the current action.

**Faithfulness tested:** `no` — the review found routing/search/page tests and benchmarks, but no with/without ablation proving injected `/brief` or `context` memories change agent behavior.

**Targeting and signal.** Targeting is `instance`. `context` receives a topic/conversation summary, max chunk count, and space, then combines typed tiers, corrections, memory search, and source-overlap-gated pages. The main signal is `inferred / embedding` plus lexical FTS and page-source overlap, narrowed by identifier filters such as space, memory type, source ids, page ids, entity/page targets, and project status file path. `/brief` also uses project identity as an `identifier` signal for the status file before loading broader context.

**Timing relative to action.** `/brief` is explicitly session-start context and can change the next move. `context` can be called at session start or topic shift. `capture`, enrichment, import, page growth, and handoff happen during or after work and mostly affect later reads.

**Selection, scope, and complexity.** Selection is controlled by tool limits, memory type tiers, trust gates, space filters, relevance thresholds, top-k search, page overlap, stale-page/user-edit locks, and optional reranking/global prelude flags. Complexity is higher than a flat memory list because read-back can combine identity/preferences, decisions, corrections, atomic search results, compiled pages, and status-file text. Origin reduces volume through distillation and overlap gates, but the resulting context packet can still mix several authority levels.

**Authority at consumption.** Retrieved memories and pages are advisory context by default. The project status file in `/brief` has stronger practical authority over current next steps, and plugin skills carry system-definition authority over when and how to call MCP tools. Pending revision blocks are audit triggers: they do not rewrite memory automatically, but they ask the human/agent to accept or dismiss a proposed trust change.

**Faithfulness.** The repo has retrieval benchmarks and tests for routing/search/page behavior, but I did not find a Synapptic-style with/without ablation proving that injected `/brief` or `context` memories change the agent's behavior. The read-back mechanism and budgets are implemented; effective behavioral uptake remains runtime-dependent.

**Other consumers.** Human users can inspect Markdown pages, session logs, status files, CLI output, git history, pending reviews, and Obsidian-style exported pages. The same retained state is therefore both agent context and human-operable memory.

## Curiosity Pass

**Origin is not actually Markdown-first, despite strong Markdown affordances.** Markdown pages and session files are central to adoption, but the daemon's libSQL schema, vector/FTS indexes, and HTTP routes are the operational memory system.

**The page source-id discipline is stronger than many README claims in this landscape.** `create_page` refuses unsourced pages and checks source ids before insertion. That makes page distillation reviewable in a way that plain LLM summary systems usually are not.

**The distill route and skill intentionally split LLM responsibility.** The route can return pending clusters instead of daemon-synthesizing everything; the skill says the agent may synthesize those clusters in-session and call `create_page` or `update_page`. This is a practical way to use the LLM already present in the host session without making the daemon own every generation path.

**Review states are scattered but meaningful.** Confirmation, stability, pending revision, stale pages, rejected memories, refinement proposals, user-edited locks, and changelog entries are separate mechanisms. That makes the system richer than a simple memory store, but it also means governance depends on multiple surfaces being surfaced consistently.

**The trace-derived path is not fully automatic.** Chat import and background enrichment are implemented daemon paths, but `/handoff` extraction depends on a host agent following skill instructions. That is still a system-definition artifact, but it is less deterministic than a daemon-only session parser.

## What to Watch

- Whether page Markdown becomes a true bidirectional source of truth or remains an export/sync surface over libSQL. That determines how much Commonplace should compare Origin to file-first KBs.
- Whether `/brief` and `context` gain behavioral ablations or post-action audits. That would move Origin from structurally engineered read-back to measured read-back authority.
- Whether imported chat/session memories retain enough source-span provenance to audit a distilled page claim back to exact conversation turns, not just memory ids.
- Whether the many review surfaces converge into one operator workflow. Pending revisions, refinement proposals, stale pages, and unconfirmed captures currently express related trust problems through different paths.
- Whether automatic background distill/page-growth becomes aggressive by default. That would raise the importance of hallucination guard, shrink guard, and user-edited locks.
- Whether spaces remain coarse buckets or become a stronger access-control/privacy boundary across clients and projects.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Origin turns chat/session/work traces into atomic memories and sourced wiki pages.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: Origin extracts future work context from prior sessions and imports.
- [Preserve evidence without loading history](../../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md) - aligns: Origin distills traces into memories/pages while keeping source ids and session artifacts.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Origin couples storage with `/brief` and `context` activation paths.
- [Symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - applies: Origin's space, project, page, source id, and memory type filters need symbols before they can target context.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Origin requires separating DB memories, graph records, pages, skills, session files, and review queues by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: recalled memories, pages, graph observations, and session logs mostly advise as evidence/context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: plugin skills, MCP schemas, quality gates, page source rules, review queues, and read-back workflows configure future behavior.
