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

Analyse one external agentic system at one frozen evidence boundary and publish its accepted set with the overview as the public entry point. Code runs the analysis as a workflow: it names each job, judges each result, and publishes. You open the run, launch the workers it names, and report.

Invocation authorizes the run directory under `kb/agentic-system-analyses/state/`, the retained set under `kb/agentic-system-analyses/retained/<system-slug>/`; code writes all of them. Code acquires and freezes a GitHub source's checkout under `related-systems/`; the boundary job may freeze other sources under its source rules; later jobs read them read-only. Invocation does not authorize editing source content, auxiliary indexes or surveys, transfer scans, landscape synthesis, other retained reports, or Git staging and commits.

Run the orchestrator's commands from the root of the prepared worktree throughout the run. The run's files, `related-systems/` and the retained set are found from there.

## Isolated run setup

Run each analysis in a dedicated Commonplace worktree at a committed method
revision. Prepare it first, from the checkout this session started in:

```bash
commonplace-workflow prepare-analysis --name <system-label>
```

Code creates a detached worktree under `.commonplace/worktrees/`, installs
its local commands from the committed lockfile, verifies their binding, and
prints a JSON record. Keep its `worktree` and `path-prefix` values.
`--worktree <new-path>` overrides the location. Existing destinations are refused.
Failed installations retain the worktree and a sibling `.preparation.json`
record for diagnosis. Preparation writes Git metadata and may download
packages: when the sandbox blocks it, request escalation for this command
alone. If preparation fails, stop and give the operator its
message; do not open a run in the originating checkout.

Preparation uses `HEAD`. It stops when `HEAD` is behind the default branch:
this session then loaded an older method. Stop and tell the operator; only the
operator selects another method with `--revision <commit>`.

By default, uncommitted changes stop preparation. `--allow-dirty-origin` permits
unrelated changes in the originating checkout and excludes them from the new
worktree; use it only when the operator asks. It never permits changed startup
instructions or configuration: instruction files such as `AGENTS.md`, project
harness settings and system prompts, skill and agent directories, extensions,
hooks and prompt resources, and repository-local targets of skill symlinks must
match the selected commit. Staged, unstaged, untracked and ignored startup files
are checked. Runtime locks, caches and top-level harness README files are not
startup inputs. The Git comparison covers repository files, not user-wide
harness settings.

A successful preparation establishes that the instructions this session loaded
are the worktree's. Continue in this session:

- Run every later command of this skill with `worktree` as its working
  directory, calling it as `<path-prefix>/commonplace-…`.
- Every path this skill names is relative to `worktree`.
- Launch workers as the driver says. Code gives each worker the command
  directory in its invocation.

Code refuses a run's command when it is called from another checkout or runs
another checkout's code, and the refusal names the directory to use. Follow
it; do not reinstall the shared user-level tool to point at the run.

Keep the worktree's code, method files, lockfile and environment unchanged
until the run finishes; develop and merge method changes elsewhere. On resume,
use the same worktree and command directory before following the
worker-recovery rules. Do not remove the worktree: its run state is the
evidence of the run. After completion, transfer the retained set back when the
operator authorizes merging the results.

A command after `--` instead starts a separate harness in the prepared
worktree with its commands on `PATH`; the operator may use it to run this
skill there. This session then stops after preparation.

## 1. Open the run

1. The run pins the worktree's method commit when it opens, and publication requires it unchanged.
2. From the worktree root, start the run:

   ```bash
   commonplace-workflow start commonplace.lib.agentic_workflow:AnalyseAgenticSystem \
     --param system="<source-native system name>" \
     --param source-identity="<stable source identity, e.g. https://github.com/owner/repo>" \
     --param source="<the caller's source input, as given>"
   ```

   Code normalizes the source identity (no surrounding whitespace, trailing `/` or trailing `.git`; a lowercase URL scheme and host), and the run uses that form throughout. The run ID takes its name from the source identity's last path segment (the repository name for a GitHub URL), or from the system name when the identity is not a URL. Publication uses that source slug as its stable directory; `review-path` is no longer a parameter. The command allocates the run ID and prints the run directory, `kb/agentic-system-analyses/state/<run-id>`.

   For a GitHub source, code freezes `related-systems/<owner>--<repo>/`
   before the boundary job. Without a revision it clones a missing checkout,
   or fetches an existing clean one, and detaches it at the tip of the
   default branch. Add `--param source-revision=<full 40-hex commit>` when
   the caller requests that revision or asks to keep the existing checkout's
   commit; for the latter, read `git -C <checkout> rev-parse HEAD` and pass
   that full commit. A missing checkout is then cloned at that commit, and a
   clean existing one is moved to it. A dirty checkout, a foreign origin, or
   an unavailable commit stops the run for the operator. The option requires
   a GitHub identity.

Do not read `kb/agentic-systems/reviews/` or `kb/agentic-system-analyses/retained/` at any point; the jobs analyse from sources only.

## 2. Drive the run

Follow [drive a code-scheduled run](./drive-a-code-scheduled-run.md) with `<run>` = the directory `start` printed. The run is new: you started it in this session.

## 3. Report

When `step` gives `done`, run `commonplace-agentic-analysis-handoff <run>/run-state.md` and include its output unchanged in your final response. After a published analysis, add that outputs under `kb/agentic-systems/comparisons/` are stale unless rebuilt under separate authority, and a prior landscape synthesis is historical unless refreshed under separate authority.

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

## Coordinator publication and method edits

Before publication, the coordinator reads [publication](../publish-analysis.md).
Only coordinators load that instruction; worker packets do not supply it.
Before editing this method, read [method maintenance](../maintain-analysis-method.md).
