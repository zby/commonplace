# Commonplace CLI Commands

All commands are installed by `pip install llm-commonplace` and available as `commonplace-*` on PATH. Run any command with `--help` for full usage.

## Project setup

### commonplace-init

Initialize or update a Commonplace project. Creates KB directories, seeds instructions and type definitions, installs skills into both `.claude/skills/` and `.agents/skills/`, and resolves templates.

```bash
commonplace-init --name <project-name>
commonplace-init --root /path/to/project
```

`--name` sets the project name for templates (defaults to directory name). Safe to rerun — never overwrites existing files, and reports whether preserved files already match the scaffold or differ from what the current run would generate.

## Validation and indexing

### commonplace-validate-notes

Deterministic validator for KB notes. Checks frontmatter validity, enum values, link health, description quality, required sections, and batch signals (orphan detection, seedling counts).

```bash
commonplace-validate-notes kb/notes/          # validate all notes
commonplace-validate-notes kb/notes/my-note.md  # validate one note
```

### commonplace-generate-notes-index

Generate an `index.md` file from frontmatter of all markdown files in a directory. Lists each note with its description.

```bash
commonplace-generate-notes-index kb/notes
commonplace-generate-notes-index kb/sources
```

### commonplace-sync-generated-index

Rebuild auto-generated sections of tag index pages. Scans notes for matching tags and updates the generated listings.

```bash
commonplace-sync-generated-index                           # all indexes
commonplace-sync-generated-index kb/notes/tags-index.md    # specific index
commonplace-sync-generated-index --dry-run                 # preview changes
```

## Note operations

### commonplace-relocate-note

Rename or move a note, updating all backlinks across the KB.

```bash
commonplace-relocate-note old-note "New note title" --apply
commonplace-relocate-note old-note --dir kb/notes/definitions --apply
commonplace-relocate-note old-note --to kb/notes/new-path.md --apply
```

Without `--apply`, previews changes without writing.

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

The review system runs LLM-based quality reviews against notes using defined review gates. For the full review workflow, read `kb/instructions/REVIEW-SYSTEM.md`. For the code architecture, see `src/commonplace/docs/REVIEW.md`.

### commonplace-review-sweep

Run a full review sweep — selects notes needing review and runs gate bundles on them.

```bash
commonplace-review-sweep prose --model claude-opus-4-6 --runner claude-code
commonplace-review-sweep prose --model claude-opus-4-6 --current      # only current-status notes
commonplace-review-sweep --all-gates --model claude-opus-4-6          # all gate bundles
commonplace-review-sweep prose --dry-run                              # preview what would run
```

### commonplace-run-review-bundle

Run a review bundle (set of gates) on a single note.

```bash
commonplace-run-review-bundle kb/notes/my-note.md prose --runner claude-code --model claude-opus-4-6
```

### commonplace-run-gate-sweep

Run a single gate across multiple notes in batched prompts.

```bash
commonplace-run-gate-sweep semantic/grounding-alignment --runner claude-code --model claude-opus-4-6
commonplace-run-gate-sweep semantic/grounding-alignment --current --batch-size 5
commonplace-run-gate-sweep semantic/grounding-alignment --note kb/notes/specific.md
commonplace-run-gate-sweep semantic/grounding-alignment --dry-run
```

### commonplace-create-review-run

Create a review run record in the review database. Outputs JSON with the review_run_id and gate definitions.

```bash
commonplace-create-review-run kb/notes/my-note.md prose --runner claude-code --model claude-opus-4-6
commonplace-create-review-run kb/notes/my-note.md prose --json   # JSON output for scripting
```

### commonplace-write-gate-review

Record a single gate review from a file into an existing review run.

```bash
commonplace-write-gate-review --review-run-id 42 --gate-id prose/clarity --input-file review-output.md
```

### commonplace-finalize-review-run

Mark a review run as completed. Validates that all expected gate reviews are present, then appends acceptance events.

```bash
commonplace-finalize-review-run --review-run-id 42
```

### commonplace-ack-gate-review

Advance acceptance baseline for specific gates without re-running the review.

```bash
commonplace-ack-gate-review kb/notes/my-note.md --model claude-opus-4-6 prose/clarity semantic/grounding-alignment
```

### commonplace-ack-trivial-note-changes

Auto-acknowledge `note-changed` stale pairs when only non-watched note parts changed. Each gate declares what it watches (body, title, description) — changes outside the watched set are acked automatically.

```bash
commonplace-ack-trivial-note-changes prose                         # all prose gates
commonplace-ack-trivial-note-changes prose --current               # current-status notes only
commonplace-ack-trivial-note-changes prose --dry-run               # preview what would ack
```

### commonplace-resolve-gates

Expand gate bundle names to individual gate IDs and output their definitions.

```bash
commonplace-resolve-gates prose                                    # all gates in prose bundle
commonplace-resolve-gates prose/clarity semantic/grounding-alignment  # specific gates
```

### commonplace-review-target-selector

List stale (note, gate) pairs that need review. Compares current note/gate SHAs against accepted SHAs.

```bash
commonplace-review-target-selector prose --model claude-opus-4-6
commonplace-review-target-selector prose --current --json          # JSON output
commonplace-review-target-selector prose --reason note-changed     # filter by staleness reason
commonplace-review-target-selector prose --ack kb/notes/foo.md:prose/clarity   # ack a pair
```

### commonplace-warn-selector

Extract warn-level findings from effective reviews.

```bash
commonplace-warn-selector                                          # all notes
commonplace-warn-selector kb/notes/my-note.md                     # specific note
commonplace-warn-selector --json                                   # JSON output
```

## Review maintenance

Operational commands for database repair and migration. All support `--dry-run`.

### commonplace-reparse-gate-review-decisions

Re-parse decision values from stored review markdown. Useful after decision parsing logic changes.

```bash
commonplace-reparse-gate-review-decisions --dry-run
commonplace-reparse-gate-review-decisions --review-run-id 42
```

### commonplace-repair-manual-import-review-results

Re-infer decisions for legacy manual-import reviews with stale footers.

```bash
commonplace-repair-manual-import-review-results --dry-run
```

### commonplace-prune-superseded-unknown-manual-import-reviews

Delete manual-import reviews with `decision=unknown` that have been replaced by definitive reviews.

```bash
commonplace-prune-superseded-unknown-manual-import-reviews --dry-run
```
