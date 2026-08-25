---
description: Scientific-software benchmark separates public-test conformance from private scientific correctness and finds supplied guidance can help, fail, or anchor repairs.
source: https://www.alphaxiv.org/abs/2608.19799
captured: "2026-08-25"
capture: trafilatura
genre: scientific-paper
snapshot_sha256: a96f8b22a189838617f56cdad75d541469ea6acda7a9776158384e9c58092a99
ingested: "2026-08-25"
type: kb/sources/types/ingest-report.md
domains: [coding-agents, evaluation, scientific-software, context-engineering]
---

# Ingest: SWE-bench Science on coding-agent repairs

## Classification

This is a scientific paper: its abstract reports a repository-level benchmark, an audit of unsuccessful repairs, and a paired ablation of explicit scientific guidance. Author: Zhipeng Xu, Jiahao Lu, Yining Zheng, Yuxin Wang, and Xipeng Qiu; the captured page identifies the authors and submission date but supplies no affiliation or peer-review signal.

## Summary

SWE-bench Science evaluates coding agents on 119 tasks from 98 repositories across 20 scientific domains, split among issue-driven, expert-exploratory, and engineering-integration paradigms. The authors report a best pass@1 below 50%, a gap between visible public checks and private scientific-validity tests, four recurring repair-failure mechanisms, and a 91-task paired ablation in which supplied scientific guidance had model-dependent effects and could anchor agents when it was poorly aligned. For Commonplace, the source is most useful as bounded evidence that local test conformance does not settle objective-level correctness, that diagnostic categories reveal more than aggregate success, and that context presence is distinct from correctly directed use and downstream benefit. The capture contains the paper abstract followed by an AlphaXiv AI overview, so details not stated in the abstract remain provisional.

## Quotes

No source quotes have been retained yet.

## Connections Found

The source is a bounded empirical anchor for [Exact implementation does not validate a requirement against its objective](../notes/exact-implementation-does-not-validate-a-requirement.md): its public/private test split instantiates local engineering conformance without treating that conformance as proof of broader scientific correctness. The guidance ablation is evidence for [Knowledge storage does not imply contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md) because supplying information does not ensure correctly directed influence or improved repair, although the captured account does not separately measure consultation and behavioral uptake. Its failure audit also supports the diagnostic-insufficiency premise of [Diagnostic richness constrains outer-loop learning quality](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md), but it does not test whether those diagnoses improve a later proposal loop.

Read through [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), agents can condition repairs on the repository snapshot, problem statement, reproduction script, public-test feedback, interaction history, and, in one treatment, explicit scientific guidance; they can compose repository exploration, test execution, code edits, and patch submission. Their effective hypothesis class maps that evidence to repair trajectories and patches within each fixed model-and-harness configuration. Task selection, repository state, public/private oracle partition, agent configuration, and the content of the supplied guidance remain outside that within-task update space. The paired ablation therefore identifies only the effect of adding versus removing that guidance in the tested setup; it does not validate the chosen guidance, benchmark decomposition, or agent action interface.

## Extractable Value

1. **Separate visible conformance from objective-level correctness.** The public/private oracle design gives the exact-implementation note a scientific-software case where passing exposed checks does not establish preservation of hidden scientific invariants. [experiment]
2. **Evaluate guidance through downstream benefit, not presence alone.** The paired guidance comparison extends the contextual-activation ladder to potentially misdirected influence: loaded information may change behavior yet reduce exact repair success. [experiment]
3. **Retain failure mechanisms alongside aggregate benchmark scores.** The four-part audit distinguishes knowledge or abstraction deficits, misguided exploration, incomplete integration, and failed generalization, offering a diagnostic vocabulary that a single pass rate erases. [just-a-reference]
4. **Bound every ablation claim to the varied coordinate.** Because the intervention changes explicit guidance while the task, executable context, test partition, and agent configuration stay fixed, its result cannot select among alternative guidance designs or validate the benchmark's other fixed choices. [quick-win]
5. **Treat scientific software as an objective-bearing instrument.** Hidden checks for semantic and scientific validity make repository repair relevant to evidence integrity, not merely program behavior, but the transfer should remain bounded to workflows whose scientific invariants are independently specified. [deep-dive]

## Limitations (our opinion)

In our opinion, this capture is not strong enough for load-bearing use of most quantitative or mechanistic details. It contains an authored abstract followed by an AlphaXiv AI overview rather than the full paper, and it exposes neither benchmark appendices nor statistical analyses. The benchmark's repository and task selection, hidden-oracle validity, per-domain coverage, uncertainty, and failure-coding procedure therefore cannot be assessed here; 119 curated tasks cannot by themselves establish performance across scientific software generally. The page reports a paired guidance ablation on 91 tasks, but it does not show enough design or trajectory evidence to distinguish anchoring from other explanations for the model-dependent performance changes. Nor does it specify the action interface and effective hypothesis class in enough detail to test whether failures arose inside the agents' update space or from fixed task, tool, guidance, and oracle choices. No code or experiments were inspected or executed for this ingest, and the captured page supplies no peer-review signal.

## Recommended Next Action

Create one separate ingest from the author-controlled full-paper PDF for arXiv:2608.19799 to verify the 91-task guidance ablation before integrating it into the contextual-activation note.
