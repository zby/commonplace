---
description: Reference for the commonplace-* CLI commands shipped by llm-commonplace - project setup, validation, indexing, snapshots, note operations, and the review system
type: kb/types/note.md
tags: []
status: current
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

Deterministic validator for KB notes. Checks frontmatter validity, enum values, link health, structural description presence, description length warnings, required sections, and batch signals (orphan detection, seedling counts). Description discrimination quality is handled by review gates, not deterministic validation.

```bash
commonplace-validate notes               # validate one collection by name
commonplace-validate kb/notes/           # validate one collection by path
commonplace-validate kb/notes/my-note.md # validate one note
```

Bare `kb` and `all` are rejected — scope must be a specific collection or file. To validate the authored library, loop over the collections explicitly:

```bash
for c in notes reference instructions agent-memory-systems sources; do
  commonplace-validate "$c"
done
```

### Generated indexes (no command)

Complete generated listings — per-collection `dir-index.md` pages and per-tag generated tails — are not committed and have no rebuild command. The mkdocs hook (`src/commonplace/docs/mkdocs_hooks.py`) materializes them in-memory at build time for the published site (ADR 025); `mkdocs build` is the only way to produce them. Agents enumerate candidates with the scoped `rg` recipes in [navigation.md](./navigation.md). The retired commands `commonplace-refresh-indexes`, `commonplace-sync-generated-index`, and `commonplace-generate-notes-index` no longer exist.

## Note operations

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

List text files and seedling notes that may be ready for promotion to higher status.

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

The review system executes LLM-based quality reviews against notes using defined review gates. For the full review workflow, read [README-REVIEW-SYSTEM.md](./README-REVIEW-SYSTEM.md). For the code architecture, see [review-architecture.md](./review-architecture.md).

### commonplace-create-review-jobs

Create one or more queued review job records in the review database and write their canonical prompts and `MANIFEST.json` files for live-agent review. Artifact paths are derived from the job id and pair set. Creation is runner-agnostic: `runner`, `runner_model`, and `runner_effort` stay null until execution.

```bash
commonplace-review-target-selector --mode requested --json --model claude-opus-4-6 accessibility prose semantic --note kb/notes/my-note.md \
  | commonplace-create-review-jobs --input - --grouping note
commonplace-review-target-selector --json --model claude-opus-4-6 prose --note kb/notes/my-note.md \
  | commonplace-create-review-jobs --input - --grouping note
```

The canonical path is selector JSON piped into `--input -`. The command prints a JSON payload with `input_mode`, `model_partition`, `grouping`, `jobs`, and `skipped_pairs`. Each job includes `review_job_id`, `status`, nullable runner provenance, `packing`, derived `prompt_path`, derived `bundle_output_path`, and pair rows with `gate_id`, `decision`, and derived `result_path`. `MANIFEST.json` is display/debug output written beside the artifacts, not a returned JSON field; pipeline commands use derived job paths as state. Note-packed jobs use gate-leaf filenames such as `source-residue.md`; gate-packed jobs use note filenames such as `my-note.md`.

### commonplace-review-job-list

List review jobs and their pair rows.

```bash
commonplace-review-job-list --status queued --json
commonplace-review-job-list --model claude-opus-4-6
```

### commonplace-finalize-review-job

Finalize a queued review job from its derived bundle output path. The command strictly parses all expected pair blocks, writes per-pair result files, records decisions, upserts accepted baselines, prunes superseded review evidence, and moves the job to `completed` in one successful finalization. Missing, duplicate, unexpected, malformed, or result-less pair blocks fail the whole job and write no acceptance rows. Exit 1 if the job failed or if a precondition fails before state changes.

```bash
commonplace-finalize-review-job --review-job-id 42
commonplace-finalize-review-job --review-job-id 42 --runner codex
commonplace-finalize-review-job --review-job-id 42 --runner codex --model gpt-5 --effort high
```

Optional provenance flags are recorded at finalization time. `--runner` may be supplied alone. `--model` may be supplied without `--runner`; it validates `build_model_partition(--model, --effort)` against the job's `model_partition` before state changes. `--effort` requires `--model`. `--telemetry-json` records an opaque harness-provided telemetry blob without interpreting it.

The command accepts `queued` jobs, rejects `completed` and `failed`, reads the job-owned `bundle-output.md`, writes per-pair result files to derived result paths with provenance frontmatter, refreshes `MANIFEST.json` for inspection, and prints JSON for success, mutated failure, and precondition failure. Result-file write failures are fatal evidence failures. Manifest refresh failures after DB completion do not fail the job; they are returned in an optional top-level `warnings` array.

### commonplace-ack-gate-review

Advance acceptance baseline for specific gates without re-running the review.

```bash
commonplace-ack-gate-review kb/notes/my-note.md --model claude-opus-4-6 prose/source-residue semantic/grounding-alignment
```

### commonplace-ack-trivial-note-changes

Auto-acknowledge `note-changed` stale pairs when only non-watched note parts changed. Each gate declares what it watches (body, title, description) — changes outside the watched set are acked automatically.

```bash
commonplace-ack-trivial-note-changes prose --model claude-opus-4-6 --note kb/notes kb/reference  # all prose gates
commonplace-ack-trivial-note-changes prose --model claude-opus-4-6 --current              # current-status notes only
commonplace-ack-trivial-note-changes prose --model claude-opus-4-6 --note kb/notes kb/reference --dry-run  # preview what would ack
```

### commonplace-resolve-gates

Expand gate bundle names to individual gate IDs and output their definitions.

```bash
commonplace-resolve-gates prose                                    # all gates in prose bundle
commonplace-resolve-gates prose/source-residue semantic/grounding-alignment  # specific gates
```

### commonplace-review-target-selector

List review target pairs. Default mode lists stale `(note, gate)` pairs by comparing current note/gate text hashes against accepted DB snapshots. `--mode requested` emits the explicitly requested applicable pairs without checking freshness, for piping into `commonplace-create-review-jobs --input -`.

```bash
commonplace-review-target-selector prose --model claude-opus-4-6 --note kb/notes kb/reference
commonplace-review-target-selector prose --model claude-opus-4-6 --current --json          # JSON output
commonplace-review-target-selector prose --model claude-opus-4-6 --note kb/notes kb/reference --reason note-changed     # filter by staleness reason
commonplace-review-target-selector prose --note kb/notes kb/reference --reason missing-review     # pairs missing under every model partition
commonplace-review-target-selector --mode requested prose --model claude-opus-4-6 --note kb/notes/my-note.md --json
```

### commonplace-warn-selector

Extract warn-level findings from effective reviews.

```bash
commonplace-warn-selector                                          # all notes
commonplace-warn-selector kb/notes/my-note.md                     # specific note
commonplace-warn-selector --json                                   # JSON output
```
