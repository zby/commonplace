---
description: Empirical study (N=112) finding experienced developers control AI agents through SE practices, not vibe coding -- grounds constraining, underspecification, and programming-practices-transfer arguments
source_snapshot: professional-software-developers-dont-vibe-they-control.md
ingested: 2026-03-09
type: scientific-paper
domains: [agentic-coding, developer-practices, task-suitability, human-ai-collaboration]
---

# Ingest: Professional Software Developers Don't Vibe, They Control

Source: professional-software-developers-dont-vibe-they-control.md
Captured: 2026-03-09
From: https://arxiv.org/html/2512.14012v1

## Classification

Type: **scientific-paper** -- mixed-methods empirical study with field observations (N=13) and qualitative survey (N=99), published as arXiv preprint (2512.14012v1, Dec 2025). Includes structured methodology, thematic analysis, and systematic task suitability coding (89 task codes from 189 raw mentions).

Domains: agentic-coding, developer-practices, task-suitability, human-ai-collaboration

Author: Ruanqianqian (Lisa) Huang, Avery Reyna, Sorin Lerner, Haijun Xia, Brian Hempel (UC San Diego). Xia and Lerner are established HCI/PL researchers; this is a well-resourced academic team with access to professional developer populations through GitHub scraping of top agentic tool repos.

## Summary

Huang et al. investigate how experienced professional developers (3+ years) actually use AI coding agents, through 45-minute field observations and a broader qualitative survey. The central finding is that professionals do not "vibe code" -- they carefully control agents through planning, explicit prompting with rich context, step-by-step supervision, and established software engineering practices (testing, version control, code review). Developers average only 2.1 agent steps per prompt, maintain design authority, and review most generated code. Task suitability maps cleanly to complexity: agents excel at straightforward, repetitive, and scaffolding tasks but fail at business logic, complex reasoning, and domain-specific work. No respondent believed agents could replace human decision-making. The paper positions developer expertise -- not AI capability -- as the binding constraint on effective agent use.

## Connections Found

`/connect` discovered 12 connections (6 strong, 6 moderate), plus 1 complementary source.

**Strong connections (empirical grounding for existing theory):**

- **[programming-practices-apply-to-prompting](../notes/programming-practices-apply-to-prompting.md)** -- *grounds*: the paper's central finding is large-scale empirical evidence for this note's theoretical argument. Quote S88 ("I prompted by applying the lessons of software engineering to narrative") is a direct statement of the thesis.
- **[agentic-systems-interpret-underspecified-instructions](../notes/agentic-systems-interpret-underspecified-instructions.md)** -- *grounds*: "vague prompts will not work" (12/13 observations, 43/99 survey) is empirical confirmation that underspecification is the practical problem.
- **[constraining](../notes/constraining.md)** -- *exemplifies*: developer control strategies (user rules, plan files, testing, version control) map directly onto the constraining spectrum from partial narrowing to full commitment.
- **[methodology-enforcement-is-constraining](../notes/methodology-enforcement-is-constraining.md)** -- *exemplifies*: Table 2 shows an enforcement gradient in practice -- instruction-layer rules through structured prompts to verification hooks.
- **[deploy-time-learning-the-missing-middle](../notes/deploy-time-learning-the-missing-middle.md)** -- *exemplifies*: plan files, context files, and user rules are deploy-time learning artifacts -- durable, inspectable adaptations persisting across sessions.
- **[constraining-during-deployment-is-continuous-learning](../notes/constraining-during-deployment-is-continuous-learning.md)** -- *exemplifies*: developer control strategies are empirical evidence that constraining during deployment constitutes continuous learning.

**Moderate connections:** [context-efficiency](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) (avg 2.1 steps/prompt as behavioral evidence of context as binding constraint), [oracle-strength-spectrum](../notes/oracle-strength-spectrum.md) (task suitability maps to verification cost), [bounded-context-orchestration-model](../notes/bounded-context-orchestration-model.md) (developers act as symbolic scheduler driving bounded calls), [inspectable-substrate](../notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) (partial tension: supervision *over* inspectable substrate is the actual pattern, not substrate alone), [writing-styles](../notes/writing-styles-are-strategies-for-managing-underspecification.md) (prompting strategies instantiate the five writing styles informally), [legal-drafting](../notes/legal-drafting-solves-the-same-problem-as-context-engineering.md) (S88's prompting style reads like a legal brief).

**Complementary source:** [context-engineering-ai-agents-oss](context-engineering-ai-agents-oss.md) triangulates the same phenomenon from the artifact side (466 AGENTS.md files) while this paper examines the behavioral side.

**Key insight:** This paper is primarily an empirical grounding source -- it validates several theoretical positions already in the KB rather than introducing new concepts. The value is evidential weight, not novel framing.

## Extractable Value

1. **Empirical validation of SE-to-prompting transfer** -- S88 quote and the finding that 65/99 respondents cite existing SE expertise as their primary strategy for agent effectiveness. Direct citation for [programming-practices-apply-to-prompting](../notes/programming-practices-apply-to-prompting.md). [quick-win]

2. **Task suitability data as oracle-strength test set** -- Table 4 contains 89 task codes with suitable/unsuitable ratings from 99 developers. This is testable data: map each task code against oracle strength (verification cost) and check whether the correlation holds. If it does, it validates oracle-strength as a practical predictor. [experiment]

3. **Developer control strategies as empirical constraining taxonomy** -- Table 2 documents the specific mechanisms (plan files, context files, user rules, iterative prompting, testing, version control, code review) with participant-level detail. These map onto the constraining spectrum but have not been systematically aligned. A synthesis note could argue that developers independently rediscover constraining. [deep-dive]

4. **Supervision-over-substrate as the actual pattern** -- 69% of participants reviewed every change, but they did so via inspectable artifacts (code diffs, test output, version control). This nuances the inspectable-substrate note: in current practice, substrate enables supervision rather than replacing it. [experiment]

5. **2.1 steps/prompt as context-efficiency behavioral data** -- developers self-limit agent autonomy to tiny chunks, which is direct behavioral evidence that practitioners treat context as the binding constraint. Useful data point for [context-efficiency](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md). [quick-win]

6. **"Vague prompts will not work" with sample size** -- 12/13 observations + 43/99 survey respondents independently confirm that clear context and explicit instructions are necessary. This is the strongest empirical support in our source collection for the underspecification thesis. [quick-win]

7. **Planning controversy as an open question** -- the 13:23 split on whether agents should be used for high-level planning is interesting because it maps to a boundary our KB hasn't explored: at what point does task complexity exceed the oracle-strength threshold for agent delegation? The disagreement may reflect different oracle-strength thresholds in different developer contexts. [just-a-reference]

## Limitations (our opinion)

**What was not tested:**

- **No performance measurement.** The paper reports developer perceptions and self-reported strategies, not objective productivity data. The authors themselves note that Becker et al. found a 19% *slowdown* with AI use in a randomized trial. Whether the control strategies described here actually improve outcomes is unknown -- developers may be confabulating post-hoc rationalizations for their habits.

- **Single 45-minute observation window.** The field observations capture one session per developer. Longitudinal patterns -- how strategies evolve, which get abandoned, how plan files accumulate or decay -- are invisible. The deploy-time learning connection (strategies as durable artifacts) is inferred but not observed across sessions.

- **Severe gender imbalance.** 97/99 survey respondents and 12/13 observation participants were male. The paper acknowledges this but does not discuss whether control-oriented strategies might be culturally or dispositionally inflected.

- **Selection bias toward agent enthusiasts.** Recruitment via GitHub users of top agentic tool repos selects for developers who already use and presumably like agents. The paper's positive sentiments (5.11/6 enjoyment) may not generalize to the broader developer population.

- **No comparison with novice developers.** The paper studies only experienced developers (3+ years). Without a novice control group, the claim that expertise drives control strategies rather than vibing is observational, not causal. We know experts control; we don't know whether novices who try to control do equally well.

- **Strategies described, not evaluated.** Plan files, user rules, and context files are documented as things developers do, but the paper doesn't assess which strategies are more effective than others, or under what conditions. The KB's constraining spectrum offers a theoretical ordering, but this paper provides no evidence for or against that ordering. See [constraining](../notes/constraining.md) for the theoretical framework that would need empirical testing.

- **Task suitability is self-reported, not benchmarked.** The 89 task codes come from what developers *say* agents are good/bad at, not from controlled experiments. Developers may systematically under-estimate agent capability for familiar tasks (where their own expertise makes the agent feel slow) and over-estimate it for unfamiliar tasks (where they can't evaluate the output quality). This matters for the oracle-strength mapping -- the correlation might be between perceived verification cost and suitability rather than actual verification cost and actual capability.

## Recommended Next Action

Write a note titled "Experienced developers independently rediscover the constraining gradient" connecting to [constraining](../notes/constraining.md), [methodology-enforcement-is-constraining](../notes/methodology-enforcement-is-constraining.md), and [programming-practices-apply-to-prompting](../notes/programming-practices-apply-to-prompting.md). The note would argue: the paper's Table 2 documents developers progressing from user rules (convention) through plan files (structured artifact) to testing and version control (commitment/verification) -- which is the constraining spectrum observed in the wild. The evidence is behavioral, not self-reported taxonomy, which makes it stronger than if developers were merely naming the concepts. The note should also flag the key limitation: the ordering is inferred from cross-sectional observation, not from longitudinal tracking of individual developers' strategy evolution.
