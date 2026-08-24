---
description: "RLM variants, Tendril, and llm-do show that control-language restriction and artifact persistence are separate questions, including where cited RLM sources leave post-return lifecycle unspecified"
type: kb/types/note.md
traits: [title-as-claim, has-comparison, has-external-sources]
tags: [computational-model, learning-theory, artifact-analysis]
---

# RLM, λ-RLM, Tendril, and llm-do separate restriction from persistence

Recursive Language Models (RLM), Tendril, a workspace agent sandbox for generated capabilities, and llm-do, a hybrid agent/tool runtime, all move work out of raw conversation and onto a symbolic substrate. The useful distinction is not "agent versus tool" or even "LLM versus code"; it is where symbolic work is allowed to persist after the model has helped create or select it, and how tightly the symbolic control language is restricted.

Here, a persistence boundary means the point at which generated or selected work stops being temporary and becomes reusable by later calls, sessions, or project code.

Restriction and persistence are separate axes. Standard RLM and λ-RLM both use a prompt-as-environment REPL within an execution. They differ inside that execution: standard RLM lets the model write arbitrary REPL code, while λ-RLM uses a deterministic planner to instantiate a recursive program from a pre-verified typed combinator library. Neither cited source specifies what happens to REPL state after the response returns, so their post-return persistence cannot be classified from these sources.

| System | Symbolic substrate | Who authors/selects the symbolic work | Persistence boundary | Recursive LLM calls | Control-language restriction | Main affordance |
|---|---|---|---|---|---|---|
| RLM | Python REPL namespace plus a scaffold-supplied recursive sub-call | The model writes orchestration code | Variables persist across REPL calls within the described execution; post-return lifecycle is unspecified | Built in through recursive sub-agent invocation | Arbitrary model-authored REPL code | External bookkeeping in variables, with sub-agent results kept outside the parent context |
| λ-RLM | REPL environment plus typed combinator runtime (`SPLIT`, `MAP`, `FILTER`, `REDUCE`) | The model selects a task type from a fixed menu; a deterministic planner builds a chain from pre-verified combinators | The finite pipeline initializes REPL state and returns a response; post-return lifecycle is unspecified | Built into a fixed recursive executor; neural work is bounded to task selection, leaf calls, and specified synthesis | Restricted typed combinator vocabulary | Prompt-as-environment recursion with auditable control flow and formal bounds |
| Tendril | Workspace `tools/index.json` plus Deno TypeScript files | The model writes named executable capabilities | Cross-session within a workspace | Not native; generated tools can only call LLMs indirectly through ordinary network APIs | Generated TypeScript tools inside a workspace capability API | Live task needs become reusable executable affordances |
| llm-do | Unified namespace of Python tools and `.agent` files | Humans and agents can move components across neural/symbolic implementations | Durable project/runtime call boundary | Possible because agents are callable components; bootstrap patterns are plausible but not extensively tested | Stable callable interface across prompt and code implementations | Components can be refactored between prompt and code without changing callers |

The cited RLM walkthrough establishes symbolic execution within a run, not absence of accumulation across runs. The model writes prompt transformations in a REPL, recursively invokes sub-agents whose responses remain symbolic variables outside the parent context, and can return a constructed Python variable. Variables persist across REPL execution calls. That is powerful for bounded-context scheduling, meaning the choice of what each limited LLM call should see and do, because bookkeeping can live in variables and loops rather than in chat history. But the source does not say what happens after the answer returns. The earlier classification of generated orchestrators as discarded per task therefore needs a separate implementation or lifecycle source; governance consequences cannot be inferred from this walkthrough alone.

λ-RLM keeps the prompt-as-environment REPL while changing the control language. Instead of letting the model synthesize arbitrary Python at each step, a deterministic planner instantiates a fixed recursive chain over typed, pre-verified combinators. Neural inference is bounded and localized to task-type selection, leaf work, and explicitly specified synthesis steps. This directly addresses analyzability and predictable execution. It does not settle accumulation: the paper describes REPL initialization, planning, one-shot execution, and response return but says nothing about state disposal, reuse, or artifact promotion afterward. The lesson is that restriction can be assessed without pretending the same evidence settles persistence.

Tendril chooses the next persistence point: externalize now, then keep the useful result as a workspace capability. It keeps the outer tool surface small, but lets the agent register a named executable capability when no existing one fits. That makes Tendril closer to [codification](./definitions/codification.md), committing a recurring behavior into executable code, than to ordinary memory. The learned artifact changes what the next session can execute, not just what information it can retrieve. The cost is that Tendril inherits the lifecycle questions RLM avoids: provenance, approval, tests, retirement, dependency drift, and permission scope.

llm-do addresses a different boundary. Its strongest idea is not that tools are callable, but that LLM-backed agents and symbolic tools share one calling convention. That makes neural-to-symbolic and symbolic-to-neural movement local: a component can be constrained into Python or relaxed back into an agent without changing the caller. Compared with Tendril, llm-do is less about autonomous creation of new tools and more about preserving a stable interface while implementation moves along the verifiability gradient, the spectrum from loose LLM-interpreted artifacts to deterministic, testable code.

Recursion separates the systems further. RLM is recursive by design: model-authored REPL code can invoke sub-agents through a scaffold-supplied recursive sub-call, while λ-RLM encodes recursion in a fixed executor over the combinator library. Tendril is self-extending but not recursive in that sense. Its generated Deno tools get `args`, `__workspace`, file access, and network access, but no injected model or child-agent primitive; a tool could call an LLM API over HTTP if given credentials, but that is ordinary network code, not Tendril calling itself. llm-do sits closer to RLM here because agents and tools share the call boundary: an agent can call another agent the same way it calls a tool. In theory, that same convention could support Tendril-like bootstrapping of agents with tools, but that path has not been tested extensively.

The systems are therefore complementary rather than substitutes. RLM is the model-authored REPL pattern for within-execution orchestration; λ-RLM is the restricted-runtime variant of that pattern. Their cited sources leave post-return lifecycle open. Tendril is the deployment-time promotion pattern for reusable generated tools. llm-do is the interface pattern that makes later refactoring across agent-backed and code-backed implementations cheap.

A combined system would likely use RLM-like within-execution orchestration to explore a task, Tendril-like promotion when an executable pattern recurs, and llm-do-like unified calling so promoted artifacts can later be split, constrained, relaxed, or replaced without caller churn. Calling the first stage ephemeral requires an implementation-specific lifecycle fact beyond the two RLM sources grounded here.

## Open Questions

- When an RLM implementation discards its generated program after a run, when should that program instead be promoted into a Tendril-style durable capability?
- When should recursive agent calls be allowed inside durable generated tools, rather than kept as ephemeral RLM-style orchestration?
- What approval or testing threshold is enough for online generated tools without destroying the deployment-time learning loop?
- Can Tendril-style generated capabilities live inside an llm-do-style unified namespace without making name selection and lifecycle management too noisy?

---

Relevant Notes:

- [RLM has the model write ephemeral orchestrators over sub-agents](./rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md) — supplies the model-authored REPL-orchestrator side of the comparison; its discard claim still needs an implementation-specific lifecycle source
- [Ingest: The Y-Combinator for LLMs](../sources/the-y-combinator-for-llms-solving-long-context-rot.ingest.md) — evidenced-by: λ-RLM keeps prompt-as-environment recursion while replacing open-ended model-authored code with a deterministic, typed combinator runtime; post-return persistence is unspecified
- [Unified calling conventions enable bidirectional refactoring between neural and symbolic](./unified-calling-conventions-enable-bidirectional-refactoring.md) — grounds: supplies the llm-do call-boundary side of the comparison
- [Tendril](../agent-memory-systems/reviews/tendril.md) — evidenced-by: source-inspected generated-capability system that occupies the cross-session workspace persistence point
- [Ephemeral computation prevents accumulation](./ephemeral-computation-prevents-accumulation.md) — mechanism: explains the accumulation trade-off for an RLM implementation that actually discards generated programs
- [Retained system-definition artifacts enable persistent deployment-time adaptation](./retained-artifacts-enable-persistent-deployment-time-adaptation.md) — mechanism: explains why Tendril's online capability registration is a durable behavior-change loop
- [The verifiability gradient](./verifiability-gradient.md) — mechanism: situates llm-do's movement between LLM-backed agents and Python functions
- [Agent orchestration occupies a multi-dimensional design space](./agent-orchestration-occupies-a-multi-dimensional-design-space.md) — extends: this note fills in one local comparison across scheduler placement, persistence horizon, and representational form
- [Ingest: Recursive Language Models - what finally gave me the 'aha' moment](../sources/recursive-language-models-what-finally-gave-me-the-aha-moment.ingest.md) — evidenced-by: practitioner walkthrough of RLM's REPL mechanism, within-execution variable persistence, recursive sub-agent invocation, and symbolic variable return; post-return lifecycle and the exact sub-call API are unspecified
- [Claude Code dynamic workflows](../agentic-systems/claude-code-dynamic-workflows.md) — evidenced-by: a placement the comparison does not yet cover — model-authored sandboxed guest-language script, session-ephemeral with whole-script promotion to a reusable `/command`
