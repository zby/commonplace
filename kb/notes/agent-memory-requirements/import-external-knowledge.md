---
description: "Agent memory systems need import paths when authoritative project knowledge already exists outside the memory substrate"
type: kb/types/note.md
traits: [has-external-sources]
tags: [agent-memory, context-engineering]
---

# Import External Knowledge Into Internal Form

Not all memory starts inside the current session. When authoritative or useful project knowledge already exists outside the memory system, the system should import external knowledge bases, documents, repositories, source snapshots, tickets, notes, or prior archives into its own internal form.

Import is not copying. It is a condensing (directed context compression) and [constraining](../definitions/constraining.md) (narrowing interpretation space) step that converts external material into artifacts that obey the receiving system's types, links, quality requirements, provenance rules, and retrieval surfaces.

## Methods

- Snapshots that preserve external sources before analysis.
- Ingest reports or source reviews that classify material, summarize it, name limitations, and link it into the internal graph.
- Conversion tools that turn raw text or legacy notes into typed internal artifacts.
- Directory or repository ingestion that treats a related file tree as one source unit.
- Re-ingest workflows that rerun classification and connection after the internal KB has changed.
- Staging in a [workshop](../a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) when the imported material is too large, messy, or contested to promote directly.

## Related Systems

[sift-kg](../../agent-memory-systems/reviews/sift-kg.md) is a partial fulfillment of this import need in a document-to-graph setting. It turns document folders into a derived knowledge graph with discovered schemas, materialized pipeline stages, confidence scores, provenance, and human-gated merge or relation review. The implementation shows what import requires beyond "upload documents": schema choice, source preservation, deduplication, review state, and derived artifacts that can be regenerated.

## Evaluation Questions

- Is import conditional on external project knowledge actually existing?
- Does the import preserve source evidence and limitations?
- Does imported material gain the receiving system's artifact contracts, links, provenance, and trust markers?
- Can the system re-run or update the import as internal knowledge changes?

---

Relevant Notes:

- [Designing a Memory System for LLM-Based Agents](../designing-agent-memory-systems.md) - places import inside the broader requirements map
- [A functioning KB needs a workshop layer, not just a library](../a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) - enables staged handling of messy imports
