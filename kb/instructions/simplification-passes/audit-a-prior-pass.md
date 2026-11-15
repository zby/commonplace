---
description: "Use when an automated improvement pass has weakened or cut a passage and the operator wants to know whether the review finding justified it before restoring anything"
type: types/edit-operation.md
effort: simple
decision: none
---

# Audit a prior pass

Restore what a pass cut without justification, in the form its own findings
asked for, and keep what it cut for cause.

Effort: simple. Search, classify, and restore against a recorded finding; the findings inputs supply the evidence.

## Steps

The caller supplies, beside the text: the pass's diff as the `diff` input,
and the findings that motivated the pass as inputs whose role begins with
`findings`, such as `findings` or `findings-semantic`. A full-pass packet's
findings are its method reports, one input each. Use only these files.

1. List each passage the diff weakened: a mapping, contrast, example, price,
   or link that the old text had and the new text does not.
2. For each, find the finding that motivated the edit. Search the findings
   inputs for the passage's words, then read the finding and the pass report's action
   for that location.
3. Classify: the finding justified the whole cut; it justified a narrower
   edit; or no finding covers the cut and it rode along with a compression
   action.
4. For the second and third classes, restore the passage in the form the
   finding suggested. A grounding failure on one phrase is fixed by removing
   that phrase, not the paragraph it sat in. Keep the finding's true part.

## Report

Per passage: what was lost, which finding, the class, what you restored.
Name any restored content the finding still leaves unsupported.

## Preserve

Every claim the pass correctly narrowed. Do not re-widen a claim to
its pre-pass strength because the wording was better.

---

Relevant Notes:

- [Two rewrites exposed a syntax-or-repetition tradeoff](../../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) — rests-on: evidence that an unguarded pass cuts relations the finding did not ask it to cut, which is what this audit restores
