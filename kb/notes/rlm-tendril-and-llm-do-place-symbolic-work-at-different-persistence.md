---
description: "Compares RLM variants, Tendril, and llm-do as placements for symbolic work and interfaces: ephemeral REPL code, typed RLM combinators, workspace-local generated tools, and durable unified callables"
type: kb/types/note.md
traits: [title-as-claim, has-comparison, has-external-sources]
tags: [computational-model, learning-theory, artifact-analysis]
status: seedling
---

# RLM, Tendril, and llm-do place symbolic work at different persistence boundaries

Recursive Language Models (RLM), Tendril, a workspace agent sandbox for generated capabilities, and llm-do, a hybrid agent/tool runtime, all move work out of raw conversation and onto a symbolic substrate. The useful distinction is not "agent versus tool" or even "LLM versus code"; it is where symbolic work is allowed to persist after the model has helped create or select it, and how tightly the symbolic control language is restricted.

Here, a persistence boundary means the point at which generated or selected work stops being temporary and becomes reusable by later calls, sessions, or project code.

Restriction and persistence are separate axes. Standard RLM and λ-RLM both keep the RLM prompt-as-environment architecture and per-task persistence boundary. They differ inside that boundary: standard RLM lets the model write arbitrary REPL code, while λ-RLM constrains orchestration to a pre-verified typed combinator library selected by a planner.

| System | Symbolic substrate | Who authors/selects the symbolic work | Persistence boundary | Recursive LLM calls | Control-language restriction | Main affordance |
|---|---|---|---|---|---|---|
| RLM | Python REPL namespace plus `recursive_llm()` | The model writes task-local orchestration code | Per task; generated orchestrators are discarded | Built in through `recursive_llm()` | Arbitrary model-authored REPL code | Cheap external bookkeeping without committing artifacts |
| λ-RLM | REPL environment plus typed combinator runtime (`SPLIT`, `MAP`, `FILTER`, `REDUCE`) | A planner selects a pre-verified combinator chain; the model handles bounded leaf calls | Per task; planned execution state is discarded | Built into the recursive executor over bounded leaves | Restricted typed combinator vocabulary | RLM-style prompt-as-environment recursion with auditable control flow and formal bounds |
| Tendril | Workspace `tools/index.json` plus Deno TypeScript files | The model writes named executable capabilities | Cross-session within a workspace | Not native; generated tools can only call LLMs indirectly through ordinary network APIs | Generated TypeScript tools inside a workspace capability API | Live task needs become reusable executable affordances |
| llm-do | Unified namespace of Python tools and `.agent` files | Humans and agents can move components across neural/symbolic implementations | Durable project/runtime call boundary | Possible because agents are callable components; bootstrap patterns are plausible but not extensively tested | Stable callable interface across prompt and code implementations | Components can be refactored between prompt and code without changing callers |

RLM is the cleanest family of symbolic execution without accumulation. In standard RLM, the model writes orchestration code, but the REPL state is only a task-local substrate. That is powerful for bounded-context scheduling, meaning the choice of what each limited LLM call should see and do, because bookkeeping lives in variables and loops rather than in chat history. It also avoids the governance burden of keeping generated artifacts: there is no approval state, lifecycle, or stale code problem for an artifact that disappears after use.

λ-RLM keeps the same RLM persistence boundary while changing the control language. Instead of letting the model synthesize arbitrary Python at each step, it executes a planner-built chain over typed, pre-verified combinators and reserves neural calls for bounded leaves. That means λ-RLM addresses RLM's verifiability and predictability problem without addressing RLM's accumulation problem: the run still does not promote useful orchestration strategies into durable project artifacts. The lesson is that restriction and persistence vary independently. A system can make per-run orchestration safer without making it reusable.

Tendril chooses the next persistence point: externalize now, then keep the useful result as a workspace capability. It keeps the outer tool surface small, but lets the agent register a named executable capability when no existing one fits. That makes Tendril closer to [codification](./definitions/codification.md), committing a recurring behavior into executable code, than to ordinary memory. The learned artifact changes what the next session can execute, not just what information it can retrieve. The cost is that Tendril inherits the lifecycle questions RLM avoids: provenance, approval, tests, retirement, dependency drift, and permission scope.

llm-do addresses a different boundary. Its strongest idea is not that tools are callable, but that LLM-backed agents and symbolic tools share one calling convention. That makes neural-to-symbolic and symbolic-to-neural movement local: a component can be constrained into Python or relaxed back into an agent without changing the caller. Compared with Tendril, llm-do is less about autonomous creation of new tools and more about preserving a stable interface while implementation moves along the verifiability gradient, the spectrum from loose LLM-interpreted artifacts to deterministic, testable code.

Recursion separates the systems further. RLM is recursive by design: standard RLM generated code can call `recursive_llm()` as part of its orchestration, while λ-RLM encodes recursion in a fixed executor over the combinator library. Tendril is self-extending but not recursive in that sense. Its generated Deno tools get `args`, `__workspace`, file access, and network access, but no injected model or child-agent primitive; a tool could call an LLM API over HTTP if given credentials, but that is ordinary network code, not Tendril calling itself. llm-do sits closer to RLM here because agents and tools share the call boundary: an agent can call another agent the same way it calls a tool. In theory, that same convention could support Tendril-like bootstrapping of agents with tools, but that path has not been tested extensively.

The systems are therefore complementary rather than substitutes. RLM is the scratchpad pattern for task-local orchestration; λ-RLM is the restricted-runtime variant of that pattern. Tendril is the deployment-time promotion pattern for reusable generated tools. llm-do is the interface pattern that makes later refactoring across agent-backed and code-backed implementations cheap.

A combined system would likely use RLM-like ephemeral orchestration to explore a task, Tendril-like promotion when an executable pattern recurs, and llm-do-like unified calling so promoted artifacts can later be split, constrained, relaxed, or replaced without caller churn.

## Open Questions

- When should an RLM-style ephemeral program be promoted into a Tendril-style durable capability?
- When should recursive agent calls be allowed inside durable generated tools, rather than kept as ephemeral RLM-style orchestration?
- What approval or testing threshold is enough for online generated tools without destroying the deployment-time learning loop?
- Can Tendril-style generated capabilities live inside an llm-do-style unified namespace without making name selection and lifecycle management too noisy?

---

Relevant Notes:

- [RLM has the model write ephemeral orchestrators over sub-agents](./rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md) — grounds: supplies the ephemeral REPL-orchestrator side of the comparison
- [Ingest: The Y-Combinator for LLMs](../sources/the-y-combinator-for-llms-solving-long-context-rot.ingest.md) — evidence: λ-RLM is an RLM variant that keeps task-local prompt-as-environment recursion while replacing arbitrary REPL code with a typed combinator runtime
- [Unified calling conventions enable bidirectional refactoring between neural and symbolic](./unified-calling-conventions-enable-bidirectional-refactoring.md) — grounds: supplies the llm-do call-boundary side of the comparison
- [Tendril](../agent-memory-systems/reviews/tendril.md) — evidence: source-inspected generated-capability system that occupies the cross-session workspace persistence point
- [Ephemeral computation prevents accumulation](./ephemeral-computation-prevents-accumulation.md) — mechanism: explains the accumulation trade-off that separates RLM from Tendril
- [Deploy-time learning is the missing middle](./deploy-time-learning-is-the-missing-middle.md) — mechanism: explains why Tendril's online capability registration is a durable behavior-change loop
- [The verifiability gradient](./verifiability-gradient.md) — mechanism: situates llm-do's movement between LLM-backed agents and Python functions
- [Agent orchestration occupies a multi-dimensional design space](./agent-orchestration-occupies-a-multi-dimensional-design-space.md) — extends: this note fills in one local comparison across scheduler placement, persistence horizon, and representational form
- [Ingest: Recursive Language Models - what finally gave me the 'aha' moment](../sources/recursive-language-models-what-finally-gave-me-the-aha-moment.ingest.md) — evidence: practitioner walkthrough of RLM's REPL mechanism and symbolic variable return
- [Claude Code dynamic workflows](../agentic-systems/claude-code-dynamic-workflows.md) — evidence: a placement the comparison does not yet cover — model-authored sandboxed guest-language script, session-ephemeral with whole-script promotion to a reusable `/command`
