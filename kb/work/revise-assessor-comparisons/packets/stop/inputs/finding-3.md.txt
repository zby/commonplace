---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
  against kb/instructions/compression-bundle/marginal-value-redundancy.md
note: kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
note-sha256: 0177d84330a5bbe930bebfc55c1c352405b81cb00146dd7b5389717615b8d3fb
criterion: kb/instructions/compression-bundle/marginal-value-redundancy.md
criterion-sha256: a4a481e4011441b80abc2140583e88da024aba95b0b14bbb973dca94c303dbb7
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews
launch: dab4048accd947108a8a5add82a5dae7
completed-at: '2026-11-22T21:53:44Z'
findings:
- scope: passage
  quotes:
  - Persistence alone therefore does not create a governed behaviour-changing write.
  reason: The paragraph's closing sentence restates its opening ('requires more than
    retaining new content') and its middle ('persistence does not decide which retained
    item should shape behaviour or with what force'). The authority-path sentences
    in between already carry the conclusion, so this closing restatement adds no admission
    beyond the opening. Cut it, or end the paragraph on the knowledge-artifact / system-definition-artifact
    distinction.
  level: warn
- scope: passage
  quotes:
  - It need not touch all three every time.
  reason: Defensive redundancy. The sentence before it already says a loop must 'coordinate
    whichever forms that update touches', which implies that one update need not touch
    all three forms. Cut the trailing sentence.
  level: warn
- scope: passage
  quotes:
  - broadening the system boundary does not remove them
  reason: Defensive clause. 'Parametric continual learning keeps its own plasticity-stability
    and catastrophic-forgetting problems' already says these problems remain. The
    clause after the semicolon guards against a misreading that 'keeps' already rules
    out. Cut it, or fold the system-boundary point into the next sentence's 'But if
    prompts, tools…' contrast.
  level: warn
- scope: passage
  quotes:
  - 'The same edit hand-authored in reaction to an incident is maintenance: the system
    learned, and people outside its loop did the selecting.'
  reason: 'This repeats the paragraph''s earlier distinction that hand-authored release-engineering
    changes ''are learning too: the software learns by selection that people perform
    on it'', while continual learning needs the system to do the selecting itself.
    The incident example does give the discriminator a concrete case. The paragraph
    still states the same contrast twice around the proposal-selection definition.
    Keep one statement: either fold the incident example into the release-engineering
    sentences or drop those sentences in favour of the example.'
  level: warn
- scope: passage
  quotes:
  - Continual-learning systems must close that evidence-responsive loop at the cadence
    their environment requires.
  reason: This may only echo paragraph 2's constraint that deployment lessons must
    take effect before a full retraining cycle. It may also do conclusion work by
    turning the selection discriminator into an operational requirement. I am unsure
    whether it earns a separate sentence.
  level: info
contract: verdict
target-sha256: 2214be116a950b1be4016de0633a69bd6e3df247b8c6750c25d37d0ef7013038
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/dab4048accd947108a8a5add82a5dae7/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/artifact/reviews/83ce2d08d2a8dc6e956dbf01/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/dab4048accd947108a8a5add82a5dae7/outputs/review.md
raw-output-sha256: a41aeed20f3b0934c6422de6786bcf5b43771bb457d79957ba2673991de7c73b
---

# Review

The note is compact, and most of it does necessary work. It has four paragraphs:

1. The claim and the authority-path distinction.
2. The deployment constraints.
3. The form surface.
4. Governance and the continual-learning discriminator.

The links carry the mechanisms, so the body stays short. The redundancy comes in a few places where a closing or trailing clause restates what the sentence before it already established. In each case, the sentence before it already does the work, so this is defensive redundancy rather than rigor.

The biggest compression gain is in the fourth paragraph. It states the human-selection versus system-selection contrast twice. First it says release engineering is learning by people's selection while continual learning needs the system to select. Then it says an incident-driven hand edit is maintenance because people did the selecting. Keeping one statement would tighten the paragraph without losing the discriminator.

Several passages pass and should stay:

- The sentence on form-placement revisability, linked to codification and relaxing, adds a dynamic the rest of the note does not state.
- The final sentence on storage, activation and parametric subproblems turns the argument into a scoping stance: governance relates these subproblems rather than replacing them. It does not merely recap them.
