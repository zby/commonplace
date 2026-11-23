---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
  against kb/instructions/review-gates/sentence/misleading-link-text.md
note: kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
note-sha256: 0177d84330a5bbe930bebfc55c1c352405b81cb00146dd7b5389717615b8d3fb
criterion: kb/instructions/review-gates/sentence/misleading-link-text.md
criterion-sha256: 29771fdb3d02cdf416ad3b68c38b2ae29bb69fe4332f316cc9475de3aa4508c2
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
  - because continual adaptation compounds silent degradation (see [Scheduler-LLM
    separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md))
  reason: The sentence cites the target as support for the claim that continual adaptation
    compounds silent degradation. The target is about moving workflow bookkeeping
    (task records, dependencies, completion state) into code because code enforces
    defined transitions while semantic judgments need fallible verification. It does
    not discuss continual adaptation, compounding, regression, or silent degradation.
    A reader following the link will not find the cited claim; at most the target
    supports why symbolic changes are cheaper to check, which is what the footer annotation
    says.
  level: warn
- scope: passage
  quotes:
  - '[Only explicit retention is durable, writable, and addressable](./only-explicit-retention-is-durable-writable-and-addressable.md)'
  reason: The link text asserts an exclusive claim that the target no longer makes.
    The target is titled 'Explicit retention provides direct targets for selective
    revision', and its description says durability, writability, and effective addressability
    still depend on the boundary and available operations. The annotation 'the form-level
    trade space this note defers to' also conflicts with the body, which defers the
    trade space to the representational-form coevolution note. Update the link text
    to the current title.
  level: warn
- scope: passage
  quotes:
  - '[Constraining during deployment is continual learning](./constraining-during-deployment-can-produce-learning-outside-weights.md)'
  reason: The link text states an unqualified identity; the target is titled 'Constraining
    during deployment can produce learning outside weights' and says retention alone
    does not establish a gain in adaptive capacity. The reader who does not follow
    the link gets a stronger claim than the target supports. Use the current title.
  level: warn
contract: verdict
target-sha256: 2214be116a950b1be4016de0633a69bd6e3df247b8c6750c25d37d0ef7013038
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/248c7f483c8b49dc81090398a3e73f15/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/artifact/reviews/a26b43ee4d6d440b6f55a836/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/248c7f483c8b49dc81090398a3e73f15/outputs/review-misleading-link-text.md
raw-output-sha256: 82c19f72d6d96bd0e07529208a7d0e454d82ed774f2623ab779d1d2d2eddb391
---

# Review

## Summary

All links resolve, including the `#what-addressability-does-not-buy` anchor in Reflection buys addressability. Body links to the learning, behavioral-authority, knowledge-artifact, system-definition-artifact, representational-form, deployment-time-learning, coevolution, codification-and-relaxing, selection-based-learning, proposal-selection-loop and contextual-activation targets match what their link text and sentences lead the reader to expect. Footer links whose text is a shortened title (First-principles reasoning, Verifiability gradient) are fine.

Three links mislead. The inline Scheduler-LLM citation is offered as evidence for a claim (compounding silent degradation under continual adaptation) that the target does not discuss. Two footer link texts carry stale titles that state stronger or exclusive claims than their targets now make.
