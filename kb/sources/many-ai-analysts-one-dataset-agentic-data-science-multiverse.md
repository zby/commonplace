---
source: https://www.pnas.org/doi/epdf/10.1073/pnas.2606495123
description: "Controlled many-agent analysis study showing that model and prompt choices steer conclusions drawn from identical data"
captured: 2026-08-18
capture: web-fetch
capture_via: https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC13393493/unicode
capture_note: "The PNAS ePDF endpoint returned HTTP 403; the article text was captured from its open-access NCBI PMC BioC mirror. The mirror omits some inline mathematical glyphs."
genre: scientific-paper
type: kb/sources/types/snapshot.md
---

# Many AI analysts, one dataset: Navigating the agentic data science multiverse

Author: Martin Bertran, Riccardo Fogliato, Zhiwei Steven Wu
Source: https://www.pnas.org/doi/epdf/10.1073/pnas.2606495123
DOI: 10.1073/pnas.2606495123
Date: 2026-07-14

## Significance

Scientific conclusions hinge not only on data but on analytic decisions that published results seldom make explicit. Using LLM-based agents, we construct a data science multiverse: a distribution of defensible analyses and outcomes, screened by an AI auditor. Across three domains, AI analysts reach divergent hypothesis-support verdicts from identical data, and conclusions can shift with model and prompt choices. As AI-assisted analysis becomes scalable at low cost, the multiverse highlights a vulnerability to selective reporting. The multiverse also provides a diagnostic, revealing when key analytic decisions were left undocumented or when research questions or procedures are underspecified. Looking ahead, we argue that reliable automated data science will require multiverse-style reporting and prompt disclosure, alongside code and data.

## Abstract

Empirical conclusions depend not only on data but also on analytic decisions. Many-analyst studies have quantified this dependence: independent teams testing the same hypothesis on the same dataset regularly reach conflicting conclusions. But such studies require costly human coordination. We show that fully autonomous AI analysts built on large language models (LLMs) can, cheaply and at scale, produce the analytic dispersion observed in human many-analyst studies. In our framework, each AI analyst independently executes a complete analysis pipeline on a fixed dataset and hypothesis; a separate AI auditor screens every run for methodological validity. Across three datasets, AI analyst-produced analyses exhibit substantial dispersion in effect sizes, p-values, and conclusions. This dispersion can be traced to identifiable analytic choices in preprocessing, model specification, and inference that vary systematically across LLM and persona conditions. Critically, the outcomes are steerable: reassigning the analyst persona or LLM shifts the distribution of results even among methodologically sound runs. These results highlight a central challenge for AI-automated empirical science: when defensible analyses are cheap to generate, evidence becomes abundant and vulnerable to selective reporting. The same capability also helps address it: treating analyst results as distributions makes analytic uncertainty visible, and deploying AI analysts against a published specification can reveal how much disagreement stems from underspecified design choices. Taken together, our results motivate a transparency norm: AI-generated analyses should be accompanied by multiverse-style reporting and full disclosure of the prompts used, on par with code and data.

## Introduction

Scientific claims often hinge on analytic choices that are rarely visible in published results. Past “many-analyst” studies have shown that independent teams analyzing the same dataset to test the same hypothesis regularly reach conflicting conclusions. In a landmark example, Silberzahn et al. asked 29 teams whether soccer referees were more likely to give red cards to dark-skinned players; 20 found significant evidence of bias, 9 did not. Breznau et al. documented substantial variation in effect estimates across 73 teams analyzing the same immigration-policy question.

These discrepancies do not arise from error or lack of expertise. They reflect the accumulation of reasonable analytic decisions, what Gelman and Loken termed the “garden of forking paths.” Many-analyst studies make this latent uncertainty visible and help explain persistent replicability failures across scientific fields. (See SI Appendix for extended related work.) But these studies are exceptionally resource-intensive, requiring months to years of coordination among dozens of independent teams. Analytical variability, therefore, remains something to be investigated on occasion, not a routine uncertainty to be quantified.

Recent large language models (LLMs) power agents that write code, execute it, and iterate on results, with applications from materials discovery to hypothesis generation. In this paper, we use such agents as AI analysts for studying analytical variability. By varying the underlying LLM and prompt framing, we generate large populations of AI analysts that independently test the same hypothesis on the same dataset, producing a scalable, automated analogue of many-analyst studies.

Our framework generates and audits AI analyst-conducted analyses at scale. In each session, an AI analyst receives a dataset, a hypothesis, and a prespecified estimand. It then makes its own analytic choices—including variable selection, model specification, and inference—before producing a structured report without any human oversight. A separate AI auditor evaluates each analysis for coherence and alignment with the study design, filtering runs with clear methodological failures (misspecified estimands, invalid variable constructions, inappropriate inference). We repeat this across four LLMs and three datasets, including the well-known many-analyst study on soccer referees from Silberzahn et al.

Across all three datasets, AI analysts display wide dispersion in effect sizes, p-values, and binary support decisions; independent runs frequently reverse whether the hypothesis is judged supported (Fig. 1). Auditing filters noncompliant runs, but does not eliminate the dispersion. The dispersion is steerable: changing the analyst persona or LLM systematically shifts the outcome distribution even among judge-approved analyses. Crucially, the use of AI enables what human many-analyst studies cannot: controlled experimentation on the analysis process itself. By manipulating persona and model while holding all else fixed, we isolate the causal effect of these factors on conclusions—something observational human studies can only approximate. These results highlight a dual challenge for AI-assisted empirical science: when defensible analyses are cheap to generate, evidence becomes abundant and vulnerable to selective reporting; yet the same capability can make multiverse-style uncertainty quantification routine, turning analytic variability from a hidden liability into a visible, measurable quantity.

### Figure 1

Specification curve for the anes-views dataset. Top: Each point is one AI analyst-produced analysis, showing the standardized OLS coefficient for TV news exposure predicting ideological misalignment, with 95% CI. Analyses are sorted by estimate; blue marks hypothesis supported by the analysis, yellow marks not supported or inconclusive. Estimates span negative to positive effects across valid runs. Bottom: Strike plot of the analytic decisions underlying each run. Each row corresponds to an analytic decision dimension (labeled on the left) and its possible categories (labeled on the right). Each column corresponds to a single analysis, whose point estimate is shown directly above in the Top panel. AI analysts vary in covariate count, regression method, SE calculation, and temporal pooling, producing a multiverse of defensible specifications from a single research question.

## Materials and Methods

### Overview

We study analytical variability by deploying fully autonomous AI analysts on fixed dataset–hypothesis tasks with prespecified estimands. Our design crosses three datasets, four base LLMs, and five analyst personas that vary in analytical behavior, totaling approximately 5,000 runs. Each AI analyst independently conducts a complete analysis—from data exploration through model specification to inference—using a standardized computational scaffold. We audit all runs for validity using transcript-based LLM evaluators and extract structured analytical decisions from each.

### Dataset–Hypothesis Tasks

Each AI analyst receives a dataset, a hypothesis stated in natural language, and a prespecified primary estimand (Table 1). Our experiments use three tasks spanning distinct domains and methodological challenges: soccer, the soccer-referee bias dataset from Silberzahn et al.; metr-rct, a recent randomized controlled trial on AI-assisted programming; and anes-views, drawn from the American National Election Studies Time Series Cumulative Data File (1948–2020). Fixing the estimand establishes a common inferential target, allowing direct comparison of effect sizes across runs; without this constraint, apparent disagreements may reflect analysts targeting different yet defensible quantities (e.g., odds ratio vs. risk difference; marginal vs. conditional effects) rather than differences in analytical approach.

#### Table 1. Dataset–hypothesis pairs and prespecified estimands

| Dataset | Hypothesis | Primary estimand |
|---|---|---|
| soccer (soccer referees) | Are soccer referees more likely to give red cards to dark- than light-skin-toned players? | Adjusted risk difference, dark vs. light skin |
| metr-rct (METR coding RCT) | Does AI assistance increase coding task completion time, accounting for task size and developer differences? | Developer-blocked geometric mean ratio of implementation time, AI vs. control |
| anes-views (ANES Time Series Cumulative File) | Do people who watch more TV news show a tighter link between symbolic ideology and policy positions? | Standardized OLS coefficient for TV news predicting ideological misalignment |

Each analyst reports the estimand with a 95% CI. Tasks span a spectrum of data contamination risk, from high (soccer) to low (anes-views).

These tasks span a spectrum of data contamination—the extent to which headline findings are likely present in LLM training data. The soccer dataset and its published conclusions are widely known, making it a high-contamination benchmark. The metr-rct dataset is recent and unlikely to appear in current training corpora; we additionally flip the directional hypothesis relative to the original study. The anes-views task is low-contamination and methodologically demanding, requiring nontrivial choices about variable construction, survey weighting, and pooling across election waves.

### AI Analysts

Each analyst receives a task prompt specifying the hypothesis, dataset path, and primary estimand. Analysts retain full autonomy over data cleaning, variable transformation, missing data handling, covariate selection, functional forms, and estimator choice. Similar to Breznau et al., each analyst must state whether the hypothesis is supported or not supported by the totality of its analysis (where “not supported” includes inconclusive or contradictory evidence) and report a p-value for its primary test of the prespecified estimand. Analysts produce reproducible analysis code and a narrative report as their final output.

Analysts are implemented as tool-using ReAct agents in the Inspect AI framework, each with access to a persistent Python session, a stateful shell, and a file editor. We test four contemporary LLMs as the underlying reasoning engine: Anthropic’s Claude Sonnet 4.5 and Haiku 4.5, and Qwen3 Coder 480B and Qwen3 235B A22B. All analysts use a fixed sampling temperature; the BioC source export omits its displayed value. Runs are capped at 250 messages or 60 min per run, whichever comes first.

### Experimental Steering

To test whether analyst persona influences analytical choices and conclusions, we vary the prompt language while holding the estimand and reporting requirements fixed. We define five personas: i) standard (neutral framing), ii) negative (hypothesis described as implausible), iii) positive (hypothesis described as plausible), iv) confirmation seeking (CS; prompted to find supporting specifications within conventional practices), and v) strong confirmation seeking (Strong CS; explicitly encouraged to engage in p-hacking–style exploration). Conditions (ii) and (iii) model analysts with prior expectations who do not actively seek confirmation; conditions (iv) and (v) model analysts who do. Exact prompt language is provided in SI Appendix.

### Quality Control Via Auditing

AI analysts do not always conduct valid analyses—in pilot runs, some produced confident reports with fully hallucinated results, and others recalled published findings from training data rather than analyzing the dataset provided. We therefore introduce a scalable AI auditor, Claude Sonnet 4.5 with a dedicated auditor prompt (SI Appendix), that reviews the full conversation transcript for each run, including all tool calls, intermediate outputs, and code artifacts. Access to these traces is critical for verifying that reported quantities match actual computational outputs.

For each run, the auditor produces a) an overall validity verdict, b) scores on 13 methodological dimensions (e.g., estimand alignment, uncertainty quantification, conclusion discipline; 0 to 10 scale), and c) extracted scalar outcomes (effect estimate, CI, p-value, hypothesis-support flag). After excluding runs that fail compliance screening, we retain approximately 30 compliant runs per (dataset × model × persona) cell, providing a basis for examining the within-cell distribution of effect estimates and hypothesis support rates.

### Decision Extraction

To link analytical choices to substantive conclusions, we extract structured decisions, including outcome transformation, covariate inclusion, and variance estimator from each run using a unified per-dataset codebook (see Fig. 1 for the anes-views specification curve).

## Main Results

Of 4,946 total runs, 3,303 (67%) passed auditor-based compliance screening (see SI Appendix, Table S1 for exclusion rates by model and persona). We report results for both the full set and the compliant subset below.

### Analytical Variability Across AI Analysts

Given identical data, hypothesis, and estimand, AI analysts reach sharply different conclusions. Fig. 1 displays the specification curve for the anes-views task: point estimates span negative to positive values, and compliant runs disagree not only on magnitude but on the direction of the effect. The strike plot beneath the curve reveals that this dispersion arises from concrete analytic choices—covariate count, regression method, SE calculation, and temporal pooling—each of which varies across runs. Similar patterns hold for soccer and metr-rct (SI Appendix). A single research question, analyzed by autonomous AI analysts, thus yields a multiverse of defensible yet divergent results.

### Persona and Model Effects on Hypothesis Support

Fig. 2 shows the fraction of runs reaching a “supported” conclusion, stratified by dataset, persona, base model, and compliance status. Both persona and model choice drive substantial variation. Across all three datasets, support rates increase from the most skeptical (Negative) to the most confirmation-seeking persona (Strong CS), a trend that holds consistently across all four LLMs. The magnitude of this persona effect varies by dataset: the Negative-to-Strong CS gap ranges from 34 percentage points (anes-views) to 66 percentage points (metr-rct), likely reflecting differences in the underlying strength of each effect. Model choice introduces additional spread: even within a given persona, different LLMs can diverge substantially in metr-rct and soccer, while remaining more tightly clustered in anes-views. Notably, the difference between Negative and Positive personas—which encode differing prior expectations without encouraging p-hacking—is modest relative to the shift induced by the CS conditions. This mirrors findings from human many-analyst studies, where analysts’ self-reported prior beliefs about a hypothesis were not strongly associated with their results.

#### Figure 2

Hypothesis support rates by dataset, persona, and model. Fraction of analyses reaching a “supported” conclusion, stratified by persona (x-axis), base model (color), and compliance status (shape: filled = compliant, open = all data), shown separately for each dataset. Personas range from Negative to Strong CS (Strong Confirmation Seeking). CS, Confirmation Seeking.

SI Appendix, Per-Model Decomposition of Figures 1 and 3 provides the corresponding per-model specification and p-value curves, separating run-to-run variation within fixed model–persona cells from across-persona and across-model differences.

Comparing all runs (open markers) with compliant runs only (filled markers) reveals that compliance filtering partially mitigates persona-driven steering. The gap between the two markers is small for Negative, Standard, and Positive personas but widens substantially for CS and Strong CS—particularly in metr-rct—indicating that the auditor disproportionately removes the more aggressive analytic strategies employed under confirmation-seeking conditions. Compliance filtering thus narrows, but does not eliminate, the persona-induced spread in conclusions.

The distributions of reported p-values underlying these binary verdicts tell a consistent story. Fig. 3 sorts each persona’s p-values in ascending order. In both metr-rct and soccer, the CS and Strong CS curves are pulled downward relative to the other personas—while the Negative and Positive curves remain largely indistinguishable from Standard. In anes-views, the separation is muted, with all personas producing broadly dispersed p-values. Comparing the top panel (all runs) with the bottom panel (compliant only) reveals the auditor’s mitigating effect from a second angle: compliance filtering pulls the CS and Strong CS curves upward toward the others, narrowing but not eliminating the persona-driven gap—consistent with the attenuation of support rates in Fig. 2. Extraction from auditor rationales reveals the mechanism behind these shifts: CS personas engage in specification search and overclaim their findings at far higher rates than other personas. The auditor catches these behaviors at elevated rates, explaining the partial attenuation after filtering.

#### Figure 3

Sorted p-value distributions by persona. Because each analyst applies a different methodology to the same fixed dataset, p-values vary across runs due to analytical choices rather than sampling variability. p-values are sorted in ascending order, shown separately for each dataset and stratified by persona. Downward-shifted curves indicate personas producing systematically smaller p-values. The gray horizontal line marks α = 0.05. Top panel includes all analyses; Bottom panel restricts to compliant analyses only.

## Discussion

Our findings show that fully autonomous AI analysts produce a multiverse of defensible yet divergent results whose dispersion is comparable in scale and structure to that documented in human many-analyst studies. We do not claim the AI-generated distribution is interchangeable with what a population of human experts would produce; the overlap between the two is an empirical question we return to under Limitations. What our experiments do establish is that this kind of multiverse can now be generated cheaply and at large scale, which makes its properties a first-order question regardless of whether humans remain in the loop. The AI setting also reveals something new: the distribution of conclusions is not merely dispersed but steerable. Active specification search shifts conclusions far more than differing prior beliefs, which is consistent with human studies in which self-reported priors show weak association with results, and auditor-based filtering attenuates but does not eliminate this effect.

### Implications

The central challenge is not that automated analyses are wrong but that they are abundant. For a fixed dataset and hypothesis, AI analysts produce many defensible pipelines that reach meaningfully different conclusions: a structural vulnerability to selective reporting. Cherry-picking a favorable run or iterating until a preferred conclusion emerges is straightforward at scale. This is especially consequential when empirical analyses inform downstream policy, regulation, or public health guidelines.

Although our experiments study fully autonomous analysts, the implications extend to AI-assisted analysis more broadly. In practice, a user’s framing of a research question to an AI coding assistant parallels our persona manipulation: describing a hypothesis as plausible resembles our Positive condition; asking the AI to find supporting evidence resembles CS. Our results indicate that passive framing of this kind produces only modest shifts, whereas explicit or repeated encouragement can substantially steer conclusions. As AI-assisted analysis becomes routine, these findings motivate concrete transparency measures. Specification curves and multiverse reporting should accompany any AI-generated analysis, and we argue that the exact prompts used should be disclosed as part of the methodological specification, on par with code and data.

Our results also point to an opportunity: the same agentic scale that creates vulnerability can make multiverse mapping routine. Traditional multiverse and specification curve analyses map analytic uncertainty by manually enumerating specifications; deploying AI analysts at scale makes such mapping practical, and treating their output as a distribution rather than a single point makes variability visible and measurable. We frame this as a complement to, not a replacement for, manual multiverse construction by human researchers: the AI-generated multiverse is a concrete, reproducible probe of the analytic decision space whose composition depends on the choice of model and prompt, and human judgment remains necessary to interpret it, audit it, and decide which slices of the decision space to inspect. The framework can also serve as a computational stress test for published findings, operationalizing the stability principle of veridical data science: given a study’s documented specification—estimand, model class, key covariates—one can supply it as a partial constraint, generate many independent reruns, and quantify residual dispersion attributable to choices the original publication left implicit. We illustrate this by supplying AI analysts with the documented specification of one human team from the soccer many-analyst study and allowing deviations where the agents judged them warranted. The AI-generated distribution of estimates clusters around the original human estimate (SI Appendix, Fig. S4), and the undocumented decisions the agents surfaced did not shift the conclusion—demonstrating that, for this specification, the implicit degrees of freedom are narrow. Conversely, when residual dispersion is large, it pinpoints which undocumented choices matter most: specifying confounders, prespecifying outlier handling rules, or fixing the SE method may each substantially narrow the distribution. The multiverse thus becomes not only an object of study but a guide for where greater precision in study design would yield more determinate findings.

### Limitations

Several limitations warrant discussion. First, even with a prespecified estimand, the space of defensible analyses remains large enough that comprehensive human review is impractical. Automated auditing is therefore necessary, but any definition of a “reasonable” analysis depends on chosen standards, and how best to evaluate LLM-based auditors remains an open question. Second, the analytical paths AI analysts explore need not coincide with those human analysts would traverse: LLMs may favor different modeling conventions, overlook domain-specific considerations, or exhibit shared blind spots inherited from training data. The multiverse we observe is therefore an AI-generated one, and its overlap with the human multiverse remains an empirical question. Nonetheless, the structural findings—which decision points drive disagreement and how framing steers conclusions—remain directly relevant to human–AI collaboration, where a user’s instructions shape the AI’s analytical choices.

## Data, Materials, and Software Availability

Code, agent prompts, auditor prompts, and analysis transcripts have been deposited in GitHub (https://github.com/amazon-science/agentic-forking-path). Previously published data were used for this work [Soccer referee bias: Silberzahn et al.; METR coding RCT: Becker et al.; and ANES Time Series Cumulative Data File: American National Election Studies].

## References

1. “Many analysts, one data set: Making transparent how variations in analytic choices affect results.” *Adv. Methods Pract. Psychol. Sci.* 1, 337–356 (2018).
2. “Observing many researchers using the same data and hypothesis reveals a hidden universe of uncertainty.” *Proc. Natl. Acad. Sci. U.S.A.* 119, e2203150119 (2022). DOI: 10.1073/pnas.2203150119.
3. “Variability in the analysis of a single neuroimaging dataset by many teams.” *Nature* 582, 84–88 (2020). DOI: 10.1038/s41586-020-2314-9.
4. “Nonstandard errors.” *J. Fin.* 79, 2339–2390 (2024).
5. “Same data, different conclusions: Radical dispersion in empirical results when independent analysts operationalize and test the same hypothesis.” *Organ. Behav. Hum. Decis. Process.* 165, 228–249 (2021).
6. “Crowdsourcing hypothesis tests: Making transparent how design choices shape research results.” *Psychol. Bull.* 146, 451 (2020). DOI: 10.1037/bul0000220.
7. “Consensus-based guidance for conducting and reporting multi-analyst studies.” *eLife* 10, e72185 (2021). DOI: 10.7554/eLife.72185.
8. A. Gelman, E. Loken, “The garden of forking paths: Why multiple comparisons can be a problem, even when there is no ‘fishing expedition’ or ‘p-hacking’ and the research hypothesis was posited ahead of time” (2013). https://sites.stat.columbia.edu/gelman/research/unpublished/p_hacking.pdf. Accessed 2026-06-29.
9. “Estimating the reproducibility of psychological science.” *Science* 349, aac4716 (2015). DOI: 10.1126/science.aac4716.
10. “Many labs 2: Investigating variation in replicability across samples and settings.” *Adv. Methods Pract. Psychol. Sci.* 1, 443–490 (2018).
11. “Evaluating the replicability of social science experiments in nature and science between 2010 and 2015.” *Nat. Hum. Behav.* 2, 637–644 (2018). DOI: 10.1038/s41562-018-0399-z.
12. “Replicability, robustness, and reproducibility in psychological science.” *Annu. Rev. Psychol.* 73, 719–748 (2022). DOI: 10.1146/annurev-psych-020821-114157.
13. S. Hong, “Data interpreter: An LLM agent for data science.” arXiv preprint (2024). https://arxiv.org/abs/2402.18679. Accessed 2026-06-29.
14. S. Guo, “DS-agent: Automated data science by empowering large language models with case-based reasoning.” arXiv preprint (2024). https://arxiv.org/abs/2402.17453. Accessed 2026-06-29.
15. X. Hu, “InfiAgent-DABench: Evaluating agents on data analysis tasks.” arXiv preprint (2024). https://arxiv.org/abs/2401.05507. Accessed 2026-06-29.
16. OpenAI, “GPT-5 system card” (Tech. Rep., OpenAI, 2025).
17. Anthropic, “Claude opus 4.5 system card” (Anthropic, System card, 2025).
18. “Autonomous chemical research with large language models.” *Nature* 624, 570–578 (2023). DOI: 10.1038/s41586-023-06792-0.
19. K. Huang, “Automated hypothesis validation with agentic sequential falsifications.” arXiv preprint (2025). https://arxiv.org/abs/2502.09858. Accessed 2026-06-29.
20. J. Becker, N. Rush, E. Barnes, D. Rein, “Measuring the impact of early-2025 AI on experienced open-source developer productivity.” arXiv preprint (2025). https://arxiv.org/abs/2507.09089. Accessed 2026-06-29.
21. American National Election Studies, “ANES time series cumulative data file (1948–2024)” (2025).
22. S. Yao, “ReAct: Synergizing reasoning and acting in language models,” in *The Eleventh International Conference on Learning Representations* (2022).
23. UK AI Security Institute, “Inspect AI: Framework for large language model evaluations.” GitHub. https://github.com/UKGovernmentBEIS/inspect_ai. Accessed 2026-06-29.
24. Anthropic, “System card: Claude haiku 4.5” (Anthropic, System card, 2025).
25. Anthropic, “System card: Claude sonnet 4.5” (Anthropic, System card, 2025).
26. Q Team, “Qwen3 technical report” (Tech. Rep., Q Team, 2025).
27. “Increasing transparency through a multiverse analysis.” *Perspect. Psychol. Sci.* 11, 702–712 (2016). DOI: 10.1177/1745691616658637.
28. “Specification curve analysis.” *Nat. Hum. Behav.* 4, 1208–1214 (2020). DOI: 10.1038/s41562-020-0912-z.
29. “Veridical data science.” *Proc. Natl. Acad. Sci. U.S.A.* 117, 3920–3929 (2020). DOI: 10.1073/pnas.1901326117.
