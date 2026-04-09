# Commonplace CLI Commands

All commands are installed by `pip install llm-commonplace` and available as `commonplace-*` on PATH. Run any command with `--help` for full usage.

## Project setup

### commonplace-init

Initialize or update a Commonplace project. Creates KB directories, seeds instructions and type definitions, installs skills into `.claude/skills/`, and resolves templates.

```bash
commonplace-init --name <project-name>
commonplace-init --root /path/to/project
```

`--name` sets the project name for templates (defaults to directory name). Safe to rerun — never overwrites existing files.

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

### commonplace-sync-topic-links

Sync topic link sections across notes. Ensures bidirectional linking consistency.

```bash
commonplace-sync-topic-links kb/notes/
commonplace-sync-topic-links kb/notes/my-note.md
commonplace-sync-topic-links --dry-run kb/notes/
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

The review system runs LLM-based quality reviews against notes using defined review gates. For the full review workflow, read `kb/instructions/REVIEW-SYSTEM.md`.

### commonplace-review-sweep

Run a full review sweep — selects notes needing review and runs gate bundles on them.

```bash
commonplace-review-sweep --model claude-sonnet-4-20250514 --runner claude-code
commonplace-review-sweep --model claude-sonnet-4-20250514 --current           # only current-status notes
commonplace-review-sweep --dry-run                              # preview what would run
```

### commonplace-run-review-bundle

Run a review bundle (set of gates) on a single note.

```bash
commonplace-run-review-bundle kb/notes/my-note.md semantic --runner claude-code --model claude-sonnet-4-20250514
```

### commonplace-run-gate-sweep

Run gate checks across multiple notes in batch.

```bash
commonplace-run-gate-sweep --runner claude-code --model claude-sonnet-4-20250514
commonplace-run-gate-sweep --current --batch-size 5
commonplace-run-gate-sweep --note kb/notes/specific.md
```

### commonplace-create-review-run

Create a review run record in the review database.

```bash
commonplace-create-review-run kb/notes/my-note.md semantic --runner claude-code --model claude-sonnet-4-20250514
```

### commonplace-write-gate-review

Write a gate review result to the review database.

```bash
commonplace-write-gate-review
```

### commonplace-finalize-review-run

Finalize a review run, marking it complete.

```bash
commonplace-finalize-review-run
```

### commonplace-ack-gate-review

Acknowledge a gate review warning — marks it as reviewed and accepted.

```bash
commonplace-ack-gate-review
```

### commonplace-resolve-gates

Resolve gate status for notes based on review history.

```bash
commonplace-resolve-gates
```
