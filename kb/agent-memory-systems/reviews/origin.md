---
description: "Origin review: local AI-work memory daemon with sourced pages, hybrid retrieval, review gates, git-backed Markdown, and MCP/Claude Code read-back"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-learning]
last-checked: "2026-06-04"
---

# Origin

Origin, from `7xuanlu/origin`, is a local-first memory daemon for AI work sessions. At the reviewed commit it ships a Rust server, CLI, MCP server, and Claude Code plugin over one local store: agents capture typed memories, import or hand off session traces, distill related memories into source-backed wiki pages, and read the result back through recall, context, brief, page, review, and distill tools ([README.md](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/README.md), [crates/origin-server/src/router.rs](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/crates/origin-server/src/router.rs), [crates/origin-mcp/src/tools.rs](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/crates/origin-mcp/src/tools.rs)).

**Repository:** https://github.com/7xuanlu/origin

**Reviewed commit:** [0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb](https://github.com/7xuanlu/origin/commit/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb)

**Last checked:** 2026-06-04

## Core Ideas

**The daemon owns the memory semantics.** The repo map describes `origin-server` as the owner of the local database, embeddings, distill cycles, graph, and HTTP API, while the plugin, MCP server, and CLI are clients over that daemon ([README.md](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/README.md), [crates/origin-server/src/routes.rs](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/crates/origin-server/src/routes.rs)). That keeps classification, search, page policy, review state, and enrichment in one service rather than scattering them through prompt snippets.

**Atomic memories are the first durable unit.** `capture` and `/api/memory/store` write one complete memory with optional type, space, entity, confidence, structured fields, retrieval cue, and supersession target; the route assigns a `mem_*` id, checks duplicates and quality gates, stores chunks, logs agent activity, and starts asynchronous classification, extraction, entity linking, title enrichment, and page growth ([plugin/skills/capture/SKILL.md](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/plugin/skills/capture/SKILL.md), [crates/origin-server/src/memory_routes.rs](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/crates/origin-server/src/memory_routes.rs), [crates/origin-core/src/post_ingest.rs](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/crates/origin-core/src/post_ingest.rs)).

**Distilled pages are sourced wiki artifacts.** Page creation rejects empty source lists, verifies each source memory exists, applies a hallucination guard, writes Markdown when a knowledge path is configured, inserts the page in the DB, resolves orphan links, verifies self-retrieval, and logs page creation. Updates bump version, keep source ids, append changelog entries, and optionally use stale-only compare-and-swap behavior ([crates/origin-core/src/post_write.rs](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/crates/origin-core/src/post_write.rs), [crates/origin-types/src/pages.rs](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/crates/origin-types/src/pages.rs), [plugin/skills/distill/SKILL.md](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/plugin/skills/distill/SKILL.md)).

**Context efficiency is engineered at retrieval and compilation time.** Memories are indexed in libSQL with FTS and embeddings; recall and context use explicit limits, optional reranking on memory search, trust-tiered sections, memory-type tiers, space filters, and source-overlap gates before pages enter context ([crates/origin-core/src/db.rs](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/crates/origin-core/src/db.rs), [crates/origin-server/src/routes.rs](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/crates/origin-server/src/routes.rs)). The result is not full transcript replay: high-volume work history is compressed into typed memories, pages, status files, and scoped context packets.

**Review before trust is implemented as state transitions.** The pre-store quality gate rejects short content, credential leaks, noise patterns, and near-duplicates before insertion; protected-memory topic matches become pending revisions or auto-supersede only under full-trust and high similarity; `/brief` surfaces pending revisions for accept/dismiss decisions ([crates/origin-core/src/quality_gate.rs](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/crates/origin-core/src/quality_gate.rs), [crates/origin-server/src/memory_routes.rs](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/crates/origin-server/src/memory_routes.rs), [plugin/skills/brief/SKILL.md](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/plugin/skills/brief/SKILL.md)).

**The trace-learning path is plural.** `/handoff` asks the acting agent to infer decisions, lessons, gotchas, corrections, facts, open threads, and project status from conversation plus git state; chat import parses exports into memories; context-packaging logic can chunk capture streams into session summaries; distill and background enrichment promote those atoms into graph links, pages, summaries, and review state ([plugin/skills/handoff/SKILL.md](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/plugin/skills/handoff/SKILL.md), [crates/origin-core/src/importer.rs](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/crates/origin-core/src/importer.rs), [crates/origin-core/src/context_packager.rs](https://github.com/7xuanlu/origin/blob/0e3eafae2b8a5a5158afcd7a57a1355c1b311eeb/crates/origin-core/src/context_packager.rs)).

## Artifact analysis

- **Storage substrate:** `sqlite` `files` `repo` `vector` `graph` — The canonical operational store is libSQL: memories, chunks, embeddings, FTS, pages, page sources, entities, observations, relations, access logs, agent registry, spaces, imports, rejections, and review queues. Markdown pages and session/status files live under `~/.origin/`, and the daemon/plugin commit logical memory batches into a local git repo when possible.
- **Representational form:** `prose` `symbolic` `parametric` — Origin combines prose memories, page bodies, session logs, and status files with symbolic memory types, ids, spaces, trust/stability/revision states, page-source lists, tool schemas, graph edges, and distributed-parametric embeddings/reranker outputs.
- **Lineage:** `authored` `imported` `trace-extracted` — Memories can be authored through capture tools, imported from chat exports, or extracted from handoff/session/activity traces; pages, graph records, summaries, tags, structured fields, and review states are derived views over those inputs.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — Retrieved memories/pages advise as knowledge; plugin skills and MCP schemas instruct and route; quality gates, hallucination guards, pending revisions, stale flags, and protected-memory conflicts enforce or validate trust; search/reranking/source-overlap choose context; enrichment and distillation learn from retained traces.

**Atomic memory records.** Storage substrate: libSQL memory/chunk rows, FTS entries, vector embeddings, access logs, and optional Markdown/session mirrors. Representational form: prose content plus symbolic type, space, source agent, confidence, confirmation, stability, supersession, structured fields, retrieval cue, quality, pending revision, and parametric embeddings. Lineage: authored by capture/CLI/MCP calls, imported from chat exports, inferred during `/handoff`, or enriched after ingest. Behavioral authority: knowledge when retrieved, learning input for enrichment/distillation, and trust-routing input when protected revisions or supersession state controls what can be used.

**Knowledge graph records.** Storage substrate: libSQL entities, aliases, observations, relations, memory-entity links, and vector indexes. Representational form: symbolic nodes/edges plus prose observations and embeddings. Lineage: agent-authored graph calls, LLM/entity extraction during post-ingest/import/refinery work, and vector/alias resolution. Behavioral authority: routing/ranking when graph-adjacent memories are selected, and knowledge when humans or agents inspect graph facts.

**Distilled pages.** Storage substrate: DB page rows plus page-source joins and Markdown exports under the knowledge path. Representational form: prose Markdown with symbolic page ids, source memory ids, version/status/stale/user-edit/changelog fields, links, embeddings, and summaries. Lineage: synthesized from memory clusters, grown by post-ingest matching, refreshed from sources, or manually/API edited. Behavioral authority: knowledge when returned by recall/context/search; validation and enforcement live in source-id requirements, hallucination guard, stale locks, CAS, shrink guard, and user-edit locks.

**Plugin skills, MCP tools, and hooks.** Storage substrate: shipped plugin files, MCP tool definitions, shell helpers, and installed host configuration. Representational form: prose instructions, JSON manifests, shell scripts, and Rust tool schemas. Lineage: authored system-definition artifacts shipped with the package. Behavioral authority: instruction/routing for `/brief`, `/capture`, `/handoff`, `/distill`, `/recall`, `/review`, and MCP-only clients.

**Session logs and project status files.** Storage substrate: Markdown/JSON files under `~/.origin/sessions/` and `~/.origin/sessions/_status/`, with git history when available. Representational form: prose session narrative plus symbolic project/status/timestamp fields. Lineage: trace-extracted by `/handoff` from conversation, git state, and current work. Behavioral authority: the status file has stronger session-start authority than semantic memory in `/brief`; it frames the next action before background memories are loaded.

**Review and rejection state.** Storage substrate: rejected-memory rows, pending-revision flags, supersession chains, refinement proposals, page stale flags, changelogs, and access logs. Representational form: symbolic statuses plus prose rejection/revision payloads. Lineage: generated by quality gates, topic-match checks, page contradiction checks, refinement paths, and user/agent review actions. Behavioral authority: validation, audit, pruning, trust routing, and sometimes enforcement because these records can block insertion, keep revisions pending, or prevent user-edited pages from being overwritten.

Promotion path: Origin moves work traces and authored captures into typed memories, memories into graph-linked/enriched records, related memories into sourced pages, repeated reads into access-weighted ranking, pages/status files into session-start context, and review decisions back into trust state. The strongest authority jump is trace or capture becoming the next agent's `/brief` frame.

## Comparison with Our System

| Dimension | Origin | Commonplace |
|---|---|---|
| Primary purpose | Local memory daemon for AI work across sessions, clients, spaces, and projects | Git-native methodology KB for agent-operated knowledge bases |
| Main substrate | libSQL database with FTS/vector/graph/page state plus Markdown/git mirrors | Repository Markdown, type specs, generated indexes, validation reports, source snapshots |
| Core artifact | Atomic memories and source-backed distilled pages | Typed notes, reviews, instructions, ADRs, sources, indexes, skills, reports |
| Write path | Capture/import/handoff, quality gate, async enrichment, graph/page growth, distill | Deliberate writing from collection contracts, source capture, review gates, validation |
| Read-back | Pull recall/search plus `/brief` and `context` scoped memory packets | Mostly explicit pull through `rg`, indexes, links, skills, and loaded instructions |
| Governance | Quality gate, protected-memory revisions, pending confirmations, stale pages, source IDs, hallucination guard, local git | Schemas, collection contracts, deterministic validation, semantic review bundles, archive/replacement discipline |

Origin is close to Commonplace in its insistence that memory should become durable, reviewable artifacts with provenance and maintenance state. The sharpest shared idea is the raw-to-distilled split: Origin does not ask every future agent to replay work history, but it also tries not to let compiled pages float away from their source memory ids.

The main divergence is the canonical substrate. Commonplace makes the reviewable Markdown artifact canonical. Origin makes libSQL canonical and exports Markdown/git surfaces around that state. That gives Origin better runtime search, incremental enrichment, and multi-client integration, but weaker plain-git inspectability than Commonplace's library layer.

### Borrowable Ideas

**Source-backed page distillation.** Ready as a design pattern. Commonplace already requires citations, but Origin's `source_memory_ids`, stale-source flags, and refresh path suggest a stricter metadata lane for notes generated from work artifacts.

**Separate atomic memory from compiled page.** Ready for workshop workflow. Keep raw session findings as temporary/evidence artifacts, then promote only coherent synthesis into durable notes.

**Page relevance by source overlap.** Needs a search layer. Origin gates compiled pages by overlap with already selected source memories; Commonplace could use the same rule when future retrieval returns synthesized notes beside source snapshots.

**Pending revision instead of silent overwrite.** Ready for review-system design. Contradictory evidence against high-authority definitions or instructions could create a revision candidate instead of editing immediately.

**Status file outranking semantic memory.** Ready now for long-running work. One current status file can serve as the live ledger, while searchable notes remain background.

**Do not borrow DB opacity into the library layer.** Keep Commonplace artifacts file-native; a DB is useful as an operational index, not as the canonical methodology knowledge.

## Write side

**Write agency:** `manual` `automatic` — Humans and agents can capture, edit, review, and distill through MCP/CLI/plugin paths; automatic operations include quality gating, duplicate rejection, asynchronous classification/extraction, entity linking, title enrichment, page contradiction marking, page growth, distill/refinery passes, access logging, confidence decay/boosting, pending-revision handling, and optional auto-supersede.

**Curation operations:** `consolidate` `dedup` `evolve` `synthesize` `invalidate` `decay` `promote` — Distillation consolidates clusters into pages/summary nodes; duplicate checks reject or merge overlapping material; enrichment evolves stored metadata, entities, titles, tags, and page links; synthesis can create page prose and graph/summary artifacts across stored memories; stale flags, supersession, protected-memory revisions, and relation supersede invalidate older state; recency/access confidence adjusts decay and salience; page/status/read-back tiers promote selected material into stronger future context.

### Trace-learning

**Trace source:** `session-logs` `tool-traces` `event-streams` — `/handoff` consumes conversation and git state, chat import consumes exported conversations, activity/context packaging consumes capture streams, and server routes log store/read/refine/page actions.

**Learning scope:** `per-project` `cross-task` — Spaces, projects, source agents, page targets, memory types, session status files, and entity ids scope memory while allowing cross-session reuse.

**Learning timing:** `online` `offline` `staged` — Capture and enrichment run during work, import is staged from exported archives, distill/refinery/background cycles run later, and `/handoff` closes a session with captures plus status files.

**Distilled form:** `prose` `symbolic` `parametric` — Traces become prose memories/pages/status logs, symbolic metadata/graph/review state, and indexed embeddings/ranking inputs.

**Trace source.** Origin qualifies as trace-learning because durable artifacts are derived from agent-work traces, not only from explicit user-authored notes. `/handoff` directs the agent to infer durable memories and status from the session, chat import turns conversation exports into memories, and the server records activity/access traces that feed later ranking, review, and onboarding state.

**Extraction.** Extraction is layered. The store path writes a raw memory quickly, then async enrichment classifies, extracts structured fields, creates or links entities, enriches titles, and grows pages. `/handoff` relies on the active agent as the extraction oracle over conversation and git evidence. Distillation clusters memories and either daemon-synthesizes page bodies in background paths or returns pending clusters for the calling agent to synthesize through the skill.

**Scope and timing.** Scope is explicit through space, project, agent, entity, memory type, page, source id, and session status path. Timing is mixed: online capture, async post-ingest reflection, offline import, staged session handoff, and background/user-triggered distillation.

**Survey placement.** Origin belongs in both trace-to-memory-record and trace-to-sourced-wiki-page families on the trace-learning survey. It strengthens the raw/distilled split: imported chats and session traces become atomic memories first; pages and status files become higher-authority context only after curation and read-back assembly.

## Read-back

**Read-back:** `both` — Agents can deliberately pull memories/pages through recall, search, list, and get-page tools, while `/brief` and the MCP `context` tool assemble retained status, identity, preferences, decisions, corrections, pages, corpus overview, and relevant memories for the acting agent before work continues.

**Read-back signal:** `coarse` `identifier` `inferred / lexical` `inferred / embedding` — `/brief` always starts from the status file and calls `context`; `context` narrows by space, memory type, source ids, page/source overlap, and query/topic while using hybrid FTS/vector search and optional read-path variants elsewhere.

**Faithfulness tested:** `no` — The repo includes retrieval, page-distillation, KG, route, and eval tests, but I did not find an end-to-end with/without or post-action audit proving that injected `/brief` or `context` memories change agent behavior.

**Targeting and signal.** Push targeting is both coarse and instance-specific. `/brief` is coarse at session start because it reads the project status file first, then resolves a space and calls context. It is instance-targeted when project/status path, active space, topic, memory type tiers, source ids, page-source overlap, and search query shape what appears. The search signals are lexical and embedding-based; identifier signals come from space, type, page/source/entity/project ids, and status file path.

**Injection point.** `/brief` is the clearest pre-invocation read-back path: it tells the agent to call Origin before other verbs at session start or major topic shift, then treat the status file as the live ledger. MCP-only clients can use `context` for the same memory packet without the Claude Code slash skill.

**Selection, scope, and complexity.** Selection is bounded by `max_chunks`, memory type tiers, trust classification, relevance threshold, space filters, source-overlap-gated pages, optional global prelude, and search/rerank choices. The packet can mix authority levels: status file, identity/preferences, decisions, corrections, compiled pages, corpus overview, and raw memory results. Origin controls volume better than transcript replay, but complexity still depends on the quality of scopes and source-overlap gates.

**Authority at consumption.** Retrieved memories and pages are advisory context by default. `/brief` gives the project status file stronger practical authority over "what next"; plugin skills and MCP schemas carry system-definition authority over when and how memory calls happen; pending revisions are audit triggers rather than automatic rewrites unless trust and similarity pass the auto-supersede path.

**Faithfulness.** The implementation tests retrieval mechanics, route behavior, page faithfulness, KG faithfulness, and benchmark recall. Those tests show that context can be selected and assembled, not that a downstream agent faithfully uses it. Effective behavioral uptake remains runtime-dependent.

**Other consumers.** Humans can inspect Markdown pages, session logs, status files, CLI output, git history, pending reviews, and Obsidian-style exports. Origin's retained state is therefore both agent context and human-operable memory.

## Curiosity Pass

**Origin is not Markdown-first, despite strong Markdown affordances.** Markdown pages and session files are central to adoption, but the daemon's libSQL schema, vector/FTS indexes, and HTTP routes are the operational memory system.

**The page source-id discipline is stronger than most memory summaries.** `create_page` refuses unsourced pages and checks source ids before insertion. That gives page distillation a reviewable spine.

**The distill route intentionally splits LLM responsibility.** The user-triggered route can return pending clusters for the calling agent to synthesize, while background paths can use daemon LLMs. This reuses the host session's LLM without forcing every generation through the daemon.

**Review states are powerful but scattered.** Confirmation, stability, pending revision, stale pages, rejected memories, refinement proposals, user-edited locks, changelogs, access counts, and trust levels all express governance. Operators need a coherent workflow or these states can become invisible maintenance debt.

**The trace-learning path is not fully daemon-deterministic.** Chat import and async enrichment are daemon paths, but `/handoff` extraction depends on an agent following skill instructions. That is still a system-definition artifact, but its quality is host-agent dependent.

## What to Watch

- Whether page Markdown becomes a bidirectional source of truth or remains an export/sync surface over libSQL; this determines how much Origin should be compared to file-first KBs.
- Whether `/brief` and `context` gain behavioral ablations or post-action audits; that would move Origin from structurally engineered read-back to measured read-back authority.
- Whether imported chat/session memories retain enough source-span provenance to audit a page claim back to exact conversation turns, not just memory ids.
- Whether the many review surfaces converge into one operator workflow; pending revisions, refinements, stale pages, and unconfirmed captures currently express related trust problems through different paths.
- Whether automatic background distill/page growth becomes aggressive by default; that raises the importance of hallucination guard, shrink guard, and user-edited locks.
- Whether spaces remain coarse buckets or become a stronger access-control/privacy boundary across clients and projects.

Relevant Notes:

- [Trace-learning techniques in related systems](../trace-learning-techniques-in-related-systems.md) - places: Origin turns chat/session/work traces into atomic memories and sourced wiki pages.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: Origin extracts future work context from prior sessions and imports.
- [Preserve evidence without loading history](../../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md) - aligns: Origin distills traces into memories/pages while keeping source ids and session artifacts.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Origin couples storage with `/brief` and `context` activation paths.
- [Symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - applies: Origin's space, project, page, source id, and memory type filters need symbols before they can target context.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Origin requires separating DB memories, graph records, pages, skills, session files, and review queues by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: recalled memories, pages, graph observations, and session logs mostly advise as evidence/context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: plugin skills, MCP schemas, quality gates, page source rules, review queues, and read-back workflows configure future behavior.
