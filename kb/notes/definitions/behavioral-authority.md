---
description: Definition - behavioral authority records who consumes a retained artifact, through which channel, and with what force
type: kb/types/definition.md
tags: [learning-theory, artifact-analysis]
---

# Behavioral authority

Behavioral authority records how a retained artifact becomes behavior-shaping: the consumer, the channel, and the force. The same stored object can have different authority in different consumption paths, so authority belongs to the use of an [operative part](./operative-part.md), not to bytes alone.

## Scope

The **consumer** may be a model, router, retriever, runtime, validator, reviewer, maintainer, assembler, or learning loop.

The **channel** may be retrieval, prompt assembly, execution, configuration, validation, routing, ranking, review, or training.

The **force** may be advice, instruction, enforcement, selection or ranking influence, audit trigger, or learning input. Audit records do not have force by themselves; they matter when a consumer acts on them.

Authority paths compose. One consumer's act is often the next path's channel — a retriever is a consumer whose output enters another consumer's channel — so a full path is a chain, and a record names one link of it.

Use the term behavioral authority to make the older knowledge/system-definition distinction precise. A [knowledge artifact](./knowledge-artifact.md) is consumed as evidence, reference, context, explanation, or advice. A [system-definition artifact](./system-definition-artifact.md) is consumed with instruction, enforcement, routing, validation, configuration, evaluation, or learning force. These are authority-path families, not intrinsic artifact classes; the field is more precise because it names the actual consumer, channel, and force.

## Exclusions

Declared intent is not enough. An advisory note may acquire high effective authority if it is always included in a late prompt position; a formal policy may have no effective authority if no component loads it. Placement within a channel is part of effective authority — the late-prompt example turns on position, not on the channel's kind.

## Misuse Cases

- Saying a memory "is active" without naming whether it advises a model, enters an instruction channel, enforces validation, influences ranking, or feeds training.
- Treating a Markdown file as low-authority because it is natural-language, even when the harness loads it as standing instruction.

---

Relevant Notes:

- [operative part](./operative-part.md) - unit: authority attaches to the behavior-shaping part and consumption path
- [lineage](./lineage.md) - interaction: derived artifacts with high authority need stronger invalidation discipline
- [retained artifact](./retained-artifact.md) - parent concept: the persisted state whose later use may shape behavior
- [knowledge artifact](./knowledge-artifact.md) - authority family: evidence, reference, context, explanation, or advice
- [system-definition artifact](./system-definition-artifact.md) - authority family: instruction, enforcement, routing, validation, configuration, evaluation, or learning input
- [a consumption channel delivers force without the history that earned it](../a-consumption-channel-delivers-force-without-the-history-that.md) - failure surface: the path confers force on its occupant without reading how it got there
- [six Commonplace paths establish broad addressability, not completeness](../evidence/six-commonplace-paths-establish-broad-addressability-not-completeness.md) - evidence boundary: scoped gates and validators expose applicability as an unresolved addition to the current record
