---
description: Multi-agent memory harness that combines state-graph traces, task-neighborhood retrieval, and scored text insights for prompt-time reuse across fixed agent workflows
type: note
tags: [related-systems]
status: current
last-checked: 2026-03-22
---

# G-Memory is a mixed-substrate multi-agent memory harness

G-Memory is a research codebase for adding cross-task memory to fixed multi-agent workflows. The repo wraps three benchmarked MAS orchestration styles (`autogen`, `dylan`, `macnet`) with a shared memory module that stores completed task traces, retrieves related prior tasks and reusable text rules, and reinjects both into agent prompts on the next task. The implementation is the official code release for the paper "G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems."

**Repository:** https://github.com/bingreeky/GMemory

## Core Ideas

**Multi-agent episodes are captured as state-local message graphs.** Inside a single task, `MASMessage` stores a `StateChain`, where each state is a `networkx.DiGraph` of agent messages plus upstream edges between agents. `add_agent_node(...)` records who said what and which upstream nodes it depended on; `move_memory_state(...)` closes that step with the chosen action, environment observation, and reward. This gives G-Memory something many single-agent memory systems lack: an explicit record of within-step coordination structure, not just a flat dialogue log.

**Cross-task retrieval is vector search amplified by a task graph.** Completed tasks are stored in Chroma keyed by `task_main`, with labels for success or failure. Separately, `TaskLayer` builds an undirected graph whose nodes are task strings and whose edges come from embedding similarity above a threshold. At query time, G-Memory first finds similar tasks in Chroma, then expands through the graph by `k` hops, then falls back to direct similarity search if the neighborhood is too sparse. The graph is not replacing vector retrieval; it is a neighborhood amplifier over it. The code also attempts an LLM relevance rerank of successful trajectories, but the current implementation overwrites the sorted result with the original slice before returning it.

**The top layer is maintained text rules, not another graph.** `InsightsManager` persists `insights.json` as a list of rules with scores plus positive and negative task associations. Every completed task gets LLM-produced key-step extraction, but the fuller insight-maintenance loop only starts after the memory crosses configured thresholds. At that point, the code compares successful and failed trajectories, proposes `ADD`/`EDIT`/`REMOVE`/`AGREE` operations, updates rule scores, and periodically clusters task nodes with FINCH before asking the LLM to merge related rules. This is the real long-term memory artifact in the repo: scored natural-language guidance tied loosely to task clusters.

**The claimed hierarchy is mixed media, not one unified graph substrate.** The repo and README describe a three-tier graph architecture: interaction graph, query graph, insight graph. In code, only the interaction layer and task layer are actual NetworkX graphs. The insight layer is a JSON rule list, and the primary episode store is Chroma. That does not make the design fake, but it does matter for interpretation: the implemented mechanism is a hybrid memory stack, not a single graph-native knowledge system.

**Prompt-time use is the real integration point.** In `autogen.py`, `dylan.py`, and `graph_mas.py`, each new task begins by retrieving successful trajectories plus top insights, formatting them into prompt context, and optionally projecting insights by agent role. The memory does not alter model weights or compile into executable tools; it changes behavior by changing what each agent sees before and during the next run.

## Comparison with Our System

G-Memory is closer to [ReasoningBank](./reasoning-bank.md) and [ExpeL](./expel.md) than to our files-first KB. It learns from repeated benchmark tasks into prompt-visible artifacts, but its substrate is still operational memory for a fixed agent harness rather than a curated body of linked knowledge.

| Dimension | G-Memory | Commonplace |
|---|---|---|
| Trace source | Multi-agent benchmark trajectories across ALFWorld, FEVER, and PDDL runs | Human+agent editing traces, notes, links, workshop artifacts |
| Learned substrate | Chroma-backed task records, task-similarity graph, scored text insights | Notes, links, instructions, workshop artifacts |
| Promotion target | Prompt-visible trajectories and natural-language rules | Inspectable text artifacts in a linked KB |
| Update style | Automatic storage, LLM rule maintenance, periodic clustering+merge | Manual curation and targeted file edits |
| Structure strength | Stronger than flat reflection buffers, weaker than typed note/link systems | Strong semantic link and document structure, weaker automatic promotion |
| Oracle strength | Benchmark outcomes and environment feedback | Mostly human judgment and local validation |
| Scope | Fixed evaluation tasks and fixed MAS workflows | Open-ended cross-domain knowledge work |

G-Memory is stronger than our system on automatic cross-task reuse. It captures multi-agent execution traces, retrieves prior successes, and maintains reusable guidance without a human curator in the loop. If the task family recurs and the oracle is strong, that is a real advantage.

Commonplace is stronger on compositional knowledge and inspectable semantics. G-Memory's rules are useful prompt payloads, but they are not typed claims, explicit relationships, or durable explanations. The system optimizes reuse for the next benchmark task, not long-horizon knowledge accumulation across domains.

## Borrowable Ideas

**Separate step-local coordination structure from cross-task memory.** Ready now as a framing. G-Memory distinguishes "what happened among agents inside this run" from "what should be reusable next time." That is cleaner than treating every trace as the same kind of memory.

**Use neighborhood expansion over retrieved tasks.** Needs a use case first. The `TaskLayer` idea is modest but solid: use vector search to find anchors, then expand through a lightweight task graph to widen recall. A KB analogue would be "retrieve candidate notes, then widen through explicit neighbors" rather than ranking every note globally.

**Maintain reusable guidance with explicit operations and scores.** Ready now as a pattern. The insight layer is not sophisticated, but it has a real lifecycle: add, edit, agree, remove, decay. That is a stronger maintenance contract than whole-document rewrites and aligns with what made [ExpeL](./expel.md) interesting.

**Project shared guidance into role-specific prompts.** Needs a use case first. `project_insights(...)` is worth watching because it treats one shared memory artifact as raw material for multiple agent roles instead of assuming one memory view fits everyone.

## Curiosity Pass

The most important correction after reading the code is that G-Memory is not really "a graph memory system" in the singular. It is a memory bundle with different substrates for different jobs: graphs for within-task coordination and task neighborhoods, vectors for coarse retrieval, JSON rules for durable guidance. The hybrid design is more credible than the marketing phrase.

That matters because the repo's strongest idea is not the graph branding. It is the decision to treat multi-agent memory as three different reuse problems:

- recover comparable prior tasks
- preserve local collaboration traces
- maintain higher-level textual guidance

Those are genuinely different problems, and forcing them into one storage abstraction would probably be worse.

The ceiling is also clear. Even if G-Memory works perfectly, it is still a benchmark-scoped prompt-memory system. Its insights are tactical rules, not explanatory knowledge. Its task graph is similarity infrastructure, not a semantic graph. So the repo is a strong reference for deploy-time memory shaping, but not for a general-purpose knowledge base architecture.

The later evaluation in [Ingest: Large Language Model Agents Are Not Always Faithful Self-Evolvers](../../sources/large-language-model-agents-are-not-always-faithful-self-evolvers.ingest.md) sharpens that limit. That paper evaluates G-Memory directly and finds raw experience interventions matter more reliably than interventions on condensed memory. This is also the concrete warning case now recorded in [distillation](../distillation.md): compressed artifacts can remain semantically plausible while losing causal influence at use time. In KB terms, and as an inference from that evaluation rather than from this repo alone: storing and reinjecting a compressed artifact is not the same as making that artifact behaviorally binding.

## What to Watch

- Whether later versions make the insight layer structurally richer than scored text rules
- Whether the task-neighborhood graph outperforms plain vector retrieval strongly enough to justify the extra maintenance
- Whether role-specific projection materially helps, or mostly renames generic prompt rewriting
- Whether future descendants keep the mixed-memory design but drop the "all layers are graphs" framing
- Whether the faithfulness critique on condensed experience pushes this line toward stronger use-time intervention tests

---

Relevant Notes:

- [agentic-memory-systems-comparative-review](./agentic-memory-systems-comparative-review.md) — extends: G-Memory adds a multi-agent, mixed-substrate memory case to the broader survey
- [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — extends: G-Memory is a multi-agent trace-derived artifact-learning system rather than a weight-learning or files-first KB system
- [ExpeL](./expel.md) — compares: both maintain reusable natural-language guidance with explicit update operations, but G-Memory adds multi-agent trajectory capture and graph-shaped task retrieval
- [ReasoningBank](./reasoning-bank.md) — compares: both learn prompt-time artifacts from repeated runs, but G-Memory is the multi-agent branch with explicit coordination traces
- [Voyager](./voyager.md) — contrasts: Voyager promotes executable skills, while G-Memory promotes retrievable trajectories and textual insights
- [distillation](../distillation.md) — sharpens: the same paper now serves as a warning case there, grounding the claim that compressed artifacts can look adequate while losing causal control at use time
- [Ingest: Large Language Model Agents Are Not Always Faithful Self-Evolvers](../../sources/large-language-model-agents-are-not-always-faithful-self-evolvers.ingest.md) — evidence: evaluates G-Memory directly and finds raw experiences remain more behaviorally active than condensed memory
