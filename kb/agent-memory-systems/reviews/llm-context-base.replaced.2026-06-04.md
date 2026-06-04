---
description: "llm-context-base review: markdown LLM-wiki template with metadata routing, training write-back, JIT instructions, lint, and multi-tool shims"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: outdated
last-checked: "2026-06-03"
tags: []
---

# llm-context-base

> Replaced 2026-06-04. See [llm-context-base](./llm-context-base.md) for the current review.

llm-context-base, by `asakin/llm-context-base`, is an opinionated Markdown/Obsidian template for building a personal LLM-maintained wiki. At the reviewed commit, it is not a runtime service: the retained system is a repository of Markdown directories, frontmatter standards, templates, tool bootstrap shims, and agent instructions that tell Claude Code, Cursor, Copilot, Windsurf, AGENTS.md-compatible tools, or other file-reading LLMs how to capture, query, lint, and adapt a personal knowledge base.

**Repository:** https://github.com/asakin/llm-context-base

**Reviewed commit:** [6d01cba8e2c22f9ca2519c70073a05cd54378a8c](https://github.com/asakin/llm-context-base/commit/6d01cba8e2c22f9ca2519c70073a05cd54378a8c)

**Last checked:** 2026-06-03

## Core Ideas

**The wiki is a template substrate, not an app.** The docs explicitly frame the repo as "a pile of markdown files" with no runtime, build step, database, or committed binary dependency; intelligence lives in the AI tools and optional integrations above the repo ([docs/design-decisions.md](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/docs/design-decisions.md)). The committed material is therefore the memory system: `_config/`, `_meta/`, content directories, templates, tool shims, Obsidian config, examples, and logs.

**Metadata summaries are the main context-efficiency device.** Every content file is supposed to carry YAML frontmatter with `type`, `summary`, `tags`, `status`, and `updated`, and the query protocol tells agents to scan filenames and summaries first, then read only the 1-3 most relevant files ([docs/metadata-standard.md](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/docs/metadata-standard.md), [_config/standard.md](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/_config/standard.md), [_meta/instructions/knowledge-query.md](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/_meta/instructions/knowledge-query.md)). This bounds both volume and complexity by keeping the ordinary read path at directory routing -> summary scan -> small full-file read set. There is no generated search index, vector store, or ranking layer in the repo at this commit.

**Agent behavior is bootstrapped through thin, duplicated tool shims.** `AGENTS.md`, `.claude/CLAUDE.md`, `.cursorrules`, `.cursor/rules/bootstrap.mdc`, `.github/copilot-instructions.md`, and `.windsurfrules` all perform the same initial handoff: check framework mode, otherwise run the session start protocol from `_config/config.md` and `_meta/instructions/general.md` ([AGENTS.md](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/AGENTS.md), [.claude/CLAUDE.md](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/.claude/CLAUDE.md), [docs/supported-tools.md](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/docs/supported-tools.md)). This gives broad adoption without making one agent product the source of truth.

**The memory system writes back learned conventions during use.** The training controller in `_config/config.md` asks agents to learn the user's role, directory needs, naming patterns, tags, preferences, and structure over a 30-day training period, then reduce initiative in cooldown and established phases ([docs/training-phases.md](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/docs/training-phases.md), [_config/config.md](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/_config/config.md)). `_meta/instructions/general.md` makes the loop more concrete: when a conversation establishes a rule, preference, structural change, or reusable pattern, the agent should write it immediately to `_config/config.md`, `_config/context.md`, `_meta/instructions/general.md`, a relevant module, the README, or `2-Knowledge/log.md` ([_meta/instructions/general.md](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/_meta/instructions/general.md)).

**Capture is deliberately inbox-first.** New knowledge lands in `_inbox/` with date-prefixed filenames and metadata, then gets filed later into `2-Knowledge/`, `1-Projects/`, `3-Journal/`, or another learned location ([_inbox/README.md](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/_inbox/README.md), [_meta/instructions/agent-write.md](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/_meta/instructions/agent-write.md)). The default is to discard raw captures after filing; `_sources/` is opt-in for preserved originals when source retention matters ([_sources/README.md](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/_sources/README.md)).

**Governance is procedural and lint-like.** The system has templates, a metadata standard, a definition-of-done module, lint checks for stale inbox items, missing metadata, stale active files, orphaned files, context bloat, filenames, and raw paths, plus a context-optimization review protocol ([_meta/instructions/knowledge-lint.md](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/_meta/instructions/knowledge-lint.md), [_meta/instructions/optimization-review.md](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/_meta/instructions/optimization-review.md)). These are instructions for the current agent to run and report, not enforced validators in the repository itself.

## Artifact analysis

- **Storage substrate:** `files` — The central retained state is a Git/Obsidian-friendly file tree of Markdown docs, frontmatter, instruction modules, templates, logs, shims, and a small Python migration script.
- **Representational form:** `prose` `symbolic` — Prose Markdown dominates, with symbolic YAML frontmatter, status/type/tag vocabularies, gitignore rules, JSON editor settings, Obsidian config, and Python migration logic.
- **Lineage:** `authored` `imported` `trace-extracted` — The template ships authored framework files, the wiki can import or file captured/source material, and training logs, operation logs, learned preferences, and decision outcomes are trace-derived during use.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `learning` — Wiki content and logs advise future work; bootstrap/config/instruction files instruct and route agents; lint protocols validate by agent procedure; learned context and decision outcomes update later behavior.

**Personal wiki content.** Storage substrate: Markdown files under `_inbox/`, `1-Projects/`, `2-Knowledge/`, `3-Journal/`, `4-Private/`, `_output/`, and optionally `_sources/`. Representational form: prose Markdown plus YAML frontmatter, links, dates, and templates. Lineage: authored or filed by the agent from conversations, captures, source documents, decisions, project work, meetings, or journal entries; `_inbox/` items are temporary source candidates, while filed knowledge is the working memory. Behavioral authority: mostly knowledge artifacts returned as evidence, context, or advice during query; decision outcomes can advise later decisions through the decision learning loop.

**Configuration and learned context.** Storage substrate: `_config/config.md`, `_config/context.md`, `_config/standard.md`, and `_config/tools.md`. Representational form: mixed prose instructions and symbolic fields. Lineage: shipped template content plus user-filled profile data and trace-derived updates during training; the current conversation, user preferences, and observed structure patterns can invalidate or update them. Behavioral authority: system-definition artifact authority when loaded at session start, because these files set the assistant's phase, tone, routing expectations, metadata contract, tool install offers, and learned user context.

**Instruction modules and templates.** Storage substrate: `_meta/instructions/*.md` and `_meta/templates/*.md`. Representational form: prose procedures with YAML frontmatter and template placeholders. Lineage: authored framework modules, locally extensible by the agent when new behavior becomes established. Behavioral authority: system-definition artifacts for file creation, query, lint, optimization review, definition-of-done, and domain-specific writing; they route future actions and constrain writes, but rely on agent compliance.

**Bootstrap shims and tool settings.** Storage substrate: `AGENTS.md`, `.claude/CLAUDE.md`, `.cursorrules`, `.cursor/rules/bootstrap.mdc`, `.github/copilot-instructions.md`, `.windsurfrules`, `.claude/settings.json`, and `.obsidian/` settings. Representational form: mostly prose instructions plus JSON config. Lineage: shipped framework files duplicated per host tool. Behavioral authority: system-definition artifacts at the host boundary; they decide whether the agent enters framework mode or personal-instance mode and which shared instructions become active.

**Logs and operation history.** Storage substrate: `WIKI-LOG.md`, `2-Knowledge/log.md`, training-log sections in `_config/config.md`, and decision `## Outcome` sections. Representational form: prose chronology plus date/action conventions. Lineage: trace-derived from wiki operations, ingests, queries, lint passes, edits, archives, and conversations that establish patterns. Behavioral authority: knowledge artifacts for audit and future synthesis; when training-log entries or decision outcomes change later routing or advice, they act as weak system-definition inputs.

**Lint, migration, and maintenance scripts.** Storage substrate: procedural instruction files and `migrate-to-yaml-frontmatter.py`. Representational form: prose checklists plus executable Python for one metadata migration. Lineage: authored framework maintenance logic. Behavioral authority: validation/advisory authority when invoked by an agent or user; there is no standing hook or CI gate in the repository that enforces the standard automatically at this commit.

**Promotion path.** The main promotion path is capture -> inbox draft -> filed wiki content -> summary/tag-visible retrieval -> query answer, decision precedent, or learned convention. A stronger path exists for behavior: conversation pattern -> `_config/context.md` or `_config/config.md` -> startup-loaded instruction/context. There is no hard promotion from ordinary knowledge note to enforced validator; authority rises when an instruction module, bootstrap file, or session protocol loads and treats the prose as operative.

## Comparison with Our System

| Dimension | llm-context-base | Commonplace |
|---|---|---|
| Primary purpose | Personal LLM wiki template that adapts to a user's habits | Methodology KB and framework for agent-operated knowledge bases |
| Main substrate | Markdown vault/repo with frontmatter, templates, shims, and instructions | Typed Markdown collections, schemas, reviews, sources, ADRs, generated indexes |
| Context strategy | Startup config/context, JIT instruction modules, directory routing, summary scan, 1-3 full-file reads | Collection contracts, type specs, `rg`, generated indexes, authored links, skills, validation/review reports |
| Governance | Agent-followed metadata standard, lint protocol, training log, templates | Type contracts, deterministic validation, semantic review, link vocabulary, archive/replacement lifecycle |
| Trace use | Conversation-derived preferences, structure, instructions, logs, and decision outcomes | Source snapshots, review reports, workshop promotion, validation/review artifacts, explicit skill workflows |
| Activation | Coarse startup push of config/context plus pull query over summaries | Mostly pull through search/index/link/skill workflows, with some instruction surfaces when invoked |

llm-context-base is close to Commonplace on philosophy: files over services, Markdown over opaque stores, agent-readable contracts, and context efficiency through routing rather than always-loading a corpus. Its adoption stance is lighter. A user can copy the template, open it in an AI tool and Obsidian, and let the training period shape the local taxonomy. Commonplace is more explicit about artifact types, collection boundaries, validation, and review authority.

The most important divergence is where the contract lives. In Commonplace, the collection/type surface is part of the durable library architecture. In llm-context-base, the contract is more conversational and procedural: `_config/config.md` and `_meta/instructions/general.md` tell the current agent when to ask, what to write back, and which module to load. That makes setup easier, but later behavior depends heavily on whether each host agent obeys the bootstrap and session protocol.

llm-context-base's context-efficiency story is intentionally simple: route by directory and question type, scan summaries/tags, then read a handful of files. Commonplace's generated indexes and schemas are heavier, but give more consistent machine parsing and QA. The reviewed repo also says it avoids central indexes, yet keeps README tables and logs as local navigational surfaces; the real distinction is not "no indexes" but "no ever-growing global context index."

**Read-back:** `both` — learned config/context and session summaries are pushed at startup, while retained wiki content is pulled through explicit knowledge-query routing, summary scans, links, and file reads.

**Read-back signal:** `coarse` — The push path is startup/session loading of learned config, context, and summaries rather than instance-specific lexical, embedding, judgment, or identifier-triggered memory selection.

**Faithfulness tested:** `no` — The review notes no benchmark, harness, or ablation showing that pushed context reliably changes later assistant behavior.

### Borrowable Ideas

**Template-first adoption with framework mode escape hatch.** Commonplace could make new consuming-project setup easier by shipping a lighter bootstrap that distinguishes "use this as my KB" from "develop the framework." Ready now as an instruction pattern, but any implementation should avoid duplicated shims drifting apart.

**Training-phase write-back as an explicit lifecycle.** llm-context-base treats the first month as a deliberate adaptation period, then reduces initiative. Commonplace could borrow the idea for new KB installations: early agents may propose structure, later agents should mostly obey established contracts. Needs a concrete consuming-project onboarding workflow.

**Summary-first query discipline.** Commonplace already uses descriptions and indexes; llm-context-base is a useful reminder that every durable artifact should expose a compact retrieval handle that is worth reading before the body. Ready now as a review criterion for collection contracts.

**Inbox TTL as a soft governance mechanism.** The 7-day inbox nudge is simple and human-friendly. Commonplace's workshop layer could use explicit expiry/triage prompts for temporary captures and investigation artifacts. Ready where workshop clutter is a recurring problem.

**Do not borrow instruction-only enforcement for core library artifacts.** llm-context-base can rely on a cooperative current agent because it is a personal template. Commonplace's methodology layer should keep deterministic validation and typed contracts for artifacts that future agents will cite as authority.

## Write-side placement

**Write agency:** `automatic` `manual` — the review identifies a trace-derived or rule-driven path that changes retained memory from execution/session evidence; manual surfaces are included where the reviewed prose describes user or operator authoring.

**Curation operations:** `consolidate` `dedup` `synthesize` `invalidate` `decay` `promote` — the existing review evidence identifies automatic store-changing operations matching these curation classes.

### Trace-derived learning
**Trace source:** `session-logs` `event-streams` — The retained learning comes from conversations, captured ideas, query/lint/edit/archive operations, decision outcomes, and observed behavior during the training period, not from automatic raw JSONL or tool-trace mining.

**Learning scope:** `per-project` `cross-task` — Learned conventions are personal-instance or repo-local, and they shape later sessions and decision/query/write tasks across the wiki.

**Learning timing:** `online` `staged` — Agents write preferences and conventions while the session is happening, within the staged training lifecycle of discovery, refinement/cooldown, and established operation.

**Distilled form:** `prose` `symbolic` — The trace loop distills into prose config, context, instructions, logs, decision outcomes, and symbolic frontmatter or structural conventions.

**Trace source.** llm-context-base qualifies as trace-derived in a limited, file-native sense. The source traces are conversations, captured ideas, query operations, lint operations, decision outcomes, and observed user behavior during the training period. The system does not mine raw JSONL transcripts automatically; it tells the active agent to notice patterns and write them into retained files while the interaction is happening.

**Extraction.** Extraction is agent-judgment-mediated. `_meta/instructions/general.md` says to capture new conventions, preferences, structural changes, purpose shifts, module behaviors, ingests, queries, lint runs, edits, and archives immediately into the relevant retained artifact. `_config/config.md` adds a training-log frame for structure adaptations, preferences learned, directories added, and conventions. The oracle is therefore the current LLM plus user approval or pushback, not a separate evaluator.

**Scope and timing.** Scope is personal-instance or repo-local. Timing is online during the session for preference and convention capture, session-start for inbox/tool/training checks, and on-demand for query, lint, optimization, or decision-learning modules. The training period gives the trace loop a lifecycle: high-initiative discovery, quieter refinement/cooldown, then established operation.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), llm-context-base belongs in the manual/agent-mediated trace-to-prose family. It strengthens the claim that trace-derived learning does not need a database, embedding store, or autonomous mining job: a conversation can become durable behavior by being written into config, context, instructions, templates, or decision outcomes. It also exposes the weak point of this family: provenance is usually summarized in prose, not retained as a replayable raw trace.

## Curiosity Pass

The strongest "memory" path is not in `2-Knowledge/`; it is `_config/context.md` and the training sections of `_config/config.md`, because those are read at session start and can change the next assistant's behavior without a query.

The framework-mode story appears slightly inconsistent in the inspected checkout. The bootstrap files check for `_config/.framework-mode`, `.gitignore` ignores that path, and the file is absent, while `CONTRIBUTING.md` says the canonical repo ships it committed. Parent QA may want to decide whether this is intentional local state, stale docs, or a real upstream mismatch.

The README says summaries scale to hundreds of documents, but there is no benchmark or harness in the repo for retrieval quality or context-size degradation. The mechanism is plausible and simple; effectiveness is not verified from code.

The lint system is a protocol, not an executable validator. That keeps the repo "dumb," but it also means two agents can run the same health check with different thoroughness unless the host supplies deterministic tooling.

The decision learning loop is more concrete than generic "memory": future decisions are supposed to inspect past decisions with filled `## Outcome` sections and surface failure constraints. That is a good example of retained knowledge changing a specific future action type without becoming a universal instruction.

## What to Watch

- Whether the project adds deterministic lint or CI around the metadata standard. That would move governance from cooperative instruction toward enforceable system-definition artifacts.
- Whether `_config/.framework-mode` handling is clarified. The current docs/bootstrap/gitignore interaction affects whether maintainers accidentally run personal-instance protocols in the framework repo.
- Whether query routing gains a generated summary index or search cache. That would improve scale but introduce derived-artifact invalidation, a problem the current design avoids by scanning files directly.
- Whether training-log updates gain source/provenance links to the conversation or operation that caused them. That would make trace-derived learning more auditable.
- Whether multi-tool shims stay duplicated or get generated from one source. Drift across bootstrap files would create tool-specific behavior differences.
- Whether the decision learning loop gets examples from real use. It is one of the most promising behavior-shaping mechanisms, but the template alone cannot show whether agents reliably apply it.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - applies: ordinary wiki pages need query/read paths, while startup-loaded config and context have stronger activation.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: the same Markdown substrate carries knowledge, instruction, routing, validation, and audit authority depending on its path and read channel.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: filed wiki notes, inbox captures, source documents, operation logs, and decision outcomes mostly advise future work when read.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: bootstrap shims, `_config/`, `_meta/instructions/`, templates, lint protocols, and metadata standards shape future agent behavior.
- [Context engineering](../../notes/definitions/context-engineering.md) - frames: llm-context-base is primarily a file-native routing and loading scheme for bounded LLM context.
