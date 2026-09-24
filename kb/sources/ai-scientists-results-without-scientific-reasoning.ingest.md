---
type: kb/sources/types/ingest-report.md
description: "Corral separates scientific task success from visible hypothesis testing and revision, but its minimal scaffolds and graph annotations limit claims about scientific learning."
source: https://arxiv.org/abs/2604.18805
captured: "2026-09-19"
ingested: "2026-09-19"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 898ebf2e679c58e6af23df696bf800b5e4dca6cc2c2c22113cd156092d7f61a8
occasion: "Assess 2026 computational implementations and evaluations of conjecture, criticism, revision, and persistence for a learning paradigm grounded directly in Popper; distinguish epistemic commitments, implementation choices, and demonstrated effects."
domains: [scientific-agents, evaluation, theory-refinement]
learning_claims: true
---

# Ingest: AI scientists produce results without reasoning scientifically

## Classification

Scientific paper: Ríos-García, Alampara, and colleagues present Corral, a controlled scientific-agent evaluation framework, performance comparisons, trace interventions, and automated epistemic-graph annotation. The captured April 2026 arXiv version reports experiments rather than merely proposing an architecture. Its authors develop both the benchmark and its reasoning taxonomy; the process judgments therefore require calibration independently of task scores.

## Summary

Corral evaluates three model versions with ReAct and native tool calling across eight scientific domains and more than 25,000 runs. Within these two minimal scaffolds, flat conversation histories, and fixed 20–40-call budgets, model differences predict performance more strongly than scaffold choice. A separate graph analysis of 626 ReAct traces identifies hypotheses, tests, observations, judgments, and revision relations; successful outcomes can coexist with weak visible testing and evidence uptake. The main text reports 68% evidence non-uptake and 26% refutation-driven revision, although Appendix H contains inconsistent prevalence summaries. Replaying successful trajectory prefixes helps workflow execution earlier than hypothesis-driven tasks, where gains require nearly complete prefixes; replay also executes tools and restores environment state. The paper offers a way to inspect scientific process separately from endpoints. Its stronger conclusion that scaffold engineering cannot repair the failures exceeds the architectures compared, and it does not test persistent learning across tasks.

## Quotes

No source quotes have been retained yet.

## Connections Found

For the occasion, the source is a bounded evaluation reference for conjecture, testing, and revision, rather than a demonstrated implementation of persistent Popperian learning. It supplies a concrete case for [an experiment identifying only its actual contrast](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md): small differences between two action interfaces with minimal orchestration do not settle the value of explicit hypothesis stores, retrieval, independent criticism, or durable revision.

It also offers limited evidence for [knowledge storage not implying contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md). An observed result and a later judgment can lack an annotated dependency even when both appear in the transcript. This makes uptake a separate evaluation question, but missing graph edges are not proof that information had no behavioral effect. The [trajectory-aware evaluation proposal](../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) is the relevant local destination: Corral motivates inspecting evidence-to-revision transitions while exposing false-positive risks that the proposal's blinded adjudication should test.

## Learning Claims (our opinion)

The source studies within-episode adaptation: an agent proposes a hypothesis, requests a measurement, interprets the result, and may revise its hypothesis. Tools expose domain evidence; the model chooses subsequent actions from its accumulated conversation. The experiment does not update model weights or carry revised hypotheses and heuristics across tasks. Injected histories come from earlier runs of the same task and reexecute their tool calls; this intervention tests continuation from a supplied trajectory and reconstructed state, not transfer of learned theories.

The hypothesis–test–revision relations partially map onto [conjectural learning](../notes/definitions/conjectural-learning.md). Explicit hypotheses can be criticizable objects, and a contradiction followed by a revised hypothesis can document an episode of error correction. The graph alone does not establish that the hypothesis content caused later decisions or that the process of conjecture and criticism improved capacity for future action. It also does not establish the separate properties of addressability, preservation of prior useful consequences, or later reuse of a retained revision. This source contributes diagnostic questions for the conjectural-learning account, not evidence that the full operation is absent from all scientific agents.

Its epistemic commitments are broader than Popper's conjecture-and-refutation schema. The authors invoke Popper for falsification patterns, but also use abductive generation, convergent evidence, and a justified-true-belief framing. Their motif vocabulary is an operational choice, not a derivation of a complete learning paradigm from Popper. The paper recommends making reasoning a training target; no training intervention demonstrates that remedy.

The [fixed-decomposition boundary](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) matters twice. Agents operate within supplied tool interfaces, budgets, and histories; their performance cannot select among excluded persistent-learning architectures. Evaluators operate within a fixed node-and-edge taxonomy and visible transcript windows; success at recovering those labels would not itself validate that taxonomy as a complete measure of scientific inquiry.

## Extractable Value

- **[experiment] Separate process, correction, and persistence measurements.** Corral's hypothesis–test–revision graphs provide a candidate within-episode assay for the Popper-grounded learning investigation. Add independent checks of whether a contradiction changed an explicit claim and whether the changed claim later controlled a new decision; Corral itself tests neither cross-task retention nor reuse.
- **[quick-win] Preserve the scaffold comparison boundary.** The reported 1.5% scaffold contribution belongs to a fitted variance decomposition over two minimal interfaces, three models, and fixed environments. It supplies an example of overgeneralization to avoid when comparing learned models with engineered learning systems; it is not a ceiling on harness effects.
- **[experiment] Calibrate missing-edge judgments before using them as criticism.** Include cases with implicit but behaviorally clear uptake, cases without an opportunity for refutation, and cases with actual contradictions followed by unchanged action. Score these with blinded human adjudication before treating motif absence as learning failure.
- **[just-a-reference] Distinguish reliable repetition from successful retry.** Corral's Pass^k measures success on every one of k trials, whereas pass@k measures at least one success. Declining all-trial reliability does not demonstrate that retries reduce the chance of eventually obtaining a correct answer.

## Limitations (our opinion)

The tested models are GPT-4o-2024-08-06, Claude Sonnet 4.5-20250929, and GPT-OSS-120B. Appendix I explicitly excludes cross-task memory, retrieval, summarization, explicit planners, and multi-agent architectures. A simpler explanation of scaffold similarity is that both scaffolds preserve nearly the same decision loop. Fixed temperature, small call budgets, and unmitigated malformed responses further limit attribution to an intrinsic reasoning defect. No alternative learning architecture or reasoning-targeted training treatment establishes the proposed remedy.

Process measurement covers 626 brief-mode ReAct traces, not the full run population. Claude annotates overlapping transcript windows and omits uncertain relations. Appendix H reports 25,369 validation warnings, predominantly non-verbatim quote matches; detailed methods and the table retain these annotations despite nearby prose saying failed checks discard graphs. A missing edge can reflect annotation omission or implicit reasoning. Illustrative non-uptake and fixed-belief examples themselves include looking back at supplied evidence or correcting a file path. They caution against equating absent edges with absent use or correction.

Calibration also has narrower coverage than some wording suggests. The 773 manually labeled behavioral traces are distinct from epistemic-graph review: Appendix H.5 describes three reviewers examining 25 of the 626 graph traces. High percentage agreement and adjusted agreement coexist with low Cohen kappa under severe label imbalance. They do not settle per-motif false positives, especially when an episode had no relevant opportunity to revise.

Internal reporting differences prevent treating headline quantities as unambiguous estimates. Main-text 68% non-uptake and 26% revision conflict with Appendix H's opening two-model figures of 88% and 4%/1%, although its later three-model table broadly supports the main aggregates. Main-text reasoning variance of 41.4% and environment-scope variance of 30.1% differ from Appendix G.5's combined model-identity 45.2% and environment-scope 32.5%; these decompositions should not be merged. Prefix interventions also bundle reasoning exposure with completed tool actions and changed environment state, so late-prefix gains cannot isolate acquisition of reusable knowledge.

## Recommended Next Action

Extend the existing [trajectory-aware evaluation proposal](../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) with a calibrated hypothesis–contradiction–revision assay that distinguishes missing annotation from missing correction and records later reuse separately from within-episode revision.
