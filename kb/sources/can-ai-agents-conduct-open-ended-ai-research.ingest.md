---
description: "CRUX shadow evaluations expose a gap between autonomous research engineering and open-ended judgment while supplying an expert-oracle design for uncontaminated tasks."
source: https://cruxevals.com/crux/can-ai-agents-conduct-research/
captured: "2026-08-06"
capture: web-fetch
genre: scientific-paper
snapshot_sha256: 24132cf17ad499684f2059ccff4dccc6ecd8d3959a7e728b01589352a124b628
ingested: "2026-08-06"
type: kb/sources/types/ingest-report.md
domains: [agent-evaluation, scientific-discovery, oracle-theory, context-engineering]
---

# Ingest: Can AI agents conduct open-ended AI research?

## Classification

A full experimental report with a stated evaluation method, two case studies, pilot and robustness runs, expert reviews, trajectory analysis, collaborator survey, appendices, and released artifacts.

Author: a 24-author CRUX collaboration that includes the core evaluation team and authors of the two original NeurIPS submissions. The original authors supply unusually strong task-specific expertise, and the report releases reviews, repositories, logs, and telemetry. They are not independent evaluators: they helped formulate the questions, knew the papers were AI-generated, had their own solutions in mind, and the core team discloses prior skepticism about imminent recursive self-improvement.

## Summary

CRUX introduces **shadow evaluation** for open-ended AI research: give an agent the central question from a high-quality unpublished paper, withhold the paper and its findings, then have the original researchers grade the output as a conference submission. Claude Opus 4.8 on OpenClaw received six days, $3,000 in API credit, GPU compute, a VM, the web, subagents, and AI review tools for each of two NeurIPS 2026 questions. The agents autonomously completed literature review, engineering, experiments, and paper production, but the original authors scored the papers 2/6 and 1/6. Log analysis attributes the failures to weak judgment about publishable evidence, uncreative responses to design problems, ineffective project-level backtracking, poor resource awareness, and instruction drift. A GPT-5.6 Sol Ultra/Codex robustness run on one question reproduced most failure modes while consuming its budget differently. The result is early evidence for an engineering/judgment split, not a general measurement of all AI research capability.

## Connections Found

This source is a bounded empirical anchor for [Automating KB learning is an open problem](../notes/automating-kb-learning-is-an-open-problem.md) and [The boundary of automation is the boundary of verification](../notes/the-boundary-of-automation-is-the-boundary-of-verification.md): extensive autonomous execution coexisted with failure on hypothesis selection, evidence calibration, substantive reframing, and knowing what to abandon. It supplies the observed cases that the earlier [When code is free, research is all that matters](./when-code-is-free-research-is-all-that-matters-2031072399731675.ingest.md) source lacked.

Its most distinctive role is methodological. Relative to [known-target discovery benchmarks](../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md), shadow evaluation keeps an authentic question uncontaminated without scoring similarity to a known answer. Relative to blind peer review, it buys deeper question-specific expertise at the cost of non-blind judgment and small samples. The runs also provide unusually direct evidence for [context-to-action failure](../notes/knowledge-storage-does-not-imply-contextual-activation.md): AI reviews often identified the same major weaknesses as the human experts, yet the agents mostly narrowed claims or added caveats instead of changing the project-level plan.

The experimental interpretation rests on [the effective-update-space distinction](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md). The robustness run varies model and scaffold together, while the selected questions, paper-shaped objective, budgets, evaluator construction, and much of the surrounding protocol stay fixed. Reproducing the outcome bounds a simple one-scaffold explanation; it does not identify the failing component or validate the fixed research decomposition.

## Extractable Value

1. **Shadow evaluation is a third oracle construction for open-ended work.** It combines an authentic unpublished question, no access to the original findings, and reviewers with months of exact-domain experience. Unlike target-reconstruction benchmarks, success is not answer similarity; unlike ordinary blind review, evaluation is deep and task-specific. The transferable method is to hold back a live expert task, let an agent attempt it independently, and have the task owners judge whether the output advances the work. [deep-dive]

2. **Correct critique can remain behaviorally inert.** Across fifteen self-review rounds, the agents never received an acceptance, and their reviews surfaced many concerns later emphasized by the human experts. The agents nevertheless treated central soundness problems as requests for caveats and narrower claims. This strengthens the context-to-action account: making a good critique visible is not enough unless the workflow forces it to govern search, abandonment, or plan revision. [quick-win]

3. **Project-level backtracking is distinct from local iteration.** The agents reran experiments, added robustness checks, and changed details, but did not restart the project after their central approaches weakened. In the TabPFN run, six approaches were rejected within fourteen hours and the solution framing then stayed fixed despite roughly 110 hours remaining. Trajectory evaluations should therefore score local repair and project-level reframing separately. [quick-win]

4. **The engineering/judgment split now has a bounded observed case.** The agents completed literature reviews, debugged GPU environments, ran hundreds of experiments, retrieved external reviews, and produced complete LaTeX papers without research help; exact-domain reviewers still issued unambiguous rejections. This does not prove that “research taste” is generally unautomatable, but it converts a conceptual automation-boundary claim into a concrete, artifact-rich failure case. [just-a-reference]

5. **Trace-driven harness revision can overfit a single trajectory.** Claude Fable 5 received a pilot telemetry log and OpenClaw documentation and proposed broad scaffold changes intended to prevent the observed failures; the authors report that it over-weighted the single sample and repeated several of the same failure modes. For trace-learning systems, this is a warning to validate promoted rules or harness edits across tasks or held-out runs rather than treating a rich trace as broad evidence. [experiment]

6. **Resource observability does not imply resource control.** The OpenClaw agents repeatedly checked available time, compute, and API spend but finished with more than half the API budget unused; the Codex robustness run exhausted the same API budget in just over two days with nearly 100 hours left. A dashboard and a recurring resume loop can expose or prolong a budget without supplying the policy that allocates it well across exploration, scaling, and writing. [experiment]

## Limitations (our opinion)

This is strong qualitative evidence and weak population evidence. The headline result comes from two questions, both empirical machine-learning projects selected through collaborators, plus five total runs of unequal status: two pilots without reasoning, two main Opus/OpenClaw runs, and one GPT/Codex robustness run. It does not establish performance on theoretical work, incremental research, fields outside ML, or questions chosen by the agent itself.

The reviewer construction trades one confound for another. Original authors know the exact question and can identify shallow evidence better than ordinary conference reviewers, but they also know their own successful approach, know the output is AI-generated, and participate in the study. The papers were apparently poor enough that the rejection conclusion is credible, yet no independent expert-review arm measures how much scores or failure attributions depend on original-author expectations. The AI reviewers also saw only rejected papers; as the authors note, repeated rejection cannot establish that those reviewers discriminate good research from bad rather than reject uniformly.

The effective update space is broad but still designed. Signals and histories included the research question, web literature, experiment outputs, logs, project files, review feedback, and live budget telemetry. Operations included coding, web and email use, GPU experiments, subagents, clean-context delegation, review, and paper revision. The model-scaffold system could express many hypotheses and experimental plans. Fixed outside that space were the two task choices, six-day and dollar budgets, top-conference paper objective, no-abstention paper requirement, original-author rubric, exploration gate, tool surface, and human decisions about interventions. Those choices can induce the observed pattern: for example, requiring a paper when a hypothesis fails can favor an underpowered negative-results paper over abstention or a longer restart.

The direct inference is therefore configuration-bounded: **a negative agent evaluation bounds the tested model-scaffold-task system; attributing the failure to the model requires decomposition-robust evidence.** This study shows that the tested compound systems failed under this protocol. It does not show that LLMs cannot conduct open-ended research across rival task representations, state and memory designs, action bases, orchestration policies, stopping rules, or human-agent divisions of labor.

The robustness check does not isolate model from scaffold. It changes Opus/OpenClaw to GPT/Codex jointly and changes budget behavior from underspending to rapid exhaustion. Similar weak final work rules out the narrow claim that one obvious OpenClaw defect wholly explains the result, but it cannot attribute failure to model, scaffold, interaction, or fixed protocol. The main OpenClaw runs also suffered a reasoning-signature bug that reset accumulated context five and fourteen times; the similar outcomes across different reset counts are reassuring but do not replace a vendor-scaffold control.

Finally, “without human help” applies to the substantive research work, not the complete trajectory. Humans patched the harness bug, supplied credentials and repositories, extended the deadline by 24 hours after weak drafts, and requested readability rewrites. Those interventions mostly favor the agents, but they matter when comparing this setup with fully autonomous or strictly standardized evaluations. Six days is also much shorter than the original authors' research process, even if the agents left budget and time unused.

## Recommended Next Action

Update [Known-target discovery benchmarks show reachability, not discovery closure](../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) with a short comparison section on **expert-grounded shadow evaluation** as an alternative oracle construction. State that it preserves an uncontaminated, open-ended question without scoring target similarity, but pays with small samples, expensive non-blind expert judgment, and no cheap inner-loop verifier; add this snapshot as `evidenced-by`.
