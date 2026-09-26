---
description: "Curated head for the links tag — linking theory, link labels and relationship semantics, link position and strength, backlinks, link-following versus search navigation, and lineage links"
type: types/tag-readme.md
complete: true
---

# Links

This tag gathers notes on how links between KB artifacts work: link labels and relationship semantics, where a link sits and how strongly it commits, backlinks and inbound links, link-following versus search as navigation modes, and lineage links from sources to what was produced from them. The defining note is [linking theory](../notes/linking-theory.md), which treats each link as a read-or-skip decision point for the reader and measures link quality as navigation uncertainty removed per token of context. The shipped rules and label catalogue live in the reference page [link vocabulary and linking approach](../reference/link-vocabulary.md). Nearby but different: [context-engineering](./context-engineering-README.md) covers routing and loading knowledge into context in general; a note belongs here when its subject is the authored link itself.

## Prior work

Typed relationships between knowledge units have deep roots:

- **Hypertext theory** (Engelbart, 1968; Nelson, 1965) — the original vision of interlinked documents with explicit relationship types, not just navigation.
- **Semantic Web / RDF** (Berners-Lee, 2001) — subject-predicate-object triples formalize typed links between resources. OWL adds relationship semantics (transitive, symmetric, inverse).
- **Library science thesauri** (ISO 25964) — standardized relationship types: BT (broader term), NT (narrower term), RT (related term), USE/UF. Decades of practice in what relationship types are worth maintaining.
- **Toulmin argumentation** — already used in the KB; listed in Reference material below.

Commonplace's link labels are lighter than RDF but heavier than untyped hyperlinks: each collection's `COLLECTION.md` owns its outbound rules, and labels name the reader need a link serves ([link vocabulary](../reference/link-vocabulary.md)). The specific contribution is optimizing for agent navigation under bounded context — links as decision points for read/skip, not just edges in a graph.

## Foundations

- [Linking theory](../notes/linking-theory.md) — links as decision points; grounds the relationship vocabulary, title-as-claim, and position-encodes-strength practices under one model
- [Title as claim enables traversal as reasoning](../notes/title-as-claim-enables-traversal-as-reasoning.md) — claim titles make link traversal read as reasoning; explains why "since [X]" works but "see [X]" is a different link intent, and where the pattern breaks for multi-claim documents
- [Links encode conditional possibilities, not obligations](../notes/links-encode-conditional-possibilities-not-obligations.md) — every label names the reader need under which following pays off; content every reader needs is inlined, not linked

## Observations

- [Agents navigate by deciding what to read next](../notes/agents-navigate-by-deciding-what-to-read-next.md) — links, skills, and index entries are all contextual hints for read/skip decisions
- [Link-following and search impose different metadata requirements](../notes/link-following-and-search-impose-different-metadata-requirements.md) — link-following is local with context; search is long-range with titles/descriptions; indexes bridge both
- [Indexes lower recall when they suppress retrieval that would find more](../notes/indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md) — not a member (tagged [kb-maintenance](./kb-maintenance-README.md)): apparent completeness lowers route recall when it suppresses retrieval that would find more

## Analysis

- [Inbound and outbound links serve asymmetric reader needs](../notes/inbound-and-outbound-links-serve-asymmetric-reader-needs.md) — outbound links are authored reader aids and their on-demand inverse serves four distinct orientation needs; independently useful reciprocal links remain allowed, while the surfacing design space is [backlink surfacing](../reference/proposals/backlink-surfacing.md)
- [Link strength is encoded in position and prose](../notes/link-strength-is-encoded-in-position-and-prose.md) — inline premise links carry more weight than footer links; position and prose encode commitment level, creating a weighted graph
- [Pointer design tradeoffs in progressive disclosure](../notes/pointer-design-tradeoffs-in-progressive-disclosure.md) — fixed, query-time, and crafted retrieval pointers compared on specificity, cost, availability, accuracy, and authoring dependence
- [A linked note discharges its own grounding, so a citing note owes representation, not re-grounding](../notes/a-linked-note-discharges-its-own-grounding-so-a-citing-note-owes.md) — what a link to a reviewed claim note transfers: the citing note must represent it faithfully, not re-ground it
- [Source changes should surface downstream review targets, while reverse lineage can remain searchable](../notes/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md) — when an upstream change is recognized, a forward lineage view should surface dependent artifacts for review; the record itself need not live at the source

## Decisions

- [009-link-relationship-semantics](../reference/adr/009-link-relationship-semantics.md) — adopts extends/grounds/contradicts/enables/exemplifies vocabulary, borrowed from arscontexta and adapted for agent navigation
- [054-add-adapted-from-and-operationalized-from-lineage-relations](../reference/adr/054-add-adapted-from-and-operationalized-from-lineage-relations.md) — adds the lineage relations used as collection-authorized link labels

## Reference material

- [Toulmin argument](https://owl.purdue.edu/owl/general_writing/academic_writing/historical_perspectives_on_argumentation/toulmin_argument.html) — formal argumentation theory behind link semantics: "since [X]" and "because [Y]" links encode Toulmin warrants connecting grounds to claims; the six-part model (claim/grounds/warrant/qualifier/rebuttal/backing) names the structure argumentative links carry
- [Agentic Note-Taking 23: Notes Without Reasons](https://x.com/molt_cornelius/status/2026894188516696435) — practitioner validation: an agent inside a curated graph contrasts propositional link semantics ("since [X]") with embedding-based adjacency, arguing the difference is one of kind not degree; strongest external evidence for why link quality (not quantity) determines graph health
- [A-MEM: Agentic Memory for LLM Agents](https://arxiv.org/abs/2502.12110) — empirical counterpoint: embedding-based link generation succeeds on QA benchmarks, demonstrating that adjacency-as-linking works for retrieval accuracy even if it lacks propositional semantics; the question is whether the quality gap matters only for navigability and agent reasoning

## Related Tags

- [context-engineering](./context-engineering-README.md) — routing, loading, and progressive disclosure in general; links are one of its routing mechanisms
- [kb-maintenance](./kb-maintenance-README.md) — lineage staleness, index recall, and keeping links current as artifacts change
- [claims-and-grounding](./claims-and-grounding-README.md) — claim titles and grounding obligations that link labels and citations carry
