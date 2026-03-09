---
source: https://www.domainlanguage.com/articles/ai-components-deterministic-system/
captured: 2026-03-09
capture: web-fetch
type: blog-post
---

# AI Components for a Deterministic System (An Example)

Author: Eric Evans
Source: https://www.domainlanguage.com/articles/ai-components-deterministic-system/
Date: August 24, 2025

## Overview

Eric Evans explores how to integrate non-deterministic AI components into deterministic software systems. Using a practical example of automatically identifying business domains in code repositories, he demonstrates strategies for constraining AI outputs to make them usable in conventional software workflows.

## Key Sections

### 1. The Problem: Non-Deterministic AI Outputs

Evans uses the OpenEMR project as a case study. When asking an LLM "what domain does this code address?" the model produces reasonable answers but in different formats each time. This variation makes it difficult for conventional software to process and compare results systematically.

### 2. Modeling vs. Classification Tasks

A critical distinction emerges: asking an LLM to *create* a categorization scheme is a modeling task (difficult, requiring iteration), while asking it to *apply* existing categories is a classification task (reliable, repeatable).

Evans demonstrates that identical prompts produce inconsistent categories across runs—making comparison and hierarchical roll-ups impossible.

### 3. Solution: Separate Concerns

The approach involves two distinct steps:

- **Modeling phase:** Generate a canonical taxonomy once
- **Classification phase:** Apply frozen categories consistently to individual code modules

This separation enables consistent, comparable results across the codebase.

### 4. Incremental Updates

For streaming scenarios, Evans suggests prompting the LLM to check new code against previously observed domains, then add genuinely new categories—allowing schemas to evolve systematically.

### 5. Iteration and Refinement

Creating quality classification schemes requires iteration. Evans mentions several techniques:

- Sampling and repeated refinement cycles
- Using "critic" models to evaluate categories
- Employing "judge" models to rate candidate schemes

However, he notes these advanced techniques didn't improve results for this particular use case.

### 6. Leveraging Published Standards

Rather than generating custom categories, Evans advocates using established classification systems like NAICS (North American Industry Classification System). This approach offers significant advantages:

- **Consistency:** Multiple runs produce stable, comparable results
- **Maturity:** Well-tested, documented schemas reduce ambiguity
- **Integration:** Published languages facilitate external system connectivity
- **Lower friction:** Eliminates custom modeling overhead

The NAICS approach showed dramatically improved consistency—running the same prompt multiple times yielded identical high-confidence results.

## Key Insight

Evans emphasizes: "Creating a classification system is a modeling task, which is much harder than the classification task itself." When a domain is generic (not your competitive advantage), using established standards beats custom AI-generated models. Only treat classification modeling as part of your core domain if it genuinely differentiates your system.
