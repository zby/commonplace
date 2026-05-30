---
description: "Pi extension that mines task-end session traces into mistake/fix reflections, scored core learnings, git-backed memory files, and prompt-time context"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-05-16"
---

# Pi Self-Learning

Pi Self-Learning is Matteo Collina's single-extension package for pi. It adds automatic task-end reflection, git-backed memory files, scored durable learnings, prompt-time context injection, and commands for manual reflection, monthly summaries, model configuration, and global-memory redistillation. The implementation is concentrated in one TypeScript extension file, so the system is easy to inspect: it is a trace-derived prose-memory loop rather than a general knowledge base or database-backed memory service.

**Repository:** https://github.com/mcollina/pi-self-learning

**Reviewed commit:** [b1add8631cb621bc2caba3c9f70376dcddf6ca36](https://github.com/mcollina/pi-self-learning/commit/b1add8631cb621bc2caba3c9f70376dcddf6ca36)

**Last checked:** 2026-05-16

## Core Ideas

**Automatic reflection is attached to pi's task boundary.** The extension registers an `agent_end` hook, checks `selfLearning.enabled`, `selfLearning.autoAfterTask`, and a temporary redistill skip window, then calls `reflectNow("Task", ctx)` without blocking normal agent completion if reflection fails ([extensions/self-learning.ts](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/extensions/self-learning.ts)). `reflectNow` takes recent branch messages, serializes them through pi's conversation helpers, asks an LLM for strict JSON shaped as `{"mistakes":["..."],"fixes":["..."]}`, appends a daily markdown entry, updates the core index and rendered memory files, and optionally commits the memory repo. This is a concrete trace-to-artifact loop, not just a README claim.

**The extraction schema is intentionally narrow.** The reflection prompt calls itself a "coding session mistake-prevention reflection engine," tells the model not to summarize accomplishments, and only accepts mistakes and fixes. Project storage keeps useful repository-specific detail, while global storage asks for cross-project reusable rules and removal of project-specific identifiers ([extensions/self-learning.ts](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/extensions/self-learning.ts)). The operative retained form is prose, but the strict JSON boundary, `learning` versus `antiPattern` kind, normalized keys, hit counts, scores, and timestamps add a light symbolic control layer.

**Interruption signals are promoted into reflection evidence.** `collectInterruptionSignals` scans recent branch entries for assistant aborts, skipped tools after a queued user message, permission denials, blocked commands, policy refusals, and user-cancelled tool results, then adds those lines to the reflection prompt as intentional user-boundary evidence ([extensions/self-learning.ts](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/extensions/self-learning.ts)). When such signals exist, the prompt requires prevention-oriented mistake and fix items. That is the system's sharpest design move: an Esc press, denied command, or blocked operation is treated as feedback about agent behavior, not as noise.

**The storage substrate is a dedicated file tree, usually a git repo.** The default project root is `.pi/self-learning-memory`; global mode uses `~/.pi/agent/self-learning-memory`. The code resolves relative project paths from the nearest `.pi/settings.json` ancestor or git root, creates `daily/`, `monthly/`, `core/`, `core/CORE.md`, `core/index.json`, and `long-term-memory.md`, and initializes a git repository in the memory root when git is enabled ([README.md](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/README.md), [extensions/self-learning.ts](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/extensions/self-learning.ts)). The memory tree is inspectable and versioned, but it is separated from the project repo's normal review path unless the user deliberately inspects `.pi/self-learning-memory`.

**Raw, daily, core, index, long-term, and monthly artifacts have different authority.** Raw branch messages and tool results are trace evidence inside pi's session store; Pi Self-Learning does not retain them as its own source corpus. Daily markdown files are trace-derived knowledge artifacts that preserve each reflection event. `core/index.json` is the canonical scored index for durable items, while `CORE.md` and `long-term-memory.md` are rendered views from that index, with `CORE.md` capped to balanced top learnings and watch-outs and `long-term-memory.md` dumping the whole sorted history ([extensions/self-learning.ts](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/extensions/self-learning.ts)). Monthly summaries are optional LLM-generated consolidations from daily files. The strongest system-definition artifacts are the context injection bundle and system-prompt policy, because they route future agent behavior.

**Ranking is flat, explicit, and decayed.** `updateCoreFromReflection` turns fixes into `learning` records and mistakes into `antiPattern` records prefixed with `Avoid:`, deduplicates by normalized text, increments hits and score on repeats, and refreshes `lastSeen`. `effectiveScore` subtracts a light age penalty, sorting then favors score, hits, and recency. `selectBalancedCoreItems` reserves space for both learnings and watch-outs when both exist before filling remaining slots from the global rank ([extensions/self-learning.ts](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/extensions/self-learning.ts)). There is no semantic merge except exact normalized-text dedupe and redistill-time rewriting.

**Context injection is both content and instruction.** On `before_agent_start`, the extension can inject recent in-memory runtime notes, `CORE.md`, optionally the latest monthly file, optionally the last N daily files, and a system-prompt policy. Strict mode says the assistant must consult self-learning memory for history, prior decisions, patterns, regressions, or follow-up work, start from `CORE.md`, check daily and monthly files for historical questions, prefer evidence over guessing, and consult `long-term-memory.md` when stuck ([extensions/self-learning.ts](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/extensions/self-learning.ts)). The injected file contents are knowledge artifacts; the strict policy is a system-definition artifact with instruction and routing authority.

**Commands cover operation, configuration, and migration rather than validation.** The extension registers `/learning-now`, `/learning-month`, `/learning-redistill`, `/learning-toggle`, `/learning-model`, `/learning-model-global`, `/learning-daily`, and `/learning-status` ([README.md](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/README.md), [extensions/self-learning.ts](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/extensions/self-learning.ts)). Model resolution tries configured model auth first and falls back to the current session model for reflection; redistill similarly tries configured then current model. The repository has no npm scripts or automated test suite, and its AGENTS file says behavior should be validated manually inside pi with extension commands ([AGENTS.md](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/AGENTS.md), [package.json](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/package.json)).

## Comparison with Our System

| Dimension | Pi Self-Learning | Commonplace |
|---|---|---|
| Primary purpose | Automatic mistake-prevention memory for pi sessions | Agent-operated KB methodology with typed artifacts, validation, reviews, and indexes |
| Trace source | Recent pi branch messages plus tool/interruption signals | Explicit source artifacts, snapshots, notes, reviews, and optional trace-derived workflows |
| Canonical store | Memory-root files, especially `core/index.json` plus daily markdown | Git-tracked typed markdown collections under `kb/` |
| Derived views | `CORE.md`, `long-term-memory.md`, monthly summaries, prompt bundle | Directory indexes, generated reports, reviews, source snapshots, validation output |
| Behavioral authority | Prompt injection and strict memory policy instruct future pi agents | AGENTS.md, collection rules, type specs, validators, skills, and review gates |
| Governance | LLM JSON parsing, exact-text dedupe, scoring, git commits, manual commands | Schemas, deterministic validation, semantic review, curated links, lifecycle states |
| Learning target | Prose mistake/fix rules and ranked reminders | Notes, instructions, skills, scripts, validators, indexes, and reviewed methodology |

The strongest alignment is filesystem-first trace-derived learning. Pi Self-Learning keeps durable memory as files, initializes a git repo, and makes the retained artifacts inspectable. It also shares commonplace's concern with behavioral activation: memory matters because `CORE.md`, daily files, monthly summaries, and strict-mode policy enter the next prompt before the agent repeats a mistake.

The main divergence is artifact contract strength. Pi Self-Learning treats every extracted mistake or fix as acceptable memory once the LLM output parses. There is no source pointer back to a concrete transcript segment, no reviewer state, no confidence field, no schema validation beyond JSON shape, no stale/superseded lifecycle, and no promotion path into tests, scripts, skills, or stronger instructions. Commonplace is heavier because it asks whether a retained artifact should advise, instruct, route, validate, or be retired.

Pi Self-Learning is also much narrower than a KB. It is excellent at "avoid repeating the thing that just went wrong." It is not meant to preserve design rationale, build arguments, connect notes, compare systems, or manage source evidence. The narrowness is part of why it can run automatically: the extraction oracle only has to decide mistakes and fixes from a recent trace.

The runtime/tool surface is tighter than commonplace's command set. Pi users get slash commands and transparent hook behavior inside one agent runtime. Commonplace is more portable across shells and agents, but the pi extension has better timing: it can inject memory at `before_agent_start` and reflect at `agent_end` without asking the agent to remember a separate procedure.

**Read-back:** both — agents can pull memory through slash commands and files, while `before_agent_start` injects ranked core, daily, and monthly context.

## Borrowable Ideas

**Treat interruptions as feedback, not errors.** Commonplace trace workflows should preserve blocked commands, permission denials, user aborts, and skipped tools as first-class learning signals. This is ready now for review and warning workflows where user interruption often means "your plan crossed a boundary."

**Make the first trace-derived schema narrow.** The `mistakes` and `fixes` pair is not a full knowledge model, but it is easy to prompt, parse, rank, and inject. A commonplace workshop command could use a similarly narrow schema for end-of-task prevention notes before attempting broader synthesis.

**Separate canonical scored state from rendered prompt views.** Pi Self-Learning's `index.json` as canonical state and `CORE.md` as a rendered top-N view is a good pattern for any future commonplace runtime memory. The rendered view should be regenerated and clearly subordinate to the source index.

**Use balanced ranking for negative and positive reminders.** Reserving room for both learnings and watch-outs avoids a common failure where only one category dominates the prompt. The mechanism is simple enough to borrow if commonplace adds scored reminder surfaces.

**Keep automatic memory non-blocking.** Reflection failures, model auth failures, malformed output, and git commit failures should not break the user's main task. The extension's defensive parsing and graceful skips are appropriate for a background learning loop.

**Do not stop at relocation.** The system mostly moves extracted strings through daily files, a scored index, and prompt views. Commonplace should borrow the capture mechanics but require promotion criteria before a repeated reminder becomes an instruction, skill, validator, or design note.

## Trace-derived learning placement

Pi Self-Learning qualifies as trace-derived learning. It consumes live agent-session traces and distills them into durable prose artifacts that can shape later agent behavior through prompt injection and strict memory policy.

**Trace source.** The raw source trace is the current pi branch: recent messages selected by `getBranchMessages`, serialized conversation text, and interruption signals from recent branch entries. The trigger boundary is task completion via `agent_end` when automatic reflection is enabled, or manual invocation via `/learning-now` ([extensions/self-learning.ts](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/extensions/self-learning.ts)).

**Extraction.** The extraction oracle is an LLM selected from configuration or the current pi session model. The prompt asks for strict JSON with `mistakes` and `fixes`, uses storage mode to choose project-specific or cross-project wording, and treats interruption signals as user-boundary evidence. If the first output does not parse, a repair prompt asks the same model to convert it into the required JSON shape ([extensions/self-learning.ts](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/extensions/self-learning.ts)).

**Storage substrate.** Raw branch traces remain in pi's session machinery, not in the Pi Self-Learning memory tree. Daily reflections live in markdown under `daily/YYYY-MM-DD.md`. The canonical durable ranking store is `core/index.json`. `core/CORE.md` and `long-term-memory.md` are markdown renderings from the index. Monthly summaries live under `monthly/YYYY-MM.md`. The whole memory root can be its own git repository, initialized and committed by the extension ([README.md](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/README.md), [extensions/self-learning.ts](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/extensions/self-learning.ts)).

**Representational form.** Raw traces are mixed pi session objects and serialized prose. Daily, core, long-term, and monthly artifacts are prose. `core/index.json` is mixed: prose item text plus symbolic keys, kinds, hit counts, scores, first/last seen timestamps, and version metadata. The ranking algorithm is symbolic. No embeddings, learned weights, vector index, or model fine-tune are retained.

**Lineage.** Lineage is shallow. Daily entries include UTC date/time headings and preserve extracted text, and `core/index.json` stores first/last seen timestamps and recurrence counts. Git history can show memory-file changes. But core items do not retain pointers to the exact source messages, tool results, model output, model ID used for each extraction, or parse/repair provenance. `CORE.md` and `long-term-memory.md` are derived views from `core/index.json`; monthly summaries are derived from daily files.

**Behavioral authority.** Raw traces are evidence. Daily files, monthly files, and long-term memory are knowledge artifacts when read as context or history. `core/index.json` becomes a system-definition artifact while it ranks what gets rendered into `CORE.md`. The injected context bundle is knowledge-artifact content, while strict-mode memory instructions are system-definition artifacts because they instruct the assistant to consult specific files and prefer memory evidence over guessing.

**Scope.** Project mode is per-repository and may keep local names. Global mode is cross-project and asks the model to rewrite details into reusable action rules. `/learning-redistill` exists specifically to migrate existing global core entries toward cross-project wording, with optional dry-run, limit, chunked model calls, dedupe, and git commit ([extensions/self-learning.ts](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/extensions/self-learning.ts)).

**Timing.** Capture is online at task end or manual command time. Activation is online before agent start. Monthly summarization and redistill are staged maintenance commands. The loop is therefore live enough to affect the next task, but maintenance and migration still depend on explicit commands.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), Pi Self-Learning is the clean branch-event-to-prose-memory case: online trace ingestion, narrow mistake/fix extraction, scored flat rule memory, rendered prompt view, and optional cross-project redistillation. It strengthens the survey's claim that trace-derived artifact learning does not require a database or vector store. It also splits the "distillation" claim: capture-time extraction and redistill perform real rewriting, but the daily/core/long-term pipeline mostly ranks and relocates extracted strings rather than synthesizing a richer knowledge artifact.

## Curiosity Pass

**The system's core mechanism is smaller than its file hierarchy.** Daily files, monthly files, core markdown, long-term markdown, git commits, and slash commands make the system feel like a full memory hierarchy. Mechanically, the main loop is recent trace text to JSON arrays to a scored flat list.

**`core/index.json` is more authoritative than `CORE.md`.** The README foregrounds `CORE.md`, but the code renders it from the index. Any review or migration should inspect `core/index.json` first because it carries recurrence, score, kind, and timestamps.

**Global mode is a second distillation problem.** Project mode can preserve concrete details, but global mode needs to strip repository identifiers while preserving the prevention intent. The redistill command acknowledges that old global entries may contain project-specific wording and provides a migration path, which is stronger than pretending prompt wording alone solves the problem.

**The model selector surface has one odd gap.** `/learning-model` writes a branch runtime model override, and `/learning-status` reports that runtime `/learning-model` override is currently ignored for reflection when present. Configured model and current session model are the actual reflection resolution path in the inspected code ([extensions/self-learning.ts](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/extensions/self-learning.ts)). That is either a deliberate UI distinction or a behavior mismatch to watch.

**Validation is manual and host-dependent.** The package manifest exposes the TypeScript file directly as the extension entry and declares pi as a peer dependency, but there are no build, lint, or test scripts. The repo's AGENTS file explicitly says there is no automated test suite and to validate manually inside pi with `/learning-status`, `/learning-now`, `/learning-month`, and `/learning-redistill` ([AGENTS.md](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/AGENTS.md), [package.json](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/package.json)).

## What to Watch

- Whether Pi Self-Learning stores source pointers, source excerpts, model IDs, or extraction diagnostics for each core item.
- Whether the memory repo gains validation for malformed `index.json`, stale `CORE.md`, oversized prompt bundles, or contradictory learnings.
- Whether rare high-severity failures can be pinned despite score, hit-count, and recency ranking favoring repetition.
- Whether `/learning-model` branch overrides become part of reflection model resolution or the status warning remains.
- Whether monthly summaries and redistill become routine activation surfaces or stay as maintenance commands users rarely run.
- Whether the project adds automated tests around hook timing, path resolution, model fallback, git failures, and redistill dry-run behavior.

---

Relevant Notes:

- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: daily, monthly, and long-term memory files advise future agents as retained evidence and history.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: strict memory policy and ranked prompt views can instruct, route, and rank future behavior.
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) - sharpens: the same extracted sentence can advise as a daily note or steer behavior when injected by strict policy.
- [Lineage](../../notes/definitions/lineage.md) - frames: rendered memory files are derived from traces and `core/index.json`, but source-message lineage is shallow.
- [Distillation](../../notes/definitions/distillation.md) - distinguishes: capture/redistill rewrite traces into rules, while much of the hierarchy is ranking and rendering.
- [Memory management policy is learnable but oracle-dependent](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) - explains: the learning loop's quality depends on the LLM extraction oracle and prompt scope.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: Pi Self-Learning turns task traces and interruptions into future mistake-prevention memory.
