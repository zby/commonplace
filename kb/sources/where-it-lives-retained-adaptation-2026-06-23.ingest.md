---
description: "Updated self-authored ASISAS position paper adding 141-system corpus evidence to the four-field retained-artifact vocabulary."
source_snapshot: "where-it-lives-retained-adaptation-2026-06-23.md"
ingested: "2026-06-23"
type: kb/sources/types/ingest-report.md
domains: [artifact-analysis, agent-memory, software-architecture]
---

# Ingest: Where It Lives Is Not What It Is (June 2026 version)

Source: where-it-lives-retained-adaptation-2026-06-23.md
Captured: 2026-06-23
From: file:///home/zby/txt/paper/submissions/asisas-2026/paper.md

## Classification

Type: scientific-paper -- an ASISAS 2026 position paper with citations, a worked architectural record, and a new corpus-analysis section. It is still mostly a conceptual architecture argument, but the June 23 version adds descriptive evidence from 141 code-grounded agent-memory reviews.
Domains: artifact-analysis, agent-memory, software-architecture
Author: This is the KB owner's own paper. For Commonplace, its authority is lineage and external framing, not independent corroboration. The corpus section is grounded in this KB's review matrix and therefore inherits the matrix's strengths and biases.

## Summary

The paper argues that retained behavior-shaping artifacts in agentic systems should be classified by storage substrate, representational form, lineage, and behavioral authority, at the level of operative parts and consumption paths rather than stored objects. The June 23 revision keeps the same vocabulary but adds Section 8, applying the record to a 141-system agent-memory/context-engineering corpus reviewed from source code. Its strongest new point is empirical-descriptive: even among the 98 systems that store retained state in files or repositories, other fields still separate behavior sharply -- 53 include enforcement, 37 include distributed-parametric parts, 39 are pull-only, and 70 have trace-extracted lineage. The paper therefore upgrades the old storage-first critique from a pure construction argument to a corpus-backed claim that substrate alone cannot predict form, authority, activation, or lineage.

## Connections Found

Connection discovery found that the source is still mostly **paper-from-KB**, not **KB-from-paper**. The vocabulary is distilled from [axes of artifact analysis](../notes/axes-of-artifact-analysis.md), the definition cluster, and [the efficiency/security/sovereignty risk triad](../notes/the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md). The new Section 8 is distilled from the living agent-memory surfaces: [the comparative review](../agent-memory-systems/agentic-memory-systems-comparative-review.md), [systems table](../agent-memory-systems/systems-table.md), `systems.csv`, and the [review type spec](../agent-memory-systems/types/agent-memory-system-review.md).

The old ingest's main follow-up has already been promoted: the sovereignty refinement now exists as [the risk-triad note](../notes/the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md). The live connection is no longer "write the sovereignty note"; it is "make the living matrix synthesis carry the within-substrate evidence that the paper now exposes." Reverse note-to-paper links should still wait until the paper is accepted or otherwise externally citable; a self-authored draft should not be used as independent `evidence` for notes it came from.

## Extractable Value

1. **Within-substrate evidence for the non-storage taxonomy** -- The new corpus section shows that even when storage is held mostly fixed to files/repositories, enforcement, distributed-parametric parts, activation direction, and trace lineage still vary. This is the cleanest new value relative to the old ingest because it gives the storage-first critique a concrete matrix-backed example. [quick-win]
2. **System-level counts expose the operative-part boundary** -- The paper notes that prose and symbolic parts appear in all 141 systems, so representational form discriminates below the system, at the artifact or consumption-path level. This directly supports the review contract's requirement to classify central retained artifacts rather than whole products. [quick-win]
3. **Frozen publication corpus versus living survey distinction** -- The paper relies on a frozen ASISAS corpus, while [agent-memory-systems/README.md](../agent-memory-systems/README.md) correctly says the living survey keeps growing and does not preserve that historical sample-origin column. The ingest should preserve that distinction: use the paper for the frozen argument, and the matrix for current counts. [just-a-reference]
4. **Old sovereignty follow-up is closed** -- The old ingest's recommended action was to mine the sovereignty axis back into notes. That has happened in [the risk-triad note](../notes/the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md), so any current action should not repeat it. [quick-win]
5. **Validation agenda is sharper but still future work** -- The revision names the missing validation more concretely: per-artifact rather than system-level statistics, a representative sampling frame, reviewer-consistency checks, and design-review or incident-analysis trials. This is useful if the KB later turns the vocabulary into an evaluated method. [deep-dive]
6. **External-facing citation package remains useful but circular** -- The paper packages the vocabulary for software-architecture readers and supplies citations for architecture, prompt-injection, digital sovereignty, and agent-memory surveys. It is useful as presentation and source-lineage material, but not as independent evidence for the KB's own notes. [just-a-reference]

## Limitations (our opinion)

This is a self-authored position paper, so it should not be treated as outside corroboration of Commonplace's artifact-analysis vocabulary. The honest relationship is lineage and publication framing: the paper distills notes and review data into an external argument, then some refinements flow back into notes.

The new corpus section is useful but not a controlled validation. The corpus is opportunistically assembled and seeded by a file/wiki-heavy Karpathy thread, so the 98-of-141 file/repo count describes this collection rather than the whole field. The counts are system-level presence fields, while the vocabulary's real unit is the operative part. The classifications were produced under one saved review contract rather than independent multi-annotator coding. Those limits do not undermine the storage-first critique, but they do constrain how strongly to state any empirical claim.

## Recommended Next Action

Update [agentic-memory-systems-comparative-review.md](../agent-memory-systems/agentic-memory-systems-comparative-review.md), in the "Storage predicts little by itself" section, with the within-files/repo breakdown from the paper: among 98 file/repo systems, 53 enforce, 37 include distributed-parametric parts, 39 are pull-only, and 70 have trace-extracted lineage. That promotes the new evidence to the living matrix synthesis without treating the self-authored paper as independent evidence.
