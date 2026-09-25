---
description: "PrimeScientist tests budget-sensitive selection among research plans while charging planning and execution together; useful evidence for controller evaluation, bounded by fixed architecture and benchmark rewards."
source: https://arxiv.org/abs/2609.17846
captured: "2026-09-24"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: a193fec920c0d278fa22414992a16db3f4ee0c5837031e6845c0e8e247b73141
ingested: "2026-09-25"
type: kb/sources/types/ingest-report.md
domains: [autonomous-research, search-control, resource-allocation, learning-theory]
learning_claims: true
---

# Ingest: PrimeScientist: Strategic Allocation of Research Effort

## Classification

A research preprint introducing a formal decision problem, an agent architecture, benchmark comparisons, and allocation-policy ablations. Xinle Yu and coauthors list affiliations at UC San Diego and Johns Hopkins University. The authors report their own system's results; the paper includes prompts and an example plan modification, but this ingest does not independently reproduce the experiments.

## Summary

[PrimeScientist](https://arxiv.org/abs/2609.17846) allocates a shared inference-token budget between constructing research plans and executing them. A reflector retains competing Markdown plans, rationales, outcomes, and reconstructible modifications in a tree; a coding agent implements and tests selected plans. A supplied selection rule increasingly favors high-value branches as the remaining budget falls. Against AutoResearch's linear refinement loop, the complete framework raises mean FIRE-Bench F1 from 0.7018 to 0.7738 with 50.6% fewer executor invocations, using one GPT-5 search per configuration; this compares architectures, not just allocation schedules. Selection-only comparisons hold the executor, reflector, plan tree, pruning, and accounting fixed and favor the adaptive rule on average, with task-specific exceptions and only small repeated-search panels. The paper contributes a concrete way to evaluate search allocation while charging for planning. Its evidence concerns benchmark rewards and complete attempts under token budgets, not independently validated discoveries or total experimental compute savings.

## Quotes

No source quotes have been retained yet.

## Connections Found

The strongest role is empirical support for [evaluating a search controller by what it brings to stronger evaluation](../notes/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md). The internal comparisons change plan selection while retaining the surrounding architecture, then compare the best task rewards reached. They test routing by its downstream consequences without requiring exhaustive knowledge of unvisited branches. The GPT-5 experiment uses one search per configuration; the repeated GPT-5-mini experiment remains small. Neither comparison isolates the value of the plan representation or the reflector's diagnoses.

The decision formulation also gives [cost-sensitive theory search](../notes/cost-sensitive-formalisms-for-tentative-theory-search.md) a concrete comparison case: available plans, observed history, and remaining resources determine whether to generate alternatives or execute one. Both activities consume the budget. This operationalizes a budgeted decision process without establishing a complexity result or a benefit attributable to retained theories. FIRE-Bench supplies a further instance of [known-target discovery as reachability testing](../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md): its F1 evaluates agreement with established findings under supplied research questions and experimental requirements.

## Learning Claims (our opinion)

PrimeScientist adapts within a task through two mechanisms. Recorded outcomes update branch values and hence selection probabilities. Separately, the reflector reads scores, execution evidence, and earlier plans to propose revised hypotheses or experimental strategies. Its prompt requests a distinction between execution failure and a tested hypothesis yielding a low score, plus a concrete hypothesis, rationale, and risks for each proposed plan. The published learning-order example shows competing explanatory experiments being developed, pruned, and selected. These are meaningful mechanisms for changing subsequent research, beyond merely preserving a transcript.

Against the [theory-builder](../notes/definitions/theory-builder.md) conditions, the Markdown plans and rationales are localized content (condition 1), with separately editable sections and recorded modifications that give some [addressability](../notes/definitions/addressable-theory.md). The executor carries out what a plan says (condition 2). The reflector's stated diagnoses, which separate execution failure from a tested hypothesis, are criticism aimed at plan content, though branch values rank whole attempts by reward; condition 3 is shown by the prompt and one worked example. Condition 4 is met within a task: the reflector reads earlier plans and their evidence, and its revised hypothesis becomes the next attempt, which is tested again. PrimeScientist is therefore a theory builder at the grade of rounds within one run, at the strength of the prompt and one worked example. Nothing persists beyond the task: each tree answers one research question against fixed reference findings, and cross-task policy learning is future work. Whether the reflector's diagnoses improve later capacity is a separate learning claim that the outcome comparisons do not isolate.

Budget adaptation is a supplied schedule, not a learned allocation policy: the sampling exponent follows remaining resources, while the reflector and executor remain fixed. Cross-task policy learning and recursive improvement of research machinery are future directions. As in [learning within a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), plan selection improves within fixed complete-attempt actions, tree representation, pruning, and benchmark feedback. The ablations compare controllers inside that space; they do not establish that this space is preferable to other representations or to reallocating resources during an unfinished attempt.

## Extractable Value

1. **A controller comparison that includes the cost of choosing.** Holding the research framework fixed, the eight-task GPT-5 comparison reports mean maximum reward of 0.598 for adaptive selection versus 0.551 for UCT, 0.563 for Greedy, and 0.546 for Random. Each configuration has one search. This is a bounded empirical example for the downstream-controller note, rather than general evidence that adaptive selection or a plan tree is superior. [quick-win]
2. **Planning and execution compete for resources.** The paper makes plan generation a charged action; its reported token breakdown assigns 38% to planning, including reflection, tree context, and child generation. This gives the cost-sensitive search catalogue a concrete accounting method. The broader lesson is to price the work that produces alternatives alongside testing them; the percentage is specific to this implementation. [quick-win]
3. **Separate outcome quality, attempts, and resource dimensions.** In the repeated six-task GPT-5-mini AutoLab comparison, the full framework obtains similar mean reward to AutoResearch, 0.4363 versus 0.4359, with about 24% fewer attempts. Both planning and execution count toward the 1M-token budget. This offers a useful evaluation pattern for KB workflows, provided attempt counts remain distinct from total work and the framework comparison is not attributed solely to its schedule. [experiment]

## Limitations (our opinion)

**The strongest headline is a compound-treatment result.** AutoResearch lacks the reflector-proposed branching and tree pruning. Its comparison cannot identify which component caused the difference. The internal ablations isolate selection but keep those components fixed. The fixed-exponent comparison is more specific: with GPT-5-mini it varies whether the exponent adapts or stays constant, reporting three searches for the adaptive method and two for each alternative. The resulting population standard deviations are descriptive; they do not establish statistical significance or general superiority.

**Average gains conceal uneven effects.** The 10.3% FIRE-Bench gain is relative, not a percentage-point change. Removing its largest individual gain leaves means of 0.7533 versus 0.7266. On AutoLab, much of the overall reward advantage comes from one accuracy-gated task; the other seven average 0.5052 versus 0.5061. The appendix's matched-attempt table presents only the three improved cases from six. These results support contingent benefits rather than a uniform advantage.

**Fewer attempts do not establish lower total experimental cost.** Attempts can contain different training or benchmarking workloads. The token budget excludes CPU/GPU hours and elapsed time, and its final action may overshoot the threshold because cost is charged on completion. FIRE-Bench executes each PrimeScientist plan twice and keeps the higher score, charging both invocations; MLE-Bench counts only attempts producing valid scores. The separate twelve-search timing comparison reports means of 32 versus 42 minutes but the same 34-minute median. Resource dimensions and counting rules must travel with any efficiency claim.

**Search rewards leave scientific warrant unresolved.** FIRE-Bench rewards agreement with known findings; it does not test prospective choice and validation of unknown discoveries. Selecting the best observed reward can also favor evaluation noise or exploitation. Independent validation remains necessary, as the authors acknowledge. Reconstructing a plan through its stored modification establishes its lineage, not the correctness of the scientific rationale. No implementation was inspected or executed for this ingest, so outcomes and operational behavior remain paper-reported.

## Recommended Next Action

Update [A search controller is tested by what it brings to stronger evaluation](../notes/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md) with the selection-only comparison as a bounded empirical example, preserving its fixed architecture, charged planning cost, and limited repetitions.
