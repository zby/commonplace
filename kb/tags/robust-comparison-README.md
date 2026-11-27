---
description: "Curated head for the robust-comparison tag — comparing two versions across every measure compatible with the purpose of the work: necessary and possible preference, splitting a comparison, and deciding when it stays open"
type: types/tag-readme.md
---

# robust-comparison

A robust comparison ranks one version of a system above another only when every measure compatible with the purpose of the work scores it at least as high and at least one strictly favors it. The defining note is [necessary preference can guide improvement without a global measure](../theory/necessary-preference-can-guide-improvement-without-a-global-measure.md), which offers one formalization of on-balance judgment. Assign this tag to work on that comparison: which measures are compatible and how that set is argued, what a claim of improvement asserts, how a disputed comparison is examined, and how to decide when the comparison stays open. Reporting that one version scored higher on a benchmark is insufficient. The subject must be a comparison that holds across a set of measures, or what to do when it does not.

[Evaluation](./evaluation-README.md) is the wider area of judging claims, changes and outputs; this tag covers one comparison rule inside it. [Improvement-loop](./improvement-loop-README.md) covers the loop that proposes and selects changes; a robust comparison is one way that loop can evaluate a candidate.

## The comparison

- [Necessary preference can guide improvement without a global measure](../theory/necessary-preference-can-guide-improvement-without-a-global-measure.md) — one formalization of on-balance judgment: the asymmetric necessary preference rule and its four verdicts
- [An objection can show where to split a comparison](../theory/an-objection-can-show-where-to-split-a-comparison.md) — how to examine a disputed comparison
- [Reversibility can favor a change by limiting future loss](../theory/reversibility-can-favor-a-change-by-limiting-future-loss.md) — why a change that can be corrected may be kept while the comparison is open

For a worked example, the [interval-weight ingest](../sources/mustajoki-interval-smart-swing.ingest.md) shows how to test a choice without fixing each criterion's weight. A rival can be eliminated if it loses throughout the permissible range. The [Choquet model ingest](../sources/angilella-ordinal-regression-smaa-choquet.ingest.md) distinguishes a preference that holds for every compatible model from a ranking that is merely frequent in a sample.

## Related Tags

- [evaluation](./evaluation-README.md) — the parent area: how claims, changes and outputs are judged
- [improvement-loop](./improvement-loop-README.md) — the proposal-selection loop whose evaluation step a robust comparison can fill
