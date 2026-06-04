---
description: "CORAL review: multi-agent coding runs with shared .coral state, eval traces, agent-written notes/skills, checkpointed public memory, and heartbeat push prompts"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: []
status: outdated
last-checked: "2026-06-01"
---

# CORAL

> Replaced 2026-06-04. See [CORAL](./CORAL.md) for the current review.

CORAL, from Human-Agent-Society, is an orchestration system for autonomous coding-agent organizations. A CORAL run gives each agent an isolated git worktree, a generated instruction file, a shared `.coral/public/` state directory, and a central grader daemon. Its memory system is not a standalone retrieval database; it is the filesystem substrate and scheduler around an iterative eval loop where agents write attempts, notes, skills, roles, and synthesis while the manager pushes score- and heartbeat-conditioned prompts back into future work.

**Repository:** https://github.com/Human-Agent-Society/CORAL

**Reviewed commit:** [fc4252d4b9fb9b0c5532c8a6dd293f29dfac971d](https://github.com/Human-Agent-Society/CORAL/commit/fc4252d4b9fb9b0c5532c8a6dd293f29dfac971d)

**Last checked:** 2026-06-01

## Core Ideas

**The central memory substrate is `.coral/public/`, symlinked into every agent runtime.** `create_project()` creates `attempts`, `logs`, `skills`, `agents`, `notes`, `heartbeat`, `eval_logs`, and `roles` under `.coral/public/`, while `setup_shared_state()` links those directories into each worktree's runtime-native shared directory such as `.claude`, `.codex`, or `.opencode` ([workspace setup](https://github.com/Human-Agent-Society/CORAL/blob/fc4252d4b9fb9b0c5532c8a6dd293f29dfac971d/coral/workspace/project.py), [shared-state symlinks](https://github.com/Human-Agent-Society/CORAL/blob/fc4252d4b9fb9b0c5532c8a6dd293f29dfac971d/coral/workspace/worktree.py)). This is a deliberately inspectable shared-state design: agents collaborate through files, not a service-owned opaque memory API.

**Attempts are both evaluation records and future coordination memory.** `coral eval` stages and commits the agent's current work, checkpoints shared state, writes a pending `Attempt` JSON under `.coral/public/attempts/`, and optionally waits for the daemon to finalize the score ([eval hook](https://github.com/Human-Agent-Society/CORAL/blob/fc4252d4b9fb9b0c5532c8a6dd293f29dfac971d/coral/hooks/post_commit.py), [attempt types](https://github.com/Human-Agent-Society/CORAL/blob/fc4252d4b9fb9b0c5532c8a6dd293f29dfac971d/coral/types.py)). The grader daemon consumes pending attempts, grades each commit in an isolated detached worktree, classifies the result as improved/baseline/regressed/crashed/timeout, writes the finalized record atomically, and increments the global eval count ([grader daemon](https://github.com/Human-Agent-Society/CORAL/blob/fc4252d4b9fb9b0c5532c8a6dd293f29dfac971d/coral/grader/daemon.py), [attempt hub](https://github.com/Human-Agent-Society/CORAL/blob/fc4252d4b9fb9b0c5532c8a6dd293f29dfac971d/coral/hub/attempts.py)).

**The human-readable memory layer is agent-authored notes, skills, and roles.** CORAL exposes Markdown notes through `coral notes`, skill directories through `coral skills`, and per-agent role files under `.coral/public/roles/` ([notes hub](https://github.com/Human-Agent-Society/CORAL/blob/fc4252d4b9fb9b0c5532c8a6dd293f29dfac971d/coral/hub/notes.py), [skills hub](https://github.com/Human-Agent-Society/CORAL/blob/fc4252d4b9fb9b0c5532c8a6dd293f29dfac971d/coral/hub/skills.py), [role seeding](https://github.com/Human-Agent-Society/CORAL/blob/fc4252d4b9fb9b0c5532c8a6dd293f29dfac971d/coral/workspace/project.py), [query CLI](https://github.com/Human-Agent-Society/CORAL/blob/fc4252d4b9fb9b0c5532c8a6dd293f29dfac971d/coral/cli/query.py)). The generated `CORAL.md` tells agents to read prior attempts, notes, skills, roles, and focus notes before choosing new work, so shared files become team memory rather than passive logs ([instruction generator](https://github.com/Human-Agent-Society/CORAL/blob/fc4252d4b9fb9b0c5532c8a6dd293f29dfac971d/coral/template/coral_md.py), [multi-agent instruction template](https://github.com/Human-Agent-Society/CORAL/blob/fc4252d4b9fb9b0c5532c8a6dd293f29dfac971d/coral/template/coral.md.template)).

**Heartbeat is the engineered push path for eval-result memory plus maintenance instructions.** Heartbeat configuration lives as JSON in `.coral/public/heartbeat/`; defaults include local `reflect`, global `consolidate`, plateau-triggered `pivot`, and global `lint_wiki` prompts ([heartbeat hub](https://github.com/Human-Agent-Society/CORAL/blob/fc4252d4b9fb9b0c5532c8a6dd293f29dfac971d/coral/hub/heartbeat.py)). The runtime layer validates interval and plateau trigger options, including an epsilon threshold for score improvements ([heartbeat runner](https://github.com/Human-Agent-Society/CORAL/blob/fc4252d4b9fb9b0c5532c8a6dd293f29dfac971d/coral/agent/heartbeat.py)). The manager watches finalized attempts, updates per-agent score history, selects triggered actions, interrupts the committing agent, and resumes it with a combined eval-result header plus heartbeat prompts ([manager monitor loop](https://github.com/Human-Agent-Society/CORAL/blob/fc4252d4b9fb9b0c5532c8a6dd293f29dfac971d/coral/agent/manager.py)). The eval-result header is retained attempt memory; the shipped heartbeat prompt templates are baseline instruction surfaces that tell the agent which retained files to inspect rather than automatically selecting note or skill bodies.

**Context efficiency comes from scoping and progressive disclosure, not compression.** CORAL does not load all shared state into every turn. It always generates a task-specific instruction file, links shared directories into the worktree, and teaches agents to use commands like `coral log`, `coral show`, `coral notes`, and `coral skills` when needed ([instruction template](https://github.com/Human-Agent-Society/CORAL/blob/fc4252d4b9fb9b0c5532c8a6dd293f29dfac971d/coral/template/coral.md.template), [query CLI](https://github.com/Human-Agent-Society/CORAL/blob/fc4252d4b9fb9b0c5532c8a6dd293f29dfac971d/coral/cli/query.py)). The system controls complexity by splitting source worktrees, public shared state, private grader data, attempt summaries, notes, skills, and heartbeat prompts into separate surfaces. It does not do semantic retrieval over notes or automatic note summarization in the inspected code.

**Trust is delegated to the eval loop and git-like artifacts.** Attempts point to code commits, grader work happens in detached worktrees, shared-state checkpoints are committed in a local git repo, and `Attempt` records carry parent commit and shared-state hashes ([eval hook](https://github.com/Human-Agent-Society/CORAL/blob/fc4252d4b9fb9b0c5532c8a6dd293f29dfac971d/coral/hooks/post_commit.py), [checkpoint hub](https://github.com/Human-Agent-Society/CORAL/blob/fc4252d4b9fb9b0c5532c8a6dd293f29dfac971d/coral/hub/checkpoint.py), [grader daemon](https://github.com/Human-Agent-Society/CORAL/blob/fc4252d4b9fb9b0c5532c8a6dd293f29dfac971d/coral/grader/daemon.py)). This gives strong operational lineage for scores and shared-state snapshots. It does not give strong semantic lineage from an individual note sentence back to the exact attempt, log, or feedback that justified it unless the agent writes that citation.

## Artifact analysis

- **Storage substrate:** `files` — `.coral/public/attempts/<commit>.json` files, written atomically
- **Representational form:** `prose` `symbolic` — prose notes, prompts, feedback, roles, and skills wrapped by symbolic JSON, frontmatter, configs, commits, scripts, and checkpoint metadata
- **Lineage:** `authored` `imported` `trace-extracted` — authored notes/skills/roles and heartbeat configs, imported seeded templates and user config, and trace-extracted attempts, logs, eval results, checkpoints, and derived synthesis
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — shared artifacts inform agents, heartbeat and generated files instruct, manager/grader paths enforce and validate, roles/skills/configs route attention, scores rank attempts, and eval traces drive learning artifacts

**Attempt JSON records.** Storage substrate: `.coral/public/attempts/<commit>.json` files, written atomically. Representational form: symbolic JSON wrapping prose titles and grader feedback. Lineage: generated from `coral eval`, a git commit, a parent commit, optional shared-state checkpoint hashes, grader output, and budget metadata. Behavioral authority: knowledge artifacts when agents or humans inspect leaderboard history; system-definition artifacts when the manager uses score, status, budget class, timestamp, and eval count to trigger heartbeat prompts, plateau pressure, stall exemptions, and CLI filtering.

**Shared notes and synthesis files.** Storage substrate: Markdown files under `.coral/public/notes/`, symlinked into each runtime's shared directory. Representational form: prose with lightweight YAML frontmatter. Lineage: agent-authored from research, eval results, teammate attempts, and heartbeat-directed reflection/consolidation; invalidation is manual unless a later note or attempt supersedes it. Behavioral authority: knowledge artifacts when read as evidence, context, advice, or coordination state. They become weak system-definition artifacts only when a prompt instructs agents to treat them as planning inputs.

**Shared skills.** Storage substrate: directories under `.coral/public/skills/` with `SKILL.md` descriptors and optional scripts or references. Representational form: prose instructions, symbolic frontmatter, and executable files. Lineage: seeded from bundled template skills, copied from user config, or agent-authored during a run. Behavioral authority: stronger than notes: a skill is a system-definition artifact when loaded by an agent runtime as procedure, tool-routing guidance, or executable workflow; it is also a knowledge artifact when merely inspected.

**Roles, focus notes, and team posture documents.** Storage substrate: `.coral/public/roles/<agent>.md` plus notes such as focus files and roster summaries. Representational form: prose with conventional frontmatter and cited evidence. Lineage: role files are seeded at run setup and are owned by their agent; focus and roster notes are written during work. Behavioral authority: coordination memory. They shape future task allocation and duplication avoidance by advice and social routing, not by hard enforcement.

**Heartbeat configs and prompt templates.** Storage substrate: `.coral/public/heartbeat/*.json` for configured actions and package prompt templates under `coral/hub/prompts/`. Representational form: symbolic trigger config plus prose prompt bodies. Lineage: authored defaults, task YAML configuration, or CLI edits. Behavioral authority: system-definition artifacts with direct instruction force, because the manager reads them, formats runtime-specific shared paths, interrupts agents, and injects them into the next agent session.

**Generated `CORAL.md` / runtime instruction files.** Storage substrate: generated files in each agent worktree, rendered from package templates and task config. Representational form: prose system instructions with embedded symbolic config values such as score direction, agent id, shared directory, and task description. Lineage: compiled view from `task.yaml`, templates, runtime choice, and agent id; regenerated during setup/resume. Behavioral authority: always-loaded system-definition artifact for the agent loop.

**Shared-state checkpoint repo and logs.** Storage substrate: a git repository inside `.coral/public/`, plus runtime logs under `.coral/public/logs/` and eval artifacts under `.coral/public/eval_logs/`. Representational form: git commits, text logs, and arbitrary grader artifacts. Lineage: checkpoints are made at eval submission; logs are generated by agent runtimes and graders. Behavioral authority: mostly knowledge artifacts for audit and replay; checkpoint hashes also become symbolic provenance fields on attempts.

The main promotion path is trace -> agent-authored note or skill -> heartbeat/instruction-mediated future behavior. CORAL has no typed promotion gate comparable to Commonplace's note types, link vocabulary, validation, or semantic review. The path is operationally effective because the run is score-driven and short-lived, but semantic quality depends on agents citing evidence and teammates reading critically.

## Comparison with Our System

| Dimension | CORAL | Commonplace |
|---|---|---|
| Primary purpose | Run autonomous coding agents against an objective and grader | Maintain a durable methodology KB for future agents and maintainers |
| Main retained unit | Attempts, notes, skills, roles, heartbeat configs, logs, checkpoints | Typed Markdown notes, instructions, reviews, sources, indexes, schemas, reports |
| Storage substrate | Per-run filesystem under `.coral/public/`, plus git worktrees and checkpoint repo | Repository files and git history as canonical library substrate |
| Activation model | Generated instructions, pull commands, and heartbeat push prompts | Search/index/link pull, always-loaded instructions, skills, and validation/review gates |
| Governance | Numeric grader, hidden private data, isolated worktrees, heartbeat defaults, human-readable logs | Collection contracts, type specs, schemas, deterministic validation, semantic review |
| Lifespan | Run-local optimization memory | Accumulating cross-session knowledge library |

CORAL and Commonplace both bet on inspectable files as the operational memory substrate. The difference is timescale and authority. CORAL is optimized for live team performance: agents can write loosely structured notes and skills because the grader supplies fast external pressure and the run's memory can be messy if it helps the next attempt. Commonplace is optimized for durable reuse: a note can outlive the session and influence future agents without the original score context, so it needs stronger type contracts, link semantics, validation, and review.

CORAL is stronger as a scheduler around trace-derived learning. It has a real feedback loop: attempts are scored, attempts trigger prompts, prompts force reflection or consolidation, and agents can distill what they learned into shared artifacts. Commonplace has richer artifact governance but weaker built-in experimental pressure; most of its learning loop is mediated by explicit review workflows rather than a continuous grader.

**Read-back:** `both` — CORAL uses pull for notes, skills, logs, attempts, and diffs through CLI/file browsing; it uses engineered push when the manager injects the committing agent's retained eval-result memory into resumed sessions, while generated startup instructions and shipped heartbeat templates are baseline instruction surfaces rather than retained-memory read-back

### Borrowable Ideas

**Treat eval feedback as a first-class lineage source.** Ready to borrow where Commonplace runs review or validation loops. A generated note, warning, or review result should preserve the triggering command, artifact version, and result summary the way CORAL attempts preserve commit and score metadata.

**Use heartbeat-like maintenance prompts for low-frequency KB hygiene.** Ready in small form. Commonplace could trigger periodic "connect, validate, or consolidate" prompts from explicit events such as batches of new notes or repeated validation warnings, without embedding that maintenance work into every navigation instruction.

**Separate shared public memory from private evaluation material.** Ready as a design rule. CORAL's `.coral/public/` versus `.coral/private/` split maps cleanly to Commonplace's distinction between agent-consumable knowledge and hidden tests, review oracles, or benchmark fixtures.

**Checkpoint shared operational state independently from code attempts.** Worth borrowing if Commonplace adds more automated agents writing reports, warnings, or candidate notes. The useful piece is not another git repo by default; it is the idea that generated operational state should have a provenance snapshot tied to the action that consumed or produced it.

**Do not borrow loose notes as a durable library standard.** CORAL's notes are useful because they are run-local and score-adjacent. Commonplace library notes need stronger frontmatter, links, status, and validation before they can carry cross-session authority.

**Use roles and posture files as coordination memory for multi-agent work.** Needs a concrete workflow. For long-running Commonplace maintenance or survey passes, a lightweight "who owns which pass" artifact could reduce duplicate work without becoming a permanent methodology note.

## Write-side placement

**Write agency:** `manual` `automatic` — agents author notes, skills, roles, and synthesis files in the shared public state, while `coral eval`, the grader daemon, checkpointing, heartbeat state, and manager-triggered prompts automatically write or schedule retained attempt, score, checkpoint, and maintenance artifacts.

**Curation operations:** `consolidate` `synthesize` `promote` — heartbeat prompts can schedule reflection, consolidation, pivoting, and wiki linting from eval traces; agents distill scores, attempts, logs, and teammate work into notes, synthesis, roles, and skills; successful trace-derived lessons can gain stronger planning or procedural authority when they become shared skills or heartbeat/instruction-mediated coordination artifacts.

### Trace-derived learning

**Trace source:** `session-logs` `tool-traces` `event-streams` — commits, eval messages, attempt records, grader outputs, runtime logs, eval logs, checkpoints, role updates, and shared notes form the run trace around each eval event.

**Learning scope:** `per-task` `per-project` `cross-task` — learning is per CORAL run/task and shared project/team state, while notes, skills, roles, and synthesis can transfer findings across sibling agents and future attempts.

**Learning timing:** `online` — attempts are graded, manager-visible events are processed, and heartbeat-triggered extraction happens while the optimization run continues.

**Distilled form:** `prose` `symbolic` — extracted lessons become Markdown notes, role/focus/synthesis files, heartbeat-directed prose, skill instructions, JSON/frontmatter metadata, configs, scripts, and checkpoint/attempt identifiers; the review found no distributed-parametric learning layer.

**Trace source.** CORAL qualifies as trace-derived learning. Raw signals include agent commits, eval messages, attempt JSON records, grader scores, status classifications, feedback text, runtime logs, eval logs, shared-state checkpoints, role updates, focus notes, and teammate notes. The central trace boundary is the eval: each `coral eval` produces a commit, an attempt record, a grader result, and a manager-visible event.

**Extraction.** Extraction is mostly agent-mediated rather than an automatic summarizer. The generated instructions tell agents to update notes or skills after every eval, to write research summaries, to inspect top attempts, and to maintain role/focus artifacts. Heartbeat prompts make that extraction more forceful: `reflect` asks for experiment notes, `consolidate` asks for synthesis, connections, open questions, and role audits, `pivot` asks agents to read prior attempts and notes before choosing a new lane, and `lint_wiki` delegates note cleanup to a librarian subagent ([reflect prompt](https://github.com/Human-Agent-Society/CORAL/blob/fc4252d4b9fb9b0c5532c8a6dd293f29dfac971d/coral/hub/prompts/reflect.md), [consolidate prompt](https://github.com/Human-Agent-Society/CORAL/blob/fc4252d4b9fb9b0c5532c8a6dd293f29dfac971d/coral/hub/prompts/consolidate.md), [pivot prompt](https://github.com/Human-Agent-Society/CORAL/blob/fc4252d4b9fb9b0c5532c8a6dd293f29dfac971d/coral/hub/prompts/pivot.md), [wiki-lint prompt](https://github.com/Human-Agent-Society/CORAL/blob/fc4252d4b9fb9b0c5532c8a6dd293f29dfac971d/coral/hub/prompts/lint_wiki.md)).

**Storage substrate and representational form.** Raw traces persist as JSON attempt files, git commits, text logs, checkpoint commits, and grader artifacts. Distilled artifacts persist as Markdown notes, role files, synthesis files, and skill directories with prose and symbolic/executable parts. The operative forms are prose for lessons and instructions, symbolic JSON/frontmatter for routing and metadata, executable scripts inside skills, and git commits for lineage. There is no distributed-parametric learning layer in the inspected implementation.

**Lineage.** Attempt lineage is strong: commit hash, parent hash, agent id, timestamp, score/status, feedback, budget class, and optional shared-state checkpoint hashes are all recorded. Distilled-note lineage is weaker: prompts ask agents to cite attempts and evidence, but the note format and note hub do not enforce source-attribution fields. Skills similarly can contain scripts and references, but the inspected code does not require a skill to cite the attempts that motivated it.

**Behavioral authority.** Raw traces are knowledge artifacts when used for audit, leaderboard comparison, or planning evidence. They become system-definition inputs when the manager uses them for heartbeat triggering, plateau detection, restart prompts, and eval-count scheduling. Distilled notes are usually knowledge artifacts. Skills and heartbeat prompts are system-definition artifacts when they guide execution, route attention, or inject mandatory maintenance tasks into the agent's next session.

**Scope and timing.** Scope is per CORAL run and per team, with per-agent ownership for worktrees and roles. Timing is online: attempts are graded while the run continues, the manager watches new scored attempts, and heartbeat-triggered extraction happens during the live optimization loop. Shared artifacts are visible to sibling agents in near real time through symlinked public directories.

**Survey placement.** CORAL belongs in the trace-to-readable-artifact family, with the important twist that extraction is socially and scheduler-mediated rather than a single LLM summarization call. It strengthens the survey claim that trace-derived learning can operate through prose and executable skills without model fine-tuning. It also exposes a governance gap: score-grounded traces can drive useful learning, but durable semantic claims still need citation, review, and invalidation rules if they are to leave the run-local context.

## Read-back placement

**Direction.** CORAL is both pull and push from the agent's perspective. The agent pulls attempts, diffs, notes, skills, logs, and checkpoint history with CLI commands or file reads. The manager pushes retained eval-result memory after scored attempts: the resumed prompt includes the score, commit id, attempt title, and grader feedback from the finalized attempt. Generated startup instructions and bundled heartbeat prompt templates are pushed context, but they ship with the system and are not retained-memory read-back.

**Read-back signal:** `identifier` — the manager targets the matching live agent by `agent_id` from the finalized attempt and selects heartbeat actions from symbolic eval-count, budget-class, score-history, plateau, score-direction, and epsilon signals.

**Faithfulness tested:** `no` — CORAL measures downstream scores, but the review found no ablation showing that a specific pushed note, heartbeat prompt, or skill changed agent behavior.

**Targeting and signal.** The memory push is instance-targeted by identifier. The manager watches new finalized attempt files, reads the attempt's `agent_id`, and interrupts/resumes the matching live agent with that attempt's score, title, commit id, budget class, and feedback. Heartbeat action selection adds engineered control signals: per-agent eval count, global eval count, real-versus-tune budget class, score history, plateau streak, score direction, and optional epsilon thresholds. These signals choose a prompt class (`reflect`, `consolidate`, `pivot`, `lint_wiki`, or custom actions), not specific note, skill, or attempt bodies beyond the current eval-result header.

**Injection point.** Heartbeat read-back assembles after an eval is finalized and before the agent continues its next work segment. The manager interrupts the active runtime and resumes it with the combined prompt, so the pushed material can change the next plan, note-writing behavior, lane choice, or consolidation work.

**Selection, scope, and complexity.** CORAL pushes the current attempt summary and feedback for the committing agent, then selects a shipped prompt class. It may tell the agent to inspect recent attempts, top attempts, notes, skills, roles, focus notes, or synthesis files, but the agent still performs that content selection. Complexity is controlled by path scoping, CLI summaries, per-agent/global heartbeat separation, and progressive disclosure through `coral log`, `coral show`, `coral notes`, and `coral skills`. There is no top-k note retriever, token budgeter, or semantic matcher over shared notes in the inspected code.

**Authority at consumption.** Generated `CORAL.md` and heartbeat prompts have direct instruction authority over the agent loop. Attempts, notes, logs, and prior diffs have advisory knowledge authority when the agent reads them. Skills can have stronger procedural authority when the agent loads and follows their `SKILL.md` or executes bundled scripts. The grader has hard evaluation authority over attempts but does not directly edit memory artifacts.

**Faithfulness.** CORAL measures downstream task scores, but I did not find a code-level read-back faithfulness test that ablates a specific note, heartbeat prompt, or skill and checks whether the agent used it. The score loop can show that a team improved after shared memory existed; it does not by itself prove which memory artifact changed behavior.

**Other consumers.** Human operators can browse attempts, notes, skills, logs, web dashboard state, and checkpoints. The grader consumes commits and hidden private data. The manager consumes attempt records, heartbeat configs, logs, session ids, process liveness, and score history. CORAL is therefore a multi-consumer memory substrate, not just agent-facing recall.

## Curiosity Pass

**CORAL is closer to an organizational memory harness than a personal agent memory.** It remembers team attempts, artifacts, roles, and scores around an objective. User preference memory or long-term personal facts are outside its core path.

**The most behavior-shaping memory is often not the note body.** Attempt metadata, score histories, heartbeat config, and generated instructions have clearer authority than many human-readable notes. The prose memory matters through the agent's voluntary planning, while the manager's symbolic state determines when prompts arrive.

**The checkpoint repo is an underused lineage asset.** CORAL records shared-state snapshots at eval submission, but ordinary agents mostly see notes/skills and attempt rows. More explicit links from notes or skills back to checkpoint hashes would make trace-derived learning easier to audit.

**The system has real push activation without semantic relevance.** Heartbeat is engineered and behavior-shaping, but it does not know which note, attempt, or skill is relevant to the current technical bottleneck. It pushes the obligation to look, not the content most likely to help.

**The private/public split is doing epistemic work.** Hiding grader internals from agents makes scores more meaningful, while exposing attempts and notes makes learning possible. That is a cleaner separation than many memory systems that expose all traces and then rely on the model not to misuse them.

## What to Watch

- Whether shared notes and skills gain required provenance fields that cite attempt hashes, feedback, or checkpoint commits; that would make trace-derived artifacts auditable rather than merely useful.
- Whether heartbeat grows semantic or typed retrieval over notes and skills; that would move CORAL from scheduler-triggered push to relevance-gated memory injection.
- Whether role and focus files remain lightweight coordination aids or become enforced scheduling inputs for assigning agents to lanes/postures.
- Whether checkpoint history becomes part of ordinary read-back, especially for comparing how shared knowledge changed between top attempts.
- Whether CORAL adds ablations or diagnostics that measure the behavioral effect of notes, skills, or heartbeat prompts separately from the base multi-agent eval loop.

Relevant Notes:

- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: CORAL turns eval traces and score feedback into run-local notes, skills, roles, and synthesis through agent-mediated extraction.
- [Activate behavior-changing memory](../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) - exemplifies: heartbeat prompts are an engineered activation path that can change the agent's next action.
- [Evaluate memory by effects](../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) - aligns: CORAL's grader gives a downstream performance signal, though it does not isolate individual memory artifacts.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - clarifies: CORAL stores many shared files, but only generated instructions, heartbeat prompts, and agent pull commands bring them into context.
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) - frames: CORAL uses scoped commands and shared directories instead of loading the full team history.
- [Files not database](../../notes/files-not-database.md) - aligns: CORAL's shared memory is inspectable filesystem state with git-like checkpointing.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: generated instructions, heartbeat configs, skill packages, and grader rules carry instruction, routing, or evaluation force.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: attempts, notes, logs, and score feedback become evidence and advice when read by later agents.
