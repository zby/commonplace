# Workshop: review-revise

Goal: find review and revision arrangements that reliably produce the kinds of improvements we made manually to the session-history note, then codify those arrangements as reusable instructions.

## Materials

- `baseline.md` — the note as of `3450a4f` (2026-03-20), before any edits
- `target.md` — the note after manual review and revision (2026-03-25)
- `change-catalogue.md` — 14 named changes across 4 categories (accessibility, clarity, structure, cosmetic), each with baseline text, problem, and desired direction

## Scoring

Each experimental run scores against the change catalogue:

- **Hit** — makes a change in the same direction (not necessarily identical text)
- **Miss** — doesn't catch the problem
- **Mistake** — introduces a new problem or moves in the wrong direction

The score is: `hits / 14` for coverage, with mistakes as a separate penalty count. A good arrangement has high hits, zero mistakes.

## What the manual session actually did

Four review lenses, each surfacing different kinds of findings:

1. **Accessibility** (A1-A3) — insular language assuming KB-internal vocabulary
2. **Clarity** (C1-C3) — ambiguous phrasing, wrong framing, misleading links
3. **Structure** (S1-S6) — duplicate sections, section ordering, compression, folding
4. **Cosmetic** (X1-X2) — formatting, broken link paths

## Questions to explore

- Can a single review pass surface all four categories, or do they need separate passes?
- What's the right ordering? (Accessibility before flow? Semantic before prose?)
- Can review findings be stated as instructions specific enough that a separate revision pass reproduces similar edits?
- How much does the revision pass need to see — the full note, or just the findings + relevant passages?
- Does iterating (review → revise → review again) converge or oscillate?
- What's the minimum number of passes to get from baseline to something close to target?

## Experiment protocol

1. Start from `baseline.md` (copy to a new file for the run)
2. Apply a review arrangement (single pass, multi-pass, specific ordering)
3. Feed findings into a revision pass
4. Score the result against `change-catalogue.md`
5. Record the arrangement, scores, and observations below

## Results

(none yet)
