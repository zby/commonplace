---
description: "Recovery failure shows content is missing from the tested source; causal provenance and live authority require independent evidence, and only pairs with unique content on both sides are bidirectionally irrecoverable"
type: kb/types/note.md
traits: [title-as-claim]
tags: [artifact-analysis, kb-maintenance]
---

# Attempted recovery identifies informational gaps, not provenance or authority

Which artifact is the source of truth: the running system or its documentation? The question is usually answered once for the whole pair, often in the system's favour. That framing combines three relations, each of which can vary independently for each unit of content:

- **Recoverability:** can a declared source set faithfully reproduce the content?
- **Provenance:** was one artifact actually worked out from the other?
- **Authority:** what must the live change loop consult or obey now?

Attempted recovery tests only the first relation. It can expose content that is absent from the tested source before a mismatch makes the absence visible. It cannot by itself establish the historical or operational relations. A common source can produce the same content in two artifacts, while a document adopted after implementation can govern future changes without altering what either artifact can reproduce.

[Commitment, not derivation, creates new ground truth](./commitment-not-derivation-creates-new-ground-truth.md) supplies the adjacent distinction. Derivation leaves content recoverable from a source plus its declared consumer goal; commitment fixes resolutions the source did not determine. Once the production relation is known, that distinction settles maintenance and disposal. This note adds a recovery assay for content availability, bounds what the assay establishes, and applies those bounds to a system and its documentation.

## Recovery is an availability assay

For each decision-relevant unit, declare the sources allowed for reconstruction, then try to reproduce the original content. Faithful recovery must reproduce the content that supported the original decisions: its actual warrant, constraints, rejected branches, coverage boundary, and epistemic status where those matter. Inventing a plausible rationale that would support the same visible behavior is substitution, not recovery.

Rejected alternatives are a useful probe because an unchosen branch often leaves no direct trace in the resulting behavior. They are not proof of provenance. Interfaces, tests, or constraints may preserve an indirect trace, and a rejected alternative can also be documented after implementation. Failure to recover one therefore establishes an information gap in the tested sources, not that the document caused the system.

Run the assay in both directions. System-to-document recovery can identify documentary content that merely restates the system. Document-to-system recovery can identify system behavior or configuration fully determined by the document. Opposite directions may succeed for different regions of the same pair. Each success establishes recoverability only relative to the declared source set, content unit, and consumer goal.

The unit cannot always be a single sentence in isolation. A behavior may depend on several specification clauses, a shared definition, and an implementation default. The assay must operate over the smallest decision-relevant closure that preserves those dependencies; otherwise, changing the chosen grain can change the result.

## Provenance needs independent evidence

Recovery is an extensional comparison between artifact contents as they stand now. Provenance is a historical relation. Two histories can end with identical code and documentation even though the document guided implementation in one and was written afterward in the other. Recovery produces the same result for both histories.

Calling documentation generative therefore requires lineage evidence that production actually consumed it: a recorded design-to-implementation link, a build or generation path, an execution trace, or another retained account of the crossing. Successful recovery supports derivation only after the relevant production inputs and consumer goal are fixed independently. Failure locates content that the tested source does not determine; it does not choose among prior generation, common cause, post-hoc explanation, error, or unrelated context.

This condition reconciles the document/system case with the commitment boundary. An underspecified design can leave implementation choices open, and the retained system then commits resolutions the design does not determine. A complete formal specification under a fixed generator is a different case: the implementation may be mechanically derived for the covered behavior. The relation follows the actual production history, not the artifacts' labels.

## What a system often cannot reproduce

Systems often omit the warrant for choices, branches considered and refused, claimed coverage boundaries, and the conjectural status of decisions made on a guess. Running behavior does not distinguish a deliberate commitment from an accident that nothing has exercised, which is one reason [exact implementation does not validate a requirement against its objective](./exact-implementation-does-not-validate-a-requirement.md).

Such omissions are common, not necessary. A literate or introspective system can retain decision records, alternatives, and confidence annotations as reproducible runtime data. Conversely, documentation can contain post-hoc commentary or error that the system cannot reproduce but that was never part of its production.

Nonrecoverability from the paired system also does not prove global uniqueness. The same rationale may survive in an issue tracker, decision record, or other authoritative source. Deleting a documentary copy is irrecoverable only when no surviving accessible source can faithfully reproduce the content. Attempted recovery against the system identifies candidates for that all-source check; it does not complete the check itself.

## A pair can be irrecoverable in both directions

Suppose documentation retains the actual warrant and rejected alternatives from which a system was worked out, and no other accessible source preserves them. Suppose the implementation also fixes resolutions that the documentation left open and records them nowhere else. The documentation cannot be regenerated from the system, and the system cannot be regenerated from the documentation without a fresh arbitration. Each side holds unique content.

For such a pair, asking which whole artifact is the source of truth forces a wrong answer for part of the content. The documentation is the historical record for its retained rationale; the system is the committed record for its added resolutions. Source-of-truth assignments belong to content units and named relations, not files.

Bidirectional irrecoverability is conditional, not universal. A code-first prototype may have no generative documentation. A complete formal specification may determine all covered implementation behavior. An introspective system may reproduce its design record, and two representations may be mutually recoverable. The assay reports which regions are occupied rather than promising that both are.

## Current authority is a third relation

Historical provenance does not determine what governs the next change. A design that generated the current system can become archival when the change loop stops using it. A post-hoc document can become authoritative when maintainers adopt it as a compatibility contract. Neither transition needs to change the pair's recovery relation.

Authority requires a causal path into the change loop. Direct reading is one path, but not the only one: requirements can generate acceptance tests, policy can be enforced by tooling, and routing can load instructions for the agent that makes the change. Content with no such path is not currently load-bearing, even if it remains an irreplaceable historical record. That is a routing or enforcement fact, not evidence that the content was semantically redundant.

## Decision boundaries

Recoverability makes deletion bounded; it does not make deletion worthwhile. A recoverable copy can still replace expensive work. For a model reader, [LLM recompute cost shifts the store-vs-recompute balance](./llm-recompute-cost-inverts-the-store-vs-recompute-default.md), but persistence pays only when the checked copy substitutes for model-side or external derivation after creation, maintenance, retrieval, and failure costs are counted.

Recoverability is also separate from correctness. A unique historical rationale can be wrong, and a derived cache can be accurate. The assay says where the tested information is available, not whether it deserves belief or binding force.

## Open Questions

- What general rule identifies the smallest decision-relevant closure when a result depends on distributed clauses, definitions, and defaults?
- What is the cheapest provenance signal that distinguishes faithful recovery from a plausible post-hoc reconstruction before a mismatch?
- Which authority paths can be checked mechanically, and which require observing whether a human or agent actually consults and follows the content?

---

Relevant Notes:

- [Commitment, not derivation, creates new ground truth](./commitment-not-derivation-creates-new-ground-truth.md) — extends: supplies the production and disposal split that recovery can apply only after provenance and allowed inputs are fixed
- [Exact implementation does not validate a requirement against its objective](./exact-implementation-does-not-validate-a-requirement.md) — grounds: behavior alone cannot report whether a requirement serves its objective, one common informational gap between a system and its rationale
- [Progressive constraining commits only after patterns stabilize](./progressive-constraining-commits-only-after-patterns-stabilize.md) — exemplifies: an underspecified crossing where implementation adds resolutions rather than mechanically reproducing its input
- [LLM recompute cost shifts the store-vs-recompute balance](./llm-recompute-cost-inverts-the-store-vs-recompute-default.md) — grounds: why a recoverable copy can still earn its maintenance cost when it substitutes for expensive model-side work
- [Source changes should surface downstream review targets, while reverse lineage can remain searchable](./artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md) — enables: retained lineage supplies provenance evidence that recovery alone cannot infer
- [History has one chance to become checkable](./history-has-one-chance-to-become-checkable.md) — grounds: why historical content absent from every surviving source cannot later be recovered faithfully
- [Specification strategy should follow where understanding lives](./specification-strategy-should-follow-where-understanding-lives.md) — extends: maps document-to-system and system-to-document production onto the lifecycle phase where understanding appears
