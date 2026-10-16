---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "KBLaM workflow account: operator-launched accuracy evaluation through knowledge-conditioned generation, attention scoring and local delivery."
run-id: AAS-2026-10-15-kblam-5a0c2fe96cc1-01
reviewed-boundary: "69683ad096e022b58854fd88c0c58968c7d8c470"
---

# KBLaM workflow report

## Workflow account

### Selected workflow and evidence limit

The representative workflow is the internal sequence behind the shipped `accuracy` evaluation command: configured experiment request, artifact loading, KB selection and projection, generation, attention scoring, then local result files. The frozen CLI cannot reach this sequence unchanged: its top-level import requests `aug_row`, but the shipped data utility defines `augment_row` and no `aug_row` alias. This fails before CLI dispatch, loading or generation, even with fancy questions disabled. The sequence below is reconstructed implementation wiring conditional on source repair and compatible assets, not a reachable unchanged command ([RT-RTE-accuracy-generation](runtime.md#rt-rte-accuracy-generation); SRC-1, `experiments/eval.py`, `src/kblam/utils/data_utils.py`). It was selected because one driver explicitly connects these steps, rather than requiring a hypothetical connection between independent scripts. This is a multi-step research computation, not a multi-agent workflow. In this path, Python functions and the local model exchange data; no child agent receives a task or returns a finding. The driver owns progression and the model generates tokens ([RT-RTE-accuracy-generation](runtime.md#rt-rte-accuracy-generation); SRC-1, `experiments/eval.py`). Consequently this account cannot establish an agent delegation, review or recovery protocol.

Evidence is implementation inspection at the boundary's frozen commit, not an executed evaluation. Additional focused inspection covers `eval_accuracy`, its CLI and loader, `KBRetriever`, `get_kb_embd`, and the Llama attention-file writer (SRC-1, `experiments/eval.py`, `src/kblam/utils/train_utils.py`, `src/kblam/models/llama3_model.py`). Focused correction inspection also covers the evaluator's top-level import and fancy-question call and the complete `src/kblam/utils/data_utils.py`, confirming the name mismatch. These are additional inspected implementation passages of SRC-1, not a new source. External model assets, compatible checkpoints, complete datasets and runtime behavior remain unobserved. The concrete trace below selects Llama and a sampled KB; the full-dataset branch has a distinct compatibility problem described below.

The entry defect and internal call are supported by the minimum passages in [RT-RTE-accuracy-generation](runtime.md#rt-rte-accuracy-generation). Repair must bind the name used both by the import and by the internal fancy-question call; changing only the imported name without updating that call leaves the fancy-question branch defective.

### Request, selection and computational handoffs

All four handoffs below describe the internal sequence conditional on repairing the entry defect.

1. **Launcher to driver.** The operator supplies paths, model family, KB size, test batch size, layer frequency and result names. `eval_accuracy_cli` loads model/tokenizer/encoder/configuration through `_prepare_models`, reads a JSON dataset and constructs `KBRetriever`. These configuration choices are not per-answer human approval. The loader enables a separate query head and loads the encoder checkpoint; merely supplying those paths does not establish artifact compatibility (SRC-1, `experiments/eval.py`; [RT-RTE-accuracy-generation](runtime.md#rt-rte-accuracy-generation)).
2. **Driver to retriever.** Below dataset size, code samples indices without replacement. It uses the same selected order for KB projection and for the first `test_batch_size` questions. With both cached arrays present, the retriever indexes the arrays; otherwise it encodes selected records. Selection is by row index, not a semantic-search agent. Cached-vector alignment with the records remains an input contract, not an independently checked semantic identity ([RT-RTE-accuracy-generation](runtime.md#rt-rte-accuracy-generation); SRC-1, `experiments/eval.py`, `src/kblam/utils/train_utils.py`).
3. **Driver to model.** The driver formats questions for the model family, tokenizes them, and calls generation with projected KB tensors, masks, a 60-new-token bound and attention-save settings. The numerical KB is additional attention input, not a child-agent instruction packet. The attention implementation consumes it as described in [RT-RTE-kb-attention](runtime.md#rt-rte-kb-attention). The call returns token IDs for decoding; it does not return a verified factual answer (SRC-1, `experiments/eval.py`).
4. **Attention writer to metric reader.** Llama saves normalized attention arrays only when gradients are not required, saving is enabled and query length exceeds one. Thus these files are not automatically a record of every single-token decoding step. The evaluator reloads files by experiment name and layer, restricts them to KB columns, and aggregates heads/query positions for ranking (SRC-1, `src/kblam/models/llama3_model.py`, `experiments/eval.py`).

> if save_attention_weights:
>     if q_len > 1:
>         save_path = os.path.join(
>             attention_save_loc,
>             f"{attention_file_base_name}_{self.layer_idx}.npy",
>         )
>         np.save(
>             save_path,
>             attn_weights.to(torch.float32).cpu().detach().numpy(),
>         )
> --- `src/kblam/models/llama3_model.py`

### Verification is measurement, not acceptance

The answer oracle is positional: question `i` is expected to attend most strongly to KB row `i` in the selected order. Top-one and top-five metrics compare that index with aggregate attention ranking. They do not compare the decoded answer with its factual reference. The relevant minimum scoring passage is retained in [RT-RTE-accuracy-generation](runtime.md#rt-rte-accuracy-generation). There is no score threshold controlling delivery in `eval_accuracy`: decoded text is written before scoring, and scores are saved regardless of their values. A low score therefore measures a failure under this proxy; it does not reject the generated text or initiate another model call (SRC-1, `experiments/eval.py`).

The driver assumes compatible saved layers: it reads indices from `range(0, 32, kb_config.kb_layer_frequency)` and asks for five ranked rows. The code therefore needs the expected layer files and at least five KB rows for that ranking operation. It also needs enough selected records for the requested question batch. These are source-level preconditions, not evidence of successful evaluation across arbitrary model configurations (SRC-1, `experiments/eval.py`).

### Rejection, recovery and terminal delivery

The first established CLI blocker is the top-level import mismatch described above, not a dataset-size rejection. It prevents entry into the following rejection and delivery branches until repaired. Within the internal sequence, an explicit rejection occurs when requested KB size exceeds dataset size. The driver raises before KB projection or generation:

> elif kb_size > len(dataset):
>     raise IndexError(
>         f"The KB size {kb_size} is greater than the dataset size {len(dataset)}"
>     )
> --- `experiments/eval.py`

That exception is not caught by the selected CLI, so no automatic smaller-KB retry or recovery handoff follows. The launcher must change inputs and rerun if it wants another attempt. This is a bounded finding about this function and caller, not a claim about all KBLaM scripts (SRC-1, `experiments/eval.py`).

A second source-visible limit affects the equal-size alternative. It supplies a Python `range` for indices, while the uncached encoding branch inspects `indices.shape`. Those interfaces do not match. Both cached arrays select a different branch, but an uncached full-dataset evaluation cannot be treated as a working alternative without repair or changed input handling (SRC-1, `experiments/eval.py`, `src/kblam/utils/train_utils.py`):

> if kb_size == len(dataset):
>     dataset_subset_idx = range(len(dataset))
> --- `experiments/eval.py`

> elif kb_dict:
>     if len(indices.shape) == 2:
> --- `src/kblam/utils/train_utils.py`

Conditional on source repair and compatible setup, delivery in this workflow means local artifacts, not reviewer approval. The unchanged CLI cannot produce these artifacts through this sequence because its import fails before dispatch. The evaluator writes decoded text to an experiment-named `_acc.txt`, saves metric pairs to `_acc.npy`, and returns per-layer dictionaries. The CLI calls it without retaining that return value; files are the durable CLI result. Attention files are intermediate artifacts consumed by scoring. Writes are sequential rather than a single commit: text can already exist when a later metric-file read fails. This path does not catch that failure or roll back the earlier output, so file presence alone cannot certify completion (SRC-1, `experiments/eval.py`).

> np.save(
>     save_path / f"{exp_config}_acc.npy",
>     np.array([(a["acc"], a["top5acc"]) for a in accs]),
> )
>
> return accs
> --- `experiments/eval.py`

Nothing in this selected path routes scores into adapter revision or re-admits generated answers as KB records. Training and dataset production have separate triggers and controls; joining them to this evaluation as an automatic improvement loop would exceed the inspected wiring ([RT-RTE-adapter-training](runtime.md#rt-rte-adapter-training), [RT-RTE-dataset-production](runtime.md#rt-rte-dataset-production); SRC-1, `experiments/eval.py`). Successful generation, complete artifact delivery, reliable factual verification and recovery effectiveness remain unobserved; moreover, unchanged CLI completion is blocked by the inspected import defect, not merely unobserved.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-accuracy-generation](runtime.md#rt-rte-accuracy-generation)

- Workflow selection: one explicitly connected internal research evaluation path, with Llama and a sampled subset as the concrete trace; not a constructed multi-agent pipeline. The frozen CLI's top-level `aug_row` import is incompatible with the utility's `augment_row` definition, blocking dispatch even without fancy questions; source repair is a prerequisite, including preserving the internal fancy-question name binding.
- Handoff control: conditional on that repair and compatible assets, the CLI and evaluator advance synchronously through loading, selection, projection, generation and scoring. No child-agent completion or review decision controls the next step.
- Verification consequence: attention ranking is measured against selected-row positions; no acceptance threshold gates text or score persistence.
- Failure ownership: unchanged entry fails at the import before loading, selection or artifact writes; the launcher needs source repair, not merely new data or external assets. Within the reconstructed sequence, oversized KB requests raise to the launcher. The selected caller implements neither retry nor rollback; the uncached equal-size branch additionally conflicts with the index-shape contract.
- Delivery criterion: source repair and compatible setup are prerequisites; the unchanged CLI cannot reach delivery. Within the reconstructed sequence, text and final metric files are written sequentially; function return and CLI artifact delivery differ because the CLI discards the returned dictionaries. Partial output is not completion evidence.
