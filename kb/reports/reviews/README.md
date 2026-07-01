# Reviews

Legacy rendered review artifacts and archived review outputs. The live review system stores canonical state in SQLite and does not use this directory as a runtime source of truth.

**System design:** [kb/reference/README-REVIEW-SYSTEM.md](../../reference/README-REVIEW-SYSTEM.md)

## Bundles

- **accessibility** — gates in `kb/instructions/review-gates/accessibility/`
- **complexity** — gates in `kb/instructions/review-gates/complexity/`
- **frontmatter** — gates in `kb/instructions/review-gates/frontmatter/`
- **prose** — gates in `kb/instructions/review-gates/prose/`
- **semantic** — gates in `kb/instructions/review-gates/semantic/`
- **sentence** — gates in `kb/instructions/review-gates/sentence/`
- **structural** — gates in `kb/instructions/review-gates/structural/`

## Instructions

- **Review batches:** `kb/instructions/run-review-batches.md` — selector JSON, grouped review jobs, live-agent delegation, and finalization

## Running

```bash
# List all stale (note, gate) pairs
commonplace-review-target-selector --model gpt-5-4-xhigh --all-gates

# List stale pairs for one bundle
commonplace-review-target-selector --model gpt-5-4-xhigh prose

# JSON output with diffs
commonplace-review-target-selector --model gpt-5-4-xhigh --all-gates --json

# Ack a review (note change was insignificant for this gate)
commonplace-ack-gate-review --model gpt-5-4-xhigh kb/notes/backlinks.md prose/source-residue
```

## Status

New live reviews are recorded in `kb/reports/review-store.sqlite` via queued review jobs. Files under this directory are optional rendered exports, backups, or historical artifacts.
