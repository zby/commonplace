# Step 5: outside reading of Neon's second revision

Reader: a fresh general-purpose agent running Claude Opus, launched by Fable
on 2026-11-21. It read the working copy of the draft after Neon's second
revision and the on-balance note, and followed one link, to the definition
of behavior-determining organization. It returned after the operator had
decided to adopt the definition. Fable transcribed and shortened this file.
The reader has not confirmed it. Fable's expected placements for the new
cases were recorded in the session beforehand.

## The new cases, which the draft does not discuss

| Case | Reader | Fable's expectation | How the reader got there |
|---|---|---|---|
| I. A blocklist: a script adds a sender after ten reports, and a moderator removes wrong ones | Additions outside. Removals inside. | Same | Additions only by analogy to the five-report bot |
| J. A shop program that trials a proposed category and keeps it above a fixed sales threshold, never reviewed | Inside, single-loop, no correction | Same | From the conditions |
| K. A glossary with a second translator who accepts or rejects, reopened entries and rewritten guidelines | Inside, double-loop, targeted correction | Same | From the conditions |
| L. A chess program that marks a line "avoid" after each loss | Outside | Same | By analogy |
| M. A coding agent whose checking prompt has never said no | Inside by the letter | Expected the draft not to settle it | No sentence addresses a judge that never rejects |
| N. A scientist's notebook and her page of lessons | Notebook outside. Lessons inside, targeted. | Same | From the conditions |

The older cases A to H came out as before. The reader marked seven of them
as discussed or nearly copied in the draft, so they test lookup.

## Findings on the definition

1. **A trigger and a fixed criterion are still not separated when the count
   is evidence about the item itself.** "Ten reports about this sender" fits
   the trigger entry and the fixed-criterion entry. The sentence that a rule
   saying when to write is not a judgment of what is written fails here.
2. **The draft's own examples of correction are automatic writes.** PRODIGY
   dropping a rule when its estimate turns negative, and an archive lowering
   an ancestor's weight, are threshold or score writes that the entries on
   triggers and direct updates would place outside condition 2. The draft
   does not say whether correction must run through a loop that meets
   condition 2.
3. **"Separate steps" is not defined.** The draft's own examples have one
   actor propose and judge in one act: an agent judging that an observation
   is worth recording, and an editor deleting a page. It does not say
   whether the judge must be independent of the proposer.
4. **"Can be rejected" is a capacity that is never tested against
   practice.** The case of the judge that never says no shows it.
5. **"On balance" is still used for a manner of deciding and for the
   verdict.**
6. **A validator has no expectation.** The sentence that the judgment is
   made "in the expectation that later work will go better" does not fit a
   program, and "treating one fixed criterion as settling the matter" does
   not say who treats it so.
7. **The store must be the system's own, yet a nested loop is assessed
   separately.** A repairer alone has no store of its own, and the draft
   also says a validator-gated repairer is assessed on its own system.
8. **The definition of correction and one of its examples differ.**
   Correction changes what the system does about an earlier edit. The
   example of deciding later deletions differently changes later decisions.
9. **What shows a capacity for double-loop is not said**, as it is for
   correction. For a human team the capacity is almost always there in
   principle.
10. **The heading "Automatic storage (outside)" opens with an example that
    is inside.**
11. **The displacement example of an archive with static scores shows no
    replacement.**
12. **"Criterion" is never related to the on-balance note's "measure".**

## On "learned"

The reader stated the comparison correctly. Open points: what "now" means
while edits keep arriving, who decides which later edits depend on a
change, a change that was already reverted, and what evidence can stand in
for a version of the system that is never run.

## Does the name fit

Worst for the shop program with a fixed threshold, with the validator alone
and the judge that never says no close behind. The reader calls it a defect
of fit between the name and the definition: "'Gated' or 'judged' would be
literal. 'Deliberative' describes the on-balance subset."

## The text as writing

- The section on "learned" now interrupts the conditions and their
  explanation. The reader would put it after correction and displacement.
  This is the opposite of the previous reader's advice.
- "Process rather than outcome" appears three times.
- Three passages to rewrite first: the last two sentences of condition 2,
  the entry on automatic storage, and the sentence reconciling "learned"
  with the on-balance note.
