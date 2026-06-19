---
description: "EchoesVault review: OpenCode plugin that bootstraps a Markdown/Obsidian vault, slash-command read-back, and agent-mediated trace capture"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-18"
tags: [trace-derived]
---

# EchoesVault / echoes-vault-opencode

EchoesVault, by psinetron, is an OpenCode plugin that creates a project-local `EchoesVault/` Markdown vault, registers slash commands, installs agent skills, and exposes write/search tools for daily logs, encyclopedia pages, and an index. At the reviewed commit the implementation is a small TypeScript plugin: its durable memory is plain files, while most governance comes from generated command and skill prompts rather than hard validators.

**Repository:** https://github.com/psinetron/echoes-vault-opencode

**Reviewed commit:** [1f12282a1452153c851aba7af312e82f28880d49](https://github.com/psinetron/echoes-vault-opencode/commit/1f12282a1452153c851aba7af312e82f28880d49)

**Source directory:** `related-systems/psinetron--echoes-vault-opencode`

## Core Ideas

**The plugin turns a project into a memory vault on load.** `OpenCodeEchoes` resolves `EchoesVault/` under the OpenCode project directory, ensures `raw/`, `pages/`, `daily/`, and `assets/`, creates `index.md` if missing, writes `.opencode/commands/*.md`, and writes `.opencode/skills/*/SKILL.md` only when absent ([index.ts](https://github.com/psinetron/echoes-vault-opencode/blob/1f12282a1452153c851aba7af312e82f28880d49/index.ts)). The adoption bet is zero setup and idempotent scaffolding rather than a separate memory service.

**Memory is split between a daily trace surface and a project encyclopedia.** Daily logs live in `EchoesVault/daily/YYYY-MM-DD.md`; durable concepts live in `EchoesVault/pages/*.md`; `EchoesVault/index.md` is the registry of page descriptions. The README frames this as an Obsidian-compatible vault with OKF-style frontmatter, wikilinks, daily logs, and deprecation-over-deletion rules ([README.md](https://github.com/psinetron/echoes-vault-opencode/blob/1f12282a1452153c851aba7af312e82f28880d49/README.md)).

**Context efficiency is coarse and bounded by convention.** `/echoes-start` injects the full index and the last three daily logs into the command template; `echoes_search_vault_pages` scans only `pages/` and returns matching lines capped to 200 characters each; `/echoes-status` emits a scale alert when the index exceeds 200 topics ([index.ts](https://github.com/psinetron/echoes-vault-opencode/blob/1f12282a1452153c851aba7af312e82f28880d49/index.ts), [README.md](https://github.com/psinetron/echoes-vault-opencode/blob/1f12282a1452153c851aba7af312e82f28880d49/README.md)). There is no vector search, graph traversal, ranking model, token budget, or progressive read path beyond "load recent logs and index, then keyword-search pages."

**Behavioral control is prompt-shaped.** The generated slash commands and skills tell the agent to read before writing, keep technical density, use YAML frontmatter, update the index, deprecate instead of deleting, and save important intermediate decisions. Those are strong instructions at consumption time, but the write tools themselves mostly accept strings and write files; the inspected code does not parse page YAML, enforce a `type` enum, or validate OKF compliance before saving a page ([index.ts](https://github.com/psinetron/echoes-vault-opencode/blob/1f12282a1452153c851aba7af312e82f28880d49/index.ts)).

**The trace-learning loop is agent-mediated, not daemonized.** `/echoes-end` tells the agent to distill the current session into `dailySummary`, optional `newPages`, `indexAppends`, and `indexUpdates`, then invoke `commit_memory_to_echoes_vault`; the tool writes the daily log, pages, and index. `echoes_append_to_daily_log` adds timestamped scratchpad notes mid-session. The plugin supplies the write surface and prompts, while the model in the active OpenCode session is the extraction oracle ([index.ts](https://github.com/psinetron/echoes-vault-opencode/blob/1f12282a1452153c851aba7af312e82f28880d49/index.ts)).

## Artifact analysis

- **Storage substrate:** `files` `repo` `prompt-registry` - The retained memory is project-local Markdown files under `EchoesVault/`; the behavior-shaping commands and skills are package constants copied into `.opencode/` files and also registered through OpenCode's command configuration; the surrounding project repository can version the resulting vault but the plugin does not require git.
- **Representational form:** `prose` `symbolic` - Daily summaries, page bodies, command prompts, and skill instructions are prose; frontmatter, filenames, directories, index lines, wikilinks, tool schemas, command metadata, and timestamped log sections are symbolic. The inspected package has no embeddings, model weights, or other parametric retained form.
- **Lineage:** `authored` `trace-extracted` - Pages and index entries can be authored by a human or agent through the write tools; daily summaries, scratchpad entries, and `/echoes-end` pages are derived from the active session context by the agent. Vault structure, commands, and skills are authored package artifacts.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `learning` - Daily logs, pages, raw materials, and search results are knowledge artifacts; slash commands and skills instruct the agent; directories, filenames, index entries, and command names route work; frontmatter/index/deprecation rules are validation pressure in prompts rather than hard code gates; session distillation and scratchpad writes create learning material for later sessions.

**Vault files.** The central memory artifact is a set of Markdown files under `EchoesVault/`. `daily/` records session history, `pages/` stores encyclopedia entries, `raw/` holds read-only source material by convention, `assets/` holds local diagrams and images, and `index.md` is the registry used by `/echoes-start`. The source of truth is readable files, not a database mirror.

**Slash commands.** `echoes-init`, `echoes-start`, `echoes-end`, and `echoes-status` are prompt templates with OpenCode command frontmatter. They are system-definition artifacts: they decide what memory is loaded, what rules are restated, and which tool call the agent must prepare. `/echoes-start` is especially important because it embeds shell reads of `EchoesVault/index.md` and the newest three daily logs into the command payload.

**Tool schemas and write functions.** `commit_memory_to_echoes_vault`, `echoes_append_to_daily_log`, `echoes_search_vault_pages`, and `echoes_create_or_update_page` are the executable API. Their schemas constrain payload shape, path placement, and some filename safety, but not semantic quality. `sanitizeFilename` strips `..` and path separators for page names; the page write path otherwise overwrites the target file with the supplied content.

**Generated skills.** The three generated skills give trigger conditions and operating rules for mid-session logging, searching, and page creation. They are instruction artifacts consumed by the host agent rather than independent code paths; their effective authority depends on OpenCode's skill loading and the model following the instructions.

Promotion path: EchoesVault can promote active-session context into daily logs, page files, and index entries. It can also install prompts that tell future agents to treat those files as memory. It does not promote memory into enforced validators, ranked indexes, symbolic policy gates, or learned retrieval models.

## Comparison with Our System

EchoesVault and Commonplace share the file-first premise: durable agent memory should be readable, editable Markdown in the project tree. Both use frontmatter, indexes, commands/skills, and explicit writing rules to make a future agent behave better than it would from raw chat history.

The main divergence is where authority lives. Commonplace puts much of the contract in collection/type specs, validators, review workflows, and link conventions. EchoesVault puts most of it in generated prompts and tool descriptions. That makes EchoesVault easy to adopt and cheap to understand, but weaker as a governed knowledge base: a page without YAML frontmatter or an incorrect `type` can still be written by the tool.

EchoesVault has a stronger out-of-the-box session loop than Commonplace's general library artifacts: start by loading recent logs and the index, append scratchpad notes while working, and end by distilling the session. Commonplace has the stronger curation and review model once material is promoted into the library.

### Borrowable Ideas

**Install project-local memory commands with the store.** Ready for narrow workflows. A Commonplace initializer could create task-start/task-end commands for a consuming project, but those commands should point at existing type contracts rather than inventing an unvalidated side system.

**Mid-session scratchpad as a first-class tool.** Ready for workshops. EchoesVault's explicit scratchpad tool captures important decisions before compaction or interruption; in Commonplace this fits `kb/work/` better than library notes until reviewed.

**Scale alert on coarse always-load memory.** Ready now. EchoesVault's 200-topic warning is simple, but the principle is useful: if an index is loaded wholesale at session start, the system should warn when the surface stops being cheap.

**Do not borrow prompt-only validation for library artifacts.** Commonplace should keep validators and type contracts for durable notes. EchoesVault shows how far adoption can get with prompts, not why enforcement should be removed.

## Write side

**Write agency:** `manual` `automatic` - Humans or agents explicitly invoke slash commands and tools to create, update, append, and search memory; the plugin automatically creates vault directories, the default index, commands, and skills on load, and the `/echoes-end` command drives agent-mediated session distillation into durable files.

**Curation operations:** `none` - The automatic path acquires and stores trace-derived summaries, pages, index edits, and scaffolding, but the inspected code does not automatically consolidate, deduplicate, evolve, synthesize across already-stored memories, invalidate, decay, or promote existing entries.

### Trace-derived learning

**Trace source:** `session-logs` - The source signal is the active OpenCode session as available to the agent when `/echoes-end` runs, plus optional intermediate scratchpad notes written during the session.

**Extraction.** The extraction oracle is the agent following the generated command or skill. `/echoes-end` asks it to produce a dense final daily summary, new encyclopedia pages for new concepts or decisions, and index line appends/updates; `echoes_append_to_daily_log` asks it to append concise dry facts after trigger events. The plugin does not read a transcript file or run an independent summarizer.

**Learning scope:** `per-project` - The vault path is resolved under the current OpenCode project directory, so learned artifacts are scoped to that project unless the user copies the vault elsewhere.

**Learning timing:** `online` `staged` - Scratchpad writes happen during the session, while `/echoes-end` is a staged end-of-session distillation command.

**Distilled form:** `prose` `symbolic` - The durable output is Markdown prose plus symbolic frontmatter, daily headings, filenames, wikilinks, and index entries.

Relative to the trace-derived survey, EchoesVault is trace-to-knowledge and trace-to-instruction-context, not trace-to-enforcement. It makes session outcomes available to future agents through files and start commands, but it does not derive validators, rankers, route tables, or code changes from the traces.

## Read-back

**Read-back:** `both` - The search tool is pull retrieval; `/echoes-start` and `/echoes-init` can push retained vault memory and memory rules into the receiving agent's command context when invoked.

**Read-back signal:** `coarse` - The push side is coarse: `/echoes-start` always reads the full index and the newest three daily logs. The pull side is keyword search over `pages/` lines using case-insensitive substring matching; there is no push-time identifier router, embedding search, or LLM relevance judge in the plugin code.

**Faithfulness tested:** `no` - The repository does not include tests or evaluations showing that loaded logs, index entries, skills, or search results change the agent's behavior correctly.

The injection point is pre-invocation command assembly. The command template embeds shell reads of the index and recent logs before the model responds to `/echoes-start`; the agent then summarizes trajectory, proposes next steps, and audits the index. Pull retrieval happens when the agent calls `echoes_search_vault_pages`, which returns matching lines with file names and line numbers.

Selection and complexity control are minimal. Recent-log loading is capped at three files, line snippets are truncated to 200 characters, and the status command warns above 200 indexed topics. The index itself is loaded in full, and search has no ranking, pagination, or result cap. Effective context dilution is therefore project-size dependent and not verified from code.

At consumption, memory authority is mixed. Daily logs and pages are advisory knowledge; command and skill text can act as instruction; index lines route the agent toward pages; frontmatter and deprecation rules are instruction-level validation. There is no hard gate that prevents a bad page write or stale index entry.

## Curiosity Pass

**The README overstates enforcement.** It says the `type` property is strictly enforced for OKF compliance, but the inspected write functions do not parse frontmatter or reject invalid page content. Enforcement is mostly delegated to the agent instructions.

**The start command is powerful but blunt.** Loading the last three logs plus the full index is a pragmatic continuity hack. It works best for small vaults and explains why the status command warns at 200 topics.

**The plugin has two memory layers with different trust levels.** Daily logs are trace-derived and useful for continuity, while encyclopedia pages are supposed to be denser architectural facts. The code does not enforce that separation beyond paths and prompt wording.

**Safe filenames are not the same as safe knowledge.** `sanitizeFilename` blocks path traversal for page names, and idempotent install avoids overwriting commands/skills, but semantic correctness still depends on the agent reading and writing responsibly.

## What to Watch

- Whether EchoesVault adds real YAML/frontmatter validation for page writes; that would move OKF compliance from prompt pressure to code-level validation.
- Whether `/echoes-start` gains indexed or ranked retrieval instead of full-index plus recent-log loading; that would change the context-efficiency story for larger vaults.
- Whether the plugin starts reading OpenCode transcript files directly; that would make trace-derived extraction less dependent on the model's current context and could introduce a stronger extraction oracle.
- Whether page updates preserve history or implement deprecation automatically; today deprecation over deletion is an instruction, not a write-side invariant.
- Whether tests or fixtures are added for command generation and tool behavior; that would make the plugin's idempotence and memory-safety claims easier to trust.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes EchoesVault's stored files from slash-command push and search-tool pull.
- [Axes of artifact analysis](../../../notes/axes-of-artifact-analysis.md) - supports separating vault files, generated commands, generated skills, and tool schemas by substrate, form, lineage, and authority.
- [Use trace-derived extraction as meta-learning](../../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - frames `/echoes-end` and scratchpad notes as session-trace distillation into future memory.
- [System-definition artifact](../../../notes/definitions/system-definition-artifact.md) - classifies generated OpenCode commands, skills, and tool schemas as behavior-shaping artifacts.
- [Knowledge artifact](../../../notes/definitions/knowledge-artifact.md) - classifies daily logs, pages, raw materials, and search results as remembered context rather than hard controls.
- [Symbolic context engineering is bounded by symbol availability](../../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - relates to EchoesVault's reliance on filenames, index lines, wikilinks, dates, and keywords as retrieval symbols.
