---
description: Definition - a knowledge artifact is a retained artifact consumed as evidence, reference, context, explanation, or advice
type: kb/types/definition.md
tags: [learning-theory, artifact-analysis]
---

# Knowledge artifact

A knowledge artifact is a [retained artifact](./retained-artifact.md) whose [operative part](./operative-part.md) is consumed as evidence, reference, context, fact, explanation, or advice. It can change behavior by changing what an agent or human knows or considers, but it does not by itself bind the next action.

## Scope

The term names a [behavioral authority](./behavioral-authority.md) family, not a storage substrate or representational form. A knowledge artifact may be prose, symbolic, distributed-parametric, or mixed; it may live in a repo, database, vector store, prompt registry, or service object.

Typical knowledge-artifact uses include:

- retrieving a note as background evidence
- reading a source summary as context
- consulting a schema or API spec as documentation
- preserving a trace as audit evidence
- loading examples as advisory cases

Knowledge artifacts may be authoritative as **sources of truth**. That is lineage or source authority. It becomes behavioral authority only through a named consumption path.

## Exclusions

A stored object is not a knowledge artifact merely because it contains true statements. It must be available to a later consumer as evidence, reference, context, explanation, or advice.

The term does not mean "low value" or "non-behavioral." Knowledge artifacts can drive major behavior changes when they alter the consumer's beliefs, but that effect is mediated through interpretation rather than instruction, enforcement, routing, validation, or training.

## Misuse Cases

- Calling a validator a knowledge artifact when a runtime uses it to block execution.
- Treating canonical source material as system definition only because it is authoritative; source authority and behavioral authority are separate.
- Assuming retrieved knowledge is harmless because it is "only context"; advisory material can acquire high effective authority through prompt placement, repetition, or activation policy.

---

Relevant Notes:

- [behavioral authority](./behavioral-authority.md) - parent field: knowledge artifact is an authority-path family
- [system-definition artifact](./system-definition-artifact.md) - contrast: retained artifacts consumed with instruction, enforcement, routing, validation, configuration, evaluation, or learning force
- [lineage](./lineage.md) - boundary: source-of-truth status is lineage, not automatically behavioral authority
