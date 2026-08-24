---
description: "RECV's forced binary verifier confounds inference type with response policy, content, and prompt bundles"
source: https://aclanthology.org/2025.findings-acl.1059.pdf
captured: "2026-08-20"
capture: pdf-read
genre: scientific-paper
snapshot_sha256: ac51d6384fc9aae49225bf9b28a0ec0f0043a6d2d45e85cb07325250ab8ae93e
ingested: "2026-08-20"
type: kb/sources/types/ingest-report.md
domains: [llm-evaluation, claim-verification, reasoning, rationale-faithfulness]
---

# Ingest: Assessing LLM Reasoning in Evidence-Based Claim Verification

## Classification

A Findings of ACL 2025 paper that defines a reasoning taxonomy, constructs an annotated benchmark, compares prompting conditions, and reports statistical and rationale evaluations.
Author: John Dougrez-Lewis, Mahmud Elahi Akhter, Federico Ruggeri, Sebastian Löbbers, Yulan He, and Maria Liakata are affiliated with the University of Warwick, Queen Mary University of London, the University of Bologna, King's College London, and the Alan Turing Institute. Peer review and detailed appendices are positive signals, but the experiments were not independently reproduced for this ingest.

## Summary

Dougrez-Lewis et al. introduce the RECV framework, which distinguishes deductive, abductive, inductive, and analogical inference, then operationalize only deduction and abduction in a 1,500-item claim-verification benchmark drawn equally from VitaminC, CLIMATE-FEVER, and PHEMEPlus. They evaluate Claude 3 Sonnet, GPT-4, and GPT-4o under zero-shot and manual chain-of-thought prompts, with and without generated rationales. Across the tested configurations, items annotated as abductive have much higher error rates than items annotated as deductive: 32% versus 10.31% on VitaminC, 48.58% versus 15.58% on CLIMATE-FEVER, and 44.68% versus 20.06% on PHEMEPlus. Rationale generation and chain-of-thought have heterogeneous effects, sometimes helping on VitaminC and often hurting on the more complex datasets or abductive subsets. Generated rationales can remain similar to selected human explanations even when verdicts are wrong. The paper therefore establishes a substantial within-RECV performance gap and useful prompt sensitivity results, but it does not identify inference type as the cause of that gap or show that the generated rationales faithfully report the models' decision process.

## Claims

No claims have been grounded yet.

## Connections Found

RECV is most useful to this KB as a benchmark-design case and a bounded empirical anchor. Its reasoning label is not the same variable as [claim modality](../notes/claim-modality-is-the-inference-form-of-the-refuter.md): RECV labels the route thought necessary to reach a supplied verification verdict, whereas local claim modality names the inference form available to a refuter. The benchmark also asks models to produce verdicts and explanations rather than [evaluate a submitted piece of reasoning](../notes/reasoning-production-is-not-reasoning-evaluation.md). Even the term *abduction* is construct-dependent: [CEDAR-GRPO](./cedar-grpo-process-aware-rl-abductive-reasoning.ingest.md) evaluates hypothesis generation and selection, while RECV forces a binary verdict from a supplied claim-evidence pair.

The result should be read through the KB's [fixed-decomposition boundary](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), [contrast-identification rule](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md), and [claim-granular warrant rule](../notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md). Models can vary their token-level rationale and verdict, but the taxonomy, evidence, sampling rules, response space, prompts, datasets, and evaluators remain fixed. The experiment therefore warrants comparisons among those fixed cells, not validation of each fixed choice or causal attribution to deduction versus abduction.

RECV's reversing prompt effects evidence the limit that [structured-prompt gains do not establish training-distribution selection](../notes/structured-prompt-gains-do-not-establish-distribution-selection.md) and diagnose [prompt variation as brittleness measurement](../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md). Its prompt arms bundle persona, demonstrations, step-by-step wording, rationale requirements, and output shape, so their effects cannot identify one structural mechanism. The controlled content manipulations in [Lampinen et al.](./language-models-like-humans-show-content-effects-on-reasoning.ingest.md) show what RECV lacks when it compares inference labels across different evidence and domains. Its rationale results are likewise a negative case for [requiring faithful rather than merely legible rationales](../notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md): reference similarity and surface quality do not establish causal faithfulness.

## Extractable Value

1. **A benchmark's response policy is part of the capability it measures** -- RECV removes `unverified` cases and requires `SUPPORTS` or `REFUTES`, even though its abductive construct is defined by partial evidence and uncertain conclusions. That policy can convert warranted abstention into an apparent reasoning error. This is a transferable benchmark-design claim not yet stated directly in the KB. [quick-win]

2. **Taxonomy validation and within-taxonomy performance require separate experiments** -- a large error difference between fixed deductive and abductive labels does not show that the two-class taxonomy is complete, consistently applied, or causally responsible for the difference. The distinction generalizes to any evaluation built on expert-assigned latent-process labels. [deep-dive]

3. **Reasoning benchmarks need orthogonal factors** -- RECV shows why inference construct, production-versus-evaluation role, semantic content, evidence sufficiency, response space, prompt structure, and rationale faithfulness should be varied or bounded separately. Collapsing them yields a capability headline whose component causes cannot be recovered from the result. [deep-dive]

4. **A response-space ablation would test the strongest alternative explanation** -- rerunning the same claim-evidence pairs with an `INSUFFICIENT EVIDENCE` or calibrated-abstention option would reveal how much of the reported abductive gap comes from forced commitment rather than an inability to compare explanations. The existing benchmark supplies a concrete starting dataset for this experiment. [experiment]

5. **Structured prompting has local, not monotonic, value** -- rationale and chain-of-thought conditions help some VitaminC cells but often hurt CLIMATE-FEVER, PHEMEPlus, and abductive cells. This is a useful boundary case against treating more explicit reasoning structure as uniformly beneficial. [just-a-reference]

6. **Reference-like explanations can coexist with decision failure** -- RECV's generated rationales sometimes resemble selected human rationales despite incorrect verdicts, while the paper itself concedes that explanations may be plausible post-hoc accounts. This is a compact worked example of why surface rationale metrics cannot certify faithful reasoning. [quick-win]

## Limitations (our opinion)

The fixed decomposition is the main interpretive limit. The model receives a claim, supplied evidence, a prompt and persona, and sometimes demonstrations. It can emit a rationale and one of two verdicts. It cannot retrieve more evidence, abstain, enumerate and test a hypothesis set, or revise the task decomposition. The learnable mapping is whatever the three fixed proprietary models and prompt arms already express. Outside that effective evaluation space are the deduction/abduction taxonomy, removal of the neutral class, sampling thresholds, dataset partitions, evidence sufficiency, prompt bundles, model versions, judges, and metrics. Performance inside this setup cannot validate those choices.

The deduction/abduction construct is not independently secure. Annotators were shown the known veracity label before assigning a reasoning route and writing a rationale, which permits a post-hoc label for how the supplied answer might be reached. Agreement falls from 0.90 in the 90-item preliminary study to 0.75, 0.56, and 0.67 on the overlapping portions of the three benchmark datasets. The abductive cells are also small and imbalanced: 29 of 500 VitaminC items, 102 of 500 CLIMATE-FEVER items, and 36 of 500 PHEMEPlus items. Definitions and examples shift between the main text and appendices, and some examples import unstated background assumptions. These issues limit the claim that RECV measures two stable atomic reasoning capabilities.

Inference type is confounded with content and difficulty. Candidate items for the two labels were sampled using different semantic-similarity heuristics. The datasets differ in domain, label balance, evidence source, and mean evidence length, while the annotated groups are not matched on those variables. Mann-Whitney comparisons can establish different error distributions within the resulting benchmark, but they cannot isolate reasoning type as their cause. The paper reports many cell-wise significance tests without a multiple-comparison correction, further weakening fine-grained attribution.

The prompt comparisons are bundled rather than factorial. Persona, examples, step-by-step wording, explanation requirements, and output shape vary across arms, so a change cannot be assigned uniquely to chain-of-thought or rationale generation. The appendix does not preserve a clearly distinct no-explanation prompt, and the paper does not report temperature, seed, repeated-run variance, or dated API model identifiers. The full paper was inspected, but no model calls, code, or data pipeline were executed; all outcome claims remain paper-reported rather than independently reproduced.

The rationale study does not test causal faithfulness. Its 100 items per dataset are restricted to cases where at least three model configurations were wrong, so the results describe a hard, error-enriched cohort rather than RECV as a whole. Human rationales were screened for readability and coherence, and the automatic metrics measure consistency, evidence appropriateness, reference similarity, and fluency. None intervenes on the stated rationale to see whether the verdict follows it. The reported metric formulas and stated score directions are also difficult to reconcile. These results support claims about surface resemblance only.

Generality is limited to three proprietary model families and three claim-verification datasets at a 2023--2024 model-generation snapshot. There is no human verifier baseline, open-model comparison, abstention baseline, retrieval condition, or evaluation of inductive and analogical cases. Finally, the text snapshot preserves all prose, tables, appendices, and figure captions but not the raster figure bodies, so diagram-only details were not assessed here.

## Recommended Next Action

Write a note titled **A forced verdict can turn warranted abstention into apparent reasoning failure** in `kb/notes/`, using RECV's removal of `unverified` cases and binary response space as the worked case and treating response policy as a fixed part of the evaluated capability.
