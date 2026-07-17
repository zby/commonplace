---
description: Tag README — PL concepts (scoping, homoiconicity, partial evaluation, typing) applied to LLM instructions, plus the scheduling architecture that follows from context scarcity
type: kb/types/tag-readme.md
index_source: tag
index_key: computational-model
---

# Computational model

What kind of "programs" LLM instructions are, and what programming-language concepts — scoping, homoiconicity, partial evaluation, typing — illuminate their behavior. Where [learning-theory](./learning-theory-README.md) covers how systems learn and [tags](./tags-README.md) covers how knowledge bases are operated, this area covers the computational properties of the medium itself and the scheduling architecture that follows from context scarcity. This is a selective head; the published site appends the complete listing, and the scoped `rg` recipes recover full membership.

## Foundations

- [agentic-systems-interpret-underspecified-instructions](./agentic-systems-interpret-underspecified-instructions.md) — core framing: LLM instructions are distinguished by underspecified semantics and execution indeterminism
- [context-efficiency-is-the-central-design-concern-in-agent-systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — why context is the scarce resource; cost has two dimensions (volume and complexity) that drive the mechanisms below
- [bounded-context-orchestration-model](./bounded-context-orchestration-model.md) — formalises orchestration as a symbolic scheduler driving bounded LLM calls through a select/call loop with explicit state update
- [llm-context-is-a-homoiconic-medium](./llm-context-is-a-homoiconic-medium.md) — instructions and data share the same representation, enabling extensibility but removing structural guardrails
- [llm-context-is-composed-without-scoping](./llm-context-is-composed-without-scoping.md) — context is flat concatenation with no scoping, producing dynamic scoping's pathologies; sub-agents are the one isolation mechanism

## Scheduling & Orchestration

- [agent orchestration occupies a multi-dimensional design space](./agent-orchestration-occupies-a-multi-dimensional-design-space.md) — scheduler placement, persistence, coordination form, guarantee, and return artifacts vary independently
- [agent orchestration needs coordination guarantees, not just coordination channels](./agent-orchestration-needs-coordination-guarantees-not-just.md) — contamination, inconsistency, and amplification arise from different missing guarantees
- [decomposition-heuristics-for-bounded-context-scheduling](./decomposition-heuristics-for-bounded-context-scheduling.md) — practical rules: separate selection from joint reasoning, choose representations not subsets, save reusable intermediates
- [llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — when the scheduler lives in an LLM conversation it degrades; three recovery strategies
- [session history should not be the default next context](./session-history-should-not-be-the-default-next-context.md) — stored history and next-context loading are separate decisions; `select` should decide what to load
- [tool loop](./tool-loop-README.md) — the tool-loop area: loop exposure, hidden schedulers, and the observability problems of framework-owned loops (apparent success, semantic recovery)
- [Claude Code dynamic workflows](../agentic-systems/claude-code-dynamic-workflows.md) — shipped instance of the cluster: a harness exposing a returning `agent()` plus host-language composition beneath its frozen loop

## Instruction Properties

- [writing-styles-are-strategies-for-managing-underspecification](./writing-styles-are-strategies-for-managing-underspecification.md) — five observed context-file writing styles as strategies for narrowing the interpretation space
- [programming-practices-apply-to-prompting](./underspecification-and-indeterminism-complicate-programming-for.md) — typing, testing, version control transfer to prompting with modified cost models
- [unified-calling-conventions-enable-bidirectional-refactoring](./unified-calling-conventions-enable-bidirectional-refactoring.md) — calling conventions that let components move between neural and symbolic implementations
- [prose has no reliable dereference, so a declared fact must be reinforced where it applies](./prose-has-no-dereference-reinforce-facts-at-point-of-use.md) — name resolution holds in formal systems but not in LLM-read prose, so single-source-of-truth gives way to checked denormalization
- [indirection is costly in LLM instructions](./indirection-is-costly-in-llm-instructions.md) — indirection is nearly free at runtime in code but costs context and interpretation overhead on every read in prompts
- [frontloading spares execution context](./frontloading-spares-execution-context.md) — partial evaluation applied to instructions: precompute known inputs and insert results to spare the consuming call's context budget

## Error Correction & Reliability

Dual-tagged with [LLM interpretation errors](./llm-interpretation-errors-README.md), which provides the broader error theory; these claims are about the scheduling architecture.

- [scheduler-llm-separation-exploits-an-error-correction-asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — symbolic operations are error-correctable through redundancy while LLM bookkeeping compounds errors silently
- [specification-level separation recovers scoping before it recovers error correction](./specification-level-separation-recovers-scoping-before-it-recovers.md) — an intermediate regime where OpenProse-like DSLs recover frame isolation without hard-oracle bookkeeping

## Tensions

- The homoiconic medium enables extensibility (ad hoc prompts, unified calling conventions) but requires explicit scoping disciplines precisely because there are no structural boundaries. The constraining gradient from instructions to scripts is one response — codifying imposes the structure the medium lacks.

## Related Tags

- [llm-interpretation-errors](./llm-interpretation-errors-README.md) — error correction theory, oracle hardening, and reliability dimensions; explains *why* the scheduling architecture works
- [tool-loop](./tool-loop-README.md) — the loop-exposure and hidden-scheduler cluster, including the observability failures of framework-owned loops
- [learning-theory](./learning-theory-README.md) — how systems learn through constraining, codification, distillation; the computational model explains *what kind of programs* these mechanisms operate on
- [tags](./tags-README.md) — practical architecture applying these computational properties; frontloading and indirection cost are PL concepts applied to KB instructions

---

Agent Notes:
- 2026-03-10: the Scheduling & Orchestration cluster plus the Multi-Agent Aggregation note formed the core of a paper-outline workshop presenting the scheduling model for an academic audience; that workshop was local scratch, not a durable citation target.
