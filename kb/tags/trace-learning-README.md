---
description: "Curated head for the trace-learning tag — external systems that learn from agent traces: raw traces accumulate, then a distillation step produces rules, memories, prompts, or weights; the tag marks system reviews whose analysis found that loop"
type: types/tag-readme.md
---

# Trace-learning

This tag gathers external systems that learn from their own agent traces: memory extraction from sessions, session capture and transcript mining, skill libraries built from past runs, and self-evolving prompts or harnesses. The historical comparison is [trace-learning techniques in related systems](../agent-memory-systems/trace-learning-techniques-in-related-systems.md). The pattern is a two-stage loop: raw traces accumulate as episodes, logs, or transcripts, then a distillation step, automatic or manual, produces something that changes later behavior: a memory entry, a rule, a prompt, a route, or a fine-tune. The tag marks analyses whose evidence identifies a trace-fed write path and a distillation mechanism. Current analyses live in [agentic-systems](../agentic-systems/README.md); reviews in [agent-memory-systems](../agent-memory-systems/README.md) retain the historical evidence and assignment contract. Nearby but different: [agent-memory](./agent-memory-README.md) covers memory architecture whether or not traces feed it. This head is selective. The generated list groups current analyses and historical reviews by collection.

## Start here

- [Trace-learning techniques in related systems](../agent-memory-systems/trace-learning-techniques-in-related-systems.md) — historical comparison across the tagged systems on ingestion pattern, representational form, behavioral authority, artifact structure, and evidence tier
- [agent-memory-system-review type](../agent-memory-systems/types/agent-memory-system-review.md) — historical Write side rule and raw-to-distilled section contract

## Representative systems

- [HyperAgents](../agentic-system-analyses/retained/facebookresearch--hyperagents/runtime.md#rt-rte-parent-selection) — scores help select a parent for the next executable revision; they do not decide whether a generation enters the archive
- [auto-harness](../agentic-system-analyses/retained/neosigmaai--auto-harness/memory.md) — a coding agent gets diagnostic traces to guide program revisions; the analysis distinguishes requested edits from demonstrated improvements
- [Dynamic Cheatsheet](../agentic-system-analyses/retained/suzgunmirac--dynamic-cheatsheet/memory.md) — the model curates a reference sheet from previous solutions; the caller supplies it on later queries
- [REM](../agentic-system-analyses/retained/satyammistari--rem/memory.md) — vectors and temporal links select stored episodes; extracting a candidate fact does not mean it was saved
- [Synapptic](../agentic-system-analyses/retained/appcuarium--synapptic/memory.md) — high-weight observations from earlier transcripts enter the prompt that extracts new observations
- [memwiki](../agentic-system-analyses/retained/hereisswapnil--memwiki/memory.md) — the agent maintains Markdown and is instructed to read the hot cache before opening domain pages

## Related Tags

- [agent-memory](./agent-memory-README.md) — the memory architecture the distilled stage lands in
- [self-improving-systems](./self-improving-systems-README.md) — the theory of systems that change their own organization; trace-learning systems are its largest external casebook
- [continual-learning](./continual-learning-README.md) — the post-release change these loops are built to absorb
