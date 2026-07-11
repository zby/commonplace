---
description: "Pratiyush llm-wiki review: local file-based transcript-to-wiki compiler with raw session capture, agent-authored wiki pages, static AI exports, MCP tools, and optional synthesis"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
last-checked: "2026-06-04"
---

# llm-wiki (Pratiyush)

`llm-wiki`, from `Pratiyush/llm-wiki`, is a local Python package and agent workflow for turning Claude Code, Codex CLI, Cursor, Gemini, Copilot, and Obsidian session history into a Karpathy-style `raw/` -> `wiki/` -> `site/` knowledge base. At the reviewed commit, the implemented core is a file-based converter, wiki/static-site builder, AI-readable exporters, lint/governance helpers, MCP server, packaged Claude skills/slash commands, and optional LLM-backed synthesis of source pages from raw sessions.

**Repository:** https://github.com/Pratiyush/llm-wiki

**Reviewed commit:** [06c30e2b0c9018b11463b4fa37de0d75248cde5c](https://github.com/Pratiyush/llm-wiki/commit/06c30e2b0c9018b11463b4fa37de0d75248cde5c)

**Last checked:** 2026-06-04

## Core Ideas

**The system preserves a three-layer file memory.** The architecture document names `raw/` as immutable source-of-truth, `wiki/` as the LLM-maintained layer, and `site/` as a regenerable static layer; `cmd_init` seeds all three plus navigation files such as `MEMORY.md`, `CRITICAL_FACTS.md`, `hints.md`, and `hot.md` ([docs/architecture.md](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/docs/architecture.md), [llmwiki/cli.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/cli.py)). The important boundary is that raw sessions are retained evidence, while wiki pages are behavior-shaping summaries and indexes.

**Adapter-driven conversion turns agent traces into durable Markdown.** Core adapters discover Claude Code and Codex CLI stores, contrib adapters cover other agents, and `convert_all` reads JSONL transcripts, filters records, redacts secrets, computes metadata such as tool counts and token totals, and writes one frontmatter-rich Markdown file under `raw/sessions/` ([llmwiki/adapters/__init__.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/adapters/__init__.py), [llmwiki/adapters/claude_code.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/adapters/claude_code.py), [llmwiki/convert.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/convert.py)).

**The wiki layer is partly agent-authored, partly optionally compiled.** The canonical ingest workflow in the packaged skill tells a host agent to read raw session Markdown, write `wiki/sources/`, create/update entities and concepts, cross-link pages, record contradictions, and update `wiki/index.md` / `wiki/overview.md` / `wiki/log.md` ([.claude/skills/llmwiki-ingest/SKILL.md](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/.claude/skills/llmwiki-ingest/SKILL.md)). Separately, `synthesize_new_sessions()` can scan new raw sessions, call a dummy/Ollama/agent-delegate backend, write `wiki/sources/<project>/<date>-<slug>.md`, preserve curated tags, update its mtime state, append one log entry, and rebuild the Sources section of the wiki index ([llmwiki/synth/pipeline.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/synth/pipeline.py), [llmwiki/synth/agent_delegate.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/synth/agent_delegate.py)).

**Context efficiency is mostly pre-compilation plus bounded pull surfaces.** `build_site()` renders sessions once, writes per-page `.txt` and `.json` siblings, builds a chunked `search-index.json`, and emits `llms.txt`, `llms-full.txt`, JSON-LD, sitemap, RSS, robots, manifest, and an AI readme ([llmwiki/build.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/build.py), [llmwiki/exporters.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/exporters.py)). The MCP `wiki_query` and `wiki_search` tools bound file reads with per-file and aggregate byte caps, while `llms-full.txt` caps the flattened dump at about 5 MB, so the system offers progressive retrieval rather than blindly loading the full corpus ([llmwiki/mcp/server.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/mcp/server.py)).

**Governance is inspectable but unevenly enforced.** Raw write guards prevent accidental overwrite unless `--force` is used; candidate pages can be promoted, merged, discarded, or listed as stale; lint rules validate frontmatter, wikilinks, stale candidates, and stale references; lifecycle and confidence modules define states and scoring, but I did not find those functions automatically rewriting normal wiki pages in the core pipeline ([llmwiki/convert.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/convert.py), [llmwiki/candidates.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/candidates.py), [llmwiki/lint/__init__.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/lint/__init__.py), [llmwiki/lifecycle.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/lifecycle.py), [llmwiki/confidence.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/confidence.py)).

## Artifact analysis

- **Storage substrate:** `files` `repo` — Retained state lives in local files: `.jsonl` session stores outside the repo, converted `raw/sessions/*.md`, `wiki/**/*.md`, generated `site/`, `.llmwiki-state.json`, `.llmwiki-synth-state.json`, `.llmwiki-queue.json`, `.llmwiki-pending-prompts/`, package skills, slash commands, tests, and docs. Git can version the project and wiki, but there is no database or vector store in the core implementation.
- **Representational form:** `prose` `symbolic` — Session bodies, wiki pages, synthesis prompts, navigation files, packaged skills, and docs are prose; frontmatter, state JSON, adapter registry names, lifecycle enums, lint rule outputs, MCP schemas, search indexes, JSON-LD, manifests, and pending sentinels are symbolic. The reviewed core does not retain embeddings or model weights.
- **Lineage:** `authored` `imported` `trace-extracted` — Skills, slash commands, docs, seeds, lint rules, and user/agent-authored wiki pages are authored; Obsidian and other input adapters can import existing files; raw sessions and synthesized source pages are derived from agent transcripts, tool calls, model metadata, and session timing.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` `learning` `enforcement` — Raw sessions, wiki pages, exports, and MCP query results serve as knowledge; packaged skills, slash commands, `CLAUDE.md`/`AGENTS.md`, and `.kiro/steering` instruct host agents; indexes, folder context, tags, adapters, queues, and state files route work; lint, lifecycle validity, redaction, path guards, raw overwrite guards, and candidate status validate or enforce boundaries; search indexes, MCP lexical scoring, facets, and confidence fields rank; conversion and synthesis are trace-derived learning from prior sessions.

**Raw session files.** These are Markdown evidence artifacts generated from JSONL records. They preserve transcript content in a redacted, truncated, metadata-rich form, with project, timestamps, model, tool counts, token totals, adapter tags, and source file lines used by later build, graph, search, and ingest paths ([llmwiki/convert.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/convert.py)).

**Wiki pages and navigation files.** `wiki/sources/`, `wiki/entities/`, `wiki/concepts/`, `wiki/syntheses/`, `wiki/index.md`, `overview.md`, and `log.md` are the main durable knowledge layer. Their authority depends on how they were produced: manual/agent ingest instructions make them authored summaries, while `synthesize_new_sessions()` can produce source pages automatically from raw session traces.

**Search and export artifacts.** `site/search-index.json`, `site/search-chunks/*.json`, per-page `.txt` / `.json`, `llms.txt`, `llms-full.txt`, `graph.jsonld`, sitemap, RSS, robots, manifest, and copied raw sources are derived access structures. They are not the source of truth, but they strongly shape what browser users, MCP clients, and downstream agents can cheaply read ([llmwiki/build.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/build.py), [llmwiki/exporters.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/exporters.py)).

**Packaged instructions and MCP tools.** The `.claude/skills/` and `.claude/commands/` files are system-definition artifacts that teach the host agent when and how to sync, ingest, query, reflect, lint, and build. The MCP server exposes a narrower programmatic read/write surface: query, search, list, read, lint, sync, export, confidence, lifecycle, dashboard, entity search, and category browse, with explicit path and byte guards ([.claude/skills/llmwiki-query/SKILL.md](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/.claude/skills/llmwiki-query/SKILL.md), [llmwiki/mcp/server.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/mcp/server.py)).

Promotion path: llm-wiki's strongest path is session JSONL -> raw Markdown -> wiki source/entity/concept/synthesis page -> search/export/MCP surface. Candidate pages add a review buffer for uncertain generated entities and concepts. There is no evidence of a fully automatic promotion from trace to verified/high-authority rule; higher authority mostly comes from explicit agent or human workflow steps.

## Comparison with Our System

| Dimension | Pratiyush llm-wiki | Commonplace |
|---|---|---|
| Primary purpose | Personal/project LLM session history wiki and static viewer | Methodology KB for agent-operated knowledge bases |
| Canonical retained artifact | Local Markdown files under `raw/` and `wiki/`, plus generated static/export files | Typed Markdown artifacts under `kb/` with collection contracts and validation |
| Source lineage | Agent transcripts and optional imported notes, transformed into wiki pages | Authored notes, instructions, reviews, snapshots, and source captures |
| Read-back | Explicit pull through skills, slash commands, MCP tools, static search, and exports | Explicit pull through `rg`, indexes, links, skills, reports, and validation |
| Governance | Redaction, raw immutability guard, lint rules, candidate workflow, lifecycle/confidence fields | Type specs, collection routing, deterministic validation, semantic review gates, curated indexes |

llm-wiki is closer to a personal transcript compiler than to Commonplace's durable methodology library. Its best design move is preserving raw session evidence while letting a higher layer compact and cross-link that evidence. Commonplace shares the file-native preference but puts more authority in typed collection contracts, validation, and review gates.

The main divergence is semantic authority. llm-wiki's packaged ingest/query skills deliberately rely on the current host agent to write and interpret the wiki. That makes adoption easy for Claude Code/Codex users, but it also means many claims about page quality, contradiction handling, and synthesis depend on agent discipline rather than a deterministic core. Commonplace is slower, but more explicit about artifact type, status, link semantics, and review state.

### Borrowable Ideas

**AI-readable sibling exports.** Ready now. Commonplace could emit per-note `.txt` / `.json` or a bounded `llms-full.txt`-style bundle for downstream agents without changing the canonical Markdown source.

**Raw overwrite guards.** Ready now. The explicit `raw/` immutability check is a useful pattern for `kb/sources/` snapshots and any future imported trace store.

**Agent-delegate synthesis handshake.** Needs a concrete workflow. The pending-prompt sentinel model is a practical way to use the current agent session without API keys, but Commonplace would need stronger validation before generated outputs enter durable collections.

**Candidate directory for low-authority generated pages.** Ready with adaptation. Commonplace's workshop layer could use a candidate namespace for generated notes that are searchable and reviewable but not yet library artifacts.

**Expose counts before content.** Ready as interface vocabulary. llm-wiki's indexes, dashboard, and MCP list/search tools let an agent estimate where useful content lives before opening large pages; Commonplace can continue pushing this through indexes and reports.

## Write side

**Write agency:** `manual` `automatic` — Users and agents manually write wiki pages through packaged workflows, candidate operations, Obsidian/vault edits, and CLI commands; automatic paths convert agent session stores into raw Markdown, optionally synthesize source pages from raw sessions, rebuild selected indexes/exports, enqueue pending ingest items, and generate static AI-readable artifacts.

**Curation operations:** `consolidate` — The optional synthesis pipeline turns an existing raw session page into a more compact wiki source page, and the agent-delegate backend stages the same consolidation through pending prompts. Other automatic changes I found are acquisition, access-structure rebuilds, state tracking, export generation, or guards, not content curation over existing memory.

### Trace-derived learning

**Trace source:** `session-logs` `tool-traces` — The primary input is agent transcript JSONL: user/assistant turns, tool-use blocks, tool results, timestamps, model usage, session paths, and project/session metadata.

**Learning scope:** `per-project` `cross-task` — Raw sessions and synthesized/wiki pages are grouped by project, but the resulting local wiki can be queried across projects and later tasks.

**Learning timing:** `offline` `staged` — Conversion and synthesis run after traces already exist, either by explicit command or external hook; the agent-delegate backend stages pending prompts for a later slash-command completion step.

**Distilled form:** `prose` `symbolic` — Distilled outputs include prose raw/session Markdown, synthesized source pages, wiki summaries, navigation files, and symbolic frontmatter, tags, state files, indexes, JSON exports, search chunks, and MCP schemas.

**Extraction.** The converter is deterministic extraction and redaction from JSONL into Markdown; it computes message/tool/token metadata but does not infer high-level lessons. The optional synthesizer performs the semantic extraction: a backend reads a raw session body and metadata through a prompt template, then writes or stages a source page with tags. The strongest automatic trace-derived loop is therefore trace -> raw Markdown -> synthesized source page, not trace -> enforced rule.

**Scope and timing.** `llmwiki sync` can be run manually, from MCP with confirmation, or by an external SessionStart hook. Synthesis is a separate command and can use dummy, Ollama, or agent-delegate backends. The agent-delegate mode writes pending prompt files and placeholder pages first, then relies on the host agent to complete them later.

**Survey fit.** llm-wiki sits in the trace-to-wiki family: raw agent traces become durable, inspectable prose artifacts, then optional summarization makes them cheaper to read. It supports later self-learning through skills such as `self-learn`, but the inspected code keeps that promotion human/agent-mediated rather than automatic.

## Read-back

**Read-back:** `pull` — Memory content reaches future agents and users through explicit actions: the packaged query skill tells the host agent to read `wiki/index.md`, `wiki/overview.md`, and relevant pages; MCP clients call query/search/read/export tools; browser users use static search; downstream agents read `llms.txt`, `llms-full.txt`, JSON-LD, or per-page siblings. I did not find a core mechanism that automatically injects selected retained wiki content into an agent context without such a query/read action.

The static search index is optimized pull: it chunks per-project entries and exposes facets, tree/flat mode, slash-command docs, and docs pages. MCP query is also pull: it does lexical scoring over `wiki/**/*.md`, caps file and aggregate bytes, and returns selected snippets plus overview context. `wiki_search` can include raw sessions, but only when the caller asks.

Packaged skills are a boundary case. Installing `llmwiki-query` can cause a host skill router to choose the query workflow when the user asks about past work, but the retained memory still enters by the agent following instructions to open selected wiki files. The skill is a pushed system-definition artifact; the wiki content itself is not pushed.

Authority at consumption is advisory. Query results, source pages, exports, and raw sessions provide evidence and context. The MCP `wiki_sync` tool can mutate by running `llmwiki sync`, but it defaults to dry-run and requires confirmation for live writes; read tools use path allowlists and byte caps. I did not find a with/without memory ablation or post-answer audit proving that queried wiki content changed behavior faithfully.

## Curiosity Pass

**The README is broader than the automatic core.** It advertises Auto Dream and rich quality governance, but the code I inspected shows many governance primitives and docs, not one always-on autonomous memory-maintenance loop.

**The most valuable retained artifact may be raw Markdown, not the generated wiki.** The raw layer gives a durable, redacted, inspectable trace corpus that can be reprocessed by better agents later.

**The agent-delegate backend is an adoption hack with real architectural value.** It converts "call an external LLM API" into "stage a prompt for the already-running coding agent", which is cheap and local but shifts quality control to the surrounding workflow.

**MCP is a read surface, not a full memory runtime.** The tools expose search, read, export, lint, and sync, but they do not maintain a relevance-triggered memory stream into future model calls.

## What to Watch

- Whether `synthesize_new_sessions()` expands from one-source summaries into cross-session concept/entity synthesis with explicit provenance and candidate review.
- Whether lifecycle/confidence functions become active mutation policies, rather than validators, dashboard fields, and search facets.
- Whether the SessionStart hook path is updated to the current package entry point everywhere; some docs still describe direct script/module patterns that look stale relative to the current CLI.
- Whether MCP adds a host-side pre-invocation hook or router that can push relevant wiki pages automatically; that would change the read-back classification.
- Whether generated source pages gain deterministic quote/span provenance back to raw session lines before promotion into trusted wiki pages.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: llm-wiki stores extensive transcript/wiki memory, but serves it mainly through explicit query/search/read/export actions.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: raw sessions, wiki pages, skills, state files, indexes, and exports differ by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: raw sessions, wiki pages, and exports mostly act as evidence/reference/context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: packaged skills, slash commands, lint rules, schemas, guards, and MCP tool definitions shape future behavior.
- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: llm-wiki derives durable raw and synthesized wiki artifacts from agent session traces.
