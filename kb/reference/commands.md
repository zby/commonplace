---
description: Reference for the commonplace-* CLI commands shipped by llm-commonplace - project setup, validation, indexing, snapshots, note operations, and the review system
type: kb/types/note.md
tags: []
---

# Commonplace CLI commands

All commands are installed by `pip install llm-commonplace` and available as `commonplace-*` on PATH. Run any command with `--help` for full usage.

## Project setup

### commonplace-init

Initialize or update a Commonplace project. Creates KB directories, seeds instructions and type definitions, copies shipped skills into the known `.claude/skills/` and `.agents/skills/` runtime layouts, and resolves templates. Runtimes with a different skill-discovery surface can expose the canonical `kb/commonplace/instructions/cp-skill-*` directories through their own skill mechanism.

```bash
commonplace-init --name <project-name>
commonplace-init --root /path/to/project
```

`--name` sets the project name for templates (defaults to directory name). Safe to rerun — never overwrites existing files, and reports whether preserved files already match the scaffold or differ from what the current run would generate.

## Validation and indexing

### commonplace-validate

Deterministic validator for KB notes. Checks frontmatter validity, schema constraints, link health, verbatim-quote resolution, structural description presence, description length warnings, required sections, and batch signals such as orphan detection. Description discrimination quality is handled by review gates, not deterministic validation.

Findings are labelled with the source that produced them — `[base]` (every typed note), `[type: <name>]` (rules the type owns), `[schema]` (the type's declarative constraints). What each source can express, and what every typed note is checked for regardless of type, is the [validation contract](./validation-contract.md).

```bash
commonplace-validate notes               # validate one collection by name
commonplace-validate types               # validate every global and collection-local type spec
commonplace-validate kb/notes/           # validate one collection by path
commonplace-validate kb/notes/my-note.md # validate one note
```

Bare `kb` and `all` are rejected — scope must be a specific collection or file. To validate the authored library, loop over the collections explicitly:

```bash
for c in types notes reference instructions agent-memory-systems sources; do
  commonplace-validate "$c"
done
```

### Generated indexes (no command)

Complete generated listings — per-collection `dir-index.md` pages and per-tag generated tails — are not committed and have no rebuild command. The mkdocs hook (`src/commonplace/docs/mkdocs_hooks.py`) materializes them in-memory at build time for the published site (ADR 025); `mkdocs build` is the only way to produce them. Agents enumerate candidates with the scoped `rg` recipes in [navigation.md](./navigation.md). The retired commands `commonplace-refresh-indexes`, `commonplace-sync-generated-index`, and `commonplace-generate-notes-index` no longer exist.

## Note operations

### commonplace-guard-full-pass-report

Compare every packet-owned capture named by one full-pass report with its current logical artifact. The command always emits JSON with one `matching`, `changed`, `missing`, or `corrupt-capture` result per guarded input; changed results include a capture-to-current unified diff.

```bash
commonplace-guard-full-pass-report kb/reports/full-pass/my-note/<pass-id>/full-pass-report.md
```

Exit 0 only when every input matches. Exit 1 is a valid guard refusal. Exit 2 means the report or invocation is invalid. The command never mutates the report or live artifacts.

### commonplace-relocate-note

Rename or move a note, updating all backlinks across the KB.

```bash
commonplace-relocate-note old-note "New note title" --apply
commonplace-relocate-note old-note --to kb/notes/definitions --apply
commonplace-relocate-note old-note --to kb/notes/new-path.md --apply
```

Without `--apply`, previews changes without writing.

### commonplace-relocate-directory

Move a KB directory, updating links and optionally adding one MkDocs redirect.

```bash
commonplace-relocate-directory kb/notes/related-systems kb/agent-memory-systems --apply
commonplace-relocate-directory kb/notes/related-systems kb/agent-memory-systems --redirect notes/related-systems/related-systems-index.md:agent-memory-systems/index.md --apply
```

Without `--apply`, previews changes without writing. `--redirect` takes `OLD:NEW` docs paths for a single redirect entry.

### commonplace-promotion-candidates

List unstructured text files ranked by incoming links so operators can decide which captures are worth structuring. The report separately surfaces files whose opened frontmatter cannot be parsed; they are invalid notes, not text candidates.

```bash
commonplace-promotion-candidates
```

Writes results to `kb/reports/promotion-candidates.md`.

## Snapshots

### commonplace-github-snapshot

Snapshot a GitHub issue or PR into `kb/sources/`. Uses the `gh` CLI to fetch issue/PR data.

```bash
commonplace-github-snapshot https://github.com/owner/repo/issues/123
commonplace-github-snapshot --out-dir kb/sources/ https://github.com/owner/repo/pull/456
```

### commonplace-x-snapshot

Snapshot an X/Twitter post into `kb/sources/`. Requires the `xdk` package (`pip install llm-commonplace[snapshot]`).

```bash
commonplace-x-snapshot https://x.com/user/status/123456789
```

## Review system

The review system executes snapshot-anchored LLM assays against notes. Closed-ended review gates produce verdicts; open-ended assays such as critique record reports without an outcome. The persisted criterion field remains named `criterion_path`. For the vocabulary and full workflow, read [README-REVIEW-SYSTEM.md](./README-REVIEW-SYSTEM.md). For the code architecture, see [review-architecture.md](./review-architecture.md).

Model flags: every partition-valued flag below is `--model-partition` and takes a partition name such as `claude-opus` or `codex` (the review-freshness key; registry in `src/commonplace/review/review_model.py`). The only `--model` flag is `commonplace-finalize-review-job`'s, which takes the concrete model the worker reported (for example `claude-fable-5`) and validates that it maps into the job's partition.

### commonplace-create-review-jobs

Create one or more queued review job records in the review database and write their canonical prompts and `MANIFEST.json` files for live-agent review. Artifact paths are derived from the job id and pair set. Creation is runner-agnostic: `runner`, `runner_model`, and `runner_effort` stay null until execution.

```bash
commonplace-review-target-selector --mode requested --json --model-partition claude-opus accessibility prose semantic --note kb/notes/my-note.md \
  | commonplace-create-review-jobs --input - --grouping note
commonplace-review-target-selector --json --model-partition claude-opus prose --note kb/notes/my-note.md \
  | commonplace-create-review-jobs --input - --grouping note
```

The canonical path is selector JSON piped into `--input -`. The command prints a JSON payload with `input_mode`, `model_partition`, `grouping`, `jobs`, and `skipped_pairs`. Each result-kind-homogeneous job includes `review_job_id`, `status`, nullable runner provenance, `grouping`, derived `prompt_path`, derived `job_output_path`, and pair rows with `criterion_id`, `result_kind`, nullable `outcome`, nullable `completed_at`, and derived `result_path`. `MANIFEST.json` is display/debug output written beside the artifacts, not a returned JSON field; pipeline commands use derived job paths as state. Note-grouped jobs use criterion-leaf filenames such as `source-residue.md`; criterion-grouped jobs use note filenames such as `my-note.md`.

### commonplace-review-job-list

List review jobs and their pair rows.

```bash
commonplace-review-job-list --status queued --json
commonplace-review-job-list --model-partition claude-opus
```

### commonplace-finalize-review-job

Finalize a queued review job from its derived job output path. The command strictly parses all expected pair blocks, writes per-pair result files, records completion under each pair's persisted result kind, creates or replaces freshness baselines, prunes superseded review evidence, and moves the job to `completed` in one successful finalization. Verdict pairs record an outcome; report pairs retain a null outcome and complete via `completed_at`. `ERROR`, missing, duplicate, unexpected, malformed, or result-less pair blocks fail the whole job and write no freshness baseline rows. Exit 1 if the job failed or if a precondition fails before state changes.

```bash
commonplace-finalize-review-job --review-job-id 42
commonplace-finalize-review-job --review-job-id 42 --runner codex
commonplace-finalize-review-job --review-job-id 42 --runner codex --model gpt-5 --effort high
```

Optional provenance flags are recorded at finalization time. `--runner` may be supplied alone. `--model` may be supplied without `--runner`; it validates `build_model_partition(--model, --effort)` against the job's `model_partition` before state changes. `--effort` requires `--model`. `--telemetry-json` records an opaque harness-provided telemetry blob without interpreting it.

The command accepts `queued` jobs, rejects `completed` and `failed`, reads the job-owned `job-output.md`, writes per-pair result files to derived result paths with provenance frontmatter, refreshes `MANIFEST.json` for inspection, and prints JSON for success, mutated failure, and precondition failure. Result-file write failures are fatal evidence failures. Manifest refresh failures after DB completion do not fail the job; they are returned in an optional top-level `warnings` array.

### commonplace-freshness-status

Report repository-wide freshness for registered targets. v1 covers migrated `review-pair` targets only. Exit `0` when all selected targets are fresh, `1` when any input changed or is missing, `2` on misuse or store errors.

```bash
commonplace-freshness-status --json
commonplace-freshness-status --all --json --model-partition codex
commonplace-freshness-status --json --diff
```

### commonplace-freshness-accept

Observation refresh or initial acceptance for non-review targets. Rejects `review-pair` in v1 — review capture finalization owns those targets.

```bash
commonplace-freshness-accept --input manifest.json
```

### commonplace-freshness-ack

Acknowledge changed inputs for a registered target from a status-derived manifest. Review-pair targets preserve evidence automatically.

```bash
commonplace-freshness-ack --input ack.json
```

### commonplace-freshness-retire

Remove a registered baseline when an artifact or target should leave global status. Idempotent when the target is already absent.

```bash
commonplace-freshness-retire --input retire.json
```

### commonplace-ack-review

Advance an existing freshness baseline for specific criteria without re-running the assay. For report pairs this reuses current evidence; it does not endorse or resolve the report.

```bash
commonplace-ack-review kb/notes/my-note.md --model-partition claude-opus prose/source-residue semantic/grounding-alignment
```

### commonplace-ack-trivial-note-changes

Auto-acknowledge `note-changed` stale pairs when only non-watched note parts changed. Each gate declares what it watches (body, title, description) — changes outside the watched set are acked automatically. Conformance pairs may be selected (`type`/`collection` requests or `--all-gates`) but never qualify: neither a type spec nor a COLLECTION.md declares watches, so each watches the whole note and no change is trivial against it.

Running this command is the explicit human-authorized trivial-change workflow under which an existing `user-verified: true` may be preserved. It advances review freshness only; it never adds or computes user verification.

```bash
commonplace-ack-trivial-note-changes prose --model-partition claude-opus --note kb/notes kb/reference  # all prose gates
commonplace-ack-trivial-note-changes prose --model-partition claude-opus --user-verified        # committed user-verified notes only
commonplace-ack-trivial-note-changes prose --model-partition claude-opus --note kb/notes kb/reference --dry-run  # preview what would ack
```

### commonplace-resolve-criteria

Resolve criterion requests and output their definitions. Catalog bundle names expand to individual gate IDs; concrete `type/{name}`, `collection/{path}`, and `critique` requests resolve to their criterion documents. Broad `type` and `collection` lenses require note scope and belong at the selector boundary.

```bash
commonplace-resolve-criteria prose                                    # all gates in prose bundle
commonplace-resolve-criteria prose/source-residue semantic/grounding-alignment  # specific gates
commonplace-resolve-criteria critique                                 # report-kind critique criterion
```

### commonplace-review-target-selector

List assay target pairs. Default mode lists stale `(note, criterion)` pairs by comparing current note/criterion text hashes against baseline DB snapshots. JSON and schema fields use `criterion_*` names. `--mode requested` emits the explicitly requested applicable pairs without checking freshness, for piping into `commonplace-create-review-jobs --input -`.

Besides catalog gate ids and bundles, the selector accepts conformance requests and the report-kind `critique` assay. Type-conformance: `type` derives one pair per typed note in scope with the note's type spec as the criterion, `type/{name}` narrows to one type's cohort. Collection-conformance: `collection` derives one pair per in-collection note with the collection's COLLECTION.md as the criterion, `collection/{path}` narrows to one collection's cohort (path relative to `kb/`, e.g. `collection/notes`). `--all-gates` selects all applicable verdict criteria — catalog gates plus both conformance pairs — and intentionally excludes heavyweight report assays. Jobs created from selector output are result-kind homogeneous.

```bash
commonplace-review-target-selector prose --model-partition claude-opus --note kb/notes kb/reference
commonplace-review-target-selector prose --model-partition claude-opus --user-verified --json    # JSON output
commonplace-review-target-selector prose --model-partition claude-opus --note kb/notes kb/reference --reason note-changed     # filter by staleness reason
commonplace-review-target-selector prose --note kb/notes kb/reference --reason missing-baseline     # pairs missing under every model partition
commonplace-review-target-selector --mode requested prose --model-partition claude-opus --note kb/notes/my-note.md --json
commonplace-review-target-selector type/definition --model-partition claude-opus --user-verified  # type-conformance pairs for one type's verified cohort
commonplace-review-target-selector collection/notes --model-partition claude-opus --user-verified # collection-conformance pairs for one collection's verified cohort
commonplace-review-target-selector critique --model-partition claude-opus --note kb/notes/my-note.md  # report-kind critique pair
```

### commonplace-warn-selector

Extract warn-level findings from effective reviews.

```bash
commonplace-warn-selector                                          # all notes
commonplace-warn-selector kb/notes/my-note.md                     # specific note
commonplace-warn-selector --json                                   # JSON output
```
