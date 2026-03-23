---
source: https://www.letta.com/blog/continual-learning
description: Letta reframes continual learning for agents as optimization over learned context rather than weights, arguing token-space memory is the primary transferable substrate for long-lived agents
captured: 2026-03-23
capture: web-open
type: blog-post
---

# Continual Learning in Token Space

Author: Letta
Source: https://www.letta.com/blog/continual-learning
Date: December 11, 2025

> The continual learning problem in LLM agents is best viewed through the lens of learning in token space: updates to learned context, not weights, should be the primary mechanism for LLM agents to learn from experience.

The biggest gap between AI agents and human intelligence is the ability to learn. Humans continually learn and improve over time, acquire new skills, update their beliefs based on new facts, and modify their behavior to correct for past mistakes. In contrast, most AI agents have an incredible amount of world knowledge, but do not meaningfully get better over time.

How do we create AI agents that can continually learn? Traditionally, the concept of continual learning for neural networks has been synonymous with weight updates, under the assumption that all learning happens in a connectionist way. The central research questions have focused on catastrophic forgetting and when and how to do weight updates via gradient descent.

But there is a disconnect between this traditional framing and the reality of modern LLM-based AI agents. Today's agents are not just model weights, they are weights plus context. The effective program that determines an agent's behavior includes not only the model parameters, but also the system prompts, retrieved documents, tool definitions, and accumulated conversation history.

Two instances of the same model, given different contexts, can behave as entirely different agents with different knowledge, capabilities, and personalities.

This realization opens up a second axis for learning: rather than updating weights, we can update the tokens that condition the model's behavior. Letta calls this learning in token space.

At Letta, the authors argue that memories learned in token space can become more valuable than the model weights themselves: agents run perpetually, enrich learned context through experience, and transfer memories across generations of models.

## The limitations of learning in weights

Continual learning through weight updates has been studied for decades, yet production LLMs still ship with frozen weights. The article points to one notable exception, Cursor's online RL for tab completion, but treats it as narrow and population-level rather than agent-specific learning.

The article argues weight-space continual learning remains impractical because:

- pretraining, mid-training, and post-training all require heavy data curation, oversight, and evaluation that cannot be repeated each time an agent learns something new
- deployment raises privacy and personalization problems when millions of users generate distinct experience streams
- efficient fine-tuning methods such as LoRA reduce cost but still assume an offline workflow with offline evaluations
- weight updates leave core continual-learning problems unresolved, including learning signal quality, recency weighting, overfitting, distribution shift, and catastrophic forgetting

## The illusion of continual in-context learning

If deployed weights do not change, agents mainly learn online through in-context learning: new reasoning, actions, and observations get appended to the context window and reused later. The article argues this works only partially.

Its limitations are:

- finite context windows, which eventually overflow and also degrade reasoning before the limit
- append-only structure, which records logs rather than refining, consolidating, or compressing experience the way durable memory should

Yet token-space memory has advantages that weight updates lack:

- interpretability: learned memories are human-readable and directly debuggable
- portability: learned context transfers across models, providers, and model generations
- control: memories can be checkpointed, diffed, rolled back, deleted, and branched like text artifacts

The article's claim is that the right question is not whether in-context learning is enough as-is, but whether agents can move beyond append-only context into active memory maintenance and refinement.

## Towards continual learning in token space

The article formalizes an agent as a pair `(theta, C)`, where `theta` is the model and `C` is the context window: system prompt, tool definitions, conversation history, and other conditioning tokens.

It then frames continual learning as minimizing cumulative loss across a sequence of tasks over time:

```text
L = (1 / N) * sum_{i=1..N} l((C_i, theta_i), T_i)
```

Traditional continual learning optimizes `theta` across tasks:

```text
min_{theta_1 ... theta_N} sum_{i=1..N} l((C, theta_i), T_i)
```

Token-space continual learning instead optimizes `C`:

```text
min_{C_1 ... C_N} sum_{i=1..N} l((C_i, theta_i), T_i)
```

The article argues this changes the catastrophic-forgetting story. If a context update hurts performance, rolling back is straightforward because learned context can be checkpointed like text. Doing the equivalent for model weights is far less practical at modern model scale.

The piece places prompt optimization methods like DSPy, GEPA, and Feedback Descent in this frame: useful for finding a strong context for a single task, but not enough for open-ended learning across months, years, and model upgrades. It positions MemGPT and sleep-time compute as work aimed at the longer-horizon version of the problem.

## Solving continual learning in token space

The article criticizes today's default long-horizon pattern as append-then-summarize: collect raw experience until context overflows, then compress it by summarization.

It argues this fails because:

- appending raw experience forces the model to re-process unstructured logs at inference time
- summarization is lossy and abrupt, so important detail can disappear without warning

### Sleep-time compute for memory refinement

One proposed direction is to allocate background compute to memory management. During downtime, agents could identify contradictions, abstract patterns from specific experiences, and pre-compute associations that make later retrieval and reasoning cheaper and stronger.

### Teaching agents to manage their own memory

The article also argues for post-training models to understand their own memory limitations. Agents should learn to recognize context degradation, stale or contradictory memories, and opportunities to restructure their own contexts.

Current frontier models still treat system prompts as static. The article argues they should instead learn to edit their own instructions and treat memory operations as first-class tool use.

## Continual learning in both weights and token space

The article does not claim token space should entirely replace parametric learning. Instead, it argues future agents will likely use both:

- token-space memory for interpretable, portable, editable learning
- parametric memory for efficiency once the learned context has matured enough to distill

The proposed path is tokens-to-weights distillation: use learned context to generate synthetic training data, evaluations, or other artifacts that later inform fine-tuning or reinforcement learning, while preserving continuity across model releases.

## Building machines that learn

The article closes with the claim that agents able to carry memory across model generations will outlast any single frontier model. In that framing, weights are temporary, while learned context is the persistent asset.

This motivates a broader research agenda around memory architectures, context management, consolidation, forgetting, and transfer of learned context between systems.
