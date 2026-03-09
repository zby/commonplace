---
description: Index of notes applying programming language theory to LLM instructions — scoping, homoiconicity, partial evaluation, typing; the computational model of LLM-based systems viewed through PL concepts
type: index
status: current
---

# Computational model

Programming language concepts applied to LLM instructions and agent architectures. Where [learning-theory](./learning-theory.md) covers how systems learn and improve, and [kb-design](./kb-design.md) covers how knowledge bases are built and operated, this area covers the computational properties of the medium itself — what kind of "programs" LLM instructions are, and what PL concepts illuminate their behavior.

## Foundations

- [agentic-systems-interpret-underspecified-instructions](./agentic-systems-interpret-underspecified-instructions.md) — the core framing: underspecified semantics and execution indeterminism as the two properties that distinguish LLM instructions from traditional programs; also foundational to [learning-theory](./learning-theory.md)
- [context-efficiency-is-the-central-design-concern-in-agent-systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — the foundational argument for why context is the scarce resource; context cost has two dimensions (volume and complexity); connects all the PL-inspired mechanisms to this dual pressure
- [llm-context-is-a-homoiconic-medium](./llm-context-is-a-homoiconic-medium.md) — instructions and data share the same representation (natural language tokens), enabling extensibility but removing structural guardrails; precedents in Lisp, Emacs, Smalltalk
- [llm-context-is-composed-without-scoping](./llm-context-is-composed-without-scoping.md) — context is flat concatenation with no scoping, producing dynamic scoping's pathologies; sub-agents are the one mechanism for isolation, using lexically scoped frames

## Scheduling & Orchestration

- [symbolic-scheduling-over-bounded-llm-calls-is-the-right-model-for-agent-orchestration](./symbolic-scheduling-over-bounded-llm-calls-is-the-right-model-for-agent-orchestration.md) — the clean model: an unbounded symbolic scheduler manages exact state and issues bounded LLM calls for semantic judgment
- [decomposition-rules-for-bounded-context-scheduling](./decomposition-rules-for-bounded-context-scheduling.md) — preliminary practical rules for scheduling bounded LLM calls: separate selection from joint reasoning, choose representations not subsets, save reusable intermediates in scheduler state
- [llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — when the scheduler lives in an LLM conversation it degrades; three recovery strategies restore the clean separation to increasing degrees
- [bounded-context-orchestration-model](./bounded-context-orchestration-model.md) — formalises agent orchestration as the select/execute/absorb loop over bounded context, with the selection function as the central optimisation problem
- [rlm-is-the-clean-model-with-llm-authored-scheduler](./rlm-is-the-clean-model-with-llm-authored-scheduler.md) — RLM instantiates the symbolic-scheduler model by having the LLM write the scheduler as code; achieves clean separation but discards the scheduler after each run
- [solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking-better-designs](./solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking-better-designs.md) — sequencing heuristic: commit least-flexible decisions first so high-flexibility choices cannot block scarce valid placements

## Instruction Properties

- [writing-styles-are-strategies-for-managing-underspecification](./writing-styles-are-strategies-for-managing-underspecification.md) — the five empirically observed context-file writing styles correspond to different strategies for narrowing the agent's interpretation space
- [programming-practices-apply-to-prompting](./programming-practices-apply-to-prompting.md) — typing, testing, version control transfer to prompting with modified cost models
- [unified-calling-conventions-enable-bidirectional-refactoring](./unified-calling-conventions-enable-bidirectional-refactoring.md) — calling conventions that let components move between neural and symbolic implementations

## Related notes in other areas

- [frontloading-spares-execution-context](./frontloading-spares-execution-context.md) (kb-design) — partial evaluation applied to LLM instructions; the mechanism behind indirection elimination and build-time generation
- [indirection-is-costly-in-llm-instructions](./indirection-is-costly-in-llm-instructions.md) (kb-design) — the cost model for indirection differs fundamentally between code and LLM instructions

## Multi-Agent Aggregation

- [synthesis-is-not-error-correction](./synthesis-is-not-error-correction.md) — merging agent outputs (synthesis) propagates errors; voting discards minorities and corrects them; Kim et al.'s -3.5% result reflects synthesis failure, not a verdict on multi-agent error correction

## Tensions

- The homoiconic medium enables extensibility (ad hoc prompts, unified calling conventions) but requires explicit scoping disciplines (lexical frames, tier separation) precisely because there are no structural boundaries. The stabilisation gradient from instructions to scripts is one response — crystallising imposes the structure the medium lacks.

## Related Areas

- [learning-theory](./learning-theory.md) — how systems learn through stabilisation, crystallisation, distillation; the computational model explains *what kind of programs* these mechanisms operate on
- [kb-design](./kb-design.md) — practical architecture that applies these computational properties; frontloading and indirection cost are PL concepts applied to KB instructions
