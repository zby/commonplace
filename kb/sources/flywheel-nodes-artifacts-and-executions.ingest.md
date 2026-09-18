---
description: "Flywheel separates research state, evidence outputs, and execution history, providing a design example for multiple memory consumers without establishing context-loading behavior."
source: https://docs.flywheel.paradigma.inc/concepts/nodes-artifacts-executions
captured: "2026-09-17"
capture: curl+trafilatura
capture_scope: partial-source
genre: practitioner-report
snapshot_sha256: f0b0e2e60fe973d7ad6523a2ef2d0f56a9347a5726747fd92e285ac36350a788
ingested: "2026-09-17"
type: kb/sources/types/ingest-report.md
domains: [agent-memory, research-workflows, evidence-management]
---

# Ingest: Flywheel — Nodes, Artifacts, And Executions

## Classification

Practitioner documentation describing a research system's durable records and their intended use, rather than reporting an evaluation. Author: Paradigma, the system's provider. This supplies first-party design intent but no independent account of operational outcomes.

## Summary

[Flywheel's records documentation](https://docs.flywheel.paradigma.inc/concepts/nodes-artifacts-executions) separates three kinds of durable record: nodes hold tasks, hypotheses, current conclusions, and neighboring work; artifacts hold concrete outputs such as reports, tables, checkpoints, and patches; executions hold run-oriented work and compute history. The stated purpose is independent inspection of work structure, produced evidence, and run history. A typical branch creates a node, launches work, attaches outputs, and saves a summary explaining them; later branches can cite the same evidence. Hosted CLI, local repository, and MCP operations have different attachment and commit sequences. For Commonplace, the page supplies a concrete record-separation design, without demonstrating better research outcomes or specifying which records agents load by default.

## Quotes

No source quotes have been retained yet.

## Connections Found

The source is a documented design example for [Serve Multiple Consumers, Not One Retrieval Interface](../notes/agent-memory-requirements/serve-multiple-consumers.md): people, agents, hooks, and exports can inspect concrete outputs without extracting them from summary prose, while work state and compute history remain separately inspectable. This bears on the note's interface-collapse failure mode, but does not establish that every consumer receives an adequate surface.

It also provides a bounded comparison with [Preserve Evidence Without Making History The Next Context](../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md). Separating compact summaries from evidence artifacts and execution records makes selective reading possible. The page leaves context assembly unspecified, so it cannot establish the note's stronger requirement that retained history stay outside ordinary agent context.

## Extractable Value

1. **A concrete design example for distinct memory consumers.** Research state, output evidence, and run history can remain inspectable as separate records linked to the same work. This adds a source-specific example to the existing multiple-consumer requirement; it does not supply new causal evidence that the design improves performance. [quick-win]
2. **Interface-specific persistence boundaries.** Hosted operations commit directly, local repository operations stage and require commit and publication, and MCP artifact attachment uses prepare, upload, and finalize operations. This is useful reference material when evaluating Flywheel integration: a generic instruction to attach and commit would omit consequential differences between interfaces. [just-a-reference]

## Limitations (our opinion)

The retained observation is marked `partial-source`. It does not include the referenced CLI and MCP contracts, and its Nodes section refers to hosted commands without retaining their list. It therefore cannot establish complete mutation sequences, transaction guarantees, failure recovery, or implementation fidelity.

This is one provider's design account, with no usage sample, failed attempts, scaling data, or comparative evaluation. Independent inspection could follow from ordinary separation of concerns; the page does not show that its exact three-record division is necessary or superior to alternatives. Artifact attachment also does not by itself establish the validity of the attached evidence. The documented ability to reuse evidence across branches leaves versioning, deletion, and provenance guarantees unspecified.

The page explains storage roles rather than an agent's read policy. As the evidence-preservation note distinguishes, retaining a run record and controlling whether it enters the next context are separate decisions. No claim about effective context budgets or reliable resumption follows from this documentation alone.

## Recommended Next Action

Add Flywheel's separation of work state, evidence outputs, and execution history as a documented design example in [Serve Multiple Consumers, Not One Retrieval Interface](../notes/agent-memory-requirements/serve-multiple-consumers.md), explicitly limiting its evidential role to design intent rather than demonstrated consumer effectiveness.
