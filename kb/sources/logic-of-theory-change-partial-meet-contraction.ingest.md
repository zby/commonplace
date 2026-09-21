---
description: "AGM characterizes rational contraction and revision by postulates and partial meet constructions, without supplying discovery or empirical warrant"
source: https://fitelson.org/piksi/piksi_22/agm.pdf
captured: "2026-09-17"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: f7cc9de543bfd3b319be88a2267a7ac4b0d7a924ccea5cef58c25865c6112a94
ingested: "2026-09-17"
occasion: "The postulates as a citation for what contraction and revision are; explicitly what they do not supply (discovery, empirical reliability)."
learning_claims: true
type: kb/sources/types/ingest-report.md
domains: [belief-revision, theory-change, formal-logic]
---

# Ingest: On the Logic of Theory Change

## Classification

This is a formal scientific paper: it defines contraction and revision functions, proves their properties, and establishes representation theorems rather than reporting an empirical study. Author: Carlos E. Alchourrón, Peter Gärdenfors, and David Makinson are the originators of the AGM framework, and the paper appeared in *The Journal of Symbolic Logic*.

## Summary

The paper asks how a logically closed theory should change when a proposition is removed or when an inconsistent proposition is added. It defines partial meet contraction as the intersection of a selected nonempty family of maximal subsets that do not imply the proposition being removed, then defines revision from contraction through the Levi identity. Its central result is a representation theorem: for theories, the basic Gärdenfors contraction postulates characterize partial meet contraction functions, with corresponding revision postulates; additional restrictions on selection yield supplementary postulates. This makes the paper a precise account of admissible change to an existing theory under a fixed consequence operation, not an account of how to discover theories or establish that revised beliefs are empirically reliable.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper is a technical basis for separating formal theory change from epistemic warrant. It supports [A claim's warrant does not determine its fit in a working theory](../notes/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory.md): the postulates constrain how membership in a theory changes, while leaving the independent warrant of retained or introduced propositions unsettled. It also compares with [Machinery persists by warrant, not position, in a reflective loop](../notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md): AGM supplies formal contraction and revision machinery, whereas that note requires governance by current warrant and empirical consequences beyond formal coherence.

## Learning Claims (our opinion)

On the paper's terms, adaptation is an operation over a theory already closed under a fixed consequence relation. Contraction removes a proposition while preserving selected maximal portions of the prior theory; revision first contracts enough to accommodate the new proposition and then adds it. Relative to [Conjectural learning](../notes/definitions/conjectural-learning.md), this supplies a rigorous family of change operators and preservation constraints, but only a partial mapping. AGM's selection function expresses which remainder sets are preferred without explaining how evidence diagnoses a fault, generates candidate repairs, or selects among them. Its representation theorems establish equivalence between postulates and formal constructions, not that either construction learns reliable theories from empirical cases.

## Extractable Value

1. **Use the postulates as a precise citation for contraction and revision.** Contraction removes a proposition from an existing theory while preserving closure and specified rationality properties; revision incorporates a proposition consistently through contraction plus expansion. [just-a-reference]
2. **Keep formal admissibility separate from warrant.** The representation theorem says which operations satisfy the postulates, but it does not show that retained beliefs are true, well supported, or useful. This sharpens the distinction in [A claim's warrant does not determine its fit in a working theory](../notes/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory.md). [quick-win]
3. **Treat the selection function as an unresolved governance input.** Partial meet contraction depends on selecting the most important maximal subsets, but the paper's construction does not supply an empirical or discovery procedure for making that choice. [deep-dive]
4. **Distinguish theory revision from theory discovery.** AGM begins with a theory, a consequence operation, and a proposition to remove or add; it does not construct new explanatory content or identify which proposition an observation should overturn. [quick-win]
5. **Use recovery and preservation as comparison points, not universal requirements.** These postulates make specific commitments about retaining prior content and treating logically equivalent inputs alike; applying them to natural-language or mixed-form theories requires an explicit interpretation of consequence and equivalence. [deep-dive]

## Limitations (our opinion)

The paper is formal rather than empirical. Its conclusions depend on an abstract consequence operation with stated logical properties and on a selection function whose substantive basis is left outside the representation theorem. It does not test whether agents can identify faulty commitments, choose useful remainder sets, interpret natural-language consequences consistently, or improve prediction and action after revision. The framework therefore cannot by itself support claims about discovery, empirical reliability, or successful conjectural learning. Its closed-theory setting also does not transfer directly to Commonplace's mixed-form, partly interpreted theories without specifying how consequences and editable parts are determined.

## Recommended Next Action

Add this ingest as the formal citation in [A claim's warrant does not determine its fit in a working theory](../notes/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory.md), with one sentence stating that AGM characterizes contraction and revision but does not supply discovery or empirical warrant.
