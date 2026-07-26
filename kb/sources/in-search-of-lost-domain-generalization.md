---
source: https://arxiv.org/abs/2007.01434
description: DomainBed testbed paper showing well-tuned ERM matches or beats specialized domain-generalization algorithms once a model selection strategy is made explicit
captured: 2026-07-26
capture: web-fetch
genre: scientific-paper
type: kb/sources/types/snapshot.md
---

# In Search of Lost Domain Generalization

Author: Ishaan Gulrajani, David Lopez-Paz
Source: https://arxiv.org/abs/2007.01434
Date: arXiv:2007.01434, submitted July 2, 2020

## Abstract

This paper addresses a critical gap in domain generalization research: the lack of standardized experimental conditions for fair algorithm comparison. The authors argue that "domain generalization algorithms without a model selection strategy should be regarded as incomplete."

They introduce **DomainBed**, a unified testbed featuring:
- Seven multi-domain datasets
- Nine baseline algorithms
- Three model selection criteria

## Key Findings

Through extensive experiments, the researchers found that empirical risk minimization (ERM), when properly implemented, achieves state-of-the-art performance across all tested datasets—challenging the superiority of more complex domain generalization methods.

## Significance

The paper highlights two critical insights:

1. **Model selection matters**: Realistic domain generalization evaluation requires explicit model selection strategies
2. **Implementation quality**: Careful implementation of standard methods can outperform specialized algorithms

The release of DomainBed aims to standardize and improve reproducibility in domain generalization research.

**Subjects:** Machine Learning (cs.LG), Machine Learning (stat.ML)
