# Report-correction implementation plan

## Commission and authority

The operator asked for this plan on 2026-10-05, after stating the intent to
implement report corrections now. The plan covers the first change only. It
has two parts that depend on each other: record-verifier findings go to the
report's declaring analyst, who writes a corrected report, for all three
analyst reports; and reconciliation is narrowed to reconciling, leaving
judgment of each report's support to the verifier.

Implementation starts when the operator accepts this plan. A live analysis
run, publication and integration each need their own authorization. Nothing
here permits changing or resuming an existing run, its worktree or a retained
set.

Read the [design brief](../../reference/agentic-system-analysis-design-brief.md)
and [method maintenance](../../agentic-system-analyses/instructions/maintain-analysis-method.md)
before editing. The [corrections candidate](./versioned-corrections-for-agentic-analysis-reports.md)
gives the design reasoning; where it and this plan differ, this plan sets
the scope of the first change.

## Why now

Four runs used the committed classification revision (method `b95a2bb79`):

| Run | Outcome | Record loop |
|---|---|---|
| `AAS-2026-10-05-dynamic-cheatsheet-39e1e27ebdc0-01` | complete | one round, no blockers |
| `AAS-2026-10-05-dynamic-cheatsheet-fabd993043b5-01` | stopped | three rounds |
| `AAS-2026-10-05-graphiti-0b7292fa4af1-01` | stopped | three rounds |
| `AAS-2026-10-05-dynamic-cheatsheet-56ba8ab235b8-01` | blocked | no outputs; cause not examined |

Both stopped runs ended on the same defect. Reconciliation amended a record,
and each later verification found report text that still asserted the old
value. In the Dynamic Cheatsheet run the stale text was first another runtime
field and then sentences in the memory report; amendments grew from 6 to 9
to 10. In the Graphiti run it was the epistemic ledger and conclusion.
Neither run returned anything to the memory analyst.

These observations come from the verifications' Blockers sections in the
run worktrees under `.commonplace/worktrees/`. They are two cases, read once,
not a controlled comparison. The models used were not checked.

## Result required

A correction changes the report that made the claim. Later jobs read one
current version of each report and apply no value overlay. Each role has one
function: the reconciler connects, the verifier judges, the declaring analyst
corrects.

1. **Addressed findings.** Each record-verifier blocker names its addressee
   in a form code reads without interpreting prose: one of the three analyst
   reports, or the reconciliation. A blocker without a valid addressee is
   refused at acceptance.
2. **Correction by the declaring analyst.** For each analyst report named,
   code runs that analyst again with its previous report, the blockers
   addressed to it and the current versions of the reports it reads. The
   analyst returns a complete report. It answers each blocker with a
   correction carried through dependent text, or with a reason for keeping
   the finding. The answers reach the next reconciler and verifier and are
   not part of the published report.
3. **Order inside one cycle.** Memory and epistemic analysts read the runtime
   report. When the runtime report is named, its correction finishes before
   the others start, and they read the corrected version. Corrections that do
   not depend on each other run in parallel. One cycle counts once.
4. **One current version.** Every version of every report is kept in the run
   directory under a round-numbered name, as memory reports are today. Code
   makes the latest accepted version current in the output set. Later jobs
   and publication receive only current versions. The published set does not
   contain predecessors.
5. **Reconciliation after correction.** A new reconciliation runs after each
   correction cycle and before the next verification. It also answers
   blockers addressed to it.
6. **Reconciliation only reconciles.** Its subject is the relations between
   reports: which records name the same thing, which are parts of others,
   where analysts converged independently, and where two reports disagree.
   - It does not judge whether one report's finding is supported by the
     sources, and it has no duty to find or repair unsupported assertions or
     coverage gaps inside a single report. Today's instruction gives it that
     duty; the verifier already has it and keeps it.
   - It does not replace a record's value and does not return findings to
     the memory analyst. It describes a cross-report disagreement, with the
     records and evidence on each side, for the verifier to assess.
   - Rules that constrain its own statements stay: it must not strengthen a
     finding, erase stated uncertainty or drop an unresolved part when it
     connects records.
   - After blockers, it answers only those addressed to reconciliation.
7. **Verifier reads text.** The verifier judges current reports as written.
   For each corrected report it also receives a code-computed difference from
   the predecessor. The rule to judge records as amended is removed.
8. **Same limit.** The loop keeps three verifications. Blockers at the third
   stop the run, as now.

Not in this change: coordinator disposition of nonblocking findings and the
[publication policy for unresolved issues](../../reference/proposals/publishing-analyses-with-unresolved-issues.md).
Keeping them out lets a trial attribute its outcome to report correction.
Also not included: declared dependency fields between findings, a durable
archive of predecessors, corrections written by an editor, and changes to the
profile or synthesis loops.

## Choices fixed by this plan

- **Judging moves wholly to the verifier.** The reconciler sees cross-report
  disagreements first because connecting reveals them, and it reports them.
  Whether either side is right is the verifier's judgment. This removes the
  reconciler's first, non-independent pass of judging and correcting. Its
  cost is that a defect the reconciler would have caught now waits for the
  verification; the trial records whether that uses rounds.
- **Supersession stays in reconciliation.** A statement that one record is
  the same as, or replaced by, other declared records is a connection between
  reports. It keeps the existing `Amendment:` supersession form and the
  overview's index line, so retained sets and their validation are unchanged.
  Only value-changing amendments are retired.
- **Declared IDs survive correction.** A corrected report keeps every record
  ID its predecessor declared, because other reports cite them. It may
  declare additional records. A correction that seems to need a record
  removed is a decision return.
- **A successor passes the original's acceptance check.** The same quotation,
  citation and declaration checks apply, plus the ID rule above.

## Affected consumers

This is a starting inventory from a search for the amendment and return
vocabulary. Search again before editing; it is not an allowlist.

- **Scheduler:** `src/commonplace/lib/agentic_workflow.py`. The record loop
  in `run`, the memory, runtime, epistemic, reconcile and verification job
  builders, the reconciliation and blocker validators, round closing, and
  the job-name mapping used on resume.
- **Records code and validation:** `amendment_index` in
  `src/commonplace/lib/agentic_records.py` and its check in
  `src/commonplace/lib/validation.py`.
- **Job instructions** under
  `kb/agentic-system-analyses/instructions/analyse-agentic-system/jobs/`:
  `verify.md`, `reconcile.md`, `runtime.md`, `memory.md`, `epistemic.md`,
  and the "resolve amendments" sentences in `profile.md`, `synthesize.md`,
  `verify-profile.md` and `verify-synthesis.md`. Check `worker-rules.md`
  for the correction-round rules analysts need.
- **Contracts:** the amendment section of
  `kb/agentic-system-analyses/instructions/agentic-analysis-records.md`, and
  the reconciliation, overview, runtime, memory and profile type specs under
  `kb/agentic-system-analyses/types/`.
- **Readers of published sets:** `scan-agentic-system-transfer` and
  `synthesize-agent-memory-landscape` describe what the reconciliation
  member holds. They must still read sets published before this change.
- **Decision record:** a new ADR revising ADR 096's rule that analyst reports
  are not rewritten and ADR 098's correction organization.

## Acceptance

Deterministic cases, using the workflow test fixture with scripted workers:

1. A blocker addressed to the epistemic report runs an epistemic correction.
   The next reconciliation and verification read the corrected report, and
   the predecessor file remains.
2. Blockers addressed to the runtime and memory reports in one cycle: the
   runtime correction finishes first, the memory correction reads it, and the
   cycle counts once.
3. A blocker addressed only to reconciliation runs no analyst job.
4. A corrected report that drops a declared ID, breaks a citation in another
   report or fails a quotation check is refused, and the current set is
   unchanged.
5. A declined blocker leaves the report bytes unchanged, and the reason
   reaches the next verification.
6. Blockers at the third verification stop the run before profile.
7. A blocker with a missing or unknown addressee is refused.
8. A reconciliation with a value-changing amendment or a return section is
   refused; a supersession is accepted and indexed.
9. Profile, synthesis and publication receive exactly the versions the last
   verification judged.
10. An interrupted run resumes at the right job for every new job name.
11. The retained `dynamic-cheatsheet` set still validates unchanged.

Then run `uv run pytest` and `uv run ruff check .`; all required tests pass.
Run `commonplace-validate` on every changed KB file. Check each changed job
packet against the 24 KiB read budget, including the blocker list and the
difference file given to the verifier.

Instruction wording has no deterministic test. Review each changed
instruction against the two stopped runs' blockers: would the addressed
analyst have received what it needed to fix the stale text? Review the
reconciliation instruction sentence by sentence: each remaining duty concerns
a relation between reports or a limit on the reconciler's own statements,
and every single-report check it loses is present in the verifier's
instruction. Passing fixtures show interface behavior, not that a model will
correct well or that a reconciler will stay within its role.

## Trial, separately authorized

After the method commit, the comparison runs are Dynamic Cheatsheet at
`5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9` and Graphiti at
`4083f51812d381d7ca28b887cfa3c3db188f576d`, with the model of the two stopped
runs once that is established from their records. Record for each run:
verifications used, blockers per verification, blockers that repeat an
earlier one, corrections declined, analyst jobs added, and the outcome. Also
record what each reconciliation contains: connections and disagreements
only, or judgments about a single report's support.

Two stopped baselines and two new runs cannot establish a rate. A run that
finishes shows the path works on that case. The trial should also show
whether a third verification still finds dependents of an earlier
correction, which bears on whether dependencies need to be declared.

## Coordination

Other sessions commit to this checkout. Check status and the latest commits
before writing. One implementer owns `agentic_workflow.py` and the job
instructions for the duration; do not merge independent rewrites of them.
Commit code, instructions, contracts and tests together so that no committed
revision has a scheduler and instructions that disagree. Do not open a run
from an uncommitted method.

## Decision returns

Stop and return to the operator when:

- the workflow engine cannot express conditional, ordered correction jobs or
  their resume without an engine change;
- a correction needs a declared record removed or renamed;
- supersession and value amendment cannot be told apart by a check;
- a job packet exceeds the read budget after the change;
- readers of previously published sets cannot support both forms without a
  compatibility branch;
- the work would require the publication policy or declared dependencies to
  be acceptable.

A partial result names what is implemented and checked and what remains.
