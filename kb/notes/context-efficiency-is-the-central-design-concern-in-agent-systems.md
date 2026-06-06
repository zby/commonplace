---
description: Context is the single scarce resource in agent systems, and it is scarce for two distinct reasons — per-window degradation (feasibility) and aggregate token economics (cost) — of which feasibility is the binding one
type: kb/types/note.md
traits: [has-external-sources, title-as-claim]
tags: [computational-model, foundations]
status: current
---

# Context efficiency is the central design concern in agent systems

In traditional systems, the scarce resources are compute, memory, storage, and bandwidth; algorithmic complexity is the dominant cost model. In agent systems, the scarce resource is context — the finite window of tokens the agent can attend to. Context differs from these in being undifferentiated: a CPU tiers registers, cache, RAM, disk, and network, whereas an LLM has one context window in which instructions, task, knowledge, and reasoning all compete for the same space.

Context is scarce for two distinct reasons, and they are different *kinds* of cost:

- **Feasibility — the per-window face.** Within a single inference call the model's competence degrades as the window fills, by [soft degradation rather than a hard token limit](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md). This is a *capability* ceiling: past it the task becomes impossible or degrades past usefulness, at any price. It is the lowest-degree-of-freedom face — the attention budget is unitary within a call, cannot be tiered at the attention level, and cannot be enlarged without architectural change. This face also carries to the decomposed case: [under sub-agent decomposition, feasibility is the heaviest fork's net load](./feasibility-is-the-heaviest-forks-net-load.md).
- **Cost — the aggregate face.** Every token processed costs money and latency, summed across all calls. This is an *economic* penalty — continuous rather than binary. Here context behaves like an ordinary resource: you can tier it, batch it, cache it, or simply spend more.

These rank: **feasibility binds first.** You can buy more tokens; you cannot buy a bigger usable window. A feasibility violation is a hard constraint — the work cannot be done — whereas a cost overrun is a soft penalty on work that can. So "context efficiency is the central design concern" is at root a claim about the binding feasibility face; aggregate cost is real but secondary. Treating the binding face first is an application of [solve low-degree-of-freedom subproblems first to avoid blocking better designs](./solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md) — optimize the tightest constraint before others, or later choices are forced into low-quality tradeoffs.

Anthropic's engineering team has converged on the same framing, defining **context engineering** as "strategies for curating and maintaining the optimal set of tokens during LLM inference" and describing context as "a critical but finite resource" with an **attention budget** that "every token depletes" ([Anthropic, 2025](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)). Independent practitioner evidence comes from OpenAI's Codex team: shipping 1M lines of agent-generated code required a 100-line AGENTS.md acting as a router with pointers to deeper docs — "a map, not a manual." The bottleneck was not model capability but the structure of the environment, of which context structure is a central component ([Lopopolo, 2026](https://openai.com/index/harness-engineering/)). Raschka reaches the same conclusion from coding-agent components: apparent model quality is largely context quality ([Raschka, 2026](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent)).

If context is the fundamental scarce resource, the natural computational model is [symbolic scheduling over bounded LLM calls](./bounded-context-orchestration-model.md): exact bookkeeping lives in code, while bounded context is reserved for semantic judgment. Whatever the model, context efficiency should be evaluated at design time, not retrofitted — where sub-agent boundaries go, what loads when, and what gets frontloaded determine it structurally.

---

Sources:
- Anthropic (2025). [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
- Lopopolo (2026). [Harness engineering: leveraging Codex in an agent-first world](https://openai.com/index/harness-engineering/) — independent practitioner convergence on context-as-scarce-resource from a 1M LOC agent-generated codebase.
- Raschka (2026). [Components of A Coding Agent](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent) — independent practitioner convergence: "a lot of apparent 'model quality' is really context quality."

Relevant Notes:

- [solve low-degree-of-freedom subproblems first to avoid blocking better designs](./solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md) — application: this note treats the feasibility face as the lowest-degree-of-freedom resource and derives the ranking from that constraint
- [agent context is constrained by soft degradation, not hard token limits](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) — grounds: establishes the binding-constraint premise behind the feasibility face
- [Under sub-agent decomposition, feasibility is the heaviest fork's net load](./feasibility-is-the-heaviest-forks-net-load.md) — extends: carries the feasibility face to the decomposed case — per-agent ceiling, heaviest fork, net load
- [symbolic scheduling over bounded LLM calls](./bounded-context-orchestration-model.md) — extends: the computational model that follows if context is the only fundamental scarce resource
- [Minimum Viable Ontology / Domain Maps](https://x.com/melodyskim/status/2029332670115614799) — exemplifies: MVO is distillation under context-efficiency pressure — compress domain knowledge into the smallest vocabulary that fits the context window
- [Harness Engineering (Lopopolo, 2026)](https://openai.com/index/harness-engineering/) — exemplifies: "give Codex a map, not a 1,000-page instruction manual" is independent practitioner convergence on context scarcity as the binding constraint
- [Harness Engineering as Cybernetics (@odysseus0z, 2026)](https://x.com/odysseus0z/status/2030416758138634583) — grounds: frames context-efficient agent runtime design as feedback-loop calibration from control theory
- [The Anatomy of an Agent Harness (Vtrivedy10, 2026)](https://x.com/Vtrivedy10/status/2031408954517971368) — exemplifies: derives runtime components by working backwards from model limitations, instantiating the architectural responses concretely
- [Components of A Coding Agent (Raschka, 2026)](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent) — grounds: independent practitioner convergence — "apparent model quality is really context quality"
