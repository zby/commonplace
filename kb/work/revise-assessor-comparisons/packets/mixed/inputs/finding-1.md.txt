---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
  against kb/instructions/review-gates/accessibility/undefined-terms.md
note: kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
note-sha256: 98643ed5cb9f96c25b62fc1fb6f075494b25c507e49ef7a7b4c51343a115fa7f
criterion: kb/instructions/review-gates/accessibility/undefined-terms.md
criterion-sha256: a29bd905ec12b7a7c8375529e490cfde6711bb4feef5529546a92fda0419af38
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews
launch: c3a0c78c628a435a90d0c342719069f5
completed-at: '2026-11-20T18:52:49Z'
findings:
- scope: passage
  quotes:
  - Whether maintaining marked heads is worth the effort depends in part on who relies
    on them to stop searching.
  reason: '"Marked heads" is KB-internal vocabulary (the active term Mark, for tag-readme
    marks) used with no gloss and no link to its definition. The preceding sentence''s
    "a validator finding a member the documented search missed" also assumes the reader
    knows that tags have heads and members. Without that context, an outside reader
    cannot tell what is maintained or why someone would rely on it to stop searching.
    Add a short inline gloss, such as a tag''s index page marked as listing every
    member, and link the Mark definition.'
  level: warn
- scope: passage
  quotes:
  - A review gate that catches the same ambiguity as the old review
  reason: '"Review gate" is Commonplace vocabulary for a single-criterion review check.
    Its meaning is roughly inferable from the sentence, so this does not block understanding.
    A brief gloss would still help an outside reader.'
  level: info
contract: verdict
target-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/c3a0c78c628a435a90d0c342719069f5/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/artifact/reviews/ff37067bb5456f498f357548/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/c3a0c78c628a435a90d0c342719069f5/outputs/review-undefined-terms.md
raw-output-sha256: f102369472b5ec3a401db93e89d156d18903c52d3cfe921e6b4b5828d3dff283
---

# Review

## Summary

Most technical terms are glossed or explained by their context. A total order is described as one that "would rank any two versions", and a partial order as representing "the preferences we can defend". The factory comparison is paraphrased in the same sentence that links it. Python and CPython details are explained by the behavior the note reports.

The gap is in the KB-maintenance example. "Marked heads" relies on the active vocabulary term Mark, which needs both an inline gloss and a link on first mention. The sentence also relies on the reader knowing how tag heads and members work. Because the passage is offered as the note's concrete example of an established local gain, an unexplained term there weakens the illustration.
