---
description: Definition - an operative part is the behavior-affecting content, structure, parameterization, or mechanism within a retained artifact or consumption path
type: kb/types/definition.md
tags: [learning-theory, artifact-analysis]
status: current
---

# Operative part

An operative part is the content, structure, parameterization, or behavior-affecting mechanism inside a [retained artifact](./retained-artifact.md) that a later consumer can apply. The same stored object may contain several operative parts: a Markdown prompt can carry prose instruction and a symbolic section contract; a retrieval package can carry prose records and distributed-parametric embeddings.

## Scope

Use the term operative part when the stored-object boundary is too coarse for architectural review. Operative parts may be prose, symbolic, distributed-parametric, or mixed. They matter because review evidence, invalidation triggers, rollback paths, and security risks attach to the part that actually shapes behavior.

## Exclusions

The operative part is not every byte in a stored object. Formatting, comments, archived traces, or metadata that no consumer uses may matter for maintenance, but they are not operative for behavior unless a consumption path gives them force.

## Misuse Cases

- Classifying a whole skill package as "prose" when its activation metadata and helper scripts create distinct symbolic operative parts.
- Classifying a vector store as "prose memory" while ignoring the embedding and ranking path that selects which prose becomes visible.

---

Relevant Notes:

- [retained artifact](./retained-artifact.md) - parent concept: the persisted object or state that may contain one or more operative parts
- [representational form](./representational-form.md) - classification field applied to operative parts
- [behavioral authority](./behavioral-authority.md) - classification field applied to consumption paths
