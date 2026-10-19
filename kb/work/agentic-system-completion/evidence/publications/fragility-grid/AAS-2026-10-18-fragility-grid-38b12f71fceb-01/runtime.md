---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Runtime baseline of fragility-grid's collection, backend alternatives and retained-record analysis at the frozen Git revision."
run-id: AAS-2026-10-18-fragility-grid-38b12f71fceb-01
reviewed-boundary: "3f51444ead009d8351de1b6b19bf901c4da3d420"
---

# fragility-grid runtime report

## Runtime account

### Work and evidence basis

The selected workflow measures multiple-choice correctness under a fixed grid of prompt formats, option orders and scoring methods. It does not let a model choose actions, tools, successors or updates. Python and shell loops own progression; models generate answers or supply continuation likelihoods. The release's claims about leaderboard instability are claims about the evaluated models, not guarantees of the evaluation machinery ([RT-CLM-grid-purpose](#rt-clm-grid-purpose)).

All source findings below use SRC-1 at the boundary's frozen revision. This inspection adds implementation coverage of configuration and classification logic in `repro/fragility_lib.py`, formatters/parsers in `repro/prompt_format_lib.py`, `load_bench` in `repro/prompt_format.py`, `_load_mcq` in `repro/brittleness.py`, roster/model loading/output helpers in `repro/common.py`, collector and inference adapter bodies, and the record loading, alignment, analysis, compression and CLI bodies in `repro/fragility_analysis.py`. `repro/test_fragility_logic.py` was read as implementation-level test specifications, not test results. Plotting internals and the shipped result values remain uninspected. No target execution, tests, provider calls or experiments were performed. Operation and benefit remain unobserved; implementation evidence does not independently authenticate the release's reported results.

### Ordinary invocation and ownership

A human/operator launches `repro/run_fragility.sh`, with environment variables controlling model keys, GPUs, benchmarks, item count and backend. The script optionally supplies a local Hugging Face token and attempts dataset predownload, tolerating predownload failure. A file queue protected by `flock` assigns each model to a GPU worker. The worker skips a key if its summary filename exists; otherwise it starts a collector subprocess with `CUDA_VISIBLE_DEVICES` and redirects stdout/stderr to a per-model log. The defaults are eight model keys, four benchmarks, 300 items, six permutations and vLLM. These shipped defaults are not a reconstruction of the README's twelve-model, 3,679-item release (SRC-1, `README.md`, `repro/run_fragility.sh`, `repro/common.py`). See [RT-RTE-sweep-driver](#rt-rte-sweep-driver).

The collector resolves a key in the merged `ROSTER`, constructs an `Engine`, then loads each benchmark afresh for that model. A seed of 1234 controls item shuffling; the first five items are reserved as a pool and excluded from evaluation, even though this experiment supplies no few-shot examples. ARC filters to four options with resolvable gold labels; TruthfulQA constructs four options from the correct answer plus the first three distractors and resets gold to position zero. HellaSwag uses labelled validation examples; MMLU uses shuffled test examples. Thus the "same items" design depends on stable external dataset bytes and loading behavior across model invocations, not on a persisted, versioned item manifest (SRC-1, `repro/prompt_format.py`, `repro/brittleness.py`).

For each benchmark, Python enumerates four generation formats times six fixed permutations plus two likelihood stems: 26 configurations at defaults. Generation creates one user-message frame per configuration/item, with no earlier conversation or model outputs carried forward. The shared benchmark items stay in host memory, but each model-visible frame contains only its formatted current question/options and the tokenizer's chat-template material. Likelihood frames instead concatenate a question stem with one option, independently of other options. These are stateless evaluation frames, not delegated agents; only answer text or numerical scores return. No frame reload or conversational compaction is implemented in these inspected calls (SRC-1, `repro/fragility_grid.py`, `repro/fragility_lib.py`, `repro/inference.py`). See [RT-RTE-generation-grid](#rt-rte-generation-grid) and [RT-RTE-likelihood-grid](#rt-rte-likelihood-grid).

The code parses generated labels, maps shown positions back through the permutation and compares with dataset gold. Unparsed answers are wrong and increment a counter. Likelihood scoring selects the largest mean continuation-token log probability, comparing the winning original option index to gold. The expected-answer oracle is the dataset label, not a model judge. All proposals here are candidate answers or experimental configurations; no candidate product revision is admitted. The operator selects the experiment scope; fixed software enumerates configurations and judges correctness. There is no per-answer human approval in these paths (SRC-1, `repro/fragility_grid.py`, `repro/fragility_lib.py`).

On successful evaluation of all requested benchmarks, the engine is freed, records are overwritten per benchmark/model, and a model summary is overwritten. Optional `PURGE_WEIGHTS=1` removes that model's cached Hub directory after output writes. The sweep then runs the CPU consumer, which reloads every matching record file under the results root, derives accuracies/ranks and writes analysis plus attempted figures. Models do not read these results on later inference calls in the inspected collector. The separate consumer, not the model, receives the retained correctness bits ([RT-RTE-record-analysis](#rt-rte-record-analysis)).

### Controls, guarantees and forcing routes

The capability surface is local model inference, dataset/model downloads, filesystem output, GPU allocation and optional recursive cache deletion. The current grant set is the invoking process's environment, credentials and filesystem/GPU access. The shell's GPU visibility is resource selection, not a sandbox. The deployed isolation envelope is not supplied. The inspected model channels return text/log probabilities to fixed consumers rather than execute model-selected shell commands. Backend/library internals and installation-time behavior are outside the frozen source evidence (SRC-1, `repro/run_fragility.sh`, `repro/fragility_grid.py`, `repro/inference.py`, `repro/common.py`).

Four source-level forcing cases qualify the ordinary path:

1. **vLLM versus HF and template fallback.** Both generation backends call `_render`, which asks the tokenizer to disable thinking, but retries without that flag on `TypeError`. Supported templates can therefore reach a render without the named flag; reliable suppression of thinking is not a universal guarantee. Likelihood scoring bypasses chat rendering entirely. HF generation truncates to `max_model_len`; HF likelihood scoring does not use that generation tokenizer guard. vLLM receives its own maximum model length. HF only interprets `load_4bit`, whereas vLLM also interprets `quant` and tensor parallelism. A backend switch need not preserve numerical scoring, quantization or context behavior (SRC-1, `repro/inference.py`, `repro/common.py`; [RT-CMP-engine](#rt-cmp-engine)).

2. **HF OOM recovery.** An HF generation chunk retries at half size after CUDA OOM, down to one example; an OOM at one re-raises. This is a best-effort recovery protocol owned by `Engine._chat_hf`, not a promise that every item completes. It covers neither HF likelihood scoring nor vLLM failures. The collector's `finally` frees the engine on evaluation exceptions, but output writing occurs only after that evaluation returns. Direct collector multi-model invocation is supported and does not provide the sweep's one-model process-exit cleanup (SRC-1, `repro/inference.py`, `repro/fragility_grid.py`; [RT-RTE-backend-recovery](#rt-rte-backend-recovery)).

3. **Resume and partial failure.** Summary existence is the sole skip predicate. It does not compare requested benchmarks, permutation count, model revision or record completeness. Direct collector invocation overwrites instead of skipping. A failure after some record writes but before summary completion can leave partial outputs; the global legend is written before model collection and can diverge from old records. The sweep reports a failed child and continues, then analyzes whatever record files are present. Its final success-looking echo is not an all-model or figure-success guarantee (SRC-1, `repro/run_fragility.sh`, `repro/fragility_grid.py`, `repro/fragility_analysis.py`).

4. **Parsing and absent bits.** The grid excludes fuzzy restatement parsing by enumerating only four label formats. This exclusion is wired for the collector, not all standalone experiments in the repository. Nevertheless, the included regex parsers accept the first matching letter/digit anywhere in the response; deterministic parsing does not guarantee faithful answer extraction. Generation uses `zip(meta, outs)` without an explicit equal-length assertion. If an external backend violates output cardinality, incomplete bit dictionaries can reach persistence. The consumer uses missing bits as zero for per-configuration accuracy, but `classify_item` considers only present values. This is a conditional vulnerability to an external contract violation, not an observed backend failure (SRC-1, `repro/prompt_format_lib.py`, `repro/fragility_grid.py`, `repro/fragility_lib.py`, `repro/fragility_analysis.py`).

The load-bearing same-grid/deterministic-design promise is owned by the collector and configuration code: **guarantee strength: protocol**; **implementation conclusion status: wired**; **operation conclusion status: uninspected**. Enforcement is fixed permutation generation, fixed item-shuffle seeds, greedy generation and mean likelihood scoring. It covers collector-generated calls under stable inputs. It requires external dataset/model/tokenizer versions, backend order/cardinality contracts and numerical/hardware stability; none is independently established. The shipped model/dataset loaders do not pin immutable Hub revisions. CPU analysis can also be invoked directly on supplied or edited records and therefore does not enforce their collection provenance (SRC-1, `repro/fragility_lib.py`, `repro/prompt_format.py`, `repro/inference.py`, `repro/fragility_analysis.py`).

The inspected path admits experimental measurements through fixed software writes, not changes to product code, instructions, capability registries or production machinery. Code changes, model selection and environment changes are operator/developer inputs; this source does not show their approval workflow. Statistical ranking and subset selection produce analysis artifacts, not automatic model deployment or retraining. Memory-specific revision conclusions are left to the memory analyst.

## Shared records

### Components

#### RT-CMP-engine
Label: Engine inference adapter

Source-native identity: `Engine` in SRC-1, `repro/inference.py`. Representational form: symbolic Python backend dispatch and numerical score extraction. Storage substrate: shipped Python source and process-local tokenizer/model/backend references. It executes generation and likelihood calls; it is not itself a model decision loop.

> if backend == "auto":
>     backend = "vllm" if _vllm_available() else "hf"
> --- `repro/inference.py`

Rendering control has a reachable fallback, so the comment's intended thinking suppression depends on tokenizer support:

> except TypeError:
>     return self._tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
> --- `repro/inference.py`

#### RT-CMP-roster-model
Label: ROSTER-selected language model

Source-native identity: `ROSTER[key]` resolving to `ModelSpec.name` (SRC-1, `repro/common.py`, `repro/fragility_grid.py`, `repro/inference.py`). Representational form: distributed-parametric weights used to generate text and continuation logits/log probabilities. Storage substrate: externally downloaded Hub checkpoint/cache, loaded into backend-managed CPU/GPU memory. Tokenizer/template bytes are an additional external dependency, not the same representational part as weights.

Parameters do not undergo training updates in the inspected inference paths: HF calls `model.eval()` and no-gradient inference; vLLM is used through generation. Exact checkpoint version is not pinned: neither model loading path supplies a revision. A mutable Hub name can resolve to different weights on later loading; this is name resolution, not a remote model-service endpoint. Provider/backend internals remain uninspected. No improved capacity is inferred from repeated evaluation.

> tok = AutoTokenizer.from_pretrained(spec.name)
> model = AutoModelForCausalLM.from_pretrained(spec.name, **kwargs)
> model.eval()
> --- `repro/common.py`

### Operative objects

#### RT-OBJ-config
Label: Config and format grid

Source-native identity: `Config`, `GEN_FORMATS`, `LL_FORMATS` and `REF_CONFIG_KEY` in SRC-1, `repro/fragility_lib.py`. Representational form: symbolic tuples/dataclass fields and fixed dispatch; their formatted natural-language strings are interpreted by the model. Storage substrate: shipped source, process-local lists and exported `config_legend.json`. The exported legend labels analysis configuration count but does not carry a cryptographic data/model provenance check.

> REF_CONFIG_KEY = "gen|letter_plain|p0"
> --- `repro/fragility_lib.py`

#### RT-OBJ-records
Label: Per-item correctness records

Source-native identity: benchmark/model JSONL records written by `run` in SRC-1, `repro/fragility_grid.py`, later loaded by `load_records` in `repro/fragility_analysis.py`. Representational form: symbolic JSON fields (`bits`, gold indices, item IDs and instrumentation); the embedded question is natural-language content, but the inspected analysis loader discards it. Storage substrate: local `results/fragility/records/`, or the `RESULTS_DIR`-selected root. These retain outcomes, not raw generated answers or full prompts.

> recs[model][bench][r["item_id"]] = r["bits"]
> --- `repro/fragility_analysis.py`

#### RT-OBJ-summary
Label: Model summary completion marker

Source-native identity: `summary/<model>.json` (SRC-1, `repro/fragility_grid.py`, `repro/run_fragility.sh`). Representational form: symbolic JSON accuracy bands, class counts and per-configuration accuracies. Storage substrate: results filesystem. Its filename existence, rather than contents, has operational force in the sweep's skip decision. The shell hardcodes `../results/fragility/summary`, whereas Python supports `RESULTS_DIR`; an override can separate write and resume roots.

> if [ -f "$SUMMARY_DIR/$m.json" ]; then
>   echo "[gpu$gpu] skip $m (summary exists)"; continue
> fi
> --- `repro/run_fragility.sh`

### Routes

#### RT-RTE-sweep-driver
Label: Sweep scheduling and resume

Endpoints/progression: operator environment → shell queue → GPU worker → collector subprocess → CPU analysis. Owner and decision policy: shell workers pop model keys under `flock`; fixed filename existence decides skip. Context/state/effects: queue/lock temporary files, credentials/cache environment, child process logs and GPU visibility; process exit is the stronger cleanup boundary than `Engine.free`. Operating mode: bounded experimental sweep. Human contribution is launch/scope selection, not per-answer approval. No answer oracle is used by scheduling.

- Immediate return: Child exit status becomes an OK/FAILED console message; workers continue to other keys.
- Later read-back: Existing model summary filenames suppress later collection, without validating their content or request compatibility.
- Delegated visibility: Collector receives model key, benchmarks, count, permutations, backend, environment and selected GPU; model sees only prepared inference inputs.
- Selection predicate: Queue order and summary existence, not measured model performance.
- Invalidation or expiry: No configuration-sensitive invalidation of summaries; queue and lock are removed after workers finish.
- Activation or effect: Wired process launch/skip; actual activation was not observed.
- Evidence limits: No supplied run trace; script completion does not establish every model or downstream figure succeeded.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Evidence: SRC-1, `repro/run_fragility.sh`.

> "$PYTHON_BIN" predownload_data.py || true
> --- `repro/run_fragility.sh`

#### RT-RTE-generation-grid
Label: Generation configuration evaluation

Endpoints/progression: loaded MCQ tuples → formatted/permuted user messages → `Engine.chat` → regex parser → original-index comparison → correctness dictionaries. Owner: collector loops and parsers; model proposes answer text, fixed code decides correctness, dataset gold supplies expected-answer oracle. Operating mode: bounded zero-shot experiment, not improvement-triggered revision. State consists of current benchmark items, prompt batch, metadata, output text and counters. It does not admit product or instruction changes.

- Immediate return: Per-item bits and unparsed counts are accumulated, then returned as benchmark record lists.
- Later read-back: Records are persisted after successful model evaluation and later consumed by CPU analysis, not reinserted into model context here.
- Delegated visibility: Each backend receives a separate single-user-message input; other items and gold are not added by the collector to that message.
- Selection predicate: Enumerated generation format/permutation crossed with every loaded evaluation item.
- Invalidation or expiry: Prompt/output arrays are ordinary current-invocation state; subsequent collection overwrites matching JSONL files.
- Activation or effect: Parser-selected shown position is mapped through `perm` before correctness comparison; execution unobserved.
- Evidence limits: Regex determinism is not semantic fidelity; output cardinality is assumed by `zip`; external template behavior is not frozen.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Evidence: SRC-1, `repro/fragility_grid.py`, `repro/prompt_format_lib.py`.

> outs = engine.chat(batch, max_new_tokens=max_new_tokens, temperature=0.0)
> --- `repro/fragility_grid.py`

> chosen_orig = perm[pred_shown]
> correct = int(chosen_orig == gold)
> --- `repro/fragility_grid.py`

#### RT-RTE-likelihood-grid
Label: Continuation likelihood evaluation

Endpoints/progression: question/cloze stem and original option strings → `score_options_many` → backend continuation scores → argmax → gold comparison. Owner: Python fixed scoring/selection policy; model provides numerical likelihoods. HF uses full-sequence forward logits, while vLLM requests prompt log probabilities on concatenated strings and extracts continuation positions. Form: natural-language input interpreted through distributed weights, then symbolic/numerical selection. Operating mode: same bounded experiment. Dataset gold is the expected-answer oracle; no model judge, human per-item veto or automatic deployment selector is involved.

- Immediate return: Per-item correctness bits; plain-cloze top-two score margin is also recorded.
- Later read-back: Correctness bits reach the analysis loader; this loader does not consume the recorded margin.
- Delegated visibility: One question stem plus one continuation per model scoring sequence; competing option texts are not included in that sequence by this route.
- Selection predicate: Both fixed likelihood stems and every loaded item; largest mean per-token continuation score wins, with first-index tie behavior from Python `max`.
- Invalidation or expiry: Score arrays are current-run state; persisted records are overwritten by matching collection.
- Activation or effect: Wired numerical argmax and gold comparison; no observed outcome asserted.
- Evidence limits: Order independence concerns independent option scoring, not backend numerical equivalence. Token boundary handling and backend extraction are implementation choices, not independently validated likelihood equivalence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Evidence: SRC-1, `repro/inference.py`, `repro/fragility_grid.py`, `repro/fragility_lib.py`.

> sp = SamplingParams(temperature=0.0, max_tokens=1, prompt_logprobs=0)
> --- `repro/inference.py`

> pred = max(range(len(opts)), key=lambda i: scores[i])
> bits[ix][c.key] = int(pred == gold)
> --- `repro/fragility_grid.py`

#### RT-RTE-backend-recovery
Label: HF chunk retry and release

Endpoints/progression: HF prompt batch → sized chunk → generate → CUDA OOM handler → smaller chunk or re-raise. Owner: `Engine._chat_hf`; the fixed rule chooses retry size, not a model. Context/state/effects: same rendered prompts, growing return list and CUDA cache; successful chunks advance the cursor. Guarantee strength: best effort. Covered path is HF generation only; likelihood and vLLM calls are alternate paths outside this handler. Required external contract: successful generation returns the chunk's outputs in order and CUDA OOM uses the caught exception class.

- Immediate return: Generated strings in chunk order if successful; exception if one example still cannot fit.
- Later read-back: inapplicable — no retained retry state is loaded by later invocations.
- Delegated visibility: inapplicable — local backend retry, not a separate delegated decision-maker.
- Selection predicate: CUDA OOM on the current generation chunk; retry halves `cur` down to one.
- Invalidation or expiry: Retry state ends on chunk success or propagated failure; engine references are cleared by `free`, but vLLM worker memory may require process exit.
- Activation or effect: Wired retry and cache clearing, not observed recovery.
- Evidence limits: No run trace; non-OOM failures and scoring calls are not covered. Direct multi-model collector calls need not exit between models.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Evidence: SRC-1, `repro/inference.py`, `repro/fragility_grid.py`.

> if cur == 1:
>     # Truly cannot fit a single example -- re-raise (real, not maskable).
>     raise
> cur = max(1, cur // 2)
> --- `repro/inference.py`

#### RT-RTE-record-analysis
Label: Record persistence and analysis

Endpoints/progression: collector record lists → overwrite JSONL/summary → later `load_records` → pooled and aligned bit arrays → `analyze` → `analysis.json` and four figure attempts. Owner: fixed collector and CPU analysis code. Admission: successful collection is sufficient for output writes; later analysis accepts parsed matching files, not per-record human approval. These are measurement artifacts, not knowledge/instruction or capability revisions. Human authorship of manual input edits is unresolved. Recovery: rerun overwrites; there is no atomic multi-file transaction or automatic rollback in these bodies. Guidance consists of fixed config definitions and statistical formulas, not a runtime-generated method revision.

Mode: bounded comparison of models/configurations. Software chooses reference ranks and adjacent pairs; bootstrap intervals crossing zero label pairs tied on robust items. Compression compares top-discrimination subsets across seeded cutoff tie-breaks with random subsets, and skips if fewer than three models or fewer than `tiny_k + 5` shared items. These comparisons do not revise the collector or deploy a winner. Expected answers enter through stored correctness bits, not a fresh gold check by this consumer. No human veto gate is required before publication to the filesystem (SRC-1, `repro/fragility_analysis.py`).

- Immediate return: Collector summary and log output; consumer writes analysis JSON and attempts PNG/PDF figure generation.
- Later read-back: JSONL bits and legend metadata are reloaded by later CPU invocations; summaries separately affect sweep resume.
- Delegated visibility: inapplicable — model does not receive analysis artifacts through the inspected route.
- Selection predicate: All `*__*.jsonl` files; filename supplies benchmark/model, item ID supplies alignment. Pooled accuracy uses each model's own items, pair analysis intersects two models, compression intersects all models.
- Invalidation or expiry: Matching collector outputs and analysis JSON overwrite; stale unmatched files remain eligible. Missing legend defaults to six permutations.
- Activation or effect: Wired numerical analysis and output writes; actual runs, correct released values and causal empirical interpretation remain unverified.
- Evidence limits: Loader keeps only bits, does not compare question text or gold, and later duplicate item IDs overwrite earlier entries. Alignment by index-derived IDs alone does not authenticate common question identity after dataset changes.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Evidence: SRC-1, `repro/fragility_grid.py`, `repro/fragility_analysis.py`, `repro/fragility_lib.py`.

> for p in sorted(RECORDS_DIR.glob("*__*.jsonl")):
>     bench, model = p.stem.split("__", 1)
> --- `repro/fragility_analysis.py`

> except Exception as e:
>     print(f"[fig] {fn.__name__} failed: {e!r}")
> --- `repro/fragility_analysis.py`

### Claims

#### RT-CLM-grid-purpose
Label: Same-item configuration comparison

Claimed operation: evaluate identical fixed items over generation formats/orders and likelihood stems, retaining correctness bits to attribute leaderboard differences. Source: SRC-1, `repro/fragility_grid.py`, with release-level reported results in `README.md`. The code wires this design within a collection invocation; external version stability and actual execution are not established.

> For each model x MCQ benchmark, evaluate the SAME fixed item set under every configuration in
> the grid (generation x {formats} x {orderings}  +  loglikelihood x {stems}) and record, per item,
> a correctness bit for each config.
> --- `repro/fragility_grid.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-prompt-answer
Label: Formatted prompt to answer

Consumer: selected model through tokenizer/backend. Channel: formatted user message plus chat template for generation, or cloze/continuation string for likelihood. Force: natural-language instructions and option presentation condition model output; parser/argmax rules then have deterministic authority over recorded correctness. Horizon: single evaluation frame, with resulting measurements persisted. No reliable compliance or demonstrated format benefit is inferred. Evidence: SRC-1, `repro/prompt_format_lib.py`, `repro/fragility_grid.py`, `repro/inference.py`; [RT-RTE-generation-grid](#rt-rte-generation-grid), [RT-RTE-likelihood-grid](#rt-rte-likelihood-grid).

> return f"{fewshot}Question: {question}\n{body}\nAnswer with the letter only:"
> --- `repro/prompt_format_lib.py`

#### RT-BAP-summary-skip
Label: Summary existence to collection skip

Consumer: shell worker. Channel: filesystem existence test on the model summary path. Force: hard skip of that model regardless of current request compatibility. Horizon: later launches while the marker remains at the shell's fixed path. Contents need not be interpreted; a changed summary value alone does not change this predicate. This is recovery/scheduling authority, not model instruction or demonstrated learning. Evidence: SRC-1, `repro/run_fragility.sh`; [RT-OBJ-summary](#rt-obj-summary), [RT-RTE-sweep-driver](#rt-rte-sweep-driver).

## Annotations

none
