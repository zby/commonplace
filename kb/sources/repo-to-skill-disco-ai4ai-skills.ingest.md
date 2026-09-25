---
description: "DisCo turns sources and task feedback into checked skill graphs; benchmark gains concern separately prepared skills, while PassNet supplies a concrete case of repairing an overbroad rule."
source: https://arxiv.org/abs/2609.02749
captured: "2026-09-24"
ingested: "2026-09-25"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 8ea10c5161292fe87f5de64a45084940bafdbdb561239582e91b3cdb4775b866
type: types/ingest-report.md
domains: [agent-skills, context-engineering, deploy-time-learning, evaluation]
learning_claims: true
---

# Ingest: Repo-To-Skill: Distilling GitHub Repositories Into AI4AI Skills

## Classification

A scientific preprint reporting a skill-construction method, a released collection, and controlled benchmark comparisons. Jianlyu Chen and coauthors, affiliated with BAAI, USTC, Renmin University, and Hong Kong Polytechnic University, describe their own DisCo agent and AREX-Skill Library. This is first-party experimental evidence, not an independent evaluation of the collection.

## Summary

DisCo constructs reusable operating guidance by selecting capabilities, grounding them in sources, packaging them as linked skills, and checking and repairing the result. Skills contain procedures, references, and optional executable helpers; agents load relevant branches through progressive disclosure. The paper reports 5,353 skills from 1,000 repositories, routed through 20 areas and 178 capability families. Its four outcome evaluations use separately constructed task- or target-conditioned skills, with GPT-5.5, Codex, and downstream execution budgets held fixed: MLE-bench Any-Medal rises from 31.11% to 72.89%, PaperBench replication from 29.45% to 39.59%, FrontierCS score from 70.63 to 77.14, and PassNet AS Score from 1.343 to 1.5313. Preparation is separate from downstream execution. These comparisons support the prepared skill packages in those settings; they do not evaluate the entire repository library or isolate verification, graph structure, or routing as the cause.

## Quotes

No source quotes have been retained yet.

## Connections Found

The PassNet appendix supplies a concrete reported case for [stating where a lesson stops](../notes/abstract-an-experience-only-when-you-can-state-the-boundary.md). An absolute warning against replacing vendor-optimized operators caused an agent to abandon a promising convolution rewrite it had recognized. The authors changed the warning into a default that graph structure and evaluator evidence could override. The trajectory supports a diagnosis of overbroad guidance; the paper does not separately measure that edit's benefit.

DisCo also provides a useful comparison with [authority earned per operation](../notes/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md). Repository checks distinguish skill gaps, native failures, and skipped checks; paper-derived skills receive module checks and bounded recovery tests. Each establishes a different claim. The four downstream improvements concern separately constructed benchmark skill packages under a fixed agent setup, so they cannot confer uniform task-level authority on every library skill.

Compared with [Machine Studying](./machine-studying.ingest.md), the consequential distinction is what preparation already knows. Machine Studying excludes downstream task information. Here MLE-bench construction explores each competition, PaperBench source selection uses target-paper context, FrontierCS refines a shared graph on development problems, and PassNet uses training instances. Excluding target solutions is narrower than preparing without target information.

## Learning Claims (our opinion)

DisCo changes retained skills while leaving model weights unchanged. Its construction mechanisms range from source inspection and API checks to execution-feedback revision. In MLE-bench, each revision receives the previous skill, summarized logs, and result analysis. FrontierCS compares candidate revisions against both a no-skill baseline and the preceding graph, then uses trajectories to locate faulty guidance. PassNet similarly revises provisional procedures from paired task runs. Freezing the resulting graph for evaluation tests its later use; the construction process is where the retained guidance changes.

Against the [theory-builder definition](../notes/definitions/theory-builder.md), conditions 1 and 2 are met: skills are stated procedures and applicability conditions, and a loaded skill changes the agent's decisions. The PassNet warning is a clear case of condition 3: a stated rule affected a decision, a reported counterexample challenged its scope, and the rule was revised; the authors made that edit, so the builder's boundary includes them for that operation. Its separately editable applicability condition illustrates [addressable theory](../notes/definitions/addressable-theory.md). Condition 4 (iteration) is met: each MLE-bench revision takes the previous skill with the analysis of its results, FrontierCS revisions are located from trajectories and compared with the preceding graph, and the revised PassNet rule is carried into later use. The construction process is therefore inside the term, human-staffed for the PassNet edit. The persistence grade reached is across the rounds of one construction run for one benchmark target; MLE-bench preparation explores the same competitions later scored. The released repository library is a handed-off product, and freezing it ends the builder; the paper does not show it or its check records taken up in later work on other problems. As a separate learning claim, the four comparisons support the prepared packages in their settings, but the isolated repair's effect remains unmeasured, and aggregate package gains do not attribute improvement to criticism of that rule.

The update space includes procedures, applicability conditions, interfaces, supporting scripts, and graph links. The source reports changing FrontierCS's initial monolithic workflow into a routed graph, so graph organization is not wholly fixed during construction. Nevertheless, the main outcome comparisons hold the model, harness, task interfaces, graders, and skill delivery mechanism fixed. Following [the fixed-decomposition distinction](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), success within this setup does not establish the superiority of skills over alternative representations or of the repository taxonomy over alternative retrieval designs. The source adds concrete learning procedures and a scope-repair case; it does not require changing the theory-builder definition.

## Extractable Value

- **An operational warning can suppress an exception the agent already sees.** The PassNet case locates failure in a rule's excessive force, rather than missing knowledge of an optimization. Preserve it as a reported case of repairing scope, without assigning the benchmark gain to that edit. [quick-win]
- **Verification should state which operation was checked.** Repository-native execution, static integrity checks, module smoke tests, source-code-free recovery, and downstream performance support different uses. DisCo's explicit native-failure and skip categories offer a practical comparison for retaining check boundaries instead of a single undifferentiated verification label. [quick-win]
- **Prepared context can improve a fixed research agent, with a separate preparation bill.** The four comparisons establish effects of benchmark-specific skill packages under matched downstream budgets. MLE-bench allows up to 24 GPU-hours per task for exploration and another 24 for running. This is evidence for separately accounting for preparation and consumption, not measured amortization across unseen tasks. [experiment]
- **Recovery can test whether extracted guidance carries enough of its source.** Paper-derived skills undergo bounded reconstruction without reopening the original implementation repository. This is a reusable test design for source-to-procedure conversion, although success on a bounded mechanism cannot establish full-paper reproducibility. [experiment]

## Limitations (our opinion)

The primary evidence is the paper; no implementation was inspected or executed for this ingest. Its broad description of a verified library must be read through the narrower checks in Appendix A.1. Static integrity and selected safe native checks leave untested workflows and unresolved gaps. The benchmark interventions are separate collections and cannot establish quality across all 5,353 repository skills.

The main comparison bundles source selection, preparation trials, skill content, and its delivery. There is no matched ablation of verification, linked versus unlinked skills, or alternative taxonomies. The claim that operational knowledge forms a distinct third layer is a useful accounting choice; the experiment does not prove that domain guidance must sit outside a harness or cannot already reside in model priors.

Matched running budgets do not equal matched total compute or realized usage. FrontierCS increases average tokens from 2.46M to 4.47M and tool calls from 64.7 to 105.0. Near-zero correlations between additional usage and gains do not substitute for a controlled resource ablation. Public leaderboard comparisons also vary model and harness. PaperBench regresses on two tasks, and PassNet's Fast_1 metric falls despite improved aggregate score and correctness; assistance is not uniformly beneficial.

Preparation boundaries limit transfer claims. MLE-bench explores the same tasks later scored, PaperBench selects sources from target context, and the two other graphs use benchmark development or training feedback. The paper does not clearly establish disjointness between FrontierCS development problems and all reported evaluation tasks. These protocols should not be read as demonstrations of corpus-only preparation or unselected future-task transfer. The PassNet convolution explanation is the authors' diagnosis, and no isolated post-edit result establishes the revised warning's effect.

## Recommended Next Action

Update [Abstract an experience into a lesson only when you can state where the lesson stops](../notes/abstract-an-experience-only-when-you-can-state-the-boundary.md) with the PassNet warning case as a reported scope repair, retaining the absence of an isolated post-edit outcome.
