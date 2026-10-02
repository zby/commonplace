---
description: "Curated head for the trace-learning tag — external systems that learn from agent traces: raw traces accumulate, then a distillation step produces rules, memories, prompts, or weights; the tag marks system reviews whose analysis found that loop"
type: types/tag-readme.md
---

# Trace-learning

This tag gathers external systems that learn from their own agent traces: memory extraction from sessions, session capture and transcript mining, skill libraries built from past runs, and self-evolving prompts or harnesses. The historical comparison is [trace-learning techniques in related systems](../agent-memory-systems/trace-learning-techniques-in-related-systems.md). The pattern is a two-stage loop: raw traces accumulate as episodes, logs, or transcripts, then a distillation step, automatic or manual, produces something that changes later behavior: a memory entry, a rule, a prompt, a route, or a fine-tune. The tag marks analyses whose evidence identifies a trace-fed write path and a distillation mechanism. Current analyses live in [agentic-systems](../agentic-systems/README.md); reviews in [agent-memory-systems](../agent-memory-systems/README.md) retain the historical evidence and assignment contract. Nearby but different: [agent-memory](./agent-memory-README.md) covers memory architecture whether or not traces feed it. This head is selective. Tag membership spans the participating collections declared in `kb/tags/COLLECTION.md`, including current analyses and historical reviews.

## Start here

- [Trace-learning techniques in related systems](../agent-memory-systems/trace-learning-techniques-in-related-systems.md) — historical comparison across the tagged systems on ingestion pattern, representational form, behavioral authority, artifact structure, and evidence tier
- [agent-memory-system-review type](../agent-memory-systems/types/agent-memory-system-review.md) — historical Write side rule and raw-to-distilled section contract

## Representative systems

- [HyperAgents](../agent-memory-systems/reviews/hyperagents.md) — benchmark feedback promotes executable changes to the harness itself
- [auto-harness](../agent-memory-systems/reviews/auto-harness.md) — a benchmark-driven loop mines training traces and evolves the agent program
- [Dynamic Cheatsheet](../agent-memory-systems/reviews/dynamic-cheatsheet.md) — test-time prompt memory curated by the model from its own solutions
- [REM](../agent-memory-systems/reviews/REM.md) — episodic memory service built from trace-learning episodes with vector and graph retrieval
- [Synapptic](../agent-memory-systems/reviews/synapptic.md) — mines transcripts into weighted user profiles
- [memwiki](../agent-memory-systems/reviews/memwiki.md) — agent-maintained trace notes in a hot-cache wiki

## Related Tags

- [agent-memory](./agent-memory-README.md) — the memory architecture the distilled stage lands in
- [self-improving-systems](./self-improving-systems-README.md) — the theory of systems that change their own organization; trace-learning systems are its largest external casebook
- [deploy-time-learning](./deploy-time-learning-README.md) — the post-release change these loops are built to absorb
