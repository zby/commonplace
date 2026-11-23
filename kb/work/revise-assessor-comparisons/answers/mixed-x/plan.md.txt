purpose: Explain how on-balance judgments guide decisions without a global measure, and where analysis helps or stops.
must-keep:
  - Keep the title “On-balance judgments can guide improvement without a global measure”.
  - Keep the heading “What Commonplace chooses to count” and its what-commonplace-chooses-to-count anchor for the four references. The objective is a practical Commonplace choice, not a universal measure.
  - Keep contrasting worked examples, including the Python release judgment and the AGENTS.md routing threshold; the possible threshold loss is not an observed failure.
  - For the decision at hand, investigate an unknown only if a plausible answer could reverse the choice.
  - A preference need not rank all releases and cannot override a binding requirement.
passes:
  - pass: fix-strategy-taxonomy
    finding: kb/reports/state/review/results/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md/accessibility/undefined-terms.md
    scope: Only the tag coverage example; identify the index marked as listing every member and why someone can stop searching.
  - pass: fix-strategy-taxonomy
    finding: kb/reports/state/review/results/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md/structural/general-before-specific.md
    scope: Opening second paragraph only. Preview the comparison and the current-decision reversal test before the remaining cases. Keep the opening case, the title and the later argument in place.
  - pass: fix-strategy-taxonomy
    finding: kb/reports/state/review/results/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md/kb/instructions/compression-bundle/detail-overhang.md
    scope: Only the last two sentences of the library hypothetical; trim the repeated counting point while retaining hypothetical status, the hidden loss and both policy branches.
  - pass: fix-strategy-taxonomy
    finding: kb/reports/state/review/results/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md/sentence/parsing-ambiguity.md
    scope: Only the first-name reference in the Python opening and the table references in the last two sentences of the routing example. Identify the ASCII input and the AGENTS.md routing material respectively, without changing the decision branches.
stop: null
