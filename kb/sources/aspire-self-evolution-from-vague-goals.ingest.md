---
description: "Aspire separates agent-chosen learning proxies from hidden outcome tests, finding sparse retained gains and narrow-validation failures within fixed evolution interfaces."
source: https://arxiv.org/abs/2608.31111
captured: "2026-09-24"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 05a1bedd050690600e92826bcc5b24247ad52d00166edc9c2d203678215d7155
ingested: "2026-09-25"
learning_claims: true
type: kb/sources/types/ingest-report.md
domains: [self-improvement, goal-operationalization, evaluation, agent-harnesses]
---

# Ingest: Aspire: Can Models Self-Evolve from Vague Goals?

## Classification

This scientific preprint introduces a benchmark, specifies its evaluation protocols, and reports weight-update and harness-editing experiments with trajectory analysis. Authors: Yuhao Wu, Jingyuan Zhang, Jiajun Shi, and collaborators affiliated with ByteDance Seed, Singapore University of Technology and Design, M-A-P, and TokenWave.AI. The benchmark designers also conduct and interpret the experiments; this is primary experimental reporting, not independent replication.

## Summary

Aspire asks agents to turn broad capability goals into data choices, update plans, and validation criteria while hiding the tasks used to measure success. Its six-goal evaluation contains 520 expert-authored items. Within a managed action interface, weight experiments change candidate weights while keeping the decision model, harness, controller, and evaluator fixed; harness experiments hold runtime weights fixed. In 24 final-only weight runs, three final checkpoints exceed their base scores. In a separate adaptive-feedback design, only one of 30 configuration–goal cells retains an eligible above-base checkpoint, selected using repeated scores from the same evaluation slice. All three valid one-step harness successors score numerically below the Qwen-Agent reference on the writing goal. The strongest contribution is the distinction between executing an update loop and improving its intended capability: narrow self-validation can reward a proxy, later checkpoints can recover from damage while staying below the base, and rollback can guarantee nonnegative retained scores without showing that attempted updates worked.

## Quotes

No source quotes have been retained yet.

## Connections Found

Aspire supplies a concrete empirical case for [A proximate target is checked for achievement, not for warrant](../notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md). In one harness-creation trajectory, a five-part answer template raises an agent's checklist result from 7/8 to 8/8 and passes two similar prompts, yet inspected hidden tasks show it recasting requests for technical content as study-design questions. Within the fixed Qwen3.5-4B runtime and writing evaluation, the resulting harness has a 19.32 task-macro mean against the reference's 28.64. This is case evidence for a proxy mismatch, not an isolated causal estimate of template use or a general failure rate.

The source also sharpens [the need to declare an improvement objective](../notes/self-improvement-is-relative-to-a-declared-objective.md): progress against the last checkpoint, the initial base, the agent's own criterion, and the external goal measure are different comparisons. Its adaptive protocol illustrates the boundary discussed in [Generalization in Adaptive Data Analysis and Holdout Reuse](./generalization-adaptive-data-analysis-holdout-reuse.ingest.md). Hidden items can still influence candidate selection through repeated aggregate scores; Aspire explicitly treats that protocol as adaptive selection, without claiming an untouched confirmation test or a formally valid reusable-holdout guarantee.

## Learning Claims (our opinion)

The source's mechanism is goal operationalization followed by bounded search. An agent chooses data and learning signals, launches weight updates or edits a harness, evaluates its own proxies, and decides whether to continue or branch. Detailed feedback concerns its own validation data. Official feedback is either absent until final submission or limited to aggregate scores. Candidate weights or harness versions persist; controller selection determines which eligible weight checkpoint is retained.

Against the [theory-builder](../notes/definitions/theory-builder.md) conditions, the two arms differ. The weight arm fails condition 1: the revised theory is the weights, where no unit says anything. The harness arm has localized content that the runtime consumes (conditions 1 and 2), and it shows stated criticism in selected cases: Terra removes a reviewer after it fabricates statistical results, and Sol rejects variants for hallucination, latency, or tool-control failures (condition 3, at trace strength; aggregate-score selection alone would not meet it). Condition 4 (iteration) is met for the harness arm: rejected variants and their stated failures shape the next candidate. The harness arm is therefore a theory builder at the strength of those traces, with persistence across the rounds of one run; condition 3 is the weak point, and runs whose acceptance is by aggregate score alone would be trial and error. Each run builds one harness for one supplied goal; freezing and executing the successor ends that builder rather than extending it. The weight arm stays outside on condition 1. Improvement is a separate claim: lower hidden writing scores do not exclude a narrower gain, such as a repaired failure path, but they prevent treating these cases as gains on the reported goal measure.

The experiments also retain a consequential boundary of the kind described in [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md). Agents can revise their proxies and candidate states, but the supplied goals, official goal partitions, evaluator, action interface, budgets, and controller selection rules remain outside that search. Weight and harness changes are studied separately. The reported decision models remain fixed; optional promotion of a trained descendant between rounds is an interface capability, not an observed recursive replacement result. The failures do not establish that a needed correction was inexpressible, and the isolated gains do not validate these fixed design choices against alternatives. The source strengthens Commonplace's demand for outcome evidence distinct from completed revision activity without deciding whether retained theories would improve this search.

## Extractable Value

1. **A bounded witness of proxy achievement without goal improvement.** The writing-harness case shows how a strongly checked structural property can direct answers away from the requested content. Its value is the observable mismatch between checklist success and hidden-task behavior under one fixed runtime and one goal, extending the existing proximate-target note with a concrete case. [quick-win]
2. **Separate attempted, selected, and retained outcomes.** Aspire distinguishes raw candidate scores, the best evaluated candidate, the best eligible candidate, and the state retained after rollback. A nonnegative retained delta is guaranteed by the controller's selection rule; a rising lineage can remain below its initial base. This accounting is reusable when assessing Commonplace revision loops that preserve an incumbent. [quick-win]
3. **Keep selection evidence distinct from confirmation evidence.** The adaptive protocol's sole retained gain is mathematics, 17.86 to 20.10, on a slice repeatedly consulted during search. The final-only protocol provides a different evidence boundary: no intermediate official score, with three above-base checkpoints among 24 runs. Neither protocol alone establishes broad transfer or preservation of unrelated abilities. [just-a-reference]
4. **Training representation can undermine the intended response behavior.** Five final checkpoints trained on numeric-label MMLU data produce single-digit answers for all 279 corresponding evaluation outputs; four score zero and one scores 6.141. This is a concrete diagnostic warning about response-format mismatch within the supplied training interface, supported by traces rather than a randomized comparison of formats. [just-a-reference]

## Limitations (our opinion)

The benchmark measures six human-chosen goal slices, with the writing goal represented by only 20 top-level task bundles. An external evaluator provides a reading independent of the agent's own proxy, but its coverage and scoring remain another operationalization of the broad goal. The tests do not establish capability growth beyond those slices or preservation of unrelated capabilities.

Replication is limited. Each adaptive configuration–goal cell has one run; final-only model–goal pairs have two. Harness results come from one creation attempt per condition, followed by three executions of each valid frozen harness. Those executions measure runtime variation, not reproducibility of harness creation; per-execution dispersion is not reported. Content-level harness diagnoses inspect one execution per successor. The two final-only science runs both score 48.00, but disagree on 20 of 75 items, so matching aggregate scores do not establish stable item-level improvement.

The PostTrainBench comparison is descriptive: official system scores and vague-goal runs can differ in metadata beyond prompting. Matched trajectories support observations about resource allocation, not a prompt-only causal effect on performance. Likewise, numeric-label training, narrow checklists, and continued search have plausible failure mechanisms, but the paper does not isolate each through a controlled ablation. Poor proxy choice or answer-format damage can explain particular losses without establishing a general inability to operationalize goals.

The managed controller removes much infrastructure work, while the comparison keeps the permitted update methods, measurement interface, and component boundaries fixed. It does not compare joint model–harness evolution, alternative action spaces, or recursive replacement of the decision model. Adaptive selection lacks a separate confirmation slice, and content-bearing traces needed for item-level causal analysis are restricted. This ingest relies on the paper; no implementation was inspected and no experiment was reproduced. Training GPU-hour totals exclude inference, judging, deployment, and idle controller time, so they are not total search-cost estimates.

## Recommended Next Action

Add the narrow-checklist harness case to [A proximate target is checked for achievement, not for warrant](../notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md), retaining its one-creation, fixed-runtime, writing-goal, and selected-trace evidence boundaries.
