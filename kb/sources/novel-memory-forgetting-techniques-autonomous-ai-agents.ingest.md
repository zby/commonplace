---
description: Formula-based adaptive forgetting with constrained optimization for agent memory — the inspectable alternative to RL-trained memory policy, with empirical evidence that uncontrolled accumulation causes false memory propagation
source_snapshot: novel-memory-forgetting-techniques-autonomous-ai-agents.md
ingested: "2026-04-04"
type: kb/sources/types/ingest-report.md
source_type: scientific-paper
domains: [agent-memory, context-efficiency, memory-curation, forgetting]
---

# Ingest: Novel Memory Forgetting Techniques for Autonomous AI Agents

Source: novel-memory-forgetting-techniques-autonomous-ai-agents.md
Captured: 2026-04-04
From: https://arxiv.org/html/2604.02280v1

## Classification

Type: scientific-paper — preprint with methodology, benchmark evaluation (LOCOMO, LOCCO, MultiWOZ 2.4), and quantitative results.
Domains: agent-memory, context-efficiency, memory-curation, forgetting
Author: Payal Fofadiya, Sunil Tiwari — not previously encountered in this KB; no strong prior signal on their experience. The work is evaluated on standard benchmarks, so the methodology can be assessed independently of author reputation.

## Summary

The paper introduces an adaptive budgeted forgetting framework for long-horizon conversational agents. Rather than accumulating memory without bound or training a policy to manage it (as AgeMem does), the framework uses an explicit, inspectable relevance-scoring formula combining recency, usage frequency, and semantic alignment with current queries. Memory selection is formulated as a constrained optimization problem: retain the highest-importance elements under a fixed budget while pruning the rest. Exponential decay prevents abrupt forgetting. Evaluated on three benchmarks (LOCOMO for 600+ turn dialogues, LOCCO for long-term persistence, MultiWOZ 2.4 for task-oriented dialogue), the framework achieves improved F1 scores and reduced false memory rates without increasing context usage, demonstrating "performance stability under bounded memory growth."

## Connections Found

The connection report identified 9 genuine connections, with the strongest being:

1. **[memory-management-policy-is-learnable-but-oracle-dependent](../notes/memory-management-policy-is-learnable-but-oracle-dependent.md)** — extends: this paper offers the inspectable, formula-based counterpart to AgeMem's opaque, RL-trained memory policy. Both confirm that memory management decomposes into selection and distillation, but they sit at opposite ends of an inspectability-learnability tradeoff. AgeMem learns *when* to forget through weights; this paper specifies *when* through an explicit formula.

2. **[agentic-memory-systems-comparative-review](../agent-memory-systems/agentic-memory-systems-comparative-review.md)** — extends: fills the "curation frontier" gap — none of the eleven reviewed systems implement bounded forgetting as a first-class operation. This paper adds a new position on the agency model dimension: developer-designed relevance formula (neither agent-self-managed nor RL-trained).

3. **[flat-memory-predicts-specific-cross-contamination-failures](../notes/flat-memory-predicts-specific-cross-contamination-failures-that-are.md)** — extends with empirical evidence: the paper's finding that uncontrolled memory accumulation causes "false memory propagation" is direct evidence for predicted failure mode #1 (operational debris pollutes search).

4. **[notes-need-quality-scores-to-scale-curation](../notes/notes-need-quality-scores-to-scale-curation.md)** — enables: the paper's relevance scoring formula (recency + frequency + semantic alignment) is a tested implementation of note quality scoring for curation at scale.

5. **[context-efficiency-is-the-central-design-concern](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md)** and **[entropy-management-must-scale-with-generation-throughput](../notes/entropy-management-must-scale-with-generation-throughput.md)** — exemplifies both: the framework is a concrete technical response to context scarcity, and its continuous forgetting is entropy management at conversational scale.

A synthesis opportunity was identified: an inspectability-learnability spectrum for memory management policy across four systems (this paper, AgeMem, Cludebot, cass-memory), with the paper's formula-based approach trading adaptability for inspectability.

## Extractable Value

1. **Inspectable forgetting as the formula-based complement to RL-trained policy.** The paper's relevance scoring formula (recency + frequency + semantic alignment) is fully inspectable and debuggable — you can see why a memory was pruned. This is the concrete counterexample to AgeMem's opaque policy. High reach: the inspectability-vs-learnability tradeoff applies to any system that manages accumulated artifacts under constraints. [quick-win] — update the memory-management-policy note to name this paper as the inspectable-side case.

2. **Constrained optimization framing for forgetting.** Formulating memory retention as "maximize importance subject to a budget constraint" is a clean abstraction that separates the scoring function (which memories matter) from the selection mechanism (how to choose under a budget). This decomposition transfers to KB curation: what to keep when note count exceeds a working set. Medium reach: the framing is general, but the specific optimization setup is tuned to conversational memory. [experiment] — test whether the optimization framing helps think about KB note retirement.

3. **Empirical evidence for false memory from uncontrolled accumulation.** The paper provides benchmark-level evidence that growing memory without pruning causes false memory propagation. This is the first quantitative evidence in this KB for the failure mode predicted by the flat-memory note. High reach: the mechanism (noise from accumulation degrades retrieval) is domain-independent. [quick-win] — cite in the flat-memory predictions note.

4. **Three-dimensional relevance scoring (recency, frequency, semantic alignment).** The three dimensions map onto scoring concepts already in the KB: recency (same as in the quality-scores note), frequency (analogous to inbound link count as usage signal), semantic alignment (analogous to type-based relevance). Having a tested three-factor formula grounds the otherwise theoretical quality-scores note. Medium reach: the specific weights are benchmark-tuned, but the three dimensions are general. [just-a-reference] — the KB already has this structure; the paper confirms it works.

5. **Exponential decay as adaptive forgetting mechanism.** Both Cludebot and cass-memory use exponential decay, but this paper adds the constrained-optimization wrapper that makes decay budget-aware rather than purely time-driven. The distinction matters: passive decay can still overshoot or undershoot the budget; constrained optimization enforces a hard bound. Low reach: the improvement is architectural, specific to systems with hard memory limits. [just-a-reference]

6. **Performance stability under bounded memory growth.** The core empirical result — matching or exceeding unbounded-accumulation performance while staying within a fixed budget — is the existence proof that forgetting doesn't require performance sacrifice. High reach: this result challenges the default assumption that more memory is always better. [deep-dive] — worth tracking whether the result replicates across different agent architectures.

## Curiosity Gate

**What is most surprising?** The paper claims that controlled forgetting *improves* performance rather than merely maintaining it under a budget constraint. If true, this means accumulated memory is actively harmful past some threshold — not just wasteful but degrading. This aligns with the false-memory prediction but goes further: it's not just search pollution but reasoning contamination. The surprise is that the improvement comes from *removing* information, not from better retrieval over the same information.

**What's the simpler account?** The improvement could be entirely due to reduced noise in retrieval — with fewer memories to search over, the relevant ones surface more reliably. This is just "less hay, easier to find the needle" — no sophisticated forgetting theory required. The constrained optimization may be doing most of its work simply by keeping the memory store small, not by the specific formula for what to keep. A random-pruning baseline that maintained the same budget would distinguish these explanations.

**Is the central claim hard to vary?** The claim "selective forgetting under budget constraints improves long-horizon reasoning" depends on: (1) the scoring formula correctly identifying what to keep, (2) the budget being tight enough that noise matters, and (3) the benchmarks requiring long-horizon retrieval. Removing component (1) — using random pruning — would test whether selectivity matters. Removing component (2) — using a very large budget — would test whether the budget constraint does the work. The claim is moderately hard to vary, but the paper doesn't test these ablations, which weakens confidence that the formula specifically (rather than budget control generally) drives the result.

## Limitations (our opinion)

**Missing baselines and ablations.** The paper does not compare against random pruning under the same budget constraint. Without this, we cannot distinguish "selective forgetting helps" from "smaller memory stores help." The KB's [memory-management-policy note](../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) identifies that composition policy is the hard part — but this paper doesn't demonstrate that its specific formula outperforms simpler alternatives for the selection component.

**No comparison to learned forgetting.** AgeMem's RL-trained policy addresses the same problem (when to forget) with a different mechanism (learned weights vs explicit formula). The paper does not compare to AgeMem or any learned-policy baseline. Without this, the inspectability-learnability tradeoff is asserted rather than measured.

**Conversational-agent-specific benchmarks only.** LOCOMO, LOCCO, and MultiWOZ are all conversational dialogue benchmarks. The paper's claims about "autonomous AI agents" are broader than what the evaluation supports. Whether constrained forgetting helps for task-oriented agents (ALFWorld, WebArena), knowledge-management agents, or multi-agent systems is untested. The reach of the results is lower than the framing implies.

**Fixed budget assumption.** The framework assumes a fixed memory budget. The KB's [soft-degradation note](../notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) argues that usable context varies by task complexity. A fixed-budget forgetting framework may be over-pruning for simple tasks and under-pruning for complex ones. The paper does not address adaptive budget sizing.

**Snapshot quality limits detailed assessment.** The arxiv HTML snapshot captures the paper's structure and key claims but may lose some quantitative detail (exact F1 scores, ablation tables, statistical significance tests). Our assessment of the empirical strength is based on the framework description and qualitative results summary rather than full numerical analysis.

## Recommended Next Action

Update [memory-management-policy-is-learnable-but-oracle-dependent](../notes/memory-management-policy-is-learnable-but-oracle-dependent.md): add a section or paragraph naming this paper as the inspectable-side counterpart to AgeMem's opaque-side approach, establishing the inspectability-learnability spectrum for memory management policy. This would ground the synthesis opportunity the connection report identified and make the tradeoff explicit in the note that already anchors this KB's analysis of memory management policy.
