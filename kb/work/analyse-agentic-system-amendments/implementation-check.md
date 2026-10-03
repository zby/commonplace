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
- The [shared record contract](../../agentic-system-analyses/instructions/agentic-analysis-records.md)
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

## Repository registration and whole-system coverage

On 2026-10-03 the operator authorized repairing the source-register ambiguity
identified in the Dynamic Cheatsheet audit. The boundary job's initial path
selection had become a binding allowlist, excluding shipped prompts and a
persistence caller from a result labelled `whole-system`.

The boundary and source contracts now register a Git repository at its pinned
commit. Listed paths describe initial inspection, not the files later jobs
may read. Workers may inspect and cite additional files at that commit and
record their coverage in their own members, using existing source IDs and
the passage's actual evidence layer. The selected target, source identity and
revision remain fixed. Captures remain limited to their frozen contents.

Before selecting `whole-system`, the boundary job inspects the tree and
traces shipped entry points and consumers. Its Boundary and evidence section
classifies each top-level tracked file or directory, names material paths,
and gives exclusions with prevented conclusions. For memory and knowledge
systems it must identify prompts and maintenance instructions, persistence
and reload callers, later consumers and evaluators. A shipped driver is not
an external host merely because it calls a library API.

Verification compares the classification with the frozen tree and actual
material wiring. It may inspect files omitted from the initial path list.
An individual finding can use the existing blocker/conflict process. An
incorrect frozen target or boundary-kind classification requires `problem`;
reconciliation cannot repair that metadata or make the wrong label acceptable
by adding a limitation. The worker rules and overview type agree with these
contracts. No runtime code, schema, report field, source ID allocation or
workflow stage changes.

The repaired instructions distinguish these concrete cases:

- A register initially lists README and API files: an analyst may inspect
  shipped prompt or caller files at the same commit without source expansion.
- Inspection finds a shipped persistence caller excluded from a purported
  whole system: the analyst identifies the responsibility and prevented
  conclusion; verification cannot silently certify that classification.
- The operator selected only the library API: the boundary states that target
  with a narrower kind; inspecting a caller for relevance does not authorize
  expanding the target.
- A newly required external repository, revision or capture remains outside
  the registered evidence boundary and requires the existing problem path.

Deterministic validation passed for all six changed method documents with
zero warnings or failures. `git diff --check` passed. This change is confined
to Markdown method documents and workshop records, so pytest is not required
under the repository's development rule. Validation checks the document
contracts; the concrete cases above are an instruction review, not a model
adherence test. The later `dynamic-cheatsheet-02` run remains the live test.
The completed `-01` set and review are unchanged and remain untracked by this
commission. The range, verification-output and candidate-identity repairs
are separate pending steps.

## Remaining repairs before the second full run

On 2026-10-03 the operator authorized the remaining fixes. The range checker
now permits ordinary `to` relations, including the audited
`EPI-OBJ-8 to RT-OBJ-1` false positive and `from RT-OBJ-1 to RT-OBJ-2`.
It continues to refuse explicit dash and `through` intervals, including
adjacent endpoints and shorthand. The proposed numeric-distance rule was
not adopted: adjacent dash ranges were real refused forms in the traces.

Regression cases reproduce the run's backticked runtime, memory and
epistemic ranges, shorthand and relation prose. An integrated fixture
confirms that verification prose comparing two records is accepted and
published without a verification retry. Both verification jobs now instruct
workers to list every ID in full, with refused `through` and adjacent dash
examples. The containment contract also states that a candidate that can
replace a record's referent is not thereby its part.

The first focused run exposed a mistake in the new fixture: its comparison
was put under Blockers rather than under the verification result. After that
fixture was corrected, its individual run passed. The full suite exposed an
existing instruction-composition test still requiring the old compact
allowlist; it now checks repository registration, unrestricted same-commit
inspection and the distinction between initial coverage and reading permission.
The final full suite passed all 1,362 tests in 91.43 seconds.
`uv run ruff check .` passed. The three changed method documents, workshop
README and recovery-history proposal validate with zero failures or warnings;
this report is validated before committing. `git diff --check` passed.

The published `-01` set and review validate cleanly and were committed
unchanged in `0f49f426a`, separately from method fixes. The retained manifest's
member hashes and the review's manifest hash remain unchanged. Its source
omissions remain evidence; the next run must supersede the review.

[Workflow recovery history](../../reference/proposals/workflow-recovery-history.md)
records the need for observable recovery evidence, manual audits, a derived
summary and separate engine-event retention. It names consumers, coverage
limits and adoption criteria without selecting a storage implementation.
Worker-side preflight tooling, run-state storage changes and deferred audit
items 8–16 remain unadopted.

All pre-run fixes are now implemented. No new analysis run was opened. The
full `dynamic-cheatsheet-02` run must still test model adherence: whole-system
coverage including shipped prompts and `run_benchmark.py`, verification without
range retries, and correct candidate-versus-admitted containment. Deterministic
tests establish the parser and workflow behavior, not those live outcomes.
