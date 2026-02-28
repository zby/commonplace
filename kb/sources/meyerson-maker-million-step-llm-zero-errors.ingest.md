---
source_snapshot: meyerson-maker-million-step-llm-zero-errors.md
ingested: 2026-02-26
type: scientific-paper
domains: [multi-agent-systems, reliability-engineering, error-correction, scaling-laws]
---

# Ingest: Solving a Million-Step LLM Task with Zero Errors

Source: meyerson-maker-million-step-llm-zero-errors.md
Captured: 2026-02-26
From: https://arxiv.org/abs/2511.09030

## Classification

Type: **scientific-paper** — Preprint with formal scaling-law derivations, controlled experiments on Towers of Hanoi benchmark, cost projections across multiple models, and empirical validation of a million-step zero-error run.

Domains: multi-agent-systems, reliability-engineering, error-correction, scaling-laws

Author: Meyerson et al. at Cognizant AI Lab (with Risto Miikkulainen, UT Austin). Miikkulainen is a well-known evolutionary computation researcher; the team has production-oriented AI research credibility. This is an industry lab paper with academic rigor.

## Summary

MAKER introduces "massively decomposed agentic processes" (MDAPs), a framework that decomposes LLM tasks to the finest possible granularity (one step per agent call), then applies first-to-ahead-by-k voting across independent samples to correct errors at each micro-step. The key theoretical result is that cost scales as O(s ln s) under maximal decomposition, compared to exponential scaling without it. Applied to the 20-disk Towers of Hanoi (1,048,575 steps), MAKER achieves zero errors using gpt-4.1-mini at approximately $3,500. The paper's most provocative claim is that small non-reasoning models suffice when decomposition is maximal — architectural error correction substitutes for model intelligence. The authors distinguish "insights" (creative, open-ended) from "execution" (plan-following) and acknowledge their framework currently addresses only execution, where per-step oracles are hard.

## Connections Found

/connect identified eight connections spanning the core theory stack:

1. **towards-a-science-of-ai-agent-reliability** (complementary): Rabanser et al. measure the reliability dimensions MAKER is engineered to solve. Their finding that capability gains outpace reliability gains motivates MAKER's architectural approach.

2. **reliability-dimensions-map-to-oracle-hardening-stages** (extends): MAKER's voting is consistency hardening; red-flagging is predictability hardening. The entire MDAP framework is oracle hardening through architecture.

3. **oracle-strength-spectrum** (grounds): MAKER's viability depends on hard per-step oracles. The insights-vs-execution distinction maps onto the spectrum — execution has harder oracles, which is why MAKER targets it first. The O(s ln s) scaling law only holds when oracle strength is sufficient.

4. **bitter-lesson-boundary** (exemplifies): MAKER is the anti-bitter-lesson bet succeeding in the calculator regime. Small non-reasoning models suffice because the domain is calculator-like (spec IS the problem).

5. **stabilisation-is-learning** (parallels): Same reliability-over-training pattern, different mechanism (voting vs versioned artifacts).

6. **storing-llm-outputs-is-stabilization** (exemplifies): Voting is a generator/verifier pattern; red-flagging is the filter strategy.

7. **voooooogel-multi-agent-future** (extends): MAKER's microagents are the extreme endpoint of "multi-agent for context isolation." But these agents don't collaborate — they independently vote, a different pattern from cooperative multi-agent architectures.

8. **evans-ai-components-deterministic-system** (parallels): Evans' modeling/classification distinction parallels MAKER's insights/execution split.

**Key synthesis insight from /connect**: Oracle strength determines the ceiling for multi-agent error correction. MAKER's success depends entirely on hard per-step oracles. Combined with the reliability-dimensions framework, this implies voting architectures are viable only in the calculator regime, and extending MDAP to softer-oracle domains is the genuine open problem.

**Flagged tension**: MAKER claims MDAPs can scale to organization-level problems, but voooooogel predicts stronger models will dissolve fixed multi-agent architectures. Resolution may be that MAKER-style voting is structural (error correction that survives model improvement) while role-based hierarchies are not.

## Extractable Value

1. **The O(s ln s) scaling law for voted micro-steps**: Formal proof that cost grows log-linearly with task length under maximal decomposition, compared to exponentially without it. This is a concrete quantitative argument for decomposition that our oracle-strength-spectrum note currently lacks. [quick-win]

2. **Red-flagging as predictability hardening**: The insight that overly long responses and format violations are correlated with errors, and that discarding them reduces correlated (not just independent) errors. This is a concrete mechanism for our reliability-dimensions framework — a specific hardening technique with empirical backing. [quick-win]

3. **Insights vs execution as oracle-strength categories**: The paper's own distinction maps cleanly onto our oracle-strength-spectrum. Execution = hard oracle (deterministic correct answer exists), insights = soft oracle (open-ended, irreducible uncertainty). This vocabulary could sharpen the spectrum note. [quick-win]

4. **Multi-agent advantage as an empirical threshold**: The paper demonstrates a concrete case where a multi-agent system solves something a single agent provably cannot (at any temperature or prompt). This "multi-agent advantage" concept (analogous to quantum advantage) is a useful frame we don't currently have. [just-a-reference]

5. **Microservices analogy for microagent architecture**: The paper's nine-point parallel between microservices and microagents is a useful conceptual mapping for thinking about agent decomposition patterns. Relevant if we ever formalize our own agent decomposition principles. [just-a-reference]

6. **Small models suffice in the calculator regime**: gpt-4.1-mini outperforms o3-mini on cost-effectiveness for execution tasks. This is empirical confirmation that reasoning models are overkill when the task is execution with hard oracles — directly relevant to our model selection for crystallised operations. [quick-win]

7. **The limits question: which tasks resist maximal decomposition?** The paper explicitly flags this as the central open problem. Tasks requiring global coherence, creative leaps, or context that cannot be compressed into a single step may resist MDAP. This is where bitter-lesson-boundary thinking applies — and where our claw work on insights/judgment operates. [deep-dive]

## Recommended Next Action

Update `project_claw/notes/oracle-strength-spectrum.md`: add a section on "Architectural error correction and oracle strength" that captures the key insight — voting-based error correction (MAKER-style) is viable only when per-step oracle strength is sufficient (hard oracles). Reference the O(s ln s) scaling law and the insights/execution distinction as concrete evidence for the spectrum's practical implications. This sharpens the existing note from a conceptual taxonomy into one with quantitative teeth. The MAKER paper and reliability-dimensions note are the two sources to cite.
