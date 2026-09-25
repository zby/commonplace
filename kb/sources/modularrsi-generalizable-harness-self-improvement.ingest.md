---
description: "ModularRSI evolves restricted harness modules using trajectory contrasts; held-out transfer supports the compound method, while integration and budget differences limit claims about modularity."
source: https://arxiv.org/abs/2609.14857
captured: "2026-09-24"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 7186fff4f0dba1c268db1c74553262e85bb8dfd05e4f84ba78551e36191150f5
ingested: "2026-09-25"
type: ingest-report
domains: [agent-harnesses, learning-theory, evaluation]
learning_claims: true
---

# Ingest: ModularRSI: Modular and Generalizable Recursive Harness Self-Improvement

## Classification

A research preprint reporting a harness evolution method, a curated task pool, benchmark evaluations, and controlled comparisons. Siwei Wu and colleagues list affiliations with Beihang University, the University of Manchester, IQuest Research, M-A-P, Langboat, and Hohai University. The evidence is the authors' account of their own system; this ingest does not independently reproduce it.

## Summary

[ModularRSI](https://arxiv.org/abs/2609.14857) improves a Terminus-2 harness by comparing successful and failed executions of the same task, pooling diagnoses across tasks, and independently evolving five supplied modules: Agent Loop, Tool Use, Observation Management, Context Management, and Task Completion Detection. An integration stage repairs interactions before freezing the function library for evaluation; a task-conditioned composer still selects functions at runtime. The authors curate 2,000 tasks independently of benchmark instances, with benchmark categories guiding construction, and use 120 tasks per source subset for main evolution. Within this fixed architecture and compound procedure, reported DeepSeek-V4-Flash-Preview accuracy rises from 47.57% to 52.43% on TerminalBench 2.0 and from 73.40% to 76.45% on SWE-Bench Verified under in-domain evolution; smaller gains transfer across the two domains and to other inference models. These results support reusable harness changes in the tested settings. They do not isolate contrastive diagnosis or establish that these five boundaries are preferable: the main modular comparison also varies aggregate evolution work, and no alternative modular decomposition is tested.

## Quotes

No source quotes have been retained yet.

## Connections Found

The source is a useful comparison for [localized retention and bounded impact](../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md). Its function-scoped edits make repair locations explicit, but independently evolved modules still need integration because their effects overlap or conflict. The reported gains arise from the full procedure within supplied module boundaries; they do not measure dependency closure or establish that restricted edits reduce the required validation scope. The source therefore illustrates the note's distinction between a small edit and a small behavioral impact, without testing its general cost claim.

It also compares with [HarnessEvolve](./harnessevolve-reference-trajectories.ingest.md) on successful-versus-failed trajectory diagnosis. ModularRSI uses repeated executions and historical successes of the same task, rather than answer-conditioned reference generation, and prioritizes proposals supported by distinct tasks. Unlike HarnessEvolve's reference-removal comparison, it has no dedicated contrast-removal ablation. Its contribution here is a specified diagnostic workflow and transfer evidence for the compound method, not independent evidence that contrastive analysis causes the gains.

## Learning Claims (our opinion)

The source's learner retains executable function variants, their natural-language descriptions, function revision histories, and rewarded task trajectories. The trajectories supply evidence; cross-task diagnoses propose behavioral changes; accepted functions alter later execution. All-fail tasks can retrieve an earlier success for comparison or receive single-sided diagnosis. All-success tasks are examined for wasted work. This broadens the improvement signal beyond current failures, while keeping the final task evaluator separate from model-authored explanations.

Against the [theory-builder definition](../notes/definitions/theory-builder.md), conditions 1 and 2 are met: module functions and their descriptions are stated units, and accepted functions alter later execution. Condition 3 is met as described. Structured findings state a divergence, a proposed counterfactual effect, and whether a repair fits the permitted module; diff review challenges the connection between the change and the evidence, including task-specific overfitting. Condition 4 is met within a run: accepted functions and their revision histories are the starting point of later epochs, where new diagnoses revise them again. ModularRSI is therefore a theory builder at the grade of rounds within one run. The library is then frozen; held-out, cross-domain, and cross-model evaluation reuse that product, which ends the builder rather than extending it. As a separate learning claim, the benchmark results support improved capacity for the overall procedure. They do not establish that its individual causal explanations are correct or that criticism, rather than another component, accounts for the improvement.

The system gives proposed repairs [addressability](../notes/definitions/addressable-theory.md) through named modules, functions, and revision histories. Addressability here supplies candidate repair locations, not unique causal attribution. The diagnosis prompt explicitly permits finding a problem that requires an architecture change while marking it unfixable in the current scope. This exposes the boundary described by [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md): module code can change, but the supplied interfaces, infrastructure exclusions, diagnosis procedure, and retention gates constrain evolution. Integration permits interaction repairs within this architecture; it does not search alternative architectures. Downstream composition uses the frozen library rather than revising it. The paper supports learning within these boundaries and leaves their comparative adequacy open; it supplies no reason to revise the theory-builder definition.

## Extractable Value

1. **Separate edit locality from integration work.** Independently evolving restricted modules can still produce conflicting behavior. ModularRSI's integration stage provides a concrete companion to the localized-retention note's warning that validation scope need not match edit scope. Its performance comparison does not isolate locality's effect or compare alternative boundaries. [quick-win]
2. **A benchmark-disjoint transfer protocol.** Independently constructed evolution instances, similarity screening, a frozen function library, and cross-domain and cross-model evaluation make reuse more testable than evolution on benchmark instances alone. The reported gains concern this complete procedure within the supplied architecture; benchmark categories still guide task construction, and runtime function selection remains adaptive. This is a reusable evaluation pattern for KB-method changes, not direct evidence that it will improve them. [experiment]
3. **Diagnosis can abstain or expose an unavailable repair.** The structured findings distinguish a plausible module repair, a problem requiring architecture change, and no supported attribution. Cross-task voting then prioritizes recurring proposals rather than the most vivid single failure. These are inspectable candidate practices for review-driven KB revision, although their individual benefits are not ablated. [experiment]

## Limitations (our opinion)

The principal modular comparison combines independent scope restriction, five three-epoch evolution runs, and integration, whereas joint and non-modular evolution use three epochs. Single-module variants improve over baseline, but that does not remove the full treatment's aggregate-budget difference. A separate comparison gives AHE and Meta-Harness 16 epochs to match aggregate rounds and favors ModularRSI; it uses DeepSeek-V4-Flash-0731 and disables web search, so its 61.79% baseline should not be mixed with the main tables' 47.57%. Matching rounds also does not establish equal token or execution cost. None of these comparisons identifies the best module partition.

The authors acknowledge the absence of an isolated contrastive-analysis ablation. Fewer mixed-success tasks could reflect multiple changes in outcomes; it is not proof that inferred causes were repaired. Later case traces show intended behavior and successful results, but also contain other updates. The medium-centered versus hard-and-easy task comparison changes the experience distribution; its 76.45% versus 74.25% result does not isolate access to contrasts from other properties of that distribution. A simpler account consistent with the evidence is that additional structured search and broadly useful execution checks improve performance, even when some diagnoses are wrong.

Retention gates should not be read as proof of behavioral improvement. Program checks test structural validity; model diff review assesses effectiveness and overfitting; execution validation runs two sampled batch tasks to detect runtime or protocol errors. The described execution gate does not require a reward increase or demonstrate non-regression across earlier tasks. Review is performed by the Code-Modify Agent, with no reported independent calibration of causal attribution or overfitting judgments.

Three downstream rollouts per task assess inference variability, not uncertainty across independent evolution runs. The two benchmarks and tested model transfers bound the generalization claim to related software and terminal work. Main evolution uses small subsets of the released pool, and category-guided construction limits any claim of domain independence. No implementation was inspected or executed for this ingest.

## Recommended Next Action

Update [localized retention and bounded impact](../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md) with ModularRSI as a bounded example of restricted edits requiring cross-module integration, keeping the unmeasured validation scope and unequal main-comparison evolution budgets beside the example.
