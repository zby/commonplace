# Instructions: Review Voyager for Trace-Derived Learning

## Goal

Produce a related-system review of Voyager focused on whether its skill-library loop belongs in [trace-derived learning techniques in related systems](../../notes/trace-derived-learning-techniques-in-related-systems.md).

Use `kb/instructions/review-related-system/SKILL.md` as the execution workflow. That skill already handles cloning the repo into `./related-systems/`, writing the review note, and running the standard follow-up checks.

## Targets

- Repo: `https://github.com/MineDojo/Voyager`
- Paper: `https://arxiv.org/abs/2305.16291`
- Suggested local clone: `related-systems/Voyager`
- Suggested note path: `kb/notes/related-systems/voyager.md`

## Why this candidate matters

Voyager is one of the most visible examples of learning reusable artifacts from iterative execution. The domain is Minecraft, but the structure may still matter for the survey.

## Inputs

Read all of:

1. The Voyager repository
2. The Voyager paper
3. [trace-derived learning techniques in related systems](../../notes/trace-derived-learning-techniques-in-related-systems.md)
4. [Trajectory-Informed Memory Generation ingest](../../sources/trajectory-informed-memory-generation-self-improving-agents.ingest.md)
5. [ClawVault](../../notes/related-systems/clawvault.md)

## Questions to answer

1. What trace substrate does Voyager actually learn from: code execution traces, task outcomes, critiques, or environment feedback?
2. What is the learned artifact: code skills, descriptions, curriculum state, exploration history?
3. How are new skills accepted or rejected?
4. Does Voyager resemble artifact-learning from trajectories, or is it better read as automated program synthesis with memory?
5. Which parts of its loop are specific to Minecraft, and which generalize to trace-derived learning more broadly?
6. Does it belong in the survey despite the domain mismatch?
7. If included, what caution text is needed so the comparison stays honest?

## Output spec

- Explicitly use `kb/instructions/review-related-system/SKILL.md`
- Write the review note in `kb/notes/related-systems/`
- Include an explicit section named `Trace-derived learning placement`
- In that section, state Voyager's position on both survey axes and whether it should be added to the survey note
- Run semantic review on the review note
- Run `/validate` on the review note

Be explicit about what is domain-specific machinery versus a reusable learning pattern.
