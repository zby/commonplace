---
description: "OOPS reuses frozen programs to reshape later program search; its Hanoi example traces a local productivity gain under a chosen language, curriculum, and bias."
source: https://sferics.idsia.ch/pub/juergen/oopsmlj.pdf
captured: "2026-09-20"
ingested: "2026-09-21"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: ce2a5d3b298b1c97527b6a550fdf1510faba48896a7e6407dadf91dfa2da0c5b
type: kb/sources/types/ingest-report.md
domains: [program-search, incremental-learning, self-improving-systems]
learning_claims: true
---

# Ingest: Optimal Ordered Problem Solver

## Classification

Jürgen Schmidhuber's 2004 *Machine Learning* paper combines a formal search construction, arguments for its restricted optimality, implementation details, and an illustrative experiment. The author designed OOPS and reports its own implementation; the experiment is not independent replication.

## Summary

OOPS searches for programs that solve an ordered sequence of verifiable tasks, freezes successful programs, and gives later searches access to that code. Half the search budget extends the most recent successful program; the other half searches fresh programs, testing them against all previous tasks when a universal solver is required. Candidate prefixes can alter the probabilities of their own continuations, letting program search discover ways to accelerate itself. Its near-bias-optimality bounds search relative to a supplied program distribution and includes verification cost; it does not promise practical speed under an unsuitable bias. In a FORTH-like language with hand-selected primitives, probability boosts, and a curriculum of string-generation tasks followed by Towers of Hanoi, the paper reports solving all 60 instances through size 30. It traces the Hanoi search benefit to a prefix that boosts instructions found in an earlier frozen program, estimating roughly a thousandfold acceleration from the resulting program probabilities. This is a mechanism-specific transfer example within that setup, not a general learning-speed benchmark.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper supplies a concrete case for [accumulation through the retained result](../notes/accumulation-counts-dependence-through-the-retained-result.md): a later prefix reads the instruction content of an earlier frozen solver to change which continuations receive search time. The earlier program is not merely responsible for generating later evidence. Its contents enter the later search directly.

It also provides bounded evidence for the distinction in [improvements can accumulate without compounding](../notes/improvements-can-accumulate-without-compounding.md). Within the paper's chosen language, curriculum, and initial boosts, the Hanoi trace connects an earlier retained solution to reduced later search cost. The reported thousandfold factor is supported by program-probability analysis, rather than a matched set of repeated transfer experiments. The paper also reports that discovery of the general string-generation solver did not benefit from its predecessors. Together these support examining individual dependence and productivity paths rather than assigning sustained compounding to an entire run.

## Learning Claims (our opinion)

The retained learning product is executable code. OOPS freezes each successful program, while later programs may invoke it, copy and edit it in writable storage, or use its contents to compute a search distribution. Distribution changes made during a candidate test are temporary and restored during backtracking. Persistent code can recreate them later; it would be misleading to describe every temporary probability update as a retained learning result.

In Commonplace terms, the experiment demonstrates operative retention and a later search that consumes it. The unusual transfer is through instruction probabilities: the Hanoi solver does not call the earlier string generator as its solution procedure. A short prefix instead makes the earlier solver's recursion-related instructions more probable in the remaining search. This extends the useful picture of reuse beyond calling or editing an earlier solution.

The mapping to [theory refinement](../notes/definitions/theory-refinement.md) is partial. Programs have executable consequences and editable parts, and the framework permits copy-editing. The demonstrated transfer, however, does not diagnose and repair an existing theory against a counterexample. It searches for a new task-solving program using retained code as bias. Addressability and self-directed search changes alone do not establish theory refinement.

The general framework admits arbitrary computable program compositions, so an omitted primitive is not automatically an unreachable behavior. Nevertheless, the experiment fixes the interpreter, available instructions, task representation, verification conditions, reset mechanism, and human-chosen task order and boosts. Following [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), success establishes a useful search path within that configuration; it does not compare alternative representations or show that OOPS learned those external choices. Its proposed world-model and action-search extension for reinforcement learning remains an outline, separate from the demonstrated task sequence.

## Extractable Value

1. **Retained content can improve later search without executing its original solution.** The identified instruction-frequency transfer adds a concrete mechanism to the KB's accumulation account: earlier code helps generate a different solver by changing continuation probabilities. This mechanism is broader than the two benchmark domains, although its usefulness depends on relevant shared program structure. [quick-win]
2. **A local productivity contribution can coexist with nonbenefiting episodes.** The Hanoi probability analysis and the earlier general string solver's lack of dependence provide a useful paired case for assessing accumulation and compounding episode by episode. Preserve the fixed language, curriculum, and bias conditions beside the roughly thousandfold estimate. [quick-win]
3. **Optimal allocation does not supply a good initial representation or bias.** The formal guarantee, the unsuccessful week-long Hanoi search beyond three disks before the curriculum, and the authors' hindsight example of a much stronger initial bias distinguish search efficiency relative to a prior from choosing a useful prior. This is a technical reference for qualifying claims about optimal self-improvement. [just-a-reference]

## Limitations (our opinion)

The empirical comparison is illustrative. Before the curriculum, the reported search used 71 instructions; the curriculum setup added two string-generation instructions and used phase-specific boosts. The paper explains the later speedup by comparing probabilities of the found solver with and without the learned prefix. That is useful mechanism evidence, but it does not isolate all curriculum and initialization choices in a matched ablation or establish the best possible alternative solver's search time. Historical comparisons with reinforcement learners and planners likewise use different representations and search spaces.

The formal guarantee is relative to the supplied bias and accounting assumptions. Extremely small solver probabilities can still imply impractical search. The experiment does not show that an expanding code library remains economical to navigate across diverse real tasks; the paper itself anticipates increasing difficulty identifying and addressing useful stored code.

Candidate testing requires restorable task state and a computable verification procedure. Section 5.2 explicitly limits the foundation where the environment cannot be reset. This prevents treating the construction as a demonstrated solution for irreversible real-world learning. Likewise, passing successive finite tasks is not by itself a proof of unrestricted future generalization, even when inspection reveals a general recursive algorithm.

No implementation was inspected or executed for this ingest. Runtime and outcome claims remain the paper's reports. The evidence supports a particular cross-task transfer mechanism, not sustained compounding, automatic curriculum discovery, or a measured improvement to agent-operated KBs.

## Recommended Next Action

Add the string-generator-to-Hanoi transfer as a bounded evidence case in [Improvements can accumulate without compounding](../notes/improvements-can-accumulate-without-compounding.md), retaining its instruction-probability mechanism, fixed experimental setup, and distinction between local productivity evidence and sustained compounding.
