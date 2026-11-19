---
description: Shankar’s dashboard examples show how to inspect generated items side by side for misleading differences in wording, structure and detail.
source: https://fsdatalab.github.io/blog/agent-text-at-scale/
captured: "2026-11-19"
capture: trafilatura
capture_scope: partial-source
genre: practitioner-report
snapshot_sha256: b6593910b606e717463b87ead232c7db5347b8a78512588aa6a89d269b84b637
ingested: "2026-11-19"
type: types/ingest-report.md
domains: [generated text feeds, dashboard readability, session titles]
---

# Ingest: Five Principles for Generating Readable AI Text in Bulk

## Classification

Shreya Shankar draws on firsthand experience generating and reading dashboards. She illustrates her advice with product examples and relates it to earlier research on reading and visualization; she does not report a reader trial of the checklist.

## Summary

Shankar asks how a reader can tell generated items apart at a glance. She recommends predictable subject and verb order, early placement of distinguishing words, and consistent syntax and terms across neighboring items. Differences in detail should convey real differences in the data; verbs should distinguish praise from complaints when that is what the dashboard tracks. Her clearest example is a set of app-review summaries: naming a software version on just one card invites a comparison the other cards cannot answer. The rewrite gives each theme the same two parts—what users said and one example—and displays review counts separately.

## Quotes

No source quotes have been retained yet.

## Connections Found

Shankar supplies a companion case to [Structured output is easier for humans to review](../theory/structured-output-is-easier-for-humans-to-review.md). That note separates evidence from reasoning so a reader can check one argument. Shankar repeats the same fields so a reader can compare *different* items. The [historical memory review type](../agent-memory-systems/types/agent-memory-system-review.md) illustrates an alternative to cutting uneven detail: when a comparison field matters, distinguish an unknown value from a field that does not apply.

## Extractable Value

1. **Review neighboring items together.** For a detail that appears in only one item, ask what its absence from the others implies. Each statement can be accurate in isolation while their juxtaposition suggests a distinction the evidence does not support. [quick-win]
2. **Check the visible prefix.** Read only the first two words of each generated title. A repeated subject may be safe to omit if doing so exposes the action that distinguishes one entry from another. This checks whether a difference is visible, not whether it identifies the right destination. [experiment]

## Limitations (our opinion)

The capture omits the figures, so the full side-by-side wording and layout cannot be checked without the [original article](https://fsdatalab.github.io/blog/agent-text-at-scale/). The theme-card rewrite changes wording, detail selection and the display of counts together. No timed or accuracy comparison establishes whether readers do better, let alone which change helps. Research on sentence parsing motivates a trial; it does not establish a benefit for every generated artifact or for an agent reading a single note.

## Recommended Next Action

Test the cross-item claim as a possible extension to [Structured output is easier for humans to review](../theory/structured-output-is-easier-for-humans-to-review.md): compare human readers’ accuracy at finding a specified difference in two lists that contain the same facts but use repeated versus varying field order.
