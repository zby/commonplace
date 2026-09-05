---
description: Reference for the commonplace-* CLI commands shipped by llm-commonplace - project setup, validation, indexing, snapshots, note operations, and the review system
type: kb/types/note.md
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

Create or extend a Commonplace project without overwriting existing files. See
[architecture](./architecture.md) for the installed topology and package/user
boundary.

### commonplace-source

Print the filesystem path of the `commonplace` package that supplies the
running commands.

## Validation and indexing

### commonplace-agentic-analysis-handoff

Validate one `complete` agentic-system analysis run state and render its
Markdown operator handoff from the frozen source and current output identities.
The command is read-only. It refuses a running, failed, or invalid run.

### commonplace-agentic-analysis-publication

Prepare or publish the review projections of one running agentic-system
analysis. `prepare` validates candidate bytes as their intended destinations,
checks incumbents, and creates the required legacy semantic-review job without
changing public artifacts. After that job finalizes with passes, `publish`
rechecks its baselines, validates the prospective complete run state, replaces
the reviews, retains the exact result bytes at
`kb/reports/retained/agentic-system-analysis/<run-id>/result.md`, and writes the
run state last. New publications require the result's `memory-comparison`
fields and matching retained-result path/hash in the public review. An existing
retained result requires a new run ID. Ordinary in-process failures roll
back written files; crash-level partial writes remain an admitted failure mode.

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

Rename or move one note and rewrite its KB backlinks. The command dry-runs
unless `--apply` is supplied.

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
`kb/sources/.snapshots/` reading cache.

### commonplace-x-snapshot

Capture an X/Twitter post, thread, or article under the ignored
`kb/sources/.snapshots/` reading cache.

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
