---
description: "Definition - representational form classifies how an operative part is encoded and consumed: natural-language, symbolic, distributed-parametric, or mixed"
type: kb/types/definition.md
tags: [learning-theory, artifact-analysis]
---

# Representational form

Representational form classifies how a retained artifact's [operative part](./operative-part.md) is encoded and consumed. This KB uses three coarse forms: **natural-language**, **symbolic**, and **distributed-parametric**. Mixed artifacts are split by operative part or consumption path when the parts have different review evidence, invalidation needs, or rollback paths.

## Scope

**Natural-language** carries behavior-shaping content whose consequences come from interpretation by a language model or human. Prompts, reflections, notes, policies, playbooks, and many skills have natural-language operative parts where their force comes from interpretation.

**Symbolic** carries behavior-shaping content in localized units whose consequences are assigned by a parser, interpreter, runtime, schema, validator, route table, or other defined consumer. The category is architectural, not a claim about classical symbolic AI.

**Distributed-parametric** carries behavior-shaping content in numerical state distributed across parameters or dense representations: weights, adapters, embedding spaces, dense-vector indexes, reward models, learned controllers, and similar artifacts.

Form sets the default inspection method: read natural-language content, test or statically check symbolic artifacts, and probe distributed-parametric artifacts behaviorally.

## Exclusions

Representational form is not storage substrate. Markdown in a repository can be natural-language, symbolic, or mixed depending on the consumer. A vector store can expose natural-language records while its retrieval behavior depends on distributed-parametric embeddings and ranking.

Representational form is also not consumption path. **Prompt** is exact when material is supplied, or explicitly assembled to be supplied, as model input. A stored note, policy, or memory record is not thereby a prompt because it might later be retrieved; retain its precise artifact name, or call it natural-language when the representational category matters. A generated model-input view can be a prompt even when it assembles natural-language and symbolic operative parts.

## Misuse Cases

- Calling learned weights "opaque" as if opacity were the form. The form is distributed-parametric; opacity is a practical inspection property that also appears at sufficient scale in natural-language and symbolic systems.
- Calling every YAML or Markdown artifact symbolic. It is symbolic only where a consumer assigns defined consequences to specific fields, values, or structures.

## Revision rationale

The category was renamed from **prose** to **natural-language** because its boundary is interpretive, not editorial. Fragments, facts, reflections, structured records, rules, and prompt components can receive their consequences through natural-language interpretation without being continuous expository prose. The older label therefore excluded central cases by connotation and encouraged the storage package to stand in for the operative part.

Apply the vocabulary in this order: name the precise artifact when the category adds nothing; use **prompt** when model-input supply is the point; use a **natural-language** category term when representational form matters; preserve **prose** for editorial meaning, quotations, historical terminology, and named review machinery. This ordering keeps prompt narrower than natural-language artifact and prevents a stored artifact from being reclassified merely because one future consumption path may place it in context.

---

Relevant Notes:

- [operative part](./operative-part.md) - unit: representational form classifies the relevant behavior-shaping part, not necessarily the whole stored object
- [storage substrate](./storage-substrate.md) - contrast: location is separate from representation
- [codification](./codification.md) - mechanism: movement from natural-language into symbolic form
- [opacity is a scale threshold](../opacity-is-a-scale-threshold.md) - caveat: practical opacity is not identical to representational form
