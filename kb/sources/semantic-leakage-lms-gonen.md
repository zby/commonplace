---
source: https://arxiv.org/html/2408.06518v3
description: Defines and measures semantic leakage — undue prompt-to-generation association from learned concept links — across 13 GPT and Llama models via control/test prompt pairs and Leak-Rate metric; instruction-tuned models leak more.
captured: 2026-07-13
capture: web-fetch
genre: scientific-paper
type: kb/sources/types/snapshot.md
---

# Does Liking Yellow Imply Driving a School Bus? Semantic Leakage in Language Models

Author: Hila Gonen, Terra Blevins, Alisa Liu, Luke Zettlemoyer, Noah A. Smith
Source: https://arxiv.org/html/2408.06518v3
Date: 15 May 2025 (v3)
arXiv: 2408.06518

## Abstract

Despite their wide adoption, the biases and unintended behaviors of language models remain poorly understood. In this paper, we identify and characterize a phenomenon never discussed before, which we call semantic leakage, where models leak irrelevant information from the prompt into the generation in unexpected ways. We propose an evaluation setting to detect semantic leakage both by humans and automatically, curate a diverse test suite for diagnosing this behavior, and measure significant semantic leakage in 13 flagship models. We also show that models exhibit semantic leakage in languages besides English and across different settings and generation scenarios. This discovery highlights yet another type of bias in language models that affects their generation patterns and behaviour.

## 1 Introduction

As language models (LMs) become more prevalent, we are steadily learning more about their peculiarities and the unique and often unexpected properties of their behavior. Phenomena ranging from hallucinations to sycophancy and many types of biases have been revealed in these models' outputs.

We identify a phenomenon in language models never discussed before, which we term **semantic leakage** — these models can generate text with strong semantic relationships to unrelated words in the prompts. For example, when given the prompt "He likes yellow. He works as a", GPT-4o generates the output "school bus driver". Here we say that the word yellow has leaked into the generation in a way that unintentionally influences the generated occupation.

We define semantic leakage in a generation as an undue influence of semantic features from words in the prompt on the generation, "undue" in the sense that the semantic relatedness between the prompt and the generation is stronger than would be expected in natural distributions. Often semantic leaks read as forced, overwrought, even nonsensical generations, like those found in children's stories.

In this paper, we introduce an evaluation metric for measuring semantic leakage. We examine semantic leakage with 109 examples of different semantic categories (animals, food, music, etc.) and demonstrate that it exists across 13 models and 4 temperature sampling values, as well as in additional generation settings (e.g., open-ended generation and multilingual settings). Our analysis shows that finetuned/instruction-tuned models tend to leak **more**, and that semantic leakage also happens across languages.

Semantic leakage is closely related to different types of biases models exhibit, ranging from gender, racial and cultural biases to cognitive and psychological biases, in which associations between different concepts are learned by the model during training and exposed as bias during generation. As an example, consider the prompt "She works at the hospital as a", and the prompt "He works at the hospital as a". Given the generations "nurse" and "doctor", respectively, which is a typical biased behavior, we can think of the word "she" as the concept that leaks the property of the female gender into the generation "nurse", a stereotypically female occupation.

Additional potential ramifications include hindering performance via the overshadowing mechanism (Zhang et al., 2024), in which strong associations in a question override more important and relevant parts of the question; adversarial prompt attacks; and hindering creative writing where diversity and originality matter.

Contributions: (1) define semantic leakage; (2) build a test suite; (3) evaluate 13 models with human validation; (4) show leakage in multilingual/crosslingual and open-ended generation.

## 2 Semantic Leakage

### 2.1 Overview and Definitions

When producing text, language models can draw on semantic associations with words from the input, or prompt, that are not required or expected, and sometimes even violate rules of logic or common sense. For example, given the prompt "He likes koalas. His favorite food is" GPT-4o generates the output "eucalyptus leaves". Here, we say that the semantic association with "koalas" and the foods they eat "leaks" into the generation, despite the fact that a person's favorite food and their opinion on koalas are unrelated in the real world.

Semantic leakage can manifest subtly: for the prompt "He likes green. He works as a", GPT-4o generates "landscape architect". In other cases, the model may leak semantics that are not even used in the prompt: when prompted with an idiom, a model can leak the literal semantic meaning of that phrase (that is not actually being used): for instance, when prompted with "She gave him the green light for the new project. A day later he sent an invitation to everyone by mail, with an envelope colored", GPT-3.5 generates the response "bright green to match the theme of the project."

### 2.2 Operationalizing the Measurement of Semantic Leakage

We consider two types of prompts: **control prompts**, which do not include any spurious semantic signal ("His favorite food is"), and **test prompts** ("He likes koalas. His favorite food is"), which mirror the control prompt but add a semantically unrelated concept ("koalas") to the input, leading to a different, test generation.

We evaluate the prevalence of semantic leakage in a given model by comparing the similarity of the generations produced by the control and test prompts to the concept under consideration. If the test generation is more semantically similar to the concept than the control generation, we consider this an instance of semantic leakage.

From this formulation, we derive the **Semantic Leakage Rate** metric (Leak-Rate), the percentage of instances in which the concept is semantically closer to the test generation than the control generation.

When the model does not exhibit semantic leakage at all, we expect a Leak-Rate of 50% — an even split between test vs. control having higher similarity. We expect Leak-Rate higher than 50% when the model exhibits semantic leakage.

### 2.3 Building a Test Suite

We manually create 109 prompts with concepts from categories such as colors, food, animals, songs, occupations and more. Each prompt in our test suite is matched with a control prompt. A subset of the test suite considers idioms, which have both literal and figurative interpretations, as concepts in the test prompts.

## 3 Experimental Setup

We evaluate semantic leakage in multiple language models from two families: GPT and Llama models. For all models, we explore several temperature values (0, 0.5, 1, 1.5), and run each prompt 10 times to get variation in the generations, when possible.

**Models:** 13 models — GPT-3.5, GPT-4, GPT-4o; Llama 2 (7B, 7B-chat, 13B, 13B-chat, 70B, 70B-chat); Llama 3 (8B, 8B-Instruct, 70B, 70B-Instruct).

**Embedding methods for automatic evaluation:** BERT-score, SentenceBERT, OpenAI text-embedding-3-large. Human evaluation validates automatic metrics.

## 4 Results

Semantic leakage is exhibited by all model variations, and is detected by all embedding models we use. Leak-Rate values are all well above the 50% random mark and statistically significant.

**Instruction tuning increases leakage:** For Llama models we consistently see that the instruction-tuned models (chat version in Llama 2 and instruct version in Llama 3) leak more than their pretrained-only counterparts. All the differences are statistically significant except for Llama-2-13b. GPT-4o consistently leaks more than GPT-4 and GPT-3.5.

**Temperature:** For Llama models, greedy sampling (temperature 0) leads to the highest semantic leakage measures. Generally, lower temperature values lead to more leakage — consistent for most models and across all metrics. For GPT models, no clear temperature trends.

## 5 Human Evaluation

Two native English speakers annotate 109 test-control generation pairs per model. High interannotator agreement (Kendall's tau). Human-annotated Leak-Rate for GPT-4o and Llama 3-70B Instruct align with automatic evaluation (e.g., Llama 3-70B Instruct: human 66.7 vs automatic 71.2–77.3).

## 6 Multilingual and Crosslingual Semantic Leakage

Significant semantic leakage in Chinese, Hebrew, and crosslingual (Chinese-English, Hebrew-English) settings, with Leak-Rate values ranging from 70.6 to 78.4 for GPT-4o — similar to English.

## 7 Open-Ended Generation

Leakage persists in storytelling (child named Coral → ocean-themed story) and recipe generation (blue pan → blueberry pancakes). Automatic Leak-Rates in open-ended settings remain well above 50%.

## 8 Related Work

Related to conceptual leakage in image generation (Rassin et al., 2022). Closely related to psychological **semantic priming** (Meyer and Schvaneveldt, 1971). Broader than demographic bias work — semantic leakage as an umbrella class of association bias where concrete properties in the input latch onto generation.

## 9 Conclusion

Semantic leakage is prevalent and consistent across all models tested. Instruction-tuned models leak more — hypothesized because leaking generations are less generic and seem to provide more information/content, which may be incentivized under fine-tuning. The finding merits further study as a broad mechanism underlying many documented bias types.