---
description: Ingest of NeurIPS 25 workshop paper benchmarking LLM web agents under long context (25k-150k tokens) with injected irrelevant task sequences — provides agent-level empirical evidence for soft degradation, loop entrapment, and objective loss, extending GSM-DC's distractor findings to multi-session agentic tasks.
source_snapshot: llm-webagents-long-context-reasoning-benchmark.md
ingested: "2026-03-26"
type: kb/sources/types/ingest-report.md
source_type: scientific-paper
domains: [context-degradation, agent-systems, web-agents, long-context-evaluation]
---

# Ingest: Evaluating Long-Context Reasoning in LLM-Based WebAgents

Source: llm-webagents-long-context-reasoning-benchmark.md
Captured: 2026-03-26
From: https://arxiv.org/html/2512.04307v1

## Classification

Type: **scientific-paper** — Peer-reviewed (NeurIPS 25 LAW Workshop), introduces a benchmark with controlled experimental design, measures four frontier models, reports quantitative results with failure-mode analysis.

Domains: context-degradation, agent-systems, web-agents, long-context-evaluation

Author: Andy Chung et al., with Joyce Chai (University of Michigan, well-known in grounded language understanding and interactive agents). The team is positioned at the intersection of language grounding and agent evaluation.

## Summary

Chung et al. introduce a benchmark for evaluating LLM-based web agents on long-context multi-session tasks. The experimental design injects irrelevant task sequences between dependent subtasks, scaling context from 25k to 150k tokens. Testing Claude-3.7, GPT-4.1, Llama 4, and o4-mini, they find success rates collapse from 40-50% at baseline to under 10% at 150k tokens. The dominant failure modes are loop entrapment (agents repeating actions without progress) and objective loss (agents forgetting or drifting from the original task goal). An implicit RAG (iRAG) approach that generates task-relevant summaries provides modest improvements but does not resolve the fundamental degradation. The paper's contribution is extending controlled irrelevant-context degradation measurements from isolated reasoning tasks to realistic agentic web interaction.

## Connections Found

The `/connect` discovery identified strong connections to 7 KB notes and 4 other sources, with the soft-degradation note as the primary hub.

**Core theory connections (notes):**
- **[agent-context-is-constrained-by-soft-degradation-not-hard-token-limits](../notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md)** — exemplifies: the benchmark provides direct empirical measurements for the soft-degradation claim at the agent level. The 40-50% to <10% collapse happens well below advertised context limits, driven by irrelevant context (complexity dimension) not volume alone. The failure modes (loops, lost objectives) are concrete manifestations of "missed instructions, hallucinates, ignores relevant document." The soft-degradation note already cites GSM-DC for the complexity dimension; this benchmark extends that evidence to agentic multi-session tasks.
- **[session-history-should-not-be-the-default-next-context](../notes/session-history-should-not-be-the-default-next-context.md)** — exemplifies: the benchmark's design literally constructs the failure this note warns about — irrelevant prior task sequences loaded as context is structurally identical to loading full session history by default.
- **[llm-context-is-composed-without-scoping](../notes/llm-context-is-composed-without-scoping.md)** — exemplifies: loop and lost-objective failures are manifestations of flat concatenation without scoped frames. If agents had scoping, irrelevant sequences would not be visible.
- **[effective-context-is-task-relative-and-complexity-relative-not-a-fixed-model-constant](../notes/effective-context-is-task-relative-and-complexity-relative-not-a.md)** — exemplifies: partially answers the note's open question about which natural-language tasks exhibit complexity-dominant collapse (web navigation, in this case). Also shows model-relative variation (o4-mini outperforms others despite similar challenges).
- **[context-efficiency-is-the-central-design-concern-in-agent-systems](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md)**, **[the-chat-history-model-trades-context-efficiency-for-implementation-simplicity](../notes/the-chat-history-model-trades-context-efficiency-for-implementation.md)**, **[llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model](../notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md)** — all exemplified by this benchmark.

**Cross-source connections:**
- **[gsm-dc-llm-reasoning-distracted-irrelevant-context](./gsm-dc-llm-reasoning-distracted-irrelevant-context.md)** — complements: GSM-DC measures irrelevant-context degradation in isolated math reasoning; this benchmark extends the same phenomenon to agentic web tasks with multi-session histories. Together they show the pattern is consistent across abstraction levels.
- **[paulsen-maximum-effective-context-window-mecw](./paulsen-maximum-effective-context-window-mecw.md)** — complements: Paulsen measures MECW for model-level tasks; this measures effective context for agent-level multi-session tasks. Both confirm nominal window size drastically overstates usable capacity.
- **[large-language-model-agents-are-not-always-faithful-self-evolvers](./large-language-model-agents-are-not-always-faithful-self-evolvers.md)** — complements: self-evolvers paper shows agents fail to use condensed experience even when provided; this shows iRAG provides only modest improvement. Both converge on: simply providing relevant information in a long context does not guarantee the agent will use it effectively.

**Synthesis opportunity:** Three sources (GSM-DC, ConvexBench, this benchmark) now document irrelevant-context degradation at different abstraction levels — isolated math reasoning, compositional symbolic reasoning, multi-session agentic web tasks. No note yet names this cross-level consistency or draws the implication that the degradation pattern appears to be a fundamental property of attention-based architectures rather than task-specific.

## Extractable Value

1. **Agent-level quantification of the soft degradation curve** — 40-50% baseline to <10% at 150k tokens provides a concrete data point for the soft-degradation note's claim that the binding constraint is silent, not hard. This is the first source that measures it at the agent-interaction level rather than single-call reasoning. High reach: the degradation mechanism (irrelevant context, not volume) transfers beyond web agents. [quick-win — cite in soft-degradation note]

2. **Failure-mode taxonomy at scale** — loops (44.3% for GPT-4.1) and objective loss are the dominant failure modes, not hallucination or tool errors. This names WHAT happens when soft degradation hits agent systems, which the existing notes theorize but don't empirically ground. Moderate reach: the specific failure modes may vary by agent architecture, but the loop/objective-loss distinction is likely general. [quick-win — cite in context-efficiency or llm-mediated-schedulers note]

3. **iRAG's modest improvement as evidence that bolt-on retrieval is insufficient** — the benchmark tests a reasonable RAG mitigation and finds it helps only modestly. This is evidence that the problem is architectural (scoping, selective loading) not informational (finding the right content). High reach: this transfers to any system attempting to fix context degradation with retrieval alone. [quick-win — cite in context-efficiency note]

4. **Partial answer to effective-context note's open question** — "Which natural-language tasks exhibit the same complexity-dominant collapse that ConvexBench shows in symbolic reasoning?" Web navigation with injected irrelevant sessions is one such task. Moderate reach: the answer is specific to this task class but extends the evidence base. [quick-win — add to open questions section]

5. **Model-relative variation** — o4-mini outperforms other models despite similar challenges, suggesting reasoning-focused models may have better soft-degradation resilience. Low reach without more data: one benchmark, one comparison. [just-a-reference]

6. **Cross-level consistency of irrelevant-context degradation** — together with GSM-DC and ConvexBench, this creates a three-point evidence base spanning isolated reasoning, compositional symbolic, and agentic multi-session tasks. High reach: if the pattern holds across these levels, it is likely a fundamental attention-architecture property. [deep-dive — synthesis note warranted]

## Limitations (our opinion)

**What was not tested:**

- **No scoping or selective-loading intervention.** The benchmark tests iRAG (a retrieval-based mitigation) but not the architectural response the KB's theory predicts would work: scoped context frames that prevent irrelevant sequences from entering the agent's context at all. The bounded-context orchestration model's `select(K)` step is the theoretically correct intervention; its absence means the benchmark measures the problem without testing the predicted solution.

- **Artificial distractor injection vs. organic accumulation.** The benchmark injects irrelevant task sequences in controlled positions between dependent subtasks. Real-world web agents accumulate context organically — failed attempts, UI noise, partially relevant exploration. The controlled injection is methodologically clean but may not capture the full complexity of organic context pollution, where relevance is graded rather than binary.

- **Limited model coverage for the key finding.** Four models tested, with o4-mini as the standout. The model-relative variation finding rests on a single benchmark configuration. Whether reasoning-focused models consistently resist soft degradation better would require broader evaluation.

- **iRAG is one retrieval strategy.** The paper tests one specific RAG approach. Dismissing retrieval-based mitigation based on one implementation is premature, though the finding is consistent with our theoretical expectation that the problem is scoping, not retrieval.

- **No measurement of the volume/complexity interaction.** The benchmark varies total context length (25k to 150k) but does not independently vary the proportion of irrelevant content at each length. This means the volume and complexity dimensions identified in the soft-degradation note cannot be cleanly separated in this data. We cannot distinguish "more tokens caused the degradation" from "more irrelevant tokens caused the degradation" — though the experimental design (injecting irrelevant sequences) strongly implies the latter.

## Recommended Next Action

Write a note titled "Irrelevant-context degradation is consistent across abstraction levels" connecting to [agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md](../notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md), [effective-context-is-task-relative-and-complexity-relative-not-a.md](../notes/effective-context-is-task-relative-and-complexity-relative-not-a.md), and the three sources (GSM-DC, ConvexBench, this benchmark) — it would argue that irrelevant-context degradation appears at isolated-reasoning, compositional-symbolic, and agentic-multi-session levels with structurally similar failure patterns, suggesting a fundamental attention-architecture property rather than a task-specific phenomenon, and that mitigation must therefore operate at the architectural level (scoping, selective loading) rather than the content level (summarization, RAG).
