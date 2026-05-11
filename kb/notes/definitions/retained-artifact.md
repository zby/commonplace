---
description: Definition - a retained artifact is retained state that a later agentic loop can consume in a behavior-shaping way, regardless of storage substrate
type: kb/types/definition.md
tags: [learning-theory]
status: current
---

# Retained artifact

A retained artifact is state that persists across time and can later be consumed by an agentic loop in a way that shapes behavior. The boundary is behavioral consequence, not storage label. A note, prompt, workflow, validator, route table, embedding index, adapter, checkpoint, or skill bundle counts when a later model, router, runtime, validator, retriever, reviewer, or learning loop can use it to change what happens.

## Scope

The term is the KB's umbrella for durable adaptation outside the current context window. It includes canonical source artifacts, derived views, generated indexes, compiled artifacts, retrieved records, and learned numerical state when they remain eligible for future behavior-shaping use.

The unit of analysis is often narrower than the stored object. When one stored object bundles multiple behavior-shaping parts, classify the relevant [operative part](./operative-part.md) or consumption path.

## Exclusions

A backup, export, raw log, or archive is not a retained artifact merely because it is persisted. It enters the scope only when some later consumption path can read, retrieve, execute, rank, validate, train on, or otherwise apply it in a behavior-shaping way.

## Misuse Cases

- Treating "memory" as a synonym for retained artifact hides prompts, validators, route tables, indexes, and code artifacts that shape behavior outside a memory store.
- Treating every stored file as a retained artifact overcounts archival material that has no live consumption path.

---

Relevant Notes:

- [operative part](./operative-part.md) - boundary: classification often targets the behavior-shaping part of a larger stored object
- [representational form](./representational-form.md) - field: records how the retained artifact's operative part is encoded and consumed
- [behavioral authority](./behavioral-authority.md) - field: records the consumption path and force that make retained state consequential
