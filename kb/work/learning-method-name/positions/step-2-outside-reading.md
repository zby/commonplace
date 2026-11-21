# Step 2: outside reading of the definition

Reader: a fresh general-purpose agent (claude-fable-5-2), launched by Fable
on 2026-11-21. It read the draft and the on-balance note as they stood after
commit `13a1803f6` plus the uncommitted edits of that hour. It was told not
to read the checks, the README, the rulings, the precedents or any position,
and it reported that it did not. Fable transcribed this file. The table and
the three answers are the reader's text, shortened only where marked. The
reader has not confirmed the file. It is the same model as one of the
authors, so it is an independent session and not an independent model.

Before the reader returned, Fable recorded expected placements in the
session. They are in the last column.

## Placements

C1 is the legible store, C2 the judgment in the loop, C3 open to criticism.

| Case | C1 | C2 | C3 | Deliberative learner? | Kind | Fable's expectation |
|---|---|---|---|---|---|---|
| A. A team adds a routing rule after weighing searches saved against misrouting. Later misrouting can lead it to revise the rule. | Pass | Pass | Pass | Yes | Undetermined | Same |
| B1. A link repairer keeps a rewrite exactly when a fixed validator passes. The repairer alone. | Doubtful | Pass, fixed measure | Fail as described | No | n/a | Outside on C3 |
| B2. The team with the repairer. The team changes the validator after bad repairs. | Pass | Pass | Pass | Yes | Double-loop for link rewrites, undetermined for validator edits | Double-loop |
| C. A nightly job ranks help articles in a readable table, up when clicked, down when clicks fall. Nothing can change the rule. | Pass | Pass on one reading, fail on another | Pass | Yes on the reader's reading | Single-loop | Inside, single-loop |
| D. A coding agent decides after each task whether to append a lesson to a memory file. Every run loads it. Nothing revises it. | Pass | Pass | Fail as described | No | n/a | Outside on C3 |
| E1. A weekly fine-tuning run. | Fail | Fail | Not reached | No | n/a | Outside on C1 |
| E2. The team that decides from evaluations whether to deploy, records it in a readable file, and rolls back. | Depends on what the file does | Pass | Pass | Yes if the file selects the checkpoint | Undetermined | Inside for the deployment file |
| F. An agent revises its written plan partway through a task. The plan is discarded at the end. | Pass | Pass, assumed | Not stated | Depends on the declared horizon | Undetermined | Depends on the horizon |

Every placement the reader could make agrees with the expectation. Where it
could not decide, it named the missing fact.

## Which sentences did the work

- "A gate that admits a change once and never lets later evidence count
  against it fails this condition" excluded D and B1.
- The sentences on gradient training excluded E1.
- "A change made because a validator passed meets the condition" admitted C.
- C3 excluded the most. C1 excluded E1. **C2 excluded nothing by itself**,
  because of the fixed-measure clause. The horizon excluded F, and it is not
  one of the three numbered conditions.

## Where the reader found the draft unclear, inconsistent or silent

1. **Fixed measure against "nothing is decided".** A validator and automatic
   trace storage are both automatic rules. The only test offered is that a
   decision "could have gone against the change". Any conditional rule
   passes that. Case C turns on it.
2. **Is undoing required?** Condition 3 says the system "undoes the change
   where that is possible". The notes say the condition "does not require
   that a change can be undone" and ask only for a changed next step.
3. **"Each change" in a mixed store.** The draft does not say whether a
   store that receives judged and unjudged changes fails C2, or whether the
   claim is made per class of change.
4. **Which loop is tested.** "Checked on the outermost loop" pulls against
   "which one a claim is about depends on the named system". In B2 the
   reader could not tell whether the store under test is the validator or
   the documents.
5. **The kind is attached to a learner and is relative to a class.**
6. **Capacity with people in the system.** People can always question a
   criterion. The draft demands an account for C3 and makes no matching
   demand for double-loop.
7. **Legibility is given by a list.** A table of numeric ranks passes. So
   would a readable table of values in tabular reinforcement learning, which
   the draft uses as its contrast.
8. **A legible pointer to an opaque artifact.** Case E2 depends on whether a
   readable file that selects a checkpoint is the store.
9. **Store against product.** The draft does not say how to treat a system
   whose job is to edit a readable artifact. In Commonplace the product and
   the store are the same thing.
10. **The horizon rule is stated only for Commonplace.**
11. **"Learning" is used in two senses.** The term is defined as learning
    that meets three conditions, and Simon's learning is a lasting change in
    capacity. The draft also says a system whose changes improve nothing is
    still doing deliberative learning.
12. **"Deliberative" is used for one condition.** The draft says adding an
    entry to `kb/log.md` "is deliberative", on C2 alone. Case D is that
    example with C3 removed, and it fails.
13. **Does a decision under an open verdict meet C2?** The trial example
    suggests yes. Condition 2 does not say so.
14. **Running the same test again.** Whether a rerun counts as evidence from
    later use is not stated.
15. **Correction by a later entry.** Whether a superseding entry in an
    append-only store is "a further change" is not stated. Case D depends on
    it.

## Does the name fit

The reader's answer, in full:

> It fits A and B2 well. People weigh considerations, and they revisit the
> outcome. It fits worst in C. A nightly job applies a click rule. Nothing
> weighs anything, and no alternative is considered. The fixed-measure clause
> admits it, and the name describes nothing in it.
>
> Cases C and D together show the mismatch. D is the case where an agent
> most plainly deliberates, and the definition excludes it. C contains no
> deliberation, and the definition admits it. A reader who knows only the
> name would place both the other way round.
>
> What the three conditions actually select is a readable store whose
> changes are gated and later corrected from use. "Deliberative" names only
> the general case of C2, and the special-case clause removes the
> deliberation.

## On "learned"

The reader could name the comparison in outline: the system with the change
against the system without it, on later work in the declared area and
horizon, under every reasonable measure. It could not tell whether "the
system without it" is the store as it stood before the change or the present
store with that one change taken out. The on-balance note compares successor
with predecessor, which is the first. The draft's Friday review compares
keeping the rule with removing it, which is the second.
