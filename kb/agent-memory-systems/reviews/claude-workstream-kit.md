---
description: "Claude Workstream Kit review: repo-local active-work memory for Claude Code with ACTIVE.md resume, workstream closure, gates, and verifier agents"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
last-checked: "2026-06-12"
---

# Claude Workstream Kit

Claude Workstream Kit, by ChristopherA, is a Claude Code project-continuity kit. It installs project-local `.claude/` instructions, skills, agents, hooks, and `.state/` seed files so multi-session work lives in git-versioned Markdown rather than account memory, chat history, or a remote tracker. I reviewed revision `35327d7e398faa86d0e0a83f9e7cea90a122a342`.

**Repository:** https://github.com/ChristopherA/claude-workstream-kit

**Reviewed commit:** [35327d7e398faa86d0e0a83f9e7cea90a122a342](https://github.com/ChristopherA/claude-workstream-kit/commit/35327d7e398faa86d0e0a83f9e7cea90a122a342)

**Last checked:** 2026-06-12

## Core Ideas

**The retained memory is the active work state, not general project knowledge.** The README defines a workstream as two small Markdown files: `workstream.md` for purpose, backlog, decisions, learnings, and deletion criteria, plus `ACTIVE.md` for the current task, next action, and blockers.

> - `.state/workstreams/<type>/<name>/workstream.md` — everything durable about the work: purpose, task backlog (checkboxes, phase-prefixed IDs), decisions with reasoning, learnings, and the deletion criteria that gate closure.
> - `.state/ACTIVE.md` — the per-project session pointer: which workstream is active, the current task, what's next, what's blocked.
> --- [README.md](https://github.com/ChristopherA/claude-workstream-kit/blob/35327d7e398faa86d0e0a83f9e7cea90a122a342/README.md)

**Session-start read-back is implemented by a hook plus an always-read convention.** Installation registers `.claude/hooks/session-start.sh` as a Claude Code `SessionStart` hook, and the hook prints `ACTIVE.md`, active-workstream counts, staleness signals, and handoff inbox counts. The installed `.claude/CLAUDE.md` tells the agent to respond to that hook before other work and to read the active `workstream.md` if one exists.

> At session start the hook prints `ACTIVE.md` plus a one-line status of the active workstream. Respond to it before other work:
> --- [.claude/CLAUDE.md](https://github.com/ChristopherA/claude-workstream-kit/blob/35327d7e398faa86d0e0a83f9e7cea90a122a342/.claude/CLAUDE.md)

**Lifecycle closure is first-class and destructive to the active state.** The close skill requires a narrative summary, disposition of each learning and open question, per-deletion-criterion evidence, user approval, an `ARCHIVE.md` line, a `ws/<name>` git tag, removal of the workstream directory, reset of `ACTIVE.md`, and a commit. That is stronger lifecycle design than a growing project note, although it is still agent-obedience driven.

> For each deletion criterion, show the criterion and its evidence (file, commit, test output). Unsatisfied criteria mean the workstream is not ready — say so and stop. When all criteria have evidence, ask the user to approve closure. Never self-certify.
> --- [.claude/skills/workstream-close/SKILL.md](https://github.com/ChristopherA/claude-workstream-kit/blob/35327d7e398faa86d0e0a83f9e7cea90a122a342/.claude/skills/workstream-close/SKILL.md)

**Evidence gates are procedural, not hard validators.** The work skill says a done claim must cite a commit, command output, or count, and the close skill says criteria need evidence before user approval. The only shipped deterministic check I found is an acceptance script that drives `claude -p` through create/work/close and greps the resulting state; there is no standalone validator that rejects an unsupported checkbox in ordinary use.

> Every "done" claim cites its evidence: a commit hash, a passing command's output, a count. No evidence, no checked checkbox.
> --- [.claude/skills/workstream-work/SKILL.md](https://github.com/ChristopherA/claude-workstream-kit/blob/35327d7e398faa86d0e0a83f9e7cea90a122a342/.claude/skills/workstream-work/SKILL.md)

**Fresh-context verification is specified as an agent role.** The kit ships a `verifier` subagent whose job is to re-derive claims from files and command output, and the work skill directs the orchestrator to use it after worker packets. That is a real harness-level verification affordance, but the repository relies on Claude Code and the agent following the role contract rather than enforcing fresh-context checks in a separate runner.

> You verify work you did not produce. You receive a specification (the packet, task description, or claim list) and check it against reality.
> --- [.claude/agents/verifier.md](https://github.com/ChristopherA/claude-workstream-kit/blob/35327d7e398faa86d0e0a83f9e7cea90a122a342/.claude/agents/verifier.md)

**Context efficiency is one active pointer plus one active file.** The design deliberately avoids loading all history: `ACTIVE.md` is kept under about 15 lines, one active `workstream.md` holds the durable active scope, and closed streams move to an archive index and tag. There is no ranking, search, embedding, or summarizer; the efficiency mechanism is small files, project scoping, and deletion of active-state directories at closure.

## Artifact analysis

- **Storage substrate:** `files` `repo` - The behavior-shaping state is project-local Markdown under `.state/`, `.claude/` skills/rules/agents/hooks/settings, and git commits/tags; the installer copies these into the target repository and seeds `.state/` without overwriting existing active state.
- **Representational form:** `prose` `symbolic` - Workstream purpose, decisions, learnings, closure summaries, skills, and agent specs are prose; frontmatter fields, checkbox task IDs, status values, hook JSON, shell scripts, grep counts, git tags, and archive-line formats are symbolic.
- **Lineage:** `authored` `trace-extracted` - The kit's rules, hooks, templates, and skills are authored system-definition artifacts; installed workstream files are authored at creation and then updated from session work, command outputs, git state, user gates, worker packets, verifier findings, and closure evidence.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` - `workstream.md`, `ACTIVE.md`, handoffs, and archive entries supply remembered work context; `.claude/CLAUDE.md` and skills instruct Claude Code; fixed paths and active pointers route reads; evidence rules, verifier specs, staleness warnings, and the acceptance script validate, mostly procedurally.

**Installed kit layer.** Storage substrate: copied `.claude/CLAUDE.md`, `.claude/rules/`, `.claude/skills/`, `.claude/agents/`, hooks, `settings.json`, and a version stamp. Representational form: prose instructions plus symbolic hook registrations and shell. Lineage: authored package files installed into each project. Behavioral authority: instruction, routing, and validation for Claude Code sessions.

**Active workstream state.** Storage substrate: `.state/ACTIVE.md` and `.state/workstreams/<type>/<name>/workstream.md`. Representational form: prose sections with symbolic frontmatter, task IDs, checkboxes, `#G-` gates, dates, and deletion criteria. Lineage: created from user interview answers and then trace-updated from actual work. Behavioral authority: knowledge and instruction; it tells later sessions what exists, what is current, what is blocked, and what must be true before closure.

**Session-start hook.** Storage substrate: shell script plus Claude Code settings. Representational form: symbolic shell over files/git and printed prose status. Lineage: authored kit code reading current project state. Behavioral authority: push read-back and validation warning; it surfaces active work and staleness before the agent chooses its next action.

**Verifier and acceptance test.** Storage substrate: `.claude/agents/verifier.md` and `tests/va3-acceptance.sh`. Representational form: prose role contract, shell checks, and Claude CLI prompts. Lineage: authored tests/specs over installed behavior. Behavioral authority: validation/evaluation, but only when invoked; ordinary state edits are not guarded by a mandatory validator.

Promotion path: the kit promotes conversation/work activity into `workstream.md` and `ACTIVE.md`, then closes the stream by moving durable insights elsewhere, writing an archive line, tagging git, and deleting active state. It does not promote memories into executable tools, schemas, or enforced validators beyond the hook/test/shell conventions.

## Comparison with Our System

| Dimension | Claude Workstream Kit | Commonplace |
|---|---|---|
| Primary purpose | Preserve active multi-session work state in one project | Maintain a typed methodology KB for agents |
| Main artifact | `.state/ACTIVE.md` plus one `workstream.md` | Typed Markdown notes, reviews, instructions, source snapshots, indexes |
| Write path | Claude Code skills update checkboxes, evidence, ACTIVE, closure artifacts | Direct artifact edits governed by collection contracts, validation, and review |
| Read-back | Session-start hook pushes ACTIVE and status; skills pull the active workstream | Mostly pull through search, indexes, links, skills, and loaded instructions |
| Governance | User gates, evidence prose, verifier agent, staleness hook, acceptance script | Schemas, validators, citation rules, review gates, generated indexes |

The kit is closest to Commonplace's workshop layer, not the durable note library. It gives active work a lifecycle that Commonplace usually handles through ad hoc work directories, session summaries, or current-agent discipline. The main tradeoff is that Claude Workstream Kit keeps the mechanism tiny and portable, but it encodes most quality gates as instructions to Claude rather than as independently executable validation.

For the requested lens, the implementation does provide project-scoped active-work memory: `.state/` is seeded into the target project, the state is intended to be committed, and the session-start hook reads the target project via `CLAUDE_PROJECT_DIR`. It also provides lifecycle closure and fresh-context verification as shipped skill/agent contracts. The weaker parts are enforcement depth and evidence auditability: unsupported evidence notes are possible unless the user, verifier, or an external test catches them.

### Borrowable Ideas

**A tiny active-work pointer separate from durable knowledge.** Ready now. Commonplace could use a small `ACTIVE.md`-style work pointer for long-running workshops without turning transient state into KB notes or indexes.

**Closure deletes the active workspace after extracting learnings.** Ready for workshop lifecycle design. The kit's close skill forces each learning/open question to be applied, handed off, or dropped before archive.

**Session-start staleness signals.** Ready now. A bounded hook that compares active-state dates with recent commits would help agents notice work happening outside the declared workshop or review run.

**Fresh-context verifier as a named role.** Ready with stronger harness support. Commonplace already runs review gates; this pattern suggests making "verify work you did not produce" a separate context whenever a worker edits bounded files.

**Do not borrow evidence gates without executable checks for high-authority artifacts.** Ready as a caution. The kit's gates are useful because the artifact is active work state; Commonplace notes and instructions need deterministic validation and semantic review when claims become durable.

## Write side

**Write agency:** `manual` `automatic` - Humans choose workstream scope, approve gates, and can edit state files; Claude Code skills are instructed to create/update `ACTIVE.md`, check off tasks with evidence, commit state, write handoffs, and archive/delete workstream directories.

**Curation operations:** `invalidate` `promote` - Closure invalidates the active workstream as current state by archiving/tagging it and removing its active directory, while learnings are promoted out of `.state/` into named durable files, handoffs, or explicit drops. The kit does not automatically deduplicate, consolidate, decay, or synthesize stored memories across workstreams.

### Trace-derived learning

**Trace source:** `tool-traces` `event-streams` - The write path records active-session outcomes, user gates, command outputs, verifier results, git status/commits/tags, and handoff events into durable workstream files. It does not parse raw chat transcripts or session logs.

**Learning scope:** `per-project` - `.state/` is scoped to the target project; handoffs can cross projects, but receiving requires explicit triage into that project's state.

**Learning timing:** `online` `staged` - Workstream files are updated during work and session exit, while creation, work, handoff, close, and session-start reconciliation are staged skill/hook occasions.

**Distilled form:** `prose` `symbolic` - Session activity becomes prose purpose, decisions, learnings, summaries, and evidence notes plus symbolic task IDs, checkboxes, frontmatter, archive lines, and git tags.

**Extraction.** Extraction is instruction-mediated. The kit does not parse raw Claude transcripts into memories; instead, the acting agent writes the active work state from the current session's actual artifacts, commits, command outputs, user approvals, and verifier findings. That is trace-derived operational memory, but not autonomous log mining.

**Scope and timing.** The active memory is per project and per workstream. It is updated online as work progresses and staged at explicit lifecycle moments. Closed work stays recoverable through git tags and an archive line, but it is deliberately removed from the active read set.

**Survey placement.** Claude Workstream Kit is in the trace-to-active-work-ledger family. It strengthens the distinction between durable memory and active memory: the valuable retained artifact is not a lesson database but a lifecycle-governed pointer to unfinished work, with closure extracting anything that should survive.

## Read-back

**Read-back:** `both` - The session-start hook pushes `ACTIVE.md`, active-workstream status, staleness, and handoff counts into a new Claude Code session; the agent then deliberately pulls the active `workstream.md`, archive pages, or handoff files when the installed conventions/skills tell it to.

**Read-back signal:** `coarse` `identifier` - The push fires coarsely at session start for any project with `.state/`, then routes by fixed project-relative identifiers such as `.state/ACTIVE.md`, the active `workstream:` path, `.state/handoffs/`, and `ARCHIVE.md`.

**Faithfulness tested:** `no` - The repository ships an acceptance script that exercises create/work/close through Claude and greps resulting files, but the runtime system does not ablate or audit whether a session-start memory actually changed downstream model behavior.

**Targeting and signal.** The hook is not relevance-ranked to the current user prompt. It prints the active pointer and counts because a session has started in a project. Instance targeting comes only through identifiers already present in state: active workstream path, task pointer, handoff directory, and archive/tag names.

**Injection point.** Read-back happens at session start before work begins. The hook prints before task work, and `.claude/CLAUDE.md` tells the agent to read the active workstream before proceeding. Commit-time state updates, closure, and archiving are write-side maintenance, not read-back.

**Selection, scope, and complexity.** Selection is intentionally simple: keep `ACTIVE.md` tiny, read one active workstream, count open tasks/gates, and skip closed work unless needed. Complexity is bounded by one active ledger, but the active file can still mix purpose, tasks, decisions, learnings, open questions, and deletion criteria.

**Authority at consumption.** `ACTIVE.md` and `workstream.md` have advisory and procedural authority through Claude Code instructions. `#G-` gates and deletion criteria are user-authority moments, but the hard stop is an instruction, not a shell-enforced block.

**Faithfulness.** The shipped verifier role tests produced work against a specification, and the acceptance script checks several lifecycle outcomes. Neither proves that recalling a workstream at session start caused the agent to behave correctly; it proves the kit has a structural read-back path and testable lifecycle outputs.

**Other consumers.** Humans can read and edit the same state files, git tags, archive lines, and handoff files. That inspectability is the main governance affordance.

## Curiosity Pass

**The design claim mostly matches the implementation.** The repo really does ship project-scoped active-work files, a session-start hook, lifecycle skills, verifier/scout/worker agents, and an acceptance script. The claim that this is "validated directly" rests on `tests/va3-acceptance.sh`, which is itself a Claude CLI integration script rather than a hermetic unit test.

**The hook surfaces only the pointer, not the full memory.** `session-start.sh` prints `ACTIVE.md` and counts, then the convention tells the agent to read `workstream.md`. That is a reasonable context-efficiency choice, but the full recall still depends on the agent following the instruction.

**Evidence is text unless someone checks it.** A checkbox can include a commit hash or command output, but the ordinary workflow has no parser that verifies the cited commit or reruns the command. The verifier agent is the intended check.

**Closure is unusually explicit for a lightweight kit.** Removing the active directory after archive prevents stale active memory from lingering in startup context, which is the failure mode the design criticizes in growing `CLAUDE.md` files.

**There is no general memory retrieval layer.** This is a workstream system, not a vector memory or knowledge base. That narrowness is a strength for active-work continuity and a limitation for reusable lessons across unrelated workstreams.

## What to Watch

- Whether the kit adds a deterministic validator for workstream frontmatter, checkbox evidence, gate state, archive/tag consistency, and `ACTIVE.md` pointers; that would turn procedural gates into enforceable ones.
- Whether session-start read-back starts loading a compact active-work summary instead of only pointer/count status; that would change the context-efficiency/readiness tradeoff.
- Whether verifier use becomes observable in state files or commits; otherwise "fresh-context verification happened" remains hard to audit after the fact.
- Whether learnings promoted at closure gain source pointers back to the workstream/tag that produced them; that would make extracted durable knowledge more reviewable.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Workstream Kit matters because active state is read back at session start, not merely stored in files.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: state files, skills, hooks, agents, tests, and git tags carry different forms and authorities.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: workstream purpose, decisions, learnings, handoffs, and archive entries mostly serve as retained context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: installed Claude instructions, skills, hook settings, verifier role, and lifecycle rules define behavior.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - relates: the kit turns session/tool outcomes into durable active-work state and extracts learnings at closure.
- [A functioning knowledge base needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) - exemplifies: the kit implements a small workshop layer with active state, closure, archive, and extraction.
- [Session history should not be the default next context](../../notes/session-history-should-not-be-the-default-next-context.md) - exemplifies: the kit stores work history in files while pushing only a compact active pointer at session start.
