---
description: Multi-agent coding harness with git worktrees, checkpointed shared notes/skills, heartbeat prompts, and eval-gated iteration; strongest lightweight open-source outer loop for collaborative code search
type: note
traits: [has-comparison, has-implementation]
tags: [related-systems]
status: current
last-checked: 2026-04-07
---

# CORAL

CORAL is a Python orchestration system for autonomous coding-agent runs over a task plus grader. It clones a seed repo into a per-run workspace, creates one git worktree per agent, hides grader assets in `.coral/private/`, exposes shared notes/skills/attempt history through `.coral/public/`, and lets agents iterate by calling `coral eval` after each change. The design target is not a general knowledge base but a lightweight evolutionary harness for code tasks where multiple agents can explore in parallel, compare scores, and accumulate reusable tactics.

**Repository:** https://github.com/Human-Agent-Society/CORAL

## Core Ideas

**Per-agent git worktrees plus a shared public hub are the main coordination substrate.** `create_project()` clones the source repo into a fresh run directory, then `create_agent_worktree()` creates `coral/<agent-id>` branches in `agents/agent-N/` worktrees. Shared state lives in `.coral/public/attempts`, `notes`, `skills`, `logs`, and `heartbeat`, then gets symlinked into each runtime-specific dotdir (`.claude/`, `.codex/`, `.opencode/`). This is a strong, inspectable split between private code search and shared learning artifacts.

**Evaluation is the hard oracle that drives the loop.** `coral eval` stages and commits the current worktree, runs the grader in a separate process with a hard timeout, records an `Attempt` JSON object, assigns a status (`improved`, `baseline`, `regressed`, `timeout`, `crashed`), and increments a global eval counter. That makes the optimization loop concrete rather than aspirational: every attempt gets a code commit, a numeric outcome, and feedback that later prompts can inspect.

**Knowledge accumulation is prompt-mediated artifact learning, not a separate memory engine.** The system’s default heartbeat prompts tell agents to reflect after intervals, consolidate across notes, and pivot after plateaus. The consolidation prompt explicitly asks for synthesis notes, connections maps, open-question lists, and promotion of reusable techniques into shared skills. CORAL does persist these artifacts and even checkpoints them in a nested git repo, but the synthesis step is still whatever the current agent can infer from notes and leaderboards.

**Warm-start research makes literature review a first-class phase.** When enabled, agents spend a bounded research-only session gathering web findings into shared notes, then resume into the coding phase from the captured session ID. That is a real mechanism, not just documentation advice: the manager runs a separate research pass, waits for it to end, and relaunches each agent with a follow-up prompt to read the notes before coding.

**Runtime abstraction is real, but safety is uneven across layers.** CORAL has concrete runtime adapters for Claude Code, Codex, OpenCode, and Kiro, plus optional tmux, Docker, and LiteLLM gateway support. But the “safe evaluation” story is mostly about hiding private grader data and isolating per-agent worktrees. The Codex integration sets `approval_policy = "never"` and `sandbox_mode = "danger-full-access"`, so the strongest safety boundary is optional runtime/container isolation, not a uniformly enforced in-process sandbox.

## Comparison with Our System

| Dimension | CORAL | Commonplace |
|---|---|---|
| Primary purpose | Multi-agent optimization harness for code tasks with a grader | Filesystem-first knowledge methodology for durable agent-operated knowledge |
| Main substrate | Per-run cloned repo + per-agent git worktrees + `.coral/public` shared hub | Git-tracked markdown KB with typed notes, indexes, instructions, and workshop artifacts |
| Core oracle | Task grader with numeric score and timeout | Structural validation plus semantic review; more curation-oriented than benchmark-oriented |
| Shared knowledge form | Notes, skills, attempt logs, heartbeat config, public logs | Notes, ADRs, sources, instructions, tasks, indexes, workshops |
| Learning path | Prompted reflection over attempts and notes; reusable skills promoted manually by agents | Human/agent-authored notes and explicit distillation into instructions, skills, and scripts |
| Isolation model | Worktree per agent, hidden `.coral/private`, optional Docker, runtime-specific permissions | No harness-owned runtime isolation; separation is conceptual and repository-structural |
| Retrieval/navigation | Leaderboards, attempt search, note/skill listing, dashboard | Descriptions, indexes, links with explicit semantics, `rg`, and note-type routing |
| Knowledge structure | Flat note/skill files in a run-local workshop | Stronger long-lived structure: type templates, relationship semantics, curated indexes |

CORAL is stronger where commonplace is still comparatively thin: it has a real outer loop for repeated experimentation, benchmark-gated progress, plateau detection, and shared workshop artifacts that agents consume during the run. Commonplace is stronger where CORAL stays intentionally light: durable knowledge structure, explicit semantic links, theory about distillation/constraining/codification, and validation of the knowledge artifacts themselves.

The deepest difference is boundary placement. CORAL treats knowledge as an optimization aid inside a task run; commonplace treats knowledge as the primary product and uses workshop layers to feed it. CORAL’s notes and skills are metabolized by the run. Our notes are supposed to outlive the task that produced them.

## Borrowable Ideas

**Link each code attempt to a versioned shared-state snapshot.** The `Attempt` record stores both code parentage and a `shared_state_hash` from the nested checkpoint repo. That is a clean provenance pattern for workshop artifacts because it ties a code result to the exact note/skill state that informed it. Ready to borrow now for any experiment loop where temporary knowledge matters.

**Plateau-triggered prompts are a good compromise between free-form reflection and rigid schedules.** CORAL’s `pivot` heartbeat fires after non-improving eval streaks instead of fixed wall-clock time. That is a sharper trigger than “reflect every N turns” because it keys off evidence of local stagnation. Ready to borrow now anywhere we have a cheap notion of improvement.

**Warm-start research as a distinct session phase is stronger than a vague “research first” instruction.** CORAL makes literature review operational by giving it its own bounded pass and shared-note target. That is more reusable than embedding research advice in a monolithic prompt. Ready to borrow now as a workshop pattern.

**Run-local shared skills are a useful middle layer between notes and code.** CORAL’s public skills directory lets agents package a tactic discovered during optimization without immediately hard-coding it into the harness. That is a credible workshop-to-library bridge. Needs a clearer use case in commonplace before borrowing wholesale, because our skill layer is meant to be durable and curated rather than task-local.

**A nested git repo for ephemeral public state is clever but not free.** Versioning `.coral/public` separately gives clean history and diffability for notes/skills without polluting the optimized code repo. That is a strong pattern if the workshop layer changes quickly and independently. Needs a concrete use case first; it also adds operational complexity and encourages `git add -A` in the nested repo.

## Curiosity Pass

**The eval loop is the strongest real mechanism in the system.** The claimed property is open-ended improvement under competition. CORAL genuinely transforms edits into scored attempts with explicit provenance and restart logic, so this is not naming. The simpler alternative is “just let multiple agents edit branches and inspect commits manually.” CORAL earns its complexity here because the grader, status assignment, and leaderboard convert branch churn into a comparable search process.

**The shared-state model mostly relocates artifacts, but in a useful way.** The property is collaboration. Mechanistically, symlinking `.coral/public` into each worktree does not synthesize knowledge; it gives every agent a common inspectable artifact pool. The simpler alternative is a normal shared branch or external database. CORAL’s file-backed public hub is the cheaper and more inspectable choice, but its ceiling is still governed by how good the agents are at writing and re-reading those artifacts.

**“Self-evolution” overstates how much learning is automated.** The repo does promote repeated work into notes and skills, and that matters. But even if it works perfectly, the ceiling is prompt-mediated workshop curation: agents read attempts, write notes, and sometimes package tactics as skills. There is no independent deduplication engine, contradiction manager, retirement policy, or artifact validator. This is real trace-to-artifact learning, but it is lighter than the naming suggests.

**The checkpoint repo adds provenance more than intelligence.** The claimed property is durable shared memory across the run. The mechanism is a local git repo over `.coral/public` with commit hashes threaded into attempt metadata. That is genuine versioning, not just relocation, but it still does not change the semantic shape of the knowledge. The simpler alternative is timestamped flat files. CORAL’s choice is better because diffs and history matter when multiple agents keep mutating shared notes and skills.

**The safety story is narrower than the README headline implies.** The property is safe autonomous experimentation. The mechanism hides private grader files, scopes some permissions, and optionally runs in Docker. But the default Codex path explicitly disables approvals and grants full filesystem access inside the worktree. So the safety that is clearly implemented is evaluation boundary protection and run isolation, not a general-purpose execution sandbox. The simpler alternative is no boundary at all; CORAL is better than that, but the label should be read narrowly.

## What to Watch

- Does CORAL add stronger lifecycle management for shared notes and skills: deduplication, retirement, contradiction handling, or validation?
- Does the system remain lightweight as the run-local workshop grows, or do note/skill/search surfaces become noisy without better structure?
- Do the runtime adapters converge on a clearer safety model, or does each agent keep a different autonomy/sandbox story?
- Does the “self-evolution” path expand beyond prompted artifact learning into stronger trace mining or even weight updates tied to the April 2026 paper?
- Does Kiro become a documented supported runtime, or is the code/docs mismatch a signal that the runtime surface is still moving quickly?

---

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — extends: CORAL belongs on the artifact-learning side of the survey because it promotes attempt history into notes and skills, but mostly through prompted synthesis rather than automatic maintenance
- [A functioning knowledge base needs a workshop layer, not just a library](../a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — extends: `.coral/public` is a concrete workshop substrate with attempts, notes, skills, and heartbeat state that feed later work
- [Skills are instructions plus routing and execution policy](../skills-are-instructions-plus-routing-and-execution-policy.md) — contrasts: CORAL treats skills as run-local optimization artifacts rather than as a long-lived capability layer for a curated KB
- [Methodology enforcement is constraining](../methodology-enforcement-is-constraining.md) — parallels: generated instruction files, heartbeat prompts, and deterministic eval hooks sit at different points on the same enforcement gradient
- [Bounded-context orchestration model](../bounded-context-orchestration-model.md) — grounds: CORAL externalizes orchestration into a symbolic manager and bounded agent sessions, though its unit of control is whole-agent runs rather than finer-grained subcalls
- [Apparent success is an unreliable health signal in framework-owned tool loops](../apparent-success-is-an-unreliable-health-signal-in-framework-owned-tool-loops.md) — warns: benchmark improvement can hide degraded execution paths or weak intermediate knowledge quality
- [Autocontext](./autocontext.md) — compares: both are outer loops over repeated coding runs, but Autocontext invests more in explicit multi-role analysis and distillation while CORAL stays as a lighter harness
- [OpenSage](./OpenSage.md) — contrasts: both manage agent runtimes and shared state, but OpenSage emphasizes runtime self-modification while CORAL emphasizes eval-gated search over a fixed task
