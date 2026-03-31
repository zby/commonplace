The note presents one main framework: a 4×3 table mapping composition modes to failure modes and missing primitives (flat context → contamination, shared memory → inconsistency, output aggregation → amplification, delegation chain → accountability vacuum).

---

**Framework: Composition mode → failure mode → missing primitive**

Grounding definition: "Whenever multiple computations compose into one larger system, ask what coordination guarantee matches that composition mode."

- Simplest instance: a single agent with one context, no composition. No failure mode applies — the framework correctly doesn't activate (it's about *composition*). ✓
- Most extreme: a large system with all four composition modes active simultaneously. Each would need its own guarantee. The framework handles this — the four rows are independent. ✓
- Between: a system that uses shared memory AND output aggregation (e.g., agents write to a shared state and their outputs are also merged). Both inconsistency and amplification could apply. The table implies independent rows, so both guarantees are needed. ✓
- Between: a system where "flat context accumulation" and "shared mutable memory" overlap — a conversation history IS shared mutable state across turns of one agent. The contamination and inconsistency failure modes could both apply. INFO — the table presents flat context and shared memory as separate rows, but in a single-agent multi-turn system, the conversation context is the shared mutable memory. The boundary between rows 1 and 2 is context-dependent.
- Adjacent concept — **ordering/priority conflicts**: when agents disagree about the sequence of operations, not about semantic content. This could be a variant of inconsistency, but the failure mode is temporal (wrong order) rather than semantic (wrong content). INFO — ordering conflicts don't clearly map to any of the four failure modes; they might need a fifth row or could be subsumed under inconsistency with an expanded definition.

**The semantic/governance distinction**

The note explicitly distinguishes three semantic failures (rows 1-3) from one governance failure (row 4). The table presents all four symmetrically in format but the text clarifies they are different in kind. ✓

**WARN — intro channels don't map to table composition modes**

The intro lists five coordination channels: "conversation, prompt refinement, forking, shared memory, synthesis." The table lists four composition modes: flat context accumulation, shared mutable memory, output aggregation, delegation chain. These are presented as different levels of description (channels vs. modes), which is the note's core argument. However, the mapping between channels and modes is not made explicit. Which composition modes does "forking" involve? Which does "conversation" involve? The reader is left to infer. Since the note's thesis is that channels and modes are distinct, an explicit mapping (or an argument for why no clean mapping exists) would strengthen the claim.

One WARN (channel-to-mode mapping not explicit). Two INFOs (flat context / shared memory overlap, ordering conflicts).
