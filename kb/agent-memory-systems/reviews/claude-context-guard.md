---
description: "Claude Context Guard review: Claude Code continuity scaffold with safeguard files, lifecycle slash commands, hooks, pagination, and itemised code indexes"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-06-01"
---

# Claude Context Guard

Claude Context Guard, from `atreiou/claude-context-guard`, is a Claude Code project scaffold for surviving session restarts, compaction, rate limits, and dropped work. It does not implement a standalone memory server or retrieval API. It installs project-local Markdown/JSON safeguard files, Claude slash-command instructions, and Claude Code hooks that make the acting agent maintain and reload external project state.

**Repository:** https://github.com/atreiou/claude-context-guard

**Reviewed commit:** [7e09e5b53099ef7b11fd400db39656e766d2e6fa](https://github.com/atreiou/claude-context-guard/commit/7e09e5b53099ef7b11fd400db39656e766d2e6fa)

**Last checked:** 2026-06-01

## Core Ideas

**Continuity is a project-file protocol, not model memory.** The installed template set creates `CLAUDE.md`, `RESUME_STATE.md`, `SESSION_LOG.md`, `TASK_REGISTRY.md`, `DECISIONS.md`, `COMMENTS.md`, `LEARNED_BEHAVIOUR.md`, `FEATURE_LIST.json`, and supporting `plans/` and `audits/` directories ([templates/](https://github.com/atreiou/claude-context-guard/tree/7e09e5b53099ef7b11fd400db39656e766d2e6fa/templates), [README.md](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/README.md)). The retained state is ordinary repo-visible text and JSON, so rollback, diff, review, and manual repair use the host project's normal filesystem and git tools.

**`/start` rebuilds working context from the current safeguard set.** The start command first locates the Context Guard root, handles first-run template creation, reads `RESUME_STATE.md` before the other safeguard files, loads declared custom context, notes archive pages without reading them, checks git state, detects orphaned sessions, and cross-references recent plans against the task registry before summarising the next session state ([.claude/commands/start.md](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/.claude/commands/start.md)). This is explicit recovery, not automatic transcript continuation.

**`/save` and `/end` make session state durable at lifecycle boundaries.** `/save` writes an in-flight handoff to `RESUME_STATE.md`, updates the log, registry, comments, decisions, learned behaviour, and feature tracker, rotates old safeguard material, then commits and pushes according to `CLAUDE.md` version-control mode ([.claude/commands/save.md](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/.claude/commands/save.md)). `/end` performs the clean-session variant, wipes resume state to a clean template, archives plans, tags commits, and verifies the handoff surface ([.claude/commands/end.md](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/.claude/commands/end.md)).

**Audit is a first-class consumer of the same retained files.** `/audit` checks git state, task registry integrity, plan cross-references, user comments, decisions, session log consistency, safeguard file existence, sidecar index freshness, and sidecar parity, then writes a timestamped audit report under `audits/` ([.claude/commands/audit.md](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/.claude/commands/audit.md)). The same files that recover work also become evidence for review.

**Hooks add two event-keyed safeguards around ordinary Claude Code actions.** `.claude/settings.json` wires a `PreToolUse` hook for Bash and a `PreCompact` hook ([.claude/settings.json](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/.claude/settings.json)). The Bash hook parses Claude's tool-use input with `jq`, detects commands containing `git commit`, and prints a pre-commit checklist without blocking the command ([.claude/hooks/pre-commit-check.sh](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/.claude/hooks/pre-commit-check.sh)). The PreCompact hook copies selected safeguard files into `compaction-backups/YYYY-MM-DD_HHMMSS/` before Claude Code compacts context ([.claude/hooks/pre-compact-save.sh](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/.claude/hooks/pre-compact-save.sh)). These hooks are workflow safeguards, not relevance-gated project-memory read-back.

**Itemisation turns source files into addressable artifacts.** `/itemise` adds numbered section markers to code files, writes paired `<source>.index.md` sidecars, backs up files first, verifies that only numbering changed, and makes `CLAUDE.md` enforce source/sidecar co-maintenance ([.claude/commands/itemise.md](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/.claude/commands/itemise.md), [templates/CLAUDE.md](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/templates/CLAUDE.md)). This is a context-economy feature: a future agent can navigate by section address instead of loading whole files.

## Artifact analysis

**Safeguard files.** Storage substrate: project filesystem and, when the project uses git, the project repository. Representational form: mixed prose and symbolic structure. `SESSION_LOG.md`, `TASK_REGISTRY.md`, `DECISIONS.md`, `COMMENTS.md`, `LEARNED_BEHAVIOUR.md`, and `RESUME_STATE.md` are mostly prose with table or field conventions; `FEATURE_LIST.json` is symbolic JSON; archive pages and audit reports are prose-derived records. Lineage: initialized from templates, then updated from session traces, user comments, task outcomes, decisions, feature verification, and save/end/audit passes. Behavioral authority: knowledge artifacts when read as evidence or history; system-definition artifacts when `/start`, `/save`, `/end`, or `/audit` requires the acting agent to obey task status, decisions, comments, feature verification semantics, and resume-state handoff.

**`CLAUDE.md` control-plane template.** Storage substrate: installed project file generated from `templates/CLAUDE.md`. Representational form: prose instructions with symbolic toggles and conventions, including version-control mode, itemisation mode, task status vocabulary, and sidecar maintenance rules. Lineage: authored scaffold content with project placeholders expanded during first run or installation. Behavioral authority: high-authority system-definition artifact because Claude Code auto-reads it and the slash commands treat it as the source of project rules, custom context declarations, git behavior, and itemisation policy.

**Slash-command instruction files.** Storage substrate: Markdown files under `.claude/commands/`. Representational form: prose procedures with required command sequences, file lists, conditional branches, output formats, and allowed-tool metadata. Lineage: authored framework instructions copied by `install.sh`, not learned from the host project. Behavioral authority: system-definition artifacts invoked by the user or agent as Claude Code commands. They define capture, recovery, audit, pagination, commit, and itemisation operations, but effective compliance depends on the model following the instruction text.

**Hook scripts and settings.** Storage substrate: `.claude/settings.json` plus shell scripts under `.claude/hooks/`. Representational form: symbolic JSON wiring and executable shell code with short prose checklist output. Lineage: authored scaffold code copied by the installer; runtime backup directories are derived from current safeguard files and timestamps. Behavioral authority: system-definition artifacts with event-triggered force. The pre-commit hook is an advisory audit trigger before a matching Bash commit command; the pre-compaction hook is an automatic preservation action before context compaction. Neither hook performs semantic selection over the retained ledgers.

**Plans, audits, archive pages, and compaction backups.** Storage substrate: project directories and files created by the slash commands or hooks. Representational form: prose Markdown, copied Markdown/JSON, and sometimes generated reports. Lineage: derived views over earlier safeguard files, project plans, audit checks, or pre-compaction snapshots. Behavioral authority: mostly knowledge artifacts for recovery, cross-reference, and evidence. They gain system-definition force only when `/start` or `/audit` reads them to flag dropped tasks, stale sidecars, inconsistent state, or missing provenance.

**Itemised source and sidecar indexes.** Storage substrate: host project source files plus paired `.index.md` sidecars. Representational form: mixed symbolic/prose: code comments encode section addresses, while the sidecar table gives human-readable descriptions and last-edit dates. Lineage: generated by `/itemise` from existing source files and then maintained on future edits. Behavioral authority: knowledge artifacts for targeted navigation; system-definition artifacts when `CLAUDE.md` and `/audit` enforce parity and freshness expectations. The promotion path is notable: ordinary source code gains an addressable index contract without changing the runtime code's semantics.

## Comparison with Our System

| Dimension | Claude Context Guard | Commonplace |
|---|---|---|
| Primary purpose | Preserve Claude Code project continuity across sessions and compaction | Maintain a typed methodology KB for future agents and maintainers |
| Canonical retained unit | Safeguard Markdown/JSON files plus command and hook scaffolding | Typed Markdown artifacts, schemas, generated indexes, reviews, and instructions |
| Capture loop | Agent-maintained session logs, registries, comments, decisions, resume state, audits, backups | Source-grounded writing, validation, semantic review, workshop artifacts, and indexes |
| Read-back | `/start` pulls safeguard files; `CLAUDE.md` is always-loaded; hooks remind or back up at selected events | Pull through search/indexes/links, plus explicit instructions and generated context where configured |
| Governance | Procedural slash commands, git checks, pagination, audits, sidecar parity, hook reminders | Collection contracts, type specs, deterministic validation, review bundles, git history |

Context Guard and Commonplace share the same core bet: plain files are good early memory infrastructure because agents, humans, and git can all inspect them. Context Guard applies that bet to project continuity. Commonplace applies it to durable methodology and typed knowledge.

The main difference is artifact typing. Context Guard uses file names, command conventions, and prose contracts to define authority. Commonplace makes more of that authority explicit through frontmatter, type specs, schemas, collection contracts, and generated indexes. Context Guard is lighter to install in an arbitrary Claude Code project, but weaker at discriminating artifact status, provenance, and review state inside the files themselves.

The other difference is lifecycle posture. Context Guard treats the active session as the center: save, resume, audit, paginate, and avoid dropped work. Commonplace treats promoted knowledge as the center: source material and workshop state matter, but library artifacts accumulate only after routing, drafting, review, and validation. Context Guard is stronger as an operational continuity harness; Commonplace is stronger as a durable knowledge system.

**Read-back:** pull plus always-load. `/start`, `/audit`, `/save`, `/end`, and `/itemise` are deliberate command surfaces from the agent's perspective, while `CLAUDE.md` is unconditional project context; the hooks are event-keyed reminders/backups, not qualifying relevance-gated memory read-back.

### Borrowable Ideas

**Use resume state as a small, separate handoff artifact.** Commonplace workshop runs could keep a narrow `RESUME_STATE`-style file for interrupted multi-step work instead of relying on session logs or chat history. Ready for long review and migration workflows.

**Treat comments as first-class retained evidence.** Context Guard's `COMMENTS.md` makes user utterances a protected artifact instead of burying them in summaries. Commonplace could use this for high-stakes review runs where exact user constraints must survive compaction. Ready as a workshop convention, but not as a global always-on rule.

**Separate current files from paginated archives.** Context Guard's archive pages preserve evidence without loading old history by default. Commonplace already has source snapshots and generated indexes; the borrowable part is making "available but not automatically loaded" explicit in workshop state. Ready where active files are growing past useful context size.

**Add event-keyed reminders for high-risk operations.** The pre-commit checklist is a small but useful workflow device. Commonplace could add hook-like reminders around commit, validation, or review-finalization commands, but only where the event reliably predicts a forgotten obligation. Needs concrete missed-step evidence before adding more ambient prompts.

**Make source navigation addressable when files are large.** Itemisation plus sidecar indexes is heavier than Commonplace normally wants, but the addressable-section pattern is worth borrowing for long generated reports or code files that agents repeatedly inspect. Needs a scoped pilot; broad automatic itemisation would add maintenance load.

## Trace-derived learning placement

**Trace source.** Context Guard qualifies as trace-derived in the weak, agent-mediated sense. The raw signals are live session context: user comments, task creation and completion, decisions, feature verification, errors, rate-limit or interruption state, git state, plans, and audit findings. It does not mine a stored full transcript automatically; the slash commands instruct the acting agent to extract and write the relevant material during `/save`, `/end`, `/start`, or `/audit`.

**Extraction.** Extraction is instruction-driven rather than algorithmic. `/save` asks the agent to review what happened since the last checkpoint and update each safeguard file with missing comments, tasks, decisions, learned behavior, feature QA, and in-flight state. `/end` performs the clean-session variant. `/start` reconstructs continuity by reading the retained files, checking git history, and cross-referencing recent plans against the registry. `/audit` turns the same records into integrity findings and a saved report.

**Scope and timing.** Scope is per project. Timing is online during normal Claude Code work, with explicit lifecycle commands and two event-triggered hooks. The durable outputs are project files, archive pages, audit reports, plans, sidecar indexes, and compaction backups, not model weights or embeddings.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), Context Guard belongs near doctrine-mediated live capture systems: the acting agent is instructed to notice and codify session evidence as files while working. It strengthens the survey's weak/manual trace-derived category. The design is valuable because the retained artifacts can shape future sessions, but the extraction oracle is mostly agent compliance and human review rather than a deterministic miner or learned judge.

## Curiosity Pass

**The memory system is mostly instructionware.** The durable state files are real, but much of the system's correctness depends on Claude following long Markdown procedures. The hooks add some mechanical support, yet save, end, start, audit, and itemise remain model-executed workflows.

**The pre-compaction hook backs up files but does not update them first.** It copies the current safeguard files. If the files are stale, the backup preserves stale state. The README frames this as a safety net, and the code supports that narrower claim.

**The git recovery behavior is ambitious.** `/start` can detect and commit orphaned work from interrupted sessions. That is useful continuity machinery, but it gives a recovery command write authority over source control unless the project mode disables it.

**Pagination solves context volume by policy, not retrieval.** Archive pages are retained and usually skipped. That is a practical context-saving choice, but there is no index, ranking layer, or query tool for finding old archived content beyond explicit user request or audit logic.

**Itemisation is both navigation aid and maintenance burden.** Addressable sections can reduce context cost, but the sidecar parity contract means every future code edit carries an extra artifact-maintenance obligation.

## What to Watch

- Whether Context Guard adds deterministic parsers for task, decision, comment, and session-log consistency; that would move more authority from prose compliance into symbolic validation.
- Whether pre-commit reminders become hard gates or configurable policy checks; that would change the hook from advisory activation to enforcement.
- Whether archive pages gain searchable indexes or source pointers; that would improve recovery from old history without making raw history default context.
- Whether `/save` or `/end` records source pointers from each retained decision, task, or learned behavior back to specific comments, plans, commits, or audit reports.
- Whether itemisation proves useful outside small codebases; its maintenance cost may dominate unless audits catch stale sidecars cheaply.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Context Guard is a weak/manual, doctrine-mediated session-capture system whose outputs shape later Claude Code sessions.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: Context Guard's same Markdown files change authority depending on whether they are read as evidence, instructions, audit inputs, or hook targets.
- [Use Trace-Derived Extraction As Meta-Learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - qualifies: session traces become task records, decisions, comments, learned behavior, and resume state through agent-mediated extraction.
- [Preserve Evidence Without Making History The Next Context](../../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md) - aligns: archive pages and backups preserve history while `/start` normally loads only current files and recent plans.
- [Session history should not be the default next context](../../notes/session-history-should-not-be-the-default-next-context.md) - contrasts: Context Guard tries to rebuild a selected next context from files rather than inherit the raw chat transcript.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - supports: Context Guard adds `/start` and hook activation paths so stored project state can affect later action.
- [Always-loaded context mechanisms in agent harnesses](../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) - compares: `CLAUDE.md`, slash commands, and hooks use different loading cadences and authorities inside one Claude Code scaffold.
