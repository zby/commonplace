---
description: "Harness-IF makes rule withholding a compliance baseline, finding 3.6–7.4-point prior-alignment inflation while leaving most surface effects unpaired"
source_snapshot: "harness-if-instruction-following-across-instruction-surfaces.md"
ingested: "2026-08-18"
type: kb/sources/types/ingest-report.md
domains: [instruction-following, agent-evaluation, harness-engineering, llm-reliability]
---

# Ingest: Harness-IF: Evaluating Instruction Following Across Instruction Surfaces in Coding Agents

Source: [harness-if-instruction-following-across-instruction-surfaces.md](./harness-if-instruction-following-across-instruction-surfaces.md)
Captured: 2026-08-18
From: https://arxiv.org/abs/2608.11727

## Classification

Genre: scientific-paper -- an arXiv v1 preprint that defines a rule-level coding-agent benchmark and reports a 12-build coding panel, a separate nine-build conflict pilot, and an exploratory non-coding extension.
Domains: instruction-following, agent-evaluation, harness-engineering, llm-reliability
Author: Zining Huang et al., primarily ByteDance Seed with Tsinghua University and Peking University affiliations. The paper reports substantial internal experiments and sensitivity analyses, but it is a new preprint whose planned benchmark release is not yet linked in this version.

## Summary

Harness-IF evaluates whether coding agents follow individual operational rules delivered through system prompts, tool descriptions, skill descriptions, project files, and user instructions. Its main panel places 302 rules across 60 multi-turn coding items, scores 256 of them from traces, diffs, tests, output, and artifacts, and produces 37,616 pass/fail verdicts across 12 model builds and three rounds. Its central control is Against-Prior Accuracy (AP-Acc): withhold a target rule to estimate whether unprompted behavior already aligns with it, then score the against-prior subset separately. Every build scores lower on AP-Acc than on aggregate accuracy, by 3.6–7.4 points. A distinct counterbalanced pilot over four synthetic conflicts reports pooled precedence `system prompt / project file / user instruction > tool description > skill description`, while the main panel's per-surface rates remain descriptive rather than causal.

## Connections Found

This paper is the strongest current empirical anchor for distinguishing behavior caused by an instruction from an output that merely matches it. The withheld-rule probe qualifies [LLM output deviation requires three-way diagnosis](../notes/llm-output-deviation-requires-three-way-diagnosis.md): a passing output does not by itself show that the specification moved the interpreter, while the paper's AP-Acc stratification still does not provide a paired injection-effect estimate. Its controlled relocation pilot supplies a surface-level instance of [systematic prompt variation as diagnosis](../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md) and evidence that [the deployed system, not the model alone, determines behavior](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md). It also turns the descriptive surface inventory in [Always-loaded context mechanisms in agent harnesses](../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) into an evaluated dimension. As a source comparison, [Harness Updating Is Not Harness Benefit](./harness-updating-is-not-harness-benefit.ingest.md) separates loading, judged procedural match, and downstream gain, whereas Harness-IF adds a withheld-rule control for prior-aligned behavior.

## Extractable Value

1. **Prior-control stratification reduces coincidence in a compliance score** -- Withholding the target rule supplies evidence about whether the agent would already behave that way. Restricting evaluation to against-prior rules lowers every model's score, and the varying 3.6–7.4-point gap shows that prior alignment does not cancel in model comparisons. Because AP-Acc compares rule strata rather than matched present-versus-absent opportunities, it does not estimate the injected rule's causal effect. [quick-win]

2. **Rule-level execution evidence prevents final task success from standing in for instruction following** -- One verdict per applicable atomic rule, grounded in traces, diffs, tests, output, and artifacts, preserves failures that a task-level pass would collapse. This is a concrete instrument adjacent to the proposed [trajectory-aware evaluation of transforming workflows](../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md), although Harness-IF does not run that proposal's paired output-only control. [experiment]

3. **Surface relocation is a diagnostic intervention, not a descriptive slice** -- The E0 pilot holds rule meaning and task structure fixed, counterbalances conflict direction, and varies the two delivery surfaces. That design can identify precedence within its tested conflicts; the main panel's assigned placements cannot. The distinction is a useful protocol rule for future agent-surface evaluations. [experiment]

4. **Failure mass must be separated from failure propensity** -- Shortfall rules account for 77.1% of failures, but they also account for most eligible opportunities and fail at 23.8% versus 20.8% for overstep rules. Grouping from declared rule modality instead of free-text judge explanations makes the decomposition reproducible and blocks the mistaken claim that agents are intrinsically much more omission-prone. [quick-win]

5. **Judge dependence can dominate an otherwise large benchmark** -- 86.8% of eligible verdicts involve the LLM judge. On 116 paired clean verdicts, a judge swap yields 62.1% agreement and Cohen's κ of 0.163; the older human-reference audit used a different five-vote configuration. The paper's common-support and item-clustered analyses stabilize the broad prior-alignment direction, but not adjacent model ranks. [just-a-reference]

## Limitations (our opinion)

The fixed-decomposition boundary is consequential. Agents can condition behavior on the assembled instruction stack, repository state, multi-turn history, and tool or test feedback; they can compose tool calls, commands, file edits, and final output; and a fixed model-plus-harness maps those signals to actions. The rule taxonomy, scenarios, fixtures, admissible surfaces, surface phrasings, tools, turn budget, model weights, item selection, prior-label process, and scoring machinery stay outside that effective update space. The results show discrimination within this compound design. They do not validate the rule taxonomy or show that the chosen surfaces and task decomposition are complete or preferable, as [learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md).

Most headline surface comparisons are not controlled. The main panel assigns each rule to one admissible surface, so rule family, wording, prior class, opportunity, and placement can co-vary; all user-instruction placements are against-prior. Only E0 relocates rules, and it covers four synthetic style conflicts, 916 runs, and nine older builds. Its full ordering appears in only six of nine individual-build fits, and the retained collection ran one conflict direction before the other. It supports a pooled tendency under those conflicts, not a universal instruction hierarchy or a causal reading of the main panel's per-surface rates.

AP-Acc also inherits imperfect label provenance. A recoverable nine-build zero-injection consensus covers 287 of 642 rules; other labels come from prior curation or unknown lineage, and 12 final labels disagree with recoverable consensus without a preserved override reason. Five probe identifiers overlap the evaluated panel, so no zero-injection label is fully independent of it. Threshold sweeps and positive gaps on the seven builds absent from the probe cohort make the direction credible, but not provenance-free.

Finally, the v1 paper promises rather than links the public package, so this ingest did not reproduce the reported benchmark, training-free recomputation, or judge-swap analysis. Item selection used observed quality and discriminativeness and may favor the evaluated models; the source is English- and software-engineering-centered; and most verdicts depend on a judge whose swap sensitivity is large. These boundaries support the cross-model prior-alignment finding more strongly than the exact accuracy levels or leaderboard order.

## Recommended Next Action

Folded into [An experiment identifies only the contrast it actually runs](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md), where the withheld-rule design supplies the simple missing-comparison case alongside bundle attribution and adjacent unrun treatments.

---

Relevant Notes:

- [An experiment identifies only the contrast it actually runs](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — abstracted-from: the zero-injection design shows why behavior matching a supplied rule does not by itself identify the rule's effect
