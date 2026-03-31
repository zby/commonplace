The note presents three frameworks: the statelessness thesis (routing is permanent architecture), a five-layer progressive disclosure hierarchy, and a degradation cliff model (binary vs. continuum). Three design consequences follow.

---

**Framework 1: Statelessness thesis**

Grounding: "Each session starts cold. It cannot learn 'last time I needed the structured-claim template, I found it in notes/types/.'"

- Simplest: an agent with one note and one routing pointer. The routing pointer is still architecture — the agent won't discover the note without it. ✓
- Most extreme: a massive KB with thousands of notes. Routing becomes essential and scaling the routing infrastructure is a real challenge. ✓
- Between: an agent with persistent memory across sessions (e.g., Claude's auto-memory). The note addresses this: "Persistent memory across sessions would relax the statelessness assumption, but routing scales with the knowledge base itself." INFO — the note treats persistent memory as a relaxation of statelessness, but current implementations offer partial memory (remembering some things, not everything). The binary framing (stateless → architectural) doesn't address the middle ground where the agent remembers some routing knowledge but not all. The note's hedge about routing scaling with KB size partially covers this.

**Framework 2: Five-layer progressive disclosure hierarchy**

1. CLAUDE.md (unconditional), 2. Skill descriptions (cheap), 3. Skill bodies (on activation), 4. Type templates (per directory), 5. Methodology notes (on demand).

- Simplest: an agent that only loads CLAUDE.md. ✓
- Most extreme: an agent traversing all five layers for an edge case. ✓
- Between: what about content that should be loaded between layers 2 and 3 — e.g., instructions that aren't skills but also aren't just descriptions? The hierarchy has a clean five-level structure but real content may not map neatly. INFO — the hierarchy is presented as a concrete system but some content types (e.g., non-skill instructions, ADR pointers) may fall between layers without a clear home.

**Framework 3: Degradation cliff**

"The human system degrades along a continuum: expert → competent → novice → uncertain. The agent system has a cliff: KB-augmented → generic."

- Simplest: agent missing one routing entry — it falls to generic for that one task. ✓
- Most extreme: agent with no loaded context — fully generic. ✓
- Between: an agent whose training data substantially overlaps with the KB's methodology. The cliff model says it falls to "a different system — a generic LLM" but if the LLM's training included similar methodology, the fall is softer. INFO — the cliff model assumes training has "no relationship to the KB's methodology," which may overstate the gap for well-trained models in familiar domains.

No WARN. Three INFOs: partial memory, content between hierarchy layers, and training/methodology overlap softening the cliff.
