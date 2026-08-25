---
description: "Crossed 4,946-run agent-analysis experiment separates sampling dispersion from model/persona steering and finds that auditing reduces but does not remove selective-reporting risk"
source: https://www.pnas.org/doi/epdf/10.1073/pnas.2606495123
captured: "2026-08-18"
capture: web-fetch
genre: scientific-paper
snapshot_sha256: 79188a6fed4a5f81ed20ec3dde4a39657a162ac43d4755b69a50ec94657c8fc4
capture_via: https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC13393493/unicode
capture_note: The PNAS ePDF endpoint returned HTTP 403; the article text was captured from its open-access NCBI PMC BioC mirror. The mirror omits some inline mathematical glyphs.
ingested: "2026-08-18"
type: kb/sources/types/ingest-report.md
domains: [agentic-analysis, research-reproducibility, prompt-sensitivity, llm-evaluation]
---

# Ingest: Many AI analysts, one dataset

## Classification

A peer-reviewed PNAS experiment with controlled model and persona conditions, three dataset–hypothesis tasks, approximately 5,000 autonomous analysis runs, and transcript-level AI auditing.
Author: Martin Bertran and Riccardo Fogliato (Amazon) and Zhiwei Steven Wu (Amazon and Carnegie Mellon). The paper discloses its experimental scaffold, tasks, prompts, code, and transcripts, but the authors also designed the system and its AI auditor; credibility rests on the reported experiment rather than independent deployment evidence.

## Summary

Bertran, Fogliato, and Wu run 4,946 autonomous data-analysis sessions across three fixed dataset–hypothesis–estimand tasks, four LLMs, and five analyst personas, then use a separate Claude Sonnet 4.5 auditor to screen full traces for methodological compliance. Only 3,303 runs (67%) pass. Even among compliant runs, effect estimates, p-values, and support verdicts vary widely; changing the base model or persona shifts their distributions, with Negative-to-Strong-Confirmation-Seeking support-rate gaps of 34 to 66 percentage points across tasks. Auditing removes aggressive specification search and overclaiming disproportionately, but does not eliminate steering. The authors argue that cheap automated analysis makes selective reporting easier while also making multiverse-style uncertainty mapping practical, and recommend reporting result distributions and disclosing prompts alongside code and data.

## Quotes

- **Source extract (verbatim):** We study analytical variability by deploying fully autonomous AI analysts on fixed dataset–hypothesis tasks with prespecified estimands. Our design crosses three datasets, four base LLMs, and five analyst personas that vary in analytical behavior, totaling approximately 5,000 runs. Each AI analyst independently conducts a complete analysis—from data exploration through model specification to inference—using a standardized computational scaffold. We audit all runs for validity using transcript-based LLM evaluators and extract structured analytical decisions from each.
  - **Source location:** “Materials and Methods,” opening paragraph
- **Source extract (verbatim):** After excluding runs that fail compliance screening, we retain approximately 30 compliant runs per (dataset × model × persona) cell, providing a basis for examining the within-cell distribution of effect estimates and hypothesis support rates.
  - **Source location:** “AI Auditor and Structured Extraction”
- **Source extract (verbatim):** Given identical data, hypothesis, and estimand, AI analysts reach sharply different conclusions. Fig. 1 displays the specification curve for the anes-views task: point estimates span negative to positive values, and compliant runs disagree not only on magnitude but on the direction of the effect.
  - **Source location:** “Results,” “Analytical Variability Across AI Analysts”

- **Source extract (verbatim):** To test whether analyst persona influences analytical choices and conclusions, we vary the prompt language while holding the estimand and reporting requirements fixed. We define five personas: i) standard (neutral framing), ii) negative (hypothesis described as implausible), iii) positive (hypothesis described as plausible), iv) confirmation seeking (CS; prompted to find supporting specifications within conventional practices), and v) strong confirmation seeking (Strong CS; explicitly encouraged to engage in p-hacking–style exploration). Conditions (ii) and (iii) model analysts with prior expectations who do not actively seek confirmation; conditions (iv) and (v) model analysts who do.
  - **Source location:** “Materials and Methods,” “Analyst Personas”
- **Source extract (verbatim):** AI analysts do not always conduct valid analyses—in pilot runs, some produced confident reports with fully hallucinated results, and others recalled published findings from training data rather than analyzing the dataset provided. We therefore introduce a scalable AI auditor, Claude Sonnet 4.5 with a dedicated auditor prompt (SI Appendix), that reviews the full conversation transcript for each run, including all tool calls, intermediate outputs, and code artifacts. Access to these traces is critical for verifying that reported quantities match actual computational outputs.
  - **Source location:** “Materials and Methods,” “AI Auditor and Structured Extraction”
- **Source extract (verbatim):** Of 4,946 total runs, 3,303 (67%) passed auditor-based compliance screening (see SI Appendix, Table S1 for exclusion rates by model and persona).
  - **Source location:** “Results,” opening paragraph

- **Source extract (verbatim):** Analysts are implemented as tool-using ReAct agents in the Inspect AI framework, each with access to a persistent Python session, a stateful shell, and a file editor. We test four contemporary LLMs as the underlying reasoning engine: Anthropic’s Claude Sonnet 4.5 and Haiku 4.5, and Qwen3 Coder 480B and Qwen3 235B A22B. All analysts use a fixed sampling temperature; the BioC source export omits its displayed value. Runs are capped at 250 messages or 60 min per run, whichever comes first.
  - **Source location:** “Materials and Methods,” analyst implementation paragraph

## Connections Found

This paper is the first end-to-end empirical case in the KB for [LLM output deviation requires three-way diagnosis](../notes/llm-output-deviation-requires-three-way-diagnosis.md). Repeated runs inside a fixed model–persona cell expose indeterminism; materially different compliant analytic pipelines show that the unchanged task admits a plural valid set; methodological rejections supply the out-of-spec category, with pilot hallucinations and recalled published findings as concrete interpreter failures. It also supports [The boundary of automation is the boundary of verification](../notes/the-boundary-of-automation-is-the-boundary-of-verification.md), because an auditor rejects one-third of generated analyses yet leaves substantial steering among accepted runs. Relative to [Prompt Stability in Code LLMs](prompt-stability-code-llms-emotion-personality-variations.ingest.md), it moves from meaning-preserving prompt variants and code correctness to end-to-end analytic pipelines and scientific conclusions. The comparison sets a boundary: confirmation-seeking prompts change the analyst's commission, so their effects are controlled steering rather than clean bias estimates under fixed semantics. The experiment's unvaried design choices remain an orthogonal coverage limit under [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), not a fourth source of output deviation.

## Extractable Value

1. **Use agent populations as an end-to-end specification stress test.** Give many tool-using agents the same input and partial contract, inspect the outcome distribution, then extract the decision dimensions responsible for dispersion. This extends prompt-variation diagnosis from final answers to complete work pipelines and can reveal which choices a specification left implicit. [experiment]

2. **Keep output-deviation causes separate from experimental coverage.** First classify repeated-sample variation, plural spec-valid analyses, and out-of-spec outputs as indeterminism, underspecification, and interpreter failure. Then report between-condition effects and alternatives excluded by the fixed decomposition as separate attribution and coverage limits. This prevents sampling noise, semantic plurality, bias, deliberate commission changes, and untested design space from being collapsed into one “variance” number. [quick-win]

3. **Audit residual distributions, not only pass rates.** A 67% compliance rate sounds like quality control, but persona-conditioned outcome shifts survive inside the accepted subset. A gate can remove invalid processes without making the retained result distribution neutral or representative; downstream evaluation should therefore compare distributions before and after filtering. [quick-win]

4. **Treat prompt-treatment semantics as part of experimental validity.** Negative and Positive personas mainly alter stated prior plausibility, while Confirmation Seeking explicitly requests supporting specifications and Strong Confirmation Seeking invites p-hacking-style exploration. Pooling those as generic “prompt sensitivity” would obscure that the latter treatments change the task commission rather than only its surface expression. [quick-win]

5. **Test multiverse reporting and prompt disclosure as interventions, not just norms.** The proposed transparency package is plausible and operationally specific, but this experiment does not show that disclosure prevents cherry-picking, improves reviewer decisions, or identifies the representative analysis distribution. A follow-up could compare decisions made from one selected run, an audited multiverse, and the same multiverse plus prompts and decision traces. [experiment]

## Limitations (our opinion)

The causal results are narrow but useful. Analysts could condition on the full dataset, hypothesis, prespecified estimand, persona prompt, model priors, run history, and tool outputs; they could compose Python, shell, file-editing, preprocessing, modeling, and inference operations. The effective hypothesis class was whatever four selected LLMs could express inside one ReAct/Inspect scaffold. The datasets, hypotheses, estimands, persona family, model family, tool surface, run cap, output protocol, decision codebook, auditor model and prompt, and compliance criteria stayed fixed. The study therefore isolates model and persona effects inside this space; it does not establish that the space represents human analysis, all defensible AI analysis, or the best decomposition for automated science.

The AI auditor is a major unverified dependency. The snapshot reports transcript-level inspection and 13 scored dimensions, but no independent human-labelled calibration of its per-run discrimination. “Compliant” therefore means accepted by this auditor, not established methodological soundness. The residual steering result is still informative—dispersion survives the filter—but neither the pass rate nor the post-filter subset should be treated as ground truth.

Coverage is limited to three tasks, four model checkpoints from two families, one agent scaffold, and one auditor. The high-contamination soccer task may activate memorized analyses; the newer METR task and constructed ANES task reduce that concern but do not supply a human many-analyst baseline. The authors explicitly do not claim that their AI-generated multiverse is interchangeable with a human-expert multiverse.

Finally, the experiment establishes that model and persona treatments change outcomes, not that multiverse reporting or prompt disclosure corrects selective reporting. It also does not code-ground or reproduce the reported results in this ingest: public code and transcripts are named in the paper, but no repository revision was inspected or executed.

## Recommended Next Action

Run a code-grounded follow-up on the paper's public repository and transcripts. Classify a stratified sample of accepted and rejected runs under the three-question diagnosis, test whether the auditor's rationales discriminate plural spec-valid analyses from interpreter failures, and keep fixed-decomposition coverage as a separate audit result.
