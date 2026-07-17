---
description: "GBrain review: Postgres/PGLite-backed agent brain with markdown write-through, hybrid retrieval, graph links, hot facts, skills, and dream-cycle maintenance"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-learning]
last-checked: "2026-06-04"
---

# GBrain

GBrain, from Garry Tan's `garrytan/gbrain` repository, is a Bun/TypeScript memory layer for AI agents. It stores a markdown "brain repo" through a Postgres-compatible database, exposes CLI and MCP operations for search, page writes, graph traversal, fact recall, synthesis, and background jobs, and ships a large skillpack that tells connected agents how to use the brain as first-stop context.

**Repository:** https://github.com/garrytan/gbrain

**Reviewed commit:** [9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac](https://github.com/garrytan/gbrain/commit/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac)

**Last checked:** 2026-06-04

## Core Ideas

**The active store is a Postgres-shaped brain index over markdown.** The schema centers on `sources`, `pages`, chunks, links, timeline entries, facts, takes, files, eval candidates, and MCP logs, with PGLite as the default local Postgres-compatible engine and full Postgres/pgvector for hosted/shared deployments ([src/schema.sql](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/schema.sql), [docs/ENGINES.md](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/docs/ENGINES.md)). The README still frames the brain repo as system of record: markdown is synced into the database for retrieval, and `put_page` can reverse-write DB pages back to disk ([README.md](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/README.md), [src/core/write-through.ts](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/core/write-through.ts)).

**One operation layer feeds CLI, MCP, and agents.** `src/core/operations.ts` is the single contract for operations such as `put_page`, `search`, `query`, `think`, `recall`, `extract_facts`, `find_trajectory`, and `schema_apply_mutations`; the MCP server and CLI route through those definitions rather than keeping separate business logic ([src/core/operations.ts](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/core/operations.ts), [src/mcp/dispatch.ts](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/mcp/dispatch.ts)). Remote calls are scope-gated and source-scoped; local calls can use stronger write-through and provenance paths.

**Writes create several derived access structures.** `put_page` parses markdown, chunks and embeds content, stores the page, optionally writes it through to disk, reconciles links and timeline entries for trusted callers, queues facts extraction, and can run post-write lint ([src/core/operations.ts](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/core/operations.ts), [src/core/import-file.ts](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/core/import-file.ts), [src/core/link-extraction.ts](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/core/link-extraction.ts)). The graph is not an external graph database; it is typed edge tables and link-extraction code over the same relational substrate.

**Context efficiency is ranked retrieval plus contextualized document vectors.** Search combines keyword, vector, RRF, source boosts, reranking, graph signals, deduplication, token budgets, adaptive return, autocut, and cache gates before serving chunks ([src/core/search/hybrid.ts](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/core/search/hybrid.ts), [src/core/search/graph-signals.ts](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/core/search/graph-signals.ts)). Its contextual retrieval tier wraps canonical chunks with document context before embedding: `balanced` defaults to a title-only wrapper, while `tokenmax` can generate one-sentence Haiku synopses per chunk, embed the wrapped text, and keep raw `content_chunks.chunk_text` as the stored snippet ([src/core/search/mode.ts](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/core/search/mode.ts), [src/core/embedding-context.ts](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/core/embedding-context.ts), [src/core/page-summary.ts](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/core/page-summary.ts), [src/core/contextual-retrieval-service.ts](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/core/contextual-retrieval-service.ts)). `think` gathers pages, takes, and optional graph/trajectory/calibration context before an LLM synthesis call, rather than loading the full brain ([src/core/think/gather.ts](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/core/think/gather.ts), [src/core/think/index.ts](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/core/think/index.ts)).

**The background cycle turns traces and accumulated entries into stronger artifacts.** `runCycle` composes sync, extraction, transcript synthesis, pattern detection, fact consolidation, take grading, calibration, atom extraction, concept synthesis, skill optimization, embedding, orphan checks, and purge phases under locks ([src/core/cycle.ts](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/core/cycle.ts)). Some phases are deterministic metadata/index maintenance; others call LLMs or subagents to write new pages, takes, patterns, concepts, or proposed skill edits ([src/core/cycle/synthesize.ts](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/core/cycle/synthesize.ts), [src/core/cycle/patterns.ts](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/core/cycle/patterns.ts), [src/core/cycle/phases/consolidate.ts](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/core/cycle/phases/consolidate.ts), [src/core/skillopt/orchestrator.ts](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/core/skillopt/orchestrator.ts)).

**Adoption is skillpack-driven.** GBrain ships 43 markdown skills and an installer protocol; the install docs tell agents to run the signal detector on every inbound message and do brain-first lookup before external APIs ([INSTALL_FOR_AGENTS.md](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/INSTALL_FOR_AGENTS.md), [skills/signal-detector/SKILL.md](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/skills/signal-detector/SKILL.md), [skills/query/SKILL.md](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/skills/query/SKILL.md)). That makes GBrain partly a memory service and partly an agent-operating-system package: the strongest behavior change depends on the host agent reading and following the shipped skills.

## Artifact analysis

- **Storage substrate:** `rdbms` — The behavior-shaping live store is Postgres/PGLite tables for pages, chunks, embeddings, links, facts, takes, jobs, logs, and caches; markdown files remain the user-auditable source/write-through surface rather than the only active substrate.
- **Representational form:** `prose` `symbolic` `parametric` — Markdown pages, skills, facts, takes, summaries, reports, and prompts are prose; frontmatter, schemas, typed links, operations, SQL rows, queue records, and config are symbolic; embeddings and reranker/vector retrieval state are parametric access structures.
- **Lineage:** `authored` `imported` `trace-extracted` — Skills, schemas, code, and user-authored pages are authored; synced markdown/code/images and external captures are imported; hot facts, atoms, patterns, concepts, eval candidates, subagent transcripts, synthesis pages, and skillopt candidates can derive from conversation turns, transcripts, tool calls, and accumulated brain evidence.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` `learning` `enforcement` — Pages, facts, takes, trajectories, and syntheses advise agents; skills and prompts instruct; schema packs, source scopes, graph edges, and operation definitions route; validators, lint gates, auth scopes, budgets, locks, and mutation guards enforce or validate; retrieval scores, emotional weight, graph signals, and rerankers rank; extraction, consolidation, concept synthesis, calibration, eval replay, and skillopt implement learning loops.

**Pages and markdown write-through.** A page bundles compiled truth, timeline text, frontmatter, type, title, timestamps, source identity, and derived generation counters in the database, with optional markdown write-through into the brain repo ([src/schema.sql](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/schema.sql), [src/core/operations.ts](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/core/operations.ts)). Its authority is primarily knowledge context, but frontmatter/type/schema fields also drive routing, extraction eligibility, source scoping, and cache invalidation.

**Chunks, embeddings, contextual wrappers, search cache, and graph links.** Content chunks, code edges, typed links, timeline entries, image/file rows, and query caches are derived system-definition artifacts: they determine what evidence is cheap to retrieve and how results are ranked or expanded. Contextual retrieval adds a second document-side indexing surface without replacing the canonical chunk: title or generated synopsis text is prepended only for the embedding input, `contextual_retrieval_mode` and `corpus_generation` record the applied tier, and failed synopsis generation falls back page-wide to the cheaper title tier before committing replacement chunks ([src/core/import-file.ts](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/core/import-file.ts), [src/core/contextual-retrieval-service.ts](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/core/contextual-retrieval-service.ts), [src/schema.sql](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/schema.sql)). Regeneration is tied to source hashes, schema/chunker versions, page generations, corpus generation, link-extractor freshness, and source sync state ([src/core/link-extraction.ts](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/core/link-extraction.ts), [src/core/search/query-cache.ts](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/core/search/query-cache.ts)).

**Hot facts, takes, and trajectories.** The `facts` and `takes` surfaces turn conversation/page evidence into shorter claims with confidence, validity windows, notability, embeddings, consolidation markers, supersession fields, and holder/source metadata ([src/core/facts/extract.ts](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/core/facts/extract.ts), [src/core/facts/backstop.ts](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/core/facts/backstop.ts), [src/core/cycle/phases/consolidate.ts](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/core/cycle/phases/consolidate.ts)). They can be read directly by `recall`, rendered into `think` prompts as takes/trajectory blocks, or injected into MCP `_meta.brain_hot_memory`.

**Skills, schema packs, and operation definitions.** Markdown skills, schema-pack manifests, operation schemas, and MCP tool definitions are retained system-definition artifacts. They do not merely describe the brain; they decide which tools agents should use, which page types exist, which facts get extracted, what remote callers can mutate, and how host agents should route tasks ([skills/RESOLVER.md](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/skills/RESOLVER.md), [src/core/schema-pack/manifest-v1.ts](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/core/schema-pack/manifest-v1.ts), [src/core/operations.ts](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/core/operations.ts)).

**Promotion path.** GBrain has several promotion paths: raw markdown/captures become parsed pages, chunks, links, and facts; repeated facts can become takes; transcripts can become new pages; atom pages can become concept pages; evaluation traces can become regression candidates; skill benchmarks can produce accepted or proposed skill edits. Promotion is implemented, but the authority of each promoted artifact varies from soft context to validated skill mutation.

## Comparison with Our System

| Dimension | GBrain | Commonplace |
|---|---|---|
| Primary purpose | Operate a personal/team agent brain for capture, retrieval, synthesis, and autonomous maintenance | Maintain a typed methodology KB for agents and maintainers |
| Canonical substrate | Postgres/PGLite active store with markdown repo write-through/sync | Git-tracked Markdown artifacts with generated indexes and validators |
| Retrieval | Hybrid keyword/vector/graph/reranker search, `think`, trajectory blocks, hot-fact recall | `rg`, curated/generated indexes, links, source snapshots, review bundles |
| Write path | CLI/MCP writes, capture/import/sync, signal detector, dream cycle, facts backstop, skillopt | Human/agent-authored notes, reviews, instructions, validation, explicit review gates |
| Governance | Auth scopes, source scoping, locks, budgets, doctor checks, eval capture, skill gates | Collection contracts, type specs, deterministic validation, semantic review, git history |

The closest alignment is that both systems treat prose files as operational artifacts rather than inert documentation. GBrain pushes further into service infrastructure: it owns database indexes, MCP transport, OAuth scopes, queues, background daemons, LLM extraction, and ranking. Commonplace keeps more authority in repo-local Markdown, schemas, instructions, and validation scripts, which makes review and rollback cheaper but read-back less automatic.

The main tradeoff is power versus inspectability. GBrain can serve targeted context and update derived memory continuously, including hot facts and dream-cycle artifacts. The cost is a larger trusted runtime surface: agents must trust operation dispatch, database migrations, background queue behavior, retrieval ranking, and LLM-derived maintenance loops. Commonplace is slower and more manual, but most behavior-shaping state is visible in ordinary diffs.

### Borrowable Ideas

**Session-scoped hot memory as metadata, not prompt prose.** Commonplace could expose a small, clearly labeled review/run memory payload to tools or agents instead of requiring agents to search the whole KB for immediate state. Ready for narrow review workflows.

**Generated context should carry freshness and lineage gates.** GBrain's page generation counters, extraction watermarks, chunker versions, and cache invalidation machinery are more explicit than many markdown-only indexes. Commonplace can borrow the pattern for expensive semantic reports and source-derived views.

**Treat background maintenance as a phase graph.** The `runCycle` phase list is a useful operational contract: it names the order, scope, and mutating status of each maintenance step. Commonplace could use a comparable phase manifest for review sweeps, index refresh, source snapshots, and semantic QA.

**Do not borrow always-on capture without an authority boundary.** The signal detector is powerful but high-risk: every inbound message can become durable memory. Commonplace would need explicit workshop scopes, expiry, source attribution, and review before adopting comparable ambient capture.

**Skill optimization needs held-out gates before mutation.** GBrain's SkillOpt loop is too product-specific to import directly, but the distinction between bundled-skill proposals and accepted mutations is a useful guardrail for any future Commonplace skill-evolution workflow.

## Write side

**Write agency:** `manual` `automatic` — Users and agents can manually author pages, facts, takes, schema mutations, and skills through CLI/MCP/files; automatic paths import/sync files, extract links/timelines/facts/atoms, write pattern/concept/synthesis pages, consolidate facts, recompute salience, capture eval candidates, run skillopt, and purge expired deleted rows.

**Curation operations:** `consolidate` `dedup` `evolve` `synthesize` `invalidate` `decay` `promote` — Consolidation clusters facts into takes; duplicate detection avoids repeated facts and sync imports; auto-link/timeline/facts extraction and emotional-weight recomputation evolve stored metadata; dream/pattern/concept/think paths synthesize new retained pages or claims; valid-until, supersession, soft-delete, and forget paths invalidate; purge removes expired deleted/archive rows; facts, atoms, and concepts are promoted into stronger or more salient artifacts.

### Trace-learning

**Trace source:** `session-logs` `tool-traces` `event-streams` `trajectories` — GBrain consumes conversation turns, transcript files, MCP/search/query eval traces, subagent messages/tool executions, and timeline/trajectory rows.

**Learning scope:** `per-project` `cross-task` — Learning is source/brain scoped and reused across later tasks, agents, queries, and cycle runs; some paths are per-session but the retained facts/pages/takes are not limited to the original turn.

**Learning timing:** `online` `offline` `staged` — `extract_facts` and the facts backstop can run inline or queue near a write; dream-cycle phases and skillopt are staged/offline maintenance; sync/import and eval capture can run continuously as background side effects.

**Distilled form:** `prose` `symbolic` `parametric` — Outputs include markdown pages, facts, takes, concepts, patterns, reports, and skill edits; symbolic rows, frontmatter, links, schema metadata, eval records, and queue logs; and embeddings over pages/facts/chunks for later retrieval.

**Trace source.** The qualifying code-grounded mechanisms are the hot-memory extractor over conversation turns, transcript-to-page synthesis, subagent transcript rendering, eval-capture rows from `search`/`query`, atom extraction from transcripts/pages, and concept/pattern synthesis over accumulated retained material ([src/core/facts/extract.ts](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/core/facts/extract.ts), [src/core/cycle/synthesize.ts](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/core/cycle/synthesize.ts), [src/core/minions/transcript.ts](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/core/minions/transcript.ts), [src/core/eval-capture.ts](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/core/eval-capture.ts), [src/core/cycle/extract-atoms.ts](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/core/cycle/extract-atoms.ts)).

**Extraction.** Extraction uses both deterministic and LLM oracles. Deterministic code parses markdown, wikilinks, frontmatter, timelines, facts fences, code references, content hashes, and sync manifests. LLM calls extract facts, transcript pages, patterns, atoms, concept narratives, calibration profiles, and skill edits, usually behind model, budget, lock, source, and review gates. Deduplication uses content hashes, cosine thresholds, row identities, and idempotency keys depending on the path.

**Scope and timing.** Online write hooks favor responsiveness: `put_page` returns while facts extraction can run queued, and MCP hot memory is cached for short sessions. Offline/staged paths favor stronger derivation: the cycle runs ordered phases after sync/extract state settles, and skillopt uses preflight, locks, benchmarks, validation, and held-out gates before mutation.

**Survey fit.** GBrain is a broad trace-learning operational-memory system. It strengthens the survey claim that trace-learning is not one mechanism: the same codebase includes raw trace capture, hot-fact extraction, consolidation, synthesis, ranking feedback, and proposed skill mutation, each with different authority and review needs.

## Read-back

**Read-back:** `both` — Agents and users can explicitly pull memory through CLI/MCP search, query, recall, graph, page, and think operations; GBrain also pushes retained facts and trajectory/calibration context into MCP or synthesis responses without the receiving agent issuing a separate memory lookup.

**Read-back signal:** `coarse` `identifier` `inferred / lexical` `inferred / embedding` `inferred / judgment` — Hot-memory `_meta` falls back to recent/session facts; recall and trajectory paths use session/entity/source identifiers; search and query use lexical/vector/reranker inference; `think` uses intent classification, entity extraction, retrieval results, and optional calibration/trajectory injection.

**Faithfulness tested:** `no` — The repository has eval capture, replay, retrieval benchmarks, A/B-style calibration utilities, and quality gates, but I did not find a code path that ablates a particular pushed memory item and verifies that it changed a downstream agent action.

**Direction edge cases.** The skillpack's brain-first protocol is instruction-level push into the host agent's operating context, but it is static baseline instruction rather than retained memory read-back. The memory push surfaces are more specific: `_meta.brain_hot_memory` is attached to MCP tool responses via the dispatcher, and `think` may inject trajectory/calibration blocks after retrieval and before the synthesis model call ([src/core/facts/meta-hook.ts](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/core/facts/meta-hook.ts), [src/commands/serve-http.ts](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/commands/serve-http.ts), [src/core/think/index.ts](https://github.com/garrytan/gbrain/blob/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac/src/core/think/index.ts)).

**Targeting and signal.** Pull retrieval has several targeting modes: exact slug/page reads, source scopes, type filters, graph traversal, hybrid search, query expansion, embeddings, reranking, and graph signals. Push targeting is mixed: `_meta.brain_hot_memory` chooses session facts when a session id exists, otherwise recent source facts; `think` trajectory injection fires only for temporal or knowledge-update intents and candidate entities.

**Injection point.** Read-back is pre-invocation context assembly for the consumer: MCP response metadata is attached before the host agent sees the tool result; `think` builds page/take/graph/calibration/trajectory blocks before the synthesis LLM call. After-turn extraction, eval capture, cache writes, consolidation, and purge are write-side maintenance.

**Selection, scope, and complexity.** GBrain has many context-efficiency controls: search limits, reranker/autocut/adaptive-return modes, token budgets, query cache, source scopes, visibility filters, trajectory timeouts, hot-memory top-k caps, and effective-confidence sorting. Actual context dilution and whether agents obey injected memory are not proven by code.

**Authority at consumption.** Search/query/recall results are advisory context; `think` uses retrieved memory inside a synthesis prompt; hot-memory `_meta` gives the host agent extra facts but does not enforce action; schema/auth/operation guards can enforce write/read boundaries; skill instructions can strongly steer compliant host agents but remain dependent on adoption.

**Other consumers.** Humans consume markdown pages, CLI output, admin UI, reports, doctor checks, and skill files. Background jobs, evaluators, schema tools, retrievers, and connected MCP clients also consume the same retained artifacts through narrower operational surfaces.

## Curiosity Pass

**The "brain repo is source of record" claim coexists with a very strong database.** Markdown keeps the system inspectable, but many behavior-shaping artifacts live only or primarily in tables: facts, eval candidates, query cache, job ledgers, OAuth clients, embeddings, MCP logs, and generation clocks. A backup/export story needs to cover both surfaces.

**GBrain contains several memory systems under one brand.** It is a RAG system, hot-fact memory, graph database, skillpack, job queue, eval recorder, schema authoring surface, and skill optimizer. Reviews and operators should classify features by artifact and authority rather than asking whether "GBrain memory" works as one unit.

**Some automatic writes are stronger than their review state.** Facts, atoms, patterns, concepts, and skill proposals can be LLM-derived. The code has budgets, locks, idempotency, and gates, but per-claim source span review is uneven across paths.

**The pushed `_meta` channel is a clean design boundary.** Injecting hot facts as metadata keeps the tool result text cleaner than silently splicing facts into every answer, though it depends on host agents actually reading `_meta`.

**SkillOpt is the highest-authority learning path.** Most trace-extracted artifacts advise retrieval or synthesis. SkillOpt can rewrite instructions that future agents follow, so its dirty-tree, bundled-skill, benchmark, held-out, and validation gates are more consequential than ordinary retrieval evals.

## What to Watch

- Whether hot-memory `_meta` becomes supported by more host agents and whether any host logs prove the agent actually used injected facts.
- Whether automatic fact/atom/pattern/concept synthesis gains per-claim provenance spans and review state comparable to source-grounded notes.
- Whether database-only retained state gets a complete export/restore path into the brain repo or another auditable artifact bundle.
- Whether schema-authoring and skillopt mutations become common over remote MCP; that would raise the importance of audit trails, held-out tests, and rollback.
- Whether retrieval benchmarks cover the full read-back stack, including graph signals, trajectory injection, hot facts, and pushed skill instructions.

Relevant Notes:

- [Trace-learning techniques in related systems](../trace-learning-techniques-in-related-systems.md) - places: GBrain derives facts, atoms, concepts, patterns, eval rows, and skill candidates from conversation/session/tool traces and retained evidence.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: GBrain has both explicit pull retrieval and pushed hot-memory/trajectory context.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: GBrain's markdown, DB rows, embeddings, graph links, skills, and operation definitions carry different forms and authorities.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: pages, facts, takes, trajectories, and syntheses usually advise rather than enforce.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: operations, auth scopes, skills, schema packs, validators, queues, and ranking/indexing code govern future behavior.
- [Use trace extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-extraction-as-meta-learning.md) - exemplifies: GBrain's hot facts, dream cycle, eval capture, and skillopt are trace-learning paths with different promotion thresholds.
