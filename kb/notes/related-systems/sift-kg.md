---
description: LLM-powered document-to-knowledge-graph pipeline with schema discovery, human-in-the-loop entity resolution, and interactive visualization
type: note
areas: [related-systems]
status: current
last-checked: 2026-03-07
---

# sift-kg

A CLI tool that turns document collections into browsable knowledge graphs. Point it at a folder of PDFs/DOCX/HTML, and it extracts entities and relations via LLM, deduplicates with your approval, generates narrative summaries, and serves an interactive force-directed viewer in the browser. Built by Juan Ceresa (University of Michigan), MIT-licensed, ~12K lines of Python across 9 modules. Version 0.8.11, 115 commits.

**Repository:** https://github.com/juanceresa/sift-kg
**Verification run:** `uv run --with pytest python -m pytest -q` on March 7, 2026 — 250 passed, 9 skipped

## Core Ideas

**LLM as the extraction engine, not the knowledge store.** Documents are chunked (10K chars, 10% overlap), each chunk sent to an LLM that returns structured JSON with entities, relations, confidence scores, and source evidence. The graph is built from these extractions deterministically — the LLM proposes, the graph stores.

**Schema-free by default.** Instead of requiring upfront ontology design, sift-kg samples 5 document chunks and asks the LLM to *design* entity and relation types tailored to the corpus. The discovered schema is cached to `discovered_domain.yaml` and reused across all subsequent chunks, preventing type drift. Predefined domains (general, OSINT, academic) are available when you want a fixed schema.

**Pipeline state is persisted as explicit files, not implicit runtime memory.** Extraction JSONs, graph JSON, merge proposals, relation review queues, and narrative outputs are all materialized and replayable. The stage boundaries (`extract -> build -> resolve -> review -> apply-merges -> narrate -> view/export`) are clean and auditable.

**Multi-layered deduplication with human gating.** Three layers: (1) deterministic pre-dedup during build — Unicode normalization, title stripping, singularization, SemHash fuzzy matching at 0.95 threshold; (2) LLM-based entity resolution that proposes merges with confidence scores; (3) human review where you approve/reject each merge in a terminal UI or by editing YAML directly. Nothing merges without approval.

**Human review gates are operational, not performative.** Merge and relation decisions are tracked as `DRAFT/CONFIRMED/REJECTED` and only applied when explicitly confirmed.

**Confidence as a first-class concept.** Every entity and relation carries a confidence score. Multiple mentions of the same triple are aggregated via product-complement (`1 - Π(1-c)`), so independent weak signals reinforce each other. Repeated mentions also preserve `support_count` and `support_documents`, making downstream filtering and review practical.

**Evidence provenance throughout.** Every extraction links back to the source document and passage. Entity context quotes travel through the pipeline — merged during dedup, injected into narrative generation, displayed in the viewer. The chain from source text to graph node to narrative sentence is traceable.

**Graph postprocessing inspired by KG literature.** Five cleanup stages after graph construction: passive relation activation (ENABLED_BY → ENABLES), self-loop/transitive redundancy removal, relation type normalization against the domain schema, direction fixing based on source/target type constraints, and pruning of isolated metadata-only entities. Cites arXiv:2408.11975.

**Narrative generation as a pipeline stage.** Not just a graph — generates a prose report with an overview, key relationship chains (shortest paths among top entities), chronological timeline from date-bearing attributes, and entity profiles grouped by Louvain communities. Has a 21-pattern banned-phrase filter that detects and rewrites LLM jargon ("played a pivotal role").

**Testing is strong for an alpha release.** The project presents as alpha but still carries broad automated coverage across config, extraction models, graph logic, resolve flows, and review workflows.

## Comparison with Our System

sift-kg and commonplace operate at different levels: sift-kg is a *processing pipeline* that transforms raw documents into a knowledge graph artifact. Commonplace is a *knowledge methodology* that structures how an agent reads, writes, connects, and navigates notes over time. The interesting comparison is in how each system models knowledge.

| Dimension | sift-kg | Commonplace |
|---|---|---|
| Knowledge unit | Entity node + relation edge | Note (markdown file with frontmatter) |
| Primary artifact | Derived knowledge graph | Authored note graph |
| Schema | Ontology of entity/relation types (discovered or predefined) | Type system of document types (note, structured-claim, index, ADR) |
| Connection model | Typed directed edges with confidence | Typed links with explicit relationship semantics |
| Stage state | Explicit pipeline files (`merge_proposals.yaml`, `relation_review.yaml`) | Workflow conventions and note/task files |
| Discovery | LLM extraction from source documents | Agent reading + human writing |
| Quality control | Deterministic graph cleanup + human approval queue | Validation rules + writing conventions |
| Confidence model | Numeric confidence on entities/relations, aggregated | Qualitative confidence encoded in prose/status |
| Primary consumer | Human analyst via viewer/exports | AI agent via file reads |
| Source handling | Extract-and-discard (entities survive, source text quoted) | Snapshot-and-ingest (source preserved alongside analysis) |
| Evolution model | Pipeline re-runs (extract → build → resolve) | Continuous note editing and connection |
| Scale assumption | Hundreds of documents, thousands of entities | Hundreds of notes, dozens of indexes |

**Where they diverge fundamentally:** sift-kg's knowledge graph is a *derived artifact* — generated from source documents, disposable, re-generable. Commonplace notes are *primary artifacts* — written once, evolved over time, not derivable from anything upstream. sift-kg optimizes for extraction fidelity and deduplication. Commonplace optimizes for compositional retrieval and agent navigation.

**Where they align:** Both treat confidence/status as first-class metadata. Both enforce relationship semantics (sift-kg via typed edges, commonplace via link-must-articulate-relationship). Both have a progressive disclosure pattern (sift-kg: entity descriptions loaded on demand in viewer; commonplace: descriptions loaded at startup, full content on demand). Both resist fully automated pipelines — sift-kg gates merges on human review, commonplace gates knowledge on agent writing quality.

## Borrowable Ideas

### Ready to borrow now

- **Schema discovery from sources.** sift-kg's technique of sampling documents and asking the LLM to design a domain schema is directly applicable to ingestion workflows. When `/ingest` processes a new domain of sources, we could ask the LLM to propose what areas/topics the source suggests, rather than requiring manual tagging.
- **Banned-phrase filters for LLM writing.** The post-generation quality filter — a regex list of LLM jargon patterns that trigger rewriting — is a practical mechanism for enforcing writing conventions. Could be adapted into our WRITING.md workflow as an automated lint pass after agent note generation.
- **Review queues as first-class artifacts.** The `DRAFT -> CONFIRMED/REJECTED` file protocol is a clean pattern for any high-impact transformation where reversible checkpoints matter.
- **Stage-shaped output contracts.** The explicit output surface makes it easy to resume, audit, and diff pipeline runs.

### Needs a concrete use case first

- **Confidence aggregation via product-complement.** The formula `1 - Π(1-c)` for combining independent confidence scores is elegant and well-motivated. If commonplace ever tracks connection strength or claim confidence numerically, this is the right aggregation function.
- **Evidence-support fields on links.** `support_count`, `support_documents`, and mention-level provenance are useful patterns if we later score connection strength in KB links.
- **Deterministic pre-dedup before LLM resolution.** The layered approach — handle the trivial cases (Unicode, titles, plurals, fuzzy strings) deterministically before involving the LLM — is a sound engineering pattern. Applicable if commonplace ever needs to deduplicate notes or sources at scale.
- **Relationship chain discovery.** Finding shortest paths between top entities and narrating the intermediary links is a compelling way to surface non-obvious connections. Could power a `/connect` enhancement that traces multi-hop paths between notes. Architecturally distant — our graph is implicit in links, not an explicit NetworkX object.
- **Schema discovery as a default route.** Useful only if we have workflows where manual type assignment is the main bottleneck.
- **Graph-first intermediate representation.** Powerful for discovery tasks, but only worth introducing if note-link traversal stops being expressive enough.

## Comparison with Cognee

[Cognee](../../sources/cognee-knowledge-engine.ingest.md) solves the same core problem — LLM-driven document-to-knowledge-graph extraction with explicit pipeline stages — but makes the opposite schema bet. sift-kg discovers schemas from the corpus: sample 5 chunks, ask the LLM to design entity and relation types, cache the result. Cognee requires schemas upfront: developers define custom Pydantic models specifying which entities and relationships to extract.

The trade-off is cold-start cost vs. extraction precision. sift-kg avoids the "what entities should I define?" problem entirely — you point it at documents and it proposes a schema. But discovered schemas may be noisy or inconsistent across corpora. Cognee's Pydantic schemas guarantee that extraction conforms to the developer's domain model, but the developer must already understand the domain well enough to write that model — a chicken-and-egg problem for unfamiliar domains.

Both systems share pipeline-first architecture with explicit stage boundaries (sift-kg: extract→build→resolve→review; Cognee: add→cognify→memify) and materialized intermediate state. The deeper difference is who does the ontology work: the LLM (sift-kg) or the developer (Cognee). This axis — schema discovery vs. schema definition — cuts across all document-to-KG systems and is orthogonal to other design choices like storage backend or confidence handling.

## What to Watch

- **Per-document cost accounting is currently broken.** `extractor.py` computes `cost_for_doc` from `getattr(r, "_cost", 0.0)`, but `ExtractionResult` has no `_cost` field, so document-level `cost_usd` remains `0.0`.
- **Dependency metadata includes a stale extra.** `pyproject.toml` declares `typer[all]>=0.9.0`, which now emits a warning with current Typer releases.
- **Resolution still scales as full-graph work.** Incremental extraction exists, but duplicate resolution still re-scans graph entities by type, which may become the dominant runtime on very large corpora.
- sift-kg is early (v0.8, alpha status). The schema-free discovery is the most novel feature — watch whether discovered schemas converge to useful ontologies or produce noisy, inconsistent types across corpora.
- The project sits upstream of Civic Table, a forensic intelligence platform with 4-tier analyst verification. If that matures, the review/verification workflow could inform how commonplace handles claim validation.
- The viewer is a strong reference for how to present knowledge graphs interactively — community regions, focus mode with keyboard navigation, trail breadcrumbs. Worth revisiting if commonplace ever needs a graph view.

---

Relevant Notes:

- [Cognee](../../sources/cognee-knowledge-engine.ingest.md) — contrasts: same problem (LLM document-to-KG pipeline) but opposite schema bet — Cognee requires upfront Pydantic schemas where sift-kg discovers schemas from corpus samples
- [Siftly](./siftly.md) — contrasts: similar ingestion ambition but uses SQLite and deterministic-first enrichment rather than LLM extraction
- [deterministic-validation-should-be-a-script](../deterministic-validation-should-be-a-script.md) — foundation: deterministic cleanup around stochastic extraction follows the same hard-oracle direction
- [a-functioning-kb-needs-a-workshop-layer-not-just-a-library](../a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — example: review queues are concrete workshop artifacts for controlled transformation
- [Related Systems Index](./related-systems-index.md) — master index of tracked systems

Topics:

- [related-systems](./related-systems-index.md)
