---
description: Brainstorming on Deutsch's "reach" concept applied to KB notes — reach is a maintenance risk signal (not a retrieval signal) because high-reach revisions break downstream reasoning silently
type: note
traits: []
tags: [learning-theory, kb-maintenance]
status: seedling
---

# Brainstorming: how reach informs KB design

Deutsch's "reach" (*The Beginning of Infinity*): a good explanation applies far beyond the specific situation it was devised for. Notes in a KB vary in reach, and this variation matters — but not for the reason you might first expect.

## Notes sit on a reach spectrum

- **High reach** — constraining, distillation, context-efficiency — principles that apply across agent systems regardless of implementation
- **Medium reach** — files-not-database, short composable notes, title-as-claim — principles that apply to a class of KBs (authored, agent-navigated) but not universally
- **Low reach** — ADR 004 (tags not areas), ADR 002 (inline templates) — choices specific to this installation

The boundary between levels is not always obvious. Many notes that look like local design choices are actually medium-reach principles. Files-not-database derives from a general argument about premature schema commitment — it applies to any system that doesn't yet know its access patterns. The Graphiti section maps where that reach ends, which is exactly what good explanations do: they have clear scope, not unlimited generality.

## Reach does not obviously help retrieval

When searching for "should I use a database?", you want files-not-database regardless of its reach level. We haven't identified a retrieval scenario where knowing a note's reach would change what you look for or which results you prefer. But this deserves more thought — it's possible reach could inform ranking or filtering in ways we haven't considered.

## Reach is valuable and dangerous

Reach is the most valuable property a note can have. A high-reach note unifies many phenomena under one explanation — it replaces many narrow notes and makes the KB more coherent. A KB with only low-reach notes describes everything and explains nothing.

But reach creates fragility. The cost of changing a note is inversely related to its reach in a non-obvious way:

- **Low-reach changes** (reversing an ADR, changing a convention) can touch many files but the work is mechanical — find-and-replace frontmatter, update instructions. Agents handle this cheaply.
- **High-reach changes** (revising a foundational principle) may touch few files directly, but the downstream reasoning across many notes may silently break. The impact is conceptual, not syntactic, and hard to grep for.

So reach is worth pursuing — but it demands care. This tension shapes two practical heuristics:

1. **When writing**, push for the most general formulation the argument supports, but map the boundaries explicitly. Overclaiming reach without marking where it ends (the way files-not-database maps its Graphiti boundary) produces brittle generality.

2. **When reviewing**, clusters of similar low-reach notes suggest an unextracted higher-reach principle. Three notes making the same argument in different contexts are a signal that a general principle is waiting to be named.

## Existing machinery already covers the consolidation case

The `/connect` skill's synthesis opportunity detection watches for "a pattern across three or more notes that has not been named," and Phase 5 abstraction logging captures the same signal. The reach concept names what those checks are detecting but may not require additional tooling.

## Open questions

- Is there a practical maintenance workflow that uses reach beyond what synthesis detection already provides?
- Should high-reach notes receive more scrutiny during review (e.g., a `/validate` check for boundary-mapping)?
- Does reach deserve to be surfaced explicitly (frontmatter, tag), or is it better left implicit — something a reviewer recognizes rather than a field an author declares?

---

Relevant notes:

- [First-principles reasoning selects for explanatory reach over adaptive fit](./first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md) — **extends**: that note defines reach as a quality criterion; this note adds the maintenance counterweight — reach is also a fragility signal. Both share the open question of whether to surface reach explicitly.
- [Learning is not only about generality](./learning-is-not-only-about-generality.md) — **grounds**: the reach spectrum (high/medium/low) instantiates the generality axis defined there (facts vs theories). This note adds that maintenance cost is asymmetric by reach level.
- [A good agentic KB maximizes contextual competence](./a-good-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trustworthy-knowledge.md) — **extends**: that note discusses reach in the context of accumulation; this note adds a dimension its "trustworthiness" property needs — high-reach changes silently invalidate downstream reasoning.
- [Link-graph plus timestamps enables make-like staleness detection](./link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — **contradicts/qualifies**: high-reach changes are precisely the case where pairwise timestamp comparison fails — the defeat condition that note already anticipates.
- [Discovery is seeing the particular as an instance of the general](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) — **extends**: the consolidation heuristic ("clusters of similar low-reach notes suggest an unextracted principle") is the discovery operation reframed as a maintenance signal.
- [Entropy management must scale with generation throughput](./entropy-management-must-scale-with-generation-throughput.md) — **extends**: maintenance cost is not uniform; high-reach changes require disproportionately expensive review.
