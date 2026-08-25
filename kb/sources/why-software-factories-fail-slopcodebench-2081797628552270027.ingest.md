---
description: "Dex Horthy's SlopCodeBench run turns long-horizon code maintenance into a delayed benchmark signal while showing why deterministic proxies do not yet warrant lights-off autonomy"
source: https://x.com/dexhorthy/status/2081797628552270027
captured: "2026-07-28T14:01:50.184617+00:00"
capture: xdk
genre: practitioner-report
snapshot_sha256: bf4776cc6b2ddc1e8494dd21481e3ba2b7fe5a96483affefe115ebf17d30dd7c
status_id: 2081797628552270027
conversation_id: 2081797628552270027
post_count: 8
ingested: "2026-07-28"
type: kb/sources/types/ingest-report.md
domains: [agentic-coding, maintainability, evaluation, verification]
---

# Ingest: Why Software Factories Fail: Benchmarking the new frontier

## Classification

Horthy reports a firsthand nine-run experiment using three Claude models, three SlopCodeBench problems, and 17 incrementally revealed checkpoints, with held-out black-box tests and deterministic code-structure metrics. It is an empirical continuation of his software-factory series, not a conceptual proposal and not a report of a self-improving system.
Author: Dex Horthy writes as a HumanLayer cofounder and coding-agent practitioner. The report has useful operator evidence because he ran and watched the trajectories, but the subset, model selection, metric port, and interpretation are author-controlled and commercially adjacent.

## Summary

Horthy evaluates Opus 5, Opus 4.8, and Sonnet 5 on three SlopCodeBench problems whose requirements arrive checkpoint by checkpoint and whose held-out black-box tests accumulate across the trajectory. Opus 5 achieves four of 17 strict passes, versus one each for the other models, but no model completes any problem without a defect; all models also increase complexity or other slop indicators over time. Horthy treats this as an early signal that current models cannot maintain real-shaped codebases lights-off, while arguing that deterministic structural metrics are useful diagnostics but not yet a complete maintainability oracle. He proposes larger runs, quality-feedback variants, and a cross-model handoff test in which a smaller model must extend a stronger model's codebase.

## Quotes

- **Source extract (verbatim):** However, each challenge in SlopCodeBench has multiple "checkpoints" - the model doesn't know the whole problem up front, it has to evolve the codebase over time as new requirements are divulged.
  - **Source location:** Opening discussion of SlopCodeBench.
- **Source extract (verbatim):** i had claude pick out 3 problems from the repo, 17 checkpoints total, a mix of easy/medium/hard labeled problems: circuit_eval — easy (8 checkpoints) database_migration — medium (5 checkpoints) dynamic_config_service_api — hard (4 checkpoints)
  - **Source location:** The benchmark subset.
- **Source extract (verbatim):** and then I ran them across all three models, in parallel, with a fresh context window per checkpoint. All models got the same prompts and ran in the claude code harness.
  - **Source location:** The benchmark subset.
- **Source extract (verbatim):** the metric I decided I care about is the strict pass: everything new is green including every regression test that was inherited from previous checkpoints. A model fails a checkpoint if the solution has a defect - defects are detected by taking the models output, a CLI to run or in some cases e.g. an api server to poke at, and running a set of held-out black-box tests against the produced entrypoint.
  - **Source location:** The benchmark subset.
- **Source extract (verbatim):** For all 9 test runs, none of the models made it to the end of any challenge with everything passing, even on the problem marked as "easy" difficulty.
  - **Source location:** The benchmark subset, run result.
- **Source extract (verbatim):** I like that these measures are repeatable and don't use a model for judgement. But the link between any one of them and "is this codebase easy to change and evolve" is not yet established.
  - **Source location:** The slop meter.

## Connections Found

The report is new practitioner evidence for [The boundary of automation is the boundary of verification](../notes/the-boundary-of-automation-is-the-boundary-of-verification.md): functional checks can be cheap and repeatable while maintainability remains a delayed property. It also operationalizes the mixed hard/soft/delayed oracle framing in [Oracle strength spectrum](../notes/oracle-strength-spectrum.md) and supplies a concrete test case for the synthetic-futures and longitudinal-outcomes design space in [Brainstorming: maintainability oracles for agentic development](../notes/brainstorming-maintainability-oracles-for-agentic-development.md). Relative to [Part I](why-software-factories-fail-2080697380379427275.ingest.md) it adds measured longitudinal evidence; relative to [Part II](why-software-factories-fail-lights-back-on-2081058573556306030.ingest.md) it explores whether a stronger verifier could eventually replace some human steering. The source does not belong as a self-improving-system case: repeated checkpoint execution is evaluation of a codebase trajectory, with no evidence that prompts, code, or harness policy learn from the outcomes and become operative.

## Extractable Value

1. **Incrementally revealed requirements create a more relevant maintenance test than one-shot task completion** -- The checkpoint protocol makes later changes exercise the design decisions embedded in earlier code, giving a practical delayed-oracle surface for codebase evolution. [deep-dive]
2. **Strict pass is a useful accumulated-defect signal, not a complete maintainability measure** -- Re-running all prior held-out tests makes an early defect constrain later success, so the metric exposes path dependence that ordinary pass-at-task-end reporting hides. [quick-win]
3. **Deterministic slop metrics are diagnostic projections, not authority** -- Complexity, duplication, dependency, and decomposition measures are repeatable and can reveal trajectory changes, but the author explicitly lacks evidence that any one metric predicts future change cost or cannot be reward-hacked. [experiment]
4. **Model capability and maintainability separate** -- Opus 5 wins the small technical comparison while still failing all three end states and writing substantially more functions and code; a stronger model can be better locally without making lights-off operation warranted. [quick-win]
5. **Cost and correctness can improve together without reaching the deployment threshold** -- The report's “every dollar bought correctness; nobody bought enough” result preserves the distinction between incremental benchmark improvement and a quality level sufficient for unattended operation. [just-a-reference]
6. **Cross-model continuation is a promising maintainability experiment** -- Asking a smaller model to extend a stronger model's earlier checkpoints could test whether the first model left a codebase whose structure remains legible and changeable, rather than measuring only the original generator's debugging power. [deep-dive]

## Limitations (our opinion)

This is a small, author-selected subset: three problems, 17 checkpoints, and nine runs, with no controlled comparison of prompts, quality guardrails, model order, or repository design. The reported 24% versus 6% strict-pass rates therefore support a directional case for an unsaturated benchmark, not a stable model ranking or a general law about software factories. The static metrics are especially vulnerable to target mismatch and Goodharting; the report itself notes that most models are flagged by the rules and that the relationship to maintainability is unestablished. Strict accumulation can also over-penalize a transient defect if later repair is not credited, while the proposed cross-model handoff remains unrun. Finally, the source demonstrates a benchmarked evaluation harness, not a closed self-improvement loop: it provides no retained lesson, prompt revision, code revision selected by the benchmark, or later behavior change attributable to evaluation.

## Recommended Next Action

Update [Brainstorming: maintainability oracles for agentic development](../notes/brainstorming-maintainability-oracles-for-agentic-development.md) with this report as `evidenced-by`: add SlopCodeBench's checkpoint protocol and strict-pass result as a bounded empirical case for synthetic-futures evaluation, and preserve the distinction between generating delayed evidence and granting that evidence authority to replace human review.
