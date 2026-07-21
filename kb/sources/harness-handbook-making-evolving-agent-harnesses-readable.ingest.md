---
description: "Source-validated behavior maps improve harness edit-site localization, while executed modification and self-evolution remain unevaluated."
source_snapshot: "harness-handbook-making-evolving-agent-harnesses-readable.md"
ingested: "2026-07-21"
type: kb/sources/types/ingest-report.md
domains: [harness-evolution, behavior-localization, progressive-disclosure, reflective-systems]
---

# Ingest: Harness Handbook

Source: [harness-handbook-making-evolving-agent-harnesses-readable.md](./harness-handbook-making-evolving-agent-harnesses-readable.md)
Captured: 2026-07-21
From: https://arxiv.org/abs/2607.13285

## Classification

Genre: scientific-paper -- an arXiv preprint with a specified construction method, controlled comparison, quantitative evaluation, appendices, and reproducible prompt templates, but no stated peer-review status.
Domains: harness-evolution, behavior-localization, progressive-disclosure, reflective-systems
Author: Ten authors affiliated primarily with Tencent HY LLM Frontier and several universities; the team designed and evaluated the proposed representation, so the paper is primary evidence with ordinary inventor self-evaluation risk.

## Summary

The paper identifies **behavior localization**—finding every code location that implements a requested behavior—as a prerequisite bottleneck in agent-harness evolution. It introduces Harness Handbook, a behavior-centric representation compiled from a harness repository through deterministic static analysis plus LLM-assisted organization. The representation has an L1 system overview, L2 execution-stage views, L3 source-backed function/file cards, and a cross-stage state-register view. Behavior-Guided Progressive Disclosure (BGPD) navigates from behavior descriptions through stages and shared state to candidate implementation sites, then verifies those sites against current source before planning. Any executed diff is designed to trigger scoped resynchronization, using fingerprints, hashes, reparsing, and conservative freezing when a derived entry cannot be revalidated. In read-only planning experiments on 30 requests each for Codex and Terminus-2, handbook access raises overall judged win rate from 28.3% to 38.3% and from 26.7% to 45.6%, respectively, while reducing planner-token use by 12.7% and 8.6%; all 24 reported recall, precision, and F1 comparisons against two model-generated reference-plan sets improve.

## Connections Found

The paper is a concrete technical basis for the KB's claim that [a derived copy of recomputable truth must be checked or absent](../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md): its generated handbook remains subordinate to source through locator validation, fingerprints and hashes, diff-driven invalidation, scoped regeneration, and freezing of unverifiable entries. Its L1-L3 navigation supplies evaluated evidence for [progressive-disclosure pointer design](../notes/pointer-design-tradeoffs-in-progressive-disclosure.md), and its synchronized caches instantiate the requirement to [keep lineage and compiled views from drifting](../notes/agent-memory-requirements/keep-compiled-views-aligned.md).

Within the KB's reflective self-improvement theory, the paper adds a useful example of one prerequisite part of the full process. The Handbook [puts the system's own organization inside its action environment](../notes/reflection-makes-own-organization-part-of-the-action-environment.md): a coding agent consumes a behavior-oriented representation of the harness's code, state relations, and execution stages to choose intervention sites. It also gives a concrete [graded reflective-coverage](../notes/reflective-coverage-is-graded-across-representational-forms.md) profile across prose and symbolic forms: generated behavioral descriptions are grounded by static facts and live-source locators, and source remains authoritative. The controlled experiment evaluates the self-representation-to-localization-and-plan segment of that pathway. It does not evaluate the later execution, outcome evaluation, operative retention, or repeated improvement segments, but evidence for this prerequisite segment is still evidence about the decomposed process rather than evidence for the whole loop.

Behavior localization also makes the cost of [retrieval failure as reflection failure](../notes/retrieval-failure-is-reflection-failure.md) unusually concrete: a self-representation that misses one distributed implementation site cannot safely mediate modification of the represented behavior. The closest existing harness-evolution comparison is [Agentic Harness Engineering](../agent-memory-systems/reviews/agentic-harness-engineering.md), whose trace-to-edit loop needs exactly this kind of complete edit-surface localization.

## Extractable Value

1. **Name behavior localization as a separate prerequisite operation** -- planning how to change a harness presupposes finding the complete implementation surface of the behavior; repository understanding and code generation do not subsume this step. [quick-win]
2. **Represent behavior separately from repository topology** -- the L1-L3 tree and state-register view organize by execution semantics while retaining source locators, giving reflective coverage and intervention-site addressability without pretending the derived map is the code. This is the paper's evaluated contribution to the larger reflective self-improvement pathway. [deep-dive]
3. **Make progressive disclosure end in live-source verification** -- fixed behavior pointers should narrow the search, but every proposed edit site must be reopened in the current repository before it can support a plan. [quick-win]
4. **Store synchronization state as part of the compiled view** -- program graph, skeleton, mappings, source fingerprints/hashes, caches, and configuration make partial regeneration and conservative invalidation possible. [experiment]
5. **Use diffs, not planned declarations, to drive invalidation** -- declarations audit whether execution followed the plan; the actual repository diff determines what derived behavior knowledge may be stale. [quick-win]
6. **Evaluate localization with both overlap and complete-miss rates** -- recall/precision/F1 reveal coverage and focus, while the zero-overlap `Wrong` rate isolates catastrophic retrieval failure. [experiment]
7. **Treat generated behavioral orientation as a live tension for the KB** -- the reported gains suggest LLM-assisted generation can add useful stage and behavior orientation, qualifying the categorical claim that [index curation adds orientation that generation cannot produce](../notes/index-curation-adds-orientation-that-generation-cannot-produce.md). [deep-dive]

## Limitations (our opinion)

The evaluation measures read-only localization and edit-plan quality, not whether agents apply correct edits, pass tests, avoid regressions, or keep the handbook synchronized through real change sequences. The advertised self-evolving loop is therefore a design and future-work claim, not an evaluated result. The study covers only two harnesses and 60 authored requests with one planner model; Terminus-2 is only six files and receives a trusted hand-authored seed skeleton, while Codex uses the much coarser file-as-leaf mode. Model judges and model-generated reference plans are proxies for ground truth, and agreement with GPT-5.5 or Opus 4.8 does not establish that every necessary edit site is correct. Planner-token savings exclude the potentially substantial cost of initially constructing, reviewing, storing, and resynchronizing the handbook. There is no ablation against alternative hierarchical repository maps, call-graph retrieval, maintained architecture documentation, or an equal-cost generated index, so the contribution of behavior-centric organization versus simply providing more precomputed repository information remains uncertain. Finally, deterministic locators constrain where entries point but do not verify that LLM-written behavioral descriptions are semantically complete; conservative freezing contains some drift but leaves coverage gaps that a trusting planner may still overlook.

## Recommended Next Action

Write a note titled **Behavior localization is the addressability prerequisite for harness self-modification**, synthesizing this paper with [Reflective system](../notes/definitions/reflective-system.md) and [Retrieval failure is reflection failure](../notes/retrieval-failure-is-reflection-failure.md), while explicitly separating the paper's evaluated planning gains from its unevaluated execution and self-evolution loop.
