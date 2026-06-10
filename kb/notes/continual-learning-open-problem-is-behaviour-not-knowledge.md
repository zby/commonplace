---
description: Continual learning splits into knowledge accumulation (solved by ordinary data engineering — DBs, files, vector stores, RAG) and behaviour change (the open problem). Behaviour change depends on behavioral authority, with distributed-parametric updates expensive and readable artifacts cheap but under-addressed
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, deploy-time-learning]
status: current
---

# Continual learning's open problem is behaviour, not knowledge

Take Herbert Simon's definition of learning, cited in [learning is not only about generality](./learning-is-not-only-about-generality.md): any durable change in a system's capacity for adapting to its environment. Under that criterion, continual learning splits by [behavioral authority](./definitions/behavioral-authority.md) (who consumes a retained artifact, through which channel, with what force): [knowledge artifacts](./definitions/knowledge-artifact.md) consumed as facts, evidence, reference, context, or advice, and [system-definition artifacts](./definitions/system-definition-artifact.md) consumed with instruction, enforcement, routing, validation, ranking, or learning force. Both are learning; they differ in what a durable write changes.

The knowledge half is solved by ordinary data engineering — databases, file systems, vector stores, RAG, agent-memory records, user profiles in aggregate hold far more than weights can. Adding entries grows the system's reach without changing its disposition.

Behaviour change — where durable writes change what the system *does* — is the open problem. Two mechanisms achieve it:

- **Distributed-parametric updates** — fine-tuning, online learning, RLHF, continual pretraining, adapters, embedding updates, learned controllers. Expensive: heavy training infrastructure, cycles of days to weeks for large updates, behavioral probes rather than direct reading, and possible regressions in unrelated behaviours.
- **Readable system-definition artifacts** — prompts, tips, notes, schemas, tools, tests. When an LLM, interpreter, runtime, validator, router, or retriever consumes such an artifact with instruction, enforcement, selection, evaluation, or learning force, a durable write changes what the system does next session. Cheap: a commit, a diff, a revert; inspectable; driveable by runtime signals.

Mainstream continual-learning research targets distributed-parametric state (the expensive behaviour mechanism) and retrieval (the solved knowledge mechanism), leaving readable system-definition artifacts — the cheap behaviour mechanism — as engineering plumbing. Recognising that plumbing as a learning regime puts it into comparison with weight updates and learned controllers; the useful question is how the mechanisms combine.

---

Relevant Notes:

- [learning is not only about generality](./learning-is-not-only-about-generality.md) — foundation: Simon's capacity-change definition of learning
- [LLM context is a homoiconic medium](./llm-context-is-a-homoiconic-medium.md) — mechanism: lets readable artifacts function as instruction rather than only as data
- [deploy-time learning is the missing middle](./deploy-time-learning-is-the-missing-middle.md) — extends: fills the timing axis for system-definition updates during deployment
- [constraining during deployment is continual learning](./constraining-during-deployment-is-continuous-learning.md) — exemplifies: versioned prompts, schemas, tools, and tests as one concrete system-definition loop
- [Axes of artifact analysis](./axes-of-artifact-analysis.md) — foundation: defines substrate, form, lineage, and authority; this note applies authority to argue which half of continual learning is open
- [treat continual learning as substrate coevolution](./treat-continual-learning-as-substrate-coevolution.md) — extends: asks how the three representational forms' improvement loops should relate
- [memory management policy is learnable but oracle-dependent](./memory-management-policy-is-learnable-but-oracle-dependent.md) — contrasts: AgeMem is the distributed-parametric behaviour-change case, against which the readable-artifact mechanism is the cheaper alternative
- [trace-derived learning techniques in related systems](../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) — grounds: surveyed systems already split into weight-promotion and artifact-promotion loops
