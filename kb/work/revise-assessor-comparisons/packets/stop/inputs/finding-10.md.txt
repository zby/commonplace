---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
  against kb/instructions/review-gates/semantic/underspecified-assertions.md
note: kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
note-sha256: 0177d84330a5bbe930bebfc55c1c352405b81cb00146dd7b5389717615b8d3fb
criterion: kb/instructions/review-gates/semantic/underspecified-assertions.md
criterion-sha256: 8c6f8c1d87e6a7fd99a51fa6c2aa1f3068c6f9d3deeadbca86366dfb0b811410
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews
launch: 003e070dff914169869d6e081eac041e
completed-at: '2026-11-22T21:54:06Z'
findings:
- scope: passage
  quotes:
  - A behaviour-changing write counts as continual learning when the system's own
    loop selects and retains it because deployment evidence bears on an improvement
    objective — for retained candidates, search, reject-capable evaluation, and operative
    retention
  reason: 'Unresolved scope. Reading A: every continual-learning write must pass through
    a proposal-selection loop with reject-capable evaluation, so direct evidence-driven
    updates (such as online gradient steps) are not continual learning. Reading B:
    ''selects'' is loose, and the three functions apply only when there are discrete
    candidates, so direct updates count whenever they are evidence-responsive. The
    choice is material. It decides whether parametric online learning, named continual
    learning earlier in the note, satisfies the title''s requirement. It changes what
    evidence would show a system is continually learning. It also changes whether
    regression validation is necessary for every continual-learning write or only
    for candidate-based ones.'
  level: warn
contract: verdict
target-sha256: 2214be116a950b1be4016de0633a69bd6e3df247b8c6750c25d37d0ef7013038
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/003e070dff914169869d6e081eac041e/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/artifact/reviews/b82d1e5a98ed7efa83d0d908/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/003e070dff914169869d6e081eac041e/outputs/review-underspecified-assertions.md
raw-output-sha256: 45186b07bebef64e0e021a0e36989b29454b9e5e3ee913be9be3a2aae46de864
---

# Review

## Summary

Most load-bearing assertions are resolved nearby. "Persistence does not decide which retained item should shape behaviour or with what force" is made exact by the consumption-path definition. The form-placement claim says which forms and that not all three must change. "At the cadence their environment requires" is relative but not materially open.

The definitional sentence that separates continual learning from maintenance leaves its scope unresolved. It is the sentence the title's "requires" depends on, so the open choice between proposal-selection-only and any evidence-responsive update changes the claim's truth conditions.
