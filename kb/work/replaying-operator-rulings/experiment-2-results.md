# Experiment 2 results: the two-conditions ruling

Run and scored 2026-11-22 by an agent (claude-fable-5-2). The design and the
predictions are in [the design file](./experiment-2-two-conditions.md). The
answers, the key and both scorers' grades are in `experiment-2-runs/`.

## Result

Nineteen Opus runs. The two scorers agreed on all nineteen.

| Condition | Grades | Hits | Predicted |
|---|---|---|---|
| W0, no hint | N, M, M | 0 of 3 | 0 |
| WG2, generality | H2, N, M | 1 of 3 | 1 |
| WB, bias text | N, N, N | 0 of 3 | 0 |
| WR, test each condition | N, N, N | 0 of 3 | 1 |
| WD4, purpose | N, N, M | 0 of 3 | 1 |
| CW, choosing | two, two, two, three | 3 of 4 chose two conditions | 2 |

Proposing the operator's ruling occurred in 1 of 15 runs. Choosing it
occurred in 3 of 4. In experiment 1 the same two rates were 1 of 64 and 0 of
8 with the checks file present.

## The hit

Answer v01, under the generality hint, proposed as its second change to drop
"open to criticism" from the conditions and report it as a property beside
single-loop and double-loop. It re-placed five cases as members that lack
the property. Its reason was not the operator's. It reused the reason the
draft records for the fixed-measure ruling:

> a small change in how a system judges should not move it out of the term.
> Under C, it does exactly that. DGM (case 13) and HGM (case 14) differ only
> in whether descendant results feed back into the parent's selection weight.

No answer gave the operator's argument, that a store whose contents can be
pointed at already lets a later entry change an earlier one. No answer earned
H2c.

A second answer under the same hint, v14, went part of the way. It kept a
minimal third condition and moved the clause on displacement out of
membership into a reported property, which admits the same five cases. It
is graded N.

## What the other runs did

- **Testing each condition confirmed the third one.** All three WR answers
  went through the conditions as asked and all three kept "open to
  criticism". One wrote that its exclusions "are principled". They tested
  whether the condition excluded something the others did not. It does, so
  they kept it. The hint did not lead them to ask whether those cases should
  be outside.
- **The purpose hint was applied to other features.** Under WD4, one answer
  moved the legible store out of membership into a kind, and one did the
  same for the outermost-loop rule. Neither touched the third condition.
- **Nearly every run found the same two other problems.** Fourteen of the
  fifteen proposing answers said that condition 2 demands a forecast of
  improvement, which the on-balance note says is usually not available.
  All fifteen said the draft excludes Commonplace's own stored session traces
  while claiming to cover all its learning. These counts were made after the
  key was opened and by one reader.

## The choosers

Three of four chose the two-condition draft, in both presentation orders.
Their reasons repeat the hit's: cases 9 and 10, and cases 13 and 14, differ
by a small change and fall on opposite sides of membership, and a graded
property says more than a pass or fail. The one answer for three conditions
argued that the condition separates the systems the KB most needs to tell
apart, and that without it a learner with no correction is neither
single-loop nor double-loop.

## What this shows

- **This ruling is within reach of the workers when shown, and mostly out of
  reach unprompted.** They accept it three times in four. They propose it
  once in fifteen.
- **A recorded reason transferred.** The draft at this state carries the
  operator's reason for the earlier fixed-measure ruling. The hit and all
  three choosers for two conditions applied that reason to a different
  condition. In experiment 1, at a state before that reason was written, no
  chooser accepted the corresponding ruling. The two experiments differ in
  more than this, so the comparison is suggestive only.
- **The purpose hint did not repeat.** It gave the one hit in experiment 1
  and none here. The generality hint gave none there and the one hit here.
  Each is one hit in three runs, which does not separate them.
- **Workers spent their three proposals on defects they agreed about.** The
  two problems that nearly all runs raised are real findings about the
  draft. A worker limited to three changes may not reach a structural change
  that it would accept if asked.

## Predictions

Right on W0, WG2 and WB. One too high on WR and WD4. One too low on choosing.

## Limits

- Three runs per condition. No difference between hints is established.
- One model family and one ruling.
- The drafts name "the operator" in two places in the earlier version, as
  the source of the fixed-measure reason. That phrase was left in, as it was
  in experiment 1.
- The counts in the third bullet under "What the other runs did" were counted
  unblinded.
