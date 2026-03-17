---
description: Index of notes applying programming language theory to LLM instructions — scoping, homoiconicity, partial evaluation, typing; the computational model of LLM-based systems viewed through PL concepts
type: index
status: current
---

# Computational model

Programming language concepts applied to LLM instructions and agent architectures. Where [learning-theory](./learning-theory-index.md) covers how systems learn and improve, and [tags](./tags-index.md) covers how knowledge bases are built and operated, this area covers the computational properties of the medium itself — what kind of "programs" LLM instructions are, and what PL concepts illuminate their behavior.

## Foundations

- [agentic-systems-interpret-underspecified-instructions](./agentic-systems-interpret-underspecified-instructions.md) — the core framing: underspecified semantics and execution indeterminism as the two properties that distinguish LLM instructions from traditional programs; also foundational to [learning-theory](./learning-theory-index.md)
- [context-efficiency-is-the-central-design-concern-in-agent-systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — the foundational argument for why context is the scarce resource; context cost has two dimensions (volume and complexity); connects all the PL-inspired mechanisms to this dual pressure
- [effective-context-is-task-relative-and-complexity-relative-not-a-fixed-model-constant](./effective-context-is-task-relative-and-complexity-relative-not-a-fixed-model-constant.md) — synthesis: usable context varies with task type and prompt complexity, so raw window size is too coarse a model of what fits
- [bounded-context-orchestration-model](./bounded-context-orchestration-model.md) — formalises agent orchestration as a symbolic scheduler driving bounded LLM calls through a select/call/absorb loop; the computational model that follows from context scarcity
- [agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate](./agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md) — synthesis: the runtime-level taxonomy connecting the scheduler model, context engineering, and inspectable external state into one architecture
- [llm-context-is-a-homoiconic-medium](./llm-context-is-a-homoiconic-medium.md) — instructions and data share the same representation (natural language tokens), enabling extensibility but removing structural guardrails; precedents in Lisp, Emacs, Smalltalk
- [llm-context-is-composed-without-scoping](./llm-context-is-composed-without-scoping.md) — context is flat concatenation with no scoping, producing dynamic scoping's pathologies; sub-agents are the one mechanism for isolation, using lexically scoped frames

## Scheduling & Orchestration

- [agent orchestration occupies a multi-dimensional design space](./agent-orchestration-occupies-a-multi-dimensional-design-space.md) — synthesis: scheduler placement, persistence horizon, coordination form, coordination guarantee, and return artifacts vary independently, so architectures do not sit on a single ladder
- [agent orchestration needs coordination guarantees, not just coordination channels](./agent-orchestration-needs-coordination-guarantees-not-just-coordination-channels.md) — sharpens: coordination form and coordination guarantee are separate dimensions because contamination, inconsistency, and amplification arise from different missing guarantees
- [session history should not be the default next context](./session-history-should-not-be-the-default-next-context.md) — protocol-level claim: session or tool-loop history may be worth storing, but `select` should decide next context rather than inheriting history by default
- [llm frameworks should expose the loop](./llm-frameworks-should-expose-the-loop.md) — the implementation-level claim: tool calls are not enough unless frameworks keep state progression and recursion exposed to application code
- [apparent success is an unreliable health signal in framework-owned tool loops](./apparent-success-is-an-unreliable-health-signal-in-framework-owned-tool-loops.md) — when agent workarounds hide broken tools, final success stops being evidence that the underlying scripts and workflows are healthy
- [silent disambiguation is the semantic analogue of tool fallback](./silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) — the same hidden-recovery problem appears when the missing piece is semantic rather than operational: an ambiguous spec forces a runtime branch that completion alone does not reveal
- [traditional debugging intuitions break when tool loops can recover semantically](./traditional-debugging-intuitions-break-when-tool-loops-can-recover-semantically.md) — programmers trained on traditional software expect broken mechanisms to fail loudly; semantic recovery breaks that heuristic and hides where debugging effort should go
- [decomposition-rules-for-bounded-context-scheduling](./decomposition-rules-for-bounded-context-scheduling.md) — preliminary practical rules for scheduling bounded LLM calls: separate selection from joint reasoning, choose representations not subsets, save reusable intermediates in scheduler state
- [llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — when the scheduler lives in an LLM conversation it degrades; three recovery strategies restore the clean separation to increasing degrees
- [rlm-achieves-the-clean-scheduler-model-but-opts-out-of-accumulation](./rlm-achieves-the-clean-scheduler-model-but-opts-out-of-accumulation.md) — RLM instantiates the symbolic-scheduler model by having the LLM write the scheduler as code; achieves clean separation but discards the scheduler after each run
- [solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking-better-designs](./solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking-better-designs.md) — sequencing heuristic: commit least-flexible decisions first so high-flexibility choices cannot block scarce valid placements
- [conversation-vs-prompt-refinement-in-agent-to-agent-coordination](./conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) — tradeoff analysis of conversation, prompt refinement, and context cloning for sub-agent coordination; each shifts costs differently between caller and callee depending on architecture

## Instruction Properties

- [writing-styles-are-strategies-for-managing-underspecification](./writing-styles-are-strategies-for-managing-underspecification.md) — the five empirically observed context-file writing styles correspond to different strategies for narrowing the agent's interpretation space
- [programming-practices-apply-to-prompting](./programming-practices-apply-to-prompting.md) — typing, testing, version control transfer to prompting with modified cost models
- [unified-calling-conventions-enable-bidirectional-refactoring](./unified-calling-conventions-enable-bidirectional-refactoring.md) — calling conventions that let components move between neural and symbolic implementations

## Related notes in other areas

- [frontloading-spares-execution-context](./frontloading-spares-execution-context.md) (kb-design) — partial evaluation applied to LLM instructions; the mechanism behind indirection elimination and build-time generation
- [indirection-is-costly-in-llm-instructions](./indirection-is-costly-in-llm-instructions.md) (kb-design) — the cost model for indirection differs fundamentally between code and LLM instructions

## Error Correction & Reliability

These notes are dual-tagged with [LLM interpretation errors](./llm-interpretation-errors-index.md), which provides the broader error-theory context. They appear here because their claims are about the scheduling architecture.

- [scheduler-llm-separation-exploits-an-error-correction-asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — conjectures that the scheduling model works because symbolic operations are error-correctable through redundancy while LLM bookkeeping compounds errors silently
- [specification-level separation recovers scoping before it recovers error correction](./specification-level-separation-recovers-scoping-before-it-recovers-error-correction.md) — identifies an intermediate regime where OpenProse-like DSLs recover frame isolation without yet gaining hard-oracle bookkeeping
- [synthesis-is-not-error-correction](./synthesis-is-not-error-correction.md) (llm-interpretation-errors) — merging agent outputs propagates errors; voting discards minorities and corrects them; the aggregation operation must match the decomposition structure

## Tensions

- The homoiconic medium enables extensibility (ad hoc prompts, unified calling conventions) but requires explicit scoping disciplines (lexical frames, tier separation) precisely because there are no structural boundaries. The constraining gradient from instructions to scripts is one response — codifying imposes the structure the medium lacks.

## Related Tags

- [llm-interpretation-errors](./llm-interpretation-errors-index.md) — error correction theory, oracle hardening, and reliability dimensions; explains *why* the scheduling architecture works
- [learning-theory](./learning-theory-index.md) — how systems learn through constraining, codification, distillation; the computational model explains *what kind of programs* these mechanisms operate on
- [tags](./tags-index.md) — practical architecture that applies these computational properties; frontloading and indirection cost are PL concepts applied to KB instructions

---

Agent Notes:
- 2026-03-10: the Scheduling & Orchestration cluster plus the Multi-Agent Aggregation note form the core of a [paper outline](../work/paper-bounded-context-orchestration/outline-v2.md) presenting the scheduling model for an academic audience. The error-correction conjecture is now captured as [scheduler-llm-separation-exploits-an-error-correction-asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md). The framework spectrum (Section 5) is not yet a standalone KB note.

## Other tagged notes <!-- generated -->

- [Context engineering](./context-engineering.md) — Definition — context engineering is the architecture and machinery for getting the right knowledge into a bounded context at the right time — routing, loading, scoping, and maintenance; distillation is its main operation but not the only one
