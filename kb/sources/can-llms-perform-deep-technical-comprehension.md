---
source: https://arxiv.org/abs/2607.11859
description: "Gauntlet study comparing independent expert-persona review plus disagreement-preserving synthesis against human and single-agent analysis of computer architecture papers"
captured: 2026-07-17
capture: pdf-read
genre: scientific-paper
type: kb/sources/types/snapshot.md
---

# Can LLMs Perform Deep Technical Comprehension of Computer Architecture Papers?

Author: Nishant Aggarwal, Ayushi Dubal, Sreeraj Kannakarankodi, Ian McDougall, Adarsh Mittal, Vishnu Ramadas, Noah Scott, Ranganath Selagamsetty, Weichu Yang, and Karthikeyan Sankaralingam
Source: https://arxiv.org/abs/2607.11859
Date: 2026-07-13

## Abstract

Can large language models perform deep technical comprehension of computer architecture papers--not summarization, but structured critique that names the core mechanism, surfaces buried assumptions, and connects a contribution beyond its own scope? We study Gauntlet, an open-source pipeline that analyzes a paper through five independent expert-persona reviewers and an adversarial synthesis stage. On 20 ISCA 2025 and HPCA 2026 papers, ten researchers each wrote their own analyses and then judged, for papers other than their own, the human analysis against Gauntlet's. Across the 20 comparisons evaluators preferred Gauntlet in 15 (human in 4, one tie); its advantage is significant on per-analyst totals (paired Wilcoxon, p < 0.01) and largest on Critical Rigor, vanishing only on Calibration. Where humans win, it is on trust and usefulness rather than depth: a confident wrong claim, a mechanism described but not taught, or unprioritized breadth. A 98-paper automated ablation shows the gain comes from the multi-agent structure--the pipeline beats the same model run as a single rich-persona agent on 96% of papers--and specifically from its synthesis pass. We release all analyses, scores, and the rubric as a community resource.

Index Terms--Large language models, scientific paper comprehension, multi-agent systems, evaluation methodology.

## I. Introduction

Keeping pace with the computer architecture literature is increasingly hard. ISCA, MICRO, and HPCA 2025 alone added more than a hundred papers across near-memory processing, accelerators, coherence, security, and ML compilation. Authors often compare against favorable baselines and leave key assumptions implicit, so a paper's real contribution can be hard to extract. Readers have little help beyond summarization, which condenses a paper without teaching it. Understanding a paper well enough to critique, build on, or teach it requires naming four things: the precise structures it builds, the non-obvious insight that makes the mechanism work, the evaluation assumptions, and the connections to related work. We call this deep technical comprehension and ask: can large language models perform it, at a level comparable to trained human researchers?

**Approach.** Simply asking a frontier model to "deeply comprehend this paper" does not get you there. A single-shot analysis reads well but misses the mechanism, as our ablation shows (Section V-B). Two ideas close the gap, and they are the core of this paper. First, several expert perspectives read a paper better than one; each catches concerns the others miss. Second, those perspectives are formed independently and then combined by a synthesis step that preserves their disagreements rather than averaging them away. We implement both in our tool Gauntlet as multi-perspective independent review followed by adversarial synthesis. Five reviewer agents analyze the paper independently (a microarchitecture specialist, a workload and evaluation analyst, a simulation-tools auditor, and two domain specialists matched to the paper's sub-topics from a ~90-persona library), and a synthesizer then integrates them (Section III). All analyses use Claude Opus 4.5.

**Findings.** Ten graduate-student researchers each analyzed two papers. Each then judged, on papers other than their own, the human analysis against Gauntlet's across five dimensions. Across 20 comparisons, evaluators preferred Gauntlet in 15 (human in 4, one tie). The advantage is significant on per-analyst totals (p < 0.01, paired Wilcoxon), largest on Critical Rigor, and vanishes only on Calibration. The four human wins turn on trust and usefulness, not analytic depth: a confident wrong claim, a mechanism described but not taught, breadth without prioritization. A 98-paper automated ablation confirms the quality comes from the multi-agent structure, and specifically its synthesis pass: the pipeline beats the same model run as a single rich-persona agent on 96% of papers.

**Framing.** We do not claim reading a paper is unnecessary. The learning that reading produces has no substitute. The claim is narrower: a multi-perspective pipeline produces a first-pass analysis good enough to take seriously for triage, for crossing into unfamiliar subdomains, and as a teaching aid. The finding is not that LLMs are smarter than humans. It is that multi-perspective synthesis catches what single-perspective reading--human or LLM--reliably misses.

**Is this architecture research?** One might argue, this as an ML paper, an "LLM-usage" paper, or "just a prompt." We see it differently, on two grounds. First, in an era of reasoning-capable models, how one elicits expert-level analysis is itself a research question. The leverage is not generic prompting but encoded domain knowledge: only a computer architect knows to instantiate a reviewer that stress-tests benchmark selection, an auditor that probes simulator fidelity, and the topic-matched specialists that sharpen a critique. Output quality tracks the architectural expertise built into the pipeline. Second, applying generative AI to architecture tasks is now an active line of work [1], [2], and CAL has long published tools papers [3]. In that tradition, this is a tools contribution: an instrument for reading the field's own literature. A secondary finding reinforces this: even with carefully engineered single-agent prompts, multi-agent runs remain necessary for high-quality analysis (Section V-B). The contribution is an architecture, not a clever prompt.

University of Wisconsin-Madison and NVIDIA Research.

## II. Related Work

**LLM feedback on scientific papers.** Liang et al. [4] found GPT-4 review comments overlap human reviews by 30-39%, comparable to the 28-35% overlap between two humans. Thakkar et al. [5], in a 20,000-review randomized study at ICLR 2025, showed that reviewers given LLM feedback wrote longer, more informative reviews. A parallel line estimates that 6.5-16.9% of recent ML review text was substantially LLM-modified [6]. These establish that LLM feedback is useful and already pervasive. We ask a narrower question: whether an LLM can perform deep technical comprehension of mechanism papers. We compare multi-agent against single-agent designs, rather than measuring LLM assistance to human reviewers.

**Benchmarking architectural knowledge.** QuArch [7] contributes an expert-curated question-answering benchmark for computer architecture, establishing a rigorous way to measure whether models grasp the field's concepts. Our study is complementary: rather than probing knowledge with targeted questions, we examine open-ended, generative comprehension of individual papers--the mechanism reconstruction and critique a researcher performs while reading. We see the two as companions along different axes--curated knowledge on one and paper-specific reasoning on the other--and the strong architectural knowledge that QuArch measures is a natural foundation for the deeper reading we study.

**Multi-agent and multi-persona prompting.** Multi-agent debate improves factuality and reasoning by having instances critique one another over rounds [8], while Solo Performance Prompting has a single model simulate multiple personas [9]. Both let agents influence each other during generation. The closest precedent is MARG [10], which splits a paper's sections across agents to beat context limits and cuts generic comments from 60% to 29% versus a single-agent GPT-4 baseline. We instead distribute perspectives: each reviewer reads the whole paper from a distinct expert viewpoint, fully independently. We then add an explicitly adversarial synthesis stage that preserves disagreement rather than merging it.

**LLM-as-judge.** Our ablation uses an LLM judge for pairwise comparison, a method characterized by Zheng et al. [11], who report over 80% agreement with human preferences alongside position, verbosity, and self-enhancement biases. We mitigate position bias with randomized order over three runs and use the judge only for the large-scale ablation (Section V-B), as a secondary instrument.

## III. The Gauntlet Comprehension Pipeline

Gauntlet reads a paper in two phases: independent multi-perspective review, then adversarial synthesis (Figure 1).

**Phase 1: independent expert reviews.** Five reviewer agents analyze the paper with no visibility into one another. Independence is deliberate, since shared context collapses distinct concerns into consensus and the most useful observations are smoothed away. Three agents are fixed: Dr. Microarch reverse-engineers the mechanism at the bit and structure level; Prof. Workloads stress-tests the evaluation and benchmark selection; Prof. Simtools audits simulation fidelity and reproducibility. Two more are chosen per paper: an initial call identifies the paper's sub-topics and matches them against a library of ~90 expert personas, instantiating the two closest--so a sparse-tensor paper draws a sparse-computation specialist rather than a generic reviewer.

**Figure 1.** The Gauntlet paper-reading pipeline. Five reviewer agents analyze the paper independently--three fixed domain-general reviewers and two specialists dynamically selected from the paper's sub-topics. A synthesizer then produces a structured reading guide, explicitly prompted to surface disagreements between reviewers rather than average them away.

**Phase 2: adversarial synthesis.** A synthesizer consumes all five reviews plus the paper and produces a consolidated reading guide organized around the same four questions used for the human analyses (Section IV): the mechanism (a whiteboard explanation), the key insight (why it works), the evaluation critique, and what the authors did not tell you. Its defining instruction is to preserve disagreement rather than average it: where the microarchitect admires a design the workloads reviewer distrusts, the synthesis surfaces the tension instead of resolving it.

**Why the structure matters.** A single LLM produces a fluent, accurate-sounding summary of almost any paper; the claim here is that multi-perspective synthesis yields qualitatively different output, because no single reader--human or model--simultaneously holds the bit-level mechanism, the benchmark methodology, and the simulation fidelity in mind. The pipeline instantiates these in parallel and extracts what becomes visible only in their comparison. We validate this with a three-way ablation (Section V-B): the ordering pipeline > persona > directive confirms the gain comes from structure, not prompt wording.

## IV. Experimental Design

**Corpus and analyses.** Ten graduate-student volunteers each analyzed two computer-architecture papers in their area, drawn from ISCA 2025 and HPCA 2026 and restricted to concrete mechanism papers. Each human analysis answered the same four questions Gauntlet does: mechanism, key insight, evaluation critique, hidden assumptions. All Gauntlet analyses used Claude Opus 4.5, whose May 2025 knowledge cutoff predates the proceedings, making this comprehension rather than retrieval.

**Evaluation protocol.** For each paper we paired the human analysis with the Gauntlet synthesis. The ten analysts (plus, in a few cases, a senior reader) judged papers they had not themselves analyzed, keeping the analyst and judge roles independent. Judges read each paper's abstract and introduction (10-15 minutes), then scored both analyses on five dimensions on a 5-point scale: Mechanistic Accuracy (is what was built described correctly?), Insight Depth (the non-obvious why), Critical Rigor (specific, genuine weaknesses), Calibration (appropriately confident, not wrong at full confidence), and Usefulness (would it prepare you for a meeting?). A pilot sixth dimension, Breadth, was dropped as redundant. Each judge also recorded an overall preference and a free-text justification.

**Open-label evaluation.** We intended to blind judges to which analysis was machine-generated, but a pilot showed Gauntlet's output trivially identifiable from its uniformity and completeness, and stylistic normalization did not hide it. Rather than claim a blinding we could not achieve, we disclosed the source. This is a real threat to validity, but its likely direction is conservative: architecture researchers' skepticism of automated analysis biases against Gauntlet, so the observed preference is more plausibly a lower bound than an inflation.

**Ablation arm.** To separate the multi-agent structure from the model, we generated two single-agent baselines with the same model: Study A (a one-sentence prompt) and Study B (a rich, skeptical computer-architect persona); the full pipeline is Study C. We ran all three over the full 98-paper corpus (80 ISCA 2025, 18 HPCA 2026; the 20 human-judged papers are a subset) and compared them pairwise with an automated judge--Gemini 3.1 Pro, blind, three randomized runs--reported separately as a secondary instrument (Section V-B).

## V. Results

From all 20 comparisons, the two papers each analyst handled are reported as two rounds of ten matched pairs ("Paper 1/2"). Evaluators preferred the Gauntlet synthesis in 15 of 20 cases and the human analysis in 4, with one tie (9:1 for Paper 1; 6:3 with one tie for Paper 2). Its mean total exceeded the human's by +4.2 and +3.6 points (of 25) across the two rounds, significant under a paired one-sided Wilcoxon test in both (p = 0.003, p = 0.008; Table I).

**Per dimension.** Two patterns are robust (Table I). Critical Rigor is the strongest and most consistent signal: it gains +1.1 in both rounds, the only dimension significant at p < 0.01 in both. Evaluators credit Gauntlet's specificity, naming missing baselines, untested regimes, and buried assumptions where human critiques stay generic (Fig. 2). This follows from its explicitly adversarial workloads and simulation reviewers. Calibration is the only dimension where humans and Gauntlet are statistically indistinguishable (p = 0.27, 0.63). It is also where Gauntlet's characteristic failure surfaces.

**Table I. Mean per-dimension and total scores (1-5 scale; total of 25), with paired one-sided Wilcoxon p-values (n = 10 per round).** Gauntlet leads on every dimension; the lead is significant on Critical Rigor in both rounds and never on Calibration.

| Dimension | Human | Gauntlet | Delta | p |
|---|---:|---:|---:|---:|
| Paper 1: Mechanistic Accuracy | 3.80 | 4.70 | +0.90 | 0.039* |
| Paper 1: Insight Depth | 3.90 | 4.70 | +0.80 | 0.059 |
| Paper 1: Critical Rigor | 3.80 | 4.90 | +1.10 | 0.002** |
| Paper 1: Calibration | 4.20 | 4.40 | +0.20 | 0.266 |
| Paper 1: Usefulness | 3.50 | 4.70 | +1.20 | 0.012* |
| Paper 1: Total (/25) | 19.2 | 23.4 | +4.2 | 0.003** |
| Paper 2: Mechanistic Accuracy | 3.80 | 4.50 | +0.70 | 0.057 |
| Paper 2: Insight Depth | 3.70 | 4.70 | +1.00 | 0.023* |
| Paper 2: Critical Rigor | 3.50 | 4.60 | +1.10 | 0.009** |
| Paper 2: Calibration | 4.30 | 4.40 | +0.10 | 0.625 |
| Paper 2: Usefulness | 3.80 | 4.50 | +0.70 | 0.063 |
| Paper 2: Total (/25) | 19.1 | 22.7 | +3.6 | 0.008** |

\* p < 0.05, \** p < 0.01.

Excerpt from Gauntlet's analysis of Qtenon, a quantum-classical accelerator (evaluation critique):

> "The comparison uses an Ethernet-connected FPGA (~10 ms latency, Table 1), but modern quantum systems (IBM, Google) use custom low-latency links, PCIe, or CXL at ~100 ns-1 us. A PCIe-attached baseline would shrink the reported 5000-6000x communication speedups to ~100-1000x."

**Figure 2.** A representative excerpt of Gauntlet's output. The critique reasons from the paper's stated Ethernet-FPGA baseline to what deployed systems actually use, then quantifies the effect on the headline result--generative technical reasoning about this paper's specific mechanism and evaluation.

### A. Where Humans Still Win

The four human-preferred cases and the one tie isolate what the pipeline fails to do. We examined all five against the papers and the evaluators' justifications. Even in the cases it lost, Gauntlet keeps its analytic edge: it wins Critical Rigor in four of the five and Insight Depth in three. Human wins turn on whether an analysis can be trusted and used, not on depth. They fall into three modes.

**Trust: a confident, wrong claim.** The only "human clearly better" verdict (MagiCache) turned on one sentence: Gauntlet asserted, at full confidence, that bit-line computation taxes every cache access by 60% (1.6 vs. 1.0 ns). A per-line "computing bit" gates the slow path, so ordinary reads stay at 1.0 ns. The dual-mode array is the paper's point. The evaluator scored Gauntlet higher overall (22 vs. 17) and called it the stronger review, yet preferred the human "clearly." A single wrong claim, stated precisely and confidently in a weakness section, voided trust. It was caught because the human reader had technical expertise.

**Teachability: mechanism told, not taught.** For Prophet and LLBP-X, the human won even though Gauntlet matched or led on the analytic dimensions. Gauntlet's mechanism description was correct but not self-contained. For LLBP-X, it leaned on undefined shorthand ("RCR," "CID 64") and figure references, prompting the verdict that "reading [the human review] is better than reading the paper." For Prophet, it gave a high-level gloss. The human instead walked through all three policies and recomputed the paper's reported 1.6% energy increase at a 35% speedup as a ~56% increase in power, exposing a misleading framing. A description the reader cannot rebuild the mechanism from fails the meeting-prep bar, even when accurate.

**Judgment: breadth without prioritization.** For LightML, Gauntlet's weakness list was comprehensive but untriaged: it set trivial points (an ADC power breakdown) beside load-bearing ones (an unvalidated simulator). The focused human review was preferred, and here over-coverage cost Gauntlet even Insight Depth and Critical Rigor. The Qtenon tie shows a related decomposition bias: Gauntlet detailed the hardware it could describe precisely but skipped the software contributions entirely, so it could not explain how the headline speedup arises. The human enumerated all seven hardware and software contributions.

### B. Ablation: Does the Multi-Agent Structure Matter?

The central claim is that the structure, not the model, drives quality. We compare three strategies on the same papers with the same model: A (a one-sentence directive), B (a rich, skeptical computer-architect persona), and C (the full pipeline). Because pairwise comparison needs more analyses than the human panel can score, an automated judge (Gemini 3.1 Pro, blind, three randomized runs) scores them over the full 98-paper corpus. The 20 human-judged papers are a subset. [1]

**Table II. Automated blind ablation over all 98 papers (Gemini 3.1 Pro, three runs; Delta is the score margin toward the winner, of 5).** The ordering C > B > A holds across both venues and every margin.

| Comparison | Winner | Win rate | Mean Delta |
|---|---|---:|---:|
| A vs. B (directive vs. persona) | B | 89% | 0.59 |
| A vs. C (directive vs. pipeline) | C | 99% | 1.04 |
| B vs. C (persona vs. pipeline) | C | 96% | 0.58 |

The ordering is unambiguous: C > B > A (Table II). A rich persona beats a bare directive on 89% of papers. The pipeline beats the directive near-unanimously (97/98) and, more tellingly, beats the strong persona on 94 of 98 (+0.58). Because B and C draw on overlapping persona expertise, this B<C result isolates the synthesis pass, the only thing C adds, as the source of the gain. The effect is not a small-sample artifact: a 22-paper pilot showed the same ordering, and scaling to 98 papers sharpened it (the B-vs-C win rate rose from 73% to 96%).

Where C's edge narrows is instructive, and mirrors Section V-A. The edge is contribution-shaped: widest on broad, multi-mechanism papers (zkSpeed -1.70, ArtMem and RAP -1.60), and narrowest, sometimes negative, on single-trick papers (a brain-computer-interface accelerator, a single-dataflow NeRF engine, and MemSOS, the lone paper where even the bare directive is competitive). When there is one idea to extract, a focused single reading captures it, and the ensemble only adds dilution.

[1] The ablation uses a six-dimension variant of the rubric; it is a secondary, machine-judged instrument.

## VI. Discussion and Data Release

**Data release.** We release all 20 human analyses, the matched Gauntlet syntheses, every score and justification, the rubric, the full Study A/B/C ablation reviews and blind-judge transcripts for all 98 corpus papers, and the complete pipeline, all at https://github.com/karusankaralingam/PARALLAX. The paired, multi-judge analyses are, to our knowledge, the first dataset for evaluating deep technical comprehension of architecture papers.

**Limitations.** Our analysts are graduate students, not senior researchers. Graduate students do most first-pass reading, so this is a realistic baseline, though not the strongest possible one. Judges and analysts are the same pool, so domain expertise varies across papers. The evaluation is also open-label (Section IV). All analyses use one model and configuration. The transferable contribution is the architecture, independent multi-perspective review plus disagreement-preserving synthesis, not the specific model.

**A teaching aid.** Reading and critiquing papers is a staple of architecture courses, yet the activity almost never receives substantive feedback. A student rarely learns whether they identified the core insight or missed the load-bearing weakness. A high-quality reference analysis is the missing answer key: a student can compare their own critique against Gauntlet's, not for a grade but to see what an expert ensemble surfaced. Our study makes this concrete: the baseline was graduate students at this task, and Gauntlet was competitive-to-preferred. The failure modes (Section V-A) are instructive too: spotting where the machine over-claims or misprioritizes is exactly the calibration and judgment that expert reading requires.

## References

1. K. Sankaralingam, "Computer architecture's AlphaZero moment: Automated discovery in an encircled world," arXiv:2604.03312, 2026.
2. Gupta et al., "ArchAgent: Agentic AI-driven computer architecture discovery," arXiv:2602.22425 [cs.AI], 2026.
3. L. Yan, X. Lu, X. Chen, Y. Han, and X.-H. Sun, "Pyramid: Accelerating llm inference with cross-level processing-in-memory," IEEE Comput. Archit. Lett., vol. 24, no. 1, p. 121-124, Jan. 2025.
4. W. Liang, Y. Zhang, H. Cao, B. Wang, D. Y. Ding, X. Yang, K. Vodrahalli, S. He, D. S. Smith, Y. Yin, D. A. McFarland, and J. Zou, "Can large language models provide useful feedback on research papers? a large-scale empirical analysis," NEJM AI, 2024.
5. N. Thakkar, M. Yuksekgonul, J. Silberg, A. Garg, N. Peng, F. Sha, R. Yu, C. Vondrick, and J. Zou, "Can LLM feedback enhance review quality? a randomized study of 20K reviews at ICLR 2025," Nature Machine Intelligence, 2026.
6. W. Liang, Z. Izzo, Y. Zhang, H. Lepp, H. Cao, X. Zhao, L. Chen, H. Ye, S. Liu, Z. Huang, D. McFarland, and J. Y. Zou, "Monitoring AI-modified content at scale: A case study on the impact of ChatGPT on AI conference peer reviews," in ICML, 2024.
7. Prakash et al., "QuArch: A question-answering dataset for AI agents in computer architecture. IEEE CAL 2025."
8. Y. Du, S. Li, A. Torralba, J. B. Tenenbaum, and I. Mordatch, "Improving factuality and reasoning in language models through multiagent debate," in ICML, ser. PMLR, vol. 235, 2024, pp. 11 837-11 860.
9. Z. Wang, S. Mao, W. Wu, T. Ge, F. Wei, and H. Ji, "Unleashing the emergent cognitive synergy in large language models: A task-solving agent through multi-persona self-collaboration," in NAACL. ACL, 2024.
10. M. D'Arcy, D. Downey, and T. Hope, "MARG: Multi-agent review generation for scientific papers," arXiv preprint arXiv:2401.04259, 2024.
11. L. Zheng, W.-L. Chiang, Y. Sheng, S. Zhuang, Z. Wu, Y. Zhuang, Z. Lin, Z. Li, D. Li, E. P. Xing, H. Zhang, J. E. Gonzalez, and I. Stoica, "Judging LLM-as-a-judge with MT-bench and chatbot arena," in NeurIPS, 2023.
