# Workshop: review-revise-gated

Goal: find review and revision arrangements that reliably produce the kinds of improvements we made manually to the session-history note, then codify those arrangements as reusable instructions.

**Status: active.** Using the gate-based review system. Gates are copied into `gates/` for experiment isolation.

## Materials

- `baseline.md` — the note as of `3450a4f` (2026-03-20), before any edits
- `target.md` — the note after manual review and revision (2026-03-25)
- `change-catalogue.md` — 16 named changes across 4 categories (accessibility, clarity, structure, cosmetic), each with baseline text, problem, and desired direction
- `gates/` — local copy of review gates, organized by bundle (accessibility, complexity, frontmatter, prose, semantic, sentence, structural)
## Instructions

- `run-review.md` — apply gates to baseline.md, write per-bundle review files to a run directory
- `run-revise.md` — revise baseline.md based on review findings, write revised note to run directory

## Experiment protocol

1. Start from `baseline.md`
2. Run `run-review.md` with the desired bundles, writing to a new run directory
3. Run `run-revise.md` on the review findings, writing `revised.md` to the same run directory
4. Score the result against `change-catalogue.md` → `{run}/scores.md`

## Scoring

Each experimental run scores against the change catalogue:

- **Hit** — makes a change in the same direction (not necessarily identical text)
- **Miss** — doesn't catch the problem
- **Mistake** — introduces a new problem or moves in the wrong direction

The score is: `hits / 16` for coverage, with mistakes as a separate penalty count. A good arrangement has high hits, zero mistakes.

## Results

### Summary across all runs

Early runs (01-04) used monolithic review instructions. Runs 05-08 used the gate system. Run data for 01-07 was removed; run-08 is the current baseline.

| Metric | Runs 01-02 (monolithic) | Runs 03-04 (v2 monolithic) | Runs 05-07 (gates) | Run-08 (gates, tuned) |
|--------|-------------------------|---------------------------|--------------------|-----------------------|
| Revision hits | 6 | 11-12 | 9-11 | **11** |
| Wrong direction | 0-1 | 0-1 | 0 | 0 |
| Factual errors | 0-1 | 0 | 0 | 0 |
| Detection (WARN+INFO) | 2-9 | 11 | 9-14 | **14** |

### Run-08: current gate system

34 gates across 7 bundles. Key gate additions from the experiment:
- `prose/bridge-paragraph-duplication` — split from redundant-restatement to force separate checking
- `sentence/concept-attribution` — catches prose claims about what linked notes contain
- `sentence/clause-packing` — catches revision bloat (sentences overloaded with clauses)

**Revision: 11/16 hits, 0 wrong-direction, 0 factual errors.**

**Detection: 14/16.** Two items undetected (S2 merge sections, S3 compress taxonomy). Two items detected but not fixed: C3 at INFO (concept-attribution), S1 partially fixed (bridge paragraph trimmed but not deleted).

See `run-08/scores.md` for per-change scoring and `run-08/gate-noise-audit.md` for gate reliability analysis.

### Remaining gaps

- **S2 (merge sections)** — no gate checks for section-merging opportunities
- **S3 (compress taxonomy)** — complexity gates consistently approve the taxonomy; completeness gate pushes toward expansion (wrong direction). Irreducible editorial judgment
- **S1 (bridge paragraph)** — detected but revision trimmed wrong part. Detection solved; revision quality is the bottleneck
- **C3 (concept attribution)** — detected at INFO, needs WARN to trigger action

## Key findings

**Gate granularity matters.** Decomposing monolithic reviews into individual gates makes it possible to improve individual checks, add new checks, and select relevant subsets per note.

**Separate gates for separate patterns.** When two failure modes share a gate, the reviewer satisfies the gate by finding either one. Splitting redundant-restatement into section-opening and bridge-paragraph gates was necessary to catch S1.

**Exhaustive-checking language helps.** Adding "report all instances, not just the first" to gate tests improved detection coverage.

**Severity thresholds drive revision behavior.** The reviser treats WARN as actionable and INFO as optional. Five gates have unstable severity (framing-mismatch, general-before-specific, unidentified-references, redundant-restatement, confidence-miscalibration) — they flip WARN/INFO across runs on the same baseline. The noise audit (run-08/gate-noise-audit.md) documents specific threshold fixes.

**Competing findings create wrong-direction risk.** The completeness-boundary-cases gate correctly detects taxonomy gaps but recommends expansion when compression is the right fix. The gate now includes guidance to consider compression before recommending expansion.

**Detection ceiling: 14/16. Revision ceiling: ~12/16.** The two undetected items (S2, S3) are editorial judgments that resist gate formulation. Iteration (reviewing revised output again) can recover 1 additional hit, as demonstrated in early runs.

## Gate audit merge

The former `review-gates-audit` workshop is merged here as the reduction path for the current gate set. Its evidence combined the gate inventory, review-store execution history, the manual-import parser repair, and `run-08/gate-noise-audit.md`.

Use two evidence tiers when judging gate quality:

- **Current behavior:** trust bundled-run rows and controlled workshop runs.
- **Older history:** reparse full-review markdown before measuring; treat repaired `manual-import` `unknown` rows as low-confidence history.

Reduction plan:

1. Retire `prose/anthropomorphic-framing` and `prose/confidence-miscalibration` unless a stronger corpus proves unique value.
2. Merge `sentence/misleading-link-text` with `sentence/concept-attribution` into one link-target-mismatch family, keeping identity claims as a sub-check.
3. Merge `complexity/claim-to-section-ratio`, `complexity/framework-decoration`, and `complexity/could-be-a-paragraph` into one structure-exceeds-substance gate with separate prompts for sections, frameworks, and whole-note compression.
4. Keep `prose/redundant-restatement` and `prose/bridge-paragraph-duplication` separate; the split improved detection.
5. Rewrite before trusting: `semantic/completeness-boundary-cases` needs "compress before expand" guidance, `structural/general-before-specific` needs a sharper exemplar-vs-tension rule, and `accessibility/unidentified-references` needs an explicit rule for whether links identify proper nouns.

The audit's evaluation rule is: do not ask only which gates warn least. Ask whether a gate creates unique, correct, actionable findings, using issue yield, stability on repeated inputs, unique contribution in the benchmark, and edit usefulness in accepted revisions.
