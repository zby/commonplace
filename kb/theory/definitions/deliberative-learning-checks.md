# Checks for the deliberative-learning definition

Maintenance material for [deliberative learning](./deliberative-learning.md).
Apply the checks when changing that definition, including cross-references
that change its meaning. Report affected cases before revising their expected
placements. Keep case numbers stable and make changes to assumptions
explicit.

These cases check selected boundaries. Unchanged answers do not prove that
the entire scope is unchanged. Report any additional scope difference the
proposed change exposes.

Adopted 2026-11-21 with the definition. Cases 1–20 were placed while the
definition was drafted. Cases 21–23 are open.

## Tests for any change to the definition

1. **Process, not outcome.** No condition may require that a change improved
   the system. "Learned" stays a separate verdict on one change.
2. **Small changes do not leave the definition.** A fixed criterion is the
   special case of condition 2, not an exclusion (operator, 2026-11-21). A
   proposed condition that puts a system outside because its criterion is
   simple, or because it never revisits a change, is a scope decision.
3. **Correction is a property.** Whether later evidence can count against an
   earlier change is reported, not required (operator, 2026-11-21).
4. **Check the named system.** Run the checks on the named system, store,
   class of changes and horizon. Do not credit an automated loop with
   judgments its designers make elsewhere.
5. **A change reports the cases it flips.** Run the proposed wording against
   the cases below. A change that flips none is a wording change. A change
   that flips one is a scope decision for the operator.

## How to read a case

Each case is checked on two conditions, two properties and a kind.

- **S, the store.** What the system retains is held in contents that can be
  read and pointed at, the system learns by changing them, and its later
  work consumes them.
- **J, the decision.** A change of the named class is proposed, judged in
  the loop on the evidence the system has, and can be rejected. A judgment
  that applies one fixed criterion counts. A rule that updates the store
  directly from an input does not, and neither does a trigger that says when
  to write without judging what is written.
- **Correction from later evidence.** *Targeted* when later evidence can
  identify the responsible change, *bundle* when it can only reverse
  everything since a baseline, otherwise *none*.
- **Displacement.** A newer alternative can replace an earlier change by
  scoring higher on the same criterion.
- **Kind.** Double-loop when the named system can revise the criterion that
  governs later decisions of the class. A different verdict under the same
  criterion is not a different criterion. Where a case does not specify the
  capacity, the kind is undetermined.

Membership requires S and J. No case assumes improved capacity unless it
specifies the comparison.

## Stipulated cases

| # | System, store and decision | Expected result and discriminator |
|---|---|---|
| 1 | A team keeps a routing rule after weighing saved searches against misrouting. Later failures can lead it to revise the rule. | Inside: S and J. Correction: targeted. Kind undetermined. Revised weights on saved searches against misrouting for later cases would show criterion revision; correcting this one rule does not. If later work is worse, the team made a bad judgment about the rule. It did not cease to use the process. Human judgment counts, and is not autonomous. |
| 2 | A service appends every interaction to a searchable log. A later tool can edit the log, but no judgment selects which entries to keep. | Outside: nothing judges, so S alone does not give J. Keeping everything is not a fixed criterion, because no judgment depends on the entry. The decision to introduce the logging is a different change: a system that makes and can revisit that decision is inside with respect to the logging rule, not the entries. |
| 3 | The team in case 1 still weighs the reasons, but no later round can challenge its decision or act differently in response to an error. | Inside on S and J. Correction: none. A team can deliberate over every new entry under a rule that gives earlier entries permanent precedence. |
| 4 | A link repairer keeps a patch exactly when its fixed validator passes. Separately, the maintaining team reviews where that test suffices, changes the validator after bad repairs, and weighs ambiguous repairs itself. | Repairer alone: inside on S and J, since the validator is a fixed criterion; single-loop; correction: none, because as stipulated evidence against a kept patch reaches only the team. S holds only if later repair runs consume the repaired documents. If the documents are only its output, the repairer has no store of its own. Team plus repairer, for repairs: inside, double-loop, because the team changes the validator; correction: targeted. |
| 5 | A team judges whether to deploy a better model release, but the training run retains only numeric weight updates under a fixed loss. | Training run and its weights: outside on S. The fixed loss would pass J. The deployment verdict is not the step that made a weight update. To classify the team, specify its own store and loop. |
| 6 | A team keeps an unexplained prompt variant after weighing mixed outcomes and revisits the choice on new evidence. By stipulation it never formulates or criticizes a claim about why the prompt works. | Inside on S and J, with targeted correction. Kind undetermined, because reconsidering a prompt need not revise how later prompts are judged. Neither an explanation of the prompt nor a measured downstream gain is required for membership. Outside the [theory builder](./theory-builder.md) definition, which requires criticism of what a stated theory says. |
| 7 | An automated builder criticizes what a retained theory says but must select the highest-scoring revision. | Inside on S and J, single-loop. Its correction depends on what the score takes in. **7a:** the score is a fixed test that takes in nothing new, so yesterday's winner is displaced only when a candidate scores higher, as in case 9. Correction: none. Displacement: yes. **7b:** the failed prediction enters the score or removes the criticized theory from the candidates, so the kept theory can lose on evidence against it, as in case 10. Correction: targeted. |
| 8 | As in case 7, but the same loop can reject the score winner for a stated reason about future work and can later correct that judgment. | Inside. A standing exception already allowed by the criterion can defeat this score winner without changing the criterion. Double-loop only if the system can revise what counts for later theory choices; the stipulation leaves that open. |
| 9 | A search keeps the highest-scoring prompt variant on a fixed benchmark. A new variant replaces the kept one only by scoring higher on that same benchmark. | Inside on S and J, single-loop. Correction: none. Displacement: yes. The earlier choice is overwritten, never found wrong: no later evidence bears on the kept variant. |
| 10 | As in case 9, but kept variants are scored again on tasks that arrive later, and a variant is dropped when its score on them falls below the threshold. | Inside, single-loop. Correction: targeted, because later evidence counts against a particular kept variant. Nothing in the loop can ask whether the score is the right one. |
| 11 | A problem solver stores a new rule for every subgoal it solves and never removes one. | Outside: no judgment decides what is added. |
| 18 | A nightly job keeps a readable table that ranks help articles for a search box. It raises an article's rank when users click it and lowers it when clicks fall off. Nothing in the job can change the rule. | Outside on J. The rule updates the table directly from its input. No change is proposed and none can be rejected. The table is legible, so S passes. This is learning by direct update, as a readable table of values in reinforcement learning is. |
| 19 | A code-review bot keeps a readable list of rules. It adds a rule when the same class of bug has been reported five times. It never changes a rule, and when two rules conflict the older one wins. | Outside as described. Five reports say when to write a rule. Nothing judges the rule that is written. Inside, single-loop and with no correction, only if a further step judges the drafted rule and can reject it. |
| 20 | A wiki receives every page from an external feed automatically. Editors read it while working and delete pages that prove wrong. | Depends on the named class. The imports are not made by a decision and are outside. The deletions are, and are inside for that class. |

Case 6 shows a deliberative learner that is not a theory builder. No case
here shows a theory builder that is not a deliberative learner. The cases do
not decide how the two definitions relate.

## Case 12: keeping a current decision

[Rao and Georgeff (1995)](../../sources/bdi-agents-from-theory-to-practice.ingest.md)
describe the OASIS arrival sequencer, which chooses a landing schedule using
a cost function. A change in wind need not reopen that choice: the sequencer
can keep the schedule while the next aircraft can still meet its assigned
time. The feasibility check can overturn a particular commitment. The
question for the definition is what changes as a result.

- **Name the current schedule as the store.** There is a decision to inspect
  (S), a test for keeping it (J), and later evidence that can defeat it.
  Without a declared horizon, the conditions could count ordinary replanning
  as single-loop learning.
- **Name the scheduling procedures as the store.** The plans are legible,
  but the reported feasibility check decides whether to keep this schedule,
  not whether to retain or correct a procedure for later scheduling. The
  paper does not show J for that store in the sequencer's own loop.

**Expected placement:** at a horizon that spans tasks, the described episode
shows commitment management, not learning a scheduling procedure. This is
not a claim that no BDI architecture learns. The placement would change if
the sequencer retained a revised feasibility rule because of what happened,
and applied it to a later scheduling decision.

## Cases 13–16: the Gödel-machine line

| # | System, store and decision | Expected result and discriminator |
|---|---|---|
| 13 | **[Darwin Gödel Machine](../../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md).** Every compiling agent stays in the archive. A benchmark score measured once at admission weights parent selection. | Inside on S (inspectable agent code) and J (admission requires that the agent compiles and can still edit code, and the score sets how often it is selected). Correction: none. Displacement: yes. No evidence from after admission updates an agent's own score. Its sampling weight falls in two ways, and neither is evidence about the agent: higher-scoring agents enter the archive, and its own count of functioning children grows. The count allocates exploration. "This parent has been explored enough" is not "its descendants turned out poorly". |
| 14 | **[Huxley-Gödel Machine](../../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md).** An admitted agent's selection weight drops when its descendants perform poorly. | Inside, single-loop. Correction: targeted, because descendant outcomes supply evidence from after admission that lowers how often the ancestor is selected, even if no other branch improves. The evidence need not come from running the admission test again. Single-loop for parent selection: new descendant scores change the weights assigned to parents, not the rule for assigning weights. |
| 15 | **Classical [Gödel machine](../goedel-machines-are-a-proof-governed-case-of-self-modification.md).** It stores readable code, takes live observations into its proofs, and rewrites any part of itself on proving higher expected utility. | Inside, **double-loop capable**. Readable code passes S and proof decides the switch (J). Later observations can end a trial (§6.1 item 2). §6.1 item 4 permits revision of the utility function and target theorem under the old standard. A successor that ranks later alternatives differently changes the criterion. No observed rewrite is required to establish the capacity. |
| 16 | **Schmidhuber's [incremental self-improvement](../../sources/on-learning-how-to-learn-learning-strategies.ingest.md).** It keeps modifications to a probability distribution over actions only while payoff per time since the modification exceeds the prior baseline. Otherwise it pops the stack and restores the earlier state. | Outside on S (opaque probability distribution). Its correction is of the bundle kind. It shows that evidence from after a change can reverse the change without a challenger, and what an addressable store adds: targeted correction in place of stack rollback. |

## Case 17: EURISKO changes how it judges generalizations

**Inside, double-loop for deciding which generalizations of heuristics to
keep.** In [Lenat's H12′ episode](../../sources/eurisko-learns-new-heuristics-and-domain-concepts.ingest.md#quotes)
(*Heuretics*, pp. 89–90), replacing AND with OR made a heuristic fire its
preliminary relevance check more often without finding more occasions when
it was useful. Dropping H12′ on that evidence reversed the addition of one
readable heuristic (S, J, targeted correction). That alone would be
single-loop.

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

The definition does not yet place these. A change that settles one should
say so and move it to the table above.

| # | Case | What is open |
|---|---|---|
| 21 | A script adds a sender to a blocklist after ten reports about that sender. A moderator removes wrong entries. | The removals are inside. For the additions, the count is evidence about the item itself, so the case fits both the trigger entry and the fixed-criterion entry. PRODIGY dropping a rule when its utility estimate turns negative has the same structure. |
| 22 | An agent decides, in one act, that an observation is worth recording and records it. | Whether "separate steps" requires separate actors or only separate functions. The definition treats this case as inside. |
| 23 | A coding agent's checking prompt can reject a proposed lesson and has never done so. | Inside by the letter. Whether a capacity to reject that practice never shows is enough. |
