# Reviews

Automated quality reviews of `kb/notes/`. The current selector and storage model are gate-based: each recorded review is keyed by `(note, gate, model)` rather than one monolithic file per note and review type.

## Review types

- **frontmatter-review** — Bundle file: `kb/instructions/review-bundles/frontmatter-review.md`
- **prose-review** — Bundle file: `kb/instructions/review-bundles/prose-review.md`
- **semantic-review** — Bundle file: `kb/instructions/review-bundles/semantic-review.md`
- **complexity-review** — Bundle file: `kb/instructions/review-bundles/complexity-review.md`

## File naming

- Gate reviews: `{encoded-note-path}/{encoded-gate-id}.{encoded-model}.md`
- Gate review index: `../review-csv/gate_reviews.csv`
- Legacy monolithic review files, summaries, and old review CSVs were moved under `kb/reports/archive/`.

## Active CSV

The active gate-based index is:

- `kb/reports/review-csv/gate_reviews.csv` — one row per recorded `(note, gate, model)` baseline

## Running

```bash
# Set the active review model for all gate-based scripts
export COMMONPLACE_REVIEW_MODEL=gpt-5.4

# Stale prose-review gate pairs
uv run scripts/gate_selector.py prose-review

# Same, via the compatibility wrapper
uv run scripts/notes_selector.py prose-review --json

# Stale semantic-review gate pairs
uv run scripts/gate_selector.py semantic-review --json

# Full gate inventory across all reviewable notes
uv run scripts/gate_selector.py --all-gates

# Finalize one recorded gate review already written at its canonical path
uv run scripts/gate_reviews.py finalize kb/notes/backlinks.md frontmatter/title-composability

# Mark one or more stale gates as trivial-change acknowledgements
uv run scripts/ack_gate_review.py kb/notes/backlinks.md frontmatter/title-composability
uv run scripts/ack_gate_review.py kb/notes/backlinks.md prose/source-residue prose/redundant-restatement

# Rebuild the active gate CSV index from stored gate reviews
uv run scripts/gate_reviews.py rebuild-csv

# Full inventory, ignoring review timestamps
uv run scripts/notes_selector.py --all
```

The gate selector is revision-based and scope-aware. It compares the current note state against:

- the current `COMMONPLACE_REVIEW_MODEL`
- the stored `recorded_commit`
- the stored `watched_hash`
- the current gate file hash
- the gate's configured staleness policy

That means a note can stay fresh for one gate and go stale for another, and a recording from one model does not make the same gate fresh for a different model.

`ack_review.py` and the old `{note-stem}.{review-type}.md` review system are legacy note-level infrastructure now archived under `kb/reports/archive/`. The gate-level trivial-change path is [scripts/ack_gate_review.py](/home/zby/llm/commonplace/scripts/ack_gate_review.py).

Full sweep instructions: `kb/instructions/frontmatter-review-sweep.md`, `kb/instructions/prose-review-sweep.md`, `kb/instructions/semantic-review-sweep.md`

## Re-running

Subsequent runs overwrite recorded gate review files for the same `(note, gate)` pair. Commit before re-running if you want historical snapshots.
