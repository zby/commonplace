---
description: "Matched guidance ablations on 60 executable science tasks show that removing full procedures hurts agent performance far more than removing method-level hints."
source: https://arxiv.org/abs/2608.17271
captured: "2026-08-31"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 1421eabed9ccff2521fb3587c195f349d0cd109e90c9bd9860e2f6b776e97173
ingested: "2026-08-31"
type: kb/sources/types/ingest-report.md
domains: [agent-evaluation, scientific-agents, instruction-design, benchmark-methodology]
---

# Ingest: ASI-Bench: At the Dawn of Artificial Superintelligence

## Classification

This is a scientific benchmark paper: it defines an executable task suite, varies methodological guidance within matched tasks, and reports empirical scores and costs for Agent×Model configurations. Author: a multi-institution team of more than 40 researchers, led largely by Tsinghua University affiliates, reports 21 retained-task contributors, five human-review rounds, more than 1,100 task-review assignments, and end-to-end sandbox validation; the benchmark creators also authored its evaluation.

## Summary

ASI-Bench packages 60 project-level tasks across 11 scientific domains and keeps each task's objective, data, required artifacts, and scoring fixed while moving from a full equation-and-procedure condition (B1), through method-level guidance (B2), to objective-and-data-only work (B3), then adding plausible distractors (B4). Across 18 Agent×Model configurations evaluated without external tool access, the macro-average score falls from 50.91 in B1 to 29.10 in B2 and 26.62 in B3, while B4 remains near B3 at 26.99; B2 also has the highest mean token and time cost. The paper is useful for estimating dependence on supplied procedure and for comparing model–harness systems, but its fixed tasks and verification artifacts do not test problem selection, prospective scientific value, or the full discovery loop.

## Quotes

No source quotes have been retained yet.

## Connections Found

ASI-Bench is a technical evidence source and a limitation case for Commonplace's accounts of instruction specification and agent evaluation. The B1→B2 loss supports the practical importance of narrowing procedural search in [Agentic systems interpret underspecified instructions](../notes/agentic-systems-interpret-underspecified-instructions.md), but the treatment does not isolate semantic ambiguity from missing equations, parameters, scientific knowledge, or execution burden. [An experiment identifies only the contrast it actually runs](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) therefore limits the paper's method-operationalization claim to the guidance bundles it varied.

Because ASI-Bench supplies the objectives, data, required artifacts, reference procedures, and scorers, it instantiates both [the fixed-client benchmark boundary](../notes/holding-the-client-fixed-exports-the-least-warrantable-decisions.md) and [known-target reachability rather than discovery closure](../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md). Its same-backbone comparisons are an empirical counterpart to [Agentic Harness Engineering](../agent-memory-systems/reviews/agentic-harness-engineering.md): capability is observed for a model–harness configuration, not attributable to the backbone alone. The aggregate B3/B4 null is a bounded counterpoint to [soft degradation from irrelevant context](../notes/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md), not evidence that distractors are harmless generally.

## Extractable Value

1. **Complete procedural guidance is a large measured lever.** Removing B1's detailed procedure while retaining method-level help in B2 lowers the macro-average score by 21.82 points on otherwise matched tasks, providing a concrete case where narrowing the executor's search space changes outcomes. The changed bundle prevents attribution to any one instruction component. [quick-win]
2. **Partial guidance may be an expensive middle state.** B2 uses 6.91 million tokens and 49.7 minutes per task on average, versus 4.35 million tokens and 37.8 minutes for B1, while gaining only 2.48 score points over B3. Together with the connected SWE-bench Science result, this motivates a testable hypothesis that guidance value depends on completeness and harness alignment rather than mere presence. [deep-dive]
3. **Agent evaluation should preserve the model–harness unit.** Selected backbones score materially differently across harnesses, giving empirical support for reporting and comparing complete Agent×Model configurations rather than treating benchmark performance as a model property. The selected pairings do not isolate which harness mechanism caused the difference. [quick-win]
4. **The benchmark measures known-target scientific execution, not discovery closure.** Fixed objectives, inputs, required artifacts, reference generation, and scoring make the tasks verifiable, but export problem choice, value judgment, and prospective acceptance. This is a concrete project-level example for the KB's benchmark-boundary notes. [quick-win]
5. **Distractor robustness remains a boundary-condition question.** One B4 distractor package produces almost no aggregate change from B3, in tension with controlled short-form distractor studies but not in contradiction with them. A matched experiment varying distractor dose, placement, task horizon, model, and harness would test the boundary. [experiment]

## Limitations (our opinion)

The guidance ablations do not identify all of the causal nouns used in the paper. In the representative task, B1→B2 jointly removes the governing equation, coefficient interpretation, discretization, time integrator, and procedural details; B2→B3 removes a broader class of methodological background rather than one independently varied method label. The large first drop therefore identifies a bundled full-guidance effect, not method operationalization alone. Likewise, the B3→B4 result tests one factually correct distractor construction and cannot establish general resistance to irrelevant context.

The effective update space is also narrower than the paper's autonomous-research framing. An Agent×Model can condition on its prompt, supplied data and metadata, and whatever interaction and execution history its harness preserves; it can compose the harness's permitted reasoning, file, code-execution, diagnosis, revision, and artifact-production operations; and the model–harness pair supplies the mappings from those signals to a workflow. Task selection, objectives, data, required artifacts, B1–B4 partition, reference generation, scoring, sandbox and external-tool policy, and the selected models and harnesses remain fixed outside that space. Under [the fixed-decomposition boundary](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), performance inside these conditions does not validate the fixed decomposition or show that the system can choose and verify worthwhile new research.

The evidence is further limited to 60 author-curated tasks, selected configurations, macro-averaged scores, and the first arXiv version. The benchmark authors built and evaluated the suite, so extensive internal expert review is not independent replication. This ingest did not execute the benchmark, task-generation code, or scorers; the reported performance and cost results remain paper-reported outcomes.

## Recommended Next Action

Draft a scoped note provisionally titled "Partial guidance can constrain search without paying down procedural reconstruction" that synthesizes ASI-Bench's B1/B2 performance-and-cost contrast with [SWE-bench Science](./swe-bench-science-arxiv-2608-19799.ingest.md) and presents guidance completeness and harness alignment as a testable hypothesis rather than a general rule.
