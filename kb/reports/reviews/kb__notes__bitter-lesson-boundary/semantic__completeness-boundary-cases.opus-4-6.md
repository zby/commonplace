The note presents one main framework: the arithmetic/vision-feature distinction (spec-is-the-problem vs. spec-approximates-the-problem), with chess as a hybrid example and three confidence signals.

---

**Framework: Arithmetic vs vision feature**

Grounding: "Both are narrow. Both are human-engineered. The difference isn't scope — it's whether the specification fully captures the problem."

- Simplest: multiplication. The spec IS the problem. ✓
- Most extreme: "seeing" — the spec (edge detection, etc.) was a theory, not a definition. ✓
- Between: **chess** — the note explicitly presents this as a boundary case where rules are arithmetic and strategy is vision-feature. "The boundary running through a single system." Excellent boundary handling. ✓
- Between: **NP-hard optimization** — "the objective and constraints are fully specified... but finding good solutions is where learned methods increasingly beat hand-crafted heuristics." This is another clean hybrid: the specification is arithmetic, the solution strategy is vision-feature. ✓
- Adjacent: **natural language processing** — is language understanding arithmetic (grammar has rules) or vision-feature (meaning is approximate)? The note doesn't discuss NLP directly, but the framework would classify grammar rules as arithmetic and semantic understanding as vision-feature. ✓

**Confidence signals table**

Three signals (correctness specifiability, definition vs proxy, local vs compositional failures). Each is presented with both sides. The note hedges: "None of these signals are decisive." ✓

**Composition failure as a tell**

"When individually sound components don't compose into the larger capability, the specs are probably theories, not definitions." This is a clean diagnostic heuristic. ✓

No WARN, no INFO. Exceptionally well-handled boundary cases for a note about boundaries.
