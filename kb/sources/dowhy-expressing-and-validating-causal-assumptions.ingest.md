---
description: "DoWhy grounds the assumption boundary for causal reach assessment: causal estimates require declared assumptions and only partial validation"
source_snapshot: "kb/sources/dowhy-expressing-and-validating-causal-assumptions.md"
ingested: "2026-07-16"
type: kb/sources/types/ingest-report.md
domains: [causal-inference, assumptions, reach-assessment]
---

# Ingest: DoWhy: Addressing Challenges in Expressing and Validating Causal Assumptions

Source: [dowhy-expressing-and-validating-causal-assumptions.md](./dowhy-expressing-and-validating-causal-assumptions.md)
Captured: 2026-07-16
From: <https://arxiv.org/abs/2108.13518>

## Classification

Genre: scientific-paper -- a workshop/method paper describing a causal-inference framework and the challenge of expressing and partially validating assumptions. The genre recorded on the snapshot is correct.
Domains: causal-inference, assumptions, reach-assessment
Author: Amit Sharma, Vasilis Syrgkanis, Cheng Zhang, and Emre Kiciman from Microsoft Research; strong practitioner-research authority for causal inference tooling, with the usual tool-builder interest in the framework's framing.

## Summary

The paper argues that causal-effect estimation depends on assumptions about the data-generating process, and unlike predictive modeling there is no global validator for a causal estimate. DoWhy's response is to make assumptions explicit through causal graphs, use identification procedures such as graph-based criteria and do-calculus, estimate effects, and run refutation or validation tests for subsets of the assumptions. For this KB, the source is the boundary condition on causal reach assessment: causal formalism can assess reach only as far as the assumptions are declared and partially checkable.

## Connections Found

This source supports [reach assessment](../notes/definitions/reach-assessment.md) and [Formal symbolic systems assess reach only through causal and proof obligations](../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md) by grounding the warning that causal discovery and causal inference are not assumption-free. It also fits [Warranted autonomy is bounded by oracle reach](../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) as a domain-specific example: automation can run the causal pipeline, but the warrant stops where assumptions cannot be globally validated.

## Extractable Value

1. **Assumptions are first-class artifacts** -- A formal reach-assessment system must represent graph, confounding, mediation, instrument, and identification assumptions explicitly, not bury them in an estimator. [quick-win]
2. **There is no global causal validator** -- This is the strongest caution against treating causal inference as a magic reach oracle. Validation is partial and assumption-specific. [quick-win]
3. **Do-calculus identifies effects, not graphs by itself** -- Useful correction for the Gödel-machine speculation: adding do-calculus to axioms is not enough unless graph learning or graph assumptions are also present. [quick-win]
4. **Causal discovery and causal inference need integration** -- The source names the gap between building the graph and estimating the effect, which maps to the design surface for a future formal symbolic reach-assessment system. [experiment]

## Limitations (our opinion)

The source is partly a tool-framework argument, so it should not be read as independent proof that DoWhy's particular API solves causal validation. The paper is most valuable for its negative claim -- assumptions are unavoidable and only partly testable -- and for the workflow decomposition. It does not make causal assumptions true, and it does not supply the missing semantic judgment for natural-language claims.

## Recommended Next Action

Keep this source as the cautionary citation in [Formal symbolic systems assess reach only through causal and proof obligations](../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md) for the assumption boundary of causal reach assessment; no separate promotion is needed now.
