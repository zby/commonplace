# Replaying operator rulings

Posed 2026-11-21 by the operator. Written by an agent (claude-fable-5-2).

## Question

**What is the most general instruction that leads a fresh worker to notice
what the operator noticed?**

While the definition of deliberative learning was drafted, the operator made
several rulings that reversed what three agents held. The
[replay index](../../reports/retained/definition-rulings-replay-index-2026-11-21.md)
lists five, each with the commit that holds the state before it.

For each ruling, a worker can be given that state together with a hint. The
hints are general advice about definitions, of several kinds. The result of
interest is which general hints, if any, lead workers to the ruling.

Telling a worker what the operator said would work and would show nothing
useful. The aim is to find other ways to induce the observation: advice
general enough to write into a type or an instruction.

## Why it matters

- **For what is written into types and instructions.** A general hint that
  works is a candidate sentence for the type or instruction that governs the
  task. The definition type gained a section on a revision bias on
  2026-11-21 from one session's evidence. This is a way to test such text
  before relying on it.
- **For what agents could do without the operator.** If a general hint is
  enough, the operator's contribution at that point could be replaced by an
  instruction. If no general hint works, it could not, at least for these
  workers.

## Plan

1. Run [experiment 1](./experiment-1-fixed-measure.md) on the first ruling to
   test the format: the materials, the hints, the limit on answers and the
   scoring.
2. Fix what the format test exposes.
3. Decide with the operator which other rulings to replay. Rows 2 to 4 of
   the index are candidates. Row 5, stopping, has no single state that poses
   its question.

The workers are cheaper models than the agents that did the original work.
The first experiment uses Claude Opus.

## What closes the workshop

- Experiment 1 has been run and its format judged usable or not.
- The operator has decided whether to replay other rulings, and those chosen
  have been run.
- Any hint that the results support has been proposed as text for a type or
  an instruction, or the reason for not proposing it is recorded.

Results that should outlast the workshop go to `kb/reports/retained/`.

## Bookkeeping

Commits carry `Workshop: kb/work/replaying-operator-rulings`.
