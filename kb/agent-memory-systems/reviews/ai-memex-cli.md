---
description: "ai-memex-cli review: Git-backed Markdown vault, agent skill workflows, trace distillation, lint/watch loops, and context bootstrap"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-04"
tags: [trace-learning]
---

# ai-memex-cli

`ai-memex-cli`, by `zelixag/ai-memex-cli`, is a TypeScript CLI for maintaining a Karpathy-style LLM wiki: raw source material is kept in a Git-friendly Markdown vault, agents compile it into structured wiki pages, and the CLI supplies deterministic capture, search, lint, session parsing, installation, watch, projection, and context-bootstrap tools. The code at the reviewed commit keeps semantic judgment outside the CLI: agent prompts and installed skills do the meaning-making, while the CLI handles files, prompts, validation reports, and host-agent integration.

**Repository:** https://github.com/zelixag/ai-memex-cli

**Reviewed commit:** [4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f](https://github.com/zelixag/ai-memex-cli/commit/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f)

**Last checked:** 2026-06-04

## Core Ideas

**The memory substrate is a plain Markdown vault with raw and wiki layers.** `memex init` creates `raw/`, `wiki/`, `index.md`, `log.md`, and a vault schema file such as `AGENTS.md`; the seeded schema tells agents that raw files are immutable source documents and wiki pages are LLM-maintained entities, concepts, sources, comparisons, overviews, and syntheses ([src/commands/init.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/commands/init.ts), [templates/AGENTS.md](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/templates/AGENTS.md)). Vault resolution prefers an explicit path, then project-local `.llmwiki/local`, then legacy or flat `.llmwiki` roots, then `~/.llmwiki` ([src/core/vault.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/core/vault.ts)).

**The CLI is the mechanical toolbox; installed agents are the semantic writer.** `memex ingest` reads the live vault schema and index, builds a prompt, and invokes a configured agent with the vault as `cwd`; its comments explicitly say the CLI does not resolve fuzzy paths or write semantic wiki content itself ([src/commands/ingest.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/commands/ingest.ts)). The installed `ai-memex` skill repeats the split: management operations modify the wiki through CLI-spawned agents, while query/status use the current outer agent and CLI search/status primitives ([templates/skills/ai-memex/SKILL.md](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/templates/skills/ai-memex/SKILL.md)).

**Context efficiency is mostly symbolic and budgeted, not vector-based.** Search is lexical over `wiki/` and usually `raw/` using ripgrep/grep, optional `qmd`, scene/type filters, and a result limit; `memex inject` follows `## @include` directives from the vault schema and can add keyword-scored wiki pages; `memex glob` builds a project-local projection by scoring page names, ids, tags, and descriptions against project keywords ([src/commands/search.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/commands/search.ts), [src/commands/inject.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/commands/inject.ts), [src/commands/glob.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/commands/glob.ts), [src/core/globber.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/core/globber.ts)). Complexity is bounded by page selection and projection files, but there is no embedded model, graph database, or vector memory layer in this repo.

**Raw capture and session distillation preserve source lineage before wiki synthesis.** `memex fetch` stores cleaned web pages under `raw/<scene>/` with source URL, fetched timestamp, and word count; keyword mode uses DuckDuckGo Lite and URL mode uses Readability/Turndown ([src/commands/fetch.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/commands/fetch.ts), [src/core/fetcher.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/core/fetcher.ts), [src/core/searcher.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/core/searcher.ts)). `memex distill` can mechanically convert the current or latest agent session into structured Markdown under `raw/<scene>/sessions/`, recording source path, timestamps, turn count, roles, and tool-call names while dropping raw JSONL bytes from the vault ([src/commands/distill.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/commands/distill.ts), [src/core/distiller.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/core/distiller.ts)).

**Governance is a two-layer health loop.** The mechanical lint pass indexes Markdown pages, checks orphan pages, broken wikilinks, and required frontmatter fields, and returns a structured report; optional semantic lint spawns an agent with the live schema plus mechanical report to repair or file unresolved semantic findings ([src/commands/lint.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/commands/lint.ts), [src/core/wiki-index.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/core/wiki-index.ts), [src/core/linker.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/core/linker.ts), [src/core/schema.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/core/schema.ts)). `memex watch` can run `ingest -> lint -> ingest` loops on raw-file changes or periodic health checks, with status and log files for observability ([src/commands/watch.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/commands/watch.ts), [src/core/ingest-lint-loop.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/core/ingest-lint-loop.ts)).

**Adoption is through native agent surfaces, not MCP.** `install-hooks` writes slash prompts, command files, prompt aliases, project `AGENTS.md` sections, Cursor rules, and the `ai-memex` skill for Claude Code and Codex; `context install` separately writes a marker-delimited vault/digest block into project files such as `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, or Cursor rules ([src/commands/install-hooks.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/commands/install-hooks.ts), [src/commands/context.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/commands/context.ts), [src/core/context-block.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/core/context-block.ts)). This makes the system easy for existing coding agents to encounter, but shifts semantic reliability to prompt-following rather than an enforced API.

## Artifact analysis

- **Storage substrate:** `files` — Durable memory is stored as filesystem Markdown under global and project-local `.llmwiki` vaults, with generated agent prompts/skills/context blocks as files in host-agent config locations; the reviewed implementation is distributed as a Git-backed TypeScript package, but the operative memory substrate is files.
- **Representational form:** `prose` `symbolic` — Raw and wiki Markdown carry prose; frontmatter, scenes/types, wikilinks, `@include` directives, context registries, lint reports, prompt templates, and CLI command contracts provide symbolic structure.
- **Lineage:** `authored` `imported` `trace-extracted` — Wiki pages are authored by humans or agents, raw pages are imported from web/files/search results, and session Markdown is extracted from agent conversation files before later ingest.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` `learning` — Wiki/raw pages advise as knowledge; vault schemas, skills, slash prompts, and context blocks instruct; scenes/types/includes route; lint validates; search/glob score and rank; trace-distilled sessions feed later ingest.

**Vault raw and wiki files.** Storage substrate: Markdown files in `raw/`, `wiki/`, `index.md`, `log.md`, and schema files such as `AGENTS.md`. Representational form: prose plus symbolic frontmatter, wikilinks, scene/type directories, source metadata, and append-only log conventions. Lineage: raw files are imported or trace-extracted source material; wiki files are derived by an agent during ingest and invalidated by source changes, contradictions, lint findings, or manual edits. Behavioral authority: raw files are preserved evidence; wiki pages are knowledge artifacts when searched or cited, and can become instruction-like when included in a local `AGENTS.md` or context block.

**Vault schema and installed agent skill/commands.** Storage substrate: template files in the package and installed files under project/user agent config directories. Representational form: prose instructions plus symbolic command metadata and generated paths. Lineage: authored templates copied or appended by `install-hooks`. Behavioral authority: system-definition artifacts; they tell agents when to capture, ingest, query, distill, lint, and status-check, and they decide whether semantic work happens in the current session or a CLI-spawned sub-agent.

**Mechanical indexes, lint reports, and search/projection outputs.** Storage substrate: transient CLI outputs plus generated `local/` vault projections, context blocks, status files, watch logs, and `~/.llmwiki/contexts.json`. Representational form: symbolic JSON/status records and prose Markdown digests. Lineage: derived from current vault files, project keywords, raw-file events, and lint runs; stale projections are overwritten or refreshed. Behavioral authority: routing, validation, ranking, and context-budget authority because these artifacts decide which pages are surfaced to an agent, which issues drive repair prompts, and which projects receive refreshed bootstrap blocks.

**Session distillation artifacts.** Storage substrate: Markdown files under `raw/<scene>/sessions/`, usually `raw/team/sessions/` by default. Representational form: prose transcript excerpts plus symbolic frontmatter (`source-type: session`, `started`, `ended`, `turns`, `sources`) and role headings. Lineage: trace-extracted from configured agent session directories; no-argument distill chooses the current Codex thread when available or the newest session file, and skips rewriting if the destination is newer than the source. Behavioral authority: initially source evidence, then learning input when `memex ingest` turns session decisions, best practices, and open questions into durable wiki pages.

**Promotion path.** The intended path is raw source or session trace -> agent-authored wiki page -> index/log update -> search/inject/glob/context-block read-back -> lint/watch maintenance. The system can promote traces into durable wiki knowledge through an agent workflow, but the code does not implement a hard review gate that changes epistemic status from "captured" to "validated"; lint is mostly structural plus prompted semantic review.

## Comparison with Our System

| Dimension | ai-memex-cli | Commonplace |
|---|---|---|
| Primary purpose | Agent-operated personal/team LLM wiki for compounding knowledge | Methodology KB for agent-operated knowledge-base design |
| Main substrate | `.llmwiki` Markdown vaults, raw/wiki split, generated prompts/skills/context blocks | Git-tracked Markdown collections, type specs, source snapshots, reviews, generated indexes |
| Semantic writes | Delegated to host agents through prompts and installed skills | Written by agents under collection/type contracts, with deterministic validation and review workflows |
| Retrieval | `memex search`, `inject`, `glob`, context digest blocks, lexical/qmd/project-keyword selection | `rg`, authored indexes, links, collection contracts, validation/review reports |
| Trace use | Session files become raw Markdown and can be ingested into wiki pages | Trace-learning is analyzed and selectively used, not a default runtime capture loop |
| Governance | Mechanical lint, optional semantic lint agent, watch self-healing loop | Type schemas, collection contracts, semantic review gates, replacement archives, validation commands |
| Activation | Pull search/query plus optional project bootstrap blocks that push vault digests into agent files | Mostly deliberate pull through search/index/link/skill workflows |

The strongest alignment is the insistence on inspectable retained artifacts. Both systems prefer Markdown, source lineage, links, and agent-operable commands over opaque vector-only memory. ai-memex-cli is more adoption-oriented: it writes into Claude Code, Codex, Cursor, Gemini, OpenCode, Aider, Continue, and generic agent surfaces, while Commonplace stays closer to a repo-native methodology system.

The largest divergence is authority. Commonplace treats type specs, collection contracts, validation, review runs, and replacement archives as the governance spine. ai-memex-cli makes the vault schema and installed prompts the main authority, then delegates semantic correctness to whichever host agent runs the workflow. That is pragmatic and portable, but weaker when a claim needs durable review status or when an automatic watch loop could repeatedly ask an agent to repair ambiguous semantic issues.

ai-memex-cli also has a clearer session-capture loop than Commonplace. It can read configured agent session directories, render trace Markdown, and ingest that into the wiki. Commonplace can use traces during reviews or investigations, but it does not ship a default "distill current session into raw source" command.

### Borrowable Ideas

**Agent-native installation matrix.** Commonplace could expose small, generated prompt/skill entrypoints for common agents rather than relying only on repo instructions. Ready when there is a concrete supported surface; otherwise it risks multiplying stale prompt files.

**Raw session Markdown as source material.** A Commonplace analogue would save selected agent sessions into `kb/sources/` or a workshop raw layer with source path, timestamps, and turn counts before any note synthesis. Ready for review workflows where session provenance matters.

**Marker-delimited context bootstrap blocks.** The context block pattern is useful for project-local recall: a generated, replaceable region in `AGENTS.md` or `CLAUDE.md` can carry vault location and top entries without taking over the whole file. Needs a strict budget and governance rule before use in Commonplace.

**Mechanical lint report as repair prompt input.** ai-memex-cli's watch loop feeds the exact lint report into the next ingest pass. Commonplace already validates deterministically; a similarly small "repair from report" prompt could make fix loops more reproducible.

**Do not borrow autonomous self-heal by default.** `memex watch --daemon --heal` is useful but token-expensive and prompt-sensitive. Commonplace should keep autonomous maintenance opt-in and bounded by explicit review gates.

## Write side

**Write agency:** `manual` `automatic` — users and agents can author wiki pages, raw captures, logs, and generated command/config files; the CLI also automatically writes raw fetched pages, session Markdown, context registries, context blocks, local projections, watch status/logs, lint-driven prompts, and agent-spawned ingest/lint outputs.

**Curation operations:** `consolidate` `synthesize` — session distillation can compress a conversation into a raw Markdown source, and ingest/semantic-lint prompts ask agents to synthesize source material, comparisons, overviews, syntheses, contradictions, cross-references, and unresolved lint reports into wiki pages.

### Trace-learning

**Trace source:** `session-logs` — The implemented trace path reads agent session files from configured session directories, including Claude Code/Codex/OpenCode/Gemini/Aider-style stores.

**Learning scope:** `per-project` `cross-task` — Session traces land in the global vault by default and can be ingested into team or other scene pages that later tasks consult; local projections and context blocks can project selected global knowledge into projects.

**Learning timing:** `offline` `staged` — `memex distill` converts a current/latest or specified session after it exists, and ingest later turns the raw session source into wiki knowledge.

**Distilled form:** `prose` `symbolic` — The first-stage output is Markdown transcript/summary prose with symbolic frontmatter, source path, timestamps, turn count, and role headings.

**Trace source.** The strongest code-grounded trace path is `memex distill`: it resolves configured session directories, selects the current Codex thread or latest session where possible, parses JSONL/JSON session records, records tool-call names, and writes Markdown under `raw/<scene>/sessions/` ([src/commands/distill.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/commands/distill.ts), [src/core/distiller.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/core/distiller.ts), [src/core/agent-adapter.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/core/agent-adapter.ts)). It is not raw transcript copying: source JSONL stays outside the vault, and the durable retained artifact is rendered Markdown.

**Extraction.** No-argument distill is mostly structural extraction: parse turns, drop system-empty and some tool-result content, render roles, timestamps, source path, and tool-call names. The agent-mediated distill path builds a prompt that asks an agent to compress a conversation into a concise Markdown summary, but the CLI does not judge the quality of that summary itself ([src/commands/distill.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/commands/distill.ts), [src/core/distiller.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/core/distiller.ts)).

**Scope and timing.** Distillation is staged: first create a raw session source, then run ingest so an agent can extract decisions, final answers, best practices, snippets, and open questions into ordinary wiki pages. Watch mode can automate the subsequent ingest/lint loop, but it still depends on the configured host agent for semantic updates ([src/core/ingest-lint-loop.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/core/ingest-lint-loop.ts), [src/commands/watch.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/commands/watch.ts)).

**Survey placement.** On the [trace-learning survey](../trace-learning-techniques-in-related-systems.md), ai-memex-cli belongs in the trace-to-source-to-wiki family: traces become durable raw Markdown, then agent workflows synthesize wiki pages. It strengthens the survey split between raw trace preservation and distilled behavior-shaping artifacts because the first-stage session file is evidence, while the later wiki page or context block is what changes future behavior.

## Read-back

**Read-back:** `both` — Wiki memory is pulled through explicit `memex search`, `memex inject`, `memex glob`, and slash/skill query workflows, while `memex context install/refresh` can push a generated vault digest and wiki location into project agent files before a future session acts.

**Read-back signal:** `coarse` — The pushed context block is an always-loaded project/session bootstrap selected by installed host file and optional scene binding, not by the current user prompt's semantic content.

**Faithfulness tested:** `no` — I found no implemented ablation, perturbation test, or post-action audit proving that pushed digests or search results changed agent behavior.

**Direction edge cases.** Installed slash prompts and the `ai-memex` skill are baseline workflow instructions, so they do not by themselves count as memory read-back. The context block is different: it renders the current vault path, page counts, scene digest, top page ids/descriptions, and command reminders into an auto-loaded project file, and `refresh --all` can update those blocks from retained wiki state after clean ingest/lint cycles ([src/core/context-block.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/core/context-block.ts), [src/commands/context.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/commands/context.ts), [src/core/context-registry.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/core/context-registry.ts), [src/core/ingest-lint-loop.ts](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/core/ingest-lint-loop.ts)).

**Targeting and signal.** Pull retrieval can be keyword, qmd, scene/type filter, include directive, or project-keyword scoring. Push retrieval is coarse: an installed project file loads a bounded digest for that project/agent, and optional scene manifests add "when to consult" instructions, but the code does not infer relevance from the current task before the first model invocation.

**Selection, scope, and complexity.** Pull paths have explicit limits: search defaults to ten results; inject follows includes plus keyword-scored pages; glob uses a max page count from config; context digest lists a configurable number of top pages per scene. The complexity risk is that a context block can make the agent aware of the vault and a small digest even when irrelevant; actual dilution and uptake are runtime properties, not proven by source.

**Authority at consumption.** Search and inject results are advisory knowledge artifacts unless the host prompt treats them as stronger. Context blocks have prompt-context authority because they live in files such as `AGENTS.md`, `CLAUDE.md`, or Cursor rules, but they are still not hard gates. They instruct the agent to consult memory and show selected wiki entries; they do not enforce use or block actions.

**Faithfulness.** The repository includes tests for command behavior and helpers, but I did not find a behavioral faithfulness test that compares agent performance with and without memex read-back. The implemented mechanism is structurally real; effective behavioral use is not verified from code.

**Other consumers.** Humans can read the Markdown vault directly, edit pages, inspect diffs, run status/lint/search, and browse generated local projections. Those are important adoption surfaces but are consumer surfaces, not separate push directions.

## Curiosity Pass

The code is more conservative than the README's "maintained by agents" phrasing can sound. The CLI does not contain a hidden LLM writer or vector store; it packages prompts, validates structure, and delegates semantic work to whatever agent is installed.

The local vault is explicitly disposable. `memex glob` copies selected global wiki pages into `<project>/.llmwiki/local/` and writes an `AGENTS.md` with includes, but the template warns that durable writes belong in the global vault. That keeps project context cheap, but it creates a source-of-truth distinction agents must obey.

The watch loop is operationally strong and epistemically weak. It can keep trying until lint is clean and refresh context blocks afterward, but the semantic fixes are only as good as the spawned agent's prompt-following and the lint report.

Session distillation is the most distinctive memory-learning path. It is not automatic profile learning or skill patching; it is a source-capture lane that makes previous conversations ingestible as ordinary wiki evidence.

The system deliberately avoids MCP. That simplifies portability across agents with prompt files and skills, but loses the typed tool annotations and explicit tool metadata that MCP-based memory systems can expose.

## What to Watch

- Whether `memex context` adds task-inferred or query-inferred selection before rendering bootstrap context. That would move push read-back from coarse project recall toward targeted instance recall.
- Whether semantic lint gets a reproducible review/audit record instead of only direct edits or a wiki page. That would strengthen governance over automated repair.
- Whether session distillation gains stronger source-preserving summaries, source spans, or judge checks. That would make trace-extracted wiki promotion safer.
- Whether `qmd` or another semantic search backend becomes a first-class indexed dependency. Retrieval behavior would change materially from lexical/project-keyword selection to stronger ranking authority.
- Whether autonomous `watch --daemon --heal` gets bounded budgets, review gates, or dry-run policies. Without that, it remains a useful but prompt-sensitive maintenance loop.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - frames why the vault alone is pull memory while `memex context` adds coarse push read-back.
- [Symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - applies: ai-memex-cli's selection uses explicit scenes, types, paths, tags, keywords, and includes rather than hidden semantic activation.
- [Use trace extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-extraction-as-meta-learning.md) - applies: session traces become raw Markdown and later wiki knowledge.
- [Preserve evidence without making history the next context](../../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md) - aligns: raw/session sources are preserved separately from selected wiki/context read-back.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: the system separates raw files, wiki pages, skills, prompts, context blocks, projections, lint reports, and session traces by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies raw sources, wiki pages, search results, and session files when consumed as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies schemas, installed prompts, skills, context blocks, validators, and ranking/projection code.
