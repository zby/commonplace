---
description: "Architecture boundaries of Commonplace freshness: target identity, accepted-input applicability, review adaptation, transitions, and concurrency guards"
type: kb/types/note.md
tags: []
---

# Freshness architecture

Freshness says whether a registered target's current inputs match the versions
accepted for it. It says nothing about truth, approval, or whether findings
were handled. A baseline is an applicability boundary for retained evidence.

This page records the relations that span the generic freshness substrate and
its review adapter. Exact store objects, schema versions, JSON fields, command
arguments, status labels, and exit codes belong to the executing
`commonplace.store`, `commonplace.freshness`, and `commonplace.cli.freshness_*`
source and command help. [Storage](./storage-architecture.md) places the SQLite
store among Commonplace's other authorities.

## Target and input boundary

The generic substrate identifies a target by kind plus a complete canonical
key. It records each role-labelled input's identity, version kind, and exact
accepted version.

The only v1 specialization is a `review-pair` target. Its key consists of note
path, criterion path, and model partition. Its two inputs are the `note` and
`criterion` files, both versioned as UTF-8 text. The model partition belongs to
target identity: evidence under one partition does not make another partition
fresh.

The criterion role is path-generic. Catalog gates, type specs, collection
contracts, and the critique instruction can occupy it. No synthetic criterion
or third dependency is registered.

Each review baseline points to the completed pair whose evidence it makes
current. Acknowledgement can advance the baseline while preserving that pair;
a new review replaces it. The store records which evidence still applies, not
whether its outcome or prose deserves endorsement.

## Registered status and review discovery

Repository-wide status starts from registered baselines. It can find changed,
missing, or unresolvable registered inputs, but not a target that never had a
baseline. Applicable-pair discovery remains review-owned: the review selector
combines notes and criteria and reports `missing-baseline` for an unregistered
pair. The two paths answer different questions.

Malformed registered state is a store error, not an absent baseline or
ordinary staleness. Exact status rendering and filtering remain in live source
and `--help`.

## Transition boundaries

| Transition | Input authority | Concurrency intent | Evidence effect |
|---|---|---|---|
| Capture refresh | Snapshots captured when a review job was created | Baseline state observed at queue time must still be current | Replace with the completed pair |
| Observation acknowledgement | Files resolved live when the acknowledgement executes | Caller revision and any supplied observed hashes must still match | Preserve the existing pair |
| Retirement | Registered target identity | Idempotent removal; revision generation remains advanced | Remove the current evidence association |

Capture refresh belongs to successful finalization. It accepts the snapshots
the worker judged rather than substituting a later live-file read. Its guard
asks whether baseline state changed while the job was queued; success replaces
the evidence association with the accepted inputs.

Observation acknowledgement applies only to an existing baseline. It compares
the caller's expected revision, resolves live text, and preserves the evidence
pair. Hashes supplied from an earlier status result guard against change
between inspection and acknowledgement; omitting them observes both registered
inputs at execution time. The review-specific acknowledgement adapter always
supplies the hashes and roles from inspected review-selector output; only the
generic transition retains the observe-at-execution option.

Retirement removes the current baseline, inputs, and evidence association. It
does not imply deletion of historical jobs or artifacts. The retirement
instruction owns the larger artifact-removal workflow.

## Queue-to-finalize concurrency invariant

A queued pair records exactly one expectation: the current baseline revision
when one exists, or the next revision from a persistent generation ledger when
none exists. Finalization must still see that expectation.

The revision guard rejects advance, removal, and retire/recreate. The generation
guard catches the otherwise invisible absent/create/retire sequence. Revisions
are never reused after retirement. These guards protect baseline concurrency,
not live-file currency: the result stays tied to its captured inputs, and a
later file change makes it stale on the next comparison.

## Registration scope

Review finalization is the only v1 path that creates or replaces a baseline;
status, acknowledgement, and retirement operate on registered targets. No
generic creation command ships because no adopted non-review target supplies a
complete identity, dependency, producer, evidence, and registration contract.
[ADR 065](./adr/065-publish-only-supported-freshness-transitions.md) owns the
rule that an interface returns only with such a consumer.

## Maintenance scope

Review this page when target identity, input dependency, registered-status
ownership, review discovery, transition evidence semantics, or queue-to-finalize
concurrency changes. Module additions, store paths, schema objects and versions,
JSON fields, command options, status labels, and exit codes do not by themselves
require an edit; their exact owners remain source, schema, and command help.

## See also

- [Review architecture](./review-architecture.md) — job creation, external dispatch, and atomic finalization
- [Review-system guide](./README-REVIEW-SYSTEM.md) — operator concepts and workflows
- [Commands](./commands.md) — discovery route for status, acknowledgement, retirement, and review commands
- [ADR 052](./adr/052-general-freshness-store-review-first-migration.md) — decision to generalize the store around targets and inputs
- [ADR 065](./adr/065-publish-only-supported-freshness-transitions.md) — no interface without an implemented target consumer
