---
description: "Claude Context Guard review: Claude Code safeguard files, slash-command recovery workflows, hooks, archives, and manual trace-to-ledger continuity"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-05-16"
---

# Claude Context Guard

Claude Context Guard, from atreiou's `claude-context-guard` repository, is a Claude Code continuity scaffold. It installs project-local slash commands, hooks, settings, and templates that turn a repository into an explicit state machine for agent work: current instructions, session history, task registry, decision register, comments log, feature tracker, learned behavior log, resume state, plan archives, audits, compaction backups, and optional numbered code indexes.

**Repository:** https://github.com/atreiou/claude-context-guard

**Reviewed commit:** [7e09e5b53099ef7b11fd400db39656e766d2e6fa](https://github.com/atreiou/claude-context-guard/commit/7e09e5b53099ef7b11fd400db39656e766d2e6fa)

**Last checked:** 2026-05-16

## Core Ideas

**The installed product is mostly markdown system-definition artifacts.** The installer copies five slash-command files, two hook scripts, optional Claude settings, and safeguard templates into a target project, with an extra parent-directory install option when Claude Code is launched above the project root ([install.sh](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/install.sh)). The commands are not helper prose on the side; once placed under `.claude/commands/`, they instruct Claude Code's acting agent how to start, audit, save, end, and itemise work ([.claude/commands](https://github.com/atreiou/claude-context-guard/tree/7e09e5b53099ef7b11fd400db39656e766d2e6fa/.claude/commands)). Storage substrate is the project filesystem. Representational form is prose instructions plus symbolic frontmatter, checklists, tables, JSON, and shell snippets. Behavioral authority is high because command invocation places these files in the agent's instruction path.

**Safeguard files are split by future consumer and authority.** The `CLAUDE.md` template tells future agents to read `RESUME_STATE.md`, `SESSION_LOG.md`, `TASK_REGISTRY.md`, `DECISIONS.md`, `LEARNED_BEHAVIOUR.md`, `FEATURE_LIST.json`, `COMMENTS.md`, plans, and audits before work; it also encodes version-control, checkpoint, comment-preservation, pagination, itemisation, and index-maintenance rules ([templates/CLAUDE.md](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/templates/CLAUDE.md)). The logs and registries are knowledge artifacts when read as evidence of prior state. The same files become system-definition artifacts when `CLAUDE.md` and slash commands require future agents to follow them as constraints, recovery input, audit source, or commit policy.

**Session recovery is a command-mediated context loader.** `/start` locates the Context Guard root, handles first-run setup from templates, reads current safeguard files, notes archive pages without loading them, checks git state, detects orphaned sessions, optionally commits recovered work, reads the last three plans, cross-references plan items against the task registry, and summarizes only actionable recovery state for the user ([.claude/commands/start.md](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/.claude/commands/start.md)). The design is activation-first: memory is useful because a named command loads it before the next work session, not because it sits in files.

**Audit and save commands make continuity a repeated governance routine.** `/audit` verifies git state, task counts, plan cross-references, comments, decision categories, session log consistency, safeguard existence, archive pages, and itemised sidecar freshness/parity, then saves an audit report under `audits/` ([.claude/commands/audit.md](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/.claude/commands/audit.md)). `/save` and `/end` require the agent to update resume state, session log, task registry, comments, decisions, learned behavior, and feature QA state before committing or closing the session ([.claude/commands/save.md](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/.claude/commands/save.md), [.claude/commands/end.md](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/.claude/commands/end.md)). The implementation is procedural rather than autonomous: the agent is the extraction and update mechanism, with user audit as the accountability surface.

**Archive files are retained evidence, not default context.** The README and templates define pagination for `SESSION_LOG`, `TASK_REGISTRY`, `DECISIONS`, `COMMENTS`, and `LEARNED_BEHAVIOUR`; `/save` and `/end` keep active or recent material in the current files and rotate older or actioned material to `*_pageN.md` archives ([README.md](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/README.md), [.claude/commands/save.md](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/.claude/commands/save.md)). `/start` notes archive existence but does not load archives by default; `/audit` reads more history when cross-reference checks require it. This gives archives evidence authority without automatically spending context on them.

**The shell-enforced layer is narrow.** `settings.json` wires a `PreToolUse` hook for Bash commands and a `PreCompact` hook for compaction ([.claude/settings.json](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/.claude/settings.json)). The pre-commit hook reads the Bash tool payload with `jq` and prints a reminder when the command contains `git commit`, but it always exits 0, so it advises rather than blocks ([.claude/hooks/pre-commit-check.sh](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/.claude/hooks/pre-commit-check.sh)). The pre-compaction hook creates a timestamped `compaction-backups/` directory and copies several safeguard files there, which is real shell-enforced backup behavior but not a full save or semantic update ([.claude/hooks/pre-compact-save.sh](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/.claude/hooks/pre-compact-save.sh)).

**Itemisation turns code into addressable context, but by instruction rather than parser.** `/itemise` instructs Claude to add numbered markers to source files, preserve existing code/comments, create backups, verify no semantic code changes, and generate `<source>.index.md` sidecars with section descriptions and last-edit dates ([.claude/commands/itemise.md](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/.claude/commands/itemise.md)). The `CLAUDE.md` template then makes source and sidecar a single split artifact whose parity must be maintained on later edits ([templates/CLAUDE.md](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/templates/CLAUDE.md)). This is a context-addressing convention, not a robust code-indexing engine: the operative authority comes from installed instructions and audit checks.

## Comparison with Our System

| Dimension | Claude Context Guard | Commonplace |
|---|---|---|
| Primary purpose | Keep one Claude Code project recoverable across sessions, compaction, rate limits, and missed saves | Build an agent-operated methodology KB with typed notes, references, instructions, validation, and reviews |
| Storage substrate | Project-local markdown, JSON, archives, plans, audit reports, compaction backups, `.claude/` commands/hooks | Git-tracked markdown collections, schemas, sources, generated indexes/reports, Python commands |
| Main behavior-shaping artifacts | `CLAUDE.md`, slash-command markdown, hook settings, task/decision/comment/session ledgers | Type specs, collection conventions, instructions, skills, validators, generated indexes, review gates |
| Activation | `/start`, `/save`, `/end`, `/audit`, `/itemise`, Claude Code hooks | `rg`, indexes, descriptions, authored links, skills, validation and review commands |
| Lineage | Good human-readable trail for sessions, tasks, comments, plans, archives, and audits; weak source IDs inside distilled decisions/learned behavior | Source-pinned reviews, snapshots, frontmatter, authored links, replacement archives, validation outputs |
| Enforcement | Mostly instruction/advice; pre-compaction backup is real shell action; pre-commit is reminder-only | Deterministic validators, schemas, review commands, file contracts, git history |

Claude Context Guard and commonplace share the filesystem-first premise: future agents behave better when important state survives as inspectable files. Both treat memory as context engineering rather than as a vector-store feature. Both also distinguish current operational state from older retained evidence, though Context Guard does so through pagination rules while commonplace does it through typed collections, statuses, generated indexes, and review lifecycle.

The main divergence is artifact contract strength. Context Guard's ledgers are practical and agent-readable, but their schemas are mostly prose/table conventions. Commonplace has more explicit type specs, link vocabulary, validation, review status, and collection-local quality bars. Context Guard is stronger as a drop-in continuity harness for ordinary projects; commonplace is stronger as a long-lived library whose artifacts are meant to accumulate and be re-used by many future agents.

The authority boundary also differs. In Context Guard, a user comment copied into `COMMENTS.md` is initially a knowledge artifact: evidence of what the user said. If the agent turns it into a `DECISIONS.md` entry, `TASK_REGISTRY.md` constraint, or `CLAUDE.md` rule, it gains system-definition authority over future work. The system relies on the acting agent to perform that promotion faithfully. Commonplace prefers making those boundaries explicit through artifact types and validation.

Context Guard's strongest design axis is not persistence alone but mandatory activation. `/start` requires the agent to reload the current state, detect missing work, and cross-reference plans before starting. That directly addresses the failure mode where a project has documentation but the next agent never reads it.

## Trace-derived learning placement

**Trace source.** Claude Context Guard qualifies as trace-derived learning, but in a manual, command-mediated form. The raw traces are the current conversation, user comments, task progress, plan files, git state, commit history, audit findings, code edits, and session activity observed by the acting Claude Code agent. The repository does not implement a general automatic transcript ingester; instead, slash commands require the agent to extract relevant material from the live session into durable files.

**Extraction.** Extraction is procedural and agent-authored. `/save` and `/end` tell the agent to identify new comments, task changes, decisions, tactical learned behavior, feature QA updates, in-flight state, errors, and next steps before updating the ledgers ([.claude/commands/save.md](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/.claude/commands/save.md), [.claude/commands/end.md](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/.claude/commands/end.md)). `/start` and `/audit` then read those durable artifacts, cross-reference them against plans and git state, and surface dropped or unexplained work. The oracle is the acting agent plus the user's ability to audit; there is no separate statistical learner or reviewer gate.

**Storage substrate.** Raw-ish retained state lives in `SESSION_LOG.md`, `COMMENTS.md`, plans, git history, audit reports, and compaction backups. Distilled retained state lives in `TASK_REGISTRY.md`, `DECISIONS.md`, `LEARNED_BEHAVIOUR.md`, `FEATURE_LIST.json`, `RESUME_STATE.md`, `CLAUDE.md`, and optional `.index.md` sidecars ([templates](https://github.com/atreiou/claude-context-guard/tree/7e09e5b53099ef7b11fd400db39656e766d2e6fa/templates)). Older evidence moves to `*_pageN.md` archives rather than being deleted.

**Representational form.** Most operative parts are prose instructions and prose ledger entries. Symbolic parts include JSON feature state, task tables, decision categories, status emojis, archive naming conventions, hook settings, shell scripts, and numbered code markers. There is no distributed-parametric artifact. The behavior-shaping form is mixed: prose tells the agent what to do, symbolic conventions make cross-checking and parsing cheaper, and shell hooks provide a thin runtime wrapper.

**Lineage.** Lineage is strongest for user comments and plans because `COMMENTS.md` preserves verbatim comments and plans remain archived for cross-reference. It is moderate for session and task history because IDs, timestamps, status, and notes preserve a trail. It is weaker for promoted decisions and learned behavior: the templates provide `Source` and `Related` fields, but the implementation does not enforce source links, confidence, contradiction handling, or regeneration rules inside every distilled entry ([templates/DECISIONS.md](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/templates/DECISIONS.md), [templates/LEARNED_BEHAVIOUR.md](https://github.com/atreiou/claude-context-guard/blob/7e09e5b53099ef7b11fd400db39656e766d2e6fa/templates/LEARNED_BEHAVIOUR.md)).

**Behavioral authority.** Session logs, comments, plans, audit reports, archives, and compaction backups are knowledge artifacts when consumed as evidence. Task registry entries route and constrain future action. Decision entries, learned behavior entries, `CLAUDE.md` rules, slash commands, hook settings, and itemisation sidecar contracts are system-definition artifacts because future agents are instructed, audited, or configured by them. The pre-commit hook has reminder authority only; the pre-compaction hook has direct backup authority.

**Scope.** Scope is project-local. The system is not a cross-project memory database, but the installed conventions can be replicated across projects. Parent-directory command installation supports Claude Code working-directory quirks without changing the project-local source of truth.

**Timing.** Extraction happens at first run, session start, checkpoint, session end, audit, itemisation, and pre-compaction. `/save` and `/end` are staged manual cycles; `PreCompact` backup is online and automatic; pre-commit reminder is online but non-blocking.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), Claude Context Guard belongs in the trace-to-ledger and trace-to-instruction family. It strengthens the survey distinction between raw trace retention and authority-bearing distilled artifacts: comments, plans, and logs preserve evidence, while decisions, task constraints, learned behavior, `CLAUDE.md`, commands, and sidecar contracts shape future behavior.

## Borrowable Ideas

**Make session recovery a named activation routine.** Ready to borrow for commonplace workshops. A workshop should not rely on a future agent guessing which files to read; it should have a compact startup command or checklist that loads active state, checks drift, and surfaces only actionable context.

**Separate current state from archive evidence.** Ready as a workshop lifecycle pattern. Context Guard keeps active records short and retains older evidence in page files that are not loaded by default. Commonplace already has library/archive concepts, but workshops could use more explicit current-versus-archive loading rules.

**Preserve user comments as first-class evidence.** Worth borrowing with stronger typing. Context Guard treats verbatim comments as safety-critical because summaries can lose intent. Commonplace could use a comment-capture convention in high-stakes workshops, then promote only reviewed comments into decisions or instructions.

**Use reminder hooks without pretending they enforce policy.** Ready as vocabulary. The pre-commit hook is useful because it interrupts at the right moment, but it exits 0. Commonplace should label this kind of artifact as advisory, not validation, unless it actually blocks or checks deterministically.

**Do not borrow manual itemisation wholesale.** The addressable-code idea is useful, but asking agents to rewrite code files with numbered comments is invasive and brittle. Commonplace should prefer generated indexes, parser-backed symbols, or source-adjacent reports unless a project explicitly wants source markers.

## Takeaways

**Context Guard is a continuity harness, not a semantic memory engine.** It preserves and activates project state through files and commands. It does not retrieve by embedding, learn model weights, or autonomously mine transcripts.

**The command files are the real implementation.** Most behavior is implemented as Claude Code slash-command procedures. That still counts as implementation because those markdown files enter the agent's instruction channel.

**The system is strongest at preventing dropped work.** Task registries, plan cross-references, orphaned-work checks, comments logs, session summaries, and audits all target the same failure mode: an agent resumes without knowing what was promised, done, pending, or contradicted.

**The governance layer is mostly social and procedural.** The shell hooks back up or remind, but they do not validate ledger quality. Correct extraction from session traces depends on the acting agent following instructions and the user auditing when necessary.

**Artifact authority needs explicit labels.** The same markdown file can be evidence, advice, instruction, audit input, or commit policy depending on who consumes it and through which command. Context Guard benefits from the knowledge-artifact/system-definition-artifact split.

## Curiosity Pass

The surprising part is how little executable code is needed to get a practical memory effect. A few command files can create real behavioral authority if the host agent treats slash commands as procedures rather than documentation.

The README overstates the pre-compaction behavior if read casually. The hook copies safeguard files to `compaction-backups/`; it does not run `/save`, update task state, extract decisions, or commit work. The automatic layer preserves files, while semantic freshness still depends on normal checkpoint discipline.

`LEARNED_BEHAVIOUR.md` is the closest thing to reusable learning, but it is only as good as the agent's judgment about what counts as a hard-won tactical lesson. Without review, it can become a grab bag of local anecdotes with instruction-like authority.

The itemisation protocol is both clever and risky. It creates cheap coordinates for code navigation, but it couples source files to generated sidecars and asks agents to preserve parity manually. That is a strong convention for projects that opt in, not a general KB default.

## Open Questions

- Would users keep `/save` and `/end` discipline over many sessions, or does the system need more blocking checks?
- Should promoted decisions and learned behavior require explicit source links back to comments, plans, commits, or audit findings?
- Can `FEATURE_LIST.json` remain a QA tracker rather than drifting into a task-completion mirror?
- Should archive pagination be deterministic code instead of agent-executed prose instructions?
- Does source-file itemisation reduce context cost enough to justify modifying code files and maintaining sidecars?
- Should the pre-commit hook ever block commits when required safeguard files are stale, or is reminder-only behavior the right trust boundary?

## What to Watch

- Whether future versions add deterministic validators for task registry, decision categories, archive headers, and sidecar parity.
- Whether slash commands move from prose-only procedures toward helper scripts for pagination, cross-reference checks, and itemisation.
- Whether compaction handling evolves from backup-only to a real semantic checkpoint.
- Whether the project adds examples of mature long-running projects using Context Guard over many archive pages.
- Whether learned behavior entries gain provenance and retirement conventions strong enough to avoid stale instruction drift.

## Bottom Line

Claude Context Guard is best read as a lightweight operating discipline for Claude Code projects. Its durable memory is not an external database but a set of project files whose authority is activated by slash commands and hooks. Commonplace should borrow the explicit startup/checkpoint/audit routines, current-versus-archive distinction, and comment-preservation discipline for workshop layers, while keeping stronger type contracts, validation, provenance, and promotion boundaries before any trace-derived artifact becomes long-lived methodology.

---

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: Context Guard turns session traces, comments, plans, and git state into project ledgers, decisions, learned behavior, and recovery instructions through command-mediated extraction.
- [A functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) - exemplifies: Context Guard is a workshop continuity layer optimized for active work rather than accumulated library knowledge.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: Context Guard requires separating safeguard files, archive pages, commands, templates, hooks, and sidecars by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: logs, comments, plans, archives, and audits preserve evidence for later agents.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: `CLAUDE.md`, slash commands, decisions, task constraints, hook settings, and index-maintenance rules instruct, route, audit, or configure future behavior.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - exemplifies: Context Guard's memory works because `/start`, `/save`, `/end`, `/audit`, and hooks activate the files at specific workflow moments.
