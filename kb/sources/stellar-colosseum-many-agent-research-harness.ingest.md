---
description: "Stellar Colosseum carries critiques through proof synthesis and local repair; benchmark gains support the combined workflow without isolating its decomposition or memory design."
source: https://arxiv.org/abs/2609.15983
captured: "2026-09-24"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 7131a950d588a1c3cb91885be2ddb269cb91589e9a216d1b873d0fe947c58b88
ingested: "2026-09-25"
type: kb/sources/types/ingest-report.md
domains: [multi-agent-coordination, mathematical-reasoning, knowledge-reuse, learning]
learning_claims: true
---

# Ingest: Stellar Colosseum: A Many-Agent Harness for Long-Horizon Research

## Classification

A research preprint describing an inference harness, benchmark evaluations, and selected research cases. Authors Honghao Lin, David P. Woodruff, Yuan Deng, Jieming Mao, Song Zuo, and Vahab Mirrokni are affiliated with Google Research, with Woodruff also at Carnegie Mellon University. They report their own system; the architectural detail is stronger evidence of the proposed mechanism than the evaluations are of any individual component's contribution. This analysis uses the captured v2 paper, including its shortened prompt appendix.

## Summary

[Stellar Colosseum](https://arxiv.org/abs/2609.15983) organizes research around strategy exploration, a readiness gate, a dependency graph of proof sections, local retries, and global verification. Within stages, sampled candidates remain paired with critiques as overlapping groups synthesize new artifacts. Unresolved objections must survive synthesis, and failed drafts plus curated findings inform subsequent rounds. On 300 TCS-Bench tasks, individual Gemini 3.1 Pro and Gemini 3.7 Flash runs score 54% and 55%; critique-based selection between them reaches 71% under a reference-assisted model grader. This is a combined harness-and-selection result, without a compute-matched comparison of alternative architectures. On 222 Codeforces problems, adding execution feedback raises acceptance from 213 to 218 while retaining the proof-oriented decomposition and terminal C++ implementation step. The paper also reports contributions to five research results and long proof drafts, with full proofs and attribution delegated to companion publications. Its strongest methodological contribution is a concrete way to carry criticism through synthesis and selective repair without treating an intermediate acceptance judgment as proof.

## Quotes

No source quotes have been retained yet.

## Connections Found

The harness is a design counterpoint to [Synthesis is not error correction](../notes/synthesis-is-not-error-correction.md). Its aggregators can reject, weaken, repair, or retain an attacked claim as an explicit obligation; synthesis therefore includes adjudication rather than indiscriminate merging. This complicates the note's categorical account of synthesis while leaving its distinction from voting intact. No critique or aggregation ablation establishes that Colosseum's particular combination reliably corrects errors or caused the reported benchmark gains.

The workflow also illustrates the scope condition in [Localized retention pays when sparse changes have bounded impact](../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md). A failed section can be retried while other sections remain, but the assembled proof still receives global verification for cross-section assumptions and target mismatch. Local editing does not establish local validation. Compared with [Prove2Me](./prove2me-collaborative-math-formalization.ingest.md), both systems expose unfinished obligations and dependencies, but Colosseum relies primarily on model-reviewed natural-language proofs. Prove2Me checks proof types against immutable formal statements in a pinned environment. Neither a model verdict nor formal type checking alone establishes correspondence to the originally intended claim.

## Learning Claims (our opinion)

The source describes two forms of within-investigation retention: the latest complete draft with its verifier feedback, and a curated directory of lemmas, failed approaches, references, and observations with sources and caveats. Strategies and section claims change in response to specific objections. The reported unit-distance case carries this state through 15 exploration rounds before producing a new draft. Across-run post-training from externally validated trajectories is a future direction, not an evaluated learning mechanism.

Against the four conditions of a [theory builder](../notes/definitions/theory-builder.md), conditions 1 to 3 are met on the described design. Strategy cards, bridge claims, and section obligations are stated units, many of them [addressable](../notes/definitions/addressable-theory.md) at fine grain (condition 1). They guide which route is explored, which sections are drafted, and which obligations a repair must meet (condition 2). Critiques are stated, paired with the candidate they attack, and require a disposition, so criticism aims at what identified claims say (condition 3). Condition 4 (iteration) is met: the verifier feedback kept with the latest draft and the curated directory of failed approaches shape the next exploration round and repair. As evaluated, Colosseum is inside the term. The directory and draft history are taken up only by later rounds on the same target, so the persistence grade reached is across rounds of one run on one problem. The five research results are separate problems, and the paper reports no finding carried from one into another. The only cross-run mechanism it names, post-training on validated trajectories, is future work and would act on weights, not on stated findings. Learning is a separate question: benchmark success and revision histories do not show that retaining findings improves future capacity over otherwise equivalent runs.

The effective revision space changes by stage. Exploration can replace a route and decomposition can create its proof plan; local retry keeps the assigned subproblem and dependencies fixed. The appendix's conservative outline repair forbids adding or reordering sections or introducing a new strategy, with major failures routed back to exploration. Population widths and sampling configurations remain fixed during the evaluated runs. Local graph restructuring and adaptive compute allocation are proposed extensions. As in [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), successful repair inside these boundaries does not compare the boundaries themselves. This is a useful worked distinction between revising subject-matter claims and adapting the harness that organizes their revision, without requiring a change to Commonplace's theory-builder definition.

## Extractable Value

1. **Make objections part of the synthesis input and output.** Pair each candidate with its criticism and require a disposition for substantive objections. The design gives the existing synthesis discussion a concrete alternative to both unfiltered merging and voting. Its causal benefit remains unmeasured. [quick-win]
2. **Gate decomposition on whether uncertainty can be assigned to stable subproblems.** The readiness gate permits an unfinished route when its remaining obligations have concrete proof or verification paths, while returning architectural uncertainty to exploration. This offers a reusable workflow criterion for deciding when parallel work can begin; it is a proposed mechanism rather than a validated optimal gate. [experiment]
3. **Keep local repair and global assurance separate.** Retaining unaffected sections reduces regeneration, but the global verifier checks dependencies and the original target again. The source operationalizes the existing locality qualification without demonstrating bounded validation cost. [quick-win]
4. **Retain the execution-feedback comparison at its tested scope.** Acceptance rises from 213 to 218 of 222 when public-sample and generated-input probes feed the existing revision loop. The mathematical subproblem graph and final implementation step remain fixed. This supports adding executable evidence within that architecture, not preferring it to a code-specific controller or alternative decomposition. [just-a-reference]

## Limitations (our opinion)

The TCS-Bench grader receives reference proofs and reports over 90% accuracy on a separate set of 100 expert-labeled proofs; it does not supply formal certificates for the evaluated outputs. The 71% score uses eight Flash critiques to select between two full model runs. The 77.3% oracle best-of-two is an upper bound, not an implemented selector. Greater inference expenditure, model complementarity, and selection can explain improvements without isolating the benefits of critique retention, readiness gating, or shared memory. The paper supplies neither matched-compute architecture baselines nor component ablations for those mechanisms.

Overlapping random groups give candidates multiple opportunities to contribute, but do not guarantee preservation of a minority route or objection. The authors themselves identify loss of minority strategies as a reason to investigate clustered exploration. Independently sampled reviews may share mistakes; the prompts' instructions to preserve objections are not demonstrated enforcement guarantees. Tree width also understates total inference because section count, retries, and revision rounds vary.

Codeforces hidden tests are reserved for final grading, so the execution-feedback comparison has a distinct external outcome check. Its fitted rating of 4263 is specific to the corpus and calibration rule, not an official contestant rating. The five research advances defer complete proofs and attribution to companion papers, while long drafts and internet-disabled rediscovery do not independently establish correctness, novelty, lack of training exposure, or autonomous contribution. This ingest inspects no implementation and executes no harness code; source descriptions and shortened prompts remain the evidence for mechanism claims.

## Recommended Next Action

Review [Synthesis is not error correction](../notes/synthesis-is-not-error-correction.md) to distinguish unfiltered merging from synthesis that explicitly adjudicates attached objections, using Colosseum as a design example while preserving the absence of an isolated error-correction result.
