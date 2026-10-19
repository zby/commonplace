---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Memory of fragility-grid: correctness records for CPU analysis, summary-existence resume and isolated inference frames."
run-id: AAS-2026-10-18-fragility-grid-38b12f71fceb-01
source-identity: https://github.com/NikolaTesla-007/fragility-grid
reviewed-boundary: "3f51444ead009d8351de1b6b19bf901c4da3d420"
---

# fragility-grid memory report

## Boundary and evidence

This report covers retained measurements and working-context control in the selected fragility-grid subsystem. It includes shell scheduling, collector writes, exposed inference operations, shared input loading and CPU read-back. Other experiments remain excluded. All direct source findings use SRC-1 at the frozen revision above; implementation is not observed execution. The supplied runtime establishes the baseline routes; the annotations below add memory-specific findings without declaring their referents again.

Direct inspection covered complete `repro/fragility_grid.py`, `repro/run_fragility.sh`, `repro/inference.py`, `repro/fragility_analysis.py`, `repro/fragility_lib.py`, `repro/predownload_data.py` and `README.md`; relevant definitions in `repro/common.py`, `repro/prompt_format.py`, `repro/brittleness.py` and `repro/prompt_format_lib.py` were also read. Git HEAD matched the registered commit and checkout status was clean. No target code, tests or model calls were run. Released result values and figures were deliberately not inspected as execution evidence.

| Entry point or memory operation | Source path, SRC-1 | Coverage and limit |
|---|---|---|
| Shell launch, queue, logs and summary skip | `repro/run_fragility.sh` | Direct read; [RT-RTE-sweep-driver](runtime.md#rt-rte-sweep-driver), [RT-BAP-summary-skip](runtime.md#rt-bap-summary-skip). Temporary queue is scheduling state; logs are diagnostics, not model memory. |
| Collector CLI and direct `run` / `eval_grid_one_model` calls | `repro/fragility_grid.py` | Direct read; [RT-RTE-generation-grid](runtime.md#rt-rte-generation-grid), [RT-RTE-likelihood-grid](runtime.md#rt-rte-likelihood-grid), [RT-RTE-record-analysis](runtime.md#rt-rte-record-analysis). Direct invocation overwrites rather than applying shell resume. |
| Rendering, chat, single/multiple option scoring, retry and free | `repro/inference.py` | Direct read; [RT-CMP-engine](runtime.md#rt-cmp-engine), [RT-RTE-backend-recovery](runtime.md#rt-rte-backend-recovery). No hook/tool registration dispatch in these inspected entry points. Backend-internal cache behavior remains opaque. |
| Dataset acquisition and item selection | `repro/predownload_data.py`, `repro/prompt_format.py`, `repro/brittleness.py` | Direct loader reads; supplied generation/likelihood routes. Dataset cache bytes and initialization control are external and uninspected; stable item identity across downloads is not established. Predownload also requests GSM8K, unused by this subsystem. |
| Legend creation and later configuration selection | `repro/fragility_lib.py`, `repro/fragility_grid.py`, `repro/fragility_analysis.py` | Direct reads; [MEM-OBJ-config-legend](#mem-obj-config-legend). Only the permutation-count metadata is read into analysis configuration selection. |
| Record admission, reload and evaluation | `repro/fragility_grid.py`, `repro/fragility_analysis.py`, `repro/fragility_lib.py` | Direct reads; [RT-OBJ-records](runtime.md#rt-obj-records), [RT-RTE-record-analysis](runtime.md#rt-rte-record-analysis). Statistical helper internals in `repro/stats.py` not inspected here; numerical validity is not certified. |
| Analysis and figure publication | `repro/fragility_analysis.py`, `repro/common.py` | Direct reads; [MEM-OBJ-analysis](#mem-obj-analysis), [MEM-OBJ-fragility-figures](#mem-obj-fragility-figures). JSON is retained; plot functions receive the current in-memory object, not a reloaded JSON checkpoint. |
| Model/dataset/compilation caches and optional purge | `repro/run_fragility.sh`, `repro/inference.py`, `repro/fragility_grid.py` | Direct reads plus supplied [RT-CMP-roster-model](runtime.md#rt-cmp-roster-model). Physical reuse is afforded by dependency caches; their internal selection, eviction and provenance are not frozen. |

## Core ideas

The durable path is measurement-to-analysis, not answer-to-next-model-context. Generated text and continuation scores become correctness bits. The next CPU invocation reloads those bits but discards the embedded question, gold and instrumentation. Consequently stored questions do not authenticate alignment at that consumer, and stored likelihood margins do not influence its ranking. See [RT-OBJ-records](runtime.md#rt-obj-records) and [RT-RTE-record-analysis](runtime.md#rt-rte-record-analysis).

A separate retained artifact does shape later workflow behavior: summary **existence** suppresses collection. The summary's explanations and numerical content have no authority at this predicate. This is a trace-derived completion marker with scheduling authority, not evidence that model capacity improves ([RT-OBJ-summary](runtime.md#rt-obj-summary), [RT-BAP-summary-skip](runtime.md#rt-bap-summary-skip)).

Each inference input is isolated by fixed code. A generation frame contains one question, permuted options and format instructions, not gold, prior outputs or aggregate results. The likelihood route supplies a stem and one continuation at a time. Returned strings/scores escape the frame for scoring; no conversational tail or compacted summary is reloaded. This resembles a call frame only at the input/return boundary: host arrays retain many prompts and outputs, and external backend caches are not established conversation memory. SRC-1, `repro/fragility_grid.py`, `repro/inference.py`; [RT-RTE-generation-grid](runtime.md#rt-rte-generation-grid), [RT-RTE-likelihood-grid](runtime.md#rt-rte-likelihood-grid).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-config-legend
Label: config_legend retained metadata

Part of: [RT-OBJ-config](runtime.md#rt-obj-config)

Source-native identity: `fragility/config_legend.json`, produced by `config_legend` and read by `load_legend`. Representational form: symbolic JSON configuration descriptors, permutations and `_meta`. Storage substrate: results filesystem. Lineage: fixed source definitions plus requested permutation count, not an inference trace. This is the durable part of the supplied configuration container, separated because its later consumer uses only one metadata field. SRC-1, `repro/fragility_lib.py`, `repro/fragility_grid.py`, `repro/fragility_analysis.py`.

> legend = load_legend()
> n_perms = legend.get("_meta", {}).get("n_perms", 6)
> --- `repro/fragility_analysis.py`

The consumer regenerates keys from current shipped definitions; it does not validate exported permutations, `_meta.ref_config` or record provenance. Writes occur before collection, and can therefore alter later analysis scope even if that collection fails. No per-content human admission or automatic compatibility check appears in these bodies. Implementation is wired; operation is uninspected.

#### MEM-OBJ-analysis
Label: analysis retained aggregate

Source-native identity: `fragility/analysis.json`, the `out` mapping from `analyze`. Representational form: symbolic JSON statistics and natural-language interpretation strings. Storage substrate: results filesystem. Lineage: retained correctness bits, legend permutation count, fixed formulas and seeded resampling/subset comparisons. Closest supplied counterpart is [RT-RTE-record-analysis](runtime.md#rt-rte-record-analysis), a route rather than this output object; it is distinct from per-item [RT-OBJ-records](runtime.md#rt-obj-records) and per-model [RT-OBJ-summary](runtime.md#rt-obj-summary). SRC-1, `repro/fragility_analysis.py`, `repro/common.py`.

> save_json(out, "fragility/analysis.json")
> for fn in (fig_accuracy_band, fig_axis_survival, fig_fragile_gap, fig_rank_volatility):
> --- `repro/fragility_analysis.py`

Fixed code admits this aggregate without per-content approval. It retains configuration/reference identifiers, ranks, intervals, champion margins and compression tie-break metadata, but not complete generated answers, model rationales, exact dataset/model revisions or every sampled subset. Its interpretation strings are authored in source, not discovered model explanations. Plotting immediately consumes the in-memory aggregate; no later reload of this JSON is wired in the inspected workflow. `README.md` affords a human reporting use, not automatic model or collector revision.

#### MEM-OBJ-fragility-figures
Label: fragility figure exports

Source-native identity: four figure names emitted under `FIG_DIR`, each as PNG and PDF. Representational form: rendered graphical displays of symbolic statistics, with natural-language labels for human interpretation. Storage substrate: figures filesystem, default `figures/fragility/`. Lineage: plot functions select bands, axis survival, adjacent-pair gaps and rank ranges from the current analysis mapping. Closest supplied record is [RT-RTE-record-analysis](runtime.md#rt-rte-record-analysis); these are its distinct display outputs, not opaque encodings of all per-item records. SRC-1, `repro/fragility_analysis.py`.

> fig.savefig(FIG_DIR / f"{name}.png", dpi=140)
> --- `repro/fragility_analysis.py`

The exports have reporting/display authority for readers, not machine admission authority over subsequent inference. `README.md` presents them as paper figures. Code writes both formats without human approval and catches failures per figure in `main`; existence of the analysis JSON is not evidence of complete figure publication. No figure read-back into collection is wired in the inspected entry points.

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-records](runtime.md#rt-obj-records)

Lineage: mixed external question/gold inputs and model-produced text or scores, transformed by fixed parser/permutation/argmax rules into symbolic correctness bits. Embedded question text is natural language; item IDs, gold, counts and margins are symbolic/numerical metadata. Persistence omits options, raw generated answers and full prompt frames. Thus this is derived outcome memory rather than a verbatim inference trace. SRC-1, `repro/fragility_grid.py`.

> recs.append({"benchmark": bench, "item_id": f"{bench}-{ix}", "question": q,
>              "model": model_key, "gold": gold, "bits": bits[ix],
>              "ll_margin": ll_margin[ix], "n_gen_unparsed": n_gen_unparsed[ix],
>              "n_gen_configs": len(gen_cfgs)})
> --- `repro/fragility_grid.py`

At the later analysis consumer only the ID and `bits` survive loading; filename selects model/benchmark. No question-text or gold reconciliation accompanies alignment. The supplied record's loader quotation establishes the omission. Human control over manual or released record initialization is unresolved; subsequent collector generation and consumer transformations are known software-controlled paths.

#### On [RT-OBJ-summary](runtime.md#rt-obj-summary)

Lineage: software aggregation of per-item bits into model bands, class counts and configuration accuracies; filesystem overwrite, no approval gate. This is derived measurement content with a separate access-metadata use. The shell consults filename existence only, so even an empty or incompatible file meets its skip predicate. These are source-level possibilities, not observed corruptions. Reasons for skipping are not reconstructed from summary content. SRC-1, `repro/fragility_grid.py`, `repro/run_fragility.sh`; the supplied summary and behavioral-authority records carry the supporting predicate.

#### On [RT-RTE-record-analysis](runtime.md#rt-rte-record-analysis)

Read-back is pull: analysis invocation triggers a directory glob, parsing and pooling, not an unsolicited context push. Selected payload is every matching file's item-ID/bit mapping; there is no relevance query, token budget or top-k retrieval stage before pooling. Pairwise analysis intersects IDs for two models; compression intersects all models. The tiny-100 item operation is downstream experimental subset analysis, not context compaction or memory retrieval for a model. SRC-1, `repro/fragility_analysis.py`.

> for iid in common:
>     ba, bb = recs[m_a][b][iid], recs[m_b][b][iid]
> --- `repro/fragility_analysis.py`

The software accepts parseable required fields without authenticating collector provenance. Invalid JSON or missing required fields can fail loading; this is not a semantic rejection/withdrawal system. Selected bits deterministically constrain statistics, but successful activation and empirical benefit remain unobserved. Stale unmatched files remain candidates until removed externally.

#### On [RT-RTE-generation-grid](runtime.md#rt-rte-generation-grid)

Working-context selector is fixed enumeration of config/item pairs. Each formatter receives an empty few-shot string. Gold is held in host metadata for scoring, not included by the formatter. The first five dataset items are reserved but not used as demonstrations. SRC-1, `repro/fragility_grid.py`, `repro/prompt_format.py`.

> prompt = fmt(q, shown, "")
> batch.append([{"role": "user", "content": prompt}])
> --- `repro/fragility_grid.py`

Budget: collector default eight new tokens; adapter default model length 4096. HF tokenization truncates with that input limit; vLLM receives its model-length setting. No preference for retaining earlier conversation exists because the collector supplies none. Template fallback may remove the thinking-disable flag. These controls isolate current work rather than selecting retained experience. Backend cache behavior beyond this adapter is uninspected. SRC-1, `repro/inference.py`; [RT-CMP-engine](runtime.md#rt-cmp-engine).

#### On [RT-RTE-likelihood-grid](runtime.md#rt-rte-likelihood-grid)

The input selector constructs stems with an empty few-shot string and scores each option independently. Numerical return arrays are transformed to bits and one plain-cloze margin; full scores do not persist. No retained record is consulted to target or adapt these calls. HF scoring tokenization does not have the generation path's truncation argument; a uniform 4096-token clipping guarantee would be false. SRC-1, `repro/fragility_grid.py`, `repro/inference.py`.

## Write side

Acquisition is external dataset/model loading with cache reuse, not user-authored memory admission. Item selection shuffles deterministically and excludes the reserved pool. External bytes and their initial human governance remain unknown; this does not obscure the later automatic filtering, formatting, parsing and scoring. SRC-1, `repro/prompt_format.py`, `repro/brittleness.py`, `repro/predownload_data.py`; [RT-CMP-roster-model](runtime.md#rt-cmp-roster-model).

Collector software rejects unparsed generation answers as incorrect while retaining an unparsed count, rather than withholding those items from persistence. Successful return from all requested benchmark evaluation precedes record writes. `finally` frees the engine even on evaluation exceptions; no complete-model result is then written by that failed evaluation. Individual file writes are not an atomic model transaction. Raw answers are reduced to bits, not compacted into reusable instructions. The resulting summary has a later scheduling consumer, but the bits have a different later CPU-analysis consumer. See [RT-RTE-generation-grid](runtime.md#rt-rte-generation-grid), [RT-RTE-record-analysis](runtime.md#rt-rte-record-analysis) and the annotations.

Maintenance consists of overwrites and resource cleanup, not semantic knowledge editing. Direct collector reruns replace matching records/summaries, while unrelated old files remain. The legend is overwritten before evaluation. Analysis reruns overwrite their own aggregate and figures. No rejection decision based on aggregate quality automatically withdraws old measurements or deploys a different model. Removing a summary externally can permit recollection, but that is not a shipped automatic invalidation mechanism. SRC-1, `repro/fragility_grid.py`, `repro/fragility_analysis.py`, `repro/run_fragility.sh`.

Optional weight purge deletes the resolved model cache folder after record and summary writes; it does not delete outcome records or clear the summary marker. Backend release drops model references and attempts GPU cache clearing; full vLLM cleanup may require process exit. Logs are redirected per-model and overwritten on a new shell collection; the shell's later grep reads diagnostics, not answer content or a learned policy. Compilation/kernel caches are configured paths with opaque dependency-managed contents; no claim of trace-derived semantic learning follows. SRC-1, `repro/fragility_grid.py`, `repro/inference.py`, `repro/run_fragility.sh`.

## Read-back

Two later machine consumers are established: CPU analysis pulls correctness bits plus legend metadata, and shell workers test summary existence. They have no language-model interpretation stage. Static format definitions shape inference but are not accumulated-through-use read-back. Model/dataset cache loading is dependency reuse whose exact retained bytes are outside the frozen boundary. SRC-1, `repro/fragility_analysis.py`, `repro/run_fragility.sh`, `repro/inference.py`, `repro/prompt_format.py`.

The reporting path affords human inspection of JSON and figures, with no wired return into model prompts, parameter updates or configuration revision in the selected workflow. Plot functions consume `out` immediately; later CPU invocations recompute it from records, not from the previous aggregate. These distinctions prevent calling an aggregate export a deployed memory-policy update. [MEM-OBJ-analysis](#mem-obj-analysis), [MEM-OBJ-fragility-figures](#mem-obj-fragility-figures).

## Integration issues

- No correction to the supplied runtime is required. Direct source reads confirm its record/summary split and the summary-existence authority path. New legend declaration is explicitly a part of [RT-OBJ-config](runtime.md#rt-obj-config); the aggregate and display objects are outputs of, not duplicates of, [RT-RTE-record-analysis](runtime.md#rt-rte-record-analysis). No possible duplicate declarations remain after this comparison.
- Unknown initialization/manual editing of records and markers prevents assigning all admission to a human or certifying provenance. Known collector writes and later analysis admission remain software-controlled. Affected: [RT-OBJ-records](runtime.md#rt-obj-records), [RT-OBJ-summary](runtime.md#rt-obj-summary).
- External dataset identity and opaque backend caches prevent authenticating cross-run item alignment and cache semantics. Index-derived IDs plus omitted question/gold checks preserve this limit even though embedded question text exists. Affected: [RT-RTE-record-analysis](runtime.md#rt-rte-record-analysis).
- Exported legend descriptors do not control read-back beyond permutation count; failed/new collection may leave a new legend beside old records. This prevents asserting that every admitted file shares one exact grid. Affected: [MEM-OBJ-config-legend](#mem-obj-config-legend), [RT-OBJ-records](runtime.md#rt-obj-records).

## Limitations and checks

The evidence supports implemented retention and consumer wiring, not observed activation, improved capacity or causal benefit. Released values, deployment isolation, exact dependency bytes and downstream human decisions remain unverified. No agentic conversation-memory mechanism is inferred from ordinary arrays, GPU memory or filesystem caches. Negative scope statements apply only to the inspected subsystem entry points, not every experiment or backend internal.

Source identity was rechecked by Git revision and clean status; source-dependent claims use registered SRC-1 paths. The supplied member types and record contract governed identity, annotation placement and comparison with runtime records. Validation: `commonplace-run validate-output` passed for this invocation. The checker reported that invocation residue was not checked; this content pass is not job acceptance or claim support.
