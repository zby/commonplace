---
description: "Passive distillation of existing agent trajectories into domain skills recovers much of a reasoning mode's performance at lower output-token cost, with skill and decomposition variance untested"
source: https://arxiv.org/html/2608.07885v1
captured: "2026-08-18"
capture: web-fetch
genre: scientific-paper
snapshot_sha256: 5563d6df0d4b948334753135a5d49408cdca7441d39e5fd721b13ceffc02ae9f
ingested: "2026-08-18"
type: kb/sources/types/ingest-report.md
domains: [trace-learning, deploy-time-learning, skill-distillation, reasoning-economics]
---

# Ingest: Reason Wide, Not Deep: Amortizing the Reasoning Premium into Distilled Skills

## Classification

An arXiv preprint with a defined corpus-to-skill method, held-out evaluations, a corpus-source ablation, a prompt-optimizer comparison, and explicit limitations.
Author: Six Microsoft researchers; the paper supplies primary experimental evidence and enough method detail to inspect the claimed comparison, but this KB has not independently reproduced the runs.

## Summary

The paper presents passive skill distillation: a coding agent analyzes 35–50 existing training trajectories for one model/domain pair, computes failure and action patterns, and writes a 40–130-line Markdown skill that is appended to a non-reasoning model's system prompt. On four held-out agent benchmarks, the GPT-5.4-mini skills recover 55%–100%+ of the measured no-think-to-think performance gap, exceed the reasoning mode on ALFWorld and retail, and use 2.9–4.5 times fewer output tokens than that model's reasoning condition. A second model improves on three of four benchmarks but regresses on retail. Skills distilled from no-think trajectories remain competitive with skills given paired think/no-think traces, and on two customer-service domains the method beats GEPA at lower reported production cost. The authors interpret this as replacing repeated within-episode reasoning about domain-invariant procedure with one corpus-wide analysis pass, while reserving reasoning for instance-specific work.

## Claims

No claims have been grounded yet.

## Connections Found

This paper is a direct empirical anchor for [system-definition artifacts as crystallized reasoning](../notes/system-definition-artifacts-are-crystallized-reasoning-under-context.md), [frontloading](../notes/frontloading-spares-execution-context.md), and [deployment-time constraining as learning](../notes/constraining-during-deployment-is-continuous-learning.md): an offline trace analysis produces an operative natural-language artifact that displaces recurring reasoning work without changing model weights. It also adds a distinct case to [Trace-learning techniques in related systems](../agent-memory-systems/trace-learning-techniques-in-related-systems.md): one passive coding-agent pass, one always-pushed model/domain skill, no fresh distillation rollouts, no runtime retrieval, and no policy training.

Its useful comparison is not simply another trajectory-memory inventory. [SkillOpt](skillopt-executive-strategy-self-evolving-agent-skills.ingest.md) iteratively edits and validation-selects natural-language skills, while this method compiles one from logs already in hand. [Large Language Model Agents Are Not Always Faithful Self-Evolvers](llm-agents-are-not-always-faithful-self-evolvers.ingest.md) supplies the main tension: many condensed memories are behaviorally inert, whereas these with/without-skill evaluations show aggregate behavioral change. The paper does not establish whether concrete actions, failure frequencies, corpus-wide recurrence, instruction authority, or another bundled feature explains the difference. Its experiments also [improve only inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md); they do not select the trajectory schema, natural-language Markdown-skill form, prompt injection point, or benchmark/harness partition.

## Extractable Value

1. **Existing logs can fund a cheap, passive learning pass** -- The distinctive method is not generic trajectory distillation but a single coding-agent analysis over rollouts already collected, reported at $1.28–$2.44 per model/domain skill and requiring no new environment interaction. This is a lower-operations alternative to active prompt optimization worth adding to the trace-learning casebook. [quick-win]
2. **Reasoning traces are not required to recover recurring procedure** -- No-think-only skills remain close to paired-corpus skills on ALFWorld and telecom, beat them by 10 points on SpreadsheetBench, and trail on retail; the result rejects a blanket requirement for reasoning traces while leaving a domain-dependent choice and uncontrolled distillation variance. [just-a-reference]
3. **Corpus-wide procedure can outperform per-episode re-derivation** -- On ALFWorld and GPT-5.4-mini retail, the distilled skill exceeds the reasoning condition. The plausible mechanism is recurrence: a rule compiled across many episodes can state a domain invariant more reliably than each episode re-derives it. The evidence supports that mechanism locally, not the paper's broader claim that wide search generally dominates deep search. [deep-dive]
4. **Some token savings come from better action, not only absent reasoning tokens** -- On ALFWorld and SpreadsheetBench the skilled model emits fewer tokens than the plain no-think baseline because it avoids loops and retries. Evaluation of prompt artifacts should therefore separate hidden/reasoning-token removal from shorter environment interaction caused by better procedure. [experiment]
5. **Concrete failure-derived rules are a candidate activation mechanism** -- The skills state exact actions, anti-patterns, and corpus frequencies, which may explain why they alter behavior where generic condensed memories often do not. A controlled comparison against equally sized generic summaries, raw examples, and unrelated rules is needed before treating specificity as the cause. [experiment]
6. **A small reasoning gap can make added rules harmful** -- Qwen's retail skill lowers performance when the base no-think model is already competent and the think/no-think gap is near zero. This is a compact warning that skill injection should be selected against a baseline rather than assumed beneficial from provenance or readability. [quick-win]

## Limitations (our opinion)

The experiments establish a useful local result, not the full “wide rather than deep” thesis. The learner can condition on recorded observations, actions and tool calls, visible outputs, rewards, pass rates, and sometimes reasoning traces; it can respond only by writing a compact model/domain-specific natural-language skill for a fixed system-prompt slot. The trajectory representation, distiller model and prompt, one-shot skill granularity, acting-model tools, harness, task partition, and benchmark oracle stay outside that update space. The corpus-source ablation varies reasoning-trace availability only, so it does not validate those adjacent fixed choices or the decomposition as a whole.

Each skill is distilled once. Three evaluation seeds estimate acting-run variance, not variance in what the coding agent writes, so the 10-point paired/no-think reversal on SpreadsheetBench and the Qwen retail regression could partly be skill-sample noise. The study covers two models and four benchmark domains, uses model/domain-specific skills, and does not test cross-model transfer. ALFWorld's atomic commands and retail's repeated authentication error are unusually crisp recurrence structures; open-ended knowledge work may supply neither repeated procedure nor a hard success oracle.

The comparisons omit several simpler explanations and controls. There is no equally sized random or irrelevant skill, direct successful-trajectory few-shot baseline, rule-based corpus miner, or per-rule intervention showing which guidance changed which action. Aggregate with/without-skill gains establish that the prompt condition matters, but not behavioral faithfulness to individual distilled rules. The GEPA comparison covers only two domains and contrasts passive reuse of existing logs with an optimizer that pays for fresh metric calls.

Finally, the cost claim is based mainly on output tokens plus one-time coding-agent spend. The paper treats the skill as a cacheable prefix but does not report full input-token, cache-miss, latency, storage, or operational costs, nor an observed break-even curve. The recurring saving is credible; its production economics should not be generalized from the reported ratios alone.

## Recommended Next Action

Write a doc-grounded lightweight review at `kb/agent-memory-systems/lightweight/passive-skill-distillation.md`, positioning the method as the no-retrieval, no-weight-update, one-pass member of the trajectory-to-skill casebook and carrying forward the fixed-decomposition and distillation-variance limits.
