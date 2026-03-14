# Review: Explanatory Reach

Audit KB notes against the explanatory reach test from [first-principles reasoning selects for explanatory reach over adaptive fit](../../notes/first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md). Identify notes that are merely adaptive (record what works without explaining why) and flag them for deepening.

This file is a stable runbook. Do not edit it per run; only change it when scope or process changes.

## Scope

- `kb/notes/*.md` — all notes with frontmatter (skip text files and indexes)
- Focus on notes with tags `learning-theory`, `computational-model` first — these are the areas where explanatory depth matters most

## Run Procedure

For each note in scope, apply the three-part test:

1. **Can you vary the explanation?** If you changed one premise, could you predict what changes in the conclusion? If yes, the note captures causal structure. If no, it may be recording correlation or pattern without mechanism.

2. **Does it reach?** Would the insight apply in a domain the note doesn't mention? If yes, the mechanism is deeper than the specific case. If no, the note may be context-fitted.

3. **Can it be criticized?** Is there a specific way the explanation could be wrong, not just incomplete? Notes that are purely definitional or taxonomic will fail this — that's fine, flag them as a different kind (framework note, not explanatory note) rather than as deficient.

## Classification

For each note, assign one of:

- **explanatory** — passes the three tests; captures mechanism with reach
- **adaptive** — records a pattern that works without explaining why; candidate for deepening
- **framework** — definitional, taxonomic, or structural; not expected to be explanatory (indexes, type definitions, methodology)
- **mixed** — has explanatory sections and adaptive sections; flag which parts could be deepened

## Output

Record findings in `kb/tasks/recurring/review-explanatory-reach-log.md`.
Append one dated section per run (e.g. `## 2026-03-07`) with:
- Notes reviewed (count and list)
- Classification breakdown
- Top candidates for deepening (adaptive notes where adding mechanism would increase reach)
- Any notes reclassified from previous runs
