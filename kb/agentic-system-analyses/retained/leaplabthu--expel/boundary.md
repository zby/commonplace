---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "ExpeL's shipped experience-gathering, insight-extraction and evaluation loop at commit e41ec9a24823e7b560c561ab191441b56d9bcefc."
run-id: AAS-2026-10-14-expel-efd908f05069-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: e41ec9a24823e7b560c561ab191441b56d9bcefc
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/LeapLabTHU/ExpeL
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/expel-efd908f05069/related-systems/LeapLabTHU--ExpeL
  revision: e41ec9a24823e7b560c561ab191441b56d9bcefc
  sha256: null
---

# ExpeL boundary

## Boundary and evidence

This run examines how ExpeL gathers task experience, retains trajectories, extracts and revises natural-language insights, and later supplies insights and retrieved experience to an acting agent. It includes the shipped training, extraction and evaluation drivers, not just the `ExpelAgent` library class. The target class is **memory/knowledge/context-engineering system**: its distinctive retained state and later context construction span model-dependent acting, reflection and critique. It also ships the enclosing benchmark agent loop. The boundary kind is **whole-system**, covering that repository's material state-producing, maintaining, admitting and consuming paths, including its evaluators (SRC-1: `train.py`, `insight_extraction.py`, `eval.py`, `agent/expel.py`, `agent/react.py`, `agent/reflect.py`).

The documentation declares the intended cross-stage use:

> Our agent autonomously gathers experiences and extracts knowledge using natural language from a collection of training tasks. At inference, the agent recalls its extracted insights and past experiences to make informed decisions.
> --- `README.md`

Implementation inspection follows all three shipped entry points. `train.py` calls the agent in training mode, advances tasks so that `ExpelAgent.next_task` records successful and failed trajectories, and saves selected agent state. `insight_extraction.py` loads that checkpoint, restores agent fields and calls `create_rules` for training subsets. `eval.py` reloads retained state, loads cached rules or creates them for a fold, and calls the agent on evaluation tasks. Thus these callers are part of the target, not excluded applications (SRC-1: `train.py`, `insight_extraction.py`, `eval.py`, `agent/expel.py`).

Two short passages anchor the maintenance and consumption responsibilities:

> self.rule_items_with_count = update_rules(self.rule_items_with_count, parsed_operations, list_full = self.max_num_rules+5 <= len(self.rule_items_with_count))
> --- `agent/expel.py`

> self.rule_template.format_messages(rules=self.rules)[0]
> --- `agent/expel.py`

The rule-operation prompts belong to the inspected system, rather than being incidental documentation. They instruct the model to revise existing rules. Trajectory-derived retrieval, filtering and prompt replacement are also included (SRC-1: `prompts/templates/human.py`, `agent/expel.py`).

> Do not mention the trials in the rules because all the rules should be GENERALLY APPLICABLE. Each rule should be concise and easy to follow. Any operation can be used MULTIPLE times. Do at most 4 operations and each existing rule can only get a maximum of 1 operation.
> --- `prompts/templates/human.py`

The immutable evidence boundary is repository `https://github.com/LeapLabTHU/ExpeL` at **e41ec9a24823e7b560c561ab191441b56d9bcefc**. The applicability cutoff is **2026-10-14**, the supplied run date, not a claim about newer releases. The checkout's HEAD matches the acquired revision and its working tree is clean. Overall evidence is **code-grounded**: static implementation and source-native design statements, not an executed reproduction. The boundary establishes functional coverage, not that every branch works or every configured benchmark has equivalent support.

### Top-level coverage

Every top-level tracked file or directory is accounted for below. “Included” establishes functional scope; inspected ranges and searches are stated separately so that uninspected contents are not represented as access failures. All paths refer to SRC-1.

| Top-level file or directory | Disposition | Material paths, role and initial inspection | Exclusion or inspection limit and conclusion prevented |
|---|---|---|---|
| `.gitignore` | Excluded | Repository hygiene; inventoried in the tracked tree. | Not a runtime contract; no conclusions about ignored-file policy. |
| `LICENSE` | Excluded | License text; inventoried. | Legal interpretation is outside this analysis. |
| `README.md` | Included | Read completely: intended operation, three driver commands, checkpoint locations and external setup. | Performance assertions remain source-native claims, not observed results. |
| `agent/` | Included | `base.py`, `react.py`, `reflect.py`, `expel.py`, `__init__.py`: inheritance and entry-point searches; inspected acting/prompt construction, reflection lifecycle, trajectory retention, rule creation/update, retrieval and context replacement. | Initial inspection is scoped rather than an exhaustive branch audit; no execution or correctness certification. |
| `assets/` | Excluded | `header_baby.png`, `expel.png`, `eval_example.png`: tracked inventory and README references. | Images were not treated as run artifacts or measurements; they cannot establish observed performance. |
| `configs/` | Included | `train.yaml`, `insight_extraction.yaml`, `eval.yaml`, `visualize_logs.yaml`; `agent/expel.yaml`; `benchmark/{alfworld,fever,hotpotqa,webshop}.yaml`: entry-point/default/task-path searches and complete agent configuration read. | Initial inspection did not audit every benchmark setting; defaults are configuration, not proof of runnable integration. |
| `data/` | Included | `alfworld/alfworld_tasks_suffix.json`, `fever/paper_dev.jsonl`, `hotpotqa/hotpot-qa-distractor-sample.joblib`, `webshop/webshop.fixed100.json`: tracked sizes and identities inventoried; task loading traced through `envs/__init__.py` and FEVER wrapper search. | Dataset records and binary payload were not inspected individually. This prevents claims about exact dataset composition or data quality, not tracing the shipped state loop. These files remain available evidence within this Git source. |
| `envs/` | Included | `__init__.py`, `base.py`, `alfworld/alfworld.py`, `hotpotqa/hotpotqa.py`, `webshop/webshop.py`, `fever/{fever,wikienv,wrappers}.py`: task construction read and adapter class, action, reward and external-call searches. | External simulators, servers and live Wikipedia responses are not frozen here; no claim about their actual responses or reproduced task outcomes. |
| `eval.py` | Included | Read completely: checkpoint reload, fold selection, rule admission, agent invocation, checkpoint writes and result aggregation. | Evaluator implementation is evidence, not an evaluation run. |
| `insight_extraction.py` | Included | Read completely: checkpoint input, restored state, fold-specific rule extraction and saved output. | No actual extracted-insight checkpoint was supplied. |
| `memory/` | Included | `__init__.py` read completely; `episode.py` class/property search. Embedding selection and trajectory representation support retrieval. | Dependency internals and actual embeddings are not supplied run evidence. |
| `models/` | Included | `llm.py` read completely; `__init__.py` inventoried as empty. Provider wrapper and model factory are included. | Provider/model implementation and generated responses are external. Source compatibility is not tested. |
| `prompts/` | Included | `templates/human.py` read completely; `templates/system.py`, `__init__.py`, `{alfworld,fever,hotpotQA,webshop}.py` searched for prompt dispatch, examples, critique/reflection instructions, parsers and formatting hooks. | Not every example was read end-to-end. The shipped prompts remain inside the boundary; no claim of uniform benchmark behavior follows from dispatch alone. |
| `requirements.txt` | Included | Read completely: declared libraries and versions. | Installation and transitive dependency behavior are not validated. |
| `tools/` | Included | `visualize_logs.py` read completely: reloads persisted logs, plots results and computes counts/token summaries using `utils.py`. | No log corpus was supplied to this run. |
| `train.py` | Included | Read completely: experience-gathering driver, checkpoint resume/write and outcome summaries. | No training execution or checkpoint contents were observed. |
| `utils.py` | Included | Persistence functions read; definitions and consumers searched for log parsing, result aggregation, token accounting and fold selection. | Not every helper body was inspected initially; quantitative outcomes cannot be inferred from helper names. |

### External dependencies and evidence limits

The in-repository adapters are included; their external implementations are not. Model calls use a LangChain `ChatOpenAI` wrapper. Retrieval uses imported embedding implementations and FAISS; the default agent configuration selects Hugging Face embeddings. Benchmark adapters depend on Wikipedia access, ALFWorld installation/data, or a separately running WebShop server. The README explicitly requires manual external setup for ALFWorld and WebShop (SRC-1: `models/llm.py`, `memory/__init__.py`, `agent/expel.py`, `configs/agent/expel.yaml`, `envs/hotpotqa/hotpotqa.py`, `envs/fever/wikienv.py`, `envs/alfworld/alfworld.py`, `envs/webshop/webshop.py`, `README.md`, `requirements.txt`).

These are deliberate external boundaries, not missing shipped driver coverage. They prevent conclusions about actual model response quality, external service semantics, current dependency compatibility and successful end-to-end execution. No target execution, tests, dependency installation or provider calls were performed. There is no supplied execution trace or causal experiment. The linked paper and project website are not acquired sources, so this run cannot use their separate contents as evidence. Available but initially uninspected repository content is not an access gap and may be inspected later at the same pinned revision.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/LeapLabTHU/ExpeL` | e41ec9a24823e7b560c561ab191441b56d9bcefc | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/expel-efd908f05069/related-systems/LeapLabTHU--ExpeL`. Implementation: complete `train.py`, `insight_extraction.py`, `eval.py`, `models/llm.py`, `memory/__init__.py`, `envs/__init__.py`, `tools/visualize_logs.py`; scoped agent and persistence bodies; source searches and tracked-tree coverage described above. Doctrine/design: complete `README.md`, `prompts/templates/human.py`, `configs/agent/expel.yaml`, with benchmark prompt/configuration searches. | Implementation: [training driver](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/train.py), [extraction driver](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/insight_extraction.py), [evaluation driver](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/eval.py), [agent state and context](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/expel.py), [persistence](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/utils.py). Doctrine/design: [README](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/README.md), [maintenance prompts](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/prompts/templates/human.py). | No repository access gap encountered. External provider, simulator/server internals and live services are not captured; no run/checkpoint corpus or controlled comparison was supplied. Implementation supports static mechanism claims; doctrine/design supports intended use only. Neither layer establishes observed reliability, measured improvement or causal benefit. |
