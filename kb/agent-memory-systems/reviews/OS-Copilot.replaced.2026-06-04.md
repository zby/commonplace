---
description: "OS-Copilot review: FRIDAY planner/executor with self-learning that promotes judged Python code into Chroma-retrieved reusable tools"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: []
status: outdated
last-checked: "2026-06-02"
---

# OS-Copilot

> Replaced 2026-06-04. See [OS-Copilot](./OS-Copilot.md) for the current review.

OS-Copilot is the OS-Copilot team's open-source framework for building generalist computer agents over files, terminals, web/API tools, and desktop applications. At the reviewed commit its main memory-relevant system is FRIDAY: an agent that plans tasks, retrieves reusable tool descriptions and code, generates and executes new code, judges the outcome, and can promote successful Python code into a generated-tool repository for later retrieval.

**Repository:** https://github.com/OS-Copilot/OS-Copilot

**Reviewed commit:** [f720af8807e49a92dda64572d2c6bc6c0ac7ee7e](https://github.com/OS-Copilot/OS-Copilot/commit/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e)

**Last checked:** 2026-06-02

## Core Ideas

**FRIDAY is a plan-retrieve-generate-execute-judge loop.** `FridayAgent` wires `FridayPlanner`, `FridayRetriever`, `FridayExecutor`, and `ToolManager`; a task is decomposed into typed subtasks, each subtask is executed, and the result is judged for completion, repair, or replanning ([agent](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/agents/friday_agent.py), [planner](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/planner/friday_planner.py), [executor](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/executor/friday_executor.py)). Memory is therefore not a note store bolted onto a chat agent; it is a tool repertoire used by the planner and executor.

**Successful generated Python code can become a reusable tool.** During self-refinement, Python subtasks judged `Complete` with score at least `config.score` are passed to `executor.store_tool()`; the default threshold is 8 ([agent](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/agents/friday_agent.py), [config](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/utils/config.py)). `store_tool()` extracts a tool description from the generated code and calls `ToolManager.add_new_tool()`, which writes `generated_tools.json`, `tool_code/<name>.py`, `tool_description/<name>.txt`, and a Chroma vector entry ([executor](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/executor/friday_executor.py), [tool manager](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/tool_repository/manager/tool_manager.py)). That is the central durable memory mechanism.

**Retrieved tool descriptions shape planning; retrieved tool code shapes generation.** Before task decomposition, `FridayAgent.planning()` asks the retriever for similar tool names and descriptions, then passes the description pair into the planning prompt as `Tool List` ([agent](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/agents/friday_agent.py), [planning prompt](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/prompts/friday_pt.py)). For Python subtasks, execution retrieves the top three similar tools by subtask description and injects their source code into the code-generation prompt as `Relevant Code` ([agent](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/agents/friday_agent.py), [executor prompt](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/prompts/friday_pt.py)). Read-back is automatic inside the agent loop, not a manual lookup command.

**Self-learning designs curricula, then learns through ordinary task execution.** `SelfLearner.design_course()` asks an LLM to produce JSON lessons for a software/package pair, optionally using demo-file content and prior course JSON; `SelfLearning.learn_course()` then calls `agent.run(lesson)` for each lesson ([self-learning agent](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/agents/self_learning.py), [learner](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/learner/self_learner.py), [course script](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/course_learning.py)). The course file is retained lesson state, but executable authority is acquired only when lessons run, generate code, are judged, and pass the storage threshold.

**Context efficiency comes from top-k retrieval and task decomposition, not bounded knowledge governance.** Chroma similarity search caps retrieved tool names at `k`, planning defaults to 10 retrieved tools, Python execution retrieves 3 relevant code snippets, and prompts pass prerequisite task outputs instead of the whole run history ([retriever](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/retriever/vector_retriever.py), [tool manager](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/tool_repository/manager/tool_manager.py), [planner](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/planner/friday_planner.py)). There is no source-preserving review surface for generated tools beyond local files, JSON, and embeddings.

**The raw execution state is short-lived evidence unless promoted.** `EnvState` records command, result, error, pwd, and directory listing, and `ExecutionState` carries code, node type, description, result, and relevant code during the step ([schema](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/utils/schema.py)). Those states guide judging, repairing, replanning, and planner updates, but the durable behavior-shaping product is the generated tool repository, not the transient execution object.

## Artifact analysis

- **Storage substrate:** `vector` — `oscopilot/tool_repository/generated_tools/generated_tools.json`, `tool_code/*.py`, `tool_description/*.txt`, and the Chroma database under `generated_tools/vectordb`
- **Representational form:** `prose` `symbolic` `parametric` — prose tool descriptions, symbolic Python code and JSON metadata, and distributed-parametric embeddings over descriptions
- **Lineage:** `authored` `imported` `trace-extracted` — authored prompts/configuration, manual tool imports, and trace-derived generated tools from executed and judged Python subtasks
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — tools can be inspected as knowledge; prompts instruct; score thresholds gate promotion; retrieval routes and ranks; judges validate; successful traces become reusable tools

**Generated tools.** Storage substrate: `oscopilot/tool_repository/generated_tools/generated_tools.json`, `tool_code/*.py`, `tool_description/*.txt`, and the Chroma database under `generated_tools/vectordb`. Representational form: mixed symbolic/prose/code state: Python source code, JSON metadata, prose descriptions, and distributed-parametric embeddings over descriptions. Lineage: trace-derived from an executed Python subtask after LLM generation, environment execution, LLM judging, optional repair, and a score threshold; manual imports can also add tools through `tool_manager.py --add`. Behavioral authority: system-definition artifact when retrieved descriptions enter planning and retrieved code enters future generation prompts; knowledge artifact when merely listed or inspected as a library entry.

**Tool-description embeddings and Chroma retrieval index.** Storage substrate: local Chroma persistent directory. Representational form: distributed-parametric vectors plus metadata ids. Lineage: derived view over tool descriptions; regenerated or updated when `ToolManager.add_new_tool()` or deletion changes the tool set. Behavioral authority: ranking and routing authority, because similarity search selects which tool names, descriptions, and code can influence later planning and execution. The code asserts that Chroma's collection count matches `generated_tools.json`, but it does not audit semantic quality.

**Planner graph and action nodes.** Storage substrate: in-memory `tool_node`, `tool_graph`, and `sub_task_list` on `FridayPlanner`. Representational form: symbolic DAG with prose task descriptions, dependency lists, task type labels, return values, relevant code, next-action maps, and status flags. Lineage: LLM-derived from the user task, working-directory listing, API list, and retrieved tool descriptions; replanning derives new nodes from judge critique. Behavioral authority: execution-routing system-definition artifact for the current run, but not durable memory unless its subtasks later produce stored tools.

**Execution and judgment state.** Storage substrate: runtime `EnvState`, `ExecutionState`, `JudgementResult`, logs, and environment outputs. Representational form: mixed structured state plus prose/code/error text. Lineage: raw trace from generated code execution and judge prompts. Behavioral authority: evidence for repair, replanning, planner updates, and tool promotion. It is not durable behavior-shaping memory by itself; it becomes a promotion source when the judge returns `Complete` with sufficient score.

**Self-learning courses.** Storage substrate: JSON files under a root-level `courses` directory created by `SelfLearning._initialize_learning()`. Representational form: prose lesson descriptions keyed by symbolic lesson names. Lineage: LLM-derived from software name, package name, optional demo-file content, and prior-course JSON. Behavioral authority: curriculum advice and task source for `SelfLearning.learn_course()`. Course lessons do not directly alter FRIDAY's future behavior; they have to be executed through the agent and promoted into tools.

**Prompts and configuration.** Storage substrate: repository Python prompt dictionaries and command-line configuration. Representational form: prose instructions with symbolic placeholders and thresholds. Lineage: authored system-definition artifacts. Behavioral authority: high: prompts define task decomposition, code generation, judging, repair, retrieval filtering, and course design; config decides generated-tool repo location, working directory, repair iterations, and score threshold.

Promotion path: OS-Copilot has a concrete trace-to-tool ladder. A lesson or user task becomes an LLM-planned Python subtask; the executor generates code and invocation; the environment runs it; the judge evaluates completion and generality; high-scoring successful code is saved as reusable source/description/JSON and embedded in Chroma; future task/subtask text retrieves that retained tool state back into planning and code generation. The path promotes raw trace evidence into symbolic executable authority plus a distributed-parametric read-back index.

## Comparison with Our System

| Dimension | OS-Copilot / FRIDAY | Commonplace |
|---|---|---|
| Primary purpose | OS automation agent with generated executable tool memory | Git-native methodology KB for agent-operated knowledge systems |
| Canonical artifacts | Generated Python tools, descriptions, Chroma embeddings, planner DAGs, courses, prompts | Typed Markdown notes, reviews, instructions, ADRs, source snapshots, indexes, validation reports |
| Learning loop | Execute/judge code, then store high-scoring Python as reusable tools | Snapshot, write, connect, validate, review, and promote knowledge artifacts |
| Read-back | Automatic vector retrieval before planning and Python generation | Mostly deliberate pull through `rg`, indexes, links, skills, and review gates |
| Governance | LLM judge score, execution output, repair loop, Chroma count assertion | Git diffs, type contracts, schemas, validation, semantic gates, source citations |

The overlap with Commonplace is not "memory" as broad storage. It is promotion: both systems care about moving something from a transient work episode into retained future behavior. OS-Copilot's promotion target is executable code with strong operational authority; Commonplace's promotion target is usually prose or symbolic methodology with reviewable lineage.

FRIDAY is more operationally aggressive. It lets a successful task trace become a reusable tool in the same runtime loop, then uses vector retrieval to push that tool back into future planning and generation. Commonplace is slower but more inspectable: artifacts carry type contracts, citations, links, validation, and replacement history before they become trusted context.

The design tradeoff is authority without review. A generated Python tool can affect future task decomposition and code generation after one LLM judgment and a score threshold. That is powerful for learning APIs like `openpyxl`; it is risky for durable system behavior because the source does not preserve the full lesson, execution trace, judge rationale, repair history, or reviewer decision alongside the stored code.

**Read-back:** `push` — With engineered push activation. Tool descriptions are automatically retrieved from task text before planning, and tool code is automatically retrieved from Python subtask descriptions before code generation; manual add/delete commands manage the repository but are not agent read-back.

### Borrowable Ideas

**Make promotion targets executable when the task is operational.** Ready only with a narrow use case. Commonplace should not convert methodology notes into executable tools by default, but workshop workflows could promote repeated maintenance routines into scripts after validation and review.

**Store reusable code and retrieval descriptors together.** Ready now for generated utilities. FRIDAY's code/description/embedding split suggests that every Commonplace script-like artifact should have an explicit retrieval description, not only a filename.

**Use a score threshold as a queue signal, not as final authority.** Ready now. A Commonplace analogue would let execution/judge scores nominate artifacts for review while preserving human/agent review gates before the artifact becomes instruction, validator, or default route.

**Inject prior successful code before generating new code.** Needs a bounded workshop. For repetitive local tooling tasks, retrieved examples could be pushed into a code-generation prompt, but the retrieved code should cite its source, test status, and scope.

**Separate course design from artifact promotion.** Ready conceptually. FRIDAY's courses are useful as exploration scaffolds, not final memory. Commonplace workshops can use curricula or task lists to drive exploration while promoting only the durable artifacts that survive review.

**Do not borrow unsupervised generated-tool authority wholesale.** The missing piece for Commonplace is provenance: a generated tool should retain the triggering task, source traces, judge/rater output, tests, and invalidation conditions before it becomes reusable infrastructure.

## Write side

**Write agency:** `automatic` `manual` — successful Python subtasks can be stored automatically as reusable tools after execution and judge scoring, while manual add/delete commands maintain the tool repository.

**Curation operations:** `synthesize` `promote` — execution traces are synthesized into reusable Python tools with descriptions and embeddings, and the judge score threshold promotes completed subtasks into the retained tool repository.

### Trace-derived learning

**Trace source:** `tool-traces` `trajectories` — generated code, invocations, environment outputs/errors, judge critiques, repairs, and self-learning lesson runs are execution traces rather than passive logs.

**Learning scope:** `per-task` `per-project` `cross-task` — individual Python subtasks can promote tools, the repository/tool-repository bounds storage, and retained tools are reused across later tasks.

**Learning timing:** `online` `staged` — ordinary execution can store a successful tool immediately, while self-learning runs staged lessons and continuous course cycles.

**Distilled form:** `prose` `symbolic` `parametric` — stored tool descriptions, Python/JSON tool records, and Chroma embeddings over descriptions.

**Trace source.** OS-Copilot qualifies as trace-derived. The raw signals are generated Python code, invocation strings, environment outputs, errors, current working directory, directory listing, task descriptions, next-action dependencies, judge critiques, repair results, and self-learning lesson runs.

**Extraction.** Extraction is LLM-mediated. The executor generates code and invocation from the subtask, prerequisite outputs, and retrieved relevant code. The environment executes it. The judge prompt evaluates task completion and code generality, returning `Complete`, `Amend`, or `Replan` plus a numeric score. Only Python tasks that complete and meet the configured score threshold are stored as reusable tools.

**Four fields.** The raw stage is runtime execution/judgment state: mixed code/prose/symbolic evidence with temporary authority over repair and replanning. The distilled stage is generated-tool state: Python code, descriptions, JSON records, and embeddings with lineage from an executed and judged task trace. The stored code and descriptions gain system-definition authority when retrieved into future planning and generation; embeddings gain ranking authority over that activation.

**Scope and timing.** Scope is repository-local and generated-tool-repository-local. Ordinary task execution can promote one successful Python subtask immediately; self-learning runs a sequence of lessons and can accumulate tools over that course. Continuous learning loops indefinitely, repeatedly designing new lessons from the latest retained course JSON and running them through the same promotion path.

**Survey placement.** OS-Copilot is a trace-to-tool system rather than a trace-to-note system. It strengthens the survey claim that trace-derived learning becomes behaviorally important at the promotion boundary: execution traces matter because judged code is converted into durable executable tools plus a retrieval index, not because raw logs are replayed.

## Read-back

**Direction.** OS-Copilot is push-only for memory read-back. Tool management has manual add/delete surfaces for repository maintenance, but I did not find a deployed agent-facing lookup command; FRIDAY pushes retrieved tool descriptions and source code into future model calls automatically from task/subtask text.

**Read-back signal:** `inferred / embedding` — Chroma similarity selects generated tools by comparing current task or subtask descriptions to retained tool descriptions.

**Faithfulness tested:** `no` — the review found structural tests and tutorial claims but no standing with/without memory ablation or post-action audit for read-back behavior.

**Targeting and signal.** Targeting is `instance`: planning calls `retrieve_tool_name(task, k=10)` and then retrieves descriptions for the selected names, while Python execution calls `retrieve_tool_name(description, 3)` and retrieves code for those names. The signal is `inferred / embedding`, because Chroma similarity selects generated tools by comparing the current task or subtask description to retained tool descriptions; precision and recall are not verified by code.

**Injection point.** Retrieval happens before task decomposition and before Python code generation. It can change the next plan or generated code before the agent acts. Repair and replanning happen after execution and can only affect later attempts or subtasks.

**Selection, scope, and complexity.** Selection is top-k by vector similarity. Planning receives up to 10 tool descriptions; Python generation receives up to 3 code snippets. Complexity is controlled by retrieval counts and subtask dependency summaries, but retrieved code can still be large, and the system does not enforce token budgets or provenance-aware filtering.

**Authority at consumption.** Retrieved descriptions are advisory context for the planner, but because the planner may reuse tool names when descriptions match, they carry routing force. Retrieved code is advisory context to the code generator; the prompt explicitly instructs reuse when relevant code directly addresses the task, giving it stronger template authority than ordinary background knowledge.

**Faithfulness.** I found structural tests and docs for the loop, but no with/without memory ablation or post-action audit proving that retrieved tools improve behavior in the general case. The self-learning tutorial reports a before/after task story, but source code does not implement a standing faithfulness test for read-back.

**Other consumers.** Human operators can add and delete tools through `tool_manager.py`, inspect generated JSON/code/description files, and run course learning. Chroma itself is consumed by FRIDAY rather than directly by users.

## Curiosity Pass

**The memory is executable before it is explainable.** The retained code is stored with a short extracted description, but the repository does not persist the full trace, judge rationale, or repair history next to the tool. That makes later behavior hard to audit.

**Self-learning is curriculum-driven rather than log-mining.** FRIDAY does not mine arbitrary past conversations for lessons. It asks an LLM to create lessons, runs them, and stores high-scoring successful code. That is a staged learning loop, not passive reflection over logs.

**The current generated-tool repository is empty at checkout.** `generated_tools.json` is `{}` and only package marker files exist under generated tool code/description directories. The mechanism is implemented, but the reviewed checkout does not ship a populated learned-tool library.

**Chroma is synchronization-sensitive.** `ToolManager.__init__()` asserts that Chroma's collection count equals the JSON tool count. That catches one class of drift, but it also means local generated-tool state can make startup fail if files and vector state diverge.

**The planner can reuse old names as future task names.** The planning prompt tells the model to use an existing tool's name when a subtask corresponds to a retrieved description. This makes descriptions part of the routing contract, not just documentation.

## What to Watch

- Whether generated tools start retaining source task, execution state, judge JSON, repair attempts, and score metadata alongside code; that would make trace-derived authority auditable.
- Whether self-learning adds a review or quarantine stage before promoted tools are available to ordinary task execution.
- Whether Chroma retrieval gets provenance, recency, package/domain scoping, or token budgets beyond top-k similarity.
- Whether generated Shell or AppleScript actions ever become durable tools; at the reviewed commit only successful high-scoring Python subtasks are stored.
- Whether future tests measure behavior with and without retrieved tools, not just that generation, planning, and course design return non-empty outputs.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: OS-Copilot turns executed and judged task traces into reusable generated tools.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: FRIDAY's Chroma store matters because the agent loop activates it before planning and generation.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: generated code, descriptions, embeddings, planner nodes, and courses carry different forms and authorities.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: courses and execution traces are evidence or task sources until promoted.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: prompts, generated tools, retrieval indexes, and planner graphs configure future behavior.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: FRIDAY extracts reusable behavior from task traces after execution and judging.
