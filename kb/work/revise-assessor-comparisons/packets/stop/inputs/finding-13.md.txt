---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
  against kb/instructions/review-gates/sentence/parsing-ambiguity.md
note: kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
note-sha256: 0177d84330a5bbe930bebfc55c1c352405b81cb00146dd7b5389717615b8d3fb
criterion: kb/instructions/review-gates/sentence/parsing-ambiguity.md
criterion-sha256: 07bf4245fd5eb41451cd2a6a79ca6655410dae6cc79b7238bcc82ad3a4799dff
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews
launch: 248c7f483c8b49dc81090398a3e73f15
completed-at: '2026-11-22T21:53:34Z'
findings:
- scope: passage
  quotes:
  - for retained candidates, search, reject-capable evaluation, and operative retention
  reason: The comma after 'retained candidates' lets the phrase read as a four-item
    list governed by 'for' (retained candidates, search, evaluation, retention), or
    as a scope qualifier 'for retained candidates' followed by a three-item list.
    With no verb, the relation of either list to the preceding clause is also unstated
    (requirements? examples?). The intended reading — for retained candidates, the
    loop requires search, reject-capable evaluation, and operative retention — needs
    an explicit verb, e.g. 'For retained candidates, that loop requires ...'.
  level: warn
contract: verdict
target-sha256: 2214be116a950b1be4016de0633a69bd6e3df247b8c6750c25d37d0ef7013038
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/248c7f483c8b49dc81090398a3e73f15/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/artifact/reviews/bf2f012acbc050fff665a44b/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/248c7f483c8b49dc81090398a3e73f15/outputs/review-parsing-ambiguity.md
raw-output-sha256: caaba92f1cb6c19b64fc442a133a314ae39d2c7270153093406bb149cc37ff03
---

# Review

## Summary

Negation scope is clear throughout ("persistence does not decide which retained item...", "does not create a governed behaviour-changing write", "need not touch all three every time"). Pronoun references hold: "It requires governing..." refers to continual learning, "Those changes are learning too" refers to the hand-authored readable changes of the preceding sentence, and "It need not touch all three" is read the same way whether "It" is the loop or the update.

The one plausible misparse is the verbless dash-appended list at the end of the continual-learning criterion, where "retained candidates" can be taken as a list item rather than as the scope of the requirements.
