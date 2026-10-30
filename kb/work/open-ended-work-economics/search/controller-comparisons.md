# Search results: controller comparisons for test 1

Raw material for the controller-cost test (reconciliation.md, "Discriminating
tests", test 1). Search worker output, 2026-10-30. Facts only: the test is
not decided here. Paths are KB-relative (`kb/...`). Quotes are verbatim from
the files named. "Reversal" lines are a one-line plausibility reading, not a
recomputation.

A search controller here is a judgment or procedure that decides which
branch, candidate, source, note or bundle receives further work, without
licensing adoption
(`kb/theory/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md`).
Several recorded comparisons vary something closer to a writer, evaluator or
reading policy. They are listed separately in section B, marked by how
closely they fit the definition.

Searched: the directories named in the brief, `kb/theory/evidence/`,
`kb/reports/retained/` (all top-level entries scanned), notes with the
`has-comparison` trait, `kb/log.md`, and the three named source ingests.
`kb/work/connect-report-mining/` contains no comparison between connect
samplers or routing policies: it mines 45 reports for recurring patterns
and states that it "does not re-run `cp-skill-connect` on anything".
`kb/log.md` has no entry pairing a controller comparison with a cost figure
(the nearest is the ADR 066 entry: 23 full passes, zero accepted conversions,
which has a single arm).

---

## A. Comparisons of Commonplace controllers (recorded, run)

### A1. Five-link reading cap versus uncapped reading in grounding review

- **Path:** `kb/reports/retained/a-five-link-cap-missed-four-grounding-findings-in-twelve-reviews.md`
- **Arms:** production `semantic/grounding-alignment` criterion capped at five
  linked artifacts versus an otherwise identical uncapped criterion; same 12
  notes, `gpt-5.4` high effort; plus a five-note capped-repeat arm to measure
  reviewer noise. The controlled variable is which linked artifacts receive
  reading.
- **Yield measure:** outcome divergence (PASS/WARN/FAIL). Five divergences;
  one attributed to reviewer sensitivity; four "appeared only under fuller
  reading: two WARN and two FAIL results after opening 6, 11, 14, or 16
  distinct linked artifacts".
- **Cost reported:** artifacts opened per job and consumed whole-file bytes
  for the uncapped arm ("322,097; 254,004; 81,152; ..."; "Median consumption
  was 11 artifacts"). Capped-arm opened counts are in the table (3–5); its
  bytes are not given. The record disclaims a price: "The assay does not
  identify a general attention price", and for the production rerun "These
  are provenance measurements, not model usage or an attention-price
  estimate." No tokens, time or money.
- **Preference and basis:** raise the cap to 16. Basis: "A cap of 16 distinct
  artifacts covers every divergent case in this sample and also matches the
  p90 offered artifact count"; tail cases (21–23 artifacts) all PASS, so no
  split-pass machinery.
- **Cost in basis?** Partly. The cap is a reading budget and the chosen value
  is set by coverage of findings; consumption is measured but not traded
  against yield.
- **Reversal:** Unlikely for cap 5 versus uncapped (two material FAILs among
  12); a priced reading could only move the chosen ceiling, which the record
  already bounds by the p90 offer.

### A2. Description allowances as read/skip pointers (description-length assay 1)

- **Path:** `kb/work/description-length-optimization/assay-1-report.md`
  (workshop question in `README.md`)
- **Arms:** descriptions shaped to 120, 160, 200, 250 and 300 characters;
  5-, 20- and 80-candidate result sets. The controlled variable is the pointer
  that decides which artifact gets opened.
- **Yield measure:** retrieval recall, irrelevant opens, downstream task
  success. "retrieval recall was 95.5% at 120, 97.7% at 160 and 200, and 100%
  at 250 and 300."
- **Cost reported:** projected pointer tokens per result slice ("approximately
  4,616, 5,370, 6,132, 7,268, and 8,212 tokens respectively, using
  `ceil(characters / 4)`") against "a declared 8,000-token-estimate pointer
  budget". Run cost also logged: "1,332,340 tokens total". Not reported:
  "Wall time and monetary inference cost were not captured consistently".
- **Preference and basis:** 250 survives as the provisional soft warning;
  "Since 300 added cost without improving any measured result and breaches
  the 80-result budget projection, 300 is dominated in this assay."
- **Cost in basis?** Yes, explicitly (Pareto frontier of recall against
  pointer budget).
- **Reversal:** Cost is already in the basis. The record notes that 160 or 200
  "sometimes also resolved" the one discriminating case, and that a cheaper
  role display may remove the need; a tighter budget could favour those.

### A3. Trace-first versus claim-first meta-analyser investigation order

- **Path:** `kb/reports/retained/meta-analyser-pilot-20261021/README.md`,
  `metrics.json`, `openresearch-compact-metrics.json`
- **Arms:** two investigation orders (which evidence the auditor inspects
  first) on one real run and one constructed case; later a compact
  trace-first prompt on the real run.
- **Yield measure:** supported residual defects, unsupported allegations,
  recognition of recovered failures. Both strategies "met the constructed
  case's two expectations"; on OpenResearch, "Same bounded outcome".
- **Cost reported:** tool calls and seconds per invocation (OpenResearch:
  trace-first 15 calls, 212.39 s; claim-first 27 calls, 263.32 s; constructed
  case 10/74.95 versus 10/77.82). `metrics.json` usage: trace-first
  `"cacheRead": 791424`, claim-first `"cacheRead": 1805440`. Compact rerun:
  "23 versus 15" calls, "199 versus 212 seconds".
- **Preference and basis:** "Use trace-first as the initial candidate for
  another pilot: in this pair it reached the same incident dispositions with
  fewer tool calls and lower elapsed time." The record also says the
  observations "do not establish general superiority, detection rates or
  cost effectiveness", and the protocol said "Do not rank prompts solely by
  number of incidents mentioned or token cost."
- **Cost in basis?** Yes: yield tied, cost broke the tie.
- **Reversal:** Not applicable; cost already decided it. Claim-first is kept
  "as a comparison" for a yield reason (it challenged load-bearing claims).

### A4. Per-gate writes versus one bundled review artifact; bundle size and grouping

- **Paths:** cost side
  `kb/reports/retained/single-artifact-review-bundles-still-cut-claude-costs-substantially.md`;
  yield side `kb/work/error-catching/gate-stats.md` §6.
- **Arms:** old per-gate write path (35 runs, 6 gates) versus bundled output
  (14 runs, 6 gates; 67 runs, 4 gates). Gate-stats §6 also compares bundle
  sizes within lens and "Note-grouped jobs" versus "criterion-grouped" jobs.
- **Yield measure:** none in the cost record. Gate-stats: catch rate by bundle
  size and grouping; "no monotone decline with bundle size"; note-grouped
  "slightly out-catch criterion-grouped in five of seven lenses".
- **Cost reported:** cost record only: "median raw tokens per gate fell from
  29,730 to 9,988"; "Median weighted cost per gate fell from $0.0962 to
  $0.0714, a 25.8% reduction"; request count from 6 to 2. Gate-stats §6
  reports no cost.
- **Preference and basis:** bundled path adopted. Gate-stats records: "the
  bundled-artifact change was adopted on cost telemetry alone, and this is
  the first check of its detection-quality side — it passes."
- **Cost in basis?** Yes for the adoption; yield checked afterwards, in a
  separate record, and not on the same runs. The grouping comparison has no
  cost.
- **Reversal:** No: the later yield check found no quality penalty, so cost
  and yield point the same way. The cost record itself says "This is not a
  controlled A/B test."

### A5. Reviewer partitions luna versus sol

- **Path:** `kb/work/error-catching/gate-stats.md` §4;
  `kb/work/error-catching/calibration-run-01.md`
- **Arms:** two model partitions reviewing the same seven notes on identical
  snapshots. (The reviewer is the detector; its WARNs route notes to repair.)
- **Yield measure:** catch rate, "luna 34.3% vs sol 13.8%".
- **Cost reported:** none. Calibration run 01 names cost as the current basis
  for partition choice: per-partition calibration is the next run "if
  partition choice ever needs justification beyond cost".
- **Preference and basis:** no preference recorded; the finding is that
  "catch rate" is "a property of the (gate, partition) pair".
- **Cost in basis?** No figure; cost is said to be the operative basis of
  partition choice outside this record.
- **Reversal:** Undeterminable from the KB: no per-partition cost is recorded,
  and recall per partition is unmeasured (calibration used one reviewer class).

### A6. Six investigation framings (curiosity prompts)

- **Path:** `kb/reports/retained/curiosity-prompts-20260310/README.md`,
  `captures/experiment-report.md`
- **Arms:** six prompt framings directing what an investigating agent looks
  at, two runs each, on one Decapod report.
- **Yield measure:** whether the run reached the target finding. "Cost/benefit
  | **Yes** | **Yes** | **2/2**"; pure curiosity 1.5/2; four others 0/2.
- **Cost reported:** none. ("Cost/benefit" names a prompt framing, not a run
  cost.) The README says the set lacks "model versions" and a complete
  run-to-output map.
- **Preference and basis:** the report calls cost/benefit "the most reliable
  agent-accessible framing"; the README notes two trials "do not establish
  stable activation rates or a general ranking".
- **Cost in basis?** No.
- **Reversal:** Unknown; no run cost exists to compare.

### A7. AutoReason trial: original versus critic-led revision versus synthesis

- **Path:** `kb/reports/retained/autoreason-compounding-trial-20260925/README.md`
- **Arms:** incumbent A, critic-led revision B, synthesis AB; three blind
  judges. The critic is the routing step that selects what the revision
  works on. One pass, one note.
- **Yield measure:** Borda points (A 3, B 6, AB 9); fidelity checks; operator
  readability.
- **Cost reported:** aggregate only: "Seven fresh agents"; "Elapsed time was
  11.6 minutes, including orchestration and checks." No per-arm cost; no
  tokens.
- **Preference and basis:** judges preferred AB; the operator found it hard to
  read and closed the experiments: "autorevision needs to stay experimental"
  and "I don't see reason to continue these experiments for now." Basis is
  readability, not cost.
- **Cost in basis?** No.
- **Reversal:** A cost reading would not reverse the stop decision; it could
  only add a second reason for it.

---

## B. Adjacent comparisons (writer, evaluator or procedure treatments)

These vary a procedure that produces or judges a candidate rather than one
that routes further work. Listed because each reports a yield-like measure.

| Path | Arms | Yield measure | Cost reported | Basis / preference | Cost in basis? |
|---|---|---|---|---|---|
| `kb/theory/evidence/three-simplification-passes-exposed-different-tradeoffs.md` (+ retained `simplification-instruction-comparison-20260807/`) | three simplification instructions vs baseline | one blind LLM ranking `D > C > A > B`; semantic regressions found | none: "recorded final word counts and edit decisions, not runtime, token cost, or reviewer effort" | established style best overall | No |
| `kb/theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md` | unguarded vs guarded ASD-STE100-inspired rewrite | semantic failures (five vs none known) | words only (+4.9%); "uses words, not model tokens" | guarded retained | No |
| `kb/theory/evidence/independent-pass-tightened-three-of-four-pirolli-verdicts.md` | joint-context vs separated grounding comparison | verdicts changed (3 of 4 tightened) | none found | separated pass is "a candidate control" | No |
| `kb/reports/retained/synthesis-distinction-pilot-20261005/README.md`, `scores.md` | combined writer+reviewer treatment vs control | predeclared promising-signal rule; target distinction caught or missed | yes: v2 "332.32 seconds of aggregate model runtime and 1,950,094 reported input-plus-output tokens"; per-job table in `scores.md`; v1 control "1,283,864 reported tokens" exceeded a 1,000,000-token ceiling | do not adopt; basis is yield (rule not met) | No (cost is a ceiling, not a criterion) |
| `kb/reports/retained/dynamic-cheatsheet-worker-instruction-comparison-2026-10-10.md` | previous vs revised worker instructions | errors caught, corrections kept: "Broader documented verification did not consistently catch more errors" | none found by cost-term search | partial improvement, no overall gain shown | No |
| `kb/reports/retained/quotes-route-rollout-grounded-more-uses-without-earning-claim-ids.md` | paraphrased claims ledger vs verbatim quotes / snapshots | grounded claim uses: 30% vs 75% | none found by cost-term search | descriptive gap; non-random cohorts | No |
| `kb/work/in-one-episode-recognition-appeared-only-in-the-corpus-loaded-run.md` | repository-free vs corpus-loaded synthesis | recognition of retained notes | none found | none; "not a result" | No |

---

## C. External comparisons in source ingests

### C1. PrimeScientist plan-selection rules

- **Path:** `kb/sources/primescientist-research-effort-allocation.ingest.md`
- **Arms:** adaptive selection versus UCT, Greedy and Random within a fixed
  framework; full framework versus AutoResearch; adaptive versus fixed
  exponent.
- **Yield:** "mean maximum reward of 0.598 for adaptive selection versus
  0.551 for UCT, 0.563 for Greedy, and 0.546 for Random"; AutoLab "0.4363
  versus 0.4359, with about 24% fewer attempts".
- **Cost:** shared token budget charging planning and execution ("1M-token
  budget"); "38% to planning"; timing "means of 32 versus 42 minutes but the
  same 34-minute median". The ingest limits it: "The token budget excludes
  CPU/GPU hours and elapsed time" and "Fewer attempts do not establish lower
  total experimental cost."
- **Cost in basis?** Yes: arms are budget-matched, so yield is measured per
  fixed budget; the AutoLab gain is in attempts at equal reward.
- **Reversal:** For the selection-rule comparison, cost is held fixed by
  design. The ingest notes uneven effects ("the other seven average 0.5052
  versus 0.5061"), which concerns the yield, not cost.

### C2. Model Discovery Agent: value-of-information versus LLM-designed or random acquisition

- **Path:** `kb/sources/model-discovery-agent-bayesian-experiment-design.ingest.md`
- **Yield:** experiments needed to reach accurate interventional prediction;
  "in the stochastic version, random acquisition is comparable in one
  analysis".
- **Cost:** experiment count only in the headline; computation is qualitative:
  the inference stack "can be computationally expensive"; one learned-summary
  "four-order-of-magnitude per-decision speedup". "Experiment efficiency and
  total efficiency are different ledgers."
- **Cost in basis?** Experiment count only; compute not compared.
- **Reversal:** Plausible in principle: the ingest itself says the
  experiment-count curves are not "a full cost comparison".

### C3. Autoreason paper

- **Path:** `kb/sources/autoreason-self-refinement-that-knows-when-to-stop.ingest.md`
- **Yield:** A/B/AB with blind Borda judges versus baselines and ablations.
- **Cost:** none reported in the ingest; the summary says "mid-tier/cost-
  conscious models gain most" but gives no cost figures. No quotes retained.
- **Cost in basis?** No (as ingested).

---

## D. Designed or predicted comparisons not yet run

- `kb/work/review-bundle-packing/measurement-plan.md`: one note × one bundle
  versus one note × all bundles, etc. Plans both tokens and "number of WARN
  findings"; no measurement table exists. "The workshop should decide
  between these after measurement, not before."
- `kb/work/conjecture-store/research-notes.md` §5: "samplers as bandit arms
  scored by later uptake only"; budget split "about 20% uniform random as
  control". §6 E3 selectors ("net code-length savings, LLM reach judgment,
  source fit, random") and a "Cheapest backcast for isotropy: ... run connect
  vs random vs bridged pairs". E1 lists "budget-matched directed connect" and
  "derivation tokens". None run: "No controlled theory-builder learning run
  has ever been performed in Commonplace."
- `kb/theory/claim-routed-reading-may-beat-reading-first-for-synthesis-notes.md`:
  "Status: conjecture" and "untested in this KB"; its test is stated per
  cost: "beats reading-first on warrant per unit of context".
- `kb/work/reflective-improvement-divergence/problem-map.md`, prediction 1:
  "Strengthening a critic without adding an episode budget will increase findings
  and episode length more reliably than it increases completed object-level
  work." Prediction 4: local scores can improve "while declining against its
  declared objective once opportunity cost is counted." No observation
  recorded.

---

## Summary lists

### Comparisons with yield but no cost (9 Commonplace, 2 external)

- A5 luna versus sol reviewer partitions (gate-stats §4)
- A6 curiosity-prompt framings
- A4 grouping/bundle-size catch comparison (gate-stats §6), taken alone
- B simplification instructions
- B ASD-STE100-inspired rewrites (word counts only)
- B Pirolli separated grounding pass
- B Dynamic Cheatsheet worker instructions
- B quotes-route rollout
- B corpus-loaded recognition episode
- C2 Model Discovery Agent (experiment count only; compute qualitative)
- C3 Autoreason paper (as ingested)

### Comparisons with both yield and cost (6 Commonplace, 1 external)

- A1 five-link cap versus uncapped (consumption bytes and opened counts; no
  tokens or price; cost partly in basis)
- A2 description-length assay (projected pointer tokens; cost in basis)
- A3 trace-first versus claim-first meta-analyser (calls, seconds, usage;
  cost was the tie-breaker)
- A4 per-gate versus bundled review output (cost and yield in separate
  records; adopted on cost, yield checked afterwards)
- A7 AutoReason trial (aggregate agents and minutes only; not per arm; not in
  basis)
- B synthesis-distinction pilot (tokens and seconds; cost as a ceiling, not
  in basis)
- C1 PrimeScientist (budget-matched tokens; cost in basis)

Strictly per-arm cost appears only in A2, A3, A4 (cost side), B
synthesis-distinction and C1. In every Commonplace case where cost entered
the basis (A2, A3, A4), it agreed with or tied the yield reading; no recorded
Commonplace preference was reversed by cost.

---

## Routine controllers and their cost-per-yield records

| Controller | Yield record | Cost record | Cost per yield anywhere? |
|---|---|---|---|
| Connect prospecting (`kb/instructions/cp-skill-connect/SKILL.md`) | none comparing samplers; mining workshop counts recurring hubs only | ordinal only: sources listed "In order of cost"; full titles listing is "roughly a quarter of" the description listing; adoption of fresh titles listing (error-catching `systematisation.md`) has no measurement | No |
| Review bundle selection / packing | gate-stats catch rates by bundle size and grouping | single-artifact cost report (tokens, $ per gate) | Separately only; never on the same runs, never as cost per finding |
| Grounding reading budget (cap 5 → 16) | A1 divergences | bytes and opened counts | Not as a ratio; record disclaims an attention price |
| Full-pass finding routing (`kb/instructions/run-full-improvement-pass-on-note.md`, `kb/types/full-pass-report.md`) | dispositions per pass; ADR 066 log entry (23 passes, zero accepted conversions) | none found: no cost field in the report type; one report instance in `kb/` | No |
| revise-autoreason critic (`kb/instructions/cp-skill-revise-autoreason/SKILL.md`) | one trial (A7) | skill states a call budget ("up to 5 passes. A normal pass uses 7 fresh Codex sub-agents"); trial records 11.6 minutes | No (one run, no per-arm cost) |
| Review gates as detectors | catch rates per gate and lens (gate-stats); calibration recall | systematisation table says "cheap per pair" without figures; calibration "rerun cost is ~11 agent tasks per 8 gates" | No |
