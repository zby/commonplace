# Practical Pipeline Sketch

This is the no-large-training version of the latent-space novelty workflow. Treat embeddings as a search and routing substrate, not as something that must be decoded directly.

## Pipeline

1. **Generate anchors.**
   Ask an LLM for many candidate ideas, prompts, answers, note titles, or connection hypotheses. Use varied prompting, source subsets, roles, constraints, and seed examples to avoid one narrow cluster.

2. **Embed everything.**
   Use a normal semantic-search embedding model: OpenAI embeddings, BGE, E5, sentence-transformers, or a local equivalent. Embed anchors, relevant source snippets, existing notes, rejected candidates, and known high-quality examples.

3. **Map the space.**
   Use similarity search, clustering, distance checks, and sparse-region detection to identify dense clusters, stale regions, outliers, and cross-cluster bridges.

4. **Choose target directions.**
   Pick where to explore:

   - between two strong but distant anchors;
   - away from common or already-covered clusters;
   - toward a sparse but relevant region;
   - across two source clusters that rarely connect;
   - near high-quality examples but far enough to avoid duplicates.

5. **Instantiate the direction in language.**
   This is the hard step. Practical no-training options:

   - **Nearest-neighbor decode.** Retrieve real texts closest to the target vector, then ask the LLM to synthesize from them. Easiest and robust, but bounded by existing nearby material.
   - **Contrastive prompting.** Give positive anchors, negative anchors, and explicit constraints: "like A/B, unlike C/D, preserve X, change Y."
   - **Exemplar bridge.** Provide two distant examples and ask for a coherent bridge, hybrid, or missing intermediate.
   - **Mutation prompt.** Ask the LLM to perturb an anchor along a named axis: more causal, more operational, more adversarial, more minimal, more cross-domain, more testable.
   - **Projector-based decode.** Use a learned projector into an LLM token-embedding space. This is closer to the Geometry paper, but it is no longer the simple no-training path.

6. **Score candidates.**
   Apply cheap filters before expensive judgment:

   - semantic distance from existing items;
   - similarity to the intended target direction;
   - duplicate and near-duplicate detection;
   - format and coherence checks;
   - source-grounding checks;
   - task-specific utility if a hard or semi-hard oracle exists.

7. **Iterate search.**
   Keep the best candidates, embed them, add them to the anchor set, and repeat. A Magellan-like version makes this explicit with MCTS: branch, score, backpropagate value, and deepen promising paths.

8. **Review before promotion.**
   Novelty is cheap to generate and expensive to validate. Use human review, a stronger LLM judge, or domain tests before letting outputs become library notes, instructions, links, or source-ingest decisions.

## KB-Specific Uses

- **Connection discovery.** Search for non-obvious bridges between two note clusters, then ask for labelled candidate links with reasons.
- **Source triage.** Generate search directions for missing evidence around an existing note.
- **Note proposal.** Identify repeated gaps in the library and propose candidate note claims, keeping them in `kb/work/` until reviewed.
- **Synthesis planning.** Build candidate outlines that bridge multiple source clusters, then score for coverage and non-duplication.

## Main Risk

The workflow can optimize for "different" rather than "useful." Any version that lacks a quality oracle will produce plausible-looking novelty sludge. The first practical test should measure how many generated candidates survive human review, not how far they are in embedding space.

