---
description: "AIDE2 finds transferable research-agent harness improvements, but its separate evolved-improver test remains inconclusive; bounded context and an inactive selection rule sharpen causal limits."
source: https://arxiv.org/abs/2609.26457
captured: "2026-09-24"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: aff09b81c1e6199f6e66b9f7c89889e8fe469c635a06bac1a24cb04b80f16600
ingested: "2026-09-25"
type: ingest-report
domains: [self-improving-systems, context-engineering, agent-evaluation]
learning_claims: true
---

# Ingest: AIDE2 — Recursive self-improvement of AI research agents

## Classification

An empirical research preprint presenting a two-loop harness optimization system, benchmark comparisons, an evolved-improver experiment, and analysis of accepted and rejected rewrites. Dhruv Srikanth, Bingchen Zhao, Dixing Xu, Yuxiang Wu, and Zhengyao Jiang are affiliated with Weco AI, which develops the production agent used as both the outer proposer and a comparison baseline. Their implementation experience supports the engineering account; the outcome evidence remains the authors' evaluation of their own system.

## Summary

[AIDE2](https://arxiv.org/abs/2609.26457) searches research-agent harness code while keeping model weights fixed. A human-engineered outer agent proposes rewrites; candidate inner agents optimize code using public feedback, and hidden scores of their returned solutions determine which rewrite becomes the next incumbent. An eight-day run accepts seven of 99 proposals, raising its selection grade from 0.703 to 0.778. Two evolved checkpoints improve over the initial agent on four held-out benchmarks, including one weather-model optimization task. These are gains from cumulative harness changes under fixed per-benchmark constraints, not isolated effects of context compression, search policy, or any other component. The discovered harness bounds prompt history and changes exploration; one purportedly robust selection rule never changes the selected candidate in replay. Crucially, the paper separately tests the evolved agent as the outer improver: three seeds per arm yield similar mean endpoints and do not establish better self-improvement efficiency. The source supports transferable harness optimization more strongly than improvement in the process that produces those gains.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper supplies evidence for [compounding needing later-improvement tests](../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md). Its main run accumulates successful rewrites while the human-engineered outer proposer remains fixed. The separate “ignition test,” which asks whether an evolved agent improves agents more effectively, holds the starting inner agent fixed and varies the outer agent. Its inconclusive result prevents the task gains from being treated as demonstrated feedback into better improvement production; it does not establish that such feedback is absent.

The bounded prompts provide a concrete comparison with [context efficiency](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md). The initial harness loads whole histories and sometimes exhausts its context window; the evolved harness uses bounded summaries and avoids those observed failures. The measurements distinguish a feasibility failure from prompt-size savings, but cumulative rewrites prevent attributing all task gains to compression. The source also sharpens [the limit imposed by the experimental contrast](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md): replay shows a named robustness penalty preserving candidate order and never changing the returned solution. That specific rule cannot explain improvement through changed final selection in those runs, even though the overall harness performs better.

## Learning Claims (our opinion)

On the source's terms, recursive self-improvement means that the next rewrite edits the agent retained from the preceding selection step. Persistence is in executable harness code rather than updated model weights. The outer agent reads earlier candidates and grades and inspects evaluation artifacts; it can change the inner agent's search, memory, and return policy. Accepted changes therefore alter what later inner runs do, and external benchmark gains support improved task-solving capacity within the reported regimes.

Against the [theory-builder](../notes/definitions/theory-builder.md) conditions, the harness code is localized content (condition 1), and inner runs consume it (condition 2). The outer agent states reasons for its rewrites, including diagnosed failures, and its evaluator repair names a specific flaw. That shows content-directed criticism in selected cases, although acceptance itself is argmax selection on the grade over whole variants; condition 3 is shown only at that trace strength, and it decides the verdict. Condition 4 (iteration) is met: each rewrite starts from the retained agent and the earlier candidates, grades, and diagnoses. Where the traces show criticism aimed at what a harness says, the run is a theory builder at that trace strength; where acceptance is by grade alone, it is trial and error. Persistence reaches the rounds of one run: the 99 steps revise one harness against one fixed selection suite and grade. The held-out benchmarks evaluate frozen checkpoints, which ends that builder rather than extending it. The ignition test reuses an evolved agent as the improver on the same optimization problem from a fresh start, set up by the experimenters, and the paper leaves promotion to the outer loop as a proposed rule, not a performed step, so no higher grade is shown. The capacity gains are a separate learning claim. The inactive selection penalty also shows that a retained rationale does not establish that the rationale governs the successful behavior.

The effective update space is broad within the inner harness but bounded outside it. The main run keeps the outer proposer, outer argmax acceptance rule, task families, grade aggregation, budgets, and models fixed. Inner policies are searched; these surrounding choices are not compared with alternative decompositions. As [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) predicts, success establishes that this configuration supports useful adaptation, not that its fixed boundaries are necessary or best. The reported repair to a scoring script also means the accepted changes cannot all be described as pure search-policy improvements.

The ignition test changes the improver while starting both arms from AIDE47. Across three 50-step runs per arm, AIDE47 and the human-engineered outer agent reach mean grades of 0.780 and 0.782. An earlier apparent plateau in the treatment mean does not resolve the variance. This is a useful attempt to test improved improvement production, but it demonstrates neither superiority nor equivalence, sustained compounding, or accelerating returns.

## Extractable Value

1. **Separate successful retention, transfer, and better improvement production.** The held-out gains and inconclusive ignition comparison offer a concrete case for the existing compounding note. Keep the initial inner agent equal when comparing improvers; task performance after bundled harness rewrites cannot substitute for that comparison. This experimental distinction transfers beyond code optimization. [quick-win]

2. **Check whether an accepted mechanism changes the decision it is supposed to improve.** The robustness penalty's replay preserves every selected candidate. Such a check can rule out a proposed causal path without requiring an expensive full component ablation. It does not rule out other robustness mechanisms or explain the bundle's benefit. [quick-win]

3. **Treat bounded history as a specific context-management candidate.** AIDE85 uses role-specific root/recent summaries and injects up to three deduplicated error signatures when the bug rate reaches 15%. End-of-run per-call character reductions versus AIDE0 reach roughly 7× on MLE-Bench, over 40× on weather, and 50× on ALE/FML. These descriptive savings and avoided context failures motivate a matched Commonplace experiment; the paper's bundled harness comparisons do not isolate their contribution to task quality or establish total monetary savings. [experiment]

4. **Measure proxy gains after integration.** On 38 kernel/training-context pairs, the reported mismatch rate falls from 55% to 32% across the evolved lineage, versus 39% for the human baseline. A case counts when isolated speedup exceeds 1.02× but less than half survives in training, or integration crashes. The reusable contribution is this downstream check; the observed reduction is specific to cumulative harness rewrites and this endpoint. [just-a-reference]

## Limitations (our opinion)

The private grade is hidden from each inner search but visible to, and repeatedly reused by, the outer search. It is a selection signal, not an untouched final evaluation. Separate external benchmarks address transfer, while noisy grades still permit false acceptance. Two additional full runs accept two and four changes, but the detailed external comparisons concern two checkpoints from the highlighted lineage. The three-seed ignition experiment lacks external evaluation of each seed's final agent and cannot establish a superior improver.

AIDE0 is deliberately pared down and concatenates full history. Fixing that concrete weakness is a simpler explanation for part of the gain than a general breakthrough in recursive improvement. The production baseline strengthens the comparison, but its margins on FML-Bench are small relative to reported standard errors. ALE and MLE use lite subsets; the weather result covers one task and measures gain over a starting dynamical core, not an absolute WeatherBench leaderboard score. ALE/MLE/weather have dollar caps as well as other constraints, whereas FML and kernel tasks use step caps; equal steps do not establish equal total cost. Models differ across benchmarks but stay fixed within each comparison.

No component ablations identify which accepted changes caused the outcome gains or reduced kernel mismatch. The fixed outer architecture is not compared with alternative evidence representations or acceptance rules. The rejected-method appendix concerns particular proposals, with several deltas within run variability; it does not establish that the associated method classes fail. Likewise, kernel mismatch measures a specific proxy failure rather than deceptive intent or general safety. This ingest neither inspected implementation code nor reproduced experiments, so mechanism details and outcomes remain paper-reported.

## Recommended Next Action

Update [Compounding is tested in later improvement, not by the accepting metric](../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) with AIDE2's ignition comparison as an inconclusive later-improvement test alongside demonstrated task transfer, keeping the shared starting agent, three-seed limit, and missing external endpoint evaluations explicit.
