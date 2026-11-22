# Experiment 2: the two-conditions ruling

Designed 2026-11-22 by an agent (claude-fable-5-2), before any run. It
replays row 4 of the
[replay index](../../reports/retained/definition-rulings-replay-index-2026-11-21.md).

## The ruling

At `13a1803f6` the draft had three conditions. The third, "open to
criticism", put outside the term an agent that decides which lessons to
record and never revises them. The operator ruled that being open to
criticism is a property and not a condition: a store whose contents can be
pointed at already lets a later entry change an earlier one. Two agents
amended this: an addressable store makes correction possible and does not
guarantee it. The draft at `7568780d3` has two conditions.

## Why this ruling

[Experiment 1](./experiment-1-results.md) reached the operator's ruling in
1 of 64 runs. That ruling was a decision about what the term is for. This
one can be argued from the text of the draft, and its outcome is easier to
score: three conditions become two.

The single hit in experiment 1 came under a hint about purpose. This ruling
has the same shape, a feature moved out of membership. So the experiment
also tests whether that hint works on a second ruling.

## Setup

As in round 4 of experiment 1. Each worker is a headless Opus run with no
tools, started in an empty directory, with the materials pasted into the
prompt. The materials are the draft, the checks file and the on-balance
note, all at `13a1803f6`. All three are declared open to change. The build
script with the prompts verbatim is kept in `experiment-2-runs/build.py`.

**Proposing**, three runs per condition. Each worker proposes its three most
important changes.

| Condition | Hint |
|---|---|
| W0 | None |
| WG2 | Prefer the most general definition; a distinguishing feature can be a kind or a property instead of a condition. Same text as in experiment 1. |
| WB | The bias text from the definition type. |
| WR | Test each condition: what does it exclude that the others do not, and should those cases be excluded? |
| WD4 | The term should be the general one; what distinguishes the project is a claim about a kind. Same text as in experiment 1. |

**Choosing**, four runs (CW). The worker sees the three-condition and the
two-condition draft, in alternating order, and says which to adopt. In the
later draft, two phrases that name the operator were made neutral.

## Scoring

Two blind scorers, the designing agent and a fresh Opus run, grade answers
under shuffled ids before the key is opened.

- **H2:** a proposed change removes "open to criticism" as a condition of
  membership and reports correction as a property or a kind.
- **H2c:** the same, and the answer also says that the store makes
  correction possible without guaranteeing it.
- **H1:** the answer questions whether the third condition belongs in
  membership, without proposing to move it.
- **N:** the third condition is discussed and stays a condition.
- **M:** it is not discussed.

## Predictions

Recorded before the runs.

| Condition | Predicted hits (H2 or H2c) |
|---|---|
| W0 | 0 of 3 |
| WG2 | 1 of 3 |
| WB | 0 of 3 |
| WR | 1 of 3 |
| WD4 | 1 of 3 |
| CW | 2 of 4 choose the two-condition draft |

The checks file at this state places a case outside "on C" several times,
so workers may defend the condition as they defended the fixed-measure
boundary.
