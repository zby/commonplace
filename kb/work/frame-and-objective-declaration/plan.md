# Plan

Revised 2026-11-20 after the operator's direction on marginal measurement. The
earlier plan was built around one ruling on the objective's accounting (D4) and
a cold-reader check. The direction replaced that ruling, so the plan is
rebuilt around what the operator settled.

Revised again the same day, after the operator read the finished theory note.
The note does more than the plan assumed. The plan relinked the notes that
state Commonplace's objective. The note also answers theory notes that stop at
"no ordering, so no answer", and it removes the measure the bootstrap article
used. Step 5 is new, the cold-reader check is now step 6, and the bootstrap
article is no longer left for the operator.

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
new line. Investigating it once serves every later routing change. A single
task fails abruptly, but across many tasks the expected loss is roughly the
share of important tasks near the limit times the size of the addition.

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

The instrument note, the frame note and the two proposals now link to that declaration. The instrument note asks for a comparison in a named area. The proposals keep their local design choices. These edits are in the working tree; the next check is whether a reader can use the instrument note and its links without the workshop discussion.

## Step 5 — carry the note into the theory notes it answers

Several theory notes reason that a comparison needs an ordering, find that the
objective supplies only a partial one, and stop there. The theory note changes
the question from ranking versions to choosing between two. Each note below
still stops at the old point and does not link to the theory note. Checked on
2026-11-20.

- **[Increasing computational autonomy relocates human effort](../../theory/increasing-computational-autonomy-relocates-human-effort.md), "What to measure instead".**
  It says a change that trades outcome quality against effort "is incomparable
  until an objective is declared". Commonplace has declared one and the trade
  still needs a judgment. Say that the order settles the cases where nothing is
  traded, and that an on-balance judgment decides the rest.
- **[Self-improvement is relative to a declared objective](../../theory/self-improvement-is-relative-to-a-declared-objective.md), "What follows".**
  "A fully indexed comparison can still have no answer" is true of ranking.
  Add that a choice between two versions can still be made, and link.
- **[A better-factory claim compares operative states](../../theory/a-better-factory-claim-compares-operative-states.md).**
  It lists non-regression on an open-ended family as an open question. The
  theory note answers it: outside the predeclared requirements, regression is
  judged on balance, not checked. Replace the question with that answer.
- **[Measuring autonomy well enough to see it improve is an open problem](../../theory/measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md).**
  Its second open question asks whether to adopt a rough proxy that lacks a
  principled basis. Add the third option: decide a transfer without the
  measure. The title's claim stands; measuring is still open.
- **[The self-improving-systems head](../../tags/self-improving-systems-README.md).**
  The theory note is tagged `evaluation` only. Read the head's inclusion
  condition. If the note meets it, add the tag and list the note under
  "Definition and objective".

Keep each edit to the passage named. If a note's argument depends on the old
framing in more places, record that here and stop; that note then needs its own
revision, outside this workshop.

**The two proposals.** Their openings link to the theory note. Their bodies
still treat the objective as measured, for example "the measure must be per
unit of human judgment, not per task" in the reusable-commitment proposal.
Rewording those passages changes what the proposals commit to test, so the
operator decides whether it happens here.

## Step 6 — one cold-reader check, after the edits

An agent other than position B's author reads the revised instrument note with
no workshop context and answers two open questions: "What does this note claim
the tag-readme trace shows about Commonplace?" and "How would you tell whether
Commonplace had improved?" Score the first for overclaims and the second
for the reasoning, not the terminology: can the reader identify the local
comparison and explain what would justify or withhold an overall judgment? Record it in `cold-reader-check.md`. If the reader misses the second point, check whether the link was missed or the linked argument was unclear before revising either.

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
- **Where Commonplace's objective lives.** It is now a section of a theory
  note, and four reference notes link to its anchor. That settles D5 + D7 by
  placement. Confirm it, or move the declaration to a reference note.
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
