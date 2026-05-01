# Workshop: Latent-Space Generation Without Training

## Question

Can latent-space exploration techniques from recent novelty-generation papers be turned into a practical workflow for agents or maintainers who do not want to train or fine-tune a large model?

## Trigger

This workshop started from comparing two papers:

- [Geometry of Knowledge Allows Extending Diversity Boundaries of Large Language Models](../../sources/geometry-of-knowledge-extending-diversity-boundaries-llms.md) — uses anchor generations, semantic embeddings, interpolation/perturbation, and xRAG-style projector conditioning to expand output diversity without modifying LLM parameters.
- [Magellan: Guided MCTS for Latent Space Exploration and Novelty Generation](https://arxiv.org/abs/2510.21341) — frames novelty generation as guided search over an LLM's latent conceptual space, using MCTS, a semantic compass, and a value function balancing coherence, novelty, and progress.

The practical question is not whether these papers are scientifically settled. It is whether their operational pattern can be borrowed for a no-training, black-box or mostly-black-box workflow.

## Working Hypothesis

The borrowable core is **embedding-guided search, not direct vector decoding**.

Normal semantic-search embeddings are enough to map candidates, detect novelty, select diverse anchors, and choose search directions. The difficult step is turning a target vector or direction back into language. For a no-training workflow, that step should be handled by retrieval, contrastive prompting, exemplar bridges, and mutation prompts rather than by a learned projector.

## Source Status

- The Geometry paper is already captured and ingested locally.
- Magellan is not yet captured in `kb/sources/`; candidate next action is to ingest it if this workshop continues.
- The Magellan code exists at <https://github.com/moyiliyi/Magellan-Novelty-Generation>, but using it directly still requires environment setup, a paper corpus, FAISS, and Qwen-family model weights.

## Working Threads

1. **Minimum viable pipeline.** What is the smallest useful workflow using ordinary embeddings, nearest-neighbor retrieval, and LLM calls?
2. **Decode problem.** Which vector-to-language approximation works best in practice: nearest-neighbor synthesis, contrastive prompting, exemplar bridges, or mutation prompts?
3. **Oracle design.** What cheap filters can reject obvious duplicates and incoherent outputs before human review?
4. **KB application.** Could this help propose notes, connections, source candidates, or synthesis directions without polluting the library layer?
5. **Tool boundary.** Is this a one-off workshop script, a future `commonplace-*` command, or a skill-level workflow?

## Closure Conditions

This workshop can close when one of these happens:

- a tested no-training pipeline is documented as an instruction or skill candidate;
- the idea is rejected as too noisy, with the failure mode documented;
- the durable insight is extracted into a note about embedding-guided generation, novelty search, or oracle bottlenecks.

