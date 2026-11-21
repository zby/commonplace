# Step 3: second outside reading, of the two-condition draft

Reader: a fresh general-purpose agent running Claude Opus, launched by Fable
on 2026-11-21 at the operator's request for a different model. It read the
draft and the on-balance note at commit `7568780d3`, and followed links to
the definitions of a self-improving system and an operative change. It was
told not to read anything else in the workshop and reported that it did not.
Fable transcribed and shortened this file. The reader has not confirmed it.
Fable's expected placements were recorded in the session before the reader
returned and are in the last column.

## What was done with it

The operator approved applying the findings on 2026-11-21. The draft was
rewritten. Condition 2 now requires a proposed change that can be rejected,
which places case C outside. A claim names a class of changes. The
single-loop sentence no longer mentions reversal. The points under "Other
points" were addressed in the rewrite.

## Placements

| Case | Store | Decision | Deliberative learner? | Kind | Correction | Displacement | Fable's expectation |
|---|---|---|---|---|---|---|---|
| A. A team adds a routing rule after weighing searches saved against misrouting, and can revise it. | Pass | Pass | Yes | Undetermined | Targeted | None stated | Same |
| B1. A link repairer that keeps a rewrite when a fixed validator passes, alone. | Depends on whether its later work consumes the repaired documents | Pass, fixed measure | Depends | Single-loop if admitted | None | None stated | Inside, with the same doubt |
| B2. The team with the repairer. | Pass | Pass | Yes | Double-loop for link rewrites | Targeted for the validator | None stated | Same |
| C. A nightly job that ranks help articles by clicks under a rule it cannot change. | Pass | **Depends**: is a direct update rule a judgment that could have gone against the change? | Depends | Single-loop if admitted | Targeted if admitted | Yes if admitted | Inside, single-loop. The reader does not confirm this. |
| D. A support bot that decides whether to add an answer and rewrites one after three unhelpful marks. | Pass | Additions pass. Rewrites depend. | Yes for additions | Undetermined | Targeted | None | Same, without the split |
| E1. A weekly fine-tuning run. | Fail | Fail | No | n/a | n/a | n/a | Same |
| E2. The team that decides on deployment, records it in a readable file, and rolls back. | Pass, but shallow | Pass | Yes | Undetermined | Targeted for deployments, bundle for weights | Yes | Same |
| F. A plan revised partway through a task and discarded at the end. | Depends on the horizon | Pass, assumed | Depends on the horizon | Undetermined | Targeted if inside | None | Same |
| G. A wiki that imports every page automatically, with editors deleting wrong ones. | Pass | Imports fail. Deletions pass. | Depends on the boundary and the class | Undetermined | None | None | Same |
| H. A code-review bot that adds a rule after five reports, never changes one, and lets the older rule win. | Pass | Pass, fixed measure | Yes | Single-loop in intent | None | None | Same |

Six placements were definite. The reader could not decide B1, C, F and G
from the draft, and split D by class of change.

## The two findings the reader puts first

1. **Condition 2 does not separate a gated decision from a direct update
   rule.** Neither "could have gone against the change" nor the
   fixed-measure clause tells the code-review bot's threshold from the click
   job's update formula, or from tabular reinforcement learning. A validator
   pass is also not a forecast that later work will go better.
2. **"Each change" does not fit "a named class of changes".** Condition 2
   says each change to the store is made by a judgment. Elsewhere a claim is
   made for a named class. The support bot, the wiki and Commonplace with
   its stored session traces get opposite answers depending on which
   sentence governs.

## Other points

- **Leftover from three conditions:** "Both are deliberative learning if
  each meets the three conditions."
- **Single-loop is defined by reversal:** "makes and reverses changes under
  a criterion it cannot revise". A learner with no correction does not fit.
- **The heading "A rule can be deliberated and then act automatically"**
  suggests that automatic writes under a deliberated rule count. The body
  says they do not.
- **The stated purpose**, to put all the learning in Commonplace under one
  name, conflicts with stored session traces being "learning but not
  deliberative".
- **"Checked on the outermost loop"** pulls against "which one a claim is
  about depends on the named system".
- **No exclusion of a work product.** The self-improving system definition
  has one. In the draft, "consumes" carries all the weight.
- **Displacement assumes a score.** It is undefined for a system that judges
  on balance.
- **The grain of a change is not fixed**, so targeted and bundle depend on
  the reader's choice.
- **Capacity or occurrence.** The kind is a capacity. Correction is phrased
  as a capacity and its example of "none" is an occurrence. The draft does
  not say which the term itself is.
- **The proviso is not in the conditions.** The sentence linking the term to
  a self-improving system adds "provided its judgment responds to evidence
  that bears on its objective". The two conditions do not require that.
- **Wording:** "that capacity" has no antecedent, "the autonomous claim" is
  undefined, criterion, standard and "measures, gates and checks" name one
  thing, and the draft carries workshop history that does not belong in a
  definition.

## Does the name fit

It fits the team cases well. It fits worst for the click job, if that job is
admitted at all, and next worst for the code-review bot. The reader: "The
Background's 'pair of scales' image fails here: there is one pan." It calls
this mainly a defect of the definition and not of the name: the
fixed-measure clause stretches "deliberative" to thresholds, and condition 2
does not mark where an update rule stops being a decision.

## Does the term add anything to the existing description

Beyond a short name, the reader finds four additions: the selection can be
an on-balance judgment with no global measure; the reporting vocabulary of
kinds, correction and displacement; the verdict "learned" for one change;
and the inclusion of changes to what is loaded or selected. It also finds
two losses that look unintended: the conditions drop responsiveness to
evidence, which only the proviso restores, and the exclusion of a work
product.

## On "learned"

The reader could state the comparison. It found "without it" underspecified,
as the first reader did: the store just before the change, or the current
store minus that one change. It also noted that the grain of the change is
not fixed and that the definition does not say whose work counts, which the
on-balance note requires.
