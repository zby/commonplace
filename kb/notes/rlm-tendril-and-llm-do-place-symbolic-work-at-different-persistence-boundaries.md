---
description: "Compares RLM, Tendril, and llm-do as three placements for symbolic work and interfaces: ephemeral REPL code, workspace-local generated tools, and durable unified callables"
type: kb/types/note.md
traits: [title-as-claim, has-comparison, has-external-sources]
tags: [computational-model, learning-theory]
status: seedling
---

# RLM, Tendril, and llm-do place symbolic work at different persistence boundaries

Recursive Language Models (RLM), Tendril, a workspace agent sandbox for generated capabilities, and llm-do, a hybrid agent/tool runtime, all move work out of raw conversation and onto a symbolic substrate. The useful distinction is not "agent versus tool" or even "LLM versus code"; it is where symbolic work is allowed to persist after the model has helped create or select it.

Here, a persistence boundary means the point at which generated or selected work stops being temporary and becomes reusable by later calls, sessions, or project code.

| System | Symbolic substrate | Who authors the symbolic work | Persistence boundary | Main affordance |
|---|---|---|---|---|
| RLM | Python REPL namespace plus `recursive_llm()` | The model writes task-local orchestration code | Per task; generated orchestrators are discarded | Cheap external bookkeeping without committing artifacts |
| Tendril | Workspace `tools/index.json` plus Deno TypeScript files | The model writes named executable capabilities | Cross-session within a workspace | Live task needs become reusable executable affordances |
| llm-do | Unified namespace of Python tools and `.agent` files | Humans and agents can move components across neural/symbolic implementations | Durable project/runtime call boundary | Components can be refactored between prompt and code without changing callers |

RLM is the cleanest version of symbolic execution without accumulation. The model writes orchestration code, but the REPL state is only a task-local substrate. That is powerful for bounded-context scheduling, meaning the choice of what each limited LLM call should see and do, because bookkeeping lives in variables and loops rather than in chat history. It also avoids the governance burden of keeping generated artifacts: there is no approval state, lifecycle, or stale code problem for an artifact that disappears after use.

Tendril chooses the next persistence point: externalize now, then keep the useful result as a workspace capability. It keeps the outer tool surface small, but lets the agent register a named executable capability when no existing one fits. That makes Tendril closer to [codification](./definitions/codification.md), committing a recurring behavior into executable code, than to ordinary memory. The learned artifact changes what the next session can execute, not just what information it can retrieve. The cost is that Tendril inherits the lifecycle questions RLM avoids: provenance, approval, tests, retirement, dependency drift, and permission scope.

llm-do addresses a different boundary. Its strongest idea is not that tools are callable, but that LLM-backed agents and symbolic tools share one calling convention. That makes neural-to-symbolic and symbolic-to-neural movement local: a component can be constrained into Python or relaxed back into an agent without changing the caller. Compared with Tendril, llm-do is less about autonomous creation of new tools and more about preserving a stable interface while implementation moves along the verifiability gradient, the spectrum from loose LLM-interpreted artifacts to deterministic, testable code.

The systems are therefore complementary rather than substitutes. RLM is the scratchpad pattern for model-authored orchestration. Tendril is the deployment-time promotion pattern for reusable generated tools. llm-do is the interface pattern that makes later refactoring across agent-backed and code-backed implementations cheap.

A combined system would likely use RLM-like ephemeral orchestration to explore a task, Tendril-like promotion when an executable pattern recurs, and llm-do-like unified calling so promoted artifacts can later be split, constrained, relaxed, or replaced without caller churn.

## Open Questions

- When should an RLM-style ephemeral program be promoted into a Tendril-style durable capability?
- What approval or testing threshold is enough for online generated tools without destroying the deployment-time learning loop?
- Can Tendril-style generated capabilities live inside an llm-do-style unified namespace without making name selection and lifecycle management too noisy?

---

Relevant Notes:

- [RLM has the model write ephemeral orchestrators over sub-agents](./rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md) — grounds: supplies the ephemeral REPL-orchestrator side of the comparison
- [Unified calling conventions enable bidirectional refactoring between neural and symbolic](./unified-calling-conventions-enable-bidirectional-refactoring.md) — grounds: supplies the llm-do call-boundary side of the comparison
- [Tendril](../agent-memory-systems/reviews/tendril.md) — evidence: source-inspected generated-capability system that occupies the cross-session workspace persistence point
- [Ephemeral computation prevents accumulation](./ephemeral-computation-prevents-accumulation.md) — mechanism: explains the accumulation trade-off that separates RLM from Tendril
- [Deploy-time learning is the missing middle](./deploy-time-learning-is-the-missing-middle.md) — mechanism: explains why Tendril's online capability registration is a durable behavior-change loop
- [The verifiability gradient](./verifiability-gradient.md) — mechanism: situates llm-do's movement between LLM-backed agents and Python functions
- [Agent orchestration occupies a multi-dimensional design space](./agent-orchestration-occupies-a-multi-dimensional-design-space.md) — extends: this note fills in one local comparison across scheduler placement, persistence horizon, and artifact class
- [Ingest: Recursive Language Models - what finally gave me the 'aha' moment](../sources/recursive-language-models-what-finally-gave-me-the-aha-moment-2035040781074145412.ingest.md) — evidence: practitioner walkthrough of RLM's REPL mechanism and symbolic variable return
