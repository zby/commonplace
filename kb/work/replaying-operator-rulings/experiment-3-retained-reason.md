# Experiment 3: the retained reason

Designed 2026-11-22 by an agent (claude-fable-5-2), before any run.

## The question

**Does a recorded reason for one ruling lead workers to a later ruling?**

[Experiment 2](./experiment-2-results.md) suggested that it does. The draft
at `13a1803f6` carries the operator's reason for the fixed-measure ruling:

> The operator's reason: the definition should be general and continuous, so
> that a small change to how a system judges does not move it out of the
> term.

The one hit in that experiment and all three workers who chose the
two-condition draft applied that reason to a different condition. The two
experiments differ in the ruling, the draft and the checks, so they do not
isolate the reason. This experiment changes only the reason.

A second observation motivates the test. The operator said about three and
a half hours before the fixed-measure ruling that a deterministic judgment
is a degenerate case of the on-balance judgment. The draft at `a6bdbb508`
records that as a claim, without a reason, and still excludes fixed-measure
learners. Workers in experiment 1 resolved the conflict by deleting the
claim. A claim recorded without its reason did not carry.

## Setup

As in experiment 2. Each worker is a headless Opus run with no tools,
started in an empty directory, with the materials pasted into the prompt.
All files are declared open to change. The prompts and the hint text are
those of experiment 2, unchanged.

Materials at `13a1803f6`, the state of experiment 2. The reason appears
only in the draft, in the note "A fixed measure is the special case". The
checks file and the on-balance note do not carry it.

| Arm | The draft |
|---|---|
| R+ | As committed. |
| R− | The quoted sentence removed. The claim that a fixed measure is the special case stays. |

| Condition | Runs per arm | Task |
|---|---|---|
| CW, choosing | 6, three in each order | Choose between the three-condition and the two-condition draft. |
| WG2, proposing | 6 | Propose the three most important changes, under the generality hint. |

In the R− arm the sentence is removed from both versions shown to a
chooser. R+ repeats experiment 2 with fresh runs. Its earlier answers are
not reused, so that both arms are run in the same batch.

That is 24 worker runs and one scoring run.

### Part A, dropped before the run

The first version of this design had a second part. It added the reason to
the draft at `a6bdbb508`, the state of experiment 1, and asked four workers
to choose between the drafts before and after the fixed-measure ruling. It
was dropped when the materials were built. The later draft that choosers saw
in experiment 1 already carries the sentence, with "The operator's reason:"
changed to "The reason:". So those choosers had read the reason, and with
the checks file present none of eight chose the later draft. Part A would
have repeated that test with the sentence in both versions.

This also corrects a reading in the
[results of experiment 2](./experiment-2-results.md), which says that in
experiment 1 no chooser accepted the ruling "at a state before that reason
was written". The state was before it. The later version shown to the
choosers was not.

## Scoring

Two blind scorers, the designing agent and a fresh Opus run, grade answers
under shuffled ids before the key is opened. The grades are
those of experiment 2: H2, H2c, H1, N and M for proposing, and the version
chosen for choosing.

One more mark is recorded for every answer: **C** when the answer gives
continuity as a reason, in the draft's words or its own. In the R− arm a C
means the worker supplied the reason unaided.

## Predictions

Recorded before the runs.

| Condition | R+ | R− |
|---|---|---|
| CW, choose the two-condition draft | 4 of 6 | 2 of 6 |
| WG2, hits (H2 or H2c) | 1 of 6 | 0 of 6 |
| Answers marked C | 6 of 12 | 1 of 12 |

## What each outcome would show

- **R+ above R− on choosing.** The recorded reason does work that the
  recorded claim does not. That supports a rule that a ruling is recorded
  with its reason, in the file the next worker reads.
- **No difference.** The effect in experiment 2 came from the ruling or the
  state, not from the reason. The suggestion in its results should then be
  withdrawn.

## Limits

- Six runs per cell. A difference of two choosers is within what order of
  presentation produced in experiment 1.
- One sentence, one model, one definition.
- The sentence names the operator in the earlier draft of the R+ arm. A
  worker may defer to the authority and not to the reason.
