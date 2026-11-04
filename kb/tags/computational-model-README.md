---
description: Tag README — PL concepts (scoping, homoiconicity, partial evaluation, typing) applied to LLM instructions, plus the scheduling architecture that follows from context scarcity
type: types/tag-readme.md
---

# Computational model

Instruction interpretation, scoping, state and orchestration of bounded LLM calls. Assign this tag to explanations or comparisons of those execution mechanisms and their limits. Merely using an LLM or tools is insufficient. [Context-engineering](./context-engineering-README.md) asks what knowledge reaches a call; this tag asks how execution works. [Learning-theory](./learning-theory-README.md) covers learning and improvement.

**The formal computational model with the LLM inside is [Bounded-context orchestration model](../theory/bounded-context-orchestration-model.md):** closed-world orchestration with explicit state and barriered batches of independent LLM calls, in a conditional select/call normal form; its generality lemma is [any symbolic program with LLM calls is a select/call program](../theory/any-symbolic-program-with-llm-calls-is-a-select-call-program.md).

## Foundations

- [Prompting changes failure diagnosis with the semantic reference](../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) — model-defined programming and English instruction execution share a prediction problem but judge conformance against different references
- [Context efficiency](../theory/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — why context is the scarce resource; cost has two dimensions (volume and complexity) that drive the mechanisms below
- [Bounded-context orchestration](../theory/bounded-context-orchestration-model.md) — gives closed-world orchestration with explicit state and barriered independent call batches a conditional select/call normal form
- [LLM contexts interpret instructions and content through the same token medium](../theory/llm-context-interprets-instructions-and-content-through-one-medium.md) — instructions and data share the same representation, enabling extensibility but removing structural guardrails
- [Context scoping](../theory/llm-context-is-composed-without-scoping.md) — selected frame inputs limit direct access; scope among supplied instructions remains a separate question

## Scheduling & Orchestration

- [agent orchestration occupies a multi-dimensional design space](../theory/agent-orchestration-occupies-a-multi-dimensional-design-space.md) — scheduler placement, persistence, coordination form, guarantee, and return artifacts vary independently
- [agent orchestration needs coordination guarantees, not just coordination channels](../theory/agent-orchestration-needs-coordination-guarantees-not-just.md) — contamination, inconsistency, and amplification arise from different missing guarantees
- [Statecharts and programs differ in what they show, not in what they can compute](../theory/statecharts-and-programs-differ-in-what-they-show-not-compute.md) — control visibility: recursion and data-dependent fan-out read as code; fixed reactive control reads as a chart
- [Decomposition heuristics](../theory/decomposition-heuristics-for-bounded-context-scheduling.md) — practical rules: separate selection from joint reasoning, choose representations not subsets, save reusable intermediates
- [LLM-mediated schedulers](../theory/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — when the scheduler lives in an LLM conversation it degrades; three recovery strategies
- [session history should not be the default next context](../theory/session-history-should-not-be-the-default-next-context.md) — stored history and next-context loading are separate decisions; `select` should decide what to load
- [A context-operation interface bounds the projections its policy can realize](../theory/context-operation-interface-bounds-context-policy.md) — models context assembly as legal interface traces whose reachable projections remain distinct from policy quality
- [Claude Code dynamic workflows](../agentic-systems/reviews/claude-code-dynamic-workflows.md) — shipped instance of the cluster: a harness exposing a returning `agent()` plus host-language composition beneath its frozen loop

## Instruction Properties

- [English can approximate a model-defined prompt language](../theory/english-can-approximate-a-model-defined-prompt-language.md) — coarse clause meanings support local reasoning where their predictions hold; residual behavior bounds fidelity
- [Clear instructions can compose into an unsettled contract](../theory/clear-instructions-can-compose-into-an-unsettled-contract.md) — scope, precedence and exceptions can leave combined English requirements unsettled

- [Instruction writing styles](../theory/writing-styles-are-strategies-for-managing-underspecification.md) — five observed context-file writing styles as strategies for narrowing the interpretation space
- [Checks for prompt programming](../theory/programming-practices-for-prompts-need-question-specific-evidence.md) — checks matched to requirements, conformance, prediction and variation
- [Unified calling conventions](../theory/unified-calling-conventions-enable-bidirectional-refactoring.md) — calling conventions that let components move between neural and symbolic implementations
- [Local materialization should outperform distant natural-language declarations](../theory/local-materialization-should-outperform-distant-declarations.md) — untested comparison of declaration-only context with generated point-of-use views, under a single canonical maintenance authority
- [Model-resolved indirection adds interpretation work to LLM execution](../theory/model-resolved-indirection-adds-interpretation-work-to-llm-execution.md) — distinguishes references resolved by the model from aliases expanded by a deterministic executor and makes literalization conditional on token and lifecycle costs
- [frontloading spares execution context](../theory/frontloading-spares-execution-context.md) — partial evaluation applied to instructions: precompute known inputs and insert results to spare the consuming call's context budget

## Error Correction & Reliability

Dual-tagged with [LLM reliability](./llm-reliability-README.md), which provides the broader error theory; these claims are about the scheduling architecture.

- [LLM output deviation requires three-way diagnosis](../theory/llm-output-deviation-requires-three-way-diagnosis.md) — specification, interpreter and execution variation require different diagnostic questions
- [Scheduler–LLM error-correction asymmetry](../theory/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — symbolic operations are error-correctable through redundancy while LLM bookkeeping compounds errors silently
- [specification-level separation recovers scoping before it recovers error correction](../theory/specification-level-separation-recovers-scoping-before-it-recovers.md) — an intermediate regime where OpenProse-like DSLs recover frame isolation without hard-oracle bookkeeping

## Tensions

- Shared text supports extension but does not itself enforce scope. Explicit runtime boundaries can supply specific guarantees; adopting a model reference alone does not.

## Related Tags

- [llm-reliability](./llm-reliability-README.md) — error correction theory, oracle hardening, and reliability dimensions; explains *why* the scheduling architecture works
- [learning-theory](./learning-theory-README.md) — how systems learn through constraining, codification, and source-derived reshaping; the computational model explains *what kind of programs* these mechanisms operate on
- [context-engineering](./context-engineering-README.md) — the practical side: frontloading and indirection cost applied to what reaches the context

---

Agent Notes:
- 2026-03-10: the Scheduling & Orchestration cluster plus the Multi-Agent Aggregation note formed the core of a paper-outline workshop presenting the scheduling model for an academic audience; that workshop was local scratch, not a durable citation target.
