---
description: "De Kleer's ATMS makes support conditional on explicit assumption environments while leaving the assumptions' warrant to the problem solver"
source: https://www.dekleer.org/Publications/An%20Assumption-Based%20TMS.pdf
captured: "2026-09-17"
capture: pdftotext
capture_scope: full-source
doi: "10.1016/0004-3702(86)90080-9"
genre: scientific-paper
snapshot_sha256: c7614538c2948df847c7c6d7a840121fa5672f5988a20ad50ab6fd0dfb3198d4
ingested: "2026-09-17"
occasion: "Maintaining conclusions relative to assumption sets and recording dependencies; what it does not establish."
learning_claims: true
type: ingest-report
domains: [truth-maintenance, dependency-tracking, learning-theory]
---

# Ingest: An Assumption-based TMS

## Classification

This is a scientific paper that defines an assumption-based truth maintenance system, gives its formal properties and algorithms, and discusses implementation choices and motivating applications.
Author: Johan de Kleer, then at Xerox PARC's Intelligent Systems Laboratory, developed the ATMS and situates it against earlier truth maintenance systems and his own qualitative-reasoning systems.

## Summary

An ATMS records each derived datum with a minimal label of consistent assumption sets under which it holds. Justifications propagate these labels, while contradictions produce minimal “nogood” assumption sets whose supersets are excluded. This lets a problem solver retain mutually incompatible possibilities in one database, reuse conclusions across contexts by subset tests, and avoid most retraction and backtracking. The paper specifies consistency, soundness, completeness, and minimality requirements for labels, describes an incremental update algorithm, and explains implementation optimizations. Its guarantees are relative to the supplied assumptions and justifications: the ATMS maintains what follows in which consistent environments, but it does not decide whether the assumptions, inference rules, or conclusions are true or empirically warranted.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper is a technical basis for comparing explicit assumption dependencies with Commonplace's checker-relative source dependencies in [A note is an atomic step relative to the check that reads it](../notes/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md): both make a conclusion's usable support conditions inspectable, although they operate over different objects and checks. It also supplies a formal counterpoint to [A claim's warrant does not determine its fit in a working theory](../notes/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory.md): an ATMS can establish derivability and consistency relative to an assumption environment without establishing the independent warrant or theory fit of any member.

## Learning Claims (our opinion)

The paper calls the ATMS an intelligent cache or primitive learning scheme because it accumulates justifications and contradictions, transfers derivations across contexts, and avoids repeating work. This is learning only in that restricted operational sense. It is not theory refinement: empirical cases do not revise a tentative theory, and the ATMS supplies no operator for judging or repairing the assumptions and domain rules that determine its consequences. Instead, it incrementally compiles problem-solver-supplied structure into labels and nogoods. The source therefore sharpens a useful boundary for Commonplace: retaining dependency structure can improve reuse and localize inconsistency without providing evidence that the retained theory became better. The paper's formal analysis supports that mechanism, but it does not empirically establish improved learning outcomes.

## Extractable Value

1. **Separate conditional validity from warrant.** An explicit dependency structure can determine that a conclusion follows under a consistent assumption set without showing that the assumptions or inference rules deserve belief. This directly answers the occasion's “what it does not establish” boundary. [quick-win]
2. **Represent support as minimal environments.** A conclusion can carry several minimal assumption sets, with every consistent superset inheriting it; contradictions can likewise be stored as minimal nogoods that invalidate all supersets. This is a reusable formal model for maintaining conclusions across alternative contexts. [deep-dive]
3. **Keep content inference separate from dependency maintenance.** The problem solver supplies assumptions, data, and justifications, while the ATMS computes where their consequences hold. The separation clarifies that provenance machinery can preserve and propagate a dependency relation without choosing the claims or validating their content. [quick-win]
4. **Treat inconsistency as scoped by dependency.** A contradiction invalidates environments containing its supporting assumptions rather than forcing global retraction, allowing unaffected conclusions to remain usable. This offers a precise comparison point for localizing conflicts in a knowledge base. [experiment]
5. **Account for combinatorial cost.** Minimal labels avoid enumerating every context, but worst-case labels and nogoods can still be exponential in the number of assumptions; explicit dependency maintenance is therefore an architectural tradeoff, not a free guarantee of scalable context management. [just-a-reference]

## Limitations (our opinion)

The paper establishes the ATMS's formal label properties relative to supplied assumptions and justifications, but it does not test whether those inputs are correct or whether the resulting conclusions match an external world. Its efficiency discussion relies on algorithmic analysis, implementation experience, and motivating examples rather than a systematic benchmark against alternatives; the author also acknowledges exponential worst cases and expensive justification retraction. The framework therefore supports claims about conditional derivability and scoped inconsistency more strongly than broad claims about practical efficiency, learning quality, or epistemic reliability. Its assumptions are symbolic and explicitly enumerated, so transfer to natural-language KB claims also requires a separate account of how assumptions and dependency edges are identified and checked.

## Recommended Next Action

Write a note titled “Dependency tracking preserves conditional support, not warrant” that states the boundary, uses the ATMS as its formal case, and distinguishes dependency maintenance from claim validation and theory refinement.
