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
| `findings.csv` | One row per finding (note, review_type, level, check, text) |
| `notes_summary.csv` | Per-note aggregation (warn/info/clean counts) |
| `checks_summary.csv` | Per-check aggregation (warn/info/clean counts) |
| `notes_by_warnings.csv` | Notes ranked by warning count descending |
| `checks_without_warnings.csv` | Checks that produced zero warnings |

## Running

```bash
# Inventory notes
uv run scripts/list_notes.py

# Regenerate summaries and CSVs from existing review files
uv run scripts/summarize_reviews.py              # all types
uv run scripts/summarize_reviews.py prose-review  # single type
```

Full sweep instructions (including sub-agent delegation): `kb/instructions/prose-review-sweep.md`, `kb/instructions/semantic-review-sweep.md`

## Re-running

Subsequent runs overwrite individual review files and summaries. Commit before re-running to track changes over time.
