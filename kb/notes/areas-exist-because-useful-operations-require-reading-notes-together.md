---
description: Areas are defined by operations that require reading notes together — orientation and comparative reading — which need sets that are both small enough for context and related enough to yield results
type: note
tags: []
status: seedling
---

# Areas exist because useful operations require reading notes together

This note is the analytical companion to [WRITING](../instructions/WRITING.md): `WRITING.md` specifies how to assign and maintain areas, while this note explains why area boundaries exist and what makes them effective.

## The operations

Two operations justify areas. Both require loading a set of notes together, and both impose the same structural constraints on that set.

**Orientation** means loading a set of notes to reconstruct the current state of understanding in a topic — what is known, what is in tension, what is open. This is the entry cost of any session that touches a topic. Without a bounded set, an agent must search, read individual notes, and piece together relationships from scratch — spending context on reconstruction rather than productive work.

**Comparative reading** means loading a set of notes together and looking for redundancy, contradiction, tension, complementarity, and merge candidates. This is the maintenance operation that turns a collection of notes into a coherent body of knowledge. Without it, notes accumulate but never integrate.

Concrete outputs of comparative reading:

- **Redundancy** — two notes making the same argument in different words. One should absorb the other.
- **Contradiction** — two notes asserting incompatible claims. Either one is wrong, or they apply in different scopes that should be made explicit.
- **Tension** — two notes that don't contradict but pull in different directions. The tension is often more interesting than either note alone.
- **Complementarity** — notes that are independent arguments for the same conclusion (like the [three output-quality arguments](./type-system-index.md)). Worth linking explicitly.
- **Merge candidates** — notes that are halves of one argument, or overlapping seedlings that haven't differentiated.
- **Missing connections** — notes that should reference each other but don't.
- **Gaps** — a claim that needs support, a category that has no instances, an argument with no counterargument.

The two operations are complementary. Orientation is read-only — it loads the current state. Comparative reading is the write operation — it improves the state that future orientation will load. An area that supports both creates a virtuous cycle: good orientation enables focused comparative reading, which produces a more coherent set, which makes future orientation faster.

## The constraints

Both operations impose the same two constraints on the note set:

**Context is finite.** An agent cannot load all notes simultaneously. Even a small KB of 100 notes at 500 words each is 50,000 words — well beyond what fits in a productive working context where the agent also needs instructions, methodology, and room to reason. The set must be bounded.

**Yield depends on relatedness.** For orientation, unrelated notes add noise — they consume context without contributing to the mental model being reconstructed. For comparative reading, unrelated notes produce null results — two notes with disjoint subjects have nothing to be redundant about, nothing to contradict, nothing to tension against. In both cases, loading unrelated notes wastes context.

Relatedness is a continuum, not a binary. Surprising cross-domain connections exist — a scheduling insight might illuminate a type system design. But the expected yield drops off steeply with decreasing relatedness. Running either operation on the full KB is not just infeasible (context limits) but inefficient (most notes don't contribute). Cross-domain connections are rare enough to justify a different operation ([/connect](./deep-search-is-connection-methodology-applied-to-temporarily-expanded-corpus.md) with corpus expansion) rather than routine loading within a single area.

**Yield also depends on maturity.** Two seedlings are more likely to be redundant than two current notes that have already been through comparative passes. This means comparative reading isn't one-shot — it should be re-run as notes evolve — but the area boundary remains the right unit for scoping each pass.

## Areas are the mechanism

An area defines a set of notes where reading together is expected to be productive — both for orientation and for comparative reading. The area is a bet: "these notes, loaded together, will provide coherent orientation and surface useful redundancies, tensions, and connections at a rate that justifies the context cost."

This grounds several conventions:

**Size limits follow from context limits.** The [split threshold of ~40 notes](../instructions/WRITING.md) isn't arbitrary — it's the approximate point where an area stops fitting in working context alongside the instructions and reasoning space the agent needs. An area that can't be read together can't serve either operation.

**Precision follows from yield.** A precise area isn't just intellectually satisfying — it's operationally necessary. An area of 48 notes where only 15 are related to each other wastes 33 notes' worth of context — noise during orientation, null results during comparative reading. Splitting into more precise areas concentrates the context budget where it's productive.

**Related Areas links are the cross-area operation.** When an agent follows a "Related Areas" link from one index to another, it's expanding the set. This is more expensive (two areas' worth of notes) but sometimes necessary — tensions between areas are real. The link makes this expansion deliberate rather than accidental.

These conventions have further consequences:

**Misplaced notes are actively harmful, not neutral.** A note in the wrong area isn't just poorly categorised — it consumes context in every pass without contributing. During orientation it's noise; during comparative reading it produces no results. Worse than an unassigned note, which at least doesn't waste other notes' context budget.

**Orphaned notes are invisible to both operations.** A note with no area can only be found by search or /connect. It never appears in orientation or comparative reading, which means its relationships with existing notes go undetected. This is why [stale indexes are worse than no indexes](./stale-indexes-are-worse-than-no-indexes.md) — a note that falls out of its area index disappears from maintenance.

**Single-area membership is the default.** If a note belongs to two areas, it gets loaded in both passes, doubling its context cost. Multi-area membership should be justified by the note genuinely participating in both domains' discourse — not by it being "sort of related" to both.

**Area splits are yield optimisations, not taxonomic refinements.** When an area is split, the question isn't "what's the most logical subdivision?" but "which partition maximises expected yield per context-unit?" A conceptually clean split that puts highly related notes on opposite sides is worse than an ugly split that keeps high-tension pairs together.

The area system is a form of probabilistic triage: allocate the expensive read-together operations where they're most likely to produce results, and use cheaper operations (search, /connect) for the long tail of cross-area connections.

## Conventions that follow

**Tag the most precise useful area.** The `areas:` field generates Topics footer links, which lead readers to area indexes for comparative reading. A large area like `kb-design` (48 notes) is too imprecise — too many notes, too low a yield per context-unit. Tag the area whose index concentrates the most relevant notes.

**Don't dual-tag parent and child.** `type-system` is a sub-area of `document-system` — that relationship is real. But `areas: [document-system, type-system]` forces the reader to choose between two indexes without guidance. Tag the most precise area only; the broader area is one hop away via "Related Areas" links. This mirrors the existing pattern — `document-system` notes don't carry `areas: [kb-design]`.

**Multiple areas are fine for independent dimensions.** `areas: [kb-design, computational-model]` is fine — independent dimensions, not parent-child. The test: would comparative reading of each area surface useful tensions with this note?

**Split when an area becomes imprecise.** The [~40 note threshold](../instructions/WRITING.md) reflects context limits, but the deeper signal is precision: if comparative reading consistently yields nothing because most note-pairs are unrelated, the area is too broad regardless of size. Splits produce peer areas linked via "Related Areas."

**areas.md stays flat.** All areas listed as peers. Sub-area relationships expressed in each area's "Related Areas" section, not in the hub.

## Tension: orientation and comparative reading pull index design in opposite directions

Orientation benefits from synthesis — current state in prose, tensions highlighted, gaps noted. An agent reading a synthesised index gets the mental model without loading every note. Comparative reading benefits from a flat loadable list — every note visible, no editorial filtering hiding potential redundancies or tensions.

A synthesised index saves orientation cost but may hide notes from comparative reading. A flat list enables comparative reading but provides no orientation shortcut. Current area indexes try to do both (context phrases on every entry, plus editorial grouping), but the two demands are genuinely in tension.

## Open questions

- Can we measure actual yield per area? If comparative reading of area X consistently produces zero results, the area is either too precise (all notes already integrated) or poorly constructed (notes aren't actually related).
- Should areas have a minimum size? An area of 2 notes doesn't need either operation — the two notes can reference each other directly. The area mechanism adds overhead without value below some threshold.
- How does this interact with the [quality signals](./quality-signals-for-kb-evaluation.md) work? Comparative reading yield could be a quality signal for area construction.

---

Relevant Notes:

- [context efficiency is the central design concern](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — foundation: context is the scarce resource that makes unbounded reading-together infeasible
- [stale indexes are worse than no indexes](./stale-indexes-are-worse-than-no-indexes.md) — consequence: a note missing from its area is invisible to both orientation and comparative reading
- [a knowledge base should support fluid resolution-switching](./a-knowledge-base-should-support-fluid-resolution-switching.md) — areas are one resolution level; both operations work within a level
- [quality signals for KB evaluation](./quality-signals-for-kb-evaluation.md) — extends: comparative reading yield as a potential quality signal
- [deep search is connection methodology applied to temporarily expanded corpus](./deep-search-is-connection-methodology-applied-to-temporarily-expanded-corpus.md) — complements: /connect handles the cross-area connections that within-area operations don't reach

Distilled into:

- [WRITING.md](../instructions/WRITING.md) — area assignment rules, lifecycle split threshold, and areas field description
