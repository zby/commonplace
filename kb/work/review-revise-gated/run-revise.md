---
type: kb/types/instruction.md
description: Revise baseline.md based on review findings — address WARNs, optionally address INFOs, write revised note to run directory
---

# Run experiment revision

Revise `baseline.md` based on review findings from a completed review run.

Inputs:

- `{run}` — run directory containing review files, e.g. `run-05`

## Steps

### 1. Read baseline and reviews

Read `baseline.md`.

Read all `*-review.md` files in `{run}/`.

### 2. Revise

Apply revisions addressing WARN-level findings. Treat INFO findings as optional — address them only if the fix is simple and doesn't risk introducing new problems.

Rules:

- Do not expand content. If a review says something is incomplete, do not add new material.
- Do not reorganize sections unless a review WARN explicitly asks for it.
- Do not fold or merge sections unless a review WARN explicitly asks for it.
- Preserve the Relevant Notes section and all links (fix broken paths if flagged).
- Preserve the frontmatter exactly.
- When identifying named systems, use only information present in the note itself or its linked sources. Do not fabricate attributions.

### 3. Write revised note

Write the revised note to `{run}/revised.md`.

## Do not

- Do not read the change catalogue or target — the revision should be driven entirely by review findings.
- Do not make changes that no review asked for.
