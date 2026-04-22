---
description: Links encode conditional possibilities, not obligations — every label must name a specific reader-need (the condition under which following pays off); content required for all reachable readers should be inlined, not linked
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, links]
status: current
---

# Links encode conditional possibilities, not obligations

## Core claim

Links encode *possibilities*, not obligations. If all reachable readers need the content, inline it. If some readers need it and others don't, link — so the subset needing it can follow, the rest can skip.

Each link is a bet on reader state:

- The author believes some readers have an unmet need at this point in the document.
- Following the link resolves that need.
- Other readers don't have the need and should skip.

The **label** names the reader-need (the condition under which following pays off). The **context phrase** names the specific one.

## Scope: inline and footer forms

The theory applies identically to both link positions. **Inline prose connectors** (`since [X]`, `because [X]`, `but [X]`) and **footer-annotated labels** (`- [title](./path.md) — label: context phrase`) both encode a reader-need. They differ only in commitment level: inline positions mark the target as a premise of the source's argument and are the strongest form; footer positions surface auxiliary follow-ups the reader may take once the core argument is read. The label grammar is the same in either position — a label that fails the reader-need test fails it as a prose connector too.

## The label test: name the reader-need

A label earns its place by naming a specific reader-need. Labels that describe document relationships instead of reader-needs are weaker — they describe the graph, not the follow-decision.

Passes the test:
- `grounds` — "reader might want to verify the premise"
- `mechanism` — "reader might want to understand how"
- `defined-in` — "reader might not know the term"
- `procedure` — "reader wants the how-to to act on this"

Weaker:
- `part-of` — names a document relation; reader-need derived at best
- `cross-reference` — almost pure graph, no specific need
- `see-also` — explicit escape hatch: "I can't name the reader-need but there's something here"

A label whose reader-need can't be stated in one sentence is a candidate to drop.

## Two reader classes

**Agent readers.** An agent's context state is partially predictable. `CLAUDE.md` is always loaded. Certain skills preload specific definitions, instructions, or index fragments. Upstream reads in the same session bring notes into context. The author can reason about what an agent probably already has before reaching a given link.

**Human readers.** Opaque context. Humans bring prior knowledge but the author can't know what they've seen or what they're currently holding. Links have to assume the worst case.

## Focus: optimise for agents

This KB is agent-operated. Agents are the primary readers.

1. **Optimise for agent follow/skip decisions.** Link vocabulary and placement should serve the agent's reading path.
2. **Agents are more predictable.** An author can bet on loaded state in ways that would be reckless for humans. This makes link decisions more tractable.
3. **Humans can follow the agent path.** A link structure optimised for agents still serves humans — possibly with some friction, but without needing a separate design. The inverse fails: human-optimised links (assume nothing pre-loaded, gloss everything, link every term) over-serve agents and waste tokens on always-already-loaded content.

When agent-optimisation and human-optimisation conflict, agents win. Don't maintain parallel vocabularies.

## "Might already be loaded" as a design axis

A link pays off only when two conditions hold:
- The reader has the need, AND
- The reader doesn't already have the answer in context.

Some content is loaded by the agent's machinery before any specific note is read: `CLAUDE.md`, frequently-invoked skill bodies, the definitions a skill pulls in. Linking to those content items is a wasted decision — the reader already has them.

Definitions are the clean case. An agent with the relevant domain skill loaded has the definitions in context; an agent working cold doesn't. First-use gloss + link handles both: the gloss covers agents with context-loaded understanding plus humans who don't need the canonical definition; the link covers agents without the skill and readers who want the full term. The link is the conditional; the gloss is the fallback.

We don't encode "assume loaded" in the vocabulary yet — too fragile, depends on skill configuration. But when a label's reader-need is almost-always-already-met for the target reader class, that's a signal the link should be cut.

## When to inline vs. link

**Inline** when:
- All reachable readers need the content.
- The content is short enough that it doesn't distort the host document.
- The content is tightly fused with the host claim — the argument can't be read meaningfully without it.

**Link** when:
- Only some readers need the content (conditional on task, skill, prior knowledge).
- The content stands as its own unit with its own reach.
- The host document's argument survives without the linked content.

If the host argument doesn't survive without the linked content, don't link — restructure so both are in the same document, or fold one into the other. *Required* content isn't linked; it's co-located.

## Implications for vocabulary design

1. **Every label must name a reader-need.** Test: "A reader who would follow this label is one who [wants to / might / needs to] ___."
2. **Prefer labels that name epistemic or task states** (wants to verify, wants to understand how, wants to execute) over labels that name static document relations (is-a-part-of, cross-references).
3. **Cross-[register](./definitions/register.md) labels name boundary-crossing needs.** (Register: one of three content modes — theoretical, descriptive, prescriptive — determining quality goal, title conventions, and linking rules.) A reader moving from theory to description has a different unmet need (evidence, instance) than one moving from description to theory (rationale). The cross-register vocabulary grows from these boundary-specific needs.
4. **If a label's reader-need is almost-always-already-met** in the target reader class, cut the label. It's a link that doesn't pay off.
5. **Weak catch-alls should be rare.** `see-also` is an explicit "I can't name what this reader needs, but something's here" — useful as an escape hatch, not as a default.

## Open questions

- When should "assume-loaded-under: skill-X" become part of the label grammar? Currently never — too fragile. If skill configurations stabilise, a label like `defined-in (assume-loaded: cp-skill-write)` could flag links agents-with-skill-X should skip. Speculative.
- Is there a reader-need no current label names? Candidate: "wants the version history / prior form" — currently handled by `supersedes` chains only in `kb/reference/adr/`. Possibly worth a dedicated label if historical traversal becomes common.

---

Relevant Notes:

- [Register](./definitions/register.md) — defined-in: the three content modes (theoretical, descriptive, prescriptive) the cross-register vocabulary organises around
- [ADR 019 — collection-owned link vocabulary](../reference/adr/019-collection-owned-link-vocabulary.md) — extends: the architecture that enforces the reader-need discipline per destination
- [ADR 020 — theoretical-default additions (contrasts, mechanism)](../reference/adr/020-theoretical-default-contrasts-mechanism.md) — extends: applies the reader-need test to label proposals
- [Linking theory](./linking-theory.md) — grounds: the decision-cost model this note instantiates
- [Backlinks](./backlinks.md) — mechanism: the inverse-view machinery that makes unidirectional link authoring workable
