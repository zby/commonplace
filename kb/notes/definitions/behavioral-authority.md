---
description: Definition - behavioral authority records who consumes a retained artifact, through which channel, and with what force
type: kb/types/definition.md
tags: [learning-theory]
status: current
---

# Behavioral authority

Behavioral authority records how a retained artifact becomes behavior-shaping: the consumer, the channel, and the force. The same stored object can have different authority in different consumption paths, so authority belongs to the use of an [operative part](./operative-part.md), not to bytes alone.

## Scope

The **consumer** may be a model, router, retriever, runtime, validator, reviewer, maintainer, assembler, or learning loop.

The **channel** may be retrieval, prompt assembly, execution, configuration, validation, routing, ranking, review, or training.

The **force** may be advice, instruction, enforcement, selection or ranking influence, audit trigger, or learning input. Audit records do not have force by themselves; they matter when a consumer acts on them.

Use behavioral authority instead of the older knowledge-role/system-definition-role shorthand when the distinction matters. "Knowledge" usually means advice or evidence through a retrieval or reading channel. "System definition" usually means instruction, enforcement, routing, validation, or learning input. The field is more precise because it names the actual consumer and force.

## Exclusions

Declared intent is not enough. An advisory note may acquire high effective authority if it is always included in a late prompt position; a formal policy may have no effective authority if no component loads it.

## Misuse Cases

- Saying a memory "is active" without naming whether it advises a model, enters an instruction channel, enforces validation, influences ranking, or feeds training.
- Treating a Markdown file as low-authority because it is prose, even when the harness loads it as standing instruction.

---

Relevant Notes:

- [operative part](./operative-part.md) - unit: authority attaches to the behavior-shaping part and consumption path
- [lineage](./lineage.md) - interaction: derived artifacts with high authority need stronger invalidation discipline
- [retained artifact](./retained-artifact.md) - parent concept: the persisted state whose later use may shape behavior
