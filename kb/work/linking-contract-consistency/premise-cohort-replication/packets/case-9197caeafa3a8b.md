# Case packet

Neutral case identifier: case-9197caeafa3a8b

The possible directed relationship from Artifact A to Artifact B is under review.

## Artifact A

# Design for the first-time human, except on access cost

A useful default when designing any system an LLM agent consumes is to treat the agent as a competent human using the system for the first time. Most of what makes a system good for a newcomer — clear naming, discoverable organization, orientation cues, honest labels, readable prose — serves the agent equally well, and human ergonomics are easier to reason about than agent behaviour. So the newcomer human is a cheap, reliable proxy for the agent: a default, not a law, holding where the two consumers share a profile and breaking where their profiles diverge.

The sharpest divergence, and the one with a clean fix, is **access cost**. A competent human reads a large artifact *sublinearly* — skim the headings, scroll to the region, Ctrl-F to the few lines that matter — so a large but well-organized artifact stays cheap. An agent reading that same artifact pays *linearly*: every byte enters [bounded context] whether it is relevant or not, and the irrelevant bulk adds interference, not just volume. So an artifact that is cheap for a newcomer human can be context debt for the agent, and you cannot read the agent's cost off human ergonomics.

The real divider is access *mode*, not human versus agent: sublinear, paying only for the slice you consult, versus linear, paying for every byte. Humans default to sublinear because their tooling makes it the path of least resistance; agents default to linear because the cheapest primitive is "read the whole thing into context." But that pairing is not fixed — an agent given a query or search interface reads sublinearly, and a human handed an unstructured blob reads linearly.

So the fix is not to pick a winner between the consumers. Give each a **materialization** with sublinear access over the slice it needs, behind a single source of truth: a human gets a rendered, browsable view with find-in-page; an agent gets a scoped query or search path. A large reference index, for instance, need not sit on the agent's default read path to earn its keep — it can be materialized for the human and reached by the agent through a query instead, routed to the consumer whose access mode makes it cheap, not deleted.

Access cost is not the only place the proxy breaks: agents also treat read text as possible instruction where a human treats it as inert, and confabulate where a human would ask. This note isolates access cost because it has a clean structural fix — not because it is the most frequent exception.

---

Relevant Notes:

## Artifact B

# Context efficiency is the central design concern in agent systems

In traditional systems, the scarce resources are compute, memory, storage, and bandwidth; algorithmic complexity is the dominant cost model. In agent systems, the scarce resource is context — the finite window of tokens the agent can attend to. Context differs from these in being undifferentiated: a CPU tiers registers, cache, RAM, disk, and network, whereas an LLM has one context window in which instructions, task, knowledge, and reasoning all compete for the same space.

Context is scarce for two distinct reasons, and they are different *kinds* of cost:

- **Feasibility — the per-window face.** Within a single inference call the model's competence degrades as the window fills, by [soft degradation rather than a hard token limit]. This is a *capability* ceiling: past it the task becomes impossible or degrades past usefulness, at any price. It is the lowest-degree-of-freedom face — the attention budget is unitary within a call, cannot be tiered at the attention level, and cannot be enlarged without architectural change. This face also carries to the decomposed case: [under sub-agent decomposition, feasibility is the heaviest fork's net load].
- **Cost — the aggregate face.** Every token processed costs money and latency, summed across all calls. This is an *economic* penalty — continuous rather than binary. Here context behaves like an ordinary resource: you can tier it, batch it, cache it, or simply spend more.

These rank: **feasibility binds first.** You can buy more tokens; you cannot buy a bigger usable window. A feasibility violation is a hard constraint — the work cannot be done — whereas a cost overrun is a soft penalty on work that can. So "context efficiency is the central design concern" is at root a claim about the binding feasibility face; aggregate cost is real but secondary. Treating the binding face first is an application of [solve low-degree-of-freedom subproblems first to avoid blocking better designs] — optimize the tightest constraint before others, or later choices are forced into low-quality tradeoffs.

Anthropic's engineering team has converged on the same framing, defining **context engineering** as "strategies for curating and maintaining the optimal set of tokens during LLM inference" and describing context as "a critical but finite resource" with an **attention budget** that "every token depletes" ([Anthropic, 2025]). Independent practitioner evidence comes from OpenAI's Codex team: shipping 1M lines of agent-generated code required a 100-line AGENTS.md acting as a router with pointers to deeper docs — "a map, not a manual." The bottleneck was not model capability but the structure of the environment, of which context structure is a central component ([Lopopolo, 2026]). Raschka reaches the same conclusion from coding-agent components: apparent model quality is largely context quality ([Raschka, 2026]).

If context is the fundamental scarce resource, the natural computational model is [symbolic scheduling over bounded LLM calls]: exact bookkeeping lives in code, while bounded context is reserved for semantic judgment. Whatever the model, context efficiency should be evaluated at design time, not retrofitted — where sub-agent boundaries go, what loads when, and what gets frontloaded determine it structurally.

---

Sources:
- Anthropic (2025). [Effective context engineering for AI agents].
- Lopopolo (2026). [Harness engineering: leveraging Codex in an agent-first world] — independent practitioner convergence on context-as-scarce-resource from a 1M LOC agent-generated codebase.
- Raschka (2026). [Components of A Coding Agent] — independent practitioner convergence: "a lot of apparent 'model quality' is really context quality."

Relevant Notes:

## Under-review context phrase

the agent's linear access cost is a context-window cost, and context is the binding scarce resource that makes the access-mode exception matter
