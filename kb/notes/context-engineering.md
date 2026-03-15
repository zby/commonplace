---
description: Definition — context engineering is the architecture and machinery for getting the right knowledge into a bounded context at the right time — routing, loading, scoping, and maintenance; distillation is its main operation but not the only one
type: note
traits: []
tags: [computational-model]
status: seedling
---

# Context engineering

The architecture and machinery for getting the right knowledge into a bounded context at the right time. [Distillation](./distillation.md) — compressing knowledge for a specific task under a context budget — is the main operation, but not the only one. Routing (what not to load), scoping (what each consumer sees), and maintenance (pruning accumulated debris) are also context engineering operations. Context engineering is the system that orchestrates all of these.

Anthropic defines it as "strategies for curating and maintaining the optimal set of tokens during LLM inference" ([Anthropic, 2025](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)). This KB's treatment is consistent but more structural — context engineering decomposes into components:

**Routing** — deciding what knowledge is relevant before loading it. The [instruction-specificity/loading-frequency match](./instruction-specificity-should-match-loading-frequency.md) (always-loaded → on-reference → on-invoke → on-demand) is routing. [CLAUDE.md as a router](./agents-md-should-be-organized-as-a-control-plane.md) is routing. [Retrieval-oriented descriptions](./agents-navigate-by-deciding-what-to-read-next.md) that let agents decide "don't follow this" without loading the target are routing.

**Loading** — assembling the prompt from selected knowledge. The `select` function in the [bounded-context orchestration model](./bounded-context-orchestration-model.md) formalizes this: given state `K` and budget `M`, build prompt `P` with `|P| ≤ M`. Loading includes both what to include and how to frame it — the same knowledge under different framing has different [extractable value](./information-value-is-observer-relative.md).

**Scoping** — isolating what each consumer sees. [Sub-agents as lexically scoped frames](./llm-context-is-composed-without-scoping.md) is scoping. The flat context has no scoping; architecture must impose it.

**Maintenance** — keeping loaded context healthy over time. Compaction, observation masking, and the [workshop layer's](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) holistic-rewrite discipline are maintenance. Without maintenance, context accumulates debris that [degrades reasoning](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) even when token counts are low.

The [bounded-context orchestration model](./bounded-context-orchestration-model.md) is the formal treatment of this machinery — the `solve` loop where the symbolic scheduler drives routing, loading, and scoping decisions for each bounded LLM call.

---

Relevant Notes:

- [distillation](./distillation.md) — the main operation context engineering performs: compressing knowledge for a task under a budget
- [context efficiency is the central design concern](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — motivation: why context engineering matters (context is the scarce resource)
- [bounded-context orchestration model](./bounded-context-orchestration-model.md) — formalisation: the select/call loop that structures context engineering decisions
- [instruction specificity should match loading frequency](./instruction-specificity-should-match-loading-frequency.md) — mechanism: the routing hierarchy (always-loaded → on-demand)
- [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — mechanism: sub-agents as the scoping component
- [agents navigate by deciding what to read next](./agents-navigate-by-deciding-what-to-read-next.md) — mechanism: routing through retrieval-oriented descriptions
- [legal drafting solves the same problem as context engineering](./legal-drafting-solves-the-same-problem-as-context-engineering.md) — parallel: law's centuries of methodology for the same problem
- [in-context learning presupposes context engineering](./in-context-learning-presupposes-context-engineering.md) — extends: in-context learning only works when context engineering has selected the right knowledge; this makes context engineering a prerequisite, not just an optimization
- [agent runtimes decompose into scheduler context engine and execution substrate](./agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md) — component view: names context engineering as the runtime's context-engine layer
