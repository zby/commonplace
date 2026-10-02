# Analyse-agentic-system amendments

## Commission

Opened on 2026-10-02 at the operator's request. Examine amendments to the
live [`analyse-agentic-system` skill](../../agentic-systems/instructions/analyse-agentic-system/SKILL.md),
starting with its shared record ID system. The operator has encountered ID
errors and wants the scheme simplified. This workshop investigates the errors
and chooses a repair before changing the live method.

The earlier [construction workshop](../analyse-agentic-system/README.md)
records how the skill was developed. This workshop concerns changes to the
method now in use. It does not commission an analysis run, alter a retained
analysis, or adopt an ID design by opening.

## Files

- [Problem](./problem.md) — the starting problem, the unowned split
  declaration, the evidence read from the archived results, and the
  questions to settle.
- [Fix options](./fix-options.md) — verified workflow context and the
  repairs considered, each judged against the archive evidence, with
  dispositions of the considered repairs; A1 and A4 are adopted.
- [Split-records proposal](./split-records-proposal.md) — the recommended
  option: a declared `Part of:` relation, splits as supersession by
  already-declared parts, and no ID allocation by reconciliation.
- [Pre-adoption check](./pre-adoption-check.md) — normalized archive copies,
  seven declared part relations, negative target checks and three bounded
  workflow fixtures; also records the limits of scripted acceptance.
- [Implementation check](./implementation-check.md) — adopted method changes,
  their consumers, verification and the stopping point before a fresh run.
- [Skill inconsistencies](./skill-inconsistencies.md) — read-only audit of
  the live skill's job texts, types, schemas, contracts and operator docs
  against the code, with a suggested fix order before the next test run.

## State and next actions

Done:

- `4e5b5d9ae` (2026-10-02): `RT-` prefix for runtime records. Adopted
  before the evidence below was collected; kept, not counted as the repair.
- `931765b02` (2026-10-02): prefix mandatory in the grammar, bare-ID
  backcompat removed, bare `####` headings under `## Shared records`
  refused by name.
- `6fd147f59` (2026-10-02): archive evidence recorded in the
  [problem](./problem.md#observed-evidence); options rejudged; proposal
  rewritten around `Part of:`.
- 2026-10-02: archive rewrite and bounded fixture updates executed at the
  operator's request. The copied sets resolve all 53 and 34 declared IDs;
  seven records become parts and both duplicate supersessions remain. See
  [pre-adoption evidence](./pre-adoption-check.md) for checks and test results.
- 2026-10-02: the operator authorized implementation through the point before
  a new run. A1 refusal hints/range detection and A4 part/split rules are
  implemented in the checker, shared contract, analyst jobs, reconciliation
  type and verification job. Reference checks now also run on returning
  reconciliation rounds. See [implementation checks](./implementation-check.md).
- 2026-10-02: the operator commissioned the minimal pre-run adoption plan.
  Its four repairs are implemented: explicit run identity and early member
  identity checks, amendment-index placement inside Source register,
  reconciliation anchor acceptance checks, and clarified heading/read order.
  Acceptance evidence is recorded in [implementation checks](./implementation-check.md).

Next, in order:

1. **First run under the amended method** (step 3 of the acceptance checks).
   The implementation is committed before opening a run, which pins that
   commit. A new run was explicitly outside this implementation commission.
   Collect
   any refusals with their stage; the identity-paragraph count is a
   secondary measure. This is also the first run under the `RT-` grammar,
   so it tests reservation 3 of the prefix change (forgotten `RT-` on
   citations).
2. **Review the new evidence, then close.** Reconsider deferred audit items
   using the run's refusals and verification findings before deciding what
   needs follow-up. Closure evidence is the split fixtures passing and the fresh
   run producing no new ID errors; a run that happens to contain no split
   does not by itself show rule 2 and rule 3 work. Record the decision in
   a commit per the closure section below and delete the workshop. Options
   B, C9 and D10 in the fix options stay unadopted unless step 1 produces a refusal that
   points at the grammar, numbering, or parallel-analyst duplicates.

The operator's original error reports are on a machine not currently
accessible; if they reappear, add them to the problem file before the fresh run.

## Minimal pre-run adoption plan

Prevent known late failures and misplaced generated content with local changes
to the existing workflow. Item numbers below refer to
[the skill audit](./skill-inconsistencies.md), not the fix-options numbering.
Items 2 and 7 were already resolved by `4807abb47`; their tests remain.
The operator subsequently authorized implementing this plan. All four repairs
below are implemented; validation evidence is retained in the
[implementation check](./implementation-check.md). The fresh run stays separate.
The audit remains a record of its original method boundary. This plan governs
the adopted pre-run scope instead of its broader suggested order.

### Adopt before the run

1. **Check member identity at acceptance (item 1).** Supply `run-id` explicitly
   in job parameters and document it in the common worker rules. In
   `pass_refusals`, compare the member's `run-id` and `reviewed-boundary`
   with the run identity and accepted boundary. Refuse mismatches while that
   analyst can still repair its output. Keep the existing set check. Test
   each mismatch separately and a matching member; verify all three analyst
   jobs use this acceptance path.
2. **Place the amendment index explicitly (item 3).** Render the generated
   line inside `## Source register`, after its supplied content. Do not rely
   on the order of sections in the boundary result or add a new boundary
   ordering requirement. Test both permitted section orders and require the
   index exactly once under Source register, with source rows preserved.
3. **Reject ranged prose anchors during reconciliation acceptance (item 5).**
   Reuse `source_anchor_refusals` for returning and non-returning outputs.
   Keep its current syntax and quotation exclusions. Test both paths with a
   prohibited anchor and retain acceptance of permitted quote attributions.
4. **Clarify two existing instructions (items 4 and 6).** State that
   Reconciliation precedes the optional memory-return section, and make an
   order refusal name that requirement. Say explicitly in the generated
   prompt that the named job instruction is read before the reading batches.
   Keep batching and accepted heading structure unchanged. Use existing
   refusal and prompt tests where applicable.

Expected implementation scope is `src/commonplace/lib/agentic_workflow.py`,
the worker rules and reconcile job under
`kb/agentic-systems/instructions/analyse-agentic-system/jobs/`, their existing
tests, and workshop status. Local implementation choices are open within
these outcomes. If a fix requires new report syntax, schema policy, shared
parser changes or workflow stages, record the obstacle and return it for
decision rather than extending this plan. Item 1 has priority if work stops
early; report any incomplete item before treating the plan as finished.

### Validate and stop

Run the focused workflow tests, then `uv run pytest -q` and
`uv run ruff check .`. Validate changed KB documents with
`commonplace-validate`. Record results and remaining limits in the workshop.
The implementation is ready when the regression cases pass and the selected
defects are fixed within the stated scope. Commit the method changes before
opening the next run so it pins the completed method. Starting that run is a
separate action; this plan neither selects a source nor launches it.

### Defer until after the full run

Defer schema alignment and metadata policy (8–10), new annotation, amendment
and absence checks (11–14), and source-path detection and verification
(15–16). Item 16 is a confirmed parser gap, but broadening the shared anchor
recognizer needs false-positive checks; it is outside this minimal workflow
repair. Existing semantic requirements remain mandatory even where code
does not enforce them.

During the run, retain refusal text, job and round, the offending output,
the repair made, and verification findings about these deferred items.
After the full run, use those cases to select the next bounded changes.
A run with no relevant case does not establish that a gap is harmless or
justify implementing the whole deferred list. Preserve any needed follow-up
before deleting this workshop at closure.

## Evaluation boundary

Use the live skill, its job instructions, member types, record contract, and
the code that validates and consumes records. Inspect concrete error evidence
and a small representative set of record interactions. Judge proposals by
whether an analyst can assign IDs reliably, another analyst can identify the
same referent, reconciliation can express the required changes, and readers
can resolve every retained reference.

Keep the run ID, source identity, and `SRC-*` source register separate from
the shared record question unless evidence shows they contribute to an
error. Existing retained sets are frozen evidence; any new grammar needs an
explicit reading path for them. The method commit pinned by an open run is
not changed to make that run resume under a revised method.

## Closure

Close with a concrete decision: a simpler record and reconciliation contract,
or a reasoned decision to keep the present scheme with targeted repairs.
Name the affected instructions, types, validators, and consumers; show how
the chosen rules handle ordinary declarations, cross-member references,
corrections, and splits. Record the observed errors separately from predicted
failure modes. Promote an adopted design through the live method and its
affected interfaces, then remove this workshop and its active-list entry.
