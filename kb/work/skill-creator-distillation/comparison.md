# Skill Creator Comparison: Claude Code vs Codex

## Question

Initial hypothesis:

- OpenAI/Codex treats skills as functional references: matter-of-fact technical artifacts for another Codex instance.
- Claude Code treats skills as approaches to classes of problems.

Related claim to test against the KB: skill creation is a [distillation](../../notes/distillation.md) process, but the source material is broader than notes — it also includes user input, experiments, failures, and product/runtime constraints.

## Source packet

Downloaded/copied on 2026-03-23:

- `sources/codex-skill-creator/` — copied from the local Codex system skill at `/home/zby/.codex/skills/.system/skill-creator`
- `sources/claude-code-skill-creator/` — copied from `https://github.com/anthropics/skills`, path `skills/skill-creator/`
- Theory note: [distillation](../../notes/distillation.md)

Quick inventory:

| Artifact | Codex | Claude Code |
|---|---:|---:|
| Files in skill folder | 9 | 18 |
| `SKILL.md` lines | 416 | 485 |
| Extra agent instructions | `agents/openai.yaml` only | `agents/grader.md`, `agents/comparator.md`, `agents/analyzer.md` |
| Scripts | `init_skill.py`, `generate_openai_yaml.py`, `quick_validate.py` | eval runner, benchmark aggregation, description improver, packaging, viewer generation |
| Primary extra reference | `references/openai_yaml.md` | `references/schemas.md` |

The folder shapes already suggest the main difference: Codex packages skill construction and registration; Claude packages skill construction plus a full evaluation loop.

## Shared substrate

The two meta-skills agree on the core ontology of what a skill is.

- Both treat the `description` field as the primary trigger surface.
- Both use progressive disclosure: metadata always loaded, `SKILL.md` on trigger, bundled resources on demand.
- Both organize bundled resources into `scripts/`, `references/`, and `assets/`.
- Both explicitly warn against bloated instructions and prefer explaining *why* rather than relying on rigid all-caps rules.

The difference is not that one system treats skills as knowledge and the other doesn't. Both treat skills as compressed operational knowledge for a bounded-context agent.

## What Codex Distills

The Codex `skill-creator` is best read as a distillation of **artifact construction conventions**.

Its process is:

1. Understand the skill with concrete examples.
2. Plan reusable contents.
3. Initialize the folder with `init_skill.py`.
4. Edit the skill and bundled resources.
5. Validate with `quick_validate.py`.
6. Iterate from real usage and optional forward-testing.

What this skill mostly teaches is:

- how to shape the skill folder
- what kinds of reusable resources belong in it
- how to keep the prompt lean
- how to generate product-specific metadata (`agents/openai.yaml`)
- where the skill should live so Codex can discover it

The methodology is aimed at producing a well-formed reusable artifact — not at running a measurement-heavy optimization loop.

The clearest product-specific signal is the supporting reference [`sources/codex-skill-creator/references/openai_yaml.md`](./sources/codex-skill-creator/references/openai_yaml.md): the extra material covers UI metadata, dependency declarations, and invocation policy. The meta-skill is concerned with how a skill is packaged into the Codex product surface.

## What Claude Code Distills

The Claude Code `skill-creator` is best read as a distillation of **iterative skill experimentation**.

Its center of gravity is not folder initialization. It is the loop:

1. capture intent
2. interview and research
3. write the draft
4. create test prompts
5. run with-skill and baseline executions
6. draft assertions while runs are executing
7. grade, benchmark, and review outputs
8. revise
9. optimize triggering with should-trigger / should-not-trigger evals

This is why the Claude packet contains far more machinery:

- grader, comparator, and analyzer agent instructions
- schemas for eval artifacts
- benchmark aggregation scripts
- trigger-description optimization scripts
- an HTML review UI

The distinction is not that Claude's version is "more detailed." It distills a different source: not just "how to write a skill," but "how to learn whether the skill is actually helping."

That source is what the initial hypothesis gestured at with "approaches to problems." The approach encoded here: co-develop with the user, compare against baselines, inspect outputs, quantify what you can, keep humans in the loop, and re-distill from evidence.

## Comparison

The initial framing is directionally right but too coarse.

More precise:

- Codex `skill-creator` distills **how to build a reusable skill artifact for another Codex instance**.
- Claude Code `skill-creator` distills **how to iteratively discover, test, and improve a skill with user feedback and benchmarks**.

So the split is not:

- Codex = technical reference
- Claude = problem-solving philosophy

It is closer to:

- Codex = artifact-construction distillation
- Claude = experimentation-and-evaluation distillation

Both are functional. Claude's function is broader: it treats skill creation as an empirical workshop process rather than mainly a packaging task.

## Distillation Implications

This comparison strengthens the KB claim that skill creation is a distillation process, but forces a refinement.

The source for skill creation is not just methodology notes. It is a mixed substrate:

- permanent guidance about skill anatomy
- product-specific constraints and metadata formats
- user intent and trigger phrasings
- concrete example tasks
- repeated work noticed across runs
- observed failures and regressions
- benchmark results and blind comparisons
- runtime constraints of the host environment

This is still distillation in the KB sense: compress knowledge so a bounded consumer can act. But the source is broader than "notes → skill":

`workshop evidence + product constraints + user language + prior methodology → skill`

Anthropic's meta-skill makes this explicit — the skill is repeatedly re-distilled from new evidence. Codex's meta-skill acknowledges the same pattern in lighter form through iteration and forward-testing, but does not formalize evidence collection as heavily.

## Provisional claim

Skill creation is not a single distillation from methodology into instructions. It is a **workshop process of repeated re-distillation** from a mixed evidence base, where the final skill is one output and the eval harness / trigger examples / helper scripts are additional distillates.

This suggests a provisional, non-exhaustive two-axis model:

| Axis | Question |
|---|---|
| Artifact distillation | What reusable knowledge/resources should live inside the skill? |
| Evaluation distillation | What evidence from tests, failures, and user review should survive into the next version? |

Codex's `skill-creator` is stronger on the first axis. Claude Code's is stronger on the second.

A third routing/interface axis may be needed for a full framework: packaging metadata, invocation policy, and trigger optimization are adjacent to artifact distillation but not identical to it.

## Implications for Commonplace

- The current note [skills derive from methodology through distillation](../../notes/skills-derive-from-methodology-through-distillation.md) is directionally right and already allows artifact-sourced skills, but does not treat evaluation traces, trigger tuning, and product constraints as equally central source material.
- A stronger formulation: skills can derive from methodology notes *or* directly from workshop evidence; the common operation is distillation from a larger operational substrate.
- Skill creation itself looks like a missing workshop template. A good workshop packet would likely include:
  - source prompts/examples
  - trigger hypotheses
  - eval prompts
  - benchmark deltas
  - failure cases
  - repeated helper-script candidates
  - final extracted skill

## Open questions

- How much of this difference is product philosophy versus product maturity?
- Is Codex under-specifying evaluation, or deliberately separating evaluation from skill creation?
- Should a Commonplace skill-creation workshop explicitly model both axes: artifact distillation and evaluation distillation?
- Does a mature skill always need an adjacent workshop history, even if only the final `SKILL.md` is shipped?
