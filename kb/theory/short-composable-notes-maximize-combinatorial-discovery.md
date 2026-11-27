---
description: "Short notes let readers combine claims for new questions. A longer synthesis earns its place when readers need the reasoning as a whole."
type: types/note.md
tags: [learning-theory, discovery, context-engineering, document-system]
---

# Short composable notes maximize combinatorial discovery

The library layer (`kb/theory/`) exists for co-loading. [Recognizing shared structure across particulars](./recognition-not-linking-is-the-hard-problem-in-knowledge-systems.md) requires co-presence: you can't find that three notes share unnamed structure if only one fits in context. Under [bounded context](./context-efficiency-is-the-central-design-concern-in-agent-systems.md), the number of notes that fit determines the surface area for cross-cutting connections. Short, atomic notes maximize that surface area.

The gain is probabilistic, not mechanical — not every pair yields a discovery. What matters is breadth of *independent* perspectives. Notes from distant domains are more likely to reveal shared structure than additional notes within the same topic. The library should be optimized for this: many small, independently authored claims that can be loaded together in varied combinations.

[Resolution-switching](./a-knowledge-base-should-support-fluid-resolution-switching.md) complements this. Claim titles and descriptions give broad surface-level pairing without loading full bodies; full notes are loaded selectively where depth is needed. Short notes make both modes cheaper.

## Prior work

Atomic, composable units are a recurring design principle:

- **Zettelkasten** (Luhmann) — one idea per note, connections between notes. "One claim, one note" is Luhmann's atomicity principle. The most direct ancestor.
- **Modular design** (Parnas, 1972) — modules hide design decisions and expose interfaces. The Unix philosophy ("do one thing well, compose through pipes") is the same principle applied to programs.
- **Faceted classification** (Ranganathan, 1933) — describe items along independent combinable facets rather than a single hierarchy. Composable notes are facets.

What's specific to our context is the bounded-context motivation: atomicity here is driven by a hard token limit that makes co-loading capacity the scarce resource, not by filing convenience or code maintainability.

**TODO:** This survey is from the agent's training data, not systematic. Zettelkasten methodology in particular has extensive practitioner literature on atomicity trade-offs worth ingesting.

## The design rule

**One claim, one note.** The title states the claim, the body supports it, the footer connects it. If a note has multiple `##` sections making independent claims, that's a signal to decompose.

**A temporary synthesis can serve one task.** A campaign summary can bring several notes together for a decision. Once the decision is made, the summary can expire without taking its sources with it.

## Evidence

The improvement log provides examples. Entries tagged ABSTRACTION and SYNTHESIS are discoveries made by co-loading notes and recognizing shared structure:

- "shared unnamed structure: execution-boundary compression" — found across five notes from different theoretical angles
- "two independent decompositions of agent memory from different traditions that together predict a two-axis taxonomy" — found by co-loading notes grounded in cognitive science alongside notes grounded in computer architecture

The structure emerged from the *juxtaposition* of independent perspectives. A single long note synthesizing all of memory theory would have contained the same information but wouldn't have surfaced the cross-cutting structure — it would have pre-committed to one narrative instead of leaving the connections available for discovery.

## Tension with argument coherence

Some arguments genuinely need space: the reasoning from premises to conclusion loses force when split apart. When readers cannot reconcile the pieces within their available context, a [compact account kept current](./evolving-understanding-needs-holistic-rewrite-not-composition.md) lets them use the argument as a whole.

Length does not decide where a synthesis belongs. A briefing assembled for one decision is [temporary work](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md). An explanation worth maintaining for future readers can be a lasting reference, even when its argument takes several pages.

---

Relevant Notes:

- [context efficiency is the central design concern](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: bounded context makes co-loading capacity the scarce resource
- [recognition, not linking, is the hard problem in knowledge systems](./recognition-not-linking-is-the-hard-problem-in-knowledge-systems.md) — grounds: recognition is the expensive step, and it requires co-presence of multiple particulars
- [agent memory needs discoverable, composable, trusted knowledge under bounded context](./agent-memory-needs-discoverable-composable-trusted-knowledge-under.md) — extends: composability as one of three memory properties; short notes compose better
- [A compact, refreshable whole-picture narrative can replace infeasible fragment reconciliation](./evolving-understanding-needs-holistic-rewrite-not-composition.md) — tension: when readers need a coherent whole, separate notes can make each reader repeat the same reconciliation work.
- [a knowledge base should support fluid resolution-switching](./a-knowledge-base-should-support-fluid-resolution-switching.md) — extends: title-level scanning for breadth, full loading for depth
- [A note is an atomic step relative to the check that reads it](./a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md) — contrasts: a second, independent size bound — one checkable inference sized to the checker's pass — that a single-claim note over many sources can fail
