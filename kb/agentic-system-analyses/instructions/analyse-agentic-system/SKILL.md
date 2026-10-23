---
name: analyse-agentic-system
description: "Use when asked to analyse, review, or refresh an external agent runtime, orchestration system, agent operating layer, agent memory/knowledge/context-engineering system, or narrower model-dependent operational mechanism from inspectable sources."
type: types/instruction.md
user-invocable: true
allowed-tools: Read, Bash
argument-hint: "<system identifier> plus source input (repository, checkout, snapshot/bundle, or documents), optional Git commit, and the worker profile"
---

# Analyse an Agentic System

Analyse one external agentic system at one frozen evidence boundary and publish its accepted artifact with the overview as the public entry point. Code runs the analysis as a workflow in one process: it opens the run, acquires the source, launches each role's worker through its harness's headless mode, checks and verifies every result, corrects what was refused, and publishes. You confirm the target, prepare the worktree, start the run, and report.

Invocation authorizes the run directory under `kb/agentic-system-analyses/state/` and the retained analysis under `kb/agentic-system-analyses/retained/<publication-name>/`; code writes both. Code acquires and freezes a GitHub source's checkout under `related-systems/`; the boundary worker may freeze other sources under its source rules; later workers read them read-only. Invocation does not authorize editing source content, auxiliary indexes or surveys, transfer scans, landscape synthesis, other retained reports, or Git staging and commits.

## Confirm the target

Before preparing a worktree or starting a run, identify the system and its source
from the caller's input. If the target is missing or ambiguous, ask: “Which system
should I evaluate? Please provide its repository URL or local checkout.” Stop
and wait for the answer. Do not select a system from prior analyses or infer an
unstated target from the current checkout. A supplied repository can identify
the system without requiring the caller to repeat its name.

For a remote repository, apply this quick shape check to the trimmed locator:

```regex
^(?:https?://[^/\s?#]+/|ssh://[^/\s?#]+/|git@[^:\s]+:)[^/\s?#]+/[^/\s?#]+/?$
```

This accepts common HTTPS, SSH URL and SCP-style repository locators, including
`.git` suffixes. Use the repository root, not an issue, file or documentation URL.
If the locator does not match, ask for a repository locator or clarification;
less common repository forms may be confirmed by the caller. A local checkout
or explicitly supplied snapshot, bundle or documents uses its existing source
route rather than this remote-URL check. Do not silently treat a malformed
repository locator as a document source.

This is a plausibility check, not proof that cloning will succeed. Do not run
`git ls-remote`, clone, fetch or test credentials during intake. Acquisition
handles unavailable repositories, permissions and clone failures later.

The run uses a worker profile from
[worker-profiles.yaml](./worker-profiles.yaml): a harness, the model it
launches and the effort. Every worker of the run uses it, verification
included, and it is fixed for the run; another profile means another run.
The advisory meta-analyser also uses that model and effort, but only on Pi,
with ambient instructions, skills and extensions disabled.
Use **`pi-sol`** (`gpt-6.1-sol`, medium effort) when the caller does not name a
profile. The command defaults to it for new runs. The caller can override it,
for example:

```text
/analyse-agentic-system https://github.com/suzgunmirac/dynamic-cheatsheet
Use worker profile pi-ultramarine.
```

An explicit profile overrides the default. A resumed run always keeps its
recorded profile; changing the default does not change existing runs.

## Isolated run setup

Run each analysis in a dedicated Commonplace worktree at a committed method
revision. Prepare it first, from the checkout this session started in:

```bash
commonplace-analysis prepare --name <system-label>
```

Use a nonempty label containing only lowercase letters, digits and hyphens,
starting with a letter or digit (`[a-z0-9][a-z0-9-]*`). This preparation label
is not the source-native display name: for example, use `--name ace` here and `--system "ACE"`
when starting the run.

Code creates a detached worktree under `.commonplace/worktrees/`, installs
its local commands from the committed lockfile, verifies their binding, and
prints a JSON record. Keep its `worktree` and `path-prefix` values.
`--worktree <new-path>` overrides the location. Existing destinations are refused.
Failed installations retain the worktree and a sibling `.preparation.json`
record for diagnosis. Preparation writes Git metadata and may download
packages: when the sandbox blocks it, request escalation for this command
alone. For a label-only rejection, you may correct only `--name` and retry
without operator escalation, but only before any worktree or run has been
created and with the target, source and scope unchanged. For every other
preparation failure, stop and give the operator its message; do not retry
automatically. Do not start a run in the originating checkout.

Preparation uses `HEAD`. It stops when `HEAD` is behind the default branch.
Stop and tell the operator; only the operator selects another method with
`--revision <commit>`.

By default, preparation permits unrelated uncommitted changes in the originating
checkout, excludes them from the new worktree, and records their exclusion in
its JSON record. `--require-clean-origin` instead stops preparation when the
origin is dirty. Startup instructions and configuration must match the
selected commit in either mode: instruction files such as `AGENTS.md`, project
harness settings and system prompts, skill and agent directories, extensions,
hooks and prompt resources, and repository-local targets of skill symlinks.
Staged, unstaged, untracked and ignored startup files are checked, except an
ignored `settings.local.json`, which holds one user's harness permissions.

Continue in this session:

- Run every later command of this skill with `worktree` as its working
  directory, calling it as `<path-prefix>/commonplace-analysis`.
- Every path this skill names is relative to `worktree`.

Code refuses a run's command when it is called from another checkout or runs
another checkout's code, and the refusal names the directory to use. Follow
it; do not reinstall the shared user-level tool to point at the run.

Keep the worktree's code, method files, lockfile and environment unchanged
until the run finishes; develop and merge method changes elsewhere. A
completed published run stays in this worktree until the operator separately
authorizes integration.

A command after `--` instead runs in the prepared worktree with its commands
on `PATH`; this session then stops after preparation. The operator may use it
to start a harness there, or to run the analysis in one step:

```bash
commonplace-analysis prepare --name <system-label> -- \
  commonplace-analysis run --system "<name>" --source-identity "<identity>" \
    --source "<input>" --worker-profile <profile>
```

Worktree removal is a separate operator decision. It is permitted only when
every run in it has completed with verified publication merged into `main`, no
integration branch awaits a merge or conflict decision, and every audit has
extracted its evidence record or the operator has said none needs it. Then use
`git worktree remove`, remove the sibling preparation record, and delete merged
analysis branches. Never remove a worktree containing a stopped run through
this routine: failures, rejected outputs and traces are evidence. Completed
local blocked/out-of-scope results also need a separate disposition decision.
Removal is never automatic.

## 1. Run the analysis

Start it:

```bash
commonplace-analysis run \
  --system "<source-native system name>" \
  --source-identity "<stable source identity, e.g. https://github.com/owner/repo>" \
  --source "<the caller's source input, as given>" \
  --worker-profile <profile> [--source-revision <full 40-hex commit>]
```

Code normalizes the source identity, allocates
`AAS-<date>-<source-slug>-<worktree-token>-<nn>` under
`kb/agentic-system-analyses/state/`, prints that path, and runs the workflow
there. The token comes from the ready preparation record. The run's source
slug is independent of its publication name: GitHub sources publish under
lowercase `<owner>--<project>`, preserving repository punctuation; other
sources keep their existing naming. There is no public-path override.

For a GitHub source, add `--source-revision` when the caller requests a
revision or asks to keep the existing checkout's commit; for the latter, read
`git -C <checkout> rev-parse HEAD` and pass that full commit. The option
requires a GitHub identity. Code freezes `related-systems/<owner>--<repo>/`
before the boundary worker: without a revision it clones a missing checkout or
fetches a clean existing one and detaches it at the default branch tip; with a
revision it uses that commit. A dirty checkout, foreign origin or unavailable
commit stops the run for the operator. If the sandbox is known to block the
network, request approval for the `run` command before running it; do not
clone or fetch yourself.

The run opens the analysis and pins the prepared method commit, then runs the
roles in the workflow's order: boundary; runtime; memory, epistemic and
workflow in parallel; reconciliation; report verification with its
correction rounds; memory profile and synthesis, each verified; assembly and
publication. Each worker is a fresh headless session of the profile's harness
in the worktree, with up to `--max-workers` (default 3) running at once and
`--timeout` seconds (default 10800) per launch. The run holds a lock: a
second `run` on the same run directory is refused.

A run takes hours. Start it so that it outlives your tool call (a background
command whose exit you wait for, or a terminal the operator keeps open), wait
for it to exit, and read its exit status and output. Exit status 0 means the
run completed: it printed the publication receipt, with `published: true` for
a complete disposition or `published: false` for a `blocked` or
`out-of-scope` boundary, which completes locally. Exit status 2 means the run
stopped and printed why; 1 means the command itself failed.

### Advisory trace audit

Before `run` exits, code saves a scan of every manifest-recorded attempt,
including failed and superseded ones. The scanner detects explicit Pi tool
failures; missing, incomplete and unsupported traces remain visible as coverage
limits. It does not discover nested workers outside the manifest.

After a completed Pi analysis, code passes the scan, attempt inventory and
accepted artifact paths to a fresh [meta-analyser](./meta-analyser.md). It uses
failures as leads for at most three verification questions and 30 tool calls,
with a timeout of 900 seconds or `--timeout`, whichever is shorter. The question
and call limits are prompt instructions, not a tool sandbox. Only read and bash
tools are exposed; read-only authority is prompt-enforced. Code saves the
returned text. No findings is not a correctness certificate.

`<run>/audit/status.json` identifies the latest snapshot. Each
`audit/<input-digest>/` keeps `scanner.json`, `attempts.json`, the input digests,
exact prompt, launch record, stdout, stderr, status and any completed report.
An unchanged rerun reuses its snapshot, including a failed audit; changed inputs
create a new one. Audit failure, timeout or incomplete coverage does not change
the analysis receipt or exit status. A stopped analysis is scanned but does not
launch the meta-analyser. Other harnesses do not launch it.

The audit is advisory: report material findings and unresolved concerns to the
operator. Do not repair accepted artifacts or rerun workers on its authority.
Audit evidence is local run state, not included by `integrate`. Before authorized
worktree removal, extract useful audit evidence to a retained destination or
obtain the operator's explicit decision that none needs retention. After an
abrupt controller death, inspect the audit's recorded PID and confirm its process
and children have stopped; an interrupted snapshot is not automatically retried.

## 2. Stops and reruns

Every worker answer is recorded under its full request, so

```bash
commonplace-analysis run <run>
```

resumes a stopped or interrupted run from where it was, without asking any
worker again whose request is unchanged; a changed `--timeout` applies to
launches not yet made. A run stops on:

- a usage limit of the harness: rerun after the limit resets;
- an environment failure (a launch still exiting nonzero after its
  relaunches, a missing command): give the operator the message; rerun after
  the repair;
- a worker's problem report (it could not do its job): `inspect` shows the
  report; the operator decides. To ask that job again, run
  `commonplace-analysis retry <run> <job>` and rerun;
- a worker launch an earlier run left unsettled (the run was killed while a
  worker ran): give the operator the launch ID; after they confirm that the
  worker and its children have stopped, they run
  `commonplace-analysis acknowledge <run> <launch>`, then rerun;
- an exhausted attempt budget, or blockers at a verifier's last attempt: the
  run has failed under the method's budgets; stop and report. A new run, or a
  method change, is the operator's call.

`retry` is the one change you make under a run: never edit the artifact,
an answer, the log or the records, and never claim
completion for a stopped run. A run that published in the worktree and must
publish again after a changed member is first withdrawn with
`commonplace-analysis reset <run>`, which requires the publication journal,
restores the opening incumbent, keeps the withdrawn bytes under the run's
`withdrawn/` as evidence and deletes the receipt; then dismiss each answer
to redo with `commonplace-analysis retry <run> <job> --key <key>` (`inspect`
lists each answer's key) and rerun. A reset interrupted midway is finished by running
it again. Already integrated results cannot be reset. If a run or reset
reports an uncertain publication effect, change nothing, preserve the
evidence and give the operator the exact output.

## 3. Report

Run `commonplace-analysis inspect <run>` and include its JSON output
unchanged in the final response, together with the run's last output.
`state` is `published` (the receipt says so), `local` (a non-complete boundary
completed without publication), `stopped` (with the reason), `withdrawn`
(reset; a rerun publishes again), `running`, `interrupted` (the latest run
neither ended nor holds the lock) or `allocated` (never run). The view
lists each job's launches, answers and failures, the accepted members and the
receipt, plus the separate `advisory-audit` status and evidence directory;
it is not a fresh audit of retained files. Read any completed audit report and
include its outcome and limits, or state why it was skipped or failed. After a published
analysis, add that outputs under `kb/agentic-systems/comparisons/` are stale
unless rebuilt under separate authority, and a prior landscape synthesis is
historical unless refreshed under separate authority. Transfer scans and
landscape synthesis need separate commissions; this run does not launch them.

## 4. Integrate

After the report and separate operator authorization, run
`commonplace-analysis integrate <run>` with the prepared worktree's command
directory and working directory; its recorded origin checkout must be clean
and on `main`. An agent also supplies `--model <model-id>`. The command
checks the run's records against the retained bytes, commits the publication
on `analysis/<run-id>` from the method commit, and merges that branch into
`main`. If Git reports a conflict, the command aborts the merge, keeps the
branch and worktree, and stops for the operator. Do not copy the retained
analysis into `main`. Before integrating, read [publication](../publish-analysis.md).

Do not read `kb/agentic-systems/reviews/` or `kb/agentic-system-analyses/retained/` at any point; the workers analyse from sources only. Before editing this method, read [method maintenance](../maintain-analysis-method.md).

---

- [Agent-runtime analysis should separate scheduling, context assembly, and external state](../../../theory/agent-runtime-analysis-should-separate-scheduling-context-state.md) — rests-on: the causal runtime responsibilities of the runtime job
- [Agent orchestration occupies a multi-dimensional design space](../../../theory/agent-orchestration-occupies-a-multi-dimensional-design-space.md) — rests-on: why the runtime inventory remains open
- [Agent memory is a crosscutting concern, not a separable niche](../../../theory/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) — rests-on: why every run has a memory analyst
- [Knowledge storage does not imply contextual activation](../../../theory/knowledge-storage-does-not-imply-contextual-activation.md) — rests-on: the retention, read-back, presence, and activation distinctions
- [Behavioral authority](../../../theory/definitions/behavioral-authority.md) — rests-on: the consumer, channel, force, and horizon record
- [Tentative theory](../../../theory/definitions/tentative-theory.md) — rests-on: the status of the theory, independent of structure or retention
- [Theory builder](../../../theory/definitions/theory-builder.md) — rests-on: localized, consumed, criticized, and retained theories, and the reflective and autonomous qualifiers
- [Addressable theory](../../../theory/definitions/addressable-theory.md) — rests-on: separately inspectable and editable parts as an additional property
- [A complete theory path does not establish improved capacity](../../../theory/a-complete-theory-path-does-not-establish-improved-capacity.md) — rests-on: the separate evidence claims and stronger requirements for later or recurrent use
- [Reflective system](../../../theory/definitions/reflective-system.md) — rests-on: the causally connected self-representation required for reflection
- [Self-improving system](../../../theory/definitions/self-improving-system.md) — rests-on: the operative, evidence-responsive change the revision-admission records describe
