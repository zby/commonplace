---
description: "Use when an automated improvement pass has weakened or cut a passage and the operator wants to know whether the review finding justified it before restoring anything"
type: kb/types/instruction.md
---

# Audit a prior pass

Restore what a pass cut without justification, in the form its own findings
asked for, and keep what it cut for cause.

Inputs: the artifact, the pass's diff, and its packet directory of findings.

1. List each passage the diff weakened: a mapping, contrast, example, price,
   or link that the old text had and the new text does not.
2. For each, find the finding that motivated the edit. Search the packet for
   the passage's words, then read the finding and the pass report's action
   for that location.
3. Classify: the finding justified the whole cut; it justified a narrower
   edit; or no finding covers the cut and it rode along with a compression
   action.
4. For the second and third classes, restore the passage in the form the
   finding suggested. A grounding failure on one phrase is fixed by removing
   that phrase, not the paragraph it sat in. Keep the finding's true part.
5. Report per passage: what was lost, which finding, the class, what you
   restored. Name any restored content the finding still leaves unsupported.

Preserve: every claim the pass correctly narrowed. Do not re-widen a claim to
its pre-pass strength because the wording was better.
