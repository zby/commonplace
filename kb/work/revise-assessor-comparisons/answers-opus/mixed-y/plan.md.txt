purpose: "Explain how on-balance judgments guide decisions without a global measure, and where analysis helps or stops."
must-keep:
  - "The title 'On-balance judgments can guide improvement without a global measure' is kept."
  - "The section heading 'What Commonplace chooses to count' and its anchor what-commonplace-chooses-to-count, used by four references, are kept."
  - "Commonplace's objective is a practical choice about the work Commonplace values, not a universal measure that every project should use."
  - "The contrasting worked examples are kept, including the Python release judgment and the routing-threshold case of the AGENTS.md line."
  - "For the decision at hand, investigate an unknown only if a plausible answer could reverse the choice."
  - "For Commonplace, we choose changes by asking whether they yield more useful and better-warranted knowledge work for the human judgment spent, on balance."
  - "We choose this objective because we repeatedly have to decide whether a gain is worth the judgment it takes to build, operate, and maintain the change. Automation alone does not answer that question."
  - "A pass answers that defined question; an on-balance judgment does not override a binding requirement."
  - "The library-hours case is marked as hypothetical, and what transfers to a KB decision is the question of whose loss a higher total can hide."
passes:
  - pass: fix-strategy-taxonomy
    scope: "First mention of Commonplace in the paragraph beginning 'For Commonplace, we choose changes'; add an identification without changing the heading or the objective's wording"
    finding: kb/reports/state/review/results/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md/accessibility/unidentified-references.md
  - pass: fix-strategy-taxonomy
    scope: "The sentence 'Whether maintaining marked heads is worth the effort depends in part on who relies on them to stop searching.' in 'What to do with an incomplete comparison'"
    finding: kb/reports/state/review/results/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md/accessibility/undefined-terms.md
  - pass: readability-and-flow
    scope: "The opening paragraphs (add one general sentence after the Python 2/3 example stating both halves of the claim, with the reversal rule scoped to the decision at hand); the opening of the 'A release judgment' section (at most a lead-in clause); the library-hours paragraph, moved into 'What analysis can settle' as the illustration for 'Who gains, and who bears the loss?', with 'Asking for another month of counts would miss the disagreement.' cut and the bullet gloss shortened to a back-reference. Do not touch the 'What Commonplace chooses to count' section, the paragraph beginning 'The case for 3.11 is not', the bold reversal-rule sentence, the AGENTS.md decision paragraph or the closing paragraph."
  - pass: fix-strategy-taxonomy
    scope: "'Python 3 rejects the mixed addition even on the first name.' and 'a longer table or a different mix of tasks can change the balance. Compare the whole table with its earlier, shorter version'"
    finding: kb/reports/state/review/results/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md/sentence/parsing-ambiguity.md
stop: null
