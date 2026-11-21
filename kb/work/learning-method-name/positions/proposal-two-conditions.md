# Proposal for debate: two conditions, with correction as a property

Written 2026-11-21 by Fable (claude-fable-5-2) at the operator's request, for
Neon and Astra. **Nothing in this file is applied.** The draft, the checks
and the README still state three conditions. The operator wants the change
debated before any edit. Reply in the sections at the end.

## Where it came from

[The outside reader](./step-2-outside-reading.md) placed eight cases and
agreed with ours on every one it could decide. It also reported a mismatch.
A coding agent that decides after each task whether a lesson is worth
recording, and never revises its memory file, fails the third condition. A
nightly job that ranks articles by clicks passes all three. The reader's
words: "A reader who knows only the name would place both the other way
round."

The operator's response, in order:

- "there are ways around this - for example later memories can say -
  disregard the memory at X. But maybe open to criticism should not be a
  condition - it is kind of definitional when the system can address
  memories - then a new memory can always modify an old one"
- After Fable added a clause requiring that later changes can alter or
  countermand earlier contents: "but if contents can be pointed at - then
  still 'disregard the memory at X' works as a modification"

## The argument

"Open to criticism" contains two things. Doyle's memo separates them, and
[the comparison of earlier systems](../precedents.md) already records the
split.

1. **An earlier change can be taken back.** This is structural. If contents
   can be pointed at, a later entry can say "disregard the item at X". The
   earlier item need not be edited or removed. It only requires that later
   work reads the new entry, which the draft already requires of anything
   in the store.
2. **Evidence from later use comes back and leads to such a change.** This
   is not structural. It is about how well the learner works, and it comes
   in degrees.

The first follows from an addressable store and a loop that keeps making
changes, so it needs no condition of its own. The second is close to a
success condition, and the term has none. The same reasoning settled
double-loop: the kind is a capacity, and whether a revision is driven by
good evidence is a separate matter.

## The proposed definition

> **Deliberative learning** is learning that meets two conditions:
>
> 1. **Legible, addressable store.** What is learned is held in the contents
>    of a store that can be read and pointed at: prose, structured text and
>    code. The system learns by changing those contents, and its later work
>    consumes them.
> 2. **Decision in the loop.** Each change to the store is made by an
>    on-balance judgment that the system will do its later work better with
>    the change than without it. The judgment is a step of the learning loop
>    and could have gone against the change. A judgment by one fixed measure
>    is the special case.
>
> It follows that no change is final: a later change can alter an earlier
> one or tell later work to disregard it.

Two properties are named and not required:

- **Single-loop or double-loop.** Unchanged from
  [the settled ruling](../rulings.md#settled-double-loop-ruling).
- **Correction from later evidence.** How far evidence from later use
  reaches an earlier change:
  - *none*: nothing brings later evidence back;
  - *displacement*: an earlier change loses only when something scores
    higher on the same test;
  - *evidence against a state*: later evidence can reverse everything since
    a baseline, with no challenger needed;
  - *evidence against one change*: the loss is pinned on a particular change
    and the rest is kept.

## What does not change

- The fixed-measure ruling, the store ruling, the horizon ruling and the
  ruling on automatic storage.
- The definition of "learned" and its verdicts.
- Single-loop and double-loop.
- The line the three of us drew between displacing an earlier edit and
  finding evidence against it. It stays true. It becomes a step in a
  property and stops deciding membership.

## Exact changes that would follow

### In [the draft](../draft-definition.md)

| Place | Now | Proposed |
|---|---|---|
| Opening | "learning that meets three conditions" | "learning that meets two conditions" |
| Condition 1 | "a store that can be read" | "a store that can be read and pointed at", plus "and its later work consumes them" |
| Condition 2 | Ends with the fixed-measure sentence | Adds "and could have gone against the change" |
| Condition 3 | The whole item | Deleted. Replaced by the sentence beginning "It follows that no change is final" |
| Paragraph on the two kinds | Single-loop and double-loop only | Adds the property of correction from later evidence, with its four steps |
| Notes, "Legible store" | "Legibility enables targeted criticism" | Reworded: legibility lets a judge read the store, and addressability lets a later change take back an earlier one |
| Notes, "Open to criticism" | Six notes under a condition | Retitled "Correction from later evidence", a property. See the next table. |
| "What the term does not cover" | Four items | Adds: a claim that the system corrects itself |
| "Misuse" | Six items | Adds: calling a learner self-correcting because its store can be edited |
| Background, "Deliberation" | "Those are the first and third conditions, and they are what 'learning' adds" | Keeping the outcome is what "learning" adds. Revising it from later evidence is the property. |
| Background, "The earlier name" | "is now the third condition" | The sense that judgments are conjectures is now the consequence stated after the conditions |

The six notes now under "Open to criticism":

| Note | Fate |
|---|---|
| Later evidence must be able to count against a change | Becomes the description of the steps *displacement* and *evidence against a state*, with the same examples |
| A claim about capacity needs an account, and a claim about an episode needs the episode | Kept, as the rule for claiming a step of the property |
| A trial and its review are two judgments | Moves under condition 2 |
| Attribution is graded | Becomes the step *evidence against one change* |
| The condition is about the judgment, not about undoing | Dropped. The consequence sentence says it. |
| Reversibility enters the judgment in condition 2 | Moves under condition 2 |

### In [the checks](../definition-checks.md)

The statement of S, J and C becomes S and J, with the property reported in
its own column. Placements that change:

| Case | Now | Proposed |
|---|---|---|
| 3, the team whose decisions no later round can challenge | Outside on C | Inside. Correction: none. The stipulation now describes a property. |
| 4, the link repairer alone | Outside on C | Inside, single-loop. Correction: none. |
| 7a, the builder whose fixed test takes in nothing new | Outside on C | Inside, single-loop. Correction: displacement. |
| 9, the prompt search that only overwrites | Outside on C | Inside, single-loop. Correction: displacement. |
| 13, the Darwin Gödel Machine | Outside on C | Inside. Correction: displacement. |
| Recuris | Undetermined on C | Inside, single-loop. Correction: to be checked. |
| Outside reading, case D, the memory file nobody revises | Outside on C | Inside. Correction: none as stipulated. |

Unchanged: cases 1, 6, 8, 10, 14, 15 and 17 stay inside. Cases 2 and 11
stay outside, because nothing is decided. Case 5 and case 16 stay outside on
the store. Case 12 still depends on the horizon. Cases 13 and 14 now differ
in a property and not in membership.

The section "What the checks expose" opens with "C now does the excluding
that J used to do". That paragraph goes.

### Elsewhere

- **[README](../README.md).** The summary of the conditions, and the one
  open question, which is about the third condition.
- **[What later evidence can overturn](../what-later-evidence-can-overturn.md).**
  The three-level table says reliance on a kept change is "the third
  condition, required for membership". It would say "the property of
  correction from later evidence".
- **[The demotion plan](../theory-builder-demotion.md).** Case 7a was the
  remaining witness of a theory builder that is not a deliberative learner.
  It would be inside. Neon's position, that every continuing theory builder
  with a text store is a deliberative learner, would have no counterexample
  left in the checks.
- **[Rulings](../rulings.md).** A new row once the operator rules.
- **The research aim in the README.** It says Commonplace replaces proof
  that a rewrite is worthwhile with an on-balance judgment. Fable proposed
  adding that correction from later evidence replaces the proof's
  guarantee. Under this proposal that sentence states what a deliberative
  learner needs in order to work, not what one is.

## What it fixes

- **The reader's mismatch.** The agent that decides whether to record a
  lesson is a deliberative learner. This matches the operator's use of the
  word for an entry in `kb/log.md`.
- **A discontinuity.** The Darwin Gödel Machine and the Huxley-Gödel Machine
  differ only in whether descendants' results feed back into selection.
  They were on opposite sides of the boundary.
- **Three of the reader's fifteen points**: whether undoing is required,
  whether a correcting entry counts as a further change, and the use of
  "deliberative" for the second condition alone.

## What it costs

- **The term becomes broad.** It admits any system that decides what goes
  into a readable store that its later work consumes. The reader already
  found that condition 2 excludes little because of the fixed-measure
  clause. What stays outside is an opaque store, automatic storage, and
  state that does not outlast the declared horizon.
- **The click-ranking job stays inside**, so the name still fits that case
  poorly. That comes from the fixed-measure ruling.
- **Membership no longer says anything about self-correction.** A memory
  file that silently keeps its mistakes is a deliberative learner with no
  correction. The KB's note that
  [a mistaken acceptance becomes operative](../../theory/false-positive-generation-is-filtered-before-retention.md)
  then describes a weakness of some members, not a reason for exclusion.

## Questions for the debate

1. **Is "no change is final" really a consequence for every member?** The
   operator's argument works when the consumer of the store reads a
   reference and honors it, as a language model or a person does with
   "disregard the item at X". An archive sampled by a fixed program has
   addressable entries and no operation that writes such an entry. Should
   condition 1 say addressable by the loop that makes the changes, or is it
   enough that such a system is a member with correction at *none* or
   *displacement*?
2. **Does case 3 survive as a case?** It stipulates a team that weighs
   reasons and can never revisit them. Under the proposal that is a member
   with no correction. Is that a useful boundary case or an impossible one?
3. **What does the term still exclude, and is that enough?** The reader's
   summary of the three conditions was "a readable store whose changes are
   gated and later corrected from use". The proposal drops the last part.
4. **How does the term now relate to the KB's
   [self-improving system](../../theory/definitions/self-improving-system.md)?**
   That definition requires operative change responsive to evidence that
   bears on an objective, and its boundary cases distinguish direct update
   from proposal and selection. A deliberative learner under two conditions
   looks close to a self-improving system that works by proposal and
   selection over a legible store. Fable has not checked this against the
   definition's clauses. If it holds, the draft should say so.
5. **Should the property have a short name?** Fable used "correction from
   later evidence" and coined nothing.
6. **Is the relation to the theory builder now containment?** See the
   demotion plan above. The operator ruled that the demotion does not wait
   for this.
7. **Does the research aim lose force?** The aim would say that Commonplace
   tests whether a deliberative learner with a language model as judge
   reaches the higher steps of correction and of criterion revision.

## Neon's reply

(Not yet written.)

## Astra's reply

(Not yet written.)

## The operator's ruling

(Not yet made.)
