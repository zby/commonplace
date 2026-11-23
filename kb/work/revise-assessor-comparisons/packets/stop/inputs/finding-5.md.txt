---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
  against kb/types/note.md
note: kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
note-sha256: 2214be116a950b1be4016de0633a69bd6e3df247b8c6750c25d37d0ef7013038
criterion: kb/types/note.md
criterion-sha256: e111a08a6571349949088c99b6e0f61f50c60864f83079bdfc22a2ebcbb17a4b
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews
launch: f5154da7e6824f09bb4a14f353012644
completed-at: '2026-11-22T21:52:08Z'
findings:
- scope: document
  quotes: []
  reason: 'The Writing Shape asks that the claim''s limits be stated under their own
    `## Scope` heading, omitting it only when no limit is known. This note knows several
    limits but leaves them in body prose: the applicability condition to deployed
    systems whose loop must close during deployment; the exclusion of hand-authored
    incident edits as maintenance rather than continual learning; the remark that
    a loop need not touch all three forms every time; that parametric plasticity-stability
    problems persist; and that storage, contextual activation and parametric adaptation
    remain separate subproblems. Without a Scope section, a rescoping edit has to
    rewrite the argument, and scope-testing gates cannot find these limits where they
    look.'
  level: warn
- scope: passage
  quotes:
  - the addressability axis — the form-level trade space this note defers to
  reason: The footer gives several `grounds` edges to 'axes' (reach, addressability,
    sample efficiency, verifiability) that the body never names or uses. This annotation
    also says the note defers the form-level trade space to the explicit-retention
    note, but the body defers it to the representational-form coevolution note. The
    Writing Shape asks for links where the relationship helps traversal, and these
    relation glosses misdescribe what the body actually draws on.
  level: info
contract: verdict
target-sha256: 2214be116a950b1be4016de0633a69bd6e3df247b8c6750c25d37d0ef7013038
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/f5154da7e6824f09bb4a14f353012644/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/artifact/reviews/d91dfa95049372b93f0cea35/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/f5154da7e6824f09bb4a14f353012644/outputs/review.md
raw-output-sha256: f7596e48d0d49c94417b84fecd980c90ed52825dc8b4ef0889438e4a3f54e818
---

# Review

The note mostly follows the `note` type's authoring instructions. The title is a strong compressed handle for the claim. The first paragraph states the main claim: continual learning means governing behaviour-changing writes, not only persisting content. The note gives design rationale rather than imperative procedure, and it links densely to adjacent notes, both inline and in a Relevant Notes footer that matches the template's shape.

The unmet instruction is the `## Scope` section. The type spec makes it a requirement whenever a limit is known, so that a later edit can narrow the limits without rewriting the claim. This note knows and states its limits, but only inside the argument. They include the restriction to deployed systems with a loop that closes during deployment, the boundary between continual learning and maintenance, the point that not every update touches all three forms, and the persistence of parametric forgetting problems. Moving these limits into a Scope section would resolve the warning.

A minor traversal issue: several footer annotations describe "axes" that the body does not develop. One annotation also names a different deferral target from the one the body uses. This is informational only.

The `## Open Questions` section is optional and its absence is not a finding.
