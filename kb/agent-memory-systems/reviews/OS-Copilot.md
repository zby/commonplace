---
description: "OS-Copilot/FRIDAY review: OS task agent with self-refining code execution, vector-retrieved generated tools, and course-driven tool-library accumulation"
type: ../types/agent-memory-system-review.md
tags: [related-systems, trace-derived]
status: current
last-checked: "2026-04-27"
---

# OS-Copilot

OS-Copilot is the open-source codebase behind FRIDAY, a generalist computer-use agent for Linux and macOS from the OS-Copilot project. The reviewed implementation is less a broad knowledge base than a task agent with an accumulated executable tool library: it decomposes OS tasks, retrieves existing tools, generates and repairs code, judges completed subtasks, and stores high-scoring Python tools for later vector retrieval.

**Repository:** https://github.com/OS-Copilot/OS-Copilot

**Reviewed commit:** https://github.com/OS-Copilot/OS-Copilot/commit/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e

## Core Ideas

**The memory object is a generated tool, not a note.** The durable store is `oscopilot/tool_repository/generated_tools/`: `generated_tools.json`, per-tool code files, per-tool description files, and a Chroma vector database. `ToolManager.add_new_tool(...)` writes all four surfaces and persists the vector index; retrieval returns tool names by embedding similarity over tool descriptions, then fetches descriptions or code from the JSON-backed map ([tool_manager.py](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/tool_repository/manager/tool_manager.py), [generated_tools.json](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/tool_repository/generated_tools/generated_tools.json)).

**Planning is a typed DAG over OS actions.** `FridayPlanner.decompose_task(...)` prompts the LLM to produce JSON subtasks with `description`, `dependencies`, and `type`, then builds an `ActionNode` graph and topologically sorts unfinished nodes. The types are execution modes rather than knowledge types: `Python`, `Shell`, `AppleScript`, `API`, and `QA` ([friday_planner.py](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/planner/friday_planner.py), [friday_pt.py](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/prompts/friday_pt.py)).

**Execution uses the operating system as the feedback surface.** `FridayExecutor.generate_tool(...)` asks the LLM for code and invocation logic, `execute_tool(...)` runs it through the unified `Env`, and `judge_tool(...)` sends the code, output, error, working directory, directory listing, and downstream task needs back to the LLM for a `Complete` / `Amend` / `Replan` judgment plus a 1-10 generality score ([friday_executor.py](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/executor/friday_executor.py), [env.py](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/environments/env.py)).

**Self-refinement is local repair plus optional replanning, with a promotion-path bug.** `FridayAgent.self_refining(...)` interprets the judge status. `Amend` enters a bounded repair loop, regenerating code from the critique and execution state. `Replan` retrieves relevant tools from the critique, asks the planner to add new tasks, and re-sorts the graph. A Python subtask is stored only when it completes and its generality score meets `config.score`, default 8, but the inspected code passes the pre-repair `code` variable to `store_tool(...)` even after `repairing(...)` returns revised code. That means initial-success paths promote the successful code, while repair-success paths appear able to promote the original failed version ([friday_agent.py](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/agents/friday_agent.py), [config.py](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/utils/config.py)).

**The explicit self-learning loop is curriculum-driven.** `SelfLearning` designs lessons for a software/package pair, optionally using demo-file content and up to 50 prior lessons, then runs each lesson through FRIDAY. The release notes call out saved historical learning courses, but the durable behavior in code is narrow: courses are JSON files under `courses/`, and the reusable behavior comes from each lesson's successful Python subtasks being promoted into the tool repository ([self_learning.py](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/agents/self_learning.py), [self_learner.py](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/modules/learner/self_learner.py), [course_learning.py](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/course_learning.py), [release.md](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/docs/release.md)).

**The shipped repository starts with an empty learned-tool library.** The checked-in `generated_tools.json` is `{}`. The system's memory value is therefore produced by running it, not by a curated library shipped with the repo. `quick_start.py` runs a single task through FRIDAY, while `course_learning.py` runs continuous learning by repeatedly designing lessons and executing them ([quick_start.py](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/quick_start.py), [course_learning.py](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/course_learning.py)).

## Comparison with Our System

| Dimension | OS-Copilot / FRIDAY | Commonplace |
|---|---|---|
| Primary substrate | Python functions, descriptions, JSON, Chroma vectors | Markdown notes, source reviews, ADRs, indexes, instructions |
| Memory atom | Reusable executable subtask tool | Typed knowledge artifact with frontmatter and links |
| Creation trigger | Successful high-scoring Python subtask | Deliberate authoring, ingest, review, or promotion |
| Retrieval | Vector search over tool descriptions | `rg`, indexes, titles/descriptions, authored links |
| Verification | LLM judge over execution state and generality score | Structural validation, semantic review, human/agent judgment |
| Behavior-changing artifact | More code available to future plans | Better context and stronger KB artifacts |
| Lifecycle | Add, overwrite, delete by tool name | Status, archive, replacement, validation, indexes |

OS-Copilot is stronger where memory should become direct action capacity. A stored tool is not advice about how to automate Excel; it is executable code that future tasks can retrieve and reuse. That is a more behavior-changing substrate than a prose note when the target domain is repetitive computer operation.

Commonplace is stronger where memory should remain inspectable, evidential, and compositional. OS-Copilot stores code and a short description, but not provenance, source traces, confidence history, citations, or typed relationships between tools. The vector index improves recall, but it does not explain why a tool should be trusted beyond the fact that the LLM judge once scored it highly.

The main tradeoff is that OS-Copilot treats learning as tool accretion. This works for narrow procedural competence and gives the agent a concrete reuse surface. It is weak for conceptual knowledge, decision history, or methodology because there is no path from a repeated observation to a note, rule, test, index, or policy artifact.

## Borrowable Ideas

**Promote only after execution plus generality judgment.** Ready to borrow as a guardrail pattern for generated scripts. The exact threshold is arbitrary, but "ran successfully" and "looks reusable" are separable checks; OS-Copilot makes both explicit before adding a tool.

**Store executable memory beside a retrieval description.** Ready for a future workshop/tool cache. A generated script alone is hard to retrieve; a natural-language description alone cannot act. Keeping both and indexing the description is a practical pairing.

**Use downstream dependency needs during judging.** Worth borrowing if Commonplace ever validates generated helpers. FRIDAY's judge prompt includes the next task, so a subtask can fail if it did not return information needed later, even if it looked locally successful.

**Course-driven exploration for tool discovery.** Needs a narrow use case. The curriculum loop is a useful way to force coverage of a software package: design progressively harder tasks, execute them, and keep reusable functions. For Commonplace, the analogue would be benchmark-like workshop exercises that deliberately produce reusable scripts or instructions.

**Treat replanning separately from code repair.** Ready as an execution-agent design pattern. `Amend` means the generated code should change; `Replan` means the environment needs another operation. That distinction keeps repair from trying to solve missing-package or missing-file problems by code editing alone.

## Trace-derived learning placement

**Trace source.** OS-Copilot qualifies as trace-derived learning. The raw trace is a subtask execution trajectory: generated code, invocation, environment output, error text, current working directory, directory listing, downstream task requirements, LLM critique, repair attempts, and final judge score. In self-learning mode, those traces are produced from curriculum lessons generated for a software/package pair.

**Extraction.** The extraction oracle is mostly an LLM judge over execution feedback. `judge_tool(...)` classifies the task as `Complete`, `Amend`, or `Replan` and assigns a generality score; `repair_tool(...)` uses the critique and state to produce revised code; `store_tool(...)` extracts a tool description from the code it receives and writes it if the tool name is not already present. Because the current caller does not reassign the repaired code before storing, repaired-success traces have weaker promotion grounding than initial-success traces.

**Storage substrate, form, and lineage.** The distilled retained state is symbolic: Python code, a natural-language description, a JSON registry entry, and an embedding index entry. Its lineage is subtask execution trace -> LLM judge/repair loop -> stored generated tool. It is not model-weight learning and not a prose knowledge base.

**Behavioral authority.** The stored tool is a system-definition artifact. It changes the agent's future action space because later planning and execution can retrieve and call that function. The course JSON is closer to work history or curriculum state; the tool repository is the real behavior-changing artifact.

**Scope.** Scope is local to the configured generated-tool repository, defaulting to `oscopilot/tool_repository/generated_tools`. There is no per-project provenance model beyond choosing a repository path, and no cross-tool abstraction layer.

**Timing.** The loop is online during task execution and staged during curriculum learning. Each task can promote a successful Python subtask immediately; continuous learning repeats course design, lesson execution, and tool accumulation.

**Survey placement.** On the [trace-derived survey](../trace-derived-learning-techniques-in-related-systems.md), OS-Copilot sits in the executable-skill-library branch: traces are not condensed into lessons or rules but into callable tools. It strengthens the survey's symbolic-artifact claim and adds a useful contrast to prose-memory systems: the artifact is harder to audit semantically, but more directly behavior-changing.

## Curiosity Pass

The headline phrase "self-improvement" is accurate only in a constrained sense. FRIDAY does not improve its model, prompts, planner, or retrieval policy. It improves by accumulating generated Python functions that future tasks can retrieve. That is still learning, but it is tool-library growth rather than agent-wide adaptation.

The code/course boundary is also weaker than the release note suggests. The self-learning loop can read prior course JSON and ask for advanced non-duplicate lessons, but the implementation saves the new course object after each run rather than maintaining a rich course history with outcomes. The stronger trace-derived mechanism is not course persistence; it is successful subtask promotion into the tool repository.

The verification story depends heavily on the same LLM family that generated the code. Environment output gives the judge real evidence, but the repo does not add independent tests, sandbox policy, provenance records, or human review before storing a tool. The repair-path variable bug makes this sharper: the judge can approve revised code while the storage call still receives the original code. For filesystem and application automation, that is a meaningful trust gap.

A simpler alternative would be a scripts directory with docstrings plus a grep index. OS-Copilot's vector retrieval is helpful once the tool library grows, but the important design move is the promoted executable artifact, not Chroma itself.

## What to Watch

- Whether generated tools gain provenance: original task, execution trace, score, repaired versions, and last successful use.
- Whether the roadmap's multi-round dialogue support changes memory scope from per-task tool reuse to session-level working memory ([roadmap.md](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/docs/roadmap.md)).
- Whether tool promotion gets stronger verification, such as generated tests or replay before reuse, and whether the repair-success path stores the repaired code rather than the original attempt.
- Whether the curriculum loop starts saving outcomes and failures, not just designed lessons.
- Whether vision-enabled FRIDAY keeps the same executable-skill-library substrate or introduces a separate visual trace memory.

---

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — extends: OS-Copilot is an executable-skill-library case where traces promote to callable code rather than prose rules
- [Voyager](./voyager.md) — compares: both accumulate executable skills, but OS-Copilot applies the pattern to general OS/software tasks rather than Minecraft
- [ExpeL](./expel.md) — contrasts: both learn from trajectories, but ExpeL promotes prompt-visible rules while OS-Copilot promotes callable Python tools
- [Pi Self-Learning](./pi-self-learning.md) — contrasts: Pi distills session mistakes into injected text; OS-Copilot distills successful execution into retrievable code
- [Deploy-time learning is the missing middle](../../notes/deploy-time-learning-is-the-missing-middle.md) — sharpens: OS-Copilot is deploy-time symbolic learning with an executable promotion target
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) — grounds: OS-Copilot separates artifact substrate from retrieval substrate, with code/description/JSON/vector entries serving different roles
