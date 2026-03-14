---
description: The library's purpose is to produce notes that can be co-loaded for combinatorial discovery — short atomic notes are a consequence of this goal; longer synthesized artifacts belong in workshops or distilled instructions
type: note
tags: [learning-theory]
status: seedling
---

# Short composable notes maximize combinatorial discovery

The library layer (`kb/notes/`) exists for co-loading. [Discovery](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) — seeing shared structure across particulars — requires co-presence: you can't find that three notes share unnamed structure if only one fits in context. Under [bounded context](./context-efficiency-is-the-central-design-concern-in-agent-systems.md), the number of notes that fit determines the surface area for cross-cutting connections. Short, atomic notes maximize that surface area.

The gain is probabilistic, not mechanical — not every pair yields a discovery. What matters is breadth of *independent* perspectives. Notes from distant domains are more likely to reveal shared structure than additional notes within the same topic. The library should be optimized for this: many small, independently authored claims that can be loaded together in varied combinations.

[Resolution-switching](./a-knowledge-base-should-support-fluid-resolution-switching.md) complements this. Claim titles and descriptions give broad surface-level pairing without loading full bodies; full notes are loaded selectively where depth is needed. Short notes make both modes cheaper.

## The design rule

**One claim, one note.** The title states the claim, the body supports it, the footer connects it. If a note has multiple `##` sections making independent claims, that's a signal to decompose.

**Longer synthesized views belong in workshops or are generated.** Theory overviews, campaign understanding, multi-note summaries — these are *consumers* of library notes, not library notes themselves. They live in `kb/work/` as workshop artifacts with lifecycles, or are generated (like indexes). When the purpose is served, the workshop artifact expires but the library notes remain available for recombination.

## Evidence

The improvement log provides examples. Entries tagged ABSTRACTION and SYNTHESIS are discoveries made by co-loading notes and recognizing shared structure:

- "shared unnamed structure: execution-boundary compression" — found across five notes from different theoretical angles
- "two independent decompositions of agent memory from different traditions that together predict a two-axis taxonomy" — found by co-loading notes grounded in cognitive science alongside notes grounded in computer architecture

The structure emerged from the *juxtaposition* of independent perspectives. A single long note synthesizing all of memory theory would have contained the same information but wouldn't have surfaced the cross-cutting structure — it would have pre-committed to one narrative instead of leaving the connections available for discovery.

## Tension with argument coherence

Some arguments genuinely need space — the reasoning from premises to conclusion loses force when atomized. The [active-campaign note](./active-campaign-understanding-needs-a-single-coherent-narrative-not-composed-notes.md) argues that working understanding during an active campaign needs holistic rewrite, not graph composition.

The resolution: coherent narratives are workshop artifacts, not library artifacts. The library stores premises and conclusions as separate composable notes. The workshop assembles them into narratives for a specific purpose. When the narrative expires, the atomic notes remain.

---

Relevant Notes:

- [context efficiency is the central design concern](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: bounded context makes co-loading capacity the scarce resource
- [discovery is seeing the particular as an instance of the general](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) — grounds: discovery requires co-presence of multiple particulars
- [a good agentic KB maximizes contextual competence](./a-good-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trustworthy-knowledge.md) — extends: composability as one of three properties; short notes compose better
- [a functioning KB needs a workshop layer not just a library](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — enables: workshops are where longer synthesized views live
- [active-campaign understanding needs a single coherent narrative](./active-campaign-understanding-needs-a-single-coherent-narrative-not-composed-notes.md) — tension: some arguments need narrative coherence; resolved by placing narratives in workshops
- [a knowledge base should support fluid resolution-switching](./a-knowledge-base-should-support-fluid-resolution-switching.md) — extends: title-level scanning for breadth, full loading for depth
