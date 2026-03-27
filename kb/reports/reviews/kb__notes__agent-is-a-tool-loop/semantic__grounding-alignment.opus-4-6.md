The note is very short and makes few causal claims. It cites three linked notes. The core claim (agent = tool loop) is explicitly positioned as a definitional choice, not a derived fact, so grounding requirements are lighter than for empirical claims.

---

**Claim: "agent = tool loop" as a technical convention**

Not attributed to any cited source. The note positions this as a stipulative convention: "a simple equivalence works." Stipulative definitions don't require external grounding — they need only to be useful. This is appropriate positioning. ✓

**Claim: "spawning a sub-agent is spawning a sub-loop — and the question of whether frameworks should expose the loop becomes the question of whether they support sub-agents as a first-class operation"**

Cited to [tool-loop-index.md] as context ("the index whose argument this convention grounds") and to [subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks.md] as motivation. The inference chain is: if agent = tool loop, then sub-agent = sub-loop, therefore framework support for sub-agents = framework exposure of loop-spawning. This follows from the convention directly. The citation to [subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks.md] provides motivation for *why* sub-agents are needed (different tool surfaces), not grounding for the equivalence itself. Attribution is correctly scoped. ✓

**Claim: "each agent is one iteration of the select/call/absorb loop"**

Cited to [bounded-context-orchestration-model.md] as "foundation: each agent is one iteration of the select/call/absorb loop." This is the claim most susceptible to scope mismatch — the cited note's description of the orchestration model may not use exactly this framing. INFO — without reading [bounded-context-orchestration-model.md], the claim that each agent is "one iteration" of a select/call/absorb loop seems like an accurate citation given the link semantics "foundation," but if the orchestration model describes the loop at a different level of abstraction (e.g., one *turn* rather than one *invocation*), the attribution could be slightly off. This is worth checking against the source note.

**Vocabulary alignment**

The note uses "capability surface" without citing a source. This term appears to be introduced here as part of the convention, not borrowed from an existing note. No attribution issue — it's defining a component of a new convention. ✓

"Prompt, capability surface, stop condition" as the three components of a tool loop — these are also introduced without citation. Consistent with the note's self-positioning as defining a convention rather than reporting an established fact. ✓

---

No WARNs. One INFO: the citation of [bounded-context-orchestration-model.md] for "each agent is one iteration of select/call/absorb" should be verified against that note's actual framing, as the level of abstraction (iteration = invocation vs. turn) could affect accuracy.
