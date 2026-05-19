---
description: "Outer-loop learning depends on inspectable failure evidence, not only on the oracle used to select winning candidates"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory]
status: current
---

# Diagnostic richness constrains outer-loop learning quality

Outer-loop learning improves a system by proposing candidate changes, evaluating them, and feeding the result into the next proposal. This note distinguishes two separable evidential bottlenecks in that loop. The oracle decides which candidates deserve promotion. Diagnostic richness decides what the proposer can infer from previous attempts before generating the next candidate. Proposer capability and search policy also matter, but they are separate from the evidence surfaces this note isolates.

Diagnostic richness is the amount and structure of retained evidence available for explanation: scores, diffs, traces, tool calls, memory state, candidate files, frontier state, and drill-down paths back to raw evidence. Frontier state means the current-best candidate set or ranking maintained by the search loop. A strong oracle can rank candidates without explaining why they worked. A rich diagnostic substrate exposes mechanisms: which tool failed, which prompt branch activated, which memory item was read, which candidate changed behavior, and which failure mode repeated.

That makes diagnostic richness orthogonal to [oracle strength](./oracle-strength-spectrum.md). Oracle strength names the quality and cost of selection. Diagnostic richness names the quality of the search context. Scores-only feedback can support promotion, but it gives the next proposer little basis for hypothesis formation. Raw traces and structured derived views cost more context, but they let the proposer search through causes rather than only outcomes.

[Meta-Harness](../sources/meta-harness-end-to-end-optimization-of-model-harnesses.md), a framework for optimizing task-specific model harnesses with prior code, scores, and traces, makes the gradient concrete through its text-classification ablation. A proposer with access to raw execution traces reached median 50.0% accuracy, while scores-only and scores-plus-summary variants reached 34.6% and 34.9%. The selection setup was comparable; proposal quality changed when the proposer could inspect richer evidence. The lesson is not "load everything." The lesson is that outer-loop search cannot improve from diagnostic information it never receives.

Richness still needs staging. Agentic Harness Engineering, an observability-driven coding-agent harness evolution loop, keeps raw traces available but normally feeds root-cause reports first to the evolve agent, the component that proposes harness changes. HALO, a trace-analysis engine for agent harnesses, indexes byte offsets, exposes bounded trace tools, summarizes oversized spans, and preserves drill-down paths to raw evidence. These systems treat summaries and indexes as navigation surfaces, not as replacements for evidence.

For KB and harness-learning loops, the design implication is direct: keep selection signals and diagnostic surfaces separate. A frontier file, score table, or review decision can tell the next agent what won; it cannot by itself tell the agent what to try next. Durable learning loops need enough retained evidence for later proposers to form causal hypotheses, plus enough progressive disclosure from summaries to raw evidence to keep that evidence affordable inside a bounded context.

---

Relevant Notes:

- [oracle strength spectrum](./oracle-strength-spectrum.md) — contrasts: oracle strength names candidate selection quality, while diagnostic richness names proposal evidence quality
- [Trace-derived learning techniques in related systems](../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) — evidence: survey paragraph and Meta-Harness ablation ground the diagnostic-richness axis
- [Ingest: Meta-Harness: End-to-End Optimization of Model Harnesses](../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) — evidence: local digest of the paper and its diagnostic-richness synthesis opportunity
- [Meta-Harness](../agent-memory-systems/reviews/meta-harness.md) — evidence: raw trace access improved proposer performance over scores-only and scores-plus-summary variants
- [Agentic Harness Engineering](../agent-memory-systems/reviews/agentic-harness-engineering.md) — exemplifies: root-cause reports compress traces while keeping raw evidence available for audit
- [HALO](../agent-memory-systems/reviews/halo.md) — exemplifies: bounded trace tools preserve drill-down from summaries and indexes to raw spans
