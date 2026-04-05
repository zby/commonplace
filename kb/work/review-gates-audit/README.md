# Workshop: review-gates audit

Goal: review the current gate system for load, overlap, reliability, and issue yield, then define a reduction path that removes obvious waste before tuning prompts.

## Evidence used

- Gate inventory in `kb/instructions/review-gates/`
- Operational review state in `kb/reports/review-store.sqlite`
- Parser health check from `python3 scripts/reparse_gate_review_decisions.py --dry-run`
- Controlled gate-quality analysis in `kb/work/review-revise-gated/run-08/gate-noise-audit.md`

## Inventory and load

- Initial audit baseline: 34 gates across 7 bundles
- Active set after removing the `structural/broken-link-path` duplicate: 33 gates across 7 bundles
- Current gate text load: 740 lines, 29,099 bytes
- Largest bundles by prompt size:
  - sentence: 146 lines, 7,045 bytes
  - prose: 166 lines, 6,782 bytes
  - accessibility: 87 lines, 4,567 bytes
  - structural: 127 lines, 4,229 bytes
- Historical execution shape in `review_runs`:
  - 809 runs total
  - 4.53 gates per run on average
  - 9 gates max in one run

This means full coverage is operationally expensive. The system is gate-local in storage, but bundle-local in execution, so a note that needs every bundle is effectively reread several times.

## Data quality caveat

Do not use the raw `gate_reviews.decision` column uncritically across the whole DB.

- Total rows: 6,674
- `manual-import` rows: 3,524
- `full-review` rows: 3,150
- Reparse dry run on all rows:
  - changed: 1,738
  - unknown: 1,746
- Reparse split by review kind:
  - `manual-import`: 1,693 changed, 1,693 unknown
  - `full-review`: 45 changed, 53 unknown
- Reparse on current bundled runs only:
  - 969 rows scanned
  - 0 changed
  - 12 unknown

At audit time, imported rows were the dominant contamination source. That has now been repaired with `scripts/repair_manual_import_review_results.py`.

Current state after repair:

- `manual-import`: 0 decision mismatches, 996 rows explicitly marked `unknown`
- `full-review`: 45 decision mismatches, 53 rows parsed as `unknown`

Conclusion: use two evidence tiers.

- For current production-like behavior, trust bundled-run rows.
- For older full-review history, reparse the markdown before measuring.
- Imported rows are now parser-clean, but the 996 `unknown` rows should still be treated as low-confidence historical data rather than strong evidence for gate quality.

## What catches the least issues

Use bundled-run rows for this question, because they are the cleanest dataset.

### Reliable recent low-yield gates

- structural/general-before-specific: 1.3% issue rate on 151 recent reviews
- structural/broken-link-path: 5.3% on 151 reviews
- semantic/internal-consistency: 7.1% on 56 reviews
- sentence/parsing-ambiguity: 0.0% on 16 reviews
- frontmatter/claim-strength: 0.0% on 6 reviews

Interpretation:

- `sentence/parsing-ambiguity` and `frontmatter/claim-strength` are low-yield in the recent corpus, but they were useful in the controlled workshop. Low yield does not automatically mean low quality.
- `structural/broken-link-path` is low-yield and also duplicates `/validate`, so it is a strong removal candidate.
- `structural/general-before-specific` is low-yield and also had unstable severity in the workshop. It should stay below the cut line unless it proves unique value.

### Cohort warning

Recent sample sizes differ by bundle:

- structural: 151 reviews per gate
- semantic: 56-57
- sentence: 16
- frontmatter: 6
- accessibility, complexity, prose: 4-5

So cross-bundle issue rates are not directly comparable. Compare gates inside the same recent cohort, or use the workshop for precision judgments.

## Duplicate and overlap findings

### 1. `structural/broken-link-path` was a real duplicate

The gate definition already said it overlapped with `/validate`'s link-health check. This was the clearest duplicate in the system.

Status: removed from the active gate set in this audit pass. Broken links should now be left to `/validate`.

### 2. `sentence/misleading-link-text` and `sentence/concept-attribution` are the same failure family

Both gates ask whether prose makes the reader expect one thing from a linked note while the target actually supports something else.

- `misleading-link-text` handles the general case
- `concept-attribution` handles the identity-claim subtype

Recommendation: merge them into one gate such as `sentence/link-target-mismatch`, with identity claims as an explicit sub-check.

### 3. Three complexity gates are really one gate

These three gates are all variants of "structure exceeds substance":

- `complexity/claim-to-section-ratio`
- `complexity/framework-decoration`
- `complexity/could-be-a-paragraph`

They differ mostly by the object being compressed:

- section scaffold
- table/taxonomy/framework
- whole note

Recommendation: merge them into one complexity gate with three questions, not three separate review passes.

### 4. Accessibility still has some double-counting risk

The workshop already found double-flagging between:

- `accessibility/undefined-terms`
- `accessibility/notation-opacity`

This is partly fixed in the gate text now, but the family is still close enough that it should be treated as a second-phase consolidation candidate rather than expanded further.

## Low-quality or noisy gates

### Quarantine or retire

- `prose/anthropomorphic-framing`
  - produced a false positive on "sessions want" in the workshop
  - 0 issues in the recent bundled cohort
  - recommendation: retire unless a stronger corpus proves unique value

- `prose/confidence-miscalibration`
  - workshop found contradictory judgments on the same text
  - recent bundled cohort also produced 0 issues
  - recommendation: retire or narrow to unsupported quantitative certainty claims only

### Keep, but rewrite

- `semantic/completeness-boundary-cases`
  - detects real soft-edge problems
  - in the workshop it often prescribed expansion when compression was the right fix
  - recommendation: keep only after adding "compress before expand" guidance

- `sentence/concept-attribution`
  - useful idea
  - false positive in the workshop
  - overlap with `misleading-link-text`
  - recommendation: keep only as part of a merged gate

- `structural/general-before-specific`
  - low recent yield
  - severity flips in workshop runs on the same baseline
  - recommendation: keep only with a sharper exemplar-vs-tension rule

- `accessibility/unidentified-references`
  - threshold ambiguity around linked proper nouns
  - recommendation: keep, but the rule about whether a link counts as identification must stay explicit

### Do not merge yet despite overlap

- `prose/redundant-restatement`
- `prose/bridge-paragraph-duplication`

The workshop showed that splitting the bridge-paragraph pattern out of generic redundancy improved detection. These two are close, but the split was useful.

## Reduction proposal

### Phase 1: safe cuts

- retire `prose/anthropomorphic-framing`
- retire `prose/confidence-miscalibration`
- merge `sentence/misleading-link-text` + `sentence/concept-attribution`
- merge `complexity/claim-to-section-ratio` + `complexity/framework-decoration` + `complexity/could-be-a-paragraph`

This reduces the active set from 33 gates to 28 without touching the semantic core.

### Phase 2: likely follow-up cuts

- decide whether `structural/bullet-capitalization` belongs in `/validate` instead of review
- decide whether accessibility should stay at three separate readability gates or collapse to two
- decide whether frontmatter needs four gates or three

The realistic medium-term target is 24-26 active gates, not 34.

## How to approach low-quality reviews

The right question is not "which gates warn least?" It is "which gates create unique, correct, actionable findings?"

Use four measurements:

1. Issue yield
   - How often does the gate produce `warn` or `fail` in a parser-clean cohort?

2. Stability
   - On the same `(note_sha, gate_sha)`, does the gate consistently separate clean from issue-bearing notes?

3. Unique contribution
   - In a controlled benchmark like `review-revise-gated`, does the gate catch a change that another gate would have missed?

4. Edit usefulness
   - When the gate warns, does the accepted revision actually keep that finding, or is it ignored, contradicted, or fixed indirectly by another gate?

A low-quality gate usually has one of these signatures:

- it fires often but adds nothing unique
- it conflicts on repeated inputs
- it points in the wrong direction
- it gets absorbed by another gate's finding

## Immediate next steps

1. Recompute any future gate metrics from reparsed `full-review` markdown or bundled runs only.
2. Make the Phase 1 cuts and merges.
3. Re-run:
   - a bundle audit on current notes
   - the `review-revise-gated` benchmark
4. Only after the gate count is lower, tune severity thresholds on the remaining gates.

## Small hygiene finding

Eight gates still use description-only frontmatter instead of the fuller `gate_id` / `name` / `lens` / `watches` / `staleness` shape:

- all 4 accessibility gates
- `sentence/parsing-ambiguity`
- `sentence/framing-mismatch`
- `sentence/misleading-link-text`
- `sentence/stock-phrases`

This is not the main load problem, but it is worth normalizing once the reduction plan settles.
