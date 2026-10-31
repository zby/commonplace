# Observation log

This is an opportunistic case series for the [watch](./README.md), not a benchmark or a frequency estimate. No new post-watch episodes have been recorded. The two records below are initial material from the commissioning investigation; neither counts toward the next-three-episodes review point.

Use one entry per independently arising episode. Keep corrections and later follow-through in that entry. Record checked false alarms, warranted syntheses, and unresolved cases as well as errors. Point to the harness's existing trace when available rather than importing whole session logs into workshop governance.

## O001 — Generalization inside operationalization

**Date and status:** 2026-10-31; single operator–assistant motivating episode. Now supported by selected conversation excerpts and a sequence of immutable Git artifact versions, **not** an independently replayed experiment.

**Provenance:** [O001 primary evidence and correction sequence](./o001-operationalization-exchange.md) records the original question, the objections, the observable assistant responses, and direct links to four historical versions of the [operationalization exploration](../operationalization-executability-automation/exploration.md). This is a manually excerpted conversation plus independently readable files, **not a complete chat export**. The originally cited [revised workshop README](https://github.com/zby/commonplace/blob/e53fc1bb1041d54de99beda36302b6ab889ad536/kb/work/operationalization-executability-automation/README.md) remains a later-state reference, not the source of the pre-correction claims.

**Question and useful directions:** the primary question concerned operationalization, execution, and automation, including their distinctions and the relation to constraining. The generalization thread was valuable to Commonplace's broader project and potentially useful as a *contrast*, but not established as a constituent of operationalization.

**Disputed relationship:** the first retained draft used a broad making-guidance-usable frame. After the initial operator objection, [revision G02](https://github.com/zby/commonplace/blob/8f034e48f420881faae027dcef6eb3472e2f1ec2/kb/work/operationalization-executability-automation/exploration.md) explicitly included "enlarging coverage" among operationalization activities and included "Generality" in its organizing dimensions. This is stronger direct evidence of the disputed inclusion than the operator's later paraphrase; its simultaneous caveats are preserved in the [evidence record](./o001-operationalization-exchange.md).

**Correction and uptake:** a subsequent executor-relative revision [G03](https://github.com/zby/commonplace/blob/56b00de7cedb71630db6f9701d31ad01a5f3b3c7/kb/work/operationalization-executability-automation/exploration.md) still listed "Generality" under the central account. Only after the operator explicitly assigned the application area to *task definition* did [G04](https://github.com/zby/commonplace/blob/961eb4539f6f0c3e136982b02f0be294546a5e6e/kb/work/operationalization-executability-automation/exploration.md) place "Generality (outside operationalization)" and separate fixed-task operationalization from widening to T'. These are stages **within O001**, not separate recurring episodes. No held-out later-task transfer was tested.

**What remains open:** why the initial inclusion was attractive; how much of the task was ambiguous; whether contextual project value, association, answer-plan templates, or edit inertia explain it; whether the correct distinction was activated before feedback; and whether the correction persists. The assistant's retrospective causal explanation is not privileged evidence. Exact model/checkpoint, decoding settings, internal reasoning traces, and complete raw conversation export are not established. This is evidence for a local output-level error and its repair sequence, not a prevalence or RL-causation claim.

## Q001 — Cross-benchmark common-mechanism claim

**Date and status:** identified in the initial review on 2026-10-31; candidate artifact for inspection, not a confirmed recurrence of utility-driven blending.

**Evidence:** [semantic-leakage ingest at the inspected commit](https://github.com/zby/commonplace/blob/e53fc1bb1041d54de99beda36302b6ab889ad536/kb/sources/semantic-leakage-lms-gonen.ingest.md), especially "Connections Found" and "Extractable Value." The [initial analysis](./findings.md#9-concrete-commonplace-dispositions) questions whether the reviewed sources warrant its assertion of one underlying mechanism across semantic leakage, GSM-DC, content effects, and ConvexBench.

**Question to check:** is there an additional argument or comparative evidence supporting that common-mechanism assertion? A fruitful shared hypothesis is not necessarily an established causal identity, but different measures do not prove different mechanisms either.

**Proposed local correction if warranted:** retain the cross-source connection as a hypothesis and state the missing evidence. No change to the source ingest is made by this workshop PR. Its generation context, the role of instrumental attractiveness, and response to correction are unknown. Do not count this as O002 without further evidence.

## Template for a new episode

Copy only the fields useful for the case; short entries are sufficient. Missing information should be explicit, not reconstructed.

### O00N — Short description

**Date / task / observer:** when and where the episode arose; who noticed it; whether the checklist or a prior correction cued the check. Record model/checkpoint and relevant settings only when known.

**Evidence:** commit and path, exact short excerpt, or available trace pointer before correction; identify paraphrases and missing context.

**Question, directions, and value:** primary question; useful secondary direction; why each mattered. Separate observed project value from an inferred motive for the agent.

**Relationship and check:** what the original answer asserted; the warrant or counterexample examined; whether the local task boundary had been explicit.

**Disposition:** unsupported integration / other error / warranted synthesis / already preserved distinction / unresolved. State why; these are working descriptions, not a new taxonomy.

**Correction and follow-through:** exact edit or feedback, corrected artifact pointer, and any later consequence checked. Mark acknowledgment-only, persistent framing, successful local repair, or unknown transfer as supported by the record. Preserve a useful tangent or record why prioritization was appropriate.

**Hypothesis update:** which competing explanations this case strengthens or weakens; what remains unknown; whether it triggers early review. Do not infer a training cause or systemic tendency from the case alone.
