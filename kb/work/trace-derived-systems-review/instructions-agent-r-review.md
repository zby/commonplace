# Instructions: Review Agent-R for Trace-Derived Learning

## Goal

Produce a related-system review of Agent-R focused on whether it belongs in [trace-derived learning techniques in related systems](../../notes/trace-derived-learning-techniques-in-related-systems.md) as a weight-learning system built from agent traces.

Use `kb/instructions/review-related-system/SKILL.md` as the execution workflow. That skill already handles cloning the repo into `./related-systems/`, writing the review note, and running the standard follow-up checks.

## Targets

- Repo: `https://github.com/ByteDance-Seed/Agent-R`
- Paper: `https://arxiv.org/abs/2501.11425`
- Suggested local clone: `related-systems/Agent-R`
- Suggested note path: `kb/notes/related-systems/agent-r.md`

## Why this candidate matters

Agent-R looks like the strongest immediate addition on the weight-learning side: reflective self-training over agent traces rather than memory notes.

## Inputs

Read all of:

1. The Agent-R repository
2. The Agent-R paper
3. [trace-derived learning techniques in related systems](../../notes/trace-derived-learning-techniques-in-related-systems.md)
4. [OpenClaw-RL ingest](../../sources/openclaw-rl-train-any-agent-simply-by-talking.ingest.md)
5. [memory management policy is learnable but oracle-dependent](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md)

## Questions to answer

1. What trace unit becomes training data in Agent-R: failed rollouts, corrected trajectories, critiques, or full interactive sessions?
2. What oracle or judge decides what becomes training signal?
3. Is training online during deployment, offline from collected traces, or staged in cycles?
4. Does Agent-R create any inspectable intermediate artifacts before weight updates?
5. Compared to OpenClaw-RL, is the main difference substrate, timing, oracle type, or all three?
6. Compared to AgeMem, is the target narrower memory policy or broader agent behavior?
7. Should Agent-R be added to the survey as a core weight-learning example?

## Output spec

- Explicitly use `kb/instructions/review-related-system/SKILL.md`
- Write the review note in `kb/notes/related-systems/`
- Include an explicit section named `Trace-derived learning placement`
- In that section, state Agent-R's position on both survey axes and whether it should be added to the survey note
- Run semantic review on the review note
- Run `/validate` on the review note

Prioritize implementation details about data collection and training flow. Do not settle for benchmark claims alone.
