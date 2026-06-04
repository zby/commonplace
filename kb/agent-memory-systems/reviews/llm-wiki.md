---
description: "LLM Wiki review: portable agent plugin that compiles source files into topic wikis, queryable through index-guided reads, audits, linting, and session lessons"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
status: current
last-checked: "2026-06-04"
---

# LLM Wiki (nvk)

LLM Wiki, from `nvk/llm-wiki`, is a portable agent protocol and plugin distribution for file-backed topic wikis. At the reviewed commit it ships a Claude Code source plugin, generated Codex and OpenCode/Pi mirrors, command wrappers, shared references, a portable `AGENTS.md`, and a deterministic Python helper for local lint/repair. The retained memory is ordinary Markdown-plus-frontmatter under a hub or project-local `.wiki/`; agents ingest immutable raw sources, compile synthesized wiki articles, query via indexes and grep, maintain inventory/datasets/output artifacts, run audits, and extract lessons from session traces.

**Repository:** https://github.com/nvk/llm-wiki

**Reviewed commit:** [7e9bd0adf0eb91962856aa0e683a2d4822b90875](https://github.com/nvk/llm-wiki/commit/7e9bd0adf0eb91962856aa0e683a2d4822b90875)

**Last checked:** 2026-06-04

## Core Ideas

**The behavior layer is an agent instruction set.** The central source of truth is `claude-plugin/skills/wiki-manager/SKILL.md`, which tells the host agent how to resolve the hub, route topic wikis, ingest sources, compile articles, query, lint, audit, collect, manage inventory and datasets, and append activity logs ([SKILL.md](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/claude-plugin/skills/wiki-manager/SKILL.md)). Commands such as `query.md`, `compile.md`, `ingest.md`, `audit.md`, and `ll.md` are pre-written task prompts with allowed tool surfaces rather than a conventional application API ([commands](https://github.com/nvk/llm-wiki/tree/7e9bd0adf0eb91962856aa0e683a2d4822b90875/claude-plugin/commands)).

**The wiki store is inspectable files, not a service database.** Topic wikis live under `HUB/topics/<name>/` or `.wiki/` and contain `raw/`, `wiki/`, `inventory/`, `datasets/`, `output/`, logs, indexes, and optional maintenance directories. Raw source files are immutable evidence; compiled wiki articles are synthesized Markdown with structured frontmatter, source references, confidence, volatility, and verification dates ([wiki-structure.md](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/claude-plugin/skills/wiki-manager/references/wiki-structure.md), [ingestion.md](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/claude-plugin/skills/wiki-manager/references/ingestion.md), [compilation.md](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/claude-plugin/skills/wiki-manager/references/compilation.md)).

**Context efficiency is index-first progressive disclosure.** Querying uses a 3-hop strategy: read the master `_index.md`, read category indexes, then read only matched article files; standard mode adds grep, deep mode expands to all indexes, relevant articles, raw sources, and sibling-wiki peeks ([indexing.md](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/claude-plugin/skills/wiki-manager/references/indexing.md), [query.md](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/claude-plugin/commands/query.md)). This keeps ordinary answers bounded to a few index files plus selected articles, but relevance and synthesis quality depend on the active agent following the protocol.

**Indexes are derived caches and lint is the migration path.** The system treats Markdown files and frontmatter as source of truth; `_index.md` files are rebuilt when stale. `scripts/llm-wiki` implements local deterministic lint checks for structure, frontmatter, canonical placement, links, source provenance, tags, coverage, freshness, and project shape, with selected `--fix` repairs such as moving misplaced files and regenerating indexes ([scripts/llm-wiki](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/scripts/llm-wiki), [linting.md](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/claude-plugin/skills/wiki-manager/references/linting.md), [test-local-cli-lint.sh](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/tests/test-local-cli-lint.sh)).

**Trust machinery is explicit but partly prompt-mediated.** Articles carry confidence and volatility metadata; librarian scans score staleness and quality into `.librarian/scan-results.json`; audit can follow output dependency chains, re-read sources, escalate to fresh research, and write `.audit/` reports plus session provenance files ([librarian.md](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/claude-plugin/skills/wiki-manager/references/librarian.md), [audit.md](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/claude-plugin/skills/wiki-manager/references/audit.md)). Deterministic lint checks structure and provenance links; semantic claims still rely on agent execution and optional web research.

**Adoption is runtime-portable.** The README and sync scripts make Claude Code the behavioral source, then mirror the same wiki skill and references into Codex and OpenCode/Pi packaging, with tests checking plugin manifests and mirror drift ([README.md](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/README.md), [sync-codex-plugin.sh](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/scripts/sync-codex-plugin.sh), [sync-opencode-plugin.sh](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/scripts/sync-opencode-plugin.sh), [test-plugin-validate.sh](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/tests/test-plugin-validate.sh)).

## Artifact analysis

- **Storage substrate:** `files` `repo` — User memory persists as Markdown files, JSON registries, logs, generated reports, indexes, and optional assets in hub/topic/project directories; the shipped behavior layer itself is a git repo with plugin manifests, command prompts, skills, references, scripts, and tests.
- **Representational form:** `prose` `symbolic` — Raw sources, compiled articles, lessons, reports, and command/skill instructions are prose; frontmatter fields, `wikis.json`, directory layouts, `_index.md` tables, plugin manifests, command metadata, lint enums, session JSON/JSONL, and source paths are symbolic. I did not find vector, graph, or model-weight retention in the reviewed repo.
- **Lineage:** `authored` `imported` `trace-extracted` — Plugin instructions, references, tests, and wiki articles can be authored by agents/humans; ingested URLs/files/repos/collections become imported raw sources; `/wiki:ll`, research session registries, audit events, checkpoints, and conversation-compiled articles derive durable artifacts from session traces.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `enforcement` `ranking` `learning` — Raw and compiled wiki files advise as knowledge; the skill and command files instruct host agents; hub resolution, topic flags, indexes, tags, source paths, inventory records, datasets, and project scopes route work; lint/audit/librarian rules validate and sometimes enforce stops or repairs; index summaries, grep hits, freshness/confidence fields, and agent judgment rank reads; lessons and compilation convert experience or imported sources into later knowledge.

**Source files and compiled articles.** `raw/` files preserve imported material with metadata and are not supposed to be modified after ingestion; `wiki/` articles synthesize and cross-reference multiple sources, carry `sources:` or `compiled-from:` frontmatter, and become the primary material read during query and compile operations ([ingestion.md](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/claude-plugin/skills/wiki-manager/references/ingestion.md), [compilation.md](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/claude-plugin/skills/wiki-manager/references/compilation.md)).

**Operational indexes and logs.** `_index.md` files are derived navigation caches, while `log.md` is append-only operational history. The cache/source distinction is explicit: stale indexes should be regenerated from actual files, so concurrent writes converge even when index updates race ([indexing.md](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/claude-plugin/skills/wiki-manager/references/indexing.md), [SKILL.md](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/claude-plugin/skills/wiki-manager/SKILL.md)).

**Maintenance reports and deterministic lint state.** `.librarian/`, `.audit/`, `.session-events.jsonl`, and `.session-checkpoint.json` hold diagnostic and provenance artifacts; `scripts/llm-wiki` provides deterministic validation/repair over the same file tree. Those reports are system-definition artifacts when later commands reuse them to route scans, assess trust, or resume work.

**Runtime packaging.** The Claude skill is the source behavior artifact; Codex and OpenCode mirrors copy or transform it for other agents. The sync and validation scripts make distribution drift a tested packaging property, not just a documentation claim.

Promotion path: LLM Wiki promotes external source material from `raw/` into synthesized `wiki/` articles, promotes catalog/research outputs into inventory/datasets or raw sources only when the workflow calls for it, and promotes session lessons into `raw/notes/` plus optional article appendices. It has stronger structural promotion than semantic promotion: frontmatter, paths, lint, and source links can be checked deterministically, while whether a synthesized article is faithful remains mostly agent- and audit-mediated.

## Comparison with Our System

LLM Wiki and Commonplace share the basic premise that Markdown files, frontmatter, indexes, and agent instructions can form an operative memory system. Both prefer inspectable artifacts over hidden service state, and both separate source material from synthesized knowledge. LLM Wiki is oriented toward end-user topic wikis and agent-operated research: it gives users slash commands, installation packaging, Obsidian-compatible links, topic hubs, collection ingestion, output generation, and local lint repair. Commonplace is more explicitly a methodology KB: it has typed collection contracts, stronger review vocabulary, and standing validation around artifact classes.

The main divergence is authority. Commonplace treats durable library artifacts as typed, reviewed, and validated knowledge objects. LLM Wiki gives more authority to the active host agent: the same instruction set tells the agent how to fetch, judge, synthesize, update, and answer. That makes LLM Wiki easier to install into Claude/Codex/OpenCode workflows, but it also means many quality guarantees are only as strong as the current agent's adherence to the prompt. Its deterministic helper covers structure, source links, freshness, placement, and indexes; it does not independently verify article truth or retrieval usefulness.

LLM Wiki's context model is closer to Commonplace than database-backed memory systems: read indexes first, then selected files, then deeper search only when needed. Its topic-wiki hub and archive lifecycle are more productized than Commonplace's review collection, while Commonplace's type specs and matrix tokens are more precise for cross-system comparison.

### Borrowable Ideas

**Topic hub plus portable paths.** Ready now as design vocabulary. Commonplace could borrow the `<HUB>/topics/<slug>` and portable `hub_path` discipline for multi-KB installs, especially where shared folders move across machines.

**Derived indexes as a concurrency contract.** Already aligned with Commonplace, but LLM Wiki's explanation is crisp: files and frontmatter are source of truth, indexes are caches, and read-time rebuilds resolve races.

**Lint as migration.** Worth borrowing carefully. Commonplace already validates, but LLM Wiki's "schema evolution is encoded as lint aliases and placement rules" is a practical way to avoid one-off migrations when file layout changes.

**Command prompts as packaged workflows.** Useful for installation UX. Commonplace skills are powerful, but LLM Wiki's thin slash-command wrappers make invocation and allowed-tool boundaries more legible to users.

**Do not borrow silent semantic authority.** LLM Wiki can compile and update articles directly from agent judgment. Commonplace should keep stronger review gates before generated synthesis becomes durable methodology.

## Write side

**Write agency:** `manual` `automatic` — Humans and agents manually trigger commands, author wiki files, approve choices, and edit artifacts; automatic and protocol-driven paths ingest source files, compile/update articles, rebuild indexes, append logs, lint/repair structure, create reports, write session provenance, archive/restore topics, collect catalogs, and extract lessons from the active session.

**Curation operations:** `consolidate` `dedup` `synthesize` `invalidate` `promote` — Compilation consolidates raw sources into fewer synthesized articles; collection ingest and lint define deduplication keys, source-reference repair, and canonical placement; compile/research/collect produce new synthesized wiki articles or output catalogs from multiple sources; audit, archive, retract, stale-session warnings, source provenance checks, and coverage reports mark stale, archived, broken, or unresolved state; lessons, inventories, datasets, and approved outputs promote temporary observations or candidates into more durable wiki surfaces. These operations are mostly instruction-mediated agent workflows, with deterministic backing for lint/structure.

### Trace-derived learning

**Trace source:** `session-logs` `event-streams` — `/wiki:ll` scans the current conversation for errors, fixes, user corrections, discoveries, configuration changes, and gotchas, then writes a structured raw lesson note. Research and audit also preserve `.session-events.jsonl`, `.session-checkpoint.json`, and session registry files for replay/resume/audit provenance ([ll.md](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/claude-plugin/commands/ll.md), [research-infrastructure.md](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/claude-plugin/skills/wiki-manager/references/research-infrastructure.md), [audit.md](https://github.com/nvk/llm-wiki/blob/7e9bd0adf0eb91962856aa0e683a2d4822b90875/claude-plugin/skills/wiki-manager/references/audit.md)).

**Learning scope:** `per-project` — Lessons target an active topic wiki or project-local `.wiki/`; they can later be compiled into articles for that wiki, and `--rules` can propose CLAUDE.md/AGENTS.md additions, but those rule edits are not automatic.

**Learning timing:** `online` `staged` — Lesson extraction runs during or at the end of the current session; dry-run and article update stages make promotion staged rather than silent. Research/audit provenance is appended during those workflows and reused later for resume or trust analysis.

**Distilled form:** `prose` `symbolic` — Distilled lesson notes are prose with symbolic frontmatter (`type: lessons-learned`, `source: session`, `lesson_count`, tags, confidence) and optional article backlinks or rule proposals.

**Extraction.** The oracle is the active agent following the command prompt: it identifies lesson-worthy patterns from the conversation, deduplicates them, writes structured Markdown, and may append a lesson rule to relevant wiki articles. The code does not implement an independent parser over transcripts; the trace-learning behavior is carried by the installed command/instruction artifact.

**Scope and timing.** The trace-derived path is narrower than the source compiler. Most wiki knowledge comes from imported raw sources; session learning is specifically for "learned by doing" operational memory and session provenance.

**Survey fit.** LLM Wiki fits the trace-to-note family: session experience becomes durable prose knowledge, then can be compiled or proposed as instructions. It does not show automatic model-weight learning, embedding-ranker training, or autonomous long-run memory evolution.

## Read-back

**Read-back:** `both` — Agents can explicitly pull memory by reading/searching wiki files and indexes; command-triggered workflows also push selected retained wiki context into the answering/working agent through prescribed index reads, query protocols, resume briefings, and structural checks. Static plugin instructions are not counted as read-back.

**Read-back signal:** `coarse` `identifier` `inferred / lexical` `inferred / judgment` — Coarse command flows read the master index, wiki identity, recent activity, or status summaries; identifiers include `--wiki`, `--local`, topic names, category flags, tags, source paths, wikilinks, and inventory/dataset scopes; lexical inference comes from index-summary scans and grep; judgment inference comes from the host agent choosing relevant articles, sources, sibling wiki matches, and deep-query followups.

**Faithfulness tested:** `no` — The repo tests plugin shape, mirror sync, deterministic lint behavior, and command/runtime structure, but I did not find a with/without memory ablation or post-action audit proving that retrieved wiki context changed agent behavior faithfully ([tests](https://github.com/nvk/llm-wiki/tree/7e9bd0adf0eb91962856aa0e683a2d4822b90875/tests)).

**Direction edge cases.** `/wiki:query` is user-triggered, but from the answering agent's perspective the command requires wiki reads before answering; that is push-like read-back via a pull interface. MCP-style tool retrieval is not present here; the retrieval surface is mainly the host agent using `Read`, `Grep`, `Glob`, and `Bash` according to command prompts.

**Selection, scope, and complexity.** Quick mode uses indexes only; standard mode reads 3-8 article files and greps `wiki/`; deep mode reads more indexes, relevant articles, raw sources, and sibling wiki indexes. The system explicitly avoids reading full sibling articles unless asked, skips archived material by default, and uses topic sub-wikis to keep unrelated domains out of context. Actual precision, recall, and context dilution are not measured in code.

**Authority at consumption.** Query results are advisory evidence for an answer. Skill and command files have instruction authority over the host agent. Lint and compile self-validation can enforce stops or repairs for structural fields; audit/librarian reports advise trust and maintenance decisions but do not rewrite knowledge during scans.

**Other consumers.** Humans use the files directly, Obsidian can consume wikilinks, Claude/Codex/OpenCode/Pi consume the packaged instructions, shell users run `scripts/llm-wiki lint`, and future agents consume `_index.md`, logs, reports, session checkpoints, inventory records, and datasets.

## Curiosity Pass

**LLM Wiki is closer to a portable operating procedure than an app.** The "implementation" that matters is a durable instruction package plus tests that keep its runtime mirrors in sync.

**The central memory optimization is old-fashioned navigation.** It does not need embeddings to be useful: frontmatter, indexes, tags, categories, links, grep, and topic boundaries carry most retrieval work.

**The strongest deterministic code is governance, not synthesis.** The Python helper can repair structure and source references, but article creation and semantic integration remain agent-mediated.

**Trace-derived behavior is narrow but real.** `/wiki:ll` turns session experience into durable raw notes and optional article/rule updates, but this is not the same as mining every tool trace into future policy automatically.

**Archive is a context-control feature.** Archived topic wikis are preserved but excluded from normal query/compile/research flows, which is a simple way to reduce accidental context bleed.

## What to Watch

- Whether `scripts/llm-wiki` grows beyond lint into deterministic query, compile planning, or provenance graph extraction; that would shift authority from prompt protocol toward executable system definition.
- Whether article compilation gains source-span provenance or automated contradiction tracking strong enough to verify synthesized claims without re-reading whole sources.
- Whether `/wiki:ll` or session provenance starts recording exact machine-readable event traces rather than relying on the host agent's conversation memory.
- Whether Codex/OpenCode packaging remains behaviorally equivalent as runtime-specific wording patches accumulate.
- Whether future retrieval adds vector search or reranking; that would change read-back signals and add parametric retained state.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: LLM Wiki's file store is only activated when commands, ambient skill rules, indexes, or explicit reads bring it into context.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: LLM Wiki's raw files, compiled articles, indexes, command prompts, lint rules, and reports differ by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: raw sources, compiled articles, outputs, inventories, and reports mainly serve as evidence, reference, and context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: skills, command prompts, lint rules, plugin manifests, and validation checks shape future agent behavior directly.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: `/wiki:ll` converts current-session errors, fixes, corrections, and discoveries into durable lessons.
