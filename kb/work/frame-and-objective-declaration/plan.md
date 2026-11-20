# Plan

Revised 2026-11-20 after the operator's direction on marginal measurement. The
earlier plan was built around one ruling on the objective's accounting (D4) and
a cold-reader check. The direction replaced that ruling, so the plan is
rebuilt around what the operator settled.

Revised again the same day, after the operator read the finished theory note.
The note does more than the plan assumed. The plan relinked the notes that
state Commonplace's objective. The note also bears on theory notes that stop
at a missing ordering, and it removes the measure the bootstrap article used. Step 5 is new, the cold-reader check is now step 6, and the bootstrap
article is no longer left for the operator. Step 5 was then narrowed after a
comment from Astra; the step records why.

## Basis

Consider adding one line to `AGENTS.md` that sends an agent to the right instructions for a task it would otherwise mishandle. Other prompts load that line too. On a task already near the limit of what the agent can use effectively, one extra line could tip a correct answer into failure. The cost on that task is failure and rework, not just the extra text. That is a possible loss, not an observed failure. How often are important tasks that close to the limit? If we cannot tell and the answer could reverse the decision, the routing gain alone does not settle it.

Four points, recorded with their history in [the settlement record](./settlement.md#operator-direction-2026-11-20):

1. Progress is measured on the margin, in a declared application area.
2. The objective says what a preference between versions is about. We can
   defend some comparisons without ranking every pair or assuming that a
   single stable overall ranking exists.
3. The claim is that the change is better on balance. The operator and users
   weigh the observed gain against losses elsewhere, considering both how
   likely each loss is and how much it would matter. No numerical estimate is required.
4. Name how a loss could arise, who would bear it, and under what conditions
   it would matter. Give the judgment for current conditions, or say what is
   unknown. An unknown leaves the overall judgment open only when a plausible
   answer to it would reverse the decision. Otherwise record the unknown and
   let the judgment stand. A larger table or a change in the task mix can
   warrant another look.

Without the limit in point 4, the rule would block every change: any addition
to text loaded on every prompt could tip some task that is near its limit.

The routing example also has a part that is shared. How often important tasks
sit near the limit is a question about `AGENTS.md` as a whole, not about the
new line. Evidence about which tasks run near their limit can inform more than
one routing decision.

## Step 1 — test the claim form on three real changes

Before anything is written into the library, check that the form produces
claims someone can judge. Apply it to three past Commonplace changes of
different kinds:

- the tag-readme change of ADR 026, where a symbolic check was added;
- one addition of routing to `AGENTS.md`, the operator's own example;
- one added or tightened review gate.

For each, name the area and prior state. Ask what changed for the task, if
anything, and what the evidence shows. Then give the regression argument. Record where the form was awkward or a part could not be filled.

[Worked cases](./worked-cases.md) complete: one observed gain, one untested
benefit, and one catch the predecessor already made. Carry that distinction
into step 2. If a part cannot be filled in two of three cases,
check why before step 2. Revise a question that does not fit the changes.
Missing evidence is a different result: record “local gain shown; overall
judgment open” when the evidence supports only that conclusion.

## Steps 2–4 — one declaration, linked by its consumers

[On-balance judgments can guide improvement without a global measure](../../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md) holds the general argument and the practical choice Commonplace makes. The [factory note](../../theory/a-better-factory-claim-compares-operative-states.md) keeps the narrower comparison under predeclared requirements. Other notes link to the relevant argument rather than repeating the declaration.

The instrument note, the frame note and the two proposals now link to that declaration. The instrument note asks for a comparison in a named area. The proposals keep their local design choices. These edits are committed; the next check is whether a reader can use the instrument note and its links without the workshop discussion.

## Step 5 — two clarifications in theory notes

Revised after a comment from Astra, relayed by the operator on 2026-11-20. The
first version of this step proposed four edits on the premise that the theory
note answers every passage that stops at a missing ordering. That premise was
wrong. Two conclusions are different:

- we cannot establish which version is better on this measure;
- we have no grounds for choosing what to do.

The theory note addresses the second. It does not overturn the first. Its own
ADR 085 example shows this: Commonplace chose deletion without claiming that
deletion beat archiving in a comparison nobody ran. So a passage that says a
comparison has no answer is usually correct as written. It needs an edit only
where a reader could infer that no reasoned choice is possible, or that
declaring an objective settles the trade.

Two edits remain:

- **[Increasing computational autonomy relocates human effort](../../theory/increasing-computational-autonomy-relocates-human-effort.md), "What to measure instead". Edit.**
  "Incomparable until an objective is declared" can suggest that the
  declaration settles the trade. Sometimes it does. Commonplace's objective
  does not: when quality rises and human effort rises too, the objective says
  what to weigh, not whether the gain was worth the cost. Say that and link.
- **[Self-improvement is relative to a declared objective](../../theory/self-improvement-is-relative-to-a-declared-objective.md), "What follows". Clarify, do not correct.**
  An objective that is only a viability bound gives no preference between two
  acceptable versions, even for one pair. An operator can still choose, and
  should then name the further consideration that favours one. One sentence
  and a link.

Two proposed edits are dropped:

- **The better-factory note.** The first version said it did not link to the
  theory note. It does, in "Scope", and says where the on-balance judgment
  applies. Its open question asks whether prior capabilities can be specified
  well enough to check non-regression. A reasoned choice outside the checked
  scope does not answer that.
- **The autonomy-measurement note.** Deciding whether to move one function to
  an agent is not a way to measure autonomy across systems or over time. The
  question stays open. Add a link only if a reader could conclude that
  practical transfers must wait for the measure, and never as a measurement
  method.

**The tag.** The theory note is tagged `evaluation` only. Read the
[self-improving-systems head's](../../tags/self-improving-systems-README.md)
inclusion condition. If the note meets it, add the tag and list the note under
"Definition and objective".

**The two proposals.** Keep a proposal's own metrics where they serve its
experiment. Consolidate only where the shared note changes what a reader can
infer. No body edit is planned.

## Step 6 — one cold-reader check, after the edits

A fresh reader who did not draft the instrument note or plan receives only the
revised instrument note and the two questions below. They may follow its
links. Withhold the workshop discussion and scoring criteria. Ask: "What does this note claim
the tag-readme trace shows about Commonplace?" and "The maintainer must choose
whether to keep this change. What can they reasonably decide now, and what can
they still not claim?" Score the first for overclaims. Score the second for the
distinction, not the terminology: the reader separates a decision the
maintainer can defend from a comparison that has not been made. A reader who
only repeats "better on balance" has not passed. Record it in `cold-reader-check.md`. If the reader misses the second point, check whether the link was missed or the linked argument was unclear before revising either.

## Left for the operator, not planned here

- **Three open points in the bootstrap article.** On the operator's
  instruction the article was revised in `a0818af2e`. It now judges progress by
  the kinds of improvement that complete with the operator's decisions
  withheld, and keeps the decision count within one kind of change. Left open:
  - The failure condition has no period. Until one is set, "the kinds that
    pass stop growing" cannot fail.
  - "Kind of improvement" is not defined. A coarse cut hides transfers and a
    fine cut makes growth trivial. The autonomy-measurement note has the same
    grain problem.
  - The worked example, a stale cross-reference repair, is hypothetical. A
    recorded transfer should replace it if one fits.
- **The frame note's person-based boundary.** The software-house investigation
  found that the frame note places people by designation while the
  theory-builder and software-house definitions place them by role. No
  position has argued it. It needs a decision on whether it belongs in this
  workshop.
- **A review or writing rule (D8).** None is planned. Revisit only if the
  claim form is used and misused.

## Close

Mark D4 reframed by the operator's direction, D1 and D3 moot, D2, D6 and D8
resolved as "no addition". Record the single owner of the objective and the frame note’s narrower scope under D5 + D7. Validate changed files with `commonplace-validate`. Delete the
directory and remove its entry from `kb/work/README.md`.

The software-house investigation is not extracted by this plan. Its
conjectures are untested. On closing, either move it to its own workshop or
record its two established findings in `kb/log.md`.

## Commits

Done: the theory note (`590a322b2`, revised in `53190e860`), the instrument,
frame and proposal links (`5a42c2e46`), the bootstrap article (`a0818af2e`).
Remaining: one for the step 5 edits, one for the cold-reader record, one for
closure. Each carries `Workshop: kb/work/frame-and-objective-declaration`.
