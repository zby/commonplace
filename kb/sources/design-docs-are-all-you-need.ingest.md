---
description: "SMART regenerates a symbolic performance library from worked-example design docs; its human revision loop supports specification feedback, while reference agreement leaves broader maintenance claims untested."
source: https://arxiv.org/abs/2609.05364
captured: "2026-09-24"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 8fc3c51052093b5c9bdec7a5264874946796c72cbd79fea9a06f5c8d55e28dea
ingested: "2026-09-25"
type: kb/sources/types/ingest-report.md
domains: [specification-strategy, code-generation, context-engineering]
learning_claims: true
---

# Ingest: Design Docs Are All You Need

## Classification

A short technical paper presenting SMART's architecture and its authors' experience regenerating a specialized library. It reports reference-model agreement and approximate rebuild costs, but provides no controlled comparison or component ablation. Authors Samuel Kushnir and colleagues are affiliated with Google DeepMind, Google, MIT, and Stanford; they describe their own system.

## Summary

SMART makes natural-language design documents the durable authority for a symbolic ML performance-modeling library, regenerating code on version changes. Read-only agents infer a document dependency graph; an orchestrator then assigns one coding agent per document in dependency order and records interpretation difficulties and bugs for human revision of the documents. Worked examples specify intermediate values and exact expected expressions. A compact recursive operator representation separates model composition from system pricing, with analytical and scheduling-based cost aggregation. Within this specialized symbolic architecture, the authors report agreement with hand-audited reference models to round-off precision, including DeepSeek-V3 serving on a TPU pod slice. They describe 50 documents, about 9,000 prose lines, and rebuilds taking 1.5–3 hours at about USD 100 in API cost. The source offers a concrete document-authority workflow; it does not demonstrate that full regeneration improves maintenance over incremental development.

## Quotes

No source quotes have been retained yet.

## Connections Found

SMART is a bounded implementation example for [specification strategy following where understanding lives](../notes/specification-strategy-should-follow-where-understanding-lives.md): documents govern generation, while execution difficulties return through an orchestrator's log to human edits for the next version. This supports the feasibility of combining upfront specification with feedback from execution, rather than comparing their relative effectiveness.

The worked traces also supply a concrete comparison for [agentic systems interpreting underspecified instructions](../notes/agentic-systems-interpret-underspecified-instructions.md). Traces and exact expected outputs constrain interpretation, but every regeneration still selects an implementation. Reported agreement with selected references under SMART's symbolic cost-model architecture establishes neither identical builds nor equivalence outside those checks.

## Learning Claims (our opinion)

The paper invokes in-context learning to explain why worked examples help generating agents. It separately describes persistent adaptation through humans revising documents after inspecting logged difficulties and bugs. These are different mechanisms: using a supplied example need not revise any retained claim, whereas the human revision loop can change what later generations consume.

In Commonplace terms, the latter makes the system a [theory builder](../notes/definitions/theory-builder.md) at the boundary containing the humans, documents, agents, and checks, at the strength of reported practice. The design documents are localized content (condition 1), and generation consumes them (condition 2). Logged interpretation difficulties and bugs point engineers at the documents that need revision, which is criticism aimed at what particular documents say (condition 3). The revised documents are retained and regenerate the library for each new version, a later problem with new requirements (condition 4). The document units and localized logs also offer [addressability](../notes/definitions/addressable-theory.md) above condition 1's minimum. Learning is a separate claim: the paper supplies no worked history connecting a particular criticism, document revision, and improvement in later capacity.

The generation stage implements the supplied document boundaries, operator representation, and reference expectations. Humans can revise those documents, but the source does not compare alternative decompositions or show their revision through feedback. As [learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) explains, successful work within the supplied architecture cannot establish that its fixed choices are preferable.

## Extractable Value

1. **Keep specification authority while returning execution discoveries to it.** The interpretation-and-bug log gives humans a concrete input for revising the next generation's instructions. This is a useful reported case for the existing specification-strategy note, with the human revision role preserved. [quick-win]
2. **Pair prose with traces and exact reconciliation anchors.** SMART combines intermediate shapes and values with expected symbolic expressions and generated assertions. Testing this pattern on one numerical Commonplace procedure could assess whether it reduces repeated interpretation failures; the paper itself does not isolate its effect. [experiment]
3. **Retain a feasibility observation with its domain boundary.** The reported rebuild times, approximate costs, and reference agreement concern a library designed around a compact symbolic representation and hand-audited references. They can inform a regeneration experiment, but cannot supply a general cost or reliability forecast. [just-a-reference]

## Limitations (our opinion)

There is no incremental-development baseline, repeated-build distribution, failure-rate accounting, or ablation separating worked examples, document partitioning, orchestration, and the symbolic representation. A simpler explanation for the reported success is that this particular domain admits compact formulas and strong reference checks. The source does not establish which ingredient causes reliability or how much human specification and reference work the quoted rebuild cost excludes.

The paper defines technical debt as a difference from a fresh implementation and declares that difference zero when rebuilding from scratch. This removes dependence on the prior code by construction; it does not measure maintenance quality, eliminate defects in specifications, or prove that two fresh generations behave alike. Its broad debt claim should not be retained as an empirical result.

Reference-model agreement checks conformance to selected hand-audited models. It does not establish prediction accuracy against hardware measurements or coverage of untested configurations. Dynamic model routing is presented as a possible architectural benefit without a measured contribution. The captured paper supplies neither detailed reconciliation results nor an implementation inspected here, so the reported outcomes remain author claims.

## Recommended Next Action

Update [Specification strategy should follow where understanding lives](../notes/specification-strategy-should-follow-where-understanding-lives.md) with SMART as a bounded reported case of execution feedback guiding human revision of authoritative design documents.
