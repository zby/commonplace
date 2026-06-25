---
source: https://arxiv.org/html/2508.10795v4
description: "LLM-assisted scholarly novelty-assessment paper using related-work retrieval and structured comparison against human novelty reviews."
captured: 2026-06-22
capture: web-fetch
type: kb/sources/types/snapshot.md
tags: [academic-paper]
---

# Beyond “Not Novel Enough”: Enriching Scholarly Critique with LLM-Assisted Feedback

Authors: Osama Mohammed Afzal; Preslav Nakov; Tom Hope; Iryna Gurevych
Source: https://arxiv.org/html/2508.10795v4
Capture note: Article body extracted from arXiv HTML; page navigation and duplicate title/author block trimmed.

## Abstract

Novelty assessment is a central yet understudied aspect of peer review, particularly in high-volume
fields like NLP where reviewer capacity is increasingly strained. We present a structured approach
for automated novelty evaluation that models expert reviewer behavior through three stages: content
extraction from submissions, retrieval and synthesis of related work, and structured comparison for
evidence-based assessment. Our method is informed by analysis of human-written novelty reviews and
captures key patterns such as independent claim verification and contextual reasoning. Evaluated on
182 ICLR 2025 submissions with human annotated reviewer novelty assessments, the approach achieves
86.5% alignment with human reasoning and 75.3% agreement on novelty conclusions—substantially
outperforming existing LLM-based baselines. The method produces detailed, literature-aware analyses
and improves consistency over ad hoc reviewer judgments. These results highlight the potential for
structured LLM-assisted approaches to support more rigorous and transparent peer review without
displacing human expertise. Data and code are made available.
https://ukplab.github.io/eacl2026-assessing-paper-novelty/

## 1 Introduction

The peer review system is collapsing under its own success. Two independent committees at NeurIPS
2021 disagreed on 23% of identical papers Beygelzimer et al. (2023)—a breakdown in consistency that
signals deeper problems than mere capacity constraints. With manuscript submissions doubling every
15 years Larsen and von Ins (2010) and reviewers now handling 14 evaluations annually Díaz et al.
(2024), the system’s 15 million annual reviewing hours Aczel et al. (2021) are producing
increasingly unreliable outcomes.

Among peer review tasks, novelty assessment stands out as one of the most problematic Ernst et al.
(2021) Horbach and Halffman (2019). Novelty assessment requires reviewers to determine whether a
submission makes sufficiently original contributions by identifying what specific advances it makes
beyond existing work, evaluating whether these advances are significant enough to warrant
publication, and verifying that the authors have accurately characterized their contributions
relative to prior research. This knowledge-intensive process demands that reviewers maintain
comprehensive awareness of related work across their field and can precisely distinguish between
meaningful innovations and incremental modifications—a task that becomes exponentially more
difficult as publication rates accelerate and research domains specialize. Overwhelmed reviewers
often resort to superficial analyses, producing vague feedback like "not novel enough" without clear
justification. The challenge compounds when reviewers encounter papers outside their specific
expertise, leading to either overly conservative rejections or inadequate assessments that fail to
catch incremental work Kuznetsov et al. (2024).

Recent advances in large language models present an unprecedented opportunity to address these
novelty assessment challenges at scale. These breakthrough technologies have revolutionized text
processing and demonstrated remarkable performance across knowledge-intensive tasks Raiaan et al.
(2024), with recent technical advancements expanding capabilities to specialized reasoning and
efficient inference Li et al. (2024); Zhang et al. (2025).

While recent LLM advances create this opportunity, no existing work specifically addresses novelty
assessment as a dedicated task within the peer review process. Prior research incorporates novelty
evaluation within idea generation pipelines Radensky et al. (2024); Lu et al. (2024); Li et al.
(2025), generates peer reviews with novelty assessments occurring as a result of them existing in
peer reviews from training data Idahl and Ahmadi (2025); D’Arcy et al. (2024), or adds novelty
assessment steps to review synthesis pipelines for improvement Zhu et al. (2025). However, these
approaches either operate on synthetic ideas rather than real research contributions or fail to
evaluate novelty assessment capabilities in isolation. This represents a critical gap requiring
specialized methodologies for peer review novelty assessment.

To address this gap, we propose an end-to-end novelty assessment pipeline for peer review
submissions. Our approach consists of three stages: document processing and content extraction,
related work retrieval and ranking, and structured novelty assessment. The final stage implements
four sequential steps: novelty related content selection from the submission pdf, building
comprehensive understanding of related work from retrieved papers, comparing claimed novelty against
the comprehensive analysis from the prior step, and generating a summary with cited evidence from
the comparison. This pipeline operates on real research papers and directly evaluates novelty
assessment capabilities, addressing the limitations of existing approaches. Importantly, we conduct
the first evaluation of LLMs for novelty assessment using actual human data, including annotated
novelty assessment statements, and provide comprehensive evaluation across multiple dimensions.

#### Research Questions and Contributions

This work aims to address the following research questions:

- How does our human-informed novelty assessment pipeline compare to existing approaches?

- How well do our assessments align with human reviewer preferences across key evaluation
  dimensions?

- Can automated evaluation reliably substitute for human judgment in assessing novelty assessment
  quality?

Our contributions are threefold:

- Human Analysis Dataset and Insights: A systematically curated dataset of 182 papers with annotated
  human novelty assessments from ICLR 2025, along with empirical insights into expert reviewer
  reasoning patterns, evaluation criteria, and argument structures that inform AI system design for
  novelty assessment.

- Human-Informed Pipeline: A literature-grounded pipeline that incorporates insights from human
  novelty assessment practices, featuring structured prompting strategies and targeted content
  extraction informed by observed expert reviewer behavior.

- Comprehensive Evaluation and Analysis: Systematic comparison of our human-informed approach
  against existing baselines and human reviewers, with fine-grained evaluation across multiple
  dimensions and validation of automated assessment methods.

> Figure 1: Automated novelty assessment pipeline. The system processes manuscripts through three
> stages: (1) Document Processing extracts content using GROBID, (2) Related Work Discovery
> identifies and ranks relevant papers via embedding similarity and LLM reranking, and (3) Novelty
> Assessment performs structured analysis to generate evidence-based novelty evaluations.

## 2 Related Work

#### AI-Assisted Peer Review Systems

Our work is positioned at the peer review stage of scientific research, where our system operates
when a manuscript is submitted for evaluation. While previous works D’Arcy et al. (2024) Idahl and
Ahmadi (2025) Zhu et al. (2025) Chitale et al. (2025) Chang et al. (2025) Nemecek et al. (2025) have
developed end-to-end peer review generation pipelines that may implicitly include novelty assessment
steps, we are the first to focus specifically on building a dedicated pipeline for novelty
assessment and the first to systematically evaluate LLMs on this task. A related line of work
operates at the ideation stage of research Radensky et al. (2024) Shahid et al. (2025) Li et al.
(2025) Lu et al. (2024), developing pipelines for research idea generation that aim to improve
novelty through feedback loops from a novelty assessor. In contrast, we operate at a more mature
stage where ideas have been fully executed and comparative analyses are well-formulated. The
evaluation in ideation-stage works focuses on synthetic ideas that are typically abstract and
loosely defined, whereas we evaluate concrete, polished research contributions that have undergone
the refinement process of execution and manuscript preparation.

#### Scientific Literature Analysis & Retrieval

Our work employs an extensive related work discovery pipeline that collects papers cited within the
submission and additionally retrieves related papers by querying with prompts generated by GPT-4.1.
Papers are then ranked using an embedding-based method and reranked using RankGPT. We adapt this
general approach from existing work Radensky et al. (2024)Shahid et al. (2025)Li et al. (2025) with
modifications to ranking and filtering for our specific task. Similar retrieval-rank-rerank
pipelines have been used for related work generation Agarwal et al. (2025). Another retrieval
approach is OpenScholar Asai et al. (2024), which uses an LLM-RAG based approach to answer
scientific queries by identifying relevant passages from 45 million open-access papers. Works like
DeepReviewer Zhu et al. (2025) incorporate OpenScholar for novelty validation. However, our primary
criticism of OpenScholar for novelty assessment is that it provides only generic comparisons rather
than the granular analysis across methodology, problem formulation, evaluation approaches, and
novelty claims that our task requires.

#### Evaluation of LLM Generated Text

Prior works evaluating generated peer reviews have adopted either quantitative evaluations, where
they compare LLM-assigned scores (such as Overall Score, Soundness, etc.) against human-assigned
scores on review forms, or qualitative evaluations using traditional metrics like BERTScore Zhang et
al. (2020), ROUGE Lin (2004), and BLEU Papineni et al. (2002), or more recent approaches like
LLM-as-Judge Zheng et al. (2023). We adopt the LLM-as-Judge approach for our evaluation. Notably, no
prior work has specifically evaluated LLM performance on novelty assessment as a dedicated task,
making our evaluation framework the first of its kind.

Dataset Scale: Our dataset comprises 182 papers and 352 reviews, which is comparable to or larger
than datasets used in related peer review research: Du et al. (2024) use 100 papers with 380
reviews, Kennard et al. (2022) label review data sourced for 188 papers, Hua et al. (2019) work with
400 reviews, and Chamoun et al. (2024) evaluate on 300 reviews. Novelty assessment requires careful
manual annotation of scattered novelty discussions across reviews, making large-scale annotation
resource-intensive. Following established practice in peer review analysis, we prioritize annotation
quality over quantity, ensuring each example receives thorough annotation.

## 3 Methodology

### 3.1 Human Analysis for Prompt Design

To understand human novelty assessment, we analyzed ICLR 2025 reviews, which explicitly require
novelty evaluation in dedicated sections. We sourced submissions from OpenReview and used
keyword-based search for terms including "novel", "original", "research gap", "innovation",
"incremental", "prior work", and "existing work". Papers were ranked by: (1) reviews with >4 novelty
keywords, (2) consistent novelty discussion patterns, and (3) total review count. We selected the
top 200 papers. To expedite annotation, we used GPT-4o mini for sentence-level classification to
identify novelty discussions, which a human annotator then verified and refined by selecting all
sentences containing actual novelty assessments. This annotation process revealed that 18 papers
(9%) contained limited genuine novelty assessments—often keyword matches referring to paper
components rather than evaluation. The remaining 182 papers formed our analysis dataset. We
identified recurring patterns in reviewer reasoning, evaluation criteria, and argument structures,
focusing on how reviewers structure arguments, prioritize evidence, and compare submissions to prior
work. The four key patterns were identified through an exploratory qualitative review, where the
primary author examined novelty-related review segments, allowing patterns to emerge inductively
through close reading and thematic analysis. This analysis revealed several key patterns in how
expert reviewers assess novelty:

Verification over acceptance: Rather than accepting author claims at face value, reviewers
independently verify relationships with prior work and critically examine how authors characterize
related research, often distinguishing between author framing and actual technical relationships.
Our prompt explicitly instructs models to "independently verify relationships" and "distinguish
between author-claimed differences and independently observed differences," mirroring this critical
verification approach, as shown in Figures 9 and 10.

Variable granularity: Reviewers assess contributions with varying detail—some providing global
novelty assessments while others examine each contribution separately against relevant prior work.
(We address this through the "Contribution Delta Analysis" section that systematically examines each
claimed contribution individually against the most similar prior work, ensuring comprehensive
coverage regardless of author presentation style, as detailed in Figure 10.)

Different analytical lenses: Some reviewers focus on methodological innovations while others
evaluate systems holistically, calibrating expectations based on field maturity. Our prompt
incorporates multiple analytical perspectives through separate sections for research positioning,
methodological relationships, and field context considerations that help calibrate novelty
expectations based on area maturity, shown across Figures 9 and 10.

Gap identification: Reviewers systematically identify gaps in related work discussions and
distinguish between implementation-level improvements and genuine conceptual advances. (The "Related
Work Considerations" section specifically instructs models to identify missing comparisons and
assess whether improvements stem from "implementation details rather than conceptual advances,"
directly addressing this reviewer behavior in Figure 10.) These insights informed both our prompt
task design and the input to the LLM.

### 3.2 Our Approach

#### Overview

Our pipeline processes submission PDFs and generates structured novelty assessments through three
stages (Figure 1): (i) Document Processing extracts key content from submissions, (ii) Related Work
Discovery identifies and ranks relevant prior work, and (iii) Novelty Assessment performs
comparative analysis to generate evidence-based novelty evaluations.

### 3.3 Stage 1: Document Processing

We extract structured content from submission PDFs using GROBID https://github.com/kermitt2/grobid
to obtain titles, abstracts, bibliographies, and citation contexts required for subsequent stages.

### 3.4 Stage 2: Related Work Discovery

This stage identifies and ranks related work through a multi-step retrieval pipeline designed to
capture both explicitly cited works and potentially relevant uncited research.

#### Cited Work Processing

Bibliography entries are matched against Semantic Scholar to obtain standardized metadata (title,
abstract, authors, publication date, venue) for consistent downstream processing.

#### Uncited Work Discovery

To identify relevant work not cited by authors, we generate 5 keyword queries using GPT-4.1 and
search Semantic Scholar. Results are filtered to remove exact title matches with the submission
(avoiding potential preprints) and papers published after the submission date.

#### Embedding-based Ranking

We generate embeddings for all collected papers using SPECTER v2 Singh et al. (2023) on concatenated
titles and abstracts. Papers are ranked by cosine similarity to the submission’s embedding to
identify semantically similar work.

#### LLM-based Reranking

To prioritize papers with conceptual rather than purely semantic similarity, we employ LLM-based
reranking Sun et al. (2023b, a) with prompts emphasizing methodological approaches, novelty claims,
and problem statements. We select the top-K (k=20) papers for novelty assessment.

#### Content Extraction

For selected papers, we retrieve PDFs through a hierarchical search across Semantic Scholar, ACL
Anthology, and arXiv. Retrieved papers are processed using MinerU Wang et al. (2024); He et al.
(2024) to extract introduction sections, with Nougat OCR Blecher et al. (2024) as fallback for
processing failures. We use these tools for OCRs here as they output more accurate OCRs and we will
be using this paper content in the next stage.

### 3.5 Stage 3: Novelty Assessment

We use GPT-4.1 OpenAI (2024) for its improved instruction-following capabilities. This stage
consists of four sequential steps.

#### Structured Extraction

Processing retrieved papers as raw text creates context optimization challenges that degrade LLM
performance. Recent research demonstrates that model performance consistently degrades with
increasing input length, even when task complexity remains constant Hong et al. (2025). This occurs
because either overwhelming models with unrelated information reduces accuracy Zhu et al. (2025);
Idahl and Ahmadi (2025) or insufficient context through heavy truncation limits understanding
Radensky et al. (2024).

We extract six structured components aligned with novelty assessment requirements from each paper’s
title, abstract, introduction: (i) Methods, (ii) Problems addressed, (iii) Datasets, (iv) Results,
(v) Evaluation approaches, and (vi) Novelty Claims. This preserves essential information while
reducing context length to mitigate the performance degradation observed with longer, unstructured
inputs (Figure 7).

Landscape Analysis Expert reviewers possess comprehensive domain knowledge of established
benchmarks, techniques, metrics, and recent developments in their areas. To approximate this
foundation, we incorporate a landscape analysis step that systematically organizes structured
components from retrieved related work. Using GPT-4.1, we perform cross-paper synthesis to identify
methodological clusters, trace problem evolution, map evaluation ecosystems, and establish technical
relationships (Figure 8). This produces a hierarchical organization of the research space with
explicit connections between related, competing, and complementary approaches, providing contextual
background for novelty assessment that mimics expert reviewers’ organized domain understanding.

#### Novelty Delta Analysis

This step performs comparative analysis between the submission and prior work using three inputs:
(1) the research landscape, (2) the submission’s claimed contributions, and (3) citation
contexts—sentences where the submission cites related work. Citation contexts reveal how authors
position their contributions, enabling verification of claimed distinctions versus rhetorical
framing. Using GPT-4.1 with prompts informed by our human analysis (Section 3.1), the system
implements key reviewer patterns: independent verification of author claims, variable granularity
examination of contributions, and identification of gaps in related work discussions (Figures 9 and
10).

#### Assessment Report Generation

The final step generates a concise paragraph long summary that appears similar to actual peer review
novelty assessments, enabling direct comparison with human-written assessments (Figure 11).

## 4 Evaluation

> Table 1: Distribution of papers and reviews with novelty discussions by ICLR 2025 decision
> outcomes

> Table 2: Summary of Reasoning Alignment, Conclusion Agreement, Positive Shift, and Negative
> Shift Metrics

### 4.1 Evaluation Data

The evaluation dataset comprises the same 182 annotated examples used during human prompt design.
For each example, we prompt GPT-4.1 with the human review and its corresponding annotated novelty
statements to generate a coherent assessment using the prompt in Figure 12. This synthesis step is
necessary because novelty-related comments in reviews are typically scattered rather than
consolidated. Direct concatenation of these fragments would introduce stylistic biases during
evaluation, as the fragmented human annotations would differ substantially in structure and
coherence from the unified assessments generated by our system. We therefore use the
GPT-4.1-synthesized assessments as our ground truth in evaluation. To assess the risk of potential
data leakage into GPT-4.1’s pre-training corpus, we examined our evaluation set of 182 ICLR 2025
submissions. Only 11 of these papers had appeared on arXiv prior to the model’s knowledge cutoff of
June 1, 2024.

### 4.2 Evaluation Methods

#### Automated Evaluation

Evaluating novelty assessment systems presents significant challenges due to the subjective and
knowledge-intensive nature of the task. What constitutes "novel" depends heavily on the evaluator’s
familiarity with the surrounding research landscape. Even when human reviewers reach similar novelty
conclusions, they may arrive at these decisions through different reasoning paths and evidence
bases.

Given these challenges, we employ an LLM-as-Judge framework using our style-normalized human novelty
assessments as ground truth. We evaluate AI-generated assessments across four key dimensions using
the prompts in Figures 13 and 14 with GPT-4.1 as our Judge:

Novelty Conclusion Alignment: Whether the AI assessment reaches similar novelty conclusions as human
reviewers.

Novelty Reasoning Alignment: Whether the AI’s reasoning process and justifications align with human
reviewer logic.

Prior Work Engagement: Whether the assessment demonstrates adequate engagement with relevant
literature rather than superficial analysis.

Depth of Analysis: Whether the assessment provides substantive, detailed evaluation rather than
surface-level observations.

These dimensions ensure that AI assessments not only align with human judgments but also meet
quality standards for thorough, evidence-based novelty evaluation. Our evaluation employs a
two-stage process to ensure consistency. First, we extract core judgments (key novelty strengths and
weaknesses) from human reviews using GPT-4.1 with the prompt in Figure 13. We perform this
extraction separately to establish stable reference judgments, as combining extraction with
evaluation would risk the LLM identifying different claims across comparisons. In the second stage,
we evaluate AI-generated assessments against these pre-extracted judgments using the prompt in
Figure 14. This evaluation quantifies four aspects: (1) judgment similarity, measuring whether the
AI identifies the same specific novelty aspects with confidence scores; (2) conclusion alignment,
checking whether bottom-line novelty sufficiency verdicts match; (3) prior work engagement,
categorized as None, Limited (1-2 citations), or Extensive (3+); and (4) depth of analysis, rated as
Surface Level, Moderate (1-2 aspects), or Deep (3+ detailed comparisons). Table 2 reports the
resulting alignment scores across these dimensions.

#### Human Evaluation

We validate our automated evaluation with three PhD students (two third-year, one first-year) in NLP
and AI for Science, all with multiple publications. They perform pairwise comparisons across the
same four dimensions, viewing side-by-side novelty assessments from humans, our system, and
baselines. We collect 100 total judgments: 25 shared samples per annotator (for agreement) and 25
unique samples each, sampled randomly. For each comparison, annotators choose A, B, Tie, or Unclear
and may optionally provide comments (Figures 5, 6). Table 7 reports moderate inter-rater agreement
(0.493–0.560) and fair kappa scores (0.287–0.368), consistent with the subjectivity of novelty
evaluation.

### 4.3 Baseline Methods

We compare our approach against three existing systems, adapting each for novelty assessment
evaluation.

#### Scideator Radensky et al. (2024)

Scideator includes a novelty classification module that uses GPT-4o with few-shot examples and task
definition to classify ideas as ’novel’ or ’not novel’. Originally designed for iterative idea
refinement, we adapt it by using paper titles and abstracts as input instead of nascent ideas.

#### OpenReviewer Idahl and Ahmadi (2025)

OpenReviewer generates comprehensive peer reviews using Llama-OpenReviewer-8B, trained on 79,000
expert reviews from top conferences. We extract novelty-related content from its outputs using the
same LLM-based approach applied to human reviews (Figure 12).

#### DeepReviewer Zhu et al. (2025)

DeepReviewer is a multi-stage review framework that combines literature retrieval done with
OpenScholar Asai et al. (2024) with evidence-based argumentation, powered by DeepReviewer-14B
trained on structured review annotations. We extract novelty assessments using the same approach as
OpenReviewer. Notably, DeepReviewer was trained on ICLR 2025 data, which includes our entire
evaluation dataset.

#### Adaptation of Baselines

Our groundtruth novelty assessments are extracted from human written reviews from the ICLR 2025 set
that we labeled earlier. These extracted novelty segments are then run via the style normalization
prompt in figure 12. Similarly both the DeepReviewer and OpenReviewer produced peer reviews are run
via this pipeline to extract novelty segments and compose a coherent novelty assessment and run
through the style normalization module. This is a fair adaptation as given these models are trained
on these peer review datasets and they should able to mimic the distribution of novelty assessments
found in these peer reviews. Given deepreviewer is trained on the data we are evaluating so even
reproducing their training data would be enough to score high on the evaluation set.

## 5 Results and Analysis

We evaluated each system by comparing its novelty assessments against human novelty assessments as
reference. For papers with multiple human reviewers, we also conducted human-vs-human comparisons to
establish a baseline. Table 2 presents the overall results.

### 5.1 Overall Performance

> Figure 2: Overall performance comparison between our system and three baseline systems based on
> human evaluation (n values indicates number of comparisons)

Our system significantly outperforms both AI baselines and the human-vs-human baseline. For
Reasoning Alignment, we achieve scores 44.1 and 35.9 percentage points higher than OpenReviewer
Idahl and Ahmadi (2025) and DeepReviewer Zhu et al. (2025), and 21.4 points above the human
baseline. For Conclusion Agreement, our system again leads all baselines, outperforming the nearest
human baseline by approximately 13 percentage points (Tables 9, 10, 11).

#### Sentiment Shift Analysis

We analyze Positive Shift (neutral/negative → positive sentiment vs. human reference) and Negative
Shift (the opposite). AI systems show optimistic bias, with DeepReviewer exhibiting high Positive
Shift. Our system shows lower Positive Shift than DeepReviewer, though OpenReviewer aligns most
closely with human rates. For Negative Shift, OpenReviewer mirrors humans’ critical tendency,
followed by DeepReviewer. Our approach achieves the lowest Negative Shift rate.

#### Depth and Prior Work Engagement

Our system achieves the highest scores for both dimensions, producing no surface-level analyses
unlike all baselines (Tables 4 and 5). This stems from our specialized multi-step pipeline targeting
novelty assessment, while other systems generate complete peer reviews where novelty is secondary.
OpenReviewer performs worst, lacking retrieval capabilities. DeepReviewer uses OpenScholar retrieval
but fails at comparative analysis. Human reviewers show high variance in engagement depth.

#### Human Evaluation Validation

> Table 3: Component Analysis: Incremental Contribution of Pipeline Components

Human evaluations validate our LLM-as-Judge framework. Our system wins 74% of comparisons against
OpenReviewer (Figures 2 and 3). Against DeepReviewer and human reviewers, win rates are lower (39%
and 36%), but high tie rates (30% and 41%) indicate comparable quality, with low loss rates
(16-26%). By dimension, Claim Substantiation and Analytical Quality achieve the highest win rates
(56% and 55%), while Novelty Decision shows the most ties (31%), suggesting similar conclusions
across approaches. These patterns align with automated results, supporting our evaluation
framework’s validity.

### 5.2 Analysis: Understanding Human Alignment Patterns

Our system’s higher agreement scores compared to human-human baselines warrant careful examination.
To investigate this, we analyzed papers with multiple human reviewers to understand the sources of
disagreement. We detail the analysis methodology in Appendix D.

#### Sources of Human Reviewer Variability

Qualitative analysis reveals several factors contributing to reviewer disagreement: Different
Evaluation Lenses: Reviewers often focus on different aspects of novelty. In submission Ipe4fMCBXk,
half the reviewers emphasized methodological contributions while others focused on application
novelty, leading to opposite conclusions from the same paper. Varying Domain Expertise: Reviewers’
background knowledge affects assessments. For instance, in a protein design paper, reviewers
familiar with the field’s history correctly identified prior work on recombination techniques, while
others assessed these as novel contributions. Assessment Granularity: Some reviewers provide
high-level judgments ("innovative approach") while others focus on specific technical details. This
variation in granularity contributes to disagreement even when reviewers might agree on underlying
facts.

#### The Role of Systematic Evaluation

Our system’s approach differs from human review in applying consistent evaluation criteria. It
evaluates multiple dimensions (methodology, application, prior work) for every paper, maintains
uniform depth of analysis across assessments, and applies consistent thresholds for novelty
judgments. This systematic approach may explain the alignment patterns: when human reviewers
disagree due to focusing on different aspects, our system’s comprehensive evaluation can align
partially with each perspective.

### 5.3 Component Analysis

Table 3 shows the incremental contribution of each pipeline component. Our human-informed prompt
design provides the largest gains (+40.7% reasoning, +46.8% conclusion), reflecting the importance
of structured evaluation criteria derived from our human analysis. Structured extraction adds
moderate improvements (+3.3% reasoning, +4.5% conclusion) but reduces overall computation costs and
time, while landscape analysis contributes minimally (+3.2% reasoning, -0.7% conclusion). The major
improvements come from the prompt design and this is an interesting finding as it shows that with
careful prompt design we are able to outperform the more complex method that underwent extensive
training.

We evaluate component contributions in our retrieval pipeline on 100 ICLR submissions (Table 6). The
full pipeline combines keyword search with cited papers, ranks results by SPECTER2 embedding
similarity, and applies GPT-3.5 reranking. Without LLM reranking (embeddings only), we achieve 71%
overlap at top-10 with the full pipeline. When considering only keyword search (excluding
citations), overlap drops to 32%, indicating that author citations provide crucial relevance signals
beyond keyword matching.

## 6 Conclusion

We present a human-informed pipeline for automated novelty assessment in peer review, addressing a
critical gap in AI-assisted review systems. Our approach combines systematic related work retrieval
with structured evaluation criteria derived from analysis of expert reviewer patterns. Experimental
results demonstrate that our system outperforms existing AI baselines and achieves higher agreement
rates than human-human comparisons across key evaluation dimensions.

Our approach demonstrates that careful prompt design can achieve strong performance without
requiring extensive model training. This is a strength of our method. While methods that attempt
training Zhu et al. (2025); Idahl and Ahmadi (2025) require substantial computational resources
(e.g., 8× H100 80G GPUs for 23,500 steps at 256K context), whereas our prompt-based approach
achieves strong performance while offering greater computational efficiency.

## Limitations

Despite achieving strong performance, our system has several important limitations:

Evaluation Scope: Our evaluation focuses on computer science papers from ICLR 2025. The system’s
performance on other scientific domains remains untested and likely requires domain-specific
adaptations.

Consistency vs. Diversity: While our analysis shows that systematic evaluation reduces reviewer
disagreement, this consistency might eliminate valuable diversity in perspectives. The 35-40%
human-human disagreement rate may reflect legitimate differences in expertise and viewpoint rather
than mere inconsistency.

Nuanced Novelty: Breakthrough ideas often challenge conventional evaluation criteria. Our system’s
consistent approach might miss paradigm-shifting contributions that human experts would recognize
through intuition or deep domain expertise.

Language Scope: Our study evaluates the system only on English‐language manuscripts and reviews. As
a result, we cannot claim that the approach generalizes to submissions written in other languages or
rooted in different academic conventions; assessing cross-lingual performance remains future work.

Human Analysis for Prompt Design: We acknowledge our approach of analysis of the selected data lacks
formal inter-rater reliability measures, but argue it was appropriate for this initial investigation
into an understudied phenomenon, with the patterns’ effectiveness ultimately validated through our
pipeline results.

Human Study: Our human evaluation is based on 100 pairwise comparisons with three expert annotators,
comparable to related work in peer review analysis (Yuan and Liu (2022): 40 papers; Chamoun et al.
(2024) 100 examples; Dycke et al. (2025): 20+ papers). While a larger sample would provide
additional confidence, novelty assessment requires in-depth domain expert annotators with deep
familiarity with the relevant literature, making extensive human evaluation resource-prohibitive.

## Acknowledgments

This work has been funded by the European Union (ERC, InterText, 101054961). Views and opinions
expressed are however those of the author(s) only and do not necessarily reflect those of the
European Union or the European Research Council. Neither the European Union nor the granting
authority can be held responsible for them. This work has also been co-funded by the LOEWE
Distinguished Chair “Ubiquitous Knowledge Processing”, LOEWE initiative, Hesse, Germany (Grant
Number: LOEWE/4a//519/05/00.002(0002)/81).

## References

- B. Aczel, B. Szaszi, and A. O. Holcombe (2021) A billion-dollar donation: estimating the cost of
  researchers’ time spent on peer review. Research Integrity and Peer Review 6 (1), pp. 14. External
  Links: Document, Link Cited by: §1.

- S. Agarwal, G. Sahu, A. Puri, I. H. Laradji, K. D. Dvijotham, J. Stanley, L. Charlin, and C. Pal
  (2025) LitLLM: a toolkit for scientific literature review. External Links: 2402.01788, Link Cited
  by: §2.

- A. Asai, J. He, R. Shao, W. Shi, A. Singh, J. C. Chang, K. Lo, L. Soldaini, S. Feldman, M. D’arcy,
  D. Wadden, M. Latzke, M. Tian, P. Ji, S. Liu, H. Tong, B. Wu, Y. Xiong, L. Zettlemoyer, G. Neubig,
  D. Weld, D. Downey, W. Yih, P. W. Koh, and H. Hajishirzi (2024) OpenScholar: synthesizing
  scientific literature with retrieval-augmented lms. External Links: 2411.14199, Link Cited by: §2,
  §4.3.

- A. Beygelzimer, Y. N. Dauphin, P. Liang, and J. W. Vaughan (2023) Has the machine learning review
  process become more arbitrary as the field has grown? the neurips 2021 consistency experiment.
  External Links: 2306.03262, Link Cited by: §1.

- L. Blecher, G. Cucurull, T. Scialom, and R. Stojnic (2024) Nougat: neural optical understanding
  for academic documents. In The Twelfth International Conference on Learning Representations,
  External Links: Link Cited by: §3.4.

- E. Chamoun, M. Schlichtkrull, and A. Vlachos (2024) Automated focused feedback generation for
  scientific writing assistance. In Findings of the Association for Computational Linguistics: ACL
  2024, L. Ku, A. Martins, and V. Srikumar (Eds.), Bangkok, Thailand, pp. 9742–9763. External Links:
  Link, Document Cited by: §2, Limitations.

- Y. Chang, Z. Li, H. Zhang, Y. Kong, Y. Wu, H. K. So, Z. Guo, L. Zhu, and N. Wong (2025)
  TreeReview: a dynamic tree of questions framework for deep and efficient LLM-based scientific peer
  review. In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing,
  C. Christodoulopoulos, T. Chakraborty, C. Rose, and V. Peng (Eds.), Suzhou, China, pp.
  15662–15693. External Links: Link, Document, ISBN 979-8-89176-332-6 Cited by: §2.

- M. P. Chitale, K. M. Shetye, H. Gupta, M. Chaudhary, M. Shrivastava, and V. Varma (2025) AutoRev:
  multi-modal graph retrieval for automated peer-review generation. External Links: 2505.14376, Link
  Cited by: §2.

- M. D’Arcy, T. Hope, L. Birnbaum, and D. Downey (2024) MARG: multi-agent review generation for
  scientific papers. External Links: 2401.04259, Link Cited by: §1, §2.

- O. Díaz, X. Garmendia, and J. Pereira (2024) Streamlining the review process: ai-generated
  annotations in research manuscripts. External Links: 2412.00281, Link Cited by: §1.

- J. Du, Y. Wang, W. Zhao, Z. Deng, S. Liu, R. Lou, H. P. Zou, P. Narayanan Venkit, N. Zhang, M.
  Srinath, H. R. Zhang, V. Gupta, Y. Li, T. Li, F. Wang, Q. Liu, T. Liu, P. Gao, C. Xia, C. Xing, C.
  Jiayang, Z. Wang, Y. Su, R. S. Shah, R. Guo, J. Gu, H. Li, K. Wei, Z. Wang, L. Cheng, S.
  Ranathunga, M. Fang, J. Fu, F. Liu, R. Huang, E. Blanco, Y. Cao, R. Zhang, P. S. Yu, and W. Yin
  (2024) LLMs assist NLP researchers: critique paper (meta-)reviewing. In Proceedings of the 2024
  Conference on Empirical Methods in Natural Language Processing, Y. Al-Onaizan, M. Bansal, and Y.
  Chen (Eds.), Miami, Florida, USA, pp. 5081–5099. External Links: Link, Document Cited by: §2.

- N. Dycke, M. Zečević, I. Kuznetsov, B. Suess, K. Kersting, and I. Gurevych (2025) STRICTA:
  structured reasoning in critical text assessment for peer review and beyond. In Proceedings of the
  63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), W.
  Che, J. Nabende, E. Shutova, and M. T. Pilehvar (Eds.), Vienna, Austria, pp. 22687–22727. External
  Links: Link, Document, ISBN 979-8-89176-251-0 Cited by: Limitations.

- N. A. Ernst, J. C. Carver, D. Mendez, and M. Torchiano (2021) Understanding peer review of
  software engineering papers. Empirical Software Engineering 26 (5), pp. 103. External Links: ISSN
  1573-7616, Document, Link Cited by: §1.

- C. He, W. Li, Z. Jin, C. Xu, B. Wang, and D. Lin (2024) OpenDataLab: empowering general artificial
  intelligence with open datasets. External Links: 2407.13773, Link Cited by: §3.4.

- K. Hong, A. Troynikov, and J. Huber (2025) Context rot: how increasing input tokens impacts llm
  performance. Technical report Chroma. External Links: Link Cited by: §3.5.

- S. P. J. M. Horbach and W. Halffman (2019) The ability of different peer review procedures to flag
  problematic publications. Scientometrics 118 (1), pp. 339–373. Note: Epub 2018 Nov 29 External
  Links: Document, Link, ISSN 0138-9130 Cited by: §1.

- X. Hua, M. Nikolov, N. Badugu, and L. Wang (2019) Argument mining for understanding peer reviews.
  In Proceedings of the 2019 Conference of the North American Chapter of the Association for
  Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers), J.
  Burstein, C. Doran, and T. Solorio (Eds.), Minneapolis, Minnesota, pp. 2131–2137. External Links:
  Link, Document Cited by: §2.

- M. Idahl and Z. Ahmadi (2025) OpenReviewer: a specialized large language model for generating
  critical scientific paper reviews. In Proceedings of the 2025 Conference of the Nations of the
  Americas Chapter of the Association for Computational Linguistics: Human Language Technologies
  (System Demonstrations), N. Dziri, S. (. Ren, and S. Diao (Eds.), Albuquerque, New Mexico, pp.
  550–562. External Links: Link, ISBN 979-8-89176-191-9 Cited by: §1, §2, §3.5, §4.3, Table 2, §5.1,
  §6.

- N. N. Kennard, T. O’Gorman, R. Das, A. Sharma, C. Bagchi, M. Clinton, P. K. Yelugam, H. Zamani,
  and A. McCallum (2022) DISAPERE: a dataset for discourse structure in peer review discussions. In
  Proceedings of the 2022 Conference of the North American Chapter of the Association for
  Computational Linguistics: Human Language Technologies, M. Carpuat, M. de Marneffe, and I. V. Meza
  Ruiz (Eds.), Seattle, United States, pp. 1234–1249. External Links: Link, Document Cited by: §2.

- I. Kuznetsov, O. M. Afzal, K. Dercksen, N. Dycke, A. Goldberg, T. Hope, D. Hovy, J. K. Kummerfeld,
  A. Lauscher, K. Leyton-Brown, S. Lu, Mausam, M. Mieskes, A. Névéol, D. Pruthi, L. Qu, R. Schwartz,
  N. A. Smith, T. Solorio, J. Wang, X. Zhu, A. Rogers, N. B. Shah, and I. Gurevych (2024) What can
  natural language processing do for peer review?. External Links: 2405.06563, Link Cited by: §1.

- P. O. Larsen and M. von Ins (2010) The rate of growth in scientific publication and the decline in
  coverage provided by science citation index. Scientometrics 84 (3), pp. 575–603. External Links:
  Document, Link, ISSN 1588-2861 Cited by: §1.

- B. Li, Y. Jiang, V. Gadepally, and D. Tiwari (2024) LLM inference serving: survey of recent
  advances and opportunities. 2024 IEEE High Performance Extreme Computing Conference (HPEC), pp.
  1–8. External Links: Link Cited by: §1.

- L. Li, W. Xu, J. Guo, R. Zhao, X. Li, Y. Yuan, B. Zhang, Y. Jiang, Y. Xin, R. Dang, Y. Rong, D.
  Zhao, T. Feng, and L. Bing (2025) Chain of ideas: revolutionizing research via novel idea
  development with LLM agents. In Findings of the Association for Computational Linguistics: EMNLP
  2025, C. Christodoulopoulos, T. Chakraborty, C. Rose, and V. Peng (Eds.), Suzhou, China, pp.
  8971–9004. External Links: Link, Document, ISBN 979-8-89176-335-7 Cited by: §1, §2, §2.

- C. Lin (2004) ROUGE: a package for automatic evaluation of summaries. In Text Summarization
  Branches Out, Barcelona, Spain, pp. 74–81. External Links: Link Cited by: §2.

- C. Lu, C. Lu, R. T. Lange, J. Foerster, J. Clune, and D. Ha (2024) The AI Scientist: towards fully
  automated open-ended scientific discovery. arXiv preprint arXiv:2408.06292. Cited by: §1, §2.

- A. Nemecek, Y. Jiang, and E. Ayday (2025) The feasibility of topic-based watermarking on academic
  peer reviews. External Links: 2505.21636, Link Cited by: §2.

- OpenAI (2024) GPT-4.1 (june 2024 version). Note: https://platform.openai.com/Large language model
  Cited by: §3.5.

- K. Papineni, S. Roukos, T. Ward, and W. Zhu (2002) Bleu: a method for automatic evaluation of
  machine translation. In Proceedings of the 40th Annual Meeting of the Association for
  Computational Linguistics, P. Isabelle, E. Charniak, and D. Lin (Eds.), Philadelphia,
  Pennsylvania, USA, pp. 311–318. External Links: Link, Document Cited by: §2.

- M. Radensky, S. Shahid, R. Fok, P. Siangliulue, T. Hope, and D. S. Weld (2024) Scideator:
  human-llm scientific idea generation grounded in research-paper facet recombination. CoRR
  abs/2409.14634. External Links: Link, Document, 2409.14634 Cited by: §1, §2, §2, §3.5, §4.3, Table
  2.

- M. A. K. Raiaan, Md. S. H. Mukta, K. Fatema, N. M. Fahad, S. J. Sakib, Most. M. J. Mim, J. Ahmad,
  M. E. Ali, and S. Azam (2024) A review on large language models: architectures, applications,
  taxonomies, open issues and challenges. IEEE Access 12, pp. 26839–26874. External Links: Link
  Cited by: §1.

- S. Shahid, M. Radensky, R. Fok, P. Siangliulue, D. S. Weld, and T. Hope (2025) Literature-grounded
  novelty assessment of scientific ideas. In Proceedings of the Fifth Workshop on Scholarly Document
  Processing (SDP 2025), T. Ghosal, P. Mayr, A. Singh, A. Naik, G. Rehm, D. Freitag, D. Li, S.
  Schimmler, and A. De Waard (Eds.), Vienna, Austria, pp. 96–113. External Links: Link, Document,
  ISBN 979-8-89176-265-7 Cited by: §2, §2.

- A. Singh, M. D’Arcy, A. Cohan, D. Downey, and S. Feldman (2023) SciRepEval: a multi-format
  benchmark for scientific document representations. In Proceedings of the 2023 Conference on
  Empirical Methods in Natural Language Processing, H. Bouamor, J. Pino, and K. Bali (Eds.),
  Singapore, pp. 5548–5566. External Links: Link, Document Cited by: §3.4.

- W. Sun, Z. Chen, X. Ma, L. Yan, S. Wang, P. Ren, Z. Chen, D. Yin, and Z. Ren (2023a) Instruction
  distillation makes large language models efficient zero-shot rankers. External Links: 2311.01555,
  Link Cited by: §3.4.

- W. Sun, L. Yan, X. Ma, S. Wang, P. Ren, Z. Chen, D. Yin, and Z. Ren (2023b) Is ChatGPT good at
  search? investigating large language models as re-ranking agents. In Proceedings of the 2023
  Conference on Empirical Methods in Natural Language Processing, H. Bouamor, J. Pino, and K. Bali
  (Eds.), Singapore, pp. 14918–14937. External Links: Link, Document Cited by: §3.4.

- B. Wang, C. Xu, X. Zhao, L. Ouyang, F. Wu, Z. Zhao, R. Xu, K. Liu, Y. Qu, F. Shang, B. Zhang, L.
  Wei, Z. Sui, W. Li, B. Shi, Y. Qiao, D. Lin, and C. He (2024) MinerU: an open-source solution for
  precise document content extraction. External Links: 2409.18839, Link Cited by: §3.4.

- W. Yuan and P. Liu (2022) KID-review: knowledge-guided scientific review generation with oracle
  pre-training. Proceedings of the AAAI Conference on Artificial Intelligence 36 (10), pp.
  11639–11647. External Links: Link, Document Cited by: Limitations.

- D. Zhang, J. Xu, J. Zhou, L. Liang, L. Yuan, L. Zhong, M. Sun, P. Zhao, Q. Wang, X. Wang, X. Du,
  Y. Hou, Y. Ao, Z. Wang, Z. Gui, Z. Yi, Z. Bo, H. Wang, and H. Chen (2025) KAG-thinker: interactive
  thinking and deep reasoning in llms via knowledge-augmented generation. ArXiv abs/2506.17728.
  External Links: Link Cited by: §1.

- T. Zhang, V. Kishore, F. Wu, K. Q. Weinberger, and Y. Artzi (2020) BERTScore: evaluating text
  generation with BERT. In 8th International Conference on Learning Representations, ICLR 2020,
  Addis Ababa, Ethiopia, April 26-30, 2020, External Links: Link Cited by: §2.

- L. Zheng, W. Chiang, Y. Sheng, S. Zhuang, Z. Wu, Y. Zhuang, Z. Lin, Z. Li, D. Li, E. Xing, H.
  Zhang, J. E. Gonzalez, and I. Stoica (2023) Judging LLM-as-a-judge with MT-bench and chatbot
  arena. In Thirty-seventh Conference on Neural Information Processing Systems Datasets and
  Benchmarks Track, External Links: Link Cited by: §2.

- M. Zhu, Y. Weng, L. Yang, and Y. Zhang (2025) DeepReview: improving LLM-based paper review with
  human-like deep thinking process. In Proceedings of the 63rd Annual Meeting of the Association for
  Computational Linguistics (Volume 1: Long Papers), W. Che, J. Nabende, E. Shutova, and M. T.
  Pilehvar (Eds.), Vienna, Austria, pp. 29330–29355. External Links: Link, Document, ISBN
  979-8-89176-251-0 Cited by: §1, §2, §2, §3.5, §4.3, Table 2, §5.1, §6.

> Table 4: Reasoning Depth Distribution (Percentages)

> Table 5: Prior Work Engagement Distribution (Percentages)

> Table 6: Retrieval Pipeline Ablation Study

## Appendix A Data Analysis

### A.1 Sampling Methodology

Our sampling is sentiment-agnostic. We sample for novelty discussions (both positive and negative),
not specifically novelty issues. Our keywords ("novel", "contribution", "prior work", etc.) appear
in both types of assessments.

#### Empirical analysis of sentiment distribution

We analyzed the sentiment of novelty discussions in our dataset (352 reviews total) and found: 45
Positive, 234 Negative, 73 Mixed. While negative discussions are more prevalent (as expected, since
issues receive more attention in reviews), our data includes substantial coverage of positive and
mixed novelty assessments, demonstrating that our sampling captures the full spectrum of novelty
discussions rather than being biased toward issues only.

## Appendix B Human Evaluation Protocol: Novelty Assessment Comparison

### B.1 Task Design

We conducted a comparative evaluation where human evaluators assessed the quality of AI-generated
novelty assessments against expert-written reference assessments. Each evaluator compared pairs of
AI-generated assessments (labeled A and B) to a human expert’s gold-standard novelty review of the
same research paper.

### B.2 Evaluation Framework

#### Materials Provided

For each evaluation, evaluators received: (1) an expert-written gold-standard novelty review as
reference, (2) two novelty assessments (A and B) with system identities hidden.

#### Evaluation Dimensions

Evaluators assessed each pair across four dimensions. For each dimension, evaluators selected one of
four options: A wins, B wins, Tie (both equally good/poor), or Unclear (cannot determine).:

- Reasoning Alignment: Which assessment better captures the key novelty reasoning from the
  reference? Evaluators considered similarity of novelty claims, logical arguments, and focus areas.

- Decision Alignment: Which assessment reaches a novelty verdict most consistent with the reference?
  This included agreement on overall judgment (novel/incremental/mixed) and similar weighting of
  novelty factors.

- Claim Substantiation: Which assessment better supports its novelty claims with evidence?
  Evaluators looked for specific citations, concrete examples from the paper, and absence of
  unsupported generalizations.

- Analytical Quality: Which assessment provides more insightful technical analysis of novelty? This
  considered depth of technical discussion, specificity of analysis, and balanced consideration of
  strengths and limitations.

### B.3 Evaluation Guidelines

#### Instructions for Evaluators

Evaluators were instructed to read the reference assessment thoroughly before evaluating A and B,
evaluate each dimension independently, and base judgments on substantive content rather than
stylistic differences. They allocated 4–7 minutes per example to ensure thorough evaluation and
flagged ambiguous cases with explanatory comments when necessary.

#### Evaluation Focus

Evaluators were instructed to prioritize substance and accuracy of novelty reasoning, alignment with
reference judgments (particularly for Dimensions 1–2), quality and depth of technical analysis
(particularly for Dimensions 3–4), and specific evidence and citations supporting claims. They were
instructed to disregard writing style, grammar, or formatting differences; suggestions for paper
improvement unrelated to novelty; minor phrasing variations with equivalent meaning; and length
differences if content quality was comparable.

### B.4 Implementation Details

#### Evaluation Platform

The evaluation was conducted through a custom web interface presenting materials in a standardized
format (see Figures 5 and 6). Each evaluator received a unique evaluator ID, 50 randomly assigned
paper-assessment pairs, and the ability to save progress and flag unclear cases.

#### Quality Control

We calculated inter-evaluator agreement using Cohen’s kappa reported in Table 7.

#### Data Collection

Completed evaluations were submitted as structured JSON files containing dimension-wise selections
(A/B/Tie/Unclear), time spent per evaluation, and comments for flagged cases.

> Table 7: Inter-Rater Reliability Metrics Across Categories

## Appendix C Output Examples

Output of our pipeline can be seen in Tables 9, 10 and 11. It is quite evident that our system
aligns better with the human as compared to the baselines across all four dimensions.

## Appendix D Understanding Human alignment patterns

#### Pattern Analysis

We analyzed 45 papers where multiple human reviewers reached different novelty conclusions. This was
determined from the LLM as judge results we received during evaluation. In a human-AI collaborative
setup, we first iteratively examined review pairs to identify recurring disagreement patterns, then
developed categories along two observable dimensions: (1) focus divergence - what aspects reviewers
discussed (methods, applications, results, prior work, etc.), and (2) assessment granularity - their
level of analytical detail (high-level vs detailed). We then used Claude Code to perform
side-by-side comparative reading and categorization of all 45 review pairs according to these
predefined categories. Our analysis revealed the patterns: 62.2% of cases (28/45) showed granularity
differences with one reviewer providing detailed component-level analysis while another gave
high-level assessment, and 75.6% of cases (34/45) showed focus differences with reviewers evaluating
different aspects of the work.

#### Misrepresentation of Novelty

Additionally we manually reviewed 10 generated outputs from the novelty-delta-analysis stage to
interpret where does the misrepresentation of novelty arise from, we analyzed the structure and
reasoning patterns. We found that the system’s primary mode of analysis involves evaluating how
authors characterize their contributions relative to cited works, using the citation contexts from
the paper. When relevant uncited work is identified, the system flags it for additional comparison
but bases its core novelty assessment on the cited literature where authors’ explicit positioning is
available. This pattern reveals that most identifiable novelty overstatement arises from inadequate
differentiation from already-cited work. Because we have access to authors’ own citation contexts,
we can directly evaluate whether their novelty claims hold up against how they characterized prior
work. In contrast, for uncited works, we can identify potential gaps but lack the authors’ explicit
framing of the novelty relationship, making these better suited for clarification during rebuttal
rather than definitive assessment.

#### Factuality Analysis

LLMs are known to hallucinate references, which is precisely why our pipeline is specifically
designed to be grounded through an extensive multi-step retrieval pipeline with multiple reranking
stages. Each related paper alongside the submission is also used in our pipeline. To directly
address whether our system’s citations accurately support the conclusions or occasionally introduce
factual inconsistencies, we conducted a systematic manual verification study.

We randomly sampled 50 factual claims from our novelty delta analysis outputs. Each claim was
manually verified against the actual paper. Claims were categorized as ACCURATE, PARTIALLY-ACCURATE,
INACCURATE, or CANNOT-VERIFY. As can be seen in table 8 that 96% of claims were accurate or
partially accurate. The 14 partially accurate claims typically involved minor discrepancies such as
incorrect author attribution (e.g., "Sun et al." instead of "Xu et al.") or year errors (e.g., 2024
instead of 2023), while the core method descriptions remained correct. Only 2 claims (4%) contained
substantive factual errors. One misattributing a paper’s domain (text vs. image attacks) and one
overstating a method’s historical significance.t

> Table 8: Verification Status Summary

> Table 9: Full novelty assessments from the human reviewer (reference), the Scideator baseline,
> and our proposed system. Key phrases are highlighted to show verdict alignment: positive novelty
> claims, limited/incremental novelty, comparative analysis, and critical issues.

> Table 10: Full novelty assessments from the human reviewer (reference), the DeepReviewer
> baseline, and our proposed system for the DuRND paper. Key phrases are highlighted to show
> verdict alignment: novel/valuable aspects, limited/incremental novelty, technical details, and
> overstated claims.

> Table 11: Full novelty assessments from the human reviewer (reference), the OpenReviewer
> baseline, and our proposed system for the Meta-Instructions in VLMs paper. Key phrases are
> highlighted to show verdict alignment: novel/strength claims, limited/incremental novelty, prior
> work comparison, and overstated claims.

> Figure 3: Performance breakdown across evaluation categories, aggregated across all baseline
> comparisons.

> Figure 4: Distribution of the number of reviews per paper. Most papers received 1 to 4 reviews.

> Figure 5: Screenshot of the custom-built interface used for human evaluation. Annotators
> compared AI-generated and human-written novelty assessments across multiple dimensions,
> including reasoning depth, prior work engagement, and conclusion alignment.

> Figure 6: Screenshot (2) of the custom-built interface used for human evaluation. Annotators
> compared AI-generated and human-written novelty assessments across multiple dimensions,
> including reasoning depth, prior work engagement, and conclusion alignment.

> Figure 7: Research Paper Information Extraction Prompt

> Figure 8: Research Landscape Analysis Prompt

> Figure 9: Novelty Delta Analysis for Reviewer Support - Part 1

> Figure 10: Novelty Delta Analysis for Reviewer Support - Part 2

> Figure 11: Reviewer Summary Prompt

> Figure 12: Novelty Assessment Normalization Prompt

> Figure 13: Core Novelty Judgment Extraction Prompt

> Figure 14: Reviewer Novelty Evaluation Prompt
