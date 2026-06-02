---
description: "OS-Copilot review: FRIDAY plans OS tasks, generates and repairs executable tools, scores them, and stores reusable Python tools in a vector-retrieved repository"
type: ../types/agent-memory-system-review.md
tags: []
status: outdated
last-checked: "2026-05-16"
---

# OS-Copilot

> Replaced 2026-06-02. See [OS-Copilot](./OS-Copilot.md) for the current review.

OS-Copilot is an open-source framework for generalist computer agents on operating-system tasks. The inspected repository implements FRIDAY, a single-round task agent that decomposes a user task into typed subtasks, retrieves existing tools, generates Python/Shell/AppleScript or API code, executes it in an environment, uses an LLM judge to decide whether to amend, replan, or complete, and stores high-scoring generated Python tools for later retrieval. Its memory system is therefore centered on reusable executable tools, not conversational recall.

**Repository:** https://github.com/OS-Copilot/OS-Copilot

**Reviewed commit:** [f720af8807e49a92dda64572d2c6bc6c0ac7ee7e](https://github.com/OS-Copilot/OS-Copilot/commit/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e)

**Last checked:** 2026-05-16

## Core Ideas

**FRIDAY treats tool use as the retained unit of improvement.** The README describes OS-Copilot as a library for agents that operate web, terminal, files, multimedia, and third-party applications, and notes that FRIDAY currently supports single-round conversation ([README.md](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/README.md)). In code, `FridayAgent` wires a planner, retriever, executor, and tool manager; each run resets the plan, decomposes the task, executes subtasks, judges or repairs failed tool executions, and may store a successful Python subtask as a reusable tool ([oscopilot/agents/friday_agent.py](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/agents/friday_agent.py)).

**The planner builds an action graph, not a memory graph.** `FridayPlanner` asks the LLM to decompose the user task into subtasks with `description`, `dependencies`, and `type`, then builds a DAG of `ActionNode`s and executes a topological sort over incomplete nodes ([oscopilot/modules/planner/friday_planner.py](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/planner/friday_planner.py), [oscopilot/tool_repository/manager/action_node.py](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/tool_repository/manager/action_node.py)). The plan is transient execution state. It can carry prerequisite return values and relevant code into later subtasks, but it is not persisted as a reusable lesson.

**Tool retrieval is vector search over descriptions plus direct lookup of code.** `FridayRetriever` asks the tool manager for related tool names, descriptions, and code, then feeds relevant code snippets into the executor when generating a Python tool ([oscopilot/modules/retriever/vector_retriever.py](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/retriever/vector_retriever.py)). `ToolManager` stores tool metadata in `generated_tools.json`, code files under `tool_code/`, description files under `tool_description/`, and a persistent Chroma collection under `vectordb/` using OpenAI or Ollama embeddings ([oscopilot/tool_repository/manager/tool_manager.py](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/tool_repository/manager/tool_manager.py), [oscopilot/tool_repository/generated_tools](https://github.com/OS-Copilot/OS-Copilot/tree/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/tool_repository/generated_tools)).

**Execution, judgment, repair, and replanning form the improvement loop.** `FridayExecutor` generates code and an invocation, executes it through the configured environment, asks an LLM judge to classify the outcome as `Complete`, `Amend`, or `Replan`, and can repair code using the previous code, error, output, current directory, working directory, file listing, critique, and prerequisite information ([oscopilot/modules/executor/friday_executor.py](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/executor/friday_executor.py)). `FridayAgent.self_refining(...)` uses those results to replan, amend, mark completion, and store high-scoring Python tools when `score >= config.score` ([oscopilot/agents/friday_agent.py](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/agents/friday_agent.py), [oscopilot/utils/config.py](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/utils/config.py)).

**Self-learning turns generated lessons into tool-acquisition tasks.** `SelfLearner` designs a JSON course from a software name, package name, demo file content, and prior course; `SelfLearning` stores course JSON under `courses/`, then runs each lesson through the same FRIDAY agent ([oscopilot/modules/learner/self_learner.py](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/learner/self_learner.py), [oscopilot/agents/self_learning.py](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/agents/self_learning.py), [course_learning.py](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/course_learning.py)). The self-learning tutorial frames this as enabling Excel/openpyxl operations after FRIDAY initially fails SheetCopilot tasks ([docs/source/tutorials/self_learning.rst](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/docs/source/tutorials/self_learning.rst)).

**The repository ships an empty generated-tool memory by default.** At the inspected commit, `generated_tools.json` is `{}` and the `tool_code/` and `tool_description/` directories contain only package scaffolding ([oscopilot/tool_repository/generated_tools/generated_tools.json](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/tool_repository/generated_tools/generated_tools.json), [oscopilot/tool_repository/generated_tools](https://github.com/OS-Copilot/OS-Copilot/tree/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/tool_repository/generated_tools)). The memory mechanism is implemented, but the checked-in repository does not include a populated public library of learned tools.

## Comparison with Our System

| Dimension | OS-Copilot / FRIDAY | Commonplace |
|---|---|---|
| Primary purpose | OS automation through generated and retrieved executable tools | Durable methodology KB for agent-operated knowledge systems |
| Main retained artifact | Reusable generated Python tools plus prose descriptions and vector embeddings | Typed Markdown notes, source snapshots, reviews, instructions, ADRs, indexes, and validation outputs |
| Storage substrate | Filesystem tool repository, `generated_tools.json`, Chroma vector store, course JSON, logs | Git-tracked Markdown, schemas, source snapshots, generated indexes, review outputs, scripts |
| Representational form | Symbolic executable code, prose descriptions/prompts/lessons, distributed-parametric embeddings | Typed prose and frontmatter, symbolic links/schemas/commands, generated indexes, validation code |
| Lineage | Execution state and judge critique feed repair and storage, but stored tools lack mandatory source trace IDs or review records | Source-pinned notes and reviews, authored citations, archive/replacement lifecycle, validation and review gates |
| Activation | Vector retrieval of tool descriptions injects tool names/descriptions/code into planning and generation | `rg`, indexes, descriptions, authored links, skills, instructions, validation and review workflows |
| Behavioral authority | Retrieved code can be reused or executed; stored tools become high-authority system-definition artifacts | Knowledge artifacts and system-definition artifacts are separated by type, instruction surface, validation, and review status |

OS-Copilot and commonplace agree that memory matters when it changes future work. FRIDAY's strongest contribution is a tight activation path: if a task resembles a stored tool description, Chroma retrieval can bring back the tool name, prose description, and executable code before code generation. That is stronger than passive storage.

The major difference is artifact governance. A FRIDAY tool combines several operative parts: a prose description used for retrieval, symbolic Python code used for execution, and a distributed-parametric embedding used for ranking. Once retrieved, the code has system-definition-artifact authority because it can be copied, adapted, or executed in the environment. Commonplace would require clearer source lineage, review state, tests, scope, and retirement policy before a generated artifact received that much authority.

FRIDAY's self-learning course files are also different from commonplace library notes. A course lesson is a generated task prompt that drives the agent to practice and possibly create tools; it is a system-definition artifact for the learning loop. It is not a stable knowledge artifact about the package unless separately reviewed, cited, and maintained.

**Read-back:** push — FRIDAY retrieves matching tools and injects descriptions and code during planning and generation.

## Trace-derived learning placement

**Trace source.** OS-Copilot qualifies as trace-derived learning. The qualifying trace is not a conversation transcript; it is the task execution trajectory around generated tools: task description, generated code, invocation, execution output, errors, current directory, file listing, prerequisite returns, LLM judge critique, repair attempts, replan reasoning, and final score. Some of this is transient in `ExecutionState`; some is logged through Python logging, but the implemented learning path consumes the live state and critique rather than later mining raw log files ([oscopilot/agents/friday_agent.py](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/agents/friday_agent.py), [oscopilot/modules/executor/friday_executor.py](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/executor/friday_executor.py), [oscopilot/utils/schema.py](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/utils/schema.py)).

**Extraction.** Extraction has two paths. During ordinary task execution, the LLM judge decides whether a generated tool is complete, amendable, or needs replanning, and assigns a generality score. If a Python tool completes and its score meets the configured threshold, FRIDAY extracts a description from the code docstring and stores the tool. During self-learning, an LLM first designs course lessons from package/software context, then FRIDAY runs those lessons; successful high-scoring Python lesson solutions can become tools ([oscopilot/modules/executor/friday_executor.py](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/executor/friday_executor.py), [oscopilot/modules/learner/self_learner.py](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/learner/self_learner.py), [oscopilot/agents/self_learning.py](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/agents/self_learning.py)).

**Storage substrate.** Raw execution traces mostly live in runtime objects and optional log files configured by `setup_config`; they are not a first-class replayable trace database. Distilled tools persist in the filesystem under `generated_tools.json`, `tool_code/`, `tool_description/`, and Chroma `vectordb/`. Course and lesson artifacts persist as JSON under `courses/`, with the continuous-learning loop updating in-memory course state and writing newly designed course JSON ([oscopilot/utils/config.py](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/utils/config.py), [oscopilot/tool_repository/manager/tool_manager.py](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/tool_repository/manager/tool_manager.py), [oscopilot/agents/self_learning.py](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/agents/self_learning.py)).

**Representational form.** Raw task descriptions, critiques, course lessons, and tool descriptions are prose. Action graphs, JSON tool metadata, Python code, shell code, API paths, thresholds, and environment commands are symbolic. Chroma embeddings are distributed-parametric retrieval state. The behavior-shaping artifact is mixed: prose descriptions are embedded and ranked, symbolic code is retrieved and executed, and JSON maps keep names, descriptions, and code synchronized.

**Lineage.** Lineage is strong inside one execution loop because the current code, output, error, critique, and prerequisite state are passed into repair and judgment prompts. It becomes weak after promotion: a stored tool has code and description, but not mandatory links to the originating task, execution output, judge reasoning, score, repair attempts, course lesson, package docs, prompt version, or environment snapshot. Course JSON records lesson text, but it is not a durable provenance record for any later stored tool.

**Behavioral authority.** Raw execution state is a knowledge artifact while it advises judge, repair, and replan decisions. Judge prompts and score thresholds have evaluation and promotion authority. Stored tools are system-definition artifacts once retrieved because their code can directly shape or perform later OS actions. Tool descriptions and embeddings have routing/ranking authority because they decide which tools become active for a task. Course lessons are system-definition artifacts for the self-learning loop because they instruct the agent what to practice.

**Scope.** The scope is project/local-agent level. A generated tool repository lives under the configured `generated_tool_repo_path`, and Chroma retrieval is local to that repository. It is not a shared, reviewed, cross-project package registry by default.

**Timing.** Tool generation, execution, repair, judging, and storage happen online during task runs. Course design can happen before or during continuous self-learning cycles, then lessons are executed online through the same agent. Retrieval happens at planning time and again before Python tool generation.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), OS-Copilot belongs on the trace-to-tool and trace-to-executable-artifact axis. It strengthens the survey distinction between raw traces and distilled artifacts: raw execution state is temporary evidence, while the durable behavior-changing artifact is a generated Python tool plus description plus embedding. It also splits "memory" into course artifacts, raw execution traces, vector retrieval state, and executable tool authority.

## Borrowable Ideas

**Use executable tools as promoted memory only after a score gate.** Worth borrowing for narrow workshop contexts. FRIDAY does not store every generated code snippet; it stores completed Python tools only when the judge's generality score clears a threshold. Commonplace could adapt this as a candidate-to-skill promotion gate, but would need tests and source lineage in addition to an LLM score.

**Retrieve code by description before generating new code.** Ready as an activation pattern. FRIDAY's tool repository makes reusable code visible at the point of generation rather than waiting for the agent to remember it. Commonplace skills and scripts could benefit from similarly explicit retrieval cues.

**Separate lesson generation from artifact promotion.** Useful for workshops. OS-Copilot's course lessons create practice tasks; successful practice can yield tools. Commonplace should keep that distinction: a generated exercise is not itself a library claim, but it can produce evidence for a later artifact.

**Do not borrow executable authority without governance.** FRIDAY's stored tools can become powerful quickly because retrieved code is executable. A commonplace analogue would need scoped permissions, tests, provenance, deprecation, and review before promoted code became an instruction-level surface.

## Takeaways

**OS-Copilot's memory is mostly a tool repository.** The durable behavior-changing substrate is generated Python code, descriptions, JSON metadata, and vector retrieval state.

**Trace-derived learning applies, but the trace is operational.** The system learns from generated-code execution, errors, repair critiques, completion judgments, and generality scores, not mainly from long conversational histories.

**Raw traces, courses, vectors, and tools have different authority.** Logs and execution state are evidence; course lessons instruct practice; embeddings rank tools; stored Python code can act directly in the environment.

**Activation is stronger than governance.** FRIDAY has a practical route from stored tools to future task execution, but it does not preserve enough lineage or validation metadata to make stored tools trustworthy outside the local run context.

**The checked-in memory starts empty.** The design supports self-improving tool accumulation, but the reviewed repository does not ship a populated library of learned tools.

## Curiosity Pass

The most interesting mechanism is the score threshold on generated code. It turns an LLM judge from a pass/fail critic into a promotion oracle for retained executable artifacts. That is also the riskiest part: the same model family that generated or repaired the code may be deciding whether it is general enough to persist.

The simpler alternative would be a normal vector store of task notes. OS-Copilot chooses a stronger form: reusable code. That can improve future action more directly, but it raises the review bar because wrong code can mutate files, call APIs, or change system state.

The course-learning loop is less "memory" than curriculum synthesis. It becomes memory only when lessons produce durable tools or when prior course JSON changes future lesson design. Treating every generated lesson as learned knowledge would overstate the implementation.

## Open Questions

- Should stored tools carry the originating task, execution output, score, judge reasoning, and repair history?
- How reliable is the LLM generality score as a promotion oracle compared with tests over parameterized examples?
- Can executable tools be sandboxed, permissioned, and retired when generated for OS-level operations?
- Does continuous self-learning preserve enough course history across restarts, or does writing only the latest designed course lose useful lineage?
- Should Chroma retrieval use tool descriptions alone, or should code, tests, and failure modes also influence ranking?
- How does the system prevent duplicate or near-duplicate tools as the generated repository grows?

## What to Watch

- Whether OS-Copilot adds provenance fields to `generated_tools.json`.
- Whether stored tools gain generated tests, benchmark results, or execution replay records.
- Whether the tool repository becomes populated and curated rather than purely local and empty by default.
- Whether self-learning adds explicit promotion, retirement, and deduplication policies for generated tools.
- Whether FRIDAY's vision/frontend paths reuse the same tool-memory architecture or introduce new retained artifacts.

## Bottom Line

OS-Copilot is best read as an OS automation agent whose memory is reusable executable tooling. FRIDAY turns task executions into candidate code, repairs and scores that code, and promotes high-scoring Python tools into a Chroma-retrieved local repository. Commonplace should borrow the activation pattern and the distinction between exercises, traces, and promoted tools, but not the authority boundary: executable retained artifacts need stronger lineage, tests, review, scope, and retirement before they can safely become durable system-definition artifacts.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: OS-Copilot distills execution traces and judge feedback into reusable executable tools.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: OS-Copilot bundles prose descriptions, symbolic code, JSON metadata, and embeddings in one tool-memory path.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: raw execution state and logs advise repair, judging, and replanning.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: stored tools, score thresholds, retrieval rankings, and course lessons can instruct, route, evaluate, or execute future behavior.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: OS-Copilot couples stored tools to planning-time and generation-time retrieval.
