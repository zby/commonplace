---
description: Controlled ablation showing raw execution traces (10 MTok/iter) outperform summaries and scores-only feedback by 10+ points in automated outer-loop harness search — strongest empirical case for diagnostic richness as a binding constraint on automated improvement
source_snapshot: meta-harness-end-to-end-optimization-of-model-harnesses.md
ingested: 2026-03-30
type: scientific-paper
domains: [learning-theory, context-engineering, evaluation, harness-engineering]
---

# Ingest: Meta-Harness: End-to-End Optimization of Model Harnesses

Source: meta-harness-end-to-end-optimization-of-model-harnesses.md
Captured: 2026-03-31
From: https://yoonholee.com/meta-harness/paper.pdf

## Classification

Type: **scientific-paper** — preprint with formal problem definition, three benchmark evaluations, controlled ablations, and quantitative baselines. Follows standard ML paper structure with appendices documenting qualitative proposer behavior.

Domains: learning-theory, context-engineering, evaluation, harness-engineering

Author: Yoonho Lee (Stanford, Chelsea Finn's group), with collaborators from MIT (Kangwook Lee) and Stanford NLP (Omar Khattab / DSPy). This is a research lab with strong track record in meta-learning and LLM systems. Khattab's involvement connects this directly to the DSPy / prompt optimization lineage. The work uses Claude Code with Opus-4.6 as the proposer agent, making it one of the first papers to study what happens when you give a coding agent unrestricted filesystem access to diagnostic history for automated search.

## Summary

Meta-Harness is an outer-loop system that searches over LLM harness code by giving a coding agent (Claude Code with Opus-4.6) full filesystem access to prior harness source code, evaluation scores, and raw execution traces. The key finding is that access to rich diagnostic information — 10 million tokens per iteration, three orders of magnitude beyond prior text optimizers — enables the proposer to do causal reasoning about why harnesses fail, not just that they fail. On three benchmarks (online text classification, IMO-level math retrieval, TerminalBench-2 agentic coding), Meta-Harness outperforms both hand-engineered baselines and prior program-search methods. The critical ablation shows that summaries do not recover the signal lost by compressing raw traces, and may even hurt — scores-only and scores+summary variants both trail the full-trace version by 15+ points on median accuracy.

## Connections Found

The `/connect` pass identified 9 connections to existing KB notes, with two synthesis opportunities:

**Strongest cluster — the trace-derived learning family.** Meta-Harness belongs in the [trace-derived learning survey](../notes/trace-derived-learning-techniques-in-related-systems.md) as the 19th system and the most extreme on the scale axis. It pushes trace ingestion volume by three orders of magnitude (10 MTok/iter vs ~26K for the largest reviewed system) with controlled ablation data proving the value of that scale. The survey's finding that "extraction detail matters" is directly validated by the ablation.

**Closest architectural relative — HyperAgents.** [HyperAgents](../notes/related-systems/hyperagents.md) is the nearest KB system: both run outer-loop evolutionary search over code artifacts with benchmark-scored selection. Meta-Harness diverges by giving the proposer filesystem access to execution traces rather than just git diffs and scores, and the ablation quantifies the value of that richer diagnostic access. HyperAgents inverts the complexity allocation (sophisticated outer loop, simpler proposer) compared to Meta-Harness (minimal outer loop, sophisticated proposer).

**Theory connections.** The paper exemplifies [deploy-time learning](../notes/deploy-time-learning-is-the-missing-middle.md) (discovered harnesses are durable inspectable symbolic artifacts that generalize across models), grounds [oracle-strength-spectrum](../notes/oracle-strength-spectrum.md) (success depends entirely on hard benchmark oracles), exemplifies [the boundary of automation is the boundary of verification](../notes/the-boundary-of-automation-is-the-boundary-of-verification.md), and extends [spec-mining-as-codification](../notes/spec-mining-as-codification.md) (the proposer's causal reasoning over failure traces is automated spec mining). It partially contradicts [evaluation-automation-is-phase-gated-by-comprehension](../notes/evaluation-automation-is-phase-gated-by-comprehension.md) — the proposer automates the comprehension phase itself in hard-oracle domains, though the note already acknowledges this scope limit.

**Synthesis opportunity.** The connect report flags an unnamed axis: "diagnostic richness" as orthogonal to oracle strength. Meta-Harness, HyperAgents, Autocontext, and text optimizers form a gradient of diagnostic richness in outer-loop search. Meta-Harness's ablation data suggests diagnostic access quality, not search algorithm sophistication, is the binding constraint on automated improvement.

## Extractable Value

1. **Diagnostic richness gradient with controlled ablation data.** The scores-only vs. scores+summary vs. full-traces ablation (Table 3) is the first controlled evidence that richer diagnostic access changes outer-loop search quality. The median accuracy gap (34.6/34.9 vs. 50.0) is large enough to matter. This names and quantifies something the KB has discussed but never had data for. High reach — the principle (richer feedback enables better search) applies beyond harness engineering to any iterative improvement loop. [quick-win: write a note naming the diagnostic-richness axis and citing this ablation]

2. **Summaries actively hurt compared to raw traces.** The scores+summary variant (best 38.7%) underperforms scores-only (best 41.3%) on best-found accuracy while barely helping median. This is a specific, surprising finding: LLM-generated summaries are not neutral compression but lossy in diagnostically harmful ways. High reach — this challenges any system that uses summary-based feedback for iterative improvement (GEPA, Feedback Descent, and potentially our own distillation workflows). [experiment: check whether our distillation practices compress away diagnostically useful detail]

3. **Qualitative proposer behavior: causal reasoning over prior failures.** The TerminalBench-2 trajectory (Appendix A) shows the proposer identifying confounds (iteration 3), isolating variables (iteration 7), and transferring knowledge across runs (iteration 10). This is the spec-mining loop automated — observe, hypothesize, test. The qualitative evidence is well-documented enough to serve as a worked example. Medium reach — the specific reasoning depends on the proposer being a highly capable coding agent with filesystem tools. [just-a-reference: cite as evidence for automated spec mining in capable-enough agents]

4. **10x convergence advantage.** Meta-Harness matches the best prior text optimizers (OpenEvolve, TTT-Discover) with 10x fewer full evaluations, and its final accuracy surpasses theirs by 10+ points. The wall-clock time is "a few hours." This makes automated harness search practical, not just theoretically interesting. Medium reach — convergence advantage depends on the proposer capability and the particular benchmarks. [just-a-reference]

5. **Discovered harnesses generalize across models and distributions.** The math retrieval harness discovered on a search set generalizes to five held-out models (including future, stronger ones). The text classification harness generalizes to 9 out-of-distribution datasets. This is evidence that code-space search produces transferable strategies, not benchmark-specific hacks. High reach — supports the deploy-time learning claim that harder symbolic artifacts enable broader applicability. [quick-win: cite in oracle-strength-spectrum or deploy-time-learning as empirical evidence]

6. **Discovered harness architectures are themselves interesting.** The Draft Verification harness (two-call with confirmers/challengers) and the Label-Primed Query harness (label primer + coverage block + contrastive pairs) are concrete designs worth studying. The four-route BM25 math retrieval harness shows domain-specific routing emerging from automated search. Low reach — these are task-specific designs, though the patterns (draft-then-verify, contrastive retrieval) transfer. [deep-dive: analyze discovered harness patterns as a separate note if we pursue harness engineering further]

7. **Population maintenance is minimal; proposer sophistication is maximal.** Meta-Harness imposes no parent-selection rule, no archive structure, no persistent memory mechanism. All the intelligence is in the proposer's ability to selectively access prior artifacts. This is a specific architectural claim: invest in the proposer, not the search scaffolding. Medium reach — depends on having a proposer capable of 82-file-per-iteration selective reading. [experiment: test whether this principle holds for less capable proposers]

## Curiosity Gate

**What is most surprising?** The summaries-hurt result (Section 4.1, Table 3). The intuition that summarizing execution traces before feeding them to an optimizer should help — by reducing noise and highlighting salient patterns — is wrong. The paper's explanation is that "summaries compress away diagnostically useful details," but this deserves more attention. It suggests that what matters for diagnosis is not the salient pattern (which summaries preserve) but the unexpected detail (which summaries discard). This has implications for any system that uses LLM-generated summaries as intermediate representations — including our own distillation practices.

**What's the simpler account?** For the main claim (rich trace access improves search): a simpler account is that Meta-Harness works because Opus-4.6 is a very capable proposer that happens to have filesystem tools, and any sufficiently capable agent with any feedback would do well. The ablation partially addresses this — the same proposer with compressed feedback does much worse — but only on the classification task. The math and TerminalBench results lack ablations, so we cannot rule out that proposer capability, not diagnostic richness, is doing the work in those domains.

**Is the central claim hard to vary?** The claim "richer diagnostic access enables better harness search" is reasonably hard to vary. You cannot swap the evidence (ablation data) and keep the conclusion — the ablation specifically tests the diagnostic-richness variable while holding the proposer constant. However, the claim is tested on only one task domain with ablation data. The TerminalBench and math results are consistent but not controlled. A weaker version — "rich trace access helps on at least some task types" — is well-supported; the stronger "rich trace access is the key ingredient across domains" requires more ablation data.

## Limitations (our opinion)

**Ablation coverage is narrow.** The critical ablation (scores-only vs. summaries vs. full traces) is run only on the text classification domain. The TerminalBench and math reasoning experiments show strong results but without ablation controls. We cannot confirm that trace access, rather than other factors (proposer capability, initial harness quality, domain-specific properties), drives performance in those domains. This is the most important limitation because the paper's central thesis depends on trace access being the key ingredient.

**Proposer is a single, highly capable system.** All experiments use Claude Code with Opus-4.6 — one of the most capable coding agents available. The paper does not test whether the approach works with less capable proposers. The 82-files-per-iteration access pattern may require a level of selective attention and long-context reasoning that weaker models cannot sustain. The principle "invest in diagnostic richness" may hold only above a proposer capability threshold.

**Hard-oracle domains only.** All three benchmarks have cheap, automated evaluation: classification accuracy, math pass@1, and TerminalBench pass rate. The paper acknowledges requiring a "task-specific reward function r(tau, x)" but does not discuss what happens with soft oracles, interactive oracles, or subjective evaluation. The [oracle-strength-spectrum](../notes/oracle-strength-spectrum.md) note predicts this approach works only at the hard-oracle end — the paper provides no evidence to the contrary.

**No cost analysis.** The paper reports "a few hours of wall-clock time" but does not disclose token costs, API costs, or compute costs for the outer loop. At 10 MTok per iteration and ~20 iterations, the proposer alone consumes ~200M tokens per search run, before counting the base model evaluation tokens. This is relevant for assessing whether the approach is practical outside well-funded research labs.

**Overfitting risk is acknowledged but not tested.** The paper argues that "overfitting in code space is more inspectable" — you can spot brittle if-chains and hard-coded mappings. But the out-of-distribution generalization results (Section 4.1) test only the text classification domain, and the math results test only model transfer (same problem distribution, different models). Distribution shift in the agentic coding domain is not tested. The inspectability argument is qualitative; no systematic analysis of discovered harnesses for overfitting signals is provided.

**Comparison baselines are uneven.** The text classification baselines include prior text optimizers (OpenEvolve, TTT-Discover) with fair comparisons. The math reasoning baselines are limited to standard retrieval methods (BM25, dense retrieval) without comparing to other optimization approaches applied to retrieval harnesses. The TerminalBench comparison is against hand-engineered systems, not other automated search methods. This makes it hard to isolate how much of the gain comes from automated search vs. the specific Meta-Harness approach.

## Recommended Next Action

Write a note titled "Diagnostic richness determines outer-loop search quality" connecting to [oracle-strength-spectrum](../notes/oracle-strength-spectrum.md), [trace-derived-learning-techniques-in-related-systems](../notes/trace-derived-learning-techniques-in-related-systems.md), and [context-efficiency-is-the-central-design-concern-in-agent-systems](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md). It would argue that the binding constraint on automated improvement loops is not search algorithm sophistication or oracle strength alone but diagnostic access quality — the ability of the proposer to selectively inspect rich, raw diagnostic information. The Meta-Harness ablation provides the first controlled evidence; position it alongside the HyperAgents/Autocontext/text-optimizer gradient to show the pattern holds across systems. This names the unnamed axis the `/connect` report flagged as a synthesis opportunity.
