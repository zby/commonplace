---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "The fragility-grid model-evaluation workflow at commit 3f51444ead009d8351de1b6b19bf901c4da3d420, including its shipped sweep driver and record consumer."
run-id: AAS-2026-10-18-fragility-grid-38b12f71fceb-01
result-disposition: complete
target-class: workflow
boundary-kind: subsystem-only
reviewed-boundary: "3f51444ead009d8351de1b6b19bf901c4da3d420"
analysis-cutoff: "2026-10-18"
evidence-tier: code-grounded
source:
  identity: https://github.com/NikolaTesla-007/fragility-grid
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-fragility-grid/related-systems/NikolaTesla-007--fragility-grid
  revision: "3f51444ead009d8351de1b6b19bf901c4da3d420"
  sha256: null
---

# fragility-grid boundary

## Boundary and evidence

This run examines the **fragility-grid harness-configuration evaluation workflow**, not an autonomous agent runtime. Its intended use is to explain how a fixed multiple-choice item set is evaluated through model calls under alternative prompt formats, option orders and scoring methods, then retained as correctness records for cross-model analysis. This is an in-scope model-dependent workflow: the collector directly calls an inference engine, which invokes vLLM or Transformers generation and continuation scoring. It is not merely a CPU analysis of someone else's model outputs (SRC-1, `repro/fragility_grid.py`, `repro/inference.py`).

> outs = engine.chat(batch, max_new_tokens=max_new_tokens, temperature=0.0)
> --- `repro/fragility_grid.py`

> outs = self._llm.generate(prompts, sp, use_tqdm=False)
> --- `repro/inference.py`

The boundary kind is **subsystem-only**: it selects the named fragility-grid experiment within a repository that also ships other benchmark experiments. It includes the complete intended collection-to-analysis path, rather than treating its caller or its retained-record consumer as an external host. It does not claim coverage of every experiment in `repro/`. The tracked tree and the following entry-point traces establish this selection (SRC-1, `README.md`, `repro/run_fragility.sh`, `repro/fragility_grid.py`, `repro/fragility_analysis.py`).

| Functional scope | Included paths and responsibilities | Inspection and limits |
|---|---|---|
| Declared release | `README.md` | Read completely; doctrine/design describing records, analysis, figures and GPU reruns. Paper claims are attributed intent/results, not independently verified conclusions. |
| Sweep driver | `repro/run_fragility.sh` | Read completely. Launches one model per GPU worker, skips a model when its summary exists, invokes the collector, then invokes CPU analysis. The shipped driver belongs to this target. |
| Collector and persistence | `repro/fragility_grid.py` | Read completely. CLI to `run`, model construction, fixed-item evaluation, generation and likelihood scoring, parsing, correctness bits, JSONL records, legend and model summaries, engine release and optional weight-cache removal. |
| Model execution adapter | `repro/inference.py` | Read completely. Backend selection, chat rendering, vLLM/HF generation, continuation scoring, HF OOM retries and resource release. External backend implementation is not frozen here. |
| Shared inputs and evaluation logic | `repro/common.py`, `repro/prompt_format.py`, `repro/brittleness.py`, `repro/prompt_format_lib.py`, `repro/fragility_lib.py`, `repro/stats.py`, `repro/predownload_data.py` | Included where used by this workflow. Initially inspected the benchmark-loader definition and imports in `prompt_format.py` and configuration definitions in `fragility_lib.py`; remaining shared definitions are available but not yet inspected. No claim of completed analysis of their correctness. Separate experiment entry points in these modules are outside the selected subsystem. |
| Retained-record consumer | `repro/fragility_analysis.py` | Inspected imports, record/legend loaders, alignment helpers and `main`. Traced record reload to `analyze`, JSON output and four figure functions. Statistical and plotting bodies remain available, not yet inspected. |
| Outputs and tests | `results/fragility/records/`, `results/fragility/summary/`, `results/fragility/config_legend.json`, `results/fragility/analysis.json`, `figures/fragility/`, `repro/test_fragility_logic.py` and relevant shared-logic tests | Included as evaluation artifacts and verification surfaces. Tree inventory only at this stage; neither artifact values nor test success have been verified. |

The persistence and later-consumption link is explicit in the collector and CPU consumer (SRC-1, `repro/fragility_grid.py`, `repro/fragility_analysis.py`):

> RECORDS_DIR = FRAG_ROOT / "records"
> SUMMARY_DIR = FRAG_ROOT / "summary"
> --- `repro/fragility_grid.py`

> recs, models, benches = load_records()
> if not models:
>     print("no fragility records found under", RECORDS_DIR)
>     return
> out = analyze(recs, models, benches)
> save_json(out, "fragility/analysis.json")
> --- `repro/fragility_analysis.py`

**Exclusions.** Other experiment entry points and their drivers, including the pass-based benchmark pipeline, judge-bias, sampling-variance, latent-skill, arena-instability and standalone prompt-format/brittleness experiments, are deliberately outside this subsystem. Their presence was established by the tracked tree; their behavior has not been assessed. This prevents conclusions about the repository's full experimental suite or a unified cross-experiment orchestration architecture. `repro/SPEC.md`, setup scripts and smoke tooling are available but not initially inspected; no assertion is made that their installation instructions reproduce the released environment. Root `.gitignore` and `LICENSE` are not operational evidence here; licensing compliance is not assessed.

**External dependencies and evidence limits.** Model checkpoints and tokenizers, Hugging Face datasets and gated access, vLLM, Transformers, PyTorch, numerical/plotting packages, GPU drivers and shell utilities are dependencies, not separately frozen sources. Dataset loading and backend access are visible in SRC-1, `repro/prompt_format.py`, `repro/inference.py` and `repro/run_fragility.sh`. This prevents independent conclusions about exact downloaded bytes, backend equivalence, hardware behavior or successful fresh reproduction. No target code, tests, examples or provider calls were executed. Available result files are not yet inspected execution evidence; this boundary supplies implementation and doctrine/design evidence, not an observed run or causal experiment.

The frozen revision is `3f51444ead009d8351de1b6b19bf901c4da3d420`; the applicability cutoff is **2026-10-18**, the supplied run date, not a claimed experiment date. The acquired checkout's HEAD matched that revision and its working-tree status was clean. The overall tier is **code-grounded**. Later inspection may cover additional files at this same registered commit within the selected workflow; it may not substitute another revision or external source.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/NikolaTesla-007/fragility-grid` | 3f51444ead009d8351de1b6b19bf901c4da3d420 | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-fragility-grid/related-systems/NikolaTesla-007--fragility-grid`. Tracked-tree inventory. Implementation: complete `repro/run_fragility.sh`, `repro/fragility_grid.py`, `repro/inference.py`; initial loader/configuration portions of `repro/prompt_format.py` and `repro/fragility_lib.py`; loader/alignment and CLI portions of `repro/fragility_analysis.py`. Doctrine/design: complete `README.md` and inspected module descriptions. | [Release](https://github.com/NikolaTesla-007/fragility-grid/blob/3f51444ead009d8351de1b6b19bf901c4da3d420/README.md); [driver](https://github.com/NikolaTesla-007/fragility-grid/blob/3f51444ead009d8351de1b6b19bf901c4da3d420/repro/run_fragility.sh); [collector](https://github.com/NikolaTesla-007/fragility-grid/blob/3f51444ead009d8351de1b6b19bf901c4da3d420/repro/fragility_grid.py); [inference](https://github.com/NikolaTesla-007/fragility-grid/blob/3f51444ead009d8351de1b6b19bf901c4da3d420/repro/inference.py); [consumer](https://github.com/NikolaTesla-007/fragility-grid/blob/3f51444ead009d8351de1b6b19bf901c4da3d420/repro/fragility_analysis.py); [loader](https://github.com/NikolaTesla-007/fragility-grid/blob/3f51444ead009d8351de1b6b19bf901c4da3d420/repro/prompt_format.py); [configuration logic](https://github.com/NikolaTesla-007/fragility-grid/blob/3f51444ead009d8351de1b6b19bf901c4da3d420/repro/fragility_lib.py) | No checkout access gap. External model/data/backend bytes are not frozen; no observed execution or independently checked result values. These limits prevent reproduction and empirical/causal validation claims. Available but initially unread code and artifacts are inspection limits, not access gaps. |
