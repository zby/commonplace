# Explorer B: a completed review can preserve the wrong execution claim

## Finding and boundary

**For the inspected case, a later worker needs to recover what the check actually establishes, not merely the instruction that made the workflow finish. A concise correction can carry that distinction. No inspected evidence shows that a larger methodological artifact improves on it.**

The case is Commonplace's recorded model-provenance regression: review results were finalized under an intended model partition despite the incident record reporting a different executing model. The surprising feature is not just wrong dispatch. It is that successful bookkeeping could preserve the error and make the work appear complete. The relevant reusable method is therefore provenance-aware review orchestration, not a general memory store.

This follows the [turn 2 retention question](../turn-02/integration.md) and preserves [turn 1's separation](../turn-01/integration.md) between useful delivery, retained change and demonstrated later benefit. Useful knowledge work and learning to automate methodologies remain the purpose. There is no doctrine deviation or proposed purpose change here.

This is a bounded documentary and implementation inspection. I inspected the incident account, the later decision and procedure, the current finalization entry point, and two relevant test definitions. I did not recover the original execution traces or run a review. Consequently, the historical occurrence is an attributed local incident report; the present trust boundary is directly inspectable in code. Neither supplies a measured benefit from the correction.

## The concrete case and evidence chain

1. **Reported event.** The [incident record](../../../../reference/harness-sub-agent-model-selection-regression.md), under “The regression produced false review provenance,” reports jobs 6677–6717: 41 jobs with 268 review pairs. It says the retained child traces recorded Sol while the parent finalized them as Luna, leaving both the selected partition and recorded runner model as Luna. These are the record's counts, not a recount in this exploration. Its account of external API capabilities is not used as evidence here.
2. **Retained procedural response.** [ADR 067](../../../../reference/adr/067-review-workers-read-one-prompt-and-write-one-output.md) distinguishes a worker's optional self-report from harness-supplied provenance. The [current batch procedure](../../../../instructions/run-review-batches.md) says to establish the partition before selecting jobs, avoid inferred concrete model metadata, retain unknown provenance as unknown, and not force finalization after a known mismatch.
3. **Inspected implementation boundary.** In [finalization.py](../../../../../src/commonplace/review/finalization.py), `ExecutionMetadata.derived_model_partition` derives a partition from the supplied runner model, or returns `None`. `finalize_review_job_from_owned_output` rejects a non-null derived partition that disagrees with the job before loading and finalizing the output. The inspected function receives execution metadata as an argument; it does not independently query the executing worker. Self-report is passed separately into result-writing and returned separately. This supports a narrow implementation claim: the entry point checks supplied consistency, not the historical truth of dispatch.
4. **Inspected tests, not executed results.** In [test_review_jobs_live_and_direct.py](../../../../../tests/commonplace/review/test_review_jobs_live_and_direct.py), `test_finalize_review_job_validates_model_effort_partition_before_mutation` asserts rejection of mismatched supplied metadata without state change, then acceptance when supplied effort makes the partition match. `test_finalize_review_job_preserves_optional_self_reported_model` asserts that self-report is retained while `runner_model` remains null. These definitions expose the intended protections. Reading them is not a passing test run or evidence of authentic runtime provenance.

The incident, decision and procedure are not three independent confirmations. They belong to one local response lineage. Current code provides additional evidence about what is enforced now, not independent authentication of the historical counts. The original traces' locations were not supplied by the inspected incident record, so I stop short of a reconstructed incident audit.

## What a later worker must recover

The following is a case-specific sufficiency argument, not a proposed mandatory record schema. The information may already arrive through the standing procedure, live harness and task packet; duplicating it in every lesson would add no demonstrated benefit.

| Decision | Information needed in this case | Error if missing |
|---|---|---|
| Apply | Whether acceptance requires a particular model, and which partition the current harness can legitimately support | A requested identity substitutes for an available execution path |
| Apply | Which values are requested, harness-supplied, worker-reported or unknown | A self-report or parent intention is promoted into execution evidence |
| Apply | Finalization checks consistency of supplied metadata; freshness is maintained under the selected identity | Successful finalization is mistaken for authentication |
| Revise | Which dependency changed: dispatch support, inheritance behavior, model mapping, telemetry availability or required assurance | An old concrete dispatch recipe is repeated after its preconditions disappear |
| Decline or narrow | What conclusion the available evidence cannot support, and who may change the acceptance condition | A worker silently substitutes a different model or demands stronger assurance than the task requires |
| Repair earlier evidence | Which old results were affected and their unresolved disposition | Restoring future dispatch is mistaken for repairing earlier misattribution |

The durable part of the correction is the distinction between a requested identity and evidence of execution. Exact model names and dispatch options are per-environment facts to reacquire. The incident record is useful for locating old affected evidence and explaining why an apparently successful check is insufficient; a later worker does not need all historical jobs to avoid the same mistake on a new job.

**Important conflict retained:** current policy permits unknown concrete provenance when the partition was legitimately known at selection. That is not equivalent to requiring an authenticated execution trace for every review. A stronger assurance requirement could be appropriate for a model-comparison experiment, but it is not licensed as a universal rule by this incident. If a particular commission requires proof of realized model identity and the harness cannot supply it, decline that claim or return partial. Do not silently strengthen ordinary review acceptance or weaken the special commission.

## What an ordinary concise correction can provide

A competent concise correction could say:

> Establish the available worker partition before creating review jobs. Keep requested model, harness-supplied metadata and worker self-report distinct. A successful finalization checks supplied consistency, not actual dispatch. Do not finalize a known mismatch; do not invent unknown concrete provenance. If this task requires execution assurance unavailable from the harness, return that limit rather than claiming it was met.

With the existing batch procedure and a pointer to the incident, this appears sufficient for ordinary recurrence. It carries the operative distinction and the refusal condition without a general store or full trace bundle. Its effectiveness remains untested.

A weaker correction—“use the correct model” or “verify the worker model”—does fail to specify the source of the evidence, the trust boundary of the check, and what to do when evidence is unavailable. But this is not evidence against concision. The omitted distinctions can be stated concisely.

More retained material becomes useful for a different decision: auditing the affected jobs, revising the evidence policy, diagnosing a new contradiction, or testing whether the correction changes behavior. Those uses need inspectable evidence or rationale, not necessarily a longer execution instruction. The historical job list can remain behind a link rather than entering every worker's context.

This agrees with the conceptual distinction in [checked outcomes versus explanatory abstraction](../../../../theory/checked-outcome-licenses-episode-retention-not-abstraction.md): success of one check does not establish a larger causal explanation. I use that note as an argument, not its external citations as fresh empirical support.

## How the method could look successful without helping

These are rival explanations and test predictions, not measured outcomes from this turn.

- **The later harness removes the original failure opportunity.** Correct runs after the correction could result from changed dispatch support rather than better instructions. Comparing before and after across harness changes would confound the two.
- **The task no longer requires the disputed distinction.** A broad partition may admit several concrete models. Correct partition handling need not establish a concrete-model claim. Counting both as the same success would erase the acceptance boundary.
- **The outcome measure repeats the parent's assertion.** Counting completed jobs or matching stored strings rewards internally consistent misattribution. The original reported failure illustrates why these are inadequate measures of execution truth.
- **A coordinator supplies the decisive intervention.** A worker may follow the method incorrectly, then the parent catches the mismatch. That can be useful system-level success, but it does not show that the worker's reusable instruction supplied the benefit. Parent work and repair belong in the comparison.
- **The relevant competence was already available.** A fresh worker given the ordinary task and current procedure may make the same correct distinction. A retained reminder could still help, but its contribution cannot be inferred merely from a later correct answer.

Changed conditions can also make the old method harmful. Treating the historical dispatch recipe as timeless can block a newly valid route or permit a now-invalid one. Treating all missing telemetry as grounds to stop could unnecessarily prevent work allowed by current policy. Treating restored dispatch as historical repair leaves old evidence mislabeled. These failure paths differ; one generic instruction to “check more carefully” does not specify their decisions.

## Strongest rival and a bounded comparison worth considering

**Strongest rival:** ordinary task-first assistance using the current procedure, a concise correction and the incident pointer, with no additional extraction product. It retains learning and is not an intentionally forgetful baseline. The case supplies no reason to reject it.

If a later allocation asks whether richer packaging helps, a small comparison could test this case rather than build a record system. The decision would be whether to supply additional case rationale beyond the concise correction. Both conditions would receive the same purpose, authority, current procedure and harness evidence. One would receive the concise correction plus incident pointer; the other an expanded case account. Access to the pointer is part of the competent rival and should not be withheld to manufacture an advantage.

Useful case variants would include known matching metadata, known mismatch, missing concrete provenance with a known partition, and a task requiring assurance that the available metadata cannot provide. Correct responses differ: rejecting everything is not success. Evaluation should distinguish proceeding appropriately, preserving unknowns, rejecting contradictions, and narrowing unsupported claims. If testing real runtime identity, the evaluator needs independent execution evidence; a worker's answer cannot be its own oracle.

This comparison is proposed, not run or commissioned. Even a favorable result would establish only an effect of the tested packaging under those conditions. It would not establish that producing the package was the best investment or that methods transfer across knowledge work. A null would count against the extra packaging, not against the value of the original correction. Source and harness inspection, reading, repair and operator review costs would all matter; none is measured here.

## Changed decisions, unknowns and parked ideas

Possible within-purpose changes supported by this inspection:

- For this case, start with a concise correction and the existing procedure, not a new methodological store.
- Judge a provenance method by the execution claims it permits or refuses, not by completed-job counts.
- Preserve the distinction between unknown metadata and contradictory metadata. They do not have the same operational consequence.
- Before claiming learning, identify whether a later improvement came from the retained instruction, the harness, or human repair. A reminder is not disqualified merely because the model already had the underlying competence.

These are findings and proposals, not edits to the review procedure. Relative priority between current service and speculative learning remains unresolved, as in the preceding integrations. Nothing here makes immediate usefulness a veto on exploration.

Unknown: original trace authenticity and complete incident reconstruction; whether affected evidence was subsequently replaced; frequency of this failure; effect of the retained correction on later workers; whether richer rationale helps under changed conditions; and total maintenance and review burden. Missing trace-level and comparative evidence limits the empirical answer. No general performance conclusion is warranted.

Parked: a future independent provenance adapter; tests that distinguish parent repair from worker success; and whether historical rationale improves adaptation when the exact dispatch surface changes. These are not an implementation queue. Operational record design remains outside this output's scope.

## Work accounting and verification

Only this assigned file was written. No other turn-3 artifact was read. Searches covered theory, reference, instructions, retained reports, sources, external-system collections and workshops while excluding the current turn. Full reads followed selected local evidence paths; search hits were navigation, not evidence. No external source claims were adopted, no ingests or snapshots were created, and no external source research or nested delegation occurred. Nested assignments and sessions: none. Experiments and review executions: zero. One attempted test-directory search used a nonexistent path; a scoped search under `tests/` located the relevant file without changing state.

Token usage, monetary cost, elapsed model time and operator attention are unknown. Activity counts are not cost estimates. Coordinator scheduling, integration and recovery remain with the coordinator. No code/library edits, commits, extraction or deletion occurred.

Validation: `commonplace-validate` succeeded for this file: one text file, zero failures and zero warnings. A manual reread checked the evidence grades, optional-provenance conflict, simple rival and authority limits. Mechanical validation cannot authenticate the incident or establish benefit. Optional future graph discovery could use `cp-skill-connect` under separate authorization; no such work is required to answer this case.
