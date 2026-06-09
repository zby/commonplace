---
description: "Manifesto arguing text optimization is a legitimate, sample-efficient update mechanism enabling update-time compute — upstream restatement of the KB continual-learning cluster"
source_snapshot: "we-should-take-text-optimization-more-seriously-2064027464926716154.md"
ingested: "2026-06-09"
type: kb/sources/types/ingest-report.md
source_type: conceptual-essay
domains: [continual-learning, context-engineering, text-optimization]
---

# Ingest: We Should Take Text Optimization More Seriously

Source: we-should-take-text-optimization-more-seriously-2064027464926716154.md
Captured: 2026-06-09T15:02:46Z
From: https://x.com/yoonholeee/status/2064027464926716154 (cross-posted from yoonholee.com/blog/2026/we-should-take-text-optimization-more-seriously/)

## Classification

Type: conceptual-essay -- a position piece/manifesto arguing a theoretical stance ("the text layer should be taken more seriously"). It argues by analogy, rebuttal, and existence-argument rather than reporting an experiment or proposing a specific system. Carries citation footnotes but no original methodology or data.
Domains: continual-learning, context-engineering, text-optimization
Author: @yoonholee (Yoonho Lee). Same author as the Meta-Harness paper already cited in this KB (`treat-continual-learning-as-substrate-coevolution`, the trace-derived survey). Acknowledges feedback from researchers including Omar Khattab (lateinteraction, DSPy/GEPA), Chelsea Finn, and others — strong research-community signal. The post is explicitly "a distillation of many conversations with researchers over the past year."

## Summary

The essay argues that the mutable "text layer" around a model (prompts, context, filesystem state, memory, retrieval indices, harness code) deserves the same research seriousness as weight optimization, on three counts: (1) text optimization is a *legitimate* update mechanism with the same functional role as gradient updates — changing future behavior in response to new information; (2) it is far more *sample-efficient* in the low-data regime because short high-likelihood text has low description length (a Kolmogorov-style compression prior), making good text updates "compact patches to a pretrained world prior"; and (3) it opens a new scaling axis, *update-time compute*, where reflective loops can fork, test, and compare multiple hypotheses against evidence in text — something SGD's single committed parameter vector cannot cheaply do. The author reframes weights-vs-text as a *routing problem* (stable repeatedly-useful information belongs in weights; volatile, local, auditable, or not-yet-trusted information stays in text) and casts the text layer as a *staging ground* for behavior eventually distilled into weights. The piece rebuts the standard pro-weights arguments (amortization, new circuits, portability, optimizer theory, universal approximation), grounds the view in extended-cognition lineage (Hutchins, Clark & Chalmers, Bush's Memex, tools-for-thought), and closes with a research agenda: theory of the text layer, better evals, "architecture research" on the design space, HCI for eliciting human input, and scaling-law-grade investment in text optimization.

## Connections Found

The companion connect report (`kb/reports/connect/sources/we-should-take-text-optimization-more-seriously-2064027464926716154.connect.md`) found the article to be a near-exact *upstream restatement* of this KB's continual-learning / substrate-coevolution / deploy-time-learning cluster, with its three pillars mapping one-to-one onto existing notes. Because the source is an immutable `kb/sources/` snapshot (it authors no outbound links), the load-bearing deliverable is seven reverse-edge `evidence` candidates from `kb/notes/` plus one from the agent-memory survey:

- [continual-learning-open-problem-is-behaviour-not-knowledge](../notes/continual-learning-open-problem-is-behaviour-not-knowledge.md) — **evidence** for the legitimacy pillar (text layer is a behaviour-change mechanism co-equal with weight updates).
- [treat-continual-learning-as-substrate-coevolution](../notes/treat-continual-learning-as-substrate-coevolution.md) — **evidence**; the weights/text "routing problem" and co-evolution argument; pairs with the Meta-Harness citation already there.
- [deploy-time-learning-is-the-missing-middle](../notes/deploy-time-learning-is-the-missing-middle.md) — **evidence**; the "staging ground for eventual distillation into weights" restates the deploy-time staging argument.
- [constraining-during-deployment-is-continuous-learning](../notes/constraining-during-deployment-is-continuous-learning.md) — **evidence**; weaker-pressure, auditable, composable text-layer edits accumulating adaptive capacity outside weights.
- [in-context-learning-presupposes-context-engineering](../notes/in-context-learning-presupposes-context-engineering.md) — **evidence**; progressive disclosure / implicitly conditioning on much-larger-than-window context.
- [readable-artifact-loop-is-the-tractable-unit-for-continual-learning](../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) — **evidence**; the update-time-compute / fork-test-compare reflective loop.
- [definitions/distillation](../notes/definitions/distillation.md) — **evidence**; the compact-patch-to-prior framing and the industry pattern of distilling the text layer into weights.
- [trace-derived-learning-techniques-in-related-systems](../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) — **evidence**; cites Reflexion, Trace, GEPA, Meta-Harness, etc. — the same systems the survey catalogues.

The connect report flagged the snapshot as a **split candidate** (seven notes, three pillars, multiple independent assertions), so edges should be distributed across the three pillars rather than concentrated on one note. It found **no new synthesis** opportunity — the article strengthens existing claims rather than implying a higher-order one. Two vocabulary gaps surfaced as non-actionable maintenance context: the KB has no named handle for "update-time compute," and no note grounds the text layer in the extended-cognition lineage (Hutchins / Clark & Chalmers / Memex) the article cites.

## Extractable Value

1. **"Update-time compute" as a named scaling axis** -- a clean, retrievable handle for a concept the KB already gestures at in `readable-artifact-loop-...` and `treat-continual-learning-as-substrate-coevolution` but never names. The framing (reflective loops can fork/test/compare multiple hypotheses where SGD commits each update) is the article's most original and high-reach contribution. [deep-dive]
2. **Weights-vs-text as a routing problem** -- the criterion "stable + repeatedly-useful → weights; volatile, local, auditable, or not-yet-trusted → text" is a sharper decision rule than the KB's substrate-coevolution note currently states, and is directly reusable as an operating principle for what belongs in a KB artifact versus a model. [quick-win]
3. **Kolmogorov / description-length justification for text sample-efficiency** -- "good text updates are compact patches to a pretrained world prior" supplies an information-theoretic backing for the KB's distillation definition (compression-under-a-prior) that the note currently grounds without naming the description-length argument. [just-a-reference]
4. **"Reachable behavior" over "representational capacity"** -- the rebuttal that the right metric is what behaviors are high-likelihood under the implicit prior (and the "headroom between latent capability and deployed behavior" frame) is a crisp framing the KB does not have, relevant to why context engineering matters even with a fixed model. [experiment]
5. **Extended-cognition lineage for the text layer** -- Hutchins (*Cognition in the Wild*), Clark & Chalmers (*Extended Mind*), Bush's Memex, tools-for-thought (Notion/Obsidian). The KB grounds the same intuition in programming/information theory but not in this cognitive-science lineage; a useful citation reservoir if that grounding becomes load-bearing. [just-a-reference]
6. **Rebuttal catalogue of the strongest pro-weights arguments** -- amortization, new circuits, portability, optimizer theory, universal approximation, benchmark-leakage vulnerability — each with the author's strongest steelman and counter. A ready-made structure for any KB note that needs to defend the readable-artifact / text-layer position against the "real learning is in the weights" objection. [just-a-reference]
7. **"Architecture research" / design-space call** -- the observation that instruction hierarchies, DSPy programs, agent skills, harnesses, and memory systems are points in one under-described design space we lack vocabulary for. Parallels (at the meta-level) the KB's `agent-orchestration-occupies-a-multi-dimensional-design-space` and the agent-memory survey's purpose; the connect report routed this to the trace-derived survey rather than the orchestration note. [just-a-reference]

## Limitations (our opinion)

This is editorial opinion. As a conceptual essay, the piece argues largely by analogy and steelman-rebuttal, so its weaknesses are the ones the type's lens predicts:

- **Reasoning by analogy without testing the analogy.** The science-as-text-optimization and extended-mind analogies are evocative but do the persuasive work without a mechanism that says where they break down. The "external text amplifies human intelligence, therefore text optimization is legitimate" existence argument is suggestive, not load-bearing.
- **Empirical claims are citation-pointers, not shown results.** "Orders of magnitude more sample-efficient" and the headroom claims are footnoted to other work (the numbered links did not resolve in the snapshot) rather than demonstrated; the reader cannot judge the strength or settings of those results from this piece.
- **Naming versus explaining.** "Update-time compute" is a compelling label, but the essay names the axis more than it characterizes when scaling it pays off, where it saturates, or how to measure it — the open research it then calls for. Treat the term as a useful handle, not a settled result.
- **Author and selection bias.** Same author as Meta-Harness, and the post is a distillation of conversations among researchers who already work on text-layer methods — the evidence base is selected to support the thesis. It is honest manifesto advocacy, not a balanced survey; the pro-weights arguments are steelmanned by an advocate for the other side. The KB should treat it as strong corroboration of claims it already holds rather than independent confirmation.

## Recommended Next Action

Run `cp-skill-write`/manual edits to add the seven reverse-edge `evidence` links from `kb/notes/` (plus the one from `trace-derived-learning-techniques-in-related-systems.md`) to this snapshot, distributed across the three pillars as the connect report's split-candidate flag advises — this is the natural payload and creates the authored outbound surface that does not yet exist. The single most valuable durable follow-up beyond linking is to evaluate whether **"update-time compute"** warrants its own note or definition (Extractable Value #1): it is the article's most original contribution and the KB currently has no named handle for it. Defer the extended-cognition-lineage grounding (#5) as a source-only reference unless that framing becomes load-bearing.
