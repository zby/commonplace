---
description: "Flywheel models research as durable work nodes with branches, evidence attachments, and merged outcomes; a provenance design example without evidence of research improvement."
source: https://docs.flywheel.paradigma.inc/concepts/graph-model
captured: "2026-09-17"
capture: curl+trafilatura
capture_scope: partial-source
genre: practitioner-report
snapshot_sha256: 6a0d6117795fa833b9810bca7b87041df4e058cc0d1fdda460274ef72f541faa
ingested: "2026-09-17"
type: ingest-report
domains: [research-provenance, knowledge-graphs, evidence-retention]
---

# Ingest: Flywheel — Graph Model

## Classification

Product documentation by Paradigma describing Flywheel's research representation and recommended modeling practice. It is a practitioner account of intended use, without an empirical evaluation or implementation inspection. The author is the product's provider; that gives a direct design account but no independent confirmation of its effectiveness.

## Summary

Flywheel represents research as a directed graph of durable work nodes containing questions, claims, hypotheses, tasks, results, or decisions. Child branches preserve divergent work and merges record a resolved outcome. The page recommends small nodes, evidence attached as artifacts, and separate children for follow-up work that can succeed or fail independently. When a branch changes a conclusion, the summary should be updated and the outcome connected to the graph. This provides a concrete design for retaining alternatives and their evidence for later inspection; the captured page does not show that the records are complete or that the design improves research outcomes.

## Quotes

No source quotes have been retained yet.

## Connections Found

Flywheel supplies a bounded design example for [History has one chance to become checkable](../notes/history-has-one-chance-to-become-checkable.md): its advice to attach evidence and preserve failed experiments alongside decisions describes how production history could become an inspectable record. It does not test the note's stronger claim about when history becomes unrecoverable. The distinction from Commonplace's [lineage](../notes/definitions/lineage.md) is also useful: Flywheel describes ancestry among research work units, while the KB definition concerns source dependencies and the obligations triggered when sources change. The captured page establishes no such invalidation or regeneration obligations.

## Extractable Value

1. **A concrete unit for preserving research alternatives.** Use a separate child node for work that can succeed or fail independently, retain its evidence, and connect the eventual outcome to its ancestry. This adds a product-specific example to the KB's existing account of carrying production history; it offers a modeling rule, not a new general theory or measured benefit. [just-a-reference]
2. **A boundary on interpreting research graphs.** Branch and merge ancestry can document how work proceeded without specifying how dependent claims are reviewed after evidence changes. This source is useful when distinguishing inspectable research history from the stronger dependency obligations in Commonplace's lineage definition. [just-a-reference]

## Limitations (our opinion)

The retained capture is marked partial-source. It establishes the graph concepts and modeling advice shown here, not the behavior of linked CLI commands, the companion research workflow, or the implementation of branches and merges. No experiments, deployment traces, team context, failure rates, or comparison with simpler records are supplied. The provider's description therefore cannot establish that a graph performs better than linked documents or that users actually preserve enough evidence.

A merged outcome records a resolution but does not establish that a claim was tested or competing evidence was resolved correctly. Small nodes and attached artifacts could help later inspection only if the relevant evidence and decision reasons are retained. The page does not specify completeness checks, immutable history, conflict-resolution criteria, or refresh obligations. Its contribution is the documented representation and practice, not an assurance of epistemic reliability.

## Recommended Next Action

File this ingest as a source-only reference for research ancestry and evidence attachment, without promoting a new note.
