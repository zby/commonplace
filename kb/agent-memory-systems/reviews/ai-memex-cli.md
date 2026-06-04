---
description: "ai-memex-cli review: Git-backed LLM wiki toolbox, installed agent skill, session distillation, coarse context bootstrap, and self-healing lint loops"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-06-03"
---

# ai-memex-cli

`ai-memex-cli`, from zelixag's `ai-memex-cli` repository, is an agent-native implementation of the LLM Wiki / Memex pattern: a file-backed Markdown knowledge base where raw sources, agent-generated wiki pages, indexes, logs, schema instructions, slash commands, and optional session-start context blocks are maintained through a CLI plus installed agent skill. The CLI is deliberately mechanical: it fetches sources, parses sessions, searches, validates frontmatter and links, installs prompts/skills, and spawns configured agent CLIs for semantic ingest or lint work rather than calling an LLM API directly.

**Repository:** https://github.com/zelixag/ai-memex-cli

**Reviewed commit:** [4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f](https://github.com/zelixag/ai-memex-cli/commit/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f)

**Last checked:** 2026-06-03

## Core Ideas

**The primary retained artifact is a user-owned Markdown vault.** The repo's default structure is `~/.llmwiki/` with `raw/`, `wiki/`, `index.md`, `log.md`, `AGENTS.md`, and a `.llmwiki/` operational subdirectory for config and daemon state; local project projections live under `<project>/.llmwiki/local/` ([README.md](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/README.md), [src/core/vault.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/core/vault.ts)). The design is explicitly anti-black-box: durable knowledge is inspectable Markdown plus frontmatter and wikilinks, while config and registries are JSON files.

**The CLI is the mechanical layer and external agents are the semantic layer.** `memex ingest`, semantic lint, agent-assisted fetch, and agent-assisted distillation build prompts and spawn a configured agent binary through the agent adapter; the CLI handles path resolution, prompt construction, streaming logs, and command execution ([src/commands/ingest.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/commands/ingest.ts), [src/commands/lint.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/commands/lint.ts), [src/core/agent-adapter.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/core/agent-adapter.ts), [src/utils/exec.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/utils/exec.ts)). This keeps the memory format model-neutral but makes the deployed behavior depend on host agents such as Claude Code, Codex, OpenCode, Gemini CLI, Aider, Cursor, or generic CLI agents.

**Context efficiency is handled by cheap lexical handles first, deeper files on demand.** The standing wiki context is not loaded wholesale by default. Search uses ripgrep or qmd over `wiki/` and `raw/`; `glob` copies a scored subset of global wiki pages into a disposable local vault; `inject` expands explicit `## @include` directives and optional keyword-selected pages; the installed `ai-memex` skill tells agents to load only the reference file for the active workflow ([src/commands/search.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/commands/search.ts), [src/commands/glob.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/commands/glob.ts), [src/commands/inject.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/commands/inject.ts), [templates/skills/ai-memex/SKILL.md](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/templates/skills/ai-memex/SKILL.md)). The main exception is `memex context install`, which pushes a bounded digest into an agent auto-loaded file at session start.

**Session traces can become raw sources for later wiki compilation.** The agent adapter records known session directories and file patterns for Claude Code, Codex, OpenCode, Gemini CLI, and Aider; `memex distill` can find the current or latest session, parse JSONL/JSON/text into structured Markdown with `source-type: session`, and place it under `raw/<scene>/sessions/` ([src/core/agent-adapter.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/core/agent-adapter.ts), [src/core/distiller.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/core/distiller.ts), [src/commands/distill.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/commands/distill.ts)). `ingest` then treats those session Markdown files as source documents to update durable wiki pages.

**The governance loop is mechanical lint plus optional agent repair.** Mechanical lint builds an index, finds orphans, broken wikilinks, and missing frontmatter, while semantic lint spawns an agent with the live vault schema and mechanical report so it can repair safe issues or file unresolved findings as a wiki page ([src/commands/lint.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/commands/lint.ts), [src/core/linker.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/core/linker.ts), [templates/AGENTS.md](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/templates/AGENTS.md)). `watch` wraps this into a file-triggered or periodic ingest-lint loop with a no-progress guard, daemon state, logs, and status files ([src/core/ingest-lint-loop.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/core/ingest-lint-loop.ts), [src/commands/watch.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/commands/watch.ts)).

**Adoption is packaged as agent-facing prompts and skills, not an MCP server.** `install-hooks` generates slash commands and, for Claude Code and Codex, installs the `ai-memex` skill files; it also appends Codex/generic AGENTS sections and emits agent-specific command files for OpenCode, Gemini CLI, Cursor, Aider, and Continue-style workflows ([src/commands/install-hooks.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/commands/install-hooks.ts), [templates/skills/ai-memex/SKILL.md](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/templates/skills/ai-memex/SKILL.md)). The integration surface is broad, but much of the semantic authority remains ordinary Markdown instruction interpreted by the host agent.

## Artifact analysis

- **Storage substrate:** `files` — The central retained state persists as filesystem Markdown and JSON: global vault files, local projection files, raw session Markdown, generated host instructions, config, context registry, watch logs, and status files.
- **Representational form:** `prose` `symbolic` — Wiki pages and skills are prose plus YAML frontmatter and wikilinks; CLI code, frontmatter schemas, generated prompts, JSON config, and daemon status are symbolic; no vector store, graph database, or model-weight memory is implemented in this checkout.
- **Lineage:** `authored` `imported` `trace-extracted` — Templates, schemas, prompts, and wiki pages are authored or agent-authored; raw sources are imported; session distillation produces trace-extracted raw Markdown that later ingest can promote.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — Raw files and wiki pages act as knowledge; skills, schemas, prompts, context blocks, validators, search/projection selection, no-progress guards, and staged session ingest can instruct, route, validate, rank, enforce, and learn into later wiki state.

**Global vault.** Storage substrate: a directory such as `~/.llmwiki/` or legacy `~/.llmwiki/global/`. Representational form: mixed Markdown, YAML frontmatter, wikilinks, and JSON config. Lineage: raw sources are imported or captured; wiki pages are agent-authored derived views; `index.md` and `log.md` are maintained summaries of the vault's state and operation history. Behavioral authority: raw files are knowledge artifacts and source-of-truth evidence; wiki pages are knowledge artifacts for query and maintenance, and can become soft system-definition artifacts when the vault schema or context block routes agents to consult them.

**Vault schema and installed skill.** Storage substrate: `AGENTS.md` / `CLAUDE.md` / `GEMINI.md` in the vault and `templates/skills/ai-memex/` when installed into agent-specific locations. Representational form: prose instructions plus YAML frontmatter and routed reference files. Lineage: authored templates copied or appended during init/install. Behavioral authority: system-definition authority when loaded by a host agent or inlined into an ingest/lint prompt; it defines page types, workflow rules, safety gates, and when the CLI should delegate semantic work.

**Raw captured sources.** Storage substrate: `raw/<scene>/` files written by `fetch`, copied from user inputs, or produced by session distillation. Representational form: Markdown with source frontmatter, plus retained source URLs, timestamps, and word counts for fetched pages. Lineage: imported from web pages, keyword search results, user files, or agent session traces; source changes do not automatically invalidate derived wiki pages except through future ingest/lint work. Behavioral authority: knowledge artifacts, not direct instructions, until `ingest` reads them and rewrites durable wiki pages.

**Wiki pages.** Storage substrate: `wiki/<scene>/<type>s/*.md`. Representational form: Markdown prose with YAML fields `name`, `description`, `type`, `scene`, optional tags/sources, and `[[wikilinks]]` ([src/core/schema.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/core/schema.ts), [src/core/wiki-index.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/core/wiki-index.ts)). Lineage: derived by agents from raw files, queries, lint reports, and prior wiki pages; `index.md`, search results, and context blocks are regenerated or refreshed from these files. Behavioral authority: knowledge artifacts for query and later maintenance; they become advisory context when pulled by search/inject or pushed through a context digest.

**Context bootstrap blocks.** Storage substrate: project host files such as `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, or `.cursor/rules/memex.mdc`, plus a registry at `~/.llmwiki/contexts.json`. Representational form: generated Markdown or Cursor MDC with marker delimiters and a JSON registry. Lineage: derived from current wiki index pages and optional scene manifests, refreshed by `context refresh` or after clean ingest-lint loops ([src/commands/context.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/commands/context.ts), [src/core/context-block.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/core/context-block.ts), [src/core/context-registry.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/core/context-registry.ts)). Behavioral authority: advisory push context at session start; the block can tell the agent where the vault is, list a digest, and suggest `memex search`/`inject`, but it is coarse and does not prove the agent used the memory.

**Session distillation artifacts.** Storage substrate: external agent session directories as trace sources, plus rendered `raw/<scene>/sessions/*.md` files inside the vault. Representational form: structured Markdown with `source-type: session`, timestamps, turn counts, source path, and user/assistant/tool-call summaries. Lineage: trace-extracted from JSONL/JSON/Markdown session stores; optional agent distillation can produce a more semantic raw document; later ingest can promote session lessons into wiki pages. Behavioral authority: raw session Markdown is a knowledge artifact; promoted wiki pages become durable knowledge artifacts, and any schema/skill edits derived from them would become system-definition artifacts if a maintainer accepts them.

**Mechanical validators and self-healing loop.** Storage substrate: TypeScript CLI code plus runtime `.llmwiki/watch.*` files. Representational form: symbolic code, structured lint reports, logs, and status JSON. Lineage: authored implementation, reports derived from current wiki files. Behavioral authority: validation/evaluation authority over frontmatter, orphans, and broken links; with `--with-semantic` or `watch`, lint reports become prompt inputs that can cause an external agent to edit the wiki.

**Promotion path.** ai-memex has a clear source-to-knowledge promotion path: captured raw files and session traces become raw Markdown, ingest compiles them into typed wiki pages, lint/watch can push repair prompts from mechanical reports, and context refresh can turn the resulting wiki index into session-start advisory context. The path crosses form and authority: imported evidence becomes derived prose knowledge, then selected summaries become prompt context.

## Comparison with Our System

| Dimension | ai-memex-cli | Commonplace |
|---|---|---|
| Primary purpose | End-user CLI and skill for maintaining a personal/team LLM wiki | Methodology KB and framework for agent-operated knowledge bases |
| Canonical substrate | User vault: raw files, wiki Markdown, schema files, config JSON, generated host prompts | Repository KB: typed Markdown collections, type specs, schemas, generated indexes, review artifacts |
| Semantic writer | External agent spawned or guided by CLI/skill | Current agent workflow plus Commonplace validation/review commands |
| Context efficiency | Search, globbed local projection, `@include` injection, skill references, bounded context digest | `rg`, indexes, collection contracts, links, skills, source snapshots, review bundles |
| Learning from traces | Session transcripts become raw session docs and can be ingested into wiki pages | Trace-derived work appears in reviews/workshops, but framework-level session mining is not core |
| Governance | Mechanical lint, semantic-lint agent, watch loop, schema instructions | Type contracts, deterministic validation, semantic gates, generated indexes, review lifecycle |

The strongest overlap is the belief that plain files can be behavior-shaping infrastructure. Both systems treat Markdown, frontmatter, links, instructions, logs, and generated indexes as inspectable retained artifacts that later agents can consume. ai-memex is more productized for user adoption: it installs slash commands, supports multiple host agents, fetches web material, parses sessions, and offers a daemonized self-healing loop. Commonplace is more explicit about collection-local contracts, type-level schemas, review gates, outbound link semantics, and artifact authority.

ai-memex's largest tradeoff is that its semantic layer is deliberately outside the CLI. That makes it portable across agents and avoids a metered API dependency, but the quality of ingest, contradiction handling, and semantic lint is only as good as the host agent and prompt. The code can verify file shape and link health; it cannot verify that a generated wiki page faithfully represents its raw source unless a later agent or human reviews it.

**Read-back:** `both` — Retained memory returns by pull through `memex search`, `memex inject`, direct wiki reads, and local projections, and by coarse push when `memex context install` writes a vault digest into auto-loaded host files. The push path is not instance-targeted or faithfulness-tested in the reviewed code, so this review does not add `push-activation`.

**Read-back signal:** `coarse` — The only push path described here is the session-start context digest written into auto-loaded host files, not instance-targeted selection.

**Read-back timing:** `pre-action` — The context block is loaded at session start before the receiving agent acts.

**Faithfulness tested:** `no` — The reviewed prose says the coarse push path is not faithfulness-tested in the code.

### Borrowable Ideas

**A context block as a managed generated region.** Commonplace could use marker-delimited generated regions for selected project-level context exports, especially when a consuming project wants a small current digest without loading the whole KB. Ready as an export pattern; it needs clear ownership so generated text does not compete with hand-authored AGENTS instructions.

**Session traces as raw sources, not immediate rules.** ai-memex's safest trace path is to render sessions into raw Markdown first, then let ingest decide what deserves durable wiki promotion. Commonplace could borrow this as a conservative session-mining workflow. Ready now for workshop experiments because it preserves trace lineage and review before authority upgrade.

**Mechanical lint reports as agent repair inputs.** The ingest-lint loop attaches structured issues to the next prompt rather than asking the agent to rediscover them. Commonplace already has review/validation reports; the borrowable part is using deterministic report deltas as the narrow input to a repair loop. Ready for bounded fixer workflows.

**Agent-neutral prompt packaging.** The adapter-plus-template approach lets one memory workflow target Claude Code, Codex, OpenCode, Gemini, Cursor, Aider, and generic agents. Commonplace skills could adopt the same separation between workflow semantics and host-specific installation formats. Needs a real distribution target before becoming core infrastructure.

**Keep local projections disposable.** `memex glob` makes project-local wiki copies explicitly generated and overwriteable. Commonplace's workshop or consuming-project projections could use the same warning pattern to prevent agents from treating convenience context as the durable source of truth. Ready for generated exports.

## Trace-derived learning placement

**Trace source:** `session-logs` `tool-traces` — Agent session stores provide user/assistant messages, timestamps, and named tool calls where available.

**Learning scope:** `per-project` `cross-task` — The trace loop is per vault and scene, with cross-session accumulation after durable wiki pages are written.

**Learning timing:** `staged` — Sessions are converted after the fact into raw material, then later ingested or lint-repaired.

**Distilled form:** `prose` `symbolic` — Session traces become Markdown raw documents and typed wiki pages with frontmatter, wikilinks, schemas, and possible schema/skill edits.

**Trace source.** ai-memex qualifies as trace-derived because configured agent session stores are first-class sources. The adapter knows paths and patterns for Claude Code, Codex, OpenCode, Gemini CLI, and Aider; `distill` can infer the current Codex session by environment or select the latest session file by modification time ([src/core/agent-adapter.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/core/agent-adapter.ts), [src/commands/distill.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/commands/distill.ts)). The raw signal is a conversation/session trace: user messages, assistant messages, timestamps, and named tool calls where available.

**Extraction.** The mechanical path parses JSONL/JSON/plain text, strips or summarizes tool-use structure, renders a Markdown session document with `source-type: session`, and writes it under `raw/<scene>/sessions/` ([src/core/distiller.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/core/distiller.ts), [src/commands/distill.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/commands/distill.ts)). The optional agent path asks a host agent to write a structured raw distillation with decisions, practices, patterns, code examples, open questions, and references. The oracle for semantic extraction is the external agent; the CLI supplies the prompt and destination.

**Scope and timing.** The trace loop is staged rather than online learning. A session is converted after the fact into raw material; `memex ingest` later compiles raw session material into typed wiki pages; `watch` can automate the raw-to-wiki and lint-repair loop when files appear. The scope is per vault and per scene, with cross-session accumulation only after the agent writes durable wiki pages.

**Survey placement.** This belongs in the trace-to-artifact family. Raw traces do not directly steer future actions; rendered session documents are knowledge artifacts, and later wiki pages or schema edits are the durable behavior-shaping artifacts. It strengthens the survey distinction between retaining traces and promoting distilled artifacts: the useful memory is not the JSONL log itself but the reviewed or at least schema-shaped wiki state derived from it.

## Curiosity Pass

**The most interesting read-back path is deliberately coarse.** `context install` pushes a digest into every new session, but the code does not implement instance-level memory targeting. The digest is useful orientation, not a relevance oracle.

**`memex inject --task` is advertised more strongly than the implementation I found.** The context block tells agents to run `memex inject --task "<current goal>"`, but the command implementation expands `@include` directives and optional `keywords`; I did not find code that turns `task` into selected pages in this checkout ([src/commands/inject.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/commands/inject.ts), [src/core/context-block.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/core/context-block.ts)).

**The system is agent-neutral but not agent-independent.** Ingest, semantic lint, agent-assisted fetch, and agent-assisted distill all depend on a host agent binary being installed and behaving well. The CLI can degrade or dry-run, but the semantic memory system is incomplete without an agent.

**The repository contains a memex block generated by its own tool.** `AGENTS.md` includes a marker-delimited context block pointing at a Windows vault and listing memex pages. That is a useful self-example of the session-start push path, but it is also a reminder that generated context can drift or expose local paths if committed accidentally.

**The no-progress guard is a practical governance detail.** The watch loop compares lint issue sets and stops when the same issues repeat, unless `--force` disables the guard. That is a small but important token-burn control for any agentic self-healing loop.

## What to Watch

- Whether `inject --task` becomes real task-conditioned selection rather than `@include` expansion plus explicit keyword matching; that would shift read-back from coarse/pull toward engineered relevance.
- Whether context bootstrap gains budgets, scene targeting, or faithfulness checks. Without them, session-start digest push remains useful but hard to trust as behavior-changing memory.
- Whether semantic lint writes durable review artifacts with provenance back to the mechanical report and agent prompt. That would make the governance loop auditable rather than just operational.
- Whether session distillation gains stable trace ids, source hashes, and promotion records tying raw sessions to derived wiki pages. That would improve invalidation and review of trace-derived artifacts.
- Whether the project narrows or formalizes the boundary between generated local projections and durable global wiki edits. The disposable projection rule is clear in templates, but host agents still need to obey it.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - compares: ai-memex turns agent sessions into raw Markdown sources and then into wiki artifacts through staged ingest.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: raw sources, wiki pages, schemas, skills, context blocks, lint reports, and daemon state have different storage, form, lineage, and authority.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: storing wiki pages is separate from pulling them by search or pushing a digest into agent context.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: raw sources, session documents, fetched pages, wiki pages, and lint reports mostly act as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: vault schemas, installed skills, generated slash commands, context blocks, and validators can instruct, route, validate, or constrain future behavior.
- [Frontloading spares execution context](../../notes/frontloading-spares-execution-context.md) - relates: generated context blocks and local projections precompute a small navigation surface before a new agent turn begins.
