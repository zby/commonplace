# Grounding Alignment

**Note:** `kb/notes/agent-statelessness-means-the-context-engine-should-inject-context-automatically.md`

## Claims checked

### 1. Statelessness grounds the need for injection (line 11)

**Claim:** "Since agents are stateless, they can't carry definitions, decisions, or vocabulary between reads."

**Source:** [agent-statelessness-makes-routing-architectural-not-learned.md](../../notes/agent-statelessness-makes-routing-architectural-not-learned.md)

The linked note establishes: "Each session starts cold. It cannot learn 'last time I needed the structured-claim template, I found it in notes/types/.'" The statelessness premise is directly supported. PASS.

### 2. "Extends document affordances" from operations to retrieval (line 13)

**Claim:** "This extends document affordances from 'what operations can I perform on this document' to 'what context gets loaded alongside this document.'"

**Source:** [document-types-should-be-verifiable.md](../../notes/document-types-should-be-verifiable.md)

The linked note describes types as telling agents "what it can do with the document" — structural verification, navigation hints, processor guidance. Its concept of "affordances" is about operations (implement from a spec, navigate an index, verify a structured-claim). The reviewed note extends this to *retrieval profiles* — what gets loaded alongside the document. The linked note doesn't discuss retrieval or loading as an affordance.

The extension relationship is explicitly signaled ("extends...from...to"), so this is framing a contribution, not misquoting. But "document affordances" in the source note has a narrower meaning (structural/operational) than the reviewed note implies when invoking the term. **INFO — the term "document affordances" is stretched from operational properties (source note) to include retrieval profiles (this note). The extension is legitimate but readers following the link may find a narrower concept than expected.**

### 3. Static hierarchy extended with dynamic layer (lines 54-56)

**Claim:** The instruction-specificity note "currently describes a static hierarchy" that this note extends with an "on reference" layer.

**Source:** [instruction-specificity-should-match-loading-frequency.md](../../notes/instruction-specificity-should-match-loading-frequency.md)

The linked note describes four levels: CLAUDE.md (always), skill descriptions (always), skill bodies (on demand/invoke), task-specific docs (on demand). All triggers are predetermined by position in the hierarchy. The characterization as "static" is accurate — nothing in that hierarchy reacts to what the agent is currently reading. The "on reference" extension is a genuine addition. PASS.

### 4. "Cannot fill gaps" row motivates injection (line 82)

**Claim:** "The 'cannot fill gaps' row in the dual-audience table is exactly the problem context injection addresses."

**Source:** [human-llm-differences-are-load-bearing-for-knowledge-system-design.md](../../notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md)

The linked note's table includes: "Completeness | Can fill gaps from background knowledge and experience | Cannot fill gaps — if it's not in the loaded context, it doesn't exist." The reviewed note claims injection addresses this gap. The linked note itself confirms the connection: "context injection — the context engine automatically providing referenced context (definitions, ADRs) that a human reader would carry from prior sessions but an LLM agent cannot" (line 44). Bidirectional confirmation. PASS.

### 5. "Two always-loaded surfaces" link annotation (line 81)

**Claim (link text):** "extends: the two always-loaded surfaces (CLAUDE.md vs skill descriptions) are both candidates for automatic injection."

**Source:** [always-loaded-context-mechanisms-in-agent-harnesses.md](../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md)

The linked note identifies four always-loaded mechanisms (system prompt files, capability descriptions, memory, configuration injection), not two. The reviewed note's annotation says "the two always-loaded surfaces" — this is a simplification that matches the instruction-specificity note's framing (which discusses CLAUDE.md and skill descriptions as the two main surfaces) rather than the linked note's four-surface taxonomy.

Additionally, "are both candidates for automatic injection" is ambiguous — it could mean these surfaces *receive* injected content or *drive* injection decisions. Since CLAUDE.md and skill descriptions are already always-loaded, "injecting" into them doesn't make obvious sense. The more likely reading is that these surfaces could contain routing rules that *trigger* injection. But the link text doesn't clarify this. **INFO — the annotation reduces four surfaces to two and the phrase "candidates for automatic injection" is ambiguous about whether these surfaces receive or drive injection.**

### 6. Parallel with typed callables (line 78)

**Claim (link text):** "parallel: that note gives skills type signatures; this note gives documents retrieval profiles."

**Source:** [instructions-are-typed-callables.md](../../notes/instructions-are-typed-callables.md)

The linked note describes skills as typed callables that accept document types as input and produce types as output. The reviewed note claims a parallel: skills have type signatures, documents have retrieval profiles. The parallel is reasonable — both extend the type system in different directions (operations for skills, loading behavior for documents). The linked note doesn't mention retrieval profiles, but the "parallel" relationship correctly signals independent extension, not grounding. PASS.

### 7. Title-as-claim exception for definitions (line 83)

**Claim:** "definitional notes are an identified exception to claim titles; the `definition` type would formalize this."

**Source:** [title-as-claim-enables-traversal-as-reasoning.md](../../notes/title-as-claim-enables-traversal-as-reasoning.md)

The linked note argues notes should be titled as claims, not topics. Definitions are inherently topical ("codification", "constraining") — they name a term, not a claim. The reviewed note correctly identifies this as an exception and proposes the `definition` type to formalize it. The linked note doesn't explicitly discuss this exception, but the logic follows from its own principles. PASS — the inference is valid even though the source doesn't state it.

## Summary

No WARNs. Two INFOs:

1. **INFO:** "Document affordances" is used more broadly (operational + retrieval) than the source note's narrower meaning (operational/structural only).
2. **INFO:** The link annotation for the always-loaded-context note reduces four surfaces to two and uses ambiguous phrasing about what "candidates for automatic injection" means.
