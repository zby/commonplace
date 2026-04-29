---
description: "Multi-agent session-transcript compiler that turns Claude/Codex/Cursor/Gemini history into a redacted markdown wiki, static site, exports, MCP tools, and agent prompt workflows"
type: ../types/agent-memory-system-review.md
tags: [related-systems, trace-derived]
status: current
last-checked: "2026-04-29"
---

# Pratiyush/llm-wiki

Pratiyush's LLM Wiki is a Python package for turning local coding-agent session history into a Karpathy-style wiki and static site. It is closer to an agent-session observability and compilation system than to the promptware-only [LLM Wiki](./llm-wiki.md): adapters read Claude Code, Codex CLI, Cursor, Gemini, Copilot, OpenCode, ChatGPT, and Obsidian traces; the converter writes redacted raw markdown; optional synthesis turns raw sessions into wiki source pages; the builder emits a browsable static site plus AI-consumable exports; and a stdlib MCP server exposes query, search, sync, lint, export, confidence, lifecycle, and dashboard tools. The most important design move is the explicit raw/wiki/site layering around agent traces, but the implementation's strongest hard guarantees are in conversion, redaction, build/export, and linting, not in the README's more ambitious "Auto Dream" memory-consolidation language.

**Repository:** https://github.com/Pratiyush/llm-wiki

**Reviewed commit:** https://github.com/Pratiyush/llm-wiki/commit/93e380d706b310852369c6cdf3ca66d7c90f5ea8

## Core Ideas

**Agent transcripts are the primary source material.** The README frames the system as a wiki compiled from Claude Code, Codex CLI, Cursor, Gemini CLI, Copilot, and Obsidian sessions. The code backs this with a common `BaseAdapter` contract: each adapter discovers session files, derives a project slug, and normalizes records into the shared renderer shape. Claude Code is the native schema; Codex has an implemented normalizer from `session_meta`, `turn_context`, `response_item`, and tool records; contrib adapters cover additional tools through the same registry ([README.md](https://github.com/Pratiyush/llm-wiki/blob/93e380d706b310852369c6cdf3ca66d7c90f5ea8/README.md), [llmwiki/adapters/base.py](https://github.com/Pratiyush/llm-wiki/blob/93e380d706b310852369c6cdf3ca66d7c90f5ea8/llmwiki/adapters/base.py), [llmwiki/adapters/claude_code.py](https://github.com/Pratiyush/llm-wiki/blob/93e380d706b310852369c6cdf3ca66d7c90f5ea8/llmwiki/adapters/claude_code.py), [llmwiki/adapters/codex_cli.py](https://github.com/Pratiyush/llm-wiki/blob/93e380d706b310852369c6cdf3ca66d7c90f5ea8/llmwiki/adapters/codex_cli.py), [llmwiki/adapters/contrib](https://github.com/Pratiyush/llm-wiki/tree/93e380d706b310852369c6cdf3ca66d7c90f5ea8/llmwiki/adapters/contrib)).

**The raw layer has real operational safeguards.** `llmwiki sync` parses JSONL, drops live sessions by default, filters noisy record types, normalizes records, redacts usernames and common secret/token shapes, caps pathological file and line sizes, writes one markdown transcript per session under `raw/sessions/`, and tracks idempotency in `.llmwiki-state.json`. It also enforces raw immutability unless `--force` is passed, which makes the "raw/ is source-of-truth" claim more than a convention ([llmwiki/convert.py](https://github.com/Pratiyush/llm-wiki/blob/93e380d706b310852369c6cdf3ca66d7c90f5ea8/llmwiki/convert.py), [docs/architecture.md](https://github.com/Pratiyush/llm-wiki/blob/93e380d706b310852369c6cdf3ca66d7c90f5ea8/docs/architecture.md)).

**The wiki layer is partly agent-maintained doctrine, partly implemented synthesis.** `AGENTS.md` and `CLAUDE.md` define the manual ingest/query/lint workflows: read raw sources, update `wiki/sources/`, maintain entities/concepts/syntheses, preserve contradictions, and append to `wiki/log.md`. Separately, `llmwiki.synth.pipeline` implements an optional raw-session-to-source-page pipeline with dummy, Ollama, and agent-delegate backends, date-prefixed output filenames, tag merging, log appends, and index rebuilds. The agent-delegate backend is a useful zero-API-cost pattern: it writes a pending prompt to `.llmwiki-pending-prompts/` and a sentinel placeholder page, then expects the live agent to complete the page later ([AGENTS.md](https://github.com/Pratiyush/llm-wiki/blob/93e380d706b310852369c6cdf3ca66d7c90f5ea8/AGENTS.md), [.claude/commands/wiki-sync.md](https://github.com/Pratiyush/llm-wiki/blob/93e380d706b310852369c6cdf3ca66d7c90f5ea8/.claude/commands/wiki-sync.md), [.claude/commands/wiki-ingest.md](https://github.com/Pratiyush/llm-wiki/blob/93e380d706b310852369c6cdf3ca66d7c90f5ea8/.claude/commands/wiki-ingest.md), [llmwiki/synth/pipeline.py](https://github.com/Pratiyush/llm-wiki/blob/93e380d706b310852369c6cdf3ca66d7c90f5ea8/llmwiki/synth/pipeline.py), [llmwiki/synth/agent_delegate.py](https://github.com/Pratiyush/llm-wiki/blob/93e380d706b310852369c6cdf3ca66d7c90f5ea8/llmwiki/synth/agent_delegate.py)).

**Static-site and AI-export surfaces are first-class.** `build.py` renders raw sessions and wiki pages into a standalone static site with project pages, session pages, activity heatmaps, model cards, token/tool visualizations, search indexes, keyboard navigation, and downloadable raw markdown. `exporters.py` writes `llms.txt`, `llms-full.txt`, `graph.jsonld`, page-level `.txt` and `.json` siblings, sitemap, RSS, robots, manifest, and `ai-readme.md`. That makes the compiled wiki consumable by humans, static hosting, and other agents without requiring a database or server at read time ([llmwiki/build.py](https://github.com/Pratiyush/llm-wiki/blob/93e380d706b310852369c6cdf3ca66d7c90f5ea8/llmwiki/build.py), [llmwiki/exporters.py](https://github.com/Pratiyush/llm-wiki/blob/93e380d706b310852369c6cdf3ca66d7c90f5ea8/llmwiki/exporters.py), [llmwiki/graph.py](https://github.com/Pratiyush/llm-wiki/blob/93e380d706b310852369c6cdf3ca66d7c90f5ea8/llmwiki/graph.py), [llmwiki/search_tree.py](https://github.com/Pratiyush/llm-wiki/blob/93e380d706b310852369c6cdf3ca66d7c90f5ea8/llmwiki/search_tree.py)).

**Quality is enforced mostly by structural lint and metadata helpers.** The lint registry ships deterministic checks for frontmatter completeness/validity, link integrity, orphan detection, content freshness, entity consistency, duplicate detection, index sync, stale candidates, tag/topic convention, stale references, frontmatter counts, and tool consistency, plus optional LLM-powered contradiction, claim-verification, and summary-accuracy rules. Separate confidence and lifecycle modules implement the advertised 4-factor confidence score and 5-state lifecycle, but those are helper mechanisms over page metadata rather than a complete semantic review system ([llmwiki/lint](https://github.com/Pratiyush/llm-wiki/tree/93e380d706b310852369c6cdf3ca66d7c90f5ea8/llmwiki/lint), [llmwiki/lint/rules](https://github.com/Pratiyush/llm-wiki/tree/93e380d706b310852369c6cdf3ca66d7c90f5ea8/llmwiki/lint/rules), [llmwiki/confidence.py](https://github.com/Pratiyush/llm-wiki/blob/93e380d706b310852369c6cdf3ca66d7c90f5ea8/llmwiki/confidence.py), [llmwiki/lifecycle.py](https://github.com/Pratiyush/llm-wiki/blob/93e380d706b310852369c6cdf3ca66d7c90f5ea8/llmwiki/lifecycle.py), [llmwiki/freshness.py](https://github.com/Pratiyush/llm-wiki/blob/93e380d706b310852369c6cdf3ca66d7c90f5ea8/llmwiki/freshness.py)).

**The integration surface is broad but uneven.** The project ships a `llmwiki` CLI, shell/batch wrappers, Claude commands, Claude skills, plugin metadata, a multi-agent skill installer, Docker/Homebrew packaging, and a stdlib JSON-RPC MCP server. The MCP server has a concrete allowlisted read surface, bounded search/query input sizes, dry-run defaults for sync, and tools for search, read, lint, export, confidence, lifecycle, dashboard, entities, and categories. By contrast, some README claims are only seeded doctrine or command instructions: `MEMORY.md`, `SOUL.md`, `CRITICAL_FACTS.md`, and hot caches are created by `init`, but I did not find a code path implementing the advertised Auto Dream consolidation beyond those artifacts and agent-facing workflows ([llmwiki/cli.py](https://github.com/Pratiyush/llm-wiki/blob/93e380d706b310852369c6cdf3ca66d7c90f5ea8/llmwiki/cli.py), [llmwiki/mcp/server.py](https://github.com/Pratiyush/llm-wiki/blob/93e380d706b310852369c6cdf3ca66d7c90f5ea8/llmwiki/mcp/server.py), [llmwiki/skill_installer.py](https://github.com/Pratiyush/llm-wiki/blob/93e380d706b310852369c6cdf3ca66d7c90f5ea8/llmwiki/skill_installer.py), [.claude/commands](https://github.com/Pratiyush/llm-wiki/tree/93e380d706b310852369c6cdf3ca66d7c90f5ea8/.claude/commands), [.claude/skills](https://github.com/Pratiyush/llm-wiki/tree/93e380d706b310852369c6cdf3ca66d7c90f5ea8/.claude/skills), [.claude-plugin/plugin.json](https://github.com/Pratiyush/llm-wiki/blob/93e380d706b310852369c6cdf3ca66d7c90f5ea8/.claude-plugin/plugin.json)).

## Comparison with Our System

| Dimension | Pratiyush/llm-wiki | Commonplace |
|---|---|---|
| Primary source | Agent session transcripts converted from local tool stores | Authored notes, sources, reviews, ADRs, and instruction artifacts |
| Main pipeline | `raw/` session markdown -> `wiki/` pages -> `site/` static outputs | `kb/` typed collections with generated indexes, validators, and review bundles |
| Knowledge creation | Converter plus optional LLM/agent synthesis over sessions | Agent/operator writing under collection-local type contracts |
| Retrieval and activation | Static search index, MCP keyword query/search, `llms*` exports, command/skill packaging | `rg`, authored indexes/descriptions, explicit links, skills, validators, review reports |
| Evidence and provenance | Raw transcript file retained; synthesized source pages cite `source_file` | Source snapshots, code-pinned citations, link semantics, review status, validation |
| Governance | Redaction, raw overwrite guard, structural lint, confidence/lifecycle metadata | Frontmatter validation, path-valued type specs, semantic review gates, curated link vocabulary |
| Learning loop | Trace-derived session-to-wiki compilation; partial agent-delegate synthesis; weak Auto Dream evidence | Mostly manual promotion from sources/workshops into library artifacts |

Pratiyush/llm-wiki is stronger where the task is "make my agent history inspectable and browseable immediately." Commonplace does not ingest local agent transcripts, render a full static UI, or ship `llms.txt`/JSON-LD/page siblings for downstream agents. Its adapter abstraction and redaction pipeline are therefore more mature than anything in commonplace's current source layer.

Commonplace is stronger where the task is "make a claim dependable." A source page generated from a transcript can preserve useful memory, but it does not by itself establish the role, scope, link semantics, or review state of the derived knowledge. Commonplace's type specs and review bundles create more friction, but that friction buys a stronger artifact contract.

The closest architectural alignment is files-first with derived projections. Both systems treat markdown files as the durable surface and indexes/exports as rebuildable views. The divergence is that llm-wiki optimizes for broad capture and presentation, while commonplace optimizes for curated methodology and semantic maintenance.

## Borrowable Ideas

**Session adapters as a source layer.** Ready once commonplace wants trace capture. The adapter contract is a clean split: each runtime owns discovery and normalization, while conversion/redaction/rendering stay shared. A commonplace analogue should write into a workshop or source collection first, not directly into mature notes.

**Raw overwrite guard.** Ready now as source-ingest guidance. The explicit refusal to overwrite existing raw files unless `--force` is passed is the right invariant for source snapshots and session-derived evidence.

**AI-consumable static exports.** Ready when publication matters. `llms.txt`, `llms-full.txt`, page-level `.txt`/`.json`, and JSON-LD are cheap derived surfaces that let another agent consume a KB without scraping HTML or understanding the repo layout.

**Agent-delegate synthesis.** Worth adapting for workflows where the user has already paid for an interactive agent session. Writing pending prompts and sentinel placeholders lets deterministic code orchestrate work without owning an API key or hiding the generation step.

**Structural lint breadth.** Partly ready. Commonplace already validates frontmatter and links, but llm-wiki's rule list is a reminder to validate stale references, tag/topic conventions, index counts, tool metadata consistency, and generated-page freshness as separate cheap checks before semantic review.

**Do not borrow the all-in-one product surface wholesale.** The static site, MCP server, skills, plugin, wrappers, Docker, Homebrew, and docs all make sense for a standalone product. Commonplace should copy individual integration patterns only when a stable consumer exists; otherwise this would add distribution machinery before the methodology needs it.

## Trace-derived learning placement

**Trace source.** The raw signal is local coding-agent session history: Claude Code JSONL, Codex CLI JSONL, and contrib adapter stores for Cursor, Gemini, Copilot, OpenCode, ChatGPT, and Obsidian. Trigger boundaries are manual or command-driven (`llmwiki sync`, `/wiki-sync`, `llmwiki synthesize`), not automatic mining at session end in the inspected code. Live sessions are skipped by default unless explicitly included.

**Extraction.** Extraction has two layers. The deterministic converter normalizes, redacts, truncates, and renders transcripts into markdown. The optional synthesis layer uses a dummy backend, Ollama backend, or agent-delegate prompt to create wiki source pages with summaries, claims, quotes, and connections. The oracle is weak: structural lint can catch broken forms and links, but the semantic correctness of a synthesized page is accepted from the LLM/agent unless the operator later reviews it.

**Substrate class and role.** The substrate is readable artifacts: raw transcript markdown, synthesized wiki pages, navigation files, static HTML, JSON/JSON-LD exports, and MCP-readable text. Most outputs play a knowledge role: future agents can query what happened and what pages say. Some seeded files (`AGENTS.md`, `CLAUDE.md`, skills, commands, `MEMORY.md`) are system-definition artifacts, but the inspected automatic path mainly promotes traces into knowledge pages, not into stronger rules or executable tools.

**Scope and timing.** Scope is per local installation and project. It is cross-agent in the sense that many agent runtimes can feed one wiki, but it is not cross-user or multi-tenant. Timing is staged and mostly offline: sync converts completed sessions, synthesis compiles new raw pages, build/export/lint produce views, and `/wiki-sync` can ask the live agent to fill pending synthesis prompts.

**Survey placement.** On the [trace-derived survey](../trace-derived-learning-techniques-in-related-systems.md), Pratiyush/llm-wiki extends the cross-agent session side with a **transcript-to-wiki compiler** subtype. Unlike cass-memory, it does not mine sessions into scored procedural rules; unlike Pi Self-Learning, it is not a single-host extension; unlike browzy.ai, it is centered on coding-agent session stores rather than interactive PKB Q&A. It strengthens the survey's claim that trace ingestion and artifact generation are easy to make concrete, while leaving the same open problem: deciding which derived claims deserve trust, promotion, and retirement.

## Curiosity Pass

The repo's most reliable contribution is not the LLM synthesis story; it is the disciplined transcript compiler. Redaction defaults, live-session skipping, raw immutability, path-safe slugs, state-file migration, generated search/export artifacts, and MCP scan caps are boring in the right way. They make the source layer robust enough that higher-level synthesis has something dependable to stand on.

The "wiki/" layer is less deterministic than the "raw/" and "site/" layers. Manual command instructions still tell the live agent to update entities, concepts, contradictions, and overview pages. The automatic synthesizer can create source pages, but it does not implement the whole AGENTS ingest contract. This is not a flaw if the project is understood as agent-in-the-loop tooling; it is a flaw only if the README is read as promising fully autonomous wiki maintenance.

The project has an unusual amount of integration surface for an alpha-stage tool. That makes it easy to adopt from many angles, but it also creates many promise surfaces: CLI help, README, Claude commands, skills, MCP tools, docs, and plugin metadata can drift from one another. The repeated comments about fixed regressions suggest the maintainers are actively tightening this, but the product surface is broad enough that drift should remain a watch item.

The confidence and lifecycle modules are conceptually good but not yet a trust system. A 4-factor score over source count, quality, recency, and inbound links can prioritize review; it cannot establish that a generated source summary preserves the important claims in the transcript. The optional LLM lint rules point in that direction but remain advisory.

## What to Watch

- Whether Auto Dream becomes an implemented consolidation loop rather than seeded `MEMORY.md`/navigation doctrine.
- Whether `llmwiki synthesize` grows from source-page generation into the full entity/concept/overview update contract currently delegated to agents.
- Whether trace-derived pages gain a review/promotion path so generated source pages can mature into trusted concept or decision artifacts.
- Whether the MCP query path stays keyword/snippet-based or grows a more typed context scheduler over projects, entities, confidence, lifecycle, and freshness.
- Whether the many adapter claims remain tested as upstream agent transcript schemas change.
- Whether broad packaging pressure causes product-surface drift, especially between README claims, slash commands, skills, and Python behavior.

---

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: Pratiyush/llm-wiki adds a multi-agent transcript-to-wiki compiler case where coding-session traces become raw markdown, wiki pages, static exports, and MCP-readable artifacts.
- [Files beat a database for agent-operated knowledge bases](../../notes/files-not-database.md) - exemplifies: raw transcripts, wiki pages, commands, skills, and exports stay file-shaped; operational state is sidecar JSON rather than a primary database.
- [A functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) - sharpens: synthesized pages should enter a workshop/review path before being treated as mature library knowledge.
- [Stale indexes are worse than no indexes](../../notes/stale-indexes-are-worse-than-no-indexes.md) - exemplifies: the system invests heavily in rebuildable search indexes, source indexes, graph exports, sitemap, RSS, and manifests because static views are only useful when regenerated.
- [LLM Wiki](./llm-wiki.md) - compares-with: both descend from Karpathy's LLM Wiki pattern, but the nvk review covers protocol/prompt packaging while Pratiyush ships a broad executable compiler and site/export toolchain.
- [kenhuangus/llm-wiki](./kenhuangus--llm-wiki.md) - compares-with: both are executable LLM Wiki implementations; kenhuangus focuses on external-source monitors and LLM claim integration, while Pratiyush focuses on agent-session transcript ingestion and static/AI export surfaces.
- [browzy.ai](./browzy-ai.md) - compares-with: both compile raw material into a local markdown wiki, but browzy centers on URLs/documents and query-time PKB use while Pratiyush centers on coding-agent history.
- [cass-memory](./cass_memory_system.md) - compares-with: both aggregate multi-agent session logs, but cass-memory promotes procedural playbook bullets with feedback scoring while Pratiyush/llm-wiki promotes browseable wiki/source artifacts.
