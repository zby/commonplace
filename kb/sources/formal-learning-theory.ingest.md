---
description: "Formal learning theory separates eventual reliable convergence from present warrant and derives short-run constraints only from additional epistemic goals"
source: https://plato.stanford.edu/entries/learning-formal/
captured: "2026-09-17"
capture: trafilatura
capture_scope: full-source
genre: conceptual-essay
snapshot_sha256: 33ff913a596a2fc07f67fd070645c17e5081571016901ac33af63da7baa9d94a
ingested: "2026-09-17"
occasion: "Convergence guarantees versus current warrant, the distinction the README's source checks require."
learning_claims: true
type: types/ingest-report.md
domains: [learning-theory, epistemology, evaluation]
---

# Ingest: Formal Learning Theory

## Classification

This is a conceptual reference essay that surveys the concepts, examples, and characterization theorems of formal learning theory, with emphasis on the nonstatistical reliabilist tradition and a later extension to statistical inquiry. Author: Oliver Schulte is the named author of a substantively revised Stanford Encyclopedia of Philosophy entry; the article locates its claims in a large technical and philosophical literature and distinguishes introductory examples from cited formal results.

## Summary

Formal learning theory evaluates an inductive method relative to a specified empirical problem and cognitive goal. Its basic success criterion is reliable identification in the limit: for every admissible complete evidence sequence, the method eventually settles on the correct hypothesis and does not leave it. This guarantee does not establish that the method's current conjecture is correct, certain, or warranted by the finite evidence currently available. The article then shows how stronger goals, including fewer mind changes, fewer regressive changes, and stable belief, can constrain short-run conjectures and motivate problem-relative simplicity principles. Its results are conditional on the hypothesis space, evidence structure, background assumptions, success criterion, and, in the statistical case, sampling assumptions.

## Quotes

No source quotes have been retained yet.

## Connections Found

The source is a technical and conceptual anchor for the distinction between eventual success and present warrant. It supports the temporal separation in [A claim's warrant does not determine its fit in a working theory](../notes/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory.md): convergence of a method across complete evidence sequences does not independently warrant its conjecture at a finite stage. It also compares with [Compounding is tested in the later improvement, not by the accepting metric](../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md), because both require evidence at the time and level where the claimed property manifests rather than treating an earlier success condition as present proof. Finally, the source supplies a formal analogue of [Warranted autonomy is bounded by oracle domain](../notes/warranted-autonomy-is-bounded-by-oracle-domain.md): a reliability result is relative to a defined problem, admissible evidence, and success criterion, so it does not license conclusions outside that domain.

## Learning Claims (our opinion)

On the source's terms, a learner maps each finite observation sequence to a hypothesis; learning is the eventual stabilization of those conjectures on the correct hypothesis for every admissible complete sequence. The effective update space consists of conjecture changes within a background hypothesis set, while the hypothesis partition, possible evidence sequences, background assumptions, and success criterion are fixed by the learning problem. Statistical identification changes the criterion to convergence in chance under explicit sampling assumptions.

This is only a partial match for Commonplace's theory refinement. The successive conjectures can change in response to evidence, but the formal learner need not revise an addressable theory with separately editable parts or preserve useful internal structure. The source therefore sharpens the distinction between using a fixed inductive method to update beliefs and revising the theory or method that produces them. Its strongest contribution to the current account is a warning about evidential tense: a property proved over complete inquiry histories need not be available as warrant for the learner's current output. Short-run constraints arise only after further ends, such as stability or avoiding regressive mind changes, are added, and even then remain relative to the fixed learning problem.

## Extractable Value

1. **Separate convergence guarantees from current warrant.** A method can be certain to settle correctly in the limit while neither the method nor its operator can know that its present conjecture is the settled one. This directly supplies the distinction needed by the occasion. [quick-win]
2. **State the problem-relative scope of every guarantee.** Reliability depends on the admissible hypothesis set, evidence sequences, background assumptions, and success criterion; changing these can change which method is optimal or whether reliable identification is possible. [quick-win]
3. **Treat short-run prescriptions as conclusions from added goals.** Long-run reliability alone can underdetermine present conjecture, while stability, mind-change bounds, or avoidance of regressive changes can select among reliable methods. [deep-dive]
4. **Distinguish belief updating from theory refinement.** Mapping observations to hypotheses may learn in the source's sense without revising an addressable theory, which prevents convergence results from being imported wholesale into Commonplace's account of theory refinement. [quick-win]
5. **Use mind-change direction as a possible evaluation dimension.** Progressive and regressive revisions distinguish correction from loss of a true conjecture, offering a more informative temporal measure than counting all revisions alike. [experiment]

## Limitations (our opinion)

The article is a broad reference synthesis rather than a single new proof or empirical evaluation. Many formal results are stated with citations while their full definitions or proofs are delegated to the bibliography and a separately linked supplement, which this capture does not include. The examples establish what follows inside explicitly defined learning problems; they do not show that a real agent's hypothesis space, evidence stream, or success criterion has been specified correctly. The framework's convergence guarantees therefore cannot establish current truth, current warrant, or successful theory refinement without additional evidence connecting those abstractions to the operative system.

## Recommended Next Action

Revise [A claim's warrant does not determine its fit in a working theory](../notes/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory.md) to state explicitly that a method's convergence guarantee does not establish warrant for its current output, using this ingest as the technical basis.
