---
name: analyse-agentic-system
description: "Use when asked to analyse, review, or refresh an external agent runtime, orchestration system, agent operating layer, agent memory/knowledge/context-engineering system, or narrower model-dependent operational mechanism from inspectable sources."
type: types/instruction.md
user-invocable: true
argument-hint: "<system identifier> plus source input (repository, checkout, snapshot/bundle, or documents), optional Git commit and public review path"
allowed-tools: Read, Write, Grep, Glob, Bash, Task
model: opus
---

# Analyse an Agentic System

Analyse one external agentic system at one frozen evidence boundary and publish its retained set and compact generated review. Code runs the analysis as a workflow: it names each job, judges each result, and publishes. You open the run, launch the workers it names, and report.

Invocation authorizes the run directory under `kb/reports/state/agentic-system-analysis/`, one generated review under `kb/agentic-systems/reviews/`, and the retained set under `kb/reports/retained/agentic-system-analysis/<run-id>/`; code writes all of them. It does not authorize changes to source worktrees, auxiliary indexes or surveys, transfer scans, landscape synthesis, other retained reports, or Git staging and commits.

Run the orchestrator from the repository root and keep that working directory throughout the run. Workers must inherit it: `commonplace-validate` discovers the root there, and the boundary job uses `related-systems/`.

## 1. Open the run

1. Commit any pending method change first: the run pins the method commit when it opens, and publication requires it unchanged.
2. From the repository root, start the run:

   ```bash
   commonplace-workflow start commonplace.lib.agentic_workflow:AnalyseAgenticSystem \
     --param system="<source-native system name>" \
     --param source-identity="<stable source identity, e.g. https://github.com/owner/repo>" \
     --param source="<the caller's source input, as given>"
   ```

   Code normalizes the source identity (no surrounding whitespace, trailing `/` or trailing `.git`; a lowercase URL scheme and host), and the run uses that form throughout. The run ID takes its name from the source identity's last path segment (the repository name for a GitHub URL), or from the system name when the identity is not a URL. Add `--param review-path=kb/agentic-systems/reviews/<name>.md` only when the caller supplied a review path; it must be directly under `reviews/`. The command allocates the run ID and prints the run directory, `kb/reports/state/agentic-system-analysis/<run-id>`.

   To reuse a Git checkout without refreshing it, add
   `--param source-revision=<full 40-hex commit>` when the caller requests
   that revision or asks to keep the existing checkout's commit. For the
   latter, read `git -C <checkout> rev-parse HEAD` and pass that full commit.
   The checkout must already exist, be clean and match the requested commit.
   The boundary worker must not clone, fetch, pull or check out another
   revision; a missing, dirty or mismatched checkout requires `problem`.
   Code refuses a boundary that reports another source kind or revision.
   Omit this option to let the boundary job acquire and freeze a source
   under its normal rules.

Do not read `kb/agentic-systems/reviews/` or `kb/reports/retained/agentic-system-analysis/` at any point; the jobs analyse from sources only.

## 2. Drive the run

Follow [drive a code-scheduled run](./drive-a-code-scheduled-run.md) with `<run>` = the directory `start` printed. The run is new: you started it in this session.

## 3. Report

When `step` gives `done`, run `commonplace-agentic-analysis-handoff <run>/run-state.md` and include its output unchanged in your final response. After a published review, add that outputs under `kb/agentic-systems/comparisons/` are stale unless rebuilt under separate authority, and a prior landscape synthesis is historical unless refreshed under separate authority.

When the run stopped, the loop's stop report is your final response; do not run the handoff. A correctable pre-publication failure keeps the run `running`: the operator repairs the condition and a later session resumes the loop. Set `run-status: failed` with one concise reason only when abandoning the run or when publication left public state uncertain. Never resume a failed run; use a new run ID.

A transfer scan is separate: run [`scan-agentic-system-transfer`](../../../instructions/scan-agentic-system-transfer/SKILL.md) only when separately commissioned and only after the complete run state validates.

---

- [Agent-runtime analysis should separate scheduling, context assembly, and external state](../../../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md) — rests-on: the causal runtime responsibilities of the runtime job
- [Agent orchestration occupies a multi-dimensional design space](../../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) — rests-on: why the runtime inventory remains open
- [Agent memory is a crosscutting concern, not a separable niche](../../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) — rests-on: why every run has a memory analyst
- [Knowledge storage does not imply contextual activation](../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) — rests-on: the retention, read-back, presence, and activation distinctions
- [Behavioral authority](../../../notes/definitions/behavioral-authority.md) — rests-on: the consumer, channel, force, and horizon record
- [Tentative theory](../../../notes/definitions/tentative-theory.md) — rests-on: the status of the theory, independent of structure or retention
- [Theory builder](../../../notes/definitions/theory-builder.md) — rests-on: localized, consumed, criticized, and retained theories, and the reflective and autonomous qualifiers
- [Addressable theory](../../../notes/definitions/addressable-theory.md) — rests-on: separately inspectable and editable parts as an additional property
- [A complete theory path does not establish improved capacity](../../../notes/a-complete-theory-path-does-not-establish-improved-capacity.md) — rests-on: the separate evidence claims and stronger requirements for later or recurrent use
- [Reflective system](../../../notes/definitions/reflective-system.md) — rests-on: the causally connected self-representation required for reflection
- [Self-improving system](../../../notes/definitions/self-improving-system.md) — rests-on: the operative, evidence-responsive change the revision-admission records describe
