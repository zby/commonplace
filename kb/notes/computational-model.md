---
description: Index of notes applying programming language theory to LLM instructions — scoping, homoiconicity, partial evaluation, typing; the computational model of LLM-based systems viewed through PL concepts
type: index
status: current
---

# Computational model

Programming language concepts applied to LLM instructions and agent architectures. Where [learning-theory](./learning-theory.md) covers how systems learn and improve, and [claw-design](./claw-design.md) covers how claws are built and operated, this area covers the computational properties of the medium itself — what kind of "programs" LLM instructions are, and what PL concepts illuminate their behavior.

## Foundations

- [agentic-systems-interpret-underspecified-instructions](./agentic-systems-interpret-underspecified-instructions.md) — the core framing: underspecified semantics and execution indeterminism as the two properties that distinguish LLM instructions from traditional programs; also foundational to [learning-theory](./learning-theory.md)
- [llm-context-is-a-homoiconic-medium](./llm-context-is-a-homoiconic-medium.md) — instructions and data share the same representation (natural language tokens), enabling extensibility but removing structural guardrails; precedents in Lisp, Emacs, Smalltalk
- [llm-context-is-composed-without-scoping](./llm-context-is-composed-without-scoping.md) — context is flat concatenation with no scoping, producing dynamic scoping's pathologies; sub-agents are the one mechanism for isolation, using lexically scoped frames

## Related notes in other areas

- [frontloading-spares-execution-context](./frontloading-spares-execution-context.md) (claw-design) — partial evaluation applied to LLM instructions; the mechanism behind indirection elimination and build-time generation
- [indirection-is-costly-in-llm-instructions](./indirection-is-costly-in-llm-instructions.md) (claw-design) — the cost model for indirection differs fundamentally between code and LLM instructions
- [programming-practices-apply-to-prompting](./programming-practices-apply-to-prompting.md) (learning-theory) — typing, testing, version control transfer to prompting with modified cost models
- [unified-calling-conventions-enable-bidirectional-refactoring](./unified-calling-conventions-enable-bidirectional-refactoring.md) (learning-theory) — calling conventions that let components move between neural and symbolic implementations

## Tensions

- The homoiconic medium enables extensibility (ad hoc prompts, unified calling conventions) but requires explicit scoping disciplines (lexical frames, tier separation) precisely because there are no structural boundaries. The stabilisation gradient from instructions to scripts is one response — crystallising imposes the structure the medium lacks.

## Related Areas

- [learning-theory](./learning-theory.md) — how systems learn through stabilisation, crystallisation, distillation; the computational model explains *what kind of programs* these mechanisms operate on
- [claw-design](./claw-design.md) — practical architecture that applies these computational properties; frontloading and indirection cost are PL concepts applied to claw instructions

