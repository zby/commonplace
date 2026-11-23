---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
  against kb/instructions/review-gates/accessibility/undefined-terms.md
note: kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
note-sha256: 0177d84330a5bbe930bebfc55c1c352405b81cb00146dd7b5389717615b8d3fb
criterion: kb/instructions/review-gates/accessibility/undefined-terms.md
criterion-sha256: a29bd905ec12b7a7c8375529e490cfde6711bb4feef5529546a92fda0419af38
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews
launch: 5cfa66d6f22840dea82b6bc7e07bc81a
completed-at: '2026-11-22T21:51:24Z'
findings:
- scope: passage
  quotes:
  - search, reject-capable evaluation, and operative retention
  reason: '"Operative retention" and "reject-capable evaluation" are KB-specific components
    of the proposal-selection loop. They carry the note''s discriminator between learning
    and maintenance but get no inline gloss. A reader who does not follow the link
    cannot tell what makes retention "operative" (presumably that the retained change
    actually governs later behaviour) or what an evaluation that is "reject-capable"
    excludes.'
  level: warn
- scope: passage
  quotes:
  - Storage, [contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md),
    and parametric adaptation
  reason: '"Contextual activation" is a KB term used without a gloss. The sentence
    lists it as a subproblem distinct from storage, but never says what it is, such
    as stored knowledge being brought into play when a situation calls for it. The
    reader must follow the link.'
  level: warn
- scope: passage
  quotes:
  - the software learns by [selection](./definitions/selection-based-learning.md)
    that people perform on it
  reason: Selection-based learning is active vocabulary. The first mention links it
    but gives only the bare word "selection" with no gloss of the mechanism, such
    as keeping candidate changes that pass evaluation and discarding the rest. The
    next sentences partly recover the meaning ("the system does the selecting itself";
    search, evaluation and retention), so the reader can infer it from context.
  level: info
- scope: passage
  quotes:
  - belongs to a consumption path, not to stored bytes
  reason: '"Consumption path" is not defined at first use. The next sentence supplies
    an implicit gloss (an artifact consumed as evidence versus consumed to instruct),
    so the meaning can be inferred. A short inline phrase such as "how a component
    reads and uses the artifact" would remove the forward dependency.'
  level: info
- scope: passage
  quotes:
  - The broader trade space and coupling among their improvement loops belongs to
  reason: '"Representational-form coevolution" is introduced only as link text. The
    surrounding words (the forms'' coupled improvement loops) let a reader infer roughly
    that the forms are improved together, so this is minor.'
  level: info
contract: verdict
target-sha256: 2214be116a950b1be4016de0633a69bd6e3df247b8c6750c25d37d0ef7013038
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/5cfa66d6f22840dea82b6bc7e07bc81a/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/artifact/reviews/f8a9bdd57bb64f87495dcb73/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/5cfa66d6f22840dea82b6bc7e07bc81a/outputs/review-undefined-terms.md
raw-output-sha256: 7efba3ab62d23304aba63e5e2b9f9df1015e4f0592f63ea517c581fe4f7d9371
---

# Review

Most technical terms have adequate local definitions. Behavioral authority, knowledge artifact, system-definition artifact, the three representational forms, plasticity-stability and catastrophic forgetting, governance and codification/relaxing are each glossed in the sentence that introduces them or the one before.

Two terms fall short. "Operative retention" (together with "reject-capable evaluation") is the core of the note's test for when a write counts as continual learning, yet the note gives the reader only link targets for it. "Contextual activation" is named as a remaining subproblem without saying what it means. Both need a short inline gloss. The remaining findings are informational: context partly recovers their meaning.
