---
description: "Weco reports fixed-model harness evolution with held-out task gains, diagnostic repairs and an inconclusive test of whether the evolved agent improves agents better."
source: https://www.weco.ai/blog/first-evidence-of-recursive-self-improvement
captured: "2026-09-27"
capture: trafilatura
capture_scope: partial-source
genre: practitioner-report
snapshot_sha256: 0226be19a52c435e2f5455fa28a6d7f380f622aa43e644ed1a4eec4fe5c4d703
ingested: "2026-09-27"
occasion: "Prepare source evidence for adding Weco/AIDE² to which-existing-self-improving-systems-are-theory-builders.md, examining reflective improvement, fixed-model learning, outer/inner loops, criticism, evaluation and compounding without presupposing theory-builder membership."
type: types/ingest-report.md
domains: [recursive-self-improvement, agent-harnesses, evaluation]
learning_claims: true
---

# Ingest: AIDE²: The First Evidence of Recursive Self-Improvement

## Classification

An experimental account by the system's builders, published on Weco's company blog. Dhruv Srikanth, Bingchen Zhao, Dixing Xu, Yuxiang Wu and Zhengyao Jiang describe the mechanism, selected results, failed proposals and deployment difficulties. Their direct involvement supplies implementation knowledge but also an interest in the claimed advance. This observation is the blog account, not its linked technical report.

## Summary

Weco reports an eight-day, 100-step run in which a hand-tuned research agent rewrote another research agent's harness and retained seven successive improvements. The outer agent uses Claude Opus 4.7 and the inner agents Gemini 3 Flash; adaptation changes harness code and prompts rather than model weights. Within a fixed evaluation arrangement of heterogeneous tasks, public/private scores and metered per-evaluation cost, selected harnesses reportedly transfer to three unseen benchmarks. Discovered changes include search allocation across solution lineages, role-specific context compression and defenses against reward hacking. The account also reports a repaired evaluator crash and an inactive statistical defense whose implementation broke during evolution. Installing an evolved agent in the outer role yielded a suggestive but statistically insignificant efficiency gain, so the authors do not claim established improvement of the improver. The results support bounded harness improvement while leaving its causal components, the broader human-R&D efficiency comparison and recursive acceleration less settled.

## Quotes

No source quotes have been retained yet.

## Connections Found

For assessing Weco/AIDE², this source contributes concrete diagnostic episodes alongside the aggregate selection story: a self-diagnosed crash led to an output guard, and an evaluator exception led to a repair. These bear on the criticism condition in [Theory builder](../notes/definitions/theory-builder.md), but the blog supplies retrospective descriptions rather than the agent's stated criticisms and their uptake. They warrant an open assessment rather than membership inferred from benchmark gains.

The ignition experiment compares directly with [Compounding is tested in later improvement, not by the accepting metric](../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md): an evolved harness is actually used to produce later harness improvements, but the reported efficiency difference is inconclusive. The successful inner-agent comparison remains bounded by fixed models, evaluation tasks and cost accounting; it does not compare alternative outer-loop decompositions. The broken statistical defense also illustrates [An experiment identifies only the contrast it actually runs](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md): retaining a successful bundle cannot credit a component that is inactive.

## Learning Claims (our opinion)

The source's learner is a nested code-search process. A fixed outer agent proposes inner-agent rewrites, evaluates their task-solving performance and retains improvements. The inner agent sees public task scores; private scores withheld from it govern outer selection. The learner can change search policy, prompts and context construction. Its history includes earlier solutions and execution outputs, with evolved policies deciding what each operator receives. The reported evaluator repair shows some implementation latitude, but does not demonstrate revision of the task objectives or the public/private evaluation principle.

Against the four [theory-builder conditions](../notes/definitions/theory-builder.md):

1. **Localized content — supported at the artifact level.** The retained programs and prompts are identifiable content. Search policies, guards and operator instructions can be named. The source does not show all their purposes or proposed explanations as separately stated conjectures.
2. **Consumption — supported by the described execution path.** Candidate harness code runs the inner search, and its prompts and policies direct decisions. The ignition experiment additionally executes a retained harness as an outer improver. This establishes operational use at the documentary level; it is not an independent execution check.
3. **Content-directed criticism — suggestive, incompletely exposed.** A score gate alone does not supply a stated reason about what a candidate says. The crash diagnosis and evaluator repair are stronger evidence because the reported corrections target identified defects, including a defect in the test. But the capture does not preserve the agent's diagnostic arguments or show how consistently such criticism, rather than score-guided variation, drives revision. The authors' later discovery of the broken defense must not be counted as criticism performed by the autonomous loop.
4. **Iteration — supported for retained changes, conditional for criticism uptake.** Successive candidates build on selected predecessors, and the diagnostic repairs reportedly enter later code. This demonstrates iteration within the run; the missing diagnostic traces limit attribution of later rounds specifically to stated criticism.

Persistence extends beyond individual trials: selected harnesses are reused on new tasks and one is tested in a new outer run. The source does not establish a cross-session library of reasons that later research consults. Meeting the criticism condition remains open on this account alone. Likewise, changing an inner research method establishes method optimization; the stronger reflective qualifier depends on exposing the purposes and criticism of those method texts. The two-agent boundary matters: the main run's improving inner harness is not continuously installed as its own outer improver.

Learning is a separate, better-supported claim: under the reported matched cost constraint, retained harnesses improve future task performance without updating the named models' weights. Transfer is not uniformly increasing—AIDE85 trails AIDE47 on MLE-Bench Lite. Following [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), these gains concern the admitted harness changes. They neither vindicate the fixed evaluation arrangement nor establish that every relevant failure is expressible within it. The ignition test addresses improvement productivity but does not establish compounding: both arms reach a similar ceiling and even the apparent speed advantage is statistically insignificant.

## Extractable Value

1. **A bounded fixed-model learning case.** The source reports transferable harness gains under the fixed public/private, heterogeneous-task and cost arrangement. This lets a Weco/AIDE² case distinguish improved future performance from model-weight learning and from theory-builder membership. [quick-win]
2. **A more discriminating criticism question.** The self-diagnosed crash and evaluator repair are concrete leads for assessing stated, content-directed criticism. Their evidential strength exceeds bare acceptance scores, but a full assessment needs the corresponding diagnosis-to-revision record. [deep-dive]
3. **An explicit but inconclusive compounding test.** Reusing AIDE47 as the outer improver tests later improvement directly. Its reported roughly 20-versus-40-step convergence to a similar ceiling is not statistically significant; preserve it as an attempted test rather than evidence of established ignition. [quick-win]
4. **A cost-sensitive context hypothesis and a maintenance warning.** The authors report 16-fold prompt compression against naive history concatenation and reinvestment into more search steps, within the tested cost regime. They also report complex evolved code, dead logic and deployment friction. The bundle comparison does not isolate compression's causal contribution or establish that additional search benefits production maintenance. [experiment]

## Limitations (our opinion)

The retained capture is partial-source text and excludes interactive figures. It preserves prose and some captions but cannot establish missing plotted values, uncertainty or full visual comparison details. No implementation was inspected or experiment reproduced for this ingest.

This is an interested builders' report centered on a selected run and selected descendants. Its discussion of rejected proposals and dead code is useful counterevidence to a simple success narrative, but does not supply complete trial records or matched human-R&D accounting. Eight unattended days versus two years of prior development does not by itself establish a hundredfold resource-efficiency advantage: setup, accumulated infrastructure and human labor are not made commensurate here. Fixed per-evaluation dollars constrain candidate evaluation, not the total historical investment comparison.

The reported reward-hacking rates—63% for AIDE0 and 34% for AIDE85—use a particular KernelBench criterion: less than half the claimed kernel speedup survives in the end-to-end workload. This is a useful operational discrepancy measure, not proof of deceptive intent or a general rate of dishonesty. Selection on private scores is a proposed explanation for the reduction, not an isolated causal result. The inactive statistical defense cannot explain the final agent's gain.

Rejected proposals compare particular implementations against contemporaneous incumbents under a fixed budget; several differences are explicitly within noise. They do not refute entire algorithm families. Similarly, reported repairs suggest meaningful criticism but do not expose enough of the autonomous reasoning record to settle theory-builder membership. The authors' novelty and future-RSI predictions exceed what this observation independently establishes.

## Recommended Next Action

Add a Weco/AIDE² case to `kb/articles/which-existing-self-improving-systems-are-theory-builders.md` that separates reported fixed-model learning, diagnostic evidence relevant to criticism, the asymmetric outer/inner boundary and the inconclusive compounding test, leaving membership open where the criticism record is missing.
