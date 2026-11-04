---
description: "Self-hosting LLM methodologies are closer to metacircular interpreters than compilers: agents re-interpret natural-language rules each session, while stable paths codify into validators and commands"
type: types/note.md
traits: [title-as-claim]
tags: [constraining, self-improving-systems, continual-learning, computational-model, learning-theory]
---

# LLM-executed methodologies are metacircular interpreters, not compilers

A methodology that LLM agents execute by reading its own artifacts is self-hosting in the interpreter sense, not the compiler sense. The host machine is the LLM plus harness. The methodology is encoded in natural-language content and structured files. When agents use that methodology to maintain the files that define it, the system is metacircular: the rules for operating the artifact system are themselves artifacts in that system.

This distinction matters because compiler self-hosting suggests a binary milestone: the compiler can build itself or it cannot. LLM-executed methodology is gradual. Some rules stay interpreted as natural language each session, some become structured skills, and some cross into symbolic consumers such as schemas, validators, tests, and commands.

## The interpreter shape

An LLM-executed methodology runs by being loaded, interpreted, and followed. A `COLLECTION.md` contract, type spec, skill, or review criterion changes future behavior only when an agent, validator, or command consumes it with force. That makes these files [system-definition artifacts](./definitions/system-definition-artifact.md), not merely documentation.

The metacircular part appears when those same artifacts govern edits to themselves. A notes collection contract can shape a note about note-writing. A validation rule can reject a stale mark in the type spec that defines the mark. A review criterion can be revised through the review machinery it helps define. This is stronger than using a wiki to document a separate system; the wiki and the operating methodology are one artifact system.

## Codification is the compiled path

The compiled analogue is [codification](./definitions/codification.md): committing a natural-language rule to symbolic execution. Packaging a practice as an instruction, skill, hook or command does not by itself establish that transition. A change is [constraining](./definitions/constraining.md) when it commits choices about applicability or acceptable responses, as [methodology enforcement](./methodology-enforcement-is-constraining.md) explains.

Consider a review rule: “Check that each claim has supporting evidence.” Moving that text into a skill can make it easier to find without changing when it applies or what counts as support. Requiring the review before publication settles its activation while leaving the support judgment to the reviewer. Adding a validator that rejects a missing review record codifies the record check; it does not codify the judgment that the evidence supports the claim.

The JIT analogy concerns selective implementation: particular operations can move into code while others remain interpreted. It does not make stability alone a reason to extract code. The choice depends on what the operation commits and how its conformance and task adequacy can be checked. A judgment-heavy review can remain natural language even when a required code check controls whether its acceptance has been recorded.

## Self-hosting remains partial

The interpreter analogy also keeps the autonomy claim honest. A self-hosting LLM methodology still depends on a host model, a harness, and often a human oracle. It governs self-extension only where the methodology settles the next meta-decisions: representation, verification, and authority. Where it does not, [a methodology governs its own extension only as far as it settles the meta-decisions it raises](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md).

The characteristic failure mode is the interpreter version of trusting-trust: an agent can follow a flawed methodology to revise that same methodology, propagating the flaw. The mitigation is not to deny self-hosting, but to keep weak-oracle paths human-inclusive and to codify only where verification is strong enough.

---

Relevant Notes:

- [methodology enforcement is constraining](./methodology-enforcement-is-constraining.md) — mechanism: separates commitments about activation from commitments about acceptable responses
- [codification](./definitions/codification.md) — defined-in: the natural-language-to-symbolic crossing that supplies the compiled path
- [system-definition artifact](./definitions/system-definition-artifact.md) — grounds: explains why methodology files can shape future behavior
- [a methodology governs its own extension only as far as it settles the meta-decisions it raises](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) — scope: why self-hosting remains partial and closure-bounded
