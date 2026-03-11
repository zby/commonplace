---
description: Benchmark proving LLM compositional reasoning collapses with depth (not token count), recovered by recursive decomposition with focused context — quantitative evidence for scheduling model predictions
source_snapshot: convexbench-can-llms-recognize-convex-functions.md
ingested: 2026-03-09
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

Author: Yepeng Liu, Yu Huang, Yu-Xiang Wang, Yingbin Liang, Yuheng Bu — academic researchers at Ohio State and UC Santa Barbara. Methodologically rigorous work (mechanically verifiable benchmark via DCP composition rules, controlled depth variable, multi-model testing). No obvious prior connection to agent architecture discourse, but the findings speak directly to it.

## Summary

The paper introduces ConvexBench, a benchmark testing whether LLMs can determine convexity of deeply composed symbolic functions. The key contribution is demonstrating a sharp "compositional reasoning gap": one-shot LLM performance collapses from perfect (F1=1.0) at depth 2 to near-failure (F1~0.2) at depth 100, even though the total token count (5,331 at depth 100) is far below context window limits. This proves that reasoning degradation is an attention-distribution and reasoning-horizon problem, not a token-capacity problem. The authors then show that agentic frameworks using divide-and-conquer with focused context (pruning irrelevant history at each recursive step) fully recover performance to F1=1.0 at all depths, because each sub-step gets a clean reasoning frame with only the information it needs.

## Connections Found

The `/connect` discovery run (2026-03-09) found **10 genuine connections** to KB notes and **3 source-to-source connections**, substantially expanding the original 5-note analysis.

**Already linked from existing notes (2):**

- [Context efficiency is the central design concern in agent systems](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — **grounds**: ConvexBench provides direct empirical evidence for "attention degradation under load." Performance degrades at 5,331 tokens (trivially below context limits), proving degradation is about reasoning complexity, not token volume.

- [LLM context is composed without scoping](../notes/llm-context-is-composed-without-scoping.md) — **grounds**: Experimentally validates the "recursion with clean frames" prediction. Focused context (giving each recursive step only its direct dependencies) recovers F1=1.0 from 0.2, confirming that flat accumulation causes the collapse.

**New connections not yet linked from notes (8):**

- [Symbolic scheduling over bounded LLM calls is the right model for agent orchestration](../notes/bounded-context-orchestration-model.md) — **exemplifies**: ConvexBench's agentic framework is a concrete instance of the scheduling model. A symbolic scheduler manages the recursion stack and sub-expression tracking (bookkeeping), while bounded LLM calls handle the semantic judgment (is this sub-function convex?). The key finding — offloading bookkeeping to deterministic tools and giving each LLM call minimal focused context recovers full performance — is exactly the scheduling model's prediction.

- [Decomposition rules for bounded-context scheduling](../notes/decomposition-rules-for-bounded-context-scheduling.md) — **exemplifies**: Demonstrates several rules empirically: "separate selection from joint reasoning" (parse deterministically, then ask LLM about convexity), "use symbolic operations wherever exactness is available" (deterministic AST parsing), "exploit clean frames recursively" (recursive verification with focused context outperforms flat). The ablation finding that finer decomposition (10-character sub-functions) consistently outperforms coarser provides quantitative evidence for aggressive decomposition.

- [Frontloading spares execution context](../notes/frontloading-spares-execution-context.md) — **exemplifies**: Offloading expression parsing to an external tool that provides explicit ASTs is textbook frontloading. A deterministic parser resolves structural ambiguity before the LLM reasons about content, removing parsing from bounded context and freeing attention for convexity analysis.

- [The bitter lesson stops at calculators](../notes/bitter-lesson-boundary.md) — **exemplifies**: Convexity verification via DCP rules is a pure calculator problem (spec IS the problem, correctness is mechanically verifiable). Yet frontier LLMs fail at depth. Scale alone does not solve calculator problems requiring compositional reasoning — engineering scaffolding is necessary.

- [Oracle-strength spectrum](../notes/oracle-strength-spectrum.md) — **exemplifies**: ConvexBench has a perfect hard oracle: DCP composition rules mechanically verify labels with zero judgment. Exemplifies the hard-oracle end of the spectrum and shows how hard oracles enable rigorous benchmarking.

- [Bounded-context orchestration model](../notes/bounded-context-orchestration-model.md) — **exemplifies**: The agentic framework with focused context is a concrete instance of the select/execute/absorb loop. Each recursive step selects what to include (only direct dependencies), executes in a clean sub-agent frame, absorbs the result, and feeds it forward. Recovery of full performance validates the claim that the loop works because of clean frame isolation.

- [Codification](../notes/codification.md) — **exemplifies**: The external AST parsing tool is codification — a deterministic code solution replacing LLM interpretation for the structural parsing sub-problem. The parsing specification IS the problem (parenthesis matching, operator scope), making it a natural codification candidate.

- [LLM-mediated schedulers are a degraded variant of the clean model](../notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — **exemplifies**: The one-shot baseline — where the LLM handles both bookkeeping and semantic judgment in a single flat context — is the degraded variant. Performance collapse from F1=1.0 to 0.2 demonstrates the degradation. The agentic framework with external parsing and focused context recovers the clean separation, achieving F1=1.0.

**Source-to-source connections (3):**

- [Agentic code reasoning ingest](agentic-code-reasoning.ingest.md) — **synthesizes**: Both sources independently show that explicit process structure outperforms free-form reasoning on deep reasoning tasks. ConvexBench for symbolic reasoning (convexity); agentic code reasoning for code semantics (patch equivalence, fault localization). Shared mechanism: structured frameworks constraining the reasoning process recover performance that free-form approaches lose.

- [MAKER ingest](meyerson-maker-million-step-llm-zero-errors.ingest.md) — **complements**: Both demonstrate that decomposition + focused context solves problems one-shot cannot. Both operate in the hard-oracle regime. Key difference: MAKER uses redundancy (voting) to handle errors; ConvexBench uses focused context to prevent errors.

- [Induction bias in sequence models ingest](induction-bias-sequence-models-ebrahimi-2026.ingest.md) — **complements**: Ebrahimi et al. explain WHY transformers fail at compositional reasoning (kappa near 1 means length-isolated learning). ConvexBench demonstrates WHAT that failure looks like (F1 collapse with depth) and HOW to work around it (recursive decomposition with clean frames). Mechanism vs manifestation+mitigation.

**Synthesis opportunities:**

1. "Compositional depth is the binding constraint, not context length" — ConvexBench + context-efficiency + scoping + induction-bias evidence converge on: long-context capability and long-horizon reasoning capability are architecturally independent, and the field's focus on context-length scaling obscures the compositional-depth bottleneck.

2. "Structured decomposition consistently outperforms free-form reasoning" — Cross-source pattern: ConvexBench (F1=1.0 recovery), agentic code reasoning (93% with templates), MAKER (zero errors over 1M steps). Across symbolic, code, and execution domains, imposing structured decomposition consistently recovers lost performance.

## Extractable Value

1. **Empirical evidence that reasoning degradation is not about token count.** At 5,331 tokens and depth 100, models collapse — separating "long-context capability" from "long-horizon reasoning capability." Directly strengthens the context-efficiency note with a concrete, citable datapoint. [quick-win]

2. **"Recursion with clean frames" experimentally validated.** The scoping note predicted this; ConvexBench demonstrates it works, recovering F1=1.0 from 0.2. The specific mechanism: each recursive sub-step receives only its direct dependencies. Turns a theoretical KB prediction into an empirically supported claim. [quick-win]

3. **Quantitative evidence for the scheduling model's decomposition rules.** The ablation showing finer decomposition (10-character sub-functions) consistently outperforms coarser decomposition, and the full breakdown of improvements from parsing offload vs recursive reasoning vs focused context, provide concrete numbers for claims the decomposition-rules note makes qualitatively. [quick-win]

4. **Capability-aware framework design pattern.** Stronger models (GPT-5) benefit mostly from decomposition alone; weaker models (Qwen3-8B) need full agentic recursion with focused context. Implications for distillation/context-loading decisions: the right scaffolding level depends on model baseline capability. [experiment]

5. **External deterministic tools for parsing as a general pattern.** The AST-parsing step that resolves structural ambiguity before the LLM reasons about content is a reusable pattern for any task involving deeply nested structure. A specific instance of frontloading applied to structural parsing, and of codification replacing LLM interpretation with code. [deep-dive]

6. **"Lazy reasoning" as a named failure mode.** Models plateau in token usage beyond depth thresholds — they stop reasoning and fall back to shallow heuristics, increasingly misclassifying as "neither" (the safest prediction). This adds a dimension beyond degradation: active economizing on reasoning effort. [just-a-reference]

7. **Hard-oracle benchmark design template.** ConvexBench's approach — generate instances with certified labels via composition rules, control complexity through a single depth parameter, mechanically verify all results — is a clean template for building benchmarks in the calculator regime. [just-a-reference]

## Limitations (our opinion)

**What was not tested:**

- **Only tested in the hard-oracle regime.** Convexity verification via DCP rules is deterministic and mechanically verifiable. The paper does not test whether the agentic framework generalises to tasks where correctness is not mechanically checkable — soft-oracle problems where the LLM's judgment is genuinely needed at the aggregation level. The scheduling model notes in this KB ([symbolic-scheduling](../notes/bounded-context-orchestration-model.md)) predict the framework should work, but the empirical evidence here is restricted to the easy end of the [oracle-strength spectrum](../notes/oracle-strength-spectrum.md).

- **Narrow task domain.** The compositional structure tested (function composition with DCP rules) is highly regular — each sub-problem has the same structure. Real-world compositional reasoning (multi-step code generation, research synthesis, architectural design) involves heterogeneous sub-problems where decomposition strategies vary at each level. The clean recursive structure may flatter the divide-and-conquer approach.

- **No adversarial or ambiguous cases.** All benchmark instances have mechanically determined ground truth. The paper does not test what happens when sub-problems are genuinely ambiguous or when the DCP rules themselves are insufficient to determine convexity (e.g., functions that are convex but not DCP-representable). This limits the relevance to tasks where [codification](../notes/codification.md) fully covers the problem — which is the minority of interesting agent tasks.

- **Token usage as a proxy for reasoning effort.** The "lazy reasoning" diagnosis rests on observing token usage plateaus, but token count is a crude proxy. The paper does not analyse the actual reasoning traces to confirm whether models are genuinely reasoning less or simply repeating different patterns. Chain-of-thought inspection could have strengthened this claim.

- **No comparison to non-recursive structured approaches.** The paper compares one-shot, decomposition, agentic recursive, and focused-context approaches, but does not test iterative (non-recursive) approaches — e.g., processing the expression left-to-right with a running summary, or using a different traversal order. The claim that "recursive decomposition" is necessary (vs. any structured decomposition) is not tested.

## Recommended Next Action

Write a note titled "Compositional depth is the binding constraint, not context length" connecting to [context-efficiency](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md), [scoping](../notes/llm-context-is-composed-without-scoping.md), and [decomposition rules](../notes/decomposition-rules-for-bounded-context-scheduling.md) — it would argue that long-context capability and long-horizon reasoning capability are architecturally independent, synthesizing ConvexBench's empirical evidence (F1 collapse at 5k tokens), the induction-bias paper's mechanistic explanation (kappa near 1), and the KB's existing theoretical framework around bounded context scheduling. This codifies a claim that multiple notes and sources converge on but none explicitly state.
