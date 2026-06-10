---
description: Index of notes about linking — how links work as decision points, navigation modes, link contracts, and automated link management
type: kb/types/index.md
index_source: tag
index_key: links
status: current
---

# Links

Links are the edges of the knowledge graph. Every link is a decision point for the reader: follow or skip? The quality of surrounding context determines whether that decision is informed or blind.

## Prior work

Typed relationships between knowledge units have deep roots:

- **Hypertext theory** (Engelbart, 1968; Nelson, 1965) — the original vision of interlinked documents with explicit relationship types, not just navigation.
- **Semantic Web / RDF** (Berners-Lee, 2001) — subject-predicate-object triples formalize typed links between resources. OWL adds relationship semantics (transitive, symmetric, inverse).
- **Library science thesauri** (ISO 25964) — standardized relationship types: BT (broader term), NT (narrower term), RT (related term), USE/UF. Decades of practice in what relationship types are worth maintaining.
- **Toulmin argumentation** — already used in the KB; listed in Reference material below.

Our link semantics (extends, grounds, contradicts, exemplifies) are lighter than RDF but heavier than untyped hyperlinks. The specific contribution is optimizing for agent navigation under bounded context — links as decision points for read/skip, not just edges in a graph.

**TODO:** This survey is from the agent's training data, not systematic. Library science thesaurus standards likely have directly applicable results about relationship type taxonomies.

## Foundations

- [title-as-claim-enables-traversal-as-reasoning](./title-as-claim-enables-traversal-as-reasoning.md) — claim titles make link traversal read as reasoning; explains why "since [X]" works but "see [X]" is a different link intent, and where the pattern breaks for multi-claim documents

## Observations

- [agents-navigate-by-deciding-what-to-read-next](./agents-navigate-by-deciding-what-to-read-next.md) — links, skills, and index entries are all contextual hints for read/skip decisions
- [two-kinds-of-navigation](./link-following-and-search-impose-different-metadata-requirements.md) — link-following is local with context; search is long-range with titles/descriptions; indexes bridge both
- [stale-indexes-are-worse-than-no-indexes](./stale-indexes-are-worse-than-no-indexes.md) — a missing index entry suppresses search; the note becomes invisible (now in [maintenance](./kb-maintenance-index.md))

## Analysis

- [backlinks](./backlinks.md) — use cases for inbound link visibility: hub identification, source-to-theory bridging, impact assessment, tension surfacing; four design options with trade-offs
- [link-strength-is-encoded-in-position-and-prose](./link-strength-is-encoded-in-position-and-prose.md) — inline premise links carry more weight than footer links; position and prose encode commitment level, creating a weighted graph
- [distilled-artifacts-need-source-tracking-at-the-source](./distilled-artifacts-need-source-tracking-at-the-source.md) — distilled artifacts shouldn't link back to sources (focus), but sources should link forward via "Distilled into:" so source changes trigger staleness review

## Decisions

- [009-link-relationship-semantics](../reference/adr/009-link-relationship-semantics.md) — adopts extends/grounds/contradicts/enables/exemplifies vocabulary, borrowed from arscontexta and adapted for agent navigation

## Theory

- [linking-theory](./linking-theory.md) — seedling: open questions about what makes links load-bearing, how relationship types interact with position, and what a principled linking theory would predict

## Reference material

- [Toulmin argument](https://owl.purdue.edu/owl/general_writing/academic_writing/historical_perspectives_on_argumentation/toulmin_argument.html) — formal argumentation theory behind link semantics: "since [X]" and "because [Y]" links encode Toulmin warrants connecting grounds to claims; the six-part model (claim/grounds/warrant/qualifier/rebuttal/backing) names the structure argumentative links carry
- [Agentic Note-Taking 23: Notes Without Reasons](https://x.com/molt_cornelius/status/2026894188516696435) — practitioner validation: an agent inside a curated graph contrasts propositional link semantics ("since [X]") with embedding-based adjacency, arguing the difference is one of kind not degree; strongest external evidence for why link quality (not quantity) determines graph health
- [A-MEM: Agentic Memory for LLM Agents](https://arxiv.org/abs/2502.12110) — empirical counterpoint: embedding-based link generation succeeds on QA benchmarks, demonstrating that adjacency-as-linking works for retrieval accuracy even if it lacks propositional semantics; the question is whether the quality gap matters only for navigability and agent reasoning
