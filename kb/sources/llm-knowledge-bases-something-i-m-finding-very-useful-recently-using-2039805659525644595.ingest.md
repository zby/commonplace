---
description: Karpathy on agent-maintained research wikis in Obsidian — index files and brief summaries replacing fancy RAG at roughly 100-article scale
source_snapshot: llm-knowledge-bases-something-i-m-finding-very-useful-recently-using-2039805659525644595.md
ingested: "2026-04-03"
type: kb/sources/types/ingest-report.md
source_type: practitioner-report
domains: [knowledge-management, context-engineering, file-based-systems, agentic-workflows]
---

# Ingest: LLM Knowledge Bases

Source: llm-knowledge-bases-something-i-m-finding-very-useful-recently-using-2039805659525644595.md
Captured: 2026-04-03T15:30:57.200477+00:00
From: https://x.com/karpathy/status/2039805659525644595

## Classification
Type: practitioner-report — a first-person workflow report describing how Karpathy uses LLMs to build and maintain a research wiki in markdown, with concrete mechanics and scale numbers but no directly inspectable repo or evaluation artifacts.
Domains: knowledge-management, context-engineering, file-based-systems, agentic-workflows
Author: Andrej Karpathy is a high-signal AI practitioner, so the workflow is worth attending to as practitioner testimony, but this is still anecdotal self-report from a single X post.

## Summary
Karpathy describes using LLMs to build personal research knowledge bases as file-backed markdown wikis: sources land in a `raw/` directory, an LLM incrementally compiles summaries, backlinks, concept pages, and indexes, and Obsidian serves as the human-facing frontend for reading both raw materials and derived artifacts. The central claim is that, at roughly 100 articles / 400K words, he did not need "fancy RAG" because auto-maintained index files and brief summaries were enough for the agent to navigate the corpus and answer complex questions. He also treats querying as a learning loop: answers are rendered as markdown, slides, or plots and often filed back into the wiki, while separate LLM "health checks" scan for inconsistencies, missing data, and candidate new articles.

## Connections Found
`/connect` placed this source in the file-first / durable-artifact / navigation cluster. It strongly exemplifies [vibe-noting](../notes/vibe-noting.md) and [continual-learning-open-problem-is-behaviour-not-knowledge](../notes/continual-learning-open-problem-is-behaviour-not-knowledge.md): knowledge work compounds because the agent operates on inspectable artifacts and files outputs back into the KB. It also strengthens [files-not-database](../notes/files-not-database.md) and [agents-navigate-by-deciding-what-to-read-next](../notes/agents-navigate-by-deciding-what-to-read-next.md) by showing a concrete retrieval layer built from maintained summaries, backlinks, and index files rather than a separate vector stack. The most interesting extension is to [knowledge-storage-does-not-imply-contextual-activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md): the source's real mechanism is not "the model can read a lot," but "the wiki contains symbolic activation scaffolds that tell the model what to load next." On the tool/interface side, [Napkin](../agent-memory-systems/reviews/napkin.md) is the closest adjacent system: an Obsidian-compatible, progressive-disclosure CLI formalizing the same human/agent coexistence pattern.

## Extractable Value
1. **[quick-win] Maintained index files and brief summaries can replace fancy RAG at small KB scale.** The surprising claim in the post has a simpler, stronger account: Karpathy did build retrieval infrastructure, but it lives as inspectable symbolic artifacts inside the file substrate rather than as a separate vector/RAG stack. High reach: this transfers to any small-to-medium corpus where the real bottleneck is navigation, not raw storage.
2. **[quick-win] Activation scaffolds matter more than raw storage.** The post is a concrete practitioner instance of the activation gap: stored knowledge became usable because the wiki maintained summaries, backlinks, and indexes that cued the model to load relevant documents. High reach: this supports the idea that many "memory" problems are really routing/activation problems.
3. **[quick-win] Query outputs become learning when they are filed back into the KB.** Rendering answers as markdown, slides, or plots and then re-filing them turns question answering from an ephemeral service into durable capacity change. High reach: the mechanism transfers beyond research wikis to any artifact-based workflow.
4. **[experiment] KB "health checks" are a viable narrow-scope mutation loop.** Inconsistency scans, missing-data imputation, and candidate-article suggestion are concrete examples of automated KB mutations that seem useful before solving the harder oracle problem for wide-scope synthesis. Medium-high reach: this is exactly the tractable end of the mutation spectrum.
5. **[deep-dive] A raw/compiled split is a useful file-based KB architecture.** The `raw/` directory plus compiled wiki pattern keeps capture and derived knowledge separate without leaving the plain-file substrate. Medium reach: worth comparing against our library/workshop distinction and other file-first systems.
6. **[just-a-reference] Obsidian is the interface layer, not the storage model.** The important property is not Obsidian specifically, but a familiar human frontend over agent-maintained files. Useful mostly as comparison material alongside Napkin and other Obsidian-adjacent systems.

## Limitations (our opinion)
- **The "no fancy RAG" claim risks overstating model capability.** The post's own description implies the opposite simpler account: maintained summaries, backlinks, and index files are load-bearing retrieval scaffolds. If those artifacts disappeared, the claimed performance would likely disappear too. The real lesson is about symbolic navigation artifacts, not retrieval-free long-context magic.
- **This is self-report from one practitioner.** We do not see the repo, the prompts, the failure cases, the maintenance burden, or the proportion of bad suggestions from the health checks. The workflow is plausible and interesting, but not independently inspectable.
- **The scale regime is explicitly small.** Roughly 100 articles / 400K words is already enough to be interesting, but it is still far below the scale where curation, index upkeep, and filed-back outputs become a serious maintenance problem. The post does not show that this pattern holds at much larger corpus sizes.
- **The capture is incomplete.** The X snapshot contains only the main post; replies or clarifications were not captured because thread fetch failed during snapshotting. Any nuance added later in the thread is missing here.

## Recommended Next Action
Write a note titled **"Maintained index files and brief summaries can replace fancy RAG at small KB scale"** connecting to [agents-navigate-by-deciding-what-to-read-next](../notes/agents-navigate-by-deciding-what-to-read-next.md), [files-not-database](../notes/files-not-database.md), and [knowledge-storage-does-not-imply-contextual-activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md). It would argue that Karpathy's success comes from symbolic activation scaffolds inside the file substrate, not from retrieval-free long-context capability.
