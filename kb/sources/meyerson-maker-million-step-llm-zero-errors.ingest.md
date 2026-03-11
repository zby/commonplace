---
description: MAKER achieves zero errors over one million LLM steps via maximal decomposition into single-step microagents with first-to-ahead-by-k voting and red-flagging — proves O(s ln s) cost scaling when hard per-step oracles exist
source_snapshot: meyerson-maker-million-step-llm-zero-errors.md
ingested: 2026-03-09
type: scientific-paper
domains: [multi-agent-systems, error-correction, scaling-laws, reliability-engineering]
---

# Ingest: Solving a Million-Step LLM Task with Zero Errors

Source: meyerson-maker-million-step-llm-zero-errors.md
Captured: 2026-02-26
From: https://arxiv.org/abs/2511.09030

## Classification

Type: **scientific-paper** — Preprint with formal scaling-law derivations (probabilistic analysis of voted micro-steps), controlled experiments on the Towers of Hanoi benchmark across 10 models, cost projections, and empirical validation of a million-step zero-error run.

Domains: multi-agent-systems, error-correction, scaling-laws, reliability-engineering

Author: Meyerson et al. at Cognizant AI Lab; Risto Miikkulainen (UT Austin & Cognizant). Miikkulainen is a well-known evolutionary computation researcher. Industry lab paper with academic rigor — formal proofs plus production-cost analysis.

## Summary

MAKER introduces "massively decomposed agentic processes" (MDAPs), a framework that decomposes LLM tasks to the finest possible granularity (one step per agent call), then applies first-to-ahead-by-k voting across independent samples to correct errors at each micro-step. The key theoretical result is that cost scales as O(s ln s) under maximal decomposition (m=1), compared to exponentially without it. A red-flagging mechanism discards responses whose structure signals unreliability (excessive length, format violations), reducing correlated errors that would defeat independent voting. Applied to the 20-disk Towers of Hanoi (1,048,575 steps), MAKER achieves zero errors using gpt-4.1-mini at approximately $3,500. The paper's most provocative claim is that small non-reasoning models suffice when decomposition is maximal — architectural error correction substitutes for model intelligence. The authors distinguish "insights" (creative, open-ended) from "execution" (plan-following) and acknowledge their framework currently addresses only execution, where per-step oracles are hard.

## Connections Found

`/connect` identified 11 connections total — 2 already linked from KB notes, 9 new.

**Already linked (notes reference MAKER directly):**

1. **[error-correction-works-above-chance-oracles-with-decorrelated-checks](../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md)** — grounds: MAKER is the primary empirical grounding for this note. The note generalizes MAKER's voting to soft oracles with TPR > FPR; the O(s ln s) scaling law is referenced as the cost baseline.

2. **[reliability-dimensions-map-to-oracle-hardening-stages](../notes/reliability-dimensions-map-to-oracle-hardening-stages.md)** — exemplifies: MAKER's voting is consistency hardening; red-flagging is predictability hardening. The note identifies MAKER as "architectural oracle hardening."

**New connections (not yet linked from any note):**

3. **[oracle-strength-spectrum](../notes/oracle-strength-spectrum.md)** — exemplifies: MAKER succeeds because Towers of Hanoi has hard per-step oracles (each move is deterministically verifiable). The insights/execution distinction maps directly onto the oracle gradient. The O(s ln s) result only holds given sufficient oracle strength. The oracle-strength note lacks this concrete success case.

4. **[bitter-lesson-boundary](../notes/bitter-lesson-boundary.md)** — exemplifies: MAKER is the anti-bitter-lesson bet succeeding in the calculator regime. Small non-reasoning models (gpt-4.1-mini) outperform reasoning models (o3-mini) on cost-effectiveness because the spec IS the problem. Direct empirical evidence for the note's claim that calculators survive scaling.

5. **[symbolic-scheduling-over-bounded-llm-calls](../notes/bounded-context-orchestration-model.md)** — exemplifies: MAKER is a concrete million-step instance of the scheduling model. The symbolic scheduler manages task state (disk configuration), decomposes into per-step sub-goals, and assembles minimal prompts for bounded LLM calls. Deterministic code does the bookkeeping; only single-step move decisions use LLM calls. Key difference: MAKER's decomposition is predetermined (recursive Hanoi structure), not discovered dynamically.

6. **[decomposition-rules-for-bounded-context-scheduling](../notes/decomposition-rules-for-bounded-context-scheduling.md)** — exemplifies: Maximal agentic decomposition (m=1) is the extreme case of "separate selection from joint reasoning." Each agent gets only the minimal context needed for its single step. The cost analysis (O(s ln s) for m=1 vs exponential for m>1) provides quantitative evidence for aggressive decomposition into narrow calls. Also exemplifies "use symbolic operations wherever exactness is available" — Hanoi recursion and state tracking are symbolic, not LLM-mediated.

7. **[spec-mining-as-codification](../notes/spec-mining-as-codification.md)** — enables: Spec mining manufactures the hard oracles that MAKER depends on. MAKER assumes per-step oracles exist; spec mining is the operational mechanism for creating them in domains where they don't naturally exist. The progression: mine a spec (create an oracle), then MAKER-style voting amplifies it.

8. **[towards-a-science-of-scaling-agent-systems](towards-a-science-of-scaling-agent-systems.ingest.md)** (source) — contradicts/complements: Kim et al. find naive multi-agent coordination yields -3.5% mean improvement with up to 17.2x error amplification. MAKER achieves zero errors over a million steps. The difference: MAKER's extreme decomposition + voting vs Kim et al.'s tested topologies (Independent, Centralized, Decentralized, Hybrid) which use simple coordination without deliberate decorrelation. Brackets the multi-agent question from both sides.

9. **[induction-bias-sequence-models](induction-bias-sequence-models-ebrahimi-2026.ingest.md)** (source) — complements: Ebrahimi et al. explain WHY transformers fail at long-range state tracking (kappa near 1, knowledge at one length doesn't transfer). MAKER shows HOW to build reliable systems despite that failure. Two papers bracket the same problem from opposite directions.

10. **[voooooogel-multi-agent-future](./voooooogel-multi-agent-future.ingest.md)** — extends (with tension): MAKER's microagents are the extreme endpoint of multi-agent isolation. But they don't collaborate, negotiate, or share context — they independently vote on single-step decisions. Voooooogel predicts stronger models dissolve fixed multi-agent architectures; MAKER's voting is structural error correction (redundancy that survives model improvement), not a role hierarchy that better models could absorb.

11. **[Evans: AI Components for a Deterministic System](./eric-evans-ai-components-deterministic-system.ingest.md)** — parallels: Evans' modeling/classification distinction maps to MAKER's insights/execution split. Both identify a boundary where LLMs are reliable (classification/execution with hard oracles) vs unreliable (modeling/insights with soft oracles). Both prescribe constraining strategies for the hard-oracle regime.

**Key synthesis insight**: Oracle strength determines the ceiling for multi-agent error correction. Voting architectures are viable only in the calculator regime; extending MDAP to soft-oracle domains (insights, creative tasks) is the genuine open problem. A synthesis note could formalize this by combining oracle-strength-spectrum, error-correction-works-above-chance-oracles, MAKER, scaling-agent-systems, and bitter-lesson-boundary.

## Extractable Value

1. **The O(s ln s) scaling law for voted micro-steps**: Formal proof that cost grows log-linearly with task length under maximal decomposition, compared to exponentially without it. The oracle-strength-spectrum note currently lacks this quantitative teeth. [quick-win]

2. **Red-flagging as decorrelation mechanism**: Overly long responses and format violations correlate with errors. Discarding them reduces correlated errors — the kind that defeat voting. This is a concrete, implementable predictability-hardening technique with empirical backing. Distinct from the existing error-correction note's theoretical treatment. [quick-win]

3. **Insights vs execution as oracle-strength categories**: The paper's own distinction maps cleanly onto our oracle-strength spectrum. Execution = hard oracle (deterministic correct answer); insights = soft oracle (irreducible uncertainty). This vocabulary could sharpen the spectrum note. [quick-win]

4. **Small models suffice in the calculator regime**: gpt-4.1-mini outperforms o3-mini on cost-effectiveness for execution tasks. Empirical confirmation that reasoning models are overkill when the task is execution with hard oracles — directly relevant to model selection for codified operations. [quick-win]

5. **Multi-agent advantage as an empirical threshold**: A concrete case where a multi-agent system solves something a single agent provably cannot (at any temperature or prompt). The "multi-agent advantage" concept (analogous to quantum advantage) is a useful frame for reasoning about when decomposition crosses from overhead to necessity. [just-a-reference]

6. **The limits question: which tasks resist maximal decomposition?**: The paper explicitly flags this as the central open problem. Tasks requiring global coherence, creative leaps, or context that cannot be compressed into a single step may resist MDAP. This is where the bitter-lesson-boundary thinking applies. [deep-dive]

7. **Microservices analogy for microagent architecture**: Nine-point parallel between microservices and microagents (modularity, data management, independent development, scalability, communication protocol, design for failure, evolutionary design). Useful conceptual mapping if we formalize agent decomposition principles. [just-a-reference]

## Limitations (our opinion)

**Domain specificity not sufficiently acknowledged.** Towers of Hanoi is the ideal case for MAKER: each step has a single correct move deterministically derivable from the current state, the state representation is compact and lossless, and the decomposition structure is known in advance (recursive). The paper's claims about extending to "organization-level problems" and "societal-scale tasks" are not supported by any evidence beyond this single domain. Real-world tasks typically have: ambiguous per-step correctness (soft oracles), state representations that grow or resist compression, and decomposition structures that must be discovered rather than given.

**The insights/execution boundary is acknowledged but underexplored.** The paper admits its framework handles only execution and treats insights as future work, yet the Discussion section speculates about superintelligence-scale applications that would necessarily involve insight generation. The gap between "we solved Towers of Hanoi" and "this scales to hospital operations" is vast and not bridged by analogy. Our [oracle-strength-spectrum](../notes/oracle-strength-spectrum.md) note provides the framework for understanding why: as oracle strength decreases, voting's effectiveness degrades, and most real-world tasks have soft oracles for at least some steps.

**Correlated errors are mitigated, not solved.** Red-flagging is shown to reduce correlated errors empirically, but the paper acknowledges "a few steps that, for no apparent reason, had substantially higher inherent error rates." These are handled by brute-force additional sampling. The theoretical analysis assumes i.i.d. errors; the gap between this assumption and reality is acknowledged but not quantified. In domains with systematic biases (e.g., LLM training distribution artifacts), correlated errors could be far more prevalent and resistant to red-flagging than in Towers of Hanoi.

**Cost analysis assumes stable API pricing.** The $3,500 cost for the million-step run depends on current per-token pricing for gpt-4.1-mini. The cost scaling law (O(s ln s)) is model-agnostic, but practical viability for any real application depends on absolute cost, not just asymptotic scaling. No analysis of how cost scales with domain complexity (prompt length, state representation size) beyond the constant-cost Hanoi case.

**No comparison with non-LLM baselines.** For Towers of Hanoi specifically, a deterministic algorithm solves the problem in O(2^n - 1) steps with zero errors and negligible cost. The paper acknowledges this but argues the domain is a testbed, not a target application. Fair enough, but the absence of any non-trivial domain where MAKER outperforms traditional approaches limits the paper's practical claims.

## Recommended Next Action

Update `kb/notes/oracle-strength-spectrum.md`: add a section on "Architectural error correction and oracle strength" capturing the key insight — voting-based error correction (MAKER-style) is viable only when per-step oracle strength is sufficient (hard oracles). Reference the O(s ln s) scaling law as the quantitative payoff when oracles are hard enough, and the insights/execution distinction as evidence that the authors themselves recognize oracle strength as the binding constraint. Cite the MAKER source and the scaling-agent-systems source (Kim et al.) as the positive and negative cases respectively.
