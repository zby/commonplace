---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
  against kb/theory/COLLECTION.md
note: kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
note-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
criterion: kb/theory/COLLECTION.md
criterion-sha256: 95ad0d6ce3828b25282f7610268c4e1aca006fa34526bc2b4e4056f3e271cccd
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews
launch: 442e05017a1a4eadbcf82b286af84cb4
completed-at: '2026-11-20T18:54:15Z'
findings:
- scope: passage
  quotes:
  - For Commonplace, we choose changes by asking whether they yield more useful and
    better-warranted knowledge work for the human judgment spent, on balance.
  reason: 'Body composability and the placement test. This section records what Commonplace
    selected as its improvement objective and why. It does not illustrate or test
    the general claim. Under the contract, a record of a Commonplace selection belongs
    in kb/reference/. Explicitly scoped local material may stay in a theory note only
    as origin, illustration or test. The section is scoped honestly (''a practical
    commitment about the work we value''). Even so, it forms a second cluster: a note
    that cites this one as a premise for the general claim would also import Commonplace''s
    declared objective. Split the declaration into a reference artifact and link to
    it, or recast the section as an application of the general claim.'
  level: warn
- scope: passage
  quotes:
  - Four checks on local CPython 3.10.16 and 3.11.11 builds illustrate what enters
    the judgment.
  reason: The Python checks and the random.py diagnostic comparison report concrete
    measurements (median timings, version-specific behaviour), but the note links
    no retained record of them. They act as illustrations rather than corroboration,
    so the contract does not require an evidenced-by edge. A link to a retained report,
    if one exists, would let readers inspect the runs instead of relying on the summary.
  level: info
- scope: document
  quotes: []
  reason: 'The description frames the note as how-to guidance (''How to decide whether
    to keep a change ...''), and parts of the body give imperative steps (''First
    ask what improved ...''). The body still argues why on-balance judgments work
    and where they fail: the alternative, the affected parties, the time period, and
    reversal-sensitive investigation. That keeps the note within theory and stops
    it from being a procedure that belongs in kb/instructions/. If the decision steps
    grow into an ordered procedure, they should move there.'
  level: info
contract: verdict
target-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/442e05017a1a4eadbcf82b286af84cb4/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/artifact/reviews/997161ba2c3659097fafed7b/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/442e05017a1a4eadbcf82b286af84cb4/outputs/review.md
raw-output-sha256: 5fca1f4d324b6a261f4c82279098e214da56a2a97a5c937d1358982d8b4ed172
---

# Review

The note belongs in `kb/theory/`, and it mostly follows the collection's conventions. Once its named system choices are scoped, a substantive claim about the design space remains. That claim is that comparative, on-balance reasons can justify keeping a change without a global score. It also says when to investigate an unknown: when a plausible answer could reverse the choice. The Python and library cases come from domains outside KB design, which counts toward explanatory-reach. The note marks its boundaries in prose: a binding requirement overrides an on-balance judgment, a preference does not assign credit to a component, and the partial order does not do the weighing.

Outbound links follow the contract. Inline links use connectives such as "By contrast" and "Nor does … identify". The single footer edge (`grounds`) points to a theory note and carries a context phrase. The note does not present the tag-coverage trace as corroboration of its claim; it uses the trace only to show a local gain. No sources are cited, so the grounding bound is not engaged.

The unmet convention is body composability. The section "What Commonplace chooses to count" records Commonplace's own selection of an improvement objective, and that selection is part of the note's contribution. A selection like this belongs in `kb/reference/`. Keeping it here means that anyone citing the general claim also imports the local commitment. The rest of the Commonplace material is acceptable: the `AGENTS.md` line and the validator are explicitly scoped illustrations of the general rule.
