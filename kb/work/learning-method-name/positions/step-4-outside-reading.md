# Outside reading of the rewritten definition

A fresh Codex sub-agent read the [draft](../draft-definition.md) and the
[on-balance note](../../../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md)
at commit `31803a8e4`. It received the same eight vignettes as the
[previous Codex reader](./step-3-outside-reading.md), with no conversation
history, expected answers or prior reports. It confirmed that it consulted
only the two assigned files. The coordinator recorded expectations before
launch and wrote this summary. The reader confirmed its own response and
has not reviewed the summary.

## Results

All eight membership readings matched the expectations recorded for the
rewrite, including cases where a fact about later use was missing. The draft
itself works through several of these examples. The test measures whether a
fresh reader can recover the intended distinctions from the text. It leaves
their application to unfamiliar systems untested.

| Case | Reader's placement and grounds |
|---|---|
| A. Team adds a routing rule | Inside if later team tasks use the rule. The team could decline the addition. Later misrouting could prompt targeted correction. The criterion for admitting routing rules could still be fixed. |
| B1. Repairer keeps links that pass a fixed validator | The validator can reject a rewrite. The repairer qualifies as single-loop if its **own** later work consumes the links. Use by outside readers alone puts it outside. |
| B2. Team changes the validator after bad repairs | The same own-use condition applies at the team boundary. Changing which repairs pass is double-loop for repairs. Classifying validator edits requires knowing how the team judges those edits. An episode requires a later decision affected by the revised validator. |
| C. Clicks directly update article ranks | Outside. A readable table used to select articles satisfies the store condition. The click changes the rank directly, without a proposed edit that a judge can reject. A later fall in clicks can lower that article's rank without introducing such a decision. |
| D. Coding agent selectively appends lessons | Inside as a capacity if the lessons can guide later tasks. Loading the file shows access. An episode requires a lesson to change what the agent does. Append-only entries leave open whether the admission criterion can change. |
| E1. Weekly fine-tuning | Outside for ordinary gradient updates. The learned contents in the weights cannot be read and pointed at individually, and the optimizer computes updates directly. |
| E2. Team records deployment choices and rolls back | Inside for deployment edits if later serving uses the choice. An evaluation can defeat a proposal. A rollback prompted by later observations corrects one deployment choice and can undo a bundle of weight changes in operation. |
| F. Agent revises a plan discarded at task end | Outside across tasks. Within the task it can qualify if the agent could keep the old plan and later steps use the revision. The vignette leaves the trigger and subsequent effect unspecified. |

## What changed since the previous reading

- **Who consumes the store.** Both readers recognized the fixed link gate.
  This reader explicitly required the repairer's own later use in B1,
  resolving the previous partial match.
- **What can be rejected.** The previous reading admitted the click ranker
  if ranks drove later selection. This reader excluded it even on that
  assumption. The rewrite changed the intended placement by requiring a
  proposed edit that can be rejected. The fixed validator in B1 still
  qualifies as a decision.
- **What single-loop means.** The reader assessed the criterion for
  admitting a lesson independently of whether the lesson can be reversed.
  The earlier reversal wording no longer left append-only learners without
  a possible kind.

The reader found one distinction still required care: a routing rule can
be the **item** judged when a team admits rules and a **criterion** when
the team judges later routing choices. It resolved the ambiguity by naming
the class of later decisions the edit governs. It found the term natural
for the routing team and less intuitive for a mechanical validator, whose
inclusion it could recover from the explicit fixed-criterion clause.

For *learned*, the reader compared the current system with the same system
with only the tested edit removed, holding the work, affected people and
horizon fixed. Every reasonable way of scoring the work as a whole must
favor the edit. None of the cases supplies that comparison or establishes
displacement by a higher-scoring alternative.
