---
source: https://alexzhang13.github.io/blog/2026/harness/
description: "Zhang and Khattab's empirical argument that context offloading and programmatic sub-calls let RLM harnesses generalize across task length and domain by keeping root-model observations locally in-distribution."
captured: 2026-07-21
capture: web-fetch
capture_note: "Main argumentative text captured; interactive plots, image assets, and the appendix's detailed metric table were omitted."
genre: practitioner-report
type: kb/sources/types/snapshot.md
---

# Language model harnesses are compositional generalizers

Author: Alex Zhang and Omar Khattab
Source: https://alexzhang13.github.io/blog/2026/harness/
Date: 2026-07-20

Harnesses can lead to compositional generalization: we observe a property in training RLMs, in which similarly structured tasks are viewed as isomorphic and all individual LM calls in the harness become in-distribution.

Modern post-training has become a brute-force paradigm of curating ever more environments and ever longer training horizons. In large part, this is because frontier Transformers are still poor at *compositional generalization*, the ability to solve unseen problems by composing familiar ones. Unless our models compose the individual lessons they learn, scaling will have slower returns than it should, as every new domain will demand its own investment in the form of training data.

Training data is not the only lever. We argue that better generalization is largely the job of what today is called a harness: the program between the external world and the neural network that decides how to encode environment state into one or more LLM inputs and how to determine the next action. Its primary job should be to carry a higher-level inductive bias that reduces unfamiliar and complex problems to compositions of simpler ones.

Concretely, a good harness shapes each call so that every observation is *locally in-distribution* (LID). We test this by reinforcement-learning a Recursive Language Model (RLM), which offloads context and defers execution to programmatic decomposition and recursive sub-calls. Training on short tasks generalizes to held-out tasks 8–32 times longer, with roughly ten times the evaluation lift, at the same training lift, of training the underlying Transformer directly. Training in one domain also transfers better to structurally similar tasks in other domains.

The proposed mechanism is that the RLM harness induces an equivalence relation between tasks with latent similarities: the root model sees nearly the same token-level trajectory. The harness thereby reduces similar tasks to the same trajectory and can lower the cost of curating more data and longer rollouts.

## Better scaling requires compositional generalization

Compositional generalization is the ability to solve unseen problems by composing familiar concepts and patterns. It lets systems reach beyond direct training-set coverage, including tasks whose surface tokens differ while their underlying structure is shared. The authors argue that Transformers are unreliable at this and that higher-level inductive biases can instead live in a harness.

## The capacity for compositional generalization can live in the harness

A harness can simplify arbitrarily complex state into many smaller observations that individual LM calls can handle. A good harness reduces unfamiliar problems to familiar ones and complex problems to simple ones. Even if the full task state is out-of-distribution, each observation can remain locally in-distribution.

The post argues that appended-history agent designs, including Claude Code and Codex, do not reliably do this because task-specific information, tool outputs, and reasoning accumulate in the main context. Context bloat eventually pushes the trajectory out of distribution. Instead, a harness should make structurally similar tasks appear isomorphic to the main model, while sub-agents handle small, individually in-distribution subtasks.

## RLMs are surprisingly good at compositional generalization

The RLM achieves this through two mechanisms:

1. **Context offloading.** Input-specific context is passed as a symbolic variable, so the root model does not directly see it and different problems can appear similar at the first step.
2. **Programmatic sub-agent calling.** Sub-agents and ordinary tools are functions in a code REPL. Outputs can remain in variables and pass into later calls without entering the root model's context.

Both mechanisms are needed to abstract task-specific information away from the main context.

### Length generalization

The authors train Qwen3-30B-A3B-Instruct-2507 for 150 steps on short splits of six environments and evaluate on much longer splits: MRCRv2, GraphWalks, LongBenchPro, OOLONG, OOLONG-Pairs, and Ada-LEval. The RLM variants improve substantially on the long evaluations, while the base Transformer with context extension generally shows flat evaluation performance even as short-task training reward rises. In several settings, the trained 30B RLM approaches or exceeds a frontier-model RLM baseline.

The claimed reason is that a length-agnostic decomposition makes the root model's view of short and long tasks nearly identical; length changes mainly the number of sub-calls, each of which remains bounded. This outcome is not automatic. A short task can be solved by offloading the whole problem to one sub-call, which does not generalize. A decomposition hint improves the MRCRv2 case, suggesting supervision or distillation can help the system converge on a generalizable strategy.

### Strategy generalization

The authors also train and evaluate across domains whose token distributions differ but whose decomposition strategies are similar: aggregation from TREC questions to spam classification, author-style retrieval from writing to mathematics, and stance search from Twitter to WildChat errors. The RLM shows clear evaluation gains in the held-out domains; the base Transformer mostly does not. The RLM's training and evaluation rewards track each other more closely despite domain change.

RLM training costs 1.5–3 times more runtime than base-Transformer training on similarly sized tasks because of multi-step samples and sub-call waits. The authors argue that this scales better with task complexity than training directly on much longer contexts or horizons.

## The scaling picture

The authors do not recommend hand-coding a narrow decomposition for every problem. Their claim is that data remains the largest driver of progress, while the architecture and inductive biases of the system determine the return on that data. Language permits higher-level symbolic inductive biases, and end-to-end RL can train systems that use context offloading and programmatic sub-agents.

The central harness-design principle is: make systems learn to reduce complex problems to sequences of individually and locally in-distribution observations. The capacity for compositional generalization may therefore live largely in the harness and increasingly blur with what counts as the architecture of a frontier AI system.

## Appendix note

The post acknowledges that “isomorphic” is used loosely. Token-level edit distance, n-gram containment, Jaccard variants, and length ratio are only proxies for whether evaluation trajectories resemble training trajectories. These proxies show RLM evaluation trajectories closer to prior training trajectories than appended-context baselines, but they do not establish semantic equivalence or bounded similarity of output distributions.

## Citation

```bibtex
@article{zhang2026harnesses,
  title  = "Language model harnesses are compositional generalizers",
  author = "Zhang, Alex and Khattab, Omar",
  year   = "2026",
  month  = "July",
  url    = "https://alexzhang13.github.io/blog/2026/harness/"
}
```
