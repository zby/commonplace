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
  repairs considered, each judged against the archive evidence, with a
  current recommendation; nothing adopted.
- [Split-records proposal](./split-records-proposal.md) — the recommended
  option: a declared `Part of:` relation, splits as supersession by
  already-declared parts, and no ID allocation by reconciliation.
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

Next, in order:

1. **A1, refusal hints and range detection.** Two separate checks. When
   an ID is unresolved, name the declared ID that differs only by prefix.
   Independently, refuse range syntax (`RT-RTE-1 through RT-RTE-4`,
   `RT-RTE-1–RT-RTE-4`) wherever it appears: a range whose endpoints both
   resolve passes the reference scan today even when the IDs between them
   do not exist, so the hint cannot hang off the unresolved case. Code and
   tests only.
2. **Pre-adoption check of the proposal**, the three steps under "Check
   before adoption" in the [proposal](./split-records-proposal.md): the
   archive rewrite with runtime IDs normalized to `RT-` first and one
   deliberately missing target; bounded workflow-test fixtures for a split
   into declared parts, a missing part with memory return, and a missing
   part retained as an unresolved conflict; then a fresh run.
3. **Adopt the proposal** if the check holds: edit the record contract, the
   memory and epistemic job texts, the reconcile job and report type, and
   the verify job as listed in the proposal; add only the `Part of:` syntax
   check, since target resolution is already covered.
4. **First run under the amended method** (step 3 of the check). Collect
   any refusals with their stage; the identity-paragraph count is a
   secondary measure. This is also the first run under the `RT-` grammar,
   so it tests reservation 3 of the prefix change (forgotten `RT-` on
   citations).
5. **Close.** Closure evidence is the split fixtures passing and the fresh
   run producing no new ID errors; a run that happens to contain no split
   does not by itself show rule 2 and rule 3 work. Record the decision in
   a commit per the closure section below and delete the workshop. Options
   B, C9 and D10 stay unadopted unless step 4 produces a refusal that
   points at the grammar, numbering, or parallel-analyst duplicates.

The operator's original error reports are on a machine not currently
accessible; if they reappear, add them to the problem file before step 3.

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
