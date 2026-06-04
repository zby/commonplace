---
description: "sage-wiki review: LLM-compiled wiki memory with SQLite search/vector/ontology state, MCP pull tools, session capture, and trust gates"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
status: current
last-checked: "2026-06-04"
---

# sage-wiki

sage-wiki, from xoai, is a Go implementation of an LLM-compiled personal or team knowledge base inspired by Andrej Karpathy's "drop documents in, compile a wiki out" framing. At the reviewed commit it ingests source documents, indexes or compiles them by tier, writes Markdown wiki articles, stores search/vector/ontology state in SQLite, exposes CLI and MCP tools for agents, generates agent skill instructions, records conversational captures and scribe-extracted entities, and quarantines generated Q&A outputs until they pass trust checks. Its memory is strongest as a pull-addressable wiki and search substrate; proactive use depends on generated agent instructions rather than an always-running retrieval hook.

**Repository:** https://github.com/xoai/sage-wiki

**Source directory:** related-systems/xoai--sage-wiki

**Reviewed commit:** [2260770053873e46669ec2a7ebaee6c24634c133](https://github.com/xoai/sage-wiki/commit/2260770053873e46669ec2a7ebaee6c24634c133)

**Last checked:** 2026-06-04

## Core Ideas

**A source tree is compiled into a dual file/database wiki.** `sage-wiki compile` diffs source files, summarizes sources, extracts concepts, writes concept articles, creates source citation edges, indexes articles in FTS5, stores vectors, chunks article text, populates ontology entities/relations, writes a manifest, and optionally git-commits the output ([pipeline.go](https://github.com/xoai/sage-wiki/blob/2260770053873e46669ec2a7ebaee6c24634c133/internal/compiler/pipeline.go), [write.go](https://github.com/xoai/sage-wiki/blob/2260770053873e46669ec2a7ebaee6c24634c133/internal/compiler/write.go), [db.go](https://github.com/xoai/sage-wiki/blob/2260770053873e46669ec2a7ebaee6c24634c133/internal/storage/db.go)). The retained artifact is not only Markdown: the operational wiki also includes `.manifest.json`, SQLite FTS/vector/chunk tables, ontology tables, compile state, and trust tables.

**Context efficiency is tiered, chunked, and budgeted.** The large-vault path routes sources through tiers: index-only, index+embed, code-parse, or full compile. Search can signal uncompiled sources, record query hits, promote sources to Tier 3, and compile a bounded topic cluster on demand ([tiers.go](https://github.com/xoai/sage-wiki/blob/2260770053873e46669ec2a7ebaee6c24634c133/internal/compiler/tiers.go), [ondemand.go](https://github.com/xoai/sage-wiki/blob/2260770053873e46669ec2a7ebaee6c24634c133/internal/compiler/ondemand.go), [server.go](https://github.com/xoai/sage-wiki/blob/2260770053873e46669ec2a7ebaee6c24634c133/internal/mcp/server.go)). Query assembly then uses chunk-level FTS/vector search, optional LLM query expansion, optional LLM re-ranking, graph expansion, and token-budgeted article loading before synthesis ([query.go](https://github.com/xoai/sage-wiki/blob/2260770053873e46669ec2a7ebaee6c24634c133/internal/query/query.go), [pipeline.go](https://github.com/xoai/sage-wiki/blob/2260770053873e46669ec2a7ebaee6c24634c133/internal/search/pipeline.go), [relevance.go](https://github.com/xoai/sage-wiki/blob/2260770053873e46669ec2a7ebaee6c24634c133/internal/graph/relevance.go)).

**Agents interact through MCP and generated skill instructions.** The MCP server registers read tools (`wiki_search`, `wiki_read`, `wiki_status`, `wiki_ontology_query`, `wiki_list`, `wiki_provenance`), write tools (`wiki_add_source`, `wiki_write_summary`, `wiki_write_article`, `wiki_add_ontology`, `wiki_learn`, `wiki_capture`, `wiki_compile_topic`), and compound compile/lint tools ([server.go](https://github.com/xoai/sage-wiki/blob/2260770053873e46669ec2a7ebaee6c24634c133/internal/mcp/server.go), [tools_write.go](https://github.com/xoai/sage-wiki/blob/2260770053873e46669ec2a7ebaee6c24634c133/internal/mcp/tools_write.go), [tools_compound.go](https://github.com/xoai/sage-wiki/blob/2260770053873e46669ec2a7ebaee6c24634c133/internal/mcp/tools_compound.go)). Skill generation writes a marked section to agent instruction files telling agents when to search, what to capture, and how to query, but it does not itself retrieve memory at runtime ([skill.go](https://github.com/xoai/sage-wiki/blob/2260770053873e46669ec2a7ebaee6c24634c133/internal/skill/skill.go), [base.md.tmpl](https://github.com/xoai/sage-wiki/blob/2260770053873e46669ec2a7ebaee6c24634c133/internal/skill/packs/base.md.tmpl)).

**Generated outputs are quarantined before they become searchable memory.** Q&A outputs can be written to `wiki/under_review/`, matched against similar questions, checked for answer agreement, verified against source passages, promoted to `wiki/outputs/`, indexed into FTS/vector/chunk stores, and represented as ontology artifacts with `derived_from` edges. Source changes can demote confirmed outputs and remove them from search indexes ([query.go](https://github.com/xoai/sage-wiki/blob/2260770053873e46669ec2a7ebaee6c24634c133/internal/query/query.go), [hooks.go](https://github.com/xoai/sage-wiki/blob/2260770053873e46669ec2a7ebaee6c24634c133/internal/trust/hooks.go), [promote.go](https://github.com/xoai/sage-wiki/blob/2260770053873e46669ec2a7ebaee6c24634c133/internal/trust/promote.go), [source_check.go](https://github.com/xoai/sage-wiki/blob/2260770053873e46669ec2a7ebaee6c24634c133/internal/trust/source_check.go)).

**Trace-derived capture is present but separate from read-back.** `wiki_capture` extracts conversation knowledge into `raw/captures/*.md` source files; `wiki_learn` stores single nuggets in the SQLite `learnings` table; `sage-wiki scribe` compresses Claude Code JSONL sessions, extracts up to ten ontology entities via an LLM, deduplicates/updates against the ontology store, and inserts entities and relations ([tools_write.go](https://github.com/xoai/sage-wiki/blob/2260770053873e46669ec2a7ebaee6c24634c133/internal/mcp/tools_write.go), [session.go](https://github.com/xoai/sage-wiki/blob/2260770053873e46669ec2a7ebaee6c24634c133/internal/scribe/session.go), [main.go](https://github.com/xoai/sage-wiki/blob/2260770053873e46669ec2a7ebaee6c24634c133/cmd/sage-wiki/main.go)). Those traces become durable memory only after the write/capture/scribe path runs; they are later served by ordinary search, ontology, compile, or query paths.

**The latest commit tightens output quality without adding semantic truth maintenance.** After Pass 3, `StripBrokenWikilinks()` scans `wiki/concepts`, strips brackets from wikilinks whose concept article does not exist, and leaves the bare text intact. This prevents phantom graph links from LLM-written articles while preserving readable prose ([pipeline.go](https://github.com/xoai/sage-wiki/blob/2260770053873e46669ec2a7ebaee6c24634c133/internal/compiler/pipeline.go), [write.go](https://github.com/xoai/sage-wiki/blob/2260770053873e46669ec2a7ebaee6c24634c133/internal/compiler/write.go), [strip_links_test.go](https://github.com/xoai/sage-wiki/blob/2260770053873e46669ec2a7ebaee6c24634c133/internal/compiler/strip_links_test.go)). This is link hygiene, not a proof that the remaining claims are correct.

## Artifact analysis

- **Storage substrate:** `files` `repo` `sqlite` `vector` `graph` `service-object` — Source files, generated Markdown, manifests, config, skill files, and optional git history sit in the filesystem/repo; SQLite stores FTS5 entries, vectors, chunk metadata, ontology graph tables, learnings, compile tiers, and trust state; CLI/MCP/server objects assemble those artifacts for users and agents.
- **Representational form:** `prose` `symbolic` `parametric` — Sources, summaries, articles, captures, skills, and query outputs are prose; manifests, config, frontmatter, compile tiers, trust states, routes, tables, ontology edges, and tool schemas are symbolic; embeddings in `vec_entries`, `vec_chunks`, and `pending_questions_vec` are distributed-parametric selectors.
- **Lineage:** `authored` `imported` `trace-extracted` — Configuration, prompts, packs, skills, source documents, and manual articles are authored/imported; compiled articles, summaries, ontology edges, chunks, embeddings, query outputs, capture files, learnings, and scribe entities are derived views; `wiki_capture` and session scribe specifically derive durable artifacts from conversation traces.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` `learning` — Wiki articles and outputs advise as knowledge; generated skills instruct agents to consult/capture; tool schemas, config, tier rules, and compile coordinator route work; lint/trust/source-change checks validate or quarantine; BM25/vector/RRF/reranker/graph scoring rank context; capture/scribe/compile/trust loops learn new retained artifacts.

**Compiled wiki articles and summaries.** Storage substrate: Markdown files under the configured output directory plus manifest records, FTS5 rows, chunk rows, vectors, and ontology entities. Representational form: prose article bodies, symbolic frontmatter/source links/type/confidence, and embeddings. Lineage: derived from imported source files by summarize, concept extraction, article writing, relation extraction, and chunking. Behavioral authority: knowledge when read by humans or agents, ranking authority through search indexes, and weak instruction authority when inserted into Q&A context.

**Source and compile state.** Storage substrate: source files, `.manifest.json`, `compile_items`, and optional `.wikitier`/frontmatter overrides. Representational form: symbolic hashes, tiers, pass-completion flags, query-hit counts, quality scores, and stale/promoted timestamps. Lineage: imported source state plus automatic compile bookkeeping. Behavioral authority: routing and ranking over what gets indexed, embedded, compiled, recompiled, or left as searchable-but-uncompiled material.

**Ontology graph.** Storage substrate: SQLite `entities` and `relations` tables plus article wikilinks and manifest provenance. Representational form: symbolic entity ids, types, relation names, source citation edges, and generated relation edges extracted from article text. Lineage: partly LLM-extracted from source documents, partly manually written through MCP/CLI, partly trace-extracted by scribe. Behavioral authority: knowledge for navigation and graph display, routing/ranking for graph-expanded query context, and validation through configured relation/entity vocabularies.

**Search, query, and ranking pipeline.** Storage substrate: SQLite FTS5, vector blobs, chunk tables, graph state, and source files read at query time. Representational form: symbolic scores/ranks/budgets, parametric embeddings, and prose context blocks. Lineage: derived from compiled artifacts and current query text. Behavioral authority: ranking and knowledge assembly; it decides what articles enter the LLM's context and in what shape, but the code does not prove the model faithfully uses that context.

**Generated agent skills.** Storage substrate: instruction files such as `CLAUDE.md`, `AGENTS.md`, `.cursorrules`, or `sage-wiki-skill.md`. Representational form: prose instructions plus marker-delimited symbolic update boundaries and project-specific tool/type/relation names. Lineage: authored template rendered from `config.yaml` and pack metadata. Behavioral authority: instruction over future agents, telling them when to call pull/write tools; it does not itself load wiki contents.

**Captured traces, learnings, and scribe entities.** Storage substrate: `raw/captures/*.md`, SQLite `learnings`, and ontology rows. Representational form: prose captures/learnings, symbolic tags/types/entity ids/relations, and later embeddings/chunks if compiled. Lineage: trace-extracted from conversations or sessions, with fallback to raw capture when LLM extraction fails. Behavioral authority: knowledge once searched/read, learning when the capture/scribe loop expands the store, and validation/routing when entity ids and relation types are checked against configured vocabularies.

**Trust-managed Q&A outputs.** Storage substrate: `wiki/under_review`, `wiki/outputs`, `pending_outputs`, `confirmation_sources`, `pending_questions_vec`, FTS/vector/chunk indexes, and ontology artifact edges. Representational form: prose answers, symbolic trust states/confirmations/source hashes, and question/output embeddings. Lineage: generated from query context and sources, then promoted, conflicted, rejected, or demoted by consensus, grounding, and source-change checks. Behavioral authority: pending outputs are quarantined knowledge; confirmed outputs gain ranking and knowledge authority by entering search.

**Promotion path.** sage-wiki has several promotion ladders: source file -> indexed source -> embedded source -> full article; query output -> pending output -> confirmed indexed artifact; source/query hits -> Tier 3 compile candidate; conversation text -> capture file or ontology entity -> compiled/searchable wiki memory. The system can strengthen access and authority, but not into hard enforcement: confirmed outputs and compiled articles remain advisory context, not rules or gates.

## Comparison with Our System

| Dimension | sage-wiki | Commonplace |
|---|---|---|
| Primary purpose | LLM-compiled personal/team wiki and MCP memory layer | Git-native methodology KB for agent-operated knowledge systems |
| Canonical retained artifact | Source files, generated wiki articles, SQLite indexes, ontology/trust state | Typed Markdown notes, instructions, reviews, sources, generated indexes, review reports |
| Storage substrate | Files plus SQLite FTS/vector/chunk/ontology/trust tables | Repository files plus deterministic indexes and validation/review outputs |
| Write path | Compile, capture, learn, scribe, MCP write tools, trust promotion/demotion | Authored notes, snapshots, explicit review gates, validation, index refreshes |
| Read-back | Pull through CLI/MCP/search/query; generated skills instruct agents to pull | Mostly explicit pull through `rg`, indexes, links, skills, loaded instructions |
| Governance | Trust quarantine, grounding, consensus, lint, source-change demotion, tier policy | Type specs, collection contracts, citations, deterministic validation, semantic gates, git history |

sage-wiki is closer to a runtime retrieval layer than Commonplace is. It has a richer query pipeline, vector search, ontology expansion, compiled output directories, web/TUI surfaces, MCP tools, and source-to-article automation. Commonplace is more conservative about authority: notes are directly reviewed Markdown artifacts with path-valued types and validator-enforced contracts, while generated Commonplace indexes stay secondary to authored artifacts.

The interesting design contrast is how each system handles generated claims. sage-wiki's trust pipeline explicitly recognizes that LLM answers can poison future retrieval, so it quarantines outputs and requires agreement/grounding before indexing them. Commonplace has stronger artifact-level validation and semantic review, but less built-in machinery for repeated-output consensus or automatic source-change demotion of generated answers.

### Borrowable Ideas

**Quarantine generated answers before indexing.** Ready now as a design pattern. Commonplace already treats ingests/reviews cautiously, but a specific `under_review` lane for generated synthesis artifacts would make it harder for unreviewed answers to become retrieval evidence.

**Expose uncompiled-source signals in search results.** Needs a concrete high-volume source workflow. sage-wiki's search response can say "there are matching sources below full compile tier"; Commonplace could similarly surface "source exists but no note/review yet" without pretending the source has already been distilled.

**Use source-change demotion for derived artifacts.** Ready for generated reports and synthesized notes. The trust hook that demotes confirmed outputs when cited source hashes change is a clean invalidation mechanism for derived KB material.

**Keep skill generation separate from retrieval.** Ready now. sage-wiki's generated skill instructions improve agent behavior without hiding read-back inside a black-box daemon; Commonplace should preserve this separation when adding richer search or MCP access.

**Do not borrow wholesale wiki compilation as the default authoring model.** Needs a distinct use case. LLM-compiled articles are useful for broad source corpora, but Commonplace's methodology layer depends on compact claims, explicit provenance, and reviewable authority. Full wiki compilation would be too generative for the default path.

## Write side

**Write agency:** `manual` `automatic` — Users and agents can add sources, write summaries/articles, add ontology entries, learn nuggets, promote/reject outputs, and edit generated files. Automatic writes come from compile passes, capture extraction, scribe extraction, indexing/chunking/embedding, query auto-filing, trust promotion/demotion, tier promotion/demotion, concept deduplication, and broken-link cleanup.

**Curation operations:** `dedup` `evolve` `invalidate` `decay` `promote` — Concept dedup merges near-duplicate candidates into existing concepts/aliases before article writing; scribe updates existing ontology definitions when a new extracted definition differs. The broken-wikilink sweep evolves existing article text by removing invalid link markup. Trust source-change checks demote confirmed outputs to stale and de-index them. Tier demotion downshifts stale sources from full compile to lower-tier handling. Query-hit and on-demand policies promote sources to Tier 3, and trust promotion moves verified outputs into indexed search.

### Trace-derived learning

**Trace source:** `session-logs` `event-streams` — `wiki_capture` consumes conversation excerpts supplied through MCP, while `sage-wiki scribe` consumes Claude Code session JSONL and keeps only user/assistant text after stripping thinking/tool blocks.

**Learning scope:** `per-project` `cross-task` — Captures, learnings, and scribe entities are stored in a project wiki and can shape later tasks for any agent connected to that project.

**Learning timing:** `online` `staged` — MCP capture and learn write during an agent session; compilation, verification, trust promotion, and scribe invocation are staged operations.

**Distilled form:** `prose` `symbolic` `parametric` — Trace outputs become prose capture files/learnings, symbolic entity/relation rows and tags, and later embeddings/chunk indexes after compilation.

**Trace source.** The trace-learning path is explicit but user/agent-triggered. `wiki_capture` takes conversation text, context, and tags, asks the configured LLM for knowledge items, writes each item to `raw/captures/*.md`, and updates the manifest. On extraction failure it stores raw content as a single capture file. `SessionScribe` reads JSONL, compresses away tool/thinking material, extracts entity candidates, enforces kebab-case ids, checks existing entities, and adds or updates ontology state.

**Extraction.** The extraction oracles are authored prompts plus the configured LLM. `wiki_capture` asks for key learnings as JSON items; session scribe asks for at most ten specific entities with valid configured entity types and optional relations. The source code has specificity gates and duplicate checks, but no independent semantic reviewer for captured content before it becomes source/ontology memory.

**Scope and timing.** A captured item first becomes a source file or learning row; it changes later behavior only when searched directly or compiled into article/index/ontology state. Session scribe writes ontology entities immediately, but article generation from scribe-created entities is still mediated by compile-on-demand or later compile workflows.

**Survey position.** sage-wiki belongs in the "trace to knowledge substrate" family rather than the "trace to enforced policy" family. It strengthens the survey claim that trace-derived memory needs a separate read-back mechanism: capture/scribe can create memory, but future behavior still depends on explicit search, generated skill instructions, or query context assembly.

## Read-back

**Read-back:** `pull` — Stored memory reaches agents through explicit CLI/MCP/search/query/read/ontology/provenance calls. Generated skill files instruct agents when to pull from the wiki, but the reviewed code does not install an always-load or event-triggered retrieval hook that injects wiki memory into a model call without the agent or host choosing a tool/query path.

The read path is still substantial. `wiki_search` performs hybrid search over FTS5 and vectors and can return compile hints; `wiki_read` returns a selected article; `wiki_ontology_query` traverses relations; `query` builds token-budgeted context from chunk/doc search plus graph expansion and asks an LLM to synthesize an answer. These are pull read-back because the consuming agent or user asks for them.

Static skill files are an edge case. They are instruction artifacts, not accumulated memory read-back: they tell the agent to call `wiki_search`, `wiki_read`, and `wiki_ontology_query` before certain work, but they do not themselves insert retained wiki content. If a host agent obeys the skill and searches before acting, the memory arrives through the pull tool call.

Selection is bounded and multi-stage rather than "load the wiki." The enhanced query pipeline caps search candidates, uses chunk-level FTS/vector retrieval, deduplicates to document level, optionally reranks, adds graph-expanded articles, truncates large articles, and stops at a configured context token budget. Precision, recall, and context dilution are not proven by static code inspection.

Authority at consumption is advisory context. Articles, captured learnings, ontology neighbors, and confirmed outputs can shape an LLM answer or an agent's plan, but the reviewed read path does not enforce actions. Trust mode controls whether outputs are eligible for search, which is a ranking/indexing authority boundary rather than a hard runtime gate on agent behavior.

## Curiosity Pass

**The system is more governed than a plain RAG wiki.** Output trust, source-change demotion, compile tiers, broken-link stripping, concept dedup, and generated skills form a real operational layer around the generated wiki.

**The read-capture-evolve loop depends on instruction following.** The memory layer can capture and serve knowledge, but proactive use is bootstrapped by skill text. That is a practical adoption mechanism, not code-level automatic context insertion.

**SQLite is doing several jobs at once.** It is FTS store, vector store, graph store, compile-state store, trust ledger, and learning table. This keeps deployment simple, but makes table semantics more important than the single "SQLite" storage label suggests.

**The latest link stripping patch is deliberately humble.** Removing brackets around missing targets improves navigation quality without pretending to validate the article's claims or relation semantics.

**Trust promotion is stronger than concept compilation.** Generated Q&A outputs have an explicit pending/confirmed/conflict/stale lifecycle; compiled articles have quality scores and linting, but not the same consensus/grounding state machine.

## What to Watch

- Whether generated skill instructions become host hooks or remain advisory text. That determines whether future versions stay pull-only or gain unsolicited memory loading.
- Whether session scribe starts writing source files as well as ontology entities. That would make trace-derived artifacts easier to audit, recompile, and invalidate.
- Whether article compilation gains a trust state comparable to Q&A outputs. Without that, compiled concept pages and generated answers have different evidence governance.
- Whether tier auto-demotion deletes, de-indexes, or only changes future compile policy. The current review treats it as lower-tier handling, not forgetting.
- Whether the graph/search pipeline gets behavioral ablations showing that graph expansion, reranking, or trust gating changes downstream agent outcomes.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: sage-wiki turns conversation captures and session logs into durable source files, learnings, and ontology rows.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: sage-wiki stores and indexes memory, but agents receive it only through explicit search/query/read paths or by following generated instructions.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: sage-wiki requires separating Markdown articles, SQLite tables, embeddings, ontology edges, trust records, generated skills, and MCP tools by substrate/form/lineage/authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: compiled articles, captures, learnings, ontology entities, and confirmed outputs mostly advise as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: skill templates, MCP tool schemas, compile tiers, trust policy, lint checks, and query ranking code constrain future behavior.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: capture and scribe extract reusable project memory from agent conversation traces.
