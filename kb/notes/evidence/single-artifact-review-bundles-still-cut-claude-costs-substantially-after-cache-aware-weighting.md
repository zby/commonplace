---
description: April 2-4, 2026 review telemetry reweighted with Anthropic Opus 4.6 prompt-caching prices still shows a substantial cost drop from the single-artifact bundle refactor
type: note
traits: [has-external-sources]
tags: [evaluation, kb-maintenance, observability]
status: current
---

# Single-artifact review bundles still cut Claude costs substantially after cache-aware weighting

The switch from per-gate writes to one bundled review artifact was a real efficiency win. Even after reweighting the runs with Anthropic's prompt-caching prices, the bundled path still shows a substantial cost reduction. The important correction is only that the billing gain is smaller than the raw-token gain, because many of the removed tokens were discounted cache reads rather than full-price output or uncached input.

The measurements below come from `kb/reports/review-store.sqlite`, using Claude review runs created by `scripts/run_review_bundle.py` between April 2, 2026 and April 4, 2026.

## Pricing correction

Anthropic's prompt-caching docs say automatic caching defaults to a 5-minute TTL, that a 1-hour TTL costs 2x base input price, and that cache reads cost 0.1x base input price. For Claude Opus 4.6, the current prices are $5 / MTok input, $10 / MTok 1-hour cache writes, $0.50 / MTok cache reads, and $25 / MTok output ([Anthropic prompt caching docs](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)).

In the bundled runs where request-level telemetry is preserved, every observed cache write lands in `ephemeral_1h_input_tokens` and none in `ephemeral_5m_input_tokens`. I therefore priced the experiment as:

```text
cost_usd =
  input_tokens * 5e-6 +
  cache_creation_input_tokens * 10e-6 +
  cache_read_input_tokens * 0.5e-6 +
  output_tokens * 25e-6
```

The older April 2 rows keep only flattened totals (`cache_creation_input_tokens`, `cache_read_input_tokens`, `output_tokens`) rather than per-request TTL detail, so applying the 1-hour write rate to those rows is an inference from the newer detailed telemetry, not a directly observed fact.

## Dataset

- **Old baseline:** 35 successful Claude `opus-4-6` runs on April 2, 2026, each reviewing 6 gates with the older per-gate write path.
- **New like-for-like set:** 14 successful Claude `opus-4-6` bundled-output runs on April 3-4, 2026, also reviewing 6 gates.
- **Morning batch:** 67 successful Claude `opus-4-6` bundled-output runs on April 4, 2026 between 03:00 and 03:29 CEST, each reviewing 4 gates.
- Failed runs and a synthetic zero-token run were excluded.

## Result

- **Like-for-like 6-gate comparison:** median raw tokens per gate fell from 29,730 to 9,988, a 66.4% reduction. Median weighted cost per gate fell from $0.0962 to $0.0714, a 25.8% reduction.
- **Morning 4-gate batch versus old 6-gate baseline:** median raw tokens per gate fell to 14,806, a 50.2% reduction. Median weighted cost per gate fell to $0.0521, a 45.8% reduction.
- **Same-note overlap:** for 35 notes reviewed in both eras, the median per-note change was -52.8% in raw tokens per gate and -50.8% in weighted cost per gate.

The refactor therefore looks successful under every comparison I can make from the available telemetry. The refinement is only that the biggest raw-token wins came from cheap token classes.

## Why the billing gain is smaller than the raw-token gain

In the old 6-gate runs, cache reads were 81.6% of all raw tokens but only 13.4% of weighted cost. Output tokens were only 5.4% of raw tokens but 44.1% of weighted cost. That means a change that mostly removes cache-read-heavy follow-up turns looks dramatic in token totals while moving dollars much less.

The bundled-output refactor still improved the harness in two real ways:

- It reduced median request count from 6 in the old 6-gate runs to 2 in the new 6-gate runs.
- It reduced weighted cost as well as raw tokens; the reduction is just smaller than the raw-token headline suggests.

So the correct reading is:

- raw-token reduction is the right sign for efficiency
- cost reduction is smaller because cache-heavy runs are not priced linearly in raw tokens
- request-count reduction still matters for latency, rate limits, and operational simplicity even when billing savings are muted

## Caveats

- This is not a controlled A/B test. Bundle sizes changed, and most of the April 4 morning runs used 4-gate bundles rather than 6-gate bundles.
- The old April 2 telemetry does not preserve explicit TTL buckets, so the 1-hour write assumption is inferred from the newer detailed rows. If those older writes had actually been priced as 5-minute writes, the like-for-like 6-gate cost reduction would be larger, roughly in the low-to-mid 30% range rather than the mid-20% range.
- This note only prices Claude `opus-4-6` runs under Anthropic's current Opus 4.6 prompt-caching rules. It does not estimate latency savings or rate-limit savings separately.

---

Relevant Notes:

- [semantic-review-catches-content-errors-that-structural-validation-cannot](../semantic-review-catches-content-errors-that-structural-validation-cannot.md) — extends: quantifies the review system's "different cost model" claim with measured run telemetry
- [quality-signals-for-kb-evaluation](../quality-signals-for-kb-evaluation.md) — exemplifies: review telemetry is a concrete operational signal rather than a purely theoretical oracle candidate
- [oracle-strength-spectrum](../oracle-strength-spectrum.md) — grounds: investing in telemetry before capability only helps if the telemetry is interpreted with the right cost model
- [selector-loaded-review-gates-could-let-review-revise-learn-from-accepted-edits](../selector-loaded-review-gates-could-let-review-revise-learn-from-accepted-edits.md) — motivates: slimmer review harnesses reduce both context load and follow-up request churn
- [010-review state should move to sqlite once reviews leave git and accumulate operational metadata](../adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and-accumulate-operational-metadata.md) — enables: the SQLite review store made this measurement possible
