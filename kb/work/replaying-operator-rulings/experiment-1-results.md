# Experiment 1: results

Run 2026-11-21 by an agent (claude-fable-5-2), following
[the design](./experiment-1-fixed-measure.md). All 29 runs completed. The
answers, the key, the script that built the prompts and both scorers' grades
are in `experiment-1-runs/`.

## Result

**No worker reached the target, under any condition.** That includes the
calibration hint, which named the question, and Part B, where a reviewer
supplied the wording. Every worker noticed the fixed measure. Every one kept
fixed-measure learners outside the definition.

The two scorers agreed on all 29 grades. The second scorer was a fresh Opus
session given the rubric and the answers without the key.

### Part A: a cold review

| Hint | Grades for the target | Proposals that generalize or remove | Proposals that add or tighten | Proposals that reword |
|---|---|---|---|---|
| R0, none | N N N | 1 | 5 | 3 |
| G1, the bias | N N N | 4 | 0 | 5 |
| G2, generality | N N N | 5 | 2 | 2 |
| G3, continuity | N N N | 2 | 3 | 4 |
| G4, test each condition | N N N | 3 | 3 | 3 |
| G5, the user's position | N N N | 0 | 6 | 3 |
| P2, calibration | N N | 1 | 2 | 3 |

N means the answer raised the fixed measure as a problem and resolved it by
sharpening or adding to the exclusion. Each row except P2 has nine
proposals.

The counts in the last three columns were assigned before the key was
opened, by the designing agent alone. They are rough: several proposals
could be placed in two columns.

### Part B: answering the objection

| Condition | Grades |
|---|---|
| B0, untyped text | A A A |
| BT1, the type as it was | A A A |
| BT2, the type with the bias section | K K K |

A means the worker declined the reviewer's wording, kept the exclusion, and
rewrote or added to the text. K means it left the definition unchanged and
defended it. No worker generalized, and none deferred.

## Against the predictions

The recorded predictions were wrong for the target. They expected zero or
one hit with no hint, about two of three under G2 to G4, and both under the
calibration. There were none anywhere. The prediction that most proposals
add when there is no hint held for two of the three R0 answers.

## What the result shows

**1. The hints changed the direction of proposals.** With no hint, five of
nine proposals added or tightened and one generalized. Under the bias text
(G1) none added and four generalized. Under the generality hint (G2) five
generalized. Asking the worker to take the position of someone applying the
definition to other people's systems (G5) pushed the other way: six
additions and no generalization.

**2. The bias section in the definition type changed what workers did with
an objection.** Without it, all six workers rewrote the condition. With it,
all three left the definition unchanged, and one cited the specification's
warning against accretion as its reason. The section lists three options
beside adding: leave unchanged, generalize, remove. Workers took the first.
The old specification made no visible difference from untyped text.

**3. No hint produced the operator's ruling.** The general hints produced
generalizations elsewhere. The common ones were to make the judgment a
decision to keep and not a claim of improvement, to loosen "the same loop"
in the third condition, and in one answer to drop the legible store as a
condition. On the fixed measure, every answer went the other way.

## Why the target was missed

Three readings, which the experiment does not separate.

- **The checks file anchored the workers.** It places the repairer, the
  score-bound builder and Recuris outside, and it says "a change that flips
  a placement deserves an explanation". Twenty-two of the 29 answers speak
  of flipping placements, and most give "no placement changes" as a merit of
  their proposal. The workers treated the checks as the standard and made
  the definition agree with them.
- **The draft has a real inconsistency, and it points the other way.** Its
  note says a change kept because a validator passed meets the condition.
  Its exclusion says retention bound to a fixed measure does not. Workers
  found the conflict and resolved it by restricting the note.
- **The ruling may not be an observation.** The draft says the exclusion is
  what the term is for, and the workers defended that with reasons: without
  it the term covers any gated hill-climber, and the autonomous claim has
  nothing to test. The operator's ruling changed what the term should do. It
  preferred generality and continuity over marking what separates
  Commonplace. A worker cannot notice a preference in the materials if the
  materials state the opposite one.

By the design's own rule, a miss under the calibration hint means the
materials or the scoring are at fault. The scoring was unambiguous. The
materials are the likely fault, and specifically the checks file.

## What the format test settled

- **Grades were assigned without argument.** Two scorers agreed on 29 of 29.
- **Three proposals is a workable limit.** No answer reached the target by
  listing, and the three proposals were enough to count direction.
- **About 6,000 words of pasted material did not dilute attention.** Every
  answer engaged the second condition.
- **The count of added and generalized proposals is the more sensitive
  measure.** The target grade did not move. The counts did.
- **Cost.** 29 worker runs and one scoring run, each a single Opus call of
  about 8,000 to 10,000 input words. The answers total 13,500 words.

## Limits

- Three runs per condition. The Part B split is three against three with no
  overlap, and it is still nine runs.
- The proposal counts have one scorer.
- One ruling, one model.
- The G hints were written by an agent that knew the target.

## Proposed next steps, for the operator

1. **Rerun the calibration and two hints without the checks file,** or with
   a sentence saying the placements are open to revision. This tests the
   first reading directly.
2. **Add a hint about purpose,** since the third reading says the ruling was
   a choice of purpose. For example: "The term should be the general one.
   What distinguishes this project can be stated as a claim about a kind
   within it."
3. **Consider rewording the bias section.** It moved workers from adding to
   leaving unchanged, which is one of the options it names. If the wanted
   effect is generalization, the section does not yet produce it here.
4. **Choose the next ruling by kind.** Row 3 of the index, the horizon, is a
   recall of what the KB already said, and is the best candidate for
   something a worker could notice. Rows 1 and 4 changed what the definition
   was for.

## Round 2: hints about removing

Run 2026-11-21 at the operator's request, after the results above. Twelve
runs, three for each of four hints from
[the design](./experiment-1-fixed-measure.md#round-2-hints-about-removing).
The files are in `experiment-1-runs/round-2/`.

**No worker reached the target.** Across both rounds that is 0 of 41.

| Hint | What the three workers did | Fixed-measure learners |
|---|---|---|
| D1, "remove one condition or exclusion" | All three removed the same exclusion, "retention without a judgment", because the second condition already implies it. Two said in the same answer that the fixed-measure exclusion earns its place. | Stay outside |
| D2, every change must remove | Two removed the sentence that admits a validator-gated change. The third did not touch the subject. All three also removed "improves" from the second condition. | Stay outside |
| D3, look for removals first | All three removed the note that admits a validator-gated change. | Stay outside |
| D4, the term should be the general one | All three moved a feature out of membership into a kind: the strict on-balance standard twice, the legible store once. All three kept the fixed measure as a condition, reworded as "a measure the loop cannot question". | Stay outside |

The scorers agreed that no answer reached the target. They differed on the
three D1 answers: the designing agent graded them N, because they name the
fixed-measure exclusion and defend it, and the second scorer graded them M,
because they do not raise it as a problem.

### Against the predictions

Predicted: one hit in three for D1 and D2, none or one for D3, two for D4.
There were none. The prediction that D1 workers would pick the cheapest
removal held in kind: all three removed a redundant exclusion. It was wrong
about which one.

### What round 2 adds

- **A command to remove produces the removal of redundancy.** Told to remove
  one thing, every worker chose text whose removal changes no placement.
  Removing is not generalizing.
- **Removal can tighten.** The draft held one sentence that pointed toward
  the operator's ruling: a change kept because a validator passed meets the
  condition. Under D2 and D3, five of six workers removed that sentence.
  They removed the inconsistency by deleting the more general side of it.
- **The purpose hint was followed, on other features.** Under D4 the workers
  did move distinguishing features out of membership. None chose the fixed
  measure. The draft and the checks present that boundary as the one the
  term exists to mark, and the workers kept it.

The three readings given above for the miss still stand, and round 2
strengthens the first and third. Workers treat the placements in the checks
file as fixed, and they treat the draft's stated purpose as the criterion.
Every generalization they proposed served that purpose. The operator's
ruling changed it.

The first proposed next step is now the most informative one: rerun D1, D4
and the calibration without the checks file.

## Round 3: proposing against choosing, and cases

Run 2026-11-21. Sixteen runs, following
[the design](./experiment-1-fixed-measure.md#round-3-proposing-against-choosing-and-cases).
The files are in `experiment-1-runs/round-3/`. The two scorers agreed on all
sixteen.

### C: choosing between the two versions

| Condition | Chose the earlier version | Chose the later version |
|---|---|---|
| C0, no checks file | 2 | 2 |
| C1, with the checks file | 4 | 0 |

- **With the checks file, every worker chose the earlier version,** whichever
  was shown first. All four gave the flipped placements as a reason.
- **Without it, every worker chose the version shown first.** The two that
  chose the later version saw it first, and the two that chose the earlier
  version saw that first. Four runs cannot separate a preference from the
  order of presentation, so C0 shows no preference either way.
- **The reasons against the later version were about the on-balance note.**
  All six that chose the earlier version said that a measure the
  system merely "treats as the only one" is not an on-balance judgment,
  because the note requires every reasonable measure to agree. Three said the
  later version only moves the break to the single-loop and double-loop
  line.
- **What they would carry across.** All six that chose the earlier version
  would keep the later version's note that later evidence must be able to
  count against the kept change. Both that chose the later version would
  keep the earlier version's basis for a single measure: that it counts
  where it is the only reasonable one.

### L: ten candidates

**The target appears in none of the four lists.** Forty candidates were
listed, and none was to admit fixed-measure learners. All four lists include
tightening the fixed-measure clause, and adopt it. The rejected candidates
were the same few in each list: require reversibility, add a success
condition, require an explanation, require a language-model judge. Each is
something the draft or the checks already rule out.

### M: minimal pairs

**All four workers said the term should mark the difference in all three
fixed-measure pairs,** and none proposed a change that puts a lone
fixed-measure learner inside. All four proposed the same repair: a fixed
rule counts when the rule is itself kept by a judgment in the same system.
Two noticed that "keep everything" and "keep what passes the validator" are
both fixed rules and that the draft treats them differently, and would
resolve it by admitting a keep-everything policy that the system can revise.

### Against the predictions

| Test | Predicted | Result |
|---|---|---|
| C0 | 2 of 4 choose the later version | 2 of 4, but the choice followed the order shown |
| C1 | 1 of 4 | 0 of 4 |
| L | The target appears in 3 of 4 lists and is rejected | It appears in none |
| M | 1 of 4 reaches the target | 0 of 4 |

## Across the three rounds

- **Proposing.** In 49 runs that asked for changes, no worker proposed the
  operator's ruling. It was not among forty candidates that included
  rejected ones. It is not an idea these workers hold and decline. They do
  not generate it from these materials.
- **Choosing.** Shown the ruling as applied, workers with the checks file
  rejected it every time. Workers without the checks file showed no
  preference that four runs can detect.
- **The anchor.** The checks file decides the choice. The draft's link to
  the on-balance note supplies the argument: a single fixed formula is not
  agreement across every reasonable measure. That objection is one the
  adopted definition later answered, by saying the judgment is a decision on
  an expectation and that "on balance" is the later verdict.

The workers' position is coherent. Given a term whose stated purpose is to
mark judgment that is not bound to a measure, and checks that encode that
purpose, they defended it and repaired the draft toward it. The operator's
ruling changed the purpose. Nothing tested here leads a worker to do that.

**What this suggests for the format.** A replay can test whether workers
notice what the materials imply. It cannot test whether they will revise
what the materials are for, unless the prompt gives them the standing to do
so. Two things remain untested for this ruling: telling the worker that the
term's purpose is open, and a worker from another model family, since a
ChatGPT review did raise the point from the published workshop.

## Round 4: all three files open to change

Run 2026-11-22 at the operator's suggestion, following
[the design](./experiment-1-fixed-measure.md#round-4-all-three-files-open-to-change).
Nineteen runs. The files are in `experiment-1-runs/round-4/`. The two
scorers agreed on all nineteen.

| Condition | Result |
|---|---|
| W0, no hint | N N N |
| WG2, generality | N N N |
| WG3, continuity | N N N |
| WD4, purpose | N **H2** N |
| WP2, calibration | N N N |
| CW, choosing with the files open | 4 of 4 chose the earlier version |

**One worker reached the ruling,** under the purpose hint with all three
files open. It is the first hit in 64 runs that asked for changes. Its first
proposal was to take "not bound to a fixed measure" out of membership and
state it as the project's claim about a kind. It reworded condition 2 so
that the retaining step "may be a human, a language model, a validator or a
benchmark gate", removed the exclusion, and moved Recuris, case 7 and the
repairer alone to "inside the term, outside the kind". Its reason:

> The draft currently writes the project's distinctive bet into the
> membership conditions. That is why it needs the "degenerate judgment"
> clause, the outermost-loop rule and the "PRODIGY together with Minton"
> move. Those devices exist to readmit validator-gated learning that
> Commonplace actually does.

It also asked whether "deliberative" fits the kind better than the general
term, which an outside reader of the adopted definition raised later.

### What opening the files changed

- **It made the hit possible, and did not make it likely.** The same purpose
  hint with the checks fixed gave no hit in round 2. With the files open it
  gave one in three. The other two workers under that hint applied it to
  other features, as in round 2.
- **Workers used the permission.** Most answers now edit the checks or the
  note as well as the definition. They edit them toward the old boundary:
  resolving the open question in the checks, adding cases that pin the
  fixed-measure line, and adding to the note the sentence that a single
  measure counts where it is the only reasonable one.
- **The calibration answers softened and still missed.** In round 1 both
  workers answered "it should stay outside". In round 4 two of three
  answered that a learner should not be outside merely for using one
  measure, and should be outside when the system cannot question it. One
  moved the exclusion from the second condition to the third. A lone
  fixed-measure learner stays outside in all three.
- **Choosing did not move.** With the files open, all four workers still
  chose the earlier version, and all four gave the same argument from the
  on-balance note.

### Against the predictions

| Test | Predicted | Result |
|---|---|---|
| W0 | 0 of 3 | 0 of 3 |
| WG2 | 1 of 3 | 0 of 3 |
| WG3 | 1 of 3 | 0 of 3 |
| WD4 | 1 of 3 | 1 of 3 |
| WP2 | 1 of 3 | 0 of 3 |
| CW | 1 of 4 | 0 of 4 |

## Across the four rounds

- **Proposing:** 1 of 64 runs. The one hit needed two things together:
  permission to change the checks and the note, and a hint that states the
  choice of purpose.
- **Choosing:** 0 of 8 with the checks file, whether or not it was open to
  change. No detectable preference without it.
- **General advice about editing definitions never reached the ruling.**
  Generality, continuity, the bias text, commands to remove, and testing
  each condition gave no hit in 39 runs across both scopes.

The hint that worked is close to a statement of the ruling's premise. It
says the term should be the general one and that what distinguishes the
project belongs in a kind. That is a decision about what the definition is
for. The workers can carry out that decision once it is made. One in three
did so here. They do not make it.

