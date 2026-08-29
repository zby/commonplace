# Normalized directional lineage relations across link vocabularies

This document normalizes every lineage relation declared by Commonplace's shared link catalogue and live collection contracts as:

```text
(derivative, relation, source)
```

It inventories declarations, not every corpus use. The authoritative surfaces are the shared [link vocabulary](../../reference/link-vocabulary.md) and each writable collection's `COLLECTION.md`; the frozen [`kb/reports/retained/link-vocabulary.md`](../../reports/retained/link-vocabulary.md) is historical corpus evidence, not a live vocabulary. Inventory date: 2026-07-28.

## Endpoint terminology

Two meanings of “source” must not be conflated:

- **Markdown source** — the artifact containing an authored link.
- **Lineage source** — the input artifact whose content shaped the derivative.

The Markdown source can be either endpoint. A target-side `derived-from` link makes the derivative the Markdown source. A source-side `Derived into:` footer makes the lineage source the Markdown source. Both can encode the same semantic tuple.

The normalized tuple always uses:

- `derivative` — the artifact whose content or executable shape depends on another artifact;
- `relation` — exactly one of the four registered lineage regimes;
- `source` — the artifact whose content was derived, generalized, operationalized, or adapted.

The tuple is semantic. Its storage carrier and authored direction are separate choices.

## The four normalized relations

| relation | normalized tuple | derivative-authored rendering | source-authored rendering | response when the source changes |
|---|---|---|---|---|
| `derived-from` | `(D, derived-from, S)` | `D — derived-from → S` | `S — Derived into: → D` | Re-derive and compare; stale until rechecked. The derivative adds no substantive claim beyond the source plus declared premises or consumer goal. |
| `abstracted-from` | `(D, abstracted-from, S)` | `D — abstracted-from → S` | `S — Abstracted into: → D` | Re-examine the generalization. The derivative posits claims beyond the source and earns authority through later testing. |
| `operationalized-from` | `(D, operationalized-from, S)` | `D — operationalized-from → S` | `S — Operationalized into: → D` | Judgmentally recheck fit. The derivative adds ordering, defaults, or stopping conditions but no substantive claims beyond the source. |
| `adapted-from` | `(D, adapted-from, S)` | `D — adapted-from → S` | `S — Adapted into: → D` | Judgmentally recheck fit. The derivative's selection, structure, or wording was materially worked up from the source for a different use. |

`operationalized-from` and `adapted-from` are alternatives for one edge, not relations to stack. A mixed artifact takes its dominant regime. The retired `Distilled into:` carrier is unclassified lineage until migrated; it does not imply any of the four tuples.

## Inventory of every live link vocabulary

This table covers the shared catalogue and every current `COLLECTION.md`, including vocabularies that declare no lineage relation. “Authored surface” describes what the contract currently tells writers to emit; “normalized meaning” removes that carrier's direction.

| vocabulary authority | current lineage declaration or carrier | authored surface | normalized meaning | finding |
|---|---|---|---|---|
| [Shared catalogue](../../reference/link-vocabulary.md#lineage-semantics) | `derived-from` / `Derived into:` | Catalogue defines both target-side label and source-side footer, while prescribing source-side recording by default. | `(D, derived-from, S)` | **Normalized.** The two renderings are inverses at the Markdown surface but one semantic relation. |
| Shared catalogue | `abstracted-from` / `Abstracted into:` | Same dual rendering and source-side default. | `(D, abstracted-from, S)` | **Normalized.** |
| Shared catalogue | `operationalized-from` / `Operationalized into:` | Same dual rendering and source-side default. | `(D, operationalized-from, S)` | **Normalized.** |
| Shared catalogue | `adapted-from` / `Adapted into:` | Same dual rendering and source-side default. | `(D, adapted-from, S)` | **Normalized, but catalogue-only.** No live collection contract currently names an executable source/destination pairing for `adapted-from`. |
| [Agent-memory systems](../../agent-memory-systems/COLLECTION.md#outbound-linking-conventions) | `derived-from` to `kb/sources/` | Review or lightweight analysis links to the source snapshot. | `(review, derived-from, snapshot)` | **Direction aligned; relation wording unsettled.** The same contract says lightweight coverage links to the snapshot it was “abstracted from,” so the pairing still needs a `derived-from` versus `abstracted-from` truth-condition check. |
| Agent-memory systems | no other lineage label | Structural, evidence, rationale, definition, comparison, and weak-navigation labels only. | — | **No additional lineage relation.** Code-grounded repo identity and reviewed revision are provenance dependencies, not registered link relations. |
| [Agentic systems](../../agentic-systems/COLLECTION.md#outbound-linking-conventions) | `derived-from` to `kb/sources/` | System analysis links to the snapshot it is grounded in. | `(analysis, derived-from, snapshot)` | **Direction aligned.** Derivative is the Markdown source. |
| Agentic systems | no other lineage label | Evidence, rationale, structure, comparison, procedure, and weak-navigation labels only. | — | **No additional lineage relation.** |
| [Articles](../../articles/COLLECTION.md) | `source_notes` metadata; no labelled footer links | Article stores paths to the notes it distils. | `(article, relation-to-classify, note)` | **Carrier declared, relation under-specified.** `source_notes` proves dependency and target-side placement but does not select `derived-from`, `abstracted-from`, `operationalized-from`, or `adapted-from`. The likely default is `adapted-from`, but that must be made contractual rather than inferred. |
| [Instructions](../../instructions/COLLECTION.md#outbound-links) | no lineage label in its outbound table | Procedures author control-flow, `operates-on`, and `rationale` links. | — | **No derivative-authored lineage authorization.** Instructions can still be derivatives reached from a methodology note's source-side `Operationalized into:` footer. |
| [Notes](../../notes/COLLECTION.md#outbound-links) | `derived-from` to reference, agent-memory, agentic-systems, and sources | Claim note links to the descriptive/source input. | `(note, derived-from, external-or-descriptive-source)` | **Direction aligned.** Derivative is the Markdown source. |
| Notes | `abstracted-from` to reference, agent-memory, agentic-systems, and sources | Generalizing note links to the instance/evidence source. | `(note, abstracted-from, external-or-descriptive-source)` | **Direction aligned.** Derivative is the Markdown source. This is the valid carrier for an immutable snapshot. |
| Notes | table lists `operationalized-from` to instructions, while prose says it is recorded as `Operationalized into:` on the methodology note | Methodology note is the Markdown source and procedure is the linked target. | `(procedure, operationalized-from, methodology-note)` | **Surface-direction conflict.** The prose's `Operationalized into:` rendering is correct; the table's `operationalized-from` identifier would grammatically assert the inverse tuple if emitted as an ordinary link. |
| [Reference](../../reference/COLLECTION.md#outbound-links) | `derived-from` to sources, agent-memory, and agentic-systems | Reference/design artifact links to the external input. | `(reference-artifact, derived-from, external-source-or-system)` | **Direction aligned.** Derivative is the Markdown source. |
| Reference | `abstracted-from` to sources, agent-memory, and agentic-systems | Reference/design artifact links to the external case it generalizes. | `(reference-artifact, abstracted-from, external-source-or-system)` | **Direction aligned.** Derivative is the Markdown source. |
| [Sources](../../sources/COLLECTION.md#outbound-links) — immutable snapshots | snapshots author no links; notes are instructed to point back with `abstracted-from` when appropriate | Derivative note is the Markdown source; immutable snapshot is target. | `(note, abstracted-from, snapshot)` | **Direction aligned and immutability-safe.** |
| Sources — ingest reports and source reviews | `abstracted-from` to notes, glossed as “this claim was abstracted from this source” | Source analysis is the Markdown source; derived claim is target. | `(note, abstracted-from, source-analysis)` | **Surface-direction conflict.** The intended meaning is source-side `Abstracted into:`; the registered `abstracted-from` identifier asserts the inverse when read as `Markdown-source <label> target`. |
| Sources | no `derived-from`, `operationalized-from`, or `adapted-from` authorization | Evidence, rationale, comparison, definition, and weak-navigation labels only. | — | **No additional lineage relation.** |
| [Workshops](../COLLECTION.md#outbound-links) | non-authoritative suggestion `abstracted-from` to reference, systems, and sources | Workshop artifact links to the material it generalizes. | `(workshop-artifact, abstracted-from, external-or-descriptive-source)` | **Direction aligned, non-authoritative.** Promotion must re-evaluate the destination collection's durable contract. |
| Workshops | local `draws-on`, `depends-on`, and `produces` suggestions | Working-state links may describe provenance loosely. | — | **Not registered lineage.** They do not select one of the four maintenance regimes. |
| [Dialectical sample](../dialectical-sample/COLLECTION.md) | mandatory source-span citations, no outbound-link vocabulary | Proposition links to attributed source spans without a relationship identifier. | — | **Specialized citation grammar, not registered lineage.** |

## Authorization expanded by relation

The same inventory viewed relation-first exposes which derivative/source pairings are executable today.

| normalized relation | derivative classes currently authorized | source classes currently authorized | valid carrier(s) under current contracts | unresolved carrier or authorization |
|---|---|---|---|---|
| `(D, derived-from, S)` | notes; reference artifacts; agent-memory reviews; agentic-system analyses | sources/snapshots; agent-memory systems; agentic systems; reference artifacts where the notes contract permits them | Derivative-authored `derived-from`; shared source-authored `Derived into:` in principle | Collection contracts authorize target-side labels but do not clearly authorize `Derived into:` as a separate carrier per source/destination pairing. |
| `(D, abstracted-from, S)` | notes; reference artifacts; workshop artifacts (non-authoritative) | sources/snapshots; source analyses; agent-memory systems; agentic systems; reference artifacts | Derivative-authored `abstracted-from`; source-authored `Abstracted into:` in principle | Sources currently spell the source-authored direction `abstracted-from`; this must become `Abstracted into:` or move to the derivative. |
| `(D, operationalized-from, S)` | instructions/procedures | methodology notes | Source-authored `Operationalized into:` on the methodology note | Notes' label table names `operationalized-from` in the source-authored direction. No instruction-side target-authored authorization exists. |
| `(D, adapted-from, S)` | none by an explicit live collection pairing; articles are a likely worked case | none by an explicit live collection pairing; article `source_notes` point to notes | Shared catalogue defines both `adapted-from` and `Adapted into:` | The write skill requires source-collection authorization, but no collection currently supplies it. Article lineage records the sources without classifying the relation. |

## Carrier-independent assertions

The normalized model permits two equivalent assertions without making the identifiers themselves ambiguous:

```text
Derivative-authored:
  derivative --relation-from--> source

Source-authored:
  source --Relation into:--> derivative

Normalized:
  (derivative, relation-from, source)
```

Therefore:

- `derived-from`, `abstracted-from`, `operationalized-from`, and `adapted-from` are valid only when the Markdown source is the **derivative**;
- `Derived into:`, `Abstracted into:`, `Operationalized into:`, and `Adapted into:` are valid only when the Markdown source is the **lineage source**;
- moving the carrier does not change the semantic relation or its invalidation response;
- a collection must authorize both the semantic relation and the permitted carrier for the source/destination pairing;
- an immutable artifact cannot carry a source-authored footer, so its derivatives must use a target-side carrier or a declared mutable companion/edge record.

## Contract changes implied by normalization

This document does not perform the contract migration, but normalization makes four repairs unavoidable:

1. **Notes → instructions:** replace the source-authored `operationalized-from` table entry with an explicit `Operationalized into:` carrier, or authorize instruction-authored `operationalized-from` links and move the edge to the procedure.
2. **Sources → notes:** replace source-authored `abstracted-from` with `Abstracted into:`, or remove it from the source contract and rely on note-authored `abstracted-from` links to snapshots/ingests.
3. **Articles:** classify what `source_notes` asserts. If articles reshape notes rather than preserve all their substantive claims, declare `(article, adapted-from, note)` and keep `source_notes` as its target-side metadata carrier.
4. **Adaptation generally:** name at least one collection-authorized `adapted-from` pairing before the generic write skill can treat that relation as executable rather than catalogue-only.

The generic write procedure must then resolve an effective lineage profile that chooses relation, carrier, and invalidation separately. It cannot infer semantic direction from whichever artifact happens to contain the Markdown link.

## Non-lineage boundary

The following live shared labels are deliberately **not** normalized as `(derivative, relation, source)` because they do not assert derivation: `extends`, `grounds`, `enables`, `exemplifies`, `mechanism`, `contradicts`, `contrasts`, `rationale`, `evidenced-by`, `is-evidence-for`, `part-of`, `contains`, `implements`, `implemented-by`, `supersedes`, `superseded-by`, `compares-with`, `procedure`, `composition`, `precondition`, `invokes`, `applies-when`, `operates-on`, `defined-in`, and `see-also`. Workshop-local suggestions `draws-on`, `tests`, `depends-on`, and `produces` likewise remain untyped working-state relations rather than registered lineage.

Their source→target grammatical direction belongs to the sibling [linking-contract-consistency](../linking-contract-consistency/README.md) workshop. Forcing them into derivative/source roles would erase the distinction between provenance, inference, structure, procedure, evidence, and navigation that the lineage vocabulary exists to preserve.
