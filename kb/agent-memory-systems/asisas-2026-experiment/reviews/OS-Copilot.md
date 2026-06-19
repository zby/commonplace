---
description: "OS-Copilot review: FRIDAY promotes judged Python execution traces into Chroma-retrieved reusable tools for later planning and codegen"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
status: current
last-checked: "2026-06-04"
---

# OS-Copilot

OS-Copilot is the OS-Copilot team's open-source framework for building generalist computer agents over files, terminals, web/API tools, and desktop applications. At the reviewed commit, its memory-relevant subsystem is FRIDAY: a planner/retriever/executor loop that can turn successful Python task traces into reusable tool code, tool descriptions, JSON metadata, and a Chroma retrieval index.

**Repository:** https://github.com/OS-Copilot/OS-Copilot

**Reviewed commit:** [f720af8807e49a92dda64572d2c6bc6c0ac7ee7e](https://github.com/OS-Copilot/OS-Copilot/commit/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e)

**Last checked:** 2026-06-04

## Core Ideas

**FRIDAY is a plan-retrieve-generate-execute-judge loop.** `FridayAgent` wires a planner, retriever, executor, and tool manager; it decomposes a task, executes typed subtasks, judges code results, repairs or replans when needed, and updates the planner with subtask results ([agent](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/agents/friday_agent.py), [planner](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/planner/friday_planner.py), [executor](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/executor/friday_executor.py)). Memory is therefore a tool repertoire inside the action loop, not a separate note store.

**Successful Python execution traces can become reusable tools.** In `self_refining()`, Python subtasks judged complete with score at least `config.score` call `executor.store_tool()`; the default threshold is 8 ([agent](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/agents/friday_agent.py), [config](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/utils/config.py)). `store_tool()` extracts a description from the generated code and hands name/code/description to `ToolManager.add_new_tool()`, which writes JSON, code, description files, and a Chroma vector entry ([executor](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/executor/friday_executor.py), [tool manager](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/tool_repository/manager/tool_manager.py)).

**Retrieved tool descriptions shape planning; retrieved tool code shapes generation.** Before task decomposition, `planning()` retrieves similar tool names from the task and passes their descriptions into the planning prompt as `Tool List`. Before Python generation, `executing()` retrieves up to three tools from the subtask description and passes their source as `Relevant Code` to the code-generation prompt ([agent](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/agents/friday_agent.py), [retriever](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/retriever/vector_retriever.py), [prompts](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/prompts/friday_pt.py)).

**Context efficiency is top-k retrieval plus decomposition.** Planning caps retrieved tool descriptions at 10 by default; Python execution retrieves 3 relevant code snippets; subtasks receive prerequisite outputs rather than the whole execution history ([tool manager](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/tool_repository/manager/tool_manager.py), [planner](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/planner/friday_planner.py), [executor](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/executor/friday_executor.py)). The budget is count-based rather than provenance-aware; retrieved code can still be large, and the implementation does not preserve a full audit packet beside promoted tools.

**Self-learning uses curricula to feed the same promotion path.** `SelfLearner` can design lesson JSON for a software/package pair, and `SelfLearning.learn_course()` runs each lesson through `agent.run()` ([self-learning agent](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/agents/self_learning.py), [learner](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/learner/self_learner.py), [course script](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/course_learning.py)). Course files are retained task scaffolds; behavioral authority is gained only if lesson execution produces a high-scoring stored Python tool.

## Artifact analysis

- **Storage substrate:** `files` `vector` `in-memory` — generated tools persist in `generated_tools.json`, `tool_code/*.py`, `tool_description/*.txt`, and a Chroma persistent directory; planner nodes and execution state are runtime structures ([tool manager](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/tool_repository/manager/tool_manager.py), [schema](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/utils/schema.py)).
- **Representational form:** `prose` `symbolic` `parametric` — retained tool descriptions are prose, generated Python and JSON metadata are symbolic, and Chroma embeddings are distributed-parametric views over descriptions.
- **Lineage:** `authored` `imported` `trace-extracted` — prompts, config, and baseline APIs are authored or imported; generated tools are extracted from LLM-generated code, environment execution state, judge critique, repairs, and self-learning lesson runs.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — stored tool files can be inspected as knowledge, prompts instruct generation and planning, score thresholds gate promotion, Chroma ranks and routes retrieved tools, judge prompts validate completion, and successful traces become learned reusable actions.

**Generated tools.** The durable behavior-shaping artifact is the generated-tool repository: JSON metadata, Python code, description text, and embeddings. It has trace lineage when created by a successful task run, and system-definition authority when descriptions enter planning or code enters later generation.

**Tool-description embeddings.** The Chroma collection is a derived access structure over tool descriptions. It has ranking and routing authority because similarity search decides which retained tools can enter the next prompt, but the code only asserts count synchronization with `generated_tools.json`; it does not audit semantic quality.

**Planner graph and execution state.** `FridayPlanner` keeps in-memory action nodes, dependencies, status, return values, and relevant-code fields. `ExecutionState` carries code, result, node type, description, and relevant code for judging and repair. These are current-run system-definition artifacts; they become durable memory only through the generated-tool promotion path.

**Self-learning courses.** Course JSON is LLM-designed lesson state used to drive future agent runs. It is a knowledge artifact and task source, not directly a memory injection surface, because lessons still need to execute and pass the promotion threshold before they change ordinary FRIDAY behavior.

Promotion path: a user task or lesson becomes a planned Python subtask; the executor generates code and invocation; the environment runs it; the judge evaluates completion and score; successful high-scoring Python code is saved with a description and embedded in Chroma; later task text retrieves that retained tool state before planning or Python code generation.

## Comparison with Our System

| Dimension | OS-Copilot / FRIDAY | Commonplace |
|---|---|---|
| Primary purpose | OS automation agent with reusable generated-tool memory | Git-native methodology KB for agent-operated knowledge systems |
| Canonical artifacts | Python tools, tool descriptions, JSON metadata, Chroma embeddings, planner DAGs, course JSON | Typed Markdown notes, reviews, instructions, ADRs, source snapshots, indexes, validation reports |
| Learning loop | Execute, judge, and store high-scoring generated code | Snapshot, write, connect, validate, review, and promote knowledge artifacts |
| Read-back | Automatic vector retrieval before planning and Python generation | Mostly deliberate pull through `rg`, indexes, links, skills, and review gates |
| Governance | LLM judge score, execution output, repair loop, Chroma count assertion | Git diffs, type contracts, schemas, validation, semantic gates, source citations |

The overlap with Commonplace is promotion: both systems move selected work products from a transient episode into retained future behavior. OS-Copilot's promotion target is executable code with strong operational authority; Commonplace's usual promotion target is reviewable prose or symbolic methodology.

FRIDAY is more operationally aggressive. A single successful, high-scoring Python subtask can become reusable code and then re-enter later prompts by vector similarity. Commonplace is slower but preserves richer provenance, replacement history, validation, and review state before artifacts become trusted context.

The design tradeoff is authority without audit depth. OS-Copilot persists code and a short description, but not the full lesson, execution trace, judge rationale, repair sequence, score history, or reviewer decision beside the promoted tool.

### Borrowable Ideas

**Make promotion targets executable when the task is operational.** Ready only for narrow workshops. Commonplace should not turn methodology notes into tools by default, but repeated maintenance routines can graduate into scripts after validation and review.

**Store reusable code and retrieval descriptors together.** Ready now for generated utilities. FRIDAY's code/description/embedding split is a useful reminder that every reusable script should have an explicit retrieval description, not only a filename.

**Use score thresholds as queue signals.** Ready now. A Commonplace analogue would let execution or judge scores nominate artifacts for review while preserving human/agent review gates before the artifact becomes instruction, validator, or default route.

**Inject prior successful code before generating new code.** Needs a bounded workshop. Retrieved examples can help repetitive local tooling tasks, but each pushed example should carry source, test status, and scope.

**Separate curriculum design from artifact promotion.** Ready conceptually. Course plans are useful exploration scaffolds; only the durable outputs that survive execution, validation, and review should become retained behavior.

## Write side

**Write agency:** `automatic` `manual` — FRIDAY can automatically store successful generated Python tools after execution and judge scoring; operators can also add or delete tools with `tool_manager.py`.

**Curation operations:** `promote` — a judged Python execution trace crosses from current-run code into retained reusable-tool memory only when the completion status and score threshold permit it.

### Trace-derived learning

**Trace source:** `tool-traces` `trajectories` — raw signal comes from generated code, invocations, environment outputs/errors, current working directory, directory listings, prerequisite outputs, judge critiques, repairs, replanning, and self-learning lesson runs.

**Learning scope:** `per-task` `per-project` `cross-task` — individual Python subtasks can promote tools, the generated-tool repository bounds storage, and retained tools are reused by later tasks.

**Learning timing:** `online` `staged` — ordinary task execution can promote a successful Python subtask immediately; self-learning runs staged lesson sequences through the same agent loop.

**Distilled form:** `prose` `symbolic` `parametric` — the retained output is a tool description, Python/JSON tool record, and embedding index.

Extraction is LLM-mediated and judge-gated. The executor generates Python code and an invocation, the environment executes it, the judge returns completion status and score, repair may rewrite the code, and only completed high-scoring Python subtasks are stored. The raw stage has temporary authority over repair and replanning; the distilled stage gains future planning and generation authority through retrieval.

Survey placement: OS-Copilot is a trace-to-tool system. It strengthens the survey pattern that trace-derived learning becomes behaviorally important at the promotion boundary: raw logs matter because judged code is converted into durable executable tools and a retrieval index, not because the raw transcript is replayed.

## Read-back

**Read-back:** `push` — FRIDAY automatically retrieves retained tools before planning and before Python code generation; I did not find an agent-facing memory lookup command that would make the agent deliberately pull the store.

**Read-back signal:** `inferred / embedding` — Chroma similarity selects tool names from current task or subtask descriptions by comparing them with stored tool descriptions.

**Faithfulness tested:** `no` — I found structural wiring, tutorials, and count synchronization, but no standing with/without memory ablation or post-action audit proving that pushed tool memory changes behavior correctly.

The push occurs at two pre-invocation points. Planning receives up to 10 retrieved tool descriptions as `Tool List`; Python execution receives up to 3 retrieved code snippets as `Relevant Code`. The code-generation prompt explicitly tells the model to reuse relevant code when it directly addresses the current task, so retrieved memory has stronger template authority than ordinary background context.

Selection is top-k embedding similarity, with no provenance-aware filter, token budget, precision measurement, or recall measurement in the inspected code. Scope is local to the configured generated-tool repository. Manual add/delete operations maintain the same store, but they do not change the read-back direction from the agent's perspective.

## Curiosity Pass

**The memory is executable before it is explainable.** Stored code gets a short extracted description, but the repository does not persist the full trace, judge rationale, repair history, or source lesson beside the tool.

**Self-learning is curriculum-driven rather than log-mining.** FRIDAY asks an LLM to design lessons and runs them; it does not mine arbitrary prior conversations for reusable behavior.

**The reviewed checkout does not ship a populated learned-tool library.** `generated_tools.json` is empty in the source tree, so the review is about the implemented mechanism rather than a large retained tool corpus.

**Chroma synchronization is brittle by assertion.** `ToolManager.__init__()` asserts that Chroma's collection count equals the JSON tool count. That catches one drift class but can make startup fail when local file and vector states diverge.

## What to Watch

- Whether generated tools start retaining source task, execution state, judge JSON, repair attempts, and score metadata alongside code.
- Whether self-learning adds a review or quarantine stage before promoted tools become available to ordinary task execution.
- Whether Chroma retrieval gets provenance, recency, package/domain scoping, or token budgets beyond top-k similarity.
- Whether future tests measure behavior with and without retrieved tools rather than only structural generation, planning, or course-design behavior.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../../trace-derived-learning-techniques-in-related-systems.md) - places: OS-Copilot turns executed and judged task traces into reusable generated tools.
- [Knowledge storage does not imply contextual activation](../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: FRIDAY's Chroma store matters because the agent loop activates it before planning and generation.
- [Axes of artifact analysis](../../../notes/axes-of-artifact-analysis.md) - applies: generated code, descriptions, embeddings, planner nodes, and courses carry different forms and authorities.
- [Knowledge artifact](../../../notes/definitions/knowledge-artifact.md) - classifies: course JSON and execution traces are evidence or task sources until promoted.
- [System-definition artifact](../../../notes/definitions/system-definition-artifact.md) - classifies: prompts, generated tools, retrieval indexes, and planner graphs configure future behavior.
- [Use trace-derived extraction](../../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: FRIDAY extracts reusable behavior from task traces after execution and judging.
