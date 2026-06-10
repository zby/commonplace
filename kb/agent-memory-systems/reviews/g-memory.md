---
description: "G-Memory review: trace-derived multi-agent memory with Chroma task storage, NetworkX task graph, JSON insights, and orchestrator-pushed examples/rules"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-04"
tags: [trace-derived]
---

# G-Memory

G-Memory, from bingreeky's `bingreeky/GMemory` repository, is a Python experiment implementation of "G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems." At the reviewed commit, it provides a multi-agent task runner for ALFWorld, FEVER, PDDL, and SciWorld-style tasks, plus a `g-memory` memory module that records completed task trajectories, stores task records in Chroma, maintains a NetworkX task graph, derives reusable insight rules with LLM prompts, and injects retrieved successes and insights into later MAS prompts.

**Repository:** https://github.com/bingreeky/GMemory

**Reviewed commit:** [7b581c51d993bd600df14691d101d7e601040cc6](https://github.com/bingreeky/GMemory/commit/7b581c51d993bd600df14691d101d7e601040cc6)

**Source directory:** `related-systems/GMemory`

## Core Ideas

**Task executions become the durable memory unit.** The MAS workflows call `init_task_context()` before a task, append agent messages and environment steps during execution, and call `save_task_context()` after final feedback; `GMemory.add_memory()` then stores a `MASMessage` as Chroma metadata with the task name as document content ([mas/memory/mas_memory/memory_base.py](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/mas_memory/memory_base.py), [mas/memory/mas_memory/GMemory.py](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/mas_memory/GMemory.py), [mas/memory/common.py](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/common.py)). The retained trace includes task text, trajectory text, success/failure label, extra LLM-derived fields, and serialized state graphs.

**The hierarchy is implemented as Chroma plus file-backed graph and rule sidecars.** `GMemory.__post_init__()` creates a Chroma store under `persist_dir`, a `TaskLayer` with a pickled NetworkX graph, and an `InsightsManager` with an `insights.json` file and log ([mas/memory/mas_memory/GMemory.py](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/mas_memory/GMemory.py), [mas/utils.py](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/utils.py)). The README's "Insight Graph, Query Graph, and Interaction Graph" framing maps in code to insight rules, task-similarity graph expansion, and the serialized per-task `StateChain` rather than to a single persisted graph database ([README.md](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/README.md)).

**Writes distill trajectories before storing them.** `_extract_mas_message()` removes states with negative reward, rewrites successful trajectories as action/observation text, strips numbers from a clean trajectory, asks an LLM for key steps, and asks another LLM prompt for failure reasons on failed runs ([mas/memory/mas_memory/GMemory.py](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/mas_memory/GMemory.py), [mas/memory/mas_memory/prompt.py](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/mas_memory/prompt.py)). This is a real trace-derived learning path: the durable memory is not just raw logs, but logs plus LLM-extracted operational summaries.

**Insights are periodically synthesized and maintained.** Once the Chroma task count reaches `start_insights_threshold`, `add_memory()` calls `finetune_insights()` every `rounds_per_insights` tasks and `merge_insights()` every 20 tasks ([mas/memory/mas_memory/GMemory.py](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/mas_memory/GMemory.py)). The insight prompts support `ADD`, `EDIT`, `REMOVE`, and `AGREE`; the update code changes rule text, score, and positive/negative task correlations, while merge clusters tasks and asks an LLM to consolidate related rules ([mas/memory/mas_memory/GMemory.py](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/mas_memory/GMemory.py), [mas/memory/mas_memory/prompt.py](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/mas_memory/prompt.py)).

**Read-back is orchestrator-pushed, not agent-initiated search.** AutoGen, DyLAN, and MacNet schedules retrieve successful trajectories and insights before each task, format them into prompt sections, and pass those prompts to the agents ([tasks/mas_workflow/autogen/autogen.py](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/tasks/mas_workflow/autogen/autogen.py), [tasks/mas_workflow/dylan/dylan.py](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/tasks/mas_workflow/dylan/dylan.py), [tasks/mas_workflow/macnet/graph_mas.py](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/tasks/mas_workflow/macnet/graph_mas.py), [tasks/mas_workflow/format.py](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/tasks/mas_workflow/format.py)). Context volume is bounded by CLI/config values for successful, failed, and insight top-k plus the similarity threshold; context complexity remains high because full task descriptions, trajectories, key steps, and free-form insight rules are injected as plain prompt text.

**Trust is mostly experimental, not governed.** The implementation has labels, scores, correlations, logs, and dataset reward feedback, but no provenance review, schema validation for LLM rule outputs beyond regex parsing, contradiction audit, or behavior-faithfulness test that proves a particular retrieved memory changed an agent's action ([mas/memory/mas_memory/GMemory.py](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/mas_memory/GMemory.py), [tasks/run.py](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/tasks/run.py)).

## Artifact analysis

- **Storage substrate:** `vector` - The central retained task store is a Chroma vector store under the configured `persist_dir`, with a pickled NetworkX task graph, `insights.json`, and logs as sidecars in the same working directory.
- **Representational form:** `prose` `symbolic` `parametric` - Task trajectories, key steps, failure reasons, and insight rules are prose; labels, scores, correlations, serialized state graphs, JSON records, prompt contracts, and graph edges are symbolic; sentence-transformer embeddings and Chroma similarity are parametric retrieval state.
- **Lineage:** `trace-extracted` `authored` - The main memory entries and insight rules are derived from MAS trajectories and reward-labeled task outcomes, while prompts, configs, graph construction code, and formatting templates are authored package artifacts.
- **Behavioral authority:** `knowledge` `routing` `ranking` `learning` - Retrieved trajectories and insight rules advise later agents as prompt context; the task graph routes query expansion; Chroma similarity and LLM relevance scores rank results; insight update operations learn and revise rule state from accumulated trajectories.

**`MASMessage` task records.** Storage substrate: Chroma documents under `persist_dir`, with `task_main` as page content and serialized `MASMessage` fields in metadata. Representational form: prose task descriptions/trajectories plus symbolic labels, extra fields, and state-chain JSON. Lineage: trace-extracted from each run, then sparsified and enriched by LLM prompts before insertion. Behavioral authority: knowledge artifact when retrieved as successful or failed examples; weak instruction surface when the formatted example appears in an agent prompt.

**Task graph.** Storage substrate: `task_layer_graph.pkl` in the memory working directory. Representational form: symbolic NetworkX graph with weighted task-similarity edges and optional cluster ids. Lineage: derived from stored task names, Chroma similarity search, and FINCH clustering. Behavioral authority: routing artifact for k-hop expansion during retrieval and for grouping tasks before insight merge.

**Insight rules.** Storage substrate: `insights.json` plus an `insights.log` trace of prompts and responses. Representational form: prose rule text with symbolic score, positive correlation tasks, and negative correlation tasks. Lineage: trace-extracted and LLM-derived from successful and failed trajectories; later edited, agreed, removed, merged, or reward-adjusted by automatic operations. Behavioral authority: prompt-level advice injected into later tasks, with role-specific projection available when enabled.

**Chroma and LLM ranking path.** Storage substrate: Chroma collection files under `persist_dir`. Representational form: parametric embeddings over task names plus symbolic metadata filters for success/failure labels. Lineage: regenerated or extended from inserted task records. Behavioral authority: ranking, because it determines which prior tasks seed graph expansion, example recall, insight lookup, and LLM relevance reranking.

There is no implemented promotion path from a retrieved task or insight into a governed rule, validator, hard constraint, or reviewed artifact. The closest promotion mechanism is salience within the same insight layer: scores and positive correlations make a rule more likely to survive and be returned.

## Comparison with Our System

| Dimension | G-Memory | Commonplace |
|---|---|---|
| Primary purpose | Experimental MAS memory for benchmark task solving | Git-native methodology KB with typed artifacts, validation, review, and generated indexes |
| Main retained artifact | Reward-labeled task trajectories, task graph, and insight rules | Typed Markdown notes, instructions, ADRs, reviews, sources, reports, and indexes |
| Write behavior | Automatic trace capture, LLM key-step/failure extraction, rule synthesis/editing/merge, reward score updates | Human/agent-authored artifacts with source grounding, validation, review, and replacement history |
| Retrieval | Chroma similarity, task-graph expansion, LLM reranking, insight correlation lookup | `rg`, authored links/indexes, collection contracts, review reports, and command workflows |
| Activation | Orchestrator pushes retrieved examples and rules into agent prompts | Mostly pull through search/links/skills, with explicit instructions and review workflows shaping load decisions |
| Governance | Reward labels, scores, logs, and regex parsing | Collection contracts, schemas, deterministic validation, semantic review, and git history |

G-Memory is much more automatic than Commonplace. It treats completed executions as training material and makes a running memory system update itself while experiments proceed. Commonplace instead keeps durable library artifacts inspectable, typed, and reviewed, and treats synthesis as a workflow with explicit lineage and validation. The tradeoff is clear: G-Memory can adapt quickly from repeated trials, but its learned rules are not source-reviewable at the same standard as a Commonplace note.

The strongest overlap is the idea that retained memory should be structured enough to route context, not merely stored as text. G-Memory uses task graph neighborhoods, success/failure labels, correlations, and top-k controls to reduce what enters the prompt. Commonplace uses collection contracts, indexes, links, and validation. Both are context-engineering systems, but G-Memory's context is optimized for immediate benchmark action, while Commonplace's is optimized for durable reuse and auditability.

### Borrowable Ideas

**Keep trace capture separate from distilled guidance.** A Commonplace analogue would retain raw task traces in a workshop or report layer, then derive reviewed notes or instructions from them. Ready now as a workflow pattern, but not as automatic library mutation.

**Use reward-labeled failures as first-class evidence.** G-Memory stores failed runs and asks for failure reasons, then uses them in comparative rule generation. Commonplace could borrow this for review gates or workflow retrospectives where failures are currently too easy to discard. Needs a concrete recurring evaluation loop.

**Let graph neighborhoods expand retrieval after a lexical or embedding hit.** The task graph shows a simple two-stage route: find similar tasks, then include local neighbors. Commonplace could use authored links or generated related-note indexes similarly, but only with visible lineage and reviewable ranking.

**Do not borrow unreviewed rule authority.** G-Memory's LLM-generated rules can be edited and scored automatically, then injected into future prompts. In Commonplace, that should remain a suggestion or derived report until accepted by a human/agent review workflow and validated as an instruction artifact.

## Write side

**Write agency:** `automatic` - The MAS workflows automatically record task traces, save completed task contexts, add Chroma documents, update the task graph, extract key steps/failure reasons, synthesize or edit insight rules, merge rules, and adjust insight scores from later rewards.

**Curation operations:** `consolidate` `dedup` `evolve` `synthesize` `promote` - `merge_insights()` consolidates clustered rule sets; `_merge_rules()` explicitly removes redundancy and combines similar rules; `_update_rules()` can edit existing rule text and correlations; LLM prompts can add new general rules from trajectory sets; `AGREE`, positive correlations, and `backward()` score increases promote rule salience. The code does not implement true invalidation with retained history or age/capacity decay.

### Trace-derived learning

**Trace source:** `trajectories` - The raw signal is each completed MAS task: agent messages, action/observation steps, reward-bearing state transitions, final feedback, and success/failure label.

**Extraction:** G-Memory filters negative-reward states, stores cleaned trajectories, extracts key steps for successful tasks, detects failure reasons for failed tasks, and periodically builds or edits insight rules from successful/failure trajectory groups using LLM prompts. The oracle is a mix of environment reward/final feedback, Chroma/graph retrieval, random task sampling, and LLM judgments.

**Learning scope:** `cross-task` - Task records, graph edges, and insight rules accumulate across benchmark tasks under `.db/{model}/{task}/{mas_type}/g-memory`.

**Learning timing:** `staged` - Raw task records are written after each task; insight finetuning starts after a threshold and repeats every configured number of rounds, while rule merging runs every 20 stored tasks.

**Distilled form:** `prose` `symbolic` - Distilled outputs are prose key steps, failure reasons, and insight rules, plus symbolic scores and positive/negative task correlations.

G-Memory supports the trace-derived survey claim that many systems split memory into raw episodes and distilled rules, but it also shows the governance gap: the distilled rules immediately shape future prompts without a separate review or validation tier.

## Read-back

**Read-back:** `push` - In the wired AutoGen, DyLAN, and MacNet loops, the orchestrator retrieves memory before agent calls and inserts successful examples and insights into the prompt; agents do not initiate their own memory search.

**Read-back signal:** `inferred / embedding` `inferred / judgment` - Selection starts from the current task text using Chroma similarity and task-graph expansion, then uses LLM relevance scoring for successful examples and correlation counting for related insight rules.

**Faithfulness tested:** `no` - The repository wires memory into prompts and runs benchmark tasks, but the memory module does not test whether a specific fired example or insight changed the agent's behavior through ablation, perturbation, or post-action audit.

The injection point is pre-invocation prompt assembly inside each MAS schedule. `format_task_prompt_with_insights()` creates prompt sections for static few-shots, past successful executions, and key insights; role projection can further rewrite general insights for each agent profile when `--use_projector` is enabled and the memory is an instance of `GMemory` ([tasks/mas_workflow/format.py](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/tasks/mas_workflow/format.py), [tasks/mas_workflow/autogen/autogen.py](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/tasks/mas_workflow/autogen/autogen.py)). Actual precision, recall, context dilution, and agent compliance are not readable from static code.

## Curiosity Pass

**The "Interaction Graph" is mostly serialized trace state, not a retrieval graph.** `StateChain` stores a sequence of NetworkX directed graphs for messages within each task, but cross-task retrieval mainly uses Chroma, task-name graph expansion, and insight correlations. That still preserves interaction structure, but it is not used as deeply as the README diagram might suggest.

**The task graph adds neighborhood expansion after embedding search.** `retrieve_related_task()` first asks Chroma for top similar task names, then expands by k-hop NetworkX neighbors. This can improve recall around related tasks, but it can also pull in indirect neighbors without a token budget or semantic explanation for why each neighbor matters.

**`backward()` applies only to cached insights.** G-Memory caches insights returned during retrieval and later adjusts their scores after task feedback. That creates a simple outcome feedback loop, but it does not know which insight, if any, the agent actually followed.

**Rule removal is not durable invalidation.** `REMOVE` lowers score and records negative correlations; `clear_insights()` deletes rules whose score falls below or equal to zero. Once deleted, the rule's history is not retained except in logs, so this is not truth maintenance in the Commonplace sense.

**The implementation is benchmark-shaped.** The CLI builds a working directory from model, task, MAS type, and memory type, and the available memory choices include several baselines. This is a research harness with persistent experiment memory, not a general user-facing memory product.

## What to Watch

- Whether future code uses the serialized interaction graphs for retrieval or insight generation. That would make the "interaction graph" more than retained trace metadata.
- Whether insight rules gain provenance pointers to exact tasks, quotes, or state ids. That would make automatic synthesis much easier to audit.
- Whether the benchmark harness adds WITH/WITHOUT memory ablations at the fired-memory level. That would change the faithfulness verdict.
- Whether deleted or contradicted rules are retained as inactive history. That would turn score-based pruning into actual invalidation.
- Whether the role projector is used consistently across MAS types and tasks. Stable projection would make G-Memory more clearly multi-agent-specific rather than a shared rule list injected into each role.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: G-Memory does activate retained memory, but through an orchestrator push rather than agent-initiated lookup.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: G-Memory separates task traces, task graph, Chroma ranking state, and insight rules across substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: retrieved successful trajectories and insight rules primarily advise later actions as prompt context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: retrieval ranking, graph routing, prompt templates, and insight update code shape which memories affect future agents.
- [Context engineering](../../notes/definitions/context-engineering.md) - frames: G-Memory is primarily a task-context selection and injection mechanism for bounded MAS prompts.
- [Agent memory needs discoverable, composable, trusted knowledge under bounded context](../../notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md) - compares: G-Memory is strong on trace-derived discovery and prompt delivery, weaker on reviewable trust and durable governance.
