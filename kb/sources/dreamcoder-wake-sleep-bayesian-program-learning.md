---
source: https://arxiv.org/abs/2006.08381
description: DreamCoder paper — wake-sleep Bayesian program synthesis that grows a domain-specific language of reusable abstractions alongside neural search guidance, producing compositional, interpretable, transferable symbolic knowledge from experience.
captured: 2026-07-26
capture: web-fetch
genre: scientific-paper
type: ./types/snapshot.md
---

# DreamCoder: Growing generalizable, interpretable knowledge with wake-sleep Bayesian program learning

Author: Kevin Ellis, Catherine Wong, Maxwell Nye, Mathias Sable-Meyer, Luc Cary, Lucas Morales, Luke Hewitt, Armando Solar-Lezama, Joshua B. Tenenbaum
Source: https://arxiv.org/abs/2006.08381
Date: June 15, 2020

**ArXiv ID:** 2006.08381

**Subject Categories:** Artificial Intelligence (cs.AI); Machine Learning (cs.LG)

## Abstract

The paper presents DreamCoder, a system that learns to solve problems through program writing. The system builds expertise by developing programming languages that express domain-specific concepts alongside neural networks that direct the search for programs within those languages.

The approach employs a "wake-sleep" learning algorithm that iteratively extends the language with new symbolic abstractions and trains neural networks on both imagined and replayed problems. The system tackles inductive programming tasks and creative endeavors like picture drawing and scene construction. Notably, it independently rediscovers foundational concepts including "functional programming basics, vector algebra and classical physics, including Newton's and Coulomb's laws."

The resulting knowledge representations are compositional, building hierarchically from previously learned concepts. This approach yields interpretable and transferable multi-layered symbolic structures that scale flexibly with accumulated experience.

## Access
- [PDF](https://arxiv.org/pdf/2006.08381)
- [TeX Source](https://arxiv.org/src/2006.08381)
- DOI: [10.48550/arXiv.2006.08381](https://doi.org/10.48550/arXiv.2006.08381)
