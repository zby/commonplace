---
description: Definition - storage substrate records where retained state persists, as an operational field distinct from form, lineage, and authority
type: kb/types/definition.md
tags: [learning-theory]
status: current
---

# Storage substrate

Storage substrate is the field that records where retained state persists: repository files, databases, vector stores, prompt registries, configuration services, service objects, audit logs, or model-artifact stores. It determines access, deletion, versioning, rollback, deployment, and latency paths, but it does not by itself say how retained behavior is represented or what force it has.

## Scope

Use storage substrate for the operational location of a [retained artifact](./retained-artifact.md). The same substrate can host many [representational forms](./representational-form.md): a repository can contain prose workflows, symbolic validators, generated prompt views, and pointers to checkpoints; a vector store can contain readable records plus distributed-parametric indexes.

## Exclusions

Do not use storage substrate as a replacement for artifact type, form, or authority. "In files", "in a database", and "in memory" are location claims, not architectural classifications of behavioral effect.

## Misuse Cases

- Comparing "files versus weights" as a single axis when storage location, representational form, and behavioral authority are changing at once.
- Calling a vector store a memory taxonomy rather than a substrate that may host prose records, dense-vector indexes, and ranking behavior.

---

Relevant Notes:

- [retained artifact](./retained-artifact.md) - scope: the state whose persistence location is being recorded
- [representational form](./representational-form.md) - contrast: how the operative part is encoded and consumed
- [lineage](./lineage.md) - contrast: source dependencies and refresh or invalidation obligations
