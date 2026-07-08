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
4. **Finalize** — the parent parses that output and, only if every expected pair is present and well-formed, records the decisions and upserts accepted baselines.

Acceptance is the durable outcome. A current acceptance row pins the exact note and gate text that was reviewed, so the selector can later tell whether either side has drifted. When a note changes only trivially, an existing acceptance can be carried forward without a fresh review (*ack*).

## Concepts

**Gate.** A markdown file at `kb/instructions/review-gates/{lens}/{name}.md` in a source checkout, or under the installed framework gate catalog in generated projects. The `{lens}/{name}` shorthand is the gate id used at the CLI boundary (for example `prose/source-residue`).

**Bundle.** A directory of gates sharing a lens. `semantic` means all gate files under `kb/instructions/review-gates/semantic/`.

**Type-conformance pair.** A review of a note against the type spec named by its frontmatter `type:` — the type spec *is* the gate ([ADR 038](./adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md)). Request it with the virtual `type` lens: `type` derives one pair per typed note in scope, `type/definition` narrows to one type's cohort. The gate id is `type/{name}`; the persisted gate identity is the type-spec path (for example `kb/types/definition.md`). Because the type spec sits on the gate side, editing it stales exactly the notes of that type as `gate-changed`, and a trivial type edit is acknowledged like any other gate edit. `--all-gates` includes type-conformance pairs alongside the catalog; request them alone via the `type` lens. The rendered prompt carries a fixed conformance instruction that references the type spec by path — the reviewer reads the spec from disk instead of receiving it packed into the prompt; if a type spec carries an authored `## Review` section, reviewers treat it as the operative test.

**Collection-conformance pair.** A review of a note against the `COLLECTION.md` contract of the collection it lives in — the contract *is* the gate ([ADR 041](./adr/041-collection-conformance-reviews-use-collection-md-as-the-gate.md)). Request it with the virtual `collection` lens: `collection` derives one pair per in-collection note in scope, `collection/notes` narrows to one collection's cohort (the path segment is the collection directory relative to `kb/`, so a collection under a namespace directory reads `collection/commonplace/notes`). The persisted gate identity is the COLLECTION.md path (for example `kb/notes/COLLECTION.md`). Editing a collection contract stales exactly that collection's notes as `gate-changed`; `--all-gates` includes collection-conformance pairs. The prompt mechanics mirror the type pair — the contract is referenced by path and read from disk, an authored `## Review` section in the COLLECTION.md is the operative test, and the reviewer judges only what the collection contract asks beyond the type contract, so the two conformance pairs do not double-flag. The contract is itself a typed artifact (`type: kb/types/collection.md`, [ADR 042](./adr/042-collection-contracts-are-typed-artifacts.md)): note sweeps exclude COLLECTION.md files explicitly, but selecting one by path derives its own type-conformance pair, so contract prose is reviewable on demand.

**Review job.** One review invocation: one rendered prompt, one output artifact directory, and one job-level status. A job is `queued` until finalization marks it `completed` or `failed`.

**Review pair.** One requested `(note_path, gate_path)` pair inside a review job. This is the unit of review output and acceptance. A pair's decision is one of `pass`, `warn`, `fail`, `error`.

**Acceptance row.** The current record that a `(note_path, gate_path, model_partition)` key was reviewed against specific note and gate text. Acceptance is what makes a pair "fresh."

**Model partition.** Reviews are partitioned by model. A review or acceptance under one model does not satisfy freshness for another.

Human-readable review output — the per-pair result files and each job's `MANIFEST.json` — is for inspection only. The SQLite decision and job-status columns are canonical; see [review architecture](./review-architecture.md) for the storage details.

## Reading freshness

The selector reports each requested `(note, gate)` pair as fresh or, if not, why it is stale. It compares three things: the current note file, the current gate file, and the current acceptance for that `(note_path, gate_path, model_partition)` key.

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

3. Finalize each completed output with `commonplace-finalize-review-job` (signature under [Command reference](#command-reference)).

**Finalization is all-or-nothing.** If any expected pair is missing, duplicated, unexpected, malformed, or lacks a valid result line, the job fails and writes no acceptance rows — a failed job accepts nothing. On success, every pair is recorded and the current acceptance row for each pair is upserted.

**Finalization-time provenance is optional.** When supplied, `--model` (with optional `--effort`) is validated against the job's model partition before any state changes, and the runner/model/effort are recorded. `--effort` requires `--model`. `--telemetry-json` stores opaque harness telemetry without making it review identity.

## Acknowledging trivial changes

For a `note-changed` pair, inspect the selector diff (see [Reading freshness](#reading-freshness)) first. If the change is insignificant for the gate, acknowledge it instead of running a fresh review.

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

## Interpreting review output

A `pass` records that the gate's check found nothing to flag; it is not a certification that the note has no problems, only that this particular check didn't detect one. Treat it as an absence-of-detected-problem signal rather than a guarantee — an automated check with real but imperfect discriminative power is still worth having, but only as long as a clean result is never trusted beyond what it actually tested.

The same principle applies once a `warn` finding is delegated to the fix system. When the fix produces a diff, reviewing that diff is the judgment step: it checks the resulting artifact directly, rather than trusting the fixing agent's own report of success. Reading the agent's self-report still matters when no diff results — there is no artifact to substitute for it, so that case still needs the claim read directly.

This is why gates route a bare finding rather than a self-graded verdict — see [composition friction gate](../instructions/composition-friction-gate.md)'s hard rule against emitting a pass/fail verdict, and the broader case in [an adversarial human-agent loop can reconstruct the writing-is-thinking filter](../notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md).

## Command reference

**Selector** — `commonplace-review-target-selector`:

- positional gate ids, bundle names, and/or conformance requests (e.g. `prose`, `semantic/grounding-alignment`, `type`, `type/definition`, `collection`, `collection/notes`)
- `--all-gates` selects every applicable review criterion in place of naming ids/bundles (mutually exclusive with them): all catalog gates plus each note's type-conformance and collection-conformance pairs. The flag means the same thing in every review command. Like every selector flag it only *chooses* pairs — the selected `(note, gate)` pairs still run through create-jobs → review → finalize; it is not a one-shot "run all gates" command
- `--note` to filter to specific note paths or directories
- `--current` to filter to notes with `status: current`
- `--model {model-partition}` selects the review model partition to inspect or write; omit it only for model-agnostic missing-review coverage
- `--json`
- `--reason {missing-review,gate-changed,note-changed}`

With `--model` omitted, the selector reports only model-agnostic missing-review coverage: a pair is `missing-review` only when there is no acceptance under any model partition. It does not classify `gate-changed` or `note-changed` in that mode, because those need a chosen baseline.

**Create jobs** — `commonplace-create-review-jobs --input - --grouping {note|gate}`. Consumes selector JSON.

**Finalize** — `commonplace-finalize-review-job --review-job-id {id} [--runner {worker}] [--model {model} [--effort {effort}]] [--telemetry-json {json}]`.

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
