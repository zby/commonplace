---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
  against kb/instructions/review-gates/sentence/stock-phrases.md
note: kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
note-sha256: 98643ed5cb9f96c25b62fc1fb6f075494b25c507e49ef7a7b4c51343a115fa7f
criterion: kb/instructions/review-gates/sentence/stock-phrases.md
criterion-sha256: 01fe5fea193e21d064468eb1b1c7495441fe3ca291ba101f15b3da55209e5241
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews
launch: 262edf34947f4789926811e68630a6b3
completed-at: '2026-11-20T18:54:22Z'
findings:
- scope: passage
  quotes:
  - This distinction guides a decision.
  reason: 'This is a signposting sentence that announces relevance instead of stating
    content. The next sentences already show how the distinction guides the decision:
    keep, investigate or leave open. If the sentence is deleted, the paragraph reads
    equally well.'
  level: warn
contract: verdict
target-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/262edf34947f4789926811e68630a6b3/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/artifact/reviews/ab67966cbb02bd2d6bead11a/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/262edf34947f4789926811e68630a6b3/outputs/review-stock-phrases.md
raw-output-sha256: a19a023afe231cce38b24f5a92660ca0a7fdbf89b7fca9313d3b84c3eede7260
---

# Review

## Summary

The note has several "not X, Y" sentences, which match the elevation pattern. Each one passes the deletion test because it carries a scope limit or a rejection the argument needs:

- "That resolves the choice between messages, not the choice between releases."
- "The case for 3.11 is not that the table has three gains and one loss."
- "These checks give reasons for the judgment, not a survey of how often each reason applies."
- "This is a practical commitment about the work we value, not a claim that every project should use the same measure."
- "That is a possible loss, not an observed failure."

Only "This distinction guides a decision." fails the deletion test: it introduces the paragraph that follows without adding anything that paragraph does not already say.
