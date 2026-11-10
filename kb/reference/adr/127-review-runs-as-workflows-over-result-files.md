---
description: "Review and freshness run as Python workflows over the headless runtime: one commonplace-review command, one result file per (note, criterion) pair hashing both inputs, no SQLite store, no acknowledgement and no model partitions"
type: reference/types/adr.md
status: accepted
---

# 127 — Review runs as workflows over result files

**Status:** accepted; implemented on the operator's direction, which also ordered the old system's retirement without compatibility or data migration.
**Date:** 2026-11-10
**Supersedes:** [ADR 010](./010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md) (review state in SQLite), [ADR 035](./035-review-jobs-finalize-all-or-nothing-with-derived-artifacts.md) (queued jobs and their finalization), [ADR 043](./043-review-state-separates-completion-outcomes-and-freshness-baselines.md) (the store's completion, outcome and baseline model), [ADR 052](./052-general-freshness-store-review-first-migration.md) (the general freshness store), [ADR 065](./065-publish-only-supported-freshness-transitions.md) (the store's published transitions) and [ADR 067](./067-review-workers-read-one-prompt-and-write-one-output.md) (the prompt-path worker contract). It also supersedes three earlier decisions about the same store: [ADR 029](./029-review-execution-unified-on-note-gate-pairs.md) (one packing protocol for pairs), [ADR 032](./032-review-freshness-uses-db-snapshots-not-git.md) (freshness from SQLite snapshots under a model partition) and [ADR 036](./036-review-acceptance-is-current-state-not-append-only-history.md) (acceptance rows as current state).
**Amends:** [ADR 038](./038-type-conformance-reviews-use-the-type-spec-as-the-gate.md) and [ADR 041](./041-collection-conformance-reviews-use-collection-md-as-the-gate.md): the type spec and the `COLLECTION.md` stay the criterion; store identity, model partitions and acknowledgement go. [ADR 051](./051-full-pass-packets-own-guarded-captures-and-resolutions.md) and [ADR 080](./080-full-passes-hand-claim-changes-back-as-a-pending-revise.md): packets, pending hand-backs and the bounded closing stay; captures and the guard command become run records and recorded hashes. [ADR 039](./039-tool-visibility-is-package-owned-and-git-is-never-invoked.md): `commonplace-review` invokes Git for the repository root and the checkout guard.

## Context

Review applies a criterion file to a note and keeps the judgment while both
texts are unchanged. The store-based system did this with an agent in a
conversation coordinating workers through files and a database: a selector,
queued jobs, a finalizer, model partitions, baselines with acknowledgement,
and a command per transition, over a 50 MB SQLite file. Most of that machinery existed
because no code owned the run. The parent agent scheduled workers, so job
state, transport files and all-or-nothing finalization had to make its
handoffs safe.

The headless runtime ([ADR 118](./118-analyses-run-as-a-workflow-over-headless-harnesses.md),
[ADR 119](./119-analysis-workers-launch-through-workjig.md)) now supplies a
workflow written in Python with what the store built by hand: one agent call
per request, a run lock, durable launch records, replay of answered calls,
deterministic checks with retry, worker problems and usage-limit stops. It
does not keep state across runs: Workjig's records belong to one run and
promise no format compatibility. Freshness across runs therefore still needs
a durable record of what text a judgment was produced from.

Phase 0 of the design work measured the store on 2026-11-09: 9,217
baselines and 6,947 recorded jobs, the last completed 2026-09-26. 37
baselines stood on an acknowledgement (note side only); that count is a lower
bound, because a later review replaces an acknowledged baseline. Outside the
review and freshness packages, only status reporting and a store health check
read the store.

## Decision

**A result is a file.** Each accepted review writes
`kb/reports/state/review/results/<note-path>/<criterion-id>.md`. Its
frontmatter names the note and the criterion with the SHA-256 of the texts
the worker was given, the outcome (`pass`, `warn`, `fail`, or `report` for a
report criterion), the worker profile, the model the harness recorded, and
the run and launch; the body is the reviewer's text. A pair is fresh when both
hashes match the current files. Status, staleness and orphan detection are
pure functions over these files. Freshness depends on neither Git nor a
store. One result exists per pair, whichever profile produced it.

**The note hash covers what the criterion watches.** A criterion that
declares `watches:` (title, description, body) is hashed against those note
parts, normalized so a whitespace-only edit changes nothing. A criterion
without a valid declaration watches the whole note. This replaces
acknowledgement of edits outside the watched parts.

**Review is workflows, under one command.** `commonplace-review` runs
`run gates` (the gate sweep), `run full-pass` (the full improvement pass)
and `run revise` (the simplification passes), with `status`, `packet`,
`retry` and `acknowledge`, plus `approve` for operator answers. A workflow is a Python function over `ask`,
`checked`, `gather` and `decide`. Each run has one directory under
`kb/reports/state/review/runs/`. A sweep opens a new directory, and
`--resume` continues it and replays answered calls. A full pass or revision
derives its directory from the workflow, the note's path and the hash of the
note's text, so repeating the command continues the run by replay, and an
edited note opens a new run. Where a workflow needs the operator, it
proposes a file in the run and stops. Explicit approval captures the edited
or unedited file as an answer, bound to that stop, proposal and its inputs.
Repeating never approves; an edit after approval has no effect until
approved again. Changed proposal inputs invalidate the approval. Options
such as the profile and the full pass's
direction are recorded with the run.

**Workers never write the checkout.** A worker receives captured inputs and
writes only its output files. Code checks each output (the strict result
line, a decision schema, the bounds an edit must keep). A workflow that edits
a note carries each edited text forward in memory and in the run directory,
and writes the note once, at its last step, only from the start text. A note
changed during the run is a conflict, and nothing is written. A checkout
guard reports paths that changed while a run was open.

**A criterion is any markdown file.** Catalog gates, a type spec, a
`COLLECTION.md` and the critique instruction all enter as the `criterion`
input. The workflow names the output contract, verdict or report.

**The full pass keeps its packet.** It asks the gates over each text it
reviews and writes result files once, at its end, for the text the note then
holds. The packet is markdown whose frontmatter
code writes: the note, the start and final text hashes, the decision, the
closing status and the resolution fields. Its start text lives in the run;
`commonplace-review packet` compares the recorded hashes with the files.

## Considered alternatives

**One long-lived run as the store.** Workjig keeps every call of a run in one
record file; thousands of pairs would make that file the database this
decision removes. Set aside for one run per invocation, with result files
carrying freshness across runs.

**Migrating the baselines.** The operator judged on 2026-10-24 that the
stored reviews were outdated. The new system started empty; the first sweeps
produce its results. The store and its job directories are abandoned local
data.

**Implicit approval on repeat.** Rejected: retrying after interruption must
not make an operator decision. A separate approval command captures the
answer; a stale proposal key is refused. The command does not authenticate
the human: operating instructions permit an agent to approve only on the
operator's stated word for that proposal.

**Keeping acknowledgement.** Dropped. It covered 37 of 9,217 baselines, and
the watched-parts hash absorbs its commonest case. A changed pair is
re-reviewed. An acknowledgement command returns only when sweeps show the
re-review cost.

**Keeping model partitions.** Dropped. The profile and the recorded model are
provenance, not identity, and `status` shows them. What would reopen it: an
operator who wants two models' verdicts on one pair kept side by side.

**One call per pair or per bundle.** Both shipped. `pair` asks one worker per
stale pair, so a criterion edit re-asks exactly its pairs; `bundle` asks one
worker per note and bundle of catalog gates for that bundle's stale gates,
and each gate still gets its own result. A launch's fixed context dominates
its cost: one live pair cost $0.095, nearly all of it fixed context, and one
bundle launch reviewed nine `prose` pairs on one short note for $0.172 in
31 s. Each figure is a single observation. The sweep defaults to `pair`
until a comparison shows whether grouping changes verdict quality; the full
pass uses `bundle`.

**Decision models for bounded gates.** Deferred. A judgment-specialized model
could serve closed-ended gates, but its cost is calibration per gate, under
the [gate calibration proposal](../proposals/calibrating-semantic-gates-against-labelled-fixtures.md).
The result file names an executor rather than a launch, so such a result
fits it.

**A directory type for a full-pass run.** Deferred until a run shows what
validating a run directory as one unit would catch that the packet type and
the result-file parser do not.

## Consequences

The operativity path: the `commonplace-review` command and its library
modules enforce result files, freshness, the checkout bounds and packets in
code. `commonplace-status --review` reads the result files. The review-system
guide, the full-pass and disposition instructions and the fix procedure bind
agents operating review. `kb/instructions/review-profiles.yaml` sets what a
worker may do. A review gate's `watches:` now decides which edits stale its
pairs, so gate authors set staleness.

Easier: adding a workflow is one Python function plus its criterion files. A
stopped run continues where it stopped without repeating a paid answer.
Freshness is inspectable as files. The full pass and the revision apply an
edit only through code that checks it, and change the note at most once per
run. A hand-back or an unfinished run leaves the note untouched, so nothing
needs restoring.

Harder: every changed pair is re-reviewed, and a type-spec or `COLLECTION.md`
edit re-reviews its whole cohort. A wrong `watches:` declaration leaves pairs
falsely fresh. A note move orphans its results; they are deleted and the
pairs reviewed again. Results stay machine-local and untracked.
`commonplace-review` needs a Git working tree: it finds the repository root
with Git and reads `git status` for the checkout guard, against ADR 039's
rule that commands never invoke Git. Freshness itself does not depend on
Git.

Dropped without replacement: acknowledgement, model partitions,
link-consumption and availability telemetry, the reviewer's self-reported
model, relocation's rekeying of review state and the generic freshness store
for non-review targets.

Open:

- the default grouping, pending a quality comparison of pair and bundle
  verdicts;
- the checkout guard cannot tell a worker's change from another session's,
  so concurrent work in the checkout makes a run exit nonzero with paths to
  inspect;
- the Claude Code profiles' write denial outside the run directory has not
  been seen to refuse a write: the guard is the only verified control;
- the `codex` profile cannot be sandboxed read-only, so it relies on the
  prompt and the guard.

Limits: decided and run in this checkout, with the `sonnet` profile for the
live runs. One full pass on a short note took 27 launches and $4.47 and ended
in a hand-back; that is one observation, not an
estimate of pass cost or outcome. The `opus` and `codex` profiles and the
revision workflow have no live measurement here. The prompt around the inputs
is outside the freshness hashes, so a prompt change re-asks calls on a
resume or repeat but stales no result; judgment belongs in criterion files.

---

Relevant Notes:

- [Review system](../README-REVIEW-SYSTEM.md) — implemented-by: the operating page of `commonplace-review`
- [Review architecture](../review-architecture.md) — implemented-by: result files, freshness, workflows and the checkout guard as built
- [The practical scheduler is the host language](../../theory/the-practical-scheduler-is-the-host-language.md) — rests-on: control flow stays in Python; the runtime journals results
- [The boundary of automation is the boundary of verification](../../theory/the-boundary-of-automation-is-the-boundary-of-verification.md) — rests-on: code applies verdicts and writes the checkout; workers only produce outputs
