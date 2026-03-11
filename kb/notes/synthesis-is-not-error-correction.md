---
description: Synthesis propagates errors by merging all agent outputs; voting corrects errors by discarding minorities — Kim et al.'s 17.2× amplification is a synthesis failure, not evidence against multi-agent coordination
type: note
areas: [llm-interpretation-errors]
status: seedling
---

# Synthesis is not error correction

Kim et al.'s [Towards a Science of Scaling Agent Systems](../sources/towards-a-science-of-scaling-agent-systems.ingest.md) reports that multi-agent systems hurt performance on average (-3.5% mean, up to 17.2× error amplification). Meyerson et al.'s [MAKER](../sources/meyerson-maker-million-step-llm-zero-errors.ingest.md) achieves zero errors over a million LLM steps. The results seem contradictory but aren't — the headline Independent topology result (17.2× error amplification) reflects a fundamentally different operation on agent outputs than MAKER's voting.

## The distinction

**Synthesis** merges outputs from multiple agents into a combined result. It tries to preserve information from all contributors. If three agents produce analyses and one contains an error, synthesis folds that error into the merged output. There is no mechanism to detect that agent 2 contradicts agents 1 and 3.

**Voting** selects the most common answer and discards minorities. It deliberately throws away information — that's the point. If two out of three agents agree, the dissenter's output is dropped entirely. Errors survive only if they're shared by a majority.

Synthesis is information aggregation. Voting is error correction. They solve different problems and have opposite failure modes: synthesis fails by propagating errors, voting fails by discarding correct minority answers.

## What Kim et al. actually tested

Kim et al.'s "Independent" topology — the one showing 17.2× error amplification — uses what the paper calls **"synthesis-only coordination"**: 3 agents run in parallel and their outputs are combined. The paper doesn't detail the synthesis mechanism, but the key point is that it's not voting — outputs are merged rather than compared for agreement. Despite mentioning "majority voting" as a design option for orchestrators, voting was not implemented in the tested configurations.

The other topologies add verification but not voting:
- **Centralized** (4.4× error amplification): an orchestrator reviews sub-agent outputs — acting as a soft oracle, partially filtering errors
- **Decentralized** (7.8×): agents debate across 3 rounds — closer to adversarial review than voting
- **Hybrid** (5.1×): combines both, but with 515% overhead

The progression 17.2× → 7.8× → 4.4× tracks increasing verification strength, not voting. Even partial verification (centralized orchestrator) cuts error amplification by 4×. The Hybrid topology (5.1×) breaks this ordering despite combining both verification mechanisms — possibly because its 515% overhead introduces coordination-failure modes that offset the verification benefit.

## What MAKER tested

MAKER uses first-to-ahead-by-k voting on maximally decomposed micro-steps (one Hanoi move per agent call). Three design choices make this work:

1. **Maximal decomposition** — each step has a single atomic answer, making voting well-defined (you can count which answer occurs most often)
2. **Hard per-step oracles** — each Hanoi move is deterministically correct or incorrect, so the problem supplies a ground truth that voting can converge toward
3. **Decorrelation** — red-flagging (discarding responses >700 tokens or with format violations) removes the output class most likely to carry correlated errors; temperature variation adds sampling diversity. These measures push toward the i.i.d. error assumption that makes voting's statistical guarantees hold

None of these are present in Kim et al.'s design: no decomposition (whole tasks given to agents), no explicit oracle, no decorrelation (identical prompts and tools across agents).

## Why this matters for the computational model

The [scheduling model](./bounded-context-orchestration-model.md) decomposes agent work into bounded LLM calls managed by a symbolic scheduler. The question of what to do with multiple agent outputs is a scheduler design decision, and synthesis vs voting are different scheduler operations with different properties:

- **Synthesis** is appropriate when agents produce complementary partial information (e.g., different sections of a document, different aspects of an analysis). The scheduler's job is assembly.
- **Voting** is appropriate when agents produce competing complete answers to the same question. The scheduler's job is selection via [error correction](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md).

Kim et al.'s Independent topology applies synthesis where voting would be more appropriate — agents solve the same complete task independently, but their outputs are merged rather than compared. This is a gap in the experimental design (voting with decorrelation was never tested), not evidence that multi-agent coordination is inherently negative-sum.

The [decomposition rules](./decomposition-rules-for-bounded-context-scheduling.md) should account for this: when decomposing a task into parallel bounded calls, the aggregation operation (synthesis vs voting vs something else) must match the relationship between the calls. Redundant calls solving the same sub-problem need voting. Complementary calls solving different sub-problems need synthesis.

## Open questions

- Structured adversarial review (Kim et al.'s Decentralized debate) may be a third category rather than a point on a synthesis-voting spectrum. Debate is iterative refinement through disagreement — agents revise their outputs in response to criticism, rather than merging or selecting. Its 7.8× error amplification (between synthesis's 17.2× and centralized verification's 4.4×) suggests partial error-correction benefit, but the mechanism is different from both.
- Can you combine synthesis and voting? E.g., decompose a complex task, have multiple agents attempt each sub-task (vote to select), then synthesize across sub-tasks. This would be the scheduling model operating with redundancy at the sub-task level.
- MAKER's success depends on maximal decomposition making voting well-defined (single atomic answers). For tasks where decomposition produces sub-tasks with complex outputs, how do you define "majority agreement"? Semantic similarity? Structural equivalence? This is where the [oracle strength](./oracle-strength-spectrum.md) question bites — you need a way to determine when two complex outputs "agree."

---

Relevant Notes:

- [error-correction-works-above-chance-oracles-with-decorrelated-checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — foundation: the theoretical framework for when voting-based error correction works (TPR > FPR, decorrelated checks); this note adds that synthesis doesn't qualify
- [bounded-context-orchestration-model](./bounded-context-orchestration-model.md) — extends: synthesis vs voting is a scheduler aggregation decision that should match the relationship between bounded calls
- [decomposition-rules-for-bounded-context-scheduling](./decomposition-rules-for-bounded-context-scheduling.md) — extends: aggregation operation must match decomposition structure (redundant calls → vote, complementary calls → synthesize)
- [oracle-strength-spectrum](./oracle-strength-spectrum.md) — grounds: voting requires an oracle to define "agreement"; oracle strength determines whether voting is viable for complex outputs
- [Kim et al.](../sources/towards-a-science-of-scaling-agent-systems.ingest.md) — evidence: 17.2× error amplification with synthesis-only Independent topology vs 4.4× with centralized verification
- [MAKER](../sources/meyerson-maker-million-step-llm-zero-errors.ingest.md) — evidence: zero errors over 1M steps using first-to-ahead-by-k voting with maximal decomposition and decorrelation

Topics:

- [llm-interpretation-errors](./llm-interpretation-errors.md)
