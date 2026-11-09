---
description: Reference for the commonplace-* CLI commands shipped by llm-commonplace - project setup, validation, indexing, snapshots, note operations, and the review system
type: types/note.md
tags: []
---

# Commonplace CLI commands

All commands are installed together with
`uv tool install --python ">=3.11" llm-commonplace` and resolve as
`commonplace-*` from uv's user-level tool executable directory. Source
contributors add `--editable .`; development-only executables such as `pytest`,
`ruff`, and `properdocs` run through `uv run`.

This page is the complete published command-name catalogue and a routing guide.
Package entry-point metadata is authoritative, and a test keeps it in exact
parity with the headings below. Run any command with `--help` for its live
arguments. For exact implementation behavior, use `commonplace-source` and
read the executing package. The prose here retains only purpose, composition,
and operational distinctions that help a reader choose the right command.

## Project setup

### commonplace-init

Create or extend a Commonplace project without overwriting its own files, and
rewrite its machine-specific pointers into the installed library: skill stubs,
`.commonplace/library.md`, and the Claude Code read rule. `--check` reports
whether those pointers are current without writing anything. See
[architecture](./architecture.md) for the installed topology and package/user
boundary.

### commonplace-source

Print the filesystem path of the `commonplace` package that supplies the
running commands.

## Validation and indexing

### commonplace-status

Show one compact, read-only situation report assembled from project and command
versions, Git state, notes validation, and workshop-and-task lifecycle
validation. `--collection NAME_OR_PATH` is required and scopes notes validation;
Git, lifecycle, and optional review summaries retain their separate project
scopes. The JSON `notes_validation.scope` and each check's `scope` identify
what was inspected. The default view gives stable next-action IDs and
drill-down commands without embedding underlying rows. Counts over the stored
review results (fresh, stale, orphaned, and current `warn` and `fail`) are
absent from the normal path; request them with `--review`.
`--json` emits `commonplace.status.v2`. The command does not mutate, rank with a
model, schedule work, or become an authority for any displayed state.

### commonplace-validate

Accepts a member file, artifact directory, ordinary subtree, or collection.
Collection names resolve generically; there is no special Notes or Theory
target. `today` and `recent` require `--collection NAME_OR_PATH` and filter
that collection's validation targets by local-date modification time. They
retain collection structure checks and ignore-marker exclusions.
A directory containing `ARTIFACT.yaml` receives artifact checks and ordinary member
checks, grouped as one artifact. Explicit file validation stays file-scoped.
See [directory artifacts](./validation-contract.md#directory-artifacts).

Check a draft in the role it is intended for with
`commonplace-validate <draft> --artifact <directory> --role <role>`.
The role is one the artifact's type declares; its path comes from the layout. The draft
replaces the incumbent in memory for every check in the invocation. Findings
are restricted to that role, with rule, location and repair text;
absent-member findings are deliberately omitted for a working artifact. When the
directory is an analysis run's `artifact/`, fields the layout binds to `run` are
checked against the run's parameters and `run-id`. This mode
writes nothing and refuses `--output`. A content pass is not job acceptance:
the workflow adds separately labelled invocation residue. It establishes
neither claim support nor analytical correctness. Member mode's default and
`--full` output use the shared finding text; `--json` emits
`commonplace.validation.member.v1` with each finding's repair and rendered text.
Unverified evidence is reported as information but refuses this content check,
as it does acceptance.

Run deterministic validation on one artifact, collection, type surface,
collection-landing set, redirect map, or the bounded workshop-and-task
lifecycle surface. The default result contains counts and every warning or
failure without printing passing artifact blocks. Use `--full` for the complete
per-artifact transcript and `--json` for the stable compact
`commonplace.validation.v1` result, including the path and detected type of
each analysed artifact. With `--json`, `--output PATH` atomically saves the
exact bytes also emitted to stdout; the destination's parent directory must
already exist. The
[validation contract](./validation-contract.md) owns the exact check domains.

### commonplace-verify-quotes

Audit `verbatim`-marked quotations over one or more Markdown files or
directories, including unresolved pairings that do not fail ordinary
validation.

### Generated indexes (no command)

Complete `dir-index.md` listings and generated tag tails have no rebuild
command. The ProperDocs hook materializes them during the site build; agents
use the scoped `rg` routes in [navigation](./navigation.md). The retired
`commonplace-refresh-indexes`, `commonplace-sync-generated-index`, and
`commonplace-generate-notes-index` commands do not exist.

## Note operations

### commonplace-guard-full-pass-report

Compare each of a full-pass packet's guarded logical artifacts with its latest
packet capture — `final.txt` for a keep pass that reached its closing phase,
otherwise `source.txt`; `merge-target.txt` for a merge target — before any
disposition, edit, or follow-up is executed. Emits per-input JSON with status
`matching`, `changed` (with a diff), `missing`, or `corrupt-capture`; exits 0
only when every input matches. The
[full-improvement instruction](../instructions/run-full-improvement-pass-on-note.md)
and [resolve a full-pass disposition](../instructions/resolve-full-pass-disposition.md)
own the refusal and reconciliation workflow.

### commonplace-relocate-note

Rename or move one note and rewrite its KB backlinks. A note that declares a
write brief moves with it: the `<stem>.brief.md` sidecar is renamed to the new
stem and the `brief:` pointer rewritten. A brief cannot be relocated on its own.
The command dry-runs unless `--apply` is supplied.

### commonplace-relocate-directory

Move a KB directory, rewrite links, and optionally add one ProperDocs redirect.
The command dry-runs unless `--apply` is supplied.

### commonplace-promotion-candidates

Rank unstructured note files in the required `NAME_OR_PATH` collection argument
by incoming links. Write `kb/reports/cache/promotion-candidates/<collection>/report.md`,
where `<collection>` is the collection's path relative to `kb/`, including any
namespace directories. Reports for distinct collections do not overwrite one
another. Invalid frontmatter is separate from text candidates; validation-ignored
subtrees are not candidates. Links resolve relative to the actual report path.

## Snapshots

### commonplace-github-snapshot

Capture a GitHub issue or pull request under the ignored
`kb/sources/.snapshots/` reading cache. An existing capture of the same source
is reported rather than replaced; `--reobserve` captures it again as a new
observation under a basename ending in the capture date.

### commonplace-x-snapshot

Capture an X/Twitter post, thread, or article under the ignored
`kb/sources/.snapshots/` reading cache. An existing capture of the same source
is reported rather than replaced; `--reobserve` captures it again as a new
observation under a basename ending in the capture date.

## Tasks

### commonplace-task

Run one runbook from `kb/tasks/` unattended in the current checkout and
check its commit:

```bash
commonplace-task run <name> [--profile NAME] [--timeout SECONDS]
```

The worker profile comes from `kb/tasks/profiles.yaml` (its `default` when
`--profile` is omitted): harness, launch model, effort and the permission
flags the headless session runs with. The command opens a Workjig run under
`kb/reports/state/tasks/<name>/<stamp>/`, asks one worker to follow the
runbook, then reads git: it reports whether exactly one new commit exists,
whether it carries the subject the runbook's `## Write scope` names, whether
it touches only that scope, and what the run left uncommitted. The JSON
report ends with `ok`; the exit status is 1 when any check fails and 2 when
the runbook or profile cannot be loaded. The worker's own report is shown
but decides nothing. Design and its limits: `kb/work/recurring-task-runner/`.

## Agentic-system analyses

### commonplace-analysis

Run one explicit source or a bounded queue without a supervising agent:

```bash
commonplace-analysis analyse https://github.com/owner/repository
commonplace-analysis batch targets.txt --concurrency 4
commonplace-analysis resume /absolute/controller
commonplace-analysis resume /absolute/controller --target https://github.com/owner/repository
commonplace-analysis report /absolute/controller
```

`analyse` owns validation, isolated preparation, execution through the prepared
command environment, waiting, guarded integration and reporting. `batch` uses
the same lifecycle and one queue. New invocations authorize integration of
complete publications into the recorded origin's `main`; low-level `run` remains
publication-only. After analysis children drain, integration runs serially
through each worktree's pinned command. A merge refusal preserves publication
and evidence rather than launching another analysis. Its input is newline repository locators or a JSON list of objects
with `source` and optional `source-kind`, `system`, `source-identity` and
`source-revision`; unknown fields and duplicate normalized identities are refused
before effects. Repository roots are shape-checked without network probes.
GitHub SSH/HTTPS aliases and case normalize to one identity. A repository's
explicit `source-identity` must match its normalized locator; aliases that cannot
be resolved locally must be supplied as one consistent canonical locator.
`--source-kind local` requires an existing path and makes it absolute;
`--source-kind documents` requires explicit system and identity. Non-Git capture
remains boundary-owned. Explicit GitHub identities retain code-owned acquisition.

New runs default to `pi-sol`. `--worker-profile`, `--source-revision`,
`--revision`, `--max-workers`, `--timeout` and `--require-clean-origin` preserve
the corresponding lower-level choices. `--state` selects a new durable controller
directory; the default is under ignored `.commonplace/worktrees/controllers/`.
`--worktree-root` selects an external worktree parent. Existing destinations are
not reused. Four analyses with three role workers each permit twelve role
workers; advisory audits occupy their analysis's slot after its roles finish.
Provider capacity, storage/inodes and placement need operator preflight before
a substantial batch. No capacity probes or automatic cleanup occur. `--model`
records explicit initiating-agent attribution for integration commits; absent
that argument, no model trailer is inferred from the analyst profile.

JSON stdout records the controller schema and policy; stderr summarizes
outcomes. Each target retains source identity, preparation/worktree, allocated
run, method/profile bindings, logs and the pinned child's inspection, including
receipt, disposition and `advisory-audit` evidence. Publication and integration
are separate recorded outcomes. A local non-complete result has no publication
to integrate. For new automatic controllers, aggregate exit 0 requires each
target to be integrated or completed locally without publication.
Legacy controllers retain publication-only success. Exit 2 means ordinary stops;
1 means command/preparation failures; 3 means pending work, unintegrated
publication or operator attention and takes precedence. A stopped target is not
success. `report` reads saved state without reconciliation or liveness claims.

`resume` first reconciles preparation/allocation evidence and inherited child
leases, then continues pending targets. Completed targets are not rerun;
ordinary stops require explicit `--target <recorded-normalized-identity>` after
operator repair. A resumable interrupted allocation keeps its original run,
method and profile. Integration reconciliation recognizes proven committed or
merged effects without rerunning workers or duplicating commits. Existing
publication-only controllers do not gain automatic integration authority.
Unknown effects, unsettled workers, unreadable records and interrupted audits
pause new effects. No missing PID establishes settlement.
There is no automatic retry, acknowledgement, reset or replacement allocation.
Ordinary stops do not prevent independent pending targets from continuing;
shared preparation/command failures and uncertain ownership pause new claims.
Opening and pinned-method guard failures are command failures for the queue,
not ordinary target-local stops. The lower-level `run` still exits 2 for them.

Controller/child leases require POSIX local-filesystem locks. A second controller
is refused. SIGINT/SIGTERM stop claims and drain owned children, including
Git/installer subprocesses isolated from the terminal process group while the
controller owns their drain. Low-level commands retain group cancellation.
Abrupt death
leaves intents to reconcile, and an orphan prepared child keeps its lease until
it exits. Workjig remains the worker-launch authority. `execute <allocation-key>`
and `inspect-execution <allocation-key>` are the pinned-child protocol: allocation
is journaled before directory creation and replayed by key, never inferred from
console output. The coordinator does not import another worktree's workflow.
New automatic controllers require a committed method carrying both execution
and integration protocols; incompatible methods are refused before allocation.
Older runs keep their own worktree's original commands, not a new binding.
See [ADR 125](./adr/125-analysis-commands-own-preparation-and-bounded-queues.md)
and [ADR 126](./adr/126-integrate-analysis-publications-by-default.md).

Low-level preparation, execution, inspection and recovery remain available.
The workflow is `commonplace.lib.agentic_analysis.workflow` over
`commonplace.headless`; [the analysis skill](../agentic-system-analyses/instructions/analyse-agentic-system/SKILL.md)
is a target-selection and invocation adapter.

`prepare --name <system>` creates a dedicated Commonplace source
worktree and installs and verifies its local command environment. It pins a
commit and a 12-hex worktree token in the preparation record for distinct
analysis run IDs. By default it permits unrelated uncommitted origin changes,
excludes their bytes from the worktree, and records their exclusion.
`--require-clean-origin` instead rejects a dirty origin; startup instructions and
configuration that differ from the selected commit always stop preparation. An
optional command after `--` runs in the prepared worktree with its commands on
`PATH`, such as a fresh harness or `commonplace-analysis run`. Without
`--revision` it refuses a `HEAD` behind the default branch. Analysis run
commands require the prepared checkout and its local executing code. See
[isolated run setup](../agentic-system-analyses/instructions/analyse-agentic-system/SKILL.md#isolated-run-setup).

`run --system <name> --source-identity <identity> --source <input>
[--worker-profile <profile>]` allocates a token-bearing run ID under
`kb/agentic-system-analyses/state/`, prints its path and runs the whole
workflow there: opening, source acquisition, each role's worker launched as a
fresh headless session of the profile's harness, the analysis's checks,
verification and corrections under the plan's attempt budgets, assembly and
publication. New runs default to `pi-sol` (`gpt-6.1-sol`, medium effort);
`--worker-profile` overrides it. Resumed runs keep their recorded profile.
Optional `--source-revision <full-40-hex-commit>` requires a
GitHub identity; `--max-workers` (default 3) bounds concurrent workers and
`--timeout` (default 10800 s) each launch. `run <run>` resumes an allocated,
stopped or interrupted run: every worker answer is recorded under its full
request, so only jobs whose request changed are asked again; a changed
`--timeout` applies to launches not yet made. The run holds a lock; a second
`run` on the same directory is refused. Exit status 0 prints the publication
receipt (`published: false` for a local `blocked` or `out-of-scope` result),
2 means the run stopped and printed why (a usage limit, an environment
failure, a worker's problem, an exhausted budget, blockers at a verifier's
last attempt, a launch an earlier run left unsettled), 1 means the command
failed.

Before returning, `run` saves an all-attempt trace scan of Pi and Claude Code
worker streams under
`<run>/audit/<input-digest>/`. Completed Pi and Claude Code analyses then
receive an advisory, read-only meta-analysis using the saved scan and accepted
outputs. It runs in the run profile's harness with that profile's model and
effort; a Codex run records a skipped audit. It has a
900-second ceiling (or the shorter `--timeout`), with prompt limits of three
questions and 30 tool calls. Missing and unsupported traces are coverage gaps,
not successful scans. An unchanged rerun reuses the snapshot; changed inputs
create a new one. Audit failure does not change the analysis exit status or
receipt. The [analysis skill](../agentic-system-analyses/instructions/analyse-agentic-system/SKILL.md#advisory-trace-audit)
sets the evidence and reporting obligations. Audit files are local state, not
included by `integrate`; evidence extraction precedes worktree removal.

`inspect <run>` prints the run's state (`published`, `local`, `stopped` with
its reason, `running`, `interrupted`), parameters, opening metadata, boundary
disposition, verdicts, worker problems, each job's launches, answers (with
their keys) and failures, the accepted members' digests and the receipt, as
JSON, from `log.jsonl`, the run's call records under `calls/`, `artifact/`
and `receipt.json`. The separate `advisory-audit` field reports the latest audit
status and evidence directory from `audit/status.json`, or null when none was
saved. It changes nothing and is not a retained-filesystem audit.

`retry <run> <job>` dismisses the job's standing worker problems, and
`retry <run> <job> --key <key>` one recorded answer, so the next `run` asks
that job again without spending an attempt. `acknowledge <run> <launch>`
records the operator's confirmation that a worker launch an earlier run left
unsettled has stopped; it inspects and kills nothing, so confirm first that
the process and its children are gone. Both take the run's lock.

`reset <run>` withdraws the run's unreleased worktree publication: it
requires the publication journal and the exact published bytes, keeps them
under the run's `withdrawn/` as evidence, restores the opening incumbent and
deletes the receipt, so a rerun after changed members can publish again.
Already integrated results are refused.

`integrate <run>` verifies opening and receipt bindings, exact retained bytes
and the incumbent archive before committing and merging the publication. New
high-level invocations supply this authority; manual integration of existing
publications requires authorization. The origin must be clean and on `main`;
competing publications and unrelated staging are refused. Cooperating
integrations serialize through an origin-wide lock. Integration records durable
intent/result evidence and verifies exact bytes through Git; it does not rerun
acceptance under current contracts or use advisory verdicts as a gate.
Reentry recognizes proven effects; ambiguous partial effects require repair.
`inspect-integration <run>` reads the pinned integration intent and actual Git
evidence without starting a transfer. It reports integration separately from
`inspect <run>`'s analytical publication state.
A conflict preserves the publication branch and worktree for review, without
automatically choosing a side. An agent supplies `--model <model-id>` for its
commit trailer. Cleanup and cross-analysis refresh remain separate commissions.

Run directories made by the retired artifact-run engine (`run.json`) are not
read by these commands. Inspect or integrate such a run from inside its own
worktree, whose `.venv` installs its pinned source; see
[ADR 118](./adr/118-analyses-run-as-a-workflow-over-headless-harnesses.md).

## Review system

`commonplace-review` reviews notes against criteria with headless workers and
keeps one result file per (note, criterion) pair under
`kb/reports/state/review/results/`. A result is fresh while the hashes of the
note (the parts the criterion watches) and of the criterion match the current
files. The review-system guide and architecture pages still describe the
store-based system it replaced.

### commonplace-review

`status [NOTES... [--criteria C...]] [--outcome O...] [--fresh | --stale] [--json]`
shows each pair's freshness and stored outcome and launches nothing. With
NOTES it covers every applicable pair, including pairs never reviewed; without
NOTES it covers every stored result. `--fresh --outcome warn` lists the current
warnings, `--stale` what a sweep would ask; `--json` gives each row's result
file. Orphaned results, whose note or criterion is gone, are listed apart;
removing one is deleting its file.

`run gates NOTES... (--criteria C... | --all-gates) [--profile NAME]` asks one
worker per pair without a fresh result, in a new run under
`kb/reports/state/review/runs/`, and writes a result file for each accepted
review. `--resume RUN_DIR` continues a run; `retry RUN JOB` and
`acknowledge RUN LAUNCH` settle a worker problem or an unsettled launch.
Criteria are catalog gate ids, bundle names, and the `type`, `collection` and
`critique` lenses; worker profiles come from the library's
`instructions/review-profiles.yaml`.
