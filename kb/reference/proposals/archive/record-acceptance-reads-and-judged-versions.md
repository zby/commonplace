---
description: "Proposal: record what a job's acceptance validator read as part of its trace, recheck accepted jobs against that recorded context, and pin the exact member version each verification judged so a replacement marks the judgment stale."
type: reference/types/design-proposal.md
traits: [has-external-sources]
---

# Record acceptance reads and judged versions

> **Archived** (see [archive README](./README.md)). Retired by [ADR 113](../../adr/113-artifact-runs-execute-declared-plans-with-pinned-judgments.md): judgments record their basis from pinned inputs and a verifier's handed versions resolve from its attempt record, so the untracked validator read and the role-only verification this proposal repaired no longer exist. The 2026-10-07 replay-recheck engine, its reachable mismatch and the build-systems classification of that engine remain here — design texture only.

Make two additions to the analysis workflow's existing trace model, and no
new storage or commit protocol. First, what a job's acceptance validator
reads becomes part of the job's recorded trace, and the replay recheck of an
accepted job runs against that recorded context rather than the current set.
Second, a verification pins the exact version of the member it judged, so
replacing that member marks the judgment stale for publication.

This is a proposed design, not implemented behavior. It addresses the replay
blocker in [declared-layout adoption](../adopt-declared-layout-in-the-analysis-workflow.md).
An earlier version of this proposal answered the same blocker with fixed set
snapshots and explicit commits; that design is recorded under Alternatives.

## Current state (as of 2026-10-07)

The engine replays the workflow definition from its beginning on every step.
For each accepted job it compares the recorded input identity and output
digest with the current files and reruns the job's validator before
continuing. See `WorkflowEngine.judge` in `src/commonplace/workflow/engine.py`.
The input identity hashes the job's prompt, launch data and declared inputs
only.

In the vocabulary of [Build Systems à la Carte](../../../sources/build-systems-a-la-carte-theory-and-practice.ingest.md),
this is a restarting scheduler with a verifying-trace rebuilder: a per-job
record of input and output hashes, rechecked on each restart from the top.
The placement is this KB's mapping, not the paper's.

The uncommitted declared-layout implementation gives the synthesis and the
three verifications their own set slots. Workers write candidates outside the
set; the coordinator copies accepted bytes into `output/`. Correction jobs
keep separate output files; the slot holds the current accepted version. The
acceptance validator for a set member places the candidate's bytes at its
slot in memory and reads every other member from the current `output/`. See
`validate_draft_at_slot` in `src/commonplace/lib/validation.py`. Every byte it
reads passes through one reader on the validation run. The set's manifest
pins member digests at publication. A verification names the role it judged
(`verifies: records`, `profile` or `synthesis`) and nothing about which
version.

Code review found a reachable mismatch: a later synthesis verification can
declare a limit that the original synthesis does not carry. On replay, the
original synthesis candidate is placed at its slot beside that verification,
its validator refuses it, and the engine reopens the original job before
reaching the correction job. No regression test or model-backed run has
demonstrated this yet.

## Problem

The job's trace does not record what its acceptance validator reads. The
validator reads sibling members in `output/` that are not declared inputs. In
the paper's terms this is an untracked dependency: the trace cannot predict
the validator's verdict, so a sibling added later changes the verdict of a
job whose inputs are unchanged. The engine then reopens a job whose repair is
owned by a later correction job. Airflow's rule states the defect in one
line: a task must never read the latest data, because an update between
reruns changes its output.

Separately, a verification is a judgment of one version of a member, but it
records only a role. Replacing the member leaves no mechanical trace that
the verification no longer judges what is in the slot. Publication can then
present a stale judgment beside the replacement it never saw.

Dropping the replay recheck would hide both problems. The recheck is what
detects a damaged output and a changed validation rule.

## Candidate model

### Record the acceptance context

The acceptance validator is part of the task that produces the job, so its
reads belong in the job's trace. At acceptance, record every path the
validator read beyond the declared inputs, with its content hash, including
paths it found absent. Keep those bytes under the job's kept files so the
recheck can be exact.

On replay, the recheck of an accepted job compares declared inputs and the
output digest as it does today, then runs the validator against the recorded
context, not the current `output/`. A changed declared input reopens the job
as it does today. A recorded context read that now differs does not reopen
the job. It is context drift: reported, and left to the job that owns the
affected relation next, which is the correction job, or to whole-artifact
validation at publication.

The split between what is pinned and what is read live follows
[criteria edits invalidate verdicts; process edits invalidate artifacts](../../../notes/criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts.md).
Type contracts and validator code are criteria: they stay live, and a change
to them changes the verdict and reopens the job, as it does now. Sibling
members are context: they are pinned, because a later sibling is not a change
to the criteria the job was accepted under.

A recorded context read that is missing or altered on disk at recheck is
reported as such. The current `output/` is never substituted for it.

### Pin what a verification judged

When the coordinator accepts a verification, it records the content hash of
the member that verification judged. Code writes this record; the worker
does not declare it, because a hand-declared version is an unchecked copy
whose forgotten update leaves a stale judgment reading as current.

A verification is stale when the judged member's current hash differs from
the recorded one. Staleness is one hop: a stale verification is a reason for
a new verification, and nothing downstream of it is flagged until it is
replaced. Publication refuses a set with a stale verification. The set
relation that every declared limit is carried by the synthesis stays a
whole-artifact check at publication.

The synthesis sequence becomes:

| Execution | Recorded context | Result |
|---|---|---|
| Original synthesis | Reports and earlier judgments; verification slots absent | Synthesis A accepted |
| Synthesis verification | A at its hash | Verification V accepted, pinned to A |
| Synthesis correction | A, V and the correction request | Synthesis B replaces A; V is now stale |
| Correction verification | B at its hash | Verification V' replaces V, pinned to B |

On replay, the original synthesis is rechecked against its recorded context,
in which the verification slot is absent. V's presence is context drift for
that job, not a refusal. The correction job's own trace records A and V.

### What exact recheck does and does not cover

Exact recheck applies to validator verdicts, which are deterministic over
their reads. It does not apply to the model-written members themselves: a
repeated model call is a new attempt whose output can differ, so a recorded
context does not promise that rerunning a job reproduces its output. The
paper reaches the same boundary for non-deterministic tasks and replaces
exact equality with membership in the set of acceptable results; here that
membership check is the validator plus the verification.

## External design basis

[Build Systems à la Carte, journal version](../../../sources/build-systems-a-la-carte-theory-and-practice.ingest.md)
classifies build systems by scheduler and rebuilder, defines correctness as
exact recomputation from recorded dependencies, and treats untracked
dependencies, task versions and non-determinism as the cases where that
definition needs adjustment. It names three responses to an untracked read:
track it, mark the task volatile, or leave it untracked. The current engine
is the volatile case. This proposal is the tracking case. The paper does not
discuss workflow engines or acceptance validators; the application is ours.

[Dagster's asset versioning](../../../sources/dagster-asset-versioning-and-caching.ingest.md)
records, per materialization, which upstream data versions it consumed and
flags an asset as unsynced one hop at a time. The ingest's verdict is that
this workflow is a departure from Dagster's main path: Dagster's versioning
exists to skip deterministic recomputation, and its default data version
assumes equal inputs give equal output, which model-written members break.
What transfers is the bookkeeping kernel only: a content fingerprint per
member, recorded by each judgment that consumed it, compared one hop at a
time. Nothing else of Dagster is proposed.

[Airflow's retained guidance](../../../sources/apache-airflow-best-practices.ingest.md)
supplies the fixed-partition rule and the warning against reading latest
data. [Iceberg's reliability account](../../../sources/apache-iceberg-reliability.ingest.md)
was the basis of the earlier snapshot-and-commit version. Its protocol serves
many writers over shared storage. This workflow has one coordinator under a
run lock with whole-state atomic writes, so that protocol answers a need the
workflow does not have.

These are official design accounts, not experiments demonstrating that the
proposed model works here.

## Alternatives and operativity

| Option | Consumer and force | Trade-off |
|---|---|---|
| Record acceptance reads and pin judged versions | The engine's judgment consumes the recorded context as part of the trace; the validation run supplies the read log; the coordinator writes the judged hash at verification acceptance; publication consumes staleness. All must be built or adapted. | Two small extensions of the existing trace. Keeps copies of the context per accepted job; sets are a handful of files. Preferred candidate. |
| Fixed set snapshots with explicit commits | The engine, handout, validator, coordinator and publication all consume a snapshot identity; a snapshot store and commit protocol must be built. | One model across every interaction, including parallel admission and commit recovery. Imports multi-writer concerns the workflow lacks. The earlier version of this proposal; set aside unless a multi-writer need appears. |
| Hashes only, no kept bytes | As the preferred option, but the recorded context holds hashes alone. | No copies. A context hash that differs cannot be rechecked exactly, so a damaged member is detected only by its hash and the validator cannot be rerun on the original context. Correct in the paper's sense only if the trace also records the validator's version. |
| Filter later roles by workflow stage | Handouts and acceptance validators consume a stage-specific visibility policy. | Less recorded state, but stage order does not identify corrected versions of earlier roles, and it duplicates the layout in workflow rules. |
| Rerun the validator against current files on every step | The current behavior: the validator is volatile. | Stable only while no sibling changes a verdict. The observed defect. |

The automated checks are warranted by the type and layout contracts, exact
byte identity and explicit acceptance predicates. They establish those
mechanical properties only. A verification remains a bounded model
judgment, not a mechanical oracle.

## Forces and free choices

- **Keep the model smaller than its implementation.** No snapshot store, no
  commit protocol, no database. The trace record and the kept-files
  mechanism already exist; the additions are a read log and a judged hash.
- **Criteria live, context pinned.** A changed type contract or validator
  reopens accepted jobs; a changed sibling does not. Collapsing the two in
  either direction reproduces a known failure: spurious reopening, or a
  stale verdict after a criteria change.
- **Keep incomplete work visible.** Context drift and stale verifications are
  reported, not treated as a whole-artifact pass or hidden by a rewrite of the
  earlier acceptance.
- **Do not absorb external effects.** Existing publication recognition and
  uncertain-effect stop rules are unchanged.

Free choices: whether the read log comes from run-time tracking in the
validation run or from a declared context list per job; whether context
bytes are kept or only hashed; where the judged hash is recorded, in the
manifest or in code-written verification frontmatter, provided the retained
set identifies what each verification judged without the run directory;
whether a validator version string joins the trace; CLI shape; and migration
for existing runs.

## Adoption criteria

Before adoption, observe all of the following:

- A regression test reproduces the old-candidate, later-verification
  mismatch and shows that replay reaches the correction job without
  reopening the original synthesis.
- Self-check, initial acceptance and replay recheck deliver identical set
  findings for identical candidate bytes and context. Context drift is
  reported distinctly from a refusal.
- A recorded context read that is missing or altered at recheck is reported
  explicitly; the current set is never substituted for it.
- Replacing a judged member marks its verification stale, publication
  refuses the set until a current verification exists, and the final set
  still enforces every declared limit and the other required relations.
- Publication emits only the current members. Traces, kept context,
  attempts, packets and run state stay unpublished.
- The two evidence runs required by declared-layout adoption validate under
  this model, with self-check context and disagreement measurements
  recorded.

The adoption decision must name where the judged hash lives and whether
context bytes are kept. Until these criteria hold, the replay blocker stays
unresolved.

---

Relevant Notes:

- [Criteria edits invalidate verdicts; process edits invalidate artifacts](../../../notes/criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts.md) — rests-on: the split between live criteria and pinned context
- [Build Systems à la Carte: theory and practice](../../../sources/build-systems-a-la-carte-theory-and-practice.ingest.md) — evidenced-by: classification of the engine, untracked dependencies and their three responses, the non-determinism boundary
- [Dagster asset versioning and caching](../../../sources/dagster-asset-versioning-and-caching.ingest.md) — evidenced-by: the consumed-version record and one-hop staleness, and the verdict that this workflow is a departure from Dagster's main path
- [Apache Airflow best practices](../../../sources/apache-airflow-best-practices.ingest.md) — evidenced-by: the rule against reading latest data between reruns
- [Apache Iceberg reliability](../../../sources/apache-iceberg-reliability.ingest.md) — see-also: the multi-writer snapshot protocol behind the set-aside alternative
