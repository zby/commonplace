---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "KBLaM's shipped research knowledge-augmentation system at commit 69683ad096e022b58854fd88c0c58968c7d8c470."
run-id: AAS-2026-10-15-kblam-5a0c2fe96cc1-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "69683ad096e022b58854fd88c0c58968c7d8c470"
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/microsoft/KBLaM
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-16-kblam/related-systems/microsoft--KBLaM
  revision: "69683ad096e022b58854fd88c0c58968c7d8c470"
  sha256: null
---

# KBLaM boundary

## Boundary and evidence

This run covers KBLaM's shipped research system for augmenting language models with an external knowledge base. It is in scope as a **memory/knowledge/context-engineering system**, not as an autonomous agent runtime. Its operation serves model calls: knowledge keys and values are encoded and supplied to modified transformer attention during generation. The intended use is research, not a production-complete application (SRC-1, `README.md`, `src/kblam/kb_encoder.py`, `src/kblam/models/llama3_model.py`, `src/kblam/models/phi3_model.py`).

> The model is intended to be used for research.
> --- `README.md`

> # Modify the attention matrix: Appendx a (seq_len, kb_len) block to the left
> kb_len = kb_keys.shape[2]
> kb_atten_mask = attention_mask.new_zeros(bsz, 1, q_len, kb_len)
> --- `src/kblam/models/llama3_model.py`

The boundary is **whole-system** for the repository's shipped knowledge-augmentation research workflow. It includes dataset creation and augmentation prompts, retained JSON data, embedding generation and splitting, adapter training and checkpoint persistence, checkpoint and embedding reload, knowledge-conditioned generation, and evaluators. In-repository training, evaluation and notebook callers are included; they are not excluded enclosing hosts merely because they invoke library APIs. This boundary does not assert that these scripts interoperate successfully without repair or local assets (SRC-1, `dataset_generation/gen_synthetic_data.py`, `dataset_generation/generate_kb_embeddings.py`, `dataset_generation/create_train_test_split.py`, `experiments/train.py`, `experiments/eval.py`, `eval_acc.ipynb`).

The inspected persistence-to-consumption chain is explicit in source: the generator saves and reloads entity and QA records; the embedding command writes key/value NumPy files; the split command partitions records and embeddings together; training reads those files and writes model, encoder and configuration checkpoints; evaluation reloads datasets, optional cached embeddings and encoder/model weights before passing `kb_kvs` to generation. Prompt templates and model-based scoring are also shipped responsibilities, not external evidence of successful operation (SRC-1, `src/kblam/utils/data_utils.py`, `dataset_generation/gen_synthetic_data.py`, `dataset_generation/generate_kb_embeddings.py`, `dataset_generation/create_train_test_split.py`, `experiments/train.py`, `experiments/eval.py`, `experiments/output_scorer.py`, `experiments/output_scorer_open_ended.py`).

> encoder_ckpt_name = encoder_dir / "encoder.pt"
> torch.save(self.kbretriever.encoder.state_dict(), encoder_ckpt_name)
> --- `experiments/train.py`

> encoder.load_state_dict(torch.load(encoder_path))
> return tokenizer, encoder, model, kb_config
> --- `experiments/eval.py`

> kb_kvs=kb_embedding_real,
> max_new_tokens=60,
> --- `experiments/eval.py`

### Tracked top-level coverage

All top-level tracked entries at the frozen commit are classified below. Included directories identify the material paths, not just their directory names. Inspection is boundary-oriented: source inventories and selected bodies establish responsibilities and callers; inclusion does not mean every line has already been analyzed.

| Top-level entry | Treatment and inspection | Role and limits / conclusion prevented |
|---|---|---|
| `.github/` | Deliberately excluded; tracked workflow and Dependabot filenames inventoried. | Repository automation, not the knowledge production/consumption loop. No conclusions about CI coverage, security scanning effectiveness or release automation. |
| `.gitignore` | Deliberately excluded; inventoried. | Checkout hygiene. No conclusion about ignored local artifacts being present or reproducible. |
| `CODE_OF_CONDUCT.md` | Deliberately excluded; inventoried. | Contributor governance; no assessment of governance practice. |
| `LICENSE` | Deliberately excluded; inventoried. | Legal terms; no legal/compliance assessment. |
| `README.md` | Included; read in full. | Declared mechanism, model families, setup, dataset and training entry points, research use and limits. Claims remain declarations, not measured results. |
| `SECURITY.md` | Deliberately excluded; inventoried. | Security reporting policy; no assessment of deployed security or vulnerability handling. |
| `SUPPORT.md` | Deliberately excluded; inventoried. | Support policy; no support-quality assessment. |
| `dataset_generation/` | Included; all three scripts read. | `gen_synthetic_data.py` produces, reloads, perturbs and augments records with model prompts; `generate_kb_embeddings.py` writes cached key/value arrays; `create_train_test_split.py` persists corresponding partitions. These are shipped drivers, not outside data suppliers. |
| `datasets/` | Included; both dataset cards and the synthetic LFS pointer read; Enron JSON structurally sampled. `.gitattributes` inventoried, not substantively inspected. | Shipped knowledge and dataset contracts. Enron has 29,096 parsed rows; only a sample was inspected, so no corpus-wide content-quality claim. `synthetic.json` contains an LFS pointer rather than its 107,374,110-byte payload in this checkout; unavailable payload prevents inspection of the full synthetic corpus, not inspection of its generating or consuming code. No LFS fetch was performed. |
| `eval_acc.ipynb` | Included; all cell sources inspected as text, not executed; stored outputs not used as evidence. | Notebook caller reloads retained records, arrays and model/encoder artifacts and calls accuracy evaluation across KB sizes. Local absolute paths and stale-looking API names do not justify excluding its responsibilities or claiming successful reproduction. |
| `experiments/` | Included; function/persistence inventory and material bodies inspected in `train.py` and `eval.py`; both scorer scripts read in full; Makefile setup and command inventory inspected. | Training, checkpoint writes/resume, dataset and array reload, generation/accuracy/refusal/standard evaluation and result persistence; `output_scorer.py` and `output_scorer_open_ended.py` contain judgment prompts and persist scores. `Makefile` wires split, training and evaluation commands. No successful end-to-end run or metric reproduction is established. |
| `pyproject.toml` | Included; read in full. | Package/build declaration and dependency surface; library package plus script-driven experiments, with no declared console-script entry points. No dependency installation or compatibility test was performed. |
| `src/` | Included; `kblam/kb_encoder.py`, `kblam/gpt_session.py`, `kblam/models/kblam_processor.py`, `kblam/utils/model_utils.py`, `kblam/utils/data_utils.py`, `kblam/utils/eval_utils.py` read in full; model attention bodies and helper/function inventory inspected. | Encodes supplied records or cached vectors; processor loads encoder and formats inputs; GPT helper handles Azure chat/embedding calls and authentication persistence; modified `models/llama3_model.py` and `models/phi3_model.py` admit KB keys/values into attention. `models/kblam_config.py` configures that mechanism. `utils/train_utils.py` maps dataset selections or cached vectors to KB tensors; `utils/convert.py` converts result JSON to CSV. Remaining internals are within scope for later analysis, not excluded material paths. No model/provider execution is inferred. |
| `tests/` | Included; both test modules read, sample-data structure and JSONL fixture inspected. | `test_kb_encoder.py` checks encoding shapes and trainable parameter names; `test_dataset_construction.py` checks record loading. `sample_data.json` and `test_dataset.json` supply fixtures. They support an account of intended tests, not a claim that tests passed. |

The evidence freeze is SRC-1 at commit `69683ad096e022b58854fd88c0c58968c7d8c470`; the applicability cutoff is **2026-10-15**. The supplied checkout's HEAD matched that pin. The overall tier is **code-grounded**: implementation and repository-native design declarations are available. No target execution, external paper retrieval, service calls, dependency installation or experiments were performed. Available but uninspected source internals are not access gaps and remain available at the registered commit.

External dependencies are not frozen implementation evidence: pretrained model/tokenizer and sentence-encoder assets, Azure OpenAI services and credentials, PyTorch/Transformers/Accelerate and evaluation packages, and experiment-specific checkpoints, embedding files and absolute-path directories. Their interfaces are visible in SRC-1 (`pyproject.toml`, `src/kblam/gpt_session.py`, `src/kblam/kb_encoder.py`, `src/kblam/utils/model_utils.py`, `experiments/train.py`, `experiments/eval.py`, `experiments/Makefile`). Their absence from this evidence set prevents conclusions about provider behavior, exact model outputs, checkpoint compatibility, historical experiment reproduction or production performance. The Enron extraction/linking process described in `datasets/datasetcard_enron.md` is attributed provenance, not an inspected implementation of that upstream pipeline. Unshipped deployment hosts and later repository changes are excluded; this run cannot establish their state-management or agent-orchestration behavior.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/microsoft/KBLaM` | 69683ad096e022b58854fd88c0c58968c7d8c470 | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-16-kblam/related-systems/microsoft--KBLaM`. Implementation: tracked tree and entry-point inventory; all dataset-generation scripts; encoder, GPT helper and processor; data/model/evaluation utilities; selected training, checkpointing, reload, attention and evaluation bodies; scorer scripts; notebook cell sources; Makefile command wiring; test modules and fixture structure. Doctrine/design: README, package declaration and both dataset cards. The coverage table bounds initial inspection; this row registers the repository at the commit, not a path allowlist. | Implementation: [record generation](https://github.com/microsoft/KBLaM/blob/69683ad096e022b58854fd88c0c58968c7d8c470/dataset_generation/gen_synthetic_data.py), [embedding persistence](https://github.com/microsoft/KBLaM/blob/69683ad096e022b58854fd88c0c58968c7d8c470/dataset_generation/generate_kb_embeddings.py), [training and checkpoints](https://github.com/microsoft/KBLaM/blob/69683ad096e022b58854fd88c0c58968c7d8c470/experiments/train.py), [reload and evaluation](https://github.com/microsoft/KBLaM/blob/69683ad096e022b58854fd88c0c58968c7d8c470/experiments/eval.py), [attention consumer](https://github.com/microsoft/KBLaM/blob/69683ad096e022b58854fd88c0c58968c7d8c470/src/kblam/models/llama3_model.py), [notebook caller](https://github.com/microsoft/KBLaM/blob/69683ad096e022b58854fd88c0c58968c7d8c470/eval_acc.ipynb). Doctrine/design: [README](https://github.com/microsoft/KBLaM/blob/69683ad096e022b58854fd88c0c58968c7d8c470/README.md), [synthetic dataset card](https://github.com/microsoft/KBLaM/blob/69683ad096e022b58854fd88c0c58968c7d8c470/datasets/datasetcard_synthetic.md), [Enron dataset card](https://github.com/microsoft/KBLaM/blob/69683ad096e022b58854fd88c0c58968c7d8c470/datasets/datasetcard_enron.md). | Implementation: synthetic dataset payload is unavailable behind the tracked LFS pointer; external weights, cached embeddings, local experiment assets and service implementations are not supplied as frozen evidence. These prevent full-corpus inspection and operational reproduction, not source tracing. Doctrine/design: upstream Enron extraction is described but not independently established. No observed-run or causal-experiment layer is claimed; no actual accuracy, reliability, scaling or production-readiness conclusion follows from source inspection alone. |
