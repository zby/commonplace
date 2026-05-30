---
description: "CORAL review: multi-agent coding harness with shared attempts, notes, skills, heartbeat prompts, and score-driven trace-to-artifact learning"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-05-16"
---

# CORAL

CORAL, from Human-Agent-Society, is a Python orchestration framework for autonomous coding and research agents. It launches multiple agent CLI subprocesses in isolated git worktrees, evaluates their commits with a task grader, and exposes shared retained state through a `.coral/public/` hub containing attempt records, notes, skills, heartbeat prompts, identities, logs, and evaluation artifacts. Its memory system is therefore not a standalone retriever; it is a run-local collaboration substrate where scored attempts and agent-written artifacts change later agent behavior.

**Repository:** https://github.com/Human-Agent-Society/CORAL

**Reviewed commit:** [ddfd2097aa42b6feb670a5d0c35c0df2f176fd89](https://github.com/Human-Agent-Society/CORAL/commit/ddfd2097aa42b6feb670a5d0c35c0df2f176fd89)

**Last checked:** 2026-05-16

## Core Ideas

**The run directory is the memory boundary.** A CORAL run creates `results/<task>/<timestamp>/` with a cloned `repo/`, per-agent worktrees, and `.coral/public/` plus `.coral/private/`. Public state is visible to agents; private grader inputs and grader environments are hidden. The public substrate is plain files: attempts, notes, skills, agent definitions, logs, heartbeats, identities, eval logs, config, and a checkpoint git repository ([README.md](https://github.com/Human-Agent-Society/CORAL/blob/ddfd2097aa42b6feb670a5d0c35c0df2f176fd89/README.md), [coral/workspace/project.py](https://github.com/Human-Agent-Society/CORAL/blob/ddfd2097aa42b6feb670a5d0c35c0df2f176fd89/coral/workspace/project.py)). The storage substrate is filesystem plus git; lineage is mostly run-local and commit/checkpoint based.

**Agent isolation and sharing are separated by worktrees and symlinks.** Each agent gets its own branch and git worktree, while runtime-specific shared directories such as `.claude/`, `.codex/`, `.cursor/`, and `.opencode/` symlink selected `.coral/public/` folders into the worktree. That lets agents see each other's attempts, notes, skills, identities, logs, heartbeat state, and eval artifacts without editing the same code checkout ([coral/workspace/worktree.py](https://github.com/Human-Agent-Society/CORAL/blob/ddfd2097aa42b6feb670a5d0c35c0df2f176fd89/coral/workspace/worktree.py), [coral/agent/manager.py](https://github.com/Human-Agent-Society/CORAL/blob/ddfd2097aa42b6feb670a5d0c35c0df2f176fd89/coral/agent/manager.py)). The isolation boundary is code; the collaboration boundary is shared retained artifacts.

**Attempts are structured traces tied to code commits and grader scores.** `coral eval` stages and commits agent changes, checkpoints shared state, writes a pending `Attempt` JSON, and optionally waits for the grader daemon. The daemon grades the commit in a detached worktree, writes score/status/feedback/metadata back atomically, increments the global eval counter, and classifies tune and grader-error attempts separately ([coral/hooks/post_commit.py](https://github.com/Human-Agent-Society/CORAL/blob/ddfd2097aa42b6feb670a5d0c35c0df2f176fd89/coral/hooks/post_commit.py), [coral/types.py](https://github.com/Human-Agent-Society/CORAL/blob/ddfd2097aa42b6feb670a5d0c35c0df2f176fd89/coral/types.py), [coral/hub/attempts.py](https://github.com/Human-Agent-Society/CORAL/blob/ddfd2097aa42b6feb670a5d0c35c0df2f176fd89/coral/hub/attempts.py), [coral/grader/daemon.py](https://github.com/Human-Agent-Society/CORAL/blob/ddfd2097aa42b6feb670a5d0c35c0df2f176fd89/coral/grader/daemon.py)). These JSON files are raw trace evidence, not distilled memory by themselves.

**Shared notes and skills are the promoted collaboration layer.** Notes are Markdown files with lightweight frontmatter and CLI search/list/read support; skills are `SKILL.md` directories with YAML frontmatter and optional scripts/examples. CORAL seeds bundled skills such as `deep-research`, `organize-files`, and `skill-creator`, then instructs agents to create or update notes and skills as they learn from experiments ([coral/hub/notes.py](https://github.com/Human-Agent-Society/CORAL/blob/ddfd2097aa42b6feb670a5d0c35c0df2f176fd89/coral/hub/notes.py), [coral/hub/skills.py](https://github.com/Human-Agent-Society/CORAL/blob/ddfd2097aa42b6feb670a5d0c35c0df2f176fd89/coral/hub/skills.py), [coral/template/coral.md.template](https://github.com/Human-Agent-Society/CORAL/blob/ddfd2097aa42b6feb670a5d0c35c0df2f176fd89/coral/template/coral.md.template), [coral/template/skills/deep-research/SKILL.md](https://github.com/Human-Agent-Society/CORAL/blob/ddfd2097aa42b6feb670a5d0c35c0df2f176fd89/coral/template/skills/deep-research/SKILL.md), [coral/template/skills/skill-creator/SKILL.md](https://github.com/Human-Agent-Society/CORAL/blob/ddfd2097aa42b6feb670a5d0c35c0df2f176fd89/coral/template/skills/skill-creator/SKILL.md)). Notes are knowledge artifacts; skills are system-definition artifacts when loaded by future agents as procedural instruction.

**Heartbeat prompts turn score events into scheduled reflection and synthesis.** The default heartbeat config fires local reflection every eval, global consolidation every ten evals, plateau-driven pivots after five non-improving real attempts, and periodic wiki linting. The manager observes finalized attempts, updates per-agent improvement counters, formats score/feedback into a prompt header, interrupts the relevant agent, and resumes it with the triggered prompts ([coral/config.py](https://github.com/Human-Agent-Society/CORAL/blob/ddfd2097aa42b6feb670a5d0c35c0df2f176fd89/coral/config.py), [coral/hub/heartbeat.py](https://github.com/Human-Agent-Society/CORAL/blob/ddfd2097aa42b6feb670a5d0c35c0df2f176fd89/coral/hub/heartbeat.py), [coral/agent/heartbeat.py](https://github.com/Human-Agent-Society/CORAL/blob/ddfd2097aa42b6feb670a5d0c35c0df2f176fd89/coral/agent/heartbeat.py), [coral/agent/manager.py](https://github.com/Human-Agent-Society/CORAL/blob/ddfd2097aa42b6feb670a5d0c35c0df2f176fd89/coral/agent/manager.py)). Reflection and consolidation prompts explicitly ask agents to write experiment notes, syntheses, open questions, skills, and identity updates ([coral/hub/prompts/reflect.md](https://github.com/Human-Agent-Society/CORAL/blob/ddfd2097aa42b6feb670a5d0c35c0df2f176fd89/coral/hub/prompts/reflect.md), [coral/hub/prompts/consolidate.md](https://github.com/Human-Agent-Society/CORAL/blob/ddfd2097aa42b6feb670a5d0c35c0df2f176fd89/coral/hub/prompts/consolidate.md), [coral/hub/prompts/pivot.md](https://github.com/Human-Agent-Society/CORAL/blob/ddfd2097aa42b6feb670a5d0c35c0df2f176fd89/coral/hub/prompts/pivot.md)).

**The agent instruction file is a generated system-definition artifact.** `generate_coral_md()` renders task description, scoring direction, shared-directory name, research mode, workflow steps, and ground rules into `CLAUDE.md`, `AGENTS.md`, or another runtime-specific instruction file. The resulting prose tells agents how to inspect attempts, read notes, use skills, publish findings, and avoid direct git operations ([coral/template/coral_md.py](https://github.com/Human-Agent-Society/CORAL/blob/ddfd2097aa42b6feb670a5d0c35c0df2f176fd89/coral/template/coral_md.py), [coral/template/coral.md.template](https://github.com/Human-Agent-Society/CORAL/blob/ddfd2097aa42b6feb670a5d0c35c0df2f176fd89/coral/template/coral.md.template), [coral/template/coral_single.md.template](https://github.com/Human-Agent-Society/CORAL/blob/ddfd2097aa42b6feb670a5d0c35c0df2f176fd89/coral/template/coral_single.md.template)). Its representational form is prose with symbolic path and command conventions; its behavioral authority is high because it is the startup instruction surface for every agent.

## Comparison with Our System

| Dimension | CORAL | Commonplace |
|---|---|---|
| Primary purpose | Multi-agent optimization harness for code/research tasks | Long-lived methodology KB for agent-operated knowledge bases |
| Storage substrate | Run-local filesystem, git worktrees, JSON attempt files, Markdown notes/skills, checkpoint repo | Git-tracked typed notes, sources, reviews, instructions, ADRs, generated indexes, validation outputs |
| Core trace | Agent commits, eval messages, scores, grader feedback, logs, checkpoint hashes | Source snapshots, review runs, validation reports, git history, authored links |
| Promoted artifacts | Notes, syntheses, open questions, skills, identities, focus notes | Notes, instructions, skills, type specs, ADRs, reviews, indexes |
| Activation | Agent startup instructions, CLI commands, shared symlinks, heartbeat interrupt/resume prompts | `rg`, indexes, descriptions, authored links, skills, validation and review workflows |
| Governance | Grader scores, heartbeat schedules, git isolation, private grader data, checkpoint history | Type contracts, link vocabulary, schema validation, review gates, curated indexes, archive/replacement lifecycle |

CORAL and commonplace share a filesystem-first design instinct. Both treat Markdown and small scripts as operational artifacts, both rely on agent-native file inspection, and both make retained state useful by placing it where the next agent will actually read it.

The main difference is time horizon. CORAL is optimized for a bounded run: many agents repeatedly change code, submit evaluations, and share discoveries while a grader supplies objective feedback. Commonplace is optimized for durable accumulation: notes and instructions are curated across tasks and validated as part of a long-lived methodology library.

CORAL is stronger as an active workshop substrate. It has built-in multi-agent scheduling, score traces, heartbeat-triggered reflection, plateau prompts, per-agent identity certificates, shared skills, and private/public separation. Commonplace is stronger on artifact contracts: frontmatter schemas, link semantics, status lifecycle, source-pinned reviews, and validation make a retained claim more reusable outside the run that produced it.

The retained-artifact split is important. A CORAL attempt JSON is a trace-derived knowledge artifact when read as evidence about prior work. A note or synthesis is a higher-level knowledge artifact. A shared skill, generated instruction file, heartbeat config, or grader configuration is a system-definition artifact because it instructs, routes, evaluates, or constrains later agents.

**Read-back:** both — agents can inspect shared files via CLI, and startup plus heartbeat prompts push retained state into context.

## Trace-derived learning placement

**Trace source.** CORAL qualifies as trace-derived learning, but the learning is mediated through agent-authored artifacts rather than an autonomous model update. Raw traces include commits, eval messages, scores, grader feedback, attempt metadata, logs, eval artifacts, shared-state checkpoint hashes, focus notes, and identity histories. The strongest implemented trace source is `.coral/public/attempts/*.json`, written by `submit_eval()` and finalized by the grader daemon ([coral/hooks/post_commit.py](https://github.com/Human-Agent-Society/CORAL/blob/ddfd2097aa42b6feb670a5d0c35c0df2f176fd89/coral/hooks/post_commit.py), [coral/grader/daemon.py](https://github.com/Human-Agent-Society/CORAL/blob/ddfd2097aa42b6feb670a5d0c35c0df2f176fd89/coral/grader/daemon.py), [coral/types.py](https://github.com/Human-Agent-Society/CORAL/blob/ddfd2097aa42b6feb670a5d0c35c0df2f176fd89/coral/types.py)).

**Extraction.** Extraction is mostly LLM-agent and prompt-mediated. The generated agent guide tells agents to inspect leaderboards, read recent attempts, write notes after evaluations, and create or update skills for reusable techniques. Heartbeat prompts force periodic reflection, synthesis, pivoting, and wiki linting after scored attempts or plateaus ([coral/template/coral.md.template](https://github.com/Human-Agent-Society/CORAL/blob/ddfd2097aa42b6feb670a5d0c35c0df2f176fd89/coral/template/coral.md.template), [coral/hub/prompts/reflect.md](https://github.com/Human-Agent-Society/CORAL/blob/ddfd2097aa42b6feb670a5d0c35c0df2f176fd89/coral/hub/prompts/reflect.md), [coral/hub/prompts/consolidate.md](https://github.com/Human-Agent-Society/CORAL/blob/ddfd2097aa42b6feb670a5d0c35c0df2f176fd89/coral/hub/prompts/consolidate.md), [coral/hub/prompts/pivot.md](https://github.com/Human-Agent-Society/CORAL/blob/ddfd2097aa42b6feb670a5d0c35c0df2f176fd89/coral/hub/prompts/pivot.md)). The oracle is a combination of grader score, agent judgment, teammate-visible evidence, and optional subagents; not a deterministic promotion rule.

**Storage substrate.** Raw traces live in JSON attempt files, log files, eval-log directories, git commits, and the shared-state checkpoint repo. Distilled artifacts live in Markdown notes, `_synthesis/` files, `_open-questions.md`, focus notes, identity certificates, and skill directories under `.coral/public/`. System-definition artifacts are then symlinked into agent runtime directories and surfaced through the generated instruction file.

**Representational form.** Raw attempts are symbolic JSON plus prose titles/feedback. Notes, syntheses, identities, and focus notes are prose with light frontmatter. Skills are mixed prose and symbolic shell/code/script artifacts. The grader and CLI are symbolic enforcement/evaluation code. There is no implemented embedding learner, ranker, fine-tune, or distributed-parametric memory in the inspected path.

**Lineage.** Attempt lineage is strong at the commit level: each attempt carries commit hash, parent hash, agent id, timestamp, score, feedback, metadata, and optional shared-state checkpoint hashes. Shared notes and skills have weaker lineage unless agents cite attempts or sources manually. The checkpoint repo preserves shared-state history, but individual promoted artifacts do not carry a mandatory derivation field back to source attempts ([coral/hub/checkpoint.py](https://github.com/Human-Agent-Society/CORAL/blob/ddfd2097aa42b6feb670a5d0c35c0df2f176fd89/coral/hub/checkpoint.py), [coral/types.py](https://github.com/Human-Agent-Society/CORAL/blob/ddfd2097aa42b6feb670a5d0c35c0df2f176fd89/coral/types.py)).

**Behavioral authority.** Raw attempt records have evidence authority: agents use them to decide what worked and what to inspect next. Notes and syntheses advise and explain. Skills, heartbeat configs, generated agent instructions, grader configs, and grader code are system-definition artifacts with instruction, routing, scheduling, evaluation, or enforcement force. Identity certificates and focus notes sit in between: they are prose knowledge artifacts about team roles, but the generated instructions tell agents to read them before choosing a lane, giving them coordination authority.

**Scope.** Learning is run-local and task-local by default. Bundled skills ship across runs, but agent-created notes and skills live in a run's shared state unless manually copied or promoted elsewhere. CORAL does not provide a built-in retirement, validation, or cross-run promotion lifecycle for learned skills.

**Timing.** Logging and attempt writing happen online during execution. Reflection and consolidation happen after finalized evaluations through heartbeat interrupt/resume cycles. Warm-start research can run before coding; plateau prompts trigger after non-improving real attempts ([coral/agent/warmstart.py](https://github.com/Human-Agent-Society/CORAL/blob/ddfd2097aa42b6feb670a5d0c35c0df2f176fd89/coral/agent/warmstart.py), [coral/agent/manager.py](https://github.com/Human-Agent-Society/CORAL/blob/ddfd2097aa42b6feb670a5d0c35c0df2f176fd89/coral/agent/manager.py)).

**Survey placement.** CORAL belongs on the trace-to-artifact / trace-to-instruction axis of the [trace-derived survey](../trace-derived-learning-techniques-in-related-systems.md). It strengthens the survey claim that raw traces are not enough: scored attempts only become behavior-changing memory when agents promote them into notes, syntheses, skills, instructions, or future experimental choices.

## Borrowable Ideas

**Use heartbeat-triggered reflection for active workshops.** Ready to borrow for commonplace workshop contexts. CORAL demonstrates a practical trigger: do not wait for agents to remember to synthesize; interrupt after meaningful events and resume with the score, feedback, and synthesis prompt.

**Keep raw attempts and promoted artifacts distinct.** Ready now as vocabulary discipline. Attempt JSONs are evidence, while notes and skills are promoted artifacts with higher behavioral authority. Commonplace should preserve this split in any trace-derived workflow.

**Attach shared-state checkpoints to evaluations.** Worth borrowing when workshop state changes alongside code. CORAL's `shared_state_hash` and `parent_shared_state_hash` fields make it possible to connect a code attempt to the surrounding notes/skills state, even though promoted artifacts still need stronger per-file lineage.

**Use identity and focus artifacts for multi-agent coordination.** Useful for workshops, not library notes. CORAL's certificates and focus notes help agents specialize by lane and posture. Commonplace could borrow the idea for temporary workspaces where multiple agents are active, then retire it after the work is promoted.

**Do not borrow run-local artifacts as a library model.** CORAL's shared notes are intentionally lightweight and fast. They need stronger type contracts, validation, link semantics, source fields, and retirement rules before becoming durable commonplace knowledge.

## Takeaways

**CORAL is a strong workshop memory system.** Its value is not a better retriever; it is a loop that keeps experiments, scores, notes, skills, and team coordination visible while agents work.

**Trace-derived learning is real but mediated.** CORAL does not automatically learn a model or rewrite instructions from traces. It creates pressure and channels for agents to distill scored work into retained artifacts that future agents read.

**Behavioral authority is layered.** Attempts advise, notes explain, skills instruct, graders enforce, and heartbeat prompts schedule reflection. Treating all of these as "memory" would be too coarse; the useful analysis is which artifact can change which future action.

**The public/private split is a practical trust boundary.** Agents can share discoveries through `.coral/public/`, while hidden grader inputs and environments remain private. That is an important pattern for evaluation integrity.

**Lineage is strongest before promotion.** Attempts have clear commit and score lineage. Notes and skills depend more on agent discipline, so cross-run promotion would need additional metadata and validation.

## Curiosity Pass

CORAL's most important memory mechanism is not the notes parser or skill loader. It is the manager's event loop that watches scored attempts and turns them into new prompts. That makes activation event-driven rather than passive search.

The system's generated instructions are unusually strong. They do not merely explain commands; they set the agent's epistemic posture, collaboration rules, research cadence, skill obligations, and lane-selection behavior. In commonplace vocabulary, this is a system-definition artifact with much more authority than a README.

The trace-derived path is vulnerable to busywork. If agents write perfunctory notes or skills after every eval, the shared state can become noisy. CORAL partially addresses this with organize-files and consolidation prompts, but it does not validate claim quality.

## Open Questions

- Do CORAL-created skills actually improve later attempts across real tasks, or do they mostly satisfy the instruction to write a skill?
- Should promoted notes and skills carry mandatory links to attempt hashes, grader feedback, and shared-state checkpoints?
- How often do heartbeat interrupts help versus disrupting productive implementation flow?
- Can run-local learned artifacts be safely promoted across tasks without importing overfit strategies?
- Will identity certificates and focus notes remain useful as agent counts grow, or do they require stronger indexing and freshness rules?
- Should the checkpoint repo expose a higher-level diff view that explains which notes/skills changed alongside a score movement?

## What to Watch

- Whether CORAL adds typed metadata or validation for notes, skills, identity certificates, and focus notes.
- Whether accepted skills gain provenance back to attempts and scores.
- Whether heartbeat schedules become adaptive to task difficulty, grader latency, and note quality.
- Whether the web dashboard starts surfacing knowledge-artifact lineage, not just leaderboards and attempt diffs.
- Whether cross-run reuse becomes a first-class promotion path.

## Bottom Line

CORAL is best read as an agent-operated workshop harness with trace-derived, prompt-mediated learning. Its raw attempts, scores, logs, and checkpoints are evidence; its notes, syntheses, focus artifacts, identities, and skills are the behavior-shaping layer that agents promote from that evidence. Commonplace should borrow CORAL's event-triggered reflection, shared-state checkpoints, and public/private workshop boundary, while retaining stronger type contracts and validation before any learned artifact enters the durable library.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: CORAL turns scored attempts and shared-state traces into notes, syntheses, and skills through heartbeat-triggered agent work.
- [A functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) - exemplifies: CORAL is primarily a workshop substrate for active multi-agent optimization.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: CORAL's attempts, notes, skills, instructions, grader configs, and heartbeat prompts require separate substrate, form, lineage, and authority analysis.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - exemplifies: CORAL activates memory through generated instructions, CLI commands, shared symlinks, and heartbeat prompts.
- [Retained artifact](../../notes/definitions/retained-artifact.md) - grounds: CORAL's public files matter when they change later agent choices, not merely because they are stored.
