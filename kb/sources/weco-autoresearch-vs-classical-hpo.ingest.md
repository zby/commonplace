---
description: "Weco's NanoChat comparison reports advantages for code-editing AutoResearch over fixed-space Optuna, while leaving content-directed criticism and reflective improvement unestablished."
source: https://www.weco.ai/blog/autoresearch-vs-classical-hpo
captured: "2026-09-27"
capture: trafilatura
capture_scope: partial-source
genre: practitioner-report
snapshot_sha256: 439d705e3aa8a1fdefa2cc85996845c757a941e4e78dbed1d1dd88fb20aefe8f
ingested: "2026-09-27"
occasion: "Prepare source evidence for adding Weco/AIDE² to which-existing-self-improving-systems-are-theory-builders.md, examining reflective improvement, fixed-model learning, outer/inner loops, criticism, evaluation and compounding without presupposing theory-builder membership."
type: types/ingest-report.md
domains: [agentic-optimization, hyperparameter-search, evaluation]
learning_claims: true
---

# Ingest: AutoResearch vs Classical Hyperparameter Tuning

## Classification

A practitioner benchmark report by Zhengyao Jiang and Bingchen Zhao, published on Weco AI's blog on April 2, 2026. The authors describe their own three-seed NanoChat comparison and interpret its results. This is direct experimental reporting by participants, with a commercial interest in agentic optimization, rather than an independent replication.

## Summary

Weco compares AutoResearch's code-editing loop with Optuna's TPE search over 16 parameters chosen by Claude Code, starting from the same NanoChat baseline. Each evaluation trains for five minutes on one H100 and measures validation bits per byte (BPB). The authors report better sample efficiency, cost efficiency, and longer-training performance for AutoResearch in this setup. Approximately 78% of its improvement is attributed to changes within Optuna's parameter space; the remaining gains include previously unexposed constants and structural code edits. The comparison changes both proposal method and editable search space, so it does not isolate their contributions. The authors propose an LLM prior as an explanation for longer-horizon generalization, but do not test that mechanism independently. The retained text excludes interactive plots and leaves detailed effect sizes and statistical calculations unavailable.

## Quotes

No source quotes have been retained yet.

## Connections Found

For the proposed Weco/AIDE² case, this source supplies a bounded empirical comparison conducted by Weco, not evidence that AIDE² implements the measured loop: the evaluated system is AutoResearch. It provides a concrete comparison for [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md): Optuna cannot propose changes outside its supplied 16-parameter space, while a code-editing agent can expose additional constants and operations. The result remains specific to those search boundaries and does not establish superiority over an expanded Optuna space.

It also illustrates why [an experiment identifies only its actual contrast](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md). Search flexibility and proposal policy change together. One run that happened to make few outside-space changes is informative trajectory evidence, but does not substitute for a randomized restriction of agent edits. Against the [theory-builder definition](../notes/definitions/theory-builder.md), the source establishes executable candidates and repeated selection more clearly than criticism aimed at their stated content.

## Learning Claims (our opinion)

The source's mechanism is an outer loop that reads and edits training code, executes an inner training run, compares validation BPB, and keeps or reverts the edit. The inner loop changes the trained model's weights; the outer loop changes the training program. No updating of the proposing LLM's weights is reported. This makes retained code improvement compatible with a fixed proposing model, without implying that the trained target model is fixed.

The four theory-builder conditions have different support here:

1. **Localized content:** supported for code candidates. The report identifies concrete constants, initialization functions, and architectural edits; these are localized formal artifacts. It does not provide the agent's explicit conjectures about why particular changes should work.
2. **Consumption:** supported at the program level. The edited training code is executed, and the next experiment starts from retained code. This establishes an operational role for candidate content, without showing the agent's uptake of any separately stated explanatory theory.
3. **Content-directed criticism:** unresolved. A score determines acceptance, and the authors retrospectively explain classes of edits. The text does not expose agent criticisms, predicted consequences, or stated reasons that attribute a failure to what an identified candidate says. These omissions prevent a membership judgment; they do not show that such criticism never occurred.
4. **Iteration:** supported for retained code and score-guided revision within a run. Whether a stated criticism shapes later conjectures is unresolved for the same reason as condition 3. No cross-run or cross-problem reuse of criticism is demonstrated.

The reported gains support improvement of the retained training pipeline within this benchmark, with longer training providing a limited transfer test. They do not establish improvement in the agent's capacity to conduct subsequent searches. Editing the object being optimized does not by itself show reflection on the optimization method: the report does not show revision of the agent's prompt, keep/revert rule, or evaluation standard. Accumulating accepted changes likewise does not establish compounding, which would require evidence that earlier changes make later improvement more effective. The important contribution to Commonplace is the separation between enlarging the editable solution space and establishing a process of content-directed criticism.

## Extractable Value

1. **A boundary on the prospective Weco/AIDE² case.** This is Weco's evidence about AutoResearch, with within-run code retention and score-guided selection. Use it to separate fixed-proposer artifact improvement from claims about AIDE², reflective method revision, or established theory-builder membership. [quick-win]
2. **A concrete omitted-search-space example.** The short attention window, RoPE frequency, and optimizer internals were absent from the initial Optuna space but reachable through code edits. The observation supports examining effective update spaces; the bundled comparison does not quantify the independent benefit of space expansion. [quick-win]
3. **A stronger comparison to run.** Compare an agent restricted to the original 16 parameters, an unrestricted agent, and Optuna with an expanded space under an explicitly shared monetary budget. This would distinguish proposal-policy effects from the particular omitted choices more directly than the observed seed differences. [experiment]
4. **A bounded generalization check.** Testing selected pipelines at longer training horizons probes whether gains survive beyond the five-minute proxy. It is useful evaluation practice, but remains a same-task compute-horizon test rather than evidence of transfer across tasks or improvement of the search method. [quick-win]

## Limitations (our opinion)

The partial capture retains prose and the in-space/outside-space table but excludes interactive plots. It cannot establish the detailed performance curves, uncertainty intervals, or statistical tests behind claims of superiority at every budget and stronger significance at longer horizons. No code or experiments were inspected or executed for this ingest.

The setup text first states equal GPU-hours, then says Optuna receives roughly twice as many trials for the same spend because agent trials add token cost. Those are different budget constraints. The prose supports the authors' intended cost comparison but does not fully specify how the two constraints were implemented. Reported trial prices are specific to their hardware and inference regime; the authors themselves expect cheaper evaluations to favor classical search more strongly.

Three seeds on one task leave substantial uncertainty about broader applicability. The classification of accepted edits is retrospective, and sequential gains may depend on preceding changes. The reported decomposition of improvement is not a factorial ablation of each edit. Likewise, initializing Optuna's search space with Claude Code does not establish identical usable priors: one method receives a fixed parameterization, while the other repeatedly reasons over code. The implicit-regularization explanation could compete with differences in reachable solutions or selection dynamics and remains a hypothesis.

Longer training tests one form of proxy robustness, not all evaluation overfitting or out-of-domain generalization. Neither the generalization claim nor the favorable optimization result demonstrates revision of the optimizer's own method, durable cross-problem learning, or content-directed criticism. Those require evidence of the relevant process in addition to outcome scores.

## Recommended Next Action

Use this report as bounded comparative evidence when adding the Weco/AIDE² case to `kb/articles/which-existing-self-improving-systems-are-theory-builders.md`, explicitly attributing the experiment to AutoResearch and leaving AIDE²'s criticism and reflection judgments to its own mechanism evidence.
