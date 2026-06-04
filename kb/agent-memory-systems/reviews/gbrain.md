---
description: "GBrain review: Postgres/PGLite brain with hybrid search, graph/schema packs, hot facts, MCP push metadata, and SkillOpt loops"
type: ../types/agent-memory-system-review.md
tags: [trace-derived, push-activation]
status: current
last-checked: "2026-06-01"
---

# GBrain

GBrain, from Garry Tan's `gbrain` repository, is a Bun/TypeScript personal and company "brain" layer for agents. It stores markdown-derived pages in Postgres or PGLite, builds hybrid search and graph surfaces over them, exposes CLI/MCP/HTTP operations, ships a large skillpack, and adds trace-derived hot-memory, dream-cycle, Minions, schema-pack, and SkillOpt loops around the core knowledge store.

**Repository:** https://github.com/garrytan/gbrain

**Reviewed commit:** [eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9](https://github.com/garrytan/gbrain/commit/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9)

**Last checked:** 2026-06-01

## Core Ideas

**The database is the operational brain, with markdown as an inspectable synchronized surface.** The schema centers on `sources`, `pages`, `content_chunks`, `links`, `timeline_entries`, `raw_data`, auth tables, Minions tables, eval tables, and later migration-created `takes` and `facts` tables (https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/schema.sql, https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/core/migrate.ts). `put_page` writes through `importFromContent`, then can atomically render the DB row back to the configured brain repo, so the DB remains the live substrate while markdown remains a committable artifact (https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/core/operations.ts, https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/core/write-through.ts).

**Retrieval is a fused planning surface, not one vector query.** `search` uses cheap hybrid retrieval; `query` exposes semantic/keyword search, query expansion, detail levels, code filters, recency and salience controls, image search, cross-modal routing, adaptive returns, and source scoping (https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/core/operations.ts). The hybrid implementation fuses keyword and vector results, applies intent weighting, backlink/salience/recency/title/graph boosts, optional reranking, alias hops, adaptive return sizing, and token budgets (https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/core/search/hybrid.ts, https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/core/search/mode.ts, https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/core/search/token-budget.ts).

**The "brain" layer synthesizes answers across pages, takes, and graph state.** `think` gathers pages by hybrid search, takes by keyword and vector search, and optional graph neighborhoods around an anchor, then asks an LLM for a cited answer with gaps and conflicts; local callers can persist synthesis pages and evidence rows (https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/core/think/index.ts, https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/core/think/gather.ts). This is more than RAG result listing, but its effective answer quality depends on the gathered context and model behavior.

**Schema packs make ontology an active runtime control.** Pack manifests define page types, primitives, aliases, extractable specs, expert routing, link types, calibration domains, and mapping rules; mutation code edits user packs atomically, audits changes, and invalidates cache state (https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/core/schema-pack/manifest-v1.ts, https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/core/schema-pack/mutate.ts). The active pack threads into type inference, query expansion, expert routing, facts extraction, cache identity, and schema-authoring MCP operations (https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/core/schema-pack/detect.ts, https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/core/operations.ts).

**The system learns from traces on several paths.** `extract_facts` turns conversation turns into durable personal facts through an LLM extractor, embeddings, deduplication, source/session provenance, visibility, confidence, notability, and optional typed-claim fields (https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/core/facts/extract.ts, https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/core/facts/backstop.ts). The dream cycle can synthesize transcripts into pages, consolidate hot facts into takes, run calibration phases, and optionally run SkillOpt over skills (https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/core/cycle.ts, https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/core/cycle/synthesize.ts). SkillOpt treats `SKILL.md` as trainable text, runs agent rollouts against benchmarks, reflects on trajectories, validates candidates, and writes accepted skill versions or proposals (https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/core/skillopt/orchestrator.ts, https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/core/skillopt/types.ts).

**Context efficiency is engineered but spread across multiple knobs.** Search modes bundle cache, expansion, search limits, token budgets, reranking, graph signals, and contextual retrieval defaults (https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/core/search/mode.ts). The token-budget enforcer trims ranked search results by estimated downstream context cost (https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/core/search/token-budget.ts). Hot-memory push caps at top-k facts with a TTL, and the OpenClaw context engine caps task/event context, but many operations still expose large read surfaces when the agent asks for them (https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/core/facts/meta-hook.ts, https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/core/context-engine.ts).

## Artifact analysis

- **Storage substrate:** `rdbms` — Postgres or PGLite `pages` plus optional filesystem markdown under the configured `sync.repo_path`
- **Representational form:** `prose` `symbolic` `parametric` — prose markdown, facts, takes, synthesized pages, and skill text; symbolic frontmatter, metadata, schema packs, handlers, job state, and tables; embeddings and vector columns
- **Lineage:** `authored` `imported` `trace-extracted` — authored pages, schema packs, skills, and runtime code; imported or synchronized markdown/files; trace-derived facts, transcripts, eval rows, Minion traces, and SkillOpt outputs
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — pages and facts provide context; skills and context engines instruct; scopes, visibility, write guards, and cost gates constrain; schema packs and search route; evals and SkillOpt validate; search/caches rank; trace loops learn

**Brain pages and synchronized markdown.** The storage substrate is Postgres or PGLite `pages` plus optional filesystem markdown under the configured `sync.repo_path`. The representational form is mixed: prose markdown, YAML frontmatter, typed page metadata, timestamps, source IDs, and generated DB columns. Lineage is authored, imported, captured, synced, or synthesized; `writePageThrough` renders markdown from the saved DB row, while `sync` and import paths can rebuild DB rows from files. Behavioral authority is mainly knowledge artifact authority: pages are evidence, reference, context, and source material. They gain system-definition authority only when their content is consumed as a skill, schema, policy, or prompt fragment.

**Chunks, embeddings, graph, timeline, and query cache.** The storage substrate is relational tables: `content_chunks`, vector columns, weighted FTS vectors, `links`, `timeline_entries`, code-edge tables, query cache, page generation counters, and derived search metadata. The representational form is symbolic plus distributed-vector state. Lineage is derived from page content, code parsing, frontmatter, wiki/markdown links, auto-link extraction, embeddings, query cache generation, and runtime retrieval telemetry. Behavioral authority is ranking, routing, filtering, and context-selection authority. These artifacts decide what the agent sees before it reasons.

**Schema packs and skills.** Schema packs live as files under GBrain-controlled pack locations and are also represented through runtime registries and cache keys. Skills live as markdown instructions under `skills/`, with `skills/RESOLVER.md` acting as the dispatcher (https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/skills/RESOLVER.md). Their representational form is prose plus symbolic manifests and TypeScript handlers. Lineage is bundled, user-authored, schema-detected, schema-suggested, or SkillOpt-derived. Behavioral authority is system-definition artifact authority: packs route extraction and retrieval semantics; skills instruct agent behavior; the resolver tells the host agent which skill to load.

**Hot facts.** The storage substrate is the migration-created `facts` table, with embeddings, source/session provenance, visibility, confidence, notability, validity windows, consolidation pointers, and typed metric fields (https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/core/migrate.ts). The representational form is symbolic rows plus prose fact text and optional embeddings. Lineage is trace-derived: conversation turns, eligible page writes, sync/import/file-upload/code-import surfaces, and explicit MCP extraction. Behavioral authority starts as knowledge artifact authority for recall and audit, then becomes advisory prompt authority when `_meta.brain_hot_memory` injects selected facts into the agent's tool response metadata.

**Takes, synthesis evidence, and calibration artifacts.** The storage substrate is the `takes` table, `synthesis_evidence`, calibration tables, and related cycle/eval outputs created through migrations. The representational form is attributed prose claims with symbolic holder, kind, weight, resolution, and embedding fields. Lineage is extracted from pages or consolidated from facts through cycle phases; synthesis evidence links generated answers back to source take rows. Behavioral authority is mixed: takes are knowledge artifacts for `think`, search, scoring, and calibration, while calibration profiles and resolved scores can become system-definition inputs to later prompts and dashboards.

**Minions and subagent traces.** The storage substrate is `minion_jobs`, inbox, attachments, `subagent_messages`, `subagent_tool_executions`, and rate leases. The representational form is symbolic job state plus JSON message/tool traces. Lineage is runtime agent execution. Behavioral authority is replay, audit, recovery, scheduling, and job-control authority; most rows are not memories for the end user directly, but they shape whether an agent loop resumes, retries, or is allowed to mutate.

**Read-back machinery.** The storage substrate is TypeScript operation code, MCP dispatch code, HTTP auth tables, the OpenClaw extension, and runtime config. The representational form is executable symbolic code and prompt templates. Lineage is authored system code plus configured runtime state. Behavioral authority is system-definition authority over when stored memory enters context, how much is selected, and which users/sources/scopes are visible.

**Promotion path.** GBrain has several promotion paths: markdown/page content -> chunks/links/timeline -> ranked context; conversation/page-write traces -> facts -> recall or MCP metadata -> possible nightly consolidation into takes; transcripts -> dream-synthesized pages -> sync/extract/embed; SkillOpt rollout trajectories -> reflected edits -> validation-gated `SKILL.md` versions or proposals. The strongest promotion is trace text becoming hot facts and then prompt metadata, because it changes later agent behavior without the user manually querying those facts.

## Comparison with Our System

| Dimension | GBrain | Commonplace |
|---|---|---|
| Primary purpose | Runtime personal/company brain for agents, with DB, MCP, HTTP, jobs, skills, and maintenance daemon | Git-tracked methodology KB with typed markdown artifacts, validation, reviews, instructions, and source workflows |
| Canonical substrate | Postgres/PGLite plus optional markdown write-through | Markdown files in a git repo, with generated indexes and validation reports |
| Retrieval | Hybrid vector/keyword/graph/rerank/search-mode stack plus `think` synthesis | Lexical search, authored links, indexes, skills, reviews, and deterministic validation |
| Learning | Conversation facts, transcript synthesis, facts-to-takes consolidation, SkillOpt, eval capture/replay | Agent-authored notes and reviews, semantic QA, validation, git lifecycle |
| Activation | Pull tools plus MCP metadata push and OpenClaw context injection | Mostly explicit pull through `rg`, indexes, links, skills, and review workflows |
| Governance | Scopes, source isolation, visibility filters, RLS attempts, write guards, cost gates, evals | Collection contracts, type specs, schemas, citations, validation, review gates, git diffs |

GBrain is stronger on live operational integration. It exposes many agent-facing operations, supports remote OAuth-scoped MCP, runs maintenance cycles, records job traces, and can push recent hot memory into tool responses. It is built for an agent that is already operating continuously.

Commonplace is stronger on library-level auditability. GBrain has provenance fields, source IDs, visibility gates, receipts, and write-through markdown, but many behavior-shaping artifacts live in DB rows, caches, generated embeddings, queue state, and LLM-derived facts. Commonplace's slower git/type/review path makes promotion more inspectable before content becomes a durable instruction or review claim.

The main tradeoff is authority speed. GBrain quickly turns runtime traces into memory surfaces and prompt-time context, which is valuable for personal assistants. Commonplace deliberately slows promotion so methodology claims and instructions can be reviewed, linked, validated, and cited.

**Read-back:** `both` — GBrain supports pull through search/query/think/recall and engineered memory push through MCP `_meta.brain_hot_memory`; the OpenClaw context engine also pushes retained workspace state during prompt assembly

### Borrowable Ideas

**MCP metadata as a narrow hot-memory push channel.** Commonplace could add a bounded metadata side channel for recent, task-relevant reminders returned alongside tool calls. Ready as a design pattern; needs strict source, scope, expiry, and audit rules before implementation.

**Named search modes as cost/context contracts.** GBrain's conservative/balanced/tokenmax bundles are a good operator-facing abstraction. Commonplace could expose named retrieval bundles for review, source inspection, and connect reports. Ready for read-only tooling.

**Schema packs as active ontology, not just documentation.** GBrain's packs route type inference, extraction, expert routing, and query cache identity. Commonplace already has collection/type contracts; a borrowable version would be a narrower, reviewable pack mechanism for opt-in project schemas. Needs a concrete multi-KB use case.

**Facts-to-takes as a promotion vocabulary.** The hot/cold split is useful: ephemeral personal facts can be captured quickly, then promoted into attributed claims after review. Commonplace could use the same distinction for workshop observations versus durable notes.

**Validation-gated skill optimization.** SkillOpt's benchmark, rollout, reflection, validation, and version-store loop is directly relevant to agent instruction maintenance. Commonplace should borrow the gate shape before borrowing auto-mutation.

**Do not borrow opaque promotion by default.** GBrain's speed comes from letting LLM extraction and runtime hooks create behavior-shaping state. Commonplace should keep durable system-definition artifacts in reviewable markdown with explicit citations, even if it later adds hotter runtime caches.

## Trace-derived learning placement

**Trace source:** `session-logs` `tool-traces` `event-streams` `trajectories` — conversation turns, transcripts, page-write/import/sync/file-upload events, eval capture, and SkillOpt rollout/tool-call trajectories

**Learning scope:** `per-task` `per-project` `cross-task` — session and benchmark-scoped capture, source/workspace-scoped facts and context, and personal/company brain memory reused across tasks

**Learning timing:** `online` `offline` `staged` — online fact extraction on conversations or page writes, opt-in replay/benchmark SkillOpt work, and scheduled dream/consolidation phases

**Distilled form:** `prose` `symbolic` `parametric` — fact text, takes, synthesized pages, and skill edits; structured claim metadata, provenance, eval rows, and schema fields; embeddings for facts, takes, chunks, and search

**Trace source.** GBrain qualifies as trace-derived. It consumes conversation turns through `extract_facts`, eligible page-write/import/sync/file-upload bodies through the facts backstop, transcript files through the dream synthesize phase, query/search calls through eval capture, and SkillOpt rollout/tool-call trajectories through the optimization loop (https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/core/facts/extract.ts, https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/core/facts/backstop.ts, https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/core/cycle/synthesize.ts, https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/core/eval-capture.ts, https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/core/skillopt/types.ts).

**Extraction.** The facts path sanitizes turn text, asks an LLM for structured claims, parses strict JSON with fallback repair, embeds fact text, resolves entity slugs, deduplicates by vector similarity and classifier logic, inserts facts, and bumps hot-memory cache state (https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/core/facts/extract.ts, https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/core/facts/backstop.ts). The dream synthesize path runs a significance verdict over transcripts, fans out trusted subagents, records tool writes, and reverse-writes generated pages (https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/core/cycle/synthesize.ts). SkillOpt uses rollout trajectories and judges to propose and validate edits to skills (https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/core/skillopt/orchestrator.ts).

**Four fields.** Raw traces are stored as transcripts, page bodies, minion/subagent rows, eval rows, or in-process SkillOpt trajectories; their representational form is mixed prose, JSON, tool-call structure, and metrics; lineage is direct runtime execution or imported conversation material; behavioral authority is evidence, replay, audit, and learning input. Distilled artifacts are facts, takes, synthesized pages, calibration profiles, and accepted/proposed skill edits; their form is prose plus symbolic metadata; lineage is LLM-derived or validator-derived from traces; behavioral authority ranges from knowledge artifact context to system-definition instruction when a skill edit or pushed hot-memory fact is consumed.

**Scope and timing.** Hot facts can be online per conversation or page write, usually scoped by source and optional session. Dream synthesis and consolidation are scheduled cycle phases. Eval capture is opt-in and used for replay/regression. SkillOpt is opt-in, benchmark-scoped, cost-capped, and validation-gated.

**Survey placement.** GBrain spans trace-to-facts, trace-to-pages, trace-to-evals, and trace-to-instructions. It strengthens the survey distinction between raw trace retention and promoted behavior-shaping artifacts: raw subagent/tool traces mostly support replay and audit, while facts and skill edits can directly change future prompts or instructions.

## Read-back placement

**Direction.** GBrain is both pull and push. Pull is explicit `search`, `query`, `think`, `recall`, graph traversal, page reads, and skill-guided lookup. Push is implemented through MCP metadata and OpenClaw context assembly. The code-grounded memory push is `_meta.brain_hot_memory`; static skillpack and resolver instructions are shipped baseline documentation, not read-back by themselves.

**Read-back signal:** `coarse` `identifier` — MCP hot-memory push uses source/session/visibility identifiers when present and a coarse recent-source fallback; OpenClaw context uses coarse per-assembly injection with deterministic file/path and time-window selectors

**Read-back timing:** `pre-action` `post-action` — `_meta.brain_hot_memory` is returned after a tool operation but before the next agent step, while OpenClaw context is assembled before the model acts

**Faithfulness tested:** `no` — the review found structural injection and eval surfaces, but no ablation proving pushed facts change downstream behavior

**Targeting and signal.** The MCP dispatcher calls a meta hook after successful tool operations; the hook skips hot-memory operations themselves, selects session-scoped facts when a `source_session` identifier is present, falls back to recent facts from the last 24 hours for the source, sorts by decayed confidence, caps at top-k, and caches per source/session/visibility hash for 30 seconds (https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/mcp/dispatch.ts, https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/core/facts/meta-hook.ts). Its best case is `instance` targeting with an `identifier` signal: source ID, session ID, and visibility/allow-list scope. Its no-session fallback is `coarse`: recent source-level facts on any successful non-memory tool response, not semantic relevance to the current task. The OpenClaw context engine runs on every `assemble()` call and injects live time, location, calendar, travel, and task context from workspace files, with sanitization and caps (https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/openclaw-context-engine.ts, https://github.com/garrytan/gbrain/blob/eefe8b5741c27e59bf65198d46e3dfe5bfa70ce9/src/core/context-engine.ts). That path is `coarse` per-assemble push with deterministic file/path and time-window selectors; the optional OpenClaw SDK memory addition is host-dependent API surface, not fully settled by this repository's code. This is enough for `push-activation`: GBrain has before-action engineered read-back hooks with scope, freshness, and budget controls, not just a static resolver or manual search.

**Timing relative to action.** `_meta.brain_hot_memory` arrives with a tool response before the next agent step that can read metadata. The OpenClaw context block arrives during prompt assembly before the model acts. Facts extraction and dream consolidation happen after source events and affect later actions.

**Selection, scope, and complexity.** Hot-memory push is bounded by source ID, session ID when available, visibility, top-k, TTL, notability/confidence fields, and active-only facts. OpenClaw live context is bounded by file paths, event windows, task caps, size guards, string sanitization, and stale-calendar warnings. Pull search has richer inferred relevance gating through hybrid retrieval and token budgets, but those results are not unsolicited.

**Authority at consumption.** Pushed facts have advisory knowledge artifact authority unless a host treats MCP metadata as stronger. The OpenClaw context block has system-prompt-adjacent instruction authority because it is inserted as `systemPromptAddition`, but its content is mostly operational context rather than domain knowledge. Effective faithfulness is not verified from code: I found structural injection and several eval surfaces, but not an ablation proving each pushed fact changes agent behavior.

**Other consumers.** Humans and operators consume CLI recall, admin dashboards, logs, doctor outputs, eval reports, and markdown write-through files. Cycle phases, SkillOpt, search ranking, and Minions also consume retained state as internal control data.

## Curiosity Pass

**The strongest memory feature is not the broad search stack.** Search is substantial, but the architecturally distinctive move is hot-memory push through MCP metadata. It gives recent trace-derived facts a path into the next action without relying on the agent to remember to call `recall`.

**GBrain has several sources of truth.** The DB is operationally primary, markdown is an inspectable mirror/source for sync, schema packs and skills live as files, and generated vectors/caches live in DB state. That gives practical power but makes provenance and invalidation harder than a markdown-only KB.

**Static skills blur into runtime authority.** `skills/RESOLVER.md` says signal detection and brain ops are always-on, but that is an instruction package, not an enforcement mechanism by itself. The real code-grounded push claim comes from `_meta.brain_hot_memory` and the OpenClaw context engine.

**Trace-derived does not always mean durable learning.** SkillOpt rollout trajectories are in-process and do not become memory by themselves; they matter when accepted edits become durable `SKILL.md` or proposed files. Minions traces mostly support recovery and audit, not direct user-memory read-back.

**Context budgeting is uneven.** Search modes and token budgets are explicit, but `think`, transcript synthesis, and broad tool reads can still assemble complex context. GBrain gives operators knobs rather than one global context-safety invariant.

## What to Watch

- Whether hot-memory `_meta` gets semantic matching against the current user intent rather than session/recent fallback. That would make push activation more precise and would strengthen the `push-activation` placement.
- Whether facts-to-takes consolidation preserves enough item-level lineage from fact IDs, source sessions, extraction prompts, and source markdown slugs for later audit.
- Whether schema packs become the dominant governance layer or remain a flexible routing layer without Commonplace-style review status.
- Whether SkillOpt's accepted edits are routinely human-reviewed before bundled or shared skills gain instruction authority.
- Whether OpenClaw context-engine injection grows from live operational context into knowledge-memory injection; that would increase both utility and prompt-dilution risk.
- Whether DB-first/write-through operation produces observable drift cases between DB rows, markdown files, embeddings, and query caches.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: GBrain turns conversation/page/transcript/rollout traces into facts, pages, eval records, and skill edits.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: GBrain includes explicit push paths through MCP metadata and OpenClaw context assembly.
- [Activate Behavior-Changing Memory Before The Mistake](../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) - exemplifies: hot facts can arrive before the next agent action.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: pages, chunks, links, facts, takes, schema packs, skills, job traces, and context hooks differ by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: pages, facts, traces, and retrieved snippets mainly serve as evidence, context, reference, and advice.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: schema packs, skills, operation handlers, auth scopes, search modes, and context engines route or instruct behavior.
