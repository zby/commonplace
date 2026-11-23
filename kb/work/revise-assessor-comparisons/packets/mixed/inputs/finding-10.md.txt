---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
  against kb/instructions/review-gates/structural/general-before-specific.md
note: kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
note-sha256: 98643ed5cb9f96c25b62fc1fb6f075494b25c507e49ef7a7b4c51343a115fa7f
criterion: kb/instructions/review-gates/structural/general-before-specific.md
criterion-sha256: 9a0e5698ffe8e1d4c95eaca4fc4cb00fd74fd70f2c9433f1cc1db1a02ffdd767
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews
launch: d51bf6640d4942339b386f73b11d273b
completed-at: '2026-11-20T18:53:32Z'
findings:
- scope: passage
  quotes:
  - 'A release judgment: Python 3.11 over 3.10'
  - 'Three choices fix the comparison:'
  reason: 'The case-study section on Python 3.11 versus 3.10 (with the library-hours
    example) comes immediately before ''What analysis can settle'', which states the
    general pattern those cases instantiate: fix the alternative, who gains and who
    loses, and the period; investigate an unknown only if a plausible answer could
    reverse the choice. The specific section exemplifies that rule rather than qualifying
    it: whole-release choice, losses on identifiable callers, and ''test its dependencies
    before deciding'' are instances of the three choices and the reversal test. Under
    the tiebreaker this is a WARN. The example-first order looks deliberate, since
    the intro is also built on cases. A fix could keep the cases while stating the
    three choices briefly before the release table, or could open the release section
    by saying which of the general choices it illustrates.'
  level: warn
contract: verdict
target-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/d51bf6640d4942339b386f73b11d273b/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/artifact/reviews/5155a3014eee8df19cb94311/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/d51bf6640d4942339b386f73b11d273b/outputs/review-general-before-specific.md
raw-output-sha256: ace2ddc8ab80cce3315e2a25072d31362ffe3ec762135f174721d5f3fa014b7f
---

# Review

The body has four sections after the introduction:

1. "A release judgment: Python 3.11 over 3.10": specific, with proper nouns, version numbers and a hypothetical library case.
2. "What analysis can settle": general. It covers the limits of analysis, the three choices that fix a comparison, and the rule for investigating an unknown.
3. "What Commonplace chooses to count": specific to Commonplace's objective.
4. "What to do with an incomplete comparison": procedural guidance illustrated with Commonplace cases.

Pair 1→2 fits the failure mode. Section 1 presents instances, and section 2 then states the rule they illustrate. The release section does not challenge or limit that rule. Its points about whole-release alternatives, distributed losses and testing a dependency before acting are the rule applied. That makes it exemplifying, so the result is WARN rather than INFO.

Pair 2→3 runs from general to specific, which is the order the gate expects.

Pair 3→4 is not a specific-then-general inversion. Section 4 does not state a general pattern that Commonplace's chosen objective exemplifies. Instead, it applies the objective and the earlier rules to Commonplace examples.
