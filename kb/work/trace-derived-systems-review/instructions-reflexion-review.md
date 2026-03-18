# Instructions: Review Reflexion for Trace-Derived Learning

## Goal

Produce a related-system review of Reflexion focused on whether it should appear in [trace-derived learning techniques in related systems](../../notes/trace-derived-learning-techniques-in-related-systems.md) as an early trace-to-artifact system.

Use `kb/instructions/review-related-system/SKILL.md` as the execution workflow. That skill already handles cloning the repo into `./related-systems/`, writing the review note, and running the standard follow-up checks.

## Targets

- Repo: `https://github.com/noahshinn/reflexion`
- Paper: `https://arxiv.org/abs/2303.11366`
- Suggested local clone: `related-systems/reflexion`
- Suggested note path: `kb/notes/related-systems/reflexion.md`

## Why this candidate matters

Reflexion is one of the clearest early examples of verbal reinforcement and episodic memory extracted from task feedback. Even if its mechanisms are simpler than newer systems, it may be an important ancestor case for the survey.

## Inputs

Read all of:

1. The Reflexion repository
2. The Reflexion paper
3. [trace-derived learning techniques in related systems](../../notes/trace-derived-learning-techniques-in-related-systems.md)
4. [OpenClaw-RL ingest](../../sources/openclaw-rl-train-any-agent-simply-by-talking.ingest.md)
5. [ClawVault](../../notes/related-systems/clawvault.md)

## Questions to answer

1. What feedback signal drives Reflexion: scalar reward, natural-language critique, success/failure labels, or environment state?
2. What exactly gets persisted: freeform reflections, episodic memories, examples, or plans?
3. Does the system learn only at prompt time, or does it ever produce training data or weight updates?
4. Is the memory per task, per benchmark environment, or meant to generalize across tasks?
5. Does Reflexion fit better as artifact-learning from trajectories or as a narrower reflection loop?
6. Relative to OpenClaw-RL, what does verbal reinforcement preserve that weight-learning throws away?
7. Does Reflexion deserve a place in the survey as a historical precedent, a live comparison point, or both?

## Output spec

- Explicitly use `kb/instructions/review-related-system/SKILL.md`
- Write the review note in `kb/notes/related-systems/`
- Include an explicit section named `Trace-derived learning placement`
- In that section, state Reflexion's position on both survey axes and whether it should be added to the survey note
- Run semantic review on the review note
- Run `/validate` on the review note

Do not let paper influence outrun source inspection. If the repo is thin, say so.
