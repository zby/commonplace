---
description: "Why the summaries-hurt ablation does not identify the effect of scoped theory formation alongside retained episodes, while still supplying adverse evidence about condensed feedback"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [learning-theory, deploy-time-learning]
---

# The Meta-Harness ablation does not identify episode-backed theory formation

[Meta-Harness](../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) is an outer-loop system that searches task-specific LLM harness code. In its text-classification ablation, a proposer given raw execution traces reached 50.0 median accuracy, versus 34.6 with scores only and 34.9 with scores plus summaries. The summaries also trailed scores only on best-found accuracy, 38.7 to 41.3; the paper attributes the loss to compression of diagnostically useful details.

The result is adverse evidence for any learning process that inserts condensed natural-language artifacts into an optimizer's information environment. It does not, however, identify the effect of the intervention this KB proposes: adding a scoped causal conjecture while retaining the episodes it was derived from. Those treatments share possible anchoring and attention costs, but differ in evidence access, attribution timing, and review.

Here, “summary” names the tested consumer-blind compressed feedback; it does not imply that every summary is merely extractive. Theory formation posits a scoped mechanism covering unseen cases—content the episodes do not entail. It is ampliative by [commitment, not derivation](./commitment-not-derivation-creates-new-ground-truth.md), so it may have [explanatory-reach](./first-principles-reasoning-selects-for-explanatory-reach-over.md)—the ability to keep explaining beyond the cases that produced it. That generalization therefore requires a [reach-assessment](./definitions/reach-assessment.md) of how far the explanation is justified. The ablation did not isolate this intervention from generic compression.

## Where the experiment departs from the proposed intervention

Four differences prevent the ablation from identifying the proposed theory-forming intervention:

1. **Summaries replaced episodes.** The scores-plus-summary arm had trace access removed, so it tested digests *instead of* episodes. The theory keeps both layers: [the episode is retained beside the distilled rule](./retaining-the-episode-keeps-a-distilled-rule-re-derivable.md), with [raw history preserved for extraction while staying out of default context](./agent-memory-requirements/preserve-evidence-without-loading-history.md). No arm tested a distilled layer that routed into retained episodes.
2. **Summarization ran pre-attribution and consumer-blind.** A fixed procedure produced the digests before the next proposer formed its diagnostic question. The proposed process instead condenses *after* attribution, [at the decision surface where the “why” is cheap](./structure-inference-needs-capture-at-the-decision-surface.md), and [only when the lesson's boundary is statable](./abstract-an-experience-only-when-you-can-state-the-boundary.md).
3. **The digests have no established conjectural or review operator.** The published description does not show the summaries stating scoped mechanisms or passing a review that could accept or reject their reach. That leaves the artifact kind needed for the comparison unmeasured.
4. **The summarizer was hand-designed and excluded from the search.** Its poor result may therefore reflect this particular fixed compression procedure as well as limits shared by condensed artifacts generally.

There is also a provenance limit: the ablation-arm code is absent from the release, so its generation procedure cannot be audited further. The [released proposer implementation](../agent-memory-systems/reviews/meta-harness.md) does contain workflow elements adjacent to theory formation: mechanism-targeting hypotheses, prototype tests, and short retained causal reports. But the release does not establish that this skill governed the Table 3 runs. The benchmark gates candidate harness code, not the truth or scope of each report, and the full-trace arm bundles reports with raw traces. Without a traces-only, no-report arm, the reports' contribution could be positive, null, or harmful. The ablation therefore rejects summarize-and-discard in its tested setting, but does not identify the effect of episode-backed theory formation.

## What the result does bound about the process being developed here

Limiting the ablation's interpretation does not dismiss its result. It still imposes three constraints:

- **Comparable attribution tasks should preserve episode access by default.** A fixing session or critique pipeline that substitutes a generic digest for the run risks the measured failure: salient patterns may survive while unexpected diagnostic details disappear. The 15-point median gap prices that risk for this proposer, task, and compression procedure; it is not a universal constant.
- **The burden of proof rests with this KB.** LLM summaries were not neutral compression; they actively hurt in the tested setting. The claim that a reviewed, scoped, episode-backed conjecture behaves differently is [openly a bet](./theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md). Until it is tested, episodes remain available and no distilled artifact substitutes for them in an attribution role.
- **The unrun arms are standing obligations.** Hold raw episodes fixed while randomizing the addition of no artifact, a generic summary, a scoped causal conjecture with provenance, and the same conjecture after reach-assessment. Separately, a reports-only arm can test whether a particular accumulated report regime eventually carries attribution without episodes; it cannot establish theory formation unless the reports actually contain scoped mechanisms and pass the claimed review.

## Scope

- This is not a dismissal of the paper's positive program. The diagnostic-richness finding is accepted; this note limits what Table 3 establishes about the unrun intervention.
- The differences are asserted against the released code and the paper's Table 3 description. If the unreleased ablation code turns out to have run a reviewed, post-attribution, episode-retaining theory arm, the central identification claim must be revised.

---

Relevant Notes:

- [Diagnostic richness constrains outer-loop learning quality](./diagnostic-richness-constrains-outer-loop-learning-quality.md) — grounds: the general evidence-surface premise that this note narrows
- [Knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md) — contrasts: condensed artifacts can fail by losing evidence before attribution or by failing to affect behavior after read-back
