---
description: "G-Memory review: benchmark MAS memory with Chroma task traces, task graphs, trace-derived insights, and relevance-gated prompt read-back"
type: ../types/agent-memory-system-review.md
tags: [trace-derived, push-activation]
status: current
last-checked: "2026-06-01"
---

# G-Memory

G-Memory, from bingreeky's `GMemory` repository, is the official implementation of "G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems." It is a benchmark-oriented Python framework that plugs memory modules into AutoGen, DyLAN, and MacNet-style multi-agent task solvers, with G-Memory adding persistent task traces, a related-task graph, distilled insights, and prompt-time read-back for ALFWorld, PDDL, FEVER, and SciWorld-style tasks.

**Repository:** https://github.com/bingreeky/GMemory

**Reviewed commit:** [7b581c51d993bd600df14691d101d7e601040cc6](https://github.com/bingreeky/GMemory/commit/7b581c51d993bd600df14691d101d7e601040cc6)

**Last checked:** 2026-06-01

## Core Ideas

**G-Memory is a benchmark MAS harness with interchangeable memory modules.** `tasks/run.py` builds an environment, a MAS workflow, a reasoning module, and a memory module selected by `module_map`; `g-memory` maps to the `GMemory` class alongside baselines such as Voyager, MemoryBank, ChatDev, Generative, and MetaGPT (https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/tasks/run.py, https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/module_map.py). The README positions the implementation as a hierarchical memory architecture for multi-agent systems rather than a general assistant memory product (https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/README.md).

**The standing memory substrate is Chroma plus local graph and JSON files.** `GMemory.__post_init__` creates a Chroma vector store under the configured working directory, then composes a `TaskLayer` and `InsightsManager` over the same persist directory (https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/mas_memory/GMemory.py). `tasks/run.py` sets that directory to `./.db/<model>/<task>/<mas_type>/<memory_type>` (https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/tasks/run.py). The task graph is pickled as `task_layer_graph.pkl`; insights are stored in `insights.json` and logged to `insights.log`.

**Completed tasks are captured as multi-agent traces.** Each workflow calls `init_task_context`, retrieves prior memory, records every agent response as an `AgentMessage` node, records action/observation/reward steps, and finally calls `save_task_context` with the environment outcome (https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/tasks/mas_workflow/autogen/autogen.py, https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/tasks/mas_workflow/dylan/dylan.py, https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/tasks/mas_workflow/macnet/graph_mas.py). `StateChain` stores a sequence of NetworkX directed graphs, where graph-level fields hold actions, observations, and rewards, and nodes hold agent messages plus upstream edges (https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/common.py).

**Trace distillation happens before storage and periodically afterward.** `add_memory` first calls `_extract_mas_message`: it removes negative-reward states from the stored successful trajectory, creates a digit-stripped `clean_traj`, asks an LLM to extract `key_steps`, and asks an LLM for a failure reason on failed tasks (https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/mas_memory/GMemory.py, https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/mas_memory/prompt.py). After enough memories accumulate, `InsightsManager.finetune_insights` samples stored traces, compares successful and failed trajectories, parses `ADD`, `EDIT`, `REMOVE`, and `AGREE` operations, updates rule scores and positive/negative task correlations, and periodically merges rules by FINCH task clusters (https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/mas_memory/GMemory.py).

**Read-back is orchestrator-pushed into the task prompt.** Before solving a task, AutoGen, DyLAN, and MacNet call `retrieve_memory`, format retrieved successful trajectories as "Your Own Past Successes," format insights as numbered rules, optionally project the rules by agent role, and pass the assembled material to each agent through `format_task_prompt_with_insights` (https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/tasks/mas_workflow/format.py, https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/tasks/mas_workflow/autogen/autogen.py). From the acting agent's perspective, this is not a manual lookup: the workflow pushes selected prior memory into context before the next action.

**Context efficiency is selection-heavy, not compression-heavy.** G-Memory controls volume through `successful_topk`, `failed_topk`, `insights_topk`, a similarity threshold, graph hop count, doubled retrieval windows, LLM reranking of successful cases, score-based insight filtering, and rule merging (https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/tasks/run.py, https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/mas_memory/GMemory.py). It does not implement a global token budget or cited snippet selection: retrieved examples include task descriptions, key steps, and detailed trajectories, while the current task summary is the full task description plus accumulating trajectory from `MASMemoryBase.summarize` (https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/mas_memory/memory_base.py, https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/tasks/mas_workflow/format.py).

## Artifact analysis

- **Storage substrate:** `vector` — A LangChain Chroma store under the run-specific `.db` working directory
- **Representational form:** `prose` `symbolic` `parametric` — Task text, trajectories, and insight rules are prose; state chains, JSON metadata, graphs, scores, and prompt/workflow code are symbolic; Chroma embeddings and embedding-derived similarity state are parametric (https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/mas_memory/GMemory.py, https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/common.py)
- **Lineage:** `authored` `trace-extracted` — Prompt assembly and workflow code are authored system definitions, while task memories, state chains, task graph edges, insights, and scores derive from completed MAS task traces.
- **Behavioral authority:** `knowledge` `instruction` `routing` `ranking` `learning` — Stored traces serve as evidence/examples, injected insights and prompt templates instruct, the task graph routes retrieval, similarity/reranking/scores rank candidates, and trace-derived rules learn from outcomes.

**Chroma task memory.** The storage substrate is a LangChain Chroma store under the run-specific `.db` working directory. The representational form is mixed: page content is the task main text, metadata serializes task description, trajectory prose, Boolean outcome label, JSON extra fields, and a JSON-serialized NetworkX state chain (https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/mas_memory/GMemory.py, https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/common.py). Lineage is direct runtime trace capture from completed benchmark tasks, lightly transformed by `_extract_mas_message`. Behavioral authority is knowledge artifact authority while stored as evidence and examples; it gains ranking and prompt-example authority when selected by retrieval.

**State chains and agent-message graphs.** The storage substrate is in-memory `MASMessage.current_task_context` during a task and serialized metadata inside Chroma after `save_task_context`. The representational form is symbolic graph structure plus prose agent messages, actions, observations, and system/user instructions (https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/common.py). Lineage is the multi-agent execution trace, including spatial dependencies in DyLAN and MacNet workflows. Behavioral authority is mostly audit and learning-input knowledge artifact authority; after successful retrieval, selected trajectories become examples in a high-authority prompt channel.

**Task graph.** The storage substrate is a NetworkX graph persisted by pickle as `task_layer_graph.pkl` in the memory directory. The representational form is symbolic graph nodes and weighted edges, with embeddings used transiently to create similarity edges and FINCH cluster labels during merge passes (https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/mas_memory/GMemory.py). Lineage derives from task-main strings already stored in Chroma. Behavioral authority is routing and ranking influence: the graph expands retrieval to k-hop related tasks, but it does not directly instruct the agent.

**Insight memory.** The storage substrate is `insights.json` plus `insights.log`. The representational form is prose rules with symbolic fields: `score`, `positive_correlation_tasks`, and `negative_correlation_tasks` (https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/mas_memory/GMemory.py). Lineage is trace-derived: LLM critiques of success/failure pairs, all-success batches, cluster merges, and post-task score updates. Behavioral authority becomes system-definition artifact authority when selected insights are inserted into the task prompt as numbered guidance; stored insights also remain knowledge artifacts for later scoring and merging.

**Role-projected insights.** The storage substrate is transient prompt output, not a durable artifact in the inspected workflows. The representational form is prose advice generated by an LLM from general insights and an agent role when `--use_projector` is enabled (https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/mas_memory/GMemory.py, https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/tasks/run.py). Lineage is derived from selected insight rules, optionally a trajectory if the API is called with one, though the workflow paths I inspected pass only the role. Behavioral authority is prompt-level advice for a role-specific agent; because it is not stored, it is a consumption-path transformation rather than standing memory.

**Prompt assembly and workflow code.** The storage substrate is Python source under `tasks/mas_workflow/` and prompt templates under `mas/memory/mas_memory/prompt.py`. The representational form is executable symbolic code plus authored prose templates (https://github.com/bingreeky/GMemory/tree/7b581c51d993bd600df14691d101d7e601040cc6/tasks/mas_workflow, https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/mas_memory/prompt.py). Lineage is authored system code. Behavioral authority is system-definition authority over when memory is retrieved, how many items are selected, how they are phrased, and which agents receive role-projected variants.

**Promotion path.** G-Memory promotes runtime traces into behavior-shaping artifacts along several paths: raw MAS trace -> cleaned/key-step trajectory -> Chroma task memory -> retrieved prompt example; success/failure traces -> LLM rule operations -> scored insights -> prompt guidance; task strings -> graph edges/clusters -> retrieval and merge routing. The strongest promotion is trace evidence becoming scored prose insights with prompt authority, but item-level provenance from each rule back to exact trace IDs and LLM outputs is not preserved in the rule object.

## Comparison with Our System

| Dimension | G-Memory | Commonplace |
|---|---|---|
| Primary purpose | Benchmark multi-agent task solving with reusable cross-task memory | Typed, agent-operated methodology knowledge base |
| Main substrate | Chroma, pickled NetworkX graph, JSON insight rules, runtime logs | Git-tracked Markdown collections, type specs, source snapshots, generated indexes, review reports |
| Memory unit | Task traces, state graphs, related-task nodes, insights, role-projected rules | Notes, reviews, instructions, sources, ADRs, indexes |
| Learning path | Automatic trace capture, LLM key-step extraction, failure analysis, rule operations, cluster merging | Agent-authored artifacts under collection/type contracts, validation, semantic review, git lifecycle |
| Activation | Pre-task prompt push with graph/vector/LLM relevance gates | Mostly explicit pull through `rg`, indexes, links, skills, and review workflows |
| Governance | Outcome labels, scores, correlations, thresholds, benchmark success | Frontmatter schemas, collection contracts, validation, citations, review gates |

G-Memory is stronger than Commonplace on automatic pre-action activation. Its workflows retrieve prior trajectories and insights before task solving begins, and then keep injecting the selected material into each agent prompt. That directly addresses the failure mode where stored knowledge exists but the acting agent never pulls it.

Commonplace is stronger on durable provenance and reviewable authority. G-Memory stores useful traces and scored rules, but the durable insight object does not cite the exact source trace pair, extraction prompt, LLM response, merge operation, or approval state that produced it. In Commonplace terms, G-Memory gives trace-derived lessons prompt authority quickly, while Commonplace usually requires a clearer promotion boundary before a lesson becomes an instruction or validator.

The systems also differ in their tolerance for opaque storage. Chroma and pickle are acceptable in a benchmark harness where runs are reproducible experiments, but they are weak as a long-lived knowledge library substrate. Commonplace's Markdown and git model makes artifacts slower to promote but easier to inspect, diff, review, invalidate, and retire.

**Read-back:** `push` — With instance-targeted inferred activation through task-graph expansion, embedding similarity, thresholds, LLM judgment reranking, top-k limits, and prompt assembly before agent action

### Borrowable Ideas

**Treat task traces as first-class evidence, not just logs.** Commonplace workshop runs could preserve a structured trace artifact containing prompt inputs, selected context, tool actions, outcomes, and reviewer feedback. Ready as a run-log schema idea; promotion into library artifacts still needs gates.

**Use a task graph as a recall expander.** G-Memory's k-hop expansion over related tasks is a compact way to retrieve neighboring experiences beyond raw vector similarity. Commonplace could use link neighborhoods or generated connect reports similarly for review examples. Needs a concrete activation workflow before implementation.

**Separate retrieved examples from distilled rules.** The distinction between successful trajectories and generalized insights is useful: examples remain knowledge artifacts, while rules can become system-definition artifacts after review. Ready now as vocabulary for workshop memory design.

**Keep role projection as a consumption-path transformation.** G-Memory projects general insights into role-specific advice without making the projection a durable source of truth. Commonplace could do the same for temporary review-worker prompts, while preserving the original reviewed artifact as canonical.

**Do not borrow opaque rule provenance.** G-Memory's insights are useful but under-cited. Commonplace should require source paths, trace IDs, extraction prompts, and review state before any trace-derived rule receives durable instruction authority.

**Use post-action feedback to demote loaded guidance.** G-Memory's `backward` path adjusts cached insight scores after task success or failure. Commonplace could record which instructions or examples were injected before a run and attach later quality signals. Needs a run-log schema and careful attribution.

## Trace-derived learning placement

**Trace source:** `session-logs` `tool-traces` `trajectories` — Completed MAS task contexts include agent messages, system/user instructions, action/observation/reward steps, final labels, environment feedback, and graph-linked trajectories.

**Learning scope:** `per-task` `cross-task` — Raw contexts are captured per completed task, while related-task retrieval, insight finetuning, correlations, and cluster merges reuse traces across tasks within the run-local benchmark memory.

**Learning timing:** `online` `staged` — Task traces are captured during execution and at task save time; insight finetuning and merge passes run later after memory-count thresholds.

**Distilled form:** `prose` `symbolic` `parametric` — Distillation produces prose key steps, failure reasons, and insight rules; symbolic state chains, graph/rule metadata, scores, and correlations; and embedding-indexed task memory for similarity retrieval.

**Trace source.** G-Memory qualifies as trace-derived learning. Raw traces are completed MAS task contexts: task text, agent messages, system/user instructions, action/observation sequences, rewards, final labels, environment feedback, and graph links among agents or nodes (https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/common.py, https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/tasks/mas_workflow/macnet/graph_mas.py).

**Extraction.** Extraction is staged. `_extract_mas_message` removes negative-reward states from successful traces, creates `clean_traj`, extracts key steps with an LLM, and records failure reasons for failed traces. `finetune_insights` samples stored memories, compares success/failure trajectories or successful chunks, asks an LLM for rule operations, parses those operations, and updates scored insights. `merge_insights` clusters tasks with FINCH and asks an LLM to merge related rules (https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/mas_memory/GMemory.py, https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/mas_memory/prompt.py).

**Four fields.** The raw stage persists in Chroma metadata and serialized state chains; its representational form is mixed prose, symbolic graph, JSON, and embedding-indexed task text; lineage is direct task execution; behavioral authority is evidence, retrieval substrate, and learning input. The distilled stage persists as JSON insight rules and scores; its representational form is prose plus symbolic correlation metadata; lineage is LLM-derived from selected task traces and cluster merges; behavioral authority is prompt-level system-definition advice when injected. The graph stage persists as pickle; its form is symbolic graph/ranking state; its authority is routing influence.

**Scope and timing.** Scope is run-local under `.db/<model>/<task>/<mas_type>/<memory_type>`, with retrieval scoped by task query, labels, top-k settings, threshold, and hop count. Trace capture is online during task execution; key-step/failure extraction happens at task save time; insight finetuning runs after memory-size thresholds; merge passes run every 20 stored memories; read-back runs before future task actions.

**Survey placement.** G-Memory belongs in the trace-to-rules plus trace-to-examples family. It strengthens the survey distinction between raw trace retention and distilled behavior-shaping artifacts: trajectories are reusable examples, while insights are generalized rules with stronger prompt authority. It also illustrates the governance gap: trace-derived rules can become prompt guidance without item-level source lineage.

## Read-back placement

**Read-back signal:** `inferred / embedding` `inferred / judgment` — Push selection is keyed to the current task through embedding similarity, graph-expanded similar tasks, cosine thresholds, and LLM judgment reranking.

**Read-back timing:** `pre-action` — Retrieval and prompt assembly happen before task solving and before each action prompt consumes the selected trajectories and insights.

**Faithfulness tested:** `no` — The review found task outcomes and score updates, but no item-level with/without ablation proving that a specific injected memory changed behavior.

**Direction.** Read-back is push from the acting agent's perspective. The MAS workflow retrieves memory before task solving and inserts selected successful trajectories and insights into the prompt; agents do not issue a memory lookup themselves (https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/tasks/mas_workflow/autogen/autogen.py, https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/tasks/mas_workflow/format.py).

**Targeting and signal.** The trigger is each scheduled task, but the loaded memory is instance-targeted to the current task text rather than coarse always-load. The signal is inferred and mixed: task cases start from embedding similarity over task nodes, expand through k-hop graph neighbors, fall back to label-filtered Chroma similarity when needed, filter by cosine threshold, double candidate windows, and then use LLM judgment to rerank successful trajectories by usefulness to the query; insights are selected by related-task correlations after similar-task retrieval (https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/mas_memory/GMemory.py). This instance-targeted inferred signal plus the before-action prompt hook justifies `push-activation`; actual precision and recall are not verified from code.

**Timing relative to action.** Retrieval happens after `init_task_context` and before the task loop. The selected trajectories and role-specific or raw insights are then reused in prompt construction for each action step. `backward` score updates happen after the task and can only affect future retrieval, not the just-finished action.

**Selection, scope, and complexity.** Selection is bounded by CLI/workflow settings (`successful_topk`, `failed_topk`, `insights_topk`, `threshold`, `hop`), graph expansion, label filtering, similarity thresholds, LLM reranking, and insight score/correlation filtering (https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/tasks/run.py, https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/mas_memory/GMemory.py). Complexity remains substantial because retrieved memory is inserted as whole formatted task cases with detailed trajectories, not as cited snippets under a token budget.

**Authority at consumption.** Retrieved successful trajectories have example authority: they shape behavior as demonstrations. Insights have stronger advisory system-definition authority because they are displayed as numbered guidance under "Key Insights from Related Tasks." Role-projected insights preserve that authority but tailor the wording to each agent role.

**Faithfulness.** The repository tracks task success and adjusts insight scores after outcomes in AutoGen and MacNet, but I did not find item-level ablations proving that a specific insight or trajectory caused a specific behavior change. Structural activation is implemented; effective per-memory influence is not verified from code. DyLAN records and retrieves memory but does not call `backward` in the inspected schedule path, unlike AutoGen and MacNet (https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/tasks/mas_workflow/dylan/dylan.py).

**Other consumers.** Humans can inspect JSON insights, logs, and local `.db` artifacts if they know the run directory. The main consumers are the workflow prompt builders, the insight finetuning/merge routines, and the task graph retriever.

## Curiosity Pass

**The named three-layer memory is unevenly visible in code.** The implementation clearly has stored interaction traces, a task/query graph, and an insight manager, but the code-level artifacts are Chroma metadata, a pickled task graph, and JSON insights rather than a single explicit three-layer graph object.

**Rule provenance is thinner than the learning loop.** The insight object records rule text, score, and correlated task names, but not the exact Chroma IDs, prompt variant, LLM response, merge source, or operation history. That makes later auditing difficult even though the extraction loop is trace-derived.

**Context selection is stronger than context budgeting.** Top-k and threshold controls exist, but whole trajectories can still enter the prompt. A system can be relevance-gated and still overload the agent with complex examples.

**The fallback retrieval branch appears weaker than intended.** In `_retrieve_memory_raw`, when graph retrieval yields too few successes or failures, the code replaces the candidate list with Chroma similarity results, then loops with a condition that cannot append new docs because it checks membership against the same list. This does not erase the retrieval mechanism, but it means graph candidates and fallback candidates are not obviously combined as the comment suggests (https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/mas_memory/GMemory.py).

**The role projector has a richer API than the workflows use.** `project_insights` can condition on a task trajectory, but AutoGen, DyLAN, and MacNet call it with role only. The implemented workflow is role projection from selected rules, not role-and-current-trajectory adaptation.

## What to Watch

- Whether future versions preserve item-level lineage from insights back to source trace IDs, extraction prompts, LLM outputs, and merge operations. That is the main bridge from benchmark memory to auditable knowledge.
- Whether prompt assembly gains a token budget or snippet selector for retrieved trajectories. That would make the relevance-gated activation more usable outside short benchmark prompts.
- Whether DyLAN gains the same post-task `backward` scoring call as AutoGen and MacNet. That determines whether insight scores consistently learn from outcomes across MAS types.
- Whether the task graph moves from pickle to an inspectable structured artifact. That would improve reviewability and make graph edits or invalidation safer.
- Whether role projection becomes durable, evaluated, or trajectory-conditioned in the workflow. That would change it from a temporary consumption transform into a stronger behavior-shaping artifact.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: G-Memory turns MAS task traces into retrieved examples, scored insights, and graph-mediated ranking state.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: G-Memory pushes selected memories into the next task prompt instead of relying on manual lookup.
- [Activate Behavior-Changing Memory Before The Mistake](../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) - exemplifies: retrieved examples and insights are selected before future task actions.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Chroma records, state graphs, task graphs, JSON insights, and prompt builders differ by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: raw traces and retrieved examples serve as evidence, context, and learning input.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: injected insights, prompt templates, retrieval settings, and workflow code shape future behavior.
