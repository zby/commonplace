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

## Procedure

1. **Generate anchors.** Ask an LLM for many candidate ideas, prompts, answers, note titles, or connection hypotheses. Vary source subsets, roles, constraints, and seed examples so the first candidate pool does not collapse into one cluster.
2. **Embed the working set.** Use an ordinary semantic-search embedding model to embed anchors, relevant source snippets, existing notes, rejected candidates, and known high-quality examples.
3. **Map the space.** Use similarity search, clustering, distance checks, and sparse-region detection to find dense clusters, stale regions, outliers, and cross-cluster bridges.
4. **Choose target directions.** Explore between strong distant anchors, away from over-covered clusters, toward sparse relevant regions, across two source clusters, or near high-quality examples while staying far enough from duplicates.
5. **Instantiate the direction in language.** Treat this as the lossy step. Use one of four no-training approximations:

    - **Nearest-neighbor decode:** retrieve real texts closest to the target vector and ask the LLM to synthesize from them.
    - **Contrastive prompting:** give positive anchors, negative anchors, and explicit constraints: "like A/B, unlike C/D, preserve X, change Y."
    - **Exemplar bridge:** provide two distant examples and ask for a coherent bridge, hybrid, or missing intermediate.
    - **Mutation prompt:** ask the LLM to perturb an anchor along a named axis, such as more causal, more operational, more adversarial, more minimal, more cross-domain, or more testable.

6. **Score candidates.** Apply cheap filters before expensive judgment: semantic distance from existing items, similarity to the intended direction, duplicate detection, coherence checks, source-grounding checks, and task-specific utility if a hard or semi-hard oracle exists.
7. **Iterate search.** Keep the best candidates, embed them, add them to the anchor set, and repeat. A Magellan-like variant makes this explicit with MCTS: branch, score, backpropagate value, and deepen promising paths.
8. **Review before promotion.** Use human review, a stronger LLM judge, or domain tests before letting outputs become library notes, instructions, links, or source-ingest decisions.

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
