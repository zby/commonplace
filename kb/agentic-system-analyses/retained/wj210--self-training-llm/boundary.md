---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Self-Training-LLM's shipped data-generation, model-training and evaluation workflow at commit 97839b29d0fd8bb474f5549fa3e9d6ca504732e0."
run-id: AAS-2026-10-15-self-training-llm-5b5ee621bde2-01
result-disposition: complete
target-class: builder or improvement plane
boundary-kind: whole-system
reviewed-boundary: "97839b29d0fd8bb474f5549fa3e9d6ca504732e0"
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/wj210/Self-Training-LLM
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/self-training-llm-5b5ee621bde2/related-systems/wj210--Self-Training-LLM
  revision: "97839b29d0fd8bb474f5549fa3e9d6ca504732e0"
  sha256: null
---

# Self-Training-LLM boundary

## Boundary and evidence

The target is the repository's model-improvement workflow, not a general agent runtime. It is in scope because its shipped generation and evaluation stages issue model calls, and its training stage consumes the resulting data to produce model checkpoints. Its intended use is to build and compare Wikipedia-grounded SFT and DPO models. The class is **builder or improvement plane**; the boundary is **whole-system**, covering the shipped source workflow from topic/document selection through persisted data, filtering, training, checkpoint consumption and evaluation. This classification does not imply an autonomous, continuously scheduled improvement loop. Operators launch the separate shell/Python stages and, for TGI, select and serve the model (SRC-1, `README.md`, `script/wiki_ques_gen.sh`, `script/train.sh`, `script/testing.sh`, `script/tgi.sh`).

The repository explicitly connects data generation with model training:

> - `wiki_ques_gen.sh`- generates both SFT and DPO dataset as well as performing knowledge filtering
> - `train.sh` - SFT and DPO
> --- `README.md`

The producer persists scored answer records; the training driver reloads them and selects preference samples. The training implementation saves a checkpoint, and the response-generation driver selects configured SFT/DPO checkpoint paths for subsequent inference. These are shipped responsibilities inside the target, not excluded callers (SRC-1, `uncertainty/wiki_generation.py`, `uncertainty/train.py`, `uncertainty/self_learning_training.py`, `uncertainty/generate_response.py`). Two implementation anchors establish the persisted-data handoff:

> all_scored_instances = get_scored_ds(ans_dict,'raw_answer_sample')
> with open(answer_path,'wb') as f:
>     pickle.dump(all_scored_instances,f)
> --- `uncertainty/wiki_generation.py`

> with open(dataset_path,'rb') as f:
>     dataset = pickle.load(f)
> --- `uncertainty/train.py`

Evaluation is included: generated responses are saved as JSONL, then paired with baseline responses and source documents for a model judge; judge decisions have a reloadable disk cache (SRC-1, `uncertainty/generate_response.py`, `uncertainty/pairwise_eval.py`, `uncertainty/scorer.py`). The evaluator's model selection is explicit:

> llm_judge = LLMJudge(engine = "gpt-4o")
> --- `uncertainty/pairwise_eval.py`

### Shipped-path coverage

The table accounts for every top-level tracked file or directory. Inclusion describes the functional evidence boundary, not a claim that every line has already been analysed. Initial inspection traced all four shipped shell entry points, their Python drivers, retained-data consumers and evaluation consumer. Helper algorithms and prompt/example bodies remain available for detailed analyst inspection at the same pin.

| Top-level tracked path | Treatment | Material paths and role | Inspection status and conclusion prevented |
|---|---|---|---|
| `.gitignore` | Included | Declares generated data, responses, checkpoints, results, credentials and judge caches outside tracked source. | Read; does not supply those generated artifacts or prove they exist. |
| `README.md` | Included | Declared stage ordering, usage, inference setup and supported configuration changes. | Read completely as doctrine/design, not proof of successful operation. It names `test.sh`; the tracked evaluation wrapper is `script/testing.sh`. |
| `requirements.txt` | Included | Declared training, generation, NLP and scoring dependencies. | Read; no installation or dependency compatibility test. |
| `configs/` | Included | `data/wiki.yaml`; `model/{tinyllama,llama2_7b,llama2_13b}.yaml`; `training/{sft_trainer,dpo_trainer,lora}.yaml`; `deepspeed.yaml`, `fsdp.yaml`, `multi_gpu.yaml`. These select input data, artifact paths, trainers and distributed execution. | All YAML files read; configuration is not evidence that a particular run used it. |
| `script/` | Included | `wiki_ques_gen.sh`, `train.sh`, `testing.sh`, `tgi.sh`: shipped generation, training, response/evaluation and model-serving launchers. | All read and traced to Python consumers or the external serving launcher. No execution claim. |
| `uncertainty/` | Included for Python source; bytecode deliberately excluded | `wiki_generation.py` produces/reloads questions and answers; `train.py` filters/reloads them; `self_learning_training.py` trains/saves models; `generate_response.py` consumes checkpoints and writes responses; `pairwise_eval.py` consumes responses; `scorer.py` supplies NLI scoring, preferences and cached model judging; `data_utils.py`, `topic_generator.py`, `titles.py`, `utils.py`, `templates.py` supply dataset selection, topic lists, model calls, cleaning and prompts. | Drivers inspected completely except generation, whose setup and persistence/main ranges were inspected. Helper imports/signatures and selected implementations were inspected; full helper bodies, topic-list contents and prompt/example bodies beyond the formatting functions are not yet inspected. These are included, not access gaps or excluded responsibilities. `uncertainty/__pycache__/` is excluded as compiled cache; no conclusions about bytecode-only legacy behavior or source/bytecode equivalence. |
| `__pycache__/` | Deliberately excluded | Root `self_learning_training.cpython-310.pyc` compiled cache. | Not decompiled; cannot establish its behavior or correspondence to current Python source. It is not a source-stage entry point in the inspected launchers. |

### Frozen evidence and limits

The source is the acquired Git checkout at **97839b29d0fd8bb474f5549fa3e9d6ca504732e0**, verified against checkout HEAD. The applicability cutoff is **2026-10-15**, the supplied run date; it is not a claim that the source is current upstream. Overall evidence is **code-grounded**: source inspection plus attributed repository documentation, with no target execution or causal experiment.

External dependencies include Wikipedia data obtained through Hugging Face datasets, pretrained language models and tokenizers, NLI models, OpenAI generation/judging, optional TGI serving, and training frameworks/GPU infrastructure. Their internal implementations and live behavior are excluded. This prevents attributing provider reliability, dataset truth, pretrained capabilities or trainer internals to this repository. The repository's adapters, prompts, configuration and launcher remain included (SRC-1, `requirements.txt`, `configs/data/wiki.yaml`, `uncertainty/data_utils.py`, `uncertainty/wiki_generation.py`, `uncertainty/scorer.py`, `script/tgi.sh`). External URLs mentioned by the README are not separately acquired sources.

No model weights, generated datasets, evaluation outputs, provider transcripts or execution traces were supplied as frozen run evidence. Their absence prevents claims of successful end-to-end execution, measured improvement, factual accuracy, reproducibility or observed deployment behavior. A complete boundary therefore means the functional source boundary has been established, not that operational success has been demonstrated.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/wj210/Self-Training-LLM` | 97839b29d0fd8bb474f5549fa3e9d6ca504732e0 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/self-training-llm-5b5ee621bde2/related-systems/wj210--Self-Training-LLM`. Implementation: tracked tree; all shell scripts and YAML configuration; `uncertainty/train.py`, `uncertainty/generate_response.py`, `uncertainty/pairwise_eval.py`; `uncertainty/wiki_generation.py` setup, persistence and main; selected scoring/judge, dataset/topic-selection, prompt-formatting and checkpoint-save implementations; helper symbol/import searches. Doctrine/design: complete `README.md` and dependency/ignore declarations. | Implementation: [generation](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/wiki_generation.py), [training](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/train.py), [response consumption](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/generate_response.py), [evaluation](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/pairwise_eval.py), [scoring and cache](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/scorer.py). Doctrine/design: [README](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/README.md). | No access gap to tracked source. External services/data/weights and unprovided run artifacts prevent operational or causal conclusions. Deliberately excluded compiled caches prevent bytecode-specific conclusions. Initially inspected paths are not an allowlist; further tracked source at this commit remains in scope. |
