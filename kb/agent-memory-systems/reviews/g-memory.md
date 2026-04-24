---
description: Multi-agent memory harness that layers within-run state-graph traces, a task-similarity graph over Chroma-stored trajectories, and a scored JSON rule list with ADD/EDIT/REMOVE/AGREE maintenance
type: ../types/agent-memory-system-review.md
traits: [has-comparison, has-external-sources]
tags: [related-systems, trace-derived]
status: current
last-checked: "2026-04-12"
---

# G-Memory

G-Memory is the official code release for the paper "G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems" (Zhang et al., arXiv 2506.07398). The repo wraps three multi-agent orchestration styles (`autogen`, `dylan`, `macnet`) with a pluggable memory module. Every completed task is archived as a `MASMessage`, retrieved prior tasks and text insights are injected into each agent's prompt on the next task, and a background maintenance loop updates the insight list over time. Benchmarks are ALFWorld, FEVER, and PDDL. The README frames the design as a "three-tier hierarchical graph"; the code is actually a hybrid memory stack with one NetworkX graph inside each task, one NetworkX similarity graph across tasks, and a flat JSON list of scored text rules on top.

**Repository:** https://github.com/bingreeky/GMemory

## Core Ideas

**Within-task coordination is captured as a chain of message DAGs.** `StateChain` in `mas/memory/common.py` stores a list of `networkx.DiGraph` states. Inside each state, `add_message(...)` writes an `AgentMessage` node keyed `"<agent_name>-<counter>"` and adds `edge_type='spatial'` edges from each declared upstream agent. `move_state(action, observation, **args)` closes the current state with the action, observation, and any extra fields (the `MASMemoryBase` wrapper passes `reward=...`), then appends a fresh empty DiGraph. This is a genuinely multi-agent trace shape: a record of who spoke to whom at each step, not just a flat dialogue log.

**Cross-task retrieval is vector search amplified by a task graph.** Completed `MASMessage` instances are stored in Chroma (`langchain_chroma.Chroma`) keyed by `task_main` with `label: True|False` metadata. `TaskLayer` keeps a parallel `nx.Graph` of task strings: `add_task_node(...)` similarity-searches Chroma for up to ten neighbors and adds edges where `1 - distance >= 0.7`. At query time, `retrieve_related_task(...)` takes top-k Chroma hits and expands through that graph by `hop` edges (default 1). If the expansion yields too few success/failure documents to meet the requested topk, `_retrieve_memory_raw(...)` falls back to a direct filtered Chroma query. The graph is a recall widener over vector search, not a replacement.

**The LLM relevance rerank is mostly a no-op in the current code.** `retrieve_memory(...)` asks the LLM to score each retrieved successful trajectory against the query via `generative_task_user_prompt`, builds `sorted_success_tasks` by sorting with those scores, and then takes `sorted_success_tasks[:successful_topk]`. Because the retrieval stage already returns `2 * successful_topk` candidates and the sort does land in a new list, the scoring does re-rank before truncation; however, there is no tie-breaking logic and every score missing a digit falls back to 0, so the effective signal is coarse. Failures and insights are taken in their original order without any rerank at all.

**The top layer is a scored JSON rule list, not a third graph.** `InsightsManager` persists `insights.json` as a list of `{rule, score, positive_correlation_tasks, negative_correlation_tasks}` dicts. Every completed task runs an LLM "key steps" extraction via `_extract_mas_message(...)`; failed tasks additionally get a `fail_reason` via `_detect_mistakes(...)`. Heavier maintenance only starts once `memory_size >= start_insights_threshold` and runs every `rounds_per_insights` completed tasks: `finetune_insights(...)` samples random prior tasks, pairs their top successful and failed trajectories, and asks the LLM for `ADD`/`EDIT`/`REMOVE`/`AGREE` operations over the current rules. `_update_rules(...)` applies these with counter semantics: `ADD` inserts at `score=2`, `AGREE` adds 1, `EDIT` rewrites text and adds 1, `REMOVE` subtracts 1 normally or 3 when the list is at `max_rules_num=10`. `clear_insights()` drops any rule whose score falls below 1. Every 20 completed tasks, `merge_insights(...)` runs FINCH clustering on task embeddings, groups rules by cluster, and asks the LLM to compress each cluster's rules by a factor of three.

**Prompt-time reinjection is the only integration surface.** In `tasks/mas_workflow/{autogen,dylan,macnet}/`, each task run calls `meta_memory.init_task_context(...)`, then `retrieve_memory(...)` to pull back successful trajectories, failed trajectories, and a ranked insight slice, then `project_insights(raw_insights, role)` to specialize the rule list per agent role via an LLM rewrite, and finally `add_agent_node(...)` / `move_memory_state(...)` during the run. After the environment returns a final reward, `save_task_context(label=...)` commits the trace and `backward(reward)` adjusts the score of every insight in `insights_cache` by `+1` on success or `-2` on failure. No weights move; memory is entirely prompt payload plus insight accounting.

**`project_insights` splits shared memory by agent role, but is text-surface only.** `project_insights(raw_insights, role, task_traj=None)` formats the rule list plus the role (and optionally a trajectory) through `project_insights_system_prompt` and parses a numbered list back. If the LLM response fails to parse, it returns the raw insights. The pattern is one shared insight list with per-role projections, not per-role memories.

## Comparison with Our System

G-Memory is closer to [ExpeL](./expel.md) than to our files-first KB. Both maintain a rule list with explicit `ADD`/`EDIT`/`REMOVE`/`AGREE` verbs, both inject rules plus trajectories at prompt time, both depend on a benchmark success signal. G-Memory adds a multi-agent trace shape and a task-neighborhood graph; it does not add inspectable structure (rules remain flat free text).

| Dimension | G-Memory | Commonplace |
|---|---|---|
| Trace source | Multi-agent benchmark trajectories across ALFWorld, FEVER, PDDL | Human and agent editing, notes, workshop artifacts, links |
| Learned substrate | Chroma task store, similarity-edge task graph, scored JSON rules | Typed markdown notes, semantic links, indexes, ADRs |
| Promotion target | Prompt-time trajectories and scored text rules | Inspectable text artifacts in a linked knowledge base |
| Update style | Automatic per-task storage, periodic LLM CRUD on rules, FINCH-triggered merge | Manual curation with validation and review bundles |
| Oracle strength | Benchmark success/failure plus environment reward | Weak human judgment plus structural validation |
| Structure strength | Weaker than typed note/link systems; rules are flat text | Strong document and link structure, weaker automatic promotion |
| Scope | Fixed MAS orchestrations over three benchmark task families | Open-ended cross-domain methodology |

G-Memory is stronger at automatic cross-task reuse when the task family repeats and the oracle is hard. It captures multi-agent execution traces, accumulates reusable guidance, and prunes through counter decay without a human in the loop.

Commonplace is stronger at compositional knowledge. G-Memory's rules are prompt payloads with no links, no types, no provenance beyond `positive_correlation_tasks`. The system is engineered for the next benchmark task rather than long-horizon knowledge that humans can read and reshape.

**Trace-derived learning placement.** The trace source is completed multi-agent benchmark trajectories over ALFWorld, FEVER, and PDDL, with trigger boundaries at per-task for storage and key-step extraction, per `rounds_per_insights` tasks for CRUD maintenance, and every 20 tasks for FINCH clustering and rule merging. Extraction pulls out task key steps (all tasks), failure reasons (failed tasks), and LLM-proposed `ADD`/`EDIT`/`REMOVE`/`AGREE` operations over the current rule list; the oracle is the environment reward that labels each trajectory success or failure, and a secondary LLM judge proposes and merges rules. Promotion targets are entirely inspectable artifacts — Chroma-stored trajectories, a NetworkX task graph, and a scored JSON rule list — plus per-role prompt projections; nothing moves into model weights. Scope is cross-task within one benchmark family, with per-task-family `persist_dir` state keeping rule sets separate. Timing is online during deployment: storage, CRUD maintenance, and prompt-time injection all happen during the same run loop. On [the survey's axes](../trace-derived-learning-techniques-in-related-systems.md), G-Memory sits in the trajectory-run pattern on axis 1 and in symbolic-artifact learning on axis 2, in the "scored flat rules" subtype on the structure spectrum, with "explicit CRUD verbs" as its maintenance path. The review reinforces the survey's existing placement and does not warrant a new subtype; the distinctive shape of the system — a within-task coordination DAG layered under a cross-task rule list — remains the one multi-agent case in the survey.

## Borrowable Ideas

**Separate step-local coordination structure from cross-task reusables.** Ready now as a framing. The repo distinguishes "what happened among agents inside this run" (state-chain DAG, discarded after commit) from "what should be reusable next time" (Chroma tasks, rule list). That split is cleaner than treating every trace as the same kind of memory.

**Neighborhood expansion over vector retrieval.** Needs a use case first. `TaskLayer.retrieve_related_task` is modest but solid: use similarity to find anchors, then expand through a lightweight similarity-edge graph to widen recall with a bounded hop. A KB analogue would be "retrieve candidate notes, then widen through explicit neighbors" rather than ranking every note globally each time.

**Decay-by-counter with asymmetric `REMOVE` weight.** Ready now as a design pattern. The rule counters create real decay (`clear_insights` drops anything below 1), and the `REMOVE` weight shift (1 normally, 3 when the list hits `max_rules_num`) is a pragmatic guard against list bloat. Both would be cheap to mirror in any commonplace artifact that accumulates LLM-proposed updates.

**Operation-level validation on LLM-proposed CRUD.** Ready now as a defensive pattern. `_update_rules(...)` rejects `ADD` of an already-matching rule, drops `EDIT`/`REMOVE`/`AGREE` with out-of-range indices, and converts `EDIT` of an existing rule text into an `AGREE` bump. That is a lightweight way to harden any LLM-driven maintenance loop against degenerate proposals.

**Cluster-then-compress as a periodic compaction pass.** Needs a use case first. `merge_insights()` clusters task nodes via FINCH and then asks the LLM to compress each cluster's rules by a factor of three. The specific algorithm is secondary; the pattern — cluster the contexts, compress the artifacts per cluster — is transferrable to any growing rule or lesson store.

**Per-role projection of one shared memory.** Needs a use case first. `project_insights(...)` treats a single shared rule list as raw material for multiple agent views rather than maintaining separate memories per role. Worth watching as agents in a KB accumulate role-specific lenses over the same underlying notes.

## Curiosity Pass

**"Three-tier graph" is mostly naming, not mechanism.** The README and source docstrings describe an interaction graph, a query graph, and an insight graph. In code, only the interaction layer (`StateChain`) and the task layer (`TaskLayer`) are NetworkX graphs. The insight layer is a flat Python list serialized to JSON; `positive_correlation_tasks` and `negative_correlation_tasks` are just lists-of-strings on each rule dict. Calling that a "graph" is marketing. The actual substrate is a hybrid: graphs for coordination shape, vectors for retrieval, lists for durable guidance. The hybrid design is credible; the unified-graph framing is not.

**The task-layer graph is thin relative to the vector store.** Edges are added only at `add_task_node` time based on a top-10 similarity query with a 0.7 threshold; the graph never densifies otherwise, and `cluster_tasks()` assigns `cluster_id` attributes but does not add edges. So `retrieve_related_task` with `hop=1` will usually return at most the top-k vector hits plus their ten-neighbor fan-out at insert time, often heavily overlapping the direct vector result. The "amplification" is real but bounded; on small memories the graph contributes little beyond the vector store.

**CRUD maintenance runs on a random sample of prior tasks, not all tasks.** `finetune_insights(num_points)` picks `num_points` random IDs from the Chroma store and runs the comparative/success critique against each. Coverage is therefore stochastic and depends on `insights_point_num` (default 5). Two consequences: useful rules may be reinforced or decayed inconsistently across rounds, and the rule list's stability is partly an artifact of sample size rather than a deliberate policy.

**The `score=2` promotion baseline is fragile.** New rules enter at score 2; a single failure-triggered `backward(reward=False)` subtracts 2, zeroing the rule out, and `clear_insights()` then removes it. So a rule can be added in one round and deleted in the next if any retrieved task fails while it is in `insights_cache`. This is stronger decay than the ExpeL counter, and it likely matters for stability on harder benchmarks — worth remembering before borrowing the numeric constants verbatim.

**The ceiling is still a benchmark-scoped prompt-memory system.** Even if every subsystem worked perfectly, the promoted artifacts are tactical rules and retrievable trajectories. There is no explanatory layer, no cross-task abstraction, no typed structure. G-Memory is a reference for deploy-time memory shaping in a fixed MAS harness — not for general-purpose knowledge base architecture. The external evaluation in [Ingest: Large Language Model Agents Are Not Always Faithful Self-Evolvers](https://arxiv.org/html/2601.22436v2) sharpens that limit: it tests G-Memory directly and finds raw trajectories remain more behaviorally binding than the condensed insight list, which is exactly the [distillation](../../notes/definitions/distillation.md) failure mode of semantically-plausible-but-causally-weak compressed artifacts.

## What to Watch

- Whether later versions replace the flat JSON rule list with something typed, linked, or provenance-bearing
- Whether the task-neighborhood graph outperforms plain vector retrieval strongly enough to justify its maintenance
- Whether `project_insights` shows measurable benefit in ablations, or collapses into generic prompt rewriting
- Whether `finetune_insights`'s random sampling is replaced by something coverage-aware
- Whether future descendants drop the "three-tier graph" framing and present the architecture honestly as a hybrid stack

---

Relevant Notes:

- [agentic-memory-systems-comparative-review](../agentic-memory-systems-comparative-review.md) — extends: G-Memory contributes the multi-agent, mixed-substrate case to the broader survey
- [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — extends: G-Memory is the multi-agent trajectory-run CRUD-verb artifact-learning instance in the survey
- [ExpeL](./expel.md) — compares: both maintain a scored rule list with ADD/EDIT/REMOVE/AGREE verbs and inject rules plus retrieved trajectories at prompt time; G-Memory adds a multi-agent trace shape and a task-neighborhood graph
- [distillation](../../notes/definitions/distillation.md) — sharpens: G-Memory's insight list is the canonical warning case — compressed artifacts that remain semantically plausible while losing causal influence at use time
- [Ingest: Large Language Model Agents Are Not Always Faithful Self-Evolvers](https://arxiv.org/html/2601.22436v2) — evidence: evaluates G-Memory directly and finds raw experiences remain more behaviorally binding than condensed memory
