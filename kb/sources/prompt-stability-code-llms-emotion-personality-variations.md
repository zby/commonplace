---
source: https://arxiv.org/pdf/2509.13680
captured: 2026-03-11
capture: pdf-read
type: academic-paper
---

# Prompt Stability in Code LLMs: Measuring Sensitivity across Emotion- and Personality-Driven Variations

Author: Wei Ma, Yixiao Yang, Jingquan Ge, Xiaofei Xie, Lingxiao Jiang
Source: https://arxiv.org/pdf/2509.13680
Date: 17 Sep 2025

## Abstract

Code generation models are widely used in software development, yet their sensitivity to prompt phrasing remains under-examined. Identical requirements expressed with different emotions or communication styles can yield divergent outputs, while most benchmarks emphasize only peak performance. We present PromptSE (Prompt Sensitivity Evaluation), a framework that creates semantically equivalent prompt variants with emotion and personality templates, and that evaluates stability using probability-aware continuous scoring, or using binary pass rates when logits are unavailable. These results are aggregated into a proposed area-under-curve metric (AUC-E) for cross-model comparison. Across 14 models from three families (Llama, Qwen and DeepSeek), our study shows that performance and stability behave as largely decoupled optimization objectives, and it reveals architectural and scale-related patterns that challenge common assumptions about model robustness. The framework supports rapid screening for closed-source models as well as detailed stability analysis in research settings. PromptSE enables practitioners to quantify performance–stability trade-offs for deployment and model selection, positioning prompt stability as a complementary evaluation dimension alongside performance and fairness, and contributing to more trustworthy AI-assisted software development tools.

## 1 Introduction

Code generation models have become integral to software development but they exhibit a critical challenge: *prompt sensitivity*, substantial performance variations from semantically equivalent but differently phrased inputs. Consider a frustrated developer at 2 AM asking "I'm stuck on this recursive problem and need to find the longest increasing subsequence, any ideas?" versus a formal request "Implement a function that computes the length of the longest increasing subsequence in an array". While both seek identical functionality, the emotional context and communication style can trigger dramatically different model behaviors, with performance swings up to 40% reported for production systems. This instability undermines deployment reliability, evaluation comparability, and user trust.

This instability exposes important limitations in current evaluation approaches. While code generation evaluation has evolved to execution-based metrics like Pass@k, these methods capture only functional correctness. Recent works have begun studying prompt sensitivity from different angles. Cao et al. demonstrate that even LLMs experience over 45% accuracy swings between best and worst prompt phrasings for identical tasks. Chen et al. show how natural perturbations affect code generation such as typos while Guo et al. show that personality-aligned prompts can improve code generation pass rates, revealing how psychological factors influence model behavior. Razavi et al. introduce benchmarks for evaluating prompt sensitivity across various NLP tasks, though their focus remains on documenting performance variations rather than establishing unified stability metrics.

Existing studies examine prompt sensitivity through performance gains or losses, but none provide a principled framework to establish stability under natural expression variations such as emotional or stylistic changes. Practitioners therefore lack systematic tools to assess this fundamental reliability dimension in code generation models. We view prompt stability from a different perspective: **how can we systematically quantify and compare stability as a measurable model property?** Unlike Chen et al. who analyze performance drops, or Guo et al. who optimize for performance gains, we focus on establishing stability as a quantifiable evaluation dimension. We propose **PromptSE** (Prompt Sensitivity Evaluation), introducing an algorithm that transforms stability assessment into standardized, comparable metrics through our novel measurement methodology.

We evaluate 14 models across three architecture families (Llama, Qwen, DeepSeek) using HumanEval with semantically equivalent variants (14,760 in total). Each variant prompt generates 16 samples under uniform decoding, with statistical analysis employing robust methods including correlation tests, confidence intervals (CI), and false discovery rate (FDR) correction. Our study includes four research questions: (1) the relationship between performance and stability; (2) how perturbation magnitude affects sensitivity across model sizes and families; (3) whether PromptSELight approximates PromptSE; (4) how emotional factors affect performance and calibration. Our findings challenge conventional assumptions about code generation models. First, performance and stability are decoupled: models distribute across all four quadrants of the performance-stability space (Spearman ρ = −0.433, p = 0.122), enabling practitioners to optimize for specific requirements without automatic tradeoffs. Second, prompt stability exhibits non-monotonic scaling patterns, with smaller models (e.g., Qwen-1.5B) achieving superior stability (AUC-E 0.646) compared to larger models, suggesting stability requires explicit optimization beyond scale. Third, emotional prompting reveals model-specific vulnerabilities and confidence miscalibration patterns not captured by traditional benchmarks. Finally, our dual-pathway evaluation achieves reasonable consistency (PromptSELight vs PromptSE: Pearson is about 0.72), enabling both rapid screening and detailed analysis for deployment decisions.

**Contributions:**

1. *Methodological innovation*: The first systematic framework for quantifying prompt stability, moving beyond performance measurement to establish stability as a distinct evaluation dimension. Psychologically-grounded perturbation templates capture simulated developer communication patterns through emotional and stylistic variations.
2. *Technical advancement*: PromptSE, a probability-aware continuous evaluation metric that distinguishes high-confidence solutions from lucky guesses, and AUC-E, a standardized 0-1 stability measure enabling systematic cross-model comparisons. The unified algorithmic framework seamlessly accommodates both open-source and closed-source models through dual evaluation pathways.
3. *Empirical insights*: The first comprehensive stability landscape across 14 models and three major model-architecture families, revealing that performance and stability are decoupled optimization objectives and establishing reproducible protocols that challenge conventional scaling assumptions while informing practical deployment decisions.

## 2 Methodological Framework

We introduce **PromptSE** (Prompt Sensitivity Evaluation), a systematic framework for quantifying code generation model stability under prompt variations. Our core insight is to transform stability from an intuitive concept into a measurable model property through psychologically-grounded perturbations and probability-aware evaluation. Our approach generates semantically equivalent prompt variants through emotion and personality templates, then evaluates model sensitivity using probability-aware continuous scoring (PromptSE) or binary evaluation (PromptSELight) depending on model accessibility. The framework operates under strict semantic and interface invariance constraints, ensuring that all variants preserve computational requirements (e.g., preserving input-output constraints, and complexity bounds) and functional specifications. We employ structured psychological templates to systematically simulate how developers might express identical requirements under different emotional states and personality traits, enabling controlled stability assessment across diverse communication styles. Our evaluation pipeline computes elasticity curves across three perturbation distances (0.1, 0.2, 0.3), then aggregates them using proposed AUC-E for cross-model comparisons. This dual-pathway design ensures compatibility with both open-source models (with probability access) and closed-source APIs (binary-only evaluation). The framework consists of three core components:

1. *Emotion-aware variant generator*: Creates semantics-preserving prompt variants using psychological templates (emotion, personality) and perturbation strength controls.
2. *Sensitivity evaluation*: Implements PromptSE for probability-based analysis and PromptSELight for binary evaluation, measuring model sensitivity to prompt variations.
3. *Elasticity quantification*: Integrates sensitivity curves across perturbation distances to compute AUC-E for cross-model stability comparison.

### 2.1 Emotion-Aware Template-Based Variant Generation Method

We adopt a template-constrained design philosophy that translates interpretable psychological factors (emotion, personality) and perturbation strength into unified linguistic constraints for controlled, semantics-preserving rewriting. This approach prioritizes semantic preservation while introducing stylistic variations through controlled template libraries.

#### 2.1.1 Theoretical Modeling Foundation

To evaluate model sensitivity to prompt variants in realistic development contexts, we observe that developers express the same coding requirements differently based on their emotional states (such as frustration or excitement) and personality traits (such as communication style preferences). Contextual factors like task complexity and time pressure further influence how these psychological factors appear in prompt formulation. Our approach makes three key modeling choices:

- *Emotion as linguistic style signals*: We treat emotions as short-term style variations using the arousal and valence framework, creating identifiable emotion templates (such as focus, excitement, anxiety) with specific linguistic features and expression patterns.
- *Personality as stable baseline*: We represent personality through three dimensions (technical orientation, experience level, collaboration style) that serve as a consistent expression baseline, with emotions layered on top through weighting mechanisms.
- *Context-sensitive weighting*: We use task attributes (such as algorithmic complexity, collaboration needs, learning goals) to adjust the influence of emotion and personality factors while maintaining semantic preservation and technical requirements.

We formalize variant generation as follows: given an original prompt p, emotion template e, personality profile Π, and contextual conditions x, we generate a semantically equivalent variant v whose style reflects the constraints from (e, Π, x) with rewriting intensity controlled by distance d.

*Emotion State.* For programming contexts, we define eight core emotion states through structured templates: *focused, excited, confident, tired, calm, anxious, frustrated, and stressed*. Each emotion prompt template consists of three components:

> Emotion e = (description, language characteristics, expression pattern)

where *description* establishes the programmer's role and cognitive state, *language characteristics* defines preferred vocabulary and linguistic features, and *expression pattern* specifies sentence structures and communication styles.

*Personality Trait Profile.* We introduce a three-dimensional personality profile Π = (T, L, C), where T denotes the technical orientation, L the experience level, and C the collaboration style. The technical orientation dimension distinguishes between algorithm experts, pragmatic engineers, experimental innovators, and defensive conservatives. The experience level dimension separates junior explorers from senior architects, thereby capturing differences in accumulated expertise. The collaboration style dimension covers logic-driven, collaboration-oriented, plan-systematic, and adaptive-flexible tendencies.

#### 2.1.2 Template Library Design and Implementation

*Emotion State Template Library.* We organize eight emotion states: focused, excited, confident, tired, calm, anxious, frustrated, and stressed. Each emotion state follows the template structure defined in Equation 1, providing role setting, linguistic features, and expression patterns for controlled generation.

*Personality Trait Template Library.* We define personality profiles across three dimensions with distinct linguistic patterns. Technical Orientation (T) includes four types: Algorithm Expert, Pragmatic Engineer, Experimental Innovator, and Defensive Conservative. Experience Level (L) distinguishes Junior Explorers and Senior Architects. Collaboration Style (C) covers four approaches: Logic-Driven, Collaboration-Oriented, Plan-Systematic, and Adaptive-Flexible.

*Perturbation Strength Template.* The perturbation distance d controls rewriting intensity across three levels: d = 0.1 applies light lexical changes, d = 0.2 introduces moderate style adjustments, and d = 0.3 creates substantial transformation while preserving semantics.

#### 2.1.3 End-to-End Emotion-Aware Variant Generation

Given an original prompt p, target emotion e, personality profile Π, and perturbation distance d, our variant generation process outputs a candidate set V = {(v, e, Π, d)}, where each variant v is tagged with its generation parameters for complete traceability. The process operates across multiple distance levels D = {0.1, 0.2, 0.3} and generates K candidates per distance layer (we generate 30 variants per original prompt for each distance).

*Template Sampling and Configuration.* The process begins by sampling emotion and personality templates from the predefined libraries based on the specified (e, Π, d) configuration. This sampling strategy ensures diverse coverage while maintaining computational efficiency.

*Prompt Construction and Constraints.* The sampled template elements are translated into natural language generation instructions that guide the rewriting process. Critical to this stage is maintaining interface invariance: function signatures, type annotations, and import statements remain unchanged. Parameters without default values may be renamed for stylistic variation, while those with defaults must preserve both names and values.

*Candidate Generation and Validation.* The system generates multiple diverse candidates using controlled randomness and multi-style resampling. Generated candidates are then validated against structural and interface requirements to ensure they maintain functional equivalence.

*Metadata and Storage.* Each validated variant is annotated with its generation parameters (emotion, personality, perturbation distance) and stored in a hierarchical cache organized by dataset, original prompt, and distance layer.

### 2.2 Sensitivity Evaluation Methods: PromptSE and PromptSELight

To quantify model output stability under prompt perturbations and address the core challenge of performance fluctuations caused by natural expression variations, we propose two complementary evaluation methods within a unified direct difference framework. PromptSE provides comprehensive analysis with probability-aware scoring for research scenarios requiring fine-grained insights, while PromptSELight offers rapid evaluation suitable for closed-source models and industrial applications where quick stability assessment is essential.

#### 2.2.1 SoftExec: Probability-Aware Continuous Evaluation

Traditional Pass@k evaluation treats all passing solutions equally, ignoring the model's confidence in its outputs. To capture this probability information, we introduce SoftExec, a continuous evaluation method that weights correctness by the model's generation probability.

SoftExec computes a weighted correctness score where each generated code sample contributes proportionally to its likelihood under the model:

> Acc_soft(p) = Σ π̂_j · I[y_j ∈ P]

where π_j is the output probability and I[y_j ∈ P] indicates whether the sample passes all tests. To ensure numerical stability and meaningful comparisons, we apply softmax normalization across all m samples from the same prompt.

#### 2.2.2 PromptSE: Comprehensive Probability-Based Sensitivity Analysis

PromptSE provides the most detailed sensitivity analysis by leveraging sequence probabilities from open-source models. The method systematically compares original prompts with their perturbed variants using continuous SoftExec scores.

**Elasticity Calculation Principle.** The core insight of PromptSE is that prompt sensitivity can be quantified through the stability of continuous correctness scores. For a given prompt p and distance d, elasticity is computed as:

> Elasticity(p, d) = 1 − (1/|V_d^p|) Σ |Acc_soft(p) − Acc_soft(v)|

This formulation exhibits several desirable mathematical and interpretive characteristics. The elasticity measure provides intuitive interpretation through its bounded range ∈ [0, 1], where values approaching 1 indicate perfect stability and values near 0 represent maximum sensitivity to prompt perturbations.

#### 2.2.3 PromptSELight: Efficient Binary-Based Sensitivity Analysis

PromptSELight provides a computationally efficient alternative for scenarios where probability information is unavailable (closed-source models) or rapid evaluation is required. It uses binary pass rates instead of continuous scores while maintaining the same emotion-aware prompt variants as PromptSE.

> Elasticity(p, d) = 1 − |Pass(p) − Pass(d)|

where Pass(p) = (1/m) Σ I[y_j^p ∈ P] (original prompt pass rate) and ΔPass(d) = |Pass(0) − Pass(d)| represents the absolute difference in success rates.

PromptSELight offers significant practical advantages: computational efficiency by eliminating expensive log-probability calculations and enabling single-pass sampling with parallel execution. It provides broad applicability as a model-agnostic approach that works with any code generation system, including closed-source models and commercial APIs.

### 2.3 AUC-E: Area Under Curve of Elasticity

To provide a single, interpretable measure of overall prompt sensitivity, we introduce AUC-E (Area Under Curve of Elasticity). This metric aggregates elasticity measurements across all perturbation distances into a unified score, delivering a calibrated 0-to-1 stability scale that enables systematic comparison across models and datasets. AUC-E captures the intuition that a robust model should maintain consistent performance across a range of prompt perturbations.

*Elasticity Curve Construction.* For each prompt p and distance d, compute individual elasticity using the formulations from Equations 4 and 5. For PromptSE mode, average across all prompts to obtain the elasticity curve E(d). Second, average across all prompts for PromptSELight mode.

*AUC-E Computation.* For our three-distance evaluation setup (d ∈ {0.1, 0.2, 0.3}), we compute AUC-E using Simpson's rule: AUC-E = (1/6) × (E(0.1) + 4 × E(0.2) + E(0.3)). Higher values indicate better prompt stability, with values approaching 1.0 suggesting highly robust models and values near 0.0 indicating high sensitivity to prompt variations.

## 3 Evaluation

### 3.1 Research Questions

Four research questions:

- **RQ1.** How are performance and prompt stability jointly structured across the evaluated models and whether there is evidence of tradeoffs?
- **RQ2.** How does perturbation distance d shape sensitivity, and to what extent do model size and family moderate this effect?
- **RQ3.** Can PromptSELight approximate PromptSE, and where does the approximation break down?
- **RQ4.** How do valence × arousal conditions independently affect correctness and calibration, and what mechanism evidence supports these effects?

### 3.2 Tasks, Data, and Models

We use the Python HumanEval benchmark as the initial dataset. The total size of the enhanced dataset is 14,760. Inputs are standardized function signatures and task descriptions. Under semantic and interface invariance, we generate semantically equivalent natural language variants using the emotion and personality template system introduced in Section 2.1. Variants are produced at three perturbation distances d ∈ {0.1, 0.2, 0.3}. We generate 30 variants per original prompt per distance with random emotion combinations.

Our model set spans multiple families and ability ranges: Llama (CodeLlama-34b, CodeLlama-13b, CodeLlama-7b, Llama3.1-8b, Llama-8b distilled, Python-Code-13b), Qwen (Qwen-32b, Qwen-14b, Qwen-7b, Qwen-1.5b, Qwen2.5-Coder-7b), and DeepSeek (DS-Coder-33b, DS-Coder-v2-Lite, DS-Coder-6.7b). For Qwen models, we use variants enhanced via distillation with DeepSeek supervision, except Qwen2.5-Coder-7b, which is evaluated as released.

*Implementation.* Inference runs on Linux with two A40/L40/L40s GPUs for models up to 30B parameters and one shared H200 GPU for larger models. We use vLLM as the model inference framework. We apply a uniform decoding policy with temperature 0.2 and draw 16 independent samples per prompt at each distance level.

### 3.3 Metrics and Statistical Tests

The primary measure is SoftExec (Acc_soft) with within-prompt normalization to obtain continuous correctness, from which we construct Elasticity(p, d) and the dataset level curve E(d). At the dataset level, AUC-E is computed with Simpson's rule and normalization. For statistical testing we use Spearman correlation primarily, with Pearson and Kendall as needed. For group comparisons we apply the Kruskal Wallis test and the Mann Whitney U test, together with bootstrap 95% confidence intervals (CI) and Benjamini and Hochberg false discovery rate control.

## 4 Results and Analysis

### 4.1 RQ1: Joint Structure of Performance and Prompt Stability

We adopt model-level Pass@1 as the performance indicator and quantify prompt stability through AUC-E. We conduct rank correlation analysis at the model level while employing a four-quadrant classification to characterize different models (i.e., combinations of high/low performance and high/low robustness). Pass@1 ranges approximately from 0.029–0.820, and AUC-E from 0.404–0.646. We compute model-level rank correlation, obtaining Spearman ρ = −0.433 (p = 0.122; 95% CI [−0.875, 0.249]), which does not reach statistical significance in the current sample, suggesting no unified negative correlation trend. Further dividing models into "four quadrants" (high/low performance × high/low robustness) based on the combination of performance and stability, the corresponding distribution is 3/4/4/3, supporting subsequent stratified analysis by family and scale.

*Summary.* Within our coverage scope, the performance–stability relationship exhibits diversity rather than a single pattern, with the four-quadrant structure leaving room for multi-dimensional selection and customized optimization; scale effects also vary by family. We recommend jointly reporting performance and AUC-E, stratified by architecture/scale for practical selection.

Two specific examples illustrate this complementary specialization: Qwen2.5-Coder-7b has higher Pass@1 (0.820) but relatively lower AUC-E (0.403); Python-Code-13b has lower Pass@1 (0.284) but higher AUC-E (0.606) (both from the same model-level data).

### 4.2 RQ2: Distance-Shaped Sensitivity and Scale/Family Moderation

We measure sensitivity across three controlled distances d ∈ {0.1, 0.2, 0.3}. The average |ΔPass| values for d = 0.1/0.2/0.3 are approximately 0.078/0.082/0.078, showing non-monotonic changes within a narrow range. The significant main effect of scale indicates that scale does have a moderating role under current settings; however, differences still vary by architecture, and we make no causal inferences. Probability-layer stability (AUC-E) differs across scale×family units. The Tiny group has higher averages (mainly driven by 1.5B distilled models); Medium and Large groups show stronger heterogeneity across different families; within the same family, expansion in scale does not show a monotonic trend, suggesting that training data, optimization objectives, and distillation strategies also affect stability.

*Summary.* Under controlled distances, sensitivity is moderated by scale and family. Probability-layer stability is generally high with architecture-related fluctuations; discrete-layer |ΔPass| shows significant main effects of scale.

### 4.3 RQ3: PromptSELight Approximation Effectiveness to PromptSE

We examine whether PromptSELight (probability-free) AUC-E approximates PromptSE (probability-aware) AUC-E at the model level and evaluate numerical and ranking consistency. Overall results are: Pearson τ = 0.717, Spearman ρ = 0.723, Kendall τ = 0.670, MAE = 0.040, RMSE = 0.050, R² = 0.41. PromptSELight and PromptSE show moderate to strong monotonic consistency with moderate absolute errors. Overall rankings are basically aligned; a small number of models show more noticeable rank drift (for example, probability-layer scoring favors models with "good confidence calibration"). In practice, PromptSELight can be used for rapid screening, followed by PromptSE for high-fidelity confirmation.

*Summary.* Under current settings, PromptSELight provides a viable approximation for model-level comparison, though individual models show predictable deviations.

### 4.4 RQ4: Effects of Valence×Arousal on Correctness and Calibration

Under valence×arousal conditions, performance–sensitivity coupling and confidence patterns show cross-model differences. For some models, emotional prompting mildly reshapes correctness and calibration, but effects vary by model and family. Probability-layer diagnostics (ECE, bias, and elasticity) complement discrete indicators, helping make "calibration-aware" model selections. High-arousal negative-valence prompts inducing confidence miscalibration in certain models (particularly the Qwen family) suggest that emotional coloring can serve as a practical probe for model brittleness. Model × emotion ECE ranges from approximately 0.055 (Qwen-1.5B) to 0.622 (DS-Coder-6.7B).

*Summary.* Under valence×arousal conditions, performance–sensitivity coupling and confidence patterns show cross-model differences. For some models, emotional prompting mildly reshapes correctness and calibration, but effects vary by model and family. Probability-layer diagnostics (ECE, bias, and elasticity) complement discrete indicators, helping make "calibration-aware" model selections.

## 5 Discussion

*Model Selection and Performance-Stability Relationships.* Our finding that Pass@1 and AUC-E exhibit no statistically significant negative correlation challenges the assumption that stronger models are inherently more robust. The four-quadrant distribution reveals that performance and stability represent distinct optimization objectives that can sometimes be jointly achieved. This provides a practical decision framework: high-performance, high-stability models are most desirable when available, but stable-but-modest models suit reliability-focused production systems, while high-performance-but-sensitive models may excel in controlled research environments. Family-specific patterns (e.g., Llama's balance vs. Qwen's performance orientation) further inform selection based on organizational priorities.

*The Role of Model Scale and Architecture.* Our observations reveal a non-monotonic relationship between model size and prompt stability in our evaluation. The finding that the Tiny group (e.g., Qwen-1.5B) achieves the highest AUC-E while larger models show greater variance suggests that prompt stability may not follow the same scaling patterns observed for other model capabilities. This could indicate that smaller, well-trained models exhibit certain stability advantages through simpler decision boundaries or reduced overfitting to training prompt distributions. The significant main effect of scale on sensitivity (Kruskal-Wallis H = 49.663, p < 0.001) combined with family-specific patterns suggests that architectural inductive biases may interact with scale effects. These findings suggest that prompt stability represents a distinct dimension of model behavior that may require explicit optimization during training, rather than emerging automatically with scale.

*Emotional and Personality Factors as Robustness Indicators.* The systematic effects of valence and arousal on model behavior extend beyond simple performance metrics. High-arousal negative-valence prompts inducing confidence miscalibration in certain models (particularly the Qwen family) suggest that emotional coloring can serve as a practical probe for model brittleness. This phenomenon may reflect training data biases where emotional language correlates with different code quality distributions, causing models to implicitly adjust their confidence based on perceived developer state. The practical implication is that emotion-aware testing can reveal latent instabilities not captured by traditional benchmarks, providing an additional dimension for robustness evaluation.

*Prompt Engineering Guidelines.* The quantified sensitivity patterns inform prompt engineering best practices. Light perturbations (d = 0.1) often preserve performance, suggesting that minor stylistic preferences (e.g., politeness markers) can be accommodated without significant risk. However, heavy changes in expression style (d = 0.3) reveal model-specific vulnerabilities, indicating where prompt standardization may be necessary. Development teams can use our emotion templates to stress-test their prompts, identifying phrasings that tend to maintain stability across emotional variations.

*Limitations.* The template-based variant generation may not capture all natural communication patterns, and our emotion/personality dimensions represent a simplified model of human expression. The choice of perturbation distances (d ∈ {0.1, 0.2, 0.3}) and use of DeepSeek-Chat for generation may introduce biases affecting sensitivity measurements. Our evaluation focuses on Python code generation using HumanEval, which may not generalize to other programming languages, task domains, or cultural contexts. The AUC-E metric involves design choices that affect interpretation, including equal weighting of perturbation distances and linear aggregation of deviations.

## 6 Related Work

*Code Generation Evaluation.* Code generation evaluation has shifted from lexical metrics to execution-based assessment. Chen et al. introduced HumanEval with pass@k metric for functional correctness, addressing BLEU's limitations. MBPP uses entry-level tasks, while APPS evaluates competitive programming. Recent work explores confidence-weighted accuracy.

*Prompt Robustness in LLMs.* Ribeiro et al. showed semantically equivalent changes can flip predictions. CheckList formalized invariance testing. In code generation, He et al. found 40% performance swings for GPT-3.5 from format changes. Chain-of-thought dramatically improves performance and Kojima et al. showed "Let's think step by step" boosted GPT-3's accuracy from 17% to 78%. Template ensembling aggregates multiple phrasings, while calibration adjusts biases.

*Reliability and Calibration Metrics.* Liang et al. argue for holistic LLM evaluation covering accuracy, robustness, and calibration. Plaut et al. found consistent miscalibration across 15 models. ECE quantifies this gap, while variance indicates stability. Our work introduces AUC-E (Area Under the Consistency Curve), providing a unified stability metric as perturbations intensify.

*Human-Like Factors in Prompts.* LLMs reliably adopt personas. Our work extends this to code generation, examining whether emotional/politeness factors impact correctness—an unexplored domain where functional requirements should theoretically dominate.

## 7 Conclusion

This work introduces PromptSE, the novel measurement framework for evaluating code generation model stability under semantically equivalent prompt variations. While existing benchmarks focus on peak performance, they overlook how developers express identical requirements through diverse phrasings influenced by emotion and personality. Our evaluation of 14 models reveals three key insights. First, performance and stability show no significant negative correlation, with models distributed across all four quadrants, suggesting decoupled optimization objectives. Second, model scale exhibits non-monotonic stability relationships—smaller models can achieve superior robustness. Third, PromptSELight strongly approximates PromptSE, enabling rapid assessment for closed-source models. We make three contributions: (1) Methodologically, principled prompt variant generation through emotion/personality templates that preserve semantics while capturing natural diversity; (2) Technically, SoftExec for probability-aware evaluation and AUC-E for standardized stability quantification; (3) Practically, a dual-pathway system where PromptSELight enables screening and PromptSE provides detailed analysis. Our findings enable informed deployment decision—organizations can quantify performance stability tradeoffs, choosing high-stability models for critical systems while accepting sensitivity for research prototypes. Emotion-aware testing reveals latent vulnerabilities beyond traditional benchmarks.

Future work includes understanding architectural stability factors, extending to other tasks, and developing adaptive prompting strategies. Our results suggest prompt stability could join performance, fairness, and safety as a core evaluation dimension. Models that maintain consistent behavior across developer expression diversity will be better positioned for production success than those optimized solely for benchmarks.
