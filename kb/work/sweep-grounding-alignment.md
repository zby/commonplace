# Handoff: sweep grounding-alignment over the ingest-citing notes

Standalone task, no workshop. Satisfies closure condition 3 of the
[claim-grounding rollout](./claim-grounding-rollout/README.md): every target note
carries a fresh `semantic/grounding-alignment` result under the chosen model
partition, after the 2026-08-25 gate revision. Delete this file when the sweep
lands.

The other four closure conditions already hold. This is the last one, and it is
the only step that checks every note's citations against the **current** rules
rather than the retired paraphrase model.

## Scope depends on one decision the operator must make

68 notes cite an ingest. Post-revision results exist for 10, **split across two
partitions**: 1 under `claude-sonnet-5` (review job 8051) and 9 under `codex`
(cohort 10b's own reviews).

- Certify under `claude-sonnet-5`, the standing default for gate sweeps: **67
  notes remain**, including re-reviewing cohort 10b's nine.
- Accept either partition as certifying: **58 remain**.

Ask before starting. Do not silently pick one — the answer decides whether a
migration is certified by one reviewer family or by two, and that is the
operator's call, not the sweep's.

## How to run it

The standard pipeline, one note at a time or batched by note:

```bash
commonplace-review-target-selector semantic/grounding-alignment \
  --mode requested --model-partition <partition> --note <paths...> --json \
  | commonplace-create-review-jobs --input - --grouping note
```

Then for each job: dispatch a fresh sub-agent that reads the job's `prompt_path`
and writes its review to `job_output_path`, and finalize with
`commonplace-finalize-review-job --review-job-id <id> --runner worker --model <model>`.

Run reviewers in **separate fresh contexts**, one job at a time. A single agent
carrying 67 notes' worth of sources will grow more charitable as it fills, and
charitable grounding is the exact defect this gate exists to catch.

## Parallelism: review wide, finalize narrow

**Reviewing is embarrassingly parallel here, unlike the grounding cohorts.** Those
mutated notes and ingests, so cohorts had to be disjoint on both axes. A review
mutates nothing: it reads the note, the criterion, and linked material, and writes
only its own `job_output_path`. Two reviewers on two notes cannot collide, so no
disjointness analysis is needed and any number can run at once.

**Finalization is the exception, and the store is not configured for it.**
`kb/reports/commonplace-store.sqlite` runs `journal_mode=delete`, not WAL, with a
5-second busy timeout and no retry logic in the code. Concurrent
`commonplace-finalize-review-job` calls contend for an exclusive write lock and
can fail with `database is locked`.

So: **fan out the reviewers, funnel the finalizations.** Finalizing is a handful
of fast writes, so a single serial queue costs almost nothing and removes the
contention entirely. If a finalize does fail on a lock, it is safe to retry — the
job output is already written and finalization is what records it.

Rough scale, from the one measured run: review job 8051 took about three minutes
for a single pair while reading a 128 KB snapshot, which is the heavy end; median
offered cost is 67 KB. Sequential, 67 notes is a few hours. Fanned out, it is
bounded by however many reviewers you are willing to run.

## Expect sampling, and say so

The gate caps link-following at five. Measured available cost puts the median
note at **7 distinct artifacts and 67 KB**, p90 at 16 and 148 KB — so most
reviews in this sweep will open a subset and disclose the rest. That is current
behavior, not a defect to fix here.

Do not raise the cap, edit the gate, or work around it. Splitting a review that
exceeds one pass is
[a live proposal](../reference/proposals/exceeding-a-review-budget-splits-the-task.md)
and is deliberately not built. **Record that the sweep was sampled** in whatever
you report, with the p50 7-against-cap-5 figure, so a later reader knows what
these verdicts cover.

## What not to do

- **Do not repair notes.** A FAIL is a finding to report, not a defect to fix.
  Repairing while reviewing destroys the measurement and blurs who judged what.
- **Do not edit the gate or any ingest.** No `## Quotes` changes, no marker
  additions.
- **Do not resolve a FAIL by adding a `(snapshot required)` marker.** That would
  convert a grounding failure into a routing change and hide it.

## What to report back

- Outcome distribution across the sweep, and every FAIL and WARN with its note.
- How often a reviewer stopped for budget rather than sufficiency. This is the
  signal the [enforcement](../reference/proposals/review-budget-enforcement-is-separable.md)
  and [splitting](../reference/proposals/exceeding-a-review-budget-splits-the-task.md)
  proposals both wait on, and a 67-note sweep is the largest sample available.
- Any case where the retired paraphrase model still shows through — a note whose
  wording only makes sense against a normalized claim that no longer exists.

## After the sweep, before deletion

Closure is the operator's call, not this task's. But the rollout's durable
findings must be extracted before the workshop is deleted, and they exist only in
files scheduled to disappear:

- the disposition distribution over ~205 claim uses, including the shift from
  ~23% grounded under the paraphrase model to 69% under quotes;
- the identity and accumulation evidence, which is what ADR 073's decision to
  ship no claim IDs, deduplication, or reconciliation actually rests on;
- snapshot-route uptake — 19 marked links across 7 notes, all precondition-valid,
  grown from a single seeded example.
