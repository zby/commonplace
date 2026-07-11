---
description: "Design heuristic for agent-consumed systems: treat agents like competent first-time humans except where linear context loading makes access costs diverge."
type: kb/types/note.md
traits: [title-as-claim, has-comparison]
tags: [document-system, context-engineering]
---

# Design for the first-time human, except on access cost

A useful default when designing any system an LLM agent consumes is to treat the agent as a competent human using the system for the first time. Most of what makes a system good for a newcomer — clear naming, discoverable organization, orientation cues, honest labels, readable prose — serves the agent equally well, and human ergonomics are easier to reason about than agent behaviour. So the newcomer human is a cheap, reliable proxy for the agent: a default, not a law, holding where the two consumers share a profile and breaking where their profiles diverge.

The sharpest divergence, and the one with a clean fix, is **access cost**. A competent human reads a large artifact *sublinearly* — skim the headings, scroll to the region, Ctrl-F to the few lines that matter — so a large but well-organized artifact stays cheap. An agent reading that same artifact pays *linearly*: every byte enters [bounded context](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) whether it is relevant or not, and the irrelevant bulk adds interference, not just volume. So an artifact that is cheap for a newcomer human can be context debt for the agent, and you cannot read the agent's cost off human ergonomics.

The real divider is access *mode*, not human versus agent: sublinear, paying only for the slice you consult, versus linear, paying for every byte. Humans default to sublinear because their tooling makes it the path of least resistance; agents default to linear because the cheapest primitive is "read the whole thing into context." But that pairing is not fixed — an agent given a query or search interface reads sublinearly, and a human handed an unstructured blob reads linearly.

So the fix is not to pick a winner between the consumers. Give each a **materialization** with sublinear access over the slice it needs, behind a single source of truth: a human gets a rendered, browsable view with find-in-page; an agent gets a scoped query or search path. A large reference index, for instance, need not sit on the agent's default read path to earn its keep — it can be materialized for the human and reached by the agent through a query instead, routed to the consumer whose access mode makes it cheap, not deleted.

Access cost is not the only place the proxy breaks: agents also treat read text as possible instruction where a human treats it as inert, and confabulate where a human would ask. This note isolates access cost because it has a clean structural fix — not because it is the most frequent exception.

---

Relevant Notes:

- [context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: the agent's linear access cost is a context-window cost, and context is the binding scarce resource that makes the access-mode exception matter
- [two context boundaries govern collection operations](./two-context-boundaries-govern-collection-operations.md) — extends: the full-text vs index boundary is the same linear-load distinction applied to whole collections; this note generalizes it to a design heuristic and adds the per-consumer materialization fix
- [Under sub-agent decomposition, feasibility is the heaviest fork's net load](./feasibility-is-the-heaviest-forks-net-load.md) — mechanism: materializing a sublinear access path for the agent is a net-load lever — the fork loads the queried slice instead of the whole artifact
- [human-LLM differences are load-bearing for knowledge system design](./human-llm-differences-are-load-bearing-for-knowledge-system-design.md) — extends: that note lists human-vs-agent need-differences as a table; this note sharpens its navigation row into a single divider — access mode — and adds the per-consumer materialization fix
- [agents navigate by deciding what to read next](./agents-navigate-by-deciding-what-to-read-next.md) — mechanism: a bare pointer forces loading the whole target to judge relevance, which is why an agent's default read is linear and why a query/search materialization saves context
- [LLM context is a homoiconic medium](./llm-context-is-a-homoiconic-medium.md) — grounds: the closing text-as-instruction exception rests on there being no program/data boundary in the window, so any loaded text can act as instruction
- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — grounds: the closing confabulation exception is the underspecification case, where a human would ask for clarification but an agent may choose one interpretation and proceed
