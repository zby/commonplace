---
description: Index of notes about linking — how links work as decision points, navigation modes, link contracts, and automated link management
type: index
status: current
---

# Links

Links are the edges of the knowledge graph. Every link is a decision point for the reader: follow or skip? The quality of surrounding context determines whether that decision is informed or blind.

## Foundations

- [title-as-claim-enables-traversal-as-reasoning](./title-as-claim-enables-traversal-as-reasoning.md) — claim titles make link traversal read as reasoning; explains why "since [X]" works but "see [X]" is a different link intent, and where the pattern breaks for multi-claim documents

## Observations

- [agents-navigate-by-deciding-what-to-read-next](./agents-navigate-by-deciding-what-to-read-next.md) — links, skills, and index entries are all contextual hints for read/skip decisions
- [two-kinds-of-navigation](./two-kinds-of-navigation.md) — link-following is local with context; search is long-range with titles/descriptions; indexes bridge both
- [stale-indexes-are-worse-than-no-indexes](./stale-indexes-are-worse-than-no-indexes.md) — a missing index entry suppresses search; the note becomes invisible (now in [maintenance](./kb-maintenance-index.md))

## Decisions

- [001-generate-topic-links-from-frontmatter](./001-generate-topic-links-from-frontmatter.md) — replace LLM-generated Topics footers with deterministic script

## Analysis

- [backlinks](./backlinks.md) — use cases for inbound link visibility: hub identification, source-to-theory bridging, impact assessment, tension surfacing; four design options with trade-offs
- [link-strength-is-encoded-in-position-and-prose](./link-strength-is-encoded-in-position-and-prose.md) — inline premise links carry more weight than footer links; position and prose encode commitment level, creating a weighted graph
- [distilled-artifacts-need-source-tracking-at-the-source](./distilled-artifacts-need-source-tracking-at-the-source.md) — distilled artifacts shouldn't link back to sources (focus), but sources should link forward via "Distilled into:" so source changes trigger staleness review

## Reference material

- [link-contracts-framework](./link-contracts-framework.md) — framework for systematic, testable linking: link contracts, intent taxonomy, agent implications
- [Toulmin argument](../sources/purdue-owl-toulmin-argument.md) — formal argumentation theory behind link semantics: "since [X]" and "because [Y]" links encode Toulmin warrants connecting grounds to claims; the six-part model (claim/grounds/warrant/qualifier/rebuttal/backing) names the structure argumentative links carry
- [Agentic Note-Taking 23: Notes Without Reasons](../sources/agentic-note-taking-23-notes-without-reasons-2026894188516696435.md) — practitioner validation: an agent inside a curated graph contrasts propositional link semantics ("since [X]") with embedding-based adjacency, arguing the difference is one of kind not degree; strongest external evidence for why link quality (not quantity) determines graph health
- [A-MEM: Agentic Memory for LLM Agents](../sources/a-mem-agentic-memory-for-llm-agents.md) — empirical counterpoint: embedding-based link generation succeeds on QA benchmarks, demonstrating that adjacency-as-linking works for retrieval accuracy even if it lacks propositional semantics; the question is whether the quality gap matters only for navigability and agent reasoning
