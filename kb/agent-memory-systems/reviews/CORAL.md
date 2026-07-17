---
description: "CORAL review: filesystem multi-agent coding hub with shared notes, skills, attempts, roles, eval feedback, heartbeat prompts, and worktree isolation"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-learning]
last-checked: "2026-06-04"
---

# CORAL

CORAL, by Human-Agent-Society, is Python infrastructure for running autonomous coding-agent organizations. At the reviewed commit it creates per-agent git worktrees, exposes shared public state through runtime-native directories, records eval attempts and grader feedback, prompts agents to write notes/skills/role descriptions, runs periodic heartbeat interventions, and keeps grader internals in a private directory hidden from agents.

**Repository:** https://github.com/Human-Agent-Society/CORAL

**Reviewed commit:** [6bcefed8e8262b0d01ab41201873d35454fe8864](https://github.com/Human-Agent-Society/CORAL/commit/6bcefed8e8262b0d01ab41201873d35454fe8864)

**Last checked:** 2026-06-04

## Core Ideas

**The memory substrate is a shared filesystem hub, not a database.** `create_project()` creates `.coral/public/` directories for attempts, logs, skills, agents, notes, heartbeat configs, roles, and eval logs, then initializes a git repo inside `.coral/public/` for checkpoints ([coral/workspace/project.py](https://github.com/Human-Agent-Society/CORAL/blob/6bcefed8e8262b0d01ab41201873d35454fe8864/coral/workspace/project.py), [coral/hub/checkpoint.py](https://github.com/Human-Agent-Society/CORAL/blob/6bcefed8e8262b0d01ab41201873d35454fe8864/coral/hub/checkpoint.py)). Each agent worktree gets symlinks from its runtime-native shared directory, such as `.claude/`, `.codex/`, or `.opencode/`, back to that same public state ([coral/workspace/worktree.py](https://github.com/Human-Agent-Society/CORAL/blob/6bcefed8e8262b0d01ab41201873d35454fe8864/coral/workspace/worktree.py), [coral/agent/runtime.py](https://github.com/Human-Agent-Society/CORAL/blob/6bcefed8e8262b0d01ab41201873d35454fe8864/coral/agent/runtime.py)).

**Attempts are the central trace object.** `coral eval` stages and commits the agent's work, checkpoints shared state, writes a pending attempt JSON, and optionally waits for the daemon to fill in score/status/feedback; the grader daemon polls attempts, grades each commit in an isolated worktree, then atomically updates the same JSON file ([coral/hooks/post_commit.py](https://github.com/Human-Agent-Society/CORAL/blob/6bcefed8e8262b0d01ab41201873d35454fe8864/coral/hooks/post_commit.py), [coral/grader/daemon.py](https://github.com/Human-Agent-Society/CORAL/blob/6bcefed8e8262b0d01ab41201873d35454fe8864/coral/grader/daemon.py), [coral/types.py](https://github.com/Human-Agent-Society/CORAL/blob/6bcefed8e8262b0d01ab41201873d35454fe8864/coral/types.py)). Attempt records also carry shared-state checkpoint hashes, so the code trace and knowledge-state trace are linked.

**Context efficiency is instruction-guided and shallow.** CORAL does not perform semantic retrieval, embedding search, or automatic summarization before loading memory. It bounds volume mostly by telling agents to use `coral log`, `coral show`, `coral notes`, and `coral skills`, with CLI limits and keyword search for attempts/notes; complexity remains low because artifacts are Markdown, JSON, YAML, prompts, and git diffs rather than nested graph context ([coral/cli/query.py](https://github.com/Human-Agent-Society/CORAL/blob/6bcefed8e8262b0d01ab41201873d35454fe8864/coral/cli/query.py), [coral/hub/notes.py](https://github.com/Human-Agent-Society/CORAL/blob/6bcefed8e8262b0d01ab41201873d35454fe8864/coral/hub/notes.py), [coral/hub/skills.py](https://github.com/Human-Agent-Society/CORAL/blob/6bcefed8e8262b0d01ab41201873d35454fe8864/coral/hub/skills.py)). The tradeoff is that recall quality depends on agent discipline and visible filenames, not on a ranked memory engine.

**Generated runtime instructions turn the shared store into an operating procedure.** `generate_coral_md()` renders runtime-specific instruction files that orient agents to the leaderboard, notes, skills, focus notes, roles, eval messages, and shared-state write rules ([coral/template/coral_md.py](https://github.com/Human-Agent-Society/CORAL/blob/6bcefed8e8262b0d01ab41201873d35454fe8864/coral/template/coral_md.py), [coral/template/coral.md.template](https://github.com/Human-Agent-Society/CORAL/blob/6bcefed8e8262b0d01ab41201873d35454fe8864/coral/template/coral.md.template), [coral/template/coral_single.md.template](https://github.com/Human-Agent-Society/CORAL/blob/6bcefed8e8262b0d01ab41201873d35454fe8864/coral/template/coral_single.md.template)). The memory system is therefore partly procedural: agents are taught when to read, when to write, and how to make discoveries legible to teammates.

**Heartbeat prompts are lightweight governance over memory use.** The manager tracks eval counts and per-agent score history, then interrupts and resumes agents with eval feedback plus configured heartbeat prompts such as `reflect`, `consolidate`, `pivot`, and `lint_wiki` ([coral/agent/manager.py](https://github.com/Human-Agent-Society/CORAL/blob/6bcefed8e8262b0d01ab41201873d35454fe8864/coral/agent/manager.py), [coral/agent/heartbeat.py](https://github.com/Human-Agent-Society/CORAL/blob/6bcefed8e8262b0d01ab41201873d35454fe8864/coral/agent/heartbeat.py), [coral/hub/heartbeat.py](https://github.com/Human-Agent-Society/CORAL/blob/6bcefed8e8262b0d01ab41201873d35454fe8864/coral/hub/heartbeat.py), [coral/hub/prompts](https://github.com/Human-Agent-Society/CORAL/tree/6bcefed8e8262b0d01ab41201873d35454fe8864/coral/hub/prompts)). This is not automatic knowledge extraction, but it is automatic timing and tasking around the knowledge store.

**Access boundaries are part of the memory design.** Public state is intentionally shared and symlinked; `.coral/private/` holds graders, hidden data, grader checkouts, and private dependencies. Generated settings and workspace guards deny agent access to private grader material while allowing worktree and public-state work ([coral/workspace/project.py](https://github.com/Human-Agent-Society/CORAL/blob/6bcefed8e8262b0d01ab41201873d35454fe8864/coral/workspace/project.py), [coral/workspace/worktree.py](https://github.com/Human-Agent-Society/CORAL/blob/6bcefed8e8262b0d01ab41201873d35454fe8864/coral/workspace/worktree.py), [docs/content/docs/concepts/shared-state.mdx](https://github.com/Human-Agent-Society/CORAL/blob/6bcefed8e8262b0d01ab41201873d35454fe8864/docs/content/docs/concepts/shared-state.mdx)).

## Artifact analysis

- **Storage substrate:** `files` — The primary retained state is file-backed under `.coral/public/`: attempt JSON, Markdown notes, skill directories, role files, heartbeat JSON, logs, eval logs, PID/state files, generated instruction files in worktrees, and a nested git repo for public-state checkpoints. Secondary substrates include per-run git worktrees, the task repository, subprocess agent sessions, and an optional LiteLLM gateway service.
- **Representational form:** `prose` `symbolic` — Notes, skills, role descriptions, heartbeat prompts, generated instructions, eval feedback, and grader explanations carry prose; attempt records, score bundles, heartbeat configs, YAML task config, symlinks, git commits, checkpoint hashes, PID/state files, CLI arguments, and permission settings are symbolic. I did not find parametric memory or learned retrieval state in the reviewed source.
- **Lineage:** `authored` `trace-extracted` `imported` — Agents and operators author notes, skills, role files, task config, grader code, and heartbeat prompts; eval attempts, logs, score histories, session ids, shared-state checkpoints, and fault dumps are extracted from agent/eval events; seed repositories, bundled skills, mounted runtime files, and configured user skills are imported into the run.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — Notes, attempts, logs, and grader feedback advise future agents as knowledge; generated runtime files and heartbeat prompts instruct; workspace permissions, private-directory separation, grader queue limits, and trauma-free but real deny rules enforce boundaries; runtime registry, symlinks, CLI commands, heartbeat triggers, and gateway routing direct access; dataclass/config checks, atomic writes, heartbeat option parsing, and grader status handling validate; leaderboards, best-score comparison, plateau streaks, and search/log ordering rank attention; trace-derived score histories and checkpoint chains update future prompts and coordination.

**Public shared state.** Storage substrate: `.coral/public/` files plus a local git repo for checkpoints. Representational form: Markdown/prose notes and skills, symbolic attempts/logs/heartbeat/roles/eval counters, and git commit hashes. Lineage: authored by agents/operators and trace-extracted from eval submissions and manager/runtime events. Behavioral authority: knowledge for agents browsing prior work, instruction when skills or generated prompts are followed, ranking through leaderboard/status views, and learning input for heartbeat timing.

**Attempt records and grader feedback.** Storage substrate: JSON files in `.coral/public/attempts/`. Representational form: symbolic fields with prose title and feedback. Lineage: trace-extracted from `coral eval`, git commits, grader results, and shared-state checkpoints. Behavioral authority: knowledge when read through `coral log`/`coral show`; ranking through score/status comparison; learning because monitor logic updates eval counts, score histories, personal bests, and plateau triggers from finalized attempts.

**Notes, skills, and roles.** Storage substrate: shared Markdown files/directories symlinked into each runtime's native shared directory. Representational form: prose guidance with symbolic frontmatter and file structure. Lineage: mostly authored by agents under generated instructions and heartbeat prompts, with bundled or user-provided skills imported at run setup. Behavioral authority: knowledge when read as findings, instruction when skill procedures or role/focus contracts steer future work, and routing when filenames, indexes, and skill names guide what to open.

**Heartbeat and resume prompts.** Storage substrate: bundled prompt Markdown, heartbeat JSON configs, manager in-memory score history, and prompt entries written into agent logs. Representational form: prose prompts plus symbolic trigger options. Lineage: authored defaults and operator edits, triggered from trace-extracted eval counts and scores. Behavioral authority: instruction and routing because the manager interrupts/resumes the agent with specific reflective, consolidation, pivot, or linting work.

**Generated instruction and runtime settings.** Storage substrate: worktree-local `CLAUDE.md`, `AGENTS.md`, or equivalent runtime settings, backed by repository templates. Representational form: prose constitution/workflow plus symbolic settings and permission rules. Lineage: authored templates assembled from task config and runtime choice. Behavioral authority: instruction and enforcement, because these files define the agent's operating loop, shared-memory protocol, and allowed access boundaries.

Promotion path: CORAL's strongest promotion path is social/procedural rather than semantic. An eval event becomes an attempt record, attempt feedback is pushed into resume/heartbeat prompts, the agent is instructed to write a note/skill/role update, and shared-state checkpointing preserves those authored artifacts beside the code attempt. The system can promote attention to a trace by ranking it on the leaderboard or triggering a pivot, but it does not itself verify or distill the content of notes into higher-authority rules.

## Comparison with Our System

| Dimension | CORAL | Commonplace |
|---|---|---|
| Primary purpose | Runtime orchestration for autonomous multi-agent coding/eval loops | Git-native methodology KB for agent-operated knowledge bases |
| Canonical memory artifact | Attempt JSON, shared note/skill/role file, generated prompt, checkpoint | Typed Markdown artifact with collection/type contract |
| Source of truth | `.coral/public/` files plus run repo/worktrees | Repository files plus generated indexes and reports |
| Write path | Eval submission, grader daemon, agent-authored shared files, heartbeat configs, checkpoints | Direct edits, snapshots, validation, semantic review, index refresh |
| Read-back | CLI/filesystem pull plus eval/heartbeat/resume prompt push | Mostly explicit pull through search, indexes, links, skills, and loaded instructions |
| Governance | Worktree/private split, generated permissions, grader daemon, queue caps, heartbeat prompts | Schema validation, collection contracts, git diffs, citations, semantic gates |

CORAL is stronger as an operational loop: it gives agents separate worktrees, a shared hub, scoring feedback, heartbeat interventions, and runtime-specific setup. Commonplace is stronger as a durable semantic corpus: its retained artifacts have explicit types, citations, validation, review workflows, and stable navigation.

The main divergence is that CORAL treats memory as run-local coordination for agents trying to improve a score. The stored artifacts are immediately useful but loosely typed: notes and skills can accumulate quickly, while their quality depends on agent discipline and later consolidation. Commonplace slows the write path to preserve meaning; CORAL speeds the loop and uses scores, roles, and heartbeat prompts to keep agents moving.

### Borrowable Ideas

**Checkpoint shared knowledge state alongside scored attempts.** Ready now as a design idea. Commonplace review runs could record the exact index/report/note state that fed a result, not just the code commit or final artifact.

**Push eval feedback into a structured reflection prompt.** Needs a concrete Commonplace workflow. For review gates or writing iterations, a short prompt containing the latest result, feedback, and next required reflective step could make failures more actionable than a passive report file.

**Use roles and focus notes as coordination artifacts.** Ready for multi-agent KB work. CORAL's role/focus split is a practical way to prevent agents from duplicating lane and posture when several agents are operating in the same repository.

**Keep private evaluator material structurally unavailable.** Ready as a constraint. CORAL's public/private split is a useful reminder that a KB can expose shared memory without exposing answer keys, graders, or hidden review material.

**Do not borrow score as semantic truth.** Ready as a guardrail. CORAL's leaderboard is useful for optimization attempts, but Commonplace claims should not become more authoritative merely because a workflow using them scored well.

## Write side

**Write agency:** `manual` `automatic` — Agents and operators manually write notes, skills, role files, task config, heartbeat settings, and code changes; automatic writes create run directories, symlinks, generated instruction files, attempt JSON, score/status feedback, eval counters, checkpoint commits, logs, PID/state files, session ids, heartbeat prompts in logs, and grader checkouts.

**Curation operations:** `promote` — CORAL automatically promotes attention by classifying attempts as improved/baseline/regressed, maintaining leaderboards and personal bests, advancing plateau streaks, and triggering heartbeat prompts. It does not automatically merge duplicate notes, summarize transcripts, or evolve stored prose in place; those are delegated to agents through prompts and skills.

### Trace-learning

**Trace source:** `session-logs` `tool-traces` `event-streams` — CORAL records agent stream logs, eval submissions, git commits, grader events, score/status transitions, checkpoint hashes, shared-state writes, process exits, stall events, and heartbeat-triggering eval counts.

**Learning scope:** `per-project` `cross-task` — Shared state is per CORAL run/project, while bundled skills and templates can seed future tasks; within a run, all agents can read the same attempts, notes, skills, roles, and logs.

**Learning timing:** `online` `staged` — Attempt records, logs, eval counters, checkpoints, and resume prompts update during operation; consolidation, role evolution, skill creation, note organization, and warm-start research are staged agent tasks triggered by generated instructions or heartbeat prompts.

**Distilled form:** `prose` `symbolic` — Raw eval/session events become symbolic attempts, score histories, checkpoint links, logs, and heartbeat triggers; agents are prompted to distill those traces into prose notes, skills, roles, focus notes, and synthesis files. There is no code-grounded parametric distilled form.

**Extraction.** The code-grounded extraction is shallow and mostly mechanical: `submit_eval()` converts an agent's commit and eval message into an `Attempt`; the daemon converts grader results into score/status/feedback; the manager converts attempt events into score histories and heartbeat prompts. Semantic extraction from logs into lessons is not automatic. Instead, CORAL asks the agent to perform that distillation by writing notes, skills, and role updates.

**Scope and timing.** The raw unit is an eval attempt, session log, or process event. The durable coordination unit is a run-local public file. Checkpointing ties a code attempt to the contemporaneous shared state, which makes later reconstruction possible even though the semantic note quality remains agent-authored.

**Survey fit.** CORAL is a trace-to-coordination system more than a trace-to-memory-mining system. It strengthens the distinction between raw trace persistence and semantic distillation: the framework records attempts and pushes prompts, but the meaning-bearing artifacts are still written by agents.

## Read-back

**Read-back:** `both` — CORAL is pull through `coral log`, `coral show`, `coral notes`, `coral skills`, filesystem symlinks, checkpoint history, and worktree inspection; it is push when the manager resumes an agent with latest eval feedback and heartbeat prompts derived from retained attempt/score history.

**Read-back signal:** `coarse` `identifier` — Generated instruction files are coarse always-present guidance about the shared store; resume and heartbeat prompts are targeted by explicit agent id, attempt ownership, eval count, score history, and configured heartbeat action name. Search through notes and attempts remains pull, even when keyword matching is used.

**Faithfulness tested:** `no` — The repository tests attempt recording, heartbeat triggers, manager seen-attempt behavior, warm-start prompts, settings, hooks, and runtime plumbing, but I did not find behavioral ablations proving that pushed feedback or heartbeat prompts reliably improve agent decisions.

**Direction edge cases.** The always-present `CORAL.md`/`AGENTS.md` runtime file is baseline instruction and does not by itself count as memory read-back. It becomes relevant here because it routes agents toward retained run artifacts. The stronger push path is manager-delivered resume/heartbeat prompts: they include the latest retained eval result and ask the receiving agent to reflect, consolidate, pivot, or continue.

**Targeting and signal.** Pull selection is manual: agents choose CLI commands, note files, skills, or attempt hashes. Push selection is symbolic. The manager watches finalized attempt filenames, reads the owning `agent_id`, increments that agent's eval count, filters tune/grader-error budget classes, updates score history, evaluates heartbeat configs, and interrupts the matching live handle with a combined prompt.

**Injection point.** Push read-back is pre-invocation relative to the next model turn. Runtime wrappers start or resume the agent CLI with the constructed prompt, and `write_coral_log_entry()` records that prompt in the log ([coral/agent/builtin/claude_code.py](https://github.com/Human-Agent-Society/CORAL/blob/6bcefed8e8262b0d01ab41201873d35454fe8864/coral/agent/builtin/claude_code.py), [coral/agent/builtin/codex.py](https://github.com/Human-Agent-Society/CORAL/blob/6bcefed8e8262b0d01ab41201873d35454fe8864/coral/agent/builtin/codex.py), [coral/agent/runtime.py](https://github.com/Human-Agent-Society/CORAL/blob/6bcefed8e8262b0d01ab41201873d35454fe8864/coral/agent/runtime.py)). Post-eval scoring, checkpointing, and heartbeat-trigger detection are write-side maintenance until their results are inserted into the next prompt.

**Selection, scope, and complexity.** Pull read-back is bounded by CLI flags such as top-N leaderboard counts, recent-note limits, keyword search, and explicit `show`/`read` targets. Push read-back is compact: latest score, commit, title, optional feedback, budget class, and one or more prompt templates. The largest context risk is not automatic over-retrieval but instruction sprawl in the generated CORAL template and uncurated growth of shared notes/skills.

**Authority at consumption.** Attempt and note reads are advisory knowledge. Heartbeat prompts and generated instructions have instruction force because they are delivered as the agent's next prompt. Workspace guards and private-directory restrictions have enforcement force. Leaderboards and score histories have ranking force, but effective authority over model behavior is not verified from code.

**Other consumers.** Humans consume the same state through CLI status/log/show/notes/skills/runs, web dashboard routes, files under `.coral/public/`, and git checkpoint history. The system is therefore both an agent memory layer and an operator-facing run observability tool.

## Curiosity Pass

**The memory system is intentionally low-tech.** CORAL gets far by making the shared files obvious, writable, and native to each runtime. That avoids opaque retrieval behavior but shifts quality control onto prompts and agent discipline.

**The strongest "learning" path is score-mediated, not semantic.** Attempts affect future behavior because their scores, feedback, and titles are searchable and pushed into heartbeat prompts. Whether the notes written after those attempts are true or useful is outside the automatic machinery.

**Prompt push is narrow but real.** The system does not push arbitrary notes into context. It pushes eval feedback and heartbeat tasks, then asks the agent to pull or write memory. That makes the push path less risky than broad always-load memory, but also less semantically rich.

**Shared-state checkpointing is underused as memory provenance.** The attempt record can store `shared_state_hash` and `parent_shared_state_hash`, but the reviewed code does not appear to turn those hashes into a normal agent-facing explanation of which notes or skills informed an attempt.

**Roles are a behavior-shaping artifact, but their quality is aspirational unless audited.** CORAL gives agents a public role file and asks for evidence-backed updates. The mechanism is promising; whether agents maintain honest, useful roles is a runtime behavior question.

## What to Watch

- Whether CORAL adds automatic semantic distillation from logs or attempts into notes/skills; that would move it from trace recording plus prompts toward a stronger trace-derived memory system.
- Whether checkpoint hashes become first-class in `coral show` or heartbeat prompts; that would make shared-state lineage easier for agents to use.
- Whether notes/skills gain schema validation or generated indexes by default; uncurated shared Markdown can become hard to navigate in long multi-agent runs.
- Whether heartbeat prompts become configurable with richer targeting over note/skill/attempt content; that would add inferred read-back beyond the current symbolic triggers.
- Whether tests add agent-behavior ablations for heartbeat and pushed feedback; without them, prompt presence should not be treated as proven behavioral uptake.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: CORAL stores attempts, notes, skills, roles, and logs, but most memory reaches agents only through explicit pull or narrow resume/heartbeat prompts.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: attempts, notes, skills, role files, heartbeat prompts, generated instructions, and access rules carry different lineage and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: attempts, logs, notes, and grader feedback mostly advise future agents as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: generated runtime instructions, heartbeat prompts, task config, workspace permissions, and grader/queue rules shape or enforce later behavior.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - relates: CORAL records eval/session traces and prompts agents to distill them, while keeping semantic extraction mostly manual.
