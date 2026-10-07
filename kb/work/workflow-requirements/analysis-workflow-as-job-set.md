# The analysis workflow as a job set

A definition of `analyse-agentic-system` in the terms of
[requirements](./requirements.md), written against the working-tree
implementation of 2026-10-07 (`src/commonplace/lib/agentic_workflow.py` and
the set type's layout). The spec is not changed here; where the mapping
needs something the spec does not give, the need is reported under
[Spec needs](#spec-needs) with a fallback that stays inside the spec.

## Conventions

- **Directory.** The run directory `state/<run-id>/`. Its `output/` is the
  typed set; state, versions and candidates live beside it. The job set is
  a file under the workflow's instructions that names the set type, and
  the run's metadata names the job set, as the spec's decisions require.
- **Member.** The current accepted version at a slot in `output/`. A model
  job's output is a candidate until a code job accepts it.
- **Reads.** A job's declared reads are current members or run files. They
  are the rerun triggers of requirement 4. Method files (the job's
  instruction, worker rules, contracts) are reads of every model job, so a
  method edit reruns the job, following the criteria rule.
- **Check jobs.** Every member-producing model job has a paired code job
  that reads the candidate, the members its role relates to and the type
  contracts it applies, validates the candidate at its slot, and accepts
  it against those reads, naming the relations it checked, or refuses it
  with the findings. Declaring the contracts as reads is what makes a
  criteria edit rerun the check and stop the old acceptance holding. This is the one judging pattern; the engine knows
  nothing of it. A declaration default could generate these pairs.
- **Apply jobs.** A verification is a model-written verdict document. A code
  job reads it and turns its blockers into refusals of the members they
  address, each scoped to the relation between the member and the
  verification. It reads the verifier's attempt record and the members at
  the versions that record pinned, not the current ones, so its judgments
  are about what the verifier saw and it reruns whenever the verifier
  judged different inputs, even to identical verdict text; pinned
  hand-outs make the two differ without any operator involved (scenarios
  21 and 22). The versions come from the engine's record, never from the
  verification's text. Only code jobs judge; model jobs write documents.
- **Check jobs read the refusal they answer.** This makes a check rerun on
  every refusal and re-accept the standing version. Under scoped
  supersession that acceptance cancels nothing and resets nothing, so the
  rerun is a redundant record, not a defect. Dropping the read would need
  another way to compare `answers.md` with the blockers.

## Jobs

Members are named by role. `+prev` means the job's own previous version
(S3). `findings` means the refusal findings the engine supplies to a rerun.

| Job | Kind | Reads | Writes or judges | Bound |
|---|---|---|---|---|
| open | code | run parameters, repository state | `run-metadata.json`; refuses to start on an unpublishable worktree or changed package | – |
| acquire | code | run-metadata | `source.json`; external effect: frozen checkout under `related-systems/` | – |
| boundary | model | run-metadata, source.json, source text | candidate boundary | 2 |
| check-boundary | code | candidate, run-metadata, source.json, checkout state | accepts boundary against those, or refuses | |
| runtime | model | boundary, findings | candidate | 3 |
| memory, epistemic | model | boundary, findings; runtime as context only (S8) | candidate, and `answers.md` on a rerun | 3 |
| check-\<report\> | code | candidate, boundary, the reports it cites, answers, the refusal it answers (S4) | accepts the report against those; refuses when the slot check fails, a declared record ID was dropped, or answers do not match the blockers | |
| reconcile | model | boundary, runtime, memory, epistemic, findings, +prev | candidate reconciliation | 3 |
| check-reconciliation | code | candidate, boundary, reports | accepts or refuses | |
| verify-records | model | boundary, reports, reconciliation, answers, +prev | candidate record-verification | 3 |
| apply-record-verification | code | candidate, its attempt record, reports, reconciliation at the pinned versions | accepts the verification against them; for each blocker, refuses the addressed member against the verification with the blocker as findings; with no blockers, accepts each report and the reconciliation against the verification | |
| profile | model | boundary, reports, reconciliation, findings, +prev; required: each report and the reconciliation accepted against record-verification | candidate memory-profile | 3 |
| check-profile | code | candidate, boundary, memory, reports | accepts or refuses; comparison version and source identity are part of the slot check | |
| verify-profile | model | memory-profile, reports, +prev | candidate profile-verification | 3 |
| apply-profile-verification | code | candidate, its attempt record, memory-profile at the pinned versions | accepts the verification; refuses the profile on blockers; accepts the profile against the verification otherwise | |
| synthesize | model | boundary, reports, reconciliation, record-verification, profile-verification, findings, +prev; required: the record acceptances above and memory-profile accepted against profile-verification | candidate synthesis | 2 |
| check-synthesis | code | candidate, boundary, reports | accepts or refuses | |
| verify-synthesis | model | synthesis, reports, record-verification, profile-verification, +prev | candidate synthesis-verification | 2 |
| apply-synthesis-verification | code | candidate, its attempt record, synthesis at the pinned versions | accepts the verification against the synthesis; refuses the synthesis on blockers or on a limit the synthesis does not carry; accepts the synthesis against the verification otherwise | |
| assemble | code | all members; required: the holding acceptances covering every declared relation of every member | `overview.md`, `ARTIFACT.yaml` with pins; accepts the overview against the members | – |
| publish | code | all members, manifest, run-metadata; required: the same acceptances plus the overview's | checks method and package unchanged and the incumbent digest; external effect: writes `retained/<slug>/`, archives the incumbent | – |

Bounds are today's rounds plus one: three attempts where two correction
rounds exist, two where one does, two for the boundary to allow one retry.
Code jobs carry none; each failure stops the invocation. Bounds count
attempts in the run and never reset, so a structural acceptance between
corrections does not replenish them. Exceeding a bound stops the
command, replacing `StopRun`. Structural refusals and verifier blockers now
share one bound per job; today they draw on separate engine and workflow
budgets.

## How a run proceeds

**Opening.** `open` and `acquire` run on the first invocation. The boundary
is handed out. Its check accepts it against the run metadata, the frozen
source record and a clean checkout. Members not required under the
boundary's disposition have no ready jobs (S7); a non-complete run goes
straight to `assemble`.

**Records.** `runtime` runs; its check accepts it. `memory` and `epistemic`
run with the runtime report exposed as context, not as a read (S8).
`reconcile` runs once the three reports are members, then `verify-records`.
`apply-record-verification` accepts the verification against the reports
and reconciliation it judged, then either refuses the addressed members or,
with no blockers, accepts every report and the reconciliation against the
verification. That second acceptance is what "records settled" means.

**A correction round is nothing but the currency rule.** A refused report's
job is ready again with the blocker as findings. Its rerun writes a new
report and `answers.md`. The check compares the answers with the blocker
and refuses a "corrected" answer whose report is byte-identical. Acceptance
replaces the member. The reconciliation's read changed, so `reconcile`
reruns; then `verify-records`, whose reads changed too. The verification's
earlier acceptance no longer holds and is replaced. The loop ends when
a verification has no blockers, or a bound is hit. No packets, round
numbers, set-check files or change diffs exist. The verifier reads the
answers and its own previous version (S3) and judges afresh, as its
instruction says today.

**A blocker addressed to the reconciliation** refuses the reconciliation
only. Its rerun reads the unchanged reports and the findings.

**Profile and synthesis** follow the same pattern with one verification
each. The synthesis loop carries the type's limits relation: the apply job
refuses a synthesis that does not carry a verification limit, so the
synthesis reruns with that finding and the verification follows.

**Assembly and publication.** `assemble` runs when every complete-disposition
member has a holding acceptance against the members it relates to, and
writes the overview and the pinned manifest. `publish` rechecks the
condition over the whole set and copies the current versions out. Its
environment checks and its external effect follow requirement 8: an
outcome that cannot be established stops the command for the operator.

**What the operator can do.** Refuse any member from the command line with
a reason; its job reruns with that reason as findings. Accept a member
against stated inputs to override a check. Both leave the same record as a
job's judgment.

## What disappears

Round counters and versioned filenames at the run root; the request
packet, change diffs and `set-check-<n>.md`; the `LATER_ROLES` filter and
the type-only manifest override, since checks read declared members only;
the engine's retry and repair limits and `StopRun`; the verifier residue
that structural failures need explicit blockers, since structurally
refused candidates never become members; the `acceptance-measurements`
record, since a worker's self-check is the same check job's validation run
by hand and the engine keeps every judgment.

## Spec needs

Each item names the need, where the mapping hit it, a proposed change, and
the fallback inside the current spec. **Status after the 2026-10-07
amendment** (judgments are declarable reads; reads are required or
optional; a job's refusals are one versioned read whose current version is
the latest refusal of its latest completed output, and a read that has
become absent has not changed):
all items except S5 are resolved (requirement numbers inside the items
predate the split of 5 into 5 to 7): S8 by requirement 2, which makes a
model job's undeclared context untracked by design; S3 by requirement 3,
which supplies a rerun with its previous output by identity; S7 by
requirement 4, which leaves a job unready when the type does not require
its member. S5, previous versions as reads, stays deferred with the change
diff it served. The items are
kept as written for the record.

- **S1. Absent inputs.** Not needed once S4 and S6 hold: every read above
  is of a file that exists before the job is ready. Recorded so the
  question stays answered: no optional reads are required.
- **S2. Acceptances compose.** Requirement 7 asks for "a current acceptance
  against every relevant input". A member's acceptances come from several
  jobs: the check job accepts a report against the boundary and its cited
  reports; the apply job accepts it against the verification. Proposal:
  state that coverage is the union of a member's current acceptances.
  Fallback: one job re-accepts against everything at assembly, which
  duplicates every relation check in one place.
- **S3. A rerun reads its own previous version.** Reconcile, the verifiers,
  the profile and the synthesis all read their previous output on a
  correction today, and the verifier's instruction depends on it.
  Proposal: a rerun may read the previous version of its own output; it is
  not a read for currency, since it cannot be. Scenario 2 states the
  constraint: the previous version must reach the rerun pinned by
  identity, as the refusal carries the refused version, never as a read of
  the slot the job writes, or each acceptance would rerun the job.
  Fallback: none inside the spec; the instructions would have to drop
  their use of the previous version.
- **S4. Judgment records are readable.** The check job for a corrected
  report must compare `answers.md` with the blockers that refused it, and
  the verifier reads the same blockers. Proposal: a judgment record is a
  file a job may declare as a read. Fallback: the apply job writes a
  requests file beside the refusal, duplicating the findings.
- **S5. Previous versions as reads.** Needed only for the change diff,
  which this mapping drops. If a reviewer wants diffs back, a code job
  would need to read a non-current version. Proposal deferred.
- **S6. Acceptance-gated readiness.** `profile` and `synthesize` must not
  run while the record verification still has blockers, and the synthesis
  must wait for the profile verification. With readiness by file
  existence alone, both run on a verification that still carries blockers
  and rerun after each round, at model cost. Proposal: a read may require
  that the member be currently accepted against named inputs, for example
  "reports accepted against record-verification". Fallback: the apply job
  writes a marker file only when no blockers remain, and the gated job
  reads the marker. The marker is a judgment in disguise.
- **S7. Disposition gates jobs.** A non-complete boundary must leave the
  analysis jobs unready. The type already says which members a
  disposition requires. Proposal: a job producing a member the current
  disposition does not require is not ready. Fallback: every analysis job
  reads the boundary and the hand-out tells the worker to stop, which
  spends a hand-out to do nothing.
- **S8. Context without currency.** `memory` and `epistemic` read the
  runtime report on their first run. Declaring it as a read makes a
  runtime correction rerun both, which today's rounds avoid: the verifier
  catches stale citations and the check job re-accepts cheaply. Proposal:
  a hand-out may expose files as context that are not declared reads;
  the type's relations, through the check jobs, remain the guard against
  inconsistency. This is a deliberate untracked read, so the spec should
  say it is allowed only where a relation check covers it. Fallback:
  accept the cascade and pay for the reruns.

## Type needs, not spec needs

- Requirement 7 needs "relevant inputs" per member to be computable. The
  layout declares identity and cites; the limits relation between the
  synthesis and its verification, the overview's amendment index against
  the reconciliation, and the profile's source identity against the memory
  report are prose. They should become declared relation partners.
- The memory analyst's provenance check named in the set type has no
  implementation in the workflow code. Either declare it or drop the
  sentence.

## Not determined

The exact publication guards in `publication.py` (`_check_incumbent`,
`require_method_unchanged`) were read at their call sites only. Whether
run-state validation runs outside publication is unknown. Neither changes
the mapping.
