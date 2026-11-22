# Checks for the selection-based-learning definition

Maintenance material for [selection-based learning](./selection-based-learning.md).
Apply the checks when changing that definition, including cross-references
that change its meaning. Report affected cases before revising their expected
placements. Keep case numbers stable and make changes to assumptions
explicit.

These cases check selected boundaries. Unchanged answers do not prove that
the entire scope is unchanged. Report any additional scope difference the
proposed change exposes.

Adopted 2026-11-21 with the definition. Cases 1–20 were placed while the
definition was drafted. Cases 21–23 were open. Later on 2026-11-21 the
operator removed the legible, addressable store from the conditions. That
change flipped cases 5 and 16 and added cases 24 and 25.

On 2026-11-22 the definition was rewritten. It no longer ties the term to
self-improvement, no longer distinguishes an open from a fixed criterion, and
no longer mentions correction. It adds the ladder of what naming a boundary
adds. That rewrite flipped case 14 and settled cases 21 and 23. Later the
same day the definition adopted the loop note's causal wording for
evaluation, which settled case 22.

## Tests for any change to the definition

1. **Process, not outcome.** No condition may require that a change improved
   the system, or that the system can later correct a kept change. Citing
   the term as evidence that the system improved or corrects itself is a
   misuse.
2. **One fixed measure is inside.** Evaluation by one fixed measure and
   evaluation across several measures both count. A proposed condition that
   puts a system outside because it evaluates by one simple measure, or
   because it never revisits a kept change, is a scope decision.
3. **Name the system and the level.** Run the checks on the named system and
   the named class of changes. Selection done outside the named system still
   makes its learning selection-based. It does not make the system
   self-improving or double-loop. Do not credit an automated loop with
   selections or criterion revisions its designers make elsewhere.
4. **A readable store is not a condition.** Where the change is held does
   not decide membership. A proposed condition that puts a system outside
   because its retained contents are opaque or unwritten is a scope decision.
5. **A change reports the cases it flips.** Run the proposed wording against
   the cases below. A change that flips none is a wording change. A change
   that flips one is a scope decision for the operator.

## How to read a case

Each case is checked on two conditions at a named level. Some rows also
place the case on the ladder.

- **R, retention.** The change is to something the named system retains, and
  its later work uses it. Where the change is held does not matter.
- **S, selection.** A change of the named class is proposed. It is evaluated, and the
  result decides whether the change is made, or undone if already made.
  The evaluation need not be a separate stage or actor, but it can reject
  the change, and the rejection is its own event. It may apply one fixed measure or compare
  across several measures. A direct update, in which the evidence determines
  the change, fails S. So does a change written automatically or on a
  trigger. The [loop note](../a-proposal-selection-loop-requires-search-evaluation-and-retention.md)
  adds that rejecting a change must be an event distinct from producing the
  next candidate.
- **Level.** The class of changes. One system can be outside for one class
  and inside for another.
- **Ladder.** *Self-improving* when the named system also does the
  selecting. *Double-loop* when the named system can revise what it selects
  by, so that a different criterion governs later decisions of the class
  ([single-loop and double-loop](./single-loop-and-double-loop-learning.md)).
  A different verdict under the same criterion is not a different criterion.
  Where a case does not specify the capacity, the kind is undetermined.

Membership requires R and S. No case assumes improved capacity unless it
specifies the comparison.

Some rows add a remark on **correction**. It is additional description, not
part of the definition, and no verdict depends on it. Correction is
*targeted* when later evidence can count against a particular kept change,
*bundle* when it can only restore an earlier state, and *none* when a kept
change is only ever displaced by a higher scorer.

## Stipulated cases

| # | System, store and decision | Expected result and discriminator |
|---|---|---|
| 1 | A team keeps a routing rule after weighing saved searches against misrouting. Later failures can lead it to revise the rule. | Inside: R and S, with evaluation across several measures. The team selects its own rule, so it is self-improving for this class. Kind undetermined. Revised weights on saved searches against misrouting for later cases would show criterion revision; correcting this one rule does not. If later work is worse, the team made a bad selection. It did not cease to use the process. |
| 2 | A service appends every interaction to a searchable log. A later tool can edit the log, but nothing selects which entries to keep. | Outside: automatic storage evaluates no entry, so R alone does not give S. Keeping everything is not a fixed measure, because no result depends on the entry. Introducing the logging is a different class of change, which could be selected. |
| 3 | The team in case 1 still weighs the reasons, but no later round can challenge its decision or act differently in response to an error. | Inside on R and S. "Can be rejected" applies when the change is proposed. No condition requires that a kept change can be revisited. |
| 4 | A link repairer keeps a patch exactly when its fixed validator passes. Separately, the maintaining team reviews where that test suffices, changes the validator after bad repairs, and weighs ambiguous repairs itself. | Repairer alone: inside on R and S, since the validator is one fixed measure; single-loop. R holds only if later repair runs consume the repaired documents. If the documents are only its output, the repairer retains nothing of its own. Team plus repairer, for repairs: inside, double-loop, because the team changes the validator. |
| 5 | A team judges whether to deploy a better model release, but the training run retains only numeric weight updates under a fixed loss. | Depends on the level. Weight updates: outside on S. Each gradient step is a direct update, so no update is proposed and none can be rejected. The deployment verdict does not control which weight updates are made. Release choices: inside on R and S, provided later work uses the deployed release. The model alone learns by a selection the team performs; the model with the team is self-improving for release choices. Kind undetermined. **Flipped 2026-11-21:** the earlier placement was outside, because the weights are not a readable store. |
| 6 | A team keeps an unexplained prompt variant after weighing mixed outcomes and revisits the choice on new evidence. By stipulation it never formulates or criticizes a claim about why the prompt works. | Inside on R and S. Kind undetermined, because reconsidering a prompt need not revise how later prompts are judged. Neither an explanation of the prompt nor a measured downstream gain is required for membership. Outside the [theory builder](./theory-builder.md) definition, which requires criticism of what a stated theory says. |
| 7 | An automated builder criticizes what a retained theory says but must select the highest-scoring revision. | Inside on R and S, single-loop. Correction (additional description) depends on what the score takes in. **7a:** the score is a fixed test that takes in nothing new, so yesterday's winner is displaced only when a candidate scores higher, as in case 9: none. **7b:** the failed prediction enters the score or removes the criticized theory from the candidates, as in case 10: targeted. |
| 8 | As in case 7, but the same loop can reject the score winner for a stated reason about future work and can later correct that judgment. | Inside, with evaluation across several measures. A standing exception already allowed by the criterion can defeat this score winner without changing the criterion. Double-loop only if the system can revise what counts for later theory choices; the stipulation leaves that open. |
| 9 | A search keeps the highest-scoring prompt variant on a fixed benchmark. A new variant replaces the kept one only by scoring higher on that same benchmark. | Inside on R and S, single-loop. Correction (additional description): none. The earlier choice is overwritten, never found wrong. |
| 10 | As in case 9, but kept variants are scored again on tasks that arrive later, and a variant is dropped when its score on them falls below the threshold. | Inside, single-loop: the later score controls whether the variant is kept. Correction (additional description): targeted. Nothing in the loop can ask whether the score is the right one. |
| 11 | A problem solver stores a new rule for every subgoal it solves and never removes one. | Outside: automatic storage. Nothing evaluates a rule and nothing can be rejected. |
| 18 | A nightly job keeps a readable table that ranks help articles for a search box. It raises an article's rank when users click it and lowers it when clicks fall off. Nothing in the job can change the rule. | Outside. The rule updates the table directly from its input. Nothing is proposed and nothing can be rejected. The definition names this job as a direct update. |
| 19 | A code-review bot keeps a readable list of rules. It adds a rule when the same class of bug has been reported five times. It never changes a rule, and when two rules conflict the older one wins. | Outside as described: the definition's trigger case. Five reports say when to write a rule. Nothing evaluates the rule that is written. Inside and single-loop only if a further step evaluates the drafted rule and can reject it. |
| 20 | A wiki receives every page from an external feed automatically. Editors read it while working and delete pages that prove wrong. | Depends on the level. The imports are automatic and outside. The deletions are selected and inside. |
| 21 | A script adds a sender to a blocklist after ten reports about that sender. A moderator removes wrong entries. Compare PRODIGY, as described in [single-loop and double-loop](./single-loop-and-double-loop-learning.md), which admits a learned rule on a positive utility estimate and later drops it when the estimate from use turns negative. | Blocklist additions: outside. The reports both nominate the entry and decide it, so the evidence determines the change and nothing is proposed apart from it. The count is a trigger. Removals: inside. PRODIGY's rules: inside for admission and for dropping, single-loop. Explanation-based learning proposes a rule, and a separate utility measurement decides whether it enters or stays. Dropping it is a rejection distinct from producing the next rule. This matches case 10 and the PRODIGY entry in the single-loop and double-loop definition. **Settled 2026-11-22:** the case was open between the trigger entry and the fixed-measure entry. |
| 22 | An agent decides, in one act, that an observation is worth recording and records it. | Inside, if the act could have ended in not recording. Evaluation need not be a separate stage. Whether this agent ever does decline is a question of evidence, as in case 23. **Settled 2026-11-22:** the definition replaced "a separate step" with the causal wording. |
| 23 | A coding agent's checking prompt can reject a proposed lesson and has never done so. | Inside on S. The definition requires that a change can be rejected, not that one has been. Whether the prompt can in fact reject is a question of evidence about the system, not of the definition. **Settled 2026-11-22:** the case was open. |
| 24 | A team discusses a proposal to change how it hands work over, agrees, and works that way from then on. Nothing is written down. | Inside on R and S. The agreed practice is retained in the members' habits and their later work follows it. Kind undetermined. Showing an episode is harder without a record, which is a matter of evidence, not membership. |
| 25 | A search trains several candidate checkpoints and deploys the one with the highest score on a fixed validation set. The system's later work runs on the deployed checkpoint. | Inside on R and S for checkpoint choices, single-loop. The gradient steps inside each training run are outside. On the definition's ladder, the model alone learns by selection, the model with the selection script is self-improving, and adding engineers who can change the score makes it double-loop. |

Case 6 shows a selection-based learner that is not a theory builder. No case
here shows a theory builder that is not a selection-based learner. The cases do
not decide how the two definitions relate.

## Case 12: keeping a current decision

[Rao and Georgeff (1995)](../../sources/bdi-agents-from-theory-to-practice.ingest.md)
describe the OASIS arrival sequencer, which chooses a landing schedule using
a cost function. A change in wind need not reopen that choice: the sequencer
can keep the schedule while the next aircraft can still meet its assigned
time. The feasibility check can overturn a particular commitment. The
question for the definition is what changes as a result.

- **Level: the current schedule.** The schedule is kept for later work, a
  feasibility check evaluates it, and the check can reject it. The quoted
  condition alone would admit ordinary replanning. It is excluded because the
  definition calls both selection and direct update learning in
  [Simon's sense](../learning-is-not-only-about-generality.md): a more or
  less permanent change in capacity. Keeping one schedule is not such a
  change.
- **Level: the scheduling procedures.** The reported feasibility check
  decides whether to keep this schedule, not whether to retain or reject a
  procedure for later scheduling. The paper does not show S at this level.

**Expected placement:** outside at both levels. The described episode shows
commitment management, not learning a scheduling procedure. This is not a
claim that no BDI architecture learns. The placement would change if the
sequencer retained a revised feasibility rule because of what happened, and
applied it to a later scheduling decision.

## Cases 13–16: the Gödel-machine line

| # | System, store and decision | Expected result and discriminator |
|---|---|---|
| 13 | **[Darwin Gödel Machine](../../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md).** Every compiling agent stays in the archive. A benchmark score measured once at admission weights parent selection. | Agents: inside on R and S. Later agents are built from archived agents, and admission rejects an agent that does not compile or can no longer edit code. That viability test is the one measure. The benchmark score does not decide admission; it only weights which parent is expanded next. Correction (additional description): none. No evidence from after admission updates an agent's own score. |
| 14 | **[Huxley-Gödel Machine](../../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md).** An admitted agent's selection weight drops when its descendants perform poorly. | Parent-selection weights: outside. Descendant outcomes update an ancestor's weight directly, and every agent stays eligible, so no alternative is dropped. Agents: inside if admission can reject an agent, as the word "admitted" implies; the ingest read for this check does not state the test. Correction (additional description): targeted, since evidence from after admission lowers how often the ancestor is chosen. **Flipped 2026-11-22:** the earlier placement was inside, single-loop, for parent selection; the definition now treats each update a weight receives from evidence as a direct update. |
| 15 | **Classical [Gödel machine](../goedel-machines-are-a-proof-governed-case-of-self-modification.md).** It stores readable code, takes live observations into its proofs, and rewrites any part of itself on proving higher expected utility. | Inside, self-improving, **double-loop capable**. Its later operation runs the rewritten code (R), and proof decides the switch (S). §6.1 item 4 permits revision of the utility function and target theorem under the old standard. A successor that ranks later alternatives differently changes the criterion. No observed rewrite is required to establish the capacity. |
| 16 | **Schmidhuber's [incremental self-improvement](../../sources/on-learning-how-to-learn-learning-strategies.ingest.md).** It keeps modifications to a probability distribution over actions only while payoff per time since the modification exceeds the prior baseline. Otherwise it pops the stack and restores the earlier state. | Inside on R and S, single-loop. Self-modification programs propose the changes, and the payoff-rate test is one fixed measure that can reject them. Popping the stack is a rejection distinct from producing the next modification. Correction (additional description): bundle. **Caveat:** this placement rests on the ingest summary, not on a reading of the paper. **Flipped 2026-11-21:** the earlier placement was outside, because the probability distribution is opaque. |

## Case 17: EURISKO changes how it judges generalizations

**Inside, double-loop for deciding which generalizations of heuristics to
keep.** In [Lenat's H12′ episode](../../sources/eurisko-learns-new-heuristics-and-domain-concepts.ingest.md#quotes)
(*Heuretics*, pp. 89–90), replacing AND with OR made a heuristic fire its
preliminary relevance check more often without finding more occasions when
it was useful. Dropping H12′ on that evidence rejected one readable
heuristic (R and S). That alone would be single-loop.

EURISKO also generated restrictions that would have kept H12′ from
surviving. It tried several and retained one against replacing AND with OR
in a heuristic's If slot. The difference is what happens to the next
generalization: its form now counts against it before its own performance
record is available. Lenat attributes this step to EURISKO, not to a
programmer. The episode shows a change in this working criterion, not a
rewrite of EURISKO's overall worth function or proof of improved
performance.

## Paired checks for double-loop

Each row is a hypothetical, not a reported run.

| Same starting system | Applies the criterion | Revises the criterion |
|---|---|---|
| Gödel machine evaluating self-rewrites | Proves the same target theorems faster. | Proves it should install a utility function that ranks later alternatives differently. Both switches need proof under the old standard. The old function licenses a successor only when the successor serves it better, so a stand-in is replaced while the objective it serves stays fixed. |
| Commonplace judging instruction edits | Rejects a long edit under its brevity rule. | Finds that short instructions repeatedly omit necessary exceptions and changes the rule for later edits. A language model explaining the failures without authority to change the rule is not enough. |
| Learner with a cheap gate and a fixed objective | Drops a routing rule because its queue-time score falls. | Replaces queue time as the test for later routing rules because short queues can still miss deadlines. The objective need not change. |

## Open cases

No case is open now. A case the definition cannot place goes here, and a
change that settles it moves it to the table above.

One wording point is open:

- **What improvement means.** The definition answers whether a selected
  change improved the system "by comparing the system with and without it".
  That comparison does not say what "the system" means while changes keep
  arriving, how a change that was already reverted is assessed, or what
  evidence can stand in for a version of the system that is never run.
