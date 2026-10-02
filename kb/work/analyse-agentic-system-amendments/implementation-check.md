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

## Minimal pre-run adoption

The operator separately authorized the README's bounded pre-run plan on
2026-10-02. All four repairs are implemented within its stated scope:

- Every generated job prompt supplies `run-id`; the common worker rules
  define it. All three analyst acceptance paths compare member `run-id` to
  the run state and `reviewed-boundary` to the accepted boundary, before
  accepting the member. The later whole-set identity check remains.
- Overview rendering inserts the amendment index inside Source register,
  after the supplied source content, in either permitted boundary-section
  order. Boundary ordering and member syntax are unchanged.
- Reconciliation acceptance applies the existing prose-anchor check to
  returning and non-returning outputs, preserving its quotation exclusions.
- The reconcile job and order-refusal message state that Reconciliation
  precedes the optional memory return. Every generated prompt explicitly
  requires reading the named job instruction before the existing reading
  batches; batching and dependency membership are unchanged.

Regression cases separately corrupt each identity field for runtime, memory
and epistemic jobs, verify refusal before reconciliation and repair to a
published matching set, and assert the explicit run parameter. Two completed
fixture runs verify amendment-index placement and source-row preservation
under both boundary orders. Returning and non-returning reconciliation
acceptance cases cover prohibited prose anchors and permitted quote
attributions. The order-refusal case and existing per-job invocation tests
cover the instruction clarifications.

The final focused run passed all 106 workflow tests in 47.72 seconds.
`uv run pytest -q` passed all 1,343 tests in 87.85 seconds.
`uv run ruff check .` passed. Validation of the two changed job instructions
passed with zero failures or warnings; workshop framing and this report are
validated separately before committing.

The remaining audit items 8–16 stay deferred under the README's scope; no
schema, shared parser, stage or report syntax changed. These scripted checks
verify the workflow repairs, not model behavior in the later full analysis.
No fresh analysis is opened by this commission.
