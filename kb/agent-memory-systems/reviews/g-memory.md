---
description: "G-Memory review: multi-agent trace capture, Chroma task recall, task-neighborhood retrieval, and scored insight rules with role-projected prompt use"
type: ../types/agent-memory-system-review.md
tags: [related-systems, trace-derived]
status: current
last-checked: "2026-05-16"
---

# G-Memory

G-Memory is bingreeky's research implementation of "Tracing Hierarchical Memory for Multi-Agent Systems." The repository wraps benchmark multi-agent systems, including AutoGen, DyLAN, and MacNet, with a memory module that stores completed task traces, retrieves related successes and failures, distills scored natural-language insights, optionally projects those insights by agent role, and injects both retrieved trajectories and insights into future task prompts. The code implements a real trace-derived memory loop, but its "graph" framing is looser than the README suggests: the durable substrate is Chroma task documents plus a pickled task-neighborhood graph and a JSON insight list, not one integrated graph database.

**Repository:** https://github.com/bingreeky/GMemory

**Reviewed commit:** [7b581c51d993bd600df14691d101d7e601040cc6](https://github.com/bingreeky/GMemory/commit/7b581c51d993bd600df14691d101d7e601040cc6)

**Last checked:** 2026-05-16

## Core Ideas

**The runtime captures multi-agent traces as state chains.** Each task starts with `MASMemoryBase.init_task_context(...)`, which creates a `MASMessage` carrying task text, trajectory text, label, extra fields, and a `StateChain` of NetworkX directed graphs ([memory_base.py](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/mas_memory/memory_base.py), [common.py](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/common.py)). AutoGen records one solver or ground-truth message per environment step; MacNet and DyLAN record graph/neuron outputs with upstream node IDs, so the interaction trace preserves both environment actions and multi-agent communication structure ([autogen.py](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/tasks/mas_workflow/autogen/autogen.py), [graph_mas.py](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/tasks/mas_workflow/macnet/graph_mas.py), [dylan.py](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/tasks/mas_workflow/dylan/dylan.py)). The state chain is later serialized into Chroma metadata, so the raw interaction graph is retained as source evidence rather than queried as a graph database.

**Task memory is a Chroma store with structured metadata.** `GMemory.__post_init__()` creates one Chroma collection under `global_config['working_dir'] / namespace`; `add_memory(...)` writes a `Document` whose `page_content` is the task main string and whose metadata is `MASMessage.to_dict(...)` ([GMemory.py](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/mas_memory/GMemory.py)). This makes the task text the vector-search key while the serialized task description, full trajectory, label, extra fields, and state chain are the payload. The storage substrate is therefore a local Chroma directory plus sidecar files, not markdown or a service API.

**The query graph is a task-neighborhood index, not the whole memory.** `TaskLayer` stores a NetworkX graph in `task_layer_graph.pkl`, adds one node per task, and connects it to prior Chroma tasks whose embedding similarity clears a threshold. Retrieval first asks Chroma for top task nodes, then expands their NetworkX neighborhood up to `hop` before fetching full Chroma documents ([GMemory.py](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/mas_memory/GMemory.py)). The README's hierarchical graph language is directionally fair, but the implemented query graph is an auxiliary task adjacency index over task strings; interaction state chains and insights are stored elsewhere.

**Insights are a scored JSON rule list with task correlations.** `InsightsManager` loads and writes `insights.json`, where each insight is a dictionary with `rule`, `score`, `positive_correlation_tasks`, and `negative_correlation_tasks` ([GMemory.py](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/mas_memory/GMemory.py)). Rule extraction is triggered after enough stored tasks and at a fixed cadence; it compares related successful and failed trajectories, or batches successful trajectories, prompts an LLM to emit `ADD`, `EDIT`, `REMOVE`, and `AGREE` operations, parses a restricted operation grammar, and updates scores and correlation task lists. This is the most behavior-shaping artifact in the system: prose rules become future prompt instructions, while scores and task lists govern survival and retrieval.

**The system has both forward prompt injection and backward reward updates.** Before each task, the MAS retrieves successful trajectories, filters successes with an LLM relevance score, retrieves insights by task overlap, formats successes as "Your Own Past Successes," and formats insights as numbered "Key Insights from Related Tasks" ([format.py](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/tasks/mas_workflow/format.py), [GMemory.py](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/mas_memory/GMemory.py)). AutoGen and MacNet call `meta_memory.backward(final_done)` after saving the task; G-Memory then increases cached insight scores after success and decreases them after failure, dropping insights whose score reaches zero ([autogen.py](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/tasks/mas_workflow/autogen/autogen.py), [graph_mas.py](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/tasks/mas_workflow/macnet/graph_mas.py), [GMemory.py](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/mas_memory/GMemory.py)). DyLAN saves task context but does not call the backward hook in the reviewed commit, so reward maintenance is not uniformly wired across MAS backends.

**Role projection is prompt-time rewriting, not a separate memory layer.** With `--use_projector`, the MAS calls `GMemory.project_insights(...)` for each role and asks the LLM to adapt general insights into role-specific numbered advice ([GMemory.py](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/mas_memory/GMemory.py), [prompt.py](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/mas_memory/prompt.py)). The projected list is not persisted as a separate artifact; it is a runtime view over the canonical general insight list.

## Comparison with Our System

| Dimension | G-Memory | Commonplace |
|---|---|---|
| Primary purpose | Improve benchmark MAS execution from previous task traces | Maintain an agent-operated methodology KB |
| Raw substrate | Chroma documents with serialized MASMessage metadata and state chains | Git-tracked notes, instructions, reviews, sources, indexes, and generated reports |
| Graph layer | NetworkX task-neighborhood graph plus serialized interaction graphs | Authored markdown links, generated indexes, and validation-backed references |
| Distilled artifact | Scored prose insight/rule dictionaries in JSON | Typed notes, instructions, ADRs, schemas, commands, skills, and review artifacts |
| Activation | Retrieved successes and insights are injected into task prompts before each action loop | Agents search, follow links, load indexes, use skills, and obey typed instructions |
| Lineage | Rules record correlated task names, but not source spans or explicit trace citations | Source URLs, reviewed commits, frontmatter status, archives, validation, and git history |
| Behavioral authority | Trajectories advise by example; insights instruct or strongly guide through prompts; scores rank and retire rules | Knowledge artifacts advise; system-definition artifacts instruct, route, validate, enforce, or configure |

G-Memory is stronger than commonplace as a live trace-to-guidance benchmark loop. It automatically captures task outcomes, extracts key steps and failure reasons, generates/update rules, retrieves neighboring tasks, and closes a simple reward loop over prompt-injected insights.

Commonplace is stronger as a durable knowledge system. G-Memory's highest-authority artifacts are compact JSON rules with scores and task-name correlations, but they do not carry source trace IDs, source excerpts, review state, invalidation conditions, or explicit authority boundaries. That is acceptable for benchmark prompt guidance; it is weak for methodology claims that a future agent must audit.

The important design split is that G-Memory uses several retained-artifact families at once. Raw trajectories and state chains are knowledge artifacts when reused as examples or evidence. Retrieved successful trajectories remain knowledge artifacts in the prompt. Distilled insights become system-definition artifacts because the task prompt tells agents to use them during execution. Chroma embeddings, the task graph, and insight scores are runtime/index surfaces with ranking or selection authority, not the canonical learned content.

## Borrowable Ideas

**Store raw multi-agent topology alongside task traces.** Ready as an evaluation pattern. G-Memory's state chain captures which agent output depended on which upstream output. A commonplace analogue would be useful for review bundles or multi-agent writing workflows where later diagnosis needs the coordination trace, not only the final text.

**Use a task-neighborhood graph as a retrieval broadener.** Worth testing when we have dense repeated tasks. G-Memory's Chroma-first, graph-neighborhood-second retrieval is a practical way to avoid relying only on nearest neighbors. In commonplace, this would belong below the library layer as a derived search aid, not as the source of truth.

**Keep scored insight rules separate from raw traces.** Ready for narrow workshop surfaces. The JSON list is small, inspectable, and easy to mutate. Commonplace could borrow the pattern for temporary warning queues or candidate operating tips, while requiring promotion into typed notes or instructions before giving them durable authority.

**Role projection should remain a runtime view.** Ready as a caution. G-Memory correctly avoids treating role-tailored advice as canonical memory. Commonplace should do the same if it ever projects general guidance into reviewer, fixer, or writer variants: persist the general source, regenerate the projection.

**Do not borrow source-light rule authority for library claims.** The score and correlation fields are useful activation signals, not proof. A durable commonplace note or instruction needs citations, review status, and clearer invalidation rules than G-Memory's insight object provides.

## Trace-derived learning placement

**Trace source.** G-Memory qualifies as trace-derived learning. Source traces are benchmark task runs across ALFWorld, PDDL, FEVER, and ScienceWorld-style environments: task descriptions, MAS agent messages, upstream agent edges, environment actions, observations, per-step rewards, final feedback, and success/failure labels. The raw trace boundary is one completed task execution.

**Extraction.** Extraction has several stages. `GMemory._extract_mas_message(...)` removes states with negative reward, builds a cleaned trajectory, asks an LLM to extract key successful steps, and asks another prompt to detect failure reasons for failed runs. `InsightsManager.finetune_insights(...)` samples stored tasks, retrieves nearby successes and failures, compares successful and failed trajectories or successful chunks, and asks for `ADD`, `EDIT`, `REMOVE`, or `AGREE` operations against current rules. The environment success label and reward supply the oracle; LLM prompts supply abstraction and mutation proposals.

**Storage substrate.** Raw task memory persists in Chroma under `.db/<model>/<task>/<mas>/<memory>/g-memory/`, with `MASMessage` serialized into document metadata. The task-neighborhood graph persists as a pickled NetworkX graph. Distilled insights persist as `insights.json`; extraction logs go to `insights.log`. Role-projected insights and prompt assemblies are runtime views, not persisted source artifacts.

**Representational form.** Raw trajectories are mixed prose and symbolic structure: text actions/observations plus serialized NetworkX state graphs. Task retrieval uses distributed-parametric embeddings in Chroma and the embedding-derived NetworkX task graph. Distilled insights are prose rules with symbolic JSON fields and numeric scores. Role projection produces prose prompt text from those general rules.

**Lineage.** The task-level lineage is recoverable from each Chroma document's task fields, label, extra fields, and serialized state chain. Rule-level lineage is partial: each insight records positive and negative correlated task names, but not source document IDs, source spans, extraction prompt versions, or a regeneration recipe. Merged insights reset to cluster-correlated task lists and score `2`, further weakening per-rule derivation history.

**Behavioral authority.** Raw state chains and task trajectories are knowledge artifacts when retained as evidence of what happened. Retrieved successes are knowledge artifacts when inserted as examples. Key insights are system-definition artifacts during execution because the formatted prompt tells agents to refer to them for improved problem solving. Chroma search, the task graph, insight scores, and backward reward updates have ranking, selection, and lifecycle authority over which artifacts reach the prompt.

**Scope.** Learning is cross-task within the configured benchmark, model, MAS type, and memory namespace. The code can run the same memory module across multiple MAS backends, but persisted memory paths are scoped by the run directory built in `tasks/run.py`, so the learned content is not a general repository-wide knowledge base.

**Timing.** Trace capture is online during task execution. Distillation is staged online/offline within the run: after enough stored tasks and every configured interval, the memory module extracts or refines insights; every twentieth task it clusters tasks and merges related insights. Backward reward updates happen after later tasks consume cached insights.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), G-Memory sits between ExpeL-style trajectory-to-rule learning and graph-memory systems. It strengthens the survey distinction between raw traces, retrieved examples, runtime indexes, and distilled system-definition artifacts: the "hierarchical graph" story becomes more precise when split into Chroma task store, task-neighborhood graph, serialized interaction graph, and scored prompt-rule list.

## Curiosity Pass

The README's "hierarchical graph" framing is more integrated than the code. There is an interaction graph per task, a query graph over task names, and an "insight graph" concept in comments, but the persistent insight layer is a JSON list. The review should describe the implemented storage split rather than repeat the diagram.

The strongest mechanism is not Chroma retrieval; it is the combination of task correlations, explicit mutation verbs, scores, and reward-backed decay over insight rules. That gives a small prose artifact a lifecycle without whole-document rewriting.

The weakest mechanism is lineage. G-Memory can tell which task names correlate with an insight, but not which messages or observations justify it. That makes automatic maintenance easy and audit expensive.

The reward loop is uneven. AutoGen and MacNet call `backward(...)`; DyLAN does not in this commit. Any claim that G-Memory universally updates insight scores from later rewards should be scoped to the wired backends.

The role projector is useful but authority-amplifying. It rewrites general rules into personalized advice immediately before action, but the projected advice has no separate validation. Treating it as a prompt view rather than a retained artifact is the right boundary.

## What to Watch

- Whether the project turns the insight layer into a real graph with explicit task, trace, role, and rule nodes, or keeps the current JSON-rule implementation.
- Whether future commits add per-rule source citations, prompt versions, or trace IDs.
- Whether DyLAN gets the same backward reward update path as AutoGen and MacNet.
- Whether role-projected insights are evaluated separately from general insights.
- Whether task-neighborhood retrieval beats simple Chroma retrieval once the memory grows beyond small benchmark runs.

## Bottom Line

G-Memory is a genuine trace-derived MAS memory system: it stores completed multi-agent task traces, retrieves related successes through Chroma and a task-neighborhood graph, distills experience into scored natural-language insights, injects those insights into future prompts, and updates consumed insights from later outcomes. Its main lesson for commonplace is the value of separating raw coordination traces, derived retrieval indexes, and behavior-shaping rules while being honest about their different authority and lineage.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: G-Memory is a mixed trace-to-rule and task-neighborhood retrieval system for benchmark MAS runs.
- [ExpeL](./expel.md) - compares-with: both use `ADD`/`EDIT`/`REMOVE`/`AGREE` rule maintenance, while G-Memory adds MAS state chains, a task graph, and role projection.
- [AriGraph](./AriGraph.md) - compares-with: both use graph language around trace-derived memory, but AriGraph builds an in-run world model while G-Memory stores cross-task MAS traces and scored insights.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: G-Memory's storage substrate, representational form, lineage, and behavioral authority differ across traces, Chroma records, task graph, insight JSON, and prompt views.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: G-Memory's raw traces and retrieved successes advise by evidence and example.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: G-Memory's injected insights carry instruction-like authority during task execution.
