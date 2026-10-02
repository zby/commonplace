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

Next, in order:

1. **First run under the amended method** (step 3 of the acceptance checks).
   The implementation is committed before opening a run, which pins that
   commit. A new run was explicitly outside this implementation commission.
   Collect
   any refusals with their stage; the identity-paragraph count is a
   secondary measure. This is also the first run under the `RT-` grammar,
   so it tests reservation 3 of the prefix change (forgotten `RT-` on
   citations).
2. **Close.** Closure evidence is the split fixtures passing and the fresh
   run producing no new ID errors; a run that happens to contain no split
   does not by itself show rule 2 and rule 3 work. Record the decision in
   a commit per the closure section below and delete the workshop. Options
   B, C9 and D10 stay unadopted unless step 1 produces a refusal that
   points at the grammar, numbering, or parallel-analyst duplicates.

The operator's original error reports are on a machine not currently
accessible; if they reappear, add them to the problem file before the fresh run.

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
