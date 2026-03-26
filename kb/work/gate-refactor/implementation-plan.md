# Implementation plan

Concrete steps to get from the current bundle-based review system to the gate-based design in [design.md](./design.md). Each step produces a working state — no step depends on completing all subsequent steps.

## Step 1: Create gate files from existing review checks

Decompose the 4 existing review bundles into individual gate files under `kb/instructions/review-gates/{lens}/`.

The exact initial gate inventory:

| Gate ID | Source | Watches | Staleness |
|---|---|---|---|
| **frontmatter/description-discrimination** | frontmatter-review check 1 | `[title, description]` | `changed` |
| **frontmatter/title-composability** | frontmatter-review check 2 | `[title]` | `changed` |
| **frontmatter/claim-strength** | frontmatter-review check 3 | `[title]` | `changed` |
| **frontmatter/title-body-alignment** | frontmatter-review check 4 | `[title, body]` | `rewrite(0.5)` |
| **prose/source-residue** | prose-review check 1 | `[body]` | `changed` |
| **prose/pseudo-formalism** | prose-review check 2 | `[body]` | `changed` |
| **prose/confidence-miscalibration** | prose-review check 3 | `[body]` | `changed` |
| **prose/proportion-mismatch** | prose-review check 4 | `[body]` | `changed` |
| **prose/orphan-references** | prose-review check 5 | `[body]` | `changed` |
| **prose/unbridged-cross-domain** | prose-review check 6 | `[body]` | `changed` |
| **prose/redundant-restatement** | prose-review check 7 | `[body]` | `changed` |
| **prose/anthropomorphic-framing** | prose-review check 8 | `[body]` | `changed` |
| **semantic/completeness-boundary-cases** | semantic-review step 2 | `[body]` | `changed` |
| **semantic/grounding-alignment** | semantic-review step 3 (includes domain coverage sub-check) | `[body]` | `changed` |
| **semantic/internal-consistency** | semantic-review step 4 | `[body]` | `changed` |
| **complexity/claim-to-section-ratio** | complexity-review check 1 | `[body]` | `changed` |
| **complexity/framework-decoration** | complexity-review check 2 | `[body]` | `changed` |
| **complexity/connection-inflation** | complexity-review check 3 | `[body]` | `changed` |
| **complexity/could-be-a-paragraph** | complexity-review check 4 | `[body]` | `changed` |
| **structural/broken-link-path** | existing gate | `[body]` | `changed` |
| **structural/compound-bullet** | existing gate | `[body]` | `changed` |
| **structural/bullet-capitalization** | existing gate | `[body]` | `changed` |
| **structural/general-before-specific** | existing gate | `[body]` | `changed` |

**23 gates total.** Note: semantic-review has 3 checks, not 4 — "domain coverage" is a sub-check of grounding-alignment (step 3.3 in the current instructions), not a standalone check.

Existing gate files in `kb/instructions/gates/` move to `kb/instructions/review-gates/structural/` with `gate_id`, `watches`, and `staleness` added to frontmatter.

Each gate file gets the frontmatter from the design:

```yaml
---
gate_id: {lens}/{name}
name: Human name
lens: {lens}
watches: [relevant regions]
staleness: changed  # or rewrite(0.5) for title-body-alignment
---
```

Body: failure mode, test, examples — extracted from the corresponding check section in the current bundle document.

**Done when:** `kb/instructions/review-gates/` has 23 gate files covering all checks from all 4 bundles plus the 4 existing gates.

## Step 2: Create bundle files

Write bundle files in `kb/instructions/review-bundles/` that list their gates. One per current review type. Each bundle has: purpose, gate list, output format. No shared check prose — that's in the gate files now.

**Done when:** 4 bundle files exist, each listing its gate IDs under a `## Gates` section.

## Step 3: Build the gate selector

New script: `scripts/gate_selector.py`. This replaces `notes_selector.py` + `selector_engine.py` for gate-based review.

**Reviewable note scope:** top-level `*.md` files in `kb/notes/` that have YAML frontmatter and are not indexes (same rule as `review_state.list_reviewable_notes`). Subdirectory notes (e.g. `kb/notes/related-systems/`, `kb/notes/definitions/`) are excluded for now. If the scope needs to expand later, change it in one place.

Inputs: a bundle name (or `--all-gates`), optional note path filter.

Logic:
1. Parse the bundle file to get gate IDs.
2. Load gate frontmatter (watches, staleness) for each gate.
3. Load `gate_reviews.csv` (or create empty if missing).
4. For each (note, gate) pair:
   - **Gate change check**: compute git blob hash of gate file, compare to `gate_hash` in CSV. Mismatch = stale.
   - **Git filter**: if note file hasn't changed since `recorded_commit`, skip (fresh).
   - **Staleness check**: for `changed` gates, hash watched regions and compare. For `rewrite(threshold)` gates, check non-body watched fields exactly, then measure body diff ratio.
   - **Missing review**: no CSV row = stale.
5. Emit stale (note, gate) pairs.

Output: JSON list of `{note_path, gate_id, reason}`, or plain paths grouped by note.

Reuse from existing code:
- `review_state.py`: `list_reviewable_notes`, `has_frontmatter`, `extract_body_lines`, `build_note_snapshot`
- `review_metadata.py`: `git_blob_sha`, `read_blob`, `run_git`
- `selector_engine.py`: `body_change_ratio`

New code needed:
- Gate frontmatter parser (read YAML, extract `gate_id`, `watches`, `staleness`)
- Watched-region hasher (hash only title / description / frontmatter / body based on `watches`)
- CSV reader/writer for `gate_reviews.csv`
- Gate file blob hash computation

Tests:
- build a fixture test repo with real git history, not mocked git responses
- fixture should contain:
  - a small `kb/notes/` tree with reviewable notes
  - a small `kb/instructions/review-gates/` tree
  - a small `kb/instructions/review-bundles/` tree
  - recorded gate review files plus generated `gate_reviews.csv`
  - at least two commits so tests can exercise `recorded_commit` vs `HEAD`
- use this fixture repo for selector tests covering:
  - missing review -> stale
  - gate file changed -> stale
  - watched hash changed -> stale
  - rewrite threshold not exceeded -> fresh
  - rewrite threshold exceeded -> stale
  - unchanged note outside git diff set -> fresh

**Done when:** `uv run scripts/gate_selector.py frontmatter-review` emits stale (note, gate) pairs. Initially everything will be stale (no recorded reviews yet).

## Step 4: Write recorded gate reviews

New script or function: after a gate review is performed, write the recorded review file and update the CSV.

Review file path: `kb/reports/reviews/gates/{encoded-note-path}/{gate-id}.md`

Metadata comment format per design.md. CSV columns: `note_path, gate_id, gate_hash, recorded_commit, watched_hash, recorded_at`.

Tests:
- use the fixture repo to verify write -> regenerate CSV -> select round-trips correctly
- verify recorded review metadata is sufficient to restore freshness without reparsing review prose

**Done when:** review files can be written and the CSV regenerated. The gate selector reads them and correctly reports fresh/stale.

## Step 5: Wire up execution

Update the review skill (or create a new one) to use the gate-based flow:

1. Run gate selector → get stale (note, gate) pairs
2. Group by (note, lens)
3. For each group: load note + gate files → run review → produce findings
4. Write recorded review files + update CSV

The applicator stage (step 4 in the design) can be manual for now — the reviewer produces findings, a human or separate call decides what to act on. Don't build applicator infrastructure until the review stage is proven.

**Done when:** a gate-based review can run end-to-end on a note and produce stored, selector-visible results.

## Step 6: Delete old bundle review infrastructure

Once gate-based reviews work:
- Delete old review files in `kb/reports/reviews/*.{type}-review.md` (or archive them)
- Remove `selector_engine.py`'s `SELECTOR_POLICIES` dict and `_frontmatter_decision` / `_full_text_decision`
- Remove or redirect `notes_selector.py` to use `gate_selector.py`
- Delete the monolithic review instruction files (the check prose is now in gate files)

**Done when:** only gate-based review infrastructure remains.

## What to skip

- **Summarize/reporting scripts**: `summarize_reviews.py` and its CSV reports can be rebuilt later once gate reviews accumulate. Don't port them preemptively.
- **Applicator infrastructure**: humans do prioritization for now. Build the applicator when the review stage is stable and you have data on what findings look like.
- **Gate extraction workflow**: `/extract-gates` from the review-revise brainstorm. Build this after the gate store exists and you have more manual edits to learn from.
- **Gate ack script**: `gate_ack.py` for acknowledging trivial changes without re-reviewing. Useful but not needed until gate reviews are running and trivial-change noise becomes a real problem.
