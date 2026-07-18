# Gate catch-rate statistics — first execution of the telemetry row

Computed 2026-07-18 from `kb/reports/commonplace-store.sqlite`: 9,286 completed catalog-gate verdicts, 2026-03-13 → 2026-07-17. This is the first-ever consumption of the store at trend level (the systematisation's "telemetry aggregation" row, previously **missing**). Queries inline for refresh; all numbers are snapshots.

## 1. The activation quantification (robust)

First-encounter catch rate — the share of (note, gate) pairs flagged on their *first* review — is **29.6%** overall (n=6,911). Per gate, the top of the table (lifetime rates, n≥30):

| gate | n | catch |
|---|---|---|
| accessibility/undefined-terms | 407 | 67.1% |
| sentence/clause-packing | 245 | 59.2% |
| accessibility/unidentified-references | 216 | 49.1% |
| sentence/misleading-link-text | 248 | 45.6% |
| sentence/parsing-ambiguity | 246 | 43.9% |
| sentence/framing-mismatch | 248 | 43.5% |
| sentence/stock-phrases | 246 | 41.5% |
| sentence/concept-attribution | 248 | 39.9% |

By lens: sentence 45.6%, accessibility 41.5%, prose 23.6%, complexity 21.0%, structural 19.8%, semantic 17.5%, frontmatter 15.6%.

Reading: these are the *most obvious* rules in the catalogue — define your terms, don't pack clauses, make link text honest — and they fire on a third to two-thirds of fresh encounters, in text written by models that state every one of these rules correctly when asked. This is the activation gap (governing claim A) quantified: the cost of a rule being merely *known* rather than *attended*, and the empirical justification for gates as focused-attention allocators. The gradient is itself informative: mechanical-surface lenses (sentence, accessibility) catch at 2–3× the rate of judgment lenses (semantic, frontmatter) — writing attention starves the small distinctions first.

## 2. The fix loop converges (robust)

Consecutive-review transitions for the same (note, gate):

| transition | n |
|---|---|
| pass → pass | 933 |
| warn → pass | 929 |
| warn → warn | 193 |
| pass → warn | 132 |
| fail → pass | 71 |
| other | 67 |

A warn is followed by a pass 79% of the time it is re-reviewed — the warn→fix→re-review loop resolves most findings in one cycle. The regression rate (pass → warn/fail) is ~14% of pass-followups, which is the price of continued editing, not reviewer noise alone. Catch by review ordinal: 1st 29.6% → 2nd 16.2% → 3rd 18.6% → 4th+ 23.8%; the non-monotonic tail is selection — notes reviewed four times are the heavily-rewritten ones, whose later reviews are effectively first reviews of new text.

## 3. Absorption: visible only within a partition (confounded overall)

Naive monthly catch rates are dominated by two confounds: which notes were in the cohort, and which model partition reviewed them. Gate-catalogue growth is *not* a confound (33 of 38 gates existed by March). The cleanest within-partition series is codex: **Apr 75.3% → May 14.1% → Jun 6.8% → Jul 6.9%** — consistent with the April sweep finding the accumulated backlog and the fix waves clearing it, after which new-flow writing violates at a several-times-lower rate. That is an absorption-shaped curve, but note-cohort drift means it is suggestive, not clean. Gate-level absorption (per-gate catch decay on new writing — claim B's promotion criterion) needs more longitudinal data per gate before it is testable; the store schema supports it, the history doesn't yet.

## 4. Reviewer variance is first-order (new finding)

Same month, same seven notes, same snapshots — the final migration sweep ran two partitions side by side: **luna 34.3% vs sol 13.8%** catch. And on the 22 same-snapshot groups reviewed more than once anywhere in history, outcomes disagree in **27%** of groups (sample too small to break down per gate). Partition strictness differences of 2–3× swamp most trends anyone would want to read from this data. Consequences: (a) every trend query must condition on partition; (b) "catch rate" is a property of the (gate, partition) pair, not the gate; (c) the drifting-term instability detector (rename-lessons, surprise 10) must use within-partition oscillation, or it will mostly measure partition disagreement; (d) the same-snapshot disagreement rate is itself worth tracking as the review system's noise floor, and multi-partition sweeps generate its data for free.

## 5. Coverage-bet failures (adjudication candidates)

Gates under 10% lifetime catch with n≥30:

| gate | n | catch |
|---|---|---|
| frontmatter/title-as-claim | 66 | 0.0% |
| semantic/explanatory-reach | 254 | 7.5% |
| semantic/load-bearing-qualifiers | 60 | 8.3% |

Two readings per gate, requiring a human call: the bet failed (the mistake class is rare or already absorbed — retire or merge), or the gate under-catches (the criterion is too loose for its reviewers — tighten or move to a stronger partition). `title-as-claim` at 0/66 is the sharpest case: either the trait convention is fully absorbed into writing practice, or the gate tests nothing its cohort can fail.

## 6. Bundling hypothesis: tested and rejected (2026-07-18)

Operator hypothesis: the mechanical-over-judgment gradient might be a harness artifact — complex gates run in bigger bundles, reviewer performance drops with bundle size. The store says no, on all three prongs. (a) The premise inverts: judgment gates ran in *smaller* bundles (semantic 4.6 pairs/job average) than mechanical ones (sentence 7.5, prose 8.9), so any bundle penalty would bias *against* the observed gradient. (b) Within lens, April onward, catch shows no monotone decline with bundle size — prose rises with it (9→23→29%), accessibility peaks mid (49→61→42%), semantic is flat-noisy; only sentence dips at 9+. (c) Note-grouped jobs slightly out-catch criterion-grouped in five of seven lenses. The dramatic bundle-of-1 under-catch that first suggested an effect is pure era: 93% of single-pair verdicts are March's pre-refactor per-gate write path (claude-opus, 7.8%). One caveat stands from the April refactor history: the bundled-artifact change was adopted on cost telemetry alone, and this is the first check of its detection-quality side — it passes.

**The remaining confound the gradient cannot escape: catch rate = incidence × recall.** The lens gradient could mean mechanical mistakes are more common in fresh writing, or that mechanical gates have higher recall (judgment reviewers holding a higher WARN bar, or missing more of what is present). Same-snapshot disagreement data is too sparse to separate these (n=22). The disentangling instrument is **seeded-violation calibration**: inject known violations of each gate's class into copies of clean notes, run the gates, measure per-gate recall directly. This would also adjudicate the dead gates (finding 5) — distinguishing "absorbed into writing practice" from "blind" — and give the activation quantification (finding 1) a corrected incidence denominator.

## Refresh queries

All tables derive from `review_pairs` joined to `review_jobs` (for `model_partition`), filtered to `result_kind='verdict'`, `completed_at IS NOT NULL`, `criterion_path LIKE 'kb/instructions/review-gates/%'`. Ordinals and transitions via `ROW_NUMBER()`/`LAG()` over `(note_path, criterion_path)` ordered by `completed_at`; same-text groups via `reviewed_note_snapshot_id`. See the shell history of 2026-07-18 or re-derive; a `scripts/` home is warranted once this runs on a schedule.

## What this changes in the systematisation

- Claim A is now quantified (29.6% first-encounter; 67% peak), and gains the lens gradient: attention starves mechanical distinctions before judgment ones.
- Claim B's absorption criterion is supported in shape (within-codex collapse post-sweep) but not yet measurable per gate.
- The telemetry row moves from **missing** to *prototyped* — the remaining gap is scheduling (a periodic run with a report artifact), not analysis.
- New row candidate: same-snapshot disagreement as the review system's noise-floor metric, fed for free by multi-partition sweeps.
