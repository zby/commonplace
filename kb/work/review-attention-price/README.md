# Workshop: review-attention-price

## Question

What are α and β in the review attention price `α · (distinct artifacts) + β · (bytes read)`, what total budget follows from them, and by what mechanism does a review criterion spend that budget — so that the per-gate reading caps stop being inherited constants?

## Why this workshop exists

ADR 079 moved `semantic/grounding-alignment` from five links to sixteen distinct artifacts on paired evidence. It calls sixteen an interim ceiling: it is the p90 offered count and the largest count any observed miss needed, which is a corpus statistic, not a price. The pricing proposal's blocking item is unchanged — identify α/β and the budget "from an independent attention outcome or a paired packaging assay". Two facts fix the starting point:

- Nothing in the modern pipeline records an independent resource outcome. Of 2,609 telemetry rows, none carries `harness_telemetry_json`; legacy codex rows (jobs 9–2302) did carry token usage at top level, so the runner can supply it.
- The uncapped arm read the corpus maximum (22 artifacts, 322 KB) in one pass with no quality loss observed in that range. Whatever the budget protects, it is not one-pass capacity at current sizes.

The other link-following criteria still carry inherited constants: `sentence/misleading-link-text` and `sentence/concept-attribution` read at most 5 distinct target notes (an interim wording change on 2026-08-25 applied ADR 079's distinct-target counting to both, replacing a count of link occurrences and of identity claims; the number itself is still inherited), and `critique-note` states no limit. Five now looks low by an order of magnitude for reads that cost a title and a paragraph each. A priced mechanism replaces these constants with one budget and per-gate reading patterns; that is the mechanism half of the question.

## The fork this workshop must resolve first

"Attention" has two operational readings, and they need different assays:

- **Cost** — tokens or active time a review spends. Identifiable cheaply by regression once usage is recorded. Yields α/β in token units and a budget that bounds spend.
- **Degradation** — how detection of a real finding falls as count and bytes rise. Identifiable only by holding the evidence task fixed and varying packaging, with known findings as the outcome. Yields α/β in detection-loss units and a budget at the point where a review stops being trustworthy.

The operator decision of 2026-08-25 made the protected resource reviewer attention, not context; ADR 079's cap was chosen on misses, not spend. That points at degradation as the sense the *cap* must answer to, with cost as the cheaper side measurement. [calibration-design.md](./calibration-design.md) runs both tracks and says which constant each produces.

## Scope

In scope: the two assays, their analysis, the α/β and budget estimates with their setting, and the mechanism — either the reviewer spends a priced budget (Mechanism A) or code assembles the evidence pack to a pass size and splits by connected component when it does not fit (Mechanism B, the preferred candidate; see the design). Recommending how the other three link-following criteria adopt it.

Out of scope: editing any production criterion before the estimate exists (each edit stales the population once). Split-pass review and pinning linked material for freshness were out of scope under Mechanism A; under Mechanism B both are consequences of code owning the pack, and the design records them as such rather than as separate decisions.

## What closes this workshop

An ADR selecting α, β, the budget, and the mechanism — or a recorded finding that the degradation assay shows no measurable loss across the corpus range, in which case the budget is a cost budget and the ADR says so. Either way: the fixture set and usage data retained where the routing table sends them, and the temporary trial criteria deleted.

Posed 2026-08-25 by the maintainer: "first of all we need the two constants + cap mechanism".

**2026-08-27.** The maintainer proposed a third mechanism that reverses this workshop's direction: cap the artifact, not the review — a note is sized so its grounding fits one pass ("atomic steps"), and a note with more sources quotes them verbatim so the check becomes mechanical (ADR 046). Under that mechanism Track B and most of Mechanism B are unnecessary. The idea is written up as the draft article [Atomic steps: size the note to its check](../../articles/atomic-steps-size-the-note-to-its-check.md) (workshop: [atomic-step-article](../atomic-step-article/README.md)); the mechanism decision here waits on that draft's review. What it changes for this workshop: under atomic steps the unit of a grounding step is the *unquoted* source — a source quoted verbatim in the note is discharged by the ADR 046 validator, and note links are charged to the representation criteria rather than to grounding — so Track B (degradation) and Mechanism B's code-assembled pack are unnecessary if the artifact-side rule is adopted, and Track A (cost) stays useful only as a side measurement. The number, the validator rule (distinct ingest targets without a verified inline quote ≤ N, with ingest-target quotes matched against `## Quotes` only), and ADR 079's fate remain this workshop's decisions. The corpus counts and the reinterpretation of the four-miss evidence are in that workshop's `grounding.md`.

## Files

- [calibration-design.md](./calibration-design.md) — Tracks A and B, Mechanism A, Mechanism B with pack rules, transport, exception, and splitting
- [change-impact.md](./change-impact.md) — what in the current system each layer of Mechanism B touches; concludes pack (layer 1) needs no store or freshness change, pin and split are separate decisions with recorded arguments against doing them now

## Grounding

- [Pricing a review link budget](../../reference/proposals/review-link-budget-prices-reviewer-attention.md) — tests: this workshop is its adoption criterion
- [ADR 079](../../reference/adr/079-grounding-reviews-budget-sixteen-distinct-linked-artifacts.md) — depends-on: the interim ceiling this would replace with a derived one
- [A five-link cap missed four grounding findings](../../notes/evidence/a-five-link-cap-missed-four-grounding-findings-in-twelve-reviews.md) — draws-on: the paired design, the noise baseline, and the fixture candidates
- [Calibrating semantic gates against labelled fixtures](../../reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md) — depends-on: fixture definition and the leakage rule the degradation assay must respect
- [review_link_consumption.py](../../../scripts/review_link_consumption.py) — produces: offered-vs-consumed aggregation, extended here with usage
