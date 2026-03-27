---
description: Run experiment review gates on baseline.md — load gates from local gates/ directory, apply each gate, write per-bundle review files to the run directory
---

# Run experiment review

Review `baseline.md` against gates from the local `gates/` directory. Write review findings to a run directory.

Inputs:

- `{run}` — run directory name, e.g. `run-05`
- `{bundles}` — one or more bundle names from `gates/`, e.g. `prose`, `accessibility`, or `prose semantic complexity structural accessibility sentence frontmatter` (= all bundles)

## Context

The baseline note originally lived at `kb/notes/session-history-should-not-be-the-default-next-context.md`. Relative links (starting with `./`) resolve from `kb/notes/`, not from the file's current location.

## Steps

### 1. Load gates

For each bundle in `{bundles}`, read all `.md` files in `gates/{bundle}/`. Each file is one gate — it defines a failure mode and a test.

### 2. Read the note

Read `baseline.md`.

For gates that require reading linked sources (e.g. `semantic/grounding-alignment`, `sentence/misleading-link-text`), resolve relative links from `kb/notes/`. Follow at most 5 links total.

### 3. Apply each gate

For each gate:

1. Apply the gate's failure mode and test to the note.
2. Rate the finding: WARN (likely real problem), INFO (worth checking), or CLEAN (check passed).
3. For WARN and INFO, quote the specific text from the note and state a recommendation.

### 4. Write per-bundle review files

Write one file per bundle to `{run}/{bundle}-review.md` using this format:

```
=== {BUNDLE} REVIEW: baseline.md ===

Checks applied: {count}

WARN:
- [{gate-name}] {finding with specific quote from the note}
  Recommendation: {what to change}

INFO:
- [{gate-name}] {finding}

CLEAN:
- [{gate-name}] {what was checked and why it held}

Overall: {CLEAN / {N} warnings, {M} info}
===
```

Report every gate — WARN, INFO, or CLEAN.

## Do not

- Do not modify `baseline.md`. This is read-only analysis.
- Do not load the monolithic review files (`accessibility-review.md`, `prose-review.md`, etc.) — those are historical artifacts from earlier runs. Use only the gate files in `gates/`.
- Do not skip writing a review for any gate in the requested bundles.
- Do not read linked notes before running accessibility gates — evaluate standalone comprehension.
- Do not fabricate identifications for named systems — recommend the author add them.
