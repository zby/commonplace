---
description: "pi-self-learning review: pi extension that reflects completed agent sessions into git-backed daily, core, and long-term memory files"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
last-checked: "2026-06-04"
---

# pi-self-learning

`pi-self-learning`, by mcollina, is a single pi coding-agent extension that turns completed agent-session traces into a git-backed memory folder. At the reviewed commit, it hooks task completion to run an LLM reflection prompt, writes daily Markdown entries, maintains a scored `core/index.json`, renders `core/CORE.md` and `long-term-memory.md`, can generate monthly summaries and redistilled global rules, and injects retained memory before later agent starts.

**Repository:** https://github.com/mcollina/pi-self-learning

**Reviewed commit:** [b1add8631cb621bc2caba3c9f70376dcddf6ca36](https://github.com/mcollina/pi-self-learning/commit/b1add8631cb621bc2caba3c9f70376dcddf6ca36)

**Source directory:** `related-systems/pi-self-learning`

## Core Ideas

**The extension makes learning a pi lifecycle hook.** The default export registers `agent_end` and `before_agent_start` handlers: after a completed task it may call `reflectNow("Task", ctx)`, and before the next agent start it may return hidden memory context plus an augmented system prompt ([extension](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/extensions/self-learning.ts)). This is runtime memory infrastructure, not a separate CLI-only note store.

**Task-end reflection extracts mistakes and fixes from recent branch messages.** `reflectNow()` reads recent session branch messages, serializes them through pi's LLM conversion helpers, collects interruption signals from recent tool results, and prompts a reflection model to return strict JSON with `mistakes` and `fixes` ([reflection prompt](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/extensions/self-learning.ts)). The README describes the same pipeline as automatic task-level reflection after completed tasks ([README](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/README.md)).

**Memory is file-native and optionally git-backed.** The storage root defaults to `.pi/self-learning-memory` in project mode or `~/.pi/agent/self-learning-memory` in global mode. The extension creates `daily/`, `monthly/`, `core/CORE.md`, `core/index.json`, and `long-term-memory.md`, initializes a repository when git is enabled, and commits updated memory files when auto-commit is enabled ([storage helpers](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/extensions/self-learning.ts), [README](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/README.md)).

**Core memory is ranked, not just appended.** `updateCoreFromReflection()` converts fixes to `learning` records and mistakes to `antiPattern` records, normalizes keys, increments repeated records, and renders a top-ranked `CORE.md`; sorting uses score, hits, and a light recency penalty, with balanced representation between learnings and watch-outs when both exist ([core index](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/extensions/self-learning.ts)). This gives the compact core file stronger future authority than the full daily journal.

**Context efficiency is coarse file selection plus character budgets.** Before an agent starts, `buildMemoryContextBundle()` can include the core file, the latest monthly summary, and a configured number of latest daily files, each trimmed under a shared `maxChars` budget. It does not perform semantic retrieval over memory entries; the main bound is "which files are configured/latest" and text truncation ([context bundle](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/extensions/self-learning.ts)).

**The memory policy can become instruction-like.** `buildMemoryInstruction()` can append an advisory or strict system-prompt policy telling the agent where memory lives, to start from `CORE.md`, to check daily/monthly files for historical questions, and to prefer memory evidence over guessing ([instruction builder](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/extensions/self-learning.ts)). The same retained prose can therefore be background evidence and system-level instruction, depending on context settings.

## Artifact analysis

- **Storage substrate:** `files` `repo` `in-memory` — Durable memory persists as Markdown and JSON files under the resolved memory root; optional git initialization and commits preserve memory history; `RUNTIME_NOTES` carries short recent notes only in process memory between starts.
- **Representational form:** `prose` `symbolic` — Daily entries, monthly summaries, `CORE.md`, and `long-term-memory.md` are prose; configuration, branch runtime overrides, strict JSON reflection outputs, `core/index.json` records, command definitions, and hook registrations are symbolic. There is no vector index or model-weight update in the inspected repository.
- **Lineage:** `authored` `trace-extracted` — Settings and extension code are authored; daily entries and core records are trace-extracted from serialized branch messages, tool-result interruption signals, and LLM reflection outputs. Redistilled entries remain derived from earlier core records.
- **Behavioral authority:** `knowledge` `instruction` `ranking` `learning` — Memory files advise as knowledge when injected; strict/advisory memory policy can instruct the agent; `core/index.json` scores and recency ranking decide what appears in `CORE.md`; the task-end reflection loop learns from previous agent work.

**Daily journal entries.** The raw durable trace layer is `daily/YYYY-MM-DD.md`, appended with "What went wrong" and "How it was fixed" sections generated from the current branch conversation. It is trace-extracted prose with knowledge authority and source value for monthly summaries or later inspection.

**Core index and renders.** `core/index.json` is the canonical scored symbolic index. `CORE.md` is a ranked prose view over that index, while `long-term-memory.md` is the complete rendered history. The index has ranking authority; the rendered files gain knowledge and possible instruction authority when pushed into context.

**Monthly summaries and redistilled global rules.** `/learning-month` consolidates daily files for a month into a prose summary. `/learning-redistill` rewrites selected core entries into cross-project action rules, can deduplicate records after key normalization, and writes the updated core files when not in dry-run mode.

**Runtime notes and system-prompt policy.** `RUNTIME_NOTES` is an in-memory carryover of the first mistake/fix note from a successful reflection. The memory instruction is authored symbolic/prose configuration that controls whether injected memory is advisory or strict.

Promotion path: recent branch messages and interruption signals are serialized; an LLM reflection extracts mistakes and fixes; daily Markdown records preserve the episode-level output; core records score and aggregate repeated items; `CORE.md`, monthly summaries, runtime notes, and strict/advisory policy can be pushed into future agent context.

## Comparison with Our System

| Dimension | pi-self-learning | Commonplace |
|---|---|---|
| Primary purpose | Personal pi extension that learns from coding-agent sessions | Git-native methodology KB and framework for agent-operated knowledge systems |
| Canonical artifacts | Daily logs, monthly summaries, `core/index.json`, `CORE.md`, `long-term-memory.md`, git commits | Typed Markdown notes, reviews, source snapshots, type specs, indexes, validation reports |
| Learning loop | Reflect after task, score repeated lessons, inject memory before later starts | Deliberately write, connect, validate, review, archive, and promote artifacts |
| Read-back | Automatic pre-start memory bundle and policy, plus commands that expose memory files | Mostly deliberate pull through `rg`, indexes, links, skills, and review workflows |
| Governance | Strict JSON parsing, ranking, git history, non-blocking failures | Type contracts, schemas, deterministic validation, semantic gates, source citations, replacement archives |

The strongest alignment is file-native memory. Like Commonplace, pi-self-learning keeps retained behavior in inspectable files and can put them under git, which makes deletion, diffing, rollback, and human review practical. The difference is authority speed: pi-self-learning lets a single post-task reflection enter `CORE.md` and future prompts quickly, while Commonplace usually requires source-grounding and validation before an artifact carries system-definition weight.

The main divergence is retrieval granularity. pi-self-learning selects memory at file and recency/configuration level; Commonplace relies on lexical search, indexes, links, and type contracts for more deliberate navigation. pi-self-learning is better for "remind this agent of recent mistakes"; Commonplace is better for durable, source-audited methodology.

### Borrowable Ideas

**Keep the memory root explicit in injected context.** Ready now. Commonplace prompts and skills should name the actual artifact paths they rely on, especially when generated context comes from a resolved project root rather than the current working directory.

**Separate raw daily traces from ranked core memory.** Ready for workshops. Commonplace could use daily work logs as raw trace evidence and a reviewed "core lessons" view as the only pushed material.

**Use branch/session runtime overrides.** Needs a concrete use case. A Commonplace analogue could temporarily disable or narrow a review/learning hook for a branch without editing durable config.

**Treat user interruptions as learning signals.** Ready as review guidance. The extension's interruption collector is a useful reminder that blocked commands, denied permissions, and aborts can encode operator boundaries, not just execution failures.

**Do not borrow unreviewed automatic promotion for durable methodology.** pi-self-learning is appropriate for personal session memory; Commonplace should keep automatic reflections as candidates until a source-grounded review or validation path promotes them.

## Write side

**Write agency:** `automatic` `manual` — `agent_end` can automatically reflect after tasks and update memory; users can also invoke commands such as `/learning-now`, `/learning-month`, `/learning-redistill`, `/learning-toggle`, and model-selection commands.

**Curation operations:** `consolidate` `dedup` `evolve` `promote` — Monthly summaries consolidate daily files; redistill can rewrite existing core records and merge duplicate normalized keys; the core index increments hits/scores and renders top-ranked items into `CORE.md`.

### Trace-derived learning

**Trace source:** `session-logs` `tool-traces` `event-streams` — The extension consumes recent session branch messages, serialized conversation text, assistant abort markers, and tool-result permission/block/cancel signals.

**Learning scope:** `per-task` `per-project` `cross-task` — Ordinary automatic reflection is per completed task; project storage keeps project-specific details under `.pi/self-learning-memory`; global storage and redistill can turn entries into cross-project rules for later sessions.

**Learning timing:** `online` `staged` — Task-end reflection runs online after `agent_end`; monthly summarization and global redistill are staged command-driven maintenance.

**Distilled form:** `prose` `symbolic` — The immediate distilled output is prose daily/core memory plus symbolic scored index entries.

Extraction is LLM-mediated and JSON-gated. The reflection prompt asks for only mistakes and fixes, with different scope rules for project versus global storage. Failed reflection is non-blocking, and malformed output can be repaired before the extension writes memory.

Survey placement: pi-self-learning is a trace-to-prose learning system with a file-native memory root and explicit pre-start injection. It strengthens the survey claim that trace-derived memory needs a promotion boundary: raw conversation logs are not replayed wholesale; extracted lessons are scored, rendered, and optionally redistilled before influencing future runs.

## Read-back

**Read-back:** `both` — Memory is pushed before future agent starts through the `before_agent_start` hook, hidden context bundle, runtime notes, and optional system-prompt policy; it is also pullable through slash commands and by directly inspecting the memory files.

**Read-back signal:** `coarse` — Pushed memory is selected by configuration, latest-file rules, fixed counts, and character budgets, not by semantic similarity, identifiers from the current task, or LLM relevance judgment.

**Faithfulness tested:** `no` — I found structural wiring, command paths, and manual validation guidance, but no with/without memory ablation or post-action audit proving that injected memory changes later agent behavior correctly.

**Direction edge cases.** `/learning-status`, `/learning-daily`, `/learning-month`, and `/learning-redistill` are operator-facing pull or maintenance paths. They do not change the direction of the agent-facing read-back path, which is push when the extension returns a hidden `self-learning-context` message or modifies the system prompt before invocation.

**Targeting and signal.** The pushed path is coarse. `includeCore`, `includeLatestMonthly`, and `includeLastNDaily` choose broad memory surfaces; `injectLastN` chooses recent in-memory notes; `maxChars` trims text. There is no per-query retrieval, embedding index, keyword search, or judged relevance selection in the inspected code.

**Injection point.** The injection point is pre-invocation: `before_agent_start` assembles memory pieces and instruction text before the agent model call. Post-task reflection is write-side learning, not read-back.

**Selection, scope, and complexity.** Scope is project or global depending on `storage.mode`, and volume is bounded by `maxChars`, per-file trimming, `includeLastNDaily`, and `injectLastN`. Complexity can still grow because `CORE.md`, latest monthly summaries, and daily files may contain broad, loosely related prose.

**Authority at consumption.** The hidden memory bundle is advisory evidence. The system-prompt policy can be advisory or strict; strict mode tells the agent it must consult memory for historical questions and prefer memory evidence over guessing. Effective compliance is not measured.

**Other consumers.** Human operators can inspect the memory folder and git history, run slash commands, preview redistill as a dry run, and edit configuration. Git is also an operational consumer because memory updates can be committed automatically.

## Curiosity Pass

**The strongest trust affordance is ordinary git, not model scoring.** The extension can commit every memory update, which makes history visible, but it does not attach source message ids, model outputs, or review status to each core record.

**`CORE.md` is a rendered view, not the source of truth.** The implementation migrates from `CORE.md` if `core/index.json` is absent, but once the index exists the scored JSON records drive the core render.

**The read-back is intentionally blunt.** Loading the top core file and latest optional summaries is cheap and predictable, but it cannot target a lesson to the current task except through broad recency and ranking.

**Redistill changes authority without external review.** Rewriting global entries into cross-project rules can make memory more reusable, but it also removes concrete identifiers and may weaken auditability unless operators inspect the dry run or git diff.

## What to Watch

- Whether future versions retain source branch/message ids or reflection model metadata beside each core record.
- Whether `CORE.md` gains review status, confidence, or quarantine before strict-mode injection.
- Whether read-back adds identifier, lexical, embedding, or judgment-based selection over memory entries.
- Whether tests or evals measure behavior with and without injected memory rather than only manual command success.
- Whether monthly summaries and redistill acquire source-grounding checks against the daily/core records they transform.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: pi-self-learning extracts durable lessons from agent-session traces and pushes them into future runs.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: pi-self-learning's memory matters because `before_agent_start` activates retained files before the model call.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: daily logs, core index, rendered memory files, runtime notes, and system-prompt policy carry different forms and authorities.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: daily logs, monthly summaries, and memory files advise as evidence and context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: hook registrations, ranking, context assembly, and strict memory policy configure future behavior.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: pi-self-learning derives reusable lessons from completed task traces.
