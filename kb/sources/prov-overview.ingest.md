---
description: "W3C PROV family roadmap — the canonical standard for 'full provenance' that the KB's lineage concept deliberately trims down from"
source_snapshot: "prov-overview.md"
ingested: "2026-07-06"
type: kb/sources/types/ingest-report.md
domains: [provenance, lineage, standards]
---

# Ingest: PROV-Overview — An Overview of the PROV Family of Documents

Source: prov-overview.md
Captured: 2026-07-06
From: https://www.w3.org/TR/prov-overview/

## Classification

Type: design-proposal -- a W3C Working Group Note that is the roadmap to a family of 12 standards specifications defining a specific conceptual model and its serializations (an architecture for representing provenance on the web). Not a research result and not a tool release; it is the entry map to a standards-body model.
Domains: provenance, lineage, standards
Author: Strong. Editors Paul Groth (VU Amsterdam) and Luc Moreau (Southampton), both foundational provenance researchers; the document is a W3C Recommendation-track family with broad institutional review (April 2013).

## Summary

PROV is the W3C's standardized model for representing and interchanging provenance — "information about entities, activities, and people involved in producing a piece of data or thing" — across heterogeneous web systems. It grew out of eight Provenance Incubator Group requirements: identifying and attributing objects, accessing and retrieving provenance, representing provenance-of-provenance, enabling reproducibility, supporting versioning, representing procedures, and modeling derivation. The family spans 12 documents split by audience: PROV-PRIMER for learners; PROV-O (OWL ontology), PROV-XML, PROV-AQ (access/query), PROV-DC, PROV-DICTIONARY for developers; and PROV-DM (conceptual model), PROV-N (notation), PROV-CONSTRAINTS (validation), PROV-SEM (first-order-logic semantics), PROV-LINKS for advanced use. This overview is a navigation map, not a specification — it tells a reader which document to open, not how the model works.

## Connections Found

Connection discovery found no artifact in the KB that references PROV or its terms — it is a fresh, currently orphaned snapshot — but it sits squarely against the KB's lineage/derivation cluster. The strongest fit is [lineage](../notes/definitions/lineage.md), which states outright that "lineage is deliberately narrower than full provenance"; PROV is precisely the canonical, standardized "full provenance" superset that sentence carves down from, and its eight requirements (attribution, reproducibility, versioning, derivation, provenance-of-provenance) enumerate what lineage trims away. It also runs parallel to the already-captured [in-toto ingest](./in-toto-farm-to-table-guarantees.ingest.md): both are external standards over artifact derivation graphs — PROV a descriptive interchange model for *what happened*, in-toto adding cryptographic integrity over a supply-chain derivation graph. More loosely, [distilled artifacts need source tracking](../notes/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md) designs the KB's own forward/reverse derivation records, for which PROV is a formal external reference vocabulary. Connect flagged a synthesis cluster (PROV + in-toto + build-systems-à-la-carte as external provenance/build-lineage models), left for a future writer.

## Extractable Value

1. **Named external anchor for "full provenance."** `lineage.md` contrasts itself with "full provenance" but points a reader at nothing concrete; PROV is the standard that scopes that superset. Adding an `evidence` reverse edge from `lineage.md` to this snapshot gives the deliberate-narrowing move a citable reference. [quick-win]
2. **The eight PROV requirements as a checklist against lineage's scope.** Attribution, access, retrieval, provenance-of-provenance, reproducibility, versioning, procedures, derivation — an explicit enumeration of what a full provenance model covers, useful for testing which concerns the KB's lineage deliberately drops (review/invalidation/regeneration) versus omits by accident. [experiment]
3. **PROV's entity/activity/agent triad as vocabulary.** A compact, widely-adopted framing for derivation graphs that could sharpen how the KB talks about who/what produced a derived artifact, parallel to the `derived-from` / `Distilled into:` scheme in [link-vocabulary.md](../reference/link-vocabulary.md). [just-a-reference]
4. **Third member of an external-standards cluster.** With in-toto and build-systems-à-la-carte already captured, PROV completes a trio of external lineage/derivation models from three domains (web interchange, supply-chain integrity, build freshness) — enough material for a synthesis note tying external provenance models to the KB's staleness theory. [deep-dive]
5. **Provenance-of-provenance as a modeled concern.** PROV explicitly treats provenance of provenance records (bundles, PROV-LINKS); a recurring blind spot when the KB's own lineage records are themselves derived artifacts that can go stale — connects to [a derived copy of recomputable truth must be checked or absent](../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md). [just-a-reference]

## Limitations (our opinion)

Opinion: this is a roadmap document, not a specification — it names the 12 PROV documents and their audiences but contains almost none of the model's actual mechanics (no term definitions, no derivation semantics, no constraint rules). Its extractable value is therefore mostly pointer-value: it tells you PROV exists and how it is organized, not how to use it; grounding any real claim about the model requires opening PROV-DM or PROV-O. It is also one step outside the KB's core methodology scope: PROV models provenance of arbitrary web data for interchange between organizations, a far heavier concern than the KB's review-scoped lineage, so the analogy should stay at the level of "what full provenance includes" and not be over-fitted — the KB deliberately does *not* want most of what PROV standardizes. Finally the document is from 2013; the standards are stable but adoption context has moved on (e.g. supply-chain provenance is now dominated by SLSA/in-toto-style crypto approaches PROV predates).

## Recommended Next Action

Add an `evidence` reverse edge from [lineage](../notes/definitions/lineage.md) to this snapshot — a footer link at the "deliberately narrower than full provenance" claim pointing at `prov-overview.md` as the standard reference for that superset. This is the single highest-value, lowest-cost move; it turns an orphan snapshot into a load-bearing external anchor for the one note whose scope it most directly grounds. (The synthesis note tying PROV + in-toto + build-systems-à-la-carte to the KB's staleness theory is the larger follow-on, but should wait for a deliberate writer.)
