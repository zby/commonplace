---
type: agentic-system-analysis-result
description: 'fragility-grid collection subsystem: fixed model-evaluation grid, file-backed
  analytical reuse and existence-only resumption without learned guidance'
run-id: AAS-2026-09-25-fragility-grid-01
system: fragility-grid
run-date: '2026-09-25'
result-disposition: complete
target-class: returning computation
boundary-kind: subsystem-only
reviewed-boundary: 3f51444ead009d8351de1b6b19bf901c4da3d420
analysis-cutoff: '2026-09-25'
evidence-tier: code-grounded
memory-comparison:
  axes:
    behavioral_authority:
      assessment: known
      basis: wired
      note: Records provide evidence to CPU analysis; queue and summary existence
        route execution; legend n_perms selects the reconstructed grid. Dataset scoring
        authority is outside this retained-memory boundary.
      records:
      - RTE-5
      - RTE-6
      - RTE-7
      values:
      - knowledge
      - routing
    curation_operations:
      assessment: absent
      basis: null
      note: No semantic maintenance of retained memory in inspected writers/readers;
        aggregation precedes initial persistence, overwrites replace run outputs,
        and queue removal acknowledges dispatch.
      records:
      - ABS-1
      values: []
    distilled_form:
      assessment: inapplicable
      basis: null
      note: Symbolic correctness summaries are evaluation aggregates, not distilled
        behavior guidance.
      records:
      - ABS-1
      values: []
    faithfulness_tested:
      assessment: not-determinable
      basis: null
      note: No retained execution evidence was admitted; source inspection cannot
        establish a dependence test on recalled content or a global absence of such
        tests.
      records:
      - ABS-1
      values: []
    learning_scope:
      assessment: inapplicable
      basis: null
      note: Restart across shell invocations is retention, not a task horizon for
        learning.
      records:
      - ABS-1
      values: []
    learning_timing:
      assessment: inapplicable
      basis: null
      note: No qualifying trace-learning route.
      records:
      - ABS-1
      values: []
    lineage:
      assessment: known
      basis: wired
      note: Questions are imported into records; the legend and queue are compiled
        from supplied configuration; bits, summaries and logs derive from execution
        outputs. No manual memory authoring interface is wired.
      records:
      - OBJ-3
      - OBJ-4
      - RTE-4
      - RTE-6
      values:
      - imported
      - other-compiled
      - trace-extracted
    read_back_direction:
      assessment: known
      basis: wired
      note: Scheduler explicitly requests queue head and summary-file status; CPU
        analysis explicitly requests matching record files and the legend. Automatic
        invocation does not turn these requested reads into push.
      records:
      - RTE-5
      - RTE-6
      - RTE-7
      values:
      - pull
    read_back_signal:
      assessment: inapplicable
      basis: null
      note: Pull-only boundary; filenames and glob patterns identify requested files,
        not automatic delivery of memory into model context.
      records:
      - RTE-5
      - RTE-6
      - RTE-7
      values: []
    representational_form:
      assessment: known
      basis: wired
      note: JSON fields and queue identifiers are symbolic; retained question strings
        and diagnostic log messages are natural language. No scoped opaque payload.
      records:
      - OBJ-3
      - OBJ-4
      values:
      - natural-language
      - symbolic
    storage_substrate:
      assessment: known
      basis: wired
      note: Retained operative objects are files; in-memory inference and loader working
        copies are not additional retention stores in this boundary.
      records:
      - OBJ-3
      - OBJ-4
      - RTE-4
      - RTE-5
      values:
      - files
    trace_learning:
      assessment: known
      basis: wired
      note: Evaluation outputs become evidence for CPU analysis, not durable guidance
        returned to inference. Scheduler uses summary existence, not a trace-derived
        prescription or rationale.
      records:
      - ABS-1
      - RTE-2
      - RTE-3
      - RTE-4
      - RTE-5
      values:
      - 'no'
    trace_source:
      assessment: inapplicable
      basis: null
      note: No qualifying trace-learning route within this boundary.
      records:
      - ABS-1
      values: []
    write_agency:
      assessment: known
      basis: wired
      note: Operator launch triggers automatic acquisition, compilation, overwrite
        and queue updates. Filesystem editability alone does not establish manual
        memory authoring.
      records:
      - RTE-4
      - RTE-6
      values:
      - automatic
  scope: 'Files accumulated or replaced by the grid and shell: result records, model
    summaries, shared config legend, temporary work queue and per-model logs; their
    scheduler and CPU loader consumers. Excludes fixed datasets, templates and pretrained
    weights, transient inference buffers, dependency caches, and downstream statistical
    artifacts beyond the loader boundary.'
---

# fragility-grid collection and resume subsystem

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-fragility-grid-01/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/fragility-grid.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-fragility-grid-01/memory-report.md`

**Memory analysis report SHA-256:** 01b3e6467c68a466f624780adef84bac6584c556040e3701b8ac9ada204f3c26

## Boundary and evidence

Target class: returning computation. Boundary kind: subsystem-only. The model-dependent grid collector, its consumed inference/dataset/parsing helpers, supplied shell resume driver and downstream artifact loader qualify without an autonomous agent loop. Include generation versus likelihood scoring, vLLM/HF/auto alternatives, fixed question selection, correctness records, summary and resume/analysis read-back. Exclude other experiment entrypoints, complete statistical/plot analysis, published result contents, hardware/cloud setup, external model/tokenizer/dataset/dependency implementations. Only the consumed _load_mcq function is included from brittleness.py.

Source-only code-grounded inspection on 2026-09-25 at full commit 3f51444ead009d8351de1b6b19bf901c4da3d420. Sole repository https://github.com/NikolaTesla-007/fragility-grid at `/home/zby/llm/commonplace/related-systems/NikolaTesla-007--fragility-grid`; all evidence reads commit-addressed. No worktree, prior analysis, ingest or released empirical-result evidence. No target inference, download, benchmark, dependency installation or source test execution.

## Source register

| Source ID | Kind | Identity/location | Revision | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | Git | https://github.com/NikolaTesla-007/fragility-grid | 3f51444ead009d8351de1b6b19bf901c4da3d420 | implementation | collector, consumed helpers, driver and later loader | `repro/fragility_grid.py:54-210`; `repro/fragility_lib.py:45-167`; `repro/inference.py:28-257`; `repro/common.py:21-61,81-111,194-228`; `repro/prompt_format.py:31-43`; `repro/brittleness.py:225-262`; `repro/prompt_format_lib.py:18-54`; `repro/run_fragility.sh:12-84`; `repro/fragility_analysis.py:35-55,300-305,586-623` | external resolved assets/backend internals and full downstream methods excluded; no empirical correctness, reproducibility or causal finding |
| SRC-2 | Git | https://github.com/NikolaTesla-007/fragility-grid | 3f51444ead009d8351de1b6b19bf901c4da3d420 | doctrine/design | README and source claims | `README.md`; `repro/fragility_grid.py:1-20`; `repro/fragility_lib.py:1-23,42-44`; `repro/run_fragility.sh:1-7` | research claims not independently reproduced; comments not execution evidence |

## Shared records

### Components

CMP-1 — Grid collector, shell model queue and file pipeline. Source-wired symbolic orchestration of a bounded experiment; no planning model or adaptive curriculum. Caller controls models, benchmark set, sample size, permutations, backend and output environment. SRC-1 `repro/fragility_grid.py:150-206`; `repro/run_fragility.sh:36-84`.

CMP-2 — Selected causal language model/tokenizer loaded through ModelSpec and vLLM or Transformers. Source-wired distributed-parametric inference; auto selects vLLM if importable else HF, explicit vLLM does not fall back. Model names, quantization, dtype and parallelism resolve at load time without immutable weights/tokenizer revision arguments on these paths. HF model.eval and no_grad govern scoped inference, with no optimizer/adaptation path in these functions; external backend internals remain uninspected. Load-time quantization is numerical representation, not learned memory. Exact asset identity is not established by the source commit. SRC-1 `repro/inference.py:47-108,141-157,193-257`; `repro/common.py:81-111,198-228`.

>     tok = AutoTokenizer.from_pretrained(spec.name)
>     model = AutoModelForCausalLM.from_pretrained(spec.name, **kwargs)
>     model.eval()
>     return tok, model
> --- `repro/common.py` @ `3f51444ead009d8351de1b6b19bf901c4da3d420`

CMP-3 — Prompt formatters, label parsers, inverse permutation mapper and gold-index checker. Source-wired deterministic scoring after opaque parametric inference. Dataset author supplies gold, not another model judge. Fixed parsers do not establish semantic answer fidelity. SRC-1 `repro/prompt_format_lib.py:18-54`; `repro/fragility_grid.py:71-105`.

### Operative objects

OBJ-1 — Static benchmark input, options, gold, configuration/permutation and formatter definitions. Imported question strings have instruction-like text capacity at the model consumer, but no separate authority/trust check is wired. Dataset answers are accepted by the scorer. No accumulated memory classification. SRC-1 `repro/prompt_format.py:31-43`; `repro/brittleness.py:225-262`; `repro/fragility_lib.py:45-116`.



OBJ-2 — Invocation-local batched prompts, generated strings, scores, bits, margins and unparsed counters. Natural-language responses and symbolic scores are converted to evidence; raw strings and full option score vectors are not persisted by this grid. SRC-1 `repro/fragility_grid.py:61-119`.



OBJ-3 — Files: question/gold/model/benchmark/item identifier, bits, one likelihood margin and parse-count JSONL; numeric per-model summary; shared symbolic legend. Lineage combines imported question text, trace-extracted scoring and configuration compilation. Consumer authority: evidence for analysis, routing metadata for scheduler/config selection. Raw generation and option text are absent from record fields. SRC-1 `repro/fragility_grid.py:107-112,122-176`; `repro/fragility_lib.py:107-116`; `repro/fragility_analysis.py:35-55,300-305`.



OBJ-4 — Temporary queue/lock and per-model log files. Queue contains configured model identifiers; it is destructive dispatch state, not a durable cross-invocation checkpoint. Logs retain stdout/stderr; availability for diagnosis is explicit, but no model read-back is wired. SRC-1 `repro/run_fragility.sh:47-79`.



### Routes

RTE-1 — Schedule/load. Shell locks a temporary queue and runs one selected model subprocess per GPU; direct CLI iterates models. Python writes a shared config legend before inference, resolves ModelSpec and loads selected engine. Default six permutations generate 24 format/order cells plus two likelihood cells. Permutation seed99 retains identity first. Data shuffle seed1234 selects n evaluation items after a reserved five-item pool, which this zero-shot grid does not use. MMLU and other dataset loads lack immutable revision arguments; ARC filters to four choices, TruthfulQA keeps correct plus first three distractors and reindexes gold to zero. Source-wired selection, not universal dataset neutrality. SRC-1 `repro/fragility_grid.py:54-80,150-166`; `repro/fragility_lib.py:81-115`; `repro/prompt_format.py:31-43`; `repro/brittleness.py:225-262`; `repro/run_fragility.sh:47-75`.

> def load_bench(name, n, seed=1234):
>     import random
>     if name == "mmlu":
>         from datasets import load_dataset
>         ds = load_dataset("cais/mmlu", "all", split="test").shuffle(seed=seed).select(range(n + 5))
>         data = [(ex["question"], ex["choices"], ex["answer"]) for ex in ds]
>     else:
>         data = _load_mcq(name)
>         random.Random(seed).shuffle(data)
>         data = data[: n + 5]
>     fewshot_pool = data[:5]
>     eval_items = data[5: n + 5]
>     return eval_items, fewshot_pool
> --- `repro/prompt_format.py` @ `3f51444ead009d8351de1b6b19bf901c4da3d420`

Engine initialization catches GatedAccessError and skips that model. HF loader explicitly raises it for missing gated-model token; equivalent vLLM access errors are not normalized by this adapter. Other load/evaluation failures can abort that subprocess. Credentials/assets/services are runtime dependencies, not supplied grants from this analysis.

Operator supplies model/grid/dataset configuration; Python creates result directories and rewrites legend; shell builds fresh queue. No retrieval of past answers enters setup. SRC-1 `repro/fragility_grid.py:150-166`; `repro/run_fragility.sh:36-42,72-77`.



RTE-2 — Generation scoring. Build all configuration×item messages with a user role, shown permuted options and no demonstrations. Request greedy eight-token chat by default; parse first standalone A-D or1-4 token, map shown position to original option and compare with gold. Unparsed output counts as wrong. Because parser accepts first matching token anywhere, deterministic parsing alone does not prove it extracted intended answer. Current engine outputs are zipped with metadata without an independent length assertion. Source-wired; no output observed. SRC-1 `repro/fragility_grid.py:71-93`; `repro/prompt_format_lib.py:46-54`.

> def parse_letter(text, options=None):
>     t = text.strip().upper()
>     m = re.search(r"\b([A-D])\b", t)
>     return LETTERS.index(m.group(1)) if m else None
> 
> 
> def parse_digit(text, options=None):
>     m = re.search(r"\b([1-4])\b", text.strip())
>     return int(m.group(1)) - 1 if m else None
> --- `repro/prompt_format_lib.py` @ `3f51444ead009d8351de1b6b19bf901c4da3d420`

HF generation truncates input to configured max_model_len4096 and halves an OOM chunk until one, then rethrows. vLLM uses its own max length/engine behavior. Chat rendering tries disabling thinking, falling back only on TypeError. Seed1234/T0 are controls, not a deployment guarantee of byte-identical output across assets/hardware/backend versions. Source-wired limits. SRC-1 `repro/inference.py:37-59,111-129,193-247`.

Zero-shot generation: all generation configurations × items enter one chat API batch per benchmark, then parsed choice is inverse-mapped and compared with gold; unparsed outputs count wrong. Eight new tokens and temperature zero are grid defaults. SRC-1 `repro/fragility_grid.py:54-93`.

>                 shown = [opts[i] for i in perm]
>                 prompt = fmt(q, shown, "")
>                 batch.append([{"role": "user", "content": prompt}])
>                 meta.append((c.key, c.fmt, c.perm_index, ix, gold))
>         if batch:
>             outs = engine.chat(batch, max_new_tokens=max_new_tokens, temperature=0.0)
> --- `repro/fragility_grid.py` @ `3f51444ead009d8351de1b6b19bf901c4da3d420`

>         enc = tok(chunk, return_tensors="pt", padding=True, truncation=True,
>                   max_length=self.max_model_len).to(self._model.device)
> --- `repro/inference.py` @ `3f51444ead009d8351de1b6b19bf901c4da3d420`

RTE-3 — Option-likelihood scoring. Two cloze stems omit answer labels/options from the prompt and score each option as its appended continuation. HF computes mean token log probability from separately tokenized prefix/full strings; vLLM requests prompt logprobs and extracts continuation means. Argmax is checked against gold; plain-cloze top-two score margin is retained. This is a different operational test from short labelled generation, not a proved neutral measurement of one latent ability. Source-wired; tokenization/backend correctness and actual scores unobserved. SRC-1 `repro/fragility_grid.py:95-105`; `repro/fragility_lib.py:53-65`; `repro/inference.py:132-191`.

>             full = prompt + " " + opt
>             pi = self._tok(prompt, return_tensors="pt").input_ids
>             fi = self._tok(full, return_tensors="pt").input_ids.to(self._model.device)
>             logits = self._model(fi).logits  # [1, T, V]
>             logp = _t.log_softmax(logits[:, :-1, :], dim=-1)
>             target = fi[:, 1:]
>             tok_lp = logp.gather(2, target.unsqueeze(-1)).squeeze(-1)[0]
>             cont_len = fi.shape[1] - pi.shape[1]
>             cont_lp = tok_lp[-cont_len:] if cont_len > 0 else tok_lp[-1:]
>             scores.append(float(cont_lp.mean().item()))
>         return scores
> --- `repro/inference.py` @ `3f51444ead009d8351de1b6b19bf901c4da3d420`

Likelihood: each cloze configuration requests option continuation scores; mean token scoring selects argmax; only plain-cloze top-two margin retained. No adaptive configuration selection. SRC-1 `repro/fragility_grid.py:95-105`; `repro/inference.py:141-191`.

>             pairs = [(stem(q, opts, ""), opts) for (q, opts, _g) in items]
>             all_scores = engine.score_options_many(pairs)   # one generate() call for all items
>             for ix, (scores, (_q, opts, gold)) in enumerate(zip(all_scores, items)):
>                 pred = max(range(len(opts)), key=lambda i: scores[i])
>                 bits[ix][c.key] = int(pred == gold)
> --- `repro/fragility_grid.py` @ `3f51444ead009d8351de1b6b19bf901c4da3d420`

RTE-4 — Summarize/persist/cleanup. Collector derives class and accuracy summaries from bit dictionaries, collects all benchmark records in memory, frees engine in finally, then directly overwrites per-benchmark/model JSONL and per-model JSON summary. Model process exit is still needed for full vLLM worker release. Records contain question/gold/positional item ID/model key/bits/margin/unparsed count; they omit options, raw answers, full option scores and resolved asset hashes. Writes have no atomic replacement or per-item recovery checkpoint on this path. Interruption may leave partial files; no transaction rolls back prior files. Source-wired retention. SRC-1 `repro/fragility_grid.py:107-147,165-194`; `repro/common.py:55-61`; `repro/inference.py:249-257`.

>         recs = []
>         for ix, (q, opts, gold) in enumerate(items):
>             recs.append({"benchmark": bench, "item_id": f"{bench}-{ix}", "question": q,
>                          "model": model_key, "gold": gold, "bits": bits[ix],
>                          "ll_margin": ll_margin[ix], "n_gen_unparsed": n_gen_unparsed[ix],
>                          "n_gen_configs": len(gen_cfgs)})
> --- `repro/fragility_grid.py` @ `3f51444ead009d8351de1b6b19bf901c4da3d420`

> def classify_item(bits: Dict[str, int]) -> str:
>     """robust_correct = correct under every config; robust_wrong = wrong under every config;
>     fragile = correctness varies across configs (the 'least sure' items)."""
>     vals = list(bits.values())
>     if not vals:
>         return "empty"
>     if all(v == 1 for v in vals):
>         return "robust_correct"
>     if all(v == 0 for v in vals):
>         return "robust_wrong"
>     return "fragile"
> --- `repro/fragility_lib.py` @ `3f51444ead009d8351de1b6b19bf901c4da3d420`

Optional PURGE_WEIGHTS=1 deletes the downloaded model repository cache after successful record/summary writes; errors are printed. This controls disk use, not learned-knowledge withdrawal. We did not run it. Result files survive until overwritten/deleted externally; no built-in version lineage of reruns is established.

After all requested benchmarks return for a model, free engine, overwrite each benchmark/model record file, derive summary, overwrite summary. Legend precedes model evaluation. PURGE_WEIGHTS removes downloaded checkpoint cache only. SRC-1 `repro/fragility_grid.py:150-194`; `repro/common.py:55-61`.

>         summ = summarize_model(key, per_bench, perms_k)
>         with open(SUMMARY_DIR / f"{key}.json", "w", encoding="utf-8") as f:
>             json.dump(summ, f, indent=2, default=str)
> --- `repro/fragility_grid.py` @ `3f51444ead009d8351de1b6b19bf901c4da3d420`

RTE-5 — Resume and later analysis. Shell skip predicate is merely existence of summary/<model>.json. It does not check configuration, dataset/model identity, completeness or even parse that summary; a partial/stale file can suppress work. Direct Python invocation does not implement this skip. Python results honor RESULTS_DIR while shell SUMMARY_DIR is fixed to ../results, so externally changed output root may diverge from resume detection. Model failures are logged and driver continues to CPU analysis. Loader glob-selects all matching JSONL filenames, keys by benchmark/model and positional item_id, then consumes bits; duplicate IDs overwrite earlier entries. Shared legend is separately loaded when present. No pinned run manifest or compatibility check binds files in this loader. Full statistical consumers are excluded, so we establish delivery to analysis, not its causal claims. Source-wired. SRC-1 `repro/run_fragility.sh:42-84`; `repro/common.py:21-23`; `repro/fragility_analysis.py:35-55,586-597`.

>     if [ -f "$SUMMARY_DIR/$m.json" ]; then
>       echo "[gpu$gpu] skip $m (summary exists)"; continue
>     fi
> --- `repro/run_fragility.sh` @ `3f51444ead009d8351de1b6b19bf901c4da3d420`

Later shell checks model summary path; later CPU main requests retained record maps and dispatches analysis. Record loader scans all matching filenames, derives model/benchmark identity from filenames, retains item_id→bits and discards other fields. Pull, wired; no per-run namespace or provenance compatibility check here. SRC-1 `repro/run_fragility.sh:55-64,81-82`; `repro/fragility_analysis.py:35-55,586-592`.

>     for p in sorted(RECORDS_DIR.glob("*__*.jsonl")):
>         bench, model = p.stem.split("__", 1)
>         with open(p) as f:
>             for line in f:
>                 r = json.loads(line)
>                 recs[model][bench][r["item_id"]] = r["bits"]
> --- `repro/fragility_analysis.py` @ `3f51444ead009d8351de1b6b19bf901c4da3d420`

RTE-6 — each shell worker requests queue head under flock, deletes the first line, then checks summary and runs or skips. Temp queue is built per invocation and removed after wait. Raw logs are overwritten per executed model; final shell grep requests outcome-shaped lines in model logs. The worker's own OK/FAILED echo is outside the redirected subprocess, so that grep need not find its intended status lines. SRC-1 `repro/run_fragility.sh:47-79`.

>   exec 9>"$LOCK"; flock 9
>   local m; m="$(head -n1 "$QUEUE")"
>   [ -n "$m" ] && sed -i '1d' "$QUEUE"
>   flock -u 9; exec 9>&-
>   printf "%s" "$m"
> --- `repro/run_fragility.sh` @ `3f51444ead009d8351de1b6b19bf901c4da3d420`

RTE-7 — CPU analyze explicitly requests shared legend; selects n_perms from _meta or fallback six, then reconstructs config keys from current source. Other legend content is not used by this selection prelude. Pull and routing authority, not a model-memory push. SRC-1 `repro/fragility_analysis.py:51-55,300-305`.

> def analyze(recs, models, benches):
>     legend = load_legend()
>     n_perms = legend.get("_meta", {}).get("n_perms", 6)
>     ref_key = F.REF_CONFIG_KEY
>     all_keys = [c.key for c in F.enumerate_configs(n_perms)]
> --- `repro/fragility_analysis.py` @ `3f51444ead009d8351de1b6b19bf901c4da3d420`

### Claims

CLM-1 — Source comments claim a reproducible grid and resumable execution, and frame deterministic parsers as excluding parser noise. Conclusion status: claimed. Fixed sampling/config ordering/seeds and a file-existence resume route are wired; immutable assets, parser semantic fidelity, atomic output and compatible-resume validation are not established by them. Research descriptions of rankings/fragility are not observed or causal evidence here. SRC-2 `repro/fragility_grid.py:1-14`; `repro/fragility_lib.py:1-23,42-44`; `repro/run_fragility.sh:1-7`.

> For each model x MCQ benchmark, evaluate the SAME fixed item set under every configuration in
> the grid (generation x {formats} x {orderings}  +  loglikelihood x {stems}) and record, per item,
> a correctness bit for each config. Deterministic: greedy generation (T=0) + loglikelihood, single
> seed -- so the whole tensor is reproducible and matches how real static leaderboards score.
> --- `repro/fragility_grid.py` @ `3f51444ead009d8351de1b6b19bf901c4da3d420`

### Evidenced absences

ABS-1 — Conclusion status: absent. Bounded absence: no trace-derived guidance returned to inference, weight training, retained-memory curation, or memory editor in the inspected grid, shell and used helper/loader paths. Raw output retention/aggregation and filesystem completion checks do not supply those routes. SRC-1 `repro/fragility_grid.py:54-194`; `repro/inference.py:111-257`; `repro/run_fragility.sh:47-82`; `repro/fragility_analysis.py:35-55,300-305,586-592`. Excludes external dependency internals and empirical execution evidence; does not assert their global absence.



Search boundary at the frozen commit: full source route enumeration of the ranges named on this record and pinned textual query `optim|backward|train\(|retrieve|memory|summary|load_records|load_legend` in the grid, inference, shell and analysis modules. Matches identify summaries, loader entrypoints and compute-memory comments, not a guidance-to-model, training or semantic-maintenance route. The negative rests on traced consumers and writers, not the lexical miss alone; full downstream methods and dependencies remain excluded.

### Behavioral-authority paths

BAP-1 — Static formatted question enters selected model as user message; likelihood path supplies raw cloze continuation. Instruction force is at model input interface, limited to current answer. Static dataset/configuration is not automatically memory read-back. Source: SRC-1 `repro/fragility_grid.py:71-105`; no additional memory authority inferred from static input.

BAP-2 — Parsed label/gold comparison determines correctness bits; stored filename/existence controls resume and retained records supply numerical analysis. Enforcement at deterministic consumers licenses those operational decisions, not universal warrant for model knowledge or rank. Source: SRC-1 `repro/run_fragility.sh:47-64`; `repro/fragility_analysis.py:35-55,300-305`. Retained evidence and routing are the specialist-supported authorities; static gold validation lies outside its memory profile.

## Runtime account

Caller launches CLI or shell with model keys and experiment settings. Shell uses a locked queue and summary-existence skip; Python constructs a legend, loads model and fixed question sample, runs generation and likelihood cells, scores against dataset gold, frees model and writes records/summary. Shell later dispatches CPU analysis across retained files. Terminal product is measurement records, not a tool action or installed improved agent. No human approval occurs inside model/scoring route; caller's filesystem/network/GPU authority determines effect envelope. Token/cache access comes from environment; isolation depends on host, not a sandbox here.

Alternate paths are direct CLI versus shell, HF/vLLM/auto and generation/likelihood. Their context handling, recovery and skip semantics differ and cannot inherit a single universal guarantee. Static forcing cases: HF OOM retries smaller batches but fails at size1; unparsed output yields zero; existing stale/partial summary skips inference; interrupted direct writes can leave loader-visible partial/mixed data. No dynamic check planned. Parser unit tests or a GPU smoke run were considered, but static branches determine these bounded findings; a run would not validate all assets, task labels or reproducibility environments. No installed packages, services, credentials or model calls were needed.

Revision admission is caller-selected config/source/assets, not automated product improvement. Grid varies prompts/scorers according to a fixed schedule, with no evidence-consuming selection that installs a new model, best prompt or changed grid for future inference. Summary overwrites are automatic derived-measurement writes; rejection is only errors/skip, with no semantic adoption review or retained rollback version. External dataset authors provide answer oracle; open-world truth beyond labels is not independently assessed. Operation is bounded experimentation, not open requests/curriculum. Underlying model theories or inaccessible reasoning remain uninspected rather than declared absent.


| Route | Immediate return and later consumer | Selection, expiry, visibility and effect bounds |
|---|---|---|
| RTE-1 | Engine/input/grid and queue; current inference | Static caller keys/seeds; legend overwritten; no past answer delivery |
| RTE-2 | Generated strings, parsed bits; current collector | Format×permutation×items, eight-token output, backend context limits; no later model readback |
| RTE-3 | Scores/bits/margin; current collector | Fixed cloze stems and all options; no adaptive cell selection or outcome-conditioned inference |
| RTE-4 | Files/summary; later scheduler and CPU loader | Model/benchmark filenames; direct overwrite, no semantic expiry; optional parameter-cache purge unrelated to memory guidance |
| RTE-5 | Skip decision or record map; model scheduler/analysis | Summary exists; filename glob/item IDs; incompatible retained runs can mix, influence not empirically measured |
| RTE-6 | Queue head removed, skip/run and logs; next worker/operator | Flock and model identity; queue deleted after wait, logs overwritten per execution; no automatic recovery of failed item |
| RTE-7 | n_perms and reconstructed keys; numerical analysis | Shared legend _meta or fallback six; current source reconstructs; no identity/freshness contract |

## Lens scoping

### Memory/context scope

Brief lens on retained evaluation records, legend, shell operational state and later resume/analysis consumers; no presumed agent-memory layer. Include all active backend/scoring/driver alternatives; static prompt/dataset/model assets differ from use-accumulated material. Mandatory fourteen-axis profile supplied by fresh specialist.

### Epistemic scope

Full lens because correctness and fragility claims depend on label parsing, gold authority, deterministic derivations and retained-output consistency. Exclude complete downstream statistics and empirical paper claims; no actual candidate/model run observed.

## Lens outputs

### Memory/context lens


Acquisition is automatic after launch. Benchmark loader shuffles with seed 1234, reserves the first five items for a few-shot pool, and returns the next N for evaluation; this grid ignores the pool. MMLU requests its test split; the helper selects HellaSwag validation, four-choice ARC Challenge test rows, and TruthfulQA validation with the correct choice plus the first three distractors. These are static input transformations, not memory evolution. SRC-1 `repro/prompt_format.py:31-43`; `repro/brittleness.py:225-262`:


Trace-to-artifact chain is OBJ-2 model outputs → parsed/mapped correctness bits plus counters/margin → OBJ-3 JSONL → CPU evidence maps. Immediate summaries reduce those invocation-local bits into numerical statistics before initial persistence. They neither prescribe future answer behavior nor retain a reason for a prescription. The scheduler reads no summary rationale or numerical content; existence alone changes scheduling. Therefore this transformation does not establish trace learning, memory consolidation, or explanation read-back.

A separate write compiles the legend from current permutations and configuration names; it is overwritten for each Python run despite the source comment saying “once.” This shared file can be replaced while older model records remain. Queue deletion is dispatch acknowledgment, not semantic forgetting. There is no manual adoption workflow or semantic withdrawal operation. Arbitrary local editing remains possible because these are ordinary files, but no authored edit route is defined in the scoped code. SRC-1 `repro/fragility_grid.py:153-156`; `repro/fragility_lib.py:107-116`; `repro/run_fragility.sh:47-53,72-77`:


File loss and overwrite are operationally significant: evaluating a model must finish all requested benchmarks before any of that model's records are written; writes then proceed individually, followed by summary. Inference failure exits after finally freeing the engine, before this write sequence. An interrupted record/summary write has no temp-file promotion or validity check in this code. Old files for benchmarks not included in a later invocation are not removed. SRC-1 `repro/fragility_grid.py:165-176`. Weight purge, SRC-1 `repro/fragility_grid.py:179-194`, is storage cleanup of downloaded external parameters, not decay of learned memory.



The shell worker is the named requesting consumer for model queue identifiers and file-existence metadata. Its request selects the queue head and the summary named by that key; it never reads answers or summary contents. CPU main is the named requesting consumer of records; its loader consumes every matching JSONL file, without a record budget or run filter, then passes a nested bits map to analysis. Legend loading is requested inside analysis. These are concrete file read routes, not hypothetical APIs and not an automatic memory selector feeding an LLM.


SRC-1 `repro/fragility_analysis.py:300-305` establishes that selection; `repro/fragility_analysis.py:35-55` establishes file loading. No retained record crosses back to RTE-2 or RTE-3. Availability of logs is separate from delivery to a human: the script points failures to their log path, but no human diagnosis or benefit was observed.

Context volume is determined by the fixed grid: four generation formats times the selected four-option permutations, each applied to all selected items; two likelihood stems. The outer batch grows with configurations × items, while each model request remains one formatted item or stem-plus-option. The engine defaults to 4096 context tokens; HF generation tokenization explicitly truncates to that bound, while vLLM receives max_model_len. HF generation retries an OOM chunk at half its size until one; likelihood HF calls and vLLM calls have different batching paths. These compute limits are not memory retrieval budgets. SRC-1 `repro/fragility_lib.py:45-116`; `repro/inference.py:47-59,77-90,141-191,193-247`:


Trust/provenance limits: record keys identify model/benchmark and item position, but the persisted schema has no checkpoint digest, dataset revision, backend, tokenizer identity, prompt text, full option list, or executed source digest. Common loaders use external repository names without revision arguments. Source pinning here does not pin those dependencies. CPU loader trusts filename identity and JSON contents; question/gold/margins remain in files but the inspected record loader delivers only bits indexed by item_id. SRC-1 `repro/fragility_grid.py:107-112,122-147`; `repro/inference.py:77-103`; `repro/common.py:225-228`; `repro/prompt_format.py:31-43`; `repro/fragility_analysis.py:40-45`.



OBJ-3 and OBJ-4 establish file retention with both symbolic and natural-language contents. Neither fixed pretrained weights nor dependency caches count as memory formed by this subsystem. OBJ-2 is invocation-local acquisition state and is excluded from the retained-store axis, though its derivation is necessary to explain OBJ-3. Imported question text, compiled configuration/queue identifiers and trace-extracted measurements account for the complete lineage union within this boundary.

RTE-5, RTE-6 and RTE-7 establish knowledge/evidence and routing authority at the actual consumers. Gold-answer validation occurs on static OBJ-1, outside the memory profile. No instruction, enforcement, learned parameters or ranking directive is delivered from retained memory to the evaluating model. Statistical ranking outputs after the loader are outside scope, so this report does not classify their consumption.

Read-back is pull because each named consumer explicitly requests files or their status. Operator-triggered whole-pipeline execution is not a second push route. Accordingly read_back_signal is inapplicable despite filenames and model identifiers. Trace extraction describes lineage, while trace learning additionally requires durable behavior guidance; measurement records and summary-existence status do not establish that. The four learning descriptors are consequently inapplicable, and ABS-1 bounds the negative curation finding. Faithfulness remains not-determinable because no retained run evidence was admitted, not because a source-only inspection proved no test exists anywhere.


### Epistemic lens

1. Source-and-claim boundary: SRC-1 selected collection/consumer subsystem at pinned commit; SRC-2 reproducibility/resume/parser claims CLM-1. Question is what these measurements and their later reuse warrant, not whether published rankings are correct. External gold/model semantics, resolved assets and empirical traces are missing, preventing performance or causal attribution.

2. Object inventory: OBJ-1 imports question/options/gold with source-author warrant uninspected; formatting/permutation reshapes these inputs without establishing unchanged difficulty. OBJ-2 contains model answer/score (semantic relation to intended answer indeterminate), plus symbolically derived correctness bits/margins (entailed only under parser, chosen options and gold premises). OBJ-3 stores derived records/summary/legend, not independently validated claims. OBJ-4 queue/log/existence is operational state; no candidate truth-apt content is required for its scheduling role.

3. Authority-route ledger (all architectural statuses implemented, no candidate instance observed):

| Route/function | Target, transformation and evaluator | Force, timing and warrant limit |
|---|---|---|
| RTE-1 acquisition | OBJ-1 external dataset import and fixed sample/config selection | dataset gold granted local scoring authority; accuracy of labels uninspected |
| RTE-2 content transformation | OBJ-1 to model output within OBJ-2; semantic relation indeterminate | short-answer generation, model assertion only before parsing |
| RTE-2 check/evidence production | parsed option within OBJ-2 compared to supplied gold | deterministic bit under encoding assumptions; malformed/ambiguous output can alter score |
| RTE-3 content transformation | option likelihoods from model; then argmax/gold derivation | separate task interpretation; mean normalization does not prove measurement equivalence |
| RTE-4 content transformation | bits to counts/bands; entailed numerical derivation | fragile means variation across chosen grid, not demonstrated cognitive uncertainty |
| RTE-4 retention | OBJ-3 measurement files, no new semantic content on serialization | preserves selected fields and loses raw-output/asset provenance; no independent acceptance transition |
| RTE-5 operational admission | OBJ-4 summary existence, no content change | permits skip immediately, without freshness/completeness warrant |
| RTE-5 consumption | OBJ-3 glob/key-selected records to downstream analysis, no new claim in loader | retained input for external method; no within-boundary grant of causal inference |

4. Lifecycle dispositions: OBJ-1 acquisition/import, discovery lifecycle not applicable; gold warrant inherited only within dataset scope and remains untested here. OBJ-2 answer interpretation is indeterminate (plausible assertion or mere label); no instance observed, no retained explanatory conjecture or content criticism established. Correctness bits and margins are entailed derivations under given scorer/gold premises, discovery lifecycle not applicable. OBJ-3 non-ampliative serialization and summary derivation; retention is implemented, epistemic acceptance and post-acceptance theory integration are not established. No lifecycle record for OBJ-4: no candidate truth-apt output for this object; relevant operational-update routes RTE-1 and RTE-5. Evaluating a model's answers does not alone identify an operative formulated theory held open to criticism.

5. Claim comparison: CLM-1 receives implementation support for deterministic grid construction, explicit inference settings and summary-existence resumption. It receives no observed-run or causal support in this analysis. Source path lacks exact resolved-asset pinning and resume compatibility checks; deterministic regex is not a proof of semantic parsing. Choosing a configuration as equally defensible or defining fragility as uncertainty needs argument/evidence beyond loop mechanics. No published empirical findings are adopted.

6. Bounded conclusion: RTE-2 and RTE-3 produce locally scored answer comparisons; RTE-4 derives and retains descriptive summaries; RTE-5 reuses measurement files and skips presumed-complete work. These routes can support a bounded experiment when their inputs and conditions are controlled, but source reconstruction alone neither reproduces an empirical effect nor validates its interpretation. They do not establish autonomous theory revision, learned model memory or improved future capacity.

## Reconciliation

Verified complete specialist report, run/source/pin, unchanged input/method and hash above. Mapped MEM-RTE-1 → RTE-6; MEM-RTE-2 → RTE-7; MEM-ABS-1 → ABS-1. Existing IDs retain their referents; no new objects needed. All five issues accepted: writes follow all model benchmarks and are non-atomic; summary existence is not valid completion; loader consumes bits from records and n_perms from legend, not summary content; hardcoded shell path can diverge from Python RESULTS_DIR; deterministic/parser/reproducibility claims remain qualified. Baseline independently identified these shared failure boundaries; convergence does not upgrade static evidence. Added legend-selection prelude to SRC-1 as the supplied source-native consumer boundary, not full downstream statistics. No unresolved conflict. All specialist quote passages integrated at supporting canonical records or already-covered data/skip excerpts, without lens duplication.

## Bounded synthesis

The strongest supported contribution is an inspectable collector that compares fixed items across explicit formatting/order/scoring alternatives and retains per-item correctness for later analysis. Its most consequential limits are parser/gold dependence, backend/context differences, incomplete output provenance and existence-only resume. A source pin alone does not freeze model/tokenizer/dataset resolution or make mixed retained runs comparable.

Conjectural learning and self-improvement remain uninspected: scored comparisons are not evidence that criticism of an operative formulated theory improved future capacity, and no such system revision is observed. Reflection is wired narrowly through retained completion-file state that alters future scheduling; it represents presumed work completion, not a self-theory or verified progress. Controlled asset-pinned runs with complete provenance and explicit freshness checks would change reproducibility conclusions; they would not automatically establish learning.

## Limitations

| Limitation | Affected IDs | Inspected boundary | Conclusion prevented | Evidence needed |
|---|---|---|---|---|
| External assets/backend semantics | CMP-2, OBJ-1 | loader names/config only | exact inference/data reproducibility or parametric internals | immutable resolutions and validated execution environment |
| Parser/gold assumptions | CMP-3, RTE-2, RTE-3 | mechanical scoring | semantic answer fidelity, neutral comparison of latent capability | retained raw answers/options and validity checks |
| File-level recovery | RTE-4, RTE-5 | direct writes/glob/existence | atomic completion or compatible run corpus | manifests, atomic completion and identity checks |
| No observed runtime | all implementation records | static code | numerical effects, faithfulness, model improvement | retained controlled executions |
| Full downstream methods excluded | RTE-5 | loader/main only | published statistical/causal claims | separately scoped method and empirical audit |
| Completion/log diagnostics | RTE-6 | shell status echo outside redirected subprocess | intended summary grep reports every model outcome | observed retained shell/subprocess logs |
| Shared legend/current-source reconstruction | RTE-7 | n_perms fallback/selection only | frozen compatible configuration semantics across files | run-bound legend and asset identity validation |

## Verification and blockers

### Semantic verification

Boundary is a returning computation, not agent runtime. Model resolution differs from parameter adaptation; fixed labels are task oracles, not universal truth tests. Static data and current batch state are not assumed memory. Both inference/scoring and direct/shell alternatives remain visible; failure/skip/persistence claims stay at their enforcement points. Integrated seven routes/four objects. Memory profile is explicitly narrower than runtime objects: retained files OBJ-3 and OBJ-4 only; static datasets/models/templates, transient inference/loader state and excluded statistical outputs are not retained stores. Imported questions, compiled configuration/queue and trace-extracted measurements exhaust scoped lineage. All readback is requested file/status pull; identifiers/globs do not establish push, so signal is inapplicable. Trace-learning no is bounded to routes RTE-2 through RTE-7/ABS-1: output becomes evidence, not guidance returned to model. Summary-existence scheduling does not supply a learned prescription. Learning source/scope/timing/form are correspondingly inapplicable; raw aggregation/overwrite/cache deletion not semantic curation. Faithfulness remains not-determinable without observed dependence evidence. Narrow operational reflection does not conflict with absence of memory learning or establish improved capacity.

### Deterministic validation

Full exact-result validation and guarded pinned-source quote/anchor checks follow specialist integration.

### Blockers

none
