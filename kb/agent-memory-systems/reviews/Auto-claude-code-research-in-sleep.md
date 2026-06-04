---
description: "ARIS review: Markdown research-skill harness with Research Wiki, cross-model review gates, traces, run state, queues, hooks, and meta-optimization"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived, push-activation]
status: current
last-checked: "2026-06-01"
---

# ARIS / Auto-claude-code-research-in-sleep

ARIS, from wanshuiyin's `Auto-claude-code-research-in-sleep`, is a research workflow harness built mostly from Markdown skills, Python helper scripts, MCP reviewer bridges, optional Claude Code hooks, and plain-file project artifacts. Its main audience is an agent running ML research workflows: literature survey, idea generation, experiment planning, remote execution, review loops, paper writing, rebuttal, resubmission, and harness self-improvement. The memory story is not a single database; it is a set of retained artifacts that keep research context, claims, failures, traces, run state, reviewer verdicts, and skill-corpus changes available to later agent actions.

**Repository:** https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep

**Reviewed commit:** [665a238fda5d46259cb99d329a89772886e76da0](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/commit/665a238fda5d46259cb99d329a89772886e76da0)

## Core Ideas

**Skills are the primary executable memory interface.** ARIS tells agents that behavior lives in `skills/<name>/SKILL.md`, with `AGENT_GUIDE.md` only as a routing index ([AGENT_GUIDE.md](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/665a238fda5d46259cb99d329a89772886e76da0/AGENT_GUIDE.md)). A skill package is a mixed retained artifact: prose procedure, symbolic frontmatter, shell blocks, helper-resolution contracts, output protocols, and authority boundaries. Once installed into a project through symlinked `.claude/skills/<skill>`, those files become system-definition artifacts because the host agent consumes them as command procedures, not as background documentation ([tools/install_aris.sh](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/665a238fda5d46259cb99d329a89772886e76da0/tools/install_aris.sh)).

**The Research Wiki is a file-backed project memory with a compiled query pack.** `/research-wiki` creates `research-wiki/` with `papers/`, `ideas/`, `experiments/`, `claims/`, `graph/edges.jsonl`, `index.md`, `log.md`, `gap_map.md`, and `query_pack.md` ([skills/research-wiki/SKILL.md](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/665a238fda5d46259cb99d329a89772886e76da0/skills/research-wiki/SKILL.md), [tools/research_wiki.py](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/665a238fda5d46259cb99d329a89772886e76da0/tools/research_wiki.py)). The key context-engineering move is `query_pack.md`: a deterministic, bounded summary assembled from project direction, gaps, failed ideas, papers, and recent graph edges. `/idea-creator` reads the pack when fresh and treats failed ideas as a banlist and gaps as search seeds before doing new literature search ([skills/idea-creator/SKILL.md](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/665a238fda5d46259cb99d329a89772886e76da0/skills/idea-creator/SKILL.md)).

**Cross-model review is the recurring governance mechanism.** ARIS routes many decisions through a non-executor reviewer: idea triage, auto-review loops, result-to-claim judgment, paper audits, kill-argument checks, render fidelity review, and meta-optimization review. The agent guide makes reviewer independence explicit and stores reviewer traces under `.aris/traces/<skill>/<date>_run<NN>/` ([AGENT_GUIDE.md](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/665a238fda5d46259cb99d329a89772886e76da0/AGENT_GUIDE.md), [tools/save_trace.sh](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/665a238fda5d46259cb99d329a89772886e76da0/tools/save_trace.sh)). `auto-review-loop` persists `review-stage/REVIEW_STATE.json`, cumulative raw reviewer responses, optional reviewer memory, debate transcripts, and final method descriptions so long-running review survives compaction and later paper-writing stages ([skills/auto-review-loop/SKILL.md](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/665a238fda5d46259cb99d329a89772886e76da0/skills/auto-review-loop/SKILL.md)).

**Acceptance is split from execution.** `run_state.py` models multi-phase workflows with `done` for executor completion and `accepted` only after a cross-model reviewer or deterministic verifier records a verdict id and reviewer; resume targets any `done` but unaccepted phase ([tools/run_state.py](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/665a238fda5d46259cb99d329a89772886e76da0/tools/run_state.py)). This is a concrete behavioral-authority distinction: the executor may report that it wrote an artifact, but the artifact does not advance the pipeline until a separate authority acquits it.

**Meta-optimization turns usage traces into staged corpus patches.** Optional hooks write Claude Code events to `.aris/meta/events.jsonl` and `~/.aris/meta/events.jsonl`; a `SessionEnd` readiness check suggests `/meta-optimize` after at least five new skill invocations ([templates/claude-hooks/meta_logging.json](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/665a238fda5d46259cb99d329a89772886e76da0/templates/claude-hooks/meta_logging.json), [tools/meta_opt/log_event.sh](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/665a238fda5d46259cb99d329a89772886e76da0/tools/meta_opt/log_event.sh), [tools/meta_opt/check_ready.sh](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/665a238fda5d46259cb99d329a89772886e76da0/tools/meta_opt/check_ready.sh)). `/meta-optimize` is a read-only producer: it analyzes event logs, proposes patches under `.aris/meta/pending/`, and requires `/meta-apply` to run a fresh cross-model jury at landing before mutating the skill corpus ([skills/meta-optimize/SKILL.md](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/665a238fda5d46259cb99d329a89772886e76da0/skills/meta-optimize/SKILL.md), [skills/meta-apply/SKILL.md](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/665a238fda5d46259cb99d329a89772886e76da0/skills/meta-apply/SKILL.md)).

**Overnight work is orchestrated by stateful queues and monitors, not only prompts.** `/experiment-queue` launches a detached scheduler on the SSH host, expands manifests, retries OOM jobs, cleans stale screens, observes phase dependencies, and writes `queue_state.json` continuously ([skills/experiment-queue/SKILL.md](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/665a238fda5d46259cb99d329a89772886e76da0/skills/experiment-queue/SKILL.md), [skills/experiment-queue/scripts/queue_manager.py](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/665a238fda5d46259cb99d329a89772886e76da0/skills/experiment-queue/scripts/queue_manager.py)). ARIS-Monitor separately scans Claude Code session registry files and transcript tails read-only to surface sessions waiting for user approval or stalled mid-tool ([aris-monitor/scanner.py](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/665a238fda5d46259cb99d329a89772886e76da0/aris-monitor/scanner.py)).

## Artifact analysis

- **Storage substrate:** `files` — The repository filesystem under `skills/`, mirrored into target projects as symlinked `.claude/skills/` entries by `install_aris.sh`
- **Representational form:** `prose` `symbolic` — Prose procedures, Markdown reports, and textual reminders plus symbolic frontmatter, JSON/JSONL state, shell snippets, diffs, hook configuration, and resolver contracts
- **Lineage:** `authored` `imported` `trace-extracted` — Authored skill corpus and project notes, imported literature/project metadata, and trace-derived reviewer, run, hook, queue, and meta-optimization records
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `learning` — Wiki pages and traces provide evidence; skills instruct; guards, verdicts, and acceptance states enforce or validate; run/queue/query-pack state routes work; meta-optimization turns traces into proposed skill changes

**Skill corpus.** Storage substrate is the repository filesystem under `skills/`, mirrored into target projects as symlinked `.claude/skills/` entries by `install_aris.sh`. Representational form is mixed: prose procedures, symbolic frontmatter, shell snippets, and resolver contracts. Lineage is authored, with helper drift checks and install manifests but not a generated build graph for every skill. Behavioral authority is system-definition authority: skills instruct the agent, route tools, define gates, name outputs, and constrain what counts as completion.

**Research Wiki.** Storage substrate is project-local files under `research-wiki/`. Representational form is mixed: Markdown pages, YAML-ish frontmatter, JSONL graph edges, append-only logs, and compiled Markdown `query_pack.md`. Lineage is partly authored and partly imported or derived: arXiv metadata, manually supplied theses, generated slugs, deterministic indexes, deterministic query-pack slices, and edges added by skills. Behavioral authority varies by consumption path. Paper pages and logs are knowledge artifacts when read as evidence; `graph/edges.jsonl`, failed-idea entries, claim statuses, and `query_pack.md` become system-definition artifacts when `/idea-creator` uses them to ban repetition, seed search, or condition candidate generation.

**Reviewer traces and review state.** Storage substrate is `.aris/traces/`, `review-stage/AUTO_REVIEW.md`, `review-stage/REVIEW_STATE.json`, `REVIEWER_MEMORY.md`, and sidecar review JSONs. Representational form is prose plus symbolic JSON state. Lineage is trace-derived: prompts, raw responses, thread ids, verdicts, and round state are retained from reviewer interactions. Behavioral authority is mixed. Raw traces are knowledge artifacts for audit and replay; `REVIEW_STATE.json`, reviewer memory, and accepted verdict ids are system-definition artifacts because they resume loops, carry reviewer suspicions, and authorize workflow progression.

**Run state and experiment queue state.** Storage substrate is `.aris/runs/<run_id>.json` locally and remote `~/.aris_queue/runs/<run_ts>/queue_state.json` plus logs. Representational form is symbolic JSON plus shell-visible metadata. Lineage is operational: phase status derives from workflow execution, deterministic verifiers, reviewer verdict handles, scheduler polling, GPU/log observations, and user or agent launches. Behavioral authority is routing and enforcement: resume points, accepted/skipped terminal states, job retry, phase transition, and stuck-job classification shape what the next agent or scheduler does.

**Meta-optimization artifacts.** Storage substrate is `.aris/meta/events.jsonl`, `~/.aris/meta/events.jsonl`, `.aris/meta/pending/*.diff`, pending manifests, backups, provenance stamps, and optimization logs. Representational form is JSONL events, unified diffs, Markdown reports, and provenance metadata. Lineage is trace-derived from hook events, skill invocations, failures, user prompts, and reviewer calls. Behavioral authority is deliberately staged: event logs are knowledge artifacts for analysis; pending diffs are candidate system-definition artifacts; landed patches become system-definition artifacts only through `/meta-apply` after a fresh jury and human invocation.

**Hook and monitor outputs.** Storage substrate is Claude Code settings hooks, shell scripts, live `~/.claude/sessions/*.json`, transcript JSONL tails, and emitted hook messages. Representational form is symbolic hook configuration, shell/Python code, and short textual reminders. Lineage is live runtime state and retained project status. Behavioral authority ranges from advisory context injection to hard-ish hook denial: `corpus_write_guard.py` returns exit 2 to block common Bash writes to the skill corpus, while session recovery and meta-readiness hooks surface reminders that the agent may act on ([templates/claude-hooks/corpus_write_guard.py](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/665a238fda5d46259cb99d329a89772886e76da0/templates/claude-hooks/corpus_write_guard.py), [docs/SESSION_RECOVERY_GUIDE.md](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/665a238fda5d46259cb99d329a89772886e76da0/docs/SESSION_RECOVERY_GUIDE.md)).

Promotion paths are explicit in several places. Research findings move from logs/results into claims, idea outcomes, and query-pack steering. Reviewer responses move into state files, memory, and accepted verdict ids. Meta events move into proposed patches, then into skill-corpus changes only after a separate landing gate. This makes ARIS stronger than prompt-only skill packs: it has retained artifacts that can change later behavior with named authority transitions.

### Borrowable Ideas

**Split executor completion from acceptance.** Commonplace should consider a `done` versus `accepted` distinction for long review or migration runs. A worker can finish writing an artifact, but a deterministic validator or review gate should be the entity that marks it accepted. Ready now as vocabulary; implementation should wait for a concrete multi-phase workflow.

**Compile task-specific query packs.** ARIS's `query_pack.md` is a practical pattern: bounded, deterministic, stale-aware context assembled from short fields before ideation. Commonplace could compile per-task packs from descriptions, indexes, open warnings, recent review findings, and selected notes. Ready for experiments in workshops, not as a default global layer.

**Treat failed ideas as anti-repetition memory.** ARIS preserves negative results and failed ideas as high-value steering material. Commonplace could use the same pattern for rejected KB designs or failed note structures: store why they failed, then surface them during nearby design work to avoid rediscovery.

**Keep meta-optimization producer and applier separate.** The `/meta-optimize` and `/meta-apply` split is worth borrowing: trace-derived proposals may drive change, but the landing authority sits in a distinct, human-invoked, reviewer-gated path. Commonplace's review auto-fix machinery should maintain the same boundary before any agent-generated rule change becomes system definition.

**Use hooks as advisory activation, and label them honestly.** ARIS distinguishes reminders, readiness nudges, and blocking corpus-write guards. Commonplace can borrow the classification: some hooks inject context, some advise, and only some enforce. The behavioral authority should be named at the hook boundary.

**Do not borrow the whole research harness shape.** ARIS's breadth is useful for its domain, but Commonplace should not absorb GPU queues, paper-writing workflows, provider routing, or release-product affordances unless a KB-maintenance use case requires them.

## Comparison with Our System

| Dimension | ARIS | Commonplace |
|---|---|---|
| Primary purpose | Run autonomous research workflows and improve a research harness | Build and maintain an agent-operated methodology KB |
| Primary substrate | Markdown skills, project files, Python helpers, hooks, JSON/JSONL state, MCP bridges | Typed Markdown collections, schemas, indexes, review reports, Python validators |
| Memory unit | Research Wiki pages, query packs, review traces, run states, queue states, skill patches | Notes, references, instructions, reviews, sources, generated indexes, review decisions |
| Activation | Slash-command skills, compiled query-pack preload, run-state resume, hooks, monitors, schedulers | `rg`, descriptions, indexes, links, skills, validation and review commands |
| Governance | Cross-model reviewer gates, deterministic evidence prechecks, accept-vs-done split, meta-apply landing gate | Type specs, collection contracts, validation, semantic review bundles, git review |
| Learning loop | Failed ideas, result-to-claim updates, reviewer traces, meta event logs, staged skill patches | Review findings, note revisions, validation, promotion from workshop to library |
| Scope | Project-level ML research workflow and its harness | Methodology KB and framework for many KBs |

The main alignment is that both systems treat files as behavior-shaping retained artifacts, not as passive documentation. ARIS's `SKILL.md` files correspond most closely to Commonplace instructions and skills; Research Wiki pages correspond to a project-local KB; query packs resemble compiled context bundles; run-state and verdict files resemble review/run gates.

The main divergence is register and product pressure. ARIS is prescriptive and operational: it wants an agent to do a task overnight, recover after compaction, and move through gates. Commonplace is descriptive/theoretical/prescriptive by collection, with stronger concern for long-lived artifact contracts and cross-system comparison. ARIS therefore accepts more procedural glue, optional hooks, shell snippets, and project-specific state; Commonplace tends to promote durable claims or instructions only after they are made reviewable under collection/type contracts.

ARIS also pushes harder on cross-model governance. Commonplace has semantic review bundles and validation, but ARIS makes "executor cannot acquit itself" a repeated runtime contract: result-to-claim, auto-review-loop, run-state acceptance, and meta-apply all preserve some form of external verdict handle. That is a strong pattern for any system that lets agents produce downstream behavior-shaping artifacts.

**Read-back:** `both` — Agents deliberately invoke skills and read files, while generated query packs, recovery hooks, readiness hooks, monitors, queues, and run-state resume paths can proactively surface retained project state before the next action

## Write-side placement

**Write agency:** `manual` `automatic` — agents and humans author wiki pages, notes, skills, claims, and pending patches through skill workflows, while helper scripts, hooks, queues, run-state files, query-pack rebuilds, reviewer-state updates, and meta-optimization paths mutate retained project or harness state.

**Curation operations:** `consolidate` `synthesize` `promote` — `research_wiki.py` and workflow skills consolidate project records into query packs, result-to-claim and meta-optimization synthesize traces into claims/statuses or pending diffs, and reviewer verdicts, accepted phase ids, claim updates, and gated meta-apply paths promote selected records into stronger steering or system-definition roles.

### Trace-derived learning

**Trace source:** `session-logs` `event-streams` — Reviewer/session traces, Claude Code hook events, run state, queue state, and project/session status are the retained raw signals described here.

**Learning scope:** `per-task` `per-project` `cross-task` — Review traces and queue runs are per task/run, Research Wiki and run state are project-local, and meta-optimization can aggregate project and global logs across skill invocations.

**Learning timing:** `online` `staged` — Wiki updates, run state, queue state, and hook events are updated during workflows, while meta-optimization stages candidate diffs before a separate apply gate.

**Distilled form:** `prose` `symbolic` — Distilled outputs are query packs, claim statuses, failed-idea warnings, reviewer memory, accepted verdict ids, run-state phase acceptance, and staged or landed skill patches.

**Trace source.** ARIS consumes several trace classes: Claude Code hook events in `.aris/meta/events.jsonl`, reviewer prompts/responses in `.aris/traces/`, auto-review round state, experiment logs and result verdicts, failed or partial ideas, queue states, and session/project status. It is not a model-training system; the learned artifacts are prose, symbolic state, query packs, and candidate diffs.

**Extraction.** Extraction is mostly procedural and deterministic around an agent judgment core. Research Wiki ingestion creates paper pages and graph edges through helper scripts; `/result-to-claim` uses a Codex judgment to update claims, experiments, idea outcomes, and query packs ([skills/result-to-claim/SKILL.md](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/665a238fda5d46259cb99d329a89772886e76da0/skills/result-to-claim/SKILL.md)). `research_wiki.py` deterministically rebuilds query packs from selected short fields. `meta-optimize` analyzes event logs, but only stages diffs; `/meta-apply` performs the binding cross-model review at landing. `capture_filter.py` blocks obvious self-poisoning captures such as transient tool failures becoming durable negative capability claims ([tools/capture_filter.py](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/665a238fda5d46259cb99d329a89772886e76da0/tools/capture_filter.py)).

**Scope and timing.** Research Wiki learning is project-local and online during normal research workflows. Reviewer traces are per skill/run and retained for audit or replay. Meta-optimization can aggregate project and global logs, but landing remains human-invoked. Queue state is per remote run and updates online every scheduler poll. Hook activation is online and event-driven.

**Raw to distilled split.** Raw traces are retained as evidence: hook events, reviewer requests/responses, experiment logs, queue logs, and session registry files. Distilled outputs are the behavior-shaping artifacts: query packs, claim statuses, failed-idea warnings, accepted verdict ids, reviewer memory, run-state phase acceptance, and staged or landed skill patches. ARIS is strongest where it keeps this split explicit. It is weaker where prose skills require the acting agent to update wiki pages or project notes faithfully.

**Survey placement.** ARIS belongs in the trace-to-wiki, trace-to-verdict, and trace-to-skill-patch families. It strengthens the survey claim that durable learning need not be distributed-parametric: symbolic query packs, verdict handles, failed-idea records, and staged diffs can strongly shape future agent behavior.

## Read-back placement

**Direction.** ARIS uses both pull and push from the acting agent's perspective. Slash-command invocation is pull, and the installed `SKILL.md` files are shipped baseline instructions rather than read-back. The memory push comes from generated project artifacts: `/idea-creator` preloads `research-wiki/query_pack.md`, session-recovery hooks surface Pipeline Status and state-file pointers, meta-readiness reads `.aris/meta/events.jsonl`, monitors read Claude session state, queues write and expose `queue_state.json`, and run-state resume reads `.aris/runs/<run_id>.json`.

**Read-back signal:** `coarse` `identifier` — Workflow hooks and reminders can fire coarsely, while the payload is selected by project paths, status fields, run ids, phase names, queue-state paths, and session ids.

**Faithfulness tested:** `no` — The review states that ARIS records traces and verdict ids but does not generally run WITH/WITHOUT ablations proving fired query packs or hooks changed agent behavior.

**Targeting and signal.** Targeting is instance-oriented where a workflow has already emitted a durable identifier: the `research-wiki/` directory and `query_pack.md` path select the active project wiki for `/idea-creator`; Pipeline Status, `REVIEW_STATE.json`, run ids, queue-state paths, and Claude session ids select the current project or run. The signal is `identifier`: path, event, project root, status field, run id, phase name, or session registry status. Some hook reminders are coarser, such as first tool call, every thirtieth tool call, pre-compaction, post-edit, or SessionEnd, but their payload is still drawn from retained project/status artifacts when present. ARIS does not use lexical, embedding, or LLM-judgment retrieval for these push paths; actual precision, recall, and context dilution are not verified from code.

**Injection point.** Query-pack read-back assembles before idea generation. Session restore and context refresh happen before tool use, so they can change the next action. Pre-compact reminders fire before context compression. Meta-readiness at session end and queue polling are write-side or operational maintenance surfaces whose retained state is later read by the agent or user as context.

**Selection, scope, and complexity.** The query pack has an 8000-character cap and selects short fields from project direction, gaps, failed ideas, papers, and recent graph edges. Recovery hooks select compact Pipeline Status and pointers rather than full project history. ARIS-Monitor intentionally avoids full transcript content, using registry status and a tail window. The selection policies are code-grounded; actual precision and context dilution are runtime properties not verified here.

**Authority at consumption.** Query packs are advisory but behavior-shaping: they bias search seeds and ban repeated failed ideas. Recovery hook output is advisory context injection. `corpus_write_guard.py` has blocking authority for common Bash corpus writes. Run-state acceptance has routing authority because resume cannot skip `done` but unaccepted phases. Queue state has scheduler authority over job launch/retry/completion.

**Faithfulness.** ARIS records traces and verdict ids, but it does not generally run WITH/WITHOUT ablations proving that a fired query pack or hook changed agent behavior. Its faithfulness story is structural rather than empirical: retained context enters the prompt or scheduler state through documented paths.

**Other consumers.** Humans consume ARIS-Monitor, rendered HTML reports, manual-review pending files, Feishu notifications, pending meta patches, and queue summaries. These surfaces matter because several gates are intentionally human-invoked or human-auditable rather than fully automatic.

## Curiosity Pass

**The repo is more methodology bundle than standalone platform source.** The README discusses ARIS-Code CLI releases, providers, and bundled skills, but this checkout's reviewable implementation is mainly skills, Python helpers, shell installers, MCP servers, docs, hooks, and monitor code rather than a full Rust/Node CLI source tree. Claims about the released binary should be treated as documentation unless separately verified from its source.

**The strongest memory mechanism is not "persistent memory" by itself; it is activation plus governance.** A Research Wiki page matters because `query_pack.md` is loaded at ideation time. A reviewer trace matters because a state file or accepted verdict id can resume or gate a phase. A meta event log matters because it can become a staged patch. Storage without these consumption paths would be much weaker.

**The system is honest about several non-enforcement boundaries.** Meta-optimize cannot land patches, but its Bash access is not a perfect sandbox. `corpus_write_guard.py` is explicitly a regex guard, not complete prevention. Session recovery hooks are optional. This is good documentation discipline: it prevents advisory mechanisms from being mistaken for hard validators.

**There is a lot of authority in prose.** Many critical transitions still rely on a skill instructing the acting agent to update ledgers, wiki pages, claims, and status. ARIS mitigates this with helper scripts, review traces, and gates, but it remains less mechanically constrained than a schema-first KB for some artifact classes.

**Anti-self-poisoning is a notable design detail.** `capture_filter.py` encodes a specific memory failure mode: transient operational failures should not become durable negative claims that later agents cite against themselves. That is a transferable lesson for any trace-derived memory system.

## What to Watch

- Whether ARIS-Code CLI source becomes available in the same repo or another source tree; that would change how much of the provider/runtime claims can be code-grounded.
- Whether Research Wiki gains stronger typed helpers for ideas, experiments, and claims beyond paper ingest and edge/query-pack rebuilding.
- Whether query-pack and hook activation get behavioral evaluations showing that fired read-back improves research outcomes rather than merely entering context.
- Whether meta-optimization gains a provenance integrity verifier or pre-push check, since the docs currently identify that as the missing backstop for unstamped corpus changes.
- Whether queue state becomes integrated into `/monitor-experiment`, closing the current gap where queue-state monitoring is documented as a manual command.

---

Relevant Notes:

- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: ARIS turns failed ideas, result verdicts, reviewer traces, and meta events into later steering artifacts.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - exemplifies: ARIS's memory becomes useful through query-pack preload, hooks, run-state resume, and monitors.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - defined-in: raw traces, logs, papers, and review responses are mostly evidence/reference until consumed by stronger paths.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - defined-in: skills, query packs at consumption time, verdict ids, run states, queues, and landed patches can instruct, route, gate, or configure behavior.
- [A functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) - compares-with: ARIS is rich in workshop artifacts for live research runs rather than long-lived methodology library artifacts.
- [ByteRover CLI](./byterover-cli.md) - compares-with: both use file-backed project memory and derived activation surfaces, but ByteRover productizes a context tree while ARIS orchestrates research workflows through skills and gates.
