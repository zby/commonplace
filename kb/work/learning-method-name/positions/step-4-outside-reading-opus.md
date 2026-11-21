# Step 4: outside reading of Neon's revision

Reader: a fresh general-purpose agent running Claude Opus, launched by Fable
on 2026-11-21. It read the working copy of the draft after Neon's revision
for flow, which was uncommitted on top of `2d04343d3`, and the on-balance
note. It followed no links, read nothing else in the workshop and did not
use git. The ten cases are the same as in
[the earlier Opus reading](./step-3-outside-reading-opus.md), so a placement
that moved was moved by the text. Fable transcribed and shortened this file.
The reader has not confirmed it. Fable's expected placements were recorded
in the session beforehand.

## What was done with it

On the operator's instruction Fable applied the findings on the definition:
the separation of proposing from judging, with a trigger outside; the
judgment as a decision on an expectation; "retains" in condition 1; the
horizon working through condition 1; and findings 6 to 10. The findings on
the text as writing, including where "learned" is defined, are left for
Neon.

## Placements

| Case | Store | Decision | Deliberative learner? | Kind | Correction | Earlier Opus reading | Fable's expectation |
|---|---|---|---|---|---|---|---|
| A. Team's routing rule | Holds | Holds | Yes | Undetermined | Targeted | Same | Same |
| B1. Link repairer alone | Depends on who reads the documents | Holds, fixed criterion | Only if the documents feed its own later work | Single-loop | None | Depends | Outside. The case does not say who reads the documents, so "depends" is the correct answer. |
| B2. Team with repairer, link repairs | As B1 | Holds | As B1 | Double-loop | Targeted, with a caveat | Yes | Same |
| C. Click-ranking job | Holds | **Fails** | **No** | n/a | n/a | Could not decide | Outside. **Settled by the new text.** |
| D. Support bot, added answers | Holds | Holds | Yes | Undetermined | Targeted | Yes | Same |
| D. Support bot, rewrites after three marks | Holds | Depends: criterion or direct update? | Depends | — | — | Depends | Not made by a decision |
| E1. Fine-tuning run | Fails | Fails | No | n/a | n/a | Same | Same |
| E2. Deploying team, deployment choices | Holds | Holds | Yes | Undetermined | Targeted | Same | Same |
| F. Plan revised within a task | Depends on the horizon | Holds | No across tasks | — | — | Same | Same |
| G. Wiki, imports | Holds | Fails | No | n/a | n/a | Could not decide | Outside. **Settled.** |
| G. Wiki, deletions | Holds | Holds | Yes | Undetermined | None | Could not decide | Inside. **Settled.** |
| H. Code-review bot, rule after five reports | Holds | **Depends**: fixed criterion or direct update? | Depends | Single-loop if inside | None | Yes | Inside. **The reader does not confirm this.** |

The reader notes that most verdicts came from the worked examples and not
from the text of the conditions. The conditions alone would not have decided
C, H or F.

## The findings that bear on the definition

1. **No test separates a direct update from a fixed criterion.** The draft
   gives examples and no rule. "Keeps a rule because a formula scored it
   above zero" is inside. "Raises a rank whenever it is clicked" is outside.
   "Adds a rule whenever a bug class is reported five times" resembles both.
   Cases H and D's rewrites cannot be decided for that reason.
2. **The fixed criterion is not a special case of an on-balance judgment as
   the note defines it.** The note's claim is that every reasonable measure
   scores the successor higher. A validator pass judges no such thing. The
   reader: "It is a different kind of judgment admitted by fiat."
3. **"On-balance judgment" is used for the deciding and for the verdict.**
   Condition 2 uses it for the judgment made when a change is proposed. The
   section on "learned" uses "on balance" for a verdict that is usually open
   for a recent change. So a typical judgment under condition 2 cannot be an
   on-balance verdict.
4. **"Learned" is used in two senses.** Condition 1 says "what is learned is
   held in the contents of a store". Later "learned" is a verdict that
   excludes open changes.
5. **The horizon decides membership and is not a condition.** The plan
   revised within a task meets both conditions and is excluded by the
   horizon.
6. **Correction and double-loop overlap.** The sentence that the system can
   "change the rule that triggered it" counts a revision of the criterion as
   correction.
7. **The link repairer appears in two examples that pull apart.** One says a
   program repairing documents that only outside readers view has no store
   in them. The other uses "link repairs" as the class of changes for a
   double-loop team.
8. **Bundle correction is illustrated with a class that fails condition 1:**
   the edits inside a deployed model.
9. **What revising an open set of considerations means is not said**, so
   every case judged by people comes out with the kind undetermined.
10. **The draft says it follows the on-balance note on the comparison and
    departs from it.** The note compares successor with predecessor. The
    draft compares the present system with one change taken out.

## On "learned"

The reader stated the comparison correctly. It found "taken out" undefined
when later edits build on the change, undescribed for a deletion, and
without a fixed reference time.

## Does the name fit

It fits the team cases and the wiki's deletions. It fits the code-review
bot worst, with the validator gate second. The reader judges this a defect
of the definition: "Either drop fixed criteria from the term and give them
their own name, or accept that the name oversells the special case and say
so in the definition."

## The text as writing

- **Order.** "Learned" is used in the opening and defined near the end. The
  reader would define it straight after the two terms. "What a claim names"
  comes before the reader knows what the store and the judgment involve.
- **Repetition.** The difference between a capacity claim and an episode
  claim is stated three times. That edits to what later work loads or
  selects count is stated four times. The named system and class are
  required twice. The exclusions repeat the examples under the decision.
- **Three passages to cut or rewrite first:**
  1. "A judgment that applies one fixed criterion is the special case." Say
     what it is a special case of and why it qualifies.
  2. The paragraph on a trial and its review. It is guidance for deciding,
     not definition.
  3. The sentence on the Gödel machine under double-loop. It answers an
     objection the reader never saw.
- **Drafting history that remains:** the header, the sentence that admitting
  a single criterion "keeps the definition continuous", and two sentences
  that answer objections the reader never saw.
