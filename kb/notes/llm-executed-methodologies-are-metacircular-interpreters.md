---
description: "Self-hosting LLM methodologies are closer to metacircular interpreters than compilers: agents re-interpret prose rules each session, while stable paths codify into validators and commands"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, constraining]
---

# LLM-executed methodologies are metacircular interpreters, not compilers

A methodology that LLM agents execute by reading its own artifacts is self-hosting in the interpreter sense, not the compiler sense. The host machine is the LLM plus harness. The methodology is source code in prose and structured files. When agents use that methodology to maintain the files that define it, the system is metacircular: the rules for operating the artifact system are themselves artifacts in that system.

This distinction matters because compiler self-hosting suggests a binary milestone: the compiler can build itself or it cannot. LLM-executed methodology is gradual. Some rules stay interpreted as prose each session, some become structured skills, and some cross into symbolic consumers such as schemas, validators, tests, and commands.

## The interpreter shape

An LLM-executed methodology runs by being loaded, interpreted, and followed. A `COLLECTION.md` contract, type spec, skill, or review criterion changes future behavior only when an agent, validator, or command consumes it with force. That makes these files [system-definition artifacts](./definitions/system-definition-artifact.md), not merely documentation.

The metacircular part appears when those same artifacts govern edits to themselves. A notes collection contract can shape a note about note-writing. A validation rule can reject a stale mark in the type spec that defines the mark. A review criterion can be revised through the review machinery it helps define. This is stronger than using a wiki to document a separate system; the wiki and the operating methodology are one artifact system.

## Codification is the compiled path

The compiled analogue is [codification](./definitions/codification.md). A practice starts as interpreted prose while its meaning is still moving, then moves down the enforcement gradient as it stabilizes: instruction, skill, hook, script, schema, validator, or command. That is why [methodology enforcement is constraining](./methodology-enforcement-is-constraining.md): each step reduces semantic underspecification and execution indeterminism.

This is closer to a JIT than to whole-program compilation. Stable hot paths become symbolic artifacts with assigned consequences; unsettled judgment stays in prose where humans and agents can still revise the interpretation cheaply.

## Self-hosting remains partial

The interpreter analogy also keeps the autonomy claim honest. A self-hosting LLM methodology still depends on a host model, a harness, and often a human oracle. It governs self-extension only where the methodology settles the next meta-decisions: representation, verification, and authority. Where it does not, [a methodology governs its own extension only as far as it settles the meta-decisions it raises](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md).

The characteristic failure mode is the interpreter version of trusting-trust: an agent can follow a flawed methodology to revise that same methodology, propagating the flaw. The mitigation is not to deny self-hosting, but to keep weak-oracle paths human-inclusive and to codify only where verification is strong enough.

---

Relevant Notes:

- [methodology enforcement is constraining](./methodology-enforcement-is-constraining.md) — mechanism: the interpreted-to-symbolic enforcement gradient
- [codification](./definitions/codification.md) — defined-in: the prose-to-symbolic crossing that supplies the compiled path
- [system-definition artifact](./definitions/system-definition-artifact.md) — grounds: explains why methodology files can shape future behavior
- [a methodology governs its own extension only as far as it settles the meta-decisions it raises](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) — scope: why self-hosting remains partial and closure-bounded
