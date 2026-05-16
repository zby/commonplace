---
description: Auto-generated directory - run commonplace-refresh-indexes to rebuild
type: kb/types/index.md
index_source: directory
---

# Tool Loop Control Directory

← [Parent](../dir-index.md)

- [A framework-owned tool loop can simulate explicit orchestration by externalizing control state](./a-framework-owned-tool-loop-can-simulate-explicit-orchestration-by.md) *(note)* - Shows how a framework-owned tool loop can recover branching, recursive decomposition, and state projection by moving the control stack into a singleton runtime/tool instead of application code
- [Anatomy of an LLM application](./anatomy-of-an-llm-application.md) *(note)* - Starts from the standard prompted-agent tool loop, showing that the real control boundary appears when applications need to change the capability surface for later steps
- [LLM frameworks should keep the tool loop optional](./llm-frameworks-should-keep-the-tool-loop-optional.md) *(note)* - Framework-owned tool loops package the common model/tool/retry pattern well, but strong frameworks keep the loop optional so applications can control state projection, branching, and re-entry
