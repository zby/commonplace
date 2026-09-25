---
description: "Human memory expertise combines meaningful encoding, learned retrieval structures and practice; its task-specific gains bound comparisons with agent knowledge access."
source: https://archive.org/download/DTIC_ADA114634/DTIC_ADA114634.pdf
captured: "2026-09-24"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: d6758de5279a6a08bad7b425754f8a6a43436e5384cdac849da028776e98bf1c
ingested: "2026-09-25"
type: types/ingest-report.md
domains: [human-memory, learning-theory, knowledge-access]
learning_claims: true
---

# Ingest: Skill and Working Memory

## Classification

An empirical and theoretical psychology report combining longitudinal training, experimental probes, expert case studies and a review of earlier research. The captured version is the April 30, 1982 technical report, announced as forthcoming in *The Psychology of Learning and Motivation*, volume 16; identity with the published chapter is not established here. Authors William G. Chase and K. Anders Ericsson report their own research on memory expertise from Carnegie-Mellon University and the University of Colorado.

## Summary

Chase and Ericsson argue that skilled memory depends on meaningful encoding into long-term memory, learned structures for retrieving the encoded material, and faster memory operations with practice. Their main evidence concerns two runners trained over hundreds of sessions on ordered digit recall, who reached maximum spans of 82 and 68 digits using running times, ages, years and numerical patterns as mnemonic codes. These gains occurred within a task with a standard presentation rate of one digit per second and self-organized grouping and retrieval; they do not establish a general increase in short-term storage capacity or superiority over alternative memory architectures. Interference experiments, unchanged consonant spans and recall through different cues support the narrower account of improved access to long-term memory. Studies of a mental calculator, a waiter and sentence recall broaden the phenomenon, with different evidential strength. The authors consequently propose that working memory include task-specific long-term retrieval and context, alongside currently active information. For Commonplace, the useful comparison is that effective memory depends on encoding, access conditions and the task being performed, rather than stored volume alone.

## Quotes

No source quotes have been retained yet.

## Connections Found

The report supplies a human comparison for [knowledge storage versus contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md). In the digit experiments, material poorly recalled through its position in an ordered list could remain accessible through semantic cues after the session. This bears on the storage-to-retrieval distinction; it does not establish the note's stronger context-to-action mechanism in agents.

It also compares with [evaluating knowledge access end to end](../notes/knowledge-access-architecture-must-be-evaluated-end-to-end.md). The trained subjects' gains depended on meaningful codes, practiced retrieval and enough encoding time within the digit-recall task. The matrix experiments further suggest that unskilled subjects can approach experts' retrieval speed when given enough time to learn the material. Access cost therefore cannot be separated from preparation and task conditions. As [human–LLM differences](../notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) requires, an agent implementation needs its own evidence: a software index and a learned human retrieval structure share a possible function without sharing an established mechanism.

## Learning Claims (our opinion)

The observed learning is a persistent improvement in domain-specific memory performance. Repeated attempts at ordered recall give subjects success and error experience while they develop mnemonic categories, grouping strategies and retrieval locations. The authors infer that practice also speeds encoding and retrieval, although they explicitly acknowledge limited speed evidence and a less clear trend for DD. A retrieval structure here is a learned long-term organization that lets a person recover a digit group by its location; it is not simply another name for the semantic knowledge used to encode that group.

This is broader adaptation than tuning values inside an immutable mnemonic system. SF adds semantic categories and new hierarchical levels during training. Those representations are among the things that change, while the basic digit input, ordered-recall requirement and ordinary presentation rate remain task conditions. In the terms of [learning within a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), an unchanged experimental interface did not imply an unchanged internal representation. The results show that these learned strategies worked under the tested conditions; they do not compare their full organization with every alternative. The separate subject who developed mnemonic codes but plateaued near eighteen digits without a comparable retrieval structure is a suggestive contrast, not a randomized component ablation.

Whether the trained subjects are [theory builders](../notes/definitions/theory-builder.md) in their memory practice remains unresolved. Their verbal reports state mnemonic codes and strategy changes, so some content is stated (condition 1), though the retrieval structures may be practiced organization no one states. The simulation's prediction of SF's coding choices suggests the stated codes guide encoding (condition 2). The skill persists across hundreds of sessions and new digit lists (condition 4). Criticism (condition 3) is unestablished and decides the verdict: the report does not show the subjects attempting to refute what a stated strategy says, and this missing evidence does not show that such criticism was absent. Learning is established: capacity improved markedly under the tested conditions. It is not attributed to criticism. The researchers' explanatory theory and its experimental tests belong to a different declared [boundary](../notes/definitions/theory-builder.md#boundary) from the subjects' acquisition of memory skill. Commonplace can use the source to distinguish observable capacity gains from evidence about the particular learning process, without forcing all practice-based adaptation into the theory-builder category.

## Extractable Value

1. **Encoding must anticipate later access.** The proposed mechanism binds the digit trace to semantic features, a retrieval location and context. Different cues then make different routes available. This adds a worked human mechanism to the existing access notes, while leaving any equivalent benefit from agent metadata or indexing to be tested. [just-a-reference]
2. **Measure useful capacity under the actual time budget.** Large digit spans arise in a practiced encoding-and-retrieval regime. At three digits per second, even the extensively trained subjects recalled only about eleven digits; given sufficient matrix-learning time, unskilled subjects approached expert retrieval times. These task-bound observations motivate measuring preparation cost, access latency and downstream performance together when comparing agent memory designs. [experiment]
3. **Diagnose the retrieval route before inferring loss of content.** Later digit groups could fare poorly in ordered recall yet well in subsequent semantic recall. The authors interpret this as interference affecting access through retrieval locations. The result gives a concrete human comparison for testing multiple cues when a stored item appears unavailable, without establishing that all forgetting is an access failure. [just-a-reference]

## Limitations (our opinion)

The main training evidence comes from two exceptional runners whose prior knowledge supplied rich numerical associations. It establishes a striking possibility under sustained practice, not the distribution of gains among ordinary learners or transfer across domains. Unchanged consonant spans limit a general-capacity interpretation, although SF's successful use of the structure for fourteen names also cautions against claiming absolute digit specificity.

The interventions vary particular conditions: whether early digit lists fit SF's available codes, which concurrent task interferes, and which cues support recall. They do not independently isolate every proposed component. Hierarchical pauses, verbal protocols and the reported simulation's roughly 90 percent prediction of SF's coding choices constrain an account, but do not uniquely establish the hypothesized memory links. Alternative explanations of some forgetting remain open. No simulation code was inspected or executed, and no experiment was reproduced for this ingest.

The further studies have separate limits. The calculator is one expert with a fitted process model. The waiter analysis is explicitly unfinished, uses simulated random orders, and changes the number of items per order across the reported training periods. Meaningful-versus-scrambled sentence recall extends the phenomenon beyond exceptional experts, but is not a demonstration of equal training gains for all adults. The authors' speculation that highly practiced long-term access approaches short-term access speed should remain distinct from the measured results.

The capture covers the full report, but OCR damages figures, formulas, names and some numbers. The analysis relies on legible prose and does not reconstruct quantitative results from broken graphics. Human span estimates, interference effects and internal learning mechanisms supply no agent context-window limit or general recommendation for hierarchical retrieval. Their transfer is constrained by the consumer differences discussed above.

## Recommended Next Action

Retain this ingest as a source-only reference for task-specific encoding and retrieval in comparisons of human and agent knowledge access.
