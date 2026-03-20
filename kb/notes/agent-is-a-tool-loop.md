---
description: A lightweight technical convention — an agent is a tool loop (prompt, capability surface, stop condition) — sidestepping the definitional debate in favor of a unit that organizes code
type: note
traits: []
tags: [computational-model, tool-loop]
status: seedling
---

# "Agent" is a useful technical convention, not a definition

The word "agent" carries too much philosophical weight to define cleanly. But as a technical convention for organizing code, a simple equivalence works: an agent is a tool loop — a prompt, a capability surface, and a stop condition, running until the model finishes or the runtime cuts it off.

The convention is deliberately minimal — it says nothing about autonomy, planning, or goals. It names the unit of execution that a programmer spawns. A sub-agent is a child loop with its own prompt and capability surface. A multi-agent system is a tree of loops coordinated by code. Two loops with different tool surfaces but the same model are different agents; the same prompt run twice is two invocations. The convention tracks code structure, not character.

That simplicity pays off in framework design. If "agent" means "tool loop," then spawning a sub-agent is spawning a sub-loop — and the question of whether frameworks should [expose the loop](./tool-loop-index.md) becomes the question of whether they support sub-agents as a first-class operation.

---

Relevant Notes:

- [tool loop](./tool-loop-index.md) — context: the index whose argument this convention grounds — sub-agents as sub-loops
- [bounded-context orchestration model](./bounded-context-orchestration-model.md) — foundation: each agent is one iteration of the `select/call/absorb` loop
- [subtasks that need different tools force loop exposure in agent frameworks](./subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks.md) — motivates: sub-agents are needed precisely because children need different capability surfaces
