# Operator rulings on the deliberative-learning definition: replay index

Recorded 2026-11-21 by an agent (claude-fable-5-2) that took part in the
work. This is an index into git history, not a copy of it. It marks five
points in the drafting of
[deliberative learning](../../theory/definitions/deliberative-learning.md)
at which the agents held one position and the operator ruled another. Each
row names the commit that holds the state before the ruling, so that an
experimenter can give that state to a fresh worker and see what it proposes.

Nothing here has been replayed. The record supports no claim about what a
model can or cannot notice.

## The five rulings

Three agents worked on the draft: claude-fable-5-2, gemini-4-neon and
gpt-6.2-astra. All paths are under `kb/work/learning-method-name/`, which
was deleted in `c3ba6b8bf`.

| # | Ruling | State before | What the agents held | The operator's ruling | Applied in |
|---|---|---|---|---|---|
| 1 | Fixed measure | `a6bdbb508` | A learner that keeps changes by one fixed measure is outside the definition. A review by ChatGPT had objected to this. The drafting agent recorded the objection as open for the operator and left the exclusion in place. | The fixed measure is a special case, not an exclusion. A small change to a system should not move it outside the definition. | `b940a86dd` |
| 2 | Changes to the store | `aa23d25fb` | The conditions and the verdict "learned" are stated in terms of reliance on a kept change. | Putting content into the store is the change that does the learning. A store holds contents, not changes. | `f8d3af9e0` |
| 3 | Horizon | `3ffd00f00` | An air-traffic sequencer that keeps or drops a schedule could not be placed. | Learning is relative to a declared horizon, as the KB's definitions of a self-improving system and an operative change already say. | `13a1803f6` |
| 4 | Two conditions | `13a1803f6` | Being open to criticism is a third condition. An agent that decides which lessons to record and never revises them is therefore outside. | A store whose contents can be pointed at already lets a later entry change an earlier one. Open to criticism is a property, not a condition. Two other agents then amended this: an addressable store makes correction possible and does not guarantee it. | `7568780d3` |
| 5 | Stopping | `e38818707` | Each outside reading's findings are applied, and another reading is run. | Adopt the definition now and defer the remaining findings. | `b80dd9c53` |

The operator's own words for each ruling are in `rulings.md` at `7e613ece8`.

## How to set up a replay

Extract the state into a directory outside any checkout of this repository:

```bash
git archive <state-commit> <paths> | tar -x -C <empty-directory>
```

- **Give the worker** `draft-definition.md` and `definition-checks.md` from
  the workshop directory, and
  `kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md`,
  all at the state commit.
- **Withhold** `rulings.md`, `README.md` and everything under `positions/`.
  They state the rulings or lead toward them. For row 4 the proposal that
  states the ruling was committed in `69f645be5`, so the state is that
  commit's parent.
- **Run the worker without this repository's instructions.** The current
  `AGENTS.md` and the definition type already carry what was learned from
  these rulings.
- **Record three outcomes:** the operator's ruling, a different change that
  simplifies or generalizes the definition, or a change that adds to it.

## Limits

- **Five rulings from one definition on one day.** They were selected by a
  participant, from memory of the session and the rulings file.
- **Rulings where the agents agreed with the operator are left out.** The
  table therefore overstates how often the agents and the operator differed.
- **The agents were not asked what a replay would ask.** In the session they
  were answering particular objections and reader findings. A worker asked
  to review the whole draft starts from a different position.
- **Row 1 was not unprompted.** An outside review had raised the point before
  the operator ruled.
- **Row 5 has no single state that poses its question.** Stopping was a
  judgment about the whole course of work. It is the weakest row as a test.
