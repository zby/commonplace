---
description: Adopts a fixed vocabulary of link relationship types (extends, grounds, contradicts, enables, exemplifies) borrowed from arscontexta and adapted for agent navigation under bounded context
type: adr
tags: [links]
status: accepted
---

# 009-Link relationship semantics

**Status:** accepted
**Date:** 2026-02-21

## Context

Untyped links ("see also", "related") tell a reader that two notes are connected but not *how*. An agent navigating under context pressure needs to decide whether following a link will advance its task — and "related" gives no signal for that decision. Wiki-style hyperlinks are cheap to create but expensive to follow blindly.

[Ars Contexta](../related-systems/arscontexta.md) proposes propositional link semantics drawn from concept-mapping research: causes, enables, contradicts, extends, specifies, supports. The key distinction is between mind mapping ("these relate somehow") and concept mapping ("this extends that because..."). We needed a vocabulary small enough to remember and use consistently, rich enough to support agent navigation decisions.

## Decision

Every link in the KB must articulate the relationship using one of these types:

- **extends** — builds on, adds a dimension to, refines
- **grounds** (also: foundation) — provides the theoretical or evidential base
- **contradicts** — conflicts with, challenges, creates tension
- **enables** — makes possible, is a prerequisite for
- **exemplifies** (also: example) — is a concrete instance of

The relationship appears in the prose surrounding the link. In body text: `since [title](./path.md)` or `because [title](./path.md)`. In Relevant Notes footers: `- [title](./path.md) — extends: ...` with an explicit relationship word and a context phrase.

"Related" is not a relationship. If you cannot name the relationship, the link may not be worth making.

## Consequences

### Easier

- **Agent navigation** — an agent can prioritize links by type: follow "grounds" when verifying a claim, follow "contradicts" when looking for tensions, skip "exemplifies" when time is tight.
- **Graph maintenance** — typed links are testable. A "grounds" link to a note that doesn't provide evidence is a detectable error. Untyped links are unfalsifiable.
- **Traversal as reasoning** — when titles are claims and links carry relationship types, traversing the graph reads as an argument chain, not a random walk.

### Harder

- **Authoring cost** — every link requires a relationship judgment. This is intentional friction — it prevents decorative linking — but it slows writing.
- **Vocabulary drift** — the vocabulary must stay small and stable. Adding types (e.g. "supersedes", "specializes") requires explicit decision, not gradual accumulation.
- **Coverage** — some genuine relationships don't fit cleanly (temporal succession, mutual dependency, "same phenomenon from a different angle"). The vocabulary is deliberately coarse; edge cases use the closest fit with a clarifying phrase.

---

Relevant Notes:

- [Ars Contexta](../related-systems/arscontexta.md) — source: propositional link semantics vocabulary we borrowed and adapted
- [title-as-claim-enables-traversal-as-reasoning](../title-as-claim-enables-traversal-as-reasoning.md) — enables: claim titles plus typed links make traversal read as reasoning
- [link-strength-is-encoded-in-position-and-prose](../link-strength-is-encoded-in-position-and-prose.md) — extends: relationship type is one axis; position and prose encode a second axis (commitment strength)
- [agents-navigate-by-deciding-what-to-read-next](../agents-navigate-by-deciding-what-to-read-next.md) — grounds: the navigation-decision model that typed links serve
