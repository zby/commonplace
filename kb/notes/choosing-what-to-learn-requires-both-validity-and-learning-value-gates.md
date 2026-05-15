---
description: "Separates two promotion checks for learning loops: whether a candidate is trustworthy enough to learn from, and whether learning it would improve the current system."
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [learning-theory]
status: current
---

# Choosing what to learn requires both validity and learning-value gates

Learning loops need two different checks before they promote a candidate into durable memory, weights, or [knowledge artifacts](./definitions/knowledge-artifact.md). The candidate must be valid enough to learn from, and it must be worth learning for the current system.

A **validity gate** asks whether the candidate is grounded, coherent, and trustworthy: whether an answer is source-supported, a proposed note is faithful to its evidence, or a link relationship is real rather than a keyword accident. Without this gate, the loop accumulates contamination.

A **learning-value gate** asks whether promoting the candidate would improve the system: whether the item covers a real gap, exposes unreliable model behavior, or helps future tasks enough to justify the added maintenance burden. Without this gate, the loop accumulates clutter.

## The self-training case

[Self-Training-LLM](../agent-memory-systems/reviews/Self-Training-LLM.md) makes the split concrete. Its pipeline constructs factual QA examples from Wikipedia-grounded traces, then filters them before SFT (supervised fine-tuning) or DPO (preference optimization) training. The corresponding paper, [Self-training Large Language Models through Knowledge Detection](../sources/self-training-large-language-models-through-knowledge-detection.ingest.md), calls the two filters consistency filtering and knowledge filtering: one rejects low-confidence reference answers; the other keeps cases where the model's unconditioned answers contradict the source-grounded answer.

## The KB case

For KB learning, the same split should govern note, link, and synthesis promotion. A proposed note can be faithful but redundant. A proposed link can be plausible but not navigationally useful. A proposed synthesis can be valid but too narrow to change future answers.

This refines [automating KB learning is an open problem](./automating-kb-learning-is-an-open-problem.md). The open problem is not one generic oracle for "should we learn this?" It is at least two oracles: one for groundedness and one for value relative to the current system's gaps. A single score can combine them for ranking, but the underlying checks should remain separate so failures are diagnosable.

---

Relevant Notes:

- [automating KB learning is an open problem](./automating-kb-learning-is-an-open-problem.md) — extends: gives the boiling-cauldron promotion loop a diagnosable acceptance interface, separating contamination control from clutter control
- [oracle strength spectrum](./oracle-strength-spectrum.md) — grounds: both gates require oracles, but their oracle targets differ
- [memory management policy is learnable but oracle-dependent](./memory-management-policy-is-learnable-but-oracle-dependent.md) — parallels: learned curation policies work only when the promotion signal is well defined
- [Self-Training-LLM](../agent-memory-systems/reviews/Self-Training-LLM.md) — evidence: code-grounded review of the separate question-filtering and unknown-filtering pattern
- [Self-training Large Language Models through Knowledge Detection](../sources/self-training-large-language-models-through-knowledge-detection.ingest.md) — evidence: paper-level account of consistency filtering and knowledge filtering as separate stages
- [Into the Unknown: Self-Learning Large Language Models](../sources/into-the-unknown-self-learning-large-language-models.ingest.md) — evidence: frames the upstream problem as deciding what previously unknown knowledge to absorb
