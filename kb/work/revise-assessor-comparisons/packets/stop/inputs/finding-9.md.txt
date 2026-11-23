---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
  against kb/instructions/review-gates/semantic/grounding-alignment.md
note: kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
note-sha256: 0177d84330a5bbe930bebfc55c1c352405b81cb00146dd7b5389717615b8d3fb
criterion: kb/instructions/review-gates/semantic/grounding-alignment.md
criterion-sha256: c6c3b904f6e6d17bc67fcfadb2cb091ce62cdfd0bb33ce30cab047914e6c9a4c
outcome: fail
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews
launch: 003e070dff914169869d6e081eac041e
completed-at: '2026-11-22T21:54:05Z'
findings:
- scope: passage
  quotes:
  - because continual adaptation compounds silent degradation (see [Scheduler-LLM
    separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md))
  reason: 'The linked note''s title and opening claim concern workflow bookkeeping:
    code enforces defined state transitions directly, while semantic judgments need
    fallible verification, and moving bookkeeping into code may lower the cost of
    reliable execution. It does not claim that continual adaptation compounds silent
    degradation, and a search of the target finds no mention of degradation, compounding,
    regression or continual adaptation. The note gives no inference from the asymmetry
    to compounding degradation. Material support for the stated reason behind the
    regression-validation requirement is therefore absent. The footer gloss (''why
    symbolic writes are cheaply validated and parametric ones are not'') also extends
    the target to parametric writes, which it does not discuss.'
  level: fail
- scope: passage
  quotes:
  - for retained candidates, search, reject-capable evaluation, and operative retention
  reason: The linked proposal-selection note says these three functions are required
    for one route of learning and states that evidence can also determine updates
    directly, with no rejectable candidate. The note's 'for retained candidates' qualifier
    roughly preserves that scope. However, the surrounding claim that continual learning
    means 'the system does the selecting itself' leans on the target as a general
    discriminator, which is broader than the target claims. The fit is plausible but
    not airtight.
  level: info
contract: verdict
target-sha256: 2214be116a950b1be4016de0633a69bd6e3df247b8c6750c25d37d0ef7013038
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/003e070dff914169869d6e081eac041e/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/artifact/reviews/1f618552e38a2c8bf41e3798/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/003e070dff914169869d6e081eac041e/outputs/review-grounding-alignment.md
raw-output-sha256: 6292c988640898cfaa0aa9618085ce96dea4f25cd58d200db4ec3b6083c7fe25
---

# Review

## Summary

Most links are represented at the scope their targets claim:

- The broad learning criterion matches Simon's definition as quoted in the learning-generality note.
- "Authority belongs to a consumption path, not stored bytes" matches the behavioral-authority definition.
- The knowledge-artifact and system-definition-artifact families match the definition of consumption with instruction, routing, validation or learning force.
- The persistent deployment-time path matches the deployed-systems note.
- The three forms match the representational-form definition.
- Codification and relaxing, coevolution, and contextual activation are cited for what their targets say.

The failure is the scheduler-LLM link. It is the only support offered for why candidate writes must be validated against regression, one of the two constraints the note derives for deployment loops, and the target makes no claim about compounding silent degradation under continual adaptation. That premise needs a supporting link or argument of its own, or it should be marked as the note's conjecture.
