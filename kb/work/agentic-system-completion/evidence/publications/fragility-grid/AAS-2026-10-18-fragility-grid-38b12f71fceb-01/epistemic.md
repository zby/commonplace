---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Epistemic routes of fragility-grid: dataset-relative correctness, configuration statistics and the limits of leaderboard interpretations."
run-id: AAS-2026-10-18-fragility-grid-38b12f71fceb-01
reviewed-boundary: "3f51444ead009d8351de1b6b19bf901c4da3d420"
---

# fragility-grid epistemic report

## Source-and-claim boundary

The question is how this evaluation workflow turns benchmark inputs and model outputs into correctness measurements and claims about leaderboard instability. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identity is see [Source register](boundary.md#source-register), SRC-1. This is the selected fragility-grid subsystem, including its shipped driver and CPU consumer, not the repository's other experiments or an autonomous agent runtime.

All additional reads below are implementation evidence at the frozen commit, except README and source comments, which supply doctrine/design or attributed results. No target execution, test execution, provider calls or experiments were performed. Shipped result values remain uninspected: their presence cannot identify the routes that produced or accepted them. External dataset, tokenizer, checkpoint and backend bytes are not frozen. This prevents authenticated reproduction, assessment of dataset truth, model-internal reasoning and backend numerical equivalence. Lack of run evidence prevents conclusions about actual activation, released numeric results or benefit. No causal experiment was inspected.

| Entry point or operation | Source path | Coverage and records |
|---|---|---|
| Shell launch, skip, child failure and CPU handoff | SRC-1 `repro/run_fragility.sh` | Direct complete read; see [RT-RTE-sweep-driver](runtime.md#rt-rte-sweep-driver), [RT-BAP-summary-skip](runtime.md#rt-bap-summary-skip). |
| Collector CLI, smoke cap, direct multi-model invocation, overwrite and purge | SRC-1 `repro/fragility_grid.py` | Direct complete read; see [RT-RTE-generation-grid](runtime.md#rt-rte-generation-grid), [RT-RTE-likelihood-grid](runtime.md#rt-rte-likelihood-grid), [RT-RTE-record-analysis](runtime.md#rt-rte-record-analysis). No registered tools or hooks in these inspected entry points; fixed CLI dispatch owns progression. |
| Input loading and gold construction | SRC-1 `repro/prompt_format.py`, `repro/brittleness.py` | Direct `load_bench` and `_load_mcq` reads; see [EPI-OBJ-benchmark-items](#epi-obj-benchmark-items). Other experiment bodies excluded, not assessed. |
| Format, permutation, parsing and correctness | SRC-1 `repro/prompt_format_lib.py`, `repro/fragility_lib.py`, `repro/fragility_grid.py` | Direct complete reads; see [EPI-RTE-label-extraction](#epi-rte-label-extraction), [EPI-RTE-gold-comparison](#epi-rte-gold-comparison). Standalone fuzzy-restatement route is not enumerated by this collector. |
| Generation, score extraction, template fallback, retry and release | SRC-1 `repro/inference.py`, `repro/common.py` | Direct complete adapter read and shared `load_model` read; see [RT-CMP-roster-model](runtime.md#rt-cmp-roster-model), [RT-RTE-backend-recovery](runtime.md#rt-rte-backend-recovery). External implementations uninspected. |
| CPU record import, alignment, statistics, ranking, subset selection, JSON and all four figure consumers | SRC-1 `repro/fragility_analysis.py`, `repro/stats.py`, `repro/common.py` | Direct complete analysis/statistics reads and `save_json` read; see [EPI-RTE-statistical-check](#epi-rte-statistical-check), [EPI-RTE-result-labeling](#epi-rte-result-labeling), [EPI-OBJ-analysis-output](#epi-obj-analysis-output). Extends runtime's uninspected plotting coverage. |
| Release assertions and warrant comments | SRC-1 `README.md`, `repro/fragility_lib.py` | Direct reads; see [RT-CLM-grid-purpose](runtime.md#rt-clm-grid-purpose), [EPI-CLM-parser-noise](#epi-clm-parser-noise), [EPI-CLM-headline-results](#epi-clm-headline-results), [EPI-CLM-reproducible-analysis](#epi-clm-reproducible-analysis). |
| Released values and tests | SRC-1 `results/fragility/`, `repro/test_fragility_logic.py` | Values not inspected; test specifications only supplied through runtime. Prevents verified empirical magnitudes and test-success assertions, not inspection of wired mechanisms. |

No additional material dispatch surface was found in the inspected driver, collector and analysis entry points. This is a bounded account of that selected subsystem, not a negative over the whole repository.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-benchmark-items](#epi-obj-benchmark-items) | Benchmark question, alternatives and imported gold index | see record | SRC-1 `repro/prompt_format.py`, `repro/brittleness.py` | Truth of gold is not checked locally. |
| [RT-OBJ-config](runtime.md#rt-obj-config) | None in dispatch tuples; formatter strings carry the question and choices | see record | SRC-1 `repro/fragility_lib.py` | Fairness of configurations is a design premise, not proved by enumeration. |
| [RT-CMP-roster-model](runtime.md#rt-cmp-roster-model) | Exact internal propositions not determinable; output can select an answer | see record | SRC-1 `repro/common.py`, `repro/inference.py` | Distributed weights inaccessible here; no parameter updates in inspected inference. |
| [EPI-OBJ-answer-candidate](#epi-obj-answer-candidate) | Selected answer is correct for this question; numeric likelihoods are scores, not truth probabilities | see record | SRC-1 `repro/fragility_grid.py`, `repro/inference.py` | Raw outputs are ephemeral and semantic extraction can fail. |
| [RT-OBJ-records](runtime.md#rt-obj-records) | Per-configuration agreement with dataset gold plus instrumentation | see record | SRC-1 `repro/fragility_grid.py` | Consumer discards question, gold, margin and unparsed count. |
| [RT-OBJ-summary](runtime.md#rt-obj-summary) | Aggregate accuracies and fractions | see record | SRC-1 `repro/fragility_grid.py`, `repro/run_fragility.sh` | Later skip relies on existence, not claim content. |
| [EPI-OBJ-analysis-output](#epi-obj-analysis-output) | Derived counts, ranks, intervals, correlation and interpretive labels | see record | SRC-1 `repro/fragility_analysis.py` | Arithmetic description and general explanatory claims have different warrant. |

## Authority-route ledger

Fields owned by a declaring record are referenced rather than restated. Status here is architectural, not an observed-run conclusion.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-generation-grid](runtime.md#rt-rte-generation-grid) | content transformation | implemented | [EPI-OBJ-benchmark-items](#epi-obj-benchmark-items), [EPI-OBJ-answer-candidate](#epi-obj-answer-candidate) | truth-apt transformation: indeterminate | see route | see route | see route | see route | see route | Generation produces candidate answers, not warranted answers | see route | see [RT-BAP-prompt-answer](runtime.md#rt-bap-prompt-answer) | SRC-1 `repro/fragility_grid.py` | [RT-CLM-grid-purpose](runtime.md#rt-clm-grid-purpose) | none | Some answers may follow from question premises; others require external knowledge. Exact content and derivation cannot be established without answer instances and premises. |
| [EPI-RTE-label-extraction](#epi-rte-label-extraction) | content transformation | implemented | [EPI-OBJ-answer-candidate](#epi-obj-answer-candidate) | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `repro/prompt_format_lib.py` | [EPI-CLM-parser-noise](#epi-clm-parser-noise) | extraction fidelity | Reformatting versus changed answer depends on response; counterexample in record. |
| [RT-RTE-likelihood-grid](runtime.md#rt-rte-likelihood-grid) | operational admission/selection/consumption | implemented | [EPI-OBJ-answer-candidate](#epi-obj-answer-candidate) | non-truth-apt policy/content update: score-based answer selection | see route | see route | see route | see route | see route | Mean token likelihood orders candidates; it is not an independent truth check | see route | see route | SRC-1 `repro/inference.py`, `repro/fragility_grid.py` | [RT-CLM-grid-purpose](runtime.md#rt-clm-grid-purpose) | none | Independently scoring options does not validate tokenizer-boundary handling or backend equivalence. |
| [EPI-RTE-gold-comparison](#epi-rte-gold-comparison) | check/evidence production | implemented | [EPI-OBJ-answer-candidate](#epi-obj-answer-candidate), [RT-OBJ-records](runtime.md#rt-obj-records) | truth-apt transformation: entailed derivation | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `repro/fragility_grid.py` | [RT-CLM-grid-purpose](runtime.md#rt-clm-grid-purpose) | none | Warrant is conditional on gold, parser and permutation fidelity. |
| [RT-RTE-record-analysis](runtime.md#rt-rte-record-analysis) | retention | implemented | [RT-OBJ-records](runtime.md#rt-obj-records), [RT-OBJ-summary](runtime.md#rt-obj-summary) | no content change | see route | see route | see route | see route | see route | Writes license no additional truth | see route | see route | SRC-1 `repro/fragility_grid.py` | none | none | Persistence is neither acceptance nor lifecycle integration. |
| [RT-RTE-record-analysis](runtime.md#rt-rte-record-analysis) | content transformation | implemented | [RT-OBJ-records](runtime.md#rt-obj-records), [EPI-OBJ-analysis-output](#epi-obj-analysis-output) | truth-apt transformation: entailed derivation | see route | see route | see route | see route | see route | Arithmetic properties of supplied bits only | see route | see route | SRC-1 `repro/fragility_analysis.py`, `repro/fragility_lib.py` | [EPI-CLM-headline-results](#epi-clm-headline-results) | none | Reload imports existing bits with unknown collection provenance; it does not recheck answers. |
| [EPI-RTE-statistical-check](#epi-rte-statistical-check) | check/evidence production | implemented | [EPI-OBJ-analysis-output](#epi-obj-analysis-output) | truth-apt transformation: entailed derivation | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `repro/stats.py`, `repro/fragility_analysis.py` | [EPI-CLM-headline-results](#epi-clm-headline-results) | none | Computed intervals do not alone warrant equality, mental uncertainty or causation. |
| [EPI-RTE-result-labeling](#epi-rte-result-labeling) | disposition/acceptance | implemented | [EPI-OBJ-analysis-output](#epi-obj-analysis-output) | truth-apt transformation: ampliative conjecture | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `repro/fragility_analysis.py` | [EPI-CLM-headline-results](#epi-clm-headline-results) | interpretive overreach | Mechanical label admission is evidenced; accepted explanatory truth is not. |
| [RT-RTE-sweep-driver](runtime.md#rt-rte-sweep-driver) | lineage/freshness/recovery | implemented | [RT-OBJ-summary](runtime.md#rt-obj-summary) | no content change | see route | see route | see route | see route | see route | No epistemic endorsement follows from existence | see route | see [RT-BAP-summary-skip](runtime.md#rt-bap-summary-skip) | SRC-1 `repro/run_fragility.sh` | none | none | Stale summaries can block refreshed measurement; failures can leave old eligible records. |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-grid-purpose](runtime.md#rt-clm-grid-purpose) | see record | SRC-1 `repro/fragility_grid.py`; doctrine/design | see record | [RT-RTE-generation-grid](runtime.md#rt-rte-generation-grid), [RT-RTE-likelihood-grid](runtime.md#rt-rte-likelihood-grid) | Uninspected | Joint grid measures variation; no independently verified component intervention | Same loaded items are crossed with configurations within an invocation | Cross-model equality requires stable external data; reproducibility is conditional. |
| [EPI-CLM-parser-noise](#epi-clm-parser-noise) | see record | SRC-1 `repro/fragility_lib.py`; doctrine/design | see record | [EPI-RTE-label-extraction](#epi-rte-label-extraction) | Uninspected | Deterministic extraction is not semantic fidelity | Fuzzy restatement is excluded | A first-match counterexample defeats universal noise exclusion. |
| [EPI-CLM-headline-results](#epi-clm-headline-results) | see record | SRC-1 `README.md`, `repro/fragility_analysis.py`; doctrine/design and attributed results | see record | [RT-RTE-record-analysis](runtime.md#rt-rte-record-analysis), [EPI-RTE-statistical-check](#epi-rte-statistical-check), [EPI-RTE-result-labeling](#epi-rte-result-labeling) | Released values uninspected | Algebra partitions a gap; observational correlation and subset contrasts do not identify why models are wrong or establish all compression methods' behavior | Implemented descriptive statistics and diagnostic labels | Exact magnitudes, mental uncertainty, equality and broad causal interpretations unestablished. |
| [EPI-CLM-reproducible-analysis](#epi-clm-reproducible-analysis) | see record | SRC-1 `README.md`; doctrine/design | see record | [EPI-RTE-statistical-check](#epi-rte-statistical-check), [RT-RTE-record-analysis](runtime.md#rt-rte-record-analysis) | Uninspected | Seeds constrain draws, not environment bytes | Seeded bootstrap/subset procedures and stable sorting are wired | One shared generator is not the actual architecture; byte-identical outputs not demonstrated. |

## Bounded conclusion

The workflow acquires benchmark content and treats imported labels as its expected-answer oracle; source warrant is unknown, not independently strengthened. Fixed permutations and prompt formatting preserve supplied question/option text before backend rendering, but TruthfulQA first reduces the option set. Neither this acquisition nor formatting produces new benchmark truth ([EPI-OBJ-benchmark-items](#epi-obj-benchmark-items)).

Generation and likelihood selection yield answer candidates. Equality with gold derives a dataset-relative correctness proposition, not a proof that the answer is true. A concrete counterexample defeats the claim that deterministic parsing excludes parser noise. The checker grants operative measurement authority: even incorrect and unparsed responses yield retained bits, rather than rejection of a proposed knowledge artifact ([EPI-RTE-label-extraction](#epi-rte-label-extraction), [EPI-RTE-gold-comparison](#epi-rte-gold-comparison)).

Retained bits feed deterministic arithmetic, rank ordering, intervals and comparison subsets. Their formal relationships hold over supplied records, conditional on alignment and completeness; they do not authenticate model/dataset lineage. Bootstrap inclusion of zero licenses the program's tied label, not affirmative equivalence. Margins and seeded cutoff tie-break distributions are genuine safeguards against simplistic champion/subset interpretations, but do not establish the broader mechanism claimed by 'manufactured' or 'least sure' ([EPI-RTE-statistical-check](#epi-rte-statistical-check), [EPI-RTE-result-labeling](#epi-rte-result-labeling)).

The material acceptance criterion implemented for interpretive labels is a nonzero reference gap plus a robust-subset bootstrap interval containing zero, for reporting adjacent-pair status on loaded records. Its consumer is the JSON/figure/console pipeline; its force is automatic publication to local artifacts, not permission to deploy or train a model. No further evidence-consuming acceptance decision warrants the broader explanatory claims, and no post-acceptance lifecycle integration is established by these inspected consumers. Retention and report use must not be relabelled as that integration ([EPI-RTE-result-labeling](#epi-rte-result-labeling), [RT-RTE-record-analysis](runtime.md#rt-rte-record-analysis)).

The only later collector behavior directly changed by a retained artifact here is the summary-existence skip. It is an enforcing recovery predicate, not epistemic evaluation, and can prevent fresh collection without reading result content. Weights remain fixed in inspected inference, and analysis does not feed back a revised method or model policy. These facts do not establish improved future capacity, exercised self-improvement, content-directed criticism or model-internal reflection; those properties require their own evidence, not a combined system verdict ([RT-BAP-summary-skip](runtime.md#rt-bap-summary-skip), [RT-CMP-roster-model](runtime.md#rt-cmp-roster-model)).

## Shared records

### Operative objects

#### EPI-OBJ-benchmark-items
Label: Benchmark items

Source-native identity: `eval_items` returned by `load_bench`, derived from `_load_mcq` or MMLU. Form: natural-language questions/options plus symbolic gold indices. Substrate: external datasets and process-local tuples. Distinct from [RT-OBJ-config](runtime.md#rt-obj-config), which specifies experiment presentation, and [RT-OBJ-records](runtime.md#rt-obj-records), which retains outcomes. SRC-1 `repro/prompt_format.py`, `repro/brittleness.py` supply implementation evidence.

Loaders acquire rather than verify truth. ARC retains resolvable four-option gold; HellaSwag converts nonempty labels. TruthfulQA changes the choice domain to the labelled correct option plus three distractors; source warrant remains unknown. Seeds stabilize order only for stable input bytes. The first five items are excluded from this evaluation even though no few-shot material is supplied.

> fewshot_pool = data[:5]
> eval_items = data[5: n + 5]
> return eval_items, fewshot_pool
> --- `repro/prompt_format.py`

> gi = labels.index(1)
> keep = [gi] + [i for i in range(len(opts)) if i != gi][:3]
> four = [opts[i] for i in keep]
> out.append((ex["question"], four, 0))  # gold now at position 0
> --- `repro/brittleness.py`

#### EPI-OBJ-answer-candidate
Label: Answer candidate

Source-native identity: generated `text`, `pred_shown`, or likelihood-selected `pred`. Form: natural-language response followed by symbolic option index; likelihood arrays are numerical model measurements, not independently warranted propositions. Substrate: current process memory, not a raw-answer archive. Distinct from [RT-OBJ-records](runtime.md#rt-obj-records): only correctness and instrumentation survive. Producer/consumer are see [RT-RTE-generation-grid](runtime.md#rt-rte-generation-grid), [RT-RTE-likelihood-grid](runtime.md#rt-rte-likelihood-grid). SRC-1 `repro/fragility_grid.py`, `repro/inference.py`, implementation.

> pred_shown = parser(text, items[ix][1])
> --- `repro/fragility_grid.py`

> pred = max(range(len(opts)), key=lambda i: scores[i])
> bits[ix][c.key] = int(pred == gold)
> --- `repro/fragility_grid.py`

#### EPI-OBJ-analysis-output
Label: Analysis output

Source-native identity: `out` returned by `analyze`, serialized to `fragility/analysis.json` and consumed by four figures and console output. Form: symbolic counts, numeric estimates and natural-language interpretation. Substrate: process dictionary, JSON and PNG/PDF files. Distinct from [RT-OBJ-summary](runtime.md#rt-obj-summary), a per-model collector output, and [RT-OBJ-records](runtime.md#rt-obj-records), its per-item inputs. Implementation evidence SRC-1 `repro/fragility_analysis.py`.

The bands derive any/all/reference correctness over bits. Pairwise decomposition sums reference differences separately on invariant versus fragile items, with the same full-pair denominator. The plot additionally shows the mean difference conditional on robust items, a different denominator; this is not a second independent measurement. Figure output does not check the interpretation. In `fig_accuracy_band`, an any-item/all-item envelope is labelled a range across configurations: these are itemwise oracle bounds, not necessarily accuracies attained by one fixed configuration. A counterexample is two items with opposite correctness in two configurations: the envelope is zero to one while both configurations score one half. This deduction follows `accuracy_band` and the inspected figure code; no target execution is needed.

> ax.barh(y, [o - r for o, r in zip(opt, rob)], left=rob, height=0.5,
>         color=C_GREY, alpha=0.30, zorder=1, label="range across the 26 configs")
> --- `repro/fragility_analysis.py`

> "acc_optimistic": sum(any_correct(r) for r in records) / n,
> "acc_reference": sum(int(r.get(ref_key) == 1) for r in records) / n,
> "acc_robust": sum(all_correct(r) for r in records) / n,
> --- `repro/fragility_lib.py`

### Routes

#### EPI-RTE-label-extraction
Label: Label extraction

Part of: [RT-RTE-generation-grid](runtime.md#rt-rte-generation-grid)

Endpoints/progression: generated text → first matching label → shown option index. Owner: fixed parser selected by format; context is the current response. This part transforms the answer representation, distinct from correctness checking. SRC-1 `repro/prompt_format_lib.py`, `repro/fragility_grid.py`, implementation. Epistemic authority: no guaranteed preservation of intended answer; operational authority: supplies the index used by the checker. Behavioral-authority path: parser return → collector, enforcing index selection for this item/configuration and its retained bit.

- Immediate return: A zero-based index or None.
- Later read-back: inapplicable — raw response and parsed index are not retained for later parsing in this workflow.
- Delegated visibility: inapplicable — fixed local parser, not a delegated model.
- Selection predicate: First standalone A–D after uppercase conversion, or first standalone 1–4.
- Invalidation or expiry: Current response/index discarded after evaluation; reruns create fresh candidates.
- Activation or effect: Wired extraction, with counterexample deduced below; actual responses unobserved.
- Evidence limits: Determinism establishes repeatability for a string, not answer fidelity.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Concrete input `Not A; B is correct.` becomes `NOT A; B IS CORRECT.`; regex search matches A first and returns index zero. With identity permutation and gold B, collector records zero even though the response explicitly selects B. This refutes universal exclusion of parser noise without establishing its empirical frequency. Alternatives include faithful one-label responses, which this parser handles correctly; the defect is not universal failure.

> t = text.strip().upper()
> m = re.search(r"\b([A-D])\b", t)
> return LETTERS.index(m.group(1)) if m else None
> --- `repro/prompt_format_lib.py`

#### EPI-RTE-gold-comparison
Label: Gold comparison

Distinct identity: spans the check portions of [RT-RTE-generation-grid](runtime.md#rt-rte-generation-grid) and [RT-RTE-likelihood-grid](runtime.md#rt-rte-likelihood-grid), not part of exactly one supplied record. Endpoints: selected option, permutation where applicable, imported gold → equality bit → record accumulator. Owner: collector. Context/effect: per-item bits and unparsed counter; expected-answer oracle is dataset gold, not an LLM or per-item human judge. Bounded experimental mode; model proposes, fixed code decides, operator selects scope but cannot veto individual writes through this path. No improvement trigger. SRC-1 `repro/fragility_grid.py`, implementation.

Check target/domain: equality of a selected original option index to gold for the loaded MCQ. Force: enforcing measurement assignment, including zero on parse failure; both success and failure are retained. Epistemic authority: entailed dataset-relative agreement conditional on faithful extraction and correct gold, not source truth. Behavioral-authority path: equality result → `bits` → summary/CPU analysis, enforcing numerical input through later artifact generation.

- Immediate return: A 0/1 correctness bit; parse failure also increments `n_gen_unparsed`.
- Later read-back: Bits persist in records and reach later CPU analysis; raw answers do not.
- Delegated visibility: Model receives question/options, not this gold-comparison decision in later context.
- Selection predicate: Every returned generation result or likelihood score row paired with an item.
- Invalidation or expiry: Matching collection overwrites records; no independent withdrawal protocol.
- Activation or effect: Wired bit assignment and instrumentation; no run observed.
- Evidence limits: Zip cardinality assumptions can omit entries; missing bits receive inconsistent downstream treatment, see supplied runtime.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> chosen_orig = perm[pred_shown]
> correct = int(chosen_orig == gold)
> --- `repro/fragility_grid.py`

> correct = 0
> n_gen_unparsed[ix] += 1   # no answer extracted under this config
> --- `repro/fragility_grid.py`

#### EPI-RTE-statistical-check
Label: Statistical check

Part of: [RT-RTE-record-analysis](runtime.md#rt-rte-record-analysis)

Endpoints: aligned robust-item reference differences → percentile-bootstrap interval; shared-item matrix → discrimination/fragility correlation, bootstrap interval and subset champion contrasts. Owner: fixed numerical code. State: arrays and seeded random generators. This part produces evidence, not the subsequent labels. SRC-1 `repro/stats.py`, `repro/fragility_analysis.py`, implementation.

Check target/domain: conditional mean difference on the jointly invariant subset; association between item-total correlation and observed configuration sensitivity; champion counts under the specified model pool, configuration grid and subsets. Bootstrap mean uses 10,000 draws and 95% percentile limits by default; correlation uses 2,000 resamples. Numeric correctness is conditional on supplied bits/alignment and dependency behavior. Statistical generalization further needs defensible sampling assumptions. Interval overlap with zero is not an equivalence test. Correlation cannot establish a causal compression mechanism.

Fixed software proposes comparison subsets and decides; no per-result human veto or independent answer oracle. Stored bits incorporate the earlier gold oracle. Mode is a bounded experiment; no policy improvement trigger. The compression route skips insufficient items/models, random subsets sample without replacement, and cutoff ties are marginalized over 200 draws. Champion margins flag fragile one-item-style wins rather than unconditionally endorsing every winner. These safeguards qualify, rather than erase, the interpretive limits.

- Immediate return: CI objects, correlation estimates and distributions of subset champion counts.
- Later read-back: Results reach persisted analysis and figures via the parent route; reruns recompute from retained bits.
- Delegated visibility: inapplicable — no model call or delegated judgment in this numerical stage.
- Selection predicate: Adjacent reference-ranked pairs, pairwise common item IDs; compression requires items shared by every model.
- Invalidation or expiry: Recomputed and overwritten on analysis invocation; no stale-source authentication.
- Activation or effect: Wired numerical inputs for labeling and output, operation unobserved.
- Evidence limits: Index-derived item identity and heterogeneous model coverage can weaken comparisons; no independent released-value check or causal intervention supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> rng = np.random.default_rng(seed)
> idx = rng.integers(0, a.size, size=(n_boot, a.size))
> boot = a[idx].mean(axis=1)
> lo, hi = np.quantile(boot, [alpha / 2, 1 - alpha / 2])
> --- `repro/stats.py`

> if len(keys) < tiny_k + 5 or len(models) < 3:
>     return {"skipped": "not enough items/models"}
> --- `repro/fragility_analysis.py`

> pick = rng.choice(tied_idx, size=n_from_tiebreak, replace=False)
> idx = np.concatenate([strict_idx, pick])
> tiny_vols.append(subset_volatility(idx))
> --- `repro/fragility_analysis.py`

#### EPI-RTE-result-labeling
Label: Result labeling

Part of: [RT-RTE-record-analysis](runtime.md#rt-rte-record-analysis)

Endpoints: robust-subset interval and reference difference → tied/manufactured booleans → JSON, console and figure consumers. Owner: analysis program, with criteria authored in source. Context/effects: adjacent pair dictionaries and aggregate headline counts. This is disposition into reporting, separate from evidence production. SRC-1 `repro/fragility_analysis.py`, implementation.

Candidate comparison roles: software selects adjacent models and assigns labels; operator launches, no per-label human approval/veto implemented. Oracle: no independent expected causal/equivalence answer; only earlier bit measurements and the bootstrap result. Mode: bounded experimental reporting, not production admission or a method-revision trigger. Admission criterion for `manufactured` is separated reference accuracy plus an interval including zero; a false condition withholds the boolean label. Filesystem write publishes both outcomes, no epistemic rollback beyond rerun/overwrite.

Epistemic authority: program-defined diagnostic label on supplied records. As a claim of causal manufacture or substantive equality it exceeds those premises. Non-entailment witness: a noisy finite robust-item sample can have a CI containing zero when the population mean difference is nonzero. Configuration sensitivity also does not entail mental uncertainty. The interpretive text therefore introduces ampliative claims rather than merely reformatting statistics. No evidence-consuming acceptance establishes these broader interpretations as true for a named intended use. Operational authority is automatic local reporting only. Behavioral-authority path: booleans/interpretation → analysis JSON, console and plots, enforcing publication; human scientific reliance is possible but unobserved and not enforced.

- Immediate return: `tied_on_robust_items`, `order_manufactured_by_fragile_items` and aggregate counts.
- Later read-back: Persisted analysis is available, but no automatic collector/model read-back is implemented in this route.
- Delegated visibility: inapplicable — no model receives these labels in the inspected pipeline.
- Selection predicate: CI includes zero and pair differs at reference for the manufactured label.
- Invalidation or expiry: New analysis overwrites JSON; no source-sensitive withdrawal or acceptance history.
- Activation or effect: Wired reporting disposition; no observed publication or downstream reliance supplied.
- Evidence limits: Labels do not provide a causal experiment, equivalence criterion, mechanistic explanation or cross-task transfer check.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> tied_robust = bool(rci is not None and rci.lo <= 0 <= rci.hi)
> # separated at reference?  (their ref accuracies differ at all)
> separated_ref = abs(dec["delta"] or 0) > 1e-12
> manufactured = bool(separated_ref and tied_robust)
> --- `repro/fragility_analysis.py`

> "pair is statistically tied on jointly-robust items yet separated overall -- the gap is "
> "carried by config-fragile items (the ones models are least sure about). config_lucky_"
> --- `repro/fragility_analysis.py`

### Claims

#### EPI-CLM-parser-noise
Label: Parser noise exclusion

Distinct from [RT-CLM-grid-purpose](runtime.md#rt-clm-grid-purpose): this is the narrower warrant that deterministic parsers exclude parser noise. Source SRC-1 `repro/fragility_lib.py`, doctrine/design. Counterexample and supported narrower conclusion are see [EPI-RTE-label-extraction](#epi-rte-label-extraction).

> # All four have deterministic parsers (letter/digit); the fuzzy "restate" format is excluded
> # so parser noise never masquerades as harness fragility.
> --- `repro/fragility_lib.py`

#### EPI-CLM-headline-results
Label: Headline results

Distinct from [RT-CLM-grid-purpose](runtime.md#rt-clm-grid-purpose): covers reported empirical magnitudes and their broader interpretations, not the grid's collection design. SRC-1 `README.md` gives attributed results; `repro/fragility_analysis.py` gives implemented interpretation. Exact results remain unverified; descriptive decomposition does not entail mental uncertainty or general causal claims about compression methods. A configuration grid varies a harness bundle; without appropriate contrasts it does not identify a finer component cause. 'Equally defensible' configurations are assumed rather than validated by a separate evaluator.

> Three results follow. Adjacent leaderboard gaps are carried almost entirely (95.7% on average) by
> items whose correctness flips across configurations, while the items both models answer stably are
> tied. Four of the 12 models reach rank one under some configuration, so the harness selects the
> winner. The items that benchmark-compression methods keep are the fragile ones (correlation 0.28,
> 95% CI 0.25 to 0.30), so a compressed leaderboard is more configuration-dependent than the full one.
> --- `README.md`

#### EPI-CLM-reproducible-analysis
Label: Reproducible analysis

Distinct from [RT-CLM-grid-purpose](runtime.md#rt-clm-grid-purpose): CPU byte-reproducibility and random-state architecture. Source SRC-1 `README.md`, doctrine/design. Implementation uses separate seeded generators: `bootstrap_mean_ci` initializes a new one for each call while `idea_a_compression` owns another. Thus the literal single-generator account is inaccurate, although repeated fixed seeds can still support repeatability under fixed inputs/environment. No two-run comparison was supplied. Plot `_save` strips PDF CreationDate but that alone does not demonstrate byte identity across library environments. No runtime supersession needed: this corrects a newly assessed public claim, not a supplied record.

> The analysis is a deterministic function of the released records and one seed (1234): the bootstrap
> resamples, the random item subsets, and the tie-breaks at the discrimination cutoff all draw from a
> single seeded generator, so two runs give byte-identical output.
> --- `README.md`

Implementation counterevidence is see [EPI-RTE-statistical-check](#epi-rte-statistical-check), SRC-1 `repro/stats.py`, and this independent generator inside compression:

> # bootstrap CI for corr(discrimination, fragility)
> rng = np.random.default_rng(seed)
> r = float(np.corrcoef(disc, frag)[0, 1]) if disc.std() and frag.std() else float("nan")
> --- `repro/fragility_analysis.py`
