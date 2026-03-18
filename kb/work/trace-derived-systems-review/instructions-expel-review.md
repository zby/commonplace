# Instructions: Review ExpeL for Trace-Derived Learning

## Goal

Produce a related-system review of ExpeL focused on whether it belongs in [trace-derived learning techniques in related systems](../../notes/trace-derived-learning-techniques-in-related-systems.md) as a cross-task experience-learning system.

Use `kb/instructions/review-related-system/SKILL.md` as the execution workflow. That skill already handles cloning the repo into `./related-systems/`, writing the review note, and running the standard follow-up checks.

## Targets

- Repo: `https://github.com/LeapLabTHU/ExpeL`
- Paper: `https://arxiv.org/abs/2308.10144`
- Suggested local clone: `related-systems/ExpeL`
- Suggested note path: `kb/notes/related-systems/expel.md`

## Why this candidate matters

ExpeL appears to turn past task trajectories into reusable natural-language experience. It may sit between Reflexion and trajectory-informed memory generation in the current landscape.

## Inputs

Read all of:

1. The ExpeL repository
2. The ExpeL paper
3. [trace-derived learning techniques in related systems](../../notes/trace-derived-learning-techniques-in-related-systems.md)
4. [Trajectory-Informed Memory Generation ingest](../../sources/trajectory-informed-memory-generation-self-improving-agents.ingest.md)
5. [Autocontext](../../notes/related-systems/autocontext.md)

## Questions to answer

1. What does ExpeL treat as "experience": full trajectories, solved tasks, mistakes, critiques, or compact lessons?
2. How is experience extracted and consolidated?
3. How is the retrieved experience injected into future runs?
4. Is the system single-task, cross-task, or benchmark-wide?
5. Does ExpeL produce only inspectable artifacts, or is there any training/distillation path?
6. Compared to trajectory-informed memory generation, what is different about the extraction granularity and memory lifecycle?
7. Does ExpeL fit the current axis model cleanly, or does it suggest a new subtype?

## Output spec

- Explicitly use `kb/instructions/review-related-system/SKILL.md`
- Write the review note in `kb/notes/related-systems/`
- Include an explicit section named `Trace-derived learning placement`
- In that section, state ExpeL's position on both survey axes and whether it should be added to the survey note
- Run semantic review on the review note
- Run `/validate` on the review note

Prefer concrete evidence about memory format and update triggers over general claims about "experience."
