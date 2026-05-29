---
description: Auto-generated directory - run commonplace-refresh-indexes to rebuild
type: kb/types/index.md
index_source: directory
---

# Tool Loop Control Directory

← [Parent](../dir-index.md)

- [LLM frameworks should keep the tool loop optional](./llm-frameworks-should-keep-the-tool-loop-optional.md) *(note)* - Framework-owned tool loops package the common model/tool/retry pattern well, but strong frameworks keep the loop optional so applications can control state projection, branching, and re-entry
- [Orchestration strategies and run-state have opposite persistence economics](./orchestration-strategies-and-run-state-have-opposite-persistence.md) *(note)* - Inside a host-language scheduler, run-state K is task-specific so it has near-zero cross-task reuse value and should stay ephemeral, while select-strategies recur and are expensive to rediscover so they are the high-value promotion target — RLM discards both, losing the valuable half
- [The practical scheduler is the host language, not a reified select](./the-practical-scheduler-is-the-host-language.md) *(note)* - The simplest practical orchestration library demotes the tool loop to a returning, per-call-parameterized function and lets ordinary host-language code play select and K — reifying K only when the run must outlive its process or outgrow its memory
