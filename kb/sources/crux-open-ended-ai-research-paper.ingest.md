---
description: "CRUX shadow evaluations document research critique that fails to redirect projects, separating local correction from project-level learning under a bounded expert-review protocol."
source: https://arxiv.org/abs/2607.27191
captured: "2026-09-24"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 9d716c573c4bbe22a21b18604e2e03e23d0b1185e7d7bef977efe75b9a621db9
ingested: "2026-09-24"
type: types/ingest-report.md
domains: [agent-evaluation, scientific-discovery, learning-theory, context-engineering]
learning_claims: true
---

# Ingest: Can AI agents conduct open-ended AI research? Early evidence from two case studies

## Classification

A scientific paper reporting an evaluation method, two research case studies, pilot runs, one robustness run, trajectory analysis, and original-author reviews. The captured paper identifies itself as arXiv v2 and includes the research questions and expert reviews in appendices.

Author: Peter Kirgis, Sayash Kapoor, and the CRUX collaboration, including the original researchers whose questions supplied the tasks. Their close subject expertise strengthens the diagnosis of specific research defects. They also helped construct the evaluation and knew the outputs were AI-generated; their expertise is not independent, blinded assessment.

## Summary

CRUX introduces **shadow evaluation**: give an agent a research question from an unpublished paper, withhold the paper and findings, and have the original authors judge whether its output advances the question. Two main Opus 4.8/OpenClaw runs received six days, $3,000 each in API credits, separate GPU budgets, research tools, subagents, and AI reviewers. The agents completed the research engineering, with disclosed human logistical and scaffold interventions, but original-author reviewers scored the resulting Personas and TabPFN papers 2/6 and 1/6. The trajectories show local experimental corrections alongside early commitment to weak research directions; repeated reviews often identified serious defects without prompting a project restart. A TabPFN robustness run jointly changing model and scaffold to GPT-5.6 Sol/Codex reproduced many failures, while exhausting its API budget much earlier. These are failures of the tested systems under supplied questions, a required conference-paper deliverable, and expert grading; the comparison does not isolate a model limitation or test alternative research decompositions.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper is a bounded empirical witness for [a failure explanation becoming search control only when it changes a later branch decision](../notes/failure-explanation-changes-later-branch-decisions.md). AI reviews identified many concerns later emphasized by experts, yet the agents often responded with qualifications and minor repairs rather than reconsidering their central approach. This does not make all critique inert: stronger follow-up experiments and corrections also occurred. The distinctive failure concerns the scale and priority of the response.

It also bears on [backtracking keeping lightweight search control provisional](../notes/backtracking-keeps-lightweight-search-control-provisional.md). Fresh-context workers were available and used for other tasks, but rarely used to restart research. Tool availability therefore did not establish an operative project-level return path in these runs. Because the experiment did not compare restart policies, it does not show that a particular backtracking design would have succeeded.

Shadow evaluation offers a comparison with [known-target discovery benchmarks](../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md): a hidden paper supplies a worthwhile question and expert evaluators, while grading concerns research value rather than recovery of its specific answer. Problem selection remains supplied, and evaluation remains expensive and non-blind. The [earlier CRUX web-report ingest](./can-ai-agents-conduct-open-ended-ai-research.ingest.md) describes the same study; the paper is another captured representation, not independent replication evidence.

## Learning Claims (our opinion)

The source studies agents that propose hypotheses, execute tests, consume reviews, and revise experiments and manuscripts. Their research state includes project files, logs, experiment results, and reviewer feedback. The learning relevant here concerns how that process changes subsequent research decisions; training the models used as experimental subjects is a separate activity.

Against the four conditions of a [theory builder](../notes/definitions/theory-builder.md), the trajectories meet all four at the strength of the paper's trajectory analysis. Hypotheses, experiment plans, results, and manuscript claims are stated in project files and drafts (condition 1), and they guide which experiments run and what is written (condition 2). AI reviews criticize what particular claims say, and some criticisms changed later action: agents strengthened tests, caught statistical errors, and retired unsupported claims (condition 3). Retention (condition 4) is met because each run pursues a sequence of different experiments over six days, and later experiments consume the stated results and reviews of earlier ones; the unit is the problem, not the run. The system boundary includes the agents, subagents, and AI reviewers. Human bug repairs, deadline extension, and readability requests are interventions from outside that process.

Learning is a separate claim, and the paper does not establish it. It shows no general improvement in research capacity caused by retaining and criticizing these formulations, and the central failure is that criticism rarely redirected a project. Rejected final papers do not show that no local learning occurred. The evidence supports distinguishing detecting a defect, making a local correction, redirecting the investigation, and improving the eventual result.

The agents could change hypotheses, datasets, code, experiments, and drafts; they could also delegate work with fresh context. This broad action space makes failure to restart informative, but does not prove that the required correction was outside their effective update space. As [learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) requires, keep the fixed layer separate: human-selected questions, a mandatory paper with no abstention option, resource budgets, reviewer construction, and much of the protocol survived the model/scaffold substitution. The study leaves open whether better use of existing operations, different research instructions, different state representations, or stronger models would change the outcome. It supplies a case for testing criticism's effect on decisions, not evidence to revise the theory-builder definition.

## Extractable Value

1. **A concrete witness for the critique-to-decision requirement.** In two main runs, major concerns appeared in self-reviews and final expert reviews, yet project direction remained largely fixed. Local correction must remain visible when using this evidence: the failure was insufficient redirection, not total disregard of feedback. This gives the existing branch-decision note a specific empirical case. [quick-win]

2. **Separate restart capability from restart behavior.** Clean-context delegation and remaining resources did not induce effective project-level backtracking. An evaluation of research workflows can record which criticism led to a new experiment, a revised premise, abandonment, or only a prose edit. The source motivates such measurement; it does not establish the best restart rule. [experiment]

3. **Expert evaluation can preserve an open answer space.** Withholding an unpublished paper while using its authors to assess progress avoids reducing success to answer similarity. This complements the KB's account of known-target discovery, while retaining human problem selection and a costly evaluator outside the agent's routine review loop. [quick-win]

4. **Budget failures can reverse under a compound system change.** The main runs used less than half their API credits; the Codex run exhausted the same $3,000 allowance in just over two days, leaving nearly 100 hours. Both returned weak work. Resource visibility and automatic continuation therefore did not suffice in these configurations, and the joint model/scaffold change does not identify which component caused either allocation pattern. [just-a-reference]

## Limitations (our opinion)

The study provides detailed cases, not a population estimate. Two selected empirical ML questions, two weaker pilots, two main runs, and one robustness run cannot establish general incapacity for open-ended research. Original authors spent much longer on their papers, and there is no matched human arm under the agents' resource constraints. The authors' prediction that additional weeks would not help is an interpretation of the trajectories, not a tested duration effect. Nor does failure on these tasks establish that open-ended research is the limiting factor in AI R&D acceleration.

Original-author review supplies unusually specific expertise but can favor the authors' framing. The evaluators knew the papers were AI-generated, and the core team discloses prior skepticism about imminent recursive self-improvement. The included reviews support the narrow rejection judgments, but an independent blinded arm is absent. Uniform rejection of the agents' drafts also cannot establish that AI reviewers discriminate acceptable work from unacceptable work; no acceptable comparison set was tested.

The robustness run changes model, scaffold, continuation behavior, and resource use together. It weakens an explanation confined to one OpenClaw defect, without isolating creativity, reasoning, memory, feedback prioritization, or protocol design as the cause. The no-abstention paper requirement could encourage exhaustive negative-result writing after early hypotheses fail. Available restart tools do not exclude an orchestration or instruction problem.

Human involvement matters when interpreting autonomy. Humans repaired a reasoning-signature bug, supplied logistical setup, extended the original deadline by 24 hours, and requested readability rewrites. The bug caused five context resets in Personas and fourteen in TabPFN. Engineering success therefore refers to the agents' substantive research work within this supported trajectory. This ingest evaluates the paper and its included reviews; it does not independently reproduce the experiments or inspect the released code and raw logs. The paper also says one study's detailed logs and generated manuscript remain undisclosed while its original research is unpublished.

## Recommended Next Action

Update [A failure explanation becomes search control only when it changes a later branch decision](../notes/failure-explanation-changes-later-branch-decisions.md) with the CRUX case, distinguishing observed local corrections from failed project-level redirection and retaining the two-task, compound-system evidence boundary.
