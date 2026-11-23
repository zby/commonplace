---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
  against kb/instructions/review-gates/sentence/parsing-ambiguity.md
note: kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
note-sha256: 98643ed5cb9f96c25b62fc1fb6f075494b25c507e49ef7a7b4c51343a115fa7f
criterion: kb/instructions/review-gates/sentence/parsing-ambiguity.md
criterion-sha256: 07bf4245fd5eb41451cd2a6a79ca6655410dae6cc79b7238bcc82ad3a4799dff
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
  - Python 3 rejects the mixed addition even on the first name.
  reason: '"First name" is a fixed English phrase meaning a given name, as opposed
    to a surname. The intended reading is the first of the two names tested, the ASCII
    one. Because the paragraph is already about personal names, the given-name reading
    is plausible on first pass and hides the point that Python 3 fails before any
    accented input appears. Rewording, for example "even on the ASCII name", removes
    the collision.'
  level: warn
- scope: passage
  quotes:
  - a longer table or a different mix of tasks can change the balance. Compare the
    whole table with its earlier, shorter version
  reason: '"Table" has no stated antecedent in this paragraph. The scenario introduced
    only "one line in `AGENTS.md`", and the only table the note has shown is the Python
    3.10/3.11 comparison table. A reader can plausibly take "the whole table" to mean
    that comparison table rather than the AGENTS.md vocabulary or routing table that
    the line belongs to. Naming the referent, for example "the AGENTS.md table", resolves
    it.'
  level: warn
contract: verdict
target-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/262edf34947f4789926811e68630a6b3/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/artifact/reviews/992466f8bcf5baaf1a9999e8/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/262edf34947f4789926811e68630a6b3/outputs/review-parsing-ambiguity.md
raw-output-sha256: 4b012c063871030e2f3e259cf6c1cb3653bfab09c5586c88f97fee4d12beb84f
---

# Review

## Summary

Two references can plausibly be read in an unintended way.

1. In the opening Python 2 example, "the first name" collides with the idiom for a given name. The paragraph is about names, which makes that misreading likely.
2. In the AGENTS.md scenario, "table" appears without an antecedent: the scenario set up a single line, not a table. The nearest table in the note is the release comparison.

I checked the other pronoun and modifier attachments ("its waiting sibling", "It describes the limits of the ranking", "its recommendation", "Their availability") and they resolve clearly. I also checked whether "for the human judgment spent" in the bold objective sentence could read as a beneficiary rather than a ratio, but "spent" makes the ratio reading clear.
