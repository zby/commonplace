---
description: "Generated comparison table for code-reviewed agent memory systems: one-line summaries plus storage, read-back, targeting, trace-learning, and enforcement."
type: kb/types/note.md
traits: [has-comparison]
tags: [agent-memory]
---

# Agent memory systems comparison table

A scannable view of the code-reviewed systems in this collection, generated from
[`systems.csv`](./systems.csv). Lightweight (doc-only) reviews are excluded — a
comparison table is for *choosing* a system, and that calls for code-grounded
evidence. Click any column header to sort (in the rendered HTML site; on GitHub
the [raw matrix](./systems.csv) is itself a sortable, searchable viewer).

This is the human view: one decision per cell. The raw [`systems.csv`](./systems.csv)
keeps the full one-hot flag sets (every authority mode, every curation operation,
every read-back signal); here each collapses to its single discriminating value,
and a plain-English description leads.

For the findings across the whole population, see the
[comparison](./agentic-memory-systems-comparative-review.md).

## How to read the columns

- **What it is** — a one-line description of the system, lifted from its review.
  Scan this first; the rest of the row tells you *how* it works.
- **Storage** — where memory physically lives: plain `files`, a git `repo`,
  `sqlite`, an `rdbms`, a `vector` or `graph` store, `kv`, `in-memory`, or
  `model-weights`. It sets the operational floor — inspectability and diffability
  at one end, scale and query power at the other. Files-family still leads, but
  roughly a third are database-backed, and the most common database is plain
  SQLite, not a vector or graph store.
- **Read-back** — how remembered material reaches the next action: the agent
  *pulls* it with an explicit lookup, the system *pushes* it in unasked, or
  *both*. The first question to ask, because it decides whether the agent has to
  remember to look or whether context arrives on its own.
- **Targeting** — for systems that push, *how* the push selects what to inject:
  `coarse` (always-load / session-start, generic recall) versus `targeted` (the
  push selects for *this* instance — an identifier match, or relevance inferred
  from content by keyword, embedding, or LLM judgment). Pull-only systems push
  nothing (`—`). The raw signal one-hots behind this live in the matrix.
- **Learns from traces** — whether memory is mined automatically from the agent's
  own execution traces rather than authored by hand. It trades throughput for
  reviewability. Most systems do — and they overwhelmingly push or do both, so
  automatic learning and automatic activation tend to ship together.
- **Enforces** — whether the stored memory ever acts as a **hard gate** (a check
  the agent can't bypass — a validation that must pass, a blocking rule, a
  required proof) rather than advisory context it can override. This is the
  *enforcement* mode of behavioral authority — nothing to do with authentication.
  The other authority modes (instruction, routing, validation, ranking, learning)
  are near-universal and so don't discriminate; they stay in the matrix.

Curation operations and the full authority and signal flag sets are dropped from
this compact view; they live in [`systems.csv`](./systems.csv).


## The systems (148 code-reviewed)

| System | What it is | Storage | Read-back | Targeting | Learns from traces | Enforces |
|---|---|---|---|---|---|---|
| [A-mem](./reviews/a-mem.md) | Python memory library with MemoryNote objects, Chroma retrieval, LLM metadata generation, and automatic neighbor evolution | in-memory | pull | — | no | — |
| [ACE](./reviews/ace.md) | trace-learning playbook evolution, reflector-scored bullets, curator additions, optional deduplication, and coarse prompt read-back | files | push | coarse | yes | — |
| [Agent Skills for Context Engineering](./reviews/agent-skills-for-context-engineering.md) | authored context-engineering skills plus a file-based researcher OS and trace-to-skill example tooling | files | pull | — | yes | — |
| [Agent Workflow Memory](./reviews/agent-workflow-memory.md) | web-agent workflow files induced from successful traces and pushed into WebArena/Mind2Web prompts | files | push | targeted | yes | — |
| [Agent-R](./reviews/agent-r.md) | MCTS trace collection, revision-trajectory synthesis, checkpoint-level read-back, and no runtime retrieval store | model-weights | push | coarse | yes | — |
| [Agent-S](./reviews/Agent-S.md) | GUI agent framework with S1/S2 JSON experience memory, embedding retrieval, S3 reflection, and BBON trace evaluation | files | both | targeted | yes | — |
| [AgentFly](./reviews/AgentFly.md) | planner-executor agent with JSONL case-bank memory, trace-judged case writes, and parametric or SimCSE case read-back | files | push | targeted | yes | — |
| [Agentic Harness Engineering](./reviews/agentic-harness-engineering.md) | trace-driven outer loop that distills coding-agent rollouts into debugger reports and durable harness edits | files | both | targeted | yes | yes |
| [Agentic Local Brain](./reviews/agentic-local-brain.md) | local PKM capture into Markdown, SQLite, Chroma vectors, mining tables, RAG chat traces, and recommendation ranking | sqlite | both | targeted | yes | — |
| [AI-Context-OS](./reviews/AI-Context-OS.md) | filesystem-first Markdown memory with L0/L1/L2 context loading, generated adapters, MCP/chat read-back, and trace-learning optimization suggestions | files | both | targeted | yes | — |
| [ai-memex-cli](./reviews/ai-memex-cli.md) | Git-backed Markdown vault, agent skill workflows, trace distillation, lint/watch loops, and context bootstrap | files | both | coarse | yes | — |
| [ai-modules](./reviews/theafh--ai-modules.md) | deployable multi-vendor skill/plugin bundle with Markdown wiki, session wrapup, task backlog, and linted file memory | files | pull | — | yes | yes |
| [Amazon Science SAGE](./reviews/amazon-science--SAGE.md) | AppWorld rollouts become reusable Python skills, retrieval state, SFT data, and GRPO reward signal | files | push | targeted | yes | yes |
| [Archie](./reviews/archie.md) | Git-native Arch Linux desktop configuration with Stow deployment, agent briefs, ADRs, and pull-only repo read-back | repo | pull | — | no | yes |
| [AriGraph](./reviews/AriGraph.md) | in-run knowledge-graph world model with episodic observation memory, Contriever retrieval, LLM extraction/refinement, and prompt pushback | in-memory | both | targeted | yes | — |
| [Ars Contexta](./reviews/arscontexta.md) | Claude Code plugin deriving file-based agent knowledge systems with generated context, skills, hooks, trace mining, and coarse push read-back | files | both | coarse | yes | yes |
| [ATLAS](./reviews/atlas.md) | logistics MCP server whose KnowledgeEngine enriches on-disk markdown files from document extractions, never overwriting — read-back only via its internal chat agent, not MCP | files | both | coarse | no | — |
| [Atomic](./reviews/atomic.md) | SQLite-backed markdown atoms with embeddings, semantic graph, wiki/report synthesis, chat, and MCP memory tools | sqlite | both | targeted | no | — |
| [Auto-claude-code-research-in-sleep](./reviews/Auto-claude-code-research-in-sleep.md) | Markdown skill harness for autonomous research with project research-wiki memory, review traces, and gated trace-learning skill optimization | files | both | coarse | yes | yes |
| [auto-harness](./reviews/auto-harness.md) | benchmark-driven coding-agent loop that mines train traces, evolves agent.py, promotes evals, and gates changes | files | both | targeted | yes | yes |
| [Autocontext](./reviews/autocontext.md) | iterative evaluation harness with trace-learning playbooks, hints, skills, tools, validators, runtime traces, and optional model distillation | files | both | targeted | yes | yes |
| [AutoSci](./reviews/AutoSci.md) | AutoSci review scoped to its OmegaWiki/SciMem subsystem: file-backed research wiki, schema/runtime contracts, skills, tools, graph, and bounded context packs | files | both | targeted | no | yes |
| [Awesome Agent Memory](./reviews/Awesome-Agent-Memory.md) | GitHub README landscape index for agent-memory products, papers, benchmarks, tutorials, articles, and workshops | repo | pull | — | no | — |
| [Basic Memory](./reviews/basic-memory.md) | local-first Markdown knowledge graph with SQLite/Postgres indexes, MCP pull tools, semantic search, schemas, and Claude hook read-back | files | both | targeted | yes | — |
| [Beever Atlas](./reviews/beever-atlas.md) | chat-ingestion knowledge base with Weaviate facts, Neo4j graph memory, MongoDB wiki pages, MCP retrieval, and trace-learning wiki synthesis | vector | pull | — | yes | — |
| [Binder](./reviews/binder.md) | local-first typed SQLite graph with Markdown sync, transaction history, CLI/MCP access, LSP validation, and explicit agent reads | sqlite | pull | — | no | yes |
| [browzy.ai](./reviews/browzy-ai.md) | terminal personal KB with Markdown/wiki files, SQLite FTS, LLM compilation, query-time context assembly, and trace-learning digests | files | push | targeted | yes | — |
| [byterover-cli](./reviews/byterover-cli.md) | local context-tree memory with HTML topic curation, BM25/runtime-signal retrieval, MCP hooks, review logs, dream pruning, and ByteRover cloud sync | files | both | coarse | yes | — |
| [cass_memory_system](./reviews/cass_memory_system.md) | file-backed procedural memory for coding agents with cass session search, diary summaries, LLM reflection, scored playbook rules, MCP tools, and trauma guards | files | both | targeted | yes | yes |
| [Claude Context Guard](./reviews/claude-context-guard.md) | Claude Code slash-command memory using project safeguard files, audits, pagination, hooks, and itemised code indexes | files | both | targeted | yes | — |
| [Claude Workstream Kit](./reviews/claude-workstream-kit.md) | repo-local active-work memory for Claude Code with ACTIVE.md resume, workstream closure, gates, and verifier agents | files | both | targeted | yes | — |
| [claude-obsidian](./reviews/claude-obsidian.md) | Obsidian vault memory with agent skills, hot cache, wiki ingestion, hybrid retrieval, locking, hooks, and methodology modes | files | both | coarse | yes | yes |
| [ClawVault](./reviews/clawvault.md) | deprecated markdown vault memory with graph/search context, OpenClaw prompt hooks, observer compression, facts, and maintenance workers | files | both | targeted | yes | yes |
| [Closure-SDK](./reviews/Closure-SDK.md) | geometric verification, Closure DNA database state, and experimental carrier-genome memory without agent prompt activation | files | pull | — | no | yes |
| [Clude](./reviews/cludebot.md) | cognitive memory SDK and MCP server with SQLite/Supabase stores, hybrid recall, dream-cycle synthesis, memory packs, and prompt-file push surfaces | sqlite | both | targeted | yes | yes |
| [CocoIndex](./reviews/cocoindex.md) | incremental AI data-pipeline framework that maintains fresh vector, graph, file, and database indexes for downstream agent retrieval | files | pull | — | no | — |
| [Cognee](./reviews/cognee.md) | graph/vector agent memory control plane with session cache, recall routing, trace-learning improve loops, MCP tools, and decorator push | graph | both | targeted | yes | — |
| [Compound Engineering Plugin](./reviews/compound-engineering-plugin.md) | repo-file workflow memory with generated strategy, brainstorm, plan, solution, pulse, session-history, and review artifacts | repo | both | targeted | yes | yes |
| [Context Constitution](./reviews/context-constitution.md) | authored Letta context doctrine with MemFS, prompt learning, compaction, reflection affordances, and no local harness implementation | files | pull | — | no | — |
| [Continuity](./reviews/continuity.md) | local-first desktop AI workspace with shared SQLite memory, MCP tools, narrative synthesis, prompt push, and org sync | sqlite | both | coarse | yes | — |
| [CORAL](./reviews/CORAL.md) | filesystem multi-agent coding hub with shared notes, skills, attempts, roles, eval feedback, heartbeat prompts, and worktree isolation | files | both | targeted | yes | yes |
| [Cortex](./reviews/cortex.md) | local RDF/SQLite cognitive knowledge service with ontology, hybrid retrieval, MCP tools, reasoning, and access-derived tier learning | graph | pull | — | yes | yes |
| [cq](./reviews/cq.md) | Mozilla AI plugin and MCP store for structured agent knowledge units, review-gated sharing, and agent-led reflection | sqlite | pull | — | yes | yes |
| [CrewAI Memory](./reviews/crewai-memory.md) | unified vector memory with LLM extraction, scoped recall, task/HITL learning, tools, and pre-task prompt injection | vector | both | targeted | yes | yes |
| [Decapod](./reviews/decapod.md) | Rust repo-native governance kernel with SQLite stores, context capsules, trace lessons, proof gates, and pull-first memory reads | files | pull | — | yes | yes |
| [deja-vu](./reviews/deja-vu.md) | local lexical memory over Claude, Codex, and opencode traces with redacted file index, MCP recall, sync/share, and SessionStart auto-recall | files | both | targeted | yes | — |
| [dense-mem](./reviews/dense-mem.md) | self-hosted MCP memory server with Neo4j evidence, typed claims, verifier gates, fact promotion, and tiered recall | graph | pull | — | yes | yes |
| [DocMason](./reviews/docmason.md) | repo-native private-document KB with provenance, governed ask, deterministic retrieval, and interaction-memory promotion | files | both | targeted | yes | yes |
| [Dynamic Cheatsheet](./reviews/dynamic-cheatsheet.md) | trace-learning test-time prompt memory with LLM cheatsheet curation, embedding retrieval, and automatic solver read-back | in-memory | push | targeted | yes | — |
| [Echel](./reviews/echel.md) | project-owned Markdown product memory, deterministic graph/report generation, evidence gates, and task-scoped agent packets | files | both | targeted | no | yes |
| [EchoesVault / echoes-vault-opencode](./reviews/echoes-vault-opencode.md) | OpenCode plugin that bootstraps a Markdown/Obsidian vault, slash-command read-back, and agent-mediated trace capture | files | both | coarse | yes | — |
| [EchoWiki](./reviews/echowiki.md) | Obsidian plugin and CLI that compile raw notes and voice transcripts into file-backed wiki pages via the Vercel AI SDK | files | both | targeted | no | yes |
| [Eidetic](./reviews/eidetic.md) | Claude Code Markdown memory with hook-pushed context, FTS/vector recall, trace capture, compounding, drift penalties, and vault export | files | both | targeted | yes | — |
| [Engraph](./reviews/engraph.md) | local Obsidian-vault gateway with hybrid search, MCP/HTTP tools, identity context, and folder-feedback learning | files | pull | — | no | yes |
| [EQUIPA](./reviews/equipa.md) | SQLite-backed agent orchestrator with trace-learning lessons, episodes, prompt variants, and prompt-time read-back | sqlite | both | targeted | yes | — |
| [Exocomp](./reviews/exocomp.md) | Go multi-agent coding workbench with YAML roles, .exocomp ledgers, sandboxed tools, skills, and recovery | files | both | coarse | no | yes |
| [ExpeL](./reviews/expel.md) | trace-learning benchmark agent that distills task trajectories into rules and retrieves prior trials as few-shots | files | both | targeted | yes | — |
| [Funes](./reviews/funes.md) | Git-native Librarian protocol for raw-source preservation, compiled Markdown wiki memory, outputs, and health-check governance | repo | pull | — | no | — |
| [G-Memory](./reviews/g-memory.md) | trace-learning multi-agent memory with Chroma task storage, NetworkX task graph, JSON insights, and orchestrator-pushed examples/rules | vector | push | targeted | yes | — |
| [GBrain](./reviews/gbrain.md) | Postgres/PGLite-backed agent brain with markdown write-through, hybrid retrieval, graph links, hot facts, skills, and dream-cycle maintenance | rdbms | both | targeted | yes | yes |
| [getsentry/skills](./reviews/getsentry-skills.md) | Sentry's repo-backed skill and subagent marketplace with authored prompts, routed references, scripts, and validation rules | repo | pull | — | no | yes |
| [Gnosis](./reviews/gnosis.md) | repo-local why-memory CLI with JSONL entries, disposable SQLite FTS search, doctrine-guided capture, and pull-only read-back | files | pull | — | no | — |
| [Graphiti](./reviews/graphiti.md) | temporal graph memory with episode provenance, LLM extraction, fact invalidation, hybrid retrieval, MCP tools, and pull-only activation | graph | pull | — | yes | — |
| [HALO](./reviews/halo.md) | trace-learning agent-harness optimizer with SQLite desktop trace store, JSONL trace indexes, recursive trace agents, and local analysis runs | sqlite | pull | — | yes | — |
| [Hindsight](./reviews/hindsight.md) | service-backed agent memory with LLM fact extraction, observations, hybrid recall, integrations, hooks, transfer, and trace-learning | rdbms | both | targeted | yes | — |
| [HippoRAG](./reviews/HippoRAG.md) | document-ingest memory framework using OpenIE triples, parquet embedding stores, igraph PageRank retrieval, and RAG QA | files | pull | — | no | — |
| [hyalo](./reviews/hyalo.md) | Rust CLI for structured Markdown vault search, mutation, linting, snapshot indexes, and Claude skill/rule integration | files | pull | — | no | yes |
| [HyperAgents](./reviews/hyperagents.md) | self-improving agent harness where trace-learning benchmark feedback promotes executable patch lineages | files | push | targeted | yes | yes |
| [interview-doc-agent](./reviews/interview-doc-agent.md) | single-file job-document skill using a file-native experience library, templates, and index-guided context | files | pull | — | no | — |
| [KBLaM](./reviews/KBLaM.md) | model-integrated key/value knowledge injection with trained encoders, modified attention, and KB-conditioned generation | files | push | targeted | no | — |
| [Kompl](./reviews/Kompl.md) | SQLite-backed knowledge compiler that ingests sources into a generated wiki with provenance, FTS/vector retrieval, MCP tools, and chat-derived drafts | sqlite | both | targeted | yes | yes |
| [LACP](./reviews/lacp.md) | local control-plane agent harness with trace-learning Obsidian/SMS memory, hook-time context injection, RAG pull, and policy gates | files | both | targeted | yes | yes |
| [Letta](./reviews/letta.md) | stateful agent server with core memory blocks, archival and recall tools, compaction, sleeptime memory agents, and optional git-backed memory | rdbms | both | targeted | yes | yes |
| [Link](./reviews/link.md) | local Markdown wiki memory with raw captures, reviewed memory pages, bounded query packets, MCP/CLI skills, validation, and local viewer | files | both | targeted | yes | — |
| [LLM Wiki (cobusgreyling)](./reviews/cobusgreyling--llm-wiki.md) | file-backed agent-maintained markdown wiki with scaffolded instructions, BM25/qmd search, linting, and pull-only read-back | files | pull | — | no | — |
| [LLM Wiki (kenhuangus)](./reviews/kenhuangus--llm-wiki.md) | local-first Obsidian/wiki compiler with source monitors, LLM extraction and integration, BM25 search, autonomous maintenance loops, and weak trace-learning prompt-optimization scaffolding | repo | both | targeted | yes | yes |
| [LLM Wiki (MehmetGoekce)](./reviews/MehmetGoekce--llm-wiki.md) | Claude Code command package for a Logseq/Obsidian wiki with L1 auto-loaded memory, L2 pull queries, schema rules, and lint gates | files | both | coarse | no | yes |
| [LLM Wiki (nvk)](./reviews/llm-wiki.md) | portable agent plugin that compiles source files into topic wikis, queryable through index-guided reads, audits, linting, and session lessons | files | both | targeted | yes | yes |
| [llm-context-base](./reviews/llm-context-base.md) | markdown-only LLM wiki template with metadata routing, training-period write-back, lint protocols, and multi-agent shims | repo | both | coarse | no | yes |
| [llm-project-wiki](./reviews/llm-project-wiki.md) | prompt-only Claude Code workflow that bootstraps an Obsidian project wiki, wiki-first rules, diff ingest, and gap audits | files | pull | — | yes | yes |
| [llm-wiki (Pratiyush)](./reviews/Pratiyush--llm-wiki.md) | local file-based transcript-to-wiki compiler with raw session capture, agent-authored wiki pages, static AI exports, MCP tools, and optional synthesis | files | pull | — | yes | yes |
| [llm-wiki-coordination](./reviews/llm-wiki-coordination.md) | Markdown protocol layer for multi-agent wiki dialogue, consensus, RoleSpace review, and structural audit | files | pull | — | no | yes |
| [LLM-WIKI-MCP](./reviews/LLM-WIKI-MCP.md) | local Markdown wiki with SQLite FTS, MCP/CLI retrieval, Ollama ask, provenance ingest, sidecar notes, and ask-history memory | files | both | targeted | yes | yes |
| [LLM-Wiki-v3](./reviews/LLM-Wiki-v3.md) | Markdown+git wiki with schema validation, provenance-checked ingest, pending review, and hybrid pull retrieval | repo | pull | — | no | yes |
| [llmwiki-marimo](./reviews/llmwiki-marimo.md) | local Marimo LLM Wiki with generated Markdown pages, SQLite FTS/citation graph, pull chat tools, and repairable wiki memory | files | pull | — | no | yes |
| [Mem0](./reviews/mem0.md) | memory SDK/server/platform with additive trace extraction, hybrid retrieval, agent plugins, hooks, and pushed context injection | vector | both | targeted | yes | yes |
| [Memex](./reviews/memex.md) | isolated Claude Code runtime that maintains a markdown wiki through queued ingest, query, and lint jobs | files | pull | — | no | yes |
| [Memori](./reviews/Memori.md) | SDK and agent integrations with trace-learning augmentation, SQL/Rust storage, hybrid recall, and pre-call memory injection | rdbms | both | targeted | yes | — |
| [MemoryOS](./reviews/MemoryOS.md) | hierarchical conversational memory with trace-learning summaries, profiles, knowledge extraction, vector retrieval, and pre-call prompt assembly | files | both | targeted | yes | — |
| [MemPalace](./reviews/mempalace.md) | local-first ChromaDB/SQLite memory palace with transcript mining, MCP tools, hooks, and explicit wake-up/search read-back | files | pull | — | yes | — |
| [memwiki](./reviews/memwiki.md) | npm CLI protocol scaffold for AGENTS/hook files, hot-cache wiki memory, agent-maintained trace updates, and coarse push read-back | files | both | coarse | yes | — |
| [MentisDB](./reviews/mentisdb.md) | append-only hash-chained agent memory with MCP/REST tools, skill registry, LLM extraction, and LangChain memory | files | both | targeted | yes | yes |
| [Meta-Harness](./reviews/meta-harness.md) | trace-learning harness search that uses logs, evaluations, proposer skills, and generated code to evolve memory and agent scaffolds | files | both | targeted | yes | yes |
| [MiroShark](./reviews/MiroShark.md) | simulation knowledge graph with Neo4j graph memory, trace-learning agent activity edges, report-agent reasoning traces, and many public export surfaces | graph | both | targeted | yes | — |
| [nao](./reviews/nao.md) | analytics-agent context builder with file-backed project context, SQL guardrails, stories, and pushed trace-learning user memory | files | both | coarse | yes | yes |
| [napkin](./reviews/napkin.md) | local Markdown/Obsidian vault CLI and SDK with progressive overview, BM25 search, read, templates, and file writes | files | pull | — | no | — |
| [Nuggets](./reviews/nuggets.md) | TypeScript HRR fact memory, Pi prompt injection, trace capture, hit-count promotion to MEMORY.md, and Telegram/WhatsApp gateway | files | both | coarse | yes | — |
| [o-o](./reviews/o-o.md) | polyglot HTML/bash living documents with embedded update contracts, source caches, changelogs, sync shell, and Claude CLI dispatch | files | pull | — | no | — |
| [OKF Harness](./reviews/okf-harness.md) | local file-first OKF wiki harness with source provenance, bounded CLI reads, generated agent guidance, lint, and graph reports | files | pull | — | no | yes |
| [OpenClerk](./reviews/openclerk.md) | local JSON runner over Markdown vaults with SQLite projections, provenance, synthesis, reports, and optional semantic modules | files | pull | — | no | yes |
| [OpenSage](./reviews/OpenSage.md) | ADK agent framework with dynamic subagents, Skills, sandbox memory, Neo4j history/memory, plugins, and RL adapters | files | both | targeted | yes | yes |
| [OpenViking](./reviews/openviking.md) | context database with viking:// files, session-derived memory, hierarchical retrieval, hooks, MCP, and LangGraph injection | files | both | targeted | yes | yes |
| [OpenWiki](./reviews/openwiki.md) | agent-generated repository wiki with Git-scoped updates, root AGENTS/CLAUDE pointers, and no wiki retrieval index | repo | both | targeted | no | yes |
| [Operational Ontology Framework](./reviews/operational-ontology-framework.md) | public D+L+A artifact templates for governed AI work, with no implemented memory runtime | repo | pull | — | no | — |
| [Origin](./reviews/origin.md) | local AI-work memory daemon with sourced pages, hybrid retrieval, review gates, git-backed Markdown, and MCP/Claude Code read-back | sqlite | both | targeted | yes | yes |
| [OS-Copilot](./reviews/OS-Copilot.md) | FRIDAY promotes judged Python execution traces into Chroma-retrieved reusable tools for later planning and codegen | files | push | targeted | yes | yes |
| [Pal](./reviews/pal.md) | Agno AgentOS personal knowledge team with PostgreSQL/pgvector routing, context files, compiled wiki, SQL, schedules, and Agno memory read-back | rdbms | both | coarse | no | yes |
| [Phantom](./reviews/phantom.md) | VM co-worker with Qdrant memory, heuristic session extraction, and queued self-evolution over config files | vector | both | targeted | yes | yes |
| [pi-self-learning](./reviews/pi-self-learning.md) | pi extension that reflects completed agent sessions into git-backed daily, core, and long-term memory files | files | both | coarse | yes | — |
| [Playground](./reviews/playground.md) | TribleSpace pile runtime with user-created temporal memory chunks and budget-aware context cover | graph | both | coarse | no | — |
| [Quicky Wiki](./reviews/quicky-wiki.md) | document-derived SQLite claim graph with confidence events, metabolism, generated wiki files, and MCP pull tools | sqlite | pull | — | no | — |
| [ReasoningBank](./reviews/reasoning-bank.md) | trace-learning benchmark memories selected by embeddings and injected into WebArena and mini-SWE-agent prompts | files | both | targeted | yes | — |
| [Reflexion](./reviews/reflexion.md) | benchmark agents turn failed trajectories and test feedback into task-local verbal lessons for later attempts | in-memory | push | targeted | yes | — |
| [ReframeWeb](./reviews/ReframeWeb.md) | SurrealDB graph memory for a voice agent; LLM-hinted tag/substring + recency-cutoff retrieval, per-turn push, agent-emitted preference memories, no curation | graph | push | targeted | no | — |
| [REM](./reviews/REM.md) | episodic memory service with trace-learning episodes, vector/graph retrieval, LangChain injection, and partially wired consolidation | rdbms | both | targeted | yes | — |
| [SAGE](./reviews/sage.md) | consensus-governed local agent memory with MCP turn capture, hooks, hybrid recall, decay, and corroboration | sqlite | both | targeted | yes | yes |
| [sage-wiki](./reviews/sage-wiki.md) | LLM-compiled wiki memory with SQLite search/vector/ontology state, MCP pull tools, session capture, and trust gates | files | pull | — | yes | — |
| [Secure LLM-Wiki](./reviews/secure-llm-wiki.md) | hardened claim-wiki pipeline with nonce-delimited extraction, trust tiers, adversarial review, write gates, quarantine, and coarse read-back | files | both | coarse | no | yes |
| [Self-Training-LLM](./reviews/Self-Training-LLM.md) | offline synthetic Wikipedia QA generation, uncertainty-filtered SFT/DPO datasets, and model-weight learning rather than contextual memory | files | pull | — | yes | — |
| [Semiont](./reviews/semiont.md) | event-sourced W3C annotation KB with human/AI peer workflows, graph/vector projections, context gathering, and pull-based agent access | files | pull | — | no | — |
| [sift-kg](./reviews/sift-kg.md) | CLI document-to-knowledge-graph pipeline with LLM extraction, human-reviewed entity resolution, graph queries, and agent skill guidance | files | pull | — | no | — |
| [Siftly](./reviews/siftly.md) | local SQLite Twitter/X bookmark knowledge base with AI enrichment, category routing, FTS5 search, LLM reranking, mindmap, exports, and JSON CLI | sqlite | pull | — | no | — |
| [Signet AI](./reviews/signetai.md) | local-first daemon memory with SQLite, FTS/vector/graph recall, hook injection, transcript lineage, and guarded repair paths | sqlite | both | targeted | yes | yes |
| [SkillNote](./reviews/skillnote.md) | self-hosted SKILL.md registry with collections, imports, sync adapters, usage/rating feedback, and prompt-derived draft candidates | rdbms | both | targeted | yes | — |
| [SkillRL](./reviews/SkillRL.md) | trajectory-derived SkillBank JSON, prompt-time skill push, dynamic failed-trajectory updates, and SFT/RL policy learning | files | push | targeted | yes | — |
| [SkillWeaver](./reviews/SkillWeaver.md) | web-agent trajectories distilled into Playwright API skills with LLM relevance push and verification metadata | files | push | targeted | yes | yes |
| [SkillX](./reviews/SkillX.md) | trajectory-derived planning, functional, and atomic skill libraries with filtering, merging, and prompt-time retrieval | files | push | targeted | yes | — |
| [Smriti-MCP](./reviews/smriti-mcp.md) | MCP markdown memory server with file-backed notes, lexical recall, traces, salience, wikilinks, and agent-mediated consolidation | files | pull | — | yes | — |
| [Spacebot](./reviews/spacebot.md) | Rust team-agent harness with SQLite graph memory, LanceDB hybrid recall, pushed working context, trace-learning persistence, and skill injection | sqlite | both | targeted | yes | — |
| [Sparks](./reviews/sparks.md) | Go runtime for Karpathy-style LLM wikis with deterministic ingest, manifest, lint, collection, query, brief, and MCP plumbing | files | pull | — | no | yes |
| [Stash](./reviews/stash.md) | MCP-served Postgres/pgvector memory with episodes, consolidated facts, graph-like relations, goals, failures, hypotheses, and decay | rdbms | pull | — | no | — |
| [supermemory](./reviews/supermemory.md) | hosted memory API with generated SDK contracts, profile/search injection middleware, MCP tools, browser capture, graph UI, and trace-learning memory | service-object | both | targeted | yes | — |
| [Synapptic](./reviews/synapptic.md) | trace-learning user-model builder that mines Claude transcripts into weighted profiles, benchmarked guards, and assistant memory files | files | both | targeted | yes | — |
| [Synthadoc](./reviews/synthadoc.md) | local LLM wiki compiler with Markdown pages, provenance, lifecycle audit, query agents, routing, SSE UI, and context packs | files | both | targeted | no | yes |
| [Synto](./reviews/synto.md) | local LLM vault compiler that turns raw notes into reviewed Markdown wiki articles, SQLite identity state, agent packs, and MCP read tools | files | both | targeted | yes | yes |
| [Tendril](./reviews/tendril.md) | self-extending desktop agent with filesystem capability registry, model-authored TypeScript tools, and Deno sandbox execution | files | pull | — | no | yes |
| [Thalo](./reviews/thalo.md) | structured plain-text knowledge language with schemas, validation, git-aware synthesis actualization, LSP tooling, and PR automation | files | pull | — | no | — |
| [TheKnowledge](./reviews/TheKnowledge.md) | file-first LLM wiki gateway with citation-grounded Markdown, NotebookLM synthesis, MCP tools, and policy distillation | files | both | targeted | yes | yes |
| [Tolaria](./reviews/tolaria.md) | files-first Markdown vault desktop app with Git, type conventions, MCP tools, and active-note AI context push | files | both | targeted | no | — |
| [Tracecraft](./reviews/tracecraft.md) | serverless bucket-backed multi-agent coordination with JSON memory, atomic claims, mailboxes, artifacts, and session mirroring | files | pull | — | no | yes |
| [Virtual Context](./reviews/virtual-context.md) | proxy-owned context virtualization with trace-learning compaction, facts, paging tools, and prompt-time memory injection | sqlite | both | targeted | yes | yes |
| [VLM-wiki](./reviews/VLM-wiki.md) | file-backed multimodal personal wiki scaffold with AGENTS instructions, raw media, VLM analysis scripts, and Obsidian Markdown read-back | files | pull | — | no | — |
| [Voiden](./reviews/voiden.md) | offline Git-native API workspace with .void Markdown/request files, linked blocks, request history, extension skills, and local execution | files | pull | — | no | yes |
| [Voyager](./reviews/voyager.md) | Minecraft lifelong-learning agent with trace-learning executable skill libraries, Chroma retrieval, curriculum QA cache, and prompt pushback | files | both | targeted | yes | — |
| [WeKnora](./reviews/WeKnora.md) | enterprise RAG and agent platform with document chunks, wiki pages, graph memory, ReAct tools, and push plus pull read-back | rdbms | both | targeted | yes | yes |
| [WUPHF](./reviews/wuphf.md) | local multi-agent office with git-backed markdown wiki, per-agent notebooks, fact extraction, learning logs, lint, and cited lookup | repo | both | targeted | yes | yes |
| [xMemory](./reviews/xMemory.md) | trace-learning hierarchical agent memory with JSONL stores, Chroma/BM25 search, semantic themes, graph files, and pull-only retrieval | files | pull | — | yes | — |
| [Zikkaron](./reviews/Zikkaron.md) | Claude Code MCP memory with SQLite/FTS/vector storage, predictive write gating, trace-learning consolidation, hooks, and push/pull recall | sqlite | both | targeted | yes | — |
