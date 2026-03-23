# Reviews

Automated quality reviews of `kb/notes/`. Each note gets individual review files; summaries aggregate findings across the KB.

## Review types

- **prose-review** — Checks whether prose faithfully represents content: source residue, pseudo-formalism, confidence miscalibration, proportion mismatch, orphan references, unbridged cross-domain evidence, redundant restatement, anthropomorphic framing. Instruction: `kb/instructions/prose-review.md`
- **semantic-review** — Checks content correctness: completeness of enumerations via boundary cases, grounding alignment with cited sources, internal consistency. Instruction: `kb/instructions/semantic-review.md`

## File naming

Individual reviews: `{note-stem}.{review-type}.md` (e.g. `backlinks.prose-review.md`)

Summaries: `SUMMARY.{review-type}.md` (per type) or `SUMMARY.md` (all types combined)

## CSV tables (`csv/`)

Normalized data for analysis. Prefixed by review type when run per-type, unprefixed when combined.

| File | Contents |
|------|----------|
| `findings.csv` | One row per finding, ordered WARN-first and clustered by high-warning notes/checks |
| `notes_summary.csv` | Per-note aggregation, ordered by warning count descending |
| `checks_summary.csv` | Per-check aggregation with sample finding, ordered by warning count descending |
| `checks_low_signal.csv` | Per-check aggregation ordered by the fewest warnings first |
| `notes_by_warnings.csv` | Note-level priority queue with top checks and sample warning |

## Running

```bash
# Notes needing prose review
uv run scripts/notes_selector.py prose-review

# Changed prose-review targets with diffs for an orchestrator
uv run scripts/notes_selector.py prose-review --json

# Notes needing semantic review
uv run scripts/notes_selector.py semantic-review

# Changed semantic-review targets with diffs for an orchestrator
uv run scripts/notes_selector.py semantic-review --json

# Accept a trivial diff without rewriting the review body
uv run scripts/ack_review.py prose-review kb/notes/backlinks.md
uv run scripts/ack_review.py semantic-review kb/notes/backlinks.md

# Full inventory, ignoring review timestamps
uv run scripts/notes_selector.py --all

# Backfill revision metadata into existing review files
uv run scripts/migrate_review_metadata.py

# Regenerate ranked CSV tables and a compact summary from existing review files
uv run scripts/summarize_reviews.py              # all types
uv run scripts/summarize_reviews.py prose-review  # single type
```

The selector is revision-based: each review stores both the last note revision that received a full review and the last note revision accepted by the sweep. The selector compares against `last-accepted-note-sha`, unchanged notes are filtered out entirely, and changed notes can be surfaced with compact diffs so the sweep orchestrator can decide whether to run a full review or just acknowledge a trivial change.

The summary generator is intentionally thin: it writes ranked CSV tables for orchestration and a compact markdown summary built from only the top rows of those tables.

Full sweep instructions (including sub-agent delegation): `kb/instructions/prose-review-sweep.md`, `kb/instructions/semantic-review-sweep.md`

## Re-running

Subsequent runs overwrite individual review files and summaries. Commit before re-running to track changes over time.
