# Agent complexity theory workshop

Working out formal consequences of the [bounded-context orchestration model](../../notes/bounded-context-orchestration-model.md) and its [universality lemma](../../notes/any-symbolic-program-with-llm-calls-is-a-select-call-program.md). The model is a deliberately simple normal form — a symbolic scheduler over bounded LLM calls — and the lemma means results proved on it transfer to all clean symbolic programs with LLM calls.

The goal is theorem sketches and proof outlines suitable for academic collaboration, not KB design notes. Artifacts here are consumed when they mature into a paper or get pitched to collaborators.

## Current direction

An [external review recorded on 2026-08-04](./architectural-decision-theorems-review.md) proposes pivoting from generic resource lower bounds to **architectural decision theorems**. The organizing claim is that a decomposition creates an information cut whose cost is set by the downstream distinctions that must cross it. Candidate results should rule out a decomposition, choose between retention and summarization, give a measurable crossover, or produce a scheduling or verification policy.

The review also identifies two corrections to current sketches:

- the width-independent adaptive-chain round lower bound is false for the stated known-layer model; unrestricted speculative breadth can collapse rounds at exponential work cost;
- arbitrary error correlation does not necessarily worsen reliability decay; a perfect shared failure event can keep success constant with chain length.

The correction arguments are direct. The broader theorem program and literature positioning remain proposals until checked.

**Downstream consumer.** The [Exo application track](../explanatory-theories-deployment-time-learning/exo-case.md) depends on two families here, and how strongly it can state its case turns on how they resolve. The semantic-retrieval bound decides whether retaining derived artifacts avoids a reconstruction cost that stronger models could erase or a lower bound no capability escapes. [No bounded summary preserves all distinctions for a rich query family](./no-bounded-summary-preserves-all-distinctions-for-a-rich-query-family.md) constrains that track's proposal in the other direction: a bounded summary must declare which query family it serves, which is what a per-class contract does. Neither inquiry should assume the other's result — record what is proved, not what is hoped.

## Candidate result families

1. **Information cuts and addressability** — exact answer-profile capacity, one-way communication, frozen decompositions, and retained-source separation
2. **Adaptivity and speculative work** — breadth/lookahead tradeoffs and a conjectured full rounds/work frontier
3. **Online architectural policies** — thresholds for decomposition, artifact materialization, verifier spacing, and pointer amortization
4. **Positive sufficient conditions** — mergeable summaries and adaptive witness coverage
5. **Boundary lemmas and accounting models** — opaque retrieval, archive readability, and call-width bookkeeping

## Proof template

1. Fix a task family
2. State what symbolic code gets for free vs what requires a bounded call
3. Define per-call bound M and output bandwidth
4. Use adversary or fooling-set argument to maintain indistinguishable worlds
5. Show insufficient calls/rounds/summary-space leaves worlds unseparated
6. Conclude failure in the simple model
7. Lift to all clean bounded-call programs via the universality lemma

## Current sketches

- [Architectural decision theorems: review and proposed pivot](./architectural-decision-theorems-review.md)
- [Exact retrieval over semantically opaque items requires linear inspection](./exact-retrieval-over-semantically-opaque-items-requires-linear.md)
- [No bounded summary preserves all distinctions for a rich query family](./no-bounded-summary-preserves-all-distinctions-for-a-rich-query-family.md)
- [Adaptive dependencies force width, reopening, or sequential rounds](./adaptive-dependencies-force-width-reopening-or-sequential-rounds.md) — adaptive-chain theorem invalid as written; interaction-cut argument remains useful
- [Few calls require width and long chains require verification](./few-calls-require-width-and-long-chains-require-verification.md) — reliability correlation caveat needs replacement
- [Archive readability toy model](./archive-readability-toy-model.md)

## Sketch abstracts

### Interaction / adaptivity lower bounds

Corrected target statement shape: a no-reopen decomposition cut must transmit enough information to distinguish every downstream answer profile. For adaptive pointer following, parallel width can remove rounds, but guaranteed lookahead `h` in a hidden `B`-ary tree requires inspecting the complete depth-`h` prefix, so latency is exchanged for exponentially growing speculative work.

Practical consequence: a scheduler chooses among another dependent round, speculative inspection, a lower-branching pointer layer, and reopening. Insufficient capacity across a frozen cut cannot be repaired by improving only the components on either side.

### Tradeoff and reliability theorems

Target statement shape: convex within-call cost and interface cost determine an optimal independent-work chunk size. Measured segment success and verifier cost determine an optimal verification interval. Repeated derivation and artifact build cost determine when reasoning should be materialized.

Practical consequence: planner designs should expose measurable costs and use crossover rules rather than treating more decomposition, more retention, or more verification as unconditionally better.

### Archive readability toy model

The prompt-bottleneck sketch now lives here as the archive-readability toy model. It isolates two first-order costs in bounded-context archive use: pointer tax (`N * p / M` calls to classify flat pointers) and compression sufficiency (`R * a * s <= M` for one-shot synthesis, or a summary tree only when bounded sufficient summaries exist). The practical theorem shape is that archive size is not the primitive bottleneck; navigation pointer cost and the existence of task-sufficient compressed intermediates are.
