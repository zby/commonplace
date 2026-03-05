---
source_snapshot: convexbench-can-llms-recognize-convex-functions.md
ingested: 2026-03-04
type: scientific-paper
domains: [compositional-reasoning, agentic-scaffolding, context-management, benchmarking]
---

# Ingest: ConvexBench: Can LLMs Recognize Convex Functions?

Source: convexbench-can-llms-recognize-convex-functions.md
Captured: 2026-03-04
From: https://arxiv.org/html/2602.01075v2

## Classification

Type: **scientific-paper** — Peer-reviewed preprint with controlled experiments, ablation studies, and mechanically verified ground truth labels across multiple frontier models.

Domains: compositional-reasoning, agentic-scaffolding, context-management, benchmarking

Author: Yepeng Liu, Yu Huang, Yu-Xiang Wang, Yingbin Liang, Yuheng Bu — academic researchers at Ohio State and UC Santa Barbara. The work is methodologically rigorous (mechanically verifiable benchmark via DCP composition rules, controlled depth variable, multi-model testing). No obvious prior connection to agent architecture discourse, but the findings speak directly to it.

## Summary

The paper introduces ConvexBench, a benchmark that tests whether LLMs can determine convexity of deeply composed symbolic functions. The key contribution is demonstrating a sharp "compositional reasoning gap": one-shot LLM performance collapses from perfect (F1=1.0) at depth 2 to near-failure (F1~0.2) at depth 100, even though the total token count (5,331 at depth 100) is far below context window limits. This proves that reasoning degradation is not a token-capacity problem but an attention-distribution and reasoning-horizon problem. The authors then show that agentic frameworks using divide-and-conquer with focused context (pruning irrelevant history at each recursive step) fully recover performance to F1=1.0 at all depths. The fix works because it gives each sub-step a clean reasoning frame with only the information needed for that step, rather than an accumulating history of all prior sub-steps.

## Connections Found

The connection search found five strong links to existing KB notes:

1. **[Context efficiency is the central design concern in agent systems](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md)** — empirically grounds. The paper's central finding — that performance degrades with depth even at ~5k tokens, far below window limits — is direct empirical evidence for the "attention degradation under load" property. The context-efficiency note argues theoretically that "more content means weaker attention to any given part" and that "the resource doesn't just run out — it degrades before it runs out." ConvexBench makes this concrete and measurable: F1 drops from 1.0 to 0.2 as compositional depth increases, even though the token count is trivial relative to the window.

2. **[LLM context is composed without scoping](../notes/llm-context-is-composed-without-scoping.md)** — empirically validates. The paper's most effective fix — "agentic reasoning with focused context" — prunes accumulated reasoning history to retain only direct dependencies for each sub-step. This is precisely the "recursion with clean frames" concept that the scoping note identifies as an undeveloped direction: "A flat context makes recursive decomposition painful because each recursive call appends to the same context. With a proper stack, each recursive call gets a clean frame and completed calls are popped." ConvexBench turns this theoretical prediction into an experimental result: flat context degrades, scoped frames recover full performance.

3. **[The bitter lesson stops at calculators](../notes/bitter-lesson-boundary.md)** — provides a test case. Convexity verification via DCP composition rules is a pure calculator problem: the specification IS the problem, correctness is mechanically verifiable, there is no gap between spec and reality. Yet frontier LLMs fail at depth. The paper shows that scale alone does not solve calculator problems that require compositional reasoning — engineering scaffolding (deterministic parsing, recursive verification with scoped context) is necessary. This is a clean datapoint for the boundary: even in the calculator regime, LLMs need architectural support for compositional depth.

4. **[Frontloading spares execution context](../notes/frontloading-spares-execution-context.md)** — exemplifies the mechanism. The paper's first improvement — offloading expression parsing to external tools that provide explicit ASTs — is textbook frontloading. Instead of asking the LLM to parse parenthesized expressions (an interpretation task), a deterministic tool produces the structured representation and hands it to the LLM. This removes parsing from the reasoning context, freeing attention for the actual convexity analysis.

5. **[The bitter lesson boundary is a gradient, not a binary](../notes/oracle-strength-spectrum.md)** — exemplifies the hard-oracle end. ConvexBench has a perfect oracle: DCP composition rules mechanically verify labels with no judgment required. This is exactly the "hard oracle" position on the spectrum — "exact, cheap, deterministic check." The hard oracle is what enables the benchmark to be rigorous and the agentic improvements to be precisely measured.

## Extractable Value

1. **Empirical evidence that reasoning degradation is not about token count.** At 5,331 tokens and depth 100, models collapse — this separates "long-context capability" from "long-horizon reasoning capability." Directly strengthens the context-efficiency note with a concrete, citable datapoint. [quick-win]

2. **"Recursion with clean frames" is experimentally validated.** The scoping note predicts this as an "undeveloped direction" — ConvexBench demonstrates that it works, recovering F1=1.0 from 0.2. The specific mechanism: each recursive sub-step receives only its direct dependencies, not the accumulated history. This turns a theoretical KB prediction into an empirically supported claim. [quick-win]

3. **"Lazy reasoning" as a named failure mode.** Models plateau in token usage beyond certain depth thresholds — they stop actually reasoning and fall back to shallow heuristics. This connects to the context-efficiency note's "interpretation cost compounds" property but adds a new dimension: the model doesn't just degrade, it actively economizes by reasoning less. Could inform thinking about how agents handle deep multi-step procedures. [just-a-reference]

4. **Capability-aware framework design.** The paper finds that stronger models (GPT-5) benefit mostly from decomposition alone, while weaker models (Qwen3-8B) need the full agentic recursion with focused context. This has implications for the distillation/context-loading decisions: the right level of scaffolding depends on the model's baseline capability. [experiment]

5. **External deterministic tools for parsing as a general pattern.** The AST-parsing step that resolves structural ambiguity before the LLM reasons about content is a reusable pattern. Any task where the LLM must parse deeply nested structure before reasoning about it could benefit from the same split: deterministic parser for structure, LLM for semantics. This is a specific instance of frontloading applied to structural parsing. [deep-dive]

6. **Hard-oracle benchmark design as a methodology.** ConvexBench's approach — generate instances with certified labels via composition rules, control complexity through a single depth parameter, mechanically verify all results — is a clean template for building benchmarks in the calculator regime. Relevant if we ever want to benchmark agent performance on our own structured tasks (e.g., link validation, frontmatter correctness). [just-a-reference]

## Recommended Next Action

Update existing note [LLM context is composed without scoping](../notes/llm-context-is-composed-without-scoping.md): in the "Undeveloped directions" section under "Recursion with clean frames," add ConvexBench as empirical evidence that validates the prediction. The note currently says this is an idea that "doesn't yet have concrete examples" — this paper IS the concrete example. Specifically: cite the F1 recovery (0.2 to 1.0) when recursive sub-steps use focused context instead of accumulated history, and note that this works even for a simple deterministic domain (convexity checking), suggesting the principle is fundamental rather than domain-specific.
