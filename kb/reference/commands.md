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
validation. The default view gives stable next-action IDs and drill-down
commands without embedding underlying rows. Review warnings, jobs, and
freshness state are deliberately absent from the normal path while the review
system remains irregular operational state; request them with `--review`.
`--json` emits `commonplace.status.v1`. The command does not mutate, rank with a
model, schedule work, or become an authority for any displayed state.

### commonplace-validate

Accepts a member file, artifact directory, ordinary subtree, or collection.
A directory containing `ARTIFACT.yaml` receives artifact checks and ordinary member
checks, grouped as one artifact. Explicit file validation stays file-scoped.
See [directory artifacts](./validation-contract.md#directory-artifacts).

Check a draft in the role it is intended for with
`commonplace-validate <draft> --artifact <directory> --role <role>`.
The role is one the artifact's type declares; its path comes from the layout. The draft
replaces the incumbent in memory for every check in the invocation. Findings
are restricted to that role, with rule, location and repair text;
absent-member findings are deliberately omitted for a working artifact. When the
directory is an engine run's `artifact/`, fields the layout binds to `run` are
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

Rank unstructured note files by incoming links and write
`kb/reports/cache/promotion-candidates.md`, separating invalid frontmatter from text
candidates.

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

## Artifact runs

### commonplace-analysis

The analysis lifecycle: prepare a worktree, run the analysis in it, inspect,
reset and integrate the run. The workflow is `commonplace.lib.agentic_analysis.workflow`
over the headless primitives in `commonplace.headless`; see
[the analysis skill](../agentic-system-analyses/instructions/analyse-agentic-system/SKILL.md).

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
--worker-profile <profile>` allocates a token-bearing run ID under
`kb/agentic-system-analyses/state/`, prints its path and runs the whole
workflow there: opening, source acquisition, each role's worker launched as a
fresh headless session of the profile's harness, the analysis's checks,
verification and corrections under the plan's attempt budgets, assembly and
publication. Optional `--source-revision <full-40-hex-commit>` requires a
GitHub identity; `--max-workers` (default 3) bounds concurrent workers and
`--timeout` (default 10800 s) each launch. `run <run>` resumes an allocated,
stopped or interrupted run: every worker answer is cached by its content, so
only jobs whose inputs changed are asked again. The run holds a lock; a second
`run` on the same directory is refused. Exit status 0 prints the publication
receipt (`published: false` for a local `blocked` or `out-of-scope` result),
2 means the run stopped and printed why (a usage limit, an environment
failure, a worker's problem, an exhausted budget, blockers at a verifier's
last attempt), 1 means the command failed. A job is retried by deleting its
cache entry under `answers/` and rerunning.

`inspect <run>` prints the run's state (`published`, `local`, `stopped` with
its reason, `running`, `interrupted`), parameters, opening metadata, boundary
disposition, verdicts, worker problems, each job's launches, answers (with
their cache files) and failures, the accepted members' digests and the
receipt, as JSON, from `log.jsonl`, the answer cache, `artifact/` and
`receipt.json`. It changes nothing and is not a retained-filesystem audit.

`reset <run>` withdraws the run's unreleased worktree publication: it
requires the publication journal and the exact published bytes, keeps them
under the run's `withdrawn/` as evidence, restores the opening incumbent and
deletes the receipt, so a rerun after changed members can publish again.
Already integrated results are refused.

`integrate <run>` independently verifies the run's opening metadata and
receipt against the retained bytes and the archive, then, after separate
operator authorization, commits the published artifact and incumbent archive
on an analysis branch and merges into `main`. The origin checkout must be clean
and on `main`. A conflict leaves the branch and worktree for review while
`main` stays unchanged. An agent supplies `--model <model-id>` for its commit
trailer.

Old engine run directories (`run.json`) are not read by these commands; their
worktrees keep their own pinned commands.

### commonplace-run

Run the generic engine on a plan. The analysis workflow no longer runs on it
(`commonplace-analysis run` above); the engine stays until its retirement.
`start <run> <plan.yaml>` writes
the run's metadata, fixing the declaration for the run; a compact plan is
expanded first, deriving each role's check or verdict application from the
type's layout, and the expansion is what the run fixes. `--param key=value`
records run parameters. `advance <run>` closes the attempts reported with
`--completed <attempt>` and `--failed <attempt>=<reason>` (`--model` and
`--effort` record the actual worker identity on those results), runs every ready
code job, hands out every ready model job, and prints the exact prompt paths,
open attempts, stops and whether the artifact is publishable; `--json` prints the
same as data. It exits 0 when the run continues, 2 when the run stopped and
1 when the command itself failed. The coordinator launches fresh workers without parent conversation
and settles all round hand-outs before advancing. The analysis manifest still
requires one consistent worker model/effort identity.
`status <run>` lists members, open hand-outs with their original prompt paths,
current failed attempts, historical `worker_problems` with full retained report
text, and refusals with identifiers; use it before resuming. `--json` includes
these independently: a completed attempt can retain a worker problem without
being a current failure. See the inspection limitations above.
Publishability means engine coverage, not publication or content validation.

`reset <run> --from <job>` archives debugging evidence outside active discovery,
withdraws that job's active attempts and dependent completions, and rebuilds the
working artifact from retained upstream acceptance records. It does not launch
workers or supply audit feedback. After the external reset, the agent follows
the existing step program without special instructions. Verification can send
retained author work through the normal correction loop. Correction attempt
budgets restart, including for retained authors. Independent work stays active.
`--json` reports the reset jobs and debugging archive path.

Reset requires no open attempts or unresolved uncertain effects. Settle workers
before invoking it; do not delete open records to simulate idleness. Refusals
and optional candidate-check context are not forward reset edges. The debugging
archive holds the pre-reset run, withdrawn external effects and prepared next
state. A pending-reset marker blocks normal engine operations after interruption;
repeat the same reset command to finish applying that prepared state.

Handlers with external effects must supply the reset hook described in
`src/commonplace/artifactrun/reset.py`. The analysis publication hook withdraws
an exact unreleased worktree publication and restores its opening incumbent, if
any, so unchanged opening metadata can support ordinary replacement publication.
It rejects altered publication bytes and already integrated results. Reset does
not alter the frozen plan, opening method commit, source snapshot or run identity;
use the run's matching command environment.

`validate-output <prompt-path>` gives a worker read-only validation feedback for
its open attempt's primary output. It resolves the output, artifact directory
and role from recorded run metadata and invokes the same role-draft validator
as `commonplace-validate <draft> --artifact <directory> --role <role>`.
Diagnostics and validation exit statuses are preserved; path/attempt lookup
errors exit 1. It neither completes the attempt nor replaces workflow checks.
Auxiliary outputs remain subject to their existing workflow checks.

**Layout coupling:** this command identifies the run and attempt from the
canonical `RUN/state/handouts/ATTEMPT/prompt.md` location, then verifies the
recorded model job and reconstructed handout path. It does not parse prompt
prose or infer a role from the attempt name. Copied prompts outside that layout,
unknown or closed attempts, and jobs without a validation role are rejected.
Moving the handout layout requires updating the resolver in
`src/commonplace/artifactrun/handouts.py`, its tests and generated invocations
together. Use the run's own command environment, as with `advance`.

`judge <run> --role <role> --outcome accepted|refused` records an operator
judgment of a role's member: `--findings` carries the reason, `--scope`
names covered relations with their partners among `--basis` roles,
`--override` names a refusal the acceptance cancels, and `--version` judges an
earlier version as evidence only. An operator's judgment leaves the same
record as a code job's; a refusal of a member whose acceptances all hold does
not by itself block publication.

## Review system

Review execution composes selection, job creation, an external worker, and
finalization. Use [the review-system guide](./README-REVIEW-SYSTEM.md) for the
operator workflow, [run review batches](../instructions/run-review-batches.md)
for the executable procedure, and [review architecture](./review-architecture.md)
for internal invariants.

Partition-valued flags are named `--model-partition`. The only `--model` flag
is finalization's concrete worker-model provenance; it must map into the job's
partition.

### commonplace-create-review-jobs

Consume selector JSON and create queued, result-kind-homogeneous review jobs
grouped by note or criterion.

### commonplace-review-job-list

List queued, completed, or failed review jobs and optionally emit JSON.

### commonplace-finalize-review-job

Finalize one job-owned output all-or-nothing, record worker provenance, write
pair results, advance their freshness baselines, and return the committed
per-pair outcomes and result paths. Unsuccessful finalization returns an empty
`pairs` array.

### commonplace-freshness-status

Report freshness for registered targets. [Freshness architecture](./freshness-architecture.md)
explains status, acknowledgement, and retirement; the live implementation owns
their exact JSON fields.

### commonplace-freshness-ack

Acknowledge changed inputs for an existing registered target from a
status-derived manifest.

### commonplace-freshness-retire

Remove a registered freshness baseline from a retire manifest, including a
baseline whose input artifact was deleted.

### commonplace-store-healthcheck

Verify operational-store structure, snapshot hashes, foreign keys, and
freshness-baseline invariants.

### commonplace-ack-review

Advance exact changed-input observations from inspected review-selector JSON
without rerunning the assay. It preserves the evidence review pair and rejects
an inspection-to-ack hash or baseline-revision race; for a report, it does not
endorse or resolve the findings.

### commonplace-ack-trivial-note-changes

Auto-acknowledge `note-changed` verdict pairs when none of the criterion's
watched note parts changed. Invoking it is explicit human authorization for
the qualifying trivial-change workflow. Type and collection conformance pairs
have no `watches:` declaration and never qualify.

### commonplace-resolve-criteria

Resolve gate, bundle, concrete type- or collection-conformance, or critique
requests into their criterion definitions.

### commonplace-review-target-selector

Select applicable assay pairs either by current staleness or by an explicit
requested-mode scope, for inspection or piping into job creation.

### commonplace-warn-selector

Extract actionable findings from effective `warn` review pairs whose live inputs
match their freshness baseline. Stale WARN pairs are reported separately. This
command is the entry point to the [fix system](../instructions/FIX-SYSTEM.md).
