# Shape of the research program note

Workshop brief requested by the operator, 2026-11-21. Write the research program note, not a second definition or an experiment report.

## What the note is for

The [definition](../../theory/definitions/deliberative-learning.md) says what deliberative learning is. The [lead article](../../articles/deliberative-learning-judgment-in-place-of-a-value-function.md) argues that a fixed-weight language model could judge changes to its own store where no fixed test is adequate. The note should tell a reader **which comparisons would distinguish that conjecture from what Commonplace can already do with its operator**. For each comparison, say what a positive result would establish and what it would leave open.

## 1. Start with three claims, not a single verdict on Commonplace

- **Membership today.** Under [Commonplace’s declared frame](../../reference/commonplace-declared-frame.md), the system includes the agents, commands and operator. Its store includes library notes, instructions, types, validators and code used across tasks. Name a class of edits, such as changes to routing instructions. Show who can reject a proposed edit, how later work uses what is kept, and how a misleading review criterion can itself be revised for future edits of that class. This is a claim about a human-assisted system’s capacity. A team with a handbook can qualify too.
- **Whether a particular edit was learned.** Admission can be a sound decision to try a reversible edit while its benefit remains unknown. To assess that edit, compare fresh work with and without it, keeping the rest of the store intact except for edits that depend on it. Name those dependencies, whose gains and losses count, and the horizon. Changed behavior shows the edit mattered; it does not say whether the change was for the better.
- **Autonomous judgment.** The conjecture is that a fixed-weight model can make the admission, correction and criterion-revision decisions without a person making them. An episode with the operator selecting is evidence about the human–machine system, not a test the autonomous model either passed or failed.

## 2. Give each capability a comparison that distinguishes it

Fix the model, task family, available evidence and budget before a test. State what result would count against the prediction **for that setup**. One unsuccessful run cannot rule out the capability for all fixed-weight models.

| Capability | Comparison and interpretation |
|---|---|
| **Admission** | Give the model and a fixed gate the same proposals and evidence. Include useful edits the gate rejects and harmful edits it admits. Compare which edits each keeps and their consequences on fresh work; also check what admitting everything would have yielded. If the gate does as well, the test has not shown an advantage for model judgment here. A persuasive explanation alone does not establish one. |
| **Targeted correction** | Put a harmful edit and an independently useful edit in the same batch. Supply evidence from later use without identifying the culprit. Can the learner remove the harm while preserving the gain? Compare its repair with leaving the batch intact and rolling it all back. If there is nothing useful to preserve, a tie with rollback cannot distinguish accurate diagnosis from indiscriminate removal. |
| **Criterion revision** | Compare later decisions on the same proposals under the old and revised criteria. A retained revision that changes which proposals pass shows that the criterion changed in practice. Whether those decisions improved is a further test: a check that rejects everything can prevent every bad admission. |

**Net gain is a separate claim about the whole loop.** All three capabilities can work while the accumulated edits make the system worse. Compare the evolving store with an otherwise matched system using the starting store over the same fresh work and horizon. Count upkeep and human supervision as well as task outcomes; use the lead article’s four hazards to identify costs local approvals could miss. If reasonable measures disagree, report the disagreement. Neither withholding the entire store nor demonstrating one successful repair establishes the net benefit of continued revision.

## 3. Name one first experiment: repair a misleading routing check

Give the model the existing check and traces in which overbroad routing instructions passed it and later misdirected work. Let the model decide whether and how to revise the check. Supply the evidence, not the diagnosis or replacement rule. Compare the old and resulting checks on the same unseen proposals, including sound rules that should still pass. On later tasks, record both misroutes prevented and useful guidance lost.

This test distinguishes three outcomes: no effective change to later decisions; different decisions with no demonstrated gain; and a revision that preserves useful guidance while preventing misroutes. It tests criterion revision, not sustained autonomous learning. Link the [testing supplement](../../articles/testing-whether-a-theory-builder-learns.md) for other designs rather than reproducing its seven tests.

Record who proposed, diagnosed, selected and installed the change. People can design the trial and independently assess outcomes afterward without judging inside the loop. A person who selects the best of several attempted repairs *is* inside it. Describe this as a proposed experiment, not a run already commissioned or completed.

## 4. Explain why the development path matters

Move decisions out of the operator’s hands one kind at a time. Report separately which operations still complete and which edits improve later work. The practical payoff to test is that a misleading check gets repaired without waiting for a person to notice the pattern and redesign it. Whether this saves human judgment overall depends on supervision and cleanup as well as the repair. The Bitter Lesson condition belongs here: computation must eventually supply and revise what the hand-written starting state provided.

## 5. State what evidence exists and where rivals disagree

- Commonplace reports no completed end-to-end demonstration of sustained autonomous double-loop learning.
- The [Python change judgment probe](../../reports/retained/python-change-judgment-probe-2026-11-20/README.md) was designed but not run. The [follow-on comparison](../../reports/retained/python-change-judgment-probe-2026-11-20/comparison/README.md) collected three model answers. Human responses, the independent mixed reading and the case variant are pending. It probes reasons given for a decision, not the later effects of an admitted edit.
- [The 2026-08-30 revision](../../theory/evidence/commonplace-revision-used-theory-guided-computational-search.md) is an observed episode with the operator selecting.
- State rival predictions only where they differ. A successful routing repair need not involve forming a new concept, so it need not decide Sutton and Javed’s claim about continual weight updates. Likewise, a stalled harness-evolution run does not by itself identify a failed judge: distinguish evidence available to the proposer from evidence available to the scorer.

## Deliverable and limits

Write a new theory note of about 1,200 words. A working title is “Commonplace tests whether a language model can run deliberative learning with no person judging.” Put the claims and their comparisons before the experiment. Link the definition instead of restating its taxonomy. Candidate tags: `deliberative-learning`, `self-improving-systems`, `learning-theory`. Once the note exists, link it as the program from the README and landing page and list it in the deliberative-learning tag head.

Leave the [older theory-builder program](../../theory/commonplace-builds-a-theory-builder-and-tests-whether-it-learns.md) in place with its rewrite notice. Criticism of theory content belongs to that program. Addressability matters here because a repair must identify an edit; persistence matters because later tasks must use it. Do not import either as a separate hierarchy or promise a [sample-efficiency advantage](../../theory/retained-theories-may-improve-sample-efficiency.md) over weight training.
