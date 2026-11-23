purpose: "Explain how on-balance judgments guide decisions without a global measure, and where analysis helps or stops."
must-keep:
  - "The agreed title: On-balance judgments can guide improvement without a global measure."
  - "The section heading What Commonplace chooses to count and its anchor what-commonplace-chooses-to-count, used by four references."
  - "Commonplace's objective is a practical choice, not a universal measure: This is a practical commitment about the work we value, not a claim that every project should use the same measure."
  - "Contrasting worked examples stay, including the Python release judgment (3.11 over 3.10) and the AGENTS.md routing-line threshold."
  - "For the decision at hand, investigate an unknown only if a plausible answer could reverse the choice."
  - "For Commonplace, we choose changes by asking whether they yield more useful and better-warranted knowledge work for the human judgment spent, on balance."
  - "Automation alone does not answer that question."
  - "A pass answers that defined question; an on-balance judgment does not override a binding requirement."
  - "Analysis can expose that trade-off; it cannot supply the weights merely by assigning each feature a score."
  - "Even a perfect attendance count would not decide which hours to keep."
  - "The library-hours case is marked as hypothetical."
passes:
  - pass: narrow-overclaims
    scope: "Two sentences only: 'Those reasons can be checked independently of who offered them.' (narrow to the factual reasons; the weighing is criticizable, not checkable) and 'The compatibility cost falls on identifiable callers' (narrow to losses a team's tests and dependency inventory can find)."
  - pass: fix-strategy-taxonomy
    finding: kb/reports/state/review/results/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md/accessibility/undefined-terms.md
  - pass: readability-and-flow
    scope: "The opening paragraphs, the library-hours paragraph in the release section, and the first paragraph and three bullets of 'What analysis can settle' (not the bold reversal-rule paragraph). Move the library-hours case to support the 'Who gains, and who bears the loss?' question and shorten that bullet's gloss to a back-reference. Cut 'Asking for another month of counts would miss the disagreement.' Keep the hypothetical marker. Add one sentence after the opening examples that states the existing two-part claim, scoped to the decision at hand. Do not touch 'What Commonplace chooses to count', the AGENTS.md decision paragraph or the closing paragraph."
  - pass: fix-strategy-taxonomy
    finding: kb/reports/state/review/results/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md/sentence/parsing-ambiguity.md
  - pass: fix-strategy-taxonomy
    finding: kb/reports/state/review/results/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md/sentence/stock-phrases.md
stop: null
