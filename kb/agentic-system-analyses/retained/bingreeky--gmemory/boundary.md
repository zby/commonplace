---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "GMemory's hierarchical memory and shipped multi-agent task loop at commit 7b581c51d993bd600df14691d101d7e601040cc6."
run-id: AAS-2026-10-15-gmemory-a2192cc823f7-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "7b581c51d993bd600df14691d101d7e601040cc6"
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/bingreeky/GMemory
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-15-g-memory/related-systems/bingreeky--GMemory
  revision: 7b581c51d993bd600df14691d101d7e601040cc6
  sha256: null
---

# GMemory boundary

## Boundary and evidence

GMemory is in scope as a memory/knowledge/context-engineering system. The target is the G-Memory implementation together with its shipped task runner, three multi-agent consumers, prompt construction, persistence and maintenance paths, and environment feedback and recording adapters. Its intended use is to carry task experience and distilled guidance into later multi-agent tasks. This is a whole-system functional boundary, not an analysis limited to the memory API. The in-repository task runner and workflows are included callers, not an assumed external host. Alternative memory implementations are comparator modes, not additional target systems (SRC-1, `README.md`, `tasks/run.py`, `mas/module_map.py`).

The code-grounded classification rests on the implemented task-to-memory-to-task loop. The runner constructs one memory module before iterating over tasks. The workflows retrieve retained trajectories and insights, format them into agent prompts, record interactions and environment outcomes, and submit completed contexts to memory. GMemory stores task records in Chroma, persists and reloads a task graph and insight JSON, and invokes model calls for trajectory extraction, relevance ranking, insight revision and role-specific guidance (SRC-1, `tasks/run.py`, `tasks/mas_workflow/autogen/autogen.py`, `tasks/mas_workflow/dylan/dylan.py`, `tasks/mas_workflow/macnet/graph_mas.py`, `tasks/mas_workflow/format.py`, `mas/memory/mas_memory/GMemory.py`, `mas/memory/mas_memory/memory_base.py`). These are source paths, not a claim that execution was reproduced.

The shipped prompt consumption is explicit:

> user_prompt: str = format_task_prompt_with_insights(
>     few_shots=few_shots,
>     memory_few_shots=successful_shots,
>     insights=roles_rules.get(solver.profile, raw_rules),
>     task_description=self.meta_memory.summarize()
> )
> --- `tasks/mas_workflow/autogen/autogen.py`

The same consumer closes the feedback loop:

> self.meta_memory.save_task_context(label=final_done, feedback=final_feedback)
> self.meta_memory.backward(final_done)
> --- `tasks/mas_workflow/autogen/autogen.py`

Reload is part of the implementation rather than an inferred service responsibility:

> if os.path.exists(self._graph_save_path):
>     with open(self._graph_save_path, 'rb') as f:
>         self.graph = pickle.load(f)
> --- `mas/memory/mas_memory/GMemory.py`

> self.persist_file: str = os.path.join(self.working_dir,f'{self.namespace}.json')
> self.insights_memory: list[dict] = load_json(self.persist_file) or []
> --- `mas/memory/mas_memory/GMemory.py`

Maintenance includes model-mediated rule operations, score-based pruning and periodic merging. The prompts are part of that mechanism, not instructions governing this analysis (SRC-1, `mas/memory/mas_memory/GMemory.py`, `mas/memory/mas_memory/prompt.py`):

> AGREE <EXISTING RULE NUMBER>: <EXISTING RULE>
> REMOVE <EXISTING RULE NUMBER>: <EXISTING RULE>
> EDIT <EXISTING RULE NUMBER>: <NEW MODIFIED RULE>
> ADD: <NEW RULE>
> --- `mas/memory/mas_memory/prompt.py`

Consumer differences remain inside the boundary. In particular, AutoGen and MacNet call `backward` after saving the task; the inspected DyLAN schedule saves the task without that call. A later account must not assume identical maintenance across all three consumers (SRC-1, `tasks/mas_workflow/autogen/autogen.py`, `tasks/mas_workflow/macnet/graph_mas.py`, `tasks/mas_workflow/dylan/dylan.py`).

### Frozen evidence and dependencies

The sole frozen source is SRC-1 at full commit `7b581c51d993bd600df14691d101d7e601040cc6`; the acquired checkout's HEAD was verified against that pin. The analysis cutoff is 2026-10-15, the supplied run date. Only this revision supplies evidence: the linked paper, upstream benchmark repositories, model weights, live pages and provider services have not been independently captured. The local checkout is a read-only access root, not the source identity.

The overall evidence tier is code-grounded. Source text establishes implemented control flow and declared intent, not successful execution or measured benefit. No target program, test or example was run. External dependencies include an OpenAI-compatible chat endpoint and credentials, SentenceTransformer embeddings, Chroma, NetworkX, FINCH, and benchmark packages/resources for ALFWorld, ScienceWorld and PDDL; FEVER uses a Wikipedia tool adapter. The shipped wrappers, configuration and feedback interpretation are inside the boundary; external service behavior and third-party internals are not attributed to GMemory (SRC-1, `mas/llm.py`, `mas/utils.py`, `requirements.txt`, `tasks/envs/alfworld_env.py`, `tasks/envs/sciworld_env.py`, `tasks/envs/pddl_env/pddl_env.py`, `tasks/envs/fever_env.py`). This prevents conclusions about provider reliability, embedding quality, simulator correctness or present-day reproducibility from this source alone.

### Top-level coverage

All rows refer to SRC-1. Included paths remain eligible for further inspection at the same commit; initial inspection is not an evidence allowlist. “Not yet inspected” below denotes available source, not an access gap.

| Top-level tracked path | Classification and material paths | Initial inspection and limits |
|---|---|---|
| `README.md` | Included: intended hierarchical memory, setup and launch contract. | Read completely as doctrine/design, not proof of improvement. |
| `run_mas.sh` | Included: shell entry point, environment export and invocation of `tasks/run.py`. | Read completely; connects the shipped launcher to the selected memory and workflow. |
| `template.env` | Included: provider configuration surface. | Read completely; no actual credential or provider response is frozen. |
| `requirements.txt` | Included: dependency declarations. | Read completely; installed dependency behavior and resolution are not established. |
| `configs/` | Included: `configs/configs.yaml`, loaded by `mas/llm.py` for generation settings. | Configuration and loader inspected. |
| `mas/` | Included: `module_map.py`; `memory/mas_memory/GMemory.py`; `memory/mas_memory/memory_base.py`; `memory/common.py`; `memory/mas_memory/prompt.py`; `utils.py`; `llm.py`; agent, reasoning and abstract MAS support. | Core memory file, base lifecycle, state serialization, embedding and LLM adapters inspected; GMemory maintenance prompts inspected. Agent/reasoning support and remaining prompt sections are available for follow-up, not independently audited here. Deliberately excluded from target behavior: comparator implementations `chatdev.py`, `generative.py`, `memorybank.py`, `metagpt.py`, `voyager.py`; their selection is inspected in `module_map.py`. This prevents baseline-equivalence and comparative-quality conclusions, not tracing the selected GMemory loop. |
| `tasks/` | Included: `run.py`, `configs.yaml`, `mas_workflow/autogen/autogen.py`, `mas_workflow/dylan/dylan.py`, `mas_workflow/macnet/graph_mas.py`, `mas_workflow/format.py`, workflow helper modules and role prompts; `prompts/` task instructions/examples; `env_configs/`; environment loaders, wrappers and recorders in `envs/`. | Runner and config read; all three schedules traced through retrieval, prompt consumption, action/observation recording and final save. Prompt formatter and task-prompt dispatch read. Environment dispatch, feedback paths for all four benchmarks, base recorder and ALFWorld/FEVER recorder paths inspected. Individual role/task prompt bodies, remaining workflow helpers/configuration, and other recorder details are available but not yet inspected in full. They remain included. Vendored `envs/pddl_env/pddlgym/` is included as benchmark support at this pin; its solver, parser, generation, rendering and test internals are inventoried but not yet audited. No simulator-correctness or exhaustive prompt-quality conclusion follows from this boundary pass. |
| `data/` | Included: ALFWorld task JSON and FEVER/PDDL/ScienceWorld JSONL inputs; `data.md` documentation. | Tracked paths and loader use in `tasks/envs/__init__.py` inspected; `data.md` read. Dataset contents not yet inspected. No dataset-coverage, split-integrity or contamination conclusion is established. |
| `logs/` | Included as candidate supplied operation artifacts: `alfworld/autogen/qwen2.5-14b-instruct/total_task.log`, `fever/autogen/qwen2.5-7b-instruct/total_task.log`, `pddl/autogen/qwen2.5-7b-instruct/total_task.log`. | Paths inventoried; contents not yet inspected. No observed-run layer or performance result is claimed here. The logs must be checked for conditions and selected memory mode before being used as run evidence. |
| `assets/` | Deliberately excluded: `assets/method.png`, explanatory illustration linked by README. | Inventoried, not image-inspected. Prevents checking visual design claims or correspondence between the diagram and implementation; does not exclude a state-producing or state-consuming path. |

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/bingreeky/GMemory` | 7b581c51d993bd600df14691d101d7e601040cc6 | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-15-g-memory/related-systems/bingreeky--GMemory`. Implementation: tracked tree, `run_mas.sh`, `tasks/run.py`, `tasks/configs.yaml`, `mas/module_map.py`, `mas/memory/mas_memory/GMemory.py`, `mas/memory/mas_memory/memory_base.py`, `mas/memory/common.py`, `mas/utils.py`, `mas/llm.py`, all three workflow schedule paths, `tasks/mas_workflow/format.py`, `tasks/prompts/__init__.py`, `tasks/envs/__init__.py`, `tasks/envs/base_env.py` and benchmark feedback/recorder ranges described above. Doctrine/design: `README.md`, GMemory sections of `mas/memory/mas_memory/prompt.py`, `configs/configs.yaml`, `requirements.txt`, `template.env`, `data/data.md`. | Implementation: [memory](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/mas_memory/GMemory.py), [runner](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/tasks/run.py), [consumer](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/tasks/mas_workflow/autogen/autogen.py). Doctrine/design: [README](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/README.md), [maintenance prompts](https://github.com/bingreeky/GMemory/blob/7b581c51d993bd600df14691d101d7e601040cc6/mas/memory/mas_memory/prompt.py). | No access gap in the acquired checkout was encountered. External models, services, benchmark installations and the linked paper are not captured; their operation cannot be verified here. Available but uninspected files are distinguished in the coverage table. No observed run or causal experiment is established by this initial inspection. |
