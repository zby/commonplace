---
description: "Hansson argues that belief bases preserve dependency structure needed for selective and repeated belief change"
source: https://link.springer.com/article/10.1007/BF00413568
captured: "2026-09-17"
capture: pdftotext
capture_scope: full-source
doi: "10.1007/BF00413568"
genre: conceptual-essay
snapshot_sha256: be3e0f06c669b1e0106a4fb900dc3a8b834323525fe2e78cb1a4841d8cfa5e2d
ingested: "2026-09-17"
occasion: "The belief-base versus belief-state distinction and its advantages for repeated change; what a base needs to record."
learning_claims: true
type: ingest-report
domains: [belief-revision, knowledge-representation, learning-theory]
---

# Ingest: In Defense of Base Contraction

## Classification

This is a conceptual essay in formal belief revision: it compares two representations through worked propositional examples and consequences for contraction operators rather than reporting an empirical evaluation. Author: Sven Ove Hansson developed formal work on base contraction and argues here within the established AGM literature while directly addressing Gärdenfors's response to an earlier example.

## Summary

Hansson argues that a logically closed belief set loses distinctions that matter for later change: two agents may believe the same consequences while grounding them in different basic commitments, so contracting the same proposition should leave different beliefs behind. A non-closed belief base preserves which propositions have independent standing and lets derivative beliefs disappear automatically when their grounds are removed. Conflicts among basic beliefs still require a selection mechanism, but Hansson argues that this mechanism can be a stable background function rather than state-specific information that must itself be updated after every change. This makes base contraction a cleaner representation for repeated contractions, although the paper does not establish that every realistic case can avoid state-specific selection.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper is a technical basis for [Lineage](../notes/definitions/lineage.md): it gives a formal case where dependency information changes valid revision behavior even though the represented consequences are identical. It also supplies a belief-revision analogue of [History has one chance to become checkable](../notes/history-has-one-chance-to-become-checkable.md) and [Bottom-up structure inference needs capture at the decision surface, not the state](../notes/structure-inference-needs-capture-at-the-decision-surface.md): an endpoint closed under consequence cannot reconstruct whether a proposition was an independent ground or only a derivative consequence.

## Learning Claims (our opinion)

The source's adaptation mechanism is contraction or revision over an explicit belief representation. Its key distinction is between the current consequences and the base that generates them. The base identifies independently held propositions; logical closure supplies their derivative consequences; and a selection mechanism resolves cases where removing a target requires choosing among basic propositions. This only partly maps to the [theory-builder definition](../notes/definitions/theory-builder.md). An explicit base meets condition 1: each basic proposition says something that can be pointed at. The paper specifies change operators, not a system, so consumption, a working criticism process, and retention for later problems (conditions 2–4) are outside its scope rather than failed. Its selection mechanism chooses what to give up, but the paper does not say how evidence criticizes what a basic proposition says. Separately editable commitments are finer [addressability](../notes/definitions/theory-builder.md#addressability), a design commitment above condition 1's minimum, not a condition of membership. Hansson also does not establish that repeated contraction improves capacity for future action; that learning claim stays separate. The paper adds a representation condition to Commonplace's account: repeated revision may require preserving dependency structure that an extensionally equivalent theory state omits. Its examples support the need for that distinction in the cases shown; they do not establish that base structure plus a background selector is sufficient for every repeated-change process.

## Extractable Value

1. **Separate generative commitments from their current consequences.** A base must record which propositions have independent standing; storing only the closure makes distinct grounds indistinguishable and can force the wrong later contraction. [quick-win]
2. **Preserve dependency structure for repeated change.** The source gives a formal mechanism for the KB's broader claim that endpoint-equivalent representations can support different valid updates because only one retains the dependencies that produced the endpoint. [deep-dive]
3. **Keep update policy distinct from represented state when possible.** Hansson's background selector shows how conflict-resolution policy can remain stable across changes, avoiding an additional state component whose own transition would need specification. [deep-dive]
4. **Do not mistake a base for full provenance.** The required record is narrower: independent commitments and enough logical structure to derive consequences. The paper does not require recording evidence, acquisition history, or rationale for each commitment. [just-a-reference]

## Limitations (our opinion)

The argument relies on small propositional examples and formal comparisons, not observations of human or machine revision in practice. Its strongest general claim rests partly on the author's inability to find a case requiring a state-specific selector for base contraction, which is weaker than a proof that no such case exists. The base records logical dependence among propositions, but it does not represent evidential provenance, graded confidence, conflicting sources, or the reasons a basic belief has independent standing. The result therefore supports preserving dependency structure without establishing that a propositional base is sufficient for agent memory or KB revision.

## Recommended Next Action

Write a note titled **Dependency-preserving representations support repeated revision** that synthesizes Hansson's base/set distinction with the existing Lineage and decision-surface claims, while stating that a useful base must retain independent commitments and derivation structure but may still need separate evidence and selection policy.
