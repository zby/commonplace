---
description: Index for agent-memory notes about memory as a crosscutting concern in agent architecture
type: kb/types/index.md
index_source: tag
index_key: agent-memory
status: current
---

# Agent memory

Agent memory notes treat memory as part of agent architecture, not just storage. Use this index for claims about what memory must do for agents, how it interacts with context engineering, and where memory-system comparisons reveal broader KB design constraints.

## Notes

- [Designing a Memory System for LLM-Based Agents](./designing-agent-memory-systems.md) - starting point: frames the design pressures around agent memory as context engineering, retrieval, and learning problems rather than a single database choice

## Related Tags

- [Learning theory](./learning-theory-index.md) - memory only matters when retained artifacts change future behavior
- [Computational model](./computational-model-index.md) - agent memory is loaded through bounded calls and scheduling decisions
- [Related systems](../agent-memory-systems/README.md) - external implementations and comparisons that expose memory-system design tradeoffs

## Other tagged notes <!-- generated -->

- [Agent memory needs discoverable, composable, trusted knowledge under bounded context](./agent-memory-needs-discoverable-composable-trusted-knowledge-under-bounded-context.md) - Frames discoverable, composable, trusted remembered knowledge as the minimal artifact-quality basis for agent memory under bounded context.
- [Raw accumulation does not create usable memory](./raw-accumulation-does-not-create-usable-memory.md) - Accumulation preserves material, but usable agent memory requires ingress work that adds handles, scope, relationships, provenance, trust signals, and lifecycle pressure.
