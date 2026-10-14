---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "EvoOntology workflow: host-led Parent/Candidate evolution through rejection, admission and terminal presentation at c94389b764394379086ff25e50d0e0f4396167b4."
run-id: AAS-2026-10-13-evoontology-f2d0c7992c6e-01
reviewed-boundary: c94389b764394379086ff25e50d0e0f4396167b4
---

# EvoOntology workflow report

## Workflow account

### Selected workflow and evidence

This account traces the Codex plugin's existing-ontology evolution workflow: a user requests improvement, the host freezes a Parent and evaluation context, diagnoses evidence, creates and tests a Candidate, repeats after rejection, and delivers an accepted or incomplete outcome. It was selected because the shipped skill connects model-dependent analysis to durable lifecycle decisions and explicit delivery. It is not a constructed sequence of unrelated APIs. The canonical route is [RT-RTE-evolution-admission](runtime.md#rt-rte-evolution-admission); its host model and state container are [RT-CMP-host-model](runtime.md#rt-cmp-host-model) and [RT-OBJ-evolution-session](runtime.md#rt-obj-evolution-session).

Evidence is SRC-1 at the frozen revision. This member directly inspected the complete Codex Evolve skill, root `evoontology/evolution/session.py`, and `evoontology/runtime/ops.py`, including lifecycle transitions and presentation wrappers. These supply doctrine/design and implementation, respectively. Runtime records supply the benchmark and later-consumption passages. There is no observed execution: host obedience, actual evaluator independence, successful opening and improved analysis remain unobserved. The account covers this selected Codex workflow, not every host or benchmark workflow.

### 1. Request, authorization and frozen handoff

The user requests evolution of an existing ontology; a reminder alone does not launch it. The host owns scope resolution, data access and experimental costs. Before starting, the skill requests an objective, acceptance criteria, unacceptable regressions and access to the native runner/evaluator. It offers quick two-round or default full eight-round budgets, with the same acceptance standards. Starting the run is authorization to conduct the bounded search, not evidence of human approval of every Candidate (SRC-1, `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md`; [RT-RTE-evolution-admission](runtime.md#rt-rte-evolution-admission)).

The handoff to `start_evolution_run` supplies workspace, Parent version, adapter, budget and acceptance mapping. `EvolutionSession.start_run` refuses another start when the latest run is running. The host must resume that run instead; resume reloads its saved state and budget and refuses terminal runs. `run.json` persists these fields. The skill additionally requires frozen input/validation IDs and evaluator references in the evaluation setup; Python does not require all of that methodological detail merely to create a run (SRC-1, `evoontology/evolution/session.py`, `evoontology/runtime/ops.py`).

> If a previous evolution run is still
> open, resume it via `resume_evolution_run` instead of starting a new one.
> --- `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md`

Fixed-split mode reuses existing training/validation partitions. Rolling mode freezes eligible post-checkpoint trajectories and separates design material from a validation reserve. Confirmed trajectory sources carry path, scope and purpose; the session stores references, not copies of the trajectories. The host must locate applicable logs and outcomes before diagnosing. If no eligible trajectories exist, the skill requests Parent baseline execution on collected questions: questions alone cannot supply observed failure evidence (SRC-1, `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md`, `evoontology/evolution/session.py`).

### 2. Diagnosis and Candidate construction

The host, not a deterministic internal planner, performs Diagnose → Attribute → Patch. It compares successes and failures, tests uncovered needs, constructs a problem map, considers competing causes, and chooses one primary causal mechanism. The skill permits Content, Tool and Schema interventions and related prompt/workflow/runtime changes. It requests a falsifiable hypothesis, localized reversible changes and low-cost checks that the intended mechanism actually changed before formal evaluation (SRC-1, `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md`; [RT-RTE-evolution-admission](runtime.md#rt-rte-evolution-admission)).

> Only proceed to formal comparison after confirming that the target mechanism
> has meaningfully changed.
> --- `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md`

The host supplies a hypothesis and Candidate version name to `begin_evolution_round`. Python checks running status, available round budget, nonempty hypothesis and a valid version path component; it then increments the round and saves the current hypothesis/Candidate. Those checks do not verify the causal explanation or the preliminary activation experiment. The Candidate is meant to remain separate from active Parent state during comparison. Session acceptance publishes semantic version files; installation or rollback of tool/schema/runtime code changes remains host-managed rather than an effect implemented by `accept` (SRC-1, `evoontology/evolution/session.py`; [RT-RTE-evolution-admission](runtime.md#rt-rte-evolution-admission)).

### 3. Evaluation handoff and veto

The host orchestrates controlled Parent/Candidate comparison with consistent inputs, split, models, evaluator, budget and configuration. Fixed-split mode uses the designated evaluator, potentially with ground truth; rolling mode uses an LLM Judge on the reserve. These are instructed roles, not source-established inaccessible sub-agent contexts. No internal host delegation mechanism is established by naming an Evaluator or Judge (SRC-1, `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md`; [RT-RTE-evolution-admission](runtime.md#rt-rte-evolution-admission)).

The included benchmark route delegates actual runs/scoring to subprocess drivers and returns normalized metrics, cases and artifact paths. Its adapters do not produce the formal `gate_input` needed for acceptance. The caller must pair observations, check regressions and record an evaluation summary for the current Candidate/round. Raw artifacts stay at their original locations; summary fields and paths persist under the run's `evaluations/` directory (SRC-1, `evoontology/evolution/session.py`; [RT-RTE-benchmark-evaluation](runtime.md#rt-rte-benchmark-evaluation)).

`accept_evolution` does not trust a verbal success report. The session validates the Candidate, finds current-round/current-Candidate gate input, requires an explicit `unacceptable_regressions:false`, checks protocol consistency where the frozen acceptance mapping names one, and recomputes the gate. Ground-truth input requires finite paired scores and unique case IDs; judge input requires valid nonempty verdicts. A nonpassing gate vetoes publication. These checks establish a mechanical acceptance boundary over supplied data, not authenticity, independence or repeated successful evaluation (SRC-1, `evoontology/evolution/session.py`; [RT-BAP-session-gate](runtime.md#rt-bap-session-gate)).

### 4. Rejection, continuation and interrupted recovery

A formal rejection is submitted through `record_evolution_round` with metrics, artifact references and notes. It appends the hypothesis/Candidate summary to `rounds.jsonl` but keeps the run running. The host must update attribution and design the next Candidate in that same frozen run; a rejection is not a delivered terminal result (SRC-1, `evoontology/evolution/session.py`, `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md`).

> **A single Reject never ends the run.**
> --- `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md`

Python refuses `finalize` while the run is running. It permits incomplete termination for named reasons: user interruption and missing permissions can stop immediately; missing data, unreliable evaluation and external block require the configured minimum rejection count, default two. A next-round request after the round budget is spent marks the run incomplete and raises budget exhaustion. These are lifecycle rules, not proof that the preceding experiments occurred: `record_round` stores caller summaries rather than independently validating failed trials (SRC-1, `evoontology/evolution/session.py`).

Recovery belongs to the host using persisted run state, source references, evaluation summaries and rejection history. An incomplete outcome does not switch the active version or advance the checkpoint within this route. The skill says the same batch should be retried later, while terminal runs cannot simply be resumed as running. The preserved Parent is the route's recovery anchor, not a guarantee against independent selector/file changes; [RT-RTE-version-override](runtime.md#rt-rte-version-override) establishes that alternate control path (SRC-1, `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md`, `evoontology/evolution/session.py`).

### 5. Publication and delivery

On acceptance, the session loads the validated Candidate, publishes it as an official version, advances the checkpoint, and saves accepted status/version/gate. The MCP wrapper also copies an available Candidate annotation report to the official version. Later semantic calls and new tasks can consume that version through [RT-RTE-semantic-retrieval](runtime.md#rt-rte-semantic-retrieval) and [RT-RTE-task-execution](runtime.md#rt-rte-task-execution). Publication and reload wiring do not establish changed model behavior or benefit. Nor is the publish/checkpoint/run-save sequence one crash-safe multi-file transaction (SRC-1, `evoontology/evolution/session.py`, `evoontology/runtime/ops.py`; [RT-RTE-evolution-admission](runtime.md#rt-rte-evolution-admission)).

Delivery has two distinct boundaries. The deterministic finalizer requires terminal accepted/incomplete state and returns that state plus a presentation result. It selects accepted version if present, otherwise Parent. The host's final report must use saved records and include comparable results, accepted/rejected hypotheses, unresolved issues and reproduction/recovery instructions; Python's state return is not that complete report (SRC-1, `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md`, `evoontology/runtime/ops.py`).

> The final report must
> be based on the session's terminal state and the saved run records, not on
> conversation memory.
> --- `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md`

Codex delivery requests `presentation:"codex", open_browser:false`; the operation generates a loopback preview URL and asks the host to open it in its browser panel. If that host tool is unavailable, the instruction says to return the URL/file path without claiming opening. Actual panel opening is external and unobserved. Rendering failure is returned separately, with retry guidance, without undoing accepted state (SRC-1, `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md`, `evoontology/runtime/ops.py`).

> return {"status": "presentation_failed", "message": str(exc),
>         "recovery": "Retry visualize_ontology; the active version is unchanged"}
> --- `evoontology/runtime/ops.py`

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-evolution-admission](runtime.md#rt-rte-evolution-admission)

Workflow-specific delivery boundary: a reject returns control to Candidate search, not to terminal reporting. Accepted/incomplete state permits finalization; the wrapper then presents accepted version or unchanged Parent. Presentation has a separate failure result and retry path. The host must still author the requested evidence-based final report and perform Codex panel opening. A successful terminal tool return therefore establishes neither complete host reporting nor visible browser delivery. The account above retains the additional delivery passages from SRC-1, `evoontology/runtime/ops.py` and `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md`.
