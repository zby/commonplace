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

### commonplace-agentic-analysis-finalize

Finalize the mechanical parts of one `running` agentic-system analysis set.
`memory <run-state>` writes `output/memory.md` from the specialist's local
`memory-report.md` and the overview's Reconciliation table: exact-token
proposal mapping, `On <ID>` conversion of declarations of records `runtime.md`
declares, removal of rejected proposals, `finalized-from` set to the local
report's SHA-256, and an appended `## Amendments` section of `none`. It prints
the mechanical edits for the overview's Reconciliation and refuses an unmapped
proposal, a rejected proposal other findings still reference, or a merged row
that disagrees with the declarations. `manifest <run-state>` writes
`output/ARTIFACT.yaml` pinning the set members present in `output/`; rerun it
after any member edit.

### commonplace-agentic-analysis-handoff

Validate one `complete` agentic-system analysis run state and render its
Markdown operator handoff from the frozen source and current output identities.
The command is read-only. It refuses a running, failed, or invalid run.

### commonplace-agentic-analysis-publication

Publication invokes the regular validator on the prospective complete run
set, including quotation occurrence within attribution ranges and the existence
of path-only source anchors at the frozen commit. Quotation generation
belongs to `commonplace-quote`; there is no separate authoring-time source-check
operation in this command.

Inspect a destination, prepare or publish the compact review of one running
agentic-system analysis. `inspect-destination` takes `--generated-destination`
and `--source-identity`; it returns a replacement decision and incumbent digest
without emitting prior review prose or descriptions. Both `prepare` and
`publish` require that digest through `--expected-incumbent-sha256` (`absent`
for a vacant destination). Destination drift requires a new inspection.

All three operations require a worktree that is clean outside the workflow's
output locations: no staged change or modified tracked file, and no untracked
file under `kb/`, except that `kb/agentic-systems/reviews/` and
`kb/reports/retained/agentic-system-analysis/` may hold untracked files and
unstaged modifications of tracked files, where a sibling run's uncommitted
publication may sit; ignored paths never count. `prepare` and `publish` also
require the overview's `inputs-commit` to be an ancestor of or equal to HEAD
with the method paths unchanged between them, so the commit identifies the
method the run used. The method paths are the `METHOD_PATHS` constant in
`src/commonplace/lib/agentic_publication.py`. They also require the source
of the running `commonplace` package, which may come from another checkout
than the one publishing (an editable install run inside a batch worktree),
to have no committed, staged, modified or untracked difference under
`src/commonplace/` from `inputs-commit`. All three errors name the
offending paths.

An incumbent is checked by bytes: it must be a generated review of the same
source whose retained manifest and members hash to their pins. It may be
committed or a sibling's fresh uncommitted publication; no publication receipt
is read. This checks replacement provenance, not compliance of the old analysis
with today's method. Replacement saves `incumbent-review.md` and an
`incumbent-<member>.md` copy of each retained member in the new run for
recovery.

`prepare` validates the directory artifact and its members as their
retained paths, the specialist memory report's pins, and the candidate review,
and checks the incumbent without changing public artifacts. It does not create
a semantic-review job; specialist analysis does not establish independent
semantic clearance. `publish` rechecks the inputs, validates the prospective
complete run state, replaces the review, retains `ARTIFACT.yaml` and the four
members byte for byte under `kb/reports/retained/agentic-system-analysis/<run-id>/`, and writes
the run state last. New publications require `memory-comparison` in the memory
member and a matching retained manifest path and hash in the public review.
An existing retained set requires a new run ID. Ordinary in-process failures
roll back written files; crash-level partial writes remain an admitted failure
mode.

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
A directory containing `ARTIFACT.yaml` receives set checks and ordinary member
checks, grouped as one artifact. Explicit file validation stays file-scoped.
See [directory artifacts](./validation-contract.md#directory-artifacts).


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

### commonplace-quote

Generate citations from selected text and an analysis run's frozen Git blob or
capture. One occurrence returns only the Markdown citation, containing the exact
source excerpt and derived range. Two to ten occurrences return JSON candidates
with selection metadata. More than ten returns an error asking for a longer
quote. When repeated occurrences share a line, the returned excerpts include
enough surrounding source to distinguish them. The author chooses one and
inserts it unchanged; the tool does not validate an assembled document.
Publication uses the regular validator. Use `--text-file` or stdin for
selected text to avoid shell quoting, and omit `--source-path` when the run's
source is a capture rather than a Git blob.

To resolve many selections in one call, pass `--selections <file>` instead: a
JSON list of objects with a unique `key`, the selected `text`, and
`source_path` (omitted or null for a capture). The output is a JSON object
keyed by selection; each value has `status: citation` with the citation to
insert unchanged, `status: candidates` with the same occurrence list as the
single-selection case, or `status: error` with the reason. Exit status 0 means
every key resolved to a citation; 2 means at least one key needs a choice or
failed, and stderr names them; 1 is a malformed list or an unusable run state.
Each source file is read once per call. Treat a `candidates` entry as a choice
to make (insert one candidate's citation unchanged, or lengthen the selection)
and an `error` entry as a selection to rewrite from a fresh source read; an
assembler that only handles `citation` fails silently on both.

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

## Workflows

### commonplace-workflow

Run a code-scheduled workflow. `start <package.module:ClassName>` creates a
run where the definition says its runs go, allocating a free name, and prints
its directory; `--run <dir>` names the directory instead; `step <run>` advances it and prints the outcome (`launch`, `done`,
`blocked` or `uncertain`); `report <run> <event>` records a failed launch, a
repair or a stop. `resolve` and `release` are the operator's commands after an
uncertain outcome or a stop-only block. The agent orchestrator's side is
`kb/instructions/analyse-agentic-system/drive-a-code-scheduled-run.md`. The
design is still a proposal: `kb/reference/proposals/code-scheduled-workflows.md`.

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
