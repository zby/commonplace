---
description: Synthesis propagates errors by merging all agent outputs; voting corrects errors by discarding minorities — Kim et al.'s 17.2× amplification is a synthesis failure, not evidence against multi-agent coordination
type: note
tags: [llm-interpretation-errors]
status: seedling
---

# Synthesis is not error correction

Merging agent outputs and selecting among them are fundamentally different operations. Synthesis propagates errors; voting corrects them. Conflating the two leads to misleading conclusions about whether multi-agent coordination works.

The concrete case: [Kim et al.](../sources/towards-a-science-of-scaling-agent-systems.ingest.md) report up to 17.2× error amplification in multi-agent systems. [MAKER](../sources/meyerson-maker-million-step-llm-zero-errors.ingest.md) achieves zero errors over a million LLM steps. The results seem contradictory but aren't — Kim et al. tested synthesis, MAKER tested voting.

## The distinction

**Synthesis** merges outputs from multiple agents into a combined result. It tries to preserve information from all contributors. If three agents produce analyses and one contains an error, synthesis folds that error into the merged output. There is no mechanism to detect that agent 2 contradicts agents 1 and 3.

**Voting** selects the most common answer and discards minorities. It deliberately throws away information — that's the point. If two out of three agents agree, the dissenter's output is dropped entirely. Errors survive only if they're shared by a majority.

Synthesis is information aggregation. Voting is error correction. They solve different problems and have opposite failure modes: synthesis fails by propagating errors, voting fails by discarding correct minority answers.

## What Kim et al. actually tested

Kim et al.'s "Independent" topology — the one showing 17.2× error amplification — uses what the paper calls **"synthesis-only coordination"**: 3 agents run in parallel and their outputs are combined. The paper doesn't detail the synthesis mechanism, but the key point is that it's not voting — outputs are merged rather than compared for agreement. Despite mentioning "majority voting" as a design option for orchestrators, voting was not implemented in the tested configurations.

The other topologies add verification but not voting:
- **Centralized** (4.4×): an orchestrator reviews sub-agent outputs — a soft oracle, partially filtering errors
- **Decentralized** (7.8×): agents debate across 3 rounds — adversarial review, not voting
- **Hybrid** (5.1×): combines both, but with 515% overhead

The progression 17.2× → 4.4× tracks increasing verification strength. Even partial verification (centralized orchestrator) cuts error amplification by 4×.

## What MAKER tested

MAKER uses first-to-ahead-by-k voting on maximally decomposed micro-steps (one Hanoi move per agent call). Three design choices make this work:

1. **Maximal decomposition** — each step has a single atomic answer, making voting well-defined (you can count which answer occurs most often)
2. **Hard per-step oracles** — each Hanoi move is deterministically correct or incorrect, so the problem supplies a ground truth that voting can converge toward
3. **Decorrelation** — red-flagging (discarding responses >700 tokens or with format violations) removes the output class most likely to carry correlated errors; temperature variation adds sampling diversity. These measures push toward the i.i.d. error assumption that makes voting's statistical guarantees hold

None of these are present in Kim et al.'s design: no decomposition (whole tasks given to agents), no explicit oracle, no decorrelation (identical prompts and tools across agents).

## The design rule

In the [scheduling model](./bounded-context-orchestration-model.md), what to do with multiple agent outputs is a scheduler design decision. The aggregation operation must match the relationship between the calls:

- **Redundant calls** solving the same sub-problem need **voting** — the scheduler's job is selection via [error correction](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md).
- **Complementary calls** solving different sub-problems need **synthesis** — the scheduler's job is assembly.

Kim et al.'s Independent topology applies synthesis where voting would be appropriate: agents solve the same complete task independently, but their outputs are merged rather than compared. This is a gap in the experimental design (voting with decorrelation was never tested), not evidence that multi-agent coordination is inherently negative-sum. The [decomposition rules](./decomposition-rules-for-bounded-context-scheduling.md) should encode this match explicitly.

## Open questions

- Adversarial debate (Kim et al.'s Decentralized topology, 7.8×) may be a third category — iterative refinement through disagreement rather than merging or selecting. Its partial error-correction benefit suggests it is somewhere between synthesis and voting, but the mechanism is different from both.
- Can you combine the two? Decompose a task, have multiple agents attempt each sub-task (vote to select), then synthesize across sub-tasks. This is the scheduling model with redundancy at the sub-task level.
- MAKER's success depends on maximal decomposition making voting well-defined (single atomic answers). For complex outputs, how do you define "majority agreement"? This is where [oracle strength](./oracle-strength-spectrum.md) bites — you need a way to determine when two outputs "agree."

---

Relevant Notes:

- [error-correction-works-above-chance-oracles-with-decorrelated-checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — foundation: the theoretical framework for when voting-based error correction works (TPR > FPR, decorrelated checks); this note adds that synthesis doesn't qualify
- [agent orchestration needs coordination guarantees, not just coordination channels](./agent-orchestration-needs-coordination-guarantees-not-just-coordination-channels.md) — extends: synthesis failures are one member of a broader family where uncoordinated composition over a shared substrate produces amplification instead of contamination or inconsistency
- [bounded-context-orchestration-model](./bounded-context-orchestration-model.md) — extends: synthesis vs voting is a scheduler aggregation decision that should match the relationship between bounded calls
- [decomposition-rules-for-bounded-context-scheduling](./decomposition-rules-for-bounded-context-scheduling.md) — extends: aggregation operation must match decomposition structure (redundant calls → vote, complementary calls → synthesize)
- [oracle-strength-spectrum](./oracle-strength-spectrum.md) — grounds: voting requires an oracle to define "agreement"; oracle strength determines whether voting is viable for complex outputs
- [Kim et al.](../sources/towards-a-science-of-scaling-agent-systems.ingest.md) — evidence: 17.2× error amplification with synthesis-only Independent topology vs 4.4× with centralized verification
- [MAKER](../sources/meyerson-maker-million-step-llm-zero-errors.ingest.md) — evidence: zero errors over 1M steps using first-to-ahead-by-k voting with maximal decomposition and decorrelation
