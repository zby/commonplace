---
description: "MemPalace review: local-first verbatim drawers, closet ranking, SQLite temporal KG, MCP/CLI/plugin surfaces, hooks, and trace-derived capture"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
status: current
last-checked: "2026-06-02"
---

# MemPalace

MemPalace, by `milla-jovovich`, is a local-first Python memory system for coding agents and terminal AI tools. At the reviewed commit it stores verbatim project files, conversations, diaries, and manual memories as searchable "drawers" in a ChromaDB-backed palace; adds "closets", hallways, tunnels, a SQLite temporal knowledge graph, and optional fact checks around that corpus; and exposes the system through a CLI, MCP server, Claude/Codex plugins, hooks, website docs, tests, and benchmark scripts.

**Repository:** https://github.com/milla-jovovich/mempalace

**Reviewed commit:** [db1fbe888b59514a66c43e745f095d762b9bf276](https://github.com/milla-jovovich/mempalace/commit/db1fbe888b59514a66c43e745f095d762b9bf276)

**Last checked:** 2026-06-02

## Core Ideas

**The canonical memory is verbatim text, not an extracted summary.** The README's central claim is that MemPalace stores conversation history "as verbatim text" and "does not summarize, extract, or paraphrase"; the implementation follows that default for project mining and conversation mining by chunking text and upserting the original chunk content as drawer documents ([README.md](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/README.md), [miner.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/miner.py), [convo_miner.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/convo_miner.py)). This makes the raw source chunk the primary retained knowledge artifact; extraction and routing metadata sit beside it rather than replacing it.

**Drawers are the storage unit; closets are a retrieval signal.** The package uses a configurable collection for drawers and a separate `mempalace_closets` collection for compact topic/entity pointer lines ([palace.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/palace.py)). Search always queries drawers directly, then queries closets and uses the closet hit as a bounded rank boost, explicitly treating closets as a signal and not a gate ([searcher.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/searcher.py)). That is the most important context-efficiency choice: compact metadata can improve ranking and source hydration, but it is not allowed to hide verbatim evidence that direct drawer search would have found.

**The palace is local-first but not filesystem-first.** The default storage backend is ChromaDB, hidden behind a backend contract with typed query/get results and a registered `chroma` entry point ([base.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/backends/base.py), [chroma.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/backends/chroma.py), [pyproject.toml](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/pyproject.toml)). User-visible concepts borrow a spatial metaphor, but rollback, diff, and inspection mostly operate through Chroma/SQLite APIs rather than plain Markdown files.

**There is a second, structured memory plane.** `knowledge_graph.py` implements a local SQLite temporal entity-relationship graph with entities, triples, validity windows, confidence, source closet/file/drawer metadata, and invalidation ([knowledge_graph.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/knowledge_graph.py)). The MCP server exposes KG add/query/invalidate/timeline/stats tools, while `fact_checker.py` uses the entity registry and KG to flag similar names, relationship mismatches, and stale facts in candidate text ([mcp_server.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/mcp_server.py), [fact_checker.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/fact_checker.py)). This gives some facts stronger symbolic shape than raw drawers, but KG facts are still manually or adapter supplied in the checked code, not automatically promoted from every drawer.

**Agent integration is broad and practical.** The CLI routes init, mining, search, wake-up, MCP setup, sync, repair, hooks, and benchmark-oriented workflows ([cli.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/cli.py)). The MCP server exposes read, write, drawer, graph, KG, diary, hook-settings, and reconnect tools; plugins package guided commands/skills and hooks for Claude Code and Codex ([mcp_server.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/mcp_server.py), [.claude-plugin](https://github.com/milla-jovovich/mempalace/tree/db1fbe888b59514a66c43e745f095d762b9bf276/.claude-plugin), [.codex-plugin](https://github.com/milla-jovovich/mempalace/tree/db1fbe888b59514a66c43e745f095d762b9bf276/.codex-plugin), [integrations/openclaw](https://github.com/milla-jovovich/mempalace/tree/db1fbe888b59514a66c43e745f095d762b9bf276/integrations/openclaw)). Adoption work is a first-class part of the system, not just packaging around a library.

**Context efficiency is layered, budgeted, and mostly pull-driven.** `layers.py` describes L0 identity, L1 essential story, L2 filtered retrieval, and L3 deep search, with explicit token estimates and hard character caps for wake-up context ([layers.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/layers.py)). Search uses top-k limits, wing/room filters, distance thresholds, BM25 hybrid reranking, optional candidate union, closet boosts, and capped neighbor hydration ([searcher.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/searcher.py)). The complexity cost is that agents must understand multiple surfaces: drawers, closets, wings, rooms, halls, hallways, tunnels, KG facts, diaries, AAAK, and wake-up layers.

## Artifact analysis

- **Storage substrate:** `vector` — ChromaDB persistent collections under the configured palace path, accessed through the backend contract
- **Representational form:** `prose` `symbolic` `parametric` — verbatim prose/source text, symbolic metadata/KG/navigation records/tool schemas, and Chroma embedding-backed retrieval
- **Lineage:** `authored` `imported` `trace-extracted` — authored manual memories, KG calls, tools, hooks, plugins, docs, and tests; imported project files and diaries; trace-extracted transcripts and hook-captured conversations
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — drawers and KG facts advise; plugins/docs instruct; hooks can block for save pressure; metadata and graph surfaces route and rank; fact checks/tests validate; mining derives durable memory artifacts

**Drawer documents.** Storage substrate: ChromaDB persistent collections under the configured palace path, accessed through the backend contract. Representational form: mixed prose/source text plus symbolic metadata such as wing, room, source file, chunk index, extraction mode, entities, and timestamps. Lineage: imported or trace-captured from project files, transcripts, daily diaries, manual MCP writes, or hooks; source changes invalidate by file hash/metadata, re-mine rules, or manual update/delete. Behavioral authority: knowledge artifacts when retrieved as evidence, context, or advice; they do not enforce behavior unless a host agent obeys the returned text.

**Closets, hallways, tunnels, and palace graph records.** Storage substrate: a separate ChromaDB closet collection plus JSON files under `~/.mempalace` for hallway/tunnel-like navigation records. Representational form: symbolic pointer lines and graph records with embedded prose previews and entity/topic labels. Lineage: derived from drawer content, metadata, co-occurrence counts, or explicit MCP/tool writes; stale drawers or changed entity extraction require rebuild or cache invalidation. Behavioral authority: ranking, routing, and navigation system-definition artifacts. They influence which drawers are found or followed, but search code keeps drawers as the floor rather than letting closets become a hard gate.

**SQLite knowledge graph.** Storage substrate: local SQLite, either the default `~/.mempalace/knowledge_graph.sqlite3` or a palace-local KG when the MCP server is pointed at a palace. Representational form: symbolic entities and triples with temporal text fields, confidence, source pointers, and adapter metadata. Lineage: authored through library/MCP calls or supplied by adapters; `valid_to` invalidation changes currentness without deleting older facts. Behavioral authority: knowledge artifacts when queried as facts; temporal filters, stale/current flags, and fact-check comparisons have validation/audit authority for later text.

**MCP tools, CLI commands, hooks, plugins, and skills.** Storage substrate: repository Python modules, shell scripts, plugin manifests, skill Markdown, and generated hook configuration. Representational form: mixed symbolic schemas/scripts and prose instructions. Lineage: authored system-definition artifacts. Behavioral authority: instruction, routing, write policy, validation, and integration authority. The Stop and PreCompact hooks can force a write-back checkpoint, but they are capture/save mechanisms, not relevance-gated read-back.

**Benchmarks, tests, website, and docs.** Storage substrate: repository files under `tests/`, `benchmarks/`, `website/`, and `docs/` ([tests](https://github.com/milla-jovovich/mempalace/tree/db1fbe888b59514a66c43e745f095d762b9bf276/tests), [benchmarks](https://github.com/milla-jovovich/mempalace/tree/db1fbe888b59514a66c43e745f095d762b9bf276/benchmarks), [website](https://github.com/milla-jovovich/mempalace/tree/db1fbe888b59514a66c43e745f095d762b9bf276/website)). Representational form: tests and scripts are symbolic; docs and benchmark explanations are prose; result files are structured evidence. Lineage: authored or experimentally generated. Behavioral authority: tests and benchmarks evaluate implementation claims; docs instruct users and host agents but are only active when installed or read.

The promotion path is partial. Raw traces and files can become drawers; drawers can produce closet pointers, hallway/tunnel records, KG facts, diary entries, and benchmark evidence; but the repository does not implement a governed path from retrieved evidence into reviewed instructions or validators. That final authority promotion remains a human or host-agent responsibility.

## Comparison with Our System

| Dimension | MemPalace | Commonplace |
|---|---|---|
| Primary purpose | Local agent memory and retrieval over user/project/conversation corpora | Git-native methodology KB for agent operation |
| Canonical artifact | Verbatim drawers in ChromaDB plus metadata | Typed Markdown notes, instructions, ADRs, reviews, indexes |
| Structured layer | SQLite temporal KG, closets, graph navigation records | Frontmatter, schemas, authored links, generated indexes, validation reports |
| Context path | CLI/MCP search, wake-up layers, explicit KG/diary/drawer tools | `rg`, indexes, collection contracts, skills, validators, review bundles |
| Learning source | Project files, transcripts, hooks, diaries, manual writes | Authored artifacts, source snapshots, reviews, validation/review outputs |
| Governance | Tool schemas, tests, fact checks, repair/sync commands | Type specs, collection contracts, validation, review gates, git history |

MemPalace is stronger than Commonplace as a local user/project memory substrate. It ingests large heterogeneous corpora, embeds them, exposes high-coverage search, and integrates with live agent harnesses. Commonplace is stronger as a governed knowledge system: its retained artifacts are ordinary repository files with type contracts, explicit links, validation, review workflows, and source-citation expectations.

The main divergence is the source-of-truth layer. MemPalace keeps source words in a vector database and makes retrievability the central promise. Commonplace keeps durable knowledge in authored Markdown, and uses generated artifacts as support rather than canonical meaning. MemPalace's verbatim stance is a useful antidote to lossy memory extraction, but Chroma/SQLite storage makes review and diff weaker than a file-native KB.

The second divergence is activation. MemPalace has hooks that push write-back obligations into an agent's workflow and can auto-mine transcripts in the background ([hooks README](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/hooks/README.md), [hooks_cli.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/hooks_cli.py)). Read-back is still explicit: wake-up, status, search, KG query, diary read, drawer fetch, graph traversal. I did not find an implemented matcher that observes the next task and injects relevant memories before action.

**Read-back:** `pull` — Agents or users deliberately call wake-up/search/status/KG/diary/drawer tools; hooks push capture and save checkpoints, not relevance-gated retrieved memory

### Borrowable Ideas

**Treat verbatim trace retention as the default baseline.** Ready to borrow for trace-heavy Commonplace workflows. Before distilling a transcript into a note, preserve the raw source or source snapshot so extraction errors are recoverable.

**Use derived indexes as boosts, not gates.** Ready now. MemPalace's closet-as-ranking-signal pattern maps well to Commonplace search: generated semantic or entity indexes should help rank candidates without suppressing direct lexical/source matches.

**Add bounded neighbor hydration to search results.** Ready with a concrete CLI need. Returning a matched chunk plus nearby source context is a practical answer to chunk-boundary failures, and could improve source snapshot and review-report exploration.

**Borrow temporal invalidation for personal facts, not methodology claims wholesale.** Needs a use case. `valid_from` / `valid_to` is valuable for user/project facts and evolving environment state; Commonplace methodology notes usually need status/replacement/revision history rather than KG-style currentness.

**Keep hook-driven save pressure separate from read-back authority.** Ready as a design caution. Hooks can protect against context loss, but they should not be treated as proof that memory is being used unless there is a separate read-back and faithfulness mechanism.

**Do not borrow database opacity as the primary KB substrate.** MemPalace's Chroma/SQLite design is reasonable for high-volume personal memory. For Commonplace's methodology KB, plain files, git diffs, type specs, and validation remain better governance surfaces.

## Write-side placement

**Write agency:** `automatic` `manual` — the review identifies a trace-derived or rule-driven path that changes retained memory from execution/session evidence; manual surfaces are included where the reviewed prose describes user or operator authoring.

**Curation operations:** `consolidate` `evolve` `synthesize` `invalidate` `decay` `promote` — the existing review evidence identifies automatic store-changing operations matching these curation classes.

### Trace-derived learning
- **Trace source:** `session-logs` `event-streams` — Claude Code, Codex, ChatGPT, Slack/plain-text conversations, hook-provided transcript paths, and hook event counts/transcript mining
- **Learning scope:** `per-project` `cross-task` — palace path, wing, room, source file, collection, and hook transcript paths scope local project/user memory across later tasks
- **Learning timing:** `online` `offline` `staged` — MCP/manual writes and hooks can capture during use; mining, sweeps, and benchmarks run batch/offline; pre-compaction and periodic hooks stage capture around workflow boundaries
- **Distilled form:** `prose` `symbolic` `parametric` — retained verbatim text, symbolic metadata/navigation/KG surfaces, and embedding-backed retrieval indexes

**Trace source.** MemPalace qualifies as trace-derived because the implemented system can ingest Claude Code, Codex, ChatGPT, Slack/plain-text conversations, hook-provided transcript paths, daily diary files, and project corpora into durable memory artifacts. The hook scripts and `hooks_cli.py` count session messages, mine transcripts, and sometimes block the agent with a save instruction before stop or compaction ([hooks README](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/hooks/README.md), [hooks_cli.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/hooks_cli.py)).

**Extraction.** The first stage is mostly raw capture: transcripts are normalized and chunked; project files are scanned and chunked; diaries are split by entries; manual MCP writes add drawers or diary entries. The second stage derives metadata and navigation surfaces: room/hall assignment, entities, closet pointer lines, hallway co-occurrences, palace graph/tunnels, optional general memory-type extraction, and manually supplied KG triples ([convo_miner.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/convo_miner.py), [diary_ingest.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/diary_ingest.py), [general_extractor.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/general_extractor.py), [hallways.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/hallways.py)).

**Four fields.** The raw stage is ChromaDB drawer storage: prose/source text plus symbolic metadata, lineage from transcript/project/diary/manual source, and knowledge-artifact authority. The derived stage is closets, graph records, KG facts, entity metadata, and benchmark/test outputs: mixed symbolic/prose/distributed-parametric representation, lineage from drawers or authored tool calls, and ranking/routing/validation/evaluation authority where consumed by search, graph traversal, KG queries, or tests.

**Scope and timing.** Scope is local and usually per-user or per-project, controlled by palace path, wing, room, source file, collection name, and hook transcript path. Timing is online for MCP/manual writes, periodic or pre-compaction for hooks, batch/offline for mining and sweeps, and post-hoc for benchmark scripts.

**Survey placement.** MemPalace belongs in the trace-to-verbatim-memory and trace-to-retrieval-index branch. It strengthens the claim that raw trace retention plus strong retrieval is a serious baseline. It does not strengthen claims about automatic high-authority rule learning: the code captures, indexes, ranks, and audits, but it does not turn traces into reviewed agent instructions without a host or human promotion step.

## Curiosity Pass

**The name metaphor is doing product work, but the implementation is conventional RAG plus local tools.** Wings, rooms, drawers, closets, halls, hallways, and tunnels make the system memorable, yet the load-bearing implementation is ChromaDB retrieval, metadata filters, SQLite facts, scripts, and MCP tools.

**The README's "no extraction" claim needs a narrow reading.** The central memory document is verbatim, but the system does extract entities, topics, hallway co-occurrences, memory types, KG triples through tool/API calls, and benchmark-oriented derived signals. The important distinction is not "no extraction"; it is "do not replace the source text with extraction."

**Hook-driven capture can look like push activation from a distance.** The hooks push save pressure and background mining into the agent loop. That is different from pushing relevant remembered content into the next decision. This distinction matters because capture volume alone does not prove memory use.

**Fact checking is narrower than the memory surface.** `fact_checker.py` checks name confusion, simple relationship mismatches, and stale KG facts. It is useful as an audit surface, but it does not validate arbitrary retrieved drawer claims.

**The benchmark material is unusually prominent.** The repository includes result files and benchmark scripts, and the public README is careful to separate retrieval recall from end-to-end QA. That is good evidence discipline, though the review still treats benchmark claims as project-provided evidence rather than independent replication.

## What to Watch

- Whether the backend abstraction grows a non-Chroma implementation with comparable search and maintenance behavior.
- Whether hooks or plugins add a real before-action read-back hook that searches by task context and injects selected memories with a budget.
- Whether KG triples gain automatic extraction from drawers with source spans, prompt/model provenance, confidence calibration, and review state.
- Whether closet, hallway, and tunnel rebuild/invalidation becomes as inspectable as the raw drawer source.
- Whether benchmark scripts publish complete source-to-result manifests for every headline score, including embedding model, split, tuning history, and reranker configuration.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: MemPalace derives durable drawers, closets, navigation records, and optional KG/fact-check surfaces from transcripts and other captured traces.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: MemPalace stores and searches a rich memory corpus, but implemented read-back is pull unless a host calls the tools.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: MemPalace requires separating raw drawers, closet indexes, graph records, KG facts, hooks, plugins, and benchmarks by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: drawers, diary entries, returned search hits, and KG query results mostly advise future behavior as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: tool schemas, hooks, plugin manifests, search/ranking code, fact-check rules, and benchmark/test scripts constrain, route, validate, or evaluate behavior.
- [Automating KB learning is an open problem](../../notes/automating-kb-learning-is-an-open-problem.md) - contrasts: MemPalace shows strong automatic capture and retrieval, not automatic promotion into governed Commonplace-style methodology artifacts.
