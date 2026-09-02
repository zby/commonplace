---
description: "Review of 25 industrial MDE studies finds mostly small-scale, mixed benefit reports and too little evidence to generalize about large-scale adoption."
source: https://www.sintef.no/publikasjoner/publikasjon/1274286/
captured: "2026-09-02"
capture: trafilatura
capture_scope: abstract
genre: scientific-paper
snapshot_sha256: 2fcef27bd23af1b9740c0e2e715da83a651180fc41b149ac3a8d81193ba8a87e
ingested: "2026-09-02"
occasion: "for kb/work/factory-theory-restart we need to ground the failure claim - snapshot and ingest a retrospective"
type: kb/sources/types/ingest-report.md
domains: [model-driven-engineering, software-factories, industrial-adoption]
---

# Ingest: Where Is the Proof? — A Review of Experiences from Applying MDE in Industry

## Classification

This is a scientific paper reporting a systematic literature review of 25 empirical studies of industrial model-driven engineering (MDE) published from 2000 through June 2007. Author: Parastoo Mohagheghi and Vegard Dehlen are named as the review authors; the capture is a SINTEF publication record, but its abstract does not expose their affiliations, review protocol, or possible interests in the framing.

## Summary

The review asks whether published industrial evidence supported claimed MDE benefits. Its search found 25 papers and reports quality improvements plus both productivity gains and losses, but mainly in small-scale studies. It found only a few reports of advantages in larger projects and says third-party tool environments were generally perceived as too immature for large-scale industrial adoption. The authors therefore conclude that the evidence available through June 2007 was too limited to generalize. For a decision-maker, the source supports an evidence-boundary claim about contemporaneous MDE outcomes, not a categorical claim that MDE or software factories failed.

## Quotes

- **Source extract (verbatim):** In most cases the maturity of third-party tool environments is still perceived as unsatisfactory for large-scale industrial adoption. We found reports of improvements in software quality and of both productivity gains and losses, but these reports were mainly from small-scale studies. There are a few reports on advantages of applying MDE in larger projects, however, more empirical studies and detailed data are needed to strengthen the evidence. We conclude that there is too little evidence to allow generalization of the results at this stage.
  - **Source location:** Abstract

## Connections Found

This review is a contemporaneous evidence-boundary anchor for the software-factory and MDE retrospective. It compares with [the reconstructed software-factory ontology](../notes/a-software-factory-is-family-scoped-lifecycle-production-machinery.md) by separating the proposed family-scoped machinery from what industrial studies had established: published quality and productivity results were mainly small-scale and did not warrant generalization. It also supports the scope discipline in [Universal software factory needs a declared universality axis](../notes/universal-software-factory-needs-a-declared-universality-axis.md). Read alongside [Greenfield's broad program](./greenfield-mass-customizing-software-factories-2007.ingest.md) and the later [MDE practice study](./state-of-practice-in-model-driven-engineering.ingest.md), it distinguishes programmatic promise, weak contemporaneous outcome evidence, and later reports of bounded success with scale-up difficulty. It does not establish categorical failure.

## Extractable Value

1. **Narrow the retrospective failure claim to failure of evidentiary warrant.** The review supports saying that the published industrial evidence available through June 2007 was too weak to justify general claims about MDE benefits; it does not support saying that MDE or the software-factory program failed outright. [quick-win]
2. **Keep reported benefits separate from demonstrated reach.** Quality improvements and productivity gains were reported, but so were productivity losses, and most reports came from small-scale studies. Successful cases therefore do not establish large-scale industrial reach. [quick-win]
3. **Treat tool maturity as a reported adoption constraint, not a complete causal explanation.** The abstract says third-party environments were generally perceived as unsatisfactory for large-scale adoption, but it does not isolate tool maturity from organizational, methodological, or domain factors. [deep-dive]
4. **Use the source in a time-ordered promise/evidence/practice comparison.** Greenfield's 2007 account states the factory program, this review marks the contemporaneous evidence gap, and the 2014 practitioner study adds later evidence of narrow success and scale-up difficulty. [just-a-reference]

## Limitations (our opinion)

The retained capture contains only the abstract. It does not expose the search protocol, inclusion and exclusion criteria, quality assessment, individual studies, sample sizes, outcome definitions, industrial contexts, or treatment of publication bias. The ingest therefore cannot judge whether the 25-paper corpus was representative or whether the review synthesized heterogeneous MDE interventions appropriately. Its evidence horizon also ends in June 2007, so it cannot establish later or current MDE outcomes.

The abstract reports study-level benefits and losses without enough detail to attribute them to MDE, third-party tool maturity, organizational conditions, or other differences. It also does not describe the evaluated systems closely enough to identify the signals and histories available to them, the operations they could compose, the mappings they could express, or the representations and process partitions fixed outside their effective update spaces. Any improvement within a particular MDE setup therefore cannot validate its fixed decomposition from this capture. The authors' conclusion supports insufficient generalizable evidence, not an industry-wide failure rate, a causal account of failure, or an explanation of any particular vendor's retreat.

## Recommended Next Action

Revise the factory-theory-restart failure claim to say that industrial MDE benefit evidence available through June 2007 was mainly small-scale and insufficient for generalization, and cite this ingest as the contemporaneous evidence boundary.
