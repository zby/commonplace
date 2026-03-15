---
description: OpenProse-like DSLs expose control flow and discretion boundaries while leaving scheduling and validation on the LLM substrate, creating an intermediate regime between flat prompting and symbolic scheduling
type: note
tags: [computational-model, llm-interpretation-errors]
status: current
---

# Specification-level separation recovers scoping before it recovers error correction

OpenProse is a useful tension case for the [scheduler-LLM separation conjecture](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md). It tries to make an LLM session behave like a symbolic executor without moving the interpreter into code. The repo provides a workflow DSL (`.prose`), an execution specification (`prose.md`), a compile/validation specification (`compiler.md`), and explicit state protocols for files and databases. That is not the clean model. But it is not just flat prompting either.

The important observation is that some benefits of separation arrive *before* the medium boundary. OpenProse names control-flow structure (`parallel`, `retry`, `resume`, loops), makes discretionary judgments explicit via `**...**`, and externalises intermediate state into bindings and agent memory files instead of keeping everything in one conversation. Those are real gains. They reduce prompt ambiguity, create cleaner frame boundaries, and recover some of the scoping benefits described in [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md).

What does **not** arrive yet is the main reliability mechanism from the error-correction note. The parser, validator, scheduler, and branch evaluator are still LLM-mediated. `prose compile` is another prose specification interpreted by the model, not a deterministic parser. `**...**` conditions are explicit soft-oracle checkpoints. Even the "VM" is induced behavior inside an existing agent runtime rather than a substrate with discrete-state restoration. The boundary between symbolic bookkeeping and semantic judgment is *named*, but not yet *hardened*.

This creates an intermediate regime:

- **Flat prompting** — no explicit scheduler vocabulary, no stable frame interfaces, state mostly lives in conversation
- **Specification-level separation** — control flow is named, state protocols are externalised, judgment holes are marked, but execution still depends on LLM compliance
- **Architectural separation** — bookkeeping moves to code or another hard-oracle substrate; the LLM handles only the semantic steps

The intermediate regime matters because it explains why systems like OpenProse can feel substantially better than raw prompting without yet earning the full error-correction benefits of symbolic execution. Syntax and file protocols can recover scoping, resumability, and some orchestration discipline before they recover hard reliability. The scheduler note should therefore not read as a binary "either fully separated or worthless." There is a meaningful middle ground.

This ordering — scoping first, error correction second — is specific to specification-level approaches that work by naming structure within the LLM's own execution. Tool-use frameworks (function calling with typed parameters, JSON schema validation) take a different path: they codify the interface contract, giving hard-oracle checks on output format without recovering scoping within the LLM's reasoning. That is mini-codification at the boundary, not specification-level separation — a different route to partial reliability that does not pass through the intermediate regime described here.

The cost of staying in that middle ground is that bookkeeping is still paid for on the stochastic substrate. The system can mark the symbolic/semantic boundary, but it cannot use hard oracles to enforce most of it. This means the asymmetry from [scheduler-LLM separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) still applies; OpenProse shows where the scoping gains start, not where the error-correction argument stops.

---

Relevant Notes:

- [scheduler-LLM separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — tension: OpenProse-like systems recover some benefits of separation without crossing the medium boundary, so the note needs an explicit middle regime
- [LLM-mediated schedulers are a degraded variant of the clean model](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — extends: this note identifies a stronger subclass of degraded schedulers that externalise state and expose control flow without fully factoring into code
- [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — grounds: the main gains OpenProse gets early are scoping gains, not hard reliability gains
- [programming practices apply to prompting](./programming-practices-apply-to-prompting.md) — explains why a DSL and explicit state protocols help before codification
- [codification](./codification.md) — contrasts: OpenProse constrains orchestration practice but does not codify the runtime semantics
- [oracle-strength-spectrum](./oracle-strength-spectrum.md) — grounds: compile-time validation and `**...**` conditions remain soft-oracle operations
