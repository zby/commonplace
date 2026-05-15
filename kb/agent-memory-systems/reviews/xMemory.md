---
description: "Research-code dialogue-memory system that distills conversations into episodes, semantic facts, and LLM-summarized themes, then retrieves top-down with coverage selection plus entropy-gated episode inclusion"
type: ../types/agent-memory-system-review.md
traits: [has-comparison, has-external-sources]
tags: [related-systems, trace-derived]
status: current
last-checked: "2026-04-12"
---

# xMemory

xMemory is the research-code companion to the paper "Beyond RAG for Agent Memory: Retrieval by Decoupling and Aggregation" (Hu, Zhu, Yan, He, Gui, arXiv 2602.02007). The repository is a HuggingFace-driven evaluation harness targeting the LoCoMo and PerLTQA dialogue-memory benchmarks. Its claim is that agent memory should stop treating the transcript as a flat RAG corpus and instead build a four-level hierarchy — raw messages, episode summaries, semantic facts, and LLM-summarized themes — then retrieve top-down, expanding to finer resolutions only when they lower the reader's answer uncertainty.

**Repository:** https://github.com/HU-xiaobai/xMemory
**Paper:** https://arxiv.org/abs/2602.02007
**Status:** Research code, still at commit `375ae14` (`Update README.md`, 2026-02-25); no package manifest beyond `environment.yml` and the thin `xMemory/__init__.py` facade around `src/`. No commits since the previous review.

## Core Ideas

**Dialogue memory as a layered stream rather than a passage corpus.** The paper argues standard RAG assumptions break when the source is a bounded conversation with many correlated or duplicate spans and temporally linked prerequisites. The implementation commits to that framing: `evaluation/locomo/add.py` feeds per-user sessions in order through `MemorySystem.add_messages()`, preserving timestamps and raw role/content pairs as `original_messages`, and writes all per-user artifacts under `config.storage_path` in `episodes/`, `semantic/`, `themes/`, `semantic_knn/`, `graphs/`, and a Chroma store — matching the layout the README advertises.

**Three-stage construction, one stage at a time.** `add_messages()` buffers messages and asks an LLM boundary detector (`BoundaryDetector`, cached per buffer state in `PerformanceOptimizer`) whether the current buffer should close. When a boundary fires, `EpisodeGenerator` produces a titled third-person narrative with an ISO timestamp and keeps the raw messages attached to the `Episode` object. An `episode_created` event is published on `EventBus` and consumed by `SemanticTaskManager`, which runs `SemanticGenerator.check_and_generate_semantic_memories()` on a thread pool. After the user is flushed, `add.py` calls `fetch_incremental_batches()`, then `update_themes()`, then `update_hierarchy_graph()`, processing the new batch only once per user. Nothing is truly online at inference time; hierarchy assembly runs as a batch post-step per user.

**Prediction-correction as the learning mechanism.** The default semantic pathway is `PredictionCorrectionEngine.learn_from_episode_simplified()`. If no prior semantic memories exist it runs `_cold_start_extraction`, which prompts the LLM directly for persistent, self-contained statements (names, professions, preferences, relationships, plans, habits). Once statements exist, the engine does a two-step cycle: retrieve the top similar statements via Chroma vector search, prompt the LLM to *predict* the episode content from the title plus those statements, then prompt again to extract facts present in `original_messages` but *missing or misrepresented* in the prediction. The "free energy" branding in comments is marketing; the implemented mechanism is LLM prediction followed by LLM gap extraction, with cosine retrieval in between.

**Theme layer maintained by thresholds, LLM summaries, and a sparsity+semantics objective.** `ThemeManager.assimilate_and_accommodate()` processes each new semantic in sequence: `_attach_semantic_to_theme()` attaches to the nearest theme centroid if cosine similarity clears `DEFAULT_THEME_ATTACH_THRESHOLD = 0.62`, with a lenient floor at `LENIENT_ATTACH_FLOOR = 0.52` when the target theme is not yet full (`MAX_THEME_SIZE = 12`); otherwise a new singleton theme is created. Overlarge or incoherent themes (`>12` members, or `>=8` members with `mean_intra_sim < MIN_INTRA_SIM = 0.72`) are split by local similarity clustering or forced PCA partition; near-duplicate themes are merged when similarity crosses `MERGE_THRESHOLD = 0.78`. Candidate splits and merges are scored by `f = SparsityScore + SemScore` where sparsity rewards balanced cluster sizes (`(N/K) * (N/Σnk²)`) and SemScore mixes per-theme cohesion with a kNN-neighbor term shaped by a Gaussian around the median. Theme summaries are produced by the configured LLM over member fact texts.

**Retrieval is top-down with coverage selection and an entropy gate.** `evaluation/locomo/xMemory_search_framework.py` keeps a `baseline` strategy (BM25 + Chroma vector with reciprocal rank fusion) and adds `adaptive_hier` as the distinctive path. Adaptive search embeds the question, scores all semantics by cosine, takes the top `N_sem_pool = 40`, maps them to candidate themes via each semantic's `semantic_ids`, picks up to `K_max_theme = 5` themes with `_pick_representatives()` (greedy coverage over the theme kNN graph, combined `alpha_coverage = 0.7` with the normalized query-theme score), then restricts the semantic pool to that theme's members and re-picks up to `K_max_sem = 20` representative semantics over the semantic kNN graph. Episodes come from two sources: parents of the selected semantics and the top `N_ep_vec = 10` question-similar episodes. Up to `K_ep_probe = 10` candidate episodes are then evaluated one by one with `_estimate_entropy()`, which asks the local HF model to complete an answer from a themes+semantics+episodes prompt and computes the mean negative log-prob. An episode is included if `ig = H_before - H_after > tau_ep = -0.45` and flagged `expand_original` if `ig > tau_ep_expand = 0.25`. Raw `original_messages` are spliced into the answer prompt only for episodes that earned the expansion flag.

**Storage is files as source plus derived vector, knn, and graph indexes.** Episodes live as per-user JSONL (`episodes/{user}_episodes.jsonl`), semantics as per-user JSONL, themes as JSONL plus `.npy` embedding matrices and id lists in `themes/vector/`, the semantic kNN as per-user JSON in `semantic_knn/`, and the full hierarchy as a GEXF file under `graphs/`. Chroma owns the live vector collections; BM25 is rebuilt in memory. Files are human-inspectable, but they are machine-shaped records (fact strings, summary blobs, embedding blobs), not authored prose. The `xMemory` Python facade is a thin `MemorySystem` wrapper; there is no CLI, MCP server, API, or library packaging — consumers invoke the scripts under `evaluation/locomo/` directly.

**The hierarchy graph is an export artifact, not the retrieval engine.** `HierarchicalMemoryGraph.incremental_update()` builds a four-level `networkx.Graph` with `message`, `episode`, `semantic`, `theme` nodes tied by `belongs_to`, `supports`, and `abstracted_by` edges, then writes a sanitized GEXF (with embeddings and large lists dropped). In `add.py` the message level is not populated (`new_messages = []` is passed explicitly, and only `new_episodes`/`new_semantics`/`new_themes` enter the graph). `adaptive_hier` never traverses the GEXF graph — it reads JSONL, the `semantic_knn` JSON, and the theme `neighbors` fields cached inside each `ThemeNode`. `evaluation/gexf_view.py` is a visualization helper, confirming the graph's primary role.

## Comparison with Our System

| Dimension | xMemory | Commonplace |
|---|---|---|
| Primary use case | Dialogue-memory QA on LoCoMo/PerLTQA benchmarks | Agent-operated KB methodology and shipped-system documentation |
| Knowledge unit | Episode JSONL, semantic fact string, LLM-summarized theme | Typed markdown note with frontmatter, prose, articulated links |
| Storage | JSONL + Chroma vectors + `.npy` theme matrices + GEXF graph | Markdown files in git, generated indexes, scoped operational SQLite |
| Learning loop | LLM boundary -> LLM episode summary -> LLM prediction+gap extraction -> vector/LLM theme grouping | Human+agent writing, linking, validation, review bundles, status transitions |
| Retrieval | Top-down theme -> semantic -> episode with coverage + entropy-gated raw expansion | Agent navigation through descriptions, links, indexes, and grep/semantic search |
| Governance | Cosine dedup (off by default), theme split/merge thresholds; no lifecycle or validation | Type system, structural validation, semantic gates, explicit `status` |
| Integration surface | Benchmark scripts only (`evaluation/locomo/add.py`, `xMemory_search_framework.py`) | `commonplace-*` CLI, review bundles, skills |
| Inspectability | JSONL plus GEXF export; content is machine-shaped | Human-authored notes, diffable, grep-able, linkable |

**xMemory's contribution is retrieval architecture, not knowledge substrate.** The four-layer resolution ladder plus coverage selection plus entropy-conditioned expansion is a genuine answer to [charting the knowledge access problem beyond RAG](../../notes/charting-the-knowledge-access-problem-beyond-rag.md). But the ladder is populated by LLM summaries and extracted fact strings that are read only by the next retrieval step. They are not written to be read, revised, or linked as arguments — the same distinction the comparative review draws between a search index and a knowledge system.

**xMemory automates the curation oracle that commonplace keeps explicit.** The pipeline asks LLMs to decide boundaries, summarize episodes, extract persistent facts, summarize themes, and rank episodes by entropy reduction. That is defensible on benchmark dialogue where the task is answering fixed questions over a closed corpus. Commonplace keeps promotion human-or-agent curated because [automating KB learning is an open problem](../../notes/automating-kb-learning-is-an-open-problem.md): extraction is the easy half — deciding what earns durable trust is not.

**The storage model is a middle case for files-first thinking.** JSONL is a file, but the interface is the Chroma/kNN/GEXF triangle that the retrieval script loads, not the file itself. This fits the derived-index boundary in [files-not-database](../../notes/files-not-database.md): when the access pattern is cross-fact coverage and entropy-conditioned expansion, vector and graph layers are reasonable derived additions. It does not challenge markdown-as-source for authored methodology, because xMemory's *source* is a dialogue trace, not a curated library.

**The hierarchy is derived; ours is authored.** xMemory's themes are clustered from semantic fact embeddings and LLM-summarized; navigation between levels is a function of vector similarity and the sparsity+semantics objective. Commonplace's hierarchy comes from typed directories, indexes, articulated link semantics, and descriptions chosen for retrieval — all editorial decisions. The derived route is cheaper to scale and more objective for benchmark retrieval; the authored route carries the argumentative context that makes a library usable as reasoning.

## Borrowable Ideas

**1. Four-resolution retrieval ladder (ready as a design reference).** Theme -> semantic fact -> episode -> raw message is a clean template for context budgeting. A commonplace analogue is index orientation -> note description -> note body -> source snapshot. The transferable insight is that expansion to the next resolution should be conditional on that level's marginal value, not automatic.

**2. Coverage-plus-relevance representative selection (needs an embedding layer first).** `_pick_representatives()` trades pure top-k for a greedy objective that rewards query similarity *and* diversity over a kNN graph. If commonplace ever derives a semantic graph over notes or source snapshots, this is a better default than raw top-k for orientation packets.

**3. Entropy-gated expansion (needs a narrow use case).** Measuring answer-log-prob change before and after adding a candidate is expensive but conceptually strong for long-trace corpora. Overkill for normal note navigation; plausibly useful for a future trace-analysis workshop where raw logs dwarf distilled artifacts, and budget matters more than recall.

**4. Keep trace layers separately addressable (ready as a workshop convention).** xMemory's separate `episodes/`, `semantic/`, `themes/`, and `semantic_knn/` directories make the promotion chain inspectable even when artifacts are not polished notes. A trace-mining workshop could copy this layering: raw run → episode segment → candidate lesson → clustered theme, each as its own file type.

**5. Split/merge scoring as a reference, not a direct borrow.** The sparsity+cohesion objective is a concrete way to manage automated clusters when they exist, but the score only reports whether vectors form balanced cohesive clusters — not whether the grouping *explains* the domain. It cannot substitute for authored indexes; use it only if commonplace ever has automated source clusters that need a maintenance heuristic.

## Curiosity Pass

**What does "decoupling" actually transform?** The implemented decoupling is neither a latent factor model nor a causal decomposition. It is: summarize messages into episodes, extract fact strings, embed facts, cluster into LLM-summarized themes, retrieve across those layers. The transformation is real but is symbolic/semantic distillation plus vector clustering — a concrete instance of [distillation](../../notes/definitions/distillation.md) rather than the deeper decomposition the paper's title suggests.

**"Free energy" framing is vocabulary, not mechanism.** `PredictionCorrectionEngine` comments reference the free-energy principle, but the pipeline is: vector-retrieve relevant statements, LLM-predict episode from title, LLM-extract gaps. No variational bound, no actual free-energy quantity. The prediction step is useful because it asks the LLM where its current semantic memory would fail, but the label over-sells the machinery.

**The sparsity+semantics objective governs local maintenance, not global retrieval.** `f = SparsityScore + SemScore` appears inside `_maybe_split_*` and `_maybe_merge_themes` to pick candidate clusterings. The retrieval path uses hard-tuned thresholds (`0.62`, `0.52`, `0.72`, `0.78`, `-0.4`, `-0.45`, `0.25`), not this objective. That is a reasonable engineering split but disagrees with the paper's suggestion that sparsity-semantics is a global retrieval driver.

**The entropy gate is permissive by design.** In `_search_adaptive_hier`, `ig = H_before - H_after` is thresholded at `tau_ep = -0.45` for inclusion and `tau_ep_stop = -0.4` for early stop. Both are negative, so episodes that slightly *increase* estimated answer uncertainty can still be included. Raw expansion uses a positive threshold (`tau_ep_expand = 0.25`). The gate is therefore an early-stop-plus-severe-harm filter at the episode layer, but a strict information-gain filter at the raw-message layer. This is an engineering choice that trades answer token cost against expansion cost; the paper can be read as stronger.

**Duplicate prevention is effectively disabled by default.** `statement_similarity_threshold` defaults to `0.7` inside the prediction-correction retrieval path, but semantic dedup at write time in the default config uses a similarity cutoff of `1`, which cosine values almost never exceed. Theme merging catches near-duplicates at the cluster level (`MERGE_THRESHOLD = 0.78`), but semantic memories themselves remain append-oriented. Lifecycle operations (deduplication below exact match, contradiction handling, revision, confidence decay) are not implemented.

**The benchmark target is conversational recall, not agent competence.** LoCoMo and PerLTQA measure whether a system can answer questions from long dialogue. Useful and legitimate, but narrower than the commonplace concern that memory must improve action capacity: classification, planning, writing, debugging, maintenance. xMemory is strong evidence for context-efficient dialogue QA; it does not test whether the same hierarchy helps an agent *act* better.

**Trace-derived learning placement.** xMemory is a **conversation-trace artifact-learning system** with an unusual four-resolution ladder.

*Trace source.* The raw signal is ordered conversation transcripts from LoCoMo/PerLTQA, fed through `evaluation/locomo/add.py` as per-user session messages with timestamps and roles. The trigger boundary is per-message into a buffer, with an LLM-gated boundary detector deciding when to close an episode; theme and graph updates fire per-user-batch after `flush()`. There is no per-run or per-tournament trigger — it is a one-pass ingestion of benchmark conversations.

*Extraction.* Four retrieval resolutions are involved: raw messages, episode summaries with titles, semantic fact strings via `PredictionCorrectionEngine` — either cold-start prompting or prediction-plus-gap prompting against the retrieved top relevant statements — and theme summaries via LLM over member facts. The derived content artifacts are the episode, semantic, and theme JSONL files; the `.npy` theme matrices; the semantic kNN JSON; and the GEXF hierarchy export. The oracle for what becomes signal is LLM judgment at every stage (boundary, episode, fact, theme, entropy-for-inclusion) with thresholded cosine similarity as a secondary gate. There is no human rater and no task-outcome signal.

*Promotion target.* All promotion is into derived artifacts and indexes: symbolic JSONL episode, semantic, and theme files, plus `.npy` theme vectors, semantic kNN JSON, and GEXF export as derived index or visualization artifacts. No weight updates, no fine-tuning, no reward-model objective. Per-user storage under `config.storage_path` persists across runs and is reused by the retrieval framework, so it is service-owned rather than ephemeral. Artifacts are mostly append-only; only the theme layer has active split/merge maintenance under the sparsity+semantics objective.

*Scope.* Per-user memory — each LoCoMo speaker pair produces its own per-user directory — but not cross-task. The extracted facts and themes are designed to serve future questions on the *same* conversation, not to transfer across conversations or tasks.

*Timing.* Offline relative to any live agent: ingestion happens before the retrieval script runs, the hierarchy graph is built per-user-batch, and the entropy gate at inference time uses a local HF model over already-persisted artifacts. There is no online memory-write during deployment.

*Position on the survey axes.* On [axis 1](../trace-derived-learning-techniques-in-related-systems.md) (ingestion pattern), xMemory is adjacent to **service-owned trace backends** because it owns its JSONL/Chroma/kNN/GEXF layout, but it is not a full service-owned backend under the survey definition; unlike OpenViking or REM it runs as a benchmark harness rather than an API-fronted service. On [axis 2](../trace-derived-learning-techniques-in-related-systems.md) (representational form), it is firmly **symbolic artifact learning**. Within that branch, xMemory is a new four-layer-ladder example, but the current code fits the symbolic-artifact branch as a benchmark-harness boundary case rather than evidence for a new subtype. The claim it most strengthens is the survey's point that log format (here, ordered per-user dialogue with role and timestamp) constrains what can be learned: the four-layer ladder only makes sense because the trace is coherent and bounded, and the entropy gate only works because the downstream task is a closed-form QA.

## What to Watch

- Whether the code is packaged as a library or MCP service rather than staying a benchmark harness.
- Whether ablations isolate the marginal gain from the theme hierarchy versus LLM extraction, vector retrieval, and entropy-gated expansion.
- Whether the information-gain thresholds are recalibrated to positive uncertainty reduction rather than permissive negatives.
- Whether semantic memories grow lifecycle management (deduplication below exact match, contradiction handling, revision, confidence decay) or stay append-only.
- Whether the GEXF hierarchy becomes an active retrieval substrate rather than an export/visualization artifact.
- Whether evaluation expands beyond LoCoMo/PerLTQA into agent tasks where memory must improve action capacity, not just answer recall.

---

Relevant Notes:

- [agent-memory-is-a-crosscutting-concern-not-a-separable-niche](../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) — grounds: xMemory touches storage, retrieval, and learning, but its evidence is strongest at retrieval over dialogue traces
- [a-knowledge-base-should-support-fluid-resolution-switching](../../notes/a-knowledge-base-should-support-fluid-resolution-switching.md) — exemplifies: the theme -> semantic -> episode -> raw-message ladder is an automated resolution-switching mechanism
- [charting-the-knowledge-access-problem-beyond-rag](../../notes/charting-the-knowledge-access-problem-beyond-rag.md) — extends: a concrete attempt to move past flat RAG by adding derived views and conditional expansion
- [distillation](../../notes/definitions/distillation.md) — exemplifies: episodes, semantic facts, and themes are successive distillations of the source conversation trace
- [automating-kb-learning-is-an-open-problem](../../notes/automating-kb-learning-is-an-open-problem.md) — contrasts: xMemory automates trace-to-artifact promotion for benchmark QA; commonplace keeps durable curation oracle-backed
- [trace-derived-learning-techniques-in-related-systems](../trace-derived-learning-techniques-in-related-systems.md) — extends: a conversation-trace, symbolic-artifact learning case with a four-layer ladder and entropy-gated raw expansion
- [files-not-database](../../notes/files-not-database.md) — contrasts: xMemory uses JSONL as storage but relies on derived Chroma/kNN/GEXF indexes as the real retrieval interface
- [an-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trusted-knowledge](../../notes/an-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trusted-knowledge.md) — contrasts: xMemory delivers discoverable derived artifacts but lacks composable claim structure and trusted curation
