# Implemented record amendments before the fresh run

The operator authorized implementation through the point before opening a
new analysis on 2026-10-02. The archive rewrite and bounded fixtures support
adopting A1 and A4. This checkpoint records the implementation and keeps the
fresh-run requirement explicit.

## Changes and consumers

- `src/commonplace/lib/agentic_records.py`: local and set checks reject ID
  ranges independently of endpoint resolution. Unresolved references suggest
  every declared ID with the same kind and number but a different analyst
  prefix; suggestions do not substitute or merge identities. `Part of:`
  requires one unindented field inside a declaration, containing exactly one
  full record ID and not naming itself. Existing reference resolution checks
  the target. Source quotations and fenced excerpts remain excluded.
- `src/commonplace/lib/agentic_workflow.py`: returning reconciliation rounds
  now receive the same reference and syntax checks as non-returning rounds.
  This closes audit finding 2 in [the separate audit](./skill-inconsistencies.md),
  which directly affected the commissioned checks. Other audit findings
  remain follow-ups.
- The [shared record contract](../../agentic-systems/instructions/agentic-analysis-records.md)
  is consumed through declared dependencies by analysts, reconciliation and
  verification. It now distinguishes identity, single-parent containment and
  overlapping groupings. Splits supersede only by already-declared parts;
  reconciliation cannot allocate IDs. Missing parts are returned to memory
  when appropriate and permitted, or retained as explicit conflicts.
- The memory and epistemic job texts instruct analysts to declare material
  parts; reconciliation's job and type specify split ownership and missing-part
  handling; verification checks containment, cross-kind explanations and
  split evidence. No new namespace, member schema or correction round is added.

Containment and supersession identity remain semantic checks performed by
verification. Matching kinds, resolved IDs and passing scripted workers
cannot establish those findings independently.

## Verification

The record-check tests cover declared endpoint ranges, backticks and supported
abbreviated ranges; source-excerpt exclusion; multiple prefix suggestions;
valid, undeclared, self-referential and malformed parents; annotation placement;
indentation and duplicate fields. Workflow tests exercise reference refusal
on returning rounds, plus the three split dispositions recorded in the
[pre-adoption report](./pre-adoption-check.md).

`uv run pytest -q`: all 1,330 tests passed in 76.33 seconds. Ruff passed for
both changed runtime modules and both changed test files. Deterministic
validation passed for the shared record contract, reconciliation report type
and all nine job instructions, with zero failures or warnings. The jobs-only
scope reports orphan notices because their declared consumers are outside
that directory; those notices do not alter the validation result.

The historical archive copies in the pre-adoption report were checked before
range refusal was implemented. They retain method-era range syntax and type
paths as recorded evidence; this adoption does not certify them under the
new grammar or current member schemas.

## Next action

Commit the amended method and its acceptance evidence before opening a fresh
run. The run pins that method commit; do not change an existing run's method
identity to resume it. The fresh run must collect refusals with their stage
and check analyst use of the part/split rules. The identity-paragraph count
is a secondary measure. Workshop closure remains conditional on that evidence;
the workshop stays active at this stopping point.
