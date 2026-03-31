The note presents two frameworks: the extraction/synthesis oracle gap (generation is easy, evaluation is hard) and three quality dimensions (fidelity, novelty, validity).

---

**Framework 1: Extraction vs synthesis oracle gap**

Grounding: "Discriminating the valuable from the noise requires judgment that is not substantially cheaper than producing the synthesis in the first place."

- Simplest: extracting an explicit claim from a source. Verification is mechanical comparison. ✓
- Most extreme: synthesizing a novel theory from many unrelated notes. Validation requires deep domain judgment. ✓
- Between: extracting an *implicit* claim (something the source implies but doesn't state). The note addresses this: "At the implicit end, it requires LLM judgment — but that judgment is still simpler than synthesis evaluation." ✓
- Adjacent: **formal domain synthesis** (mathematical theorem proving, code composition). The note explicitly scopes these out: "in formal domains like mathematics or code composition, synthesis verification *can* be cheap — proof checkers and test suites serve as hard oracles." ✓

**Framework 2: Three quality dimensions**

Fidelity (automatable), novelty (partially automatable via similarity search), validity (the hard part).

- The ordering from easy to hard is clean and well-grounded. ✓
- Adjacent: **utility** — is the synthesis not just valid and novel but *useful*? A connection can be real but trivial. INFO — the note focuses on validity as the hard dimension but doesn't address utility as a separate evaluation criterion. A valid, novel connection that nobody would use is still a poor synthesis.

**Pattern across current attempts**

Four examples (tip consolidation, A-MEM, Cognee, /connect) consistently show the pattern: "synthesis works when there's an oracle." Clean inductive support. ✓

No WARN. One INFO on utility as an unaddressed evaluation dimension.
