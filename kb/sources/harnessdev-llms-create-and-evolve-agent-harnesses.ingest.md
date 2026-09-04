---
description: "HarnessDev provides bounded evidence that harness quality depends on executor fit, diagnostic use, evaluation noise, and the fixed development regime."
source: https://arxiv.org/abs/2609.01437
captured: "2026-09-04"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: efea62ea652086c948aa278def416578de52aa678e8d953e721a2ad98560cb9e
ingested: "2026-09-04"
type: kb/sources/types/ingest-report.md
domains: [agent-harnesses, agent-evaluation, harness-evolution, executor-transfer]
---

# Ingest: HarnessDev: Can LLMs Create and Evolve Agent Harnesses?

## Classification

This is a scientific paper that introduces a benchmark, reports controlled harness-creation and harness-evolution experiments, and analyzes performance, execution cost, transfer, revision trajectories, and mechanism reachability.
Author: The authors are researchers affiliated with ByteDance Seed, Singapore University of Technology and Design, Georgia Institute of Technology, M-A-P, and TokenWave.AI; the retained version is the first arXiv release rather than a peer-reviewed publication.

## Summary

HarnessDev evaluates persistent runnable agent harnesses as the output of development rather than treating a fixed harness as part of the benchmark setup. Six creator models build harnesses for code, data analysis, writing, and research from a weak seed; five creator-runtime lineages and four fixed-Gemini lineages then revise code harnesses using visible benchmark feedback. Generated harnesses remain behind selected mature systems on code and research, approach or exceed those references on writing and machine-learning experimentation, and vary widely in executor-token cost. Evolution yields local gains, but scores fluctuate across versions, visible-feedback gains transfer inconsistently to held-out tasks, and changing the runtime model can reverse the effect of a revision. The paper is therefore most useful as evidence that harness quality is conditional on the model and evaluation regime, and that reliable improvement requires diagnosis, regression control, and held-out selection rather than revision alone.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper is an empirical anchor for [The deployed system, not the model, is the unit of learning](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md): changing the harness with model weights fixed, and changing the executor behind a frozen harness, both move capability and cost. Its unchanged-commit score spread supports [Execution indeterminism is a property of the sampling process](../notes/execution-indeterminism-is-a-property-of-the-sampling-process.md), while its frozen versions, paired evaluations, and declared final candidate instantiate [A proposal-selection loop requires search, evaluation, and retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md). The low rate of case and trajectory inspection, together with the strongest documented repair following a concrete false-success diagnosis, is descriptive evidence for [Diagnostic richness constrains outer-loop learning quality](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md), not a controlled test of diagnostic richness.

[Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) limits the transfer claim. Creators could condition revisions on task specifications, development cases, scores, run diagnostics, trajectories, artifacts, and persistent repository history. They could compose code edits to the execution loop, tools, context, state, lifecycle, and verification logic, so a general coding model supplied a broad but unspecified hypothesis class over mappings from feedback to harness programs. The seed interface, development environment, model weights, task families, feedback and held-out partitions, scorers, evaluation budgets, and runtime binding within each comparison remained fixed outside that update space. Improvement therefore demonstrates search within the admitted harness-program space; it does not validate those fixed choices or establish self-hosted evolution.

## Extractable Value

1. **Treat harness quality as a conditional system property** -- The cross-executor reversals and large token-cost variation show that a harness result should travel with its creator, executor, runtime limits, task distribution, and scorer rather than become an executor-independent harness ranking. [deep-dive]
2. **Use failure diagnosis as evidence, not merely as workflow advice** -- Creators inspected only 0.5% to 40.2% of feedback tasks and called the dedicated trajectory interface twice, while a targeted diagnosis of premature success led to one of the clearest supported improvements. The association is descriptive but directly strengthens the KB's diagnostic-richness account. [quick-win]
3. **Make final-version selection a held-out and noise-aware operation** -- An unchanged commit varied by roughly plus or minus 4.75 pair-score points, feedback and held-out scores moved in the same direction in only 34 of 64 switches, and only two of nine declared versions were held-out-optimal. These results motivate repeated evaluation, explicit retention, and selection rules that do not equate the latest or highest visible score with progress. [experiment]
4. **Audit whether a mechanism executes, not only whether code declares it** -- The study distinguishes defined, reachable, and observed mechanisms and finds substantial dead or inactive code, especially in state and memory. This supplies a reusable evaluation method for separating architectural inventory from operative behavior. [experiment]
5. **Keep capability and executor cost as separate outcome axes** -- Execution-token use varied sharply and did not reliably predict downstream success, so a single performance score hides operationally consequential harness differences. [just-a-reference]

## Limitations (our opinion)

The strongest evolutionary conclusions are preliminary. Each creator-runtime cell has one trajectory, one main-runtime cell is unfinished, and post-freeze held-out evaluation covers only SWE-Pro, so the study cannot estimate population-level uncertainty or establish that the observed version-selection failures generalize across domains. Small adjacent score changes are especially hard to attribute because unchanged commits vary materially; the paper's reachability and case-level analyses strengthen a few mechanism claims but do not make every revision causal.

The selected human-engineered references are uneven external system results rather than paired controls under one executor, so gaps to those references conflate harness, model, runtime, and evaluation differences. Unified-Eval improves the generated-harness comparison but fixes Gemini as the executor, and GPT-5.5 alone uses Codex rather than Claude Code as its development environment. More broadly, the experiment exposes rich feedback and a broad code-editing action space while fixing the seed contract, development tools, benchmarks, scorers, budgets, and task partitions. It shows that models can improve within that decomposition, not that the decomposition is sufficient for deployment or that a harness can become its own development environment.

## Recommended Next Action

Write a new `kb/notes/` claim titled “A harness-quality result belongs to a model-harness-runtime-regime pairing” that synthesizes the executor-transfer, token-cost, stochastic-score, and fixed-decomposition evidence into the metadata that must accompany any reusable harness-quality claim.
