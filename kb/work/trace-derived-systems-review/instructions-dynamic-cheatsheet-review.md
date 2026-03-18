# Instructions: Review Dynamic Cheatsheet for Trace-Derived Learning

## Goal

Produce a related-system review of Dynamic Cheatsheet focused on whether it belongs in [trace-derived learning techniques in related systems](../../notes/trace-derived-learning-techniques-in-related-systems.md).

The core question is whether this system is genuinely trace-derived learning or mainly a retrieval wrapper with persistent state.

Use `kb/instructions/review-related-system/SKILL.md` as the execution workflow. That skill already handles cloning the repo into `./related-systems/`, writing the review note, and running the standard follow-up checks.

## Targets

- Repo: `https://github.com/suzgunmirac/dynamic-cheatsheet`
- Paper: `https://arxiv.org/abs/2504.07952`
- Suggested local clone: `related-systems/dynamic-cheatsheet`
- Suggested note path: `kb/notes/related-systems/dynamic-cheatsheet.md`

## Why this candidate matters

Dynamic Cheatsheet looks like a strong artifact-promotion case: live experience condensed into a persistent cheatsheet that shapes future inference without weight updates.

## Inputs

Read all of:

1. The Dynamic Cheatsheet repository
2. The Dynamic Cheatsheet paper
3. [trace-derived learning techniques in related systems](../../notes/trace-derived-learning-techniques-in-related-systems.md)
4. [Pi Self-Learning](../../notes/related-systems/pi-self-learning.md)
5. [Trajectory-Informed Memory Generation ingest](../../sources/trajectory-informed-memory-generation-self-improving-agents.ingest.md)

## Questions to answer

1. What raw signal feeds the cheatsheet updates: interaction turns, solved tasks, corrections, benchmark runs, or user feedback?
2. What is the update clock: every interaction, every task, every batch, or manual rebuild?
3. Is the cheatsheet schema narrow and typed, or open natural language?
4. How is persistence handled: append-only, merge, overwrite, score, or judge?
5. Is reinjection prompt-time only, or is there any training/distillation step?
6. Does this belong under artifact-learning, single-session extension, trajectory-run, or some combination?
7. Compared to Pi Self-Learning and trajectory-informed memory generation, what is genuinely new here?

## Output spec

- Explicitly use `kb/instructions/review-related-system/SKILL.md`
- Write the review note in `kb/notes/related-systems/`
- Include an explicit section named `Trace-derived learning placement`
- In that section, state Dynamic Cheatsheet's position on both survey axes and whether it should be added to the survey note
- Run semantic review on the review note
- Run `/validate` on the review note

Be careful not to overclaim learning if the repo only shows persistent prompting or retrieval.
