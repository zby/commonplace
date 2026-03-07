# Commonplace Knowledge Base

Commonplace is a framework for building **agent-operated knowledge bases** — structured markdown files that an AI agent can autonomously navigate, extend, and maintain. This repo uses its own knowledge system to document the methodology for building them.

**The content is AI-generated** through human-AI collaboration: a human directs the inquiry, and AI agents draft, connect, and maintain the notes.

## Key ideas

**Title as claim, not topic.** Note titles are assertions that work as prose when linked: "context efficiency is the central design concern in agent systems" instead of "context efficiency". Following links reads like a chain of reasoning.

**Progressive refinement.** Capture with zero friction — a file with no frontmatter is a valid `text` type with zero structural requirements. Add frontmatter to make it a `note`. Add Evidence/Reasoning/Caveats sections to make it a `structured-claim`. Structure is earned, not imposed.

**Files, not database.** Universal interface, free versioning via git, zero infrastructure. Derived indexes solve scale problems without replacing the source of truth.

**The network IS the knowledge.** Individual notes matter less than their relationships. Every link must articulate its relationship (extends, grounds, contradicts, exemplifies) — "related" is not a relationship. An unconnected note is invisible.

**First-principles design.** The KB's architecture is derived from constraints of the medium — finite context windows, stateless agents, text-in/text-out processing — not adopted from convention. We [borrow widely but filter by first principles](./notes/design-methodology-borrow-widely-filter-by-first-principles.md), selecting for [explanatory reach over adaptive fit](./notes/first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md).

## Starting points

- [KB design](./notes/kb-design.md) — architecture, skills, evaluation, and design principles
- [Learning theory](./notes/learning-theory.md) — how systems learn, verify, and improve: stabilisation, distillation, discovery
- [Areas](./notes/areas.md) — all topic areas at a glance
- [Linking methodology](./notes/links.md) — how notes connect and what link semantics mean
- [Related systems](./notes/related-systems/related-systems-index.md) — comparisons with other knowledge and agent memory systems
- [Writing guide](./WRITING.md) — conventions, templates, and quality checklist
- [Notes directory](./notes/index.md) — auto-generated listing of all notes
- [Sources](./sources/index.md) — snapshotted external sources and analyses
