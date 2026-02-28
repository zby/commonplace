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

- [agents-navigate-by-deciding-what-to-read-next](./observations/agents-navigate-by-deciding-what-to-read-next.md) — links, skills, and index entries are all contextual hints for read/skip decisions
- [two-kinds-of-navigation](./observations/two-kinds-of-navigation.md) — link-following is local with context; search is long-range with titles/descriptions; indexes bridge both
- [topic-links-from-frontmatter-are-deterministic](./observations/topic-links-from-frontmatter-are-deterministic.md) — the areas-to-Topics mapping is mechanical, now automated (outdated — see ADR)
- [stale-indexes-are-worse-than-no-indexes](./observations/stale-indexes-are-worse-than-no-indexes.md) — a missing index entry suppresses search; the note becomes invisible

## Decisions

- [001-generate-topic-links-from-frontmatter](./adr/001-generate-topic-links-from-frontmatter.md) — replace LLM-generated Topics footers with deterministic script

## Analysis

- [backlinks](./backlinks.md) — use cases for inbound link visibility: hub identification, source-to-theory bridging, impact assessment, tension surfacing; four design options with trade-offs

## Reference material

- [link-contracts-framework](./link-contracts-framework.md) — framework for systematic, testable linking: link contracts, intent taxonomy, agent implications
- [Toulmin argument](../sources/purdue-owl-toulmin-argument.md) — formal argumentation theory behind link semantics: "since [X]" and "because [Y]" links encode Toulmin warrants connecting grounds to claims; the six-part model (claim/grounds/warrant/qualifier/rebuttal/backing) names the structure argumentative links carry
- [Agentic Note-Taking 23: Notes Without Reasons](../sources/agentic-note-taking-23-notes-without-reasons-2026894188516696435.working.md) — practitioner validation: an agent inside a curated graph contrasts propositional link semantics ("since [X]") with embedding-based adjacency, arguing the difference is one of kind not degree; strongest external evidence for why link quality (not quantity) determines graph health

---

Agent Notes:
- 2026-02-24: added Foundations section with title-as-claim-enables-traversal-as-reasoning. The note belongs here because it's fundamentally about link semantics: "since [X]" vs "see [X]" is the distinction between argumentative and referential links, which determines how links function as reasoning connectors. The link-contracts-framework's intent taxonomy is the systematic version of what this note describes for inline prose links. Together with agents-navigate, these form a chain: title-as-claim explains WHY claim titles work -> agents-navigate explains HOW agents use that signal -> link-contracts provides the RULES for maintaining link quality.
- 2026-02-26: added Toulmin argument source to Reference material. The Toulmin model provides the formal theory behind the argumentative link semantics described in title-as-claim and link-contracts — "since [X]" is a warrant, "because [Y]" connects grounds to claim. The six-part decomposition (claim/grounds/warrant/qualifier/rebuttal/backing) names what we do intuitively when writing inline argumentative links.
- 2026-02-26: added Notes Without Reasons source. The article is the strongest external validation for the links index's core thesis: an agent operating inside a curated graph describes from first-person the qualitative difference between propositional links and embedding-based adjacency. It also provides the negative case that our notes theorize about but don't demonstrate — what happens when link quality fails: the agent learns to discount all links, genuine connections get buried under noise, and the system that measures health by connection count doesn't know it's sick.
