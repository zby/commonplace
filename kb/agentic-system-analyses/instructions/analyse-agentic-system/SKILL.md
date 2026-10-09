---
name: analyse-agentic-system
description: "Use when asked to analyse, review, or refresh an external agent runtime, orchestration system, agent operating layer, agent memory/knowledge/context-engineering system, or narrower model-dependent operational mechanism from inspectable sources."
type: types/instruction.md
user-invocable: true
argument-hint: "<system identifier> plus source input (repository, checkout, snapshot/bundle, or documents), optional Git commit"
allowed-tools: Read, Write, Grep, Glob, Bash, Task
model: opus
---

# Analyse an Agentic System

Analyse one external agentic system at one frozen evidence boundary and publish its accepted artifact with the overview as the public entry point. Code runs the analysis as a workflow: it names each job, judges each result, and publishes. You open the run, launch the workers it names, and report.

Invocation authorizes the artifact-run directory under `kb/agentic-system-analyses/state/`, the retained analysis under `kb/agentic-system-analyses/retained/<system-slug>/`; code writes all of them. Code acquires and freezes a GitHub source's checkout under `related-systems/`; the boundary job may freeze other sources under its source rules; later jobs read them read-only. Invocation does not authorize editing source content, auxiliary indexes or surveys, transfer scans, landscape synthesis, other retained reports, or Git staging and commits.

Run the orchestrator's commands from the root of the prepared worktree throughout the run. The run's files, `related-systems/` and the retained analysis are found from there.

## Isolated run setup

Run each analysis in a dedicated Commonplace worktree at a committed method
revision. Prepare it first, from the checkout this session started in:

```bash
commonplace-analysis prepare --name <system-label>
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
are checked, except an ignored `settings.local.json`, which holds one user's
harness permissions. Runtime locks, caches and top-level harness README files are not
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
worker-recovery rules. A completed published run stays in this worktree until the
operator separately authorizes integration. Keep using the prepared worktree's
command directory and working directory for
`commonplace-analysis integrate <run>` after the report; its recorded
origin checkout must be clean and on `main`. An agent also supplies
`--model <model-id>`. The command commits
the publication on `analysis/<run-id>` from the method commit and merges that
branch into `main`. If Git reports a conflict, the command aborts the merge,
keeps the branch and worktree, and stops for the operator. Do not copy the
retained analysis into `main`.

Worktree removal is a separate operator decision. It is permitted only when
every run in it has completed with verified publication merged into `main`, no
integration branch awaits a merge or conflict decision, and every audit has extracted its
evidence record or the operator has said none needs it. Then use `git worktree
remove`, remove the sibling preparation record, and delete merged analysis
branches. Never remove a worktree containing a `failed` run through this
routine: failures, rejected outputs and traces are evidence. Completed local
blocked/out-of-scope results also need a separate disposition decision, not this
published-run cleanup route. Disposing of
such evidence needs a separate explicit operator decision after reviewing
the failure and any uncertain public state. Removal is never automatic.

A command after `--` instead starts a separate harness in the prepared
worktree with its commands on `PATH`; the operator may use it to run this
skill there. This session then stops after preparation.

## 1. Open the run

From the prepared worktree root, using its command directory, allocate the run:

```bash
commonplace-analysis start \
  --system "<source-native system name>" \
  --source-identity "<stable source identity, e.g. https://github.com/owner/repo>" \
  --source "<the caller's source input, as given>" \
  --harness <this harness> [--profile <operator-named profile>]
```

Code normalizes the source identity and allocates
`AAS-<date>-<source-slug>-<worktree-token>-<nn>` under
`kb/agentic-system-analyses/state/`. The token comes from the ready preparation
record, including with `--worktree`. The source slug determines the stable
publication directory; there is no public-path override. The command pins the
plan and prints the run path. It does not advance, acquire sources
or launch workers. The first advance opens the analysis and pins the prepared
method commit; publication requires it unchanged.

For a GitHub source, add `--source-revision <full 40-hex commit>` when the caller
requests a revision or asks to keep the existing checkout's commit. For the
latter, read `git -C <checkout> rev-parse HEAD` and pass that full commit. The
option requires a GitHub identity. During advance, code freezes
`related-systems/<owner>--<repo>/` before the boundary job. Without a revision it
clones a missing checkout or fetches a clean existing one and detaches it at the
default branch tip. With a revision it uses that commit. A dirty checkout,
foreign origin or unavailable commit stops the run for the operator.

Every worker of a run uses one worker profile from
[worker-profiles.yaml](./worker-profiles.yaml): a harness, `launch-model` and effort.
Pass `commonplace-analysis start` this session's harness with `--harness <name>`
(`claude-code`, `codex` or `pi`), and the profile the operator names with
`--profile <name>`. Without a named profile, code uses the harness's default;
it refuses a profile of another harness. Opening records the profile and
publication writes it to the retained manifest. If the harness cannot select
the profile's launch model and effort for a fresh worker, stop before starting
the run and tell the operator.

Do not read `kb/agentic-systems/reviews/` or `kb/agentic-system-analyses/retained/` at any point; the jobs analyse from sources only.

## 2. Drive the run

Follow [drive a code-scheduled run](./drive-a-code-scheduled-run.md) with `<run>` = the path `commonplace-analysis start` printed. The run is new: you started it in this session.

## 3. Report

Run `commonplace-analysis inspect <run>` and include its JSON output
unchanged in the final response, together with any stops from the last advance.
The report does not reconstruct invocation-specific scheduling stops or audit
retained files. `publishable` is engine coverage, not proof of publication.
`state: completed` means the bound publication job completed on current inputs.
For `blocked` or `out-of-scope` dispositions, `completion: local` means no retained
publication. `completion: publication-job-completed` is still not a fresh
filesystem audit; separately authorized integration independently verifies exact
evidence before committing.

If the loop stops or reports an uncertain effect, preserve its evidence and give
the operator the exact command output and error. Do not edit engine state or
claim completion. After a published analysis, add that outputs under
`kb/agentic-systems/comparisons/` are stale unless rebuilt under separate
authority, and a prior landscape synthesis is historical unless refreshed under
separate authority. Transfer scans and landscape synthesis need separate
commissions; this run does not launch them.

Old or mixed run directories are explicitly rejected. Preserve their retained
data and failed-run evidence. If the operator independently chooses to handle
old evidence, that requires its archived method checkout and command environment;
there is no compatibility adapter or legacy execution route in this tree.

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
