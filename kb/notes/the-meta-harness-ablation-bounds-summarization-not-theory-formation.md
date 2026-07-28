---
description: "Why the summaries-hurt ablation is no evidence against gated condensation: its arms depart from this KB's theory at four named points and its winning arm instantiates the theory. What it does bound: never feed digests to attribution consumers"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [learning-theory, deploy-time-learning]
---

# The Meta-Harness ablation bounds summarization, not theory-formation

[Meta-Harness's controlled ablation](../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) found that its harness-search proposer fed raw execution traces beat scores-only and scores-plus-summary feedback by 15+ points median — and that the summaries *actively hurt*, trailing even scores-only on best-found accuracy, because they "compress away diagnostically useful details." Read flatly, this indicts any learning process that condenses episodes into compact artifacts — including this KB's, whose loop distills episodes into gated theory notes. This note records why that reading fails, and what the result legitimately constrains.

The premise the flat reading misses: summarization and theory-formation are different operations. A summary claims a subset of what its episodes claimed — selection and shortening are all it does. A distilled theory posits a mechanism covering unseen cases, content the episodes do not entail — ampliative by [commitment, not derivation](./commitment-not-derivation-creates-new-ground-truth.md), which is why it can carry [explanatory-reach](./first-principles-reasoning-selects-for-explanatory-reach-over.md) and why it owes a [reach-assessment](./definitions/reach-assessment.md) a summary never incurs. An experiment on the first operation bounds the second only if it implements it.

## Where the experiment departs from the theory it is read against

Four departures, each at a point where this KB's theory prescribes the opposite:

1. **Summaries replaced episodes.** The scores-plus-summary arm had trace access removed, so it tested digests *instead of* episodes. The theory keeps both layers: [the episode is retained beside the distilled rule](./retaining-the-episode-keeps-a-distilled-rule-re-derivable.md), with [raw history preserved for extraction while staying out of default context](./agent-memory-requirements/preserve-evidence-without-loading-history.md). No arm tested a distilled layer routing into retained episodes.
2. **Summarization ran pre-attribution and consumer-blind.** The digests were produced by a fixed procedure before any diagnosis, without the diagnostic question in hand — where the theory condenses *after* attribution, [at the decision surface where the "why" is cheap](./structure-inference-needs-capture-at-the-decision-surface.md), and [only when the lesson's boundary is statable](./abstract-an-experience-only-when-you-can-state-the-boundary.md).
3. **No conjectural operator, no gate.** The digests posited no mechanism, claimed no scope, and passed no review — nothing that could earn or lose reach. The condensation regime tested is the one this KB independently rejects as the junk drawer.
4. **The summarizer was hand-designed and excluded from the search** — by the paper's own optimize-the-harness thesis, an unsearched component — and the ablation arms' code is absent from the release, so the generation procedure cannot be audited further.

And the winning arm quietly instantiates the theory: [the released proposer skill mandates](../agent-memory-systems/reviews/meta-harness.md) three falsifiable, mechanism-targeting hypotheses per iteration, prototype tests before implementation, and a retained ≤30-line causal report per iteration — what changed, why, a takeaway — re-read every round. "Full traces" is episodes *plus* consumer-authored, post-attribution distillation produced by a conjecture-test-distill cycle. The comparison was therefore consumer-blind pre-attribution digests-instead-of-episodes against episodes-with-gated-distillation, and the strongest condensation regime sampled sits mislabeled in the baseline. With these departures, the ablation cannot argue against the theory; it refutes summarize-and-discard, which the theory also refutes.

## What the result does bound about the process being developed here

Dismissing the flat reading does not dismiss the result. Three constraints bind:

- **Attribution consumers must get episodes, not digests.** Any Commonplace step that feeds condensed views into diagnosis — compacted context in a fixing session, a critique pipeline reading summaries of runs rather than runs — risks the measured cliff, and the failure shape is specific: salient pattern preserved, unexpected detail lost. This is the empirical form of the theory's own two-layer separation, now with a 15-point price on getting it wrong.
- **The bet's burden of proof is located, and it is ours.** LLM summaries were not neutral compression; they actively hurt. The claim that LLM *conjecture* — gated, scoped, episode-backed — behaves differently is [openly a bet](./theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md), and this KB's condensation-faithfulness experiment (a live workshop) is the designed test. Until it runs, episodes stay retained and no distilled artifact substitutes for them in an attribution role.
- **The unrun arms are standing obligations:** distilled-theories-plus-episodes as proposer feedback, and reports-only — whether accumulated distillation can eventually carry attribution without the episodes. The winning arm's architecture is adjacent evidence for the first; nothing yet tests the second.

## Scope

- This is not a dismissal of the paper's positive program. The diagnostic-richness finding is accepted and cited elsewhere in this KB; only the reading of the summaries arm as evidence against condensation-as-learning is blocked.
- The departures are asserted against the released code and the paper's Table 3 description; if the unreleased ablation code turns out to have run a gated, post-attribution, episode-retaining summary arm, points 2–3 fall and this note must be revised.

---

Relevant Notes:

- [Commitment, not derivation, creates new ground truth](./commitment-not-derivation-creates-new-ground-truth.md) — grounds: the ampliative addition separating a posited theory from any reduction of its episodes
- [First-principles reasoning selects for explanatory-reach over adaptive fit](./first-principles-reasoning-selects-for-explanatory-reach-over.md) — grounds: reach as the property only the conjectural operation produces
- [Reach-assessment](./definitions/reach-assessment.md) — defined-in: the debt a theory incurs and a summary never does
- [Retaining the episode keeps a distilled rule re-derivable](./retaining-the-episode-keeps-a-distilled-rule-re-derivable.md) — grounds: the two-layer retention the summary arm violated and the winning arm practiced
- [Preserve evidence without loading history](./agent-memory-requirements/preserve-evidence-without-loading-history.md) — grounds: the two-layer separation the result prices empirically
- [Structure inference needs capture at the decision surface](./structure-inference-needs-capture-at-the-decision-surface.md) — grounds: why pre-attribution condensation loses what diagnosis needs
- [Abstract an experience into a lesson only when you can state where the lesson stops](./abstract-an-experience-only-when-you-can-state-the-boundary.md) — grounds: the gate that separates distillation from shortening
- [Theory-mediated learning may improve sample efficiency under structured shifts](./theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) — extends: the bet whose burden of proof this result locates on our side
- [Meta-Harness](../agent-memory-systems/reviews/meta-harness.md) — evidenced-by: the code-grounded review; the proposer skill's mandated hypotheses, prototypes, and retained causal reports are the winning arm's condensation regime
- [Meta-Harness paper ingest](../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) — evidenced-by: the ablation numbers, the summaries-actively-hurt finding, and the paper's own compression diagnosis
