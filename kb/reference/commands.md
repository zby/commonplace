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

Check an ingest candidate against its drafting run with
`commonplace-validate <candidate> --handoff <record>`, where the record comes
from `commonplace-ingest-handoff prepare`. The candidate is validated as if it
were at its ingest path. This mode also requires the snapshot to hash to the
checksum pinned at dispatch, the Quotes block to equal the incumbent's byte for
byte, and `occasion` and code grounding to match what the run supplied.
Ordinary validation reports an ingest's contract findings (Quotes position,
local-only references, uncopied capture metadata) and dead links as warnings;
this mode fails on them. It prints `HANDOFF CLEAN` or `HANDOFF FAILED` with one
line per failure and appends the verdict to the handoff record. It writes
nothing else.

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
by incoming links. Write `kb/reports/state/promotion-candidates/<collection>/report.md`,
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

### commonplace-ingest-handoff

Open, publish and close the drafting handoff of one ingest. The drafting
worker writes a candidate under the ignored `kb/reports/state/ingest/<slug>/`;
the ingest in `kb/sources/` is not written until the candidate is accepted.
`prepare <ingest>` requires the name-paired snapshot, refuses an incumbent
whose `snapshot_sha256` differs from the snapshot, refuses a second run for a
source whose earlier run is still open, and writes the handoff record:
the pinned checksum, the incumbent's hash and the supplied occasion.
`publish <record>` repeats the handoff check and copies a clean candidate to
the ingest path only if the incumbent is unchanged since `prepare`.
`close <record>` ends the run without publishing and keeps the candidate.

The working directory stays after the run. Its record lists every handoff
check with its failure lines, and the outcome: `published`, `closed`, or none
for a run that stopped midway. Only the last run of an ingest is kept: `prepare`
replaces a finished run and refuses an open one. `prune [--days N]` deletes
the directories of runs published at least N days ago (default 30; `0`
deletes every published run). It keeps open and closed runs.

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
note (the parts the criterion watches), criterion and output contract match. The [review-system guide](./README-REVIEW-SYSTEM.md) covers operation
and [review architecture](./review-architecture.md) how it is built.

### commonplace-review

`status [NOTES... [--criteria C...]] [--outcome O...] [--fresh | --stale] [--json]`
shows each pair's freshness and stored outcome and launches nothing. With
NOTES it covers every applicable pair, including pairs never reviewed; without
NOTES it covers every stored result. `--fresh --outcome warn` lists the current
warnings, `--stale` what a sweep would ask; `--json` gives each row's result
file. Orphaned results, whose note or criterion is gone, are listed apart;
removing one is deleting its file.

`run gates NOTES... (--criteria C... | --all-gates | --criterion-file PATH) [--profile NAME]` asks one
worker per pair without a fresh result, in a new run under
`kb/reports/state/review/runs/v2/`, and writes a typed result file for each accepted
review. `--grouping bundle` asks one worker per note and bundle of catalog
gates for that bundle's stale gates instead of one per pair; each gate still
gets its own result file. `--resume RUN_DIR` continues a run; `retry RUN JOB` and
`acknowledge RUN LAUNCH` settle a worker problem or an unsettled launch.
Criteria are catalog gate ids, bundle names, the `type` and `collection`
lenses, compression check ids such as `compression/detail-overhang`, one id
per check, and the report instructions `critique`, `friction`, `premises`,
`compression-synthesis` and `role`; worker profiles come from the library's
`instructions/review-profiles.yaml`. `compression-synthesis` runs alone on one
note with its findings as `--input ROLE=PATH` files. `role`, the role report,
runs alone on one note with its inbound contexts as `--input inbound=PATH`;
without `--input`, the command collects them: the passages of Markdown files
under `kb/` that link to the note, outside `kb/reports/` and `kb/work/`.
Neither publishes a current result, and `status` refuses both. Draft selection and `--input ROLE=PATH`
retain run-local evidence without publishing a catalog result. Operational
inputs must be self-contained; their provenance links grant no cross-run access.

`show RUN [--observation ID] --json` inspects retained findings, exact capture
references and retry diagnostics. `fixture create --from RUN --observation ID
--substitute-current-executor` retains a content baseline with an explicit
executable substitution and recorded configuration gaps; `--repair ORIGINAL=PATH`
can supply missing historical dirty bytes matching their recorded hashes.
Creation launches nothing. `run gates --fixture PATH` runs one independent
trial through the same implementation, currently with Claude Code, pair
grouping and one worker. It never publishes live results. `--resume TRIAL_RUN`
continues that trial; it is not another observation. Fixture overrides are rejected.

`run edit OPERATION NOTE [--input ROLE=PATH ...] [--text PATH] [--profile NAME]`
runs one [edit operation](../types/edit-operation.md), such as
`instructions/simplification-passes/readability-and-flow.md`, on one note, in a
new run under `kb/reports/state/review/runs/v2/`. It writes nothing to the
checkout. The result is a typed [edit result](../types/edit-result.md) with
outcome `changed`, `unchanged`, `proposed` or `problem`, retained with its
candidate text in the run's observation under `artifact/edits/`; the JSON
report names both. `--text PATH` supplies a repository file as the start text
in place of the note's file. `--input ROLE=PATH` supplies a file the operation
reads under that role, such as `findings` or `diff`. A `per-item` operation
first returns `proposed`. Create the pending answers file with `answers
create`, record the operator's decision on each item, and run the operation
again with `--input answers=PATH`: it applies the `approved` items and
returns `changed`. The answers must pass the validator, and their question
must be a result of the same operation on the same text. The
profile defaults to the `effort` mapping for the operation's `effort`. It exits
0 for an accepted `changed`, `unchanged` or `proposed` result with a clean
guard, 1 otherwise, and 2 for a command error. `run edit --fixture PATH` reruns
a fixture created from an edit observation.

`run revise ARTIFACT` is the one runner of the improvement procedures:
focused (`--plan`, `--pass`, `--finding`, `--answers`), triage (`--triage`),
quick (`--assess`) and full (`--full`). Each makes the plan the runner executes
([ADR 135](./adr/135-improvement-procedures-are-three-plans-on-one-runner.md)).
Every invocation needs one of these choices; a bare `run revise ARTIFACT` is
a command error. The JSON report names the mode as `fixed-plan`, `answers`,
`triage`, `assess` or `full`.
`run revise ARTIFACT --plan FILE` executes fixed work without assessment.
The YAML plan supplies `purpose`, `must-keep`, ordered `passes` with optional
`scope`, and `stop`; see the [single-pass example](../instructions/simplification-passes/README.md#fixed-plan-execution-the-simple-baseline).
A plan with any other field is refused. `must-keep` lists only what the run
keeps beyond the note's write brief, whose Must keep every worker receives.
Do not also supply `--purpose` or `--must-keep`: the plan owns those fields.
A plan entry for a pass that declares `responds-to` also names the review
result it fixes as `finding`, and takes the depth of that result's criterion.
`run revise ARTIFACT --pass NAME [--purpose TEXT] [--must-keep CLAIM ...]` writes
and runs a one-entry plan for that pass. `run revise ARTIFACT --finding RESULT
[--purpose TEXT] [--must-keep CLAIM ...]` writes and runs a one-entry plan for
[fix a finding by a named strategy](../instructions/fix-warnings/fix-strategy-taxonomy.md)
with RESULT as its `finding`; RESULT must be a review result of ARTIFACT.
Both are fixed-plan runs, and their purpose and must-keep claims go into the
plan. `run revise ARTIFACT --triage [--purpose TEXT] [--must-keep CLAIM ...]`
asks the operator about the artifact's fresh stored review results with
outcome `warn` or `fail`. It launches no review and no assessor. It copies
each result that has a `warn` or `fail` finding into `artifact/findings/`,
writes one pending answers file per result,
`artifact/finding-answers-<key>.md`, whose items are the result's `warn` and
`fail` findings, records the results in `triage-inputs.json` and ends. The
JSON report's `triage` lists each file. With no such result, the run ends
with no change and `triage.what` says so. A finding identical to one the
operator decided in an earlier run on the note starts decided, with
`carried-from`.
`run revise ARTIFACT --assess [--purpose TEXT] [--must-keep CLAIM ...]` instead
commissions [assessment and pass selection](../instructions/simplification-passes/revise-an-article-or-note.md).
The assessor also receives the artifact's fresh stored review results with
outcome `warn` or `fail`; no review is launched.
`run revise ARTIFACT --full [--purpose TEXT] [--must-keep CLAIM ...]` first runs
every review operation that declares a `depth` on the artifact, with bundle
grouping, on the profile file's `default` profile. Fresh results are reused;
new results go to the shared store. The compression synthesis runs on the
compression checks' results, and the role report on the artifact's inbound
contexts; neither publishes a result. The review runs live under the revise
run directory, in `reviews/`, `synthesis/` and `role/`; the JSON report lists
them under `reviews`. A review without a result stops the run before
assessment. The assessor then receives the `warn` and `fail` results, the
depth 1 reports, the compression synthesis report and the role report, and
may stop the plan on a depth 1 proposal, naming the dependents a change would reach.
It retains `artifact/assessment.md` and `artifact/plan.yaml` and runs the
validated plan without routine approval.
Settled intermediate passes run in order, each on the
profile its `effort` selects through the `effort` mapping of
`instructions/review-profiles.yaml` (`--profile-simple`, `--profile-judgment`
override it). Each pass works on the text the one before left, through the
`run edit` route. `--plan FILE` supplies an explicit validated input or
override without assessment or approval; it also replaces a stopped plan.
An invalid plan is a command error. A plan with `stop` set ends the run and
leaves `artifact/stop-answers.md`; replace the plan through `--plan`.
Editing the retained plan alone is not an override.

Every invocation of `run revise` opens a new run under
`kb/reports/state/review/runs/v2/revise/<note path without .md>/<UTC stamp>/`,
with `-2`, `-3` on a collision; runs made before this layout keep 12-hex
hash names. The run records the note, the hash of its start text and the
hash of the captured write brief in `start.json`. No run is repeated or
resumed ([ADR 138](./adr/138-a-stop-ends-the-run-and-naming-its-output-is-the-approval.md)).
The run ends at its first stop. A `per-item` pass (plain-wording,
abstractions) that proposes anything ends the run with the pending answers
file `artifact/<pass>-answers.md`; later passes wait. A pass that ends with
a problem ends the run, after the passes before it are published.

The run publishes without a stop: before a `per-item` pass is asked for
proposals, what the earlier passes applied, and when the run ends, what the
passes applied since. It writes only a text that differs from the artifact,
only while the artifact holds the text the run last knew, its start text or
the text it last published, and only while the captured brief is unchanged;
otherwise the run ends with a conflict and writes nothing. The check and the
write hold the artifact's publication lock under
`kb/reports/state/review/publication-locks/`, shared by every revise and
rewrite run and `publish`. Each publication
keeps the text as `artifact/publications/<n>.md` and its diff from the text
before it as `artifact/publications/<n>.diff`, and records the hash, the plan
entries it covers, the time and who decided it in the run's
`published.json`. The JSON report lists them under `publications` and has
`published: true` when the run wrote the artifact. Nothing is committed:
`git diff` shows the change, and git reverses it. A candidate that adds a
validation warning the artifact's text does not have is not published: the
run holds it as `artifact/final.md` with `artifact/final.diff` and
`held.json`, asks no per-item pass for proposals, and ends; the report's
`held` names the files, the `new-warnings` and the `publish` commands.

A run that leaves work unfinished writes `continuation.json` and reports it
as `continuation`: `run-dir`; `made-for`, the artifact's `note`, `sha256` and
`text` when the run ended; and `items` in dependency order. Each item has
`id`, `kind`, `what`, `actor` (`operator`, `session-agent`, or `worker` with
its `effort`), `after` (the ids of the items to settle first), `how` (`step`,
the step of [continue a revise pass](../instructions/continue-a-revise-pass.md),
and where they apply `command`, `record` and `revised`), `answers` (the
answers files it waits for) and `evidence`. The kinds are `failure`,
`findings`, `plan-stop`, `held-candidate`, `proposals`, `claim-questions`,
`direct-entry`, `per-item-entry`, `fix-entry`, `interactive-entry` and
`stale-reviews`; the [review-system guide](./README-REVIEW-SYSTEM.md#revise-runs-and-the-continuation-record)
says when each is left. A plan entry not run is continued by `--plan` on a
one-entry plan the run wrote under `artifact/continue/`, which keeps the
entry's scope, or by `--answers FILE` when it applies the operator's
answers; a fix names the run's copy of its review result. The run keeps its report as `report.json`. It exits
0 when it ends with a clean guard, complete or with work to continue, 1 for
a failed pass or review, a conflict or a guard change, and 2 for a command
error, including an invalid plan or refused answers.

`run revise ARTIFACT --answers FILE [--answers FILE ...] [--purpose TEXT]
[--must-keep CLAIM ...]` names the operator's decided
[answers](../types/answers.md) files. Naming a file is the operator's
approval; an agent names it only on the operator's stated word for that
exact file. The run keeps a copy of each named file under `answers/` before
it launches anything. One file over a `per-item` pass's proposals makes a
run of that pass alone, in the scope the asking run's plan gave it, which
applies the `approved` items and publishes. It is refused unless the validator accepts the answers, the artifact holds
exactly the text the proposals were made for, the write brief is the one the
asking run recorded, and some item is approved. Files over review results,
such as a triage's or those `record` writes, make a plan with one fix entry
per result with an `approved` finding, in depth order, each receiving its
answers as `finding-answers`. They are refused unless each result's
criterion watches the same parts of the artifact it judged and some finding
is approved. One run takes either one file over proposals or files over
review results, not both.

`publish RUN [--revised FILE]` publishes the candidate the revise or rewrite
run RUN held, and launches nothing. Naming the run is the operator's
approval of its exact candidate. It is refused, writing nothing, when the
artifact no longer holds the text the candidate was held over, when
`final.md`, `final.diff` or a rewrite's accepted review changed after the
run, when the write brief changed since the run, or when the operator
already published the candidate. `--revised FILE` publishes the operator's
full revised text instead, from a file outside the run's `artifact/`, after
those checks and the candidate checks (frontmatter, H1, `user-verified` and
no new validation failure). The run keeps it as `artifact/revised.md`, with
`artifact/revised-from-final.diff` (from `final.md`) and
`artifact/revised.diff` (from the artifact); the JSON report's
`revised-candidate` names the files. For a rewrite run whose published text
is the judged candidate, the accepted review becomes the note's current
result, named in `current-result`; otherwise `not-current` says why not.

`record RUN` writes a pending answers file over each review result of the
revise run RUN that has a `warn` or `fail` finding, and launches nothing. The
results are those the run's assessor or triage received. Each file is the one
a triage writes: `artifact/finding-answers-<key>.md`, whose question is the
run's copy of the result in `artifact/findings/`. The command prints each
file with the command that records it. It works whether or not the note still
holds the run's text. It makes no plan, runs no fix and publishes nothing.
A file that already exists, from a triage or an earlier `record`, is left as
it is. Use it to record the operator's decisions on findings answered
outside the run, such as by a split; keep the decided file with
`answers record FILE`. A run that holds no review results is a command error.

`answers create --from QUESTION [--to PATH]` writes the pending answers file
for a question and launches nothing. A question is an edit result with
outcome `proposed`, whose items are its proposals; a review result with
outcome `warn` or `fail`, whose items are its `warn` and `fail` findings,
each with its position in `findings` as id; or any other file, a text to
approve, with one item naming its hash. The default PATH is
`<question stem>-answers.md` beside the question; an existing file is never
replaced. A path under `kb/reports/state/review/results/` is refused, since
the store would read the file as a review result; give `--to` for a stored
result. The command writes every hash, so nobody writes one by hand.
`commonplace-validate PATH` checks a completed file against its question.

`answers record FILE` keeps an answers file under a revise or rewrite run's
`artifact/` as the operator's decisions, in that run's `answers/`, and
launches nothing. Use it for a file whose decisions nothing consumes: one
that approves no item, a plan stop's `stop-answers.md`, or the files
`record` writes. The validator must accept the file against its question;
otherwise nothing is kept. Recording a file again after a change, such as an
added `resolution`, replaces the record. Naming the file is the operator's
approval of its text.

`run rewrite NOTE --commission FILE [--profile NAME]` rewrites
one note from its authorized sources, for a note whose contribution is known
but whose claims or synthesis are unsettled. FILE is the commission: Markdown
with YAML frontmatter naming `note` and `sources` (each a repository `path`
and its `role`), and the section `## Current direction`. When the note has
no write brief, the commission also needs `## Intended contribution`,
`## Must keep`, `## Must exclude` and `## Reserved decisions`. When it has
one, those sections are optional and hold only what this rewrite adds to the
brief. Every invocation opens a new run under
`kb/reports/state/review/runs/v2/rewrite/<note path without .md>/<UTC stamp>/`,
named as a revise run is, and needs the commission. The run captures the
commission, with the note's write brief, the sources
and the note's type and collection contracts. A source that git ignores, or
lies under a `.snapshots/` directory, or is not text, is referenced by path
and SHA-256 and never copied into the run. Fresh workers then reconstruct
the sources and account for the claims without the note, write a candidate
with a reconciliation report, and review the exact candidate, ending
`accept` or `block`. Before the candidate, the run obtains the note's role
report: a fresh one kept by `run revise --full` on the same text, without a
launch, or else one call of the role report alone on the profile file's
`default` profile, in `role/` under the run. The candidate, repair and
review calls receive its `## Role` section as `kb-role`, and the operator's
earlier decisions on the note, from revise and rewrite runs, as
`earlier-decisions` when there are any. The JSON report's `role` names the
role report and whether it was reused. A `block` allows one repair and a second fresh review;
a second `block` ends the run unpublished, with `blocked` in the JSON report.
After `accept`, a candidate other than the note's text is held, as `run
revise` holds one with a new warning, and the run ends; `publish RUN`
publishes it. A referenced source whose bytes changed stops the run before
the candidate is held. `--profile` names the worker profile for every call;
the default is the `effort` mapping for `judgment`. It exits 0 when the run
ends with a held candidate, no change or a block and a clean guard, 1 for a
stop, a conflict or a guard change, and 2 for a command error. See
[the rewrite workflow](./README-REVIEW-SYSTEM.md#rewriting-a-note).

`decisions [--note PATH] [--class NAME] [--json]` lists operator and agent
decisions and launches nothing. It is read-only: it reads the revise and
rewrite run directories and writes no state. An answers file is a decision
once a command kept it in a run's `answers/`: a run it was named to with
`--answers`, or `answers record`. A file kept by two runs is listed once.
So that decisions recorded before ADR 135 stay visible, it also reads the
records of the retired procedures: operator records in full-pass run
directories, full-pass packets under `kb/reports/state/review/packets/` and
fix reports under `kb/reports/state/fixes/`. Operator records of revise and
rewrite runs are not read. Each
entry says who proposed and who decided (`operator`, `agent`, `automatic`,
`version-guard`, `pending` for an answers file a continuation record waits
for or a held candidate not yet published, or `overtaken` for such an entry
whose note is gone or no longer holds the text the run left it), the action
class (the pass name of a per-item stop, `finding` for a triage or `record`
file, whose item names the criterion, `stop` for a plan stop,
`publication`, `packet` or `fix-report`), and whether the decision covered
one `item` or a `bundle`. A kept answers file gives one entry per item, with
its state (`approved`, `rejected`, `deferred`, `pending` or `overtaken`) and
the operator's reason. A publication is one bundle entry for the published
text, not one per edit, decided by `automatic` or, through `publish`, by the
operator; one that published the operator's revised text has
`revised: true` in JSON and `revised candidate` in the text. A packet gives
its disposition as an agent entry and, once resolved, its resolution. A fix
report is listed once, by path, since its format is free. Entries are
grouped by note and ordered by decision time; untimed entries come last.
`--note` and `--class` filter; `--json` gives the entries as JSON. The
command computes no statistics. A malformed record exits 2 with its path.
This is the operator-decision record
([ADR 130](./adr/130-the-operator-decision-record-is-a-query-over-the-state-tree.md)).
