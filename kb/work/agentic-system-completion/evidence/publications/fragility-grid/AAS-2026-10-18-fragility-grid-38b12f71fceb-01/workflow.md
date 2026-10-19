---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Workflow account of fragility-grid's operator-launched model sweep through correctness collection, failure handling and CPU artifact delivery."
run-id: AAS-2026-10-18-fragility-grid-38b12f71fceb-01
reviewed-boundary: "3f51444ead009d8351de1b6b19bf901c4da3d420"
---

# fragility-grid workflow report

## Workflow account

### Selected workflow and evidence

The representative workflow is the shipped `repro/run_fragility.sh` sweep: an operator requests evaluation of model keys, shell workers collect correctness records, and a CPU consumer produces cross-model analysis and figures. It was selected because it connects the model-dependent work to both persisted measurements and their delivered analysis. This is a fixed model-evaluation workflow, not a team of autonomous agents. Models supply answers and likelihoods; shell and Python code own succession and acceptance ([RT-RTE-sweep-driver](runtime.md#rt-rte-sweep-driver), [RT-RTE-generation-grid](runtime.md#rt-rte-generation-grid), [RT-RTE-likelihood-grid](runtime.md#rt-rte-likelihood-grid)).

All source findings use SRC-1 at the frozen revision. This member directly inspected complete `repro/run_fragility.sh` and `repro/fragility_grid.py`, `Engine._chat_hf` and `free` in `repro/inference.py`, and the loading/alignment and `main` portions of `repro/fragility_analysis.py`. These are implementation evidence, not observed execution. The supplied runtime records provide the remaining configuration, loader and analysis baseline. No target execution, tests, result-value inspection or experiments were performed. Successful reproduction and the release's empirical conclusions are not established here.

### Request, assignment and model work

1. **The operator defines the sweep.** Environment variables select models, GPUs, benchmarks, item count, permutations and backend. Defaults are eight models, four benchmarks, 300 items and six permutations, not the release's full reported experiment. Dataset predownload is attempted but failure is tolerated. The operator supplies scope and credentials, not per-answer approval (SRC-1, `repro/run_fragility.sh`; [RT-RTE-sweep-driver](runtime.md#rt-rte-sweep-driver)).

2. **Shell workers assign model jobs.** A temporary queue holds model keys; `flock` serializes removal of its first entry. Each GPU worker skips a model if the model summary filename already exists. Otherwise it launches a collector subprocess with the model key, requested benchmarks, count, permutation count and backend, plus the inherited environment and GPU visibility. Stdout and stderr go to a per-model log. This delegates computation, not authority to choose a new task. The summary is a completion marker rather than a request-compatibility check ([RT-OBJ-summary](runtime.md#rt-obj-summary), [RT-RTE-sweep-driver](runtime.md#rt-rte-sweep-driver); SRC-1, `repro/run_fragility.sh`).

3. **The collector constructs inputs and requests answers.** It resolves the model key, constructs an `Engine`, and evaluates all requested benchmarks. For each benchmark it loads items once for that model, enumerates the generation and likelihood configurations, and retains per-item correctness dictionaries in host memory. At default permutations the grid has 24 generation configurations and two likelihood configurations. Generation sends independent single-user-message frames containing the current formatted question and reordered options. Likelihood calls instead score option continuations against fixed stems. The model receives neither dataset gold nor earlier model answers through these prepared inputs. These are isolated evaluation inputs, not conversational subtasks that return plans ([RT-OBJ-config](runtime.md#rt-obj-config), [RT-RTE-generation-grid](runtime.md#rt-rte-generation-grid), [RT-RTE-likelihood-grid](runtime.md#rt-rte-likelihood-grid); SRC-1, `repro/fragility_grid.py`).

### Verification and the persistence handoff

The collector owns answer acceptance. A parser extracts a displayed option position from generated text; code maps it back through the permutation and compares it with dataset gold. An unparsed answer becomes an incorrect bit and increments an instrumentation counter. Likelihood scoring selects the largest mean continuation score and compares the selected original option with gold. The dataset label is the expected-answer oracle; there is no model judge or per-item human veto. Rejection here means recording zero, not requesting a corrected answer or revising the prompt ([RT-RTE-generation-grid](runtime.md#rt-rte-generation-grid), [RT-RTE-likelihood-grid](runtime.md#rt-rte-likelihood-grid); SRC-1, `repro/fragility_grid.py`).

This gate measures correctness under the chosen extraction rules; it does not establish semantic fidelity of parsing. Generation's `zip(meta, outs)` assumes backend output cardinality, without an equal-length assertion. A shorter return could leave incomplete dictionaries rather than trigger a collection rejection. This is a conditional implementation limit, not an observed failure ([RT-RTE-generation-grid](runtime.md#rt-rte-generation-grid); SRC-1, `repro/fragility_grid.py`).

After evaluation returns for all requested benchmarks of a model, the collector frees the engine, overwrites each benchmark/model JSONL file, computes the model summary and overwrites its JSON file. It does not checkpoint completed benchmarks during evaluation. The configuration legend is written before model collection. Records carry questions, gold, correctness bits and instrumentation, but not raw generated answers or complete rendered prompts. Consequently downstream analysis cannot reconstruct answer extraction from the retained records alone ([RT-OBJ-records](runtime.md#rt-obj-records), [RT-RTE-record-analysis](runtime.md#rt-rte-record-analysis); SRC-1, `repro/fragility_grid.py`).

### Failure, recovery and continuation

**Local recovery is narrow.** For HF generation, `Engine._chat_hf` catches CUDA OOM, clears cache and retries the current chunk at half size, down to one example; OOM at one propagates. The model does not diagnose or repair the failure. This handler does not cover likelihood calls or vLLM. On evaluation failure the collector's `finally` still calls `engine.free()`, but the subsequent record writes are not reached. The shell's one-model subprocess adds a process-exit cleanup boundary ([RT-RTE-backend-recovery](runtime.md#rt-rte-backend-recovery); SRC-1, `repro/inference.py`, `repro/fragility_grid.py`).

**A collector skip can look like shell success.** The collector catches `GatedAccessError` during engine construction, prints a skip and continues. For the shell's single-model child this path can end normally without producing that model's records or summary. The worker's `OK` tests process exit, not artifact completeness. This workflow-specific distinction supplements [RT-RTE-sweep-driver](runtime.md#rt-rte-sweep-driver); SRC-1, `repro/fragility_grid.py`, `repro/run_fragility.sh`:

> except GatedAccessError as e:
>     print(f"SKIP {key}: {e}")
>     continue
> --- `repro/fragility_grid.py`

**A failed child does not stop the sweep.** The worker reports `FAILED` and takes another model from the queue. After workers finish, CPU analysis runs on whatever matching records exist. Retry of failed collection requires another launch or direct collector invocation; there is no immediate shell retry. Summary existence suppresses future collection without checking benchmark selection or configuration compatibility. Partial writes can remain if persistence fails after evaluation; neither collector nor consumer provides a multi-file transaction or rollback. Unmatched old record files remain eligible for analysis ([RT-RTE-sweep-driver](runtime.md#rt-rte-sweep-driver), [RT-RTE-record-analysis](runtime.md#rt-rte-record-analysis); SRC-1, `repro/run_fragility.sh`, `repro/fragility_grid.py`, `repro/fragility_analysis.py`).

### Delivery and its limits

The CPU consumer reloads all matching JSONL files, derives model and benchmark identities from filenames, and retains only item-ID-to-bits mappings. It does not receive the collector's question text, gold or raw answers as verification material. Pairwise comparisons intersect item IDs; shared IDs alone do not authenticate identical question content across independently loaded dataset versions. The consumer therefore trusts retained measurements rather than rerunning their answer checks ([RT-RTE-record-analysis](runtime.md#rt-rte-record-analysis); SRC-1, `repro/fragility_analysis.py`).

Delivery is local filesystem publication: `analysis.json` is written, then four figure functions are attempted and a console headline is printed. No records yields an early return. Figure exceptions are printed and tolerated after JSON publication. The sweep neither aggregates all child failures into a required success condition nor makes its final message conditional on successful CPU analysis. Thus its final `ALL DONE` message is not an acceptance certificate for a complete requested sweep or all figures. The operator must distinguish model skips/failures, record availability, JSON publication and figure success ([RT-RTE-record-analysis](runtime.md#rt-rte-record-analysis); SRC-1, `repro/fragility_analysis.py`, `repro/run_fragility.sh`).

The model does not consume the delivered analysis in later calls along this inspected workflow. Later invocations instead reload correctness records for CPU analysis or consult summary existence for scheduling. There is no source-supported model-led revision cycle to append to this trace ([RT-RTE-record-analysis](runtime.md#rt-rte-record-analysis), [RT-BAP-summary-skip](runtime.md#rt-bap-summary-skip)). Implementation wiring establishes these handoffs and failure branches, not that any particular launch exercised them successfully.

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

#### On [RT-RTE-sweep-driver](runtime.md#rt-rte-sweep-driver)

Workflow acceptance distinction: the shell judges collector process exit, not successful collection of the assigned model. The caught gated-access branch shown above can produce a normal child exit with a skip and no new model output. The operator remains responsible for resolving access and relaunching; the worker proceeds rather than repairing credentials. This is an implementation-supported branch, not an observed skip (SRC-1, `repro/fragility_grid.py`, `repro/run_fragility.sh`).

#### On [RT-RTE-record-analysis](runtime.md#rt-rte-record-analysis)

Delivery distinction: JSON publication precedes figure attempts, and each figure can fail independently without rejecting that JSON. An empty record set returns before analysis publication. Neither downstream entry point supplies an all-requested-models completeness gate. These conditions bound what the sweep's terminal message establishes (SRC-1, `repro/fragility_analysis.py`, `repro/run_fragility.sh`).

> if not models:
>     print("no fragility records found under", RECORDS_DIR)
>     return
> --- `repro/fragility_analysis.py`
