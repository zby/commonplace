---
description: Tag index — PL concepts (scoping, homoiconicity, partial evaluation, typing) applied to LLM instructions, plus the scheduling architecture that follows from context scarcity
type: index
status: current
---

# Computational model

What kind of "programs" LLM instructions are, and what programming-language concepts — scoping, homoiconicity, partial evaluation, typing — illuminate their behavior. Where [learning-theory](./learning-theory-index.md) covers how systems learn and [tags](./tags-index.md) covers how knowledge bases are operated, this index covers the computational properties of the medium itself and the scheduling architecture that follows from context scarcity.

## Foundations

- [agentic-systems-interpret-underspecified-instructions](./agentic-systems-interpret-underspecified-instructions.md) — core framing: LLM instructions are distinguished by underspecified semantics and execution indeterminism; also foundational to [learning-theory](./learning-theory-index.md)
- [context-efficiency-is-the-central-design-concern-in-agent-systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — why context is the scarce resource; cost has two dimensions (volume and complexity) that drive the mechanisms below
- [effective-context-is-task-relative-and-complexity-relative-not-a-fixed-model-constant](./effective-context-is-task-relative-and-complexity-relative-not-a-fixed-model-constant.md) — usable context varies with task type and prompt complexity, so raw window size is too coarse
- [bounded-context-orchestration-model](./bounded-context-orchestration-model.md) — formalises orchestration as a symbolic scheduler driving bounded LLM calls through select/call/absorb
- [agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate](./agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md) — runtime taxonomy connecting scheduler, context engine, and inspectable external state
- [llm-context-is-a-homoiconic-medium](./llm-context-is-a-homoiconic-medium.md) — instructions and data share the same representation (natural language tokens), enabling extensibility but removing structural guardrails; precedents in Lisp, Emacs, Smalltalk
- [llm-context-is-composed-without-scoping](./llm-context-is-composed-without-scoping.md) — context is flat concatenation with no scoping, producing dynamic scoping's pathologies; sub-agents are the one mechanism for isolation

## Scheduling & Orchestration

### Design space & decomposition

- [agent orchestration occupies a multi-dimensional design space](./agent-orchestration-occupies-a-multi-dimensional-design-space.md) — scheduler placement, persistence, coordination form, guarantee, and return artifacts vary independently
- [agent orchestration needs coordination guarantees, not just coordination channels](./agent-orchestration-needs-coordination-guarantees-not-just-coordination-channels.md) — contamination, inconsistency, and amplification arise from different missing guarantees
- [decomposition-rules-for-bounded-context-scheduling](./decomposition-rules-for-bounded-context-scheduling.md) — practical rules: separate selection from joint reasoning, choose representations not subsets, save reusable intermediates
- [semantic-sub-goals-that-exceed-one-context-window-become-scheduling-problems](./semantic-sub-goals-that-exceed-one-context-window-become-scheduling-problems.md) — goals too large for one call require symbolic partitioning and staged aggregation
- [solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking-better-designs](./solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking-better-designs.md) — sequencing heuristic: commit least-flexible decisions first

### Scheduler implementation

- [llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — when the scheduler lives in an LLM conversation it degrades; three recovery strategies
- [rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents](./rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md) — the LLM writes the scheduler as code, achieving clean separation but discarding it after each run

### Session history & handoff

- [the chat-history model trades context efficiency for implementation simplicity](./the-chat-history-model-trades-context-efficiency-for-implementation-simplicity.md) — chat became the default because transcript carry-forward is cheap to build and preserves information
- [session history should not be the default next context](./session-history-should-not-be-the-default-next-context.md) — stored history and next-context loading are separate decisions; `select` should decide what to load
- [conversation-vs-prompt-refinement-in-agent-to-agent-coordination](./conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) — conversation preserves trace, prompt refinement compresses it, context cloning forks a prefix

### Tool loop & hidden scheduling

- [tool loop](./tool-loop-index.md) — tool calls are not enough unless frameworks keep state progression and recursion exposed
- [subtasks that need different tools force loop exposure in agent frameworks](./subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks.md) — the decisive boundary: child tasks need fresh tool surfaces, not one fixed loop
- [stateful tools recover control by becoming hidden schedulers](./stateful-tools-recover-control-by-becoming-hidden-schedulers.md) — hidden loops can recover substantial control by relocating the scheduler into tools
- [codified scheduling patterns can turn tools into hidden schedulers](./codified-scheduling-patterns-can-turn-tools-into-hidden-schedulers.md) — once next-step policy stabilizes into code, hiding it collapses orchestration into covert runtime logic

### Observability & error masking

- [apparent success is an unreliable health signal in framework-owned tool loops](./apparent-success-is-an-unreliable-health-signal-in-framework-owned-tool-loops.md) — agent workarounds hide broken tools, so final success stops being evidence of healthy scripts
- [silent disambiguation is the semantic analogue of tool fallback](./silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) — the same hidden-recovery problem for semantic rather than operational missing pieces
- [traditional debugging intuitions break when tool loops can recover semantically](./traditional-debugging-intuitions-break-when-tool-loops-can-recover-semantically.md) — semantic recovery hides where debugging effort should go

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

- ["Agent" is a useful technical convention, not a definition](./agent-is-a-tool-loop.md) — A lightweight technical convention — an agent is a tool loop (prompt, capability surface, stop condition) — sidestepping the definitional debate in favor of a unit that organizes code
- [Context engineering](./context-engineering.md) — Definition — context engineering is the discipline of designing systems around bounded-context constraints; its operational core is routing, loading, scoping, and maintenance for each bounded call
- [Pointer design tradeoffs in progressive disclosure](./pointer-design-tradeoffs-in-progressive-disclosure.md) — Design tradeoffs for progressive disclosure pointers — context-specificity vs precomputation cost vs reliability; fixed pointers (descriptions, abstracts) trade specificity for reliability and cheap reads, query-time pointers (re-rankers) trade cost for specificity, crafted pointers (link phrases) achieve highest density but depend on authoring discipline
