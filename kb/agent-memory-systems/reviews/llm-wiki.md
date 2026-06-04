---
description: "nvk llm-wiki review: multi-runtime agent wiki manager with Markdown topics, generated indexes, lint/archive helpers, and lesson capture"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-06-02"
---

# LLM Wiki (nvk)

LLM Wiki, by nvk, is a multi-runtime agent-operated wiki protocol and plugin package. At the reviewed commit it ships a Claude Code plugin as the behavioral source of truth, generated Codex and OpenCode mirrors, a portable `AGENTS.md`, deterministic local helpers, and tests for plugin structure, sync drift, runtime packaging, and wiki lint behavior. Its memory model is file-native: agents ingest raw sources, compile topic-scoped Markdown articles, maintain derived indexes, query those articles by reading selected files, and can extract session lessons back into the wiki.

**Repository:** https://github.com/nvk/llm-wiki

**Reviewed commit:** [7e9bd0adf0eb91962856aa0e683a2d4822b90875](https://github.com/nvk/llm-wiki/commit/7e9bd0adf0eb91962856aa0e683a2d4822b90875)

**Last checked:** 2026-06-02

## Core Ideas

**A topic wiki is the memory boundary.** The central structure is a lightweight hub with `wikis.json`, `_index.md`, `log.md`, and `topics/`, where each topic wiki owns its own `raw/`, `wiki/`, `inventory/`, `datasets/`, `output/`, logs, and indexes. The source-of-truth behavior is described in `claude-plugin/skills/wiki-manager/SKILL.md`, mirrored in the portable `AGENTS.md`, and supported by reference files such as `wiki-structure.md`, `indexing.md`, and `hub-resolution.md` ([SKILL.md](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/claude-plugin/skills/wiki-manager/SKILL.md), [AGENTS.md](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/AGENTS.md), [wiki-structure.md](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/claude-plugin/skills/wiki-manager/references/wiki-structure.md)).

**Agents are both compiler and query engine.** Source documents are ingested into immutable `raw/`, then compiled into interconnected `wiki/` articles with frontmatter, sources, confidence, volatility, and dual Obsidian/Markdown links. Query commands navigate indexes, read selected articles, optionally search raw sources, and synthesize an answer from wiki content only ([ingest.md](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/claude-plugin/commands/ingest.md), [compile.md](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/claude-plugin/commands/compile.md), [query.md](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/claude-plugin/commands/query.md)).

**Context efficiency comes from topic isolation and staged disclosure.** The system keeps unrelated subjects in separate topic wikis, makes `_index.md` a derived cache for navigation, tells agents to read indexes before article bodies, supports quick/standard/deep query depths, skips archived topics by default, and uses lazy optional layers for inventory and datasets. It does not put the whole wiki into an agent prompt; it narrows context by topic, index rows, selected articles, grep matches, and explicit depth flags ([query.md](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/claude-plugin/commands/query.md), [indexing.md](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/claude-plugin/skills/wiki-manager/references/indexing.md), [archive.md](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/claude-plugin/commands/archive.md)).

**The behavior layer is packaged for several agent runtimes.** `claude-plugin/` is the primary distribution target; `plugins/llm-wiki/` is a generated Codex plugin mirror with `agents/openai.yaml`; `plugins/llm-wiki-opencode/` is a generated OpenCode/Pi mirror; and scripts synchronize runtime-specific wording while preserving the same reference corpus. Tests fail when generated mirrors drift from the Claude source ([README.md](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/README.md), [sync-codex-plugin.sh](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/scripts/sync-codex-plugin.sh), [test-codex-sync.sh](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/tests/test-codex-sync.sh), [test-opencode-sync.sh](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/tests/test-opencode-sync.sh)).

**Governance is partly symbolic and partly agentic.** The deterministic `scripts/llm-wiki` helper resolves hubs, lints frontmatter and placement, checks links and source provenance, repairs indexes, and archives/restores whole topics. The Claude command layer adds research, audit, librarian, thesis, planning, output, collection, and lesson workflows that still depend on the agent following Markdown instructions ([scripts/llm-wiki](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/scripts/llm-wiki), [audit.md](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/claude-plugin/commands/audit.md), [librarian.md](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/claude-plugin/commands/librarian.md)).

**Lessons learned make session experience durable.** `/wiki:ll` scans the current session for error-fix patterns, user corrections, discoveries, configuration changes, and gotchas, writes structured `type: lessons-learned` notes under `raw/notes/`, optionally appends rules to relevant articles, and can suggest `CLAUDE.md`/`AGENTS.md` rule additions. That is a real trace-derived path, not only ordinary source ingestion ([ll.md](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/claude-plugin/commands/ll.md)).

## Artifact analysis

- **Storage substrate:** `files` — Markdown files in a hub or project-local `.wiki/`, organized under `raw/`, `wiki/`, `inventory/`, `datasets/`, `output/`, `.audit/`, `.librarian/`, and logs
- **Representational form:** `prose` `symbolic` — prose wiki articles, raw notes, reports, and command instructions plus symbolic YAML frontmatter, JSON registries/state, path conventions, directory placement, links, helper code, and tests
- **Lineage:** `authored` `imported` `trace-extracted` — plugin instructions and helpers are authored, raw sources are imported, and lesson/session state is extracted from agent sessions and workflows
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — wiki content advises, command specs instruct and route, lint/tests can enforce and validate, indexes rank/navigation-scope reads, and lesson workflows learn from sessions

**Topic wiki files.** Storage substrate: Markdown files in a hub or project-local `.wiki/`, organized under `raw/`, `wiki/`, `inventory/`, `datasets/`, `output/`, `.audit/`, `.librarian/`, and logs. Representational form: prose plus symbolic YAML frontmatter, path conventions, directory placement, and dual links. Lineage: raw files are imported or session-derived source records; compiled articles are derived from raw sources; outputs, audit reports, and librarian reports are generated artifacts; indexes are regenerated views over file frontmatter. Behavioral authority: raw sources are knowledge artifacts; compiled articles advise future agents during query/plan/output workflows; indexes and frontmatter carry routing/ranking authority; command instructions and lint rules are system-definition artifacts.

**Plugin instructions and command specs.** Storage substrate: repository Markdown under `claude-plugin/commands/`, `claude-plugin/skills/wiki-manager/`, generated plugin mirrors, and portable `AGENTS.md`. Representational form: prescriptive prose with YAML frontmatter, command arguments, allowed tools, and workflow stages. Lineage: authored in the Claude source tree, mirrored into Codex/OpenCode by sync scripts, and checked by sync/validate tests. Behavioral authority: system-definition artifacts with instruction and routing force for agents that install or load the plugin.

**Generated indexes and registries.** Storage substrate: `_index.md` files throughout the hub/topic tree and `wikis.json` in the hub. Representational form: symbolic/prose tables and JSON registry records. Lineage: derived from file presence, frontmatter, topic registry entries, and archive status; invalidated by file moves, frontmatter edits, and archive/restore operations. Behavioral authority: ranking, navigation, and scope-selection authority. They shape what the agent reads first, but the files they summarize remain the source of truth.

**Session, research, audit, and librarian state.** Storage substrate: `.research-session.json`, `.thesis-session.json`, `.session-events.jsonl`, `.session-checkpoint.json`, `.audit/`, `.librarian/`, and report files inside a wiki. Representational form: structured JSON event/checkpoint state plus prose Markdown reports. Lineage: generated from multi-round research, audit scans, output dependency checks, truth escalation, and maintenance passes. Behavioral authority: knowledge artifacts for resume/audit and maintenance; some fields have routing or evaluation authority when future commands decide whether to resume, refresh, verify, or escalate.

**Lesson notes.** Storage substrate: `raw/notes/YYYY-MM-DD-ll-<slug>.md` in a target topic wiki, with optional appended article updates and suggested external rules. Representational form: structured prose lessons with category, context, symptom, root cause, fix, and rule fields. Lineage: trace-extracted from the current agent session and optionally promoted into compiled articles or human-approved instruction files. Behavioral authority: knowledge artifact as raw notes; advisory compiled knowledge after `/wiki:compile`; potential system-definition authority only if a human accepts suggested rules into `CLAUDE.md` or `AGENTS.md`.

**Deterministic helper and tests.** Storage substrate: `scripts/llm-wiki` and shell/Promptfoo tests under `tests/`. Representational form: symbolic Python and shell code, YAML test config, and golden/defect fixtures. Lineage: authored validation and packaging machinery, with fixtures generated for known wiki states. Behavioral authority: validation, repair, archive, and packaging quality authority; stronger than prose because it can fail builds or return nonzero lint status.

The main promotion path is source-to-article-to-output: external or session-derived material is captured as raw/source state, compiled into articles, then consumed by query, plan, research, output, audit, or lesson workflows. A second promotion path exists for lessons: trace-derived raw notes can become compiled articles, and suggested rules can move into agent instruction files if explicitly accepted. The weak point is that many promotions depend on an agent following command prose rather than a single enforced transaction.

## Comparison with Our System

| Dimension | LLM Wiki (nvk) | Commonplace |
|---|---|---|
| Primary purpose | Agent-managed topic wikis for research, querying, collection, audit, and output generation | Methodology KB for agent-operated knowledge bases, with typed notes, reviews, validation, and review gates |
| Canonical artifacts | Topic wiki Markdown, raw sources, compiled articles, indexes, logs, inventories, datasets, outputs | Typed Markdown notes, source snapshots, instructions, reviews, ADRs, generated indexes, review reports |
| Runtime surface | Claude plugin plus generated Codex/OpenCode mirrors and portable `AGENTS.md` | Repository conventions plus `commonplace-*` commands and local skills |
| Context efficiency | Topic isolation, derived indexes, query depths, archive exclusion, selected article reads | Collection contracts, curated/generated indexes, lexical search, type specs, skills, validation reports |
| Governance | Deterministic lint/archive helpers, sync tests, audit/librarian workflows, but many agentic writes | Schemas, validation, review runs, archived replacements, collection contracts, source snapshots |
| Trace learning | `/wiki:ll`, research events/checkpoints, audit provenance, optional article/rule promotion | Review/workshop traces can be captured, but promotion is usually explicit and review-gated |

LLM Wiki is closer to Commonplace than many memory systems because its retained artifacts are inspectable Markdown files with frontmatter, indexes, logs, and validation scripts. The largest difference is register and authority. LLM Wiki is an end-user wiki manager: it aims to help any agent build subject wikis and outputs. Commonplace is a methodology KB: it treats type specs, collection contracts, validation, source snapshots, and semantic review as first-class system-definition artifacts.

The multi-runtime packaging is a useful contrast. LLM Wiki keeps a Claude-first behavior layer and regenerates Codex/OpenCode mirrors with runtime-specific text patches. Commonplace currently installs skills and commands into consuming projects but does not have the same explicit generated-plugin mirror discipline.

**Read-back:** `pull` — Dominant and query/command-mediated; indexes, articles, and lessons re-enter action when an agent invokes or auto-activates the wiki skill and reads selected files, but the source does not implement an engineered relevance-gated memory push into an already-running receiving agent's context

The trace-derived path is real but deliberately file-mediated. Lessons learned are not hidden vector memories; they are raw notes and optional article/rule updates. That makes them reviewable, but also means quality depends on agent judgment and later compilation or human approval.

### Borrowable Ideas

**Generated runtime mirrors with drift tests.** Ready now. Commonplace skills could distinguish source-of-truth instructions from generated Claude/Codex/OpenCode packaging and add drift checks where runtime wording must differ.

**Topic archive lifecycle.** Ready with adaptation. LLM Wiki archives whole topic wikis under `topics/.archive/` and keeps archived content out of normal context. Commonplace could use a similar quiet-preservation pattern for retired workshops or superseded survey clusters.

**Session lesson command as a raw-source producer.** Worth borrowing, with stronger gates. A Commonplace analogue should write trace-derived lessons into a workshop or source layer first, then require review before promotion into instructions or durable methodology notes.

**Derived-index protocol as an explicit contract.** Ready now. LLM Wiki's insistence that indexes are caches over files matches Commonplace's generated indexes; documenting staleness checks and rebuild behavior at the command level would reduce ambiguity.

**Portable hub resolution rules.** Needs a concrete multi-machine use case. The `hub_path` versus `resolved_path` distinction is a practical answer for synced folders and sandboxed agents, but Commonplace's repo-local model currently avoids most of that complexity.

**Do not borrow unchecked agentic compilation wholesale.** LLM Wiki's ease of writing and updating articles is useful for personal wikis, but Commonplace should preserve type validation, source snapshots, and semantic review before high-authority knowledge changes.

## Trace-derived learning placement

**Trace source:** `session-logs` `event-streams` — `/wiki:ll` consumes the current session, while research and audit workflows persist `.session-events.jsonl` and checkpoint state.

**Learning scope:** `per-task` `per-project` `cross-task` — lesson capture starts from a session/workflow, is retained inside a target topic or project-local wiki, and can influence later wiki queries, articles, outputs, or accepted rules.

**Learning timing:** `online` `staged` — research/audit event state is written during workflows, while lesson extraction and promotion into articles or instructions are manually invoked and staged.

**Distilled form:** `prose` `symbolic` — extracted lessons become structured prose notes and optional article/rule updates with frontmatter, JSON state, and instruction-file changes.

**Trace source.** LLM Wiki qualifies as trace-derived because `/wiki:ll` consumes the current session: errors, fixes, user corrections, discoveries, configuration changes, and gotchas. Research and audit workflows also produce `.session-events.jsonl` and `.session-checkpoint.json`, giving later resume and audit commands durable traces of work performed.

**Extraction.** Lesson extraction is agentic and instruction-guided. The command asks the agent to scan the conversation, deduplicate events, generalize each lesson into a rule, write a structured raw note, optionally update relevant articles, and optionally suggest rule additions. The oracle is the acting agent plus any user approval for rule changes; no deterministic classifier verifies lesson quality.

**Four fields.** The raw stage is session/conversation/workflow trace material, retained as Markdown lessons or JSON event/checkpoint state. Its storage substrate is the wiki filesystem, representational form is prose plus symbolic frontmatter/JSON, lineage is trace-extracted or command-generated, and initial behavioral authority is knowledge artifact. Distilled outputs can become compiled articles with advisory authority, or suggested rules that only become system-definition artifacts if accepted into instruction files.

**Scope and timing.** `/wiki:ll` is per session and manually invoked. Research/audit session traces are per wiki and per workflow, written during multi-round research or audit. Promotion from raw lessons to compiled articles is staged and optional, not automatic on every query.

**Survey placement.** LLM Wiki sits in the trace-to-note and trace-to-rule-suggestion family. It strengthens the survey distinction between raw traces and durable behavior-shaping artifacts: the session itself is not the memory until it is extracted into a raw lesson, compiled article, checkpoint, report, or accepted instruction.

## Curiosity Pass

**The most important implementation is Markdown instruction, not Python.** The Python helper enforces structure, but the core compiler/query behavior lives in command specs and skill prose.

**Codex support is a generated skill, not a separate command system.** The Codex mirror rewrites Claude command language into `@wiki`/natural-language workflow guidance and includes `allow_implicit_invocation`; that broadens activation but still does not make wiki content automatically selected and injected.

**The portable `AGENTS.md` is both product and fallback.** It lets any agent run the protocol without installing a plugin, but its authority depends entirely on whether the host agent reads and follows it.

**The lesson workflow is more conservative than hidden memory.** It writes visible raw notes and suggests rules; it does not silently mutate the agent's startup instructions.

**Archive semantics matter for context quality.** Hiding archived topics by default is a context-efficiency choice, not just a file-management feature.

## What to Watch

- Whether `/wiki:ll` gains stronger provenance or review queues before lesson rules can update compiled articles or instruction files.
- Whether Codex/OpenCode mirrors remain generated-only as plugin packaging evolves; drift discipline is the feature to preserve.
- Whether query gains a relevance-gated pre-action read-back hook rather than explicit query/skill activation. That would change the `push-activation` decision.
- Whether deterministic lint expands from structure/provenance into stronger semantic checks for compiled articles.
- Whether session event/checkpoint provenance becomes a replayable audit input that can regenerate or verify outputs, not only summarize recent work.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - clarifies: LLM Wiki stores rich topic memory, but most read-back is still explicit query or skill-mediated pull.
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) - applies: topic isolation, indexes, archives, and query depths are all context-shaping mechanisms.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: LLM Wiki requires separating raw sources, compiled articles, indexes, logs, lesson notes, reports, and command specs by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: raw sources, compiled articles, session lessons, and reports advise later agents unless promoted into stronger channels.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: plugin skills, command specs, lint rules, sync scripts, and validation tests configure or constrain future agent behavior.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: `/wiki:ll` extracts lessons from session traces into durable raw notes and possible rules.
