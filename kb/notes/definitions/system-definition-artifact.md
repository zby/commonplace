---
description: Definition - a system-definition artifact is a retained artifact consumed with instruction, enforcement, routing, validation, configuration, evaluation, or learning force
type: kb/types/definition.md
tags: [learning-theory, artifact-analysis]
status: current
---

# System-definition artifact

A system-definition artifact is a [retained artifact](./retained-artifact.md) whose [operative part](./operative-part.md) is consumed through a path that defines, configures, constrains, routes, validates, evaluates, or trains future behavior. The term is shorthand for a high-authority [behavioral authority](./behavioral-authority.md) family, not an intrinsic artifact class.

## Scope

System-definition artifacts include retained artifacts used with force such as:

- **instruction** - prompts, rules, standing guidance, playbooks, persona files
- **configuration or routing** - tool allowlists, route tables, scheduler policies, context-loading rules
- **validation or enforcement** - schemas, tests, validators, guardrails, permission policies
- **evaluation** - rubrics, acceptance checks, reviewer gates, benchmark criteria
- **learning input** - trace datasets, reward signals, training records, preference labels

The artifact may be prose, symbolic, distributed-parametric, or mixed. A Markdown file, schema, script, vector index, checkpoint, or training dataset can all be system-definition artifacts when the consumption path gives them behavior-shaping force.

## Exclusions

Declared intent is not enough. A policy document is not a system-definition artifact for a given system if no component reads, invokes, validates against, routes through, or learns from it.

The term does not replace the four artifact-analysis fields. A precise record still names storage substrate, representational form, lineage, and behavioral authority.

## Misuse Cases

- Treating "system-definition" as a representational form, as if all system-definition artifacts were prose prompts or symbolic code.
- Calling every important artifact system definition. A canonical API spec is a knowledge artifact when read as reference and a system-definition artifact when a validator, generator, or runtime consumes it to constrain behavior.
- Ignoring lineage for generated system-definition artifacts. High-authority derived views need explicit source, invalidation, and regeneration rules.

---

Relevant Notes:

- [behavioral authority](./behavioral-authority.md) - parent field: system-definition artifact is an authority-path family
- [knowledge artifact](./knowledge-artifact.md) - contrast: retained artifacts consumed as evidence, reference, context, explanation, or advice
- [lineage](./lineage.md) - interaction: high-authority derived artifacts need stronger invalidation discipline
