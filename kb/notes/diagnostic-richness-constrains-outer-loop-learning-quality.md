---
description: "Outer-loop learning depends on inspectable failure evidence, not only on the oracle used to select winning candidates"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, deploy-time-learning]
---

# Diagnostic richness constrains outer-loop learning quality

Outer-loop learning improves a system by proposing candidate changes, evaluating them, and feeding the result into the next proposal. This note distinguishes two separable evidential bottlenecks in that loop. The oracle decides which candidates deserve promotion. Diagnostic richness decides what the proposer can infer from previous attempts before generating the next candidate. Proposer capability and search policy also matter, but they are separate from the evidence surfaces this note isolates.

Diagnostic richness is the amount and structure of retained evidence available for explanation: scores, diffs, traces, tool calls, memory state, candidate files, frontier state, and drill-down paths back to raw evidence. Frontier state means the current-best candidate set or ranking maintained by the search loop. A strong oracle can rank candidates without explaining why they worked. A rich diagnostic substrate exposes mechanisms: which tool failed, which prompt branch activated, which memory item was read, which candidate changed behavior, and which failure mode repeated.

That makes diagnostic richness orthogonal to [oracle strength](./oracle-strength-spectrum.md). Oracle strength names the quality and cost of selection. Diagnostic richness names the quality of the search context. Scores-only feedback can support promotion, but it gives the next proposer little basis for hypothesis formation. Raw traces and structured derived views cost more context, but they let the proposer search through causes rather than only outcomes.

[Meta-Harness](../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md), a framework for optimizing task-specific model harnesses, makes the gradient concrete through its online text-classification ablation. Every proposer arm could inspect prior scores and code. The Scores Only arm reached 34.6% median accuracy, the Scores + Summary arm reached 34.9% without traces, and the full arm reached 50.0% with traces. The fixed summary treatment therefore did not recover the trace-access arm in this setup. These are point summaries without a reported statistical-significance estimate, and the experiment tests one trace-removing summary treatment rather than summaries or abstraction in general. The bounded result supports this note's claim that a proposer cannot exploit diagnostic information it does not receive; it does not license the stronger instruction to "load everything."

Richness still needs staging. Agentic Harness Engineering, an observability-driven coding-agent harness evolution loop, keeps raw traces available but normally feeds root-cause reports first to the evolve agent, the component that proposes harness changes. HALO, a trace-analysis engine for agent harnesses, indexes byte offsets, exposes bounded trace tools, summarizes oversized spans, and preserves drill-down paths to raw evidence. These systems treat summaries and indexes as navigation surfaces, not as replacements for evidence.

For KB and harness-learning loops, the design implication is direct: keep selection signals and diagnostic surfaces separate. A frontier file, score table, or review decision can tell the next agent what won; it cannot by itself tell the agent what to try next. Durable learning loops need enough retained evidence for later proposers to form causal hypotheses, plus enough progressive disclosure from summaries to raw evidence to keep that evidence affordable inside a bounded context.

---

Relevant Notes:

- [oracle strength spectrum](./oracle-strength-spectrum.md) — contrasts: oracle strength names candidate selection quality, while diagnostic richness names proposal evidence quality
- [Trace-learning techniques in related systems](../agent-memory-systems/trace-learning-techniques-in-related-systems.md) — evidenced-by: survey paragraph and Meta-Harness ablation ground the diagnostic-richness axis
- [Ingest: Meta-Harness: End-to-End Optimization of Model Harnesses](../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) — evidenced-by: local digest of the paper and its diagnostic-richness synthesis opportunity
- [Meta-Harness](../agent-memory-systems/reviews/meta-harness.md) — evidenced-by: raw trace access improved proposer performance over scores-only and scores-plus-summary variants
- [Agentic Harness Engineering](../agent-memory-systems/reviews/agentic-harness-engineering.md) — exemplifies: root-cause reports compress traces while keeping raw evidence available for audit
- [HALO](../agent-memory-systems/reviews/halo.md) — exemplifies: bounded trace tools preserve drill-down from summaries and indexes to raw spans
