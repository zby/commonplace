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

### commonplace-validate

Run deterministic validation on one artifact, collection, type surface,
collection-landing set, or redirect map. The
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

Compare a full-pass packet's guarded captures with their live artifacts before
any disposition is executed. The
[full-improvement instruction](../instructions/run-full-improvement-pass-on-note.md)
owns the refusal and reconciliation workflow.

### commonplace-relocate-note

Rename or move one note and rewrite its KB backlinks. The command dry-runs
unless `--apply` is supplied.

### commonplace-relocate-directory

Move a KB directory, rewrite links, and optionally add one ProperDocs redirect.
The command dry-runs unless `--apply` is supplied.

### commonplace-promotion-candidates

Rank unstructured note files by incoming links and write
`kb/reports/promotion-candidates.md`, separating invalid frontmatter from text
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
pair results, and advance their freshness baselines.

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

Advance existing review freshness without rerunning the assay. It preserves
the evidence review pair; for a report, it does not endorse or resolve the
findings.

### commonplace-ack-trivial-note-changes

Auto-acknowledge `note-changed` verdict pairs when none of the criterion's
watched note parts changed. Invoking it is explicit human authorization for
the qualifying trivial-change workflow.

### commonplace-resolve-criteria

Resolve gate, bundle, concrete conformance, or critique requests into their
criterion definitions.

### commonplace-review-target-selector

Select applicable assay pairs either by current staleness or by an explicit
requested-mode scope, for inspection or piping into job creation.

### commonplace-warn-selector

Extract actionable findings from effective `warn` review pairs. It is the
entry point to the [fix system](../instructions/FIX-SYSTEM.md).
