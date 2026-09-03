---
description: "A persistent automated theory builder for external users becomes a software house when genuinely new domains require it to revise the software that performs theory production rather than only the theories produced"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, self-improving-systems, learning-theory]
---

# An open-domain theory builder becomes a software house when new domains require production-machinery changes

Consider a persistent automated system that builds, tests, and revises natural-language theories for external users across domains not fixed in advance. Language models currently supply the broadly applicable semantic operations: interpreting claims, comparing explanations, proposing counterexamples, and revising scope. Software outside model interpretation supplies the corpus, exact state transitions, scheduling, checks, indexes, and rollback.

New domains can bring new manipulation requirements as well as new content. A domain whose claims must be compared across changing versions of a source may require snapshot pins in the note schema and a validator for them, even if no earlier domain needed either. Other domains may require new evidence models, dependency representations, retrieval paths, evaluators, or workflows.

When such requirements arise, either the builder revises its own supporting software or a person repeatedly supplies the required changes. In the second case that person fills an internal production role in the complete theory-building system. An automated builder must bring the role inside its computational boundary. It then persistently develops software in response to demands and operating consequences for external users, which meets the definition of a [software house](./definitions/software-house.md).

The claim is conditional, not an impossibility theorem about fixed harnesses. A sufficiently general fixed harness might sustain theory building across genuinely new domains without requiring demand-specific machinery changes. Such a construction would refute this link while leaving open the broader question of whether automated software houses are reachable. The empirical issue is whether new domains repeatedly expose production requirements that were not economically or practically anticipated in the fixed substrate.

---

Relevant Notes:

- [Software house](./definitions/software-house.md) — defines: the complete persistent producer whose boundary follows internal production roles
- [Code complements the weight–prompt pair with independently executed symbolic operations](./code-complements-weight-prompt-with-symbolic-operations.md) — grounds: the division between open-ended semantic operations and exact installed transitions
- [Scheduler-LLM separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — grounds: why exact state, checks, and bookkeeping remain software responsibilities
- [Broad software demands create pressure for agentic factory development](./broad-software-demands-create-pressure-for-agentic-factory-development.md) — parallels: broad demand classes create practical pressure to acquire new production machinery without proving that a fixed universal substrate is impossible
