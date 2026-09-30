# Review fixes before refresh batch 01

Worker packet, written 2026-09-28 after two independent reviews of the
code and the contracts at `86b4f98f`. Purpose: remove every defect that
would stop, corrupt or mislead the first refresh batch
(`kb/work/agentic-memory-refresh/batch-01-handoff.md`), and nothing else.
The broader cleanup the reviews found (dead code, duplicated parsers,
schema-duplicate checks, test bloat) is a later packet; do not start it.
The deliberate decisions in the [transition plan](./transition-plan.md)
stand: relaxed run-state verification, committed inputs, parallel
publication, set validation deferred to `kb/work/directory-artifacts`.

## Fixes, as separate commits with tests

1. **Publication worktree check** (`src/commonplace/lib/agentic_publication.py`).
   Parse `git status --porcelain -z --untracked-files=all` so quoted paths
   and renames are read correctly. Exempt both untracked and modified paths
   under the two output locations (`kb/agentic-systems/reviews/`,
   `kb/reports/retained/agentic-system-analysis/`), so a sibling run that
   replaced an existing review does not block another run's publish; staged
   or modified paths elsewhere still fail. Tests: a non-ASCII untracked name
   under `kb/notes/` fails; a modified tracked review under `reviews/` passes.
2. **Rollback leaves no retained directory.** When publish created
   `kb/reports/retained/agentic-system-analysis/<run-id>/` and rolls back,
   remove that directory, so a retry with the same run ID works. Extend the
   rollback test to assert the directory is gone and a retry succeeds.
3. **Manifest and pass reporting.** A manifest entry whose `path`, `sha256`
   or `type` is not a string fails with a `ValueError` naming the entry,
   never a `TypeError`. The "manifest members present, hashed and typed"
   pass is recorded only when those checks produced no error.
4. **Comparison loader matches publication.** `systems_matrix.load_results`
   drops the cross-member ID resolution (`set_record_errors`) and validates
   the memory profile only through the memory member's own validation, so a
   set that publishes also loads. Keep the source-identity-in-register check
   only if run-state verification makes the same check; otherwise drop it
   too and say which in the commit message.
5. **Contract fixes** (type specs and schemas; the instructions only where
   named):
   - Memory report type: profile records must be declared or annotated
     (`On <ID>`) in the report itself; say so where it now says "declared
     somewhere in the set", and say the specialist annotates any seeded
     record its profile cites. Add the same one-line rule to
     `kb/instructions/analyse-agentic-system/jobs/memory.md`.
   - One placement for amendments: an `## Amendments` section at the end of
     the declaring member, holding `Amendment:` entries keyed by ID. State it
     once, in the overview's grammar section; the memory type points to it;
     add the section as optional to the memory and runtime schemas.
   - One placement for annotations: in the section the member's type names
     (`## Annotations` in the runtime report, under `## Shared records` in
     the memory report). State it in the overview grammar.
   - Memory schema: `finalized-from` in `required`, nullable.
   - Rename the memory report's `analysis-run` field to `run-id`, matching
     the other members; update schema, type, fixtures, code
     (`agentic_set.py` special case) and the memory instruction.
   - Epistemic proposals: the coordinator registers an accepted `EPI-`
     proposal in the runtime report. Say so in the overview grammar.
   - Method paths: the skill and `kb/reference/commands.md` point to the
     code constant `METHOD_PATHS` instead of listing paths in prose; add
     `kb/types/note.schema.yaml` and `kb/types/note-base.schema.yaml` to the
     constant, since every member schema references them.
6. **Skill fixes** (`kb/instructions/analyse-agentic-system/SKILL.md`):
   - Step 7: for a blocked or out-of-scope run, write the overview only,
     with an empty manifest.
   - A blocked specialist report: recommission a fresh specialist against
     the same frozen input if the block is correctable; otherwise the run
     completes as `blocked`. One sentence.
   - The epistemic member is written or remapped after reconciliation, so
     it cites only canonical IDs; state that at step 5 or 6.
   - "Shared records rules for theory routes" links the runtime type's
     section.
   - Replace "bundle" with "set" in the skill, `commands.md`, the memory
     instruction, and user-facing messages and docstrings in
     `agentic_publication.py`, `cli/agentic_analysis_publication.py`,
     `cli/quote.py`, `scripts/verify_report_quotes.py`; fix the stale comment
     in `validation.py` around line 934 that claims run-state verification
     resolves IDs across the set and applies a set quote minimum.

## Scope and checks

Owned: `src/commonplace/**`, `tests/**`, `scripts/verify_report_quotes.py`,
the six analysis type specs and schemas under `kb/types/` and
`kb/agentic-systems/types/`, the three analysis instructions,
`kb/reference/commands.md`. Not owned: `kb/work/**`, `properdocs.yml`,
everything under `kb/agentic-systems/reviews*` and `kb/reports/**`. Other
sessions' modified files are in the working tree (installed-test tooling,
`kb/work/directory-artifacts/`); never stage them. Stage by explicit path.

`uv run pytest` and `uv run ruff check src tests scripts` pass after each
commit; every changed KB file passes `commonplace-validate`. Stop and
report if a fix contradicts a decision in the transition plan or needs a
file outside the owned scope. Return per commit: hash, what changed,
choices made, test count.
