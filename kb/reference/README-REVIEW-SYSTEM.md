---
description: How to use the Commonplace review system — concepts, freshness, the review-batch workflow, and command surface
type: kb/types/note.md
tags: []
status: current
---

# Review system

The review system runs gate-based quality reviews of KB notes and records their outcomes. A single review checks one note against one *gate* — a review lens such as `prose/source-residue` — and produces a decision (`pass`, `warn`, `fail`, or `error`) together with a written rationale. The notes and gates being reviewed stay as markdown files in the repo; the review state produced about them lives in a local SQLite database.

Two properties shape everything else:

- **Freshness is independent of Git.** Review creation, full-review acceptance, and trivial acknowledgement each store DB-owned snapshots of the exact note and gate text that form the accepted baseline. Staleness is decided by comparing current file text against those snapshots, not by inspecting Git history.
- **It is experimental and opt-in.** Reviewing is not part of the default note-writing flow, and reviews are not always-on checks. You invoke the system deliberately when you want a note judged.

Storing review state in SQLite is a scoped exception to the repo's file-first design; [ADR-010](./adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md) records why. This document covers how to operate the system; for how it is built, see [review architecture](./review-architecture.md).

## How a review flows

A full review runs as a short pipeline, from a stale-pair query to a durable acceptance:

1. **Select** — the selector lists `(note, gate)` pairs that are stale or unreviewed for a given model partition, and says why.
2. **Create jobs** — selected pairs are packed into one or more queued *review jobs*, each with its own rendered prompt.
3. **Review** — a worker (typically a sub-agent) reads a job's prompt and writes a single sentinel-delimited `bundle-output.md`.
4. **Finalize** — the parent parses that output and, only if every expected pair is present and well-formed, records the decisions and appends acceptance events.

Acceptance is the durable outcome. An acceptance event pins the exact note and gate text that was reviewed, so the selector can later tell whether either side has drifted. When a note changes only trivially, an existing acceptance can be carried forward without a fresh review (*ack*).

## Concepts

**Gate.** A markdown file at `kb/instructions/review-gates/{lens}/{name}.md` in a source checkout, or under the installed framework gate catalog in generated projects. The `{lens}/{name}` shorthand is the gate id used at the CLI boundary (for example `prose/source-residue`).

**Bundle.** A directory of gates sharing a lens. `semantic` means all gate files under `kb/instructions/review-gates/semantic/`.

**Review job.** One review invocation: one rendered prompt, one output artifact directory, and one job-level status. A job is `queued` until finalization marks it `completed` or `failed`.

**Review pair.** One requested `(note_path, gate_path)` pair inside a review job. This is the unit of review output and acceptance. A pair's decision is one of `pass`, `warn`, `fail`, `error`.

**Acceptance event.** A record that a `(note_path, gate_path, model_partition)` key was reviewed against specific note and gate text. Acceptance is what makes a pair "fresh."

**Model partition.** Reviews are partitioned by model. A review or acceptance under one model does not satisfy freshness for another.

Human-readable review output — the per-pair result files and each job's `MANIFEST.json` — is for inspection only. The SQLite decision and job-status columns are canonical; see [review architecture](./review-architecture.md) for the storage details.

## Reading freshness

The selector reports each requested `(note, gate)` pair as fresh or, if not, why it is stale. It compares three things: the current note file, the current gate file, and the latest acceptance for that `(note_path, gate_path, model_partition)` key.

- no acceptance for the pair → `missing-review`
- accepted note or gate snapshot is missing → `missing-review`
- accepted gate text differs from the current gate → `gate-changed`
- accepted note text differs from the current note → `note-changed`
- otherwise the pair is fresh

For `note-changed` pairs, the selector can show the diff against the accepted note text, so you can judge whether the change is significant for that gate.

## Running a review batch

The full procedure is in [run review batches](../instructions/run-review-batches.md). In outline:

1. Select stale pairs and create jobs:

   ```
   commonplace-review-target-selector ... --json | commonplace-create-review-jobs --input - --grouping {note|gate}
   ```

   `--grouping note` packs all gates for one note into a shared prompt; `--grouping gate` packs one gate across notes. Choose according to the prompt shape you want.

2. For each job, launch a sub-agent that reads the job's `prompt_path` and writes its review to the job's `bundle_output_path`.

3. Finalize each completed output:

   ```
   commonplace-finalize-review-job --review-job-id {id} [--runner {worker}] [--model {model} [--effort {effort}]]
   ```

**Finalization is all-or-nothing.** If any expected pair is missing, duplicated, unexpected, malformed, or lacks a valid result line, the job fails and appends no acceptance events — a failed job accepts nothing. On success, every pair is recorded and one acceptance event per pair is appended.

**Finalization-time provenance is optional.** When supplied, `--model` (with optional `--effort`) is validated against the job's model partition before any state changes, and the runner/model/effort are recorded. `--effort` requires `--model`.

## Reviewing stale pairs

Use the same [run review batches](../instructions/run-review-batches.md) procedure. Select stale pairs for a model partition:

```
commonplace-review-target-selector --model {model-partition} {gate-or-bundle}... --note {note-or-dir}... --json
```

Then create jobs from that JSON with `--grouping note` or `--grouping gate`.

For `note-changed` pairs, inspect the selector diff first. If the change is insignificant for the gate, acknowledge it instead of running a fresh review (see below).

## Acknowledging trivial changes

`commonplace-ack-gate-review` advances the accepted baseline when a note changed but not in a way that matters for the gate. It carries the existing review forward: it records the current note and gate text as newly accepted, pointing at the completed review pair being reused. It does not rewrite any file or review prose.

```
commonplace-ack-gate-review --model {model-partition} {note_path} {gate_id}...
```

Ack fails when there is no completed review for the same `(note_path, gate_path, model_partition)` — there must be existing review evidence to carry forward. Output lines have the form `acked: <note_path> <gate_id>`.

## Building a warn/fix queue

`commonplace-warn-selector` builds a fixing queue from the current review state — the actionable findings from reviews whose decision is `warn`. It is the entry point to the [fix system](../instructions/FIX-SYSTEM.md), which turns these findings into applied corrections and fix reports.

- it reads current accepted review pairs across all models
- it loads each review's rationale text from the accepted pair's result file (unavailable if the file is missing)
- it skips findings whose gate changed since acceptance
- it collapses model partitions to one current entry per `(note_path, gate_path)`, choosing the latest accepted warn review

## Command reference

**Selector** — `commonplace-review-target-selector`:

- positional gate ids and/or bundle names (e.g. `prose`, `semantic/grounding-alignment`)
- `--all-gates` to check all gates
- `--note` to filter to specific note paths or directories
- `--current` to filter to notes with `status: current`
- `--model {model-partition}` selects the review model partition to inspect or write; omit it only for model-agnostic missing-review coverage
- `--json`
- `--reason {missing-review,gate-changed,note-changed}`

With `--model` omitted, the selector reports only model-agnostic missing-review coverage: a pair is `missing-review` only when there is no acceptance under any model partition. It does not classify `gate-changed` or `note-changed` in that mode, because those need a chosen baseline.

**Create jobs** — `commonplace-create-review-jobs --input - --grouping {note|gate}`. Consumes selector JSON.

**Finalize** — `commonplace-finalize-review-job --review-job-id {id} [--runner {worker}] [--model {model} [--effort {effort}]]`.

**Ack** — `commonplace-ack-gate-review --model {model-partition} {note_path} {gate_id}...`.

**Warn queue** — `commonplace-warn-selector`.

## The reviewer output contract

A worker reviewing a job writes one sentinel-delimited `bundle-output.md` covering every pair in the job. Each pair block ends with exactly one parseable result line:

```text
## Result: PASS
## Result: WARN
## Result: FAIL
## Result: ERROR
```

Aliases such as `Verdict`, `Outcome`, `INFO`, `OK`, and `UNKNOWN` are invalid — finalization rejects them. The worker writes only the bundle output file; it does not touch notes, gates, indexes, or the review database.

## Authoring a gate

Gates are typed `kb/types/review-gate.md`. See [that type spec](../types/review-gate.md) for the frontmatter and body contract, and `kb/instructions/review-gates/` for examples. This document covers runtime concepts (bundles, freshness, acceptance, the batch workflow); the type owns the authored shape of a gate.
