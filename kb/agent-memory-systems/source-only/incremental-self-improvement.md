---
description: "Source-only coverage note for Schmidhuber's incremental self-improvement paradigm, a reward-gated self-modification system for learning learning strategies"
type: kb/types/note.md
traits: [has-comparison, has-external-sources]
tags: [related-systems, learning-theory]
status: current
---

# Incremental Self-Improvement

Incremental Self-Improvement is tracked here as source-only related-system coverage, not as an `agent-memory-system-review`. The coverage comes from Jürgen Schmidhuber's [1995 revised FKI-198-94 technical report](../../sources/on-learning-how-to-learn-learning-strategies.md), which presents a paradigm and concrete toy implementation but no reachable repository to inspect. It belongs outside `../reviews/` until there is code-grounded evidence.

The system is not an agent memory system in the current KB sense. It is relevant because it is an early, explicit architecture for a lifelong agent that changes the mechanism by which it learns. The persistent learned state is not notes, memories, or retrieved artifacts; it is the context-dependent probability distribution over future instruction sequences, including future self-modification programs.

## Source-visible design

**Self-modification as ordinary action.** The system runs a Turing-equivalent, assembler-like language. Some action subsequences interact with the environment; others are self-delimiting self-modification programs. Those programs can modify probabilities for future action subsequences, including the probabilities of future self-modification programs. The architecture intentionally removes the hard boundary between learning, meta-learning, and ordinary computation.

**Whole-life reward accounting.** The paper rejects resettable training episodes as the default abstraction. System life is treated as a one-way sequence, and utility is measured as payoff per time since startup or since a self-modification program began. Learning time, evaluation time, and management overhead are part of the accounting rather than hidden outside the objective.

**Reward-gated retention.** A fixed top-level credit-assignment strategy keeps only probability changes made by self-modification programs that improve payoff intake relative to the system or to earlier useful self-modification programs. When a modification stops qualifying, the top level restores older probability distributions from a stack. The resulting memory-management analogue is conservative: new learning must pay for itself in observed reward rate or it is rolled back.

**Low-level implementation.** The concrete implementation stores integer work cells and program cells. Each program cell has probabilities over possible instruction or argument values. Self-referential primitives read and adjust those probabilities, while an `EndSelfMod`-style boundary hands control back to the top-level retention policy.

## Comparison with Our System

Commonplace promotes knowledge into inspectable artifacts and uses validation, review, links, and indexes to control when those artifacts become reliable context. Incremental Self-Improvement promotes changes into the agent's policy distribution, with reward/time as the retention gate. That makes it closer to weight or policy learning than to an agent-operated knowledge base.

The useful comparison is therefore not storage substrate but promotion discipline. Commonplace mostly relies on human or semantic-review judgment for whether a note should persist. Schmidhuber's system assumes a numeric payoff signal strong enough to decide whether a self-modification increased lifetime reward rate. That is attractive when the oracle is hard and cheap, but it does not solve the KB case where "better future reasoning" is delayed, ambiguous, and hard to measure.

This is the same pressure described by [choosing what to learn requires both validity and learning value gates](../../notes/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md). In the report, payoff per time tries to collapse both questions into one scalar: did the modification work, and was it worth retaining? For KB methodology those gates come apart. A claim can be valid but low-value, or promising but insufficiently grounded, so automatic promotion needs more than a single reward-rate analogue.

## Borrowable Ideas

**Charge learning to the same budget as acting.** Ready to borrow conceptually. Review and distillation workflows should account for their cost, not only the apparent quality of the produced artifact.

**Make promotion reversible.** The stack-backed restoration mechanism is a useful analogue for KB changes: durable promotion should preserve enough previous state to retire or replace a bad rule without pretending the system never learned it.

**Treat primitive choice as prior bias.** The paper is explicit that prior knowledge enters through the primitive operations and payoff function. For KB methodology, this maps to type specs, validation rules, and available skills: the substrate constrains what agents can easily learn.

## Review boundary

Do not create `kb/agent-memory-systems/reviews/incremental-self-improvement.md` unless a reachable implementation is found and inspected. The current evidence is a technical report with a described implementation and toy experiments, not a repository-backed system. The note should be used as conceptual lineage for self-improving agents, trace-derived policy learning, and promotion-gate design, not as implementation evidence for modern agent memory infrastructure.

## What to Watch

- Whether later open implementations of Schmidhuber-style self-referential learners expose an inspectable memory or policy substrate
- Whether Gödel-machine or self-referential meta-learning systems make the reward-gated promotion policy operational in modern agents
- Whether agent-memory systems can approximate payoff-per-time accounting with weaker semantic or task-completion oracles

---

Relevant Notes:

- [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — compares nearby systems that learn from trajectories, sessions, or next-state feedback; this paper is useful lineage but lower-confidence as source-only theory
- [Ingest: On Learning How to Learn Learning Strategies](../../sources/on-learning-how-to-learn-learning-strategies.ingest.md) — source coverage: classifies the report and extracts the payoff-per-time, reversible-promotion, and oracle-dependence lessons
- [Self-Training-LLM](../reviews/Self-Training-LLM.md) — compares: both promote experience into model-side behavior rather than a readable KB artifact, but Self-Training-LLM is repo-inspected and dataset-driven
- [Meta-Harness](../reviews/meta-harness.md) — compares: a modern code-inspected system where benchmark-scored runs select improved harness variants rather than self-modifying instruction probabilities
- [choosing what to learn requires both validity and learning value gates](../../notes/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md) — refines: explains why KB promotion cannot collapse correctness and value into one payoff-per-time gate
- [oracle strength spectrum](../../notes/oracle-strength-spectrum.md) — rationale: reward-gated self-modification only works cleanly where the evaluation signal can carry the promotion decision
