---
description: "llm-wiki review: local coding-agent transcript ingestion into immutable raw Markdown, distilled wiki pages, static AI exports, MCP pull tools, and lifecycle lint"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-06-02"
---

# llm-wiki

llm-wiki, from Pratiyush's `Pratiyush/llm-wiki` repository, is a local-first Python system for turning coding-agent session histories into a Karpathy-style LLM Wiki. At the reviewed commit, its implemented core still consumes local agent traces from Claude Code, Codex CLI, Copilot, Cursor, Gemini, OpenCode, ChatGPT exports, and optional Obsidian content; converts them into redacted immutable raw Markdown; then uses agent, dummy, or local Ollama synthesis paths plus manual slash-command workflows to produce interlinked wiki pages, a static HTML site, AI-consumable exports, and MCP query/read tools.

**Repository:** https://github.com/Pratiyush/llm-wiki

**Reviewed commit:** [06c30e2b0c9018b11463b4fa37de0d75248cde5c](https://github.com/Pratiyush/llm-wiki/commit/06c30e2b0c9018b11463b4fa37de0d75248cde5c)

**Last checked:** 2026-06-02

## Core Ideas

**Raw session Markdown is the preserved trace layer.** `llmwiki sync` discovers enabled adapters, parses local session stores, normalizes agent-specific records, redacts secrets and usernames, filters noisy record types, and writes frontmatter-rich Markdown under `raw/sessions/` ([llmwiki/convert.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/convert.py), [llmwiki/adapters/base.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/adapters/base.py)). The implementation now treats raw output as a guarded source-of-truth surface: `_raw_write_guard()` refuses to overwrite existing raw files unless `--force` is passed, and failures are recorded in `.llmwiki-quarantine.json` rather than silently dropped ([llmwiki/convert.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/convert.py), [llmwiki/quarantine.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/quarantine.py), [tests/test_raw_immutability.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/tests/test_raw_immutability.py)).

**Adapters separate discovery from conversion.** Core adapters include Claude Code and Codex CLI; contrib adapters cover Copilot Chat/CLI, Cursor, Gemini CLI, OpenCode, ChatGPT export, and Obsidian ([llmwiki/adapters/__init__.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/adapters/__init__.py), [tests/test_adapters.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/tests/test_adapters.py)). The base contract exposes session discovery, project slug derivation, sub-agent detection, and optional record normalization. Non-AI content such as Obsidian is marked opt-in, so default sync does not ingest a personal vault merely because it exists ([llmwiki/adapters/contrib/obsidian.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/adapters/contrib/obsidian.py), [tests/test_raw_immutability.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/tests/test_raw_immutability.py)).

**The wiki layer is trace distillation, not just indexing.** `CLAUDE.md`, `AGENTS.md`, skills, and slash commands define an ingest workflow where agents read raw source Markdown, write `wiki/sources/`, create or update entity/concept/synthesis pages, cross-link them, flag contradictions, and update `wiki/index.md`, `wiki/overview.md`, and `wiki/log.md` ([CLAUDE.md](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/CLAUDE.md), [AGENTS.md](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/AGENTS.md), [.claude/skills/llmwiki-ingest/SKILL.md](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/.claude/skills/llmwiki-ingest/SKILL.md)). The automated synthesis path can generate source pages from raw sessions using a dummy backend, local Ollama, or an agent-delegate placeholder/pending-prompt loop ([llmwiki/synth/pipeline.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/synth/pipeline.py), [llmwiki/synth/ollama.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/synth/ollama.py), [llmwiki/synth/agent_delegate.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/synth/agent_delegate.py)).

**Context efficiency is layered and mostly pull-oriented.** The system does not put the entire corpus into the next agent prompt by default. It creates progressively consumable surfaces: `wiki/index.md` and `overview.md`, folder `_context.md` stubs for large directories, `hot.md` and other seeded nav files, static search indexes with lazy per-project chunks, capped `llms-full.txt`, per-page `.txt`/`.json` siblings, JSON-LD graph exports, MCP `wiki_query`/`wiki_search`/`wiki_read_page`, and prompt-cache scaffolding for future Anthropic batch synthesis ([llmwiki/context_md.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/context_md.py), [llmwiki/build.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/build.py), [llmwiki/exporters.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/exporters.py), [llmwiki/mcp/server.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/mcp/server.py), [llmwiki/cache.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/cache.py)). Context volume is bounded by file caps, byte caps, result counts, source-page synthesis body caps, and export caps; context complexity is reduced by making agents choose a layer before reading deeper.

**Governance is a mix of runtime guards, lint, lifecycle metadata, and candidate quarantine.** The repo implements confidence scoring, lifecycle transitions, 16 lint rules, stale-candidate detection, link checking, build manifests with hashes/perf budgets, and a candidate promotion/merge/discard workflow ([llmwiki/confidence.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/confidence.py), [llmwiki/lifecycle.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/lifecycle.py), [llmwiki/lint/rules/__init__.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/lint/rules/__init__.py), [llmwiki/candidates.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/candidates.py), [llmwiki/manifest.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/manifest.py)). Some README claims run ahead of code: "Auto Dream" appears as seeded `MEMORY.md` text and README/release prose, but I found no consolidation implementation beyond the seed file; `.claude-plugin/plugin.json` declares a `hooks/session-start.sh` hook file that is not present in the checkout ([README.md](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/README.md), [llmwiki/cli.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/cli.py), [.claude-plugin/plugin.json](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/.claude-plugin/plugin.json)).

**MCP and static exports make the wiki consumable by other agents.** The MCP server is stdlib JSON-RPC over stdio with twelve tools for query, search, list, read, lint, sync, export, confidence, lifecycle, dashboard, entity search, and category browse ([llmwiki/mcp/server.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/mcp/server.py), [README.md](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/README.md), [tests/test_mcp_protocol.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/tests/test_mcp_protocol.py)). Important safety details are implemented: `wiki_read_page` is path-traversal guarded and allowlisted, `wiki_search`/`wiki_query` have per-file and aggregate byte caps, and MCP `wiki_sync` defaults to dry-run unless `confirm=true` is supplied ([llmwiki/mcp/server.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/llmwiki/mcp/server.py), [tests/test_mcp_read_page_allowlist.py](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/tests/test_mcp_read_page_allowlist.py)).

## Artifact analysis

- **Storage substrate:** `model-weights` — Python modules under `llmwiki/adapters/` and `llmwiki/convert.py`, plus user config and state files such as `examples/sessions_config.json` and `.llmwiki-state.json`
- **Representational form:** `prose` `symbolic` — prose Markdown, docs, prompts, and wiki pages plus symbolic code, config, frontmatter, links, JSON, indexes, manifests, and lint/lifecycle rules
- **Lineage:** `authored` `imported` `trace-extracted` — authored implementation, instructions, wiki edits, and validators; imported opt-in user content and static exports; trace-extracted raw sessions and distilled wiki pages
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — pages and exports act as knowledge; commands, skills, adapters, MCP tools, lint, lifecycle, candidates, caps, search, graph, and trace distillation instruct, enforce, route, validate, rank, and learn from traces

**Adapter registry and conversion rules.** Storage substrate: Python modules under `llmwiki/adapters/` and `llmwiki/convert.py`, plus user config and state files such as `examples/sessions_config.json` and `.llmwiki-state.json`. Representational form: symbolic code/config, with prose comments and docs. Lineage: authored implementation plus adapter-specific schema assumptions; state entries derive from source file mtimes and adapter names. Behavioral authority: system-definition artifacts for routing which traces enter the raw layer, how project slugs are assigned, which records are filtered, what is redacted, and whether a source is treated as AI-session material or opt-in user content.

**Raw session Markdown.** Storage substrate: filesystem files under `raw/sessions/`, optionally under a vault overlay path when `--vault` is used. Representational form: prose Markdown with symbolic YAML frontmatter for project, slug, time, model, tools, counts, sub-agent status, and source path. Lineage: trace-extracted from local JSONL/session/export files through an adapter and converter; source file mtime state determines idempotency; existing raw files are not overwritten without `--force`. Behavioral authority: knowledge artifacts as preserved evidence for later ingest, query, build, exports, and audit. Raw files are intentionally not trusted as the final distilled wiki layer.

**Wiki pages and navigation files.** Storage substrate: Markdown under `wiki/`: source pages, entities, concepts, syntheses, comparisons, questions, projects, index, overview, log, hints, hot caches, `MEMORY.md`, `SOUL.md`, and `CRITICAL_FACTS.md`. Representational form: mixed prose and symbolic frontmatter/wikilinks. Lineage: LLM- or agent-authored from raw traces, manual edits, candidates, or synthesis backends; index/log/overview updates are part of slash-command and pipeline workflows. Behavioral authority: mostly knowledge artifacts for future agents and humans; some files become weak system-definition artifacts when an agent follows `CLAUDE.md`/`AGENTS.md` instructions to read them before ingest/query or treats `CRITICAL_FACTS.md`/`MEMORY.md` as navigation guidance. Effective authority depends on the host agent actually loading those files.

**Synthesis state and pending prompts.** Storage substrate: `.llmwiki-synth-state.json`, `.llmwiki-pending-prompts/`, and generated `wiki/sources/<project>/<date>-<slug>.md` pages. Representational form: symbolic state JSON plus prose prompt files and Markdown output. Lineage: raw session Markdown is compared by mtime, passed through a prompt template, then either synthesized by dummy/Ollama or deferred to a running coding agent through a sentinel. Behavioral authority: system-definition authority for deduplication and workflow routing; synthesized source pages become knowledge artifacts that can later shape answers, entities, concepts, and summaries. The agent-delegate backend is a staged human/agent-in-the-loop distillation path, not an autonomous model service.

**Static site and AI exports.** Storage substrate: generated `site/` files, including HTML, `.txt`, `.json`, `llms.txt`, `llms-full.txt`, `graph.jsonld`, `sitemap.xml`, `rss.xml`, `robots.txt`, `ai-readme.md`, `manifest.json`, and search indexes. Representational form: mixed prose, HTML, JSON, JSON-LD, XML, and symbolic hashes/perf budgets. Lineage: compiled from raw sessions, wiki pages, metadata, wikilinks, and render/export code; regenerated by `llmwiki build`, `llmwiki graph`, `llmwiki export`, or `llmwiki all`. Behavioral authority: knowledge artifacts for humans and agents; search indexes and graph outputs have ranking/navigation authority because they decide what is discoverable first.

**MCP server and slash-command surfaces.** Storage substrate: `.claude/commands/`, `.claude/skills/`, `.claude-plugin/plugin.json`, and `llmwiki/mcp/server.py`. Representational form: mixed prose instructions, symbolic plugin manifest, and executable Python. Lineage: authored project instructions and code. Behavioral authority: system-definition artifacts for agent workflows. Slash commands tell a coding agent how to ingest/query/sync, while MCP tools expose pull/query/read/sync operations to an MCP client. The plugin manifest advertises a SessionStart hook, but the corresponding hook script is absent at this commit, so that push wiring is not verified from code.

**Lint, lifecycle, confidence, candidates, quarantine, and manifest artifacts.** Storage substrate: Python rule modules and generated/local JSON files such as `.llmwiki-quarantine.json`, `.llmwiki-queue.json`, build manifests, and archived candidate files. Representational form: symbolic rules/state plus prose reason files. Lineage: authored validators applied to current wiki/raw/site state; candidates derive from ingest and are promoted, merged, or discarded by explicit operator action. Behavioral authority: system-definition artifacts for validation, review routing, stale detection, lifecycle state, and operational audit.

Promotion path: llm-wiki has a clear trace-to-knowledge promotion path: local session traces -> immutable raw Markdown -> wiki source pages -> entities/concepts/syntheses/navigation -> static/MCP exports. It has weaker promotion from prose memory to hard enforcement. Candidates, lint, lifecycle, confidence, and raw immutability improve governance, but most behavior change still depends on an agent or user pulling and trusting the relevant page.

## Comparison with Our System

| Dimension | llm-wiki | Commonplace |
|---|---|---|
| Primary purpose | Turn personal coding-agent history into a wiki and static site | Build and operate typed agent-facing knowledge bases |
| Main source material | Local agent session transcripts and optional user content | Authored KB artifacts, source snapshots, reviews, notes, ADRs, instructions |
| Raw layer | Immutable `raw/sessions/*.md` derived from traces | Source snapshots and retained source/review artifacts |
| Distilled layer | `wiki/` source/entity/concept/synthesis pages | Typed collection artifacts with schemas, contracts, links, validation, reviews |
| Retrieval/read-back | Pull through slash commands, MCP tools, static exports, search, graph, index pages | Pull through `rg`, indexes, links, skills, validation/review workflows |
| Governance | Redaction, immutability guard, quarantine, lint, candidates, lifecycle, confidence, manifests | Collection contracts, type specs, deterministic validation, review gates, git history |

llm-wiki is closer to Commonplace than many memory systems because it is file-first, agent-operated, and explicit about the raw -> distilled separation. Its strongest contribution is operational breadth: it handles many agent transcript substrates, keeps the raw trace layer inspectable, exports machine-readable site artifacts, and provides MCP tools without introducing a database or embedding dependency.

The main divergence is type authority. Commonplace makes the artifact type, collection contract, validation surface, and review lifecycle central to interpretation. llm-wiki has frontmatter and lint, but the system's standing wiki pages are still looser: a source/entity/concept page can carry advice and claims without the same path-valued type contract or deterministic schema vocabulary that Commonplace uses.

The other divergence is activation. llm-wiki is excellent at making historical work searchable and exportable, but the implemented core does not decide that a memory is relevant before an agent acts. The README and plugin metadata mention SessionStart automation, pending queues, and hook installation, yet the code I found mainly converts/queues/syncs or exposes pull tools. I did not find a relevance-gated `UserPromptSubmit`-style path that injects selected memory into the agent's next prompt.

**Read-back:** `pull` — In the implemented core. Agents and users call `/wiki-query`, read files, use MCP `wiki_query`/`wiki_search`/`wiki_read_page`, browse static exports, or run sync/build commands; no current code path pushes relevance-matched memory into a receiving agent before action

### Borrowable Ideas

**Keep a hard raw/source layer for traces.** Commonplace already snapshots sources, but llm-wiki's raw immutability guard plus quarantine file is a useful operational pattern for trace ingestion. Ready now for any future Commonplace trace-ingest workflow.

**Use adapter contracts for external trace substrates.** A Commonplace trace system could borrow the base adapter split: discover source files, derive project/session scope, normalize records, and classify AI-session vs opt-in user content separately. Ready when Commonplace ingests agent traces directly.

**Expose AI-readable static siblings.** Per-page `.txt`/`.json`, `llms.txt`, `llms-full.txt`, `graph.jsonld`, and manifests are simple external-consumer affordances. Commonplace could borrow the idea for publishing selected KB surfaces without asking agents to scrape rendered HTML. Needs a publication use case first.

**Treat MCP as a bounded pull surface.** llm-wiki's MCP caps, read allowlist, dry-run default for sync, and twelve-tool division are worth copying if Commonplace ships an MCP server. Ready as design input; implementation should preserve Commonplace's stronger type/routing vocabulary.

**Use candidate quarantine for hallucination-prone page creation.** Commonplace already uses review gates, but a candidate subtree could help where automated entity/concept creation is expected to be noisy. Worth borrowing only for automatic artifact generation, not for normal authored notes.

**Do not borrow README-ahead-of-code drift.** The Auto Dream, SessionStart hook, and plugin hook claims are useful product ambitions, but Commonplace should keep advertised activation paths tied to installed code and tested behavior.

## Trace-derived learning placement

**Trace source:** `session-logs` `tool-traces` — coding-agent session histories, JSONL sessions, exports, local stores, and tool-bearing session records are converted into raw Markdown

**Learning scope:** `per-project` `cross-task` — retained pages are organized by project slug, adapter, local installation, and optional vault overlay, then reused across later query/read/export surfaces

**Learning timing:** `staged` — sync, synthesis/ingest, and build/export/graph compilation run after sessions or raw files already exist

**Distilled form:** `prose` `symbolic` — distilled wiki pages are prose Markdown with symbolic frontmatter, wikilinks, indexes, graph/search exports, and MCP/static export metadata

**Trace source.** llm-wiki qualifies as trace-derived learning because it derives durable retained artifacts from coding-agent traces. Qualifying traces include Claude Code JSONL sessions, Codex CLI JSONL sessions, Copilot/Cursor/Gemini/OpenCode-like local stores, ChatGPT exports, and optional Obsidian notes when explicitly enabled. The trace boundary is adapter discovery plus converter parsing.

**Extraction.** The first extraction step is deterministic conversion: records are normalized, redacted, filtered, summarized into Markdown sections, and tagged with frontmatter and metrics. The second step is distillation into `wiki/` pages. That second step may be manual agent work following `CLAUDE.md`/`AGENTS.md`, dummy test output, local Ollama synthesis, or the agent-delegate pending-prompt flow. The oracle is therefore mixed: code for conversion safety and idempotency; LLM/agent judgment or operator review for wiki-page content.

**Four-field placement.** Raw session Markdown is a trace-extracted filesystem knowledge artifact with preserved source lineage and immutability protection. Wiki source/entity/concept/synthesis pages are trace-derived prose/symbolic knowledge artifacts with stronger navigation authority through indexes, wikilinks, graph/search exports, and MCP query results. Slash-command instructions, adapter code, lint rules, lifecycle rules, and MCP manifests are system-definition artifacts that route, validate, or expose those retained memories.

**Scope and timing.** Scope is local installation, project slug, adapter, and optional vault overlay. Timing is staged: sync converts traces after sessions exist; synthesis/ingest runs after raw creation; build/export/graph compile read-back surfaces later. SessionStart hook automation is documented and manifest-advertised, but not verified as an installed hook implementation in this checkout.

**Survey placement.** llm-wiki sits in the trace-to-wiki family. It strengthens the survey claim that raw trace retention is not enough: durable behavior-shaping value comes after a distillation boundary into source/entity/concept/synthesis pages and after those pages are reachable through explicit query/read surfaces.

## Curiosity Pass

**The README is ahead of the code in several authority-sensitive places.** The README says Auto Dream consolidates `MEMORY.md`, but the inspected code only seeds `MEMORY.md` text and system-page lists. The plugin manifest declares `hooks/session-start.sh`, but no such file appears in the checkout. Those differences matter because they would change both trace-derived timing and read-back direction if implemented.

**The system is strongest before the LLM step.** Adapter discovery, raw write guards, redaction, state keys, quarantine, path caps, search caps, manifest hashes, and MCP allowlists are concrete. The quality of synthesized wiki pages depends more on the active agent workflow than on an intrinsic verifier.

**The MCP server is intentionally not a memory-injection system.** It is a useful query/read/export surface, and `wiki_query` reads `index.md` and `overview.md`, ranks matches, and returns snippets. From the receiving agent's perspective, though, memory arrives only after an explicit tool call.

**`hot.md`, `MEMORY.md`, and `CRITICAL_FACTS.md` are attractive names but weak implemented authority.** They are scaffolded navigation files; I did not find current code that maintains `hot.md` or consolidates `MEMORY.md` automatically. They should be treated as authored or seeded guidance, not as verified adaptive memory.

**The candidate workflow is a real governance improvement.** Moving noisy generated entities/concepts through `wiki/candidates/` before promotion is a simple way to avoid treating every LLM-created page as trusted memory.

**The package name differs from the repo name.** `pyproject.toml` publishes `llm-notebook` while the CLI/module is `llmwiki` and the repository is `llm-wiki` ([pyproject.toml](https://github.com/Pratiyush/llm-wiki/blob/06c30e2b0c9018b11463b4fa37de0d75248cde5c/pyproject.toml)). That is not a memory-design issue, but it can affect adoption and connector setup.

## What to Watch

- Whether a real SessionStart hook implementation lands and whether it only syncs/queues traces or also pushes selected wiki memory into agent context.
- Whether Auto Dream becomes executable code that consolidates `MEMORY.md`; that would create a stronger trace-derived distilled memory artifact.
- Whether the agent-delegate synthesis path gets a review/verification loop before pages leave pending/candidate state.
- Whether `wiki_query` evolves from lexical pull into relevance-gated pre-action injection; that would change the read-back decision.
- Whether frontmatter/type validation becomes strong enough that source/entity/concept/synthesis pages gain Commonplace-like typed authority.
- Whether static AI exports are consumed by external agents often enough to justify stronger freshness and invalidation metadata.

## Bottom Line

llm-wiki is a real trace-derived agent memory system, but not a push-activation system at this commit. Its most valuable design is the explicit raw trace -> distilled wiki -> static/MCP export pipeline, backed by local files and pragmatic safety guards. For Commonplace, the borrowable pieces are adapterized trace ingestion, raw immutability, bounded pull surfaces, candidate quarantine, and machine-readable exports; the part to avoid is letting product documentation imply behavior-shaping automation before the code and tests make that authority real.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: llm-wiki turns local coding-agent traces into durable raw Markdown and distilled wiki pages.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - exemplifies: llm-wiki stores and exposes memory well, but current read-back is explicit pull.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: llm-wiki separates raw traces, distilled pages, indexes, exports, MCP tools, and governance state by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: raw sessions, wiki pages, static exports, and MCP query results mostly act as evidence, context, and reference.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: adapters, slash commands, skills, lint rules, lifecycle rules, MCP schemas, and build/export code route or govern future behavior.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: trace material is converted and distilled into reusable memory artifacts rather than only stored as opaque logs.
