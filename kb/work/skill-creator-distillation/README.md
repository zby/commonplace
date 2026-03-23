# Workshop: Skill Creator Distillation

## Question

How should we understand skill creation as a distillation process, and what do the Claude Code and Codex `skill-creator` meta-skills reveal about the source material being distilled?

## Why this workshop exists

The starting prompt came from an external observation: OpenAI/Codex seems to treat skills as functional technical references, while Claude Code seems to treat skills more as approaches to classes of problems.

This workshop tests that framing against actual artifacts:

- Codex's system `skill-creator`
- Anthropic's `skills/skill-creator`
- the local theory note on [distillation](../../notes/distillation.md)

The goal is not just to compare two meta-skills, but to sharpen a KB claim: skill creation is broader than `methodology -> skill`. It also absorbs user language, experiments, failures, benchmarks, and product/runtime constraints.

## Current conclusion

The comparison supports the broad intuition, but refines it.

- Codex `skill-creator` is strongest as **artifact-construction distillation**: how to build, package, and validate a reusable skill artifact for another Codex instance.
- Claude Code `skill-creator` is strongest as **experimentation-and-evaluation distillation**: how to iteratively test, benchmark, review, and improve a skill with user feedback and explicit eval machinery.

The stronger generalization is:

`workshop evidence + product constraints + user language + prior methodology -> skill`

So skill creation looks less like a one-shot extraction from notes and more like a workshop process of repeated re-distillation from a mixed evidence base.

## Key artifact

- [comparison.md](./comparison.md) — synthesis note comparing the two meta-skills and refining the distillation claim

## Source packet

- [codex-skill-creator/](./sources/codex-skill-creator/) — local copy of the Codex system skill
- [claude-code-skill-creator/](./sources/claude-code-skill-creator/) — local copy of Anthropic's `skill-creator` folder

## Open questions

- How much of the difference is product philosophy versus product maturity?
- Should Commonplace model skill creation explicitly as a workshop pattern with source prompts, eval prompts, benchmark deltas, and final extracted skill?
- Is there a missing third axis around routing/interface distillation, distinct from both artifact contents and evaluation evidence?
