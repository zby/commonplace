---
description: "Claude Context Guard review: Claude Code slash-command memory using project safeguard files, audits, pagination, hooks, and itemised code indexes"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
status: current
last-checked: "2026-06-04"
---

# Claude Context Guard

Claude Context Guard, by atreiou, is a Claude Code project-memory harness. At the reviewed commit it installs slash commands, hooks, and templates that turn a project directory into a set of persistent safeguard files: session logs, task registry, decisions, user comments, learned behaviour, feature QA state, resume state, archived plans, audit reports, and optional itemised code sidecar indexes.

**Repository:** https://github.com/atreiou/claude-context-guard

**Reviewed commit:** [7e09e5b53099ef7b11fd400db39656e766d2e6fa](https://github.com/atreiou/claude-context-guard/commit/7e09e5b53099ef7b11fd400db39656e766d2e6fa)

**Last checked:** 2026-06-04

## Core Ideas

**The memory is a file contract for Claude Code, not a daemon or database.** Installation copies `.claude/commands`, `.claude/hooks`, `.claude/settings.json`, and templates into a target project; the first `/start` creates the project files from those templates ([install.sh](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/install.sh), [.claude/commands/start.md](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/.claude/commands/start.md)). The durable memory after installation is ordinary Markdown and JSON in the host project, governed by command instructions rather than a standalone runtime.

**Session recovery is coarse, deliberate rehydration.** `/start` locates the Context Guard root, reads `RESUME_STATE.md`, `CLAUDE.md`, `SESSION_LOG.md`, `TASK_REGISTRY.md`, `DECISIONS.md`, `LEARNED_BEHAVIOUR.md`, `COMMENTS.md`, `FEATURE_LIST.json`, declared custom context files, and the last three plan files, then cross-references plans and task registry before asking for confirmation ([.claude/commands/start.md](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/.claude/commands/start.md)). This gives a fresh agent a high-recall project state, but it is not relevance-ranked per user prompt.

**Context efficiency comes from pagination and addressable source sections.** The README and command files keep current safeguard files lean by archiving older sessions, done tasks, superseded decisions, and actioned comments into `*_page*.md` files; `/start` notes archives without reading them unless explicitly needed ([README.md](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/README.md), [.claude/commands/save.md](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/.claude/commands/save.md)). `/itemise` adds numbered code-section markers and `<source>.index.md` sidecars so an agent can navigate large files by symbolic address instead of loading whole files ([.claude/commands/itemise.md](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/.claude/commands/itemise.md), [templates/CLAUDE.md](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/templates/CLAUDE.md)).

**The strongest governance is procedural cross-checking.** `TASK_REGISTRY.md` must contain every task; `COMMENTS.md` preserves user directives; `DECISIONS.md` records architectural constraints; `FEATURE_LIST.json` separates manually verified features from task completion ([templates/TASK_REGISTRY.md](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/templates/TASK_REGISTRY.md), [templates/COMMENTS.md](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/templates/COMMENTS.md), [templates/DECISIONS.md](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/templates/DECISIONS.md), [templates/FEATURE_LIST.json](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/templates/FEATURE_LIST.json)). `/audit` then checks git state, plan cross-references, stale work, missing files, sidecar freshness, and parity ([.claude/commands/audit.md](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/.claude/commands/audit.md)).

**Hooks are safety rails, not a complete memory engine.** The settings file registers a Bash pre-tool hook for commit reminders and a pre-compaction hook for backup; the shell scripts remind or copy files rather than interpret their contents ([.claude/settings.json](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/.claude/settings.json), [.claude/hooks/pre-commit-check.sh](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/.claude/hooks/pre-commit-check.sh), [.claude/hooks/pre-compact-save.sh](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/.claude/hooks/pre-compact-save.sh)). Behavioral reliability therefore depends heavily on Claude following the installed command prose.

## Artifact analysis

- **Storage substrate:** `files` - The primary retained state persists as project-local Markdown and JSON safeguard files, plan archives, audit reports, code sidecar indexes, `.claude` command files, settings, and shell hooks; git commits and pushes are secondary durability and rollback surfaces.
- **Representational form:** `prose` `symbolic` - The system is mostly prose instructions and logs, with symbolic task IDs, decision IDs, statuses, dates, JSON feature records, hook configuration, shell scripts, file names, archive-page conventions, section numbers, sidecar tables, and git command protocols.
- **Lineage:** `authored` `trace-extracted` - The command/templates layer is authored by the package; installed project memories are authored from user and agent work, then trace-extracted from conversation state, git state, plans, task progress, comments, decisions, feature verification, and code edits.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` - Session logs, comments, tasks, decisions, learned behaviour, and plans supply knowledge; `CLAUDE.md` and slash commands instruct the agent; root detection, custom context declarations, archive rules, and itemised addresses route context; `/audit` and sidecar parity checks validate integrity.

**Installed command layer.** Storage substrate: `.claude/commands/*.md`, `.claude/settings.json`, and `.claude/hooks/*.sh` copied into the project. Representational form: prose procedures plus symbolic allowed-tool frontmatter, hook JSON, and shell logic. Lineage: authored package code, installed into each project and optionally merged with a parent `.claude` directory. Behavioral authority: system-definition artifact for Claude Code because slash commands and hooks tell the agent which files to read, write, audit, back up, commit, and push.

**Safeguard files.** Storage substrate: root-level `CLAUDE.md`, `RESUME_STATE.md`, `SESSION_LOG.md`, `TASK_REGISTRY.md`, `DECISIONS.md`, `LEARNED_BEHAVIOUR.md`, `COMMENTS.md`, and `FEATURE_LIST.json` created from templates. Representational form: prose records plus symbolic task/status tables, decision categories, feature booleans, timestamps, and custom context declarations. Lineage: initialized from templates, then maintained from session traces, user comments, plans, decisions, QA reports, and git state. Behavioral authority: knowledge artifacts when read for state, and instruction artifacts where `CLAUDE.md` and decisions constrain later work.

**Plans, archives, resume state, and compaction backups.** Storage substrate: `plans/`, `*_page*.md`, `audits/`, `RESUME_STATE.md`, and `compaction-backups/` files. Representational form: prose handoff notes, audit reports, and archive pages with symbolic session/task ranges. Lineage: derived views from prior plans, older safeguard entries, audit runs, and pre-compaction copy events. Behavioral authority: knowledge and validation, because `/start` cross-references the latest plans and `/audit` uses archives to avoid false dropped-task findings.

**Itemised source files and sidecar indexes.** Storage substrate: edited source files plus `<source>.index.md` files beside them. Representational form: symbolic section markers and sidecar tables, with prose descriptions. Lineage: generated or refined by `/itemise` over existing source, then maintained on each later code edit. Behavioral authority: routing and validation, because agents can target section addresses and `/audit` checks source/sidecar parity and stale dates.

**Git history and remotes.** Storage substrate: the host project's git repository and optional remote. Representational form: symbolic commits, tags, branch state, and command output. Lineage: derived from approved work and safeguard updates. Behavioral authority: validation and durability; `/start`, `/save`, `/end`, and `/audit` use git state to detect orphaned work, unpushed commits, and incomplete save points.

Promotion path: Context Guard's path is from raw conversation and work traces to written safeguard records, then to always-read project instructions, session recovery summaries, audits, archives, and git commits. It does not promote memories into learned retrieval models or hard validators; its promotion is procedural, file-native, and agent-obedience dependent.

## Comparison with Our System

| Dimension | Claude Context Guard | Commonplace |
|---|---|---|
| Primary purpose | Recover Claude Code project state across sessions and context loss | Maintain a typed methodology KB for agent-operated knowledge bases |
| Main artifact | Safeguard files plus slash-command procedures | Typed Markdown artifacts, source snapshots, reviews, indexes, and instructions |
| Write path | `/start`, `/save`, `/end`, `/audit`, `/itemise`, hooks, and agent-maintained logs | Direct file edits, source snapshots, validation, semantic review, index refresh |
| Read-back | Coarse startup/command rehydration into Claude Code context | Mostly explicit search, indexes, links, skills, and loaded instructions |
| Governance | Cross-reference audits, task/comment preservation rules, git checks, sidecar parity | Collection/type contracts, schemas, citations, validation, review gates |
| Context efficiency | Pagination, current-file loading, last-three-plan window, itemised code addresses | Directory indexes, tags, links, `rg`, typed artifacts, generated navigation |

Context Guard and Commonplace share the premise that file-native memory is inspectable, durable, and easy for agents to operate. Context Guard optimizes for continuity in an application project: do not drop tasks, lose user comments, forget decisions, or miss uncommitted work after a restart. Commonplace optimizes for durable knowledge quality: make claims, sources, artifact types, links, and review status explicit enough that later agents can reason from them.

The main design split is authority depth. Context Guard's safeguards are operationally forceful because its command prose tells Claude to treat them as mandatory, but the repository does not include an independent semantic checker that proves the agent preserved user intent or obeyed recalled decisions. Commonplace has weaker automatic session recovery, but stronger typed validation and review conventions around durable knowledge artifacts.

### Borrowable Ideas

**A small `RESUME_STATE.md` handoff separate from historical logs.** Ready now. Commonplace could use a short work-in-flight artifact for long operations without mixing transient state into durable notes or indexes.

**Treat user comments as first-class retained evidence.** Ready now for review/workshop workflows. Context Guard's `COMMENTS.md` is blunt but useful: the exact user wording is often more valuable than a cleaned summary.

**Archive old operational history out of startup context.** Ready now as a design rule. The pagination policy keeps the current state loaded while preserving older history for audits; Commonplace can apply the same rule to workshop logs and generated review runs.

**Sidecar indexes for large code files.** Needs a concrete use case. Section-address sidecars could help code-heavy reviews or source snapshots, but they add a maintenance contract that is only worth it where targeted source reads are common.

**Do not borrow command-prose enforcement as the only gate.** Ready now as a caution. Context Guard shows how far careful instructions can go, but Commonplace should keep deterministic validators and semantic review for high-authority artifacts.

## Write side

**Write agency:** `manual` `automatic` - Humans trigger slash commands and approve project decisions, while Claude is instructed to update safeguard files from session state, git state, comments, decisions, feature QA, plans, and audits; hooks automatically remind before commits and copy files before compaction.

**Curation operations:** `decay` `invalidate` - Pagination moves older or actioned material out of the current startup set, while superseded decisions, actioned comments, clean resume states, stale sidecar entries, and orphaned work checks mark prior state as no longer current without deleting the underlying history.

### Trace-derived learning

**Trace source:** `session-logs` `tool-traces` `event-streams` - The durable files are updated from conversation/session history, user comments, plan files, git logs/status/diffs, command invocations, save/end/audit runs, and Claude Code hook events.

**Learning scope:** `per-project` - The installed safeguards live in one project root and are meant to guide later sessions in that project; parent-directory command installation only improves discovery from a higher Claude Code working directory.

**Learning timing:** `online` `staged` - The template asks agents to update safeguard files incrementally during work, while `/save`, `/end`, `/start`, `/audit`, `/itemise`, pre-commit reminders, and pre-compaction backups are staged occasions.

**Distilled form:** `prose` `symbolic` - Session traces become prose summaries, comments, decisions, learned behaviour, resume notes, audits, and sidecar descriptions, plus symbolic task IDs, statuses, feature pass/fail JSON, decision categories, archive references, and section numbers.

**Extraction.** Extraction is instruction-mediated rather than model-service automated. The slash commands tell Claude what to inspect and how to write the retained artifact: `/save` checks in-flight work, comments, tasks, decisions, learned behaviour, feature QA, and pagination before committing; `/end` does the clean wrap-up version; `/audit` writes an audit report; `/itemise` converts source structure into addressable markers and sidecar descriptions ([.claude/commands/save.md](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/.claude/commands/save.md), [.claude/commands/end.md](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/.claude/commands/end.md), [.claude/commands/audit.md](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/.claude/commands/audit.md), [.claude/commands/itemise.md](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/.claude/commands/itemise.md)).

**Scope and timing.** Context Guard is per project and cross-session. Its online path is the auto-checkpoint discipline embedded in `CLAUDE.md`; its staged path is the user-invoked slash command suite and Claude Code hooks. It does not implement cross-project learning, embeddings, or a separate learned model.

**Survey fit.** Context Guard belongs in the trace-to-operational-file-memory family. It strengthens the survey pattern where raw session traces remain useful mostly after distillation into compact handoff, task, decision, and audit artifacts; the behavior-shaping artifact is the curated file, not the transcript itself.

## Read-back

**Read-back:** `both` - Retained project memory is pushed to the receiving Claude session through auto-read `CLAUDE.md` and user-invoked slash commands such as `/start` and `/audit`; older archives, sidecar indexes, custom context files, plans, and safeguard records can also be pulled by deliberate file reads when the current recovery set is insufficient.

**Read-back signal:** `coarse` `identifier` - The push is mostly coarse session-start or command-triggered recall, then identifier-scoped by fixed file names, detected `CCG_ROOT`, custom context paths, latest plan files, archive names, and sidecar section numbers.

**Faithfulness tested:** `no` - The repository checks file presence, cross-references, git state, sidecar parity, and backup/reminder mechanics, but it does not include an ablation showing that recalled safeguards reliably change Claude's downstream behavior.

**Targeting and signal.** `/start` is the main read-back surface: it loads the current safeguard set, declared custom files, and latest plans by identifier after locating the project root. That is targeted by project/file identity, not by inferred relevance to the current user request. Archive pages are intentionally not loaded by default; the command notes their existence and reads them only if the user asks or missing context makes them necessary.

**Injection point.** `CLAUDE.md` enters at Claude Code session startup, and slash-command recovery assembles context before the next substantive work. Pre-commit and pre-compaction hooks fire around tool/compaction events, but their outputs are reminders or backups; they are not post-action memory read-back.

**Selection, scope, and complexity.** Selection is deliberately simple: read current files, skip archive pages, read last three plans, parse custom context declarations, and use itemised sidecar addresses for code. This keeps volume bounded for mature projects, but complexity is still high because the loaded state mixes instructions, task truth, decisions, comments, QA status, git state, and recent plans in one recovery procedure.

**Authority at consumption.** `CLAUDE.md`, slash commands, and decision records are consumed as instructions by Claude Code. Session logs, comments, plans, audits, and feature records are knowledge artifacts. The strongest authority is social/procedural: the command says to follow steps "EXACTLY", but the shell hooks are reminders/backups rather than hard gates.

**Faithfulness.** Context Guard validates that the memory files exist and cross-reference each other, not that Claude actually obeys the recalled state. `/audit` can flag dropped tasks, unexplained work, stale indexes, and git problems after the fact, but it does not measure with/without memory behavior.

**Other consumers.** Human maintainers read the same safeguard files, audit reports, git history, archive pages, sidecar indexes, and compaction backups. The design is meant to be auditable in ordinary project files, not hidden behind a memory service.

## Curiosity Pass

**The README names a different clone URL than the supplied source identity.** The reviewed source URL is `atreiou/claude-context-guard`, while the README install block says `atreiou/context-guard`; I did not verify whether that is a rename, alias, or stale documentation ([README.md](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/README.md)).

**The mechanism is powerful because it is boring.** Plain files, git, hooks, and slash-command procedures solve a real continuity problem without vector retrieval, but they also leave meaning-quality to the agent and human.

**The task registry is closer to an operational ledger than a memory note.** Its value is not prose richness; it is the hard rule that every task must have a row, status, and source.

**Itemisation is a context-efficiency idea with a high maintenance cost.** Addressable code sections can reduce reads, but stale sidecars become false context unless the audit/parity contract is actually followed.

**Pre-compaction backup protects bytes, not semantics.** Copying safeguard files before compaction prevents loss, but the files still need to have been updated correctly before the hook fires.

## What to Watch

- Whether Context Guard adds deterministic tests or fixtures for slash-command procedures; that would make the command layer less dependent on informal prompt obedience.
- Whether `/start` gains relevance-ranked or task-scoped loading instead of current-file plus last-three-plan loading; that would change the read-back signal from coarse/identifier toward inferred selection.
- Whether archive pagination starts summarizing older material rather than only moving it; that would add a true consolidation operation and create new lineage questions.
- Whether hooks become blocking gates for missing safeguard updates rather than reminders/backups; that would strengthen behavioral authority from instruction/validation toward enforcement.
- Whether sidecar index maintenance proves usable on large real projects; if not, the maintenance burden may outweigh the context savings.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Context Guard's value comes from making project files enter future Claude sessions, not merely storing them.
- [Axes of artifact analysis](../../../notes/axes-of-artifact-analysis.md) - applies: safeguard files, command prose, hooks, git state, plans, audits, and sidecar indexes carry different authority.
- [Knowledge artifact](../../../notes/definitions/knowledge-artifact.md) - classifies: logs, comments, plans, feature records, and audit reports mostly serve as evidence and context.
- [System-definition artifact](../../../notes/definitions/system-definition-artifact.md) - classifies: `CLAUDE.md`, slash commands, hooks, audit rules, and itemisation rules instruct or validate future behavior.
- [Use trace-derived extraction](../../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: Context Guard turns session and tool traces into durable operational memory files.
