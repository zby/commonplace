---
description: "Survey of 33 agent-evaluation trends connects system-level attribution, trajectory evidence, reliability, and judge validation to Commonplace workflow evaluation."
source: https://sage.cs.princeton.edu/trends/emerging-trends-paper.pdf
captured: "2026-10-26"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: fcfe9f4c19d83454456e81a510e683851d6802f17d21e9ee10202f2e8aa6ca96
ingested: "2026-10-26"
type: types/ingest-report.md
domains: [agent-evaluation, measurement-validity, trajectory-analysis, evaluator-independence]
---

# Ingest: Emerging Trends in AI Agent Evaluation

## Classification

An opinionated research survey and agenda, not a new benchmark or controlled intervention. It organizes public research and practitioner materials into 33 methodological, deployment, and institutional trends. Its methods use snowball sampling and citation chains; citations illustrate the selected trends rather than establish comprehensive coverage.

Authors: Felix Chen, Stephan Rabanser, Peter Kirgis, Nitya Nadgir, Rishi Bommasani, Magda Dubois, Elham Tabassi, Cozmin Ududec, Anka Reuel, Sanmi Koyejo, Sayash Kapoor, and Arvind Narayanan. Affiliations span Princeton, Stanford, the UK AI Security Institute, Brookings, UC Berkeley, and the Institute for Advanced Study. Several authors also contributed to evaluation infrastructure and studies discussed in the survey. The acknowledgements disclose research funding and API credits from OpenAI and Google.

## Summary

The paper argues that evaluating agents requires evaluating the combined model, scaffold, tools, environment, and human interventions rather than treating a final response as the sole object of measurement. Part 1 assembles practices for defining constructs, auditing tasks and graders, reporting cost and reliability, controlling causal comparisons, limiting contamination, validating judges, and inspecting trajectories. It distinguishes repeated-run consistency from robustness to changed environments and explains why model–scaffold interactions complicate attribution. Part 2 separates capability evidence, human-interaction outcomes, and systemic impact; simulated users, laboratory trials, field experiments, and production observations answer different questions. Detailed open-world cases complement benchmarks but do not establish typical performance. Part 3 treats access, funding, disclosure rights, rising costs, and agenda-setting as conditions that shape which evaluation evidence exists. The contribution is methodological synthesis and a research agenda, not a demonstration that these recommended practices improve every evaluation workflow.

## Contribution assessment (our opinion)

The problem is important: scores can appear comparable while changes in scaffolds, environments, grading, or human assistance change what they measure. The survey's likely contribution is to connect these failure modes with established measurement concepts and practical experimental controls, making agent claims easier to criticize and test. Its separation of capability, interaction, and institutional evidence is especially useful for preventing unsupported extrapolation. The synthesis appears valuable as an entry point and design reference, but its opinionated, illustrative sampling does not establish the prevalence of all 33 trends or the superiority of this organization over rival surveys. Its significance is more plausibly improved evaluation design than a new empirical finding.

## Quotes

No source quotes have been retained yet.

## Connections Found

The survey is a methodological companion to [Final task success does not establish intended-path health](../theory/final-task-success-does-not-establish-intended-path-health.md). Sections 1a and 1i explain how successful outcomes can hide shortcuts, contamination, or other invalid routes. This broadens the measurement context without implying that every fallback weakens guarantees; it also limits the remedy, since incomplete or apparently clean logs cannot certify problem-free execution.

Section 1e compares directly with [An experiment identifies only the contrast it actually runs](../theory/an-experiment-identifies-only-the-contrast-it-actually-runs.md): model, scaffold, environment, and budget changes must be separated before assigning component effects. A model–scaffold factorial comparison under fixed environmental and budget conditions can estimate interactions within those conditions. It does not compare every alternative system decomposition or establish effects outside that setup.

Sections 1h–1i complement [Evaluation automation is phase-gated by comprehension](../theory/evaluation-automation-is-phase-gated-by-comprehension.md) through manual exploration, representative human-labelled holdouts, and explicit judge-error assessment. This is methodological agreement, not an experiment validating the note's exact sequence. The existing [trajectory-aware evaluation proposal](../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) is the concrete local destination: it already defines a blinded output-only versus trajectory-aware comparison, evidence localization, false-positive accounting, and cost measurement. The survey motivates and bounds that unadopted experiment rather than demonstrating its success.

## Extractable Value

1. **Keep outcome and route evidence separate.** Sections 1a and 1i explain why a successful artifact cannot establish valid execution. Relative to the intended-path note and trajectory proposal, the useful qualification is that more trace access enables criticism but does not make absence of detected defects proof of compliance. [quick-win]
2. **Validate negative judgments as well as detected failures.** Section 1h recommends human-coded holdouts and manual inspection of cases the automated reviewer passed. Sampling those passes can expose missed failures that adjudicating only reported findings cannot reveal. Judge error should enter reported uncertainty rather than disappear behind an aggregate score. [experiment]
3. **Separate consistency, robustness, and generalization.** Section 1d distinguishes success at least once in repeated attempts from success on every attempt, and both from behavior under environmental changes. For KB workflow evaluation, repeated runs on frozen cases answer a narrower question than performance on new workflows or harnesses. [quick-win]
4. **Control the comparison before attributing gains.** Section 1e recommends fixed budgets and environments with independently varied components, including model–scaffold interaction tests when affordable. This operationalizes the experimental-contrast note; improvements within a chosen component boundary remain evidence about that contrast, not evidence that the boundary itself is best. [just-a-reference]
5. **Track what makes evaluation possible.** Part 3 distinguishes access from methodological freedom, disclosure rights, and agenda independence. A retained external evaluation can therefore be assessed for access restrictions and funding conditions without treating third-party status as sufficient evidence of independence. [just-a-reference]

## Limitations (our opinion)

The central synthesis depends on an explicitly opinionated selection of public materials. Snowball sampling and illustrative citations can overrepresent visible, connected evaluation organizations and cannot establish how common each practice is. Part 3 is particularly bounded by public disclosures; the paper cannot reconstruct undisclosed access agreements, unfavorable unpublished evaluations, or all funding relationships.

This paper reports other studies rather than running a unified comparison of its recommendations. Their results retain their original tasks, component boundaries, interfaces, budgets, and graders. The causal controls proposed in section 1e help separate effects inside a selected decomposition; they do not show that competing representations or decompositions were tested. No cited intervention was reproduced for this ingest.

The paper's scope centers frontier agent evaluation. Its recommendations require adaptation to Commonplace's document transformations and semantic review. Human-labelled calibration, repeated runs, and trajectory inspection cost time and compute; the survey supplies no local estimate of whether added detection is worth that cost. As the existing trajectory proposal recognizes, extra evidence can introduce false positives, length sensitivity, and judge-policy variance. A clean review remains limited by missing telemetry and monitor recall.

The automation-versus-augmentation and three-layer framing prevents overclaiming but does not itself identify how benchmark capability translates into institutional benefit. Similarly, the paper describes detailed open-world cases as evidence of achievable performance, not reliable estimates of a population's typical performance or a mathematical ceiling on capability.

## Recommended Next Action

Review `kb/reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md` against section 1h's recommendation to manually sample judge-passed cases, so its calibration design can assess missed failures rather than only adjudicate surfaced findings.
