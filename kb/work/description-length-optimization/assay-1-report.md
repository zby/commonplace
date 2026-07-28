# Assay 1: marginal description value in realistic candidate sets

> Subsequent decision, 2026-07-27: the user adopted 250 characters as the global soft upper warning. The report below preserves the assay's pre-decision conclusion and uncertainty.

## Result

The provisional 250-character soft-warning hypothesis survives this first assay, but the evidence does not yet establish 250 as a globally optimal limit.

Descriptions under all five allowances retrieved 9 of 10 targets perfectly. The sole discriminating case was a source ingest placed beside its same-title raw snapshot: 120, 160, and 200-character variants sometimes selected the snapshot, while 250 and 300-character variants selected the ingest in every run. Across all 44 trials per allowance, retrieval recall was 95.5% at 120, 97.7% at 160 and 200, and 100% at 250 and 300. The uncertainty intervals overlap, so this is a useful failure mechanism, not yet a statistically decisive global threshold.

There was no measured retrieval benefit from 300 over 250. Under a declared 8,000-token-estimate pointer budget, descriptions shaped to the 250 allowance fit both the observed p95 tag slice of 70 results and the 80-result assay condition; descriptions shaped to 300 exceed the budget at 80 results. That places 250 on this assay's observed Pareto frontier and makes 300 dominated.

The practical conclusion is therefore:

- Do not defend the current 200 warning as an index-size necessity; this assay found a realistic disambiguation that benefited from more room.
- Keep 250 as the leading candidate for a **soft global warning**, not a hard maximum.
- Do not change the shipped contract from this run alone. The benefit came from one source-ingest/snapshot pair, while every other target plateaued at or below 120.
- Test more same-title and same-lineage artifact pairs before deciding whether source artifacts need type-specific guidance or whether a better title/path distinction solves the problem without longer descriptions.

## What ran

### Cases and variants

Ten actual artifacts were stratified across four theoretical notes, one definition, one ADR, one reference document, two instructions, and one source ingest. Title strength was classified before evaluation as four strong, four medium, and two weak cases. The case set intentionally included short and long incumbents and close conceptual neighborhoods.

Each target received independently written truthful variants under 120, 160, 200, 250, and 300-character ceilings. These were ceilings rather than padded target lengths; mean realized lengths were 110.1, 147.8, 185.9, 242.7, and 289.9 characters. An independent reviewer checked every variant against the full artifact: 50 of 50 passed semantic-fidelity review.

The frozen definitions are in [cases.json](./cases.json). The reviewer judgments are in [generated/fidelity-review.json](./generated/fidelity-review.json).

### Retrieval trials

For each task, the target was mixed with real corpus artifacts chosen by deterministic lexical overlap between the task and each incumbent path/title/description pointer. Only the target description changed across allowances; distractors retained their incumbent descriptions. This isolates the marginal value of the target description beyond its title and path.

The evaluator selected every artifact it would open, with abstention allowed and unnecessary opens explicitly costed. Trials were:

| Candidate count | Cases | Order repetitions | Trials per allowance | Total trials |
|---:|---:|---:|---:|---:|
| 5 | 10 | 2 | 20 | 100 |
| 20 | 10 | 2 | 20 | 100 |
| 80 | 4 | 1 | 4 | 20 |
| **Total** |  |  | **44** | **220** |

The large condition used one theoretical note, one definition, one ADR, and the source ingest. Candidate order was deterministically randomized by case, scale, allowance, and repetition. Exact prompts and raw results are preserved under [generated](./generated/README.md).

### Evaluator provenance

Thirty retrieval batches, ten split fidelity batches, and ten downstream batches completed successfully: 50 model calls producing 220 retrieval decisions, 50 fidelity judgments, and 40 downstream answers. All successful calls used Codex CLI 0.145.0, default model `gpt-5.6-sol`, high reasoning effort, and read-only evaluator sandboxes. The logs report 786,820 retrieval tokens, 277,943 fidelity tokens, and 267,577 downstream tokens, or 1,332,340 tokens total. These are runner-reported whole-call tokens, not pointer tokens.

Two pre-inference problems were excluded from the measurements:

- the requested `luna` model alias was unsupported for the active ChatGPT account;
- the first retrieval attempt used the JSON Schema keyword `uniqueItems`, which this response-format implementation rejects. All 30 calls failed before inference; the keyword was removed and the frozen prompts were rerun successfully.

Wall time and monetary inference cost were not captured consistently and are not reported.

## Retrieval measurements

Each allowance has 44 trials. Confidence intervals are 95% Wilson intervals for target recall.

| Allowance | Target recall | 95% interval | False skips | Irrelevant opens | Mean realized target description |
|---:|---:|---:|---:|---:|---:|
| 120 | 42/44 (95.5%) | 84.9–98.7% | 2 | 2 | 110.1 chars |
| 160 | 43/44 (97.7%) | 88.2–99.6% | 1 | 1 | 147.8 chars |
| 200 | 43/44 (97.7%) | 88.2–99.6% | 1 | 1 | 185.9 chars |
| 250 | 44/44 (100%) | 92.0–100% | 0 | 0 | 242.7 chars |
| 300 | 44/44 (100%) | 92.0–100% | 0 | 0 | 289.9 chars |

Every incorrect selection chose exactly one irrelevant artifact and omitted the target. All four errors were the same source case: the evaluator selected `trajectory-informed-memory-generation-self-improving-agents.md` rather than the requested `.ingest.md` analysis. The failures occurred at 120 in one 5-result and one 20-result ordering, at 160 in one 5-result ordering, and at 200 in one 5-result ordering. The 250 and 300 variants were stable across all five trials of that case.

This failure is meaningful because the raw snapshot and ingest share a stem and much factual content. The task also requested the KB's assessment of the narrow task-completion oracle. Shorter descriptions identified the paper and its result but did not always supply enough artifact-role or analytical-scope information to distinguish the analysis from the source.

At 5 candidates, recall was 95% for 120–200 and 100% for 250–300. At 20, it was 95% at 120 and 100% for every other allowance. All 80-candidate trials succeeded at every allowance. The 80-result condition had only four comparatively easy cases and one ordering, so its perfect result is weak evidence about attention under large slices.

## Downstream subset

The 20-candidate selections for four cases (pointer design, representational form, ADR 025, and trajectory memory) continued into a body-reading task at both order repetitions: 40 downstream trials. The evaluator received only the first 15,000 characters of each selected artifact and answered a predeclared factual question. A deterministic, case-specific required-term rubric scored the answers; the rubric is in [downstream-cases.json](./downstream-cases.json).

| Allowance | Success | Body characters loaded across 8 trials |
|---:|---:|---:|
| 120 | 7/8 (87.5%) | 59,028 |
| 160 | 8/8 (100%) | 64,644 |
| 200 | 8/8 (100%) | 64,644 |
| 250 | 8/8 (100%) | 64,644 |
| 300 | 8/8 (100%) | 64,644 |

The only failure followed the 120-character source mis-selection. The raw paper snapshot supported the 14.3-point AppWorld result but not the KB analysis's oracle limitation, and the evaluator explicitly reported that the evidence was insufficient. The other shorter-condition retrieval misses occurred only in the 5-candidate condition, which this downstream subset did not continue. This downstream result therefore connects one false skip to task failure but does not distinguish 160, 200, 250, and 300.

## Pointer-context cost

The live 769-artifact pointer corpus has mean path/title/format overhead of 120.7 characters per result (p95 169) and mean incumbent description length of 179.4 characters (p95 273). Across the 30 actual retrieval prompts, changing one target while holding distractors fixed produced these mean total pointer costs:

| Candidates | 120 | 160 | 200 | 250 | 300 |
|---:|---:|---:|---:|---:|---:|
| 5 | 1,697 chars | 1,734 | 1,772 | 1,829 | 1,876 |
| 20 | 6,959 chars | 6,996 | 7,034 | 7,091 | 7,138 |
| 80 | 26,988 chars | 27,026 | 27,061 | 27,119 | 27,164 |

Those rows measure marginal target substitution, not a policy applied to every result. For the policy-level budget check, scaling mean corpus overhead plus each allowance's mean realized description to 80 results gives approximately 4,616, 5,370, 6,132, 7,268, and 8,212 tokens respectively, using `ceil(characters / 4)`.

The current corpus has 30 used note tags. Their membership counts have median 14, p95 70, and maximum 105 (`learning-theory`). With a declared first-assay budget of 8,000 estimated pointer tokens:

- 250-character-shaped descriptions project to about 6,360 tokens at the p95 70-result slice and 7,268 at 80;
- 300-character-shaped descriptions project to about 7,185 at 70 but 8,212 at 80;
- neither 250 nor 300 fits the 105-result maximum without candidate-set control (about 9,540 and 10,780 tokens respectively).

The evaluator's exact tokenizer was unavailable locally. Character and UTF-8 byte counts in `manifest.json` are exact; all pointer-token figures are explicitly labelled four-characters-per-token estimates. The budget is a declared experimental budget, not a shipped Commonplace contract.

## Interpretation

### Why 250 survives

250 is the shortest allowance with perfect observed retrieval, zero irrelevant opens, and perfect observed downstream performance. It also fits the declared budget at the observed p95 tag size and the deliberately larger 80-result condition. Since 300 added cost without improving any measured result and breaches the 80-result budget projection, 300 is dominated in this assay.

### Why this does not settle the global contract

Nine targets showed no measurable benefit above 120. The apparent 250 advantage is entirely one artifact-role collision, and 160 or 200 sometimes also resolved it. Wilson intervals overlap substantially, one evaluator model supplied all judgments, and the tasks often used vocabulary present in strong titles and paths. The result supports extra headroom for unusually discriminating descriptions, not a claim that ordinary descriptions should approach 250 characters.

The source case also admits a cheaper alternative explanation: `.md` versus `.ingest.md` is a path-level role distinction that the evaluator failed to use consistently. Better title or role display may remove the need for longer source descriptions. The next assay must compare those interventions rather than attribute the whole gain to length.

## Limitations and next assay

- The case set has 10 targets rather than the planned 40–60. This was a deliberately bounded first execution with real variants and independent judgments.
- One model (`gpt-5.6-sol`) and two orderings at only the 5/20 scales do not establish cross-model or sampling variance. The 80 scale has four cases and one ordering.
- Candidate ranking uses lexical overlap with a task written for the target, which can make titles and descriptions unusually diagnostic.
- Only the target description changes. This isolates marginal information but does not measure interference when every candidate becomes longer.
- Artifact-type coverage is too sparse to justify type-specific numeric limits; the source class has one target.
- Title-strength labels were author judgments rather than independently calibrated measurements.
- Downstream success used four cases, 15,000-character excerpts, and deterministic required-term rubrics. It demonstrates one propagated miss, not broad task quality.
- Exact evaluator pointer tokens, wall time, and monetary cost were unavailable.

The next run should concentrate power where this run found uncertainty:

1. Add 15–20 same-title or same-lineage pairs: snapshot/ingest, proposal/ADR, instruction/skill, definition/theoretical note, and current/superseded reference.
2. Factor description allowance against explicit artifact-role display, holding wording constant, to test whether length or role discrimination caused the source result.
3. Add 20 ordinary targets sampled without author-chosen retrieval vocabulary, including genuinely weak titles.
4. Run at least two evaluator models and three independent repetitions at 20 candidates; reserve the 80-result condition for the subset that remains difficult.
5. Apply each allowance to all candidates in a slice so aggregate attention effects and policy-level context costs are measured directly.

Until then, the appropriate decision status is: **250 remains the provisional soft-warning candidate; 200 has no recovered architectural rationale; no shipped change yet.**
