---
description: "Accepted decision that grounding reviews budget sixteen distinct linked artifacts globally, count repeated targets once, and disclose sampled coverage without failing on budget alone"
type: ../types/adr.md
tags: []
status: accepted
---

# 079-Grounding reviews budget sixteen distinct linked artifacts

**Status:** accepted
**Date:** 2026-08-25

## Context

The `semantic/grounding-alignment` criterion limited a review to five link
occurrences. That rule could charge the same resolved target repeatedly, did not
say whether tracked ingests shared the budget, and sat below the median seven
distinct artifacts offered across 337 measured targets.

A paired twelve-note assay compared that criterion with an otherwise identical
uncapped criterion under isolated `gpt-5.4` workers. Five outcomes diverged.
One warning recurred in a capped repeat that read all three available artifacts,
so it was reviewer sensitivity rather than a cap effect. Fuller reading exposed
four other findings after 6–16 artifacts, including two FAIL outcomes. The
uncapped cases offering 21–23 artifacts all passed. The population's p90 offer
was sixteen distinct artifacts.

## Decision

`semantic/grounding-alignment` may inspect up to sixteen distinct linked
artifacts in one pass. The budget is global across linked notes, ordinary linked
sources, and tracked ingests. Repeated links to one resolved target consume one
slot, and an ingest consumes one slot whether its Quotes route or its declared
snapshot route is used. The target note and criterion are not linked material
and do not consume the budget.

The limit constrains reading, not verdict semantics. Reaching it is not itself a
WARN or FAIL. When a reviewer stops with a material support route unchecked, it
names that route and scopes the verdict to what it inspected. The review
protocol's consumption record remains provenance for the exact opened paths and
whether budget or sufficiency stopped the pass.

Sixteen is an interim per-artifact ceiling justified by this assay and the
observed p90 offer, not a derived attention price. The separate proposal to
combine artifact count and bytes remains open until a measurement identifies
their relative contribution. Split-pass review is not adopted. Reopen it if
reviews at the new ceiling produce outcome divergence in the tail.

The operativity path is the hashed production gate criterion. Review prompts
embed it as binding judgment instruction, and changing it makes existing pairs
stale through ordinary criterion freshness.

## Considered alternatives

**Keep five.** Rejected because four mechanism-aligned findings appeared only
under fuller reading, and every one was reachable by sixteen artifacts. Two
were material failures rather than differences in explanatory wording.

**Remove the limit.** Rejected because linked reading still consumes reviewer
attention. Uncapped workers opened as many as twenty-two artifacts, while the
three cases beyond sixteen produced no outcome divergence. The observed result
supports moving the boundary, not deleting it.

**Fail a pair when the budget is reached.** Rejected because the budget prices a
review pass, not note correctness. Automatic failure would penalize link density
and would conflate unchecked coverage with demonstrated misgrounding.

**Split an over-budget review into covering passes.** Deferred. It requires
partial-coverage, combination, and freshness semantics that the review model
does not have. The assay found no divergent case above the selected ceiling.
It also could not test split review's severed-support hazard because every
capped baseline was PASS.

**Select enforcement per run.** Rejected for this decision because the setting
would change verdict meaning and therefore review identity. The measured problem
can be addressed in the criterion without adding a run dimension.

**Adopt a count-and-byte price now.** Deferred because capped or uncapped stop
points do not identify the exchange rate between artifact-switching and bytes
read. Choosing coefficients would restate the inherited-number problem in a
more elaborate form.

## Consequences

The budget now counts what the prompt and telemetry already expose: distinct
resolved artifacts. Ingest applicability and deduplication are explicit, and
reviewers can inspect every divergent case observed in the assay without
special review-model machinery. Reviews may load more material than before, and
existing grounding baselines become stale once because the judgment-bearing
criterion changed.

The rule still ignores artifact-size heterogeneity. Reviews above sixteen may
remain sampled, so disclosure and consumption telemetry stay necessary. The
decision is bounded to the production grounding criterion and to the measured
setting: twelve selected source-citing notes, the `codex` partition, and
`gpt-5.4`. It does not establish sixteen as a capacity limit for other gates,
models, or corpora.

---

Relevant Notes:

- [A five-link cap missed four grounding findings in twelve reviews](../../notes/evidence/a-five-link-cap-missed-four-grounding-findings-in-twelve-reviews.md) — evidenced-by: supplies the paired outcomes, repeat baseline, natural reading demand, and limits behind the selected ceiling
- [Grounding alignment gate](../../instructions/review-gates/semantic/grounding-alignment.md) — procedure: carries the operative count, scope, and disclosure rule
- [Review link budget prices reviewer attention](../proposals/review-link-budget-prices-reviewer-attention.md) — see-also: retains the unresolved count-and-byte calibration beyond this interim ceiling
