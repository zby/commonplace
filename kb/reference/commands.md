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

Initialize or update a Commonplace project. Creates KB directories, seeds instructions and type definitions, attempts known `.claude/skills/` and `.agents/skills/` projections for shipped skills, and resolves templates. If those optional projections cannot be created, other runtimes can still expose the canonical `kb/commonplace/instructions/cp-skill-*` directories through their own skill mechanism.

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

The review system runs LLM-based quality reviews against notes using defined review gates. For the full review workflow, read [REVIEW-SYSTEM.md](./REVIEW-SYSTEM.md). For the code architecture, see [review-architecture.md](./review-architecture.md).

### commonplace-review-sweep

Run a full review sweep — selects notes needing review and runs gate bundles on them.

```bash
commonplace-review-sweep prose kb/notes kb/reference --model claude-opus-4-6 --runner claude-code
commonplace-review-sweep prose --model claude-opus-4-6 --runner claude-code --current   # only current-status notes
commonplace-review-sweep --all-gates kb/notes kb/reference --model claude-opus-4-6 --runner claude-code       # all gate bundles
commonplace-review-sweep prose kb/notes kb/reference --model claude-opus-4-6 --runner claude-code --dry-run   # preview what would run
```

### commonplace-run-review-bundle

Run a review bundle (set of gates) on a single note.

```bash
commonplace-run-review-bundle kb/notes/my-note.md prose --runner claude-code --model claude-opus-4-6
```

### commonplace-run-gate-sweep

Run a single gate across multiple notes in batched prompts.

```bash
commonplace-run-gate-sweep semantic/grounding-alignment --runner claude-code --model claude-opus-4-6 --note kb/notes kb/reference
commonplace-run-gate-sweep semantic/grounding-alignment --runner claude-code --model claude-opus-4-6 --current --batch-size 5
commonplace-run-gate-sweep semantic/grounding-alignment --runner claude-code --model claude-opus-4-6 --note kb/notes/specific.md
commonplace-run-gate-sweep semantic/grounding-alignment --runner claude-code --model claude-opus-4-6 --note kb/notes kb/reference --dry-run
```

### commonplace-create-review-run

Create a review run record in the review database. With `--with-prompt`, also emits the canonical bundle prompt, `MANIFEST.json`, and artifact paths for live-agent review.

```bash
commonplace-create-review-run kb/notes/my-note.md prose --runner claude-code --model claude-opus-4-6
commonplace-create-review-run kb/notes/my-note.md prose --runner claude-code --model claude-opus-4-6 --json
commonplace-create-review-run kb/notes/my-note.md prose --runner claude-code --model claude-opus-4-6 --with-prompt
```

The `--with-prompt` JSON payload includes `prompt_path`, `bundle_output_path`, and `manifest_path`. The manifest lists each pair and its packing-derived `result_path`; note-packed runs use gate filenames such as `prose__source-residue.md`.

### commonplace-ingest-bundle-output

Parse a sentinel-delimited review bundle and finalize its existing review run.

```bash
commonplace-ingest-bundle-output --review-run-id 42 --input-file kb/reports/bundle-reviews/review-run-42/bundle-output.md
```

### commonplace-prepare-review-batch

Create one review run for a note-packed or gate-packed set of `(note, gate)` pairs and render one batch prompt for an external executor (live agent or orchestrator). Returns `review_run_id`, per-pair metadata, skipped pairs, and artifact paths, including `manifest_path`, as JSON.

```bash
commonplace-prepare-review-batch kb/notes/a.md::prose/source-residue kb/notes/b.md::prose/source-residue --runner live-agent --model claude-opus-4-6
```

### commonplace-ingest-batch-output

Parse a batch's pair-delimited output and finalize its review run with pair salvage. Completed pairs are stored and accepted; missing pairs are marked `missing`, and the run fails with run-level failure context. Exit 1 if the run failed.

```bash
commonplace-ingest-batch-output --review-run-id 42 --input-file kb/reports/bundle-reviews/review-run-42/bundle-output.md
```

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

List stale (note, gate) pairs that need review. Compares current note/gate SHAs against accepted SHAs.

```bash
commonplace-review-target-selector prose --model claude-opus-4-6 --note kb/notes kb/reference
commonplace-review-target-selector prose --model claude-opus-4-6 --current --json          # JSON output
commonplace-review-target-selector prose --model claude-opus-4-6 --note kb/notes kb/reference --reason note-changed     # filter by staleness reason
commonplace-review-target-selector prose --note kb/notes kb/reference --reason missing-review     # pairs missing under every model partition
commonplace-review-target-selector prose --model claude-opus-4-6 --ack kb/notes/foo.md:prose/source-residue   # ack a pair
```

### commonplace-warn-selector

Extract warn-level findings from effective reviews.

```bash
commonplace-warn-selector                                          # all notes
commonplace-warn-selector kb/notes/my-note.md                     # specific note
commonplace-warn-selector --json                                   # JSON output
```

## Review maintenance

Operational commands for database repair and cleanup.

### commonplace-prune-superseded-reviews

Delete superseded non-current review-pair rows and whole run artifact directories when every pair in the run is obsolete. It does not delete individual files from a retained shared run directory.

```bash
commonplace-prune-superseded-reviews --dry-run
commonplace-prune-superseded-reviews --apply
```

### commonplace-repair-model-partitions

Collapse known model aliases in review runs, review pairs, and acceptance events.

```bash
commonplace-repair-model-partitions --dry-run
```
