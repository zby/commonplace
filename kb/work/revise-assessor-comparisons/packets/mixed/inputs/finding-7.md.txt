---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
  against kb/instructions/review-gates/semantic/completeness-boundary-cases.md
note: kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
note-sha256: 98643ed5cb9f96c25b62fc1fb6f075494b25c507e49ef7a7b4c51343a115fa7f
criterion: kb/instructions/review-gates/semantic/completeness-boundary-cases.md
criterion-sha256: b46ca399a83da384b7f5217f86945cff08f0ae3c084711ab6fec66a558192323
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews
launch: c479bc55423643ddb825da7ad43b3276
completed-at: '2026-11-20T18:55:18Z'
findings:
- scope: passage
  quotes:
  - investigate an unknown only if a plausible answer could reverse the choice
  - If the evidence supports only the routing gain, leave the overall judgment open.
  reason: 'The investigation rule and the three-branch decision for the AGENTS.md
    line cover two outcomes: the preference survives every plausible answer (act),
    or a plausible answer reverses it (investigate). A boundary case the note itself
    raises falls outside both: an uncertainty that could reverse the choice but that
    investigation cannot settle, such as future use, which the note says an estimate
    ''cannot settle''. In that case the rule sends the reader to an investigation
    that cannot resolve the question, and ''leave the overall judgment open'' does
    not say whether to keep or remove the change while a decision is still due. The
    description promises guidance on ''which uncertainties justify further investigation
    before acting'', so this case lies inside the claimed coverage.'
  level: warn
- scope: passage
  quotes:
  - 'Three choices fix the comparison:'
  reason: Tested against the note's own boundary, the three choices (alternative,
    who gains or loses, period) do not fix value weights; the note says elsewhere
    that analysis cannot supply them. Read with 'fix the comparison' meaning 'fix
    what is being compared', the list holds, so coverage is strained rather than broken.
  level: info
contract: verdict
target-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/c479bc55423643ddb825da7ad43b3276/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/artifact/reviews/a7b65ac5397325e891480498/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/c479bc55423643ddb825da7ad43b3276/outputs/review-completeness-boundary-cases.md
raw-output-sha256: 5db12dbd611d88c63062ef4e33870104578b8f7cc567602be8d58dcad761fdb2
---

# Review

## Summary

The note offers two small frameworks: three choices that fix a comparison, and a decision rule for uncertain comparisons, illustrated by the AGENTS.md routing line. I tested each against the simplest case, the extreme case and adjacent cases. The three-choice list survives with some strain, because value weights stay outside it by the note's own design. The decision rule has a gap. It tells the reader to act when the preference is robust and to investigate when a plausible answer could reverse it. It says nothing about a reversing uncertainty that investigation cannot resolve, even though the note names one such case, future use. Adding a category is not necessarily the fix: one sentence on the default when investigation cannot settle the question may be enough.
