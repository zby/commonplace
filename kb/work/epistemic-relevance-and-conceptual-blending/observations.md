# Observation log

This is an opportunistic case series for the [watch](./README.md), not a benchmark or a frequency estimate. No new post-watch episodes have been recorded. The two records below are initial material from the commissioning investigation; neither counts toward the next-three-episodes review point. Q001 has since been checked and repaired, so it is a finished artifact-level case the review may use. Q002 is a checked non-error on an external artifact; it does not count either.

Use one entry per independently arising episode. Keep corrections and later follow-through in that entry. Record checked false alarms, warranted syntheses, and unresolved cases as well as errors. Point to the harness's existing trace when available rather than importing whole session logs into workshop governance.

## O001 — Generalization inside operationalization

**Date and status:** 2026-10-31; single operator–assistant motivating episode. Now supported by selected conversation excerpts and a sequence of immutable Git artifact versions, **not** an independently replayed experiment.

**Provenance:** [O001 primary evidence and correction sequence](./o001-operationalization-exchange.md) records the original question, the objections, the observable assistant responses, and direct links to four historical versions of the [operationalization exploration](../operationalization-executability-automation/exploration.md). This is a manually excerpted conversation plus independently readable files, **not a complete chat export**. The originally cited [revised workshop README](https://github.com/zby/commonplace/blob/e53fc1bb1041d54de99beda36302b6ab889ad536/kb/work/operationalization-executability-automation/README.md) remains a later-state reference, not the source of the pre-correction claims.

**Question and useful directions:** the primary question concerned operationalization, execution, and automation, including their distinctions and the relation to constraining. The generalization thread was valuable to Commonplace's broader project and potentially useful as a *contrast*, but not established as a constituent of operationalization.

**Disputed relationship:** the first retained draft used a broad making-guidance-usable frame. After the initial operator objection, [revision G02](https://github.com/zby/commonplace/blob/8f034e48f420881faae027dcef6eb3472e2f1ec2/kb/work/operationalization-executability-automation/exploration.md) explicitly included "enlarging coverage" among operationalization activities and included "Generality" in its organizing dimensions. This is stronger direct evidence of the disputed inclusion than the operator's later paraphrase; its simultaneous caveats are preserved in the [evidence record](./o001-operationalization-exchange.md).

**Correction and uptake:** a subsequent executor-relative revision [G03](https://github.com/zby/commonplace/blob/56b00de7cedb71630db6f9701d31ad01a5f3b3c7/kb/work/operationalization-executability-automation/exploration.md) still listed "Generality" under the central account. Only after the operator explicitly assigned the application area to *task definition* did [G04](https://github.com/zby/commonplace/blob/961eb4539f6f0c3e136982b02f0be294546a5e6e/kb/work/operationalization-executability-automation/exploration.md) place "Generality (outside operationalization)" and separate fixed-task operationalization from widening to T'. These are stages **within O001**, not separate recurring episodes. No held-out later-task transfer was tested.

**What remains open:** why the initial inclusion was attractive; how much of the task was ambiguous; whether contextual project value, association, answer-plan templates, or edit inertia explain it; whether the correct distinction was activated before feedback; and whether the correction persists. The assistant's retrospective causal explanation is not privileged evidence. Exact model/checkpoint, decoding settings, internal reasoning traces, and complete raw conversation export are not established. This is evidence for a local output-level error and its repair sequence, not a prevalence or RL-causation claim.

## Q001 — Cross-benchmark common-mechanism claim (checked 2026-11-01)

**Date / task / observer:** identified in the initial review on 2026-10-31 as a candidate artifact; inspected and repaired on 2026-11-01 under operator authorization. Generation context of the original wording is unknown: the three artifacts were written in earlier sessions (ingests dated 2026-07-13), with no trace of how the wording arose. This remains an artifact-level case, not an observed run-level episode, and it does not count toward the next-three-episodes review point.

**Evidence:** at commit `340a4c3af`, the same assertion sat in three places: the [semantic-leakage ingest](../../sources/semantic-leakage-lms-gonen.ingest.md) ("not independent interference axes — they stress the same mechanism under different experimental regimes ... What differs is measurement surface, not underlying cause"), the [GSM-DC ingest](../../sources/gsm-dc-llm-reasoning-distracted-irrelevant-context.ingest.md) ("surface regimes of one mechanism ... one mechanism, multiple empirical regimes, one architectural remedy"), and the theory note [LLM context is composed without scoping](../../theory/llm-context-is-composed-without-scoping.md) ("not independent interference axes; they stress the same flat-context failure"). The pre-repair wording is retrievable from that commit.

**Question, directions, and value:** the ingest's job was to place Gonen's semantic-leakage result in the KB. The useful secondary direction was the context-engineering remedy (exclusion/scoping) that the scoping note argues for. Each benchmark is independently valuable to that remedy argument because each shows unlicensed prompt content reaching generation.

**Relationship and check:** the artifacts asserted causal identity: one mechanism, with the four benchmarks differing only in measurement surface. The only stated warrant was the scoping note's architectural argument, and the scoping note in turn cited the same three studies as the measurement of its mechanism. That warrant is circular, and the architectural argument establishes a shared *enabling condition* (nothing in a flat context excludes the content), not a shared *cause*. Counterexamples checked: training responds differently in each paradigm (hard-distractor training helps in GSM-DC; instruction tuning increases leakage in Gonen; instruction tuning leaves content effects unchanged in Lampinen); Lampinen's content sits in the task's own premises, so the single proposed remedy, exclusion, cannot apply to it; ConvexBench has no irrelevant content at all; and the GSM-DC ingest's own extractable-value item 2 said the SAcc/PAcc gap shows "two distinct degradation channels requiring different mitigations", contradicting the "one mechanism, one remedy" synthesis a few paragraphs above it. That internal contradiction counts against the ingest's coherence whichever side is right; the two-channel reading itself turned out to rest on a self-contradictory passage in the paper (see follow-through), so it is a weak counterexample. The same Gonen ingest also warned, for the Lampinen/Gonen instruction-tuning pair, "do not collapse different tasks and metrics into one mechanism", so the artifact applied the distinction to one neighboring pair and withheld it from the other.

**Disposition:** unsupported integration. A shared enabling condition and a shared usefulness to the remedy argument were stated as a shared mechanism. The cross-source connection itself is warranted and was kept.

**Correction and follow-through:** all three artifacts were edited to state the shared condition, mark the common-mechanism claim as a hypothesis, list the divergent training responses and the Lampinen counterexample, and name the missing comparison (manipulate one factor, measure across paradigms). The Gonen ingest's extractable-value item 3 and recommended next action were reworded to match. The downstream note [context contamination operates below compliance reasoning](../../theory/context-contamination-operates-below-an-agents-compliance-reasoning.md) already called Gonen "an analogous content-influence result" and needed no change. Uptake check: the GSM-DC synthesis paragraph now states that the remedy follows from the cause rather than treating one remedy as settled, which is the consequential inference that changed. Transfer to future writing is unknown. Two frozen replication packets under `kb/work/linking-contract-consistency/` quote the old wording and were deliberately left as they were.

Because the GSM-DC ingest contradicted itself, the operator had it re-ingested on 2026-11-01 through `cp-skill-ingest` with a fresh drafting worker and the same pinned snapshot. The regenerated report treats the cross-paradigm relation as a comparison axis with divergent training responses, states that the divergence is evidence against assuming one mechanism without establishing that the mechanisms differ, and flags a source-level problem the old ingest had missed: the paper's sentence defining Δ(SAcc, PAcc) as a ratio where lower means a larger gap, then reading a higher value for clean-trained models as more execution damage. The published Figure 6 caption reports step accuracy, not the ratio, so the paper does not resolve it. Three library sentences had stated the arithmetic-execution finding as settled and were qualified: the soft-degradation note, the process-structure note, and the Gonen ingest's sibling paragraph.

**Hypothesis update:** this case fits the watched pattern at the output level: two directions each useful to a broader goal (the exclusion remedy), joined by an identity relation the evidence did not support, with the stated rationale for the join being that usefulness ("one architectural remedy"). Two further observations are worth carrying to the review. First, the unsupported relation propagated across three artifacts and was cited circularly between them, so a correction has to find every copy. Second, the same artifact withheld the merge where a limitation section prompted it and applied the merge where a connections section rewarded it, which weakens a pure association account and is consistent with a role-of-section or candidate-selection account. Nothing here establishes a cause; the generation context is unavailable.

## Q002 — External literature review checked for the pattern (checked 2026-11-01)

**Date / task / observer:** 2026-11-01. The operator supplied a ChatGPT-generated literature review of this workshop's hypothesis. The review synthesizes about twenty sources into one account, which is the kind of artifact where an unsupported common-mechanism relation could appear, so the checklist was applied to it as an artifact-level check. Generation context unknown beyond the model family.

**Evidence:** [retained review](./external-review-2026-11-01.md), verbatim.

**Relationship and check:** the review's load-bearing relations are "neighboring", "analogue", "precedent" and "motivates". Its summary table assigns each source to one transition of the proposed process and names the remaining gap for each. It explicitly declines the merge: "combining them into a single established theory would exceed their evidence", and it separates four attractions (practical payoff, semantic familiarity, agreement, explanatory completeness) rather than collapsing them.

**Disposition:** checked non-error; warranted separation. The review groups sources by shared relevance to the workshop's goal without asserting identity, inclusion or a common cause among them.

**Hypothesis update:** none on the mechanism. One methodological note: the review was produced under a request that invited criticism of the hypothesis rather than a unified account, which is the answer-form condition the new sixth competing explanation in the [findings](./findings.md#4-competing-explanations-and-discriminators) predicts should reduce the failure. That is consistent with the account, not evidence for it.

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
