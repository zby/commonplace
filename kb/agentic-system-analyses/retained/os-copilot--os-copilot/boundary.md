---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "OS-Copilot's shipped agent runtime, tool retention and learning paths at commit f720af8807e49a92dda64572d2c6bc6c0ac7ee7e."
run-id: AAS-2026-10-16-os-copilot-7cef03148c53-01
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: "f720af8807e49a92dda64572d2c6bc6c0ac7ee7e"
analysis-cutoff: "2026-10-16"
evidence-tier: code-grounded
source:
  identity: https://github.com/OS-Copilot/OS-Copilot
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-18-os-copilot/related-systems/OS-Copilot--OS-Copilot
  revision: f720af8807e49a92dda64572d2c6bc6c0ac7ee7e
  sha256: null
---

# OS-Copilot boundary

## Boundary and evidence

This run analyses OS-Copilot as shipped in its repository, not just its reusable tool manager. Its intended use is to build computer-operating agents. The principal shipped agent is FRIDAY. The target qualifies as an **enclosing runtime** because its own code owns model-directed planning, execution, feedback, repair and replanning. The quick-start caller instantiates these components and invokes the agent; it is part of the target, not an excluded host application (SRC-1, `README.md`, `quick_start.py`, `oscopilot/agents/friday_agent.py`).

The classification rests on executable control flow, not the project's self-improvement label:

> sub_task = self.planner.sub_task_list.pop(0)
> execution_state = self.executing(sub_task, task)
> isTaskCompleted, isReplan = self.self_refining(sub_task, execution_state)
> --- `oscopilot/agents/friday_agent.py`

The **whole-system** boundary includes the shipped task drivers and UI, the FRIDAY planning/retrieval/execution modules, their prompts, execution environments, local tool services, tool admission and maintenance, retained-tool reload and reuse, the course-generation driver and its retained course state, alternative example loops, and evaluation/test code. It does not imply that every line has been inspected or that every path works. Initial inspection traced these responsibilities sufficiently to establish the functional boundary; later jobs may inspect additional files at the same registered commit.

The retained-tool loop is included end to end. FRIDAY conditionally admits Python code after its completion/score decision; the executor prepares tool information; the manager persists code, descriptions, metadata and the vector index. New manager instances reload the metadata and index. Retrieval supplies descriptions to planning and code to generation. Manual add/delete operations are included because they alter the same retained state (SRC-1, `oscopilot/agents/friday_agent.py`, `oscopilot/modules/executor/friday_executor.py`, `oscopilot/tool_repository/manager/tool_manager.py`, `oscopilot/modules/retriever/vector_retriever.py`). The admission branch is explicit:

> if node_type == 'Python' and isTaskCompleted and score >= self.score:
>     self.executor.store_tool(tool_name, code)
> --- `oscopilot/agents/friday_agent.py`

The course driver is also included, rather than treated as an external training application. It constructs the same agent, invokes continuous learning, reads or creates a course file, supplies previous course content to model-directed course design, runs lessons through the agent and saves course output. Text extraction itself calls the agent. These are shipped producers and consumers of state; their inclusion does not establish that saved courses accurately record successful learning (SRC-1, `course_learning.py`, `oscopilot/agents/self_learning.py`, `oscopilot/modules/learner/self_learner.py`, `oscopilot/tool_repository/basic_tools/text_extractor.py`).

> new_course = self.learner.design_course(software_name, package_name, demo_file_path, file_content, prior_course)
> self.course.update(new_course)
> self.learn_course(new_course)
> save_json(prior_course_path, new_course)
> --- `oscopilot/agents/self_learning.py`

The frozen revision is **f720af8807e49a92dda64572d2c6bc6c0ac7ee7e**. The checkout's HEAD was checked against that acquisition pin, and tracked working-tree/index diffs were empty. The applicability cutoff is **2026-10-16**, the supplied run date; it is not a claim that the revision was current on that date. The overall evidence tier is **code-grounded**. The repository supplies implementation and doctrine/design evidence; the self-learning tutorial also supplies attributed reported operation. No target execution, tests, provider calls or experiments were performed. Repository examples, fixture workbooks and a tutorial's success narrative are not observed-run or causal-experiment evidence.

External dependencies include model/embedding providers selected through configuration (OpenAI or Ollama), Chroma/LangChain, the host OS and its Python/Jupyter/shell/AppleScript facilities, installed applications and packages, network/API providers, and the Node/React/Electron UI stack. Their shipped adapters and invocation code are included; the external implementations and live service behavior are not. Thus the run can describe how the repository requests models, executes code and manages state, but cannot establish provider reliability, real OS compatibility, desktop-task success, isolation guarantees, retrieval quality or empirical improvement (SRC-1, `oscopilot/modules/base_module.py`, `oscopilot/utils/llms.py`, `oscopilot/environments/env.py`, `oscopilot/tool_repository/manager/tool_manager.py`, `oscopilot/tool_repository/manager/api_server.py`, `fronted/src/interface/api.js`). Linked paper, website, hosted documentation, FRIDAY-Gizmos and benchmark downloads were not acquired as additional sources. Their contents and results are outside this frozen evidence set.

### Top-level coverage

The tracked tree was enumerated at the pin. “Included” means within the analysis boundary, not a claim of exhaustive inspection. Rows distinguish inspected responsibility paths from uninspected assets and support files; no material shipped loop was excluded for lack of access. All path references below are SRC-1.

| Top-level tracked path | Classification | Material paths, role and initial inspection | Limit or conclusion prevented |
| --- | --- | --- | --- |
| `.env_template` | Included | Configuration surface for provider/service setup; identified in tree and README, not inspected in detail. | No assertion about exact template defaults. Runtime configuration was inspected in `oscopilot/utils/config.py`, `oscopilot/utils/llms.py` and `oscopilot/modules/base_module.py`. |
| `.github/` | Excluded | Issue-report templates only, per tracked tree. | No conclusion about community reporting or project governance. |
| `.gitignore` | Excluded | Repository hygiene. | No conclusion about completeness of ignored local artifacts or developer state. |
| `.readthedocs.yaml` | Excluded | Hosted documentation build configuration. | No conclusion about the deployed documentation build or live site. |
| `LICENSE` | Excluded | Licensing rather than agent operation. | No legal/license assessment. |
| `README.md` | Included | Inspected declared purpose, quick-start, single-round limitation and UI/tutorial pointers. | Declared capabilities are not execution evidence. |
| `course_learning.py` | Included | Inspected shipped continuous-learning entry point and component construction. | No course-learning run was observed. |
| `docs/` | Included | Inspected `docs/source/tutorials/add_tool.rst` and `docs/source/tutorials/self_learning.rst`; API-reference/build/release/roadmap tree identified. Maintenance instructions and claimed learning outcome belong to the boundary. Remaining documentation and static assets were not exhaustively read. | Tutorial outcome is reported operation only; uninspected docs do not establish additional mechanisms or results. |
| `environment.yml` | Included | Dependency/environment declaration identified, not inspected in detail. | No reproducibility or dependency-resolution conclusion. |
| `examples/` | Included | Inspected `examples/GAIA/run_GAIA.py`, `examples/SheetCopilot/run_sheet_task.py`, and loop portions of `examples/light_friday/light_friday.py` and `examples/friday_vision/friday_vision.py`; searched `examples/LLAMA3/test_llama3.py`. Covers benchmark callers/result writing, simplified model/code feedback loop, screenshot/OCR variant and model-service example. SheetCopilot input/answer workbooks and dataset identified, not evaluated. | No benchmark accuracy, workbook correctness or desktop success established. The GAIA driver is code, not a supplied result trace. |
| `fronted/` | Included | Inspected `fronted/README.md`, `fronted/src/interface/api.js`, `fronted/src/interface/constant.js`; searched `fronted/public/electron.js`. UI launches `quick_start.py` and reads its log records. Remaining React presentation, assets and dependency lockfile were not exhaustively inspected. | No claim about UI rendering, packaging success or interaction robustness. This caller is not an excluded enclosing application. |
| `oscopilot/` | Included | Inspected `oscopilot/agents/friday_agent.py`, `oscopilot/agents/self_learning.py`; compared `oscopilot/agents/friday2_agent.py` and inspected export paths. Inspected responsibility-bearing portions of `oscopilot/modules/planner/friday_planner.py`, `oscopilot/modules/planner/basic_planner.py`, `oscopilot/modules/executor/friday_executor.py`, `oscopilot/modules/learner/self_learner.py`, and `oscopilot/modules/base_module.py`; read `oscopilot/modules/retriever/vector_retriever.py`. Inspected judge/course prompts in `oscopilot/prompts/friday_pt.py` and searched other prompt definitions. Inspected `oscopilot/environments/env.py`, `oscopilot/tool_repository/manager/tool_manager.py` admission/reload/retrieval/maintenance paths, `oscopilot/tool_repository/manager/api_server.py`, `oscopilot/tool_repository/basic_tools/text_extractor.py`, empty `oscopilot/tool_repository/generated_tools/generated_tools.json`, `oscopilot/utils/config.py` and provider-adapter portions of `oscopilot/utils/llms.py`. Searched Bing/audio/caption service routes and identified OpenAPI/tool-request paths. | Remaining adapter internals, language-environment internals, schema/helpers and unused/alternative definitions were not exhaustively read. No execution or cross-version compatibility claim follows from inspection. They remain available within the pin, not excluded responsibilities. |
| `pic/` | Excluded | README/framework illustration assets. | No interpretation of diagrams as independently verified architecture or run evidence. |
| `quick_start.py` | Included | Inspected shipped task entry point, configuration and agent construction. | A runnable script is not proof of successful installation; `setup.py` declares a `quick_start:main` console entry while this file has top-level code rather than a `main` definition. |
| `requirements.txt` | Included | Dependency declaration identified through `setup.py`; not dependency-audited. | No compatibility/security/completeness assessment of installed dependencies. |
| `setup.py` | Included | Inspected package declaration and console entry point. | Packaging metadata is not installation evidence. |
| `test/` | Included | Searched all five test files for setup, imports, tests and assertions: planner/basic planner, executor generation, data loader, self-learning/text extraction/course execution. | Tests were not executed; assertions are intended checks, not passing results. |
| `working_dir/` | Included | Tracked spreadsheet/document inputs identified; quick-start and course configuration consume this directory. Contents not substantively evaluated. | Fixtures do not establish task success or retained learned competence. |

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/OS-Copilot/OS-Copilot` | f720af8807e49a92dda64572d2c6bc6c0ac7ee7e | implementation; doctrine/design; reported operation | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-18-os-copilot/related-systems/OS-Copilot--OS-Copilot`. Implementation: tracked tree and entry-point/consumer tracing, task and course drivers, FRIDAY agent/modules, tool storage/reload/retrieval/manual maintenance, environment dispatch, service routes, UI process/log integration, example loops and test structure, as detailed above. Doctrine/design: README, judge/course prompts, tool-maintenance and self-learning tutorials. Reported operation: the self-learning tutorial's before/after Excel-task account only. | Implementation: [task entry](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/quick_start.py), [agent loop](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/agents/friday_agent.py), [tool state](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/tool_repository/manager/tool_manager.py), [course loop](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/agents/self_learning.py), [UI caller](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/fronted/src/interface/api.js). Doctrine/design: [README](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/README.md), [prompts](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/oscopilot/prompts/friday_pt.py), [maintenance tutorial](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/docs/source/tutorials/add_tool.rst). Reported operation: [self-learning tutorial](https://github.com/OS-Copilot/OS-Copilot/blob/f720af8807e49a92dda64572d2c6bc6c0ac7ee7e/docs/source/tutorials/self_learning.rst). | No required repository path was inaccessible. External providers, operating environment, downloaded benchmarks and linked external documents are outside this source. No inspectable execution trace or intervention/comparison was supplied or produced; the tutorial does not establish observed performance or causal improvement. Available but uninspected files are inspection limits, not access gaps. |
