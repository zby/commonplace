---
description: "pi-self-learning review: Pi extension that distills task traces into git-backed daily, core, monthly, and injected memory files"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-06-02"
---

# pi-self-learning

pi-self-learning, by Matteo Collina, is a Pi coding-agent extension that adds self-learning memory to a running Pi agent. It listens for task completion, reflects on recent branch conversation and interruption signals, writes the result into a git-backed memory folder, maintains ranked durable learnings, can generate monthly summaries, and injects configured memory files plus memory-use policy into future agent starts.

**Repository:** https://github.com/mcollina/pi-self-learning

**Reviewed commit:** [b1add8631cb621bc2caba3c9f70376dcddf6ca36](https://github.com/mcollina/pi-self-learning/commit/b1add8631cb621bc2caba3c9f70376dcddf6ca36)

**Last checked:** 2026-06-02

## Core Ideas

**The system is a single host extension around Pi lifecycle hooks.** The package manifest points Pi at `extensions/self-learning.ts`, and the implementation registers `agent_end` and `before_agent_start` hooks plus slash commands such as `/learning-now`, `/learning-month`, `/learning-redistill`, `/learning-toggle`, and model-selection commands ([package.json](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/package.json), [extensions/self-learning.ts](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/extensions/self-learning.ts)). It is not a separate memory server; its authority comes from the Pi extension API and local filesystem/git side effects.

**Task-end reflection is the learning boundary.** On `agent_end`, when enabled and automatic reflection is on, the extension gathers recent branch messages, serializes the conversation, collects interruption signals, asks an LLM for strict JSON `mistakes` and `fixes`, appends a daily markdown entry, updates the ranked core index and rendered memory files, and optionally commits those files in the memory repository ([extensions/self-learning.ts](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/extensions/self-learning.ts)). Reflection failures are swallowed so memory cannot break normal agent flow.

**User interruptions are treated as signal, not noise.** The implementation scans recent tool results and assistant stop reasons for blocked commands, permission denials, skipped tools after queued user messages, and aborted assistant responses. When such signals exist, the reflection prompt tells the model to treat them as intentional user-boundary evidence and produce prevention-oriented mistakes and fixes ([extensions/self-learning.ts](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/extensions/self-learning.ts)).

**Durable memory is a small scored core rendered from a fuller trace log.** Daily files preserve task-level reflections; `core/index.json` is the canonical scored record with `kind`, `hits`, `score`, `firstSeen`, and `lastSeen`; `core/CORE.md` renders a balanced top set of learnings and watch-outs; `long-term-memory.md` renders the complete ranked history. Ranking favors score, repeated hits, and recency, with a light age penalty and reserved representation for both learnings and anti-patterns ([extensions/self-learning.ts](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/extensions/self-learning.ts), [README.md](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/README.md)).

**Memory is git-backed by default.** The storage root defaults to `.pi/self-learning-memory` in project mode or `~/.pi/agent/self-learning-memory` in global mode. The extension initializes a git repo there, writes a README and long-term memory file on first use, stages only memory-relative paths for each update, and commits task, monthly, and redistillation changes when git auto-commit is enabled ([extensions/self-learning.ts](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/extensions/self-learning.ts), [docs/example-settings.json](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/docs/example-settings.json)).

**Context efficiency is file-level and truncation-based.** The injected context builder can include `CORE.md`, optional latest monthly summary, optional last N daily files, and recent in-memory notes, then caps the whole bundle with `context.maxChars` and each file to roughly a quarter of that budget. There is no semantic retrieval, embedding search, or relevance classifier in the inspected implementation; efficiency comes from durable-core distillation, configurable inclusion flags, and character truncation ([extensions/self-learning.ts](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/extensions/self-learning.ts)).

**Global memory can be redistilled into cross-project rules.** In global storage mode, `/learning-redistill` rewrites selected core entries into concise reusable action rules, removes project-specific identifiers, repairs malformed JSON outputs, merges deduplicated records, rewrites `CORE.md`, `long-term-memory.md`, and `core/index.json`, and commits the result. The command intentionally refuses project mode because the rewrite target is global reusable behavior ([extensions/self-learning.ts](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/extensions/self-learning.ts), [README.md](https://github.com/mcollina/pi-self-learning/blob/b1add8631cb621bc2caba3c9f70376dcddf6ca36/README.md)).

## Artifact analysis

- **Storage substrate:** `service-object` — Pi session branch entries at runtime, not pi-self-learning's durable store
- **Representational form:** `prose` `symbolic` — serialized conversation prose, markdown memory files, JSON score records, git history, hook return values, and structured Pi message/tool/stop-reason objects
- **Lineage:** `trace-extracted` — durable memory is derived from branch conversation, interruption signals, task-end reflection, monthly summarization, and global redistillation
- **Behavioral authority:** `knowledge` `instruction` `ranking` `learning` — traces and markdown files are evidence/context, strict mode adds memory-use policy, `core/index.json` ranks durable memory, and reflected records feed later summaries and redistillation

**Branch conversation and interruption signals.** Storage substrate: Pi session branch entries at runtime, not pi-self-learning's durable store. Representational form: mixed message objects, tool result text, assistant stop reasons, and serialized conversation prose. Lineage: captured from the current branch shortly before reflection; the extension samples only recent messages and scans a wider recent window for interruption signals. Behavioral authority: knowledge artifacts during reflection, because they are evidence for the LLM extraction oracle; they do not directly instruct future agents until distilled.

**Daily reflection files.** Storage substrate: markdown files under `daily/YYYY-MM-DD.md` inside the configured memory root. Representational form: prose sections for "What went wrong" and "How it was fixed", organized by UTC task time. Lineage: trace-derived from recent branch messages plus interruption signals through an LLM JSON reflection and markdown renderer. Behavioral authority: knowledge artifacts as historical evidence; they can become prompt context only when `includeLastNDaily` is configured or when a user/agent explicitly opens them.

**Core index and rendered core memory.** Storage substrate: `core/index.json`, `core/CORE.md`, and `long-term-memory.md` in the memory root. Representational form: mixed symbolic/prose: JSON records are the canonical scored index, while markdown files are rendered views. Lineage: derived from reflected fixes and mistakes, with duplicate keys, hit counts, scores, first/last seen timestamps, and light recency decay; `CORE.md` and `long-term-memory.md` regenerate from `core/index.json`. Behavioral authority: `core/index.json` has ranking/selection authority for durable memory; `CORE.md` and long-term memory are knowledge artifacts when read, and advisory system-definition context when injected before agent start.

**Monthly summaries.** Storage substrate: markdown files under `monthly/YYYY-MM.md`. Representational form: LLM-generated prose with sections requested by the month prompt. Lineage: derived from all daily files for a given month through `/learning-month`; empty months produce no summary, and generation skips if no usable reflection model is available. Behavioral authority: knowledge artifact by default, with advisory context authority only when `includeLatestMonthly` is enabled or the file is manually consulted.

**Memory git repository.** Storage substrate: a git repository initialized inside the memory root. Representational form: symbolic version history around markdown and JSON memory files. Lineage: commits are generated after initialization, task reflection, monthly summary, or redistillation operations. Behavioral authority: audit, rollback, and review support rather than direct model instruction; it strengthens trust in memory changes but does not itself decide what reaches context.

**Before-start context bundle and system prompt policy.** Storage substrate: in-memory hook return values from `before_agent_start`. Representational form: prose context blocks and prose policy appended to the system prompt. Lineage: assembled from recent runtime notes, configured memory files, resolved filesystem paths, and current config. Behavioral authority: advisory context plus, in strict mode, instruction-like policy telling the assistant when and where it must consult memory for history-related questions. Effective faithfulness is not verified from code; the hook can place memory and policy into context, but it does not test whether the receiving model follows it.

Promotion path: pi-self-learning has a clear raw-trace -> daily reflection -> scored durable core -> rendered prompt context path. It can also redistill global core entries into more generic action rules. The promotion path remains prose/symbolic and git-readable; it does not promote into validators, tools, route tables, embeddings, or model weights.

## Comparison with Our System

| Dimension | pi-self-learning | Commonplace |
|---|---|---|
| Primary purpose | Improve one Pi agent's future behavior from its own task traces | Maintain a typed methodology KB for agents and maintainers |
| Storage substrate | Local memory folder with markdown, JSON, and git history | Git-tracked KB markdown, schemas, type specs, indexes, reports, sources |
| Canonical retained unit | Daily reflections and scored core memory records | Typed notes, reviews, instructions, ADRs, sources, generated indexes |
| Learning loop | Automatic LLM reflection after task end; optional monthly and global redistillation | Deliberate source-grounded writing, validation, semantic review, and workshop promotion |
| Read-back | Always-load configured memory and policy before agent start; pull slash commands for manual reflection/status/files | Mostly deliberate pull through `rg`, indexes, links, skills, and explicit instructions |
| Governance | Git commits and inspectable files, but weak schema/semantic gates | Collection contracts, type schemas, deterministic validation, review gates, source citations |

pi-self-learning is smaller and more directly behavioral than Commonplace. It is not trying to build a browsable knowledge base; it is trying to close a loop from "the agent made a mistake or was interrupted" to "future starts include a compact memory of what to avoid." Its best design move is keeping the learned surface local, readable, and git-versioned instead of hiding it in a service or vector store.

The main divergence is authority control. Commonplace makes promotion explicit: a source can become a note, an instruction, a type spec, or a validator only through a visible artifact boundary. pi-self-learning promotes automatically after every task when enabled. That is useful for rapid adaptation, but it gives LLM-reflected prose a short path into future prompt context with no deterministic validation beyond JSON parse/repair and no semantic review gate.

**Read-back:** `both` — Manual commands such as `/learning-now`, `/learning-daily`, `/learning-status`, `/learning-month`, and `/learning-redistill` are pull surfaces. The `before_agent_start` hook pushes retained memory into the receiving agent's context, but targeting is `coarse` and signal is n/a: selection is session-start/config-flag/recency loading of recent runtime notes plus configured core, daily, and monthly memory files, not instance relevance. The appended memory policy is baseline instruction, not memory read-back, and this review does not assign `push-activation`.

**Read-back signal:** `coarse` — push read-back is session-start/config-flag/recency loading of recent runtime notes plus configured core, daily, and monthly memory files, not instance relevance.

**Read-back timing:** `pre-action` — the `before_agent_start` hook injects retained memory before the receiving agent starts its next task.

**Faithfulness tested:** `no` — the review states effective faithfulness is not verified from code and does not report a with/without behavior ablation for injected memory.

### Borrowable Ideas

**Treat interruption as learning signal.** Commonplace review and agent-operation workflows could preserve "user stopped me here" as first-class evidence rather than discarding it as noise. Ready for review reports and work logs, especially around permission denials and direction changes.

**Keep generated memory git-native.** pi-self-learning's memory root is simple but strong: markdown/JSON plus git commits. Commonplace should prefer this kind of inspectable substrate for any generated operational memory before considering service or vector-store state.

**Use a scored core beside full history.** A Commonplace analogue would keep full traces or workshop logs separate from a small ranked "operational lessons" view. Ready as a workshop experiment; needs careful promotion rules before loading into global instructions.

**Render prompt memory from a canonical index.** `CORE.md` is not the source of truth; it is a rendered view from `core/index.json`. Commonplace generated context bundles could use the same split: symbolic selection record first, prose render second.

**Redistill global lessons separately from project lessons.** The project/global storage-mode split is a useful guardrail. Commonplace should not automatically turn project-specific fixes into framework-wide instructions without a redistillation and review step.

**Do not borrow unconditional injection as the final read-back design.** The always-load hook is pragmatic for a small personal memory, but Commonplace would need relevance gates, scope checks, and faithfulness tests before pushing memory into agent context by default.

## Trace-derived learning placement

**Trace source:** `session-logs` `tool-traces` `event-streams` — task-end reflection consumes recent Pi branch messages, serialized conversation text, tool result errors, assistant stop/skip signals, and lifecycle/interruption signals.

**Learning scope:** `per-task` `per-project` `cross-task` — reflections are task-level, storage mode scopes memory to a project or global root, and global redistillation produces cross-project reusable rules.

**Learning timing:** `online` `staged` — reflection can run after each `agent_end`, while durable behavior changes are written/committed after the task and injected on a later `before_agent_start`.

**Distilled form:** `prose` `symbolic` — daily, monthly, core, long-term, and redistilled memory are prose renders, while `core/index.json` is the canonical scored symbolic record.

**Trace source.** pi-self-learning qualifies as trace-derived learning. The raw traces are recent Pi branch messages, serialized conversation text, tool result errors, assistant abort stop reasons, queued-user-message skips, and related interruption signals collected around task end.

**Extraction.** Extraction is LLM-mediated. The reflection prompt asks for strict JSON with `mistakes` and `fixes`, focuses on prevention rather than accomplishment summaries, and changes wording rules by storage mode: project mode may keep repository-specific detail, while global mode must distill cross-project reusable rules. A repair prompt and fallback JSON extraction handle malformed output; if parsing still fails, the reflection is skipped.

**Four-field placement.** Raw branch messages and interruption signals are runtime knowledge artifacts. Daily entries are trace-derived prose knowledge artifacts. `core/index.json` is a trace-derived symbolic ranking artifact, and `CORE.md` plus `long-term-memory.md` are rendered prose views with advisory context authority when injected. Monthly summaries and redistilled global entries are second-stage derived artifacts from earlier trace-derived memory.

**Scope and timing.** Scope is project or global by storage mode, with project roots resolved from `.pi/settings.json` or git ancestry. Reflection happens after `agent_end`; it affects only later starts. Monthly summary and global redistillation are manual commands. The loop is online enough to run after each task, but the durable behavior change is staged: trace now, reflect/write/commit after task, inject on a later `before_agent_start`.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), pi-self-learning sits in the trace-to-prose-rule family. It strengthens the survey split between trace retention and behavior-shaping distillation: raw conversation is not loaded by default, while reflected learnings, watch-outs, and redistilled core rules are the behavior-shaping outputs.

## Curiosity Pass

**The read-back is push but not selective.** From the agent's perspective, memory arrives unsolicited before start. From a context-engineering perspective, the selector is mostly configuration, file recency, and truncation. That is enough for a small personal memory, but it is not a relevance gate.

**`injectLastN` and `includeLastNDaily` are different memory paths.** `injectLastN` loads short in-process runtime notes from the current extension process; `includeLastNDaily` reads daily markdown files from disk. The README emphasizes file context, but the implementation also has this small transient note channel.

**The strongest canonical artifact is JSON, not Markdown.** `CORE.md` is what the model sees, but `core/index.json` carries scores, hits, timestamps, and kind. Reviewers should treat the markdown as a rendered prompt surface, not the whole memory.

**Strict policy is narrower than general instruction authority.** Strict mode tells the assistant to consult memory for history, prior decisions, patterns, regressions, or follow-up work. It does not require obeying every learning as a rule for all tasks.

**The git story is local and useful but isolated.** The memory repo gives audit and rollback inside the memory root, but those commits are separate from the project repo and from any review workflow unless a user inspects or exports them.

**There are no automated tests in the repository.** `AGENTS.md` says behavior is validated manually in Pi with extension commands. That matters because hook timing, model registry compatibility, and context injection are host-dependent.

## What to Watch

- Whether pi-self-learning adds semantic or task-state relevance gating before injecting memory, rather than always loading configured files.
- Whether core memory gains review or approval states before reflected lessons enter prompt context.
- Whether the git-backed memory repo gets export/import or diff tooling that makes learned behavior easy to inspect outside Pi.
- Whether global redistillation starts preserving stronger lineage from rewritten rule back to original core entries and daily evidence.
- Whether monthly summaries become part of the default injected context; that would raise context dilution risk without a stronger selector.
- Whether future versions add tests for hook behavior, model fallback, malformed model outputs, and memory file migrations.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: pi-self-learning distills task traces and interruption signals into daily reflections, scored core records, and redistilled global rules.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - exemplifies: stored memory files affect behavior only through before-start injection, strict policy, or explicit command/file access.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: pi-self-learning separates raw traces, daily reflections, scored indexes, rendered views, git history, and hook-injected context by substrate, form, lineage, and authority.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: the system turns mistakes, fixes, and interruption signals into future behavior guidance.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - defined-in: daily logs, monthly summaries, long-term memory, and raw traces are consumed as evidence or historical context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - defined-in: scored indexes, rendered prompt bundles, strict memory policy, and git-backed memory updates can select, instruct, or audit future behavior.
