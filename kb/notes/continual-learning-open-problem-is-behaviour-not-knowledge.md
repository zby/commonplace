---
description: Continual learning's hard part is behaviour change; knowledge accumulation fits ordinary stores, while durable behaviour change comes through weights or readable artifacts
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, deploy-time-learning]
status: current
---

# Continual learning's open problem is behaviour, not knowledge

Take Herbert Simon's definition of learning, cited in [Learning is not only about generality](./learning-is-not-only-about-generality.md): any durable change in a system's capacity for adapting to its environment. Under that criterion, continual learning splits by [behavioral authority](./definitions/behavioral-authority.md): who consumes a retained artifact, through which channel, and with what force. [Knowledge artifacts](./definitions/knowledge-artifact.md) are consumed as facts, evidence, reference, context, or advice. [System-definition artifacts](./definitions/system-definition-artifact.md) are consumed with instruction, enforcement, routing, validation, ranking, or learning force. Both are learning; they differ in what a durable write changes.

The knowledge half is solved by ordinary data engineering: databases, file systems, vector stores, retrieval-augmented generation (RAG), agent-memory records, and user profiles. In aggregate, these systems and stores hold far more than weights can. Adding entries grows the system's reach without changing its disposition.

Behaviour change — where durable writes change what the system *does* — is the open problem. Two mechanisms achieve it:

| Mechanism | Examples | Behaviour-change profile |
|---|---|---|
| **Distributed-parametric updates** | Fine-tuning, online learning, reinforcement learning from human feedback (RLHF), continual pretraining, adapters, embedding updates, learned controllers | Heavy training infrastructure, substantial retraining cycles for large updates, behavioral probes rather than direct reading, and possible regressions in unrelated behaviours |
| **Readable system-definition artifacts** | Prompts, tips, notes, schemas, tools, tests | A durable write changes what the system does next session when an LLM, interpreter, runtime, validator, router, or retriever consumes the artifact with instruction, enforcement, selection, evaluation, or learning force. The artifact is cheap to write, review, and revert; inspectable; driveable by runtime signals |

This split prevents retrieval from standing in for behaviour change. Retrieval grows accessible knowledge without changing the system's disposition. Distributed-parametric updates and readable system-definition artifacts both change disposition, but in different substrate regimes. Recognising readable-artifact work as a learning regime puts it into comparison with weight updates and learned controllers; the useful question is how the mechanisms combine.

---

Relevant Notes:

- [Learning is not only about generality](./learning-is-not-only-about-generality.md) — foundation: broadens learning beyond generality, so both knowledge accumulation and behaviour change count as capacity changes
- [LLM context is a homoiconic medium](./llm-context-is-a-homoiconic-medium.md) — mechanism: lets readable artifacts function as instruction rather than only as data
- [Deploy-time learning is the missing middle](./deploy-time-learning-is-the-missing-middle.md) — extends: fills the timing axis for system-definition updates during deployment
- [Constraining during deployment is continual learning](./constraining-during-deployment-is-continuous-learning.md) — exemplifies: versioned prompts, schemas, tools, and tests as one concrete system-definition loop
- [Axes of artifact analysis](./axes-of-artifact-analysis.md) — foundation: defines substrate, form, lineage, and authority; this note applies authority to argue which half of continual learning is open
- [Treat continual learning as substrate coevolution](./treat-continual-learning-as-substrate-coevolution.md) — extends: asks how the three representational forms' improvement loops should relate
- [Memory management policy is learnable but oracle-dependent](./memory-management-policy-is-learnable-but-oracle-dependent.md) — contrasts: AgeMem is a learned memory-management policy system and the distributed-parametric behaviour-change case, against which the readable-artifact mechanism is the cheaper alternative
- [Trace-derived learning techniques in related systems](../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) — grounds: surveyed systems already split into weight-promotion and artifact-promotion loops
