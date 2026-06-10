---
description: "Definition - representational form classifies how an operative part is encoded and consumed: prose, symbolic, distributed-parametric, or mixed"
type: kb/types/definition.md
tags: [learning-theory, artifact-analysis]
status: current
---

# Representational form

Representational form classifies how a retained artifact's [operative part](./operative-part.md) is encoded and consumed. This KB uses three coarse forms: **prose**, **symbolic**, and **distributed-parametric**. Mixed artifacts are split by operative part or consumption path when the parts have different review evidence, invalidation needs, or rollback paths.

## Scope

**Prose** carries behavior-shaping content in natural language interpreted by a language model or human. Prompts, reflections, notes, policies, playbooks, and many skills are prose where their force comes from interpretation.

**Symbolic** carries behavior-shaping content in localized units whose consequences are assigned by a parser, interpreter, runtime, schema, validator, route table, or other defined consumer. The category is architectural, not a claim about classical symbolic AI.

**Distributed-parametric** carries behavior-shaping content in numerical state distributed across parameters or dense representations: weights, adapters, embedding spaces, dense-vector indexes, reward models, learned controllers, and similar artifacts.

Form sets the default inspection method: read prose, test or statically check symbolic artifacts, and probe distributed-parametric artifacts behaviorally.

## Exclusions

Representational form is not storage substrate. Markdown in a repository can be prose, symbolic, or mixed depending on the consumer. A vector store can expose prose records while its retrieval behavior depends on distributed-parametric embeddings and ranking.

## Misuse Cases

- Calling learned weights "opaque" as if opacity were the form. The form is distributed-parametric; opacity is a practical inspection property that also appears at sufficient scale in prose and symbolic systems.
- Calling every YAML or Markdown artifact symbolic. It is symbolic only where a consumer assigns defined consequences to specific fields, values, or structures.

---

Relevant Notes:

- [operative part](./operative-part.md) - unit: representational form classifies the relevant behavior-shaping part, not necessarily the whole stored object
- [storage substrate](./storage-substrate.md) - contrast: location is separate from representation
- [codification](./codification.md) - mechanism: movement from prose into symbolic form
- [opacity is a scale threshold](../opacity-is-a-scale-threshold.md) - caveat: practical opacity is not identical to representational form
