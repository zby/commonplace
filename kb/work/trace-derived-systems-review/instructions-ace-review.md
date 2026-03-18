# Instructions: Review ACE for Trace-Derived Learning

## Goal

Produce a related-system review of ACE focused on whether it belongs in [trace-derived learning techniques in related systems](../../notes/trace-derived-learning-techniques-in-related-systems.md).

This is not a generic repo summary. The review should answer how ACE learns from execution traces, what substrate it promotes into, and whether it changes the current two-axis comparison.

Use `kb/instructions/review-related-system/SKILL.md` as the execution workflow. That skill already handles cloning the repo into `./related-systems/`, writing the review note, and running the standard follow-up checks.

## Targets

- Repo: `https://github.com/ace-agent/ace`
- Paper: `https://arxiv.org/abs/2510.04618`
- Suggested local clone: `related-systems/ace`
- Suggested note path: `kb/notes/related-systems/ace.md`

## Why this candidate matters

ACE looks like one of the closest external analogues to the artifact-learning side of the current survey: execution feedback, evolving playbooks, and repeated improvement across runs.

## Inputs

Read all of:

1. The ACE repository
2. The ACE paper
3. [trace-derived learning techniques in related systems](../../notes/trace-derived-learning-techniques-in-related-systems.md)
4. [Autocontext](../../notes/related-systems/autocontext.md)
5. [ClawVault](../../notes/related-systems/clawvault.md)

## Questions to answer

1. What is ACE's actual source trace: conversation logs, judge outputs, execution telemetry, or run trajectories?
2. What are the trigger boundaries for learning: per turn, per run, per tournament, per benchmark pass?
3. What intermediate artifacts does ACE create: playbooks, lessons, prompts, plans, reports, or something else?
4. Does ACE stop at inspectable artifacts, or does it also promote into weights?
5. On axis 1 of the current survey, is ACE best read as a service-owned backend, a trajectory-run system, or something else?
6. On axis 2, is ACE purely artifact-learning, or mixed?
7. Does ACE strengthen, weaken, or split any claim in the current survey note?

## Output spec

- Explicitly use `kb/instructions/review-related-system/SKILL.md`
- Write the review note in `kb/notes/related-systems/`
- Include an explicit section named `Trace-derived learning placement`
- In that section, state ACE's position on both survey axes and whether it should be added to the survey note
- Run semantic review on the review note
- Run `/validate` on the review note

Write concisely. Prioritize implementation-backed claims over paper framing whenever they differ.
