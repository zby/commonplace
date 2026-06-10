---
description: Index for agent-memory notes about memory as a crosscutting concern in agent architecture
type: kb/types/tag-readme.md
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
- [Computational model](./computational-model-README.md) - agent memory is loaded through bounded calls and scheduling decisions
- [Related systems](../agent-memory-systems/README.md) - external implementations and comparisons that expose memory-system design tradeoffs
