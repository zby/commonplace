---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
  against kb/instructions/review-gates/accessibility/unidentified-references.md
note: kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
note-sha256: 98643ed5cb9f96c25b62fc1fb6f075494b25c507e49ef7a7b4c51343a115fa7f
criterion: kb/instructions/review-gates/accessibility/unidentified-references.md
criterion-sha256: 422847c587793f494bfa140e10c46772cc1decaf72d3a611ec83daa39da288c3
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews
launch: c3a0c78c628a435a90d0c342719069f5
completed-at: '2026-11-20T18:52:50Z'
findings:
- scope: passage
  quotes:
  - For Commonplace, we choose changes by asking whether they yield more useful and
    better-warranted knowledge work for the human judgment spent, on balance.
  reason: Commonplace is named for the first time in a section heading and in this
    sentence without saying what it is. A reader who arrives without KB context cannot
    tell whether it is a project, a tool, an organization or a knowledge base, so
    the stated objective has no clear subject. Add a short inline identification,
    such as Commonplace, the framework for agent-operated knowledge bases that this
    note belongs to.
  level: warn
- scope: passage
  quotes:
  - one line in `AGENTS.md` reliably directs agents to instructions
  reason: '`AGENTS.md` is not identified as the project instruction file that agent
    runtimes load into their prompts. The next sentence ("Other prompts load that
    line too") partly supplies that context, so the example remains followable. An
    explicit gloss on first mention would make it clear at once.'
  level: info
contract: verdict
target-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/c3a0c78c628a435a90d0c342719069f5/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/artifact/reviews/f042f762ceb8f5bbdfe945a6/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/c3a0c78c628a435a90d0c342719069f5/outputs/review-unidentified-references.md
raw-output-sha256: 9be2a2e046e7da05323f307fc237ddf1617bccc62947cddfb99ab284771033b2
---

# Review

## Summary

The external names are identified adequately. Python and CPython are the subject of a worked comparison. TOML is introduced as "a TOML configuration". `asyncio.TaskGroup`, `tomllib` and `inspect.getargspec` are each described by what they do or what changed.

The gap is Commonplace. The note's normative section depends on it, but the note never says what kind of thing it is. `AGENTS.md` is a lesser case: the surrounding text largely implies what the file does.
