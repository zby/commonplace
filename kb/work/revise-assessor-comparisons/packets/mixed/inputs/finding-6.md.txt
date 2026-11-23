---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
  against kb/types/note.md
note: kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
note-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
criterion: kb/types/note.md
criterion-sha256: e111a08a6571349949088c99b6e0f61f50c60864f83079bdfc22a2ebcbb17a4b
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews
launch: 48304ea68f5f486cb18f054cd613064f
completed-at: '2026-11-20T18:53:54Z'
findings:
- scope: document
  quotes: []
  reason: 'The type spec asks that the claim''s limits be stated under their own `##
    Scope` heading, omitting the section only when no limit is known. This note knows
    several limits but scatters them through the body: the Commonplace objective is
    ''not a claim that every project should use the same measure''; the release checks
    are ''not a survey of how often each reason applies''; an on-balance judgment
    ''does not override a binding requirement''; preferring the successor does not
    assign credit to a component; and the availability of reasons ''does not establish
    that any particular agent judges well''. With no `## Scope` section, a rescoping
    edit has to rewrite body prose, and scope-testing gates will not find these limits
    where they look.'
  level: warn
- scope: passage
  quotes:
  - Is Python better than it was twenty years ago?
  reason: The spec asks that the main claim or mechanism come near the top. The opening
    reaches the claim through a Python example, and the general statement (preferences
    defended by reasons about which work changed, for whom, and why, without a score)
    is only implicit in the second paragraph. The title carries the claim, so this
    is acceptable, but stating the general mechanism in one sentence before or right
    after the example would make the claim recoverable without reading through the
    case.
  level: info
contract: verdict
target-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/48304ea68f5f486cb18f054cd613064f/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/artifact/reviews/2df2578fec47e8554720079e/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/48304ea68f5f486cb18f054cd613064f/outputs/review.md
raw-output-sha256: 124178af86aaea8cc560924516b9343e20e7eb9ae9edfcd414ac73fa0e072ffb
---

# Review

The note mostly does what the `note` type spec asks. The title compresses the claim. The description says why to retrieve the note: deciding whether to keep a change with mixed gains and losses, and which uncertainties to investigate. The note links to adjacent notes both inline (the tag coverage trace, the factory comparison, the contrast note) and in the footer (the declared-objective note), and each link says what it contributes. It keeps to design rationale. Its few imperatives ("investigate an unknown only if a plausible answer could reverse the choice", "First ask what improved") are decision criteria with their reasons attached, not procedural steps that belong in an instruction.

The one unmet authoring instruction is the `## Scope` section. The spec allows omitting it only when no limit is known, and this note states several limits, all of them inline. Gathering them under `## Scope` would satisfy the spec without changing the argument. The info finding about where the main claim first appears is advisory: the claim is reachable from the title and the first two paragraphs, but it appears as an instance before it appears as a general mechanism.
