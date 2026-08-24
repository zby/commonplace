---
description: "DoWhy grounds the assumption boundary for causal reach assessment: causal estimates require declared assumptions and only partial validation"
source: https://arxiv.org/abs/2108.13518
captured: "2026-07-16"
capture: pdf-read
genre: scientific-paper
snapshot_sha256: e918a866be472d575e0025c5bd7de18964a1b06c6e5e3a58d073ec1f6ace06e8
ingested: "2026-07-16"
type: kb/sources/types/ingest-report.md
domains: [causal-inference, assumptions, reach-assessment]
---

# Ingest: DoWhy: Addressing Challenges in Expressing and Validating Causal Assumptions

## Classification

A workshop/method paper describing a causal-inference framework and the challenge of expressing and partially validating assumptions. The genre recorded on the snapshot is correct.
Author: Amit Sharma, Vasilis Syrgkanis, Cheng Zhang, and Emre Kiciman from Microsoft Research; strong practitioner-research authority for causal inference tooling, with the usual tool-builder interest in the framework's framing.

## Summary

The paper argues that causal-effect estimation depends on assumptions about the data-generating process, and unlike predictive modeling there is no global validator for a causal estimate. DoWhy's response is to make assumptions explicit through causal graphs, use identification procedures such as graph-based criteria and do-calculus, estimate effects, and run refutation or validation tests for subsets of the assumptions. For this KB, the source is the boundary condition on causal reach assessment: causal formalism can assess reach only as far as the assumptions are declared and partially checkable.

## Claims

- **Claim (paraphrase):** DoWhy makes causal assumptions explicit in a user-supplied graph, then separates modeling, identification, estimation, and validation; graph-based criteria and do-calculus identify effects relative to that graph, while the validation path cannot fully verify its causal assumptions.
  - **Source extract (verbatim):** four steps: model, identify, estimate, and validate.
  - **Source location:** Introduction, “DoWhy: Expressing and validating assumptions”; short fragment required by the two-column PDF capture.
  - **Source extract (verbatim):** Before starting any causal analysis, DoWhy stipulates that
  - **Source location:** Section 3.1, first half of the user-graph requirement; two-column capture.
  - **Source extract (verbatim):** the user provide a causal graph over the observed variables.
  - **Source location:** Section 3.1, second half of the user-graph requirement; next captured line.
  - **Source extract (verbatim):** DoWhy uses graph-based criteria and do-calculus to find
  - **Source location:** Section 3.1, first half of the identification statement; two-column capture.
  - **Source extract (verbatim):** expressions that can identify the causal effect.
  - **Source location:** Section 3.1, second half of the identification statement; next captured line.
  - **Source extract (verbatim):** It is important to note here that causal assumptions cannot be fully verified. Rather, the intent is to validate some
  - **Source location:** Section 3.2, validation boundary; the right PDF column is contiguous across these two captured lines.
  - **Scope:** DoWhy's four-stage causal-effect workflow and the validation/refutation methods described in the 2021 paper; the user or another process supplies the graph and domain assumptions.
  - **Confidence:** High for the framework architecture and the authors' explicit full-verification limitation.
  - **Limitation:** Do-calculus identifies an effect under a supplied graph; it does not establish that the graph's variables or arrows are causally correct. Refutation tests can expose some failures but are not a global validator analogous to predictive cross-validation.

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
