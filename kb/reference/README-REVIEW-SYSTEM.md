---
description: How to use the Commonplace review system — concepts, freshness, the review-batch workflow, and command surface
type: kb/types/note.md
tags: []
status: current
---

# Review system

The review system runs snapshot-anchored assays over KB notes and records their outcomes. Most pairs are verdict-kind gate reviews producing `pass`, `warn`, `fail`, or `error`; the opt-in critique assay is report-kind and completes without a decision. Notes and assay criteria stay as markdown files in the repo; review state lives in a local SQLite database.

Two properties shape everything else:

- **Freshness is independent of Git.** Assay creation, finalization, and acknowledgement store DB-owned snapshots of the exact note and criterion text that form the accepted baseline. Staleness is decided by comparing current file text against those snapshots, not by inspecting Git history.
- **It is experimental and opt-in.** Reviewing is not part of the default note-writing flow, and reviews are not always-on checks. You invoke the system deliberately when you want a note judged.

Storing review state in SQLite is a scoped exception to the repo's file-first design; [ADR-010](./adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md) records why. This document covers how to operate the system; for how it is built, see [review architecture](./review-architecture.md).

## How a review flows

A full review runs as a short pipeline, from a stale-pair query to a durable acceptance:

1. **Select** — the selector lists `(note, criterion)` pairs that are stale or unreviewed for a given model partition, and says why. Persisted and JSON identities remain `(note_path, gate_path)`.
2. **Create jobs** — selected pairs are packed into one or more queued *review jobs*, each with its own rendered prompt.
3. **Review** — a worker (typically a sub-agent) reads a job's prompt and writes a single sentinel-delimited `bundle-output.md`.
4. **Finalize** — the parent parses that output against each pair's persisted result contract and, only if every expected pair is present and well-formed, records completion and upserts accepted baselines.

Acceptance is the durable freshness baseline. A current acceptance row pins the exact note and criterion text that was reviewed, so the selector can later tell whether either side has drifted. It is not a universal endorsement: a verdict acceptance records a bounded gate outcome, while a report acceptance records that the retained report matches the pinned inputs. When a change does not invalidate that evidence, an acceptance can be carried forward without a fresh run (*ack*).

## Concepts

**Assay.** Any snapshot-anchored LLM evaluation executed through selector → job → worker → finalizer. An assay is classified by its result kind. Verdict-kind assays are bounded checks; report-kind assays produce reusable analysis without deciding the note.

**Gate.** A bounded, verdict-kind assay criterion. Catalog gates are markdown files at `kb/instructions/review-gates/{lens}/{name}.md` in a source checkout, or under the installed framework gate catalog in generated projects. The `{lens}/{name}` shorthand is the gate id used at the CLI boundary (for example `prose/source-residue`). Type- and collection-conformance pairs are virtual gates whose criterion files are the type spec and `COLLECTION.md`.

**Criterion.** The instruction text applied to the note. It occupies the persisted `gate_path` side of every pair, including report assays. “Gate” remains in schema and CLI identifiers because the pair mechanism was built for gates; prose uses “criterion” when the statement includes non-gate assays.

**Bundle.** A directory of gates sharing a lens. `semantic` means all gate files under `kb/instructions/review-gates/semantic/`.

**Type-conformance pair.** A review of a note against the type spec named by its frontmatter `type:` — the type spec *is* the gate ([ADR 038](./adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md)). Request it with the virtual `type` lens: `type` derives one pair per typed note in scope, `type/definition` narrows to one type's cohort. The gate id is `type/{name}`; the persisted gate identity is the type-spec path (for example `kb/types/definition.md`). Because the type spec sits on the gate side, editing it stales exactly the notes of that type as `gate-changed`, and a trivial type edit is acknowledged like any other gate edit. `--all-gates` includes type-conformance pairs alongside the catalog; request them alone via the `type` lens. The rendered prompt carries a fixed conformance instruction that references the type spec by path — the reviewer reads the spec from disk instead of receiving it packed into the prompt; if a type spec carries an authored `## Review` section, reviewers treat it as the operative test.

**Collection-conformance pair.** A review of a note against the `COLLECTION.md` contract of the collection it lives in — the contract *is* the gate ([ADR 041](./adr/041-collection-conformance-reviews-use-collection-md-as-the-gate.md)). Request it with the virtual `collection` lens: `collection` derives one pair per in-collection note in scope, `collection/notes` narrows to one collection's cohort (the path segment is the collection directory relative to `kb/`, so a collection under a namespace directory reads `collection/commonplace/notes`). The persisted gate identity is the COLLECTION.md path (for example `kb/notes/COLLECTION.md`). Editing a collection contract stales exactly that collection's notes as `gate-changed`; `--all-gates` includes collection-conformance pairs. The prompt mechanics mirror the type pair — the contract is referenced by path and read from disk, an authored `## Review` section in the COLLECTION.md is the operative test, and the reviewer judges only what the collection contract asks beyond the type contract, so the two conformance pairs do not double-flag.

**Review job.** One review invocation: one rendered prompt, one output artifact directory, and one job-level status. A job is `queued` until finalization marks it `completed` or `failed`.

**Review pair.** One requested `(note_path, gate_path)` pair inside a review job. This is the unit of output and acceptance. Its persisted `result_kind` is `verdict` or `report`; report pairs complete with `decision = NULL`.

**Result kind.** The persisted output contract fixed when the pair is created. A `verdict` pair completes with `reviewed_at` plus one decision (`pass`, `warn`, `fail`, `error`). A `report` pair completes with `reviewed_at`, a null decision, and `## Result: REPORT`. Completion and decision are separate facts.

**Critique pair.** Request the virtual `critique` lens for one report-kind pair per explicitly targeted note. Its persisted gate identity is `kb/instructions/critique-note.md` (or the installed framework equivalent), so editing that instruction yields `gate-changed`. It is intentionally excluded from `--all-gates`.

**Acceptance row.** The current record that a `(note_path, gate_path, model_partition)` key completed against specific note and criterion text. Acceptance makes the evidence fresh; it does not imply that report findings were handled or that the note is globally approved.

**Model partition.** Reviews are partitioned by model. A review or acceptance under one model does not satisfy freshness for another. A partition is a named bucket (`claude-opus`, `claude-opus-4.8`, `codex`) that groups concrete model IDs judged equivalent for review freshness — it is the review-identity key, not the literal model that ran. Concrete model IDs map into partitions through `MODEL_PARTITION_REGISTRY` in `src/commonplace/review/review_model.py` (`build_model_partition`). The CLI flag names carry the distinction: every partition-valued flag is `--model-partition`; the only `--model` flag in the review CLI is `commonplace-finalize-review-job`'s, which records the concrete worker model and is validated to map into the job's partition.

Human-readable review output — the per-pair result files and each job's `MANIFEST.json` — is for inspection. SQLite `result_kind`, `decision`, `reviewed_at`, acceptance, and job status are canonical state; see [review architecture](./review-architecture.md) for storage details.

### Semantic boundaries

| Do not conflate | Distinction |
|---|---|
| assay and gate | An assay is any snapshot-anchored evaluation; a gate is the bounded verdict-kind subset. |
| criterion and `gate_path` | Criterion is the concept; `gate_path` is the historical schema field that stores its identity. |
| completion and decision | Both result kinds complete; only verdict pairs carry a decision. |
| acceptance and endorsement | Acceptance pins current evidence to snapshots. It does not approve a note or resolve report findings. |
| freshness and handling | Fresh means the evidence matches current inputs. Handling findings is a separate downstream action. |
| `REPORT` and a verdict | `REPORT` is a protocol completion marker, not a fifth decision. |

## Reading freshness

The selector reports each requested `(note, criterion)` pair as fresh or, if not, why it is stale. The JSON and schema retain `gate_*` field names. Selection compares the current note file, current criterion file, and current acceptance for the persisted key.

- no acceptance for the pair → `missing-review`
- accepted note or gate snapshot is missing → `missing-review`
- accepted gate text differs from the current gate → `gate-changed`
- accepted note text differs from the current note → `note-changed`
- otherwise the pair is fresh

For `note-changed` pairs, the selector can show the diff against the accepted note text, so you can judge whether the change invalidates that assay's evidence.

## Running a review batch

The full procedure is in [run review batches](../instructions/run-review-batches.md). In outline:

1. Select stale pairs and create jobs:

   ```
   commonplace-review-target-selector ... --json | commonplace-create-review-jobs --input - --grouping {note|gate}
   ```

   `--grouping note` packs one note's pairs by bundle; `--grouping gate` packs one shared criterion across notes. The option name is historical schema vocabulary. Jobs are always result-kind homogeneous.

2. For each job, launch a sub-agent that reads the job's `prompt_path` and writes its review to the job's `bundle_output_path`.

3. Finalize each completed output with `commonplace-finalize-review-job` (signature under [Command reference](#command-reference)).

**Finalization is all-or-nothing.** If any expected pair is missing, duplicated, unexpected, malformed, or lacks a valid result line, the job fails and writes no acceptance rows — a failed job accepts nothing. On success, every pair records per-kind completion and the current acceptance row for each pair is upserted.

**Finalization-time provenance is optional.** When supplied, `--model` (with optional `--effort`) is validated against the job's model partition before any state changes, and the runner/model/effort are recorded. `--effort` requires `--model`. `--telemetry-json` stores opaque harness telemetry without making it review identity.

## Acknowledging trivial changes

For a `note-changed` pair, inspect the selector diff first. If the change does not invalidate the existing evidence, acknowledge it instead of rerunning. For a verdict pair this carries a bounded decision; for a report pair it only reuses the report as current evidence and endorses nothing.

`commonplace-ack-gate-review` advances the accepted baseline when a note changed but not in a way that matters for the criterion. It carries the existing evidence forward: it records the current note and criterion text as newly accepted, pointing at the completed review pair being reused. It does not rewrite any file or assay prose. The command name and arguments retain gate vocabulary.

```
commonplace-ack-gate-review --model-partition {model-partition} {note_path} {gate_id}...
```

Ack fails when there is no completed review for the same `(note_path, gate_path, model_partition)` — there must be existing review evidence to carry forward. Output lines have the form `acked: <note_path> <gate_id>`.

## Building a warn/fix queue

`commonplace-warn-selector` builds a fixing queue from the current review state — the actionable findings from reviews whose decision is `warn`. It is the entry point to the [fix system](../instructions/FIX-SYSTEM.md), which turns these findings into applied corrections and fix reports.

- it reads current accepted review pairs across all models
- it loads each review's rationale text from the accepted pair's result file (unavailable if the file is missing)
- it skips findings whose gate changed since acceptance
- it collapses model partitions to one current entry per `(note_path, gate_path)`, choosing the latest accepted warn review

## Interpreting review output

A `pass` records that a bounded gate found nothing to flag. It is not certification that the note has no problems. `REPORT` is not a fifth decision: it says the report protocol completed. A fresh critique means the critique matches the current inputs, not “critiqued and handled.”

The same principle applies once a `warn` finding is delegated to the fix system. When the fix produces a diff, reviewing that diff is the judgment step: it checks the resulting artifact directly, rather than trusting the fixing agent's own report of success. Reading the agent's self-report still matters when no diff results — there is no artifact to substitute for it, so that case still needs the claim read directly.

Unbounded methods therefore remain report-shaped rather than being forced into gate decisions. The anchored critique uses report-kind completion; the unanchored [composition friction gate](../instructions/composition-friction-gate.md) routes attention without entering the acceptance store.

## Command reference

**Selector** — `commonplace-review-target-selector`:

- positional gate ids, bundle names, conformance requests, and/or `critique` (e.g. `prose`, `semantic/grounding-alignment`, `type`, `collection/notes`, `critique`)
- `--all-gates` selects every applicable verdict criterion in place of naming ids/bundles (mutually exclusive with them): all catalog gates plus each note's type-conformance and collection-conformance pairs. It intentionally excludes report assays. Like every selector flag it only *chooses* pairs — the selected pairs still run through create-jobs → worker → finalize; it is not a one-shot "run all gates" command
- `--note` to filter to specific note paths or directories
- `--current` to filter to notes with `status: current`
- `--model-partition {model-partition}` selects the review model partition to inspect or write; omit it only for model-agnostic missing-review coverage
- `--json`
- `--reason {missing-review,gate-changed,note-changed}`

With `--model-partition` omitted, the selector reports only model-agnostic missing-review coverage: a pair is `missing-review` only when there is no acceptance under any model partition. It does not classify `gate-changed` or `note-changed` in that mode, because those need a chosen baseline.

**Create jobs** — `commonplace-create-review-jobs --input - --grouping {note|gate}`. Consumes selector JSON.

**Finalize** — `commonplace-finalize-review-job --review-job-id {id} [--runner {worker}] [--model {model} [--effort {effort}]] [--telemetry-json {json}]`.

**Ack** — `commonplace-ack-gate-review --model-partition {model-partition} {note_path} {gate_id}...`.

**Warn queue** — `commonplace-warn-selector`.

## The reviewer output contract

A worker writes one sentinel-delimited `bundle-output.md` covering every pair in the result-kind-homogeneous job. Verdict blocks end in a decision marker; report blocks end in `REPORT`:

```text
## Result: PASS
## Result: WARN
## Result: FAIL
## Result: ERROR
## Result: REPORT
```

`REPORT` is a completion marker, not a decision. `INFO` may label a non-actionable finding inside verdict prose but is not a valid final decision. Aliases such as `Verdict`, `Outcome`, `OK`, and `UNKNOWN` are invalid. The worker writes only the bundle output file; it does not touch notes, criteria, indexes, or the review database.

## Authoring a gate

Gates are typed `kb/types/review-gate.md`. See [that type spec](../types/review-gate.md) for the frontmatter and body contract, and `kb/instructions/review-gates/` for examples. This document covers runtime concepts (bundles, freshness, acceptance, the batch workflow); the type owns the authored shape of a gate.
