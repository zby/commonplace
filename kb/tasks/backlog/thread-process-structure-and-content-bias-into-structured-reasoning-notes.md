# Thread process structure and content bias into structured reasoning notes

## Status
ready for implementation

## Prerequisites
- [ ] none

## Goal
Make the KB’s structured-reasoning cluster account for two missing dimensions: process structure vs output structure, and content bias as both evidence for structure and a source of correlated error.

## Context
- Relevant files/symbols:
  - `kb/notes/structure-activates-higher-quality-training-distributions.md`
  - `kb/notes/human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md`
  - `kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md`
  - `kb/sources/agentic-code-reasoning.ingest.md`
  - `kb/sources/language-models-like-humans-show-content-effects-on-reasoning-tasks.ingest.md`
- Related tasks/notes/docs:
  - Extractable Value #3 in `kb/sources/agentic-code-reasoning.ingest.md`
  - Extractable Value #3 and #6 in `kb/sources/language-models-like-humans-show-content-effects-on-reasoning-tasks.ingest.md`
  - Current modified worktree state around `kb/sources/language-models-like-humans-show-content-effects-on-reasoning-tasks.ingest.md`
- How to verify / reproduce:
  - Confirm the KB has an explicit home for the process-structure vs output-structure distinction
  - Confirm `structure-activates-higher-quality-training-distributions.md` uses Lampinen evidence directly or links to the note that does
  - Confirm `error-correction-works-above-chance-oracles-with-decorrelated-checks.md` mentions content bias as a correlated-error source

## Decision Record
- Decision:
  - Group the missing distinctions because they all touch the same emerging theory cluster around structured reasoning quality.
- Inputs:
  - Agentic Code Reasoning and Lampinen source ingests
  - The current notes already contain partial support, but the distinctions remain buried rather than first-class
- Options:
  - Add one-off citations to the existing notes
  - Write a new note for process vs output structure, then re-thread the cluster
  - Wait until the current Lampinen-related user edits settle
- Outcome:
  - Keep this as a backlog task rather than editing immediately. The conceptual work is clear, but part of the source cluster is already being edited elsewhere in the worktree.
- Follow-ups:
  - Re-check `git status` before touching the Lampinen ingest or nearby notes

## Tasks
- [x] Write or promote a note distinguishing process structure from output structure — wrote `kb/notes/process-structure-and-output-structure-are-independent-levers.md`, connected to type-system index, distribution-selection note, and error-correction note
- [x] Thread Lampinen evidence into the distribution-selection note — already done (pre-existing)
- [x] Decide where the "instruction tuning and scaling do not remove content bias" claim should live — already in `structure-activates-higher-quality-training-distributions.md` (line 21)
- [x] Update the error-correction note to treat content bias as a source of correlated model error — added "Content bias as a correlated error source" subsection to the decorrelation section

## Current State
All four subtasks complete. The architecture decision was: new note for process vs output structure, content bias threaded into existing notes (distribution-selection and error-correction) rather than a separate note.

## Notes
- `human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md` already carries some Lampinen-derived support, so this is not greenfield.
- The outstanding question is architecture: whether to add one synthesis note or distribute the missing claims across the existing notes.
